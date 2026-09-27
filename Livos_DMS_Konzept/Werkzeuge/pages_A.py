"""Seiten 01–07 des draw.io-Konzeptdiagramms (Systemlandschaft, Schnittstellen, Mandantenmodell,
Informationsmodell, Aktenplan, Lieferanten-/Kreditorenmodell, Prozesslandkarte). Aufruf: build(doc)."""
from dio import C, S, legend_box, status_legend

# ---------------------------------------------------------------- Hilfsfunktionen
LBG = "labelBackgroundColor=#FFFFFF;"
TXT_TL = "verticalAlign=top;align=left;spacingLeft=6;spacingTop=4;"


def tag(p, x, y, w, text, h=18, color=None, align="center", extra=""):
    """Kleines Kantenetikett (weißer Hintergrund) – manuell positioniert."""
    return p.box(x, y, w, h, text, "text",
                 extra=f"fontSize=10;fontStyle=1;fontColor={color or C['teal']};align={align};verticalAlign=middle;"
                       f"spacing=0;spacingLeft=2;spacingRight=2;labelBackgroundColor=#FFFFFF;" + extra)


def rowlabel(p, x, y, w, text):
    return p.box(x, y, w, 18, text, "text",
                 extra=f"fontSize=10;fontStyle=1;fontColor={C['navy']};verticalAlign=middle;spacing=0;")


def cell(fill, fs=10, align="left", bold=False, color=None):
    st = f"fillColor={fill};strokeColor={C['grey_m']};fontSize={fs};align={align};spacingLeft=4;spacingRight=2;verticalAlign=middle;"
    if bold: st += "fontStyle=1;"
    if color: st += f"fontColor={color};"
    return st


def tbl(p, x, y, colw, rows, rowh=26, hrow=28, fs=10, cellstyle=None):
    """Tabelle mit dunklem Kopf; cellstyle(ri, ci, text) -> Stilstring oder None."""
    cy = y
    for ri, row in enumerate(rows):
        rh = hrow if ri == 0 else rowh
        cx = x
        for ci, txt in enumerate(row):
            if ri == 0:
                st = S['th'] + f"fontSize={fs};verticalAlign=middle;"
            else:
                st = (cellstyle(ri, ci, txt) if cellstyle else None) or cell("#FFFFFF" if ri % 2 else C['grey_l'], fs)
            p.box(cx, cy, colw[ci], rh, txt, st)
            cx += colw[ci]
        cy += rh
    return cy


def phase_badge(p, x, y, ph, w=80, h=22):
    colors = {"1": C['green'], "2": C['navy'], "3": C['orange'], "4": C['purple'], "5": C['grey']}
    col = colors.get(str(ph)[0], C['grey'])
    return p.box(x, y, w, h, f"Phase {ph}", f"rounded=1;arcSize=50;fillColor={col};strokeColor=none;fontColor=#FFFFFF;fontSize=10;fontStyle=1;")


def inline_legend(p, x, y, items, colw=230, sw=26):
    cx = x
    for st, lab in items:
        p.box(cx, y + 2, sw, 16, "", st)
        p.box(cx + sw + 6, y, colw - sw - 10, 20, lab, "text", extra="fontSize=10;verticalAlign=middle;spacing=0;")
        cx += colw


# Status-Zellfarben (Schnittstellen)
ST_FILL = {"S": C['blue_l'], "K": C['yellow_l'], "A": C['green_l']}


# =================================================================== 01 Systemlandschaft
def page01(doc):
    p = doc.page("01 Systemlandschaft", "p01")
    p.header("01 Systemlandschaft – Zielarchitektur",
             "d.velop Cloud (C1) als zentrale Plattform für Eingangsrechnungen, Verträge und Post; Umsysteme über Standard-Optionen "
             "und MDIS BeSync. Kanten = Schnittstellen S-xx (Details Seite 02).")

    # ---- d.velop Cloud
    cl = p.box(400, 128, 790, 607,
               "d.velop Cloud · Betriebsform C1 (Multi-Tenant, AWS Frankfurt) · 1 Tenant Produktion + 1 Test-Tenant (AE-01)",
               "group_t", extra="opacity=100;fillColor=#EEF7F8;")
    X0 = 420
    rowlabel(p, X0, 162, 700, "Zugang, Identität & Rechte")
    idb = p.box(420, 182, 365, 48, "usermanagement: Benutzer & Gruppen (SCIM)\nSSO per OIDC", "dvelop_l", extra="fontSize=11;")
    p.box(805, 182, 365, 48, "Rechte: Kategorie × Rechtestufe\nRestriction Sets RS_Mandant / RS_Objekt (AE-18)", "dvelop_l", extra="fontSize=11;")

    rowlabel(p, X0, 244, 700, "Eingang & Erkennung")
    ib = p.box(420, 264, 172, 62, "inbound / email import\n(Funktionspostfächer, Scan)", "dvelop", extra="fontSize=11;")
    p.box(612, 264, 172, 62, "document reader\n(KI-Erkennung)", "dvelop", extra="fontSize=11;")
    p.box(804, 264, 172, 62, "eInvoice converter\n(ZUGFeRD 2.x, XRechnung 3.0)", "dvelop", extra="fontSize=11;")
    p.box(996, 264, 174, 62, "KI-Trennung / -Klassifizierung (Post)", "dvelop", extra="fontSize=11;")

    rowlabel(p, X0, 340, 750, "Rechnungsverarbeitung – d.velop invoices (Paket Medium, AE-02)")
    p.box(420, 360, 550, 152, "smart invoice – Rechnungsworkflows WF-01 … WF-05", "dvelop",
          extra="verticalAlign=top;spacingTop=6;fontSize=12;")
    steps = ["Verteilung", "Sachl. Prüfung\n& Kontierung", "Fachl. Freigabe\n1..n", "Zahlungs-\nfreigabe", "Buchhaltung\n(Trios)"]
    for i, s in enumerate(steps):
        p.box(431 + i * 108, 392, 100, 50, s, "dvelop_l", extra="fontSize=10;")
    p.box(431, 452, 528, 48, "Rechnungseingangsbuch (REB) · Freigabematrix (Spalte Mandant)\nMandanten ≤ 1.000 je Bucket · Klärfall / Clearing je Mandant",
          "dvelop_l", extra="fontSize=10;")
    ld = p.box(990, 360, 180, 152,
               "**Option DATEV Rechnungswesen**\n\nLDconnect (LIONDEER)\nüber DATEVconnect\n\nBuchungsvorschlag + Beleglink,\nStammdaten täglich",
               "partner", extra="fontStyle=0;fontSize=11;")

    rowlabel(p, X0, 524, 750, "Dokumentenmanagement & Verträge (platform edition business)")
    docs = p.box(420, 544, 250, 68, "d.velop documents\nAkten, Suche, Aufgaben, Aufbewahrung", "dvelop", extra="fontSize=11;")
    p.box(690, 544, 230, 68, "d.velop contracts\nVertragsakte, Fristen", "dvelop", extra="fontSize=11;")
    p.box(940, 544, 230, 68, "d.velop mail dispatcher\nPostverteilung an Gruppen", "dvelop", extra="fontSize=11;")

    rowlabel(p, X0, 624, 750, "Prozesse, KI & Zugang")
    p.box(420, 644, 250, 68, "process studio\nweitere Freigaben, externe Benutzeraufgabe", "dvelop", extra="fontSize=11;")
    p.box(690, 644, 230, 68, "d.velop pilot\nKI-Fragen an Dokumente / Verträge", "dvelop", extra="fontSize=11;")
    p.box(940, 644, 230, 68, "d.velop mobile App\nOutlook-Integration", "dvelop", extra="fontSize=11;")

    # ---- BeSync
    bs = p.box(400, 800, 790, 170, "MDIS BeSync – Middleware-Plattform (Betrieb MDIS, Anpassung [A], P3)", "mdis",
               extra="verticalAlign=top;align=left;spacingLeft=10;spacingTop=6;fontSize=13;")
    p.box(420, 838, 250, 114, "**Lieferanten-App**\nKonsolidierungsnr., Kreditor-Mapping je Mandant, Gesellschafts- und Objektstamm, FSB-Status",
          "task_mdis", extra="fillColor=#FFFFFF;fontSize=11;")
    p.box(690, 838, 270, 114, "**Integrationsdienste**\nDATEV-OPOS, BIM4You-Transfer, Mailversand (Graph oder d.velop-Messaging-API, OP-25), Export je Gesellschaft",
          "task_mdis", extra="fillColor=#FFFFFF;fontSize=11;")
    p.box(985, 838, 185, 114, "MS-SQL-Staging\n(Prozessereignisse)", "db", extra=f"strokeColor={C['green']};fillColor=#FFFFFF;")

    # Cloud <-> BeSync (senkrecht)
    for fx, st, lbl, tw, left in [(0.10, "data2", "S-04 Stammdaten,\nKonsolidierungsnr.", 130, False),
                                  (0.37, "data", "S-06 Zahlstatus\n→ DMS-Eigenschaft", 130, False),
                                  (0.63, "data2", "S-08 / S-09\nTransfer Bau", 110, False),
                                  (0.88, "data", "S-11 / S-12\nWebhooks", 90, False)]:
        x = 400 + fx * 790
        if st == "data" and lbl.startswith("S-06"):
            p.edge(bs, cl, "", "data", exit=(fx, 0), entry=(fx, 1))
        else:
            p.edge(cl, bs, "", st, exit=(fx, 1), entry=(fx, 0))
        tag(p, x + 6, 748, tw, lbl, h=34, align="left")

    # ---- linke Spalte
    m365 = p.box(40, 160, 270, 180,
                 "**Microsoft 365 / Entra ID**\n\nPostfächer rechnung@…, Alias je Gesellschaft, freigabe-hv@…\n\nIdentitäten und Gruppen",
                 "ext", extra="fontStyle=0;")
    lief = p.box(40, 420, 180, 80, "**Lieferanten**\nPDF, E-Rechnung, Papier", "ext", extra="fontStyle=0;")
    pm = p.box(40, 560, 270, 90, "**Property Manager (HV, ~10)**\nbuchen und zahlen selbst; Freigabe-Rechnungen über Schwellwert per E-Mail",
               "ext", extra="fontStyle=0;")
    p.edge(m365, idb, "", "data", exit=(1, 0.256), entry=(0, 0.5))
    tag(p, 316, 186, 80, "S-13 SCIM/OIDC")
    p.edge(m365, ib, "", "data", exit=(1, 0.744), entry=(0, 0.5))
    tag(p, 316, 276, 80, "S-14 E-Mail")
    p.edge(lief, m365, "", "flow", exit=(0.5, 0), entry=(0.333, 1))
    tag(p, 134, 368, 120, "Rechnungen", align="left")
    p.edge(pm, m365, "", "flow", exit=(0.85, 0), entry=(0.85, 1))
    tag(p, 60, 514, 205, "Freigabe-Rechnungen (freigabe-hv@…)", align="right", h=34)
    # S-11 an Lieferanten / PM, S-16, S-17
    p.edge(bs, lief, "", "data", exit=(0, 0.088), entry=(1, 0.5), points=[(350, 815), (350, 460)])
    tag(p, 226, 424, 118, "S-11 Rückweisung,\nKürzung", h=32, align="left")
    p.edge(bs, pm, "", "data", exit=(0, 0.294), entry=(0.648, 1), points=[(215, 850)])
    tag(p, 222, 690, 120, "S-11 Rück-\nmeldung PM", h=32, align="left")
    p.edge(pm, bs, "", "data", exit=(0.3, 1), entry=(0, 0.588), points=[(121, 900)])
    tag(p, 126, 862, 86, "S-16 (optional)", align="left")
    p.edge(pm, docs, "", "data", exit=(1, 0.2), entry=(0, 0.5),
           extra=f"strokeColor={C['red']};fontColor={C['red']};")
    tag(p, 356, 556, 44, "S-17", color=C['red'])

    # ---- rechte Spalte
    p.box(1320, 128, 294, 402, "DATEV-Umgebung (extern gehostet)", "group_g", extra="fontSize=12;")
    trios = p.box(1335, 162, 264, 64, "**Trios** (Buchhaltungsdienstleister)\nbucht in DATEV, legt Kreditoren an", "ext", extra="fontStyle=0;")
    rw = p.box(1335, 248, 264, 88, "**DATEV Rechnungswesen**\nKreditoren, Buchungen, OPOS, Zahlungsvorschlag", "ext", extra="fontStyle=0;")
    gw = p.box(1335, 360, 264, 72, "**Riecken Cloud Gateway**\n(DATEVconnect-Zugang)", "ext", extra="fontStyle=0;")
    duo = p.box(1335, 452, 264, 62, "**DATEV Unternehmen online**\n(optional, Belegbilder)", "ext", extra="fontStyle=0;dashed=1;")
    p.edge(trios, rw, "", "flow", exit=(0.5, 1), entry=(0.5, 0))
    p.edge(gw, rw, "", "data2", exit=(0.5, 0), entry=(0.5, 1))
    p.edge(ld, gw, "", "data", exit=(1, 0.184), entry=(0, 0.389))
    p.edge(gw, ld, "", "data", exit=(0, 0.83), entry=(1, 0.395))
    p.edge(ld, duo, "", "data", exit=(1, 0.79), entry=(0, 0.45))
    tag(p, 1262, 370, 52, "S-01")
    tag(p, 1262, 422, 52, "S-02")
    tag(p, 1262, 462, 52, "S-03")
    mc = p.box(1335, 560, 264, 72, "**multicash (Omikron)**\nZahllauf, Unterschrift (EBICS)", "ext", extra="fontStyle=0;")
    p.edge(rw, mc, "", "flow", exit=(1, 0.5), entry=(1, 0.5), points=[(1628, 292), (1628, 596)])
    tag(p, 1480, 537, 120, "S-07 SEPA-XML", align="right", color=C['navy'])
    bim = p.box(1335, 680, 264, 86, "**BIM4You (BIB GmbH)**\nBau-Budget, VOB, Einbehalte, Prüfer-Workflow", "ext", extra="fontStyle=0;")
    ev = p.box(1335, 895, 264, 62, "**evidanza (BI)**\nDurchlauf- und Liegezeiten", "ext", extra="fontStyle=0;")
    arch = p.box(1335, 995, 264, 80, "Archivpaket je Gesellschaft\n(Verkauf, Betriebsprüfung)", "doc")

    # Korridor-Kanten BeSync <-> rechts
    p.edge(bs, trios, "", "data2", exit=(1, 0.088), entry=(0, 0.5), points=[(1215, 815), (1215, 194)])
    tag(p, 1220, 150, 98, "S-05 Kreditor-\nAnlage", h=32, align="left")
    p.edge(rw, bs, "", "data", exit=(0, 0.886), entry=(1, 0.176), points=[(1240, 326), (1240, 830)])
    tag(p, 1244, 306, 74, "S-06 OPOS", align="left")
    p.edge(bs, bim, "", "data", exit=(1, 0.353), entry=(0, 0.29), points=[(1270, 860), (1270, 705)])
    tag(p, 1274, 686, 56, "S-08", align="left")
    p.edge(bim, bs, "", "data", exit=(0, 0.72), entry=(1, 0.47), points=[(1295, 742), (1295, 880)])
    tag(p, 1196, 883, 96, "S-09 / S-10", align="left")
    p.edge(bs, ev, "", "data", exit=(1, 0.765), entry=(0, 0.645))
    tag(p, 1196, 910, 120, "S-12 Ereignisse", align="left")
    p.edge(bs, arch, "", "data", exit=(0.9, 1), entry=(0, 0.45), points=[(1111, 1031)])
    tag(p, 1150, 1011, 120, "S-15 Export", align="left")

    # ---- Hinweise + Legende
    p.box(400, 995, 690, 118,
          "**Leitplanken der Architektur**\n"
          "• Nur d.velop übergibt Eingangsrechnungen an DATEV (S-01); der BIM4You-DATEV-Export für ER bleibt aus (AE-11).\n"
          "• Je Objekttyp im Bucket ein Schreiber: DATEV-Stammdaten nur LDconnect (S-02); BeSync nur Mandanten, Custom Entities, DMS-Eigenschaften (AE-09).\n"
          "• Zahlungen führt multicash aus (S-07); d.velop liefert die Zahlungsfreigabe, BeSync meldet „bezahlt“ zurück (S-06).\n"
          "• BeSync nur, wo der Standard endet – Betrieb durch MDIS (P3).",
          "info")
    legend_box(p, 40, 935, [("dvelop", "d.velop Standard"), ("dvelop_l", "d.velop Konfiguration"),
                            ("partner", "Drittanbieter-Option (über d.velop)"), ("mdis", "MDIS BeSync (Anpassung)"),
                            ("ext", "Umsystem / extern"), ("open", "offen / Folgeprojekt")], "Legende Status", w=270)


# =================================================================== 02 Schnittstellen
S_ROWS = [
    ["ID", "Schnittstelle", "Richtung", "Technik", "Auslöser", "Status", "Phase"],
    ["S-01", "DATEV Buchungsvorschlag + Beleglink", "d.velop → DATEV", "Option DATEV Rechnungswesen (LDconnect, DATEVconnect, Riecken-Gateway)", "Schritt Buchhaltung (ereignisgesteuert)", "K", "1"],
    ["S-02", "DATEV-Stammdaten (Kreditoren, Sachkonten, Steuerschlüssel, Zahlungsbedingungen, Bankverbindungen, KOST1/2)", "DATEV → smart invoice", "LDconnect", "täglich", "K", "1"],
    ["S-03", "Belegbilder nach DATEV Unternehmen online", "d.velop → DUO", "Option DUO", "Übergabe", "K (optional)", "nach Bedarf"],
    ["S-04", "Lieferanten-App ↔ d.velop (Konsolidierungsnr., Gesellschafts-/Objektstamm, Datasets, Restriction Sets, smart-invoice-Mandanten)", "BeSync ↔ d.velop", "smart-invoice-Stammdaten-API, DmsConfig-/DMS-API", "nächtlich + bei Änderung", "A", "1 Erstimport /\n2 Automatik"],
    ["S-05", "Lieferanten-App ↔ DATEV (Kreditor-Mapping, Anlage-Anforderung an Trios)", "BeSync ↔ DATEV / Trios", "DATEVconnect lesen + Anforderung an Trios (Aufgabe / E-Mail)", "bei Neuanlage / Klärfall", "A", "1 E-Mail-Anforderung /\n2 automatisiert"],
    ["S-06", "Zahlstatus „bezahlt“ (OPOS)", "DATEV → BeSync → d.velop", "DATEVconnect accounts-payable → DMS-API (E-23)", "täglich (nachts, optional mehrfach)", "A", "3"],
    ["S-07", "Zahlungsdatei SEPA → multicash", "DATEV → multicash", "DATEV-Zahlungsverkehr / SEPA-XML, multicash-Import (Standard beider Hersteller)", "Zahllauf", "S (außerhalb d.velop)", "1"],
    ["S-08", "BIM4You Hinweg (Bau-Rechnung)", "d.velop → BeSync → BIM4You", "smart-invoice-Transfer (asynchron) → E-Rechnungsimport / Austauschordner", "Schrittverbindung „Bauprüfung“", "A", "3"],
    ["S-09", "BIM4You Rückweg (Prüfergebnis, Einbehalte, Freigabestatus, Prüfbericht)", "BIM4You → BeSync → d.velop", "Export / Polling → DMS-API + Transfer-Rückmeldung", "Freigabe / Storno in BIM4You", "A", "3"],
    ["S-10", "BIM4You-Stammdaten (Projekte, Vergabeeinheiten, Verträge)", "BIM4You → smart invoice", "Custom Entities / Stammdaten-API", "nächtlich", "A", "3"],
    ["S-11", "Rückweisungs-, Kürzungs- und PM-Rückmelde-Mail", "d.velop → BeSync → Lieferant / PM", "Webhook an Verbindung → Microsoft Graph oder d.velop-Messaging-API (OP-25)", "Ablehnen / Endverbindung / Kürzung", "A", "2"],
    ["S-12", "Prozessereignisse → evidanza", "d.velop → BeSync → MS SQL → evidanza", "Export-Events je Schrittwechsel + nächtliche API-Abfrage", "Schrittwechsel", "A", "1 Protokoll /\n2 Auswertungen"],
    ["S-13", "Identitäten (Benutzer, Gruppen)", "Entra ID → d.velop", "SCIM 2.0, OIDC", "laufend", "S/K", "0 / 1"],
    ["S-14", "E-Mail-Eingang (Rechnungen, PM-Freigabe, Post)", "M365 → d.velop", "email import (Graph) / inbound e-mail", "laufend", "S", "1 ER · 2 PM · 4 Post"],
    ["S-15", "Export je Gesellschaft", "d.velop → Archivpaket", "repo export-API + BeSync-Skript", "Anlass (Verkauf, Prüfung)", "A", "1 Voraussetzung P1 /\n2 Exportskript"],
    ["S-16", "PM-Buchungsdaten (monatlich) → BI", "PM → BeSync → BI", "Upload / Postfach, Parser", "monatlich", "A (optional)", "3 (optional)"],
    ["S-17", "ERP-/PM-Stammdatensync (perspektivisch)", "bidirektional", "d.velop REST-API", "Folgeprojekt", "A (Katalog 5.4)", "Folgeprojekt"],
]


def page02(doc):
    p = doc.page("02 Schnittstellenübersicht", "p02")
    p.header("02 Schnittstellenübersicht (S-01 … S-17)",
             "Status: S Standard · K Konfiguration / Standard-Option · A Anpassung über MDIS BeSync. Phase gemäß Schnittstellenkatalog (Kap. 15.1.2) und Roadmap (Kap. 19).")

    def cs(ri, ci, t):
        base = "#FFFFFF" if ri % 2 else C['grey_l']
        if ci == 0:
            return cell(base, 10, bold=True, color=C['navy'])
        if ci == 5:
            return cell(ST_FILL.get(t[0], base), 10, align="center", bold=True)
        if ci == 6:
            return cell(base, 10, align="center")
        return None
    tbl(p, 40, 116, [52, 372, 212, 420, 220, 138, 160], S_ROWS, rowh=36, hrow=28, fs=10, cellstyle=cs)
    # y-Ende = 116 + 28 + 17*36 = 756

    p.box(40, 776, 700, 26, "Datenflüsse im Überblick", "h2")
    lp = p.box(40, 850, 140, 56, "Lieferanten /\nProperty Manager", "ext")
    m3 = p.box(230, 850, 120, 56, "M365 /\nEntra ID", "ext")
    cl = p.box(400, 840, 230, 76, "d.velop Cloud\ninvoices · documents · contracts", "dvelop")
    ld = p.box(690, 850, 130, 56, "LDconnect\n(Riecken-Gateway)", "partner")
    dv = p.box(870, 850, 100, 56, "DATEV\n(Trios)", "ext")
    mc = p.box(1000, 850, 100, 56, "multicash", "ext")
    bs = p.box(400, 1010, 230, 60, "MDIS BeSync\nLieferanten-App", "mdis")
    bim = p.box(190, 1015, 150, 50, "BIM4You", "ext")
    ev = p.box(690, 1015, 130, 50, "evidanza", "ext")

    p.edge(lp, m3, "", "flow")
    tag(p, 182, 856, 46, "E-Mail", color=C['navy'])
    p.edge(m3, cl, "", "data", exit=(1, 0.5), entry=(0, 0.53))
    tag(p, 352, 832, 46, "S-13\nS-14", h=26)
    p.edge(cl, ld, "", "line", exit=(1, 0.53), entry=(0, 0.5))
    p.edge(ld, dv, "", "data", exit=(1, 0.3), entry=(0, 0.3))
    p.edge(dv, ld, "", "data", exit=(0, 0.75), entry=(1, 0.75))
    tag(p, 822, 846, 46, "S-01")
    tag(p, 822, 894, 46, "S-02")
    p.edge(dv, mc, "", "flow", exit=(1, 0.5), entry=(0, 0.5))
    tag(p, 968, 832, 36, "S-07", color=C['navy'])
    # Cloud <-> BeSync
    p.edge(cl, bs, "", "data2", exit=(0.2, 1), entry=(0.2, 0))
    tag(p, 452, 930, 44, "S-04", align="left")
    p.edge(cl, bs, "", "data", exit=(0.45, 1), entry=(0.45, 0))
    tag(p, 510, 952, 64, "S-08 S-11\nS-12", h=30, align="left")
    orange = f"strokeColor={C['orange']};strokeWidth=2;"
    p.edge(bs, cl, "", "data", exit=(0.72, 0), entry=(0.72, 1), extra=orange)
    tag(p, 569, 925, 60, "S-06\nS-09", h=30, align="left", color=C['orange'])
    # BIM4You
    p.edge(bs, bim, "", "data", exit=(0, 0.3), entry=(1, 0.26))
    tag(p, 346, 1008, 50, "S-08")
    p.edge(bim, bs, "", "data", exit=(1, 0.74), entry=(0, 0.7), extra=orange)
    tag(p, 342, 1054, 56, "S-09/10", color=C['orange'])
    p.edge(bs, ev, "", "data", exit=(1, 0.5), entry=(0, 0.5))
    tag(p, 634, 1020, 52, "S-12")
    # DATEV -> BeSync (S-06)
    p.edge(dv, bs, "", "data", exit=(0.5, 1), entry=(0.87, 0), points=[(920, 975), (600, 975)], extra=orange)
    tag(p, 830, 957, 90, "S-06 OPOS", color=C['orange'])
    # BeSync -> Lieferant/PM (S-11)
    p.edge(bs, lp, "", "data", exit=(0.1, 1), entry=(0.5, 1), points=[(423, 1095), (110, 1095)])
    tag(p, 116, 1060, 40, "S-11", align="left")

    p.box(1130, 790, 484, 150,
          "**Rückkanäle BIM4You / DATEV → DMS-Eigenschaften**\n**Kein Schreibzugriff auf laufende smart-invoice-Belege**\n\n"
          "S-06 (Zahlstatus aus DATEV-OPOS, Phase 3) und S-09 (Prüfergebnis BIM4You) setzen über BeSync DMS-Eigenschaften am Beleg "
          "(E-22, E-23) und legen Prüfberichte ab (K-08). Laufende smart-invoice-Belege ändert BeSync nicht per API "
          "(nicht belegt, OP-07). Den Zahlbetrag setzt die Rechnungsprüfung auf Basis des BIM4You-Ergebnisses.",
          "warn", extra="fontSize=11;")
    legend_box(p, 1130, 960, [(cell(ST_FILL['S'], 10), "S – Standard"), (cell(ST_FILL['K'], 10), "K – Konfiguration / Standard-Option"),
                              (cell(ST_FILL['A'], 10), "A – Anpassung über MDIS BeSync")], "Legende Status", w=300)
    p.box(1440, 964, 174, 100, "Orange Kanten = Rückkanäle in DMS-Eigenschaften", "text",
          extra=f"fontSize=10;fontColor={C['orange']};fontStyle=1;")


# =================================================================== 03 Mandantenmodell
def page03(doc):
    p = doc.page("03 Mandanten- und Organisationsmodell", "p03")
    p.header("03 Mandanten- und Organisationsmodell",
             "Ein Tenant, ein Repository, ein smart-invoice-Bucket; jede Gesellschaft = ein Mandant (AE-01, AE-03, P1). Gesellschafts-IDs und Namen: Beispiele.")

    # ---- Struktur (links)
    p.box(40, 112, 560, 26, "Struktur in der d.velop Cloud", "h2")
    ten = p.box(60, 150, 330, 60, "**Tenant „Livos Produktion“**\nd.velop Cloud C1 (AWS Frankfurt)", "dvelop", extra="fontStyle=0;")
    tst = p.box(420, 150, 170, 60, "Test-/Abnahme-Tenant\n(gleiche Struktur)", "dvelop_l", extra="dashed=1;")
    p.edge(ten, tst, "", "assoc")
    rep = p.box(60, 250, 330, 60, "**Repository (1) – d.velop documents**\nKategorien, Eigenschaften, Akten, Rechte", "dvelop", extra="fontStyle=0;")
    bk = p.box(60, 350, 330, 60, "**smart-invoice-Bucket (1)**\nWorkflows, Freigabematrix, Stammdaten", "dvelop", extra="fontStyle=0;")
    p.edge(ten, rep, "", "tree")
    p.edge(rep, bk, "", "tree")
    p.box(420, 240, 170, 180,
          "1 Tenant für die Livos-Gruppe: Der Tenant trennt Kunden, nicht Gesellschaften.\n\nMehr als 100 Gesellschaften passen als Mandanten in einen Bucket.",
          "note")
    mands = [("10010", "Livos Objektgesellschaft Nord mbH"), ("10020", "Livos Objektgesellschaft Süd mbH"),
             ("10030", "Livos Bau & Projekt GmbH"), ("…", "bis 1.000 Mandanten je Bucket")]
    for i, (mid, nm) in enumerate(mands):
        b = p.box(50 + i * 137, 460, 128, 66, f"**{mid}**\n{nm}", "dvelop_l", extra="fontSize=10;")
        p.edge(bk, b, "", "tree")
    p.box(50, 530, 540, 20, "Mandanten = Gesellschaften (Beispiel-IDs, fiktive Demo-Gesellschaften)", "small")

    # ---- Segmente
    p.box(40, 566, 560, 26, "Segmente (E-31, aus dem Gesellschaftsstamm)", "h2")
    segs = [("Bestand", "Objektgesellschaften im Bestand, z.B. Livos Objektgesellschaft Nord mbH (Beispiel)",
             "WF-01; PM-verwaltete Objekte zusätzlich WF-03 (PM-Freigabe)"),
            ("Privatisierung", "Gesellschaften mit Verkauf von Einheiten",
             "WF-01; bei Verkauf einer Gesellschaft Export je Gesellschaft (S-15)"),
            ("Bau", "Projekt- und Baugesellschaften, z.B. Livos Bau & Projekt GmbH (Beispiel)",
             "WF-02 mit BIM4You (S-08 / S-09); Kennzeichen Bauleistender § 13b")]
    for i, (t, d, w) in enumerate(segs):
        x = 40 + i * 190
        p.box(x, 600, 180, 34, t, "dvelop", extra="fontSize=13;")
        p.box(x, 634, 180, 150, f"{d}\n\n**Prozess:** {w}", "text",
              extra=f"strokeColor={C['teal']};fillColor=#FFFFFF;fontSize=11;spacingLeft=6;spacingTop=6;")
    p.box(40, 800, 560, 104,
          "**Gesellschaftsstamm (AE-28) – führend Lieferanten-App / BeSync**\n"
          "Mandanten-ID · Name exakt wie auf Rechnungen · Anschrift · USt-IdNr. · StNr. · DATEV-Berater-/Mandantennr. · "
          "Segment · Bauleistender § 13b · Verwaltungsart Eigen-/PM-verwaltet · PM-Name · Freigabeverbund\n"
          "→ per API in smart-invoice-Mandanten, DMS-Datasets und Restriction Sets (S-04)",
          "task_mdis", extra=TXT_TL + "fontSize=11;")
    p.box(40, 920, 560, 96,
          "**Mandantenerkennung (AE-23):** Der Standard erkennt den Empfänger über Name + Anschrift. "
          "Gleiche Anschriften (z.B. Nord und Bau & Projekt, Hafenstraße 22) brauchen das Maßnahmenbündel: "
          "exakte Gesellschaftsbezeichnung, Käuferreferenz (BT-10), Alias-Postfach je Gesellschaft, Klärfall-Mandant, "
          "Test mit echten Livos-Belegen (OP-02).",
          "warn", extra="fontSize=11;")

    # ---- Schlüssel (Mitte)
    p.box(640, 112, 470, 26, "Gesellschaft = Mandant (P1, AE-03)", "h2")
    key = p.box(640, 150, 470, 150,
                "**Gesellschaftsschlüssel = Mandanten-ID**\n"
                "DMS-Eigenschaft „Mandant“ (E-01) + „Mandantenname“ (E-02)\n"
                "keine zweite Eigenschaft „Gesellschaft“\n\n"
                "**Mandanten-ID = DATEV-Mandantennummer (Vorschlag)**\n"
                "feste Länge, nur Ziffern, z.B. 10010 (Format mit Trios abstimmen)",
                "dvelop_l", extra="fontSize=12;")
    p.box(640, 312, 470, 20, "Der Schlüssel steuert:", "text", extra="fontStyle=1;fontSize=11;spacing=0;")
    uses = [("Rechte", "Restriction Sets RS_Mandant_Lesen/_Bearbeiten, Gruppen DMS_G_/DMS_GB_<MandantNr>"),
            ("Aktenbildung", "Mandant in jeder Erkennung (S1–S6, Seite 05)"),
            ("Workflow-Routing", "Freigabematrix Spalte Mandant, Clearing je Mandant"),
            ("DATEV-Übergabe", "LDconnect je DATEV-Mandant (S-01 / S-02)"),
            ("Mandantenerkennung", "Name + Anschrift, Alias-Postfach je Gesellschaft"),
            ("Export je Gesellschaft", "Verkauf, Betriebsprüfung (S-15)")]
    for i, (t, d) in enumerate(uses):
        x = 640 + (i % 2) * 240
        y = 338 + (i // 2) * 88
        p.box(x, y, 230, 78, f"**{t}**\n{d}", "task", extra="fontSize=11;")

    p.box(640, 616, 470, 26, "Rechtebezug orthogonal: Rolle × Gesellschaft (AE-18)", "h2")
    r1 = p.box(640, 654, 220, 60, "**DMS_R_Pruefer**\nRollengruppe → Permission", "dvelop_l")
    r2 = p.box(890, 654, 220, 60, "**DMS_G_10010 / DMS_GB_10010**\nGesellschaftsgruppen → RS_Mandant_Lesen / _Bearbeiten", "dvelop_l")
    r3 = p.box(720, 764, 310, 60, "Benutzer bearbeitet Belege der Kategorie K nur für Mandant 10010", "task")
    p.edge(r1, r3, "", "tree")
    p.edge(r2, r3, "", "tree")
    p.box(640, 834, 470, 34, "Annahme: Das Restriction Set zieht Werte aus allen Gruppen des Benutzers (Test T03, OP-08).", "small",
          extra="fontSize=10;")
    p.box(640, 876, 470, 140,
          "**Mengengerüst Rechte**\n"
          "• ca. 50–70 Permissions, unabhängig von der Zahl der Gesellschaften\n"
          "• Rollengruppen DMS_R_* (ca. 10–12)\n"
          "• Gesellschaftsgruppen DMS_G_ / DMS_GB_<MandantNr> (nur Werteträger)\n"
          "• Verbundgruppen DMS_GF_<Verbund> für Geschäftsführung\n"
          "• Objektgruppen DMS_O_<ObjektID> für Projektleitung (RS_Objekt)\n"
          "• smart-invoice-Gruppen dv_* / SI_<Rolle>_<MandantNr>\n"
          "• Identitäten aus Entra ID per SCIM, flache Gruppen (S-13)",
          "info", extra="fontSize=11;")

    # ---- Limits + Onboarding (rechts)
    p.box(1150, 112, 464, 26, "Limits je smart-invoice-Bucket", "h2")
    kpis = [("1.000", "Mandanten je Bucket"), ("100.000", "Kreditoren je Bucket"), ("50.000", "Sachkonten je Bucket"),
            ("100", "Workflowdefinitionen je Bucket (je max. 50 Schritte)"), ("50", "Buckets bzw. Repositories (max.)")]
    for i, (v, t) in enumerate(kpis):
        x = 1150 + (i % 3) * 158
        y = 148 + (i // 3) * 82
        w = 148 if i < 3 else (148 if i == 4 else 148)
        p.box(x, y, w, 72, f"<b style='font-size:18px'>{v}</b><br>{t}", "ui_kpi", raw=True, extra="fontSize=10;")
    p.box(1466, 230, 148, 72, "Quelle: smart invoice Cloud Handbuch 06/2026", "small", extra="fontSize=9;verticalAlign=middle;")
    p.box(1150, 314, 464, 58,
          "Kreditoren werden je Mandant angelegt: Bei > 100 DATEV-Mandanten Kreditoren- und Sachkontenlimit beobachten.",
          "warn", extra="fontSize=11;")

    p.box(1150, 386, 464, 26, "Onboarding neue Gesellschaft (per API automatisierbar)", "h2")
    trg = p.box(1150, 420, 464, 50, "Auslöser: Gesellschaft in der Lieferanten-App freigegeben (R-12) → BeSync (S-04)",
                "mdis", extra="fontStyle=0;fontSize=11;")
    steps = [("smart-invoice-Mandant im Bucket", "ID, Name und Anschrift exakt wie auf Rechnungen (Stammdaten-API)"),
             ("Dataset-Wert „Mandant“ ergänzen", "DMS-Wertemenge über DmsConfig-API"),
             ("Gruppen DMS_G_<MandantNr> / SI_<Rolle>_<MandantNr>", "Entra ID → SCIM, Mitglieder zuordnen"),
             ("Zuordnung in RS_Mandant_Lesen / _Bearbeiten", "Gesellschafts- und Verbundgruppe → Mandanten-ID")]
    prev = trg
    for i, (t, d) in enumerate(steps):
        y = 494 + i * 84
        b = p.box(1190, y, 424, 62, f"**{t}**\n{d}", "task_mdis", extra="align=left;spacingLeft=10;fontSize=11;")
        p.box(1150, y + 17, 28, 28, str(i + 1), "ann", extra="fontSize=13;")
        p.edge(prev, b, "", "flow", exit=(0.5 if i else 0.543, 1), entry=(0.5, 0))
        prev = b
    p.box(1150, 834, 464, 92,
          "**Außerdem:** Freigabematrix-Zeilen je Mandant (API) · Gesellschaftsakte entsteht beim ersten Dokument.\n"
          "**Manuell:** DATEV-Bestand (Trios), LDconnect/Gateway-Freigabe, Clearing- und REB-Berechtigung je Mandant "
          "(API nicht dokumentiert, OP-08), Testbeleg zur Abnahme (Kap. 6.9).",
          "open", extra="fontSize=10;align=left;verticalAlign=top;spacing=6;")
    status_legend(p, 1150, 944)
    p.box(1466, 944, 148, 146, "Neue Gesellschaft: keine neue Kategorie, kein neuer Workflow, keine neue Permission (Kap. 6.9)",
          "note", extra="fontSize=10;")


# =================================================================== 04 Informationsmodell
E_ROWS = [
    ["ID", "Eigenschaft", "Typ", "Quelle / Wertemenge"],
    ["E-01", "Mandant (Mandanten-ID)", "Text", "Dataset Gesellschaften (BeSync) / smart invoice"],
    ["E-02", "Mandantenname", "Text", "aus Stamm"],
    ["E-03", "Objekt-ID", "Text", "Dataset Objekte (global eindeutig, BeSync)"],
    ["E-04", "Objektbezeichnung", "Text", "aus Stamm"],
    ["E-05", "Kreditor-Nr (DATEV)", "Text", "smart-invoice-Bucket (LDconnect)"],
    ["E-06", "Kreditorname", "Text", "Bucket"],
    ["E-07", "Lieferanten-Konsolidierungsnummer", "Text", "Lieferanten-App (BeSync)"],
    ["E-08", "Rechnungsnummer", "Text", "Erkennung"],
    ["E-09", "Rechnungsdatum", "Datum", "Erkennung"],
    ["E-10", "Leistungsdatum / -zeitraum", "Text/Datum", "Erkennung"],
    ["E-11", "Nettobetrag / Steuerbetrag / Bruttobetrag", "Währung", "Erkennung"],
    ["E-12", "Zahlbetrag", "Währung", "smart invoice (pay_amount)"],
    ["E-13", "Kürzungsgrund", "Text", "Werteliste Kürzungsgründe"],
    ["E-14", "Belegart", "Text", "Rechnung · Gutschrift · Abschlag · Schluss · Storno"],
    ["E-15", "Fälligkeit netto / Skontofrist / Skontobetrag", "Datum/Währung", "Erkennung / Zahlungsbedingung Stamm"],
    ["E-16", "IBAN (Beleg)", "Text", "Erkennung, Abgleich mit Stamm"],
    ["E-17", "Kostenstelle(n) / Sachkonto / KOST2", "Text", "Bucket (DATEV)"],
    ["E-18", "Gewerk / Vergabeeinheit (Los)", "Text", "BIM4You-Stamm (Custom Entity, BeSync)"],
    ["E-19", "Auftragsnummer / Vertragsnummer", "Text", "Erkennung / Stamm"],
    ["E-20", "Reverse Charge § 13b", "Text", "Wertemenge Ja/Nein (kein Boolean-Typ)"],
    ["E-21", "FSB gültig bis / FSB-Status", "Datum/Text", "Bescheinigung / BeSync"],
    ["E-22", "Sicherheitseinbehalt / geprüfter Betrag / Freigabestatus BIM4You", "Währung/Text", "BeSync (BIM4You)"],
    ["E-23", "Zahlstatus / Zahldatum", "Text/Datum", "BeSync (DATEV-OPOS)"],
    ["E-24", "Workflowstatus / aktueller Schritt", "Text", "smart invoice (kein eigenes Statusfeld)"],
    ["E-25", "Eingangskanal", "Text", "E-Mail · Scan · E-Rechnung · Upload · PM-Freigabe"],
    ["E-26", "Rückweisungsgrund", "Text", "Werteliste (5 Standardgründe)"],
    ["E-27", "Dokumentdatum / Betreff / Absender", "Datum/Text", "Erkennung / manuell"],
    ["E-28", "Vertragsdaten (Partner, Beginn, Ende, Kündigungsfrist, Verlängerung, Wert)", "div.", "d.velop contracts"],
    ["E-29", "Aufbewahrungsbeginn", "Datum", "berechnet (31.12. des Belegjahres)"],
    ["E-30", "Verwaltungsart / Property Manager", "Text", "Objektstamm (BeSync)"],
    ["E-31", "Segment", "Text", "Bestand · Privatisierung · Bau (Gesellschaftsstamm)"],
    ["E-32", "Workflowbeteiligte (IDs)", "Text, mehrfach", "smart invoice"],
]


def page04(doc):
    p = doc.page("04 Informationsmodell", "p04")
    p.header("04 Informationsmodell – Kategorien und Eigenschaften",
             "Kategorien K-01 … K-15 (Dokumentarten D, Aktenarten A) mit Pflicht-Eigenschaften; Eigenschaftenkatalog E-01 … E-32 (AE-29: eine Eigenschaft je Fachbegriff).")
    boxst = TXT_TL + "fontSize=11;"
    # Dokumentarten
    p.box(40, 112, 770, 492, "Dokumentarten (D)", "group", extra="fontSize=13;")
    p.box(55, 142, 740, 120,
          "**K-01 Eingangsrechnung** – Rechnungen, Gutschriften, Abschlags-/Schlussrechnungen (smart-invoice-Onboarding-Kategorie) · Aufbewahrung 8 J. ab E-29 · Phase 1\n\n"
          "**Pflicht (DMS):** E-01 Mandant · E-25 Eingangskanal · E-29 Aufbewahrungsbeginn (E-02, E-32 automatisch aus smart invoice)\n"
          "**Fachlich in smart invoice:** E-05 Kreditor-Nr · E-08 Rechnungsnr. · E-09 Rechnungsdatum · E-10 Leistungsdatum · E-11 Beträge · "
          "E-14 Belegart · E-15 Fälligkeit/Skonto · E-16 IBAN · E-17 Kontierung · E-20 § 13b\n"
          "**Bedingt:** E-03 Objekt-ID (objektbezogen) · E-12/E-13 Zahlbetrag/Kürzungsgrund · E-18/E-19/E-21/E-22 (Bau) · "
          "E-26 Rückweisungsgrund · E-30 Verwaltungsart (WF-03)",
          "task", extra=boxst)
    ks = [("K-02 Rechnungsanlage / Nachweis", "Lieferschein, Aufmaß, Abnahmeprotokoll, Stundenzettel", "E-01 · E-03 · E-27", "8 J.", "1"),
          ("K-03 Auftrag / Bestellung", "Auftrag, Auftragsbestätigung, Bestellung", "E-01 · E-03 · E-19 · E-27", "6 J.", "1"),
          ("K-04 Angebot", "Angebote, Angebotsvergleich", "E-01 · E-03 · E-27", "6 J.", "1"),
          ("K-05 Vertrag", "Verträge, Nachträge, Kündigungen (d.velop contracts)", "E-01 · E-03 · E-28", "ab Vertragsende", "4"),
          ("K-06 Bescheinigung", "FSB § 48b, Unbedenklichkeit, Versicherungsnachweise", "E-01 · E-05 · E-21 · E-27", "8 J. ab Gültigkeitsende", "1 (Automatik 3)"),
          ("K-07 Korrespondenz", "Briefe, E-Mails, Rückweisungs- und Kürzungsmails, PM-Freigabemails", "E-01 · E-27", "6 J.", "1 (Ablage auto. 2)"),
          ("K-08 BIM4You-Prüfbericht", "Prüfbericht, Zahlungsfreigabe, Einbehaltsnachweis", "E-01 · E-03 · E-05 · E-19", "8 J.", "3"),
          ("K-09 Sonstiges Posteingangsdokument", "Behörden, Steuer, Versicherung, Mieterpost", "E-01 · E-25 · E-27", "6 J.", "4"),
          ("K-15 Organisationsunterlage", "Verfahrensdoku, Arbeitsanweisungen, Stände Workflow/Freigabematrix, Lösch-/Rechteprotokolle", "E-01 · E-27 · E-29", "10 J.", "1")]
    for i, (t, d, e, ab, ph) in enumerate(ks):
        x = 55 + (i % 5) * 149
        y = 276 + (i // 5) * 164
        hl = f"fillColor={C['yellow_l']};" if t.startswith("K-15") else ""
        p.box(x, y, 142, 156, f"**{t}**\n{d}\n**Pflicht:** {e}\n**Aufbew.:** {ab}\n**Phase:** {ph}", "task", extra=TXT_TL + "fontSize=10;" + hl)
    p.box(55 + 4 * 149, 440, 142, 156,
          "**Neu: K-15** (Audit)\nAufbewahrung 10 Jahre ab E-29 (§ 147 Abs. 1 Nr. 1 AO, § 257 Abs. 1 Nr. 1 HGB). Gruppenweite Unterlagen: Mandant der verantwortenden Gesellschaft (Vorschlag Obergesellschaft).",
          "note", extra="fontSize=10;")
    # Aktenarten
    p.box(40, 620, 770, 200, "Aktenarten (A)", "group", extra="fontSize=13;")
    ak = [("K-10 Gesellschaftsakte", "alle Dokumente einer Gesellschaft", "E-01 · E-02"),
          ("K-11 Objektakte", "Dokumente je Objekt / Bauvorhaben", "E-01 · E-03 · E-04"),
          ("K-12 Kreditorenakte", "je Kreditor und Gesellschaft (inkl. FSB, Rahmenvertrag)", "E-01 · E-05 · E-06"),
          ("K-13 Vorgangsakte", "Auftrag / Vergabeeinheit: Auftrag, Abschläge, Schlussrechnung, Nachweise", "E-01 · E-03 · E-19"),
          ("K-14 Vertragsakte", "Vertrag, Nachträge, Korrespondenz (d.velop contracts)", "E-01 · E-28")]
    for i, (t, d, e) in enumerate(ak):
        p.box(55 + i * 149, 650, 142, 156, f"**{t}**\n{d}\n\n**Pflicht:**\n{e}", "task_d", extra=boxst)
    p.box(40, 836, 540, 150,
          "**Modellregeln**\n"
          "• E-01 Mandant ist in allen Kategorien Pflicht (P1).\n"
          "• Eine Eigenschaft je Fachbegriff; Demo-Struktur wird nicht übernommen (AE-29).\n"
          "• Status kommt aus smart invoice (E-24) – kein eigenes Statusfeld.\n"
          "• Wertemengen: Datasets aus BeSync (Mandant, Objekt); Wertelisten für Belegart, Kürzungs- und Rückweisungsgrund, "
          "Eingangskanal, § 13b (Ja/Nein).\n"
          "• Aufbewahrung je Kategorie ab E-29 (AE-24).",
          "info", extra="fontSize=11;")
    legend_box(p, 596, 836, [("task", "Dokumentart (D)"), ("task_d", "Aktenart (A)"),
                             (cell(C['green_l']), "Quelle über BeSync [A]")], "Legende", w=214)

    p.box(40, 1000, 770, 100,
          "**Wertelisten (Vorschlag, von Livos zu bestätigen)**\n"
          "**Rückweisungsgründe (E-26):** (1) Pflichtangaben § 14 UStG fehlen/fehlerhaft · (2) falscher Rechnungsempfänger/Gesellschaft · "
          "(3) Leistung nicht/nicht vollständig erbracht bzw. Nachweise fehlen · (4) Preis/Menge weicht von Auftrag/Vertrag ab · (5) formaler E-Rechnungsfehler\n"
          "**Kürzungsgründe (E-13):** Mengenabweichung · Preisabweichung · Mangel/Minderung · Einbehalt · Bauabzug 15 % (§ 48) · Skonto-/Nachlassdifferenz · Sonstiges (Freitext)",
          "note", extra="fontSize=10;")
    # Eigenschaftenkatalog
    p.box(838, 112, 776, 22, "Eigenschaftenkatalog E-01 … E-32", "h2")

    def cs(ri, ci, t):
        base = "#FFFFFF" if ri % 2 else C['grey_l']
        if ci == 0:
            return cell(base, 10, bold=True, color=C['navy'])
        if ci == 3 and "BeSync" in t:
            return cell(C['green_l'], 10)
        return None
    tbl(p, 838, 138, [48, 358, 96, 274], E_ROWS, rowh=29, hrow=26, fs=10, cellstyle=cs)


# =================================================================== 05 Aktenplan
def page05(doc):
    p = doc.page("05 Aktenplan", "p05")
    p.header("05 Aktenplan (AE-19)",
             "Gesellschaftsakte → Objektakte → Vorgangs-/Vertragsakte; Gesellschaftsakte → Kreditorenakte; K-07, K-09, K-15 direkt an der Gesellschaftsakte (S10). Beispiel mit Demo-Daten.")
    # Ebenen-Bänder
    bands = [(140, 100, "Ebene 1\nGesellschaft"), (260, 110, "Ebene 2\nObjekt / Kreditor"),
             (390, 190, "Ebene 3\nVorgang / Vertrag\nbzw. Dokument"), (600, 100, "Ebene 4\nDokument")]
    for i, (y, h, t) in enumerate(bands):
        p.box(40, y, 110, h, t, "lane_h", extra="horizontal=1;fontSize=11;")
        p.box(150, y, 860, h, "", "lane" if i % 2 == 0 else "lane_alt")

    ges = p.box(400, 155, 340, 70, "**K-10 Gesellschaftsakte**\nLivos Objektgesellschaft Nord mbH · Mandant 10010", "task_d")
    kre = p.box(170, 280, 300, 70, "**K-12 Kreditorenakte**\nMusterbau GmbH · 10010 / 70012", "task_d")
    obj = p.box(600, 280, 330, 70, "**K-11 Objektakte**\nBV Hafenstraße 22 · Objekt-ID 10010-0001", "task_d")
    lb = LBG + "fontSize=11;fontStyle=1;"
    p.edge(ges, kre, "S1", "tree", extra=lb)
    p.edge(ges, obj, "S2", "tree", extra=lb)
    org = p.box(488, 282, 100, 66, "**K-15**\nOrganisations-\nunterlage", "doc", extra="fontSize=10;")
    p.edge(ges, org, "S10", "tree", extra=lb)

    hi = f"fillColor={C['yellow_l']};strokeColor={C['orange']};strokeWidth=2;"
    fsb = p.box(160, 410, 130, 80, "**K-06 FSB § 48b**\ngültig bis 31.12.2026", "doc", extra="fontSize=10;")
    re1 = p.box(305, 410, 170, 80, "**K-01 RE-2026-1041**\n14.756,00 €", "doc", extra=hi + "fontSize=11;")
    re2 = p.box(500, 410, 170, 80, "**K-01 RE-2026-1041**\n14.756,00 €", "doc", extra=hi + "fontSize=11;")
    vg = p.box(690, 410, 150, 80, "**K-13 Vorgangsakte**\nA-2026-0815 · Rohbau Los 3", "task_d", extra="fontSize=11;")
    vt = p.box(855, 410, 145, 80, "**K-14 Vertragsakte**\nGU-Vertrag (Beispiel)", "task_d", extra="fontSize=11;")
    p.edge(kre, fsb, "S6", "tree", extra=lb, exit=(0.2, 1))
    p.edge(kre, re1, "S3", "tree", extra=lb, exit=(0.7, 1))
    p.edge(obj, re2, "S4", "tree", extra=lb, exit=(0.15, 1))
    p.edge(obj, vg, "S7", "tree", extra=lb, exit=(0.45, 1))
    p.edge(obj, vt, "S5", "tree", extra=lb, exit=(0.85, 1))
    re3 = p.box(600, 620, 140, 70, "**K-01 RE-2026-1041**\n14.756,00 €", "doc", extra=hi + "fontSize=10;")
    d1 = p.box(750, 620, 120, 70, "**K-03** AB A-2026-0815\n**K-02** Aufmaß", "doc", extra="fontSize=10;")
    d2 = p.box(880, 620, 120, 70, "**K-05 Vertrag**\n+ Nachträge", "doc", extra="fontSize=10;")
    p.edge(vg, re3, "S8", "tree", extra=lb, exit=(0.3, 1))
    p.edge(vg, d1, "S8", "tree", extra=lb, exit=(0.7, 1))
    p.edge(vt, d2, "S5", "tree", extra=lb)
    ho = f"strokeColor={C['orange']};strokeWidth=2;dashed=1;startArrow=open;endArrow=open;"
    p.edge(re1, re2, "", "assoc", extra=ho, exit=(1, 0.5), entry=(0, 0.5))
    p.edge(re2, re3, "", "assoc", extra=ho + "edgeStyle=orthogonalEdgeStyle;", exit=(0.5, 0.9), entry=(0, 0.5), points=[(585, 655)])
    p.box(160, 520, 420, 170,
          "**Mehrfachablage:** ein Original RE-2026-1041 (Musterbau GmbH, 14.756,00 €), drei Fundorte – keine Kopie:\n"
          "• Kreditorenakte Musterbau GmbH (S3)\n• Objektakte BV Hafenstraße 22 (S4)\n• Vorgangsakte A-2026-0815 (S8, nur wenn E-19 gefüllt)\n\n"
          "Beispielwerte fiktiv (Demo-Testdaten).",
          "text", extra=f"fontSize=11;fillColor={C['yellow_l']};strokeColor={C['orange']};spacingLeft=8;spacingTop=6;")

    # rechts: Grundsätze
    p.box(1040, 128, 574, 26, "Grundsätze", "h2")
    p.box(1040, 160, 574, 180,
          "• **Mandant in jeder Erkennungskombination** – Kreditor- und Objektnummern kollidieren je Gesellschaft.\n"
          "• **Maximal 4 Ebenen** (Workshop-Empfehlung 4–5).\n"
          "• **Erkennungsfelder sind Pflicht** – leere Felder ergeben keine Aktenverknüpfung (Verhalten in der Cloud testen, OP-08).\n"
          "• **Akten sind eigene Kategorien** mit eigenen Permissions nach demselben Muster (RS_Mandant).\n"
          "• **Mehrfachablage** über eine zweite Regel für dasselbe Dokument (Test T13).\n"
          "• smart-invoice-„Kreditorenvorgangsakte“ wiederverwenden oder bewusst ersetzen.\n"
          "• Livos liefert die fachliche Ordnerstruktur (OP-17).",
          "info", extra="fontSize=12;spacing=10;")
    p.box(1040, 360, 574, 26, "Gesellschaftsübergreifende Lieferantensicht", "h2")
    srch = p.box(1040, 392, 280, 110, "**Gespeicherte Suche „Lieferant L-000123“**\nE-07 Konsolidierungsnummer = L-000123", "dvelop_l",
                 extra="fontSize=11;")
    res = p.box(1350, 392, 264, 110, "Alle Dokumente der Musterbau GmbH in allen Gesellschaften, für die der Benutzer berechtigt ist\n(keine eigene Akte)", "task",
                extra="fontSize=11;")
    p.edge(srch, res, "", "flow")
    p.box(1040, 506, 574, 30, "Gespeicherte Suchen und Akten respektieren die Rechte (RS_Mandant) – Nutzer sehen nur ihre Gesellschaften.",
          "small", extra="fontSize=10;")

    p.box(1040, 548, 574, 26, "Beispiel Bau-Rechnung (Vorgangsakte)", "h2")
    p.box(1040, 580, 574, 110,
          "Die Rechnung RE-2026-1041 trägt die Auftragsnummer A-2026-0815 (E-19). Regel S8 verknüpft sie zusätzlich mit der "
          "Vorgangsakte „A-2026-0815 · Rohbau Los 3“ – zusammen mit Auftragsbestätigung und Aufmaß. So entsteht die Sicht "
          "Auftrag → Abschläge → Schlussrechnung für die VOB-Kumulation (Prüfung in BIM4You, WF-02).",
          "task_d", extra=TXT_TL + "fontSize=11;")
    # Tabelle Regeln
    p.box(40, 712, 1574, 26, "Aktenbildungsregeln S1 – S10 (Strukturregeln; S1–S6 Kern, S7–S10 Ergänzung – nicht zu verwechseln mit Schnittstellen S-xx)", "h2")
    rows = [["Regel", "Übergeordnet → untergeordnet", "Erkennung", "Vererbung (von oben nach unten)", "Status"],
            ["S1", "K-10 Gesellschaftsakte → K-12 Kreditorenakte", "E-01", "E-02, E-31", "[K]"],
            ["S2", "K-10 Gesellschaftsakte → K-11 Objektakte", "E-01", "E-02, E-31", "[K]"],
            ["S3", "K-12 Kreditorenakte → K-01 Eingangsrechnung", "E-01 + E-05", "E-06, E-07", "[K]"],
            ["S4", "K-11 Objektakte → K-01 Eingangsrechnung", "E-01 + E-03", "E-04, E-30", "[K]; zweite Regel für dieselbe Dokumentart – Mehrfachablage testen (OP-08)"],
            ["S5", "K-11 Objektakte → K-14 Vertragsakte → K-05 Vertrag", "E-01 + E-03 bzw. Vertrags-ID", "E-04; Vertragsdaten (E-28) von K-14 an K-05", "[K]; Muster d.velop contracts"],
            ["S6", "K-12 Kreditorenakte → K-06 Bescheinigung", "E-01 + E-05", "E-06, E-07", "[K]"],
            ["S7", "K-11 Objektakte → K-13 Vorgangsakte", "E-01 + E-03", "E-04", "[K] (Ergänzung)"],
            ["S8", "K-13 Vorgangsakte → K-01, K-02, K-03, K-08", "E-01 + E-03 + E-19", "E-18", "[K] (Ergänzung); nur wenn E-19 gefüllt"],
            ["S9", "K-12 Kreditorenakte → K-02, K-03, K-04, K-07, K-08", "E-01 + E-05", "E-06, E-07", "[K] (Ergänzung)"],
            ["S10", "K-10 Gesellschaftsakte → K-07, K-09, K-15", "E-01", "E-02", "[K] (Ergänzung); K-15 Organisationsunterlage (10 Jahre)"]]

    def cs(ri, ci, t):
        base = "#FFFFFF" if ri % 2 else C['grey_l']
        if ci == 0:
            return cell(base, 11, align="center", bold=True, color=C['navy'])
        if ri == 4:
            return cell(C['yellow_l'], 11)
        return cell(base, 11)
    tbl(p, 40, 742, [70, 420, 250, 380, 454], rows, rowh=30, hrow=28, fs=11, cellstyle=cs)
    p.box(40, 1072, 1574, 36,
          "Erkennungsfelder sind Pflicht; ohne Wert entsteht keine Verknüpfung. Rechte je Akte nach dem Muster der Seite 03 (RS_Mandant / RS_Objekt).",
          "small", extra="fontSize=11;")


# =================================================================== 06 Lieferanten / Kreditoren
def page06(doc):
    p = doc.page("06 Lieferanten- und Kreditorenmodell", "p06")
    p.header("06 Lieferanten- und Kreditorenmodell (AE-09)",
             "Drei Nummernkreise, ein führendes System je Datenobjekt (P4). Lieferanten-App führt die Identität, DATEV führt die Kreditorenkonten.")
    p.box(40, 112, 1060, 26, "Drei Nummernkreise", "h2")
    nk = [("mdis", "① Lieferanten-Konsolidierungsnummer",
           "**führend:** Lieferanten-App (MDIS BeSync)\n**gilt:** gesellschaftsübergreifend – ein Lieferant = eine Nummer\n"
           "**im DMS:** Eigenschaft E-07 an der Kreditorenakte, vererbt an die Dokumente (nicht im Bucket)\n"
           "**Zweck:** Lieferantensicht über alle Gesellschaften, BI, KI-Konsolidierung"),
          ("ext", "② DATEV-Kreditorennummer je Mandant",
           "**führend:** DATEV (Anlage durch Trios)\n**Kreis:** 70000er, je Gesellschaft verschieden\n"
           "**im DMS:** smart-invoice-Bucket über LDconnect (S-02, täglich), Eigenschaft E-05\n"
           "**Zweck:** Buchung, Kreditorenakte (Mandant + Kreditor-Nr)"),
          ("ext", "③ HV-Kreditorennummer",
           "**Herkunft:** Buchhaltungen der Property Manager\n**Kreis:** 80000er\n"
           "**im DMS:** nicht im Bucket; nur Abgleich über BeSync / BI (S-16, optional Phase 3)\n"
           "**Zweck:** Vollständigkeits- und Kreditorenabgleich PM-verwalteter Objekte")]
    for i, (st, t, d) in enumerate(nk):
        x = 40 + i * 358
        p.box(x, 146, 344, 40, t, st, extra="fontSize=13;")
        p.box(x, 186, 344, 130, d, "text",
              extra=f"strokeColor={C['green'] if st == 'mdis' else C['grey']};fillColor=#FFFFFF;fontSize=11;spacingLeft=8;spacingTop=6;")

    p.box(1130, 112, 484, 26, "Regeln", "h2")
    p.box(1130, 146, 484, 118,
          "**DATEV-Stammdaten schreibt nur LDconnect** – je Objekttyp im Bucket genau ein schreibendes System (AE-09, Kap. 8.7).\n"
          "BeSync schreibt nur smart-invoice-Mandanten und Custom Entities (BIM4You) und setzt die Konsolidierungsnummer als DMS-Eigenschaft E-07 (Kreditorenakte → Dokumente).\n"
          "Option B (offen): BeSync schreibt den Bucket, LDconnect nur Buchung.",
          "warn", extra="fontSize=10;")
    p.box(1130, 270, 484, 50,
          "Livos legt keine DATEV-Kreditoren an; Trios bucht und legt an. Initiale Konsolidierung per KI-Mapping (MDIS X.One, PoC).",
          "info", extra="fontSize=11;")

    p.box(40, 330, 1260, 26, "Mapping-Beispiel in der Lieferanten-App (fiktiv)", "h2")
    rows = [["Konsolidierungsnr.", "Lieferant", "Mandant (Gesellschaft)", "Kreditor-Nr", "Kreis", "Quelle", "Status"],
            ["L-000123", "Musterbau GmbH", "10010 · Livos Objektgesellschaft Nord mbH", "70012", "intern", "DATEV", "bestätigt"],
            ["L-000123", "Musterbau GmbH", "10020 · Livos Objektgesellschaft Süd mbH", "70388", "intern", "DATEV", "bestätigt"],
            ["L-000123", "Musterbau GmbH", "10020 · Livos Objektgesellschaft Süd mbH", "80417", "HV", "PM-Buchhaltung", "KI-Vorschlag, offen"],
            ["L-000124", "Elektro Nordlicht GmbH", "10010 · Livos Objektgesellschaft Nord mbH", "70044", "intern", "DATEV", "bestätigt"],
            ["L-000124", "Elektro Nordlicht GmbH", "10030 · Livos Bau & Projekt GmbH", "70102", "intern", "DATEV", "bestätigt"],
            ["(neu)", "Recht & Partner mbB", "10030 · Livos Bau & Projekt GmbH", "–", "–", "Klärfall „Kreditor fehlt“", "Anlage angefordert"]]

    def cs(ri, ci, t):
        base = "#FFFFFF" if ri % 2 else C['grey_l']
        if ci == 0:
            return cell(C['green_l'], 11, bold=True)
        if ci in (3, 4):
            return cell(base, 11, align="center")
        if ci == 6 and t != "bestätigt":
            return cell(C['yellow_l'], 11)
        return cell(base, 11)
    tbl(p, 40, 360, [150, 200, 330, 120, 90, 200, 170], rows, rowh=26, hrow=26, fs=11, cellstyle=cs)
    p.box(1330, 360, 284, 182,
          "**Schlüssel:** DATEV-Mandantennr + Kreditorennr (Vorschlag Trios).\n\n"
          "Jeder Schlüssel hat genau eine Konsolidierungsnummer; eine Konsolidierungsnummer hat beliebig viele Kreditorennummern.",
          "note", extra="fontSize=11;")

    # Prozess Neuanlage
    p.box(40, 560, 1574, 26, "Neuanlage Kreditor (WF-04, Klärfall „Kreditor fehlt“)", "h2")
    from dio import lanes
    L = lanes(p, 40, 592, 1574, [("Rechnungs-\neingang (R-02)", 120), ("Lieferanten-\nApp (R-12)", 120),
                                ("Trios / DATEV\n(R-06)", 120), ("LDconnect\n(S-02)", 120)], head_w=60)
    y1, y2, y3, y4 = [L[k][1] for k in L]
    st = p.box(205, y1 - 18, 36, 36, "", "start")
    p.box(178, y1 + 20, 90, 30, "Beleg ohne Kreditor", "small", extra="align=center;fontSize=9;")
    t1 = p.box(280, y1 - 30, 170, 60, "Klärfall „Kreditor fehlt“\n(WF-04, M-05)", "task_d")
    t2 = p.box(480, y2 - 30, 180, 60, "Treffer prüfen, Lieferant\nbestätigen oder neu anlegen", "task_mdis")
    t3 = p.box(690, y2 - 30, 170, 60, "Anlage-Anforderung an Trios\n(S-05: Ph. 1 E-Mail,\nPh. 2 automatisiert)", "task_mdis", extra="fontSize=11;")
    t4 = p.box(900, y3 - 30, 180, 60, "Kreditor in DATEV anlegen,\nBankverbindung 4-Augen", "task_ext")
    t5 = p.box(1110, y4 - 30, 190, 60, "Stammdaten-Abgleich täglich\n→ Bucket (Folgetag, S-02)", "auto")
    t6 = p.box(1110, y2 - 30, 190, 60, "Mapping: Konsolidierungsnr. ↔\nMandant + Kreditor-Nr (S-05)", "task_mdis", extra="fontSize=11;")
    t7 = p.box(1340, y1 - 30, 170, 60, "Kreditor zuordnen –\nweiter zur sachl. Prüfung", "task_d")
    en = p.box(1545, y1 - 18, 36, 36, "", "end")
    p.box(1520, y1 + 20, 90, 30, "weiter in WF-01", "small", extra="align=center;fontSize=9;")
    p.edge(st, t1, "", "flow")
    p.edge(t1, t2, "", "flow", exit=(1, 0.5), entry=(0.5, 0))
    p.edge(t2, t3, "", "flow")
    p.edge(t3, t4, "Mail / Workflow", "msg", exit=(0.5, 1), entry=(0, 0.5), extra=LBG)
    p.edge(t4, t5, "", "flow", exit=(1, 0.5), entry=(0.5, 0))
    p.edge(t4, t6, "DATEVconnect lesen", "data", exit=(0.5, 0), entry=(0, 0.5), extra=LBG)
    p.edge(t5, t7, "", "flow", exit=(1, 0.5), entry=(0.75, 1))
    p.edge(t6, t7, "E-07 am Beleg", "data", exit=(1, 0.5), entry=(0.2, 1), extra=LBG)
    p.edge(t7, en, "", "flow")
    p.box(640, y1 - 40, 440, 70,
          "Durchlauf realistisch 1–3 Arbeitstage bis zur Kreditorzuordnung. Die sachliche Prüfung kann parallel beginnen; "
          "die DATEV-Übergabe ist erst nach dem Abgleich möglich. Skonto-kritische Belege priorisieren.",
          "note", extra="fontSize=10;")
    inline_legend(p, 40, 1086, [("task_d", "d.velop Konfiguration"), ("task_mdis", "MDIS BeSync (Anpassung)"),
                                ("task_ext", "Umsystem / extern"), ("auto", "automatisch (Drittanbieter-Option)")], colw=260)


# =================================================================== 07 Prozesslandkarte
def page07(doc):
    p = doc.page("07 Prozesslandkarte", "p07")
    p.header("07 Prozesslandkarte (WF-01 … WF-10)",
             "Kern- und unterstützende Prozesse mit Werkzeug und Einführungsphase (P8: Rechnungseingang zuerst, dann PM-Freigabe, Bau/BIM4You, Verträge, Post).")
    # Steuerung
    p.box(40, 112, 1574, 80, "Führung & Steuerung", "group_g", extra="fontSize=12;")
    for i, (t, link) in enumerate([("Freigabematrix & Wertgrenzen (M-17) → Seite 11", "p11"),
                                   ("Eskalation & Vertretung (AE-17) → Seite 12", "p12"),
                                   ("Statusmodell Rechnung (E-24) → Seite 14", "p14"),
                                   ("REB (M-09) & Reporting evidanza (S-12) → Seite 21", "p21")]):
        p.box(230 + i * 345, 132, 325, 44, t, "dvelop_l", link=f"data:page/id,{link}",
              extra="fontSize=11;fontStyle=1;fontColor=%s;" % C['teal'])

    # Kernprozesse
    p.box(40, 206, 1574, 500, "Kernprozesse", "group_t", extra="opacity=100;fillColor=#EEF7F8;")
    stp = "shape=step;perimeter=stepPerimeter;fixedSize=1;size=14;whiteSpace=wrap;html=1;fontSize=10;"
    SD = stp + f"fillColor={C['teal_l']};strokeColor={C['teal']};"
    SM = stp + f"fillColor={C['green_l']};strokeColor={C['green']};"
    SE = stp + f"fillColor={C['grey_l']};strokeColor={C['grey']};"
    core = [("WF-01 Standard-Eingangsrechnung", "smart invoice", "1",
             [("Eingang &\nErkennung", SD), ("Verteilung\n(Mandant, Kreditor)", SD), ("Sachl. Prüfung\n& Kontierung", SD),
              ("Fachl. Freigabe\n1..n (Matrix)", SD), ("Zahlungs-\nfreigabe", SD), ("Buchhaltung →\nDATEV (S-01)", SD)],
             "Prozess → Seite 08\nKap. 9, 10", "p08"),
            ("WF-02 Bau-Eingangsrechnung", "smart invoice + BeSync", "3",
             [("Eingang &\nErkennung (Bau)", SD), ("Verteilung", SD), ("Sachl. Prüfung", SD),
              ("BIM4You-Prüfung\n(S-08 / S-09) [A]", SM), ("Fachl. Freigabe &\nZahlungsfreigabe", SD), ("Buchhaltung →\nDATEV (S-01)", SD)],
             "Prozess → Seite 10\nKap. 9 · Pilot ohne Automatik in Ph. 1", "p10"),
            ("WF-03 PM-Freigabe", "smart invoice + BeSync", "2",
             [("Eingang\nfreigabe-hv@…", SD), ("Verteilung (Objekt,\nGesellschaft, PM)", SD), ("Freigabe Asset\nManagement (Matrix)", SD),
              ("Ende: freigegeben\n/ abgelehnt", SD), ("Rückmeldung\nan PM (S-11) [A]", SM)],
             "Prozess → Seite 15\nKap. 11 · keine Buchung/Zahlung", "p15"),
            ("WF-06 Vertragsprozess", "d.velop contracts + process studio", "4",
             [("Eingang", SD), ("Verarbeitung", SD), ("Verteilung", SD), ("Klassifizierung", SD),
              ("Fachliche\nFreigabe", SD), ("Archivierung &\nFristen", SD)],
             "Prozess → Seite 16\nKap. 12", "p16"),
            ("WF-07 Postverteilung", "inbound + KI + mail dispatcher", "4",
             [("Eingang\n(Scan, E-Mail)", SD), ("Verarbeitung\n(KI-Trennung)", SD), ("Klassifizierung\n(KI)", SD),
              ("Verteilung\n(mail dispatcher)", SD), ("Archivierung\nin Akten", SD)],
             "Prozess → Seite 17\nKap. 12", "p17")]
    for r, (name, tool, ph, steps, ref, link) in enumerate(core):
        y = 240 + r * 92
        p.box(56, y, 250, 78, f"**{name}**\nWerkzeug: {tool}", "dvelop", link=f"data:page/id,{link}" if link else None,
              extra="fontStyle=0;align=left;spacingLeft=8;fontSize=11;")
        phase_badge(p, 316, y + 28, ph, w=84)
        for i, (t, sst) in enumerate(steps):
            p.box(412 + i * 164, y + 9, 172, 60, t, sst)
        p.box(1420, y + 9, 180, 60, ref, "ui_btn2" if link else "text",
              link=f"data:page/id,{link}" if link else None,
              extra="fontSize=10;fontStyle=0;" + ("" if link else f"strokeColor={C['grey_m']};fillColor=#FFFFFF;align=center;verticalAlign=middle;"))

    # Unterstützende Prozesse
    p.box(40, 720, 1574, 250, "Unterstützende Prozesse", "group_g", extra="fontSize=12;")
    sup = [("WF-04 Klärfall", "Mandant / Kreditor unbekannt, Clearing je Mandant, Kreditor-Anlage via Lieferanten-App / Trios",
            "smart invoice (+ Lieferanten-App)", "1", "Prozess → Seite 09", "p09"),
           ("WF-05 Rückweisung / Kürzung", "Ablehnen mit Pflichtgrund, Vorlagen-Mail an Lieferanten (S-11), Ablage Korrespondenz",
            "smart invoice + BeSync", "2", "Sonderfälle → Seite 13", "p13"),
           ("WF-08 Aufgaben / Wiedervorlagen", "Ad-hoc-Aufgaben und Wiedervorlagen am Dokument",
            "d.velop documents", "1", "alle Kategorien · Kap. 12", None),
           ("WF-09 Weitere Freigaben", "Freigaben ohne Rechnung, z.B. Ausbuchungen auf Mietkonten (Ausblick)",
            "process studio", "5", "Kap. 11", None),
           ("WF-10 Externe Ad-hoc-Freigabe", "externe Benutzeraufgabe per E-Mail-Link, Beleg als befristeter Teilen-Link; nur Stellungnahme – verbindliche Freigabe intern (R-03/R-04)",
            "process studio + BeSync", "3", "Maske M-19 → Seite 41", "p41")]
    for i, (t, d, tool, ph, ref, link) in enumerate(sup):
        x = 56 + i * 311
        st = "task_mdis" if "BeSync" in tool else "task_d"
        p.box(x, 752, 296, 200, f"**{t}**\n{d}\n\n**Werkzeug:** {tool}", st, extra=TXT_TL + "fontSize=11;")
        phase_badge(p, x + 8, 918, ph, w=76)
        p.box(x + 92, 914, 196, 30, ref, "ui_btn2" if link else "text", link=f"data:page/id,{link}" if link else None,
              extra="fontSize=10;fontStyle=0;" + ("" if link else "align=left;verticalAlign=middle;fontColor=%s;" % C['grey']))

    # Basis
    p.box(40, 984, 1574, 76, "Basis", "group_g", extra="fontSize=12;")
    for i, (t, link) in enumerate([("Akten, Suche, Aufbewahrung – Seite 05", "p05"),
                                   ("Stammdaten Lieferanten / Kreditoren – Seite 06", "p06"),
                                   ("Mandanten, Gruppen, Rechte – Seite 03", "p03"),
                                   ("Schnittstellen S-01 … S-17 – Seite 02", "p02")]):
        p.box(130 + i * 370, 1006, 350, 40, t, "ui_btn2", link=f"data:page/id,{link}")
    inline_legend(p, 40, 1072, [(SD.replace(stp, ""), "d.velop Standard / Konfiguration"), (SM.replace(stp, ""), "MDIS BeSync (Anpassung)"),
                                ("task_d", "unterstützender Prozess (d.velop)"), ("task_mdis", "unterstützend mit BeSync")], colw=300)
    for i, ph in enumerate(["1", "2", "3", "4", "5"]):
        phase_badge(p, 1250 + i * 74, 1072, ph, w=68, h=20)


def build(doc):
    page01(doc)
    page02(doc)
    page03(doc)
    page04(doc)
    page05(doc)
    page06(doc)
    page07(doc)
