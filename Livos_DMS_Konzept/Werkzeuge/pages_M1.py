"""Masken-Mockups M-01 bis M-10 (Seiten p23–p32) für das Livos DMS-Gesamtkonzept.
Grundlage: Kapitel 14 (K14_masken.md, Abschnitte 14.0–14.10). Aufruf: build(doc)."""
from dio import C, S, ui_window, ui_tabs, ui_viewer

# ---------------------------------------------------------------- Geometrie (smart-invoice-Masken)
WX, WY, WW, WH = 40, 112, 1190, 996          # Fenster
AX, AW = 1250, 364                           # Randspalte Erläuterungen
LX, LW = 52, 716                             # Datenbereich links
VX, VW = 780, 438                            # Belegvorschau rechts
ACT_Y = WY + WH - 44                         # Aktionsleiste

TD_AI = f"fillColor={C['blue_l']};strokeColor={C['grey_m']};fontSize=11;align=left;spacingLeft=4;verticalAlign=middle;"
TD_B = f"fillColor=#FFFFFF;strokeColor={C['grey_m']};fontSize=11;align=left;spacingLeft=4;verticalAlign=middle;fontStyle=1;"
TD_Y = f"fillColor={C['yellow_l']};strokeColor={C['grey_m']};fontSize=11;align=left;spacingLeft=4;verticalAlign=middle;"
TD_R = f"fillColor={C['red_l']};strokeColor={C['grey_m']};fontSize=11;align=left;spacingLeft=4;verticalAlign=middle;"
TD_G = f"fillColor={C['green_l']};strokeColor={C['grey_m']};fontSize=11;align=left;spacingLeft=4;verticalAlign=middle;"
TD_O = f"fillColor={C['orange_l']};strokeColor={C['grey_m']};fontSize=11;align=left;spacingLeft=4;verticalAlign=middle;fontStyle=1;"
TD_GRP = f"fillColor={C['teal_l']};strokeColor={C['grey_m']};fontSize=11;align=left;spacingLeft=6;verticalAlign=middle;fontStyle=1;fontColor={C['navy']};"
TD_GRP2 = f"fillColor={C['grey_l']};strokeColor={C['grey_m']};fontSize=11;align=left;spacingLeft=22;verticalAlign=middle;fontStyle=1;"
HILITE = f"rounded=1;arcSize=3;fillColor={C['orange_l']};strokeColor={C['orange']};opacity=55;"
NB = " "


def _nb(lines):
    return [l.replace(" ", NB) for l in lines]


INV = _nb([
    "Musterbau GmbH · Industriestr. 5 · Hamburg",
    "USt-IdNr. DE 123 456 789",
    "",
    "Livos Objektgesellschaft Nord mbH",
    "Hafenstraße 22 · 20359 Hamburg",
    "",
    "RECHNUNG  RE-2026-1041",
    "Rechnungsdatum:     15.09.2026",
    "Leistungszeitraum:  01.08.–31.08.2026",
    "BV Hafenstraße 22 · Auftrag AV-2026-017",
    "",
    "Pos Leistung                Menge    Betrag",
    "1   Rohbauarbeiten BT A     1 psch  8.400,00",
    "2   Baustelleneinrichtung   1 psch  3.480,00",
    "3   Regiestunden Polier     8 Std     520,00",
    "",
    "Nettobetrag                        12.400,00",
    "USt 19 %                            2.356,00",
    "Rechnungsbetrag                14.756,00 EUR",
    "",
    "Zahlbar in 14 Tagen mit 3 % Skonto,",
    "30 Tage netto.",
    "IBAN DE12 3456 7890 1234 5678 90",
])


# ---------------------------------------------------------------- Bausteine
def mark(p, x, y, n):
    p.box(x, y, 20, 20, str(n), "ann", extra="fontSize=10;")


def fld(p, x, y, w, label, value="", kind="input", h=24, warn=False, n=None, hl=False):
    """Feld mit Label. kind: Kombination aus req, ai, ro, sel, input (mit '+' verbunden)."""
    ks = kind.split("+")
    st, extra = "ui_input", ""
    if "ro" in ks: st = "ui_ro"
    if "ai" in ks: st = "ui_ai"
    if "req" in ks: extra += f"strokeColor={C['teal']};strokeWidth=2;"
    if warn: extra += f"strokeColor={C['red']};strokeWidth=2;fillColor={C['red_l']};fontColor={C['black']};"
    if hl: extra += f"strokeColor={C['orange']};strokeWidth=2;fillColor={C['orange_l']};fontColor={C['black']};fontStyle=1;"
    if h > 30: extra += "verticalAlign=top;spacingTop=4;"
    p.box(x, y, w, 14, label + (" *" if "req" in ks else ""), "ui_label")
    p.box(x, y + 14, w, h, value, st, extra=extra)
    if "sel" in ks:
        p.box(x + w - 18, y + 14, 16, 24, "▾", "textc", extra=f"fontSize=11;fontColor={C['grey']};")
    if n is not None:
        mark(p, x + w - 20, y - 6, n)
    return y + 14 + h + 8


def row(p, x, y, w, specs, gap=10):
    """specs = [(label, value, kind, span[, opt]), ...] im 12-Spalten-Raster."""
    unit = (w + gap) / 12
    cx, ys = x, []
    for s in specs:
        label, value, kind, span = s[:4]
        opt = s[4] if len(s) > 4 else {}
        ys.append(fld(p, cx, y, span * unit - gap, label, value, kind, **opt))
        cx += span * unit
    return max(ys)


def sec(p, x, y, w, title, n=None):
    p.box(x, y, w, 20, title, "ui_sec")
    p.line(x, y + 21, x + w, y + 21, "line")
    if n is not None:
        mark(p, x + w - 20, y - 1, n)
    return y + 26


def kopf(p, x, y, w, text, badges, n=None):
    text = text.replace("   ", NB * 3)
    p.box(x, y, w, 34, text, f"rounded=0;fillColor={C['teal_l']};strokeColor={C['teal']};align=left;spacingLeft=10;fontSize=12;")
    bx = x + w - 8
    for t, st, bw in reversed(badges):
        bx -= bw
        p.box(bx, y + 7, bw, 20, t, st)
        bx -= 8
    if n is not None:
        mark(p, x - 8, y - 8, n)
    return y + 42


def backdrop(p, idx, x, y, w, h, style=HILITE):
    """Hintergrundfläche nachträglich hinter bereits gezeichnete Elemente legen."""
    p.box(x, y, w, h, "", style)
    p.cells.insert(idx, p.cells.pop())


def hint(p, x, y, w, text, st="ui_hint", h=24, n=None):
    p.box(x, y, w, h, text, st, extra="fontSize=10;" + ("verticalAlign=top;spacingTop=3;" if h > 26 else ""))
    if n is not None:
        mark(p, x + w - 24, y + (h - 20) / 2, n)
    return y + h + 4


def _bw(t):
    return max(84, int(6.3 * len(t)) + 26)


def btns(p, x, y, labels, gap=8, right=False):
    ws = [_bw(t) for t, _ in labels]
    if right:
        x = x - sum(ws) - gap * (len(ws) - 1)
    x0 = x
    for (t, st), bw in zip(labels, ws):
        p.box(x, y, bw, 28, t, st)
        x += bw + gap
    return x0, x


def table(p, x, y, colw, rows, rowh=24, styles=None):
    return p.table(x, y, colw, rows, rowh=rowh, styles=styles)


def _lines(text, cpl):
    total = 0
    for para in text.replace("**", "").replace("__", "").split("\n"):
        n, l = 0, 1
        for wd in para.split(" "):
            add = len(wd) + (1 if n else 0)
            if n + add > cpl and n:
                l += 1
                n = len(wd)
            else:
                n += add
        total += l
    return total


def notes(p, x, y, w, items, title="Erläuterungen", fs=10):
    p.box(x, y, w, 22, title, "h2", extra="fontSize=13;")
    cy = y + 28
    cpl = int((w - 36) / (fs * 0.53))
    for n, t in items:
        h = _lines(t, cpl) * (fs + 3) + 8
        p.box(x, cy, 20, 20, str(n), "ann", extra="fontSize=10;")
        p.box(x + 26, cy - 3, w - 26, h, t, "text", extra=f"fontSize={fs};spacingTop=0;")
        cy += max(h, 22) + 5
    return cy


def flegend(p, x, y, w=364):
    rows = [("ui_req", "", "Pflichtfeld (Label mit *) – je Schritt konfiguriert"),
            ("ui_ai", "", "KI-/erkannt (document reader, E-Rechnung, Vorschlag)"),
            ("ui_ro", "", "schreibgeschützt / berechnet (nur lesen)"),
            ("ui_input", "▾", "Auswahl (Werteliste, Stamm, Custom Entity)"),
            ("ui_input", "", "freie Eingabe")]
    h = 30 + 24 * len(rows) + 50
    p.box(x, y, w, h, "", f"rounded=1;arcSize=4;fillColor=#FFFFFF;strokeColor={C['grey_m']};")
    p.box(x + 10, y + 4, w - 20, 20, "Legende Feldarten", "h2", extra="fontSize=12;")
    cy = y + 28
    for st, v, lab in rows:
        p.box(x + 12, cy + 1, 44, 18, v, st, extra="align=right;spacingRight=4;fontSize=10;")
        p.box(x + 64, cy, w - 74, 20, lab, "text", extra="fontSize=10;verticalAlign=middle;")
        cy += 24
    p.box(x + 12, cy + 2, 18, 18, "1", "ann", extra="fontSize=9;")
    p.box(x + 36, cy, w - 46, 22, "Annotation (Erläuterung in der Randspalte)", "text", extra="fontSize=10;verticalAlign=middle;")
    p.box(x + 12, cy + 24, w - 24, 22, "[S] Standard · [K] Konfiguration · [A] Anpassung (BeSync) · [O] offen",
          "text", extra=f"fontSize=10;verticalAlign=middle;fontColor={C['grey']};")
    return y + h


def si_window(p, step, user, crumbs_extra="RE-2026-1041", h=WH, y=WY, x=WX, w=WW):
    return ui_window(p, x, y, w, h, f"smart invoice  ›  {step}",
                     f"Start › Rechnungseingangsbuch › Meine offenen Rechnungen › {crumbs_extra}", user=user)


def rcol(p, items, legend_bottom=True, y=112, title="Erläuterungen"):
    """Randspalte rechts: Annotationen oben, Feldarten-Legende unten."""
    end = notes(p, AX, y, AW, items, title)
    ly = 1120 - 200 if legend_bottom else end + 10
    flegend(p, AX, max(ly, end + 8))
    return end


# =========================================================================================== M-01
def m01(doc):
    p = doc.page("M-01 Rechnung einlesen / Stapel", "p23")
    p.header("M-01 Rechnung einlesen / Stapel",
             "Rolle R-02 Rechnungseingang (R-01 für Papierpost) · Werkzeug: d.velop invoices „Rechnung einlesen“, inbound-Stapelübersicht, Import-Widget · "
             "Umsetzung [S] Funktion, [K] Importprofile, Postfächer, Schlüssel-Wert-Paare · Weg inbound → document reader → smart invoice (AE-22)")
    ui_window(p, WX, WY, WW, WH, "d.velop invoices  ›  Rechnung einlesen",
              "Start › d.velop invoices › Rechnung einlesen › Stapel „rechnung-nord · 16.09.2026 08:12“")
    x0, y0, w0 = 52, 180, 1166
    # Upload-Zone
    p.box(x0, y0, w0, 64, "⇪  Rechnungen hierher ziehen (PDF, ZUGFeRD, XRechnung, Factur-X) – Einzel- oder Mehrfach-Upload",
          f"rounded=1;arcSize=6;dashed=1;fillColor={C['grey_l']};strokeColor={C['teal']};align=left;spacingLeft=16;fontSize=12;fontColor={C['navy']};")
    btns(p, x0 + w0 - 12, y0 + 18, [("Dateien wählen", "ui_btn"), ("🖨 Scannen (scanner connector)", "ui_btn2")], right=True)
    mark(p, x0 - 8, y0 - 8, 1)
    # Stapelliste
    SX, SW = 52, 250
    y = sec(p, SX, 256, SW, "Stapel")
    mark(p, SX + SW - 20, 255, 2)
    stapel = [("rechnung-nord@livos.de · 16.09. 08:12", "3 Dokumente · 7 Seiten", "offen", "badge", True),
              ("Upload Maria L. · 16.09. 09:40", "5 Dokumente · 11 Seiten", "in Verarbeitung", "badge_o", False),
              ("Scan Poststelle (R-01) · 15.09.", "12 Dokumente · 31 Seiten", "abgeschlossen", "badge_g", False),
              ("rechnung-sued@livos.de · 15.09.", "1 Dokument · 2 Seiten", "Fehler", "badge_r", False)]
    for t1, t2, stt, bst, sel in stapel:
        ex = f"strokeColor={C['teal']};strokeWidth=2;" if sel else ""
        p.box(SX, y, SW, 58, f"**{t1}**\n{t2}", "ui_widget", extra="shadow=0;fontSize=10;" + ex)
        p.box(SX + SW - 108, y + 32, 100, 18, stt, bst)
        y += 64
    hint(p, SX, y + 4, SW, "Fehlermails landen im Ordner „dvelop_not_processed“; Jobübersicht mit Neustart [S]", "ui_err", h=44)
    hint(p, SX, y + 54, SW, "Postfach vor Aktivierung bereinigen: alle vorhandenen Mails werden importiert [S]", "ui_hint", h=44)
    hint(p, SX, y + 104, SW, "Keine Nicht-Rechnungen über das ER-Postfach – Post/Verträge an post@… weiterleiten (Regel)", "ui_hint", h=44)
    # Mitte: Stapeleigenschaften
    MX, MW = 316, 520
    y = sec(p, MX, 256, MW, "Stapeleigenschaften")
    y = row(p, MX, y, MW, [("Stapelname", "rechnung-nord · Musterbau GmbH · Rechnung RE-2026-1041", "ro", 12, {"n": 3})])
    y = row(p, MX, y, MW, [("Quelle / Postfach bzw. Alias", "rechnung-nord@livos.de (Alias Nord)", "ro", 7),
                           ("Importprofil", "ER-Postfach Nord", "ro", 5)])
    y = row(p, MX, y, MW, [("Eingangsdatum/-zeit", "16.09.2026 08:12", "ro", 4, {"n": 4}),
                           ("Mandant (Vorbelegung über Alias)", "10010 · Livos Objektgesellschaft Nord mbH", "ro", 8, {"n": 5})])
    y = row(p, MX, y, MW, [("Anzahl Dokumente / Seiten", "3 Dokumente / 7 Seiten (max. 200)", "ro", 7, {"n": 6}),
                           ("Status Stapel", "offen", "ro", 5)])
    # Seiten + Trenner
    y = sec(p, MX, y + 2, MW, "Seiten und Dokumenttrenner", n=7)
    btns(p, MX, y, [("Trenner setzen", "ui_btn2"), ("Trenner entfernen", "ui_btn2"), ("⟳ Drehen", "ui_btn2"), ("🗑 Seite löschen", "ui_btn_r")])
    y += 38
    tx = MX
    pages = [(1, "Rechnung"), (2, "Anlage"), None, (3, "XRechnung"), (4, "Visual."), (5, "Visual."), None, (6, "Lieferschein"), (7, "Lieferschein")]
    seps = iter([("blue", "KI"), ("orange", "man.")])
    for pg in pages:
        if pg is None:
            col, lab = next(seps)
            p.box(tx + 2, y - 4, 6, 92, "", f"rounded=0;fillColor={C[col]};strokeColor=none;")
            tx += 12
            continue
        n, lab = pg
        sel = "strokeColor=%s;strokeWidth=2;" % C['teal'] if n == 1 else ""
        p.box(tx, y, 52, 70, f"S. {n}", f"rounded=0;fillColor=#FFFFFF;strokeColor={C['grey']};fontSize=10;verticalAlign=bottom;shadow=1;" + sel)
        p.box(tx + 8, y + 8, 36, 30, "≡", "textc", extra=f"fontSize=16;fontColor={C['grey_m']};")
        p.box(tx - 4, y + 72, 60, 14, lab, "textc", extra=f"fontSize=9;fontColor={C['grey']};")
        tx += 58
    y += 94
    p.box(MX, y, 14, 10, "", f"rounded=0;fillColor={C['blue']};strokeColor=none;")
    p.box(MX + 18, y - 5, 200, 20, "Trenner KI-Vorschlag", "text", extra="fontSize=10;verticalAlign=middle;")
    p.box(MX + 170, y, 14, 10, "", f"rounded=0;fillColor={C['orange']};strokeColor=none;")
    p.box(MX + 188, y - 5, 200, 20, "Trenner manuell gesetzt", "text", extra="fontSize=10;verticalAlign=middle;")
    y += 22
    # Dokumentliste
    y = sec(p, MX, y, MW, "Dokumente im Stapel", n=8)
    rows = [["✓", "Nr", "Dokumenttyp", "Format", "Seiten", "E-Rechnungs-Prüfbericht"],
            ["☑", "1", "Rechnung  ▾ (S. 2 Anlage)", "PDF", "2", "–"],
            ["☑", "2", "Rechnung  ▾", "XRechnung", "3", "⚠ 1 Warnung (BR-DE-15)"],
            ["☐", "3", "Anlage  ▾  → an Dok. 2", "PDF", "2", "–"]]
    y = table(p, MX, y, [26, 30, 170, 80, 48, 166], rows,
              styles={(1, 3): TD_AI, (2, 3): TD_AI, (3, 3): TD_AI, (2, 5): TD_Y})
    mark(p, MX + 26 + 30 + 170 + 60, y - 4 * 24 - 8, 9)
    y = hint(p, MX, y + 8, MW, "ⓘ Dok. 2 (XRechnung): Prüfbericht mit 1 Warnung – Validierung setzt den neuen\nKommunikationsweg inbound → document reader → smart invoice voraus (AE-22)", "ui_hint", h=36)
    # Vorschau
    ui_viewer(p, 850, 256, 368, 770, "Vorschau Seite 1 von 7 (Großansicht)", INV)
    # Aktionen
    p.line(52, ACT_Y - 10, 1218, ACT_Y - 10)
    btns(p, 52, ACT_Y, [("Dokument ablehnen", "ui_btn_r"), ("Dokument übernehmen", "ui_btn2")])
    x0b, _ = btns(p, 1218, ACT_Y, [("Stapel abschließen & exportieren", "ui_btn")], right=True)
    mark(p, x0b - 12, ACT_Y - 8, 10)
    rcol(p, [
        (1, "**Hochladen / Scannen** – Drag & Drop, „Dateien wählen“ oder Scanner-Symbol legt einen Stapel an; alternativ Import-Widget auf der Startseite [S]."),
        (2, "**Stapelliste** je Quelle mit Status (Feld 10): offen · in Verarbeitung · abgeschlossen · Fehler [S]."),
        (3, "**Stapelname, Quelle, Importprofil** (Felder 1–3) vom System aus Postfach bzw. Alias; das Importprofil bestimmt Standardkategorie, Trennung und OCR [K]."),
        (4, "**Eingangsdatum/-zeit** – Grundlage der Durchlaufzeit [S]."),
        (5, "**Mandant-Vorbelegung** nur bei Alias-Postfach über Schlüssel-Wert-Paar am Alias; Test OP-02 [K]/[O]."),
        (6, "**Anzahl Dokumente/Seiten** berechnet; Import hart auf 200 Seiten begrenzt [S]."),
        (7, "**Trenner setzen/entfernen**, Seite drehen/löschen – nur vor der Übergabe (Fehlscan). Farben: KI-Vorschlag / manuell [S]."),
        (8, "**Dokumenttyp je Dokument** (Rechnung/Anlage, Pflicht); Anlagen werden dem Rechnungs-PDF angehängt (Importprofil-Option). Haken = Dokument übernehmen [S]."),
        (9, "**Format** erkannt: PDF, ZUGFeRD, XRechnung, Factur-X; E-Rechnungs-Prüfbericht nur lesend [S]."),
        (10, "**Stapel abschließen / exportieren** – Übergabe an Erkennung und Workflowstart; bei Postfächern automatisch („Stapel nach Import abschließen“) [S]/[K]."),
    ])


# =========================================================================================== M-02
def m02(doc):
    p = doc.page("M-02 Verteilung", "p24")
    p.header("M-02 Verteilung",
             "Rolle R-02 Rechnungseingang · Werkzeug: smart invoice, Schritt „Verteilung“ (Aufruf aus Meine Aufgaben, REB, E-Mail) · "
             "Umsetzung [S] Schritt und Maske, [K] Layout, Feldkonfiguration, Bedingungen, Custom-Felder")
    si_window(p, "Verteilung", "Maria L. (Rechnungseingang)")
    y = kopf(p, 52, 180, 1166, "**Verteilung**   |   10010 Livos Objektgesellschaft Nord mbH   |   70012 Musterbau GmbH   |   RE-2026-1041   |   **14.756,00 €**",
             [("Skonto 29.09. (3 Tage)", "badge_o", 150), ("Offen", "badge", 80)], n=1)
    y = hint(p, 52, y, 1166, "⚠ Dublettenverdacht: Musterbau GmbH · RE-2026-1041 bereits am 15.09.2026 eingegangen (Beleg SI-2026-004711). "
             "Annahme nur mit Begründung; Ablehnung intern ohne Lieferantenmail.", "ui_err", n=2)
    y = hint(p, 52, y, 1166, "ⓘ Zahlungsbedingung des Belegs (14 Tage 3 % Skonto, 30 Tage netto) weicht vom Kreditorenstandard (30 Tage netto) ab – Bearbeiter entscheidet.", "ui_hint", n=3)
    y = hint(p, 52, y, 1166, "⚠ IBAN (Beleg) DE12 3456 7890 1234 5678 90 weicht von der Stamm-Bankverbindung ab – nicht übernehmen, klären (Anzeigeform Test OP-10).", "ui_err", n=4)
    y = hint(p, 52, y, 1166, "ⓘ § 13b: Kreditor als Bauleistender gekennzeichnet und Steuer > 0 – Reverse Charge prüfen.", "ui_hint")
    top = y + 6
    y = sec(p, LX, top, LW, "A  Zuordnung")
    y = row(p, LX, y, LW, [("Mandant", "10010", "req+ai+sel", 2, {"n": 5}),
                           ("Mandantenname", "Livos Objektgesellschaft Nord mbH", "ro", 4),
                           ("Kreditor", "70012 · Musterbau GmbH", "req+ai+sel", 4, {"n": 6}),
                           ("Eingangskanal", "E-Mail", "ro", 2)])
    y = sec(p, LX, y, LW, "B  Belegkopf")
    y = row(p, LX, y, LW, [("Belegart", "Rechnung", "req+ai+sel", 3, {"n": 7}),
                           ("Rechnungsnummer", "RE-2026-1041", "req+ai", 3),
                           ("Rechnungsdatum", "15.09.2026", "req+ai", 3),
                           ("Leistungsdatum/-zeitraum", "01.08.–31.08.2026", "ai", 3, {"n": 8})])
    y = row(p, LX, y, LW, [("Währung", "EUR", "req+sel", 2),
                           ("Nettobetrag", "12.400,00", "req+ai", 3),
                           ("Steuerbetrag", "2.356,00", "req+ai", 2),
                           ("Bruttobetrag", "14.756,00", "req+ai", 3, {"n": 9}),
                           ("§ 13b Reverse Ch.", "nein", "sel", 2)])
    y = sec(p, LX, y, LW, "C  Zahlung")
    y = row(p, LX, y, LW, [("Zahlungsbedingung", "14 T. 3 % / 30 T. netto", "ai+sel", 4),
                           ("Skontofälligkeit", "29.09.2026", "ro", 3),
                           ("Skontobetrag", "442,68", "ro", 2),
                           ("Nettofälligkeit", "15.10.2026", "ro", 3)])
    y = row(p, LX, y, LW, [("IBAN (Beleg)", "⚠ DE12 3456 7890 1234 5678 90", "ro", 6, {"warn": True}),
                           ("Bankverbindung (Stamm)", "DE89 2005 0550 1234 5678 00 · Haspa", "sel", 6)])
    y = sec(p, LX, y, LW, "D  Kostenobjekt und Routing   ·   E  Steuerung")
    y = row(p, LX, y, LW, [("Objekt-ID / Objektbezeichnung", "10010-0001 · BV Hafenstraße 22", "req+sel", 5, {"n": 10}),
                           ("Auftrags-/Vertragsnummer", "AV-2026-017", "input", 3),
                           ("Gewerk / Vergabeeinheit", "VE 300 Rohbau", "sel", 4)])
    y = row(p, LX, y, LW, [("Sachlicher Prüfer", "SI_Pruefung_10010 (Vorschlag)", "req+sel", 6, {"n": 11}),
                           ("Klärgrund (Pflicht bei Aktion „Klärfall“)", "–", "sel", 6)])
    y = sec(p, LX, y, LW, "Positionen", n=12)
    rows = [["Pos", "Positionstext", "Menge", "Einzelpreis", "Betrag", "StSchl", "Sachkonto", "Kostenstelle", "KOST2 (Objekt)"],
            ["1", "Rohbauarbeiten Bauteil A", "1 psch", "8.400,00", "8.400,00", "9", "6000", "KST-2000", "10010-0001"],
            ["2", "Baustelleneinrichtung", "1 psch", "3.480,00", "3.480,00", "9", "6000", "KST-2000", "10010-0001"],
            ["3", "Regiestunden Polier", "8 Std", "65,00", "520,00", "9", "6000", "KST-2000", "10010-0001"],
            ["", "Summe netto", "", "", "12.400,00", "", "", "", ""]]
    stl = {(r, c): TD_AI for r in (1, 2, 3) for c in (6, 7)}
    stl.update({(4, c): TD_B for c in range(9)})
    y = table(p, LX, y, [30, 170, 55, 75, 80, 42, 80, 84, 100], rows, styles=stl)
    hint(p, LX, y + 8, LW, "✓ Summenprüfung: Netto + Steuer = Brutto; Kopf = Positionen", "ui_ok")
    ui_tabs(p, VX, top, ["Beleg", "Anlagen", "Historie", "Notizen"], 0, w=VW / 4)
    ui_viewer(p, VX, top + 26, VW, ACT_Y - 14 - top - 26, "Belegvorschau – PDF (Original unverändert)", INV)
    p.line(52, ACT_Y - 10, 1218, ACT_Y - 10)
    btns(p, 52, ACT_Y, [("Notiz hinzufügen", "ui_btn2"), ("Teilen", "ui_btn2")])
    x0b, _ = btns(p, 1218, ACT_Y, [("An Lieferant zurückweisen", "ui_btn_r"), ("Dublette ablehnen", "ui_btn_r"),
                                   ("Dublette annehmen", "ui_btn2"), ("Klärfall", "ui_btn2"),
                                   ("Weiter zur sachlichen Prüfung", "ui_btn")], right=True)
    mark(p, x0b - 12, ACT_Y - 8, 13)
    rcol(p, [
        (1, "**Kopfzeile**: Schritt, Mandant, Kreditor, Rechnungsnummer, Brutto, Skontoampel (gelb/rot/dunkelrot), Status [S]."),
        (2, "**Dublettenwarnung**: gleicher Kreditor + Rechnungsnummer innerhalb 18 Monaten, zusätzlich document reader. Annahme nur mit Begründung; Ablehnen = interner Abschluss „Abgelehnt – Dublette“ ohne Lieferantenmail [S]/[K]."),
        (3, "**Zahlungsbedingung weicht ab** vom Kreditorenstandard: Hinweis, keine Blockade [S]."),
        (4, "**IBAN-Abweichung**: Warnung, Bankverbindung nicht automatisch übernehmen; Fallback BeSync-Prüfung mit Klärfall [A] – [O] OP-10."),
        (5, "**Mandant** (E-01): Erkennung über Name + Anschrift (AE-23) bzw. Alias. Leer/unsicher → Klärfall „Mandant unbekannt“; „Weiter“ gesperrt [S]/[K]."),
        (6, "**Kreditor**: Auswahl nur aus Kreditoren des Mandanten (DATEV-Stamm, LDconnect S-02). Fehlt → Klärfall „Kreditor fehlt“ (WF-04)."),
        (7, "**Belegart**: Abschlag/Schluss steuert Bau-Routing (WF-02) und macht Auftrags-/Vertragsnr. zur Pflicht [K]."),
        (8, "**Leistungsdatum** leer → Hinweis § 14 UStG, keine Blockade (G-4)."),
        (9, "**Summenprüfung** Netto + Steuer = Brutto, Kopf = Positionen [S]."),
        (10, "**Objekt-ID** (Custom Entity aus Lieferanten-App) – Pflicht bei objektbezogenen Kosten/Bau; trägt Aktenbildung und Bearbeiterfindung [K]."),
        (11, "**Sachlicher Prüfer**: Vorschlag der Bearbeiterfindung je Mandant/Objekt; Team oder Person [S]."),
        (12, "**Positionen**: KI-Kontierungsvorschlag und kreditorenabhängige Kontierungsvorlagen; Split über mehrere Zeilen [S]."),
        (13, "**Aktionen**: Weiter (Standard) [S]/[K]; Klärfall → M-05; Zurückweisen → M-06 [K]/[A]; Notiz, Teilen [S]."),
    ])


# =========================================================================================== M-03
def m03(doc):
    p = doc.page("M-03 Sachliche Prüfung & Kontierung", "p25")
    p.header("M-03 Sachliche Prüfung & Kontierung",
             "Rolle R-03 Sachlicher Prüfer, R-08 Kernpartner (Bau) · Werkzeug: smart invoice, Schritt „Sachliche Prüfung“ · "
             "Umsetzung [S] Schritt, sachlich richtig, Positionen; [K] Zahlbetrag schreibbar, Kürzungsgrund (Custom-Feld mit Werteliste), Bedingung")
    si_window(p, "Sachliche Prüfung", "Thomas B. (Objekt Nord)")
    y = kopf(p, 52, 180, 1166, "**Sachliche Prüfung**   |   10010 Livos Objektgesellschaft Nord mbH   |   70012 Musterbau GmbH   |   RE-2026-1041   |   **14.756,00 €**",
             [("Skonto 29.09. (3 Tage)", "badge_o", 150), ("In Prüfung", "badge", 90)])
    y = hint(p, 52, y, 1166, "⚠ Zahlbetrag (14.601,30 €) ≠ Bruttobetrag (14.756,00 €): Kürzungsgrund ist Pflicht – „Sachlich richtig & weiter“ erst mit Kürzungsgrund "
             "(Bedingung an der Verbindung „Custom-Feld Kürzungsgrund vorhanden“).", "ui_err", n=1)
    y = hint(p, 52, y, 1166, "ⓘ Anlagen am Beleg: Lieferschein LS-5521, Aufmaß 08/2026 (K-02). Bau-Abschläge: Zahlbetrag auf Basis BIM4You-Prüfbericht (K-08).", "ui_hint")
    top = y + 6
    y = sec(p, LX, top, LW, "▸ A/B  Zuordnung und Belegkopf (eingeklappt, nur lesen)", n=2)
    p.box(LX, y, LW, 24, "10010 Livos Objektgesellschaft Nord mbH · 70012 Musterbau GmbH · RE-2026-1041 · 15.09.2026 · Rechnung", "ui_ro")
    y += 32
    y = row(p, LX, y, LW, [("Nettobetrag", "12.400,00", "ro", 4), ("Steuerbetrag", "2.356,00", "ro", 4), ("Bruttobetrag", "14.756,00", "ro", 4)])
    cy0, idx = y, len(p.cells)
    y = sec(p, LX, y, LW, "C  Zahlung und Kürzung")
    y = row(p, LX, y, LW, [("Zahlbetrag (Kopf)", "14.601,30", "req", 3, {"n": 3}),
                           ("Kürzungsbetrag", "154,70", "ro", 3, {"n": 4}),
                           ("Kürzungsgrund", "Mengenabweichung", "req+sel", 6, {"n": 5})])
    backdrop(p, idx, LX - 6, cy0 - 4, LW + 12, y - cy0 + 2)
    y = sec(p, LX, y + 6, LW, "D  Kostenobjekt und Buchung")
    y = row(p, LX, y, LW, [("Objekt-ID / Objektbezeichnung", "10010-0001 · BV Hafenstraße 22", "sel", 5, {"n": 6}),
                           ("Auftrags-/Vertragsnummer", "AV-2026-017", "input", 3),
                           ("Gewerk / Vergabeeinheit", "VE 300 Rohbau", "sel", 4)])
    y = row(p, LX, y, LW, [("Buchungstext", "Musterbau GmbH RE-2026-1041 Rohbau BT A", "input", 7, {"n": 7}),
                           ("Weitere Prüfer", "–   (+ Prüfer hinzufügen)", "sel", 5, {"n": 8})])
    y = sec(p, LX, y, LW, "Positionen (Kontierung und sachliche Prüfung)", n=9)
    btns(p, LX, y, [("Kontierungsvorlage anwenden", "ui_btn2"), ("Position teilen (Split)", "ui_btn2")])
    y += 36
    rows = [["Pos", "Positionstext", "Menge", "EP", "Netto", "Zahlbetrag", "Sachkto", "Kostenstelle", "KOST2", "sachl. ✓"],
            ["1", "Rohbauarbeiten BT A", "1 psch", "8.400,00", "8.400,00", "9.996,00", "6000", "KST-2000", "10010-0001", "☑"],
            ["2", "Baustelleneinrichtung", "1 psch", "3.480,00", "3.480,00", "4.141,20", "6000", "KST-2000", "10010-0001", "☑"],
            ["3", "Regiestunden Polier", "6 Std ✎", "65,00", "390,00", "464,10", "6000", "KST-2000", "10010-0001", "☐"],
            ["", "Summe", "", "", "12.270,00", "14.601,30", "", "", "", "2 / 3"]]
    stl = {(r, c): TD_AI for r in (1, 2, 3) for c in (6,)}
    stl.update({(3, 2): TD_O, (3, 4): TD_Y, (3, 5): TD_Y})
    stl.update({(4, c): TD_B for c in range(10)})
    y = table(p, LX, y, [28, 142, 60, 62, 68, 76, 52, 78, 80, 70], rows, styles=stl)
    y = hint(p, LX, y + 8, LW, "ⓘ Menge Pos. 3 von 8 auf 6 Std geändert → Positionsbetrag neu berechnet; Vollständigkeit über Bedingung „alle Positionen geprüft“ (Pos. 3 offen).", "ui_hint", h=30)
    y = sec(p, LX, y + 10, LW, "Weitere Regeln der Maske")
    y = hint(p, LX, y, LW, "Kürzungsgrund = „Sonstiges“ → Pflichtnotiz [K]", "ui_hint")
    y = hint(p, LX, y, LW, "Zahlbetrag > Bruttobetrag → nicht zulässig (Hinweis) [K]", "ui_err")
    y = hint(p, LX, y, LW, "E-Rechnung mit Formfehler → Rückweisung statt Kürzung (AE-14) · Bau-Abschlag/-Schluss → Zahlbetrag lt. BIM4You-Prüfbericht (AE-11) [K]/[A]", "ui_hint")
    y = hint(p, LX, y, LW, "Kürzung erfasst → optional Kürzungsmitteilung an den Lieferanten über BeSync (WF-05) [A]", "ui_ok")
    ui_tabs(p, VX, top, ["Beleg", "Anlagen (2)", "Historie", "Notizen"], 1, w=VW / 4)
    vy = top + 26
    p.box(VX, vy, VW, 70, "", "ui_viewer")
    for i, (t, n) in enumerate([("📎 Lieferschein LS-5521.pdf", "K-02 · 12.09.2026"), ("📎 Aufmaß 08-2026.pdf", "K-02 · 14.09.2026")]):
        p.box(VX + 8, vy + 6 + i * 30, VW - 16, 26, f"{t}   ·   {n}", "ui_input", extra="fontSize=10;")
    ui_viewer(p, VX, vy + 78, VW, ACT_Y - 14 - vy - 78, "Belegvorschau – PDF mit Annotation (Original unverändert)", INV)
    p.box(VX + 40, vy + 78 + 356, 300, 40, "✎ Annotation T. Berger zu Pos. 3: nur 6 Std. lt. Stundenzettel", "ui_callout", extra="fontSize=10;")
    p.line(52, ACT_Y - 10, 1218, ACT_Y - 10)
    btns(p, 52, ACT_Y, [("Notiz / Annotation", "ui_btn2"), ("Nachweis anhängen", "ui_btn2")])
    x0b, _ = btns(p, 1218, ACT_Y, [("An Lieferant zurückweisen", "ui_btn_r"), ("Rückfrage an Verteilung", "ui_btn2"),
                                   ("Sachlich richtig & weiter", "ui_btn")], right=True)
    mark(p, x0b - 12, ACT_Y - 8, 10)
    rcol(p, [
        (1, "**Kürzungsgrund Pflicht**, wenn Zahlbetrag ≠ Brutto: Aktion „weiter“ nur mit Kürzungsgrund (Bedingung an der Verbindung); Meldetext im Test prüfen [K]/[O]."),
        (2, "**Block A/B** (Mandant, Kreditor, RE-Nr., Datum, Belegart, Beträge) aus der Verteilung – nur lesen, eingeklappt."),
        (3, "**Zahlbetrag (Kopf)**: vorbelegt = Brutto, darf Brutto nicht übersteigen; bei Positionskürzung Summe der Positions-Zahlbeträge [K]."),
        (4, "**Kürzungsbetrag** = Brutto − Zahlbetrag (berechnet)."),
        (5, "**Kürzungsgrund** (Werteliste): Mengenabweichung · Preisabweichung · Mangel/Minderung · Einbehalt · Bauabzug 15 % (§ 48) · Skonto-/Nachlassdifferenz · Sonstiges (Notiz Pflicht)."),
        (6, "**Objekt-ID, Auftrag, Gewerk** aus der Verteilung – Korrektur möglich, wird protokolliert."),
        (7, "**Buchungstext**-Vorschlag „Kreditorname Rechnungsnummer Leistung“."),
        (8, "**Weitere Prüfer** (z. B. Kernpartner R-08) parallel oder nachgelagert [S]."),
        (9, "**Positionen**: Menge/EP ändern berechnet netto neu (T-30); Zahlbetrag je Position; Sachkonto/KST Pflicht (KI-Vorschlag, Vorlage); Split per Teilung oder %-Vorlage (OP-10); „sachl. richtig“ über Bedingung."),
        (10, "**Aktionen**: Sachlich richtig & weiter [S]; Nachweis anhängen (K-02) [S]; Rückfrage mit Pflichtnotiz [K]; Zurückweisen → M-06 (bei E-Rechnungs-Formfehler statt Kürzung, AE-14); Kürzungsmitteilung optional über BeSync (WF-05) [A]."),
    ])


# =========================================================================================== M-04
def m04(doc):
    p = doc.page("M-04 Fachliche Freigabe / Zahlungsfreigabe", "p26")
    p.header("M-04 Fachliche Freigabe / Zahlungsfreigabe",
             "Rollen R-04 Fachliche Freigabe, R-05 Zahlungsfreigabe, R-08 Bau-Freigabe · Werkzeug: smart invoice, Schritttyp „Freigabe“ (auch mobil) · "
             "Umsetzung [S] Freigabeschritt, Matrix, Wertgrenzen-Verbindung; [K] Layout, Zahlungsfreigabe-Schritt")
    H1 = 700
    si_window(p, "Fachliche Freigabe", "Dr. K. Sander (GF Nord)", h=H1)
    y = kopf(p, 52, 180, 1166, "**Fachliche Freigabe**   |   10010 Livos Objektgesellschaft Nord mbH   |   70012 Musterbau GmbH   |   RE-2026-1041   |   **14.756,00 €**",
             [("Stufe 1 von 2", "badge", 110), ("Skonto 29.09. (3 Tage)", "badge_o", 150)], n=1)
    y = hint(p, 52, y, 1166, "ⓘ Zahlbetrag weicht vom Bruttobetrag ab (Kürzung 154,70 € – Mengenabweichung). Nettobetrag je Kostenobjekt 12.270,00 € > 5.000 € (Beispielgrenze Stufe 1, Kap. 10.2) → zweite Freigabestufe.", "ui_hint")
    top = y + 4
    idx = len(p.cells)
    y = sec(p, LX, top + 2, LW, "C  Zahlung (hervorgehoben)")
    y = row(p, LX, y, LW, [("Zahlbetrag", "14.601,30 €", "ro", 3, {"hl": True, "n": 2}),
                           ("Kürzungsgrund", "Mengenabweichung", "ro", 4, {"hl": True}),
                           ("Freigabestufe", "Stufe 1 von 2", "ro", 5, {"n": 3})])
    y = row(p, LX, y, LW, [("Skontofälligkeit", "29.09.2026  ●", "ro", 4, {"n": 4}),
                           ("Skontobetrag", "438,04", "ro", 3),
                           ("Nettofälligkeit", "15.10.2026", "ro", 5)])
    backdrop(p, idx, LX - 6, top - 2, LW + 12, y - top + 2)
    y = sec(p, LX, y + 8, LW, "A/B  Zuordnung und Belegkopf (nur lesen)")
    y = row(p, LX, y, LW, [("Mandant / Mandantenname", "10010 · Livos Objektgesellschaft Nord mbH", "ro", 7),
                           ("Kreditor", "70012 · Musterbau GmbH", "ro", 5)])
    y = row(p, LX, y, LW, [("Rechnungsnummer", "RE-2026-1041", "ro", 3), ("Rechnungsdatum", "15.09.2026", "ro", 3),
                           ("Belegart", "Rechnung", "ro", 2), ("Nettobetrag", "12.400,00", "ro", 2, {"n": 5}), ("Bruttobetrag", "14.756,00", "ro", 2)])
    y = sec(p, LX, y, LW, "D  Kostenobjekte (Grundlage Freigabematrix)", n=6)
    rows = [["Objekt-ID", "Objektbezeichnung", "Kostenstelle", "Netto", "Freigabegruppen lt. Matrix"],
            ["10010-0001", "BV Hafenstraße 22", "KST-2000", "12.270,00", "S1 SI_Freigabe1_10010 · S2 SI_Freigabe2_10010"]]
    y = table(p, LX, y, [90, 140, 90, 80, 316], rows)
    y = row(p, LX, y + 8, LW, [("Sachliche Prüfer (Historie)", "T. Berger (Objekt Nord) – sachlich richtig 18.09.2026 14:02", "ro", 12, {"n": 7})])
    y = fld(p, LX, y, LW, "Kommentar (Pflicht bei Ablehnen und Rückfrage)", "", "input", h=34, n=8)
    ui_tabs(p, VX, top, ["Beleg", "Historie", "Belegänderungsansicht"], 2, w=VW / 3)
    vy = top + 26
    vh = WY + H1 - 58 - vy
    p.box(VX, vy, VW, vh, "", "ui_viewer")
    p.box(VX + 10, vy + 8, VW - 20, 20, "Verteilung ↔ aktueller Schritt", "text", extra="fontSize=11;fontStyle=1;verticalAlign=middle;")
    ch = [("Pos. 3 Menge: 8 Std → 6 Std", "ui_hint"), ("Zahlbetrag: 14.756,00 → 14.601,30", "ui_hint"),
          ("Kürzungsgrund: Mengenabweichung", "ui_ok"), ("Buchungstext ergänzt", "ui_ok"), ("Pos. 3 Kostenstelle KST-2100 entfernt", "ui_err")]
    cy = vy + 34
    for t, st in ch:
        p.box(VX + 10, cy, VW - 20, 22, t, st)
        cy += 26
    p.box(VX + 10, cy + 2, VW - 20, 18, "gelb = geändert · grün = hinzugefügt · rot = gelöscht", "small")
    mark(p, VX + VW - 28, vy + 8, 9)
    cy += 30
    p.box(VX + 10, cy, VW - 20, 20, "Historie", "text", extra="fontSize=11;fontStyle=1;verticalAlign=middle;")
    hist = ["16.09. 08:12  Eingang E-Mail (rechnung-nord@)", "16.09. 10:05  Verteilung – Maria L.",
            "18.09. 14:02  Sachliche Prüfung – T. Berger", "18.09. 14:02  Kürzung 154,70 € erfasst", "19.09. 09:30  Fachliche Freigabe Stufe 1 – offen"]
    p.box(VX + 10, cy + 22, VW - 20, 16 * len(hist) + 10, "\n".join(hist), "text", extra="fontSize=10;fillColor=#FFFFFF;")
    ay = WY + H1 - 44
    p.line(52, ay - 10, 1218, ay - 10)
    x0b, _ = btns(p, 1218, ay, [("An Lieferant zurückweisen", "ui_btn_r"), ("Rückfrage", "ui_btn2"),
                                ("Ablehnen", "ui_btn_r"), ("Freigeben", "ui_btn")], right=True)
    mark(p, x0b - 12, ay - 8, 10)
    # Variante Zahlungsfreigabe
    Y2 = WY + H1 + 14
    H2 = 1108 - Y2
    ui_window(p, WX, Y2, WW, H2, "smart invoice  ›  Zahlungsfreigabe (Variante Schritt Z)", user="S. Kühn (Zahlungsfreigabe)")
    y = kopf(p, 52, Y2 + 44, 1166, "**Zahlungsfreigabe**   |   10010 Livos Objektgesellschaft Nord mbH   |   70012 Musterbau GmbH   |   RE-2026-1041   |   Zahlbetrag **14.601,30 €**",
             [("Skonto 29.09. (3 Tage)", "badge_o", 150)])
    hint(p, 52, y, 1166, "⚠ IBAN (Beleg) weicht von der Stamm-Bankverbindung ab – vor Zahlung klären (Warnung wird in der Zahlungsfreigabe erneut angezeigt).", "ui_err", n=11)
    y += 30
    row(p, 52, y, 1166, [("IBAN (Beleg)", "⚠ DE12 3456 7890 1234 5678 90", "ro", 3, {"warn": True}),
                         ("Bankverbindung (Stamm)", "DE89 2005 0550 1234 5678 00 · Haspa", "ro", 3),
                         ("Fälligkeit für Zahllauf", "29.09.2026 (Skonto)", "ro", 2, {"n": 12}),
                         ("Kommentar / Grund", "IBAN beim Lieferanten bestätigen", "input", 4)])
    ay2 = Y2 + H2 - 40
    p.box(52, ay2, 600, 28, "ⓘ Zahlungsfreigabe liegt vor der DATEV-Übergabe – LDconnect überträgt keine Zahlungssperre (AE-06).", "info", extra="verticalAlign=middle;")
    x0b, _ = btns(p, 1218, ay2, [("Zahlung zurückstellen", "ui_btn2"), ("Zahlung freigeben", "ui_btn")], right=True)
    mark(p, x0b - 12, ay2 - 8, 13)
    rcol(p, [
        (1, "**Kopfzeile** mit Freigabestufe („Stufe 1 von 2“) und Skontoampel [S]."),
        (2, "**Zahlbetrag / Kürzungsgrund** aus der Prüfung – hervorgehoben, wenn Zahlbetrag ≠ Brutto."),
        (3, "**Freigabestufe** aus der Freigabematrix; ab Wertgrenze zweite Stufe über Verbindung mit Bedingung auf den Nettobetrag (in Cent: 5.000 € = 500000; Beispiel) [S]/[K]."),
        (4, "**Skonto-/Nettofälligkeit, Skontobetrag** berechnet, mit Ampel; Eskalation statisch oder dynamisch vor Skonto/Netto [S]."),
        (5, "**Wertgrenzen gelten netto je Kostenobjekt** (AE-05)."),
        (6, "**Kostenobjekte mit Beträgen** = Grundlage der Matrix; ein Splitbeleg kann mehrere Freigeber erzeugen [S]."),
        (7, "**Vier-Augen**: Prüfer ≠ Freigeber (Standard); „Vier-Augen ab Betrag“ nur nach d.velop-Freigabe (OP-09) [S]/[O]."),
        (8, "**Kommentar** Pflicht bei Ablehnen und Rückfrage."),
        (9, "**Register** Historie (wer hat wann geprüft) und Belegänderungsansicht (Verteilung ↔ aktueller Schritt) [S]."),
        (10, "**Aktionen**: Freigeben → nächste Stufe/Zahlungsfreigabe [S]; Ablehnen → zurück zur Prüfung [S]; Rückfrage mit Rückkehr in denselben Schritt [K]; Zurückweisen nur ausnahmsweise → M-06 [K]/[A]."),
        (11, "**Nur Zahlungsfreigabe (Z1)**: IBAN (Beleg) / Bankverbindung (Stamm) mit erneuter Warnung bei Abweichung."),
        (12, "**Fälligkeit für Zahllauf** (Z2) berechnet."),
        (13, "**Zahlung freigeben** → Buchhaltung; **zurückstellen** → „Klärfall Zahlung“ mit Grund (z. B. IBAN klären) [K]."),
    ])


# =========================================================================================== M-05
def m05(doc):
    p = doc.page("M-05 Klärfall", "p27")
    p.header("M-05 Klärfall",
             "Rolle R-02 Rechnungseingang, Clearing-Gruppe je Mandant · Werkzeug: smart invoice Clearing („Clearing Modus“) bzw. Schritt „Klärfall“, Lieferanten-App (M-16) · "
             "Umsetzung [S] Clearing, [K] Klärschritt und Klärgrund, [A] Anlage-Anforderung und Status aus der Lieferanten-App")
    si_window(p, "Klärfall", "Maria L. (Rechnungseingang)", crumbs_extra="RE-2026-0877")
    y = hint(p, 52, 180, 1166, "⚠ Klärgrund: **Kreditor fehlt** – Elektro Nordlicht GmbH ist im DATEV-Stamm des Mandanten 10010 nicht vorhanden. Anlage bei Trios angefordert am 22.09.2026.", "ui_err", n=1)
    y = kopf(p, 52, y + 2, 1166, "**Klärfall**   |   10010 Livos Objektgesellschaft Nord mbH   |   Kreditor: – (Elektro Nordlicht GmbH erkannt)   |   RE-2026-0877   |   **2.380,00 €**",
             [("Clearing Modus", "badge_o", 120), ("seit 4 AT", "badge_r", 80)])
    top = y + 4
    idx = len(p.cells)
    y = sec(p, LX, top + 2, LW, "Klärung")
    y = row(p, LX, y, LW, [("Klärgrund", "Kreditor fehlt", "req+sel", 5, {"n": 2}),
                           ("Wiedervorlage am", "29.09.2026", "input", 3, {"n": 3}),
                           ("Dubletten-Referenz", "–", "ro", 4, {"n": 4})])
    y = fld(p, LX, y, LW, "Klärhinweis (Freitext, wird als Notiz gespeichert)", "Kreditor-Anlage über Lieferanten-App angefordert; USt-IdNr. aus Beleg übernommen.", "input", h=30)
    p.box(LX, y, LW, 14, "Anlage-Anforderung (Status aus Lieferanten-App)", "ui_label")
    mark(p, LX + LW - 20, y - 6, 5)
    sx = LX
    for i, t in enumerate(["angefordert 22.09.", "bei Trios", "angelegt", "synchronisiert"]):
        st = "ui_ok" if i == 0 else ("ui_hint" if i == 1 else "ui_ro")
        p.box(sx, y + 16, 164, 24, ("✓ " if i == 0 else ("● " if i == 1 else "○ ")) + t, st, extra="fontSize=10;align=center;")
        if i < 3:
            p.box(sx + 166, y + 16, 18, 24, "›", "textc", extra=f"fontColor={C['grey']};fontSize=14;")
        sx += 184
    y += 46
    backdrop(p, idx, LX - 6, top - 2, LW + 12, y - top + 2)
    y = sec(p, LX, y + 10, LW, "A  Zuordnung")
    y = row(p, LX, y, LW, [("Mandant", "10010", "req+ai+sel", 2, {"n": 6}),
                           ("Mandantenname", "Livos Objektgesellschaft Nord mbH", "ro", 4),
                           ("Kreditor", "– nicht im Stamm –", "req+sel", 4, {"warn": True, "n": 7}),
                           ("Eingangskanal", "E-Mail", "ro", 2)])
    p.box(LX, y, LW, 44, "**Erkannte Kreditordaten (Vorbelegung für die Anlage-Anforderung)**\n"
          "Elektro Nordlicht GmbH · Werftstraße 8, 20457 Hamburg · USt-IdNr. DE 298 765 432 · IBAN DE44 2004 1111 0123 4567 00",
          "ui_ai", extra="verticalAlign=top;spacingTop=4;fontSize=10;")
    y += 52
    y = sec(p, LX, y, LW, "B  Belegkopf (Korrektur von Erkennungsfehlern)", n=8)
    y = row(p, LX, y, LW, [("Belegart", "Rechnung", "sel", 3), ("Rechnungsnummer", "RE-2026-0877", "req+ai", 3),
                           ("Rechnungsdatum", "12.09.2026", "req+ai", 3), ("Leistungsdatum", "05.09.2026", "ai", 3)])
    y = row(p, LX, y, LW, [("Währung", "EUR", "sel", 2), ("Nettobetrag", "2.000,00", "req+ai", 3),
                           ("Steuerbetrag", "380,00", "req+ai", 3), ("Bruttobetrag", "2.380,00", "req+ai", 4)])
    y = sec(p, LX, y, LW, "C/D  Zahlung und Kostenobjekt")
    y = row(p, LX, y, LW, [("Zahlungsbedingung", "30 Tage netto", "ai+sel", 4), ("Bankverbindung (Stamm)", "– erst nach Sync –", "sel", 4),
                           ("Objekt-ID", "10010-0001 · BV Hafenstraße 22", "sel", 4)])
    y = hint(p, LX, y + 4, LW, "ⓘ Keine Kreditoranlage in d.velop: Anlage durch Trios in DATEV, Sync über LDconnect – Kreditor ab Folgetag auswählbar (AE-09).", "info", h=30, n=9)
    y = hint(p, LX, y, LW, "ⓘ Klärfall-Mandant: eigener Mandant im Bucket für nicht zuordenbare Belege; Rechte nur Zentralrollen (Clearing-Gruppe SI_Clearing_10010) [K].", "ui_hint")
    y = hint(p, LX, y, LW, "⚠ Liegezeit: Eskalation für Klärfälle nach 5 Arbeitstagen (Vorschlag) – hier seit 4 AT [K].", "ui_err")
    ui_tabs(p, VX, top, ["Beleg", "Anlagen", "Historie", "Notizen (2)"], 0, w=VW / 4)
    inv = _nb(["Elektro Nordlicht GmbH · Werftstraße 8", "20457 Hamburg · USt-IdNr. DE 298 765 432", "",
               "Livos Objektgesellschaft Nord mbH", "Hafenstraße 22 · 20359 Hamburg", "",
               "RECHNUNG  RE-2026-0877", "Datum: 12.09.2026 · Leistung: 05.09.2026", "",
               "1  E-Check Treppenhausbeleuchtung   2.000,00", "", "Netto                               2.000,00",
               "USt 19 %                              380,00", "Gesamt                          2.380,00 EUR", "",
               "Zahlbar innerhalb 30 Tagen netto.", "IBAN DE44 2004 1111 0123 4567 00"])
    ui_viewer(p, VX, top + 26, VW, ACT_Y - 14 - top - 26, "Belegvorschau – PDF", inv)
    p.line(52, ACT_Y - 10, 1218, ACT_Y - 10)
    btns(p, 52, ACT_Y, [("Zurückstellen", "ui_btn2"), ("Dublette ablehnen", "ui_btn_r"), ("Dublette annehmen", "ui_btn2")])
    x0b, _ = btns(p, 1218, ACT_Y, [("An Lieferant zurückweisen", "ui_btn_r"), ("Kreditor-Anlage anfordern", "ui_btn2"),
                                   ("Zurück in Verteilung", "ui_btn")], right=True)
    mark(p, x0b - 12, ACT_Y - 8, 10)
    rcol(p, [
        (1, "**Hinweisleiste „Klärgrund“** ganz oben; Status „Clearing Modus“ im REB [S]."),
        (2, "**Klärgrund** (Pflicht): Mandant unbekannt · Kreditor fehlt · Dublettenverdacht · IBAN klären · Sonstiges [K]."),
        (3, "**Wiedervorlage am** – eigene Erinnerung; „Zurückstellen“ hält den Beleg bis dahin im Klärfall [K]."),
        (4, "**Dubletten-Referenz** – Verweis auf den Ursprungsbeleg (nur bei Dublettenverdacht)."),
        (5, "**Anlage-Anforderung (Status)** aus der Lieferanten-App: angefordert · bei Trios · angelegt · synchronisiert; im Beleg als Notiz [A]."),
        (6, "**Mandant** – Klärfall-Mandant durch echten Mandanten ersetzen. Der Klärfall-Mandant ist ein eigener Mandant im Bucket, Rechte nur Zentralrollen [K]."),
        (7, "**Kreditor** (Pflicht) – nach Anlage in DATEV und Sync am Folgetag auswählbar."),
        (8, "**Rechnungsnummer, Datum, Beträge** – Korrektur von Erkennungsfehlern."),
        (9, "**Keine Kreditoranlage in d.velop** – Livos legt keine DATEV-Kreditoren an (AE-09)."),
        (10, "**Aktionen**: Zurück in Verteilung (Standard) [K]; Kreditor-Anlage anfordern öffnet die Lieferanten-App vorbelegt (Mandant, Name, Anschrift, USt-IdNr., IBAN) [A]; Dublette ablehnen/annehmen mit Begründung [S]; Zurückweisen (z. B. falscher Rechnungsempfänger) → M-06 [K]/[A]; Zurückstellen [K]. Eskalation nach 5 Arbeitstagen (Vorschlag) [K]."),
    ])


# =========================================================================================== M-06
def m06(doc):
    p = doc.page("M-06 Rückweisungsdialog", "p28")
    p.header("M-06 Rückweisungsdialog",
             "Rollen R-02, R-03 (ausnahmsweise R-04) · Werkzeug: smart invoice Aktion „An Lieferant zurückweisen“; Versand und Ablage über BeSync (Webhook → Microsoft Graph, S-11) · "
             "Umsetzung [K] Aktion, Grund, Endpfad; [A] Mailversand, Vorlagen, Ablage als Korrespondenz")
    si_window(p, "Sachliche Prüfung", "Thomas B. (Objekt Nord)")
    kopf(p, 52, 180, 1166, "**Sachliche Prüfung**   |   10010 Livos Objektgesellschaft Nord mbH   |   70012 Musterbau GmbH   |   RE-2026-1041   |   **14.756,00 €**",
         [("In Prüfung", "badge", 90)])
    # abgeblendete Belegmaske im Hintergrund
    for i in range(6):
        p.box(LX, 240 + i * 50, LW, 36, "", "ui_ro")
    p.box(VX, 240, VW, 800, "", "ui_viewer")
    p.box(52, 226, 1166, 822, "", "rounded=0;fillColor=#1B1B1B;strokeColor=none;opacity=35;")
    # Dialog
    DX, DY, DW, DH = 90, 262, 620, 640
    p.box(DX, DY, DW, DH, "", f"rounded=1;arcSize=2;fillColor=#FFFFFF;strokeColor={C['grey']};shadow=1;")
    p.box(DX, DY, DW, 36, "An Lieferant zurückweisen – RE-2026-1041", "ui_bar")
    p.box(DX + DW - 36, DY + 4, 28, 28, "✕", "textc", extra="fontColor=#FFFFFF;fontSize=14;")
    x, w = DX + 20, DW - 40
    y = DY + 50
    p.box(x, y, w, 14, "Rückweisungsgrund *", "ui_label")
    mark(p, x + w - 20, y - 6, 1)
    y += 16
    grounds = ["(1) Pflichtangaben § 14 UStG fehlen/fehlerhaft",
               "(2) Falscher Rechnungsempfänger / falsche Gesellschaft",
               "(3) Leistung nicht/nicht vollständig erbracht bzw. Nachweise fehlen",
               "(4) Preis/Menge weicht von Auftrag/Vertrag ab",
               "(5) Formaler E-Rechnungsfehler / Format nicht verarbeitbar"]
    p.box(x, y, w, 5 * 28 + 8, "", f"rounded=1;arcSize=3;fillColor=#FFFFFF;strokeColor={C['teal']};strokeWidth=2;")
    for i, g in enumerate(grounds):
        sel = i == 2
        p.box(x + 6, y + 4 + i * 28, w - 12, 26, ("◉  " if sel else "○  ") + g, "text",
              extra="fontSize=11;verticalAlign=middle;" + (f"fillColor={C['teal_l']};fontStyle=1;" if sel else ""))
    y += 5 * 28 + 18
    y = fld(p, x, y, w, "Ergänzender Text (wird in die Mail übernommen)",
            "Für Position 3 (Regiestunden Polier) fehlen die abgezeichneten Stundenzettel. Bitte reichen Sie eine korrigierte Rechnung mit Nachweisen ein.",
            "input", h=62, n=2)
    y = fld(p, x, y, w, "Empfänger", "rechnung@musterbau.de  (Rechnungskorrespondenz-Adresse, Lieferanten-App)", "ro", n=3)
    p.box(x, y, w, 14, "Platzhalter der Vorlage (aus dem Beleg)", "ui_label")
    mark(p, x + w - 20, y - 6, 4)
    y += 14
    table(p, x, y, [150, 145, 130, 155], [["Mandantenname", "Rechnungsnummer", "Rechnungsdatum", "Bruttobetrag"],
                                           ["Livos Obj.-Ges. Nord mbH", "RE-2026-1041", "15.09.2026", "14.756,00 €"]], rowh=24)
    y += 56
    y = hint(p, x, y, w, "ⓘ Bei E-Rechnungen: Hinweis „Bitte senden Sie eine berichtigte E-Rechnung“ wird automatisch ergänzt (Feld 5).", "ui_hint", h=28, n=5)
    y = hint(p, x, y, w, "⚠ Fehlt die Empfängeradresse: Hinweis – Versand manuell über „Teilen per E-Mail“.", "ui_err", h=24)
    y = fld(p, x, y + 2, w, "Versandstatus (Rückmeldung BeSync)", "– noch nicht versendet  (danach: versendet 26.09.2026 10:14 · Fehler)", "ro", n=6)
    hint(p, x, y, w, "Dubletten nie über diesen Dialog – interne Ablehnung ohne Lieferantenmail (M-02).", "ui_hint", n=9)
    p.line(DX, DY + DH - 50, DX + DW, DY + DH - 50)
    x0b, _ = btns(p, DX + DW - 20, DY + DH - 40, [("Abbrechen", "ui_btn2"), ("Zurückweisen mit Prüfung (B)", "ui_btn2"),
                                                  ("Zurückweisen (A)", "ui_btn")], right=True)
    mark(p, x0b - 12, DY + DH - 48, 7)
    # Variante B – Mailentwurf in BeSync / Lieferanten-App
    BX, BY, BW, BH = 740, 262, 470, 540
    p.box(BX, BY, BW, BH, "", f"rounded=1;arcSize=2;fillColor=#FFFFFF;strokeColor={C['green']};strokeWidth=2;shadow=1;")
    p.box(BX, BY, BW, 36, "Lieferanten-App (BeSync) – Mailentwurf prüfen · Variante B [A]", "mdis", extra="rounded=0;align=left;spacingLeft=10;")
    mark(p, BX + BW - 28, BY + 8, 8)
    y = BY + 50
    y = fld(p, BX + 16, y, BW - 32, "An", "rechnung@musterbau.de", "ro")
    y = fld(p, BX + 16, y, BW - 32, "Betreff", "Rückweisung Ihrer Rechnung RE-2026-1041 – Livos Objektgesellschaft Nord mbH", "input")
    body = ("Sehr geehrte Damen und Herren,\n\nIhre Rechnung **RE-2026-1041** vom 15.09.2026 über 14.756,00 € an die "
            "Livos Objektgesellschaft Nord mbH weisen wir zurück.\n\n**Grund:** Leistung nicht vollständig erbracht bzw. Nachweise fehlen.\n\n"
            "Für Position 3 (Regiestunden Polier) fehlen die abgezeichneten Stundenzettel. Bitte reichen Sie eine korrigierte Rechnung "
            "mit Nachweisen ein.\n\nMit freundlichen Grüßen\nLivos Rechnungseingang")
    p.box(BX + 16, y, BW - 32, 14, "Nachricht (aus Vorlage „Rückweisung Grund 3“, anpassbar)", "ui_label")
    p.box(BX + 16, y + 14, BW - 32, 250, body, "ui_input", extra="verticalAlign=top;spacingTop=6;spacingLeft=8;spacingRight=8;")
    y += 272
    p.box(BX + 16, y, BW - 32, 22, "📎 Anhang: RE-2026-1041.pdf", "text", extra="fontSize=10;verticalAlign=middle;")
    btns(p, BX + BW - 16, BY + BH - 44, [("Verwerfen", "ui_btn_r"), ("Senden & ablegen (K-07)", "ui_btn")], right=True)
    p.box(BX, BY + BH + 12, BW, 118,
          "**Ablauf Variante A (Standardvorschlag)**: Endpfad „Zurückgewiesen“ → Export an BeSync → BeSync versendet die Vorlagenmail sofort und legt sie als K-07 in der Kreditorenakte ab.\n\n"
          "**Variante B**: BeSync erzeugt diesen Entwurf; Versand erst nach Bestätigung.\n\n"
          "**Grenze**: Mailvorschau in smart invoice nicht möglich (keine Mailfunktion im Standard).", "info")
    rcol(p, [
        (1, "**Rückweisungsgrund** (Pflicht, Werteliste/Custom Entity) – fünf Standardgründe; Aktion nur mit Grund (Verbindungsbedingung) [K]."),
        (2, "**Ergänzender Text** (optional) wird in die Mail übernommen."),
        (3, "**Empfänger** aus Rechnungskorrespondenz-Adresse (Lieferanten-App) bzw. vendor.email (Stamm) – nur lesen."),
        (4, "**Platzhalter** der Vorlage: Mandantenname, Rechnungsnummer, Rechnungsdatum, Bruttobetrag."),
        (5, "**Hinweis E-Rechnung**: berichtigte E-Rechnung anfordern (vom System gesetzt)."),
        (6, "**Versandstatus** aus BeSync-Rückmeldung: versendet / Fehler (Notiz bzw. Korrespondenz K-07)."),
        (7, "**Aktionen**: Zurückweisen (A) [K]/[A] · Zurückweisen mit Prüfung (B) [A] · Abbrechen [S]. Webhook muss innerhalb 30 s quittieren → BeSync quittiert sofort, versendet asynchron."),
        (8, "**Variante B**: Mailentwurf zur Kontrolle in der Lieferanten-App bzw. BeSync-Oberfläche („anpassbare Standard-E-Mail“) [A]."),
        (9, "**Dubletten** nie über diesen Dialog – interne Ablehnung ohne Lieferantenmail in M-02 (Regel)."),
    ])


# =========================================================================================== M-07
def m07(doc):
    p = doc.page("M-07 Buchhaltung / DATEV-Übergabe", "p29")
    p.header("M-07 Buchhaltung / DATEV-Übergabe",
             "Rolle R-06 Buchhaltung (Trios) · Werkzeug: smart invoice, Schritt „Buchhaltung“ (Aufruf aus Meine Aufgaben / REB) · "
             "Umsetzung [S] Schritt, Historie, Notizen; [K] Export an die Integration DATEV Rechnungswesen (LDconnect, S-01)")
    si_window(p, "Buchhaltung", "J. Wolter (Trios Buchhaltung)")
    y = kopf(p, 52, 180, 1166, "**Buchhaltung**   |   10010 Livos Objektgesellschaft Nord mbH   |   70012 Musterbau GmbH   |   RE-2026-1041   |   **14.756,00 €**",
             [("Zahlung freigegeben", "badge_g", 140), ("Skonto 29.09. (3 Tage)", "badge_o", 150)])
    y = hint(p, 52, y, 1166, "⚠ Zahlbetrag (14.601,30 €) ≠ Bruttobetrag: Zahlbetrag und Kürzungsgrund werden nicht an DATEV übertragen – Behandlung in DATEV/Zahlungsvorschlag gemäß Abstimmung mit Trios (OP-05).", "ui_err", n=1)
    y = hint(p, 52, y, 1166, "ⓘ Einstufige Übergabe erst nach Zahlungsfreigabe (AE-08). Steuerschlüssel bei § 13b prüfen.", "ui_hint")
    top = y + 6
    DL = lambda lab, d: f"{lab}  → {d}"
    y = sec(p, LX, top, LW, "Kopfdaten (kompakt, in Reihenfolge der DATEV-Übergabe)", n=2)
    y = row(p, LX, y, LW, [(DL("Mandant", "DATEV-Mandant"), "10010 · Livos Obj.-Ges. Nord mbH", "ro", 5),
                           (DL("Kreditor", "Konto / Geschäftspartner"), "70012 · Musterbau GmbH", "req+sel", 4, {"n": 3}),
                           (DL("Belegart", "Vorzeichen"), "Rechnung", "sel", 3)])
    y = row(p, LX, y, LW, [(DL("Rechnungsnr.", "Belegfeld 1"), "RE-2026-1041", "ro", 3),
                           (DL("Rechnungsdatum", "Datum"), "15.09.2026", "ro", 3),
                           (DL("Leistungsdatum", "Leistungsd."), "31.08.2026", "input", 3),
                           (DL("Währung", "WKZ"), "EUR", "ro", 3)])
    y = row(p, LX, y, LW, [(DL("Bruttobetrag", "Brutto-Betrag"), "14.756,00", "ro", 3),
                           ("Zahlbetrag / Kürzungsgrund  (nicht übertragen)", "14.601,30 · Mengenabweichung", "ro", 5, {"hl": True, "n": 4}),
                           (DL("Buchungstext", "Buchungstext"), "Musterbau RE-2026-1041 Rohbau", "input", 4)])
    y = sec(p, LX, y, LW, "Buchungsvorschau (Positionen, schreibbar wenn geprüft)", n=5)
    rows = [["Pos", "Konto", "BU-Gegenkto", "StSchl", "Satz", "KOST1", "KOST2", "Brutto", "Buchungstext"],
            ["1", "70012", "6000", "9", "19 %", "KST-2000", "10010-0001", "9.996,00", "Musterbau RE-2026-1041 Rohbau"],
            ["2", "70012", "6000", "9", "19 %", "KST-2000", "10010-0001", "4.141,20", "Musterbau RE-2026-1041 BE"],
            ["3", "70012", "6000", "9", "19 %", "KST-2000", "10010-0001", "618,80", "Musterbau RE-2026-1041 Regie"],
            ["", "", "", "", "", "", "Summe", "14.756,00", ""]]
    stl = {(4, c): TD_B for c in range(9)}
    y = table(p, LX, y, [30, 56, 92, 48, 46, 76, 76, 80, 212], rows, styles=stl)
    y = sec(p, LX, y + 10, LW, "Übergabe")
    y = row(p, LX, y, LW, [(DL("Dokumentenlink", "Dokumentenlink"), "https://livos.d-velop.cloud/dms/r/…/o2/SI-2026-004812", "ro", 8, {"n": 6}),
                           ("Exportstatus", "bereit zur Übergabe", "ro", 4, {"n": 7})])
    p.box(LX, y + 2, LW, 64, "**LDconnect überträgt je Buchungssatz höchstens:** Belegfeld 1, Belegfeld 2, Brutto-Betrag, BU-Gegenkonto, Buchungstext, Datum, "
          "Dokumentenlink, Geschäftspartner, Konto, KOST1, KOST2, Leistungsdatum, Steuersatz, Steuerschlüssel, Waren und Dienstleistungen, WKZ.", "info")
    ui_tabs(p, VX, top, ["Beleg", "Historie", "Notizen (1)"], 1, w=VW / 3)
    vy = top + 26
    vh = ACT_Y - 14 - vy
    p.box(VX, vy, VW, vh, "", "ui_viewer")
    mark(p, VX + VW - 28, vy + 8, 8)
    hist = [("16.09.2026 08:12", "Eingang E-Mail · rechnung-nord@livos.de", "System"),
            ("16.09.2026 10:05", "Verteilung abgeschlossen", "Maria L."),
            ("18.09.2026 14:02", "Sachlich richtig · Kürzung 154,70 €", "T. Berger"),
            ("19.09.2026 09:30", "Fachliche Freigabe Stufe 1", "Dr. K. Sander"),
            ("22.09.2026 11:15", "Fachliche Freigabe Stufe 2", "SI_Freigabe2_10010"),
            ("24.09.2026 16:40", "Zahlung freigegeben", "S. Kühn"),
            ("26.09.2026 09:02", "Buchhaltung – in Bearbeitung", "J. Wolter")]
    cy = vy + 10
    for d, t, u in hist:
        p.box(VX + 12, cy, 8, 8, "", f"ellipse;fillColor={C['teal']};strokeColor=none;")
        p.box(VX + 28, cy - 6, VW - 40, 40, f"**{t}**\n{d} · {u}", "text", extra="fontSize=10;spacingTop=0;")
        cy += 46
    p.box(VX + 12, cy + 6, VW - 24, 20, "Notizen", "text", extra="fontSize=11;fontStyle=1;")
    p.box(VX + 12, cy + 30, VW - 24, 64, "**T. Berger, 18.09.:** Pos. 3 nur 6 Std. lt. Stundenzettel – Kürzung 154,70 €; Rest wie Aufmaß.",
          "note", extra="spacingRight=16;")
    p.box(VX + 12, cy + 104, VW - 24, 50, "**Separate Buchungsvorschau** als eigene DATEV-Maske nicht belegt – die Positionsansicht dient als Vorschau [O].", "ui_hint",
          extra="verticalAlign=top;spacingTop=4;")
    p.box(VX + 12, cy + 164, VW - 24, 50, "**Exportfehler** → Beleg läuft in den Fehlerschritt; Meldung im Administrations-Dashboard [S].", "ui_err",
          extra="verticalAlign=top;spacingTop=4;")
    p.line(52, ACT_Y - 10, 1218, ACT_Y - 10)
    btns(p, 52, ACT_Y, [("Notiz", "ui_btn2")])
    x0b, _ = btns(p, 1218, ACT_Y, [("Klärfall Buchhaltung", "ui_btn2"), ("Zurück an Prüfung", "ui_btn2"),
                                   ("An DATEV übergeben", "ui_btn")], right=True)
    mark(p, x0b - 12, ACT_Y - 8, 9)
    rcol(p, [
        (1, "**Hinweis Zahlbetrag ≠ Brutto** – Zahlbetrag/Kürzungsgrund werden nicht übertragen; Behandlung gemäß Abstimmung mit Trios (OP-05)."),
        (2, "**Kopfdaten kompakt** in der Reihenfolge der DATEV-Übergabe; Label zeigt das DATEV-Zielfeld (→)."),
        (3, "**Kreditor** schreibbar, nur Stammkreditoren (Konto/Geschäftspartner); Belegart Gutschrift steuert das Vorzeichen."),
        (4, "**Zahlbetrag / Kürzungsgrund** aus der Prüfung – nur lesen, hervorgehoben."),
        (5, "**Buchungsvorschau**: Sachkonto (BU-Gegenkonto), Steuerschlüssel, Steuersatz, KOST1, KOST2, Betrag – Option „schreibbar wenn geprüft“ [S]."),
        (6, "**Dokumentenlink** für die Beleganzeige aus DATEV (SYS)."),
        (7, "**Exportstatus**: „An DATEV übergeben“ / Fehler."),
        (8, "**Register Historie und Notizen** (im Workshop gezeigt) [S]."),
        (9, "**Aktionen**: An DATEV übergeben (Standard, Endpfad „Übergeben“ mit Export an die Integration) [K]; Zurück an Prüfung [K]; Klärfall Buchhaltung, z. B. Kreditor in DATEV gesperrt [K]; Notiz [S]."),
    ])


# =========================================================================================== REB
REB_COLS = ["Status", "Mandant", "Kreditor", "Rechnungsnr.", "RE-Datum", "Brutto", "Skonto / fällig", "Nettofällig", "Aktueller Schritt", "seit", "Zugewiesen", "Format"]


def reb_quick(p, x, y, w, items, active=0):
    p.box(x, y, w, 22, "Schnellzugriffe", "ui_sec")
    y += 28
    for i, (t, n, own) in enumerate(items):
        st = "ui_tab_a" if i == active else "text"
        ex = "align=left;spacingLeft=8;verticalAlign=middle;fontSize=11;" + ("" if i == active else f"fillColor=#FFFFFF;")
        p.box(x, y, w, 26, ("★ " if own else "") + t, st, extra=ex)
        if n is not None:
            p.box(x + w - 40, y + 4, 34, 18, str(n), "badge" if not own else "badge_o")
        y += 30
    return y


def m08(doc):
    p = doc.page("M-08 REB Arbeitsansicht", "p30")
    p.header("M-08 Rechnungseingangsbuch – Arbeitsansicht",
             "Rolle: alle Workflowrollen (Beispiel R-03) · Werkzeug: REB als Widget auf der Startseite oder eigene App · "
             "Umsetzung [S] Schnellzugriffe, Spalten, Filter, Gruppierung, CSV-Export; [K] eigene Schnellzugriffe")
    X, Y, W, H = 40, 112, 1574, 600
    ui_window(p, X, Y, W, H, "Rechnungseingangsbuch", "Start › Rechnungseingangsbuch › Meine offenen Rechnungen", user="Thomas B. (Objekt Nord)")
    QX, QW = 52, 230
    reb_quick(p, QX, 180, QW, [("Meine offenen Rechnungen", 7, False), ("Rechnungen in Vertretung", 2, False),
                              ("An mich eskalierte Rechnungen", 1, False), ("Alle offenen Rechnungen", 48, False), ("Archiv", None, False),
                              ("Skonto in 5 Tagen", 3, True), ("Klärfälle", 4, True), ("Kürzungen dieses Monats", 6, True),
                              ("Bau – wartet auf BIM4You", 2, True)])
    mark(p, QX + QW - 20, 178, 1)
    p.box(QX, 470, QW, 34, "★ = eigener Schnellzugriff [K]\n(Filter + Layout gespeichert)", "small")
    LX2, LW2 = 296, 1000
    # Filterleiste
    p.box(LX2, 180, LW2, 34, "Filter:  Mandant = 10010  UND  Aktueller Schritt ≠ Buchhaltung      + Filter      Gruppieren: –      Spalten ▾".replace("  ", NB * 2),
          "ui_input", extra="fontSize=11;")
    btns(p, LX2 + LW2 - 8, 183, [("CSV-Export", "ui_btn2")], right=True)
    mark(p, LX2 - 10, 172, 2)
    rows = [REB_COLS,
            ["● Neu", "10010 Nord", "Musterbau GmbH", "RE-2026-1041", "15.09.26", "14.756,00", "442,68 · 29.09.", "15.10.26", "Sachl. Prüfung", "2 T.", "T. Berger", "PDF"],
            ["● Neu", "10010 Nord", "Elbe Haustechnik KG", "EH-55812", "18.09.26", "3.927,00", "78,54 · 02.10.", "18.10.26", "Sachl. Prüfung", "1 T.", "SI_Pruefung_10010", "XRechn."],
            ["Offen", "10010 Nord", "Glas Petersen OHG", "2026-0917", "10.09.26", "1.190,00", "23,80 · 27.09.", "10.10.26", "Sachl. Prüfung", "6 T.", "T. Berger", "PDF"],
            ["Eskalation 1", "10010 Nord", "Stadtwerke Nord", "SW-7781230", "01.09.26", "612,40", "– ", "30.09.26", "Sachl. Prüfung", "11 T.", "T. Berger", "ZUGFeRD"],
            ["Offen", "10020 Süd", "Musterbau GmbH", "RE-2026-1033", "08.09.26", "8.211,00", "–", "08.10.26", "Sachl. Prüfung", "4 T.", "Vertretung", "PDF"],
            ["Offen", "10010 Nord", "Dach & Fach GmbH", "DF-1209", "12.09.26", "5.474,00", "109,48 · 26.09.", "12.10.26", "Rückfrage", "3 T.", "T. Berger", "PDF"],
            ["Offen", "10010 Nord", "Hansa Reinigung", "HR-26-0911", "11.09.26", "886,55", "–", "11.10.26", "Sachl. Prüfung", "5 T.", "SI_Pruefung_10010", "XRechn."]]
    stl = {}
    for r in (1, 2):
        for c in range(12):
            stl[(r, c)] = TD_B
    stl[(1, 6)] = TD_Y; stl[(2, 6)] = TD_G; stl[(3, 6)] = TD_R; stl[(6, 6)] = TD_R
    stl[(4, 0)] = TD_O
    stl[(1, 0)] = TD_B; stl[(4, 9)] = TD_R
    y = table(p, LX2, 224, [82, 72, 126, 92, 64, 72, 98, 68, 104, 42, 116, 64], rows, rowh=28, styles=stl)
    p.box(LX2, 224 + 28, 1000, 28, "", f"rounded=0;fillColor=none;strokeColor={C['teal']};strokeWidth=2;")
    mark(p, LX2 + 82 + 72 + 126 + 92 + 64 + 72 + 76, 208, 3)
    mark(p, LX2 + 1000 - 64 - 116 - 22, 208, 4)
    mark(p, LX2 - 10, 250, 5)
    p.box(LX2, y + 6, LW2, 20, "7 Einträge · ungelesene fett · Klick öffnet die Belegmaske (M-03) · Spalten wählen/fixieren über „Spalten ▾“", "small")
    # Detail
    DX, DW = 1308, 294
    p.box(DX, 180, DW, 470, "", f"rounded=0;fillColor={C['grey_l']};strokeColor={C['grey_m']};")
    p.box(DX + 10, 186, DW - 20, 22, "Detail / Historie – RE-2026-1041", "ui_sec")
    mark(p, DX + DW - 30, 186, 6)
    steps = [("Eingang (E-Mail)", "16.09. 08:12 · System", "ui_ok"), ("Verteilung", "16.09. 10:05 · Maria L.", "ui_ok"),
             ("Sachliche Prüfung", "seit 24.09. · T. Berger", "ui_hint"), ("Fachliche Freigabe", "offen", "ui_ro"),
             ("Zahlungsfreigabe", "offen", "ui_ro"), ("Buchhaltung / DATEV", "offen", "ui_ro")]
    cy = 218
    for t, s, st in steps:
        p.box(DX + 12, cy, DW - 24, 40, f"**{t}**\n{s}", st, extra="verticalAlign=middle;")
        cy += 44
    p.box(DX + 12, cy + 4, DW - 24, 20, "Kommentare / Notizen", "text", extra="fontSize=11;fontStyle=1;")
    p.box(DX + 12, cy + 28, DW - 24, 58, "**Maria L., 16.09.:** Dublettenverdacht geprüft – Ursprungsbeleg war Angebot, keine Dublette.", "note", extra="spacingRight=16;")
    # Aktionsleiste
    ay = Y + H - 44
    p.line(52, ay - 10, 1602, ay - 10)
    x0b, _ = btns(p, 296, ay, [("Öffnen", "ui_btn"), ("Historie anzeigen", "ui_btn2"), ("Filter / Gruppieren", "ui_btn2"),
                               ("Spalten wählen / fixieren", "ui_btn2"), ("Schnellzugriff speichern", "ui_btn2"), ("CSV-Export", "ui_btn2")])
    mark(p, x0b - 12, ay - 8, 7)
    # Erläuterungen unten
    items = [
        (1, "**Schnellzugriffe** mit Zähler: Meine offenen (persönlich und über Gruppen), in Vertretung, an mich eskaliert (mit Stufe), alle offenen (global/je Mandant), Archiv (6 bzw. 12 Monate) [S]; eigene (★) mit gespeichertem Filter und Layout [K]."),
        (2, "**Filterleiste**: Filter mit Operatoren und logischen Verknüpfungen, Gruppierung; CSV-Export sichtbarer oder aller Spalten, Download 30 Tage [S]."),
        (3, "**Skontoampel** in „Skonto / fällig“: gelb = nahe, rot = heute/abgelaufen; Skontobetrag und -fälligkeit berechnet."),
        (4, "**Aktueller Schritt seit** = Liegezeit im aktuellen Schritt; „Zugewiesen“ Benutzer/Gruppe; Rechnungsformat E-Rechnung/sonstige."),
        (5, "**Liste**: Status inkl. ungelesen (fett), Clearing Modus, Eskalation Stufe 1/2. Standardspalten 1–12 in dieser Reihenfolge."),
        (6, "**Detail/Historie** (bei Auswahl): Weg durch den Workflow, Kommentare, Notizen."),
        (7, "**Aktionen**: Öffnen (Belegmaske), Historie, Filter/Gruppieren, Spalten wählen/fixieren, eigenen Schnellzugriff speichern, CSV-Export [S]."),
        (8, "**Regeln**: Sichtbarkeit folgt der REB-Berechtigung (Kapitel 13.5.3). E-Mail-Benachrichtigungen je Aufgabe abschaltbar – gearbeitet wird über diese Liste (T-17)."),
    ]
    _notes_cols(p, items, Y + H + 12)


def _notes_cols(p, items, y0, ncols=3, lw=364):
    cw = (1574 - lw - 20 - (ncols - 1) * 16) / ncols
    per = (len(items) + ncols - 1) // ncols
    p.box(40, y0, 400, 22, "Erläuterungen", "h2", extra="fontSize=13;")
    for c in range(ncols):
        sub = items[c * per:(c + 1) * per]
        if not sub:
            continue
        x = 40 + c * (cw + 16)
        cy = y0 + 28
        cpl = int((cw - 36) / 5.3)
        for n, t in sub:
            h = _lines(t, cpl) * 13 + 8
            p.box(x, cy, 20, 20, str(n), "ann", extra="fontSize=10;")
            p.box(x + 26, cy - 3, cw - 26, h, t, "text", extra="fontSize=10;spacingTop=0;")
            cy += max(h, 22) + 5
    flegend(p, 1614 - lw, y0)


def m09(doc):
    p = doc.page("M-09 REB Managementsicht", "p31")
    p.header("M-09 Rechnungseingangsbuch – Managementsicht",
             "Rollen R-07 Controlling/Management, R-04 Gesellschaftsverantwortliche, R-02 · Werkzeug: REB, Schnellzugriff „Alle offenen Rechnungen“ mit Gruppierung · "
             "Umsetzung [S] REB; [K] Schnellzugriffe; historische Durchlaufzeiten [A] in evidanza (S-12)")
    X, Y, W, H = 40, 112, 1574, 660
    ui_window(p, X, Y, W, H, "Rechnungseingangsbuch", "Start › Rechnungseingangsbuch › Offen je Gesellschaft", user="C. Hartmann (Controlling)")
    QX, QW = 52, 230
    reb_quick(p, QX, 180, QW, [("Alle offenen Rechnungen", 48, False), ("Archiv", None, False),
                              ("Offen je Gesellschaft", 48, True), ("Liegezeit > 10 Tage", 5, True), ("Eskalationen", 3, True),
                              ("Klärfälle", 4, True), ("Zahlungsfreigabe offen", 6, True), ("Monatsende unverbucht", 17, True)], active=2)
    mark(p, QX + QW - 20, 178, 1)
    table(p, QX, 472, [110, 120], [["Schnellzugriff", "Gruppierung"], ["Offen je Ges.", "Mandant → Schritt"], ["Liegezeit > 10 T.", "Schritt → Zugew."],
                                  ["Eskalationen", "Mandant"], ["Klärfälle", "Mandant"], ["Zahlungsfr. offen", "Nettofälligkeit"], ["Monatsende", "Mandant"]], rowh=22)
    LX2, LW2 = 296, 1306
    p.box(LX2, 180, LW2, 34, "Filter:  Status = offen      Gruppieren nach:  Mandant  →  Aktueller Schritt      Spalten ▾".replace("  ", NB * 2), "ui_input", extra="fontSize=11;")
    btns(p, LX2 + LW2 - 8, 183, [("CSV-Export (alle Spalten) → evidanza", "ui_btn2")], right=True)
    mark(p, LX2 - 10, 172, 2)
    cols = ["Status", "Kreditor", "Rechnungsnr.", "Belegart", "RE-Datum", "Netto", "Brutto", "Zahlbetrag [O]", "Skonto fällig", "Nettofällig", "Schritt seit", "Zugewiesen", "Format"]
    colw = [92, 138, 98, 110, 70, 86, 86, 100, 90, 80, 82, 110, 64]  # = 1206? adjust
    scale = LW2 / sum(colw)
    colw = [round(c * scale) for c in colw]
    colw[-1] += LW2 - sum(colw)
    y = 224
    y = table(p, LX2, y, colw, [cols], rowh=26)
    data = [
        ("g1", "▾  10010 Livos Objektgesellschaft Nord mbH  (21 Rechnungen · 184.320,00 € brutto)"),
        ("g2", "▾  Verteilung  (4)"),
        ("r", ["Offen", "Elbe Haustechnik KG", "EH-55812", "Rechnung", "18.09.26", "3.300,00", "3.927,00", "3.927,00", "02.10.26", "18.10.26", "1 T.", "Maria L.", "XRechn."]),
        ("g2", "▾  Sachliche Prüfung  (9)"),
        ("r", ["Offen", "Musterbau GmbH", "RE-2026-1041", "Rechnung", "15.09.26", "12.400,00", "14.756,00", "14.601,30", "29.09.26", "15.10.26", "2 T.", "T. Berger", "PDF"]),
        ("r!", ["Eskalation 1", "Stadtwerke Nord", "SW-7781230", "Rechnung", "01.09.26", "514,62", "612,40", "612,40", "–", "30.09.26", "11 T.", "T. Berger", "ZUGFeRD"]),
        ("g2", "▸  Fachliche Freigabe  (5)"),
        ("g2", "▸  Zahlungsfreigabe  (3)"),
        ("g1", "▾  10020 Livos Objektgesellschaft Süd mbH  (15 Rechnungen · 97.415,20 € brutto)"),
        ("g2", "▾  Klärfall – Clearing Modus  (2)"),
        ("r!", ["Clearing Modus", "– (Malerbetrieb Kruse)", "MK-0412", "Rechnung", "12.09.26", "2.000,00", "2.380,00", "–", "–", "12.10.26", "4 T.", "SI_Clearing_10020", "PDF"]),
        ("r", ["Clearing Modus", "Bauhof Süd GmbH", "BS-2026-311", "Gutschrift", "15.09.26", "-800,00", "-952,00", "–", "–", "15.10.26", "3 T.", "SI_Clearing_10020", "PDF"]),
        ("g2", "▸  Sachliche Prüfung  (8)"),
        ("g2", "▸  Fachliche Freigabe  (5)"),
        ("g1", "▸  10030 Livos Bau & Projekt GmbH  (12 Rechnungen · 412.908,75 € brutto)"),
    ]
    for kind, v in data:
        if kind in ("g1", "g2"):
            p.box(LX2, y, LW2, 26, v, TD_GRP if kind == "g1" else TD_GRP2)
            y += 26
        else:
            stl = {}
            if kind == "r!":
                stl = {(0, 0): TD_O, (0, 10): TD_R}
            y = p.table(LX2, y, colw, [v], rowh=26, header=False, styles=stl)
    mark(p, LX2 - 22, 224 + 26 + 3, 3)
    cx7 = LX2 + sum(colw[:7])
    mark(p, cx7 + colw[7] - 22, 216, 4)
    cx10 = LX2 + sum(colw[:10])
    mark(p, cx10 + colw[10] - 22, 216, 5)
    p.box(LX2, y + 6, LW2, 20, "▾ aufgeklappt · ▸ eingeklappt · Gruppenzeilen mit Anzahl und Bruttosumme · Zahlbetrag-Spalte nur, sofern im REB verfügbar [O]", "small")
    ay = Y + H - 44
    p.line(52, ay - 10, 1602, ay - 10)
    x0b, xe = btns(p, 296, ay, [("Öffnen", "ui_btn"), ("Gruppieren", "ui_btn2"), ("Filtern", "ui_btn2"), ("CSV-Export (alle Spalten)", "ui_btn2")])
    mark(p, x0b - 12, ay - 8, 6)
    x0b = xe
    p.box(x0b + 10, ay, 1602 - x0b - 10, 28, "ⓘ Archiv nur 6 bzw. 12 Monate – historische Durchlauf-/Liegezeiten je Benutzer/Schritt nur über BeSync-Protokollierung und evidanza (AE-16, T-23).",
          "ui_hint", extra="fontSize=10;")
    items = [
        (1, "**Schnellzugriffe (Vorschlag)**: Offen je Gesellschaft · Liegezeit > 10 Tage · Eskalationen · Klärfälle · Zahlungsfreigabe offen · Monatsende unverbucht – mit Filter und Gruppierung gespeichert [K]."),
        (2, "**Filter / Gruppierung** Mandant → Aktueller Schritt; CSV-Export aller Spalten → evidanza (Stichtagssicht, Monatsabschluss/Rückstellungen AE-08) [S]."),
        (3, "**Gruppenzeilen** mit Anzahl (und Summe) je Mandant und Schritt; auf-/zuklappbar."),
        (4, "**Zusatzspalten** gegenüber M-08: Nettobetrag, Belegart, Zahlbetrag (sofern als Spalte verfügbar [O])."),
        (5, "**Schritt seit** = Liegezeit im aktuellen Schritt (Katalog 3.2); Eskalation und Clearing Modus hervorgehoben."),
        (6, "**Aktionen**: Gruppieren, Filtern, CSV-Export [S]. Kennzahlen-Diagramme nicht im REB/d.velop – liefert evidanza (G-7)."),
    ]
    _notes_cols(p, items, Y + H + 12)


# =========================================================================================== M-10
def m10(doc):
    p = doc.page("M-10 Startseite je Rolle", "p32")
    p.header("M-10 Startseite / Dashboard je Rolle",
             "Rolle: alle (Beispiel R-03 Sachlicher Prüfer) · Werkzeug: d.velop documents Startseite; Administration: Konfiguration › Erscheinungsbild › Startseite · "
             "Umsetzung [S] Widgets; [K] Verknüpfungs-Widgets und Sichtbarkeit je Gruppe")
    X, Y, W, H = 40, 112, 1190, 590
    ui_window(p, X, Y, W, H, "documents  ›  Startseite", "", nav_items=["⌂ Startseite", "✓ Aufgaben (5)", "▤ Rechnungseingangsbuch", "🔍 Suche", "▣ Akten", "★ Favoriten", "⚙ Einstellungen"],
              nav_w=170, user="Thomas B. (Objekt Nord)")
    gx, gy = 222, 160
    cw, gap = 316, 14
    rh = [228, 140]

    def widget(c, r, title, body, n=None, cs=1, hh=None):
        x = gx + c * (cw + gap)
        y = gy + sum(rh[:r]) + r * gap
        w = cw * cs + gap * (cs - 1)
        h = hh or rh[r]
        p.box(x, y, w, h, "", "ui_widget")
        p.box(x, y, w, 28, title, "text", extra=f"fontSize=12;fontStyle=1;fontColor={C['navy']};spacingLeft=10;verticalAlign=middle;fillColor={C['grey_l']};")
        if n is not None:
            mark(p, x + w - 26, y + 4, n)
        return x + 10, y + 36, w - 20
    x, y, w = widget(0, 0, "Aufgaben – Meine Aufgaben (5)", "", n=1)
    for t, s in [("Sachliche Prüfung RE-2026-1041", "Musterbau GmbH · 14.756,00 € · Skonto 29.09."),
                 ("Sachliche Prüfung EH-55812", "Elbe Haustechnik KG · 3.927,00 €"),
                 ("Rückfrage DF-1209", "Dach & Fach GmbH · 5.474,00 €"),
                 ("Sachliche Prüfung 2026-0917", "Glas Petersen OHG · 1.190,00 €")]:
        p.box(x, y, w, 40, f"**{t}**\n{s}", "ui_input", extra="fontSize=10;verticalAlign=middle;")
        y += 45
    x, y, w = widget(1, 0, "Rechnungseingangsbuch – Meine offenen (7)", "", n=2)
    table(p, x, y, [100, 80, 116], [["Kreditor", "Brutto", "Schritt seit"], ["Musterbau GmbH", "14.756,00", "2 T."],
                                     ["Elbe Haustechnik", "3.927,00", "1 T."], ["Glas Petersen", "1.190,00", "6 T."],
                                     ["Stadtwerke Nord", "612,40", "11 T. ⚠"], ["Dach & Fach", "5.474,00", "3 T."]], rowh=24)
    p.box(x, y + 152, w, 20, "→ zum Rechnungseingangsbuch", "text", extra=f"fontSize=10;fontColor={C['teal']};fontStyle=1;")
    x, y, w = widget(2, 0, "Suche", "", n=3)
    p.box(x, y, w, 28, "🔍  Kreditor, Rechnungsnr., Objekt …", "ui_input")
    p.box(x, y + 38, w, 20, "Gespeicherte Suchen", "text", extra="fontSize=10;fontStyle=1;")
    for i, t in enumerate(["Meine Rechnungen BV Hafenstraße 22", "Kürzungen 2026 – Objekt Nord", "Musterbau GmbH – alle Belege"]):
        p.box(x, y + 62 + i * 28, w, 24, "▸ " + t, "text", extra=f"fontSize=10;fontColor={C['teal']};verticalAlign=middle;")
    x, y, w = widget(0, 1, "Zuletzt bearbeitet", "", n=4)
    p.box(x, y, w, 90, "RE-2026-1041 · Musterbau GmbH\nAufmaß 08-2026.pdf\nObjektakte 10010-0001 BV Hafenstraße 22\nDF-1209 · Dach & Fach GmbH",
          "text", extra="fontSize=10;")
    x, y, w = widget(1, 1, "Favorisiert", "")
    p.box(x, y, w, 90, "★ Objektakte 10010-0001 · BV Hafenstraße 22\n★ Kreditorenakte 70012 Musterbau GmbH\n★ Objektakte 10010-0002 · Kaiweg 4", "text", extra="fontSize=10;")
    x, y, w = widget(2, 1, "Beobachtet", "")
    p.box(x, y, w, 90, "👁 RE-2026-1033 · Musterbau GmbH (Mandant 10020)\n👁 Vertrag AV-2026-017 Rohbau", "text", extra="fontSize=10;")
    # Zeile 3 Verknüpfungs-Widgets
    ly = gy + sum(rh) + 2 * gap
    p.box(gx, ly - 2, 990, 20, "Verknüpfungs-Widgets (Ziel-URL, Symbol Pflicht)", "text", extra=f"fontSize=11;fontStyle=1;fontColor={C['teal']};verticalAlign=middle;")
    mark(p, gx + 330, ly - 2, 5)
    for i, (ic, t) in enumerate([("🔎", "Gespeicherte Suche\nBV Hafenstraße 22"), ("▣", "Objektakte\n10010-0001"), ("▤", "REB: Kürzungen\ndieses Monats"), ("＋", "Widget hinzufügen")]):
        bx = gx + i * 246
        p.box(bx, ly + 22, 232, 56, f"{ic}   {t}", "ui_widget", extra="verticalAlign=middle;fontSize=11;" + ("dashed=1;shadow=0;" if ic == "＋" else ""))
    mark(p, gx + 3 * 246 + 208, ly + 16, 6)
    # Widgets je Rolle
    ty = Y + H + 16
    p.box(40, ty, 800, 22, "Widgets je Rolle (Vorschlag, Sichtbarkeit je Gruppe)", "h2", extra="fontSize=13;")
    mark(p, 480, ty + 1, 7)
    roles = ["R-01", "R-02", "R-03", "R-04/05", "R-06", "R-07", "R-11", "R-12"]
    M = [("Aufgaben", "Standard", "xxxxx-xx"), ("Rechnungseingangsbuch", "Standard", "-xxxxx-x"), ("Suche", "Standard", "xxxxxxxx"),
         ("Zuletzt bearbeitet", "Standard", "xxx-x-xx"), ("Beobachtet", "Standard", "-xx---xx"), ("Favorisiert", "Standard", "-xxx-xxx"),
         ("Import-Widget (Dropzones)", "Standard", "xx----x-"), ("Link „Klärfälle“ (REB)", "Verknüpfung", "-x-----x"),
         ("Link „Offen je Gesellschaft“ (REB)", "Verknüpfung", "---x-x--"), ("Link Lieferanten-App", "Verknüpfung", "-x--x--x"),
         ("Link d.velop contracts / Fristen", "Verknüpfung", "------x-"), ("Links gespeicherte Suchen", "Verknüpfung", "-xxx-xx-"),
         ("Link evidanza-Bericht", "Verknüpfung", "---x-x--")]
    rows = [["Widget", "Typ"] + roles] + [[n, t] + ["●" if c == "x" else "–" for c in s] for n, t, s in M]
    colw = [230, 90] + [56] * 8
    stl = {}
    for ri in range(1, len(rows)):
        for ci in range(2, 10):
            stl[(ri, ci)] = S["td_c"] + (f"fillColor={C['teal_l']};fontColor={C['teal']};fontStyle=1;" if rows[ri][ci] == "●" else f"fontColor={C['grey_m']};")
        if ri == 3 or True:
            pass
    # R-03 Spalte hervorheben
    table(p, 40, ty + 28, colw, rows, rowh=21, styles=stl)
    p.box(40 + 230 + 90 + 2 * 56, ty + 28, 56, 21 * len(rows), "", f"rounded=0;fillColor=none;strokeColor={C['orange']};strokeWidth=2;")
    # Grenzen-Box neben Matrix
    gx2 = 40 + sum(colw) + 20
    p.box(gx2, ty + 28, 1230 - gx2, 200, "**Regeln / Grenzen**\n\n"
          "• Nur Standard-Widgets mit Fachinhalt (Suche, Zuletzt bearbeitet, Beobachtet, Favorisiert) plus Aufgaben-, REB- und Import-Widget – keine Diagramm-Widgets [S]\n"
          "• Eigene Widgets nur als Verknüpfung, Liste (serverseitige URL) oder erweitertes Widget (iframe); Listen/iframes mit Fachdaten = Entwicklung [S]/[A]\n"
          "• Sichtbarkeit je Benutzer/Gruppe ist keine Zugriffsbeschränkung (G-8) [S]\n"
          "• „Zuletzt bearbeitet“ zeigt keine Statuswechsel [S]", "warn")
    rcol(p, [
        (1, "**Aufgaben** (Meine Aufgaben) – Standard-Widget, Einstieg in die Belegmaske [S]."),
        (2, "**Rechnungseingangsbuch** mit Schnellzugriff „Meine offenen Rechnungen“ (M-08) [S]."),
        (3, "**Suche** mit gespeicherten Suchen der Rolle (M-12) [S]."),
        (4, "**Zeile 2**: Zuletzt bearbeitet · Favorisiert · Beobachtet (Standard) [S]."),
        (5, "**Zeile 3**: Verknüpfungs-Widgets auf gespeicherte Suchen, Objektakten und REB-Schnellzugriffe [K]."),
        (6, "Anwender können Widgets ergänzen, entfernen und vergrößern (im Workshop gezeigt) [S]."),
        (7, "**Widgets je Rolle**: Zuordnung über Administration „Sichtbarkeit von Widgets → Zuordnungen anwenden“ [K]. Orange Rahmen = Beispielrolle R-03 im Mockup."),
        (8, "**Dashboard-Grenze (G-7)**: keine Kennzahlen-Diagramme in d.velop; Kennzahlen liefern REB (M-09) und evidanza (AE-16)."),
    ])


def build(doc):
    m01(doc)
    m02(doc)
    m03(doc)
    m04(doc)
    m05(doc)
    m06(doc)
    m07(doc)
    m08(doc)
    m09(doc)
    m10(doc)
