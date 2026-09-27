import importlib, sys
from dio import *
PAGES = [
 ("Architektur & Modelle", [("p01","01 Systemlandschaft"),("p02","02 Schnittstellenübersicht"),("p03","03 Mandanten- und Organisationsmodell"),("p04","04 Informationsmodell"),("p05","05 Aktenplan"),("p06","06 Lieferanten- und Kreditorenmodell"),("p07","07 Prozesslandkarte")]),
 ("Prozesse", [("p08","08 ER-Prozess End-to-End (WF-01)"),("p09","09 Eingang, Vorqualifikation, Klärfall (WF-04)"),("p10","10 Bau-Rechnung mit BIM4You (WF-02)"),("p11","11 Freigabematrix und Wertgrenzen"),("p12","12 Eskalation und Vertretung"),("p13","13 Sonderfälle Eingangsrechnung"),("p14","14 Statusmodell Rechnung"),("p15","15 Property-Manager-Freigabe (WF-03)"),("p16","16 Vertragsprozess (WF-06)"),("p17","17 Postverteilung (WF-07)")]),
 ("Rollen, Integration, Steuerung", [("p18","18 Rollen und Berechtigungsmatrix"),("p19","19 Rechtemodell Cloud"),("p20","20 DATEV- und Zahlungsintegration"),("p21","21 Reporting und KPI"),("p22","22 Roadmap")]),
 ("Masken (Mockups)", [("p23","M-01 Rechnung einlesen / Stapel"),("p24","M-02 Verteilung"),("p25","M-03 Sachliche Prüfung & Kontierung"),("p26","M-04 Freigabe / Zahlungsfreigabe"),("p27","M-05 Klärfall"),("p28","M-06 Rückweisungsdialog"),("p29","M-07 Buchhaltung / DATEV"),("p30","M-08 REB Arbeitsansicht"),("p31","M-09 REB Managementsicht"),("p32","M-10 Startseite je Rolle"),("p33","M-11 Aktenansicht"),("p34","M-12 Suche"),("p35","M-13 PM-Freigabe"),("p36","M-14 Vertragsmaske"),("p37","M-15 Postverteilung"),("p38","M-16 Lieferanten-App"),("p39","M-17 Freigabematrix-Pflege"),("p40","M-18 Vertretung / Abwesenheit"),("p41","M-19 Externe Benutzeraufgabe")]),
]
def overview(doc, present):
    p = doc.page("00 Übersicht", "p00")
    p.box(0, 0, p.w, 8, "", "rounded=0;fillColor=%s;strokeColor=none;" % C['teal'])
    p.box(40, 30, 1100, 44, "Livos – DMS-Gesamtkonzept auf Basis d.velop", "title", extra="fontSize=28;")
    p.box(40, 78, 1200, 50, "Alle Sichten und Masken des Konzepts (Dokument 3) · MDIS Consulting · Stand 26.09.2026 · Entwurf zur Abstimmung\nKlick auf einen Eintrag öffnet die Seite; jede Seite führt über „zur Übersicht“ zurück. IDs (AE, R, K, E, WF, S, M, OP) verweisen auf das Konzeptdokument.", "subtitle")
    x0, y0, colw = 40, 150, 395
    for ci, (grp, items) in enumerate(PAGES):
        x = x0 + ci * (colw + 12)
        p.box(x, y0, colw, 34, grp, "dvelop", extra="fontSize=14;")
        y = y0 + 44
        for pid, name in items:
            st = "ui_btn2" if pid in present else "open"
            p.box(x, y, colw, 30, name, st, link=f"data:page/id,{pid}", extra="align=left;spacingLeft=10;fontStyle=0;")
            y += 36
    ly = 930
    status_legend(p, 40, ly - 40)
    legend_box(p, 360, ly - 40, [("task", "Aktivität (Mensch)"), ("auto", "automatischer Schritt"), ("gateway", "Entscheidung"), ("start", "Start"), ("end", "Ende")], "Legende Prozesse", w=260)
    legend_box(p, 640, ly - 40, [("ui_req", "Pflichtfeld"), ("ui_ai", "KI-/automatisch erkannt"), ("ui_ro", "schreibgeschützt"), ("ui_input", "Eingabe/Auswahl"), ("ui_hint", "Hinweis/Warnung")], "Legende Masken", w=260)
    p.box(930, ly - 40, 684, 150, "**Status-Kürzel** [S] Standard · [K] Konfiguration · [A] Anpassung (MDIS BeSync) · [O] offen/zu verifizieren\n**Katalogbewertung** S/K/A/N gemäß Livos-Leistungskatalog\nBeispielwerte (Gesellschaften, Grenzen, Fristen, Belege) sind fiktiv und als Vorschlag zu verstehen.", "info")
    p.box(40, p.h - 34, p.w - 80, 22, "Livos · DMS-Gesamtkonzept d.velop · Übersicht · MDIS Consulting · Stand 26.09.2026", "small", extra="align=center;")
def main(out):
    doc = Doc()
    mods = [m for m in ["pages_A", "pages_B", "pages_C", "pages_M1", "pages_M2"]]
    sub = Doc()
    for m in mods:
        try: importlib.import_module(m).build(sub)
        except (ModuleNotFoundError, AttributeError) as e: print("fehlt", m, e)
    present = {pg.id for pg in sub.pages}
    overview(doc, present)
    order = [pid for _, items in PAGES for pid, _ in items]
    byid = {pg.id: pg for pg in sub.pages}
    for pid in order:
        if pid in byid: doc.pages.append(byid[pid])
        else: print("Seite fehlt:", pid)
    extra = [pg.id for pg in sub.pages if pg.id not in order]
    if extra: print("unerwartete Seiten:", extra)
    doc.save(out); print("Seiten:", len(doc.pages))
if __name__ == "__main__": main(sys.argv[1])
