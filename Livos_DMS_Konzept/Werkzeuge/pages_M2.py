"""Masken-Mockups M-11 bis M-19 (Seiten p33–p41) des draw.io-Konzeptdiagramms.
Spezifikation: Kapitel 14 (K14_masken.md, Abschnitte 14.0, 14.11–14.19). Aufruf: build(doc)."""
from math import ceil
from dio import C, S, ui_window, ui_viewer, legend_box

# Raster: Maskenfenster links, Erläuterungsspalte rechts
WX, WY, WW = 40, 112, 1190
RX, RW = 1250, 364

STATUS = {"S": ("dvelop", "[S] Standard"), "K": ("dvelop_l", "[K] Konfiguration"),
          "A": ("mdis", "[A] Anpassung BeSync"), "O": ("open", "[O] offen")}
KIND = {"input": "ui_input", "req": "ui_req", "ro": "ui_ro", "ai": "ui_ai", "select": "ui_input"}


# ---------------------------------------------------------------- Hilfsfunktionen
def est_h(text, w, fs=10):
    """grobe Höhe eines umbrechenden Textes (Helvetica)."""
    cpl = max(8, int((w - 12) / (fs * 0.47)))
    n = sum(max(1, ceil(len(seg) / cpl)) for seg in text.replace("**", "").split("\n"))
    return n * (fs + 4) + 10


def mk(p, x, y, n):
    """Annotationsmarker (orange Kreis) im Mockup."""
    p.box(x, y, 20, 20, str(n), "ann", extra="fontSize=10;")


def notes(p, x, y, w, items, title="Erläuterungen", fs=10):
    if title:
        p.box(x, y, w, 24, title, "h2")
        y += 30
    for n, t in items:
        mk(p, x, y, n)
        h = est_h(t, w - 30, fs)
        p.box(x + 28, y - 4, w - 28, h, t, "text", extra=f"fontSize={fs};")
        y += max(24, h) + 5
    return y


def card(p, x, y, w, title, body, st="info", fs=11, h=None):
    txt = f"**{title}**\n{body}" if title else body
    hh = h or est_h(txt, w - 14, fs) + 6
    p.box(x, y, w, hh, txt, st, extra=f"fontSize={fs};")
    return y + hh


def chips(p, x, y, codes, label="Umsetzung"):
    p.box(x, y, 80, 22, label, "text", extra="fontSize=11;fontStyle=1;verticalAlign=middle;fontColor=%s;" % C['navy'])
    cx = x + 82
    for c in codes:
        st, t = STATUS[c]
        w = int(6.0 * len(t) + 14)
        if cx + w > RX + RW:
            cx, y = x + 82, y + 26
        p.box(cx, y + 1, w, 20, t, st, extra="fontSize=10;")
        cx += w + 6
    return y + 32


def field_legend(p, x, y, w=RW):
    return legend_box(p, x, y, [
        ("ui_req", "Pflichtfeld, schreibbar (req) – Bezeichnung mit *"),
        ("ui_ai", "erkannt / vorbelegt (ai: KI, E-Rechnung, System) – prüfen"),
        ("ui_ro", "schreibgeschützt / berechnet (ro)"),
        ("ui_input", "frei editierbar (input)"),
        ("ui_input", "Auswahl / Werteliste (select), erkennbar an ▾"),
        ("ann", "Annotation – Erläuterung in der Randspalte")], "Legende Feldarten", w)


def fld(p, x, y, w, label, value="", kind="input", h=24, n=None, star=False):
    """Feld wie dio.ui_field, zusätzlich mehrzeilig und mit Marker."""
    lab = label + (" *" if (kind == "req" or star) else "")
    p.box(x, y, w, 14, lab, "ui_label")
    val = value + ("   ▾" if kind == "select" else "")
    extra = "verticalAlign=top;spacingTop=3;" if h > 30 else ""
    if kind == "select":
        extra += "fontColor=%s;" % C['black']
    p.box(x, y + 14, w, h, val, KIND[kind], extra=extra)
    if n is not None:
        mk(p, x + w - 12, y + 4, n)
    return y + 14 + h + 8


def frow(p, x, y, w, fields, gap=12):
    """Feldzeile. fields = [(label, value, kind, {wt, n, h, star})]."""
    wts = [(f[3] if len(f) > 3 else {}).get("wt", 1) for f in fields]
    avail = w - gap * (len(fields) - 1)
    cx, ye = x, y
    for f, wt in zip(fields, wts):
        o = f[3] if len(f) > 3 else {}
        fw = avail * wt / sum(wts)
        ye = max(ye, fld(p, cx, y, fw, f[0], f[1], f[2], o.get("h", 24), o.get("n"), o.get("star", False)))
        cx += fw + gap
    return ye


def sec(p, x, y, w, title, n=None):
    p.box(x, y, w, 20, title, "ui_sec")
    p.line(x, y + 21, x + w, y + 21, "line")
    if n is not None:
        mk(p, x + w - 20, y - 2, n)
    return y + 28


def tabs(p, x, y, labels, active=0, fs=10, h=24, w=None):
    cx = x
    for i, t in enumerate(labels):
        tw = w or int(6.4 * len(t) + 22)
        p.box(cx, y, tw, h, t, "ui_tab_a" if i == active else "ui_tab", extra=f"fontSize={fs};")
        cx += tw
    return y + h


def bw(t, fs):
    return int(fs * 0.62 * len(t) + 24)


def btns(p, x, y, items, fs=11, h=28, gap=8):
    cx = x
    for t, st in items:
        w = bw(t, fs)
        p.box(cx, y, w, h, t, st, extra=f"fontSize={fs};")
        cx += w + gap
    return cx


def btns_r(p, xr, y, items, fs=11, h=28, gap=8):
    tot = sum(bw(t, fs) for t, _ in items) + gap * (len(items) - 1)
    btns(p, xr - tot, y, items, fs, h, gap)
    return xr - tot


def tbl(p, x, y, colw, rows, rowh=26, fs=10, hl=(), hdr=True, cell=None, hh=None, hmap=None):
    """Tabelle in Masken. hl = markierte Zeilen, cell(ri, ci) -> Zusatzstil."""
    cy = y
    for ri, row in enumerate(rows):
        rh = (hh or rowh) if (hdr and ri == 0) else (hmap or {}).get(ri, rowh)
        cx = x
        for ci, v in enumerate(row):
            if hdr and ri == 0:
                st, ex = "th", f"fontSize={fs};"
            else:
                st = "td_alt" if ri % 2 == 0 else "td"
                ex = f"fontSize={fs};"
                if ri in hl:
                    ex += "fillColor=%s;" % C['teal_l']
                if cell:
                    ex += cell(ri, ci) or ""
            p.box(cx, cy, colw[ci], rh, v, st, extra=ex)
            cx += colw[ci]
        cy += rh
    return cy


def frame(doc, pid, name, sub, codes):
    p = doc.page(name, pid)
    p.header(name, sub)
    return p, chips(p, RX, WY, codes)


def pill(p, x, y, t, fill, stroke, w=None, fs=10, fc=None):
    w = w or int(6.2 * len(t) + 18)
    p.box(x, y, w, 20, t, "rounded=1;arcSize=50;fillColor=%s;strokeColor=%s;fontSize=%d;fontStyle=1;fontColor=%s;"
          % (fill, stroke, fs, fc or C['navy']))
    return x + w


DV_NAV = ["Start", "Aufgaben (7)", "Rechnungseingangsbuch", "Suche", "Akten", "Verträge", "Postkorb"]


# ================================================================ M-11
def page33(doc):
    p, ny = frame(doc, "p33", "M-11 Aktenansicht",
                  "Kreditorenakte (K-12) / Objektakte (K-11) · Rolle: alle mit Leserecht (Kapitel 13.4) · Werkzeug: d.velop documents – Akte "
                  "aus Suche, aus Dokument („In Akte anzeigen\") oder als Favorit · Umsetzung: [S] Akte, [K] Aktenarten K-10 bis K-14, Strukturregeln",
                  "SK")
    ui_window(p, WX, WY, WW, 690, "Akten › Kreditorenakte",
              crumbs="Start › Suche › Kreditorenakte 10010 / 70012 · Musterbau GmbH", user="Jana K. (Asset Management)")
    x0, y = 52, 180
    p.box(x0, y, 700, 28, "📁  Musterbau GmbH  ·  Kreditorenakte 10010 / 70012", "text",
          extra="fontSize=16;fontStyle=1;fontColor=%s;verticalAlign=middle;" % C['navy'])
    pill(p, 770, y + 4, "Aktenart K-12 Kreditorenakte", C['teal_l'], C['teal'])
    mk(p, 740, y + 4, 1)
    y = frow(p, x0, y + 34, 1166, [
        ("Mandant", "10010", "ro", {"wt": .55}),
        ("Mandantenname", "Livos Objektgesellschaft Nord mbH", "ro", {"wt": 1.55}),
        ("Kreditor-Nr (DATEV)", "70012", "ro", {"wt": .75}),
        ("Kreditorname", "Musterbau GmbH", "ro", {"wt": 1}),
        ("Lieferanten-Konsolidierungsnummer", "LK-000482  ·  ↗ alle Gesellschaften", "ro", {"wt": 1.5, "n": 2}),
        ("FSB gültig bis / FSB-Status", "31.12.2027 · gültig", "ro", {"wt": 1, "n": 3}),
    ])
    # Aktionsleiste
    btns(p, x0, y, [("⬆ Ablegen", "ui_btn"), ("Öffnen", "ui_btn2"), ("In Akte anzeigen", "ui_btn2"),
                    ("Verknüpfen / Lösen", "ui_btn2"), ("Eigenschaften exportieren (Excel/CSV)", "ui_btn2"),
                    ("☆ Beobachten", "ui_btn2"), ("★ Favorisieren", "ui_btn2"), ("＋ Aufgabe zur Akte", "ui_btn2")],
         fs=10, h=24, gap=6)
    mk(p, 1196, y + 2, 9)
    y += 36
    # Aktenbaum
    tx, tw = x0, 226
    yl, gr = "fillColor=%s;" % C['yellow_l'], "fillColor=%s;fontColor=%s;" % (C['grey_l'], C['grey'])
    nb = " " * 4
    tree = [["Aktenbaum"], ["▾ 📁 70012 Musterbau GmbH"],
            [nb + "📂 Eingangsrechnungen (3)"], [nb + "📂 Verträge (1)"], [nb + "📂 Bescheinigungen (1)"],
            [nb + "📂 Korrespondenz (1)"], [nb + "📂 Aufträge (1)"], [nb + "📁 Nachweise (0)"], [nb + "📁 Angebote (0)"]]
    ye = tbl(p, tx, y, [tw], tree, rowh=28, fs=11,
             cell=lambda ri, ci: "fontStyle=1;" if ri == 1 else (yl if ri <= 6 else gr))
    p.box(tx, ye + 4, tw, 34, "gelb = Unterakte mit Inhalt · grau = leer; Unterakten entstehen automatisch", "small")
    mk(p, tx + tw - 22, y + 3, 4)
    # Akteninhalt
    cx0, cw = tx + tw + 12, 596
    colw = [96, 132, 70, 78, 64, 58, 48, 50]
    rows = [["Kategorie", "Titel", "Rechnungs-/ Dok.-datum", "Kreditor / Absender", "Brutto €", "Workflow (E-24)", "Zahlst. (E-23)", "Status"],
            ["K-01 Eingangs- rechnung", "RE-2026-1041 Rohbauarbeiten", "15.09.2026", "Musterbau GmbH", "14.756,00", "Sachl. Prüfung", "offen", "Bearb."],
            ["K-01 Eingangs- rechnung", "RE-2026-0987 Abschlag 3", "18.08.2026", "Musterbau GmbH", "35.700,00", "abge- schlossen", "bezahlt", "Archiv"],
            ["K-01 Eingangs- rechnung", "RE-2026-0911 Abschlag 2", "21.07.2026", "Musterbau GmbH", "35.700,00", "abge- schlossen", "bezahlt", "Archiv"],
            ["K-05 Vertrag", "Rahmenvertrag Musterbau 2026", "02.01.2026", "Musterbau GmbH", "–", "–", "–", "Freigabe"],
            ["K-06 Bescheinigung", "Freistellungs- bescheinigung § 48b", "10.01.2026", "Finanzamt Hamburg", "–", "–", "–", "Freigabe"],
            ["K-07 Korrespondenz", "Nachtragsangebot N-03 Hafenstraße 22", "03.09.2026", "Musterbau GmbH", "–", "–", "–", "Freigabe"],
            ["K-03 Auftrag", "Auftrag A-2026-118 Rohbau BV Hafenstraße 22", "05.01.2026", "Musterbau GmbH", "–", "–", "–", "Freigabe"]]
    ye = tbl(p, cx0, y, colw, rows, rowh=36, fs=10, hl=(1,), hh=36)
    mk(p, cx0 + cw - 22, y + 8, 5)
    p.box(cx0, ye + 4, cw, 18, "7 Elemente · angezeigt: die ersten 100 Elemente (umstellbar ▾) · Spalten konfigurierbar", "small")
    p.box(cx0, ye + 28, cw, 50, "⬇  Dateien hierher ziehen – Ablage automatisch · manuell · mit Vorlage",
          "rounded=1;arcSize=6;dashed=1;fillColor=%s;strokeColor=%s;fontColor=%s;fontSize=11;" % (C['grey_l'], C['teal'], C['teal']))
    mk(p, cx0 + cw - 22, ye + 30, 7)
    p.box(cx0, ye + 88, cw, 36,
          "Mehrfachablage: RE-2026-1041 liegt zusätzlich in der Objektakte „10010-0001 · BV Hafenstraße 22\" – sichtbar über „In Akte anzeigen\" (Vorbehalt Test T13)",
          "ui_hint")
    mk(p, cx0 + cw - 22, ye + 96, 6)
    # Vorschau / Eigenschaften
    vx, vw = cx0 + cw + 12, 1218 - (cx0 + cw + 12)
    tabs(p, vx, y, ["Vorschau", "Eigenschaften", "Notizen", "Versionen", "Aktivitäten"], 0, fs=9, w=vw / 5)
    ui_viewer(p, vx, y + 24, vw, 440, "Vorschau: RE-2026-1041 (Original)",
              ["RECHNUNG", "", "Musterbau GmbH", "Industriestr. 5", "", "an: Livos Objektgesellschaft", "    Nord mbH", "",
               "RE-Nr.: RE-2026-1041", "Datum:  15.09.2026", "BV Hafenstraße 22", "", "Rohbauarbeiten", "  12.400,00", "",
               "USt 19 %  2.356,00", "Brutto 14.756,00 €"])
    mk(p, vx + vw - 22, y + 27, 8)
    # Variante Objektakte
    oy = 818
    p.box(WX, oy, WW, 100, "", "group_g")
    p.box(WX + 10, oy + 6, 700, 20, "Variante Objektakte (K-11) – Aktenkopf  ·  📁 BV Hafenstraße 22 (10010-0001)", "ui_sec",
          extra="verticalAlign=middle;")
    mk(p, WX + WW - 30, oy + 6, 10)
    frow(p, WX + 12, oy + 36, WW - 24, [
        ("Mandant", "10010", "ro", {"wt": .5}),
        ("Objekt-ID (global eindeutig)", "10010-0001", "ro", {"wt": .9}),
        ("Objektbezeichnung (Titel)", "BV Hafenstraße 22, 20359 Hamburg", "ro", {"wt": 1.5}),
        ("Verwaltungsart / Property Manager", "Eigenverwaltung · Asset Mgmt. Nord", "ro", {"wt": 1.5}),
        ("Segment", "Bau", "ro", {"wt": .6})])
    card(p, WX, 934, 570, "Regeln (14.11)",
         "• Aktenkategorien (Unterakten) werden automatisch angelegt, nicht manuell.\n"
         "• Mehrfachablage Rechnung in Kreditoren- und Objektakte unter Vorbehalt Test T13.\n"
         "• Akten sind nicht als PDF exportierbar – Export nur der Eigenschaften (Excel/CSV).\n"
         "• Sichtbar sind nur Dokumente mit Leserecht (Kapitel 13.4).", "note", h=100)
    field_legend(p, 630, 934, 330)
    card(p, 980, 934, 250, "Aufruf",
         "aus der Suche (M-12), aus einem Dokument („In Akte anzeigen\", Akteninhalt am Dokument) oder als Favorit auf der Startseite (M-10).",
         "info", fs=10, h=128)
    notes(p, RX, ny, RW, [
        (1, "Aktenkopf mit Titel und Akteneigenschaften. Mandant und Kreditor-Nr (DATEV) sind Erkennungsmerkmale der Aktenbildung (Pflicht, nur lesen); Mandantenname und Kreditorname werden vererbt [S]/[K]."),
        (2, "Lieferanten-Konsolidierungsnummer aus der Lieferanten-App (LAP, über BeSync). Link „alle Gesellschaften\" = gespeicherte Suche „Lieferant gesellschaftsübergreifend\" (M-12)."),
        (3, "FSB gültig bis / FSB-Status als BeSync-Rückmeldung (BES), Phase 3 (AE-15)."),
        (4, "Aktenbaum links: Unterakten je Kategorie, gelb = Inhalt, grau = leer. Strukturregeln der Aktenart K-12 [K]."),
        (5, "Akteninhalt: Kategorie · Titel · Dokument-/Rechnungsdatum · Kreditor bzw. Absender · Bruttobetrag (bei K-01) · Workflowstatus (E-24) · Zahlstatus (E-23) · Status (Bearbeitung/Freigabe/Archiv)."),
        (6, "„In Akte anzeigen\" zeigt alle Akten eines Dokuments – hier Kreditorenakte und Objektakte (Mehrfachablage, Test T13)."),
        (7, "Dropzone unten in der Akte: Ablage per Drag & Drop automatisch, manuell oder mit Vorlage [S]."),
        (8, "Rechts Vorschau, Eigenschaften, Notizen, Versionen, Aktivitäten des markierten Dokuments [S]."),
        (9, "Aktionen [S]: Ablegen, Öffnen, In Akte anzeigen, Verknüpfen/Lösen, Eigenschaften exportieren, Beobachten, Favorisieren, Aufgabe zur Akte erstellen."),
        (10, "Objektakte K-11: Mandant und Objekt-ID (global eindeutig) aus der Aktenbildung; Objektbezeichnung, Verwaltungsart/PM und Segment (Bestand · Privatisierung · Bau) aus der Lieferanten-App/Objektstamm (LAP)."),
    ])
    return p


# ================================================================ M-12
def page34(doc):
    p, ny = frame(doc, "p34", "M-12 Suche / gespeicherte Suchen",
                  "Rolle: alle · Werkzeug: d.velop documents Suche (Widget, Suchleiste), Outlook-Add-In (Desktop) · "
                  "Umsetzung: [S] Suche; [K] Eigenschaften je Kategorie für Suche, Facetten, Ergebnisliste; [O] zentrale Zuweisung von Suchvorlagen",
                  "SKO")
    ui_window(p, WX, WY, WW, 664, "Suche", crumbs="Start › Suche › Kategorie K-01 Eingangsrechnung",
              user="Maria L. (Rechnungseingang)")
    x0, y = 52, 180
    p.box(x0, y, 760, 30, "🔍  Musterbau Hafenstraße", "ui_input", extra="fontSize=12;")
    btns(p, x0 + 770, y + 1, [("Suchen", "ui_btn")])
    p.box(x0 + 880, y + 4, 300, 22, "Volltext inkl. OCR · nur berechtigte Treffer", "small", extra="verticalAlign=middle;")
    mk(p, x0 + 738, y + 5, 1)
    y += 44
    # linke Spalte: Kategorie + Suchfelder
    lw = 316
    ly = sec(p, x0, y, lw, "Kategorie", 2)
    ly = fld(p, x0, ly, lw, "Kategorie(n)", "K-01 Eingangsrechnung", "select")
    ly = sec(p, x0, ly, lw, "Suchfelder K-01 (Reihenfolge)")
    F = [("Mandant", "10010 · Livos Nord", "select"), ("Kreditor", "Musterbau GmbH", "select"),
         ("Konsolidierungsnummer", "LK-000482", "input"), ("Rechnungsnummer", "", "input"),
         ("Rechnungsdatum von", "01.01.2026", "input"), ("Rechnungsdatum bis", "30.09.2026", "input"),
         ("Bruttobetrag von", "", "input"), ("Bruttobetrag bis", "", "input"),
         ("Objekt-ID", "10010-0001", "select"), ("Auftrags-/Vertragsnummer", "", "input"),
         ("Belegart", "Rechnung", "select"), ("Workflowstatus", "alle", "select"), ("Zahlstatus", "alle", "select")]
    for i in range(0, len(F), 2):
        pair = F[i:i + 2]
        o = [{"n": 3}] if pair[0][0] == "Konsolidierungsnummer" else [{}]
        ly = frow(p, x0, ly, lw if len(pair) == 2 else (lw - 12) / 2, [pair[0] + tuple(o)] + list(pair[1:]), gap=12)
    # Facetten
    fx = x0 + lw + 14
    fw = 190
    fy = sec(p, fx, y, fw, "Facetten", 4)
    fac = ("**Mandant**\n☑ 10010 Livos Objektges. Nord (6)\n☐ 10020 Livos Objektges. Süd (2)\n☐ 10030 Livos Bau & Projekt (1)\n\n"
           "**Kategorie**\n☑ Eingangsrechnung (9)\n☐ Vertrag (1)\n☐ Korrespondenz (2)\n\n"
           "**Jahr**\n☑ 2026 (9)\n☐ 2025 (4)\n\n**Kreditor**\n☑ Musterbau GmbH (9)\n\n**Zahlstatus**\n☐ offen (2)\n☐ bezahlt (7)")
    p.box(fx, fy, fw, 400, fac, "ui_nav", extra="fontSize=10;")
    # Ergebnisliste
    rx = fx + fw + 14
    rw = 1218 - rx
    btns(p, rx, y, [("Suche speichern", "ui_btn"), ("Link kopieren", "ui_btn2"), ("☆ Beobachten", "ui_btn2")],
         fs=10, h=24, gap=6)
    btns(p, rx, y + 30, [("Eigenschaften exportieren", "ui_btn2"), ("In PDF zusammenfassen", "ui_btn2"),
                         ("Zur Liste hinzufügen", "ui_btn2")], fs=10, h=24, gap=6)
    mk(p, 1196, y + 2, 6)
    ry = y + 66
    p.box(rx, ry, 300, 18, "9 Treffer · sortiert nach Rechnungsdatum ▾", "small", extra="fontStyle=1;")
    ry += 22
    tw = 400
    colw = [42, 62, 68, 58, 54, 70, 46]
    rows = [["Mdt.", "Kreditor", "Rechnungs-nr.", "Datum", "Brutto €", "Objekt-ID", "Zahlst."],
            ["10010", "Musterbau GmbH", "RE-2026-1041", "15.09.2026", "14.756,00", "10010-0001", "offen"],
            ["10010", "Musterbau GmbH", "RE-2026-0987", "18.08.2026", "35.700,00", "10010-0001", "bezahlt"],
            ["10010", "Musterbau GmbH", "RE-2026-0911", "21.07.2026", "35.700,00", "10010-0001", "bezahlt"],
            ["10010", "Musterbau GmbH", "RE-2026-0850", "20.06.2026", "35.700,00", "10010-0001", "bezahlt"],
            ["10020", "Musterbau GmbH", "RE-2026-0772", "12.05.2026", "4.165,00", "10020-0001", "bezahlt"],
            ["10010", "Musterbau GmbH", "RE-2026-0698", "14.04.2026", "35.700,00", "10010-0001", "bezahlt"],
            ["10030", "Musterbau GmbH", "RE-2026-0655", "02.04.2026", "8.330,00", "10030-0001", "offen"]]
    ye = tbl(p, rx, ry, colw, rows, rowh=34, fs=9, hl=(1,), hh=34)
    mk(p, rx + tw - 22, ry - 22, 5)
    p.box(rx, ye + 6, tw, 34, "Spalten je Kategoriekombination konfiguriert [K]; Workflowstatus/Belegart per Spaltenauswahl einblendbar",
          "small")
    # Vorschau
    vx = rx + tw + 10
    ui_viewer(p, vx, ry - 22, 1218 - vx, ye + 40 - (ry - 22), "Vorschau",
              ["RECHNUNG", "", "Musterbau GmbH", "", "RE-2026-1041", "15.09.2026", "", "BV Hafenstr. 22", "",
               "Brutto", "14.756,00 €"])
    mk(p, 1196, ry - 20, 7)
    p.box(rx, ye + 50, 1218 - rx, 34, "Suchergebnisse zeigen nur Dokumente, für die der Benutzer berechtigt ist (Kapitel 13).",
          "ui_ok")
    p.box(rx, ye + 92, 1218 - rx, 34,
          "[O] Eine zentrale Zuweisung von Suchvorlagen an Rollen ist nicht belegt → Verteilung per Link und Verknüpfungs-Widgets (M-10).",
          "ui_err")
    mk(p, 1196, ye + 99, 8)
    # Tabellen unten
    by = 790
    p.box(WX, by, 560, 22, "Suchfelder je Kategorie (Auszug, Reihenfolge)", "h2", extra="fontSize=13;")
    tbl(p, WX, by + 26, [120, 440], [
        ["Kategorie", "Suchfelder"],
        ["K-01 Eingangsrechnung", "Mandant · Kreditor · Konsolidierungsnummer · Rechnungsnummer · Rechnungsdatum (von–bis) · Bruttobetrag (von–bis) · Objekt-ID · Auftrags-/Vertragsnummer · Belegart · Workflowstatus · Zahlstatus"],
        ["K-02 bis K-04, K-07", "Mandant · Kreditor · Objekt-ID · Auftragsnummer · Dokumentdatum · Betreff · Absender"],
        ["K-05 / K-14 Vertrag", "Mandant · Vertragspartner · Vertragstyp · Vertragsstatus · Vertragsbeginn/-ende · Objekt-ID"],
        ["K-06 Bescheinigung", "Mandant · Kreditor · Gültig bis"],
        ["K-09 Post", "Mandant · Absender · Betreff · Dokumentdatum · Eingangskanal"],
        ["Akten", "Mandant · Kreditor-Nr · Objekt-ID · Vertrags-ID"]], rowh=34, fs=10, hmap={1: 50})
    gx = WX + 580
    p.box(gx, by, 610, 22, "Gespeicherte Suchen (Vorschlag, per Link an Rollen verteilt)", "h2", extra="fontSize=13;")
    tbl(p, gx, by + 26, [190, 240, 110, 70], [
        ["Name", "Kriterien", "Rolle", "Beobachten"],
        ["Lieferant gesellschaftsübergreifend", "Konsolidierungsnummer = X, alle Kategorien", "R-02, R-07", "–"],
        ["Rechnungen zu Vertrag/Auftrag", "Auftrags-/Vertragsnummer = X", "R-03, R-11", "–"],
        ["Bescheinigungen laufen ab", "K-06, Gültig bis ≤ heute + 60 Tage", "R-02", "ja"],
        ["Unbezahlte Rechnungen über Fälligkeit", "K-01, Zahlstatus ≠ bezahlt, Nettofälligkeit < heute", "R-07", "ja"],
        ["Z2 – Eingangsrechnungen Gesellschaft X, Jahr Y", "K-01, Mandant, Rechnungsdatum", "R-14-Betreuung", "–"],
        ["Meine Objekte – neue Dokumente", "Objekt-ID der eigenen Objekte", "R-03", "ja"]], rowh=34, fs=10, hmap={1: 50},
        cell=lambda ri, ci: "align=center;" if ci == 3 else "")
    ny = notes(p, RX, ny, RW, [
        (1, "Suchleiste oben: Volltextsuche inkl. OCR-Text der Belege [S]. Aufruf auch über das Such-Widget der Startseite oder das Outlook-Add-In (Desktop)."),
        (2, "Kategorie wählen → die zugehörigen Eigenschaftsfelder erscheinen in der konfigurierten Reihenfolge [K]."),
        (3, "Konsolidierungsnummer (E-07) findet einen Lieferanten gesellschaftsübergreifend über alle Mandanten."),
        (4, "Facetten links (z. B. Mandant, Kategorie, Jahr, Kreditor) verfeinern die Trefferliste [S]/[K]."),
        (5, "Ergebnisliste Mitte mit Spalten je Kategoriekombination [K]; Doppelklick öffnet das Dokument, „In Akte anzeigen\" führt zu M-11."),
        (6, "Aktionen [S]: Suchen · Filtern · Suche speichern (persönlicher Ordner) · Link kopieren · Beobachten (E-Mail bei neuen Treffern, ab business) · Eigenschaften exportieren · In PDF zusammenfassen · Zur Liste hinzufügen."),
        (7, "Vorschau rechts zeigt das markierte Dokument."),
        (8, "Gespeicherte Suchen werden als Link bzw. Verknüpfungs-Widget (M-10) an die Rollen verteilt – keine zentrale Zuweisung [O]."),
    ])
    field_legend(p, RX, ny + 10)
    return p


# ================================================================ M-13
def page35(doc):
    p, ny = frame(doc, "p35", "M-13 PM-Freigabe",
                  "Workflow WF-03 · Rolle: R-04 Asset Management (Verteilung durch R-02) · Werkzeug: smart invoice, eigene Workflowdefinition WF-03 mit Postfach "
                  "freigabe-hv@… und eigenem Importprofil · Umsetzung: [S] Freigabeschritt, [K] Workflow/Felder/Matrix, [A] Rückmeldemail über BeSync (S-11)",
                  "SKAO")
    ui_window(p, WX, WY, WW, 790, "smart invoice › Aufgabe PM-Freigabe",
              crumbs="Start › Aufgaben › PM-Freigabe › SI-2026-004902", user="Jana K. (Asset Management)")
    x0, y = 52, 180
    # Kopfzeile
    p.box(x0, y, 1166, 40, "", "rounded=1;arcSize=6;fillColor=%s;strokeColor=%s;" % (C['teal_l'], C['teal']))
    p.box(x0 + 10, y + 4, 800, 32,
          "**PM-Freigabe**  ·  Livos Objektgesellschaft Nord mbH  ·  Musterbau GmbH  ·  RE-2026-1187  ·  Brutto 9.996,00 €",
          "text", extra="fontSize=12;verticalAlign=middle;")
    pill(p, x0 + 846, y + 10, "PM-Freigabe – keine Zahlung", C['orange_l'], C['orange'], w=190)
    pill(p, x0 + 1044, y + 10, "Status: offen", "#FFFFFF", C['teal'], w=110)
    mk(p, x0 + 1144, y - 8, 1)
    y += 48
    # Hinweisleiste
    p.box(x0, y, 1166, 26, "ⓘ  Freigabematrix WF-03: Nettobetrag 8.400,00 € > Schwellwert 5.000,00 € (Mandant 10010) → Freigabe durch Asset Management. "
          "Keine Kontierung, keine DATEV-Übergabe, keine Zahlung.", "ui_hint")
    mk(p, x0 + 1144, y + 3, 2)
    y += 36
    lw, lx = 600, x0
    ly = sec(p, lx, y, lw, "A  Zuordnung (aus Verteilung)")
    ly = frow(p, lx, ly, lw, [("Mandant", "10010 · Livos Objektgesellschaft Nord mbH", "ro", {"n": 3, "star": True}),
                              ("Objekt-ID / Objektbezeichnung", "10010-0002 · Wohnanlage Elbblick 5", "ro", {"n": 4, "star": True})])
    ly = frow(p, lx, ly, lw, [("Verwaltungsart / Property Manager", "PM-verwaltet · Nordhaus Hausverwaltung GmbH", "ro", {"n": 5}),
                              ("Absender (PM-E-Mail)", "rechnungen@nordhaus-hv.example", "ro", {"n": 6, "star": True})])
    ly = sec(p, lx, ly, lw, "B  Belegkopf")
    ly = frow(p, lx, ly, lw, [("Kreditorname", "Musterbau GmbH", "ai", {"n": 7, "star": True, "wt": 1}),
                              ("Kreditor-Nr (HV-Kreditor, nicht Pflicht)", "80412", "ro", {"wt": 1})])
    ly = frow(p, lx, ly, lw, [("Rechnungsnummer", "RE-2026-1187", "ai", {"star": True}),
                              ("Rechnungsdatum", "11.09.2026", "ai", {"star": True, "n": 8})])
    ly = frow(p, lx, ly, lw, [("Nettobetrag", "8.400,00 €", "ai", {"star": True}),
                              ("Bruttobetrag", "9.996,00 €", "ai", {"star": True, "n": 9})])
    ly = sec(p, lx, ly, lw, "E  Freigabe und Rückmeldung an den Property Manager")
    ly = fld(p, lx, ly, lw, "Leistungsbeschreibung (Kurztext)", "Instandsetzung Tiefgaragenzufahrt, Abdichtung und Entwässerungsrinne", "input")
    ly = fld(p, lx, ly, lw, "Rückmeldetext an PM (wird in die E-Mail übernommen)",
             "Freigabe erteilt. Bitte die Abnahmebestätigung nachreichen und im nächsten Objektbericht ausweisen.", "input", h=54, n=10)
    ly = fld(p, lx, ly, lw, "Ablehnungsgrund (Werteliste – Pflicht bei „Ablehnen\")", "— bitte wählen —", "select", n=11)
    p.box(lx, ly, lw, 34, "Positionsbereich ausgeblendet – in WF-03 findet keine Positionskontierung statt.", "text",
          extra="fontSize=10;fontColor=%s;fillColor=%s;strokeColor=%s;dashed=1;rounded=1;arcSize=6;verticalAlign=middle;spacingLeft=8;"
          % (C['grey'], C['grey_l'], C['grey_m']))
    mk(p, lx + lw - 22, ly + 7, 12)
    # Vorschau rechts
    vx = x0 + lw + 16
    vw = 1218 - vx
    tabs(p, vx, y, ["Beleg", "Anlagen (1)", "Historie", "Notizen"], 0, fs=10, w=vw / 4)
    ui_viewer(p, vx, y + 24, vw, 530, "Belegvorschau (Original-PDF aus freigabe-hv@…)",
              ["RECHNUNG", "", "Musterbau GmbH · Industriestr. 5", "an: Livos Objektgesellschaft Nord mbH",
               "     c/o Nordhaus Hausverwaltung GmbH", "", "Objekt: Wohnanlage Elbblick 5", "",
               "Rechnungs-Nr.: RE-2026-1187", "Datum: 11.09.2026", "",
               "Pos 1  Instandsetzung TG-Zufahrt  …  8.400,00", "", "Netto 8.400,00 · USt 19 % 1.596,00",
               "Brutto 9.996,00 €", "", "gebucht durch Property Manager (HV-Kreditor 80412)"])
    # Aktionsleiste
    ay = 862
    p.line(x0, ay - 8, 1218, ay - 8)
    btns_r(p, 1218, ay, [("Rückfrage an PM", "ui_btn2"), ("Ablehnen", "ui_btn_r"), ("✔ Freigeben", "ui_btn")])
    mk(p, 1196, ay - 16, 13)
    p.box(x0, ay, 560, 28, "Klick auf eine Aktion beendet die Aufgabe; Rückmeldung an den PM per E-Mail über BeSync", "small",
          extra="verticalAlign=middle;")
    # Aktionen-Tabelle unten
    by = 918
    p.box(WX, by, 600, 22, "Aktionen (14.13)", "h2", extra="fontSize=13;")
    tbl(p, WX, by + 26, [170, 570, 90], [
        ["Aktion", "Wirkung", "Status"],
        ["Freigeben", "Ende „Freigegeben\", Webhook → BeSync-Mail an PM mit Freigabevermerk", "[S] / [A]"],
        ["Ablehnen", "Ende „Abgelehnt\", Mail mit Grund (Ablehnungsgrund Pflicht)", "[S] / [A]"],
        ["Rückfrage an PM", "Mail mit Frage, Beleg wartet (Wiedervorlage)", "[A] / [O]"]], rowh=28, fs=10)
    card(p, 890, by + 26, 340, "Regeln",
         "Beleg zählt ins invoices-Volumen. Keine DATEV-Übergabe. Scope und Schwellwerte legt Livos fest (OP-17).",
         "note", fs=10, h=112)
    ny = notes(p, RX, ny, RW, [
        (1, "Kopfzeile wie 14.0.3 mit Kennzeichnung „PM-Freigabe – keine Zahlung\" [K]."),
        (2, "Hinweisleiste: Schwellwert netto aus der Freigabematrix WF-03 (M-17); Hinweise statt Blockaden."),
        (3, "Mandant: Pflicht; in der Verteilung schreibbar, in der Freigabe nur lesen."),
        (4, "Objekt-ID/-bezeichnung: Pflicht, Spalte der Freigabematrix; Freigabe nur lesen."),
        (5, "Verwaltungsart / Property Manager aus dem Objektstamm (LAP) – Plausibilität PM ↔ Objekt."),
        (6, "Absender = PM-E-Mail aus dem Mail-Eingang (SYS); Empfänger der Rückmeldung."),
        (7, "Kreditorname Pflicht (ERK); Kreditor-Nr nicht Pflicht – HV-Kreditor, 80000er-Kreis [O]."),
        (8, "Rechnungsnummer / -datum aus der Erkennung, Pflicht, schreibbar."),
        (9, "Netto-/Bruttobetrag Pflicht; Schwellwert gilt netto (Freigabematrix)."),
        (10, "Rückmeldetext an PM (optional) wird in die BeSync-Mail übernommen [A]."),
        (11, "Ablehnungsgrund aus Werteliste – bedingt Pflicht bei „Ablehnen\"."),
        (12, "Positionsbereich ausgeblendet: keine Kontierung, keine Buchung."),
        (13, "Aktionen: Freigeben (Standard, hervorgehoben), Ablehnen, Rückfrage an PM [A]/[O]."),
    ], fs=10)
    field_legend(p, RX, ny + 6)
    return p


# ================================================================ M-14
def page36(doc):
    p, ny = frame(doc, "p36", "M-14 Vertragsmaske",
                  "Rolle: R-11 Vertragsmanagement; Leser R-04, R-07 · Werkzeug: d.velop contracts – Dashboard, „Neuer Vertrag\", Vertragsdetailansicht, "
                  "Fristenkalender · Umsetzung: [S] contracts; [K] Vertragstypen, Wertemengen, Zusatzfelder; [O] Freigabe-Workflow (OP-12)",
                  "SKAO")
    ui_window(p, WX, WY, WW, 900, "contracts › Vertragsdetailansicht",
              crumbs="Start › Verträge › V-2026-0042 · Rahmenvertrag Musterbau 2026", user="Tim B. (Vertragsmanagement)")
    x0, y = 52, 180
    # Kopf
    p.box(x0, y, 1166, 74, "", "rounded=1;arcSize=6;fillColor=%s;strokeColor=%s;" % (C['grey_l'], C['grey_m']))
    p.box(x0 + 12, y + 6, 700, 26, "Rahmenvertrag Musterbau 2026 – Rohbauleistungen", "text",
          extra="fontSize=16;fontStyle=1;fontColor=%s;verticalAlign=middle;" % C['navy'])
    pill(p, x0 + 730, y + 9, "Aktiv", C['green_l'], C['green'], w=70)
    p.box(x0 + 810, y + 8, 340, 24, "Musterbau GmbH · Mandant 10010 · Bauvertrag", "small", extra="verticalAlign=middle;")
    bx, bwid = x0 + 12, 900
    p.box(bx, y + 42, bwid, 14, "", "rounded=1;arcSize=50;fillColor=#FFFFFF;strokeColor=%s;" % C['grey_m'])
    p.box(bx, y + 42, bwid * 0.37, 14, "", "rounded=1;arcSize=50;fillColor=%s;strokeColor=%s;" % (C['teal'], C['teal']))
    p.box(bx + bwid * 0.87, y + 38, 3, 22, "", "rounded=0;fillColor=%s;strokeColor=none;" % C['red'])
    p.box(bx + bwid + 10, y + 36, 240, 28, "Laufzeit 01.01.2026 – 31.12.2027 · 37 % · Kündigungsstichtag 30.09.2027",
          "small", extra="verticalAlign=middle;")
    mk(p, x0 + 1144, y - 8, 1)
    y += 86
    # Spalten
    lw = 560
    tabs(p, x0, y, ["Stammdaten", "Laufzeit & Fristen"], 0, fs=10, w=lw / 2)
    ly = y + 32
    ly = sec(p, x0, ly, lw, "Block 1 – Stammdaten")
    ly = fld(p, x0, ly, lw, "1.1 Vertragsgegenstand", "Rahmenvertrag Musterbau 2026 – Rohbauleistungen", "req")
    R = lambda fs: frow(p, x0, ly, lw, fs)
    ly = R([("1.2 Vertrags-ID (intern)", "V-2026-0042", "ro", {"n": 2}), ("1.3 Vertrags-ID (extern)", "MB-RV-2026/01", "input")])
    ly = R([("1.4 Vertragstyp", "Bauvertrag", "select", {"star": True, "n": 3}), ("1.5 Vertragsart", "Rahmenvertrag", "select", {"star": True})])
    ly = R([("1.6 Übergeordneter Rahmenvertrag", "— nur bei Einzelvertrag mit RV —", "select", {"n": 4}),
            ("1.7 Vertragsstatus", "Aktiv", "select", {"star": True})])
    ly = R([("1.8 Mandant / Mandantenname", "10010 · Livos Objektgesellschaft Nord mbH", "select", {"star": True, "wt": 1.3, "n": 5}),
            ("1.9 Organisation", "Livos Nord (Verbund)", "select", {"wt": .7})])
    ly = R([("1.10 Objekt-ID", "10010-0001 · BV Hafenstraße 22", "select", {"wt": 1.1}),
            ("1.11 Vertragspartner", "Musterbau GmbH (LK-000482)", "select", {"star": True, "n": 6, "wt": .9})])
    ly = R([("1.12 Kreditor-Nr", "70012", "select", {"wt": .6}),
            ("1.13 Verantwortlicher (intern)", "Tim Brandt (Vertragsmanagement)", "select", {"star": True, "wt": 1.4, "n": 7})])
    ly = sec(p, x0, ly + 4, lw, "Block 2 – Register „Laufzeit & Fristen\"")
    ly = R([("2.1 Vertragsbeginn", "01.01.2026", "req"), ("2.2 Vertragsende (leer = unbefristet)", "31.12.2027", "input")])
    ly = R([("2.3 Kündigungsfrist", "3 Monate zum Laufzeitende", "input", {"n": 8}),
            ("2.4 Verlängerungsart / -zeitraum", "rollierend · 12 Monate", "select")])
    ly = R([("2.5 Kündigungsstichtag (berechnet)", "30.09.2027", "ro"), ("2.6 Vertragswert", "1.250.000,00 €", "input")])
    ly = R([("2.7 Gewährleistungsende / Sicherheit bis (Bau)", "31.12.2032", "input", {"n": 9}), ("", "", "ro")]) if False else \
        frow(p, x0, ly, lw / 2 - 6, [("2.7 Gewährleistungsende / Sicherheit bis (Bau)", "31.12.2032", "input", {"n": 9})])
    # Dokumente
    dx = x0 + lw + 16
    dw = 360
    tabs(p, dx, y, ["Dokumente (6)"], 0, fs=10, w=dw)
    dy = y + 32
    ye = tbl(p, dx, dy, [112, 180, 68], [
        ["3.1 Dokumenten- typ *", "Titel", "Datum"],
        ["Vertrag ▾", "Rahmenvertrag Musterbau 2026 (signiert)", "02.01.2026"],
        ["Anlage ▾", "Leistungsverzeichnis Rohbau", "02.01.2026"],
        ["Bürgschaft ▾", "Vertragserfüllungsbürgschaft 5 %", "15.01.2026"],
        ["Protokoll ▾", "Vergabeprotokoll BV Hafenstraße 22", "12.12.2025"],
        ["Nachtrag ▾", "Nachtrag 01 – Mehrmengen Bewehrung", "20.08.2026"],
        ["Korrespondenz ▾", "Schreiben Bauzeitverlängerung", "03.09.2026"]], rowh=34, fs=10, hl=(1,))
    mk(p, dx + dw - 22, y + 2, 10)
    ui_viewer(p, dx, ye + 10, dw, 262, "Vorschau: Rahmenvertrag (signiert)",
              ["RAHMENVERTRAG", "", "zwischen Livos Objektgesellschaft", "Nord mbH und Musterbau GmbH", "",
               "§ 1 Vertragsgegenstand", "§ 5 Laufzeit, Kündigung", "", "✍ signiert (d.velop sign)"])
    btns(p, dx, ye + 282, [("＋ Dokument hinzufügen", "ui_btn2"), ("Mit d.velop pilot fragen", "ui_btn2")], fs=10, h=26)
    mk(p, dx + dw - 22, ye + 285, 11)
    # Aufgaben/Verlauf
    ax = dx + dw + 14
    aw = 1218 - ax
    tabs(p, ax, y, ["Aufgaben / Verlauf"], 0, fs=10, w=aw)
    items = [("⏰ Frist", "Kündigungsstichtag 30.09.2027 – Erinnerung 90 Tage vorher an T. Brandt", "ui_hint"),
             ("☐ Aufgabe", "Bürgschaft auf Rückgabe prüfen – fällig 15.10.2026 (WF-08)", "ui_hint"),
             ("✔ Signatur", "Vertrag signiert über d.velop sign – 02.01.2026", "ui_ok"),
             ("✔ Freigabe", "Vertragsfreigabe durch GF – 22.12.2025", "ui_ok"),
             ("✎ Änderung", "Status Entwurf → Aktiv, T. Brandt – 02.01.2026", "ui_ok"),
             ("✎ Dokument", "Nachtrag 01 hinzugefügt – 20.08.2026", "ui_ok")]
    iy = y + 32
    for t, b, st in items:
        p.box(ax, iy, aw, 58, f"**{t}**\n{b}", st, extra="verticalAlign=top;spacingTop=4;")
        iy += 64
    mk(p, ax + aw - 22, y + 2, 12)
    # Aktionsleiste
    ay = 964
    p.line(x0, ay - 8, 1218, ay - 8)
    btns_r(p, 1218, ay, [("Frist-Erinnerung / Aufgabe", "ui_btn2"), ("Signatur starten", "ui_btn2"),
                         ("Freigabe starten", "ui_btn2"), ("Vertrag speichern", "ui_btn")])
    mk(p, 1196, ay - 18, 13)
    p.box(x0, ay, 420, 28, "„Vertrag anlegen / speichern\" legt die Vertragsakte (K-14) in documents an", "small",
          extra="verticalAlign=middle;")
    card(p, WX, 1024, WW, "Regeln (14.14)",
         "Fehlerhafte Werte in Wertemengen (Schreibweise) verhindern die Aktenanlage · Datentyp und Anzahl der Werte sind nachträglich nicht änderbar · "
         "Rechte je Organisation × Vertragstyp plus DMS-Rechte (Kapitel 13).", "note", fs=10, h=48)
    ny = notes(p, RX, ny, RW, [
        (1, "Kopf: Vertragsgegenstand, Vertragsstatus, Laufzeitbalken (rote Marke = Kündigungsstichtag) [S]."),
        (2, "Vertrags-ID intern (SYS) verknüpft Vertragsakte und Dokumente, nur lesen."),
        (3, "Vertragstyp aus Wertemenge – Werte exakt wie in documents [S]/[K]."),
        (4, "Übergeordneter Rahmenvertrag: Pflicht bei Vertragsart „Einzelvertrag mit Rahmenvertrag\" (Vertragshierarchie)."),
        (5, "Mandant aus Dataset – Livos-Pflicht (P1) [K]/[O]; Organisation = Gesellschaftsverbund (Vorschlag 12.1.9)."),
        (6, "Vertragspartner aus business objects; Übernahme aus der Lieferanten-App über BeSync (Vorschlag) [A]/[O]. Kreditor-Nr (STA) bei Lieferantenverträgen, Objekt-ID bei objektbezogenen Verträgen [K]."),
        (7, "Verantwortlicher (intern) empfängt die Fristmeldungen [S]."),
        (8, "Kündigungsfrist und Verlängerung steuern die Laufzeit-/Fristberechnung; Kündigungsstichtag berechnet [S]/[O] (Feldnamen [O])."),
        (9, "Gewährleistungsende / Sicherheit bis: Zusatzfeld je Vertragstyp Bau [K]."),
        (10, "Register Dokumente: Pflichtangabe Dokumententyp je Dokument (Vertrag · Nachtrag · Kündigung · Anlage · Protokoll · Korrespondenz · Bürgschaft) [K]."),
        (11, "Dokument hinzufügen per Upload oder Outlook [S]; Chat zum Vertragsdokument mit d.velop pilot [S]."),
        (12, "Aufgaben/Verlauf: Fristen, Aufgaben, Aktivitäten; Frist-Erinnerung als Wiedervorlage (WF-08)."),
        (13, "Aktionen: Vertrag speichern [S] · Freigabe starten (process studio „Vertragsfreigabe\") [K]/[O] · Signatur starten (d.velop sign) [S] · Frist-Erinnerung [S]."),
    ], fs=10)
    field_legend(p, RX, ny + 6)
    return p


# ================================================================ M-15
def page37(doc):
    p, ny = frame(doc, "p37", "M-15 Postverteilung",
                  "Teil A: R-01 Poststelle – inbound scan (Stapelbearbeitung) · Teil B: Empfängergruppen (R-02, R-03, R-05, R-11, Fachbereiche) – "
                  "d.velop mail dispatcher (WF-07) · Umsetzung: [S]; [K] Importprofile, Klassifizierung, Empfängergruppen, Schnellaktionen; KI nur C1",
                  "SKO")
    # ---------- Teil A
    ui_window(p, WX, WY, WW, 420, "inbound scan › Stapelbearbeitung Post",
              crumbs="Teil A · Poststapel 26.09.2026 · Stapel P-0926-01 (42 Seiten)", user="Petra S. (Poststelle)")
    x0, y = 52, 180
    sw = 250
    tbl(p, x0, y, [120, 60, 70], [
        ["Stapel", "Seiten", "Status"],
        ["P-0926-01 Post", "42", "in Arbeit"],
        ["P-0926-02 Post", "18", "neu"],
        ["P-0926-03 Einschreiben", "3", "neu"],
        ["P-0925-04 Post", "37", "verteilt"]], rowh=30, fs=10, hl=(1,))
    mk(p, x0 + sw - 22, y + 3, 1)
    # Seiten mit Trennern
    mx = x0 + sw + 14
    mw = 420
    p.box(mx, y, mw, 22, "Seiten mit Trennern (Dokument 3 von 11)", "ui_sec", extra="verticalAlign=middle;")
    ty = y + 30
    cols = [("S.7", None), ("S.8", "o"), ("S.9", None), ("S.10", "b"), ("S.11", None), ("S.12", "g")]
    cx = mx
    for t, sep in cols:
        if sep:
            col = {"o": C['orange'], "b": C['blue'], "g": C['green']}[sep]
            p.box(cx, ty - 4, 6, 104, "", "rounded=0;fillColor=%s;strokeColor=none;" % col)
            cx += 12
        p.box(cx, ty, 52, 96, t + "\n\n≡≡≡\n≡≡\n≡≡≡", "rounded=0;fillColor=#FFFFFF;strokeColor=%s;shadow=1;fontSize=9;fontColor=%s;"
              % (C['grey_m'], C['grey']))
        cx += 60
    mk(p, mx + mw - 22, y + 1, 2)
    p.box(mx, ty + 108, mw, 40, "▮ orange / ▮ blau = KI-Trenner (Vorschlag) · ▮ grün = manueller Trenner · Trennblatt-Barcode liefert den Mandanten",
          "small")
    p.box(mx, ty + 150, mw, 90, "", "ui_viewer")
    p.box(mx + 8, ty + 156, mw - 16, 78, "Vorschau Seite 10: Musterbau GmbH · Schreiben vom 22.09.2026 · Betreff: Bauzeitverlängerung BV Hafenstraße 22",
          "text", extra="fontSize=10;fontFamily=Courier New;")
    # Klassifizierung
    kx = mx + mw + 16
    kw = 1218 - kx
    ky = sec(p, kx, y, kw, "Klassifizierung und Eigenschaften")
    p.box(kx, ky, kw, 42, "KI-Vorschlag (Top 3):  ● Korrespondenz 86 %   ○ Nachtrag 9 %   ○ Rechnung 3 %", "ui_ai",
          extra="fontSize=10;")
    mk(p, kx + kw - 14, ky - 8, 3)
    ky += 50
    ky = frow(p, kx, ky, kw, [("A1 Postklasse (Kategorie)", "K-07 Korrespondenz", "select", {"star": True}),
                              ("A2 Mandant", "10010 · Livos Objektges. Nord", "ai", {"star": True, "n": 4})])
    ky = frow(p, kx, ky, kw, [("A3 Empfängergruppe", "Gruppe Vertragsmanagement", "ai", {"star": True, "n": 5}),
                              ("A4 Priorität", "normal", "select", {"star": True})])
    ky = frow(p, kx, ky, kw, [("A5 Posttyp", "gescannt", "ro"), ("A6 Eingangsdatum", "26.09.2026", "ro"),
                              ("A7 Absender", "Musterbau GmbH", "ai")])
    ky = fld(p, kx, ky, kw, "A8 Kommentar", "Original liegt im Postfach Vertragsmanagement", "input")
    btns_r(p, 1218, 488, [("Dokument zurückstellen", "ui_btn2"), ("Stapel freigeben / verteilen", "ui_btn")], fs=10, h=26)
    # ---------- Teil B
    by = 548
    ui_window(p, WX, by, WW, 496, "mail dispatcher › Gruppenpostkorb Vertragsmanagement",
              crumbs="Teil B · Digitaler Posteingang", user="Tim B. (Vertragsmanagement)",
              nav_items=["**Aufgabenlisten**", "", "Meine Aufgaben (2)", "An mich gesendet (1)", "An mich und andere (0)", "",
                         "**Gruppenpostkörbe**", "", "▸ Vertragsmanagement (4)", "   Rechnungseingang (9)", "   Recht (1)"], nav_w=190)
    mk(p, WX + 164, by + 64, 6)
    cx0, cy0 = WX + 202, by + 68
    vw = 370
    ui_viewer(p, cx0, cy0, vw, 410, "Dokument: Schreiben Musterbau GmbH 22.09.2026",
              ["Musterbau GmbH", "Industriestr. 5", "", "Livos Objektgesellschaft", "Nord mbH", "",
               "22.09.2026", "", "Betreff: Bauzeitverlängerung", "BV Hafenstraße 22", "", "Sehr geehrte Damen und Herren,", "…"])
    rx = cx0 + vw + 16
    rw = 1218 - rx
    ry = cy0
    ry = fld(p, rx, ry, rw, "B1 Betreff der Aufgabe", "Digitaler Posteingang: Empfänger:in prüfen", "ro", n=7)
    ry = frow(p, rx, ry, rw, [("B2 Fällig / Erinnerung", "29.09.2026 · Erinnerung nach 2 Tagen", "ro"),
                              ("B3 Zielkategorie", "K-07 Korrespondenz", "select", {"star": True, "n": 8})])
    ry = frow(p, rx, ry, rw, [("B4 Mandant", "10010 · Livos Objektges. Nord", "select", {"star": True}),
                              ("B5 Kreditor-Nr (Pflicht K-06/K-07)", "70012 · Musterbau GmbH", "select", {"star": True, "n": 9})])
    ry = frow(p, rx, ry, rw, [("B6 Objekt-ID (bei Objektbezug)", "10010-0001 · BV Hafenstraße 22", "select"),
                              ("B7 Dokumentdatum", "22.09.2026", "ai", {"star": True})])
    ry = frow(p, rx, ry, rw, [("B7 Betreff", "Bauzeitverlängerung BV Hafenstraße 22", "ai", {"star": True, "wt": 1.4}),
                              ("B7 Absender", "Musterbau GmbH", "ai", {"star": True})])
    ry = fld(p, rx, ry, rw, "B8 Weiterleitungskommentar (vordefiniert oder frei)", "Bitte Frist prüfen", "select")
    btns(p, rx, ry, [("Übernehmen", "ui_btn2"), ("✔ Es ist für mich", "ui_btn"), ("An Kollegen*in senden", "ui_btn2"),
                     ("An Posteingang", "ui_btn2")], fs=10, h=26, gap=6)
    mk(p, 1196, ry - 16, 10)
    ry += 34
    p.box(rx, ry, 300, 18, "Schnellaktionen (max. 20):", "small", extra="verticalAlign=middle;fontStyle=1;")
    cxx = rx
    for t in ["An Rechnungseingang", "An Vertragsmanagement", "An Recht", "Rechnung in ER-Strecke"]:
        cxx = pill(p, cxx, ry + 20, t, C['teal_l'], C['teal'], fs=9, w=int(5.6 * len(t) + 16)) + 6
    mk(p, 1196, ry + 20, 11)
    card(p, WX, 1056, WW, None,
         "**Regeln (14.15):** Postdokumente im Status Freigabe · Person als Erstempfänger erzeugt keine Aufgabe · jede Weiterleitung wird protokolliert · "
         "B7 bildet den Titel „Betreff, Dokumentdatum\" · B8 vordefiniert oder frei.", "note", fs=10, h=44)
    ny = notes(p, RX, ny, RW, [
        (1, "Teil A – Stapelliste links: Poststapel des Tages (inbound scan) [S]."),
        (2, "Seiten mit Trennern: KI-Trenner orange/blau (Vorschlag), manuelle Trenner grün; Korrektur per Klick [S]."),
        (3, "A1 Postklasse: KI-Vorschlag Top 3; < 80 % → „Unbestimmt\" → manuelle Auswahl (Katalog 12.2.4) [K]."),
        (4, "A2 Mandant aus dem Trennblatt-Barcode (SYS) oder manuell – ohne Mandant keine Verteilung."),
        (5, "A3 Empfängergruppe berechnet aus Postklasse + Mandant, immer eine Gruppe. A4 Priorität normal/hoch, A5 Posttyp und A6 Eingangsdatum vom System."),
        (6, "Teil B – mail dispatcher: Aufgabenlisten (Meine Aufgaben · An mich gesendet · An mich und andere · Gruppenpostkörbe) [S]."),
        (7, "B1/B2 vom System: Betreff der Aufgabe, Fälligkeit, Erinnerung nach Tagen; Eskalation über Priorität."),
        (8, "B3 Zielkategorie (aus A1) Pflicht bei „Es ist für mich\"; B4 Mandant aus A2."),
        (9, "B5 Kreditor-Nr Pflicht für K-06/K-07 (Lieferant); B6 Objekt-ID Pflicht für K-02, K-03, K-04 mit Objektbezug."),
        (10, "Übernehmen sperrt die Gruppenaufgabe · Es ist für mich = Zielkategorie + Ablegen, Aufgabe quittiert, Aktenbildung · An Kollegen*in senden (mit Kommentar) · An Posteingang senden [S]."),
        (11, "Schnellaktionen (max. 20) [S]/[K]; „Rechnung in ER-Strecke\" = Import über das ER-Importprofil (12.2.6) [K]/[O]."),
    ], fs=10)
    field_legend(p, RX, ny + 6)
    return p


# ================================================================ M-16
def mdis_window(p, x, y, w, h, title, user):
    p.box(x, y, w, h, "", "ui_win")
    p.box(x, y, w, 38, "", "rounded=0;fillColor=%s;strokeColor=%s;" % (C['green'], C['green']))
    p.box(x + 10, y + 7, 64, 24, "MDIS", "rounded=1;arcSize=20;fillColor=#FFFFFF;strokeColor=none;fontStyle=1;fontSize=12;fontColor=%s;"
          % C['navy'])
    p.box(x + 84, y + 4, 600, 30, title, "text", extra="fontSize=13;fontStyle=1;fontColor=#FFFFFF;verticalAlign=middle;")
    p.box(x + w - 330, y + 8, 320, 22, f"BeSync · Mandantenübergreifend   👤 {user}", "text",
          extra="fontSize=10;fontColor=#FFFFFF;align=right;verticalAlign=middle;")
    p.box(x, y + 38, w, 30, "", "rounded=0;fillColor=%s;strokeColor=%s;" % (C['green_l'], C['green']))
    cx = x + 10
    for i, t in enumerate(["Lieferanten", "Kreditor-Mapping", "Anlage-Anforderungen (3)", "FSB-Übersicht", "Änderungsprotokoll"]):
        tw = int(6.6 * len(t) + 26)
        p.box(cx, y + 42, tw, 24, t, "rounded=1;arcSize=20;fontSize=10;fillColor=%s;strokeColor=%s;fontColor=%s;%s"
              % ("#FFFFFF" if i == 0 else C['green_l'], C['green'] if i == 0 else C['green_l'], C['navy'], "fontStyle=1;" if i == 0 else ""))
        cx += tw + 6


MB = "rounded=1;arcSize=20;fillColor=%s;strokeColor=%s;fontColor=#FFFFFF;fontStyle=1;" % (C['green'], C['green'])
MB2 = "rounded=1;arcSize=20;fillColor=#FFFFFF;strokeColor=%s;fontColor=%s;fontStyle=1;" % (C['green'], C['navy'])
MBR = "rounded=1;arcSize=20;fillColor=#FFFFFF;strokeColor=%s;fontColor=%s;fontStyle=1;" % (C['red'], C['red'])


def page38(doc):
    p, ny = frame(doc, "p38", "M-16 Lieferanten-App",
                  "Rolle: R-12 (Pflege), R-02 (Anforderung), R-06 (Rückmeldung Anlage) · Werkzeug: bestehende MDIS-App auf BeSync (Erweiterung), "
                  "Link aus Startseite und Klärfall (M-05) · Umsetzung: [A] – Oberfläche an die bestehende App anpassen, Struktur ist ein Vorschlag",
                  "AO")
    mdis_window(p, WX, WY, WW, 610, "Lieferanten-App · Lieferantenstamm", "Sven R. (Fachadministration)")
    x0, y = 52, WY + 80
    # Lieferantenliste
    lw = 270
    p.box(x0, y, lw, 28, "🔍  Name, Konsolidierungsnr., USt-IdNr., Kreditor-Nr", "ui_input", extra="fontSize=10;")
    mk(p, x0 + lw - 22, y - 16, 1)
    tbl(p, x0, y + 36, [170, 100], [
        ["Lieferant", "Konsol.-Nr"],
        ["Musterbau GmbH", "LK-000482"],
        ["Musterbau Gebr. GmbH ⚠ Dublette?", "LK-000517"],
        ["Elbe Haustechnik KG", "LK-000311"],
        ["Hansa Gerüstbau GmbH", "LK-000209"],
        ["Nordlicht Elektro GmbH", "LK-000377"],
        ["Nordhaus Hausverwaltung GmbH", "LK-000126"],
        ["Steinmetz Tiefbau AG", "LK-000455"]], rowh=34, fs=10, hl=(1,),
        cell=lambda ri, ci: "fontColor=%s;" % C['red'] if ri == 2 and ci == 0 else "")
    by_ = y + 36 + 34 * 8 + 10
    p.box(x0, by_, lw, 26, "＋ Lieferant anlegen", MB, extra="fontSize=10;")
    p.box(x0, by_ + 32, lw, 26, "Dubletten zusammenführen", MB2, extra="fontSize=10;")
    mk(p, x0 + lw - 10, by_ - 8, 2)
    # Stamm
    mx = x0 + lw + 16
    mw = 500
    my = sec(p, mx, y, mw, "Block 1 – Lieferantenstamm: Musterbau GmbH")
    my = frow(p, mx, my, mw, [("1.1 Konsolidierungsnummer", "LK-000482", "ro", {"star": True, "n": 3, "wt": .6}),
                              ("1.2 Name, Anschrift", "Musterbau GmbH · Industriestr. 5 · 22113 Hamburg", "req", {"wt": 1.4})])
    my = frow(p, mx, my, mw, [("1.3 USt-IdNr. / Steuernummer", "DE123456789", "input", {"n": 4}),
                              ("1.4 E-Mail Rechnungskorrespondenz", "rechnung@musterbau.example", "input", {"n": 5})])
    my = frow(p, mx, my, mw, [("1.5 Bankverbindungen (Anzeige, führend DATEV)", "DE12 3456 7890 … · 2 Verbindungen", "ro", {"wt": 1.4}),
                              ("1.6 Bauleistender (§ 13b/§ 48)", "☑ ja", "input", {"wt": .6, "n": 6})])
    # Mapping
    my = sec(p, mx, my + 4, mw, "Block 2 – Kreditor-Mapping je Mandant", 7)
    ye = tbl(p, mx, my, [150, 84, 80, 96, 90], [
        ["2.1 Mandant", "2.2 DATEV-Kreditor (70000er)", "2.3 HV-Kreditor (80000er)", "2.4 Mapping-Status", "Aktion"],
        ["10010 Livos Objektges. Nord mbH", "70012", "80412", "bestätigt", ""],
        ["10020 Livos Objektges. Süd mbH", "70388", "–", "vorgeschlagen (KI)", "✔ / ✖"],
        ["10030 Livos Bau & Projekt GmbH", "–", "–", "Anlage angefordert", ""],
        ], rowh=34, fs=10, hh=40,
        cell=lambda ri, ci: ("fillColor=%s;" % C['blue_l'] if ri == 2 and ci == 3 else "") +
        ("fillColor=%s;" % C['grey_l'] if ci in (0, 1) and ri > 0 else ""))
    btns(p, mx, ye + 8, [("Mapping bestätigen", MB), ("Mapping ablehnen", MBR)], fs=10, h=26, gap=6)
    p.box(mx, ye + 42, mw, 36, "KI-Vorschlag (X.One): 10020 / 70388 „Musterbau GmbH\" – Übereinstimmung Name, USt-IdNr., IBAN. "
          "Schlüssel = Mandantennr + Kreditornr.", "ui_hint")
    # FSB und Anforderungen
    fx = mx + mw + 16
    fw = 1218 - fx
    fy = sec(p, fx, y, fw, "Block 3 – Freistellungsbescheinigung", 8)
    fy = fld(p, fx, fy, fw, "3.1 FSB gültig bis (Pflicht für Bauleistende)", "31.12.2027", "req")
    fy = fld(p, fx, fy, fw, "3.2 FSB-Prüfnachweis (EIBE-Abfrage, Datum)", "BZSt-Portal geprüft · 12.01.2026", "input", star=True)
    fy = fld(p, fx, fy, fw, "3.3 FSB-Dokument (Link auf K-06)", "📄 Freistellungsbescheinigung § 48b ↗", "ro")
    btns(p, fx, fy, [("FSB erfassen", MB2)], fs=10, h=26)
    fy += 40
    fy = sec(p, fx, fy, fw, "Block 4 – Anlage-Anforderung an Trios", 9)
    fy = fld(p, fx, fy, fw, "4.1 Mandant, Beleg-ID, angefordert von / am", "10030 · SI-2026-004711 · M. Lorenz · 22.09.2026", "ro", h=40,
             star=True)
    fy = fld(p, fx, fy, fw, "4.2 Anforderungsstatus (schreibbar für R-06)", "bei Trios", "select")
    p.box(fx, fy, fw, 34, "angefordert → bei Trios → angelegt → synchronisiert", "small")
    btns(p, fx, fy + 40, [("Anlage anfordern (Mail/Aufgabe)", MB)], fs=10, h=26)
    # Fußbereich im Fenster
    ay = 676
    p.line(x0, ay - 10, 1218, ay - 10)
    btns_r(p, 1218, ay, [("Änderungsprotokoll anzeigen", MB2), ("Speichern", MB)], fs=11, h=28)
    mk(p, 1196, ay - 22, 10)
    p.box(x0, ay, 700, 28, "Letzte Änderung: 22.09.2026 · S. Richter · Mapping 10010 bestätigt", "small", extra="verticalAlign=middle;")
    # Datenflüsse
    fy2 = 752
    p.box(WX, fy2, 800, 22, "Datenflüsse der Lieferanten-App (Vorschlag)", "h2", extra="fontSize=13;")
    flows = [("DATEV (LDconnect)\nKreditoren je Mandant", "ext"), ("Lieferanten-App\n(BeSync, MDIS)", "mdis"),
             ("d.velop documents\nDMS-Eigenschaft E-07 am Beleg", "dvelop_l"), ("Trios (R-06)\nAnlage-Anforderung", "ext")]
    xs = [WX, WX + 330, WX + 660, WX + 990]
    ids = []
    for (t, st), fx_ in zip(flows, xs):
        ids.append(p.box(fx_, fy2 + 34, 200, 52, t, st, extra="fontSize=11;"))
    p.edge(ids[0], ids[1], "S-05 Kreditoren", "data")
    p.edge(ids[1], ids[2], "Konsolidierungsnr. (AE-09)", "data")
    p.edge(ids[1], ids[3], "Anlage-Anforderung (Mail/Aufgabe)", "data", exit=(0.5, 1), entry=(0.5, 1),
           points=[(WX + 430, fy2 + 116), (WX + 1090, fy2 + 116)])
    p.box(WX + 880, fy2 - 2, 310, 30, "FSB-Status / Zahlstatus kommen über BeSync als DMS-Eigenschaften an Akte und Beleg (E-21, E-23).", "small")
    card(p, WX, 900, WW, None,
         "**Regeln (14.16):** Schreibend in den smart-invoice-Bucket nur LDconnect · die App schreibt die Konsolidierungsnummer als DMS-Eigenschaft an den Beleg (AE-09) · "
         "Livos pflegt keine technischen Middleware-Tabellen (P3).", "note", fs=10, h=44)
    ny = notes(p, RX, ny, RW, [
        (1, "Lieferantenliste links: Suche nach Name, Konsolidierungsnummer, USt-IdNr., Kreditor-Nr."),
        (2, "Lieferant anlegen · Dubletten zusammenführen (Hinweis „Dublette?\" aus der Dublettenprüfung) [A]."),
        (3, "1.1 Konsolidierungsnummer: von der App vergeben (SYS), gesellschaftsübergreifend eindeutig, nur lesen."),
        (4, "1.2 Name/Anschrift Pflicht; 1.3 USt-IdNr./Steuernummer (MAN/DATEV) für die Dublettenprüfung."),
        (5, "1.4 E-Mail = Empfänger der Rückweisungsmail (M-06); 1.5 Bankverbindungen nur Anzeige, führend DATEV."),
        (6, "1.6 Kennzeichen Bauleistender (§ 13b/§ 48) für WF-02."),
        (7, "Block 2: Mapping je Mandant – DATEV-Kreditor (S-05) nur lesen, HV-Kreditor aus PM-Daten; Status vorgeschlagen (KI) · bestätigt · abgelehnt."),
        (8, "Block 3: FSB gültig bis (Pflicht für Bauleistende), Prüfnachweis (manuelle EIBE-Abfrage im BZSt-Portal), Link auf K-06 (AE-15)."),
        (9, "Block 4: Anlage-Anforderung aus dem Klärfall (M-05) an Trios; Status pflegt R-06."),
        (10, "Änderungsprotokoll je Lieferant [A]."),
    ], fs=10)
    ny = legend_box(p, RX, ny + 6, [(MB, "Primäraktion im MDIS/BeSync-Look"), ("mdis", "MDIS BeSync (Anpassung [A])")],
                    "Hinweis Darstellung", RW)
    field_legend(p, RX, ny + 8)
    return p


# ================================================================ M-17
def page39(doc):
    p, ny = frame(doc, "p39", "M-17 Freigabematrix-Pflege",
                  "Rolle: R-12 (Pflege), GF (Freigabe der Änderung) · Werkzeug: smart invoice Administration › Freigabematrizen › Matrix wählen; "
                  "alternativ API-Import aus Excel-Vorlage über BeSync [A] · Umsetzung: [S] Matrix; [K] Spalten und Zeilen",
                  "SKAO")
    ui_window(p, WX, WY, WW, 480, "smart invoice › Administrieren › Freigabematrizen",
              crumbs="Administrieren › Freigabematrizen › Freigabe Stufe 1", user="Sven R. (Fachadministration)")
    x0, y = 52, 180
    lw = 220
    tbl(p, x0, y, [lw], [["Freigabematrizen"], ["Freigabe Stufe 1"], ["Freigabe Stufe 2 (GF)"], ["Zahlungsfreigabe"],
                         ["PM-Freigabe (WF-03)"], ["Sachliche Prüfer"]], rowh=32, fs=11, hl=(1,))
    mk(p, x0 + lw - 22, y + 4, 1)
    p.box(x0, y + 32 * 6 + 8, lw, 60, "Je Freigabestufe eine eigene Matrix; Untergrenze über die Strategie „Von unten zum Freigeber\".",
          "small")
    mx = x0 + lw + 16
    mw = 620
    btns(p, mx, y, [("＋ Spalte hinzufügen", "ui_btn2"), ("＋ Zeile hinzufügen", "ui_btn2"), ("Speichern", "ui_btn"),
                    ("⬇ Export (Rezertifizierung)", "ui_btn2")], fs=10, h=26, gap=6)
    mk(p, mx + mw - 22, y + 3, 2)
    ty = y + 50
    ye = tbl(p, mx, ty, [150, 92, 76, 84, 128, 90], [
        ["1 Bearbeiter", "2 Freigabe- grenze (netto)", "3 Mandant", "4 Kosten- stelle", "5 Kostenträger / Objekt", "6 Segment"],
        ["SI_Freigeber_10010", "5.000,00", "10010", "", "10010-0001", "Bau"],
        ["SI_Freigeber_10010", "5.000,00", "10010", "", "", "Bestand"],
        ["SI_Freigeber_10020", "5.000,00", "10020", "", "", "Bestand"],
        ["SI_Freigeber_10020", "25.000,00", "10020", "4100", "", "Privatisierung"],
        ["SI_Freigeber_10030", "50.000,00", "10030", "", "10030-0001", "Bau"],
        ["J. Krüger (Person)", "2.500,00", "10030", "4200", "", ""]], rowh=32, fs=10, hl=(1,), hh=40)
    mk(p, mx + 128, ty - 22, 3)
    mk(p, mx + 220, ty - 22, 4)
    mk(p, mx + 296, ty - 22, 5)
    p.box(mx, ye + 6, mw, 20, "Feste Spalten 1–2 · Zusatzspalten 3–6 (bis 20 Spalten) · Zeile markiert → Zeileneditor", "small")
    p.box(mx, ye + 32, mw, 30, "✖ BeSync-Prüfung [A]: Mandant 10030 fehlt in „Freigabe Stufe 2 (GF)\" – mind. eine Zeile je Gesellschaft und Stufe.",
          "ui_err")
    mk(p, mx + mw - 10, ye + 24, 6)
    p.box(mx, ye + 70, mw, 30, "⏳ Änderung wartet auf Vier-Augen-Freigabe durch GF (Kapitel 13.8.2) – eingereicht 25.09.2026, S. Richter",
          "ui_hint")
    mk(p, mx + mw - 10, ye + 62, 7)
    # Zeileneditor
    ex = mx + mw + 16
    ew = 1218 - ex
    ey = sec(p, ex, y, ew, "Zeileneditor")
    ey = fld(p, ex, ey, ew, "1 Bearbeiter (Person oder Gruppe)", "SI_Freigeber_10010", "select", star=True)
    ey = fld(p, ex, ey, ew, "2 Freigabegrenze (netto, je Kostenobjekt)", "5.000,00 €", "req")
    ey = fld(p, ex, ey, ew, "3 Mandant (Groß-/Kleinschreibung!)", "10010", "req")
    ey = fld(p, ex, ey, ew, "4 Kostenstelle", "", "input")
    ey = fld(p, ex, ey, ew, "5 Kostenträger / Objekt", "10010-0001", "select")
    ey = fld(p, ex, ey, ew, "6 Segment (optional, Vorschlag)", "Bau", "select")
    btns(p, ex, ey, [("Übernehmen", "ui_btn"), ("Zeile löschen", "ui_btn_r")], fs=10, h=26, gap=6)
    mk(p, ex + ew - 22, y - 2, 8)
    # unten
    by = 612
    p.box(WX, by, 760, 22, "Stufenlogik (AE-05) – ohne Spalten „Stufe\" und „Betrag von/bis\"", "h2", extra="fontSize=13;")
    sx, prev = WX, None
    for t, st in [("Rechnung\nnetto 12.400 €", "task_ext"), ("Matrix „Freigabe Stufe 1\"\nGrenze je Kostenobjekt", "task_d"),
                  ("Matrix „Freigabe Stufe 2 (GF)\"\nWertgrenzen-Verbindung", "task_d"), ("Zahlungsfreigabe\n(R-05)", "task")]:
        cid = p.box(sx, by + 32, 170, 56, t, st, extra="fontSize=10;")
        if prev:
            p.edge(prev, cid, "", "flow")
        prev, sx = cid, sx + 200
    p.box(WX, by + 96, 770, 34, "Strategie „Von unten zum Freigeber\": gesucht wird der erste Bearbeiter, dessen Grenze den Betrag deckt – "
          "die Untergrenze ergibt sich aus der nächstniedrigeren Zeile [S]/[K].", "small")
    card(p, 830, by, 400, "Beispiel Rechnung 12.400 € netto, Mandant 10010, Objekt 10010-0001",
         "Stufe 1: Zeile „SI_Freigeber_10010 · 5.000,00 · 10010-0001\" deckt den Betrag nicht → nächste Zeile bzw. Stufe 2 (Leitung Asset Management, bis 25.000 €) übernimmt. "
         "Grenzen gelten netto und je Kostenobjekt.", "info", fs=10)
    ey2 = 780
    p.box(WX, ey2, 900, 22, "Alternative: Pflege per Excel-Vorlage und API-Import über BeSync [A]", "h2", extra="fontSize=13;")
    sx, prev = WX, None
    for t, st in [("Excel-Vorlage je Stufe\npflegen (R-12)", "task_ext"), ("Vier-Augen-Freigabe\nder Änderung (GF)", "task"),
                  ("BeSync: API-Import\nZeilen im Batch", "task_mdis"), ("BeSync-Prüfung: ≥ 1 Zeile\nje Gesellschaft und Stufe", "task_mdis"),
                  ("Freigabematrix in\nsmart invoice aktualisiert", "task_d")]:
        cid = p.box(sx, ey2 + 32, 190, 56, t, st, extra="fontSize=10;")
        if prev:
            p.edge(prev, cid, "", "flow")
        prev, sx = cid, sx + 250
    card(p, WX, 900, WW, None,
         "**Regeln (14.17):** Änderungen nur nach Vier-Augen-Freigabe (Kapitel 13.8.2) · jede Gesellschaft braucht mindestens eine Zeile je Stufe (Prüfung durch BeSync [A]) · "
         "Aktionen: Zeile hinzufügen/ändern/löschen · Spalte hinzufügen (bis 20) · Speichern · Export der Matrix für die Rezertifizierung [S]/[O].",
         "note", fs=10, h=48)
    ny = notes(p, RX, ny, RW, [
        (1, "Matrixliste links: je Freigabestufe eine eigene Matrix (z. B. „Freigabe Stufe 1\", „Freigabe Stufe 2\") [K]."),
        (2, "Oben: Spalte hinzufügen (bis 20), Zeile hinzufügen, Speichern, Export für die Rezertifizierung [S]/[O]."),
        (3, "Spalte 1 Bearbeiter (fest, Pflicht): Person oder Gruppe – Gruppen bevorzugt (SI_Freigeber_<Nr>)."),
        (4, "Spalte 2 Freigabegrenze (fest, Pflicht): netto, gilt je Kostenobjekt."),
        (5, "Spalten 3–6 Zusatzspalten: Mandant (Pflicht, Groß-/Kleinschreibung beachten), Kostenstelle, Kostenträger/Objekt, Segment (optional, Vorschlag)."),
        (6, "Vollständigkeitsprüfung durch BeSync: mindestens eine Zeile je Gesellschaft und Stufe [A]."),
        (7, "Vier-Augen-Freigabe der Änderung durch GF (Kapitel 13.8.2)."),
        (8, "Zeileneditor rechts bearbeitet die markierte Zeile."),
    ], fs=10)
    field_legend(p, RX, ny + 10)
    return p


# ================================================================ M-18
def page40(doc):
    p, ny = frame(doc, "p40", "M-18 Vertretung / Abwesenheit",
                  "Rolle: alle; R-12 und Vorgesetzte mit administrativen Rechten für Dritte (T-39, AE-17) · Werkzeug: Startseite › Profilbild › "
                  "Abwesenheitsstatus; d.velop mobile; Vertretungsregeln unter Konfiguration › Aufgaben und Prozesse › Vertretungsregeln · Umsetzung: [S]",
                  "S")
    ui_window(p, WX, WY, WW, 560, "Startseite", crumbs="Start", nav_items=DV_NAV, user="Jana K. (Asset Management)")
    # abgedunkelte Startseite
    for i, t in enumerate(["Meine Aufgaben (7)", "Rechnungseingangsbuch", "Zuletzt bearbeitet", "Gespeicherte Suchen"]):
        p.box(234 + (i % 2) * 490, 190 + (i // 2) * 240, 470, 220, t, "ui_widget")
    p.box(WX, WY + 34, WW, 526, "", "rounded=0;fillColor=%s;strokeColor=none;opacity=45;" % C['navy'])
    # Profilmenü
    p.box(1000, 150, 220, 118, "👤 Jana Krüger\n─────────────\n● Abwesenheitsstatus …\n   Profil\n   Einstellungen\n   Abmelden",
          "ui_widget", extra="fontSize=11;")
    mk(p, 1196, 140, 1)
    # Dialog
    dx, dy, dw, dh = 330, 190, 600, 410
    p.box(dx, dy, dw, dh, "", "rounded=1;arcSize=2;fillColor=#FFFFFF;strokeColor=%s;shadow=1;" % C['grey'])
    p.box(dx, dy, dw, 40, "Abwesenheitsstatus festlegen", "ui_bar", extra="rounded=0;")
    p.box(dx + dw - 40, dy + 8, 28, 24, "✕", "text", extra="fontColor=#FFFFFF;align=center;verticalAlign=middle;")
    fx, fw = dx + 24, dw - 48
    fy = dy + 56
    fy = fld(p, fx, fy, fw, "Benutzer (andere nur mit administrativen Rechten)", "Jana Krüger (eigenes Konto)", "select", star=True, n=2)
    fy = frow(p, fx, fy, fw, [("Start", "29.09.2026  08:00        🕒 jetzt", "req", {"n": 3}),
                              ("Ende (leer = unbegrenzt)", "10.10.2026  18:00", "input", {"n": 4})])
    fy = fld(p, fx, fy, fw, "Vertretung", "Tim Brandt (Asset Management Nord)", "select", star=True, n=5)
    p.box(fx, fy - 4, fw, 36, "Hinweis: Vertretung möglichst aus demselben Gesellschaftsverbund wählen; Zahlungsfreigaben nur an R-05 (Zahlungsfreigeber).",
          "ui_hint")
    fy += 40
    fy = fld(p, fx, fy, fw, "Nachricht (Abwesenheitsnotiz)",
             "Ich bin bis 10.10.2026 nicht im Büro. Freigaben übernimmt Tim Brandt.", "input", h=62, n=6)
    p.line(fx, fy + 4, fx + fw, fy + 4)
    btns_r(p, fx + fw, fy + 16, [("Aufgaben gesammelt weiterleiten", "ui_btn2"), ("Abwesenheit beenden", "ui_btn_r"),
                                 ("Speichern", "ui_btn")], fs=10, h=28, gap=6)
    mk(p, fx + fw - 12, fy + 50, 7)
    # mobile
    mx, my = 1020, 290
    p.box(mx, my, 190, 356, "", "rounded=1;arcSize=8;fillColor=#FFFFFF;strokeColor=%s;strokeWidth=3;" % C['navy'])
    p.box(mx + 10, my + 16, 170, 30, "d.velop mobile", "ui_bar", extra="fontSize=11;")
    p.box(mx + 10, my + 56, 170, 250, "**Abwesenheit**\n\nStart\n29.09.2026 08:00\n\nEnde\n10.10.2026 18:00\n\nVertretung\nTim Brandt ▾\n\nNachricht\nIch bin bis …",
          "text", extra="fontSize=10;")
    p.box(mx + 30, my + 312, 130, 26, "Speichern", "ui_btn", extra="fontSize=10;")
    mk(p, mx + 168, my - 8, 8)
    # Vertretungsregeln
    by = 700
    p.box(WX, by, 700, 22, "Vertretungsregeln (Konfiguration › Aufgaben und Prozesse › Vertretungsregeln) – Beispiel", "h2",
          extra="fontSize=13;")
    mk(p, WX + 690, by + 1, 9)
    tbl(p, WX, by + 28, [300, 280, 270, 340], [
        ["Aufgabentyp", "Vertretung", "Sichtbarkeit für Vertretung", "Hinweis (Vorschlag)"],
        ["smart invoice – Sachliche Prüfung / Freigabe", "erlaubt", "nur persönlich zugestellte Aufgaben", "Vertretung wird Workflowbeteiligte (L*)"],
        ["smart invoice – Zahlungsfreigabe", "nur an R-05", "nur persönlich zugestellte Aufgaben", "Vertretungsausschluss für andere Rollen"],
        ["mail dispatcher – Postaufgaben", "erlaubt", "persönliche Aufgaben", "Gruppenpostkörbe bleiben bei der Gruppe"],
        ["process studio – Vertragsfreigabe", "erlaubt", "persönliche Aufgaben", "Beispiel, Festlegung Kapitel 13.7"]], rowh=30, fs=10)
    card(p, WX, by + 190, WW, None,
         "**Regeln (14.18):** Die Vertretung übernimmt die Rechte für die Aufgaben · in smart invoice sieht sie nur persönlich zugestellte Aufgaben · "
         "Vertretungsausschluss je Aufgabentyp möglich (Kapitel 13.7) · für erkrankte Kollegen setzen Administrator oder Vorgesetzte die Abwesenheit (T-39).",
         "note", fs=10)
    ny = notes(p, RX, ny, RW, [
        (1, "Aufruf: Startseite › Profilbild › Abwesenheitsstatus [S]."),
        (2, "Benutzer: eigenes Konto (SYS); Auswahl anderer Benutzer nur mit administrativen Rechten (R-12, Vorgesetzte) – z. B. für erkrankte Kollegen."),
        (3, "Start Pflicht, auch vorab planbar; „jetzt\" per Uhrsymbol."),
        (4, "Ende optional – leer = unbegrenzt."),
        (5, "Vertretung Pflicht; Hinweis: möglichst derselbe Gesellschaftsverbund, Zahlungsfreigabe nur an R-05."),
        (6, "Nachricht = Abwesenheitsnotiz (optional)."),
        (7, "Aktionen: Speichern · Abwesenheit beenden · Aufgaben gesammelt weiterleiten (nur Berechtigte) [S]."),
        (8, "Gleiche Funktion in d.velop mobile [S]."),
        (9, "Vertretungsregeln je Aufgabentyp in der Konfiguration; Vertretungsausschluss möglich (Kapitel 13.7)."),
    ], fs=10)
    field_legend(p, RX, ny + 10)
    return p


# ================================================================ M-19
def page41(doc):
    p, ny = frame(doc, "p41", "M-19 Externe Benutzeraufgabe",
                  "Rolle: R-10 Ad-hoc-Externe (ohne Lizenz, ohne Konto; Katalog 4.2, WF-10) – nur Stellungnahme, Freigabe bleibt intern · Werkzeug: process studio „Externe Benutzeraufgabe\" – "
                  "E-Mail mit Link auf ein d.velop-forms-Formular, Beleg als Teilen-Link · Umsetzung: [S] Aufgabe/Formular, [K] Formular, [A] Kopplung über BeSync",
                  "SKAO")
    # Browser
    bx, by, bw_, bh = WX, WY, 720, 870
    p.box(bx, by, bw_, bh, "", "ui_win")
    p.box(bx, by, bw_, 34, "", "rounded=0;fillColor=%s;strokeColor=%s;" % (C['grey_m'], C['grey_m']))
    p.box(bx + 10, by + 10, 40, 14, "● ● ●", "text", extra="fontSize=10;fontColor=%s;verticalAlign=middle;" % C['grey'])
    p.box(bx + 60, by + 6, bw_ - 80, 22, "🔒 https://livos.d-velop.cloud/forms/extern/freigabe?task=…", "ui_input",
          extra="fontSize=10;fontColor=%s;" % C['grey'])
    fx, fw = bx + 60, bw_ - 120
    y = by + 56
    p.box(fx, y, 110, 40, "LIVOS", "rounded=0;fillColor=%s;strokeColor=none;fontColor=#FFFFFF;fontStyle=1;fontSize=18;" % C['navy'])
    p.box(fx + 124, y, 420, 40, "Stellungnahme zur Rechnung", "text", extra="fontSize=20;fontStyle=1;fontColor=%s;verticalAlign=middle;" % C['navy'])
    mk(p, fx + fw - 20, y, 1)
    y += 52
    p.box(fx, y, fw, 40, "⏱  Antwort bis 03.10.2026, 18:00 Uhr · noch 6 Tage 23 Std. – danach ist dieses Formular nicht mehr aufrufbar.",
          "ui_hint", extra="fontSize=11;fontStyle=1;")
    mk(p, fx + fw - 20, y + 10, 2)
    y += 48
    p.box(fx, y, fw, 34, "Ihre Stellungnahme ist keine verbindliche Freigabe – die Freigabe der Rechnung erfolgt intern bei Livos.",
          "info", extra="fontSize=10;verticalAlign=middle;")
    mk(p, fx + fw - 20, y + 7, 12)
    y += 44
    y = sec(p, fx, y, fw, "Belegdaten")
    y = fld(p, fx, y, fw, "1 Gesellschaft (Mandantenname)", "Livos Objektgesellschaft Nord mbH", "ro", n=3)
    y = fld(p, fx, y, fw, "2 Kreditorname", "Musterbau GmbH", "ro")
    y = frow(p, fx, y, fw, [("3 Rechnungsnummer", "RE-2026-1041", "ro"), ("Rechnungsdatum", "15.09.2026", "ro")])
    y = frow(p, fx, y, fw, [("4 Bruttobetrag", "14.756,00 €", "ro"), ("Zahlbetrag", "14.756,00 €", "ro")])
    y = fld(p, fx, y, fw, "5 Objekt / Leistung", "BV Hafenstraße 22 · Rohbauarbeiten (Abschlag 4)", "ro")
    y = fld(p, fx, y, fw, "6 Link zum Beleg (nur Lesen, gültig bis 23.03.2027)", "📄 Beleg RE-2026-1041 öffnen ↗", "ro", n=4)
    y = fld(p, fx, y, fw, "7 Antwort bis", "03.10.2026, 18:00 Uhr", "ro", n=5)
    y = sec(p, fx, y + 4, fw, "Ihre Stellungnahme")
    nb = "\u00a0" * 8
    p.box(fx, y, fw, 14, "8 Stellungnahme *", "ui_label")
    p.box(fx, y + 16, fw, 30, f"◉ Keine Einwände{nb}○ Einwände{nb}○ Rückfrage", "ui_req", extra="fontSize=12;")
    mk(p, fx + fw - 12, y + 4, 6)
    y += 56
    y = fld(p, fx, y, fw, "9 Kommentar (Pflicht bei Einwänden / Rückfrage)", "Leistung vor Ort am 12.09.2026 abgenommen.", "input", h=60, n=7)
    y = fld(p, fx, y, fw, "10 Name der entscheidenden Person (Bestätigung, kein Login)", "Dr. Kai Wendt, Wendt Projektsteuerung", "req", n=8)
    btns_r(p, fx + fw, y + 4, [("Absenden", "ui_btn")], fs=12, h=32)
    mk(p, fx + fw - 12, y - 8, 9)
    p.box(fx, y + 50, fw, 40, "Ihre Angaben werden an Livos übermittelt. Kein Zugriff auf weitere Dokumente. · Impressum · Datenschutz",
          "small", extra="align=center;")
    # Rechts: Ablauf, E-Mail, abgelaufen
    rx, rw = bx + bw_ + 20, WW - bw_ - 20
    ry = WY
    p.box(rx, ry, rw, 22, "Ablauf WF-10 (Kopplung über BeSync [A])", "h2", extra="fontSize=13;")
    ry += 30
    steps = [("smart invoice: Stellungnahme eines Externen anfordern", "task_d"), ("BeSync startet Prozess", "task_mdis"),
             ("process studio: externe Benutzeraufgabe + Teilen-Link", "task_d"), ("E-Mail mit Formular-Link", "task_ext"),
             ("Formular ausgefüllt / Timer abgelaufen", "task_ext"), ("BeSync: Stellungnahme an den Beleg – interne Freigabe entscheidet", "task_mdis")]
    for i, (t, st) in enumerate(steps):
        p.box(rx + 20, ry, rw - 40, 40, t, st, extra="fontSize=10;")
        if i < len(steps) - 1:
            p.line(rx + rw / 2, ry + 40, rx + rw / 2, ry + 54, "straight")
        ry += 54
    mk(p, rx + rw - 22, WY, 10)
    ry += 10
    p.box(rx, ry, rw, 22, "E-Mail an den Externen", "h2", extra="fontSize=13;")
    ry += 28
    p.box(rx, ry, rw, 190,
          "**Von:** Livos Rechnungseingang (no-reply)\n**Betreff:** Bitte um Stellungnahme – RE-2026-1041 Musterbau GmbH\n\n"
          "Guten Tag Herr Dr. Wendt,\nbitte geben Sie bis 03.10.2026, 18:00 Uhr Ihre Stellungnahme zur Rechnung ab:\n\n"
          "▸ Zum Formular\n▸ Beleg ansehen (Teilen-Link, nur Lesen)\n\nMit freundlichen Grüßen\nLivos Objektgesellschaft Nord mbH",
          "rounded=1;arcSize=3;fillColor=#FFFFFF;strokeColor=%s;align=left;verticalAlign=top;spacing=8;fontSize=10;shadow=1;" % C['grey_m'])
    ry += 204
    p.box(rx, ry, rw, 22, "Zustand nach Ablauf des Timers", "h2", extra="fontSize=13;")
    ry += 28
    p.box(rx, ry, rw, 110, "", "ui_win")
    p.box(rx + 12, ry + 12, rw - 24, 86, "**⏱ Diese Aufgabe ist abgelaufen.**\nDie Antwortfrist endete am 03.10.2026, 18:00 Uhr. "
          "Das Formular kann nicht mehr aufgerufen werden. Bitte wenden Sie sich an Ihre Ansprechperson bei Livos.", "ui_err",
          extra="fontSize=10;verticalAlign=top;spacingTop=6;")
    mk(p, rx + rw - 22, ry - 26, 11)
    ry += 124
    card(p, rx, ry, rw, "Regeln (14.19)",
         "• Kein Zugriff auf Dokumente in d.velop – der Beleg kommt nur über den Teilen-Link (max. 180 Tage, nur Lesen).\n"
         "• Passwortschutz für Link und Formular nicht dokumentiert → nur geringe Beträge und bekannte Empfänger (Vorschlag) [O].\n"
         "• Ausführungen zählen auf das process-studio-Kontingent (OP-11).", "warn", fs=10)
    ny = notes(p, RX, ny, RW, [
        (1, "Schlichtes Webformular (d.velop forms) mit Livos-Kennzeichnung (Logo), Titel und Frist [K]."),
        (2, "Frist-Hinweis aus dem Timer der externen Benutzeraufgabe: nach Ablauf ist das Formular nicht mehr aufrufbar [S]."),
        (3, "Felder 1–5 nur lesen: ausschließlich gemappte Prozessvariablen (Gesellschaft, Kreditor, Rechnungsnr./-datum, Brutto- und Zahlbetrag, Objekt/Leistung)."),
        (4, "Link zum Beleg = zeitlich begrenzter Teilen-Link: gültig bis Datum, max. 180 Tage, nur Lesen."),
        (5, "Antwort bis (SYS, Timer)."),
        (6, "Stellungnahme Pflicht: Keine Einwände · Einwände · Rückfrage (entspricht Freigeben · Ablehnen · Rückfrage in 14.19, aber unverbindlich)."),
        (7, "Kommentar bedingt Pflicht bei Einwänden/Rückfrage."),
        (8, "Name der entscheidenden Person als Bestätigung – kein Login, keine Lizenz."),
        (9, "Absenden: Prozess läuft weiter; BeSync überträgt die Stellungnahme an den smart-invoice-Beleg; die verbindliche Freigabe trifft der interne Freigeber [S]/[A]."),
        (10, "Kopplung smart invoice ↔ process studio über BeSync [A]."),
        (11, "Timer abgelaufen: Formular gesperrt, Beleg läuft ohne Stellungnahme zurück an die interne Bearbeitung."),
        (12, "Nur Stellungnahme: Externe geben keine verbindliche Freigabe; die Freigabe bleibt intern (Freigabematrix, M-04)."),
    ], fs=10)
    field_legend(p, RX, ny + 10)
    return p


def build(doc):
    for f in (page33, page34, page35, page36, page37, page38, page39, page40, page41):
        f(doc)
