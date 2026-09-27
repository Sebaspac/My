"""Markdown -> DOCX (pandoc + Formatierung per python-docx). Aufruf: python3 mkdocx.py in.md out.docx "Titel" "Untertitel" """
import sys, subprocess, pypandoc, os
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
TEAL=RGBColor(0x1F,0x6F,0x78); NAVY=RGBColor(0x17,0x32,0x4D); GREY=RGBColor(0x5F,0x6B,0x73)
here=os.path.dirname(os.path.abspath(__file__)); ref=os.path.join(here,"reference.docx")
def make_ref():
    subprocess.run([pypandoc.get_pandoc_path(),"-o",ref,"--print-default-data-file","reference.docx"],check=True)
    d=Document(ref)
    st=d.styles
    for name in ["Normal","Body Text","First Paragraph","Compact"]:
        if name in [s.name for s in st]:
            s=st[name]; s.font.name="Calibri"; s.font.size=Pt(10.5)
            s.element.rPr.rFonts.set(qn('w:eastAsia'),"Calibri")
    for lvl,size,col in [(1,18,NAVY),(2,14,TEAL),(3,12,TEAL),(4,11,NAVY)]:
        s=st[f"Heading {lvl}"]; s.font.name="Calibri"; s.font.size=Pt(size); s.font.color.rgb=col; s.font.bold=True
    for name,size,col in [("Title",26,NAVY),("Subtitle",14,GREY)]:
        s=st[name]; s.font.name="Calibri"; s.font.size=Pt(size); s.font.color.rgb=col
    for sec in d.sections:
        sec.left_margin=sec.right_margin=Cm(2.0); sec.top_margin=Cm(2.0); sec.bottom_margin=Cm(1.8)
    d.save(ref)
def shade(cell,hexcol):
    tcPr=cell._tc.get_or_add_tcPr()
    for old in tcPr.findall(qn('w:shd')): tcPr.remove(old)
    sh=OxmlElement('w:shd'); sh.set(qn('w:val'),'clear'); sh.set(qn('w:color'),'auto'); sh.set(qn('w:fill'),hexcol)
    after=[qn('w:'+t) for t in ['noWrap','tcMar','textDirection','tcFitText','vAlign','hideMark']]
    for i,ch in enumerate(list(tcPr)):
        if ch.tag in after: tcPr.insert(i,sh); return
    tcPr.append(sh)
def borders(tbl):
    tblPr=tbl._tbl.tblPr; b=OxmlElement('w:tblBorders')
    for e in ['top','left','bottom','right','insideH','insideV']:
        el=OxmlElement(f'w:{e}'); el.set(qn('w:val'),'single'); el.set(qn('w:sz'),'4'); el.set(qn('w:space'),'0'); el.set(qn('w:color'),'BFC6CC'); b.append(el)
    for old in tblPr.findall(qn('w:tblBorders')): tblPr.remove(old)
    after=[qn('w:'+t) for t in ['shd','tblLayout','tblCellMar','tblLook','tblCaption','tblDescription']]
    for i,ch in enumerate(list(tblPr)):
        if ch.tag in after: tblPr.insert(i,b); return
    tblPr.append(b)
def post(path,title,subtitle):
    d=Document(path)
    for t in d.tables:
        borders(t)
        for ri,row in enumerate(t.rows):
            for c in row.cells:
                for p in c.paragraphs:
                    p.paragraph_format.space_after=Pt(1); p.paragraph_format.space_before=Pt(1)
                    for r in p.runs:
                        r.font.size=Pt(8.5)
                        if ri==0: r.font.bold=True; r.font.color.rgb=RGBColor(0xFF,0xFF,0xFF)
                if ri==0: shade(c,"17324D")
                elif ri%2==0: shade(c,"F2F4F5")
    # Kopf-/Fußzeile
    for sec in d.sections:
        sec.orientation=sec.orientation
        hp=sec.header.paragraphs[0]; hp.text=f"{title}  ·  MDIS Consulting"; hp.runs[0].font.size=Pt(8); hp.runs[0].font.color.rgb=GREY
        fp=sec.footer.paragraphs[0]; fp.alignment=WD_ALIGN_PARAGRAPH.CENTER
        r=fp.add_run("Seite "); r.font.size=Pt(8)
        for code in ["PAGE"]:
            f1=OxmlElement('w:fldSimple'); f1.set(qn('w:instr'),code); rr=OxmlElement('w:r'); t=OxmlElement('w:t'); t.text="1"; rr.append(t); f1.append(rr); fp._p.append(f1)
    d.save(path)
if __name__=="__main__":
    src,out,title,subtitle=sys.argv[1:5]
    if not os.path.exists(ref): make_ref()
    md=open(src,encoding="utf-8").read()
    meta=f"---\ntitle: \"{title}\"\nsubtitle: \"{subtitle}\"\nlang: de-DE\n---\n\n"
    extra=["--reference-doc",ref,"--toc","--toc-depth=2","-M","toc-title=Inhalt"] if "--notoc" not in sys.argv else ["--reference-doc",ref]
    pypandoc.convert_text(meta+md,"docx",format="markdown+pipe_tables+grid_tables+raw_attribute",outputfile=out,extra_args=extra)
    post(out,title,subtitle); print("ok",out)
