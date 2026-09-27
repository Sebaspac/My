"""Kleine Hilfsbibliothek zum Erzeugen mehrseitiger draw.io-Dateien (unkomprimiertes XML).
Verwendung:
    from dio import Doc
    d = Doc(); p = d.page("01 Systemlandschaft")
    a = p.box(40, 80, 200, 60, "d.velop documents", "dvelop")
    b = p.box(400, 80, 200, 60, "DATEV", "ext")
    p.edge(a, b, "ER-Journal", "flow")
    d.save("out.drawio")
Koordinaten absolut in px. Seitenformat Standard A3 quer (1654 x 1169).
"""
from xml.sax.saxutils import escape, quoteattr
import itertools, re

# ---- Farbwelt (MDIS/d.velop-neutral) ----
C = dict(
    teal="#1F6F78", teal_l="#D6ECEE", green="#8DC63F", green_l="#EAF5DC", navy="#17324D",
    grey="#5F6B73", grey_l="#F2F4F5", grey_m="#D9DEE2", orange="#E8912D", orange_l="#FCEBD6",
    red="#C0392B", red_l="#F8DAD6", purple="#6C4E9C", purple_l="#E7E0F2", yellow_l="#FFF5CC",
    blue="#2E75B6", blue_l="#DCEAF7", white="#FFFFFF", black="#1B1B1B")

BASE = "whiteSpace=wrap;html=1;fontFamily=Helvetica;fontSize=12;"
S = {
    # Systeme / Bausteine
    "dvelop":   f"rounded=1;arcSize=8;fillColor={C['teal']};strokeColor={C['teal']};fontColor=#FFFFFF;fontStyle=1;",
    "dvelop_l": f"rounded=1;arcSize=8;fillColor={C['teal_l']};strokeColor={C['teal']};fontColor={C['navy']};",
    "ext":      f"rounded=1;arcSize=8;fillColor={C['grey_l']};strokeColor={C['grey']};fontColor={C['navy']};fontStyle=1;",
    "mdis":     f"rounded=1;arcSize=8;fillColor={C['green_l']};strokeColor={C['green']};fontColor={C['navy']};fontStyle=1;",
    "partner":  f"rounded=1;arcSize=8;fillColor={C['orange_l']};strokeColor={C['orange']};fontColor={C['navy']};fontStyle=1;",
    "open":     f"rounded=1;arcSize=8;fillColor={C['red_l']};strokeColor={C['red']};fontColor={C['navy']};dashed=1;",
    "group":    f"rounded=1;arcSize=3;fillColor=none;strokeColor={C['grey']};dashed=1;verticalAlign=top;align=left;spacingLeft=8;spacingTop=4;fontStyle=1;fontColor={C['grey']};",
    "group_t":  f"rounded=1;arcSize=3;fillColor={C['teal_l']};strokeColor={C['teal']};opacity=60;verticalAlign=top;align=left;spacingLeft=8;spacingTop=4;fontStyle=1;fontColor={C['navy']};fontSize=14;",
    "group_g":  f"rounded=1;arcSize=3;fillColor={C['grey_l']};strokeColor={C['grey']};verticalAlign=top;align=left;spacingLeft=8;spacingTop=4;fontStyle=1;fontColor={C['navy']};fontSize=14;",
    # Prozess (BPMN-nah)
    "task":     f"rounded=1;arcSize=12;fillColor=#FFFFFF;strokeColor={C['teal']};fontColor={C['black']};",
    "task_d":   f"rounded=1;arcSize=12;fillColor={C['teal_l']};strokeColor={C['teal']};fontColor={C['black']};",
    "task_ext": f"rounded=1;arcSize=12;fillColor={C['grey_l']};strokeColor={C['grey']};fontColor={C['black']};",
    "task_mdis":f"rounded=1;arcSize=12;fillColor={C['green_l']};strokeColor={C['green']};fontColor={C['black']};",
    "task_open":f"rounded=1;arcSize=12;fillColor={C['red_l']};strokeColor={C['red']};dashed=1;fontColor={C['black']};",
    "auto":     f"rounded=1;arcSize=12;fillColor={C['blue_l']};strokeColor={C['blue']};fontColor={C['black']};",
    "gateway":  f"rhombus;fillColor={C['yellow_l']};strokeColor={C['orange']};fontColor={C['black']};fontSize=11;",
    "start":    f"ellipse;fillColor={C['green_l']};strokeColor={C['green']};strokeWidth=2;fontSize=10;",
    "end":      f"ellipse;fillColor={C['red_l']};strokeColor={C['red']};strokeWidth=3;fontSize=10;",
    "inter":    f"ellipse;shape=doubleEllipse;fillColor=#FFFFFF;strokeColor={C['orange']};fontSize=10;",
    "doc":      f"shape=document;boundedLbl=1;size=0.15;fillColor=#FFFFFF;strokeColor={C['grey']};fontSize=11;",
    "db":       f"shape=cylinder3;boundedLbl=1;size=10;fillColor={C['grey_l']};strokeColor={C['grey']};fontSize=11;",
    "lane_h":   f"fillColor={C['navy']};strokeColor={C['navy']};fontColor=#FFFFFF;fontStyle=1;horizontal=0;",
    "lane":     f"fillColor=#FFFFFF;strokeColor={C['grey_m']};",
    "lane_alt": f"fillColor={C['grey_l']};strokeColor={C['grey_m']};",
    # Text / Hinweise
    "title":    f"text;fontSize=24;fontStyle=1;fontColor={C['navy']};align=left;verticalAlign=middle;",
    "subtitle": f"text;fontSize=13;fontColor={C['grey']};align=left;verticalAlign=top;",
    "h2":       f"text;fontSize=15;fontStyle=1;fontColor={C['teal']};align=left;verticalAlign=middle;",
    "text":     f"text;fontSize=12;align=left;verticalAlign=top;spacing=4;",
    "textc":    f"text;fontSize=12;align=center;verticalAlign=middle;",
    "small":    f"text;fontSize=10;fontColor={C['grey']};align=left;verticalAlign=top;",
    "note":     f"shape=note;size=14;fillColor={C['yellow_l']};strokeColor={C['orange']};align=left;verticalAlign=top;spacing=6;fontSize=11;",
    "warn":     f"rounded=1;arcSize=6;fillColor={C['red_l']};strokeColor={C['red']};align=left;verticalAlign=top;spacing=6;fontSize=11;",
    "info":     f"rounded=1;arcSize=6;fillColor={C['blue_l']};strokeColor={C['blue']};align=left;verticalAlign=top;spacing=6;fontSize=11;",
    "badge":    f"rounded=1;arcSize=50;fillColor={C['navy']};strokeColor=none;fontColor=#FFFFFF;fontSize=10;fontStyle=1;",
    "badge_g":  f"rounded=1;arcSize=50;fillColor={C['green']};strokeColor=none;fontColor=#FFFFFF;fontSize=10;fontStyle=1;",
    "badge_o":  f"rounded=1;arcSize=50;fillColor={C['orange']};strokeColor=none;fontColor=#FFFFFF;fontSize=10;fontStyle=1;",
    "badge_r":  f"rounded=1;arcSize=50;fillColor={C['red']};strokeColor=none;fontColor=#FFFFFF;fontSize=10;fontStyle=1;",
    # Tabellen
    "th":       f"fillColor={C['navy']};strokeColor={C['grey_m']};fontColor=#FFFFFF;fontStyle=1;fontSize=11;align=left;spacingLeft=4;",
    "td":       f"fillColor=#FFFFFF;strokeColor={C['grey_m']};fontSize=11;align=left;spacingLeft=4;verticalAlign=middle;",
    "td_alt":   f"fillColor={C['grey_l']};strokeColor={C['grey_m']};fontSize=11;align=left;spacingLeft=4;verticalAlign=middle;",
    "td_c":     f"fillColor=#FFFFFF;strokeColor={C['grey_m']};fontSize=11;align=center;",
    # UI-Mockups (Masken)
    "ui_win":   f"rounded=0;fillColor=#FFFFFF;strokeColor={C['grey']};shadow=1;",
    "ui_bar":   f"rounded=0;fillColor={C['navy']};strokeColor={C['navy']};fontColor=#FFFFFF;align=left;spacingLeft=10;fontStyle=1;",
    "ui_nav":   f"rounded=0;fillColor={C['grey_l']};strokeColor={C['grey_m']};align=left;verticalAlign=top;spacingLeft=8;spacingTop=6;fontSize=11;",
    "ui_sec":   f"text;fontSize=12;fontStyle=1;fontColor={C['teal']};align=left;verticalAlign=bottom;",
    "ui_label": f"text;fontSize=10;fontColor={C['grey']};align=left;verticalAlign=bottom;spacingBottom=1;",
    "ui_input": f"rounded=1;arcSize=4;fillColor=#FFFFFF;strokeColor={C['grey_m']};align=left;spacingLeft=6;fontSize=11;",
    "ui_req":   f"rounded=1;arcSize=4;fillColor=#FFFFFF;strokeColor={C['teal']};strokeWidth=2;align=left;spacingLeft=6;fontSize=11;",
    "ui_ro":    f"rounded=1;arcSize=4;fillColor={C['grey_l']};strokeColor={C['grey_m']};align=left;spacingLeft=6;fontSize=11;fontColor={C['grey']};",
    "ui_ai":    f"rounded=1;arcSize=4;fillColor={C['blue_l']};strokeColor={C['blue']};align=left;spacingLeft=6;fontSize=11;",
    "ui_btn":   f"rounded=1;arcSize=20;fillColor={C['teal']};strokeColor={C['teal']};fontColor=#FFFFFF;fontStyle=1;fontSize=11;",
    "ui_btn2":  f"rounded=1;arcSize=20;fillColor=#FFFFFF;strokeColor={C['teal']};fontColor={C['teal']};fontStyle=1;fontSize=11;",
    "ui_btn_r": f"rounded=1;arcSize=20;fillColor=#FFFFFF;strokeColor={C['red']};fontColor={C['red']};fontStyle=1;fontSize=11;",
    "ui_tab":   f"rounded=0;fillColor={C['grey_l']};strokeColor={C['grey_m']};fontSize=11;",
    "ui_tab_a": f"rounded=0;fillColor=#FFFFFF;strokeColor={C['teal']};fontSize=11;fontStyle=1;fontColor={C['teal']};",
    "ui_viewer":f"rounded=0;fillColor={C['grey_l']};strokeColor={C['grey_m']};fontColor={C['grey']};fontSize=12;",
    "ui_widget":f"rounded=1;arcSize=4;fillColor=#FFFFFF;strokeColor={C['grey_m']};verticalAlign=top;align=left;spacingLeft=8;spacingTop=6;fontSize=11;shadow=1;",
    "ui_kpi":   f"rounded=1;arcSize=6;fillColor={C['teal_l']};strokeColor={C['teal']};fontSize=11;",
    "ui_chk":   f"rounded=0;fillColor=#FFFFFF;strokeColor={C['grey']};fontSize=10;",
    "ui_hint":  f"rounded=1;arcSize=6;fillColor={C['yellow_l']};strokeColor={C['orange']};fontSize=10;align=left;spacingLeft=6;",
    "ui_err":   f"rounded=1;arcSize=6;fillColor={C['red_l']};strokeColor={C['red']};fontSize=10;align=left;spacingLeft=6;",
    "ui_ok":    f"rounded=1;arcSize=6;fillColor={C['green_l']};strokeColor={C['green']};fontSize=10;align=left;spacingLeft=6;",
    "ui_callout":f"shape=callout;perimeter=calloutPerimeter;position2=0.1;size=12;base=14;fillColor={C['orange_l']};strokeColor={C['orange']};fontSize=10;align=left;spacingLeft=4;",
    "ann":      f"ellipse;fillColor={C['orange']};strokeColor=none;fontColor=#FFFFFF;fontStyle=1;fontSize=11;",
}
E = {
    "flow":  f"edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;html=1;endArrow=block;endFill=1;strokeColor={C['navy']};fontSize=10;",
    "data":  f"edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=open;endFill=0;dashed=1;strokeColor={C['teal']};fontSize=10;fontColor={C['teal']};",
    "data2": f"edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=open;startArrow=open;dashed=1;strokeColor={C['teal']};fontSize=10;fontColor={C['teal']};",
    "msg":   f"edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=open;endFill=0;startArrow=oval;startFill=0;dashed=1;strokeColor={C['grey']};fontSize=10;",
    "straight": f"html=1;endArrow=block;endFill=1;strokeColor={C['navy']};fontSize=10;",
    "line":  f"html=1;endArrow=none;strokeColor={C['grey']};",
    "assoc": f"html=1;endArrow=none;dashed=1;strokeColor={C['grey']};fontSize=10;",
    "tree":  f"edgeStyle=elbowEdgeStyle;elbow=vertical;html=1;endArrow=block;endFill=1;strokeColor={C['grey']};rounded=0;",
    "treeh": f"edgeStyle=elbowEdgeStyle;elbow=horizontal;html=1;endArrow=block;endFill=1;strokeColor={C['grey']};rounded=0;",
    "red":   f"edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor={C['red']};fontColor={C['red']};fontSize=10;",
    "green": f"edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeColor={C['green']};fontColor={C['navy']};fontSize=10;",
}

_ids = itertools.count(1)

def _v(text):
    """Text -> draw.io-Label (HTML). Zeilenumbruch \n -> <br>. **fett** -> <b>."""
    if text is None: return ""
    t = escape(str(text))
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"__(.+?)__", r"<i>\1</i>", t)
    return t.replace("\n", "<br>")

class Page:
    def __init__(self, doc, name, pid, w=1654, h=1169):
        self.doc, self.name, self.id, self.w, self.h = doc, name, pid, w, h
        self.cells = []
    def _add(self, xml): self.cells.append(xml)
    def box(self, x, y, w, h, text="", style="task", extra="", link=None, tooltip=None, raw=False):
        cid = f"{self.id}-{next(_ids)}"
        st = BASE + (S.get(style, style)) + extra
        val = text if raw else _v(text)
        geo = f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/>'
        if link or tooltip:
            attrs = f' label={quoteattr(val)}'
            if link: attrs += f' link={quoteattr(link)}'
            if tooltip: attrs += f' tooltip={quoteattr(tooltip)}'
            self._add(f'<UserObject id="{cid}"{attrs}><mxCell style={quoteattr(st)} vertex="1" parent="1">{geo}</mxCell></UserObject>')
        else:
            self._add(f'<mxCell id="{cid}" value={quoteattr(val)} style={quoteattr(st)} vertex="1" parent="1">{geo}</mxCell>')
        return cid
    def text(self, x, y, w, h, text, style="text", extra=""):
        return self.box(x, y, w, h, text, style, extra)
    def edge(self, src, tgt, label="", style="flow", extra="", points=None, exit=None, entry=None):
        cid = f"{self.id}-{next(_ids)}"
        st = E.get(style, style) + extra
        if exit: st += f"exitX={exit[0]};exitY={exit[1]};exitDx=0;exitDy=0;"
        if entry: st += f"entryX={entry[0]};entryY={entry[1]};entryDx=0;entryDy=0;"
        pts = ""
        if points:
            pts = "<Array as=\"points\">" + "".join(f'<mxPoint x="{px}" y="{py}"/>' for px, py in points) + "</Array>"
        self._add(f'<mxCell id="{cid}" value={quoteattr(_v(label))} style={quoteattr(st)} edge="1" parent="1" source="{src}" target="{tgt}"><mxGeometry relative="1" as="geometry">{pts}</mxGeometry></mxCell>')
        return cid
    def line(self, x1, y1, x2, y2, style="line", label="", extra=""):
        cid = f"{self.id}-{next(_ids)}"
        st = E.get(style, style) + extra
        self._add(f'<mxCell id="{cid}" value={quoteattr(_v(label))} style={quoteattr(st)} edge="1" parent="1"><mxGeometry relative="1" as="geometry"><mxPoint x="{x1}" y="{y1}" as="sourcePoint"/><mxPoint x="{x2}" y="{y2}" as="targetPoint"/></mxGeometry></mxCell>')
        return cid
    def header(self, title, subtitle="", nr=None):
        """Seitenkopf mit Titel, Untertitel, Fußzeile und Link zurück zur Übersicht."""
        self.box(0, 0, self.w, 8, "", "rounded=0;fillColor=%s;strokeColor=none;" % C['teal'])
        self.box(40, 24, self.w - 380, 40, title, "title")
        if subtitle: self.box(40, 64, self.w - 380, 40, subtitle, "subtitle")
        self.box(self.w - 320, 28, 280, 30, "◀ zur Übersicht (Seite 00)", "ui_btn2", link="data:page/id,p00")
        self.box(40, self.h - 34, self.w - 80, 22,
                 f"Livos · DMS-Gesamtkonzept d.velop · {self.name} · MDIS Consulting · Stand 26.09.2026 · Entwurf zur Abstimmung",
                 "small", extra="align=center;")
    def table(self, x, y, colw, rows, rowh=26, header=True, styles=None, hmap=None):
        """rows: Liste von Zeilen (Liste von Strings). colw: Spaltenbreiten. hmap: {row_index: height}."""
        cy = y
        for ri, row in enumerate(rows):
            rh = (hmap or {}).get(ri, rowh)
            cx = x
            for ci, cell in enumerate(row):
                if header and ri == 0: st = "th"
                else: st = (styles or {}).get((ri, ci)) or ("td_alt" if ri % 2 == 0 else "td")
                self.box(cx, cy, colw[ci], rh, cell, st)
                cx += colw[ci]
            cy += rh
        return cy
    def legend(self, x, y, items, title="Legende"):
        self.box(x, y, 220, 22, title, "h2")
        cy = y + 26
        for style, label in items:
            self.box(x, cy, 26, 18, "", style)
            self.box(x + 32, cy - 2, 190, 22, label, "text", extra="verticalAlign=middle;")
            cy += 26
        return cy
    def xml(self):
        body = "".join(self.cells)
        return (f'<diagram id="{self.id}" name={quoteattr(self.name)}>'
                f'<mxGraphModel dx="1400" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{self.w}" pageHeight="{self.h}" background="#FFFFFF" math="0" shadow="0">'
                f'<root><mxCell id="0"/><mxCell id="1" parent="0"/>{body}</root></mxGraphModel></diagram>')

class Doc:
    def __init__(self): self.pages = []
    def page(self, name, pid=None, w=1654, h=1169):
        p = Page(self, name, pid or f"p{len(self.pages):02d}", w, h)
        self.pages.append(p); return p
    def xml(self):
        return ('<mxfile host="app.diagrams.net" agent="MDIS Konzeptgenerator" version="24.7.0" type="device">'
                + "".join(p.xml() for p in self.pages) + "</mxfile>")
    def save(self, path):
        open(path, "w", encoding="utf-8").write(self.xml())


# ======================================================================
# Höhere Bausteine (für alle Seiten verwenden, damit das Bild einheitlich bleibt)
# ======================================================================

def lanes(p, x, y, w, specs, head_w=150, gap=0):
    """Swimlane-Block. specs = [(titel, hoehe), ...]. Gibt dict {titel: (y_top, y_mitte, hoehe)} zurück.
    Zeichnet Kopf (links, dunkel) und Bahn (abwechselnd weiß/grau)."""
    out, cy = {}, y
    for i, (title, h) in enumerate(specs):
        p.box(x, cy, head_w, h, title, "lane_h")
        p.box(x + head_w, cy, w - head_w, h, "", "lane" if i % 2 == 0 else "lane_alt")
        out[title] = (cy, cy + h / 2, h)
        cy += h + gap
    return out

def ui_window(p, x, y, w, h, title, crumbs="", nav_items=None, nav_w=170, user="Maria L. (Rechnungseingang)"):
    """Browserfenster im d.velop-Look. Gibt (cx, cy, cw, ch) = nutzbarer Inhaltsbereich zurück."""
    p.box(x, y, w, h, "", "ui_win")
    p.box(x, y, w, 34, f"d.velop  |  {title}", "ui_bar")
    p.box(x + w - 260, y + 6, 250, 22, f"🔍 Suchen …        👤 {user}", "text", extra="fontColor=#FFFFFF;fontSize=10;align=right;verticalAlign=middle;")
    top = y + 34
    if crumbs:
        p.box(x, top, w, 24, crumbs, "text", extra=f"fontSize=10;fontColor={C['grey']};spacingLeft=10;verticalAlign=middle;fillColor={C['grey_l']};")
        top += 24
    if nav_items:
        p.box(x, top, nav_w, y + h - top, "\n".join(nav_items), "ui_nav")
        return (x + nav_w + 12, top + 10, w - nav_w - 24, y + h - top - 20)
    return (x + 12, top + 10, w - 24, y + h - top - 20)

def ui_field(p, x, y, w, label, value="", kind="input", h=24, hint=None):
    """Beschriftetes Eingabefeld. kind: input | req (Pflicht) | ro (schreibgeschützt) | ai (KI-erkannt) | select.
    Gibt y unterhalb des Feldes zurück."""
    style = {"input": "ui_input", "req": "ui_req", "ro": "ui_ro", "ai": "ui_ai", "select": "ui_input"}[kind]
    lab = label + (" *" if kind == "req" else "")
    p.box(x, y, w, 14, lab, "ui_label")
    val = value + ("   ▾" if kind == "select" else "")
    p.box(x, y + 14, w, h, val, style)
    if hint:
        p.box(x + w + 6, y + 14, 200, h, hint, "ui_hint")
    return y + 14 + h + 8

def ui_fields(p, x, y, w, fields, cols=1, colgap=16):
    """Mehrere Felder in Spalten. fields = [(label, value, kind), ...]. Gibt y-Ende zurück."""
    cw = (w - colgap * (cols - 1)) / cols
    ys = [y] * cols
    for i, f in enumerate(fields):
        c = i % cols
        label, value, kind = (list(f) + ["input"])[:3]
        ys[c] = ui_field(p, x + c * (cw + colgap), ys[c], cw, label, value, kind)
    return max(ys)

def ui_section(p, x, y, w, title):
    p.box(x, y, w, 20, title, "ui_sec")
    p.line(x, y + 21, x + w, y + 21, "line")
    return y + 28

def ui_buttons(p, x, y, labels, w=120, gap=10):
    """labels = [(text, style), ...] style: ui_btn | ui_btn2 | ui_btn_r"""
    cx = x
    for t, st in labels:
        bw = max(w, 9 * len(t) + 24)
        p.box(cx, y, bw, 28, t, st)
        cx += bw + gap
    return cx

def ui_tabs(p, x, y, labels, active=0, w=130):
    for i, t in enumerate(labels):
        p.box(x + i * w, y, w, 26, t, "ui_tab_a" if i == active else "ui_tab")
    return y + 26

def ui_viewer(p, x, y, w, h, title="Belegvorschau (Original-PDF / E-Rechnung visualisiert)", lines=None):
    p.box(x, y, w, h, "", "ui_viewer")
    p.box(x, y, w, 26, title, "text", extra=f"fillColor={C['grey_m']};fontSize=10;fontStyle=1;spacingLeft=8;verticalAlign=middle;")
    # stilisierte Rechnung
    p.box(x + 30, y + 46, w - 60, h - 70, "", "rounded=0;fillColor=#FFFFFF;strokeColor=%s;shadow=1;" % C['grey_m'])
    body = lines or ["RECHNUNG", "", "Musterbau GmbH · Industriestr. 5", "an: Livos Objektgesellschaft Nord mbH", "     Hafenstraße 22, 20359 Hamburg", "", "Rechnungs-Nr.: RE-2026-1041", "Datum: 15.09.2026", "", "Pos 1  Rohbauarbeiten  ……  12.400,00", "", "Netto 12.400,00 · USt 19 % 2.356,00", "Brutto 14.756,00 €", "", "IBAN DE12 3456 …"]
    p.box(x + 44, y + 58, w - 88, h - 94, "\n".join(body), "text", extra="fontSize=10;fontFamily=Courier New;")
    return y + h

def ui_table(p, x, y, colw, rows, rowh=24):
    """Tabellen-/Listenansicht in Masken (Kopf dunkel, Zeilen hell)."""
    return p.table(x, y, colw, rows, rowh=rowh)

def ann(p, x, y, n, text=None, tx=None, ty=None, tw=260):
    """Nummerierte Annotation (orange Kreis) + optional Erläuterungstext rechts/links."""
    p.box(x, y, 22, 22, str(n), "ann")
    if text:
        p.box(tx if tx is not None else x + 28, ty if ty is not None else y - 2, tw, 40, f"**{n}** {text}", "text", extra="fontSize=10;")

def legend_box(p, x, y, rows, title="Legende", w=300):
    """rows = [(style, label)]"""
    h = 30 + 24 * len(rows)
    p.box(x, y, w, h, "", "rounded=1;arcSize=4;fillColor=#FFFFFF;strokeColor=%s;" % C['grey_m'])
    p.box(x + 10, y + 4, w - 20, 20, title, "h2", extra="fontSize=12;")
    cy = y + 28
    for st, lab in rows:
        p.box(x + 12, cy + 2, 30, 16, "", st)
        p.box(x + 50, cy, w - 60, 20, lab, "text", extra="fontSize=10;verticalAlign=middle;")
        cy += 24
    return y + h

def status_legend(p, x, y):
    return legend_box(p, x, y, [("dvelop", "d.velop Standard"), ("dvelop_l", "d.velop Konfiguration"),
                                ("mdis", "MDIS BeSync (Anpassung)"), ("ext", "Umsystem / extern"),
                                ("open", "offen / zu verifizieren")], "Legende Status")
