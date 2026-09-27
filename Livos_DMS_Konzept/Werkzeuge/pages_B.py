"""Seiten 08-17 (Prozesse Eingangsrechnung, Freigabe, Status, PM, Verträge, Post).
build(doc) legt die Seiten p08 ... p17 an."""
from dio import C, S, E

# ----------------------------------------------------------------------
# lokale Hilfsfunktionen (nur Stile aus dio.py)
# ----------------------------------------------------------------------
LBL = "labelBackgroundColor=#FFFFFF;"


def lanes_h(p, x, y, w, specs, head_w=130):
    """Swimlanes mit waagerechter Kopfbeschriftung. Gibt Liste [(top, mitte, hoehe)] zurück."""
    out, cy = [], y
    for i, (t, h) in enumerate(specs):
        p.box(x, cy, head_w, h, t, "lane_h", extra="horizontal=1;fontSize=11;spacing=4;")
        p.box(x + head_w, cy, w - head_w, h, "", "lane" if i % 2 == 0 else "lane_alt")
        out.append((cy, cy + h / 2, h))
        cy += h
    return out


def T(p, cx, cy, w, h, text, st="task", fs=10, extra="", link=None):
    return p.box(cx - w / 2, cy - h / 2, w, h, text, st, extra=f"fontSize={fs};" + extra, link=link)


def GW(p, cx, cy, text, s=62, fs=9):
    return p.box(cx - s / 2, cy - s / 2, s, s, text, "gateway", extra=f"fontSize={fs};")


def EV(p, cx, cy, label="", kind="start", r=30, pos="below", lw=110, lh=28):
    cid = p.box(cx - r / 2, cy - r / 2, r, r, "", kind)
    if label:
        if pos == "below":
            p.box(cx - lw / 2, cy + r / 2 + 1, lw, lh, label, "small", extra="align=center;fontSize=9;fontColor=#1B1B1B;")
        elif pos == "above":
            p.box(cx - lw / 2, cy - r / 2 - lh - 1, lw, lh, label, "small", extra="align=center;verticalAlign=bottom;fontSize=9;fontColor=#1B1B1B;")
        elif pos == "right":
            p.box(cx + r / 2 + 3, cy - lh / 2, lw, lh, label, "small", extra="verticalAlign=middle;fontSize=9;fontColor=#1B1B1B;")
        elif pos == "left":
            p.box(cx - r / 2 - 3 - lw, cy - lh / 2, lw, lh, label, "small", extra="align=right;verticalAlign=middle;fontSize=9;fontColor=#1B1B1B;")
    return cid


def F(p, a, b, label="", st="flow", ex=None, en=None, pts=None, extra=""):
    return p.edge(a, b, label, st, extra=LBL + extra, points=pts, exit=ex, entry=en)


PROC_LEG = [("task", "d.velop Standard [S]"), ("task_d", "d.velop Konfiguration [K]"),
            ("task_mdis", "MDIS BeSync [A]"), ("task_ext", "Umsystem / extern"),
            ("task_open", "offen / zu verifizieren [O]")]
EDGE_LEG = [("flow", "Sequenz"), ("data", "Datenfluss"), ("msg", "Nachricht / E-Mail"), ("red", "Ablehnen / Zurückweisen")]


def legend_row(p, x, y, items=PROC_LEG, edges=EDGE_LEG, title="Legende"):
    """Einzeilige Legende (Kästchen + Kantentypen)."""
    p.box(x, y, 64, 20, title, "text", extra="fontStyle=1;fontSize=10;verticalAlign=middle;spacing=0;")
    cx = x + 66
    for st, lab in items:
        p.box(cx, y + 2, 24, 16, "", st)
        lw = int(len(lab) * 5.6) + 8
        p.box(cx + 28, y, lw, 20, lab, "text", extra="fontSize=10;verticalAlign=middle;spacing=0;")
        cx += 28 + lw + 12
    for st, lab in (edges or []):
        p.line(cx, y + 10, cx + 34, y + 10, st)
        lw = int(len(lab) * 5.6) + 8
        p.box(cx + 38, y, lw, 20, lab, "text", extra="fontSize=10;verticalAlign=middle;spacing=0;")
        cx += 38 + lw + 12
    return cx


def card(p, x, y, w, h, title, body, st="info", fs=11):
    return p.box(x, y, w, h, f"**{title}**\n{body}", st, extra=f"fontSize={fs};")


# ======================================================================
# p08  ER-Prozess End-to-End (WF-01)
# ======================================================================
def page08(doc):
    p = doc.page("08 ER-Prozess End-to-End (WF-01)", "p08")
    p.header("08 · Eingangsrechnung End-to-End (WF-01)",
             "Standard-Eingangsrechnung vom Eingang bis zum Zahlstatus „bezahlt“ · Rollen R-02…R-06, Schnittstellen S-01/S-06/S-07/S-11 · AE-06, AE-07, AE-10, AE-13")
    X0, W, HW = 40, 1574, 118
    L = lanes_h(p, X0, 112, W, [("Lieferant", 72), ("d.velop System", 84), ("Rechnungseingang\nR-02", 100),
                                 ("Sachl. Prüfer\nR-03", 84), ("Freigeber\nR-04", 100), ("Zahlungs-\nfreigeber R-05", 78),
                                 ("Buchhaltung\nTrios R-06", 84), ("DATEV\n(Hoster)", 84), ("multicash\n(Omikron)", 78),
                                 ("BeSync (MDIS)", 78)], head_w=HW)
    LIEF, DV, R02, R03, R04, R05, TRI, DAT, MC, BS = [l[1] for l in L]
    cx = lambda i: X0 + HW + 50 + i * 96
    tw, th = 90, 56

    st = EV(p, cx(0), LIEF, "Rechnung versendet", "start", r=28, pos="right", lw=110, lh=28)
    t_ein = T(p, cx(0), DV, tw, th, "Eingang\nE-Mail · Scan ·\nE-Rechnung [S]")
    t_erk = T(p, cx(1), DV, tw, th, "Erkennung &\nVorqualifikation\n(Seite 09) [S]", link="data:page/id,p09")
    t_ver = T(p, cx(2), R02, tw, th + 4, "Verteilung M-02\nMandant · Kreditor\n· Kostenobjekt [K]", "task_d")
    g_kl = GW(p, cx(3), R02, "Klärfall?", s=58)
    t_kl = T(p, cx(4), R02 + 8, tw, th, "Klärfall WF-04\nClearing je\nMandant [K]", "task_d", link="data:page/id,p09")
    t_pr = T(p, cx(4), R03, tw, th + 4, "Sachl. Prüfung &\nKontierung M-03\n(KI-Vorschlag) [S]")
    t_zw = T(p, cx(5), R02 + 8, tw, th + 8, "Zurückweisen\nmit Grund E-26\n(aus Verteilung/\nPrüfung) [K]", "task_d")
    e_zw = EV(p, cx(6), R02 + 8, "Zurück-\ngewiesen", "end", r=28, pos="right", lw=60, lh=28)
    i_mail = EV(p, cx(5), LIEF, "Rückweisungsmail erhalten\n(bei Dublette keine Mail)", "inter", r=28, pos="right", lw=160, lh=28)
    t_f1 = T(p, cx(5), R04, tw, th + 4, "Fachl. Freigabe\nStufe 1 M-04\n(Matrix) [K]", "task_d", link="data:page/id,p11")
    g_wg = GW(p, cx(6), R04, "Über\nWertgrenze?", s=60)
    t_f2 = T(p, cx(7), R04, tw, th + 4, "Fachl. Freigabe\nStufe 2\n(Vier-Augen) [K]", "task_d")
    t_zf = T(p, cx(7), R05, tw, th, "Zahlungs-\nfreigabe M-04\n(AE-06) [K]", "task_d")
    t_bh = T(p, cx(8), TRI, tw, th, "Buchhaltung M-07\nKontrolle &\nÜbergabe [K]", "task_d")
    t_s01 = T(p, cx(8), DAT, tw, th + 4, "S-01 Buchungs-\nvorschlag +\nBeleglink [K]", "task_d")
    t_bu = T(p, cx(9), TRI, tw, th, "Buchen in\nDATEV\n(OP entsteht)", "task_ext")
    t_zv = T(p, cx(10), TRI, tw, th, "Zahlungs-\nvorschlag\n(OPOS, Skonto)", "task_ext")
    t_sepa = T(p, cx(10), DAT, tw, th, "SEPA-XML\nerzeugen\n(S-07) [S]", "task_ext")
    t_us = T(p, cx(11), MC, tw, th, "Import &\nUnterschrift\nR-05 (EBICS)", "task_ext")
    t_ka = T(p, cx(12), MC, tw, th, "Kontoauszug\ncamt.053\n→ DATEV", "task_ext")
    t_op = T(p, cx(13), DAT, tw, th, "Zahlung buchen,\nOP ausgleichen\n(Trios)", "task_ext")
    t_s06 = T(p, cx(13), BS, tw, th, "S-06 OPOS lesen\n→ Zahlstatus\n„bezahlt“ [A]", "task_mdis")
    e_end = EV(p, cx(14), BS - 8, "Bezahlt (E-23)", "end", r=28, lw=90, lh=16)

    F(p, st, t_ein, ex=(0.5, 1), en=(0.5, 0))
    F(p, t_ein, t_erk)
    F(p, t_erk, t_ver, ex=(1, 0.5), en=(0.5, 0))
    F(p, t_ver, g_kl)
    F(p, g_kl, t_kl, "ja", ex=(1, 0.5), en=(0, 0.5))
    top02 = L[2][0]
    F(p, t_kl, t_ver, "geklärt", ex=(0.5, 0), en=(0.5, 0), pts=[(cx(4), top02 + 12), (cx(2), top02 + 12)])
    F(p, g_kl, t_pr, "nein", ex=(0.5, 1), en=(0, 0.5))
    F(p, t_pr, t_f1, ex=(0.5, 1), en=(0, 0.5))
    F(p, t_f1, t_pr, "Ablehnen", "red", ex=(0.2, 0), en=(1, 0.75))
    F(p, t_pr, t_zw, "Zurückweisen", "red", ex=(1, 0.2), en=(0.75, 1))
    F(p, t_zw, e_zw, "", "red")
    F(p, t_zw, i_mail, "S-11 Mail via BeSync [A] (ab Phase 2)", "msg", ex=(0.5, 0), en=(0.5, 1))
    F(p, t_f1, g_wg)
    F(p, g_wg, t_f2, "ja", ex=(1, 0.5), en=(0, 0.5))
    F(p, g_wg, t_zf, "nein", ex=(0.5, 1), en=(0, 0.5))
    F(p, t_f2, t_zf, ex=(0.5, 1), en=(0.5, 0))
    F(p, t_zf, t_bh, ex=(1, 0.5), en=(0.5, 0))
    F(p, t_bh, t_s01, ex=(0.5, 1), en=(0.5, 0))
    F(p, t_s01, t_bu, ex=(1, 0.5), en=(0.5, 1))
    F(p, t_bu, t_zv)
    F(p, t_zv, t_sepa, ex=(0.5, 1), en=(0.5, 0))
    F(p, t_sepa, t_us, ex=(1, 0.5), en=(0.5, 0))
    F(p, t_us, t_ka)
    F(p, t_ka, t_op, ex=(1, 0.5), en=(0, 0.5))
    F(p, t_op, t_s06, ex=(0.5, 1), en=(0.5, 0))
    F(p, t_s06, e_end, ex=(1, 0.5), en=(0, 0.5))

    # Hinweise in freien Bahnbereichen
    T(p, (cx(6) + cx(9)) / 2, R03, cx(9) - cx(6) + 60, 50,
      "**Bau-Rechnung (WF-02):** nach der Sachlichen Prüfung folgt der asynchrone BIM4You-Schritt → Seite 10",
      "info", fs=10, extra="align=left;verticalAlign=middle;", link="data:page/id,p10")
    T(p, (cx(7) + cx(13)) / 2, DV, cx(13) - cx(7) + 90, 50,
      "Rechnungseingangsbuch (REB) zeigt je Beleg den aktuellen Schritt, „seit“, Zugewiesen und Status (AE-16). "
      "Zahlstatus/Zahldatum (E-23) setzt BeSync als DMS-Eigenschaft am archivierten Beleg.",
      "info", fs=10, extra="align=left;verticalAlign=middle;")
    T(p, (cx(10) + cx(14)) / 2 + 10, R04, cx(14) - cx(10) + 70, 60,
      "Freigabematrix je Mandant/Kostenobjekt, Stufe 2 ab Wertgrenze über Verbindung mit Bedingung auf "
      "voucher.net_amount in Cent (Beispiel > 500000 = 5.000 € netto) → Seite 11",
      "info", fs=10, extra="align=left;verticalAlign=middle;", link="data:page/id,p11")
    T(p, (cx(10) + cx(14)) / 2 + 10, R02 + 8, cx(14) - cx(10) + 70, 56,
      "Eskalation je Schritt und vor Skonto-/Nettofälligkeit, Vertretung über Abwesenheit → Seite 12. "
      "Sonderfälle (Kürzung, Dublette, § 13b, § 48b …) → Seite 13",
      "info", fs=10, extra="align=left;verticalAlign=middle;", link="data:page/id,p12")

    y = L[-1][0] + L[-1][2] + 10
    legend_row(p, 40, y)
    y += 30
    w3 = (1574 - 2 * 16) / 3
    card(p, 40, y, w3, 92, "Warum die Zahlungsfreigabe vor der DATEV-Übergabe liegt (AE-06)",
         "LDconnect überträgt keine Zahlungssperre. Nach der Übergabe kann der offene Posten sofort in einen "
         "Zahlungsvorschlag laufen. Deshalb übergibt d.velop erst nach der Zahlungsfreigabe an DATEV (S-01).", "info")
    card(p, 40 + w3 + 16, y, w3, 92, "Einstufige Übergabe (AE-08, Entscheidung mit Trios offen)",
         "Kein Vorerfassungsjournal in DATEV. Offene und noch nicht übergebene Rechnungen zeigt das REB mit Status "
         "und CSV-Export (z. B. Monatsende). Option Phase 3: frühe Übergabe mit Postensperre über BeSync [A].", "note")
    card(p, 40 + 2 * (w3 + 16), y, w3, 92, "Zahlung außerhalb von d.velop (AE-10)",
         "Trios bucht und erstellt den Zahlungsvorschlag in DATEV. Unterschrift und Vier-Augen bleiben in multicash. "
         "BeSync liest die offenen Posten (DATEVconnect) und meldet „bezahlt“ an den Beleg zurück (S-06).", "info")
    return p




# ======================================================================
# p09  Eingang, Vorqualifikation und Klärfall (WF-04)
# ======================================================================
def page09(doc):
    p = doc.page("09 Eingang, Vorqualifikation und Klärfall (WF-04)", "p09")
    p.header("09 · Eingang, Vorqualifikation und Klärfall (WF-04)",
             "Eingangskanäle (AE-22), automatische Prüfungen vor dem ersten Benutzerschritt und Behandlung der Klärfälle Mandant, Kreditor, Dublette (AE-09, AE-23)")
    # --- Zone 1 Kanäle
    p.box(40, 116, 300, 830, "1 · Eingangskanäle (AE-22, S-14)", "group_g")
    chans = [
        ("**rechnung@…** zentrale Rechnungsadresse\nemail import über Microsoft Graph (M365) [S]", "task", 62),
        ("**Alias je Gesellschaft**\nrechnung+<MandantNr>@… mit eigenem Importprofil → Vorbelegung Mandant [K]\n(Übernahme testen, OP-02)", "task_d", 84),
        ("**E-Rechnung** XRechnung 3.0 · ZUGFeRD 2.x · Factur-X über dieselben Postfächer; XML ist das Original [S]", "task", 70),
        ("**Papier** → zentraler Scan (R-01, inbound scan) bzw. Scandienstleister (OP-13) [S]", "task", 62),
        ("**Upload** „Rechnung einlesen“ (M-01), Dropzones je Importprofil [S]", "task", 54),
    ]
    y = 156
    chan_ids = []
    for txt, st_, h in chans:
        chan_ids.append(p.box(56, y, 268, h, txt, st_, extra="fontSize=10;align=left;spacingLeft=6;"))
        y += h + 14
    card(p, 56, y + 6, 268, 96, "Kommunikationsweg",
         "inbound → document reader → smart invoice von Beginn an; der alte Weg endet am 01.01.2027. Nur der neue Weg liefert die XRechnung-Prüfberichte.", "info", fs=10)
    card(p, 56, y + 116, 268, 96, "Voraussetzungen",
         "M365 bei Livos (OP-16). C1: 10.000 E-Mails je Monat und Postfach – bei 20–30 Rechnungen/Tag unkritisch. Peppol nicht erforderlich.", "note", fs=10)

    # --- Zone 2 Prüfungen
    p.box(370, 116, 410, 830, "2 · Verarbeitung & Vorqualifikation (automatisch)", "group_g")
    t_imp = p.box(386, 156, 378, 52, "**Import-Stapel → document reader**\nAuslesen Kopf-/Positionsdaten, Visualisierung E-Rechnung [S]", "task", extra="fontSize=10;")
    for cid in chan_ids:
        F(p, cid, t_imp, en=(0, 0.5), extra="endSize=5;")
    checks = [
        ("1", "Pflichtangaben § 14 UStG – Grundprüfung (Name/Anschrift Mandant, USt-IdNr./StNr., Datum, Nummer, Beträge)", "task", "[S]"),
        ("2", "XRechnung-Validierung KoSIT (Syntax, EN 16931), Prüfbericht als Anlage · ZUGFeRD-Profilprüfung", "task", "[S]/[A]"),
        ("3", "Dublette Stufe 1 – document reader: Rechnungsnummer gegen validierte Belege", "task", "[S]"),
        ("4", "Dublette Stufe 2 – smart invoice: Kreditor + Rechnungsnummer, 18 Monate, Annahme nur mit Begründung", "task", "[S]"),
        ("5", "Mandant – Rechnungsempfänger nur über Name + Anschrift (keine USt-IdNr.), Alias-Vorbelegung (AE-23)", "task_d", "[K]"),
        ("6", "Kreditor – USt-IdNr., Name, Anschrift, Bankverbindung gegen Kreditoren des Mandanten (S-02)", "task", "[S]"),
        ("7", "IBAN – vorhanden; Abgleich Beleg-IBAN ↔ Stamm-IBAN, Anzeige der Warnung testen (OP-10)", "task_open", "[O]"),
        ("8", "Zahlungsbedingung – Hinweis bei Abweichung vom Kreditor-Standard; Skonto-/Nettofälligkeit", "task", "[S]"),
        ("9", "Bau-Kreditor – FSB-Status § 48b über BeSync an der Startverbindung (AE-15, Phase 3)", "task_mdis", "[A]"),
    ]
    y = 226
    for n, txt, st_, tag in checks:
        p.box(386, y, 26, 26, n, "ann")
        p.box(418, y - 6, 346, 60, f"{txt}  **{tag}**", st_, extra="fontSize=10;align=left;spacingLeft=6;")
        y += 74
    p.box(386, y - 4, 378, 30, "Ergebnis: Beleg mit Mandant, Kreditor und Hinweisen → Weichen", "text",
          extra="fontSize=10;fontStyle=2;")

    # --- Zone 3 Weichen
    GX = 880
    p.box(810, 116, 140, 24, "3 · Weichen", "h2", extra="fontSize=13;")
    g1 = GW(p, GX, 235, "Mandant\nerkannt?", s=84, fs=10)
    g2 = GW(p, GX, 480, "Kreditor\nvorhanden?", s=84, fs=10)
    g3 = GW(p, GX, 725, "Dublette?", s=84, fs=10)
    t_fin = T(p, GX, 895, 190, 60, "**Verteilung M-02** → Sachliche Prüfung\n(WF-01, Seite 08) [K]", "task_d", fs=10, link="data:page/id,p08")
    F(p, t_imp, g1, ex=(1, 0.5), en=(0, 0.5))
    F(p, g1, g2, "ja", ex=(0.5, 1), en=(0.5, 0))
    F(p, g2, g3, "ja", ex=(0.5, 1), en=(0.5, 0))
    F(p, g3, t_fin, "nein", ex=(0.5, 1), en=(0.5, 0))

    RX, RW = 960, 654
    # Zeile A Mandant
    p.box(RX, 128, RW, 222, "A · Klärfall Mandant nicht erkannt", "group")
    a1 = p.box(980, 200, 180, 70, "Standardmandant „Klärfall“ → Clearing-Gruppe (REB „Clearing Modus“, M-05) [K]", "task_d", extra="fontSize=10;")
    a2 = p.box(1190, 158, 190, 64, "R-02 ordnet Mandant zu; Kreditor wird neu ermittelt [S]", "task", extra="fontSize=10;")
    a2b = p.box(1190, 236, 190, 50, "Gesellschaft fehlt: Anlage im Stamm (R-12, AE-28) [A]", "task_mdis", extra="fontSize=10;")
    a3 = p.box(1190, 296, 190, 46, "Livos nicht Empfänger → Rückweisung Grund 2 [K]", "task_d", extra="fontSize=10;")
    card(p, 1400, 158, 200, 184, "Vorbeugen (AE-23)",
         "exakte Gesellschaftsbezeichnung im Lieferantenanschreiben · Käuferreferenz BT-10 bei E-Rechnungen · Alias je Gesellschaft · Test mit echten Livos-Belegen (OP-02)", "note", fs=10)
    F(p, g1, a1, "nein", ex=(1, 0.5), en=(0, 0.5))
    F(p, a1, a2, ex=(1, 0.3), en=(0, 0.5))
    F(p, a1, a2b, ex=(1, 0.7), en=(0, 0.5))
    F(p, a1, a3, "", "red", ex=(0.5, 1), en=(0, 0.5))
    F(p, a2, g2, "Mandant gesetzt", ex=(1, 0.5), en=(0.5, 0), pts=[(1392, 190), (1392, 362), (GX, 362)])
    # Zeile B Kreditor
    p.box(RX, 372, RW, 214, "B · Klärfall Kreditor fehlt (AE-09, S-05)", "group")
    bw = 146
    bx = [976 + i * (bw + 14) for i in range(4)]
    b1 = p.box(bx[0], 440, bw, 84, "Anlage-Anforderung an Trios: Phase 1 per E-Mail, ab Phase 2 aus der Lieferanten-App (M-16, S-05) [A]", "task_mdis", extra="fontSize=10;")
    b2 = p.box(bx[1], 440, bw, 84, "Trios legt Kreditor in DATEV an (je Mandant, 70000er-Kreis)", "task_ext", extra="fontSize=10;")
    b3 = p.box(bx[2], 440, bw, 84, "LDconnect-Sync S-02 (täglich) → Kreditor im Bucket; BeSync ergänzt E-07 [K]", "task_d", extra="fontSize=10;")
    b4 = p.box(bx[3], 440, bw, 84, "Wiedervorlage im Klärfall → Beleg läuft mit Kreditor weiter (Folgetag) [S]", "task", extra="fontSize=10;")
    p.box(976, 534, 500, 44, "Livos legt keine Kreditoren in DATEV an. Eskalation nach 2 AT an Leitung Kreditorenbuchhaltung (Vorschlag), weil Skontofristen laufen.",
          "text", extra="fontSize=10;fontStyle=2;")
    F(p, g2, b1, "nein", ex=(1, 0.5), en=(0, 0.5))
    F(p, b1, b2); F(p, b2, b3); F(p, b3, b4)
    F(p, b4, g3, "Kreditor gesetzt", ex=(0.5, 1), en=(0.5, 0), pts=[(bx[3] + bw / 2, 602), (GX, 602)])
    # Zeile C Dublette
    p.box(RX, 618, RW, 232, "C · Klärfall Dublettenverdacht (Mail und Post, PDF und E-Rechnung)", "group")
    c1 = p.box(976, 690, 170, 70, "R-02 vergleicht mit dem Original (Link in der Warnung) [S]", "task", extra="fontSize=10;")
    gc = GW(p, 1210, 725, "Echte\nDublette?", s=74, fs=9)
    c2 = p.box(1290, 650, 190, 60, "Ablehnen mit Grund „Dublette“ – ohne Lieferantenmail [K]", "task_d", extra="fontSize=10;")
    ce = EV(p, 1530, 680, "Zurückgewiesen\n(verknüpft mit Original)", "end", r=28, pos="below", lw=130, lh=28)
    c3 = p.box(1290, 752, 190, 60, "Warnung mit Pflicht­begründung akzeptieren (Protokoll) [S]", "task", extra="fontSize=10;")
    F(p, g3, c1, "ja", ex=(1, 0.5), en=(0, 0.5))
    F(p, c1, gc)
    F(p, gc, c2, "ja", "red", ex=(0.5, 0), en=(0, 0.5))
    F(p, c2, ce, "", "red")
    F(p, gc, c3, "nein", ex=(0.5, 1), en=(0, 0.5))
    F(p, c3, t_fin, "weiter", ex=(0.5, 1), en=(1, 0.5), pts=[(1385, 857), (1000, 857), (1000, 895)])

    card(p, 1020, 866, 594, 78, "Falsch zugeordnet (nach der Verteilung erkannt)",
         "Prüfer oder Freigeber meldet falschen Mandanten/Kreditor → Clearing-Modus: Clearing-Gruppe korrigiert, alle Felder beschreibbar, Änderungen im Workflowprotokoll [S].", "info", fs=10)
    legend_row(p, 40, 962)
    card(p, 40, 994, 780, 76, "Clearing je Mandant [K]",
         "Globale Clearing-Gruppe SI_Clearing_Zentral (Kreditorenbuchhaltung Livos); SI_Clearing_<MandantNr> nur dort, wo eine eigene Buchhaltungsverantwortung besteht. "
         "WF-04 ist ein fachlich eigener Prozess (AE-04), technisch Klärfall-Schritt und Clearing in WF-01 bis WF-03; eine eigene Definition bleibt möglich.", "info", fs=10)
    card(p, 834, 994, 780, 76, "Jede Automatik hat einen Klärfall-Ausgang (P7)",
         "Hinweise (Dublette, Zahlungsbedingung, IBAN, § 13b-Plausibilität) quittiert R-02 in der Verteilung. Rückweisungen an den Lieferanten laufen über WF-05 (Seite 13); "
         "IBAN-Abweichung und § 48b sind Sonderfälle mit eigener Behandlung.", "note", fs=10)
    return p


# ======================================================================
# p10  Bau-Rechnung mit BIM4You (WF-02)
# ======================================================================
def page10(doc):
    p = doc.page("10 Bau-Rechnung mit BIM4You (WF-02)", "p10")
    p.header("10 · Bau-Eingangsrechnung mit BIM4You (WF-02)",
             "Asynchroner Transfer an BIM4You nach der Sachlichen Prüfung · S-08 Hinweg, S-09 Rückweg · AE-11 · Nur d.velop übergibt Eingangsrechnungen an DATEV")
    X0, W, HW = 40, 1574, 140
    L = lanes_h(p, X0, 116, W, [("d.velop\n(smart invoice)", 190), ("BeSync (MDIS)", 170), ("BIM4You\n(BIB GmbH)", 160),
                                 ("Rechnungsprüfung\nR-02 / R-03", 160)], head_w=HW)
    DV, BS, BIM, RP = [l[1] for l in L]
    DVt = DV - 30
    cx = lambda i: X0 + HW + 56 + i * 110.5
    tw, th = 104, 78
    st = EV(p, cx(0), DVt, "Bau-Rechnung\neingegangen", "start", r=30, lw=100, lh=28)
    t_erk = T(p, cx(1), DVt, tw, th + 8, "Erkennung Bau: Objekt = Bauprojekt, Belegart Abschlag/ Schluss, Kreditor Bauleistender [K]", "task_d", fs=10)
    t_pr = T(p, cx(2), RP, tw, th + 8, "Verteilung & Sachl. Prüfung (Vorprüfung, Nachweise) [K]", "task_d", fs=10)
    t_tr = T(p, cx(3), DVt, tw, th + 8, "Verbindung „Bauprüfung“: asynchroner Transfer (Abhol-API) [S/K]", "task_d", fs=10)
    t_s08 = T(p, cx(4), BS, tw, th + 14, "S-08 Beleg abholen: Kopfdaten, PDF/XML, Beleg-ID als Barcode/ Referenz [A]", "task_mdis", fs=10)
    t_imp = T(p, cx(5), BIM, tw, th, "Import\n(E-Rechnungs-\nimport / Ordner)", "task_ext", fs=10)
    t_chk = T(p, cx(6), BIM, tw, th + 8, "Budgetabgleich, kumulierte VOB-Prüfung, Einbehalte, Nachträge", "task_ext", fs=10)
    t_frg = T(p, cx(7), BIM, tw, th, "Prüfer-Workflow RP1/RP2, Freigabe in BIM4You", "task_ext", fs=10)
    t_s09 = T(p, cx(8), BS, tw, th + 34, "S-09 Ergebnis pollen · E-22 setzen · Prüfbericht K-08 ablegen · Transfer melden [A]", "task_mdis", fs=10)
    g_ok = GW(p, cx(9), DVt, "Transfer\nerfolgreich?", s=66)
    t_kl = T(p, cx(9), RP, tw, th + 8, "Fehler-/Klärschritt: BIM4You-Stand prüfen, erneut übergeben oder ablehnen", "task_d", fs=10)
    t_zb = T(p, cx(10), RP, tw, th + 8, "Zahlbetrag manuell (pay_amount) + Kürzungsgrund „Einbehalt“ [K]", "task_d", fs=10)
    t_fr = T(p, cx(11), DVt, tw, th + 8, "Fachl. Freigabe → Zahlungs-freigabe → Buchhaltung (WF-01) [K]", "task_d", fs=9, link="data:page/id,p08")
    t_dat = T(p, cx(12), DVt, tw, th, "S-01 → DATEV\nnur aus d.velop [K]", "task_d", fs=10)
    e_end = EV(p, cx(12), DV + 60, "Übergeben", "end", r=26, pos="left", lw=60, lh=20)

    F(p, st, t_erk)
    F(p, t_erk, t_pr, ex=(1, 0.5), en=(0.5, 0))
    F(p, t_pr, t_tr, ex=(1, 0.5), en=(0.25, 1))
    F(p, t_tr, t_s08, "Export", "data", ex=(0.75, 1), en=(0, 0.5))
    F(p, t_s08, t_imp, "Datei / Import", "data", ex=(1, 0.5), en=(0.5, 0))
    F(p, t_imp, t_chk)
    F(p, t_chk, t_frg)
    F(p, t_frg, t_s09, "Ergebnis", "data", ex=(1, 0.5), en=(0.5, 1))
    F(p, t_s09, g_ok, "successful\ntrue/false", "data", ex=(0.5, 0), en=(0, 0.5))
    F(p, g_ok, t_zb, "ja", ex=(1, 0.5), en=(0.5, 0))
    F(p, g_ok, t_kl, "nein / Timeout", "red", ex=(0.5, 1), en=(0.5, 0))
    F(p, t_zb, t_fr, ex=(1, 0.5), en=(0.5, 1))
    F(p, t_fr, t_dat)
    F(p, t_dat, e_end, ex=(0.5, 1), en=(0.5, 0))
    # Transferfenster
    T(p, (cx(4) + cx(7)) / 2, DV + 62, cx(7) - cx(4) + 70, 42,
      "Status „Warten auf BIM4You“ = Phase „aktiver Belegdatentransfer“ im REB · Fenster max. 28 Tage (Vorschlag 14 Tage), danach Fehlerschritt",
      "info", fs=10, extra="align=center;verticalAlign=middle;")
    # BIM4You-DATEV deaktiviert
    p.box(X0 + HW + 12, BIM - 42, 250, 84,
          "**BIM4You-DATEV-Connector für Eingangsrechnungen deaktiviert**\nkeine Doppelübergabe (P4); führendes System je Rechnungstyp mit Livos/BIB klären (OP-06)",
          "open", extra="fontSize=10;align=left;verticalAlign=middle;spacingLeft=8;")
    p.box(X0 + HW + 12, BS - 34, 250, 68,
          "**S-10 Stammdaten** BIM4You → smart invoice: Projekte, Vergabeeinheiten, Verträge als Custom Entities (nächtlich) [A]",
          "task_mdis", extra="fontSize=10;align=left;verticalAlign=middle;spacingLeft=8;")

    y = L[-1][0] + L[-1][2] + 12
    legend_row(p, 40, y)
    y += 32
    w3 = (1574 - 2 * 16) / 3
    card(p, 40, y, w3, 170, "Rückweg in d.velop (S-09)",
         "BeSync setzt DMS-Eigenschaften E-22 (geprüfter Betrag, Sicherheitseinbehalt, Freigabestatus BIM4You) und legt den Prüfbericht bzw. die "
         "Zahlungsfreigabe als K-08 in der Vorgangsakte ab. Ablehnung in BIM4You → successful = false mit Meldetext → Fehler-/Klärschritt.", "info", fs=12)
    card(p, 40 + w3 + 16, y, w3, 170, "Zahlbetrag manuell (OP-07)",
         "Ein API-Schreibzugriff auf laufende smart-invoice-Belege ist nicht dokumentiert. Die Rechnungsprüfung überträgt den BIM4You-Zahlbetrag in pay_amount "
         "mit Kürzungsgrund „Einbehalt“ bzw. „Bauabzug 15 %“. Automatische Übernahme nur nach Bestätigung durch d.velop.", "note", fs=12)
    card(p, 40 + 2 * (w3 + 16), y, w3, 170, "Abgrenzung und Übergang",
         "BIM4You führt Budget, Vertrag/Nachtrag, VOB-Kumulation und Einbehalte; d.velop führt Beleg, Workflow, Freigabe und DATEV-Übergabe. "
         "Storno in BIM4You wird gespiegelt. Sonderbuchungsinfos (ARAP/PARP, Rückstellungen) Folgeprojekt. Pilot-Bau in Phase 1: über WF-01 ohne BIM4You-Automatik; Prüfer trägt Zahlbetrag mit Kürzungsgrund ein. WF-02 ab Phase 3.", "info", fs=12)
    return p


# ======================================================================
# p11  Freigabematrix und Wertgrenzen
# ======================================================================
def page11(doc):
    p = doc.page("11 Freigabematrix und Wertgrenzen", "p11")
    p.header("11 · Freigabematrix und Wertgrenzen",
             "Gesellschaftsindividuelle Freigaben über Regeln statt Workflowkopien (AE-05, P6) · Freigabematrix, Wertgrenzen-Verbindungen, Vier-Augen-Prinzip")
    p.box(40, 112, 860, 26, "Freigabematrix in smart invoice (Pflege M-17 durch R-12)", "h2")
    p.box(40, 142, 860, 34, "BEISPIEL – fiktive Gesellschaften und Grenzen. Livos legt Grenzen und Personenketten im Prozess-Workshop fest (OP-17).",
          "warn", extra="fontSize=11;fontStyle=1;verticalAlign=middle;")
    rows = [["Mandant", "Kostenobjekt", "Rang", "Bearbeiter (Gruppe)", "Freigabegrenze netto", "Bedeutung (Beispiel)"],
            ["10010 NORD", "* (alle)", "1", "Asset Manager NORD (SI_Freigeber_10010)", "bis 5.000 €", "eine Freigabe bis 5.000 €"],
            ["10010 NORD", "*", "2", "Leitung Asset Management", "bis 25.000 €", "2. Stufe 5.000–25.000 €"],
            ["10010 NORD", "*", "3", "Geschäftsführung NORD", "unbegrenzt", "über 25.000 € GF"],
            ["10020 SUED", "*", "1", "Asset Manager SUED (SI_Freigeber_10020)", "bis 5.000 €", "wie NORD"],
            ["10020 SUED", "*", "2", "Leitung Asset Management", "bis 25.000 €", "wie NORD"],
            ["10020 SUED", "*", "3", "Geschäftsführung SUED", "unbegrenzt", "wie NORD"],
            ["10030 BAUP", "*", "1", "Projektleitung Bau (SI_Freigeber_10030)", "bis 10.000 €", "Bau mit höherer 1. Stufe"],
            ["10030 BAUP", "*", "2", "Leitung Projektentwicklung", "bis 50.000 €", ""],
            ["10030 BAUP", "*", "3", "Geschäftsführung BAUP", "unbegrenzt", ""],
            ["10010 NORD", "VERW (Verwaltung)", "1", "Kaufmännische Leitung", "bis 25.000 €", "abweichende Kette Verwaltung"]]
    yend = p.table(40, 184, [96, 120, 46, 268, 130, 200], rows, rowh=28)
    p.box(40, yend + 6, 860, 58,
          "Strategie „Von unten zum Freigeber“: smart invoice sammelt Freigaben aufsteigend nach Rang, bis ein Freigeber mit ausreichender Grenze erreicht ist [S]. "
          "Gruppen statt Personen; neue Gesellschaft = neue Matrixzeilen, kein neuer Workflow (P6). Auswertung case-sensitiv; * = alle, leer = alle.",
          "text", extra="fontSize=11;")
    # Rechenbeispiel
    y0 = yend + 76
    p.box(40, y0, 860, 24, "Beispiel RE-2026-1041 · Musterbau GmbH · 10010 NORD · netto 12.400,00 € (brutto 14.756,00 €)", "h2", extra="fontSize=13;")
    chain = [("Sachliche Prüfung\nR-03 (Prüfer ≠ Freigeber)", "task"), ("Stufe 1 Asset Manager NORD\nSI_Freigeber_10010\n(bis 5.000 €)", "task_d"),
             ("Stufe 2\nLeitung Asset Management\n(bis 25.000 €) erreicht", "task_d"), ("Zahlungsfreigabe R-05\nSI_Zahlung_10010", "task_d")]
    ids = []
    for i, (t, st_) in enumerate(chain):
        ids.append(p.box(40 + i * 222, y0 + 34, 190, 62, t, st_, extra="fontSize=10;"))
    for a, b in zip(ids, ids[1:]):
        F(p, a, b)
    # Kostenobjekt-Hinweis
    y1 = y0 + 116
    p.box(40, y1, 860, 150, "", "warn")
    p.box(52, y1 + 6, 836, 22, "Wertgrenze gilt je Kostenobjekt, nicht je Rechnung (smart invoice Cloud Handbuch 06/2026)", "text", extra="fontStyle=1;fontSize=12;")
    inv = p.box(60, y1 + 50, 150, 70, "Rechnung\n25.000 € netto", "doc", extra="fontSize=11;")
    k1 = p.box(290, y1 + 40, 170, 38, "KST A: 17.000 €", "task", extra="fontSize=10;")
    k2 = p.box(290, y1 + 92, 170, 38, "KST B: 8.000 €", "task", extra="fontSize=10;")
    F(p, inv, k1, ex=(1, 0.5), en=(0, 0.5)); F(p, inv, k2, ex=(1, 0.5), en=(0, 0.5))
    p.box(480, y1 + 36, 408, 104,
          "Jedes Kostenobjekt wird einzeln gegen die Grenzen geprüft. Eine Rechnung über der Gesamtgrenze kann so mit Teilfreigaben unterhalb der Grenze laufen. "
          "**Gegenmaßnahme:** Wertgrenzen-Verbindung auf den Rechnungsnettobetrag (rechts), die ab Betrag X unabhängig von der Aufteilung eine Stufe erzwingt.",
          "text", extra="fontSize=11;")

    y2 = y1 + 170
    p.box(40, y2, 860, 26, "Personenketten (Beispiele, Kapitel 10.2.4)", "h2", extra="fontSize=13;")
    p.table(40, y2 + 32, [330, 530], [["Kette", "Anwendung"],
            ["Asset Manager → Leitung AM → GF", "Bestand/Privatisierung, objektbezogene Kosten"],
            ["Projektleitung → Leitung Projektentwicklung → GF", "Bau (nach BIM4You-Prüfung, WF-02)"],
            ["Kaufmännische Leitung → GF", "Verwaltungs- und Gesellschaftskosten"],
            ["Asset Management", "PM-Freigaben (WF-03, Seite 15)"]], rowh=26)

    # rechts: Entscheidungslogik
    RX = 940
    p.box(RX, 112, 674, 26, "Entscheidungslogik am Schritt „Fachliche Freigabe Stufe 1“", "h2")
    stp = p.box(RX, 190, 150, 250, "**Schritt**\nFachliche Freigabe Stufe 1\n\n(Freigabeschritt mit Pflichtaktionen Bestätigen / Ablehnen)", "task_d", extra="fontSize=11;")
    p.box(RX + 180, 148, 494, 30, "Verbindungen werden top-down ausgewertet – die erste zutreffende gewinnt", "text", extra="fontSize=11;fontStyle=2;verticalAlign=middle;")
    conns = [("1", "Bestätigen · Bedingung\nvoucher.net_amount > 2500000\n(> 25.000,00 € netto)", "Freigabe GF\n(Geschäftsführung Mandant)", "flow"),
             ("2", "Bestätigen · Bedingung\nvoucher.net_amount > 500000\n(> 5.000,00 € netto)", "Fachliche Freigabe\nStufe 2", "flow"),
             ("3", "Bestätigen · ohne Bedingung\n(Standardverbindung)", "Zahlungsfreigabe", "flow"),
             ("4", "Ablehnen · Kommentar Pflicht", "Sachliche Prüfung\n(Rückfrage)", "red")]
    for i, (n, ctext, target, est) in enumerate(conns):
        yy = 190 + i * 66
        c = p.box(RX + 200, yy, 262, 56, f"**{n}.** " + ctext, "ui_ro" if est == "red" else "ui_ai", extra="fontSize=10;fontColor=#1B1B1B;align=left;spacingLeft=6;")
        tg = p.box(RX + 504, yy + 4, 170, 48, target, "task_d" if est != "red" else "task", extra="fontSize=10;")
        F(p, c, tg, "", est)
        F(p, stp, c, "", "data", ex=(1, (yy + 28 - 190) / 250), en=(0, 0.5))
    p.box(RX, 460, 674, 70,
          "Beträge in Bedingungen stehen in Cent (10.000,00 € = 1000000). Bezugsgröße ist netto (Standardbedingung voucher.net_amount; Livos bestätigt, AE-05). "
          "Höchste Grenze steht oben. Jede Grenze in der Abnahme mit Beträgen knapp darunter und darüber testen. Alle Grenzen: Beispiele.",
          "info", extra="fontSize=11;")
    p.box(RX, 540, 674, 56,
          "Mandantenabhängige Grenzen: zusätzliche Verbindung mit Bedingung auf Mandant (voucher.company.nr) und Betrag vor Regel 2 – Syntax im Test-Tenant bestätigen [O].",
          "note", extra="fontSize=11;")
    # Vier-Augen
    p.box(RX, 612, 674, 26, "Vier-Augen-Prinzip", "h2")
    va = [("Prüfer ≠ Freigeber: Wer sachlich geprüft hat, erhält die Freigabe desselben Belegs nicht (Leistungsbeschreibung 12/2025).", "task", "[S]"),
          ("Zweite Freigabe ab Betrag X über Wertgrenzen-Verbindung oder Matrix-Strategie „Von unten zum Freigeber“; getrennte Gruppen je Stufe.", "task_d", "[K]"),
          ("Freigeber ≠ Zahlungsfreigeber (Vorschlag: nicht die letzte fachliche Freigabe, Test T41). „Freigabe überspringen“ wird nicht aktiviert.", "task_d", "[K]"),
          ("Vorschau-Feature „Vier-Augen-Prinzip in der Freigabe“ nur nach Freigabe durch d.velop (OP-09).", "task_open", "[O]"),
          ("Zahlungsausführung: Unterschrift in multicash nach Unterschriftsklassen.", "task_ext", "[S]")]
    for i, (t, st_, tag) in enumerate(va):
        p.box(RX, 646 + i * 58, 674, 50, f"{t}  **{tag}**", st_, extra="fontSize=11;align=left;spacingLeft=8;")
    legend_row(p, 40, 1090, edges=[("flow", "Sequenz / Verbindung"), ("red", "Ablehnen")])
    return p


# ======================================================================
# p12  Eskalation und Vertretung
# ======================================================================
def page12(doc):
    p = doc.page("12 Eskalation und Vertretung", "p12")
    p.header("12 · Eskalation und Vertretung",
             "Eskalationsfristen je Schritt und vor Skonto-/Nettofälligkeit, Empfänger je Mandant (AE-17) · Vertretung über Abwesenheit (M-18) · alle Fristen sind Vorschläge")
    p.box(40, 112, 1200, 26, "A · Statische Eskalation je Schritt (Vorschlag in Arbeitstagen, einheitlich für alle Gesellschaften – P6)", "h2")
    TX, DAY, NDAY = 330, 95, 9
    p.box(40, 146, 280, 22, "Schritt (Rolle)", "text", extra="fontStyle=1;fontSize=11;verticalAlign=middle;")
    for d in range(NDAY + 1):
        p.box(TX + d * DAY - 20, 146, 40, 22, f"{d} AT", "textc", extra="fontSize=10;")
        p.line(TX + d * DAY, 170, TX + d * DAY, 178 + 6 * 58 - 10, "assoc")
    p.box(TX + NDAY * DAY + 30, 146, 1614 - (TX + NDAY * DAY + 30), 22, "Empfänger Stufe 1 / Stufe 2 (Beispiele)", "text",
          extra="fontStyle=1;fontSize=11;verticalAlign=middle;")
    rows = [("Verteilung / Klärfall (R-02)", 2, 4, "Leitung Kreditorenbuchhaltung / Leitung Finanzen"),
            ("Sachliche Prüfung (R-03)", 3, 6, "Teamleitung des Prüfers (Gruppe je Mandant) / Leitung AM bzw. Projektentwicklung"),
            ("Fachliche Freigabe je Stufe (R-04)", 3, 6, "nächsthöhere Freigabestufe des Mandanten / Geschäftsführung des Mandanten"),
            ("Zahlungsfreigabe (R-05)", 1, 2, "Stellvertretung Zahlungsfreigabe / Leitung Finanzen/Treasury"),
            ("Buchhaltung (Trios, R-06)", 2, 4, "Teamleitung Trios / Leitung Finanzen Livos"),
            ("Warten auf BIM4You (WF-02)", 0, 0, "Transferfenster (Vorschlag 14 Tage, max. 28) → Fehlerschritt, R-02 prüft")]
    RXE = TX + NDAY * DAY + 30
    for i, (lab, f1, f2, emp) in enumerate(rows):
        y = 178 + i * 58
        p.box(40, y, 280, 46, lab, "task_d" if f1 else "task_mdis", extra="fontSize=11;align=left;spacingLeft=8;")
        if f1:
            p.box(TX, y + 10, f1 * DAY, 26, "in Frist", "ui_ok", extra="align=center;")
            p.box(TX + f1 * DAY, y + 10, (f2 - f1) * DAY, 26, "Stufe 1 aktiv", "ui_hint", extra="align=center;")
            p.box(TX + f2 * DAY, y + 10, (NDAY - f2) * DAY, 26, "Stufe 2 aktiv", "ui_err", extra="align=center;")
            p.box(TX + f1 * DAY - 26, y - 6, 52, 16, f"S1: {f1} AT", "badge_o")
            p.box(TX + f2 * DAY - 26, y - 6, 52, 16, f"S2: {f2} AT", "badge_r")
        else:
            p.box(TX, y + 10, NDAY * DAY, 26, "kein Benutzerschritt: Phase „aktiver Belegdatentransfer“ – Überwachung über Transferfenster und tägliche Abstimmliste BeSync",
                  "info", extra="fontSize=10;align=center;verticalAlign=middle;")
        p.box(RXE, y, 1614 - RXE, 46, emp, "text", extra="fontSize=10;verticalAlign=middle;")
    # dynamisch
    y0 = 178 + 6 * 58 + 12
    p.box(40, y0, 1200, 26, "Dynamische Eskalation vor Fälligkeit (Beispiel Zahlungsbedingung 14 Tage 2 % Skonto, 30 Tage netto)", "h2", extra="fontSize=13;")
    CX, CD = 330, 30
    yb = y0 + 60
    p.box(CX, yb, 14 * CD, 22, "Skontofrist läuft", "ui_ok", extra="align=center;")
    p.box(CX + 14 * CD, yb, 16 * CD, 22, "nur noch Nettofrist", "ui_hint", extra="align=center;")
    for d, lab in [(0, "Rechnungsdatum\nTag 0"), (14, "Skontofrist\nTag 14"), (30, "Nettofälligkeit\nTag 30")]:
        p.line(CX + d * CD, yb - 8, CX + d * CD, yb + 30, "line")
        p.box(CX + d * CD - 55, yb + 32, 110, 30, lab, "textc", extra="fontSize=10;")
    for d, lab in [(11, "3 Tage vor Skonto"), (25, "5 Tage vor netto")]:
        p.box(CX + d * CD - 55, yb - 34, 110, 20, lab, "badge_o")
        p.line(CX + d * CD, yb - 14, CX + d * CD, yb + 22, "red")
    p.box(40, yb - 10, 280, 70, "An aktuellen Bearbeiter und Leitung Kreditorenbuchhaltung; bei Skonto-/Nettofrist 0 oder leer keine dynamische Eskalation.",
          "text", extra="fontSize=10;")
    p.box(1270, yb - 34, 344, 96, "**Ampeln (Vorschlag):** Fälligkeitsampel gelb ab 10, rot ab 5 Tagen vor netto; Skontoampel gelb/rot/dunkelrot. "
          "REB-Filter „Skonto in den nächsten 5 Tagen“.", "note", extra="fontSize=10;")
    y1 = yb + 76
    w4 = (1574 - 3 * 14) / 4
    infos = [("Empfänger je Mandant [K]", "Bearbeiterfindung per Regex auf Gruppennamen, z. B. /^SI_Eskalation_#{voucher.company.nr}$/ – eine Eskalationsgruppe je Gesellschaft bzw. Verbund."),
             ("Wirkung [S]", "Eskalation benachrichtigt, sie weist nicht neu zu. REB-Schnellzugriff „An mich eskalierte Rechnungen“, Statusspalte Stufe 1/2."),
             ("Kanal [O]", "Ob die Eskalation zusätzlich per E-Mail zugestellt wird, ist nicht dokumentiert → Test im Test-Tenant (OP-10)."),
             ("Grenzen [S]", "Arbeitstage zählen das Wochenende nicht, Feiertage schon. Globale 2. Stufe gilt für alle Schritte; unterschiedliche Fristen je Gesellschaft nicht vorgesehen.")]
    for i, (t, b) in enumerate(infos):
        card(p, 40 + i * (w4 + 14), y1, w4, 86, t, b, "info" if i != 2 else "note", fs=10)

    # B Vertretung
    y2 = y1 + 104
    p.box(40, y2, 1200, 26, "B · Vertretung (AE-17, M-18)", "h2")
    yf = y2 + 36
    s0 = EV(p, 70, yf + 50, "Abwesenheit", "start", r=30, pos="below", lw=80, lh=16)
    v1 = p.box(120, yf, 250, 44, "geplant: Mitarbeiter setzt Abwesenheit, Zeitraum und Vertretung im Profil [S]", "task", extra="fontSize=10;")
    v2 = p.box(120, yf + 56, 250, 44, "ungeplant: Admin/Vorgesetzte (R-12) setzt Abwesenheit für erkrankte Kollegen [S]", "task", extra="fontSize=10;")
    v3 = p.box(420, yf + 22, 220, 56, "neue persönliche Aufgaben gehen an die Vertretung; REB „Rechnungen in Vertretung“ [S]", "task", extra="fontSize=10;")
    v4 = p.box(690, yf + 22, 220, 56, "offene Aufgaben gesammelt weiterleiten (berechtigte Personen) [S]", "task", extra="fontSize=10;")
    v5 = p.box(960, yf + 22, 220, 56, "Vertreter wird beim Öffnen Workflowbeteiligter und erhält Leserecht; Protokoll [S]", "task", extra="fontSize=10;")
    e0 = EV(p, 1230, yf + 50, "Rückkehr", "end", r=30, pos="below", lw=80, lh=16)
    F(p, s0, v1, ex=(1, 0.5), en=(0, 0.5)); F(p, s0, v2, ex=(1, 0.5), en=(0, 0.5))
    F(p, v1, v3, ex=(1, 0.5), en=(0, 0.3)); F(p, v2, v3, ex=(1, 0.5), en=(0, 0.7))
    F(p, v3, v4); F(p, v4, v5); F(p, v5, e0)
    p.box(1290, yf - 4, 324, 110, "**Einschränkung smart invoice:** Die Vertretung sieht nur persönlich zugestellte Aufgaben, keine Gruppenaufgaben. "
          "→ Aufgaben möglichst an Personen oder an Gruppen mit mindestens zwei Mitgliedern; keine Ein-Personen-Gruppen [K].", "warn", extra="fontSize=10;")
    yg = yf + 122
    p.box(40, yg, 1574, 60, "**Governance [K]:** Vertretungen möglichst innerhalb derselben Gesellschaftsgruppe (DMS_GF_<Verbund>, Rechte über RS_Mandant) · "
          "Freigabe-Vertretung nur durch Personen mit mindestens gleicher Freigabestufe · keine Vertretung Prüfer ↔ Freigeber desselben Vorgangs · "
          "Vertretungshandlungen im Workflowprotokoll mit handelndem Benutzer.", "info", extra="fontSize=11;verticalAlign=middle;")
    legend_row(p, 40, 1092, edges=[("flow", "Sequenz")])
    return p


# ======================================================================
# p13  Sonderfälle Eingangsrechnung
# ======================================================================
TAGSTYLE = {"S": "task", "K": "task_d", "A": "task_mdis", "E": "task_ext", "O": "task_open"}


def tile(p, x, y, w, h, title, steps, foot, link=None):
    p.box(x, y, w, h, "", "rounded=1;arcSize=3;fillColor=#FFFFFF;strokeColor=%s;" % C["grey_m"])
    p.box(x, y, w, 34, title, "dvelop", extra="fontSize=12;align=left;spacingLeft=8;", link=link)
    n = len(steps)
    sh = 62 if n >= 4 else 70
    gap = 14
    prev = None
    yy = y + 46
    for txt, tag in steps:
        st_ = TAGSTYLE[tag[0]]
        lab = f"{txt}  **[{tag}]**" if tag[0] != "E" else txt
        cid = p.box(x + 12, yy, w - 24, sh, lab, st_, extra="fontSize=10;")
        if prev:
            F(p, prev, cid, extra="endSize=5;")
        prev = cid
        yy += sh + gap
    p.box(x + 8, yy - 4, w - 16, y + h - yy, foot, "text", extra="fontSize=10;")


def page13(doc):
    p = doc.page("13 Sonderfälle Eingangsrechnung", "p13")
    p.header("13 · Sonderfälle Eingangsrechnung",
             "Mini-Abläufe je Sonderfall mit Belegstatus [S] Standard · [K] Konfiguration · [A] Anpassung BeSync · [O] offen (Kapitel 9.11)")
    tiles = [
        ("Kürzung (AE-14)", [("Prüfer stellt Mengen-/Preisabweichung oder Mangel fest", "S"),
                             ("Zahlbetrag pay_amount < Brutto (Kopf/Position, Neuberechnung)", "K"),
                             ("Pflicht: Kürzungsgrund E-13 + Notiz/Annotation", "K"),
                             ("optional Kürzungsmitteilung an Lieferant (S-11)", "A")],
         "**Original bleibt unverändert** (P5, § 146 Abs. 4 AO; XML ist Original). Keine „lokale Bearbeitung“. Formal/steuerlich falsche Rechnung → Rückweisung. DATEV-Verarbeitung des Zahlbetrags mit Trios klären (OP-05)."),
        ("Rückweisung (AE-13, WF-05)", [("Aktion „An Lieferant zurückweisen“ in Verteilung/Prüfung", "K"),
                                         ("Pflicht-Rückweisungsgrund E-26 (Werteliste)", "K"),
                                         ("Export → BeSync: Vorlage je Grund an vendor.email (Graph oder d.velop-Messaging-API, OP-25)", "A"),
                                         ("gesendete Mail als K-07 in Kreditorenakte", "A")],
         "**5 Gründe (Vorschlag):** 1 Pflichtangaben § 14 · 2 falscher Empfänger · 3 Leistung/Nachweise fehlen · 4 Preis/Menge weicht ab · 5 E-Rechnungsfehler. Phase 1: „Teilen per E-Mail/Link“ manuell [S]; automatische Mail ab Phase 2."),
        ("Dublette", [("Stufe 1 document reader: Rechnungsnummer", "S"),
                      ("Stufe 2 smart invoice: Kreditor + Nummer, 18 Monate", "S"),
                      ("R-02 vergleicht mit Original (Klärfall C, Seite 09)", "S"),
                      ("echt: ablehnen ohne Mail · sonst Annahme mit Begründung", "K")],
         "Häufig bei Doppeleingang Mail + Post oder PDF + E-Rechnung. Abgelehnte Dublette bleibt archiviert und mit dem Original verknüpft. Lieferanten: nur noch elektronisch an rechnung@."),
        ("Abschlag / Schluss kumuliert", [("Belegart Abschlag/Schluss (E-14; XRechnung 875/877)", "K"),
                                          ("Auftrags-Nr. E-19, Vergabeeinheit E-18 → Vorgangsakte K-13", "K"),
                                          ("kumulierte VOB-Prüfung in BIM4You (WF-02)", "A"),
                                          ("Ergebnis E-22 + Prüfbericht K-08 am Beleg", "A")],
         "Beispiel: 60.000 € kumuliert − 25.000 € 1. Abschlag − 3.500 € Einbehalt = 31.500 €. Schlussrechnung: vereinnahmte Teilentgelte absetzen (§ 14 Abs. 5 UStG). Katalog 5.2: N (d.velop) / A (BIM4You)."),
        ("Sicherheitseinbehalt", [("BIM4You berechnet Einbehalt je Abschlag", "E"),
                                  ("E-22 Sicherheitseinbehalt am Beleg (S-09)", "A"),
                                  ("Zahlbetrag reduziert, Kürzungsgrund „Einbehalt“", "K"),
                                  ("Verwaltung über Laufzeit/Rückgabe in BIM4You bzw. DATEV-OP", "E")],
         "VOB/B § 17: je Zahlung höchstens 10 % bis zur vereinbarten Sicherheitssumme. Rückgabe nach Abnahme bzw. Gewährleistung außerhalb von d.velop."),
        ("Reverse Charge § 13b UStG", [("Bau-Kreditor mit Steuerkategorie (z. B. BAU13B) je Mandant", "K"),
                                       ("automatische Steuerschlüsselermittlung Kreditor × Sachkonto", "S"),
                                       ("Plausibilität: § 13b-Fall mit USt ≠ 0 → Hinweis/Klärfall", "K"),
                                       ("E-20 = Ja; Buchung durch Trios", "E")],
         "Nur Gesellschaften, die selbst nachhaltig Bauleistungen erbringen, sind Steuerschuldner (Kennzeichen im Gesellschaftsstamm, AE-28). Gesellschaften und DATEV-BU-Schlüssel mit Trios/Steuerberatung klären."),
        ("§ 48b EStG – FSB (AE-15)", [("FSB als K-06 in Kreditorenakte, „Gültig bis“ (E-21)", "K"),
                                      ("BeSync-FSB-Status prüft Bau-Rechnung an der Startverbindung", "A"),
                                      ("fehlt/abgelaufen: Klärfall, Vorschlag Zahlbetrag 85 % „Bauabzug 15 %“", "A"),
                                      ("EIBE-Einzelabfrage beim BZSt manuell (keine API)", "S")],
         "Bagatellgrenzen 5.000 € bzw. 15.000 € je Leistendem und Jahr. Anmeldung und Abführung in DATEV durch Trios. Bis Phase 3: E-21 „FSB-Status“ Pflichtfeld in der Verteilung [K]. Katalog 2.7 = A."),
        ("Gutschrift / Storno", [("Belegart Gutschrift bzw. Stornorechnung (E-14)", "K"),
                                 ("Verweis auf Ursprungsrechnung (Notiz/Custom-Feld)", "K"),
                                 ("Pfad in WF-01: Verteilung → Prüfung → Buchhaltung", "K"),
                                 ("Ursprung noch offen: mit Verweis ablehnen", "K")],
         "Keine Zahlungsfreigabe im Gutschriftpfad. Empfehlung: Pfad in WF-01 über Bedingung auf Belegart; alternativ eigene Workflowdefinition. Die ID WF-04 bleibt dem Klärfall vorbehalten."),
        ("E-Rechnung formal fehlerhaft", [("XRechnung-Validierung KoSIT, Prüfbericht als Anlage", "S"),
                                          ("ZUGFeRD MINIMUM/BASIC-WL erkennen", "A"),
                                          ("Rückweisung Grund 5: Neuausstellung als E-Rechnung anfordern", "K"),
                                          ("keine Korrektur durch Livos, XML bleibt Original", "S")],
         "Inhaltliche Fehler → Rückweisung; Leistungskürzung → Zahlbetrag (E-Rechnung bleibt formal gültig). Übergang: bis 31.12.2026 Papier/PDF zulässig, 2027 eingeschränkt, ab 2028 Pflicht."),
        ("IBAN-Abweichung", [("Beleg-IBAN ↔ Stamm-IBAN (S-02) am Beleg", "S"),
                             ("Warnanzeige in der Maske testen (OP-10)", "O"),
                             ("Fallback: BeSync-Prüfung an der Startverbindung → Klärfall", "A"),
                             ("Rückruf über Stamm-Telefonnummer; Änderung nur durch Trios in DATEV", "E")],
         "Typisches Betrugsmuster. Gezahlt wird immer auf die DATEV-Stammbankverbindung; Stammänderung nach Vier-Augen-Prüfung durch Trios."),
    ]
    w = (1574 - 4 * 12) / 5
    h = 470
    for i, (t, steps, foot) in enumerate(tiles):
        r, c = divmod(i, 5)
        tile(p, 40 + c * (w + 12), 112 + r * (h + 12), w, h, t, steps, foot)
    legend_row(p, 40, 1080, items=PROC_LEG, edges=[("flow", "Ablauf")])
    return p


# ======================================================================
# p14  Statusmodell Rechnung
# ======================================================================
def page14(doc):
    p = doc.page("14 Statusmodell Rechnung", "p14")
    p.header("14 · Statusmodell der Rechnung",
             "Fachlicher Status abgeleitet aus aktuellem Schritt (E-24), Workflowzustand und Sonderzuständen – kein eigenes Statusfeld; „Bezahlt“ über BeSync (E-23, S-06)")
    SW, SH = 176, 58
    xs = [120 + i * 300 for i in range(5)]
    R1, R2, R3 = 250, 420, 580
    X = "arcSize=30;fontSize=11;fontStyle=1;align=center;verticalAlign=middle;"
    def S_(x, y, t, st="dvelop_l", w=SW):
        return p.box(x, y, w, SH, t, st, extra=X)
    s0 = EV(p, 70, R1 + SH / 2, "", "start", r=26)
    eing = S_(xs[0], R1, "Eingegangen /\nin Erkennung", "dvelop_l")
    vert = S_(xs[1], R1, "In Verteilung")
    pruef = S_(xs[2], R1, "In sachlicher\nPrüfung")
    frei = S_(xs[3], R1, "In Freigabe\nStufe n")
    zf = S_(xs[4], R1, "In Zahlungs-\nfreigabe")
    kl = S_(xs[1], R2, "Klärfall /\nClearing")
    bim = S_(xs[2] + 150, R2, "Transfer / Warten\nauf BIM4You", "mdis", w=190)
    esk = p.box(xs[3] + 150, R2, 210, SH, "Eskaliert Stufe 1/2\n(Zusatzstatus)", "ui_hint", extra=X)
    zur = S_(xs[2] - 110, 124, "Zurückgewiesen", "warn", w=190)
    bh = S_(xs[4], R3, "In Buchhaltung\n(Trios)")
    ueb = S_(xs[3], R3, "Übergeben an DATEV")
    bez = S_(xs[2], R3, "Bezahlt / teilbezahlt\n(BeSync, ab Phase 3)", "mdis")
    e1 = EV(p, xs[2] - 60, R3 + SH / 2, "Ende", "end", r=26, pos="below", lw=40, lh=16)

    F(p, s0, eing)
    F(p, eing, vert, "Erkennung fertig /\nWorkflowstart")
    F(p, vert, pruef, "verteilt")
    F(p, pruef, frei, "geprüft")
    F(p, frei, zf, "letzte Stufe\nfreigegeben")
    F(p, frei, frei, "Wertgrenze → nächste Stufe", ex=(1, 0.2), en=(0.8, 0), pts=[(xs[3] + SW + 30, R1 + 12), (xs[3] + SW + 30, R1 - 26), (xs[3] + SW * 0.8, R1 - 26)])
    F(p, frei, pruef, "Ablehnen / Rückfrage", "red", ex=(0.2, 0), en=(0.8, 0), pts=[(xs[3] + SW * 0.2, R1 - 40), (xs[2] + SW * 0.8, R1 - 40)])
    F(p, zf, pruef, "Ablehnen", "red", ex=(0.5, 0), en=(0.5, 0), pts=[(xs[4] + SW / 2, R1 - 64), (xs[2] + SW / 2, R1 - 64)])
    F(p, vert, zur, "Dublette /\nRückweisung", "red", ex=(0.5, 0), en=(0, 0.5), pts=[(xs[1] + SW / 2, 153)])
    F(p, pruef, zur, "Zurückweisen\n(S-11)", "red", ex=(0.25, 0), en=(0.75, 1), pts=[(xs[2] + SW * 0.25, 200), (xs[2] - 110 + 190 * 0.75, 200)])
    F(p, vert, kl, "Mandant/Kreditor\nfehlt, Dublette", ex=(0.3, 1), en=(0.3, 0))
    F(p, kl, vert, "geklärt", ex=(0.7, 0), en=(0.7, 1))
    F(p, pruef, bim, "Bau: Transfer S-08", ex=(0.6, 1), en=(0, 0.5), pts=[(xs[2] + SW * 0.6, R2 + SH / 2)])
    F(p, bim, frei, "successful", ex=(1, 0.3), en=(0.2, 1), pts=[(xs[3] + SW * 0.2, R2 + SH * 0.3)])
    F(p, bim, pruef, "false /\nTimeout", "red", ex=(0.2, 1), en=(0.2, 1), pts=[(xs[2] + 150 + 38, R2 + SH + 22), (xs[2] + SW * 0.2, R2 + SH + 22)])
    for src in (frei, zf):
        F(p, src, esk, "", "assoc", ex=(0.5, 1) if src == zf else (0.8, 1), en=(0.5, 0) if src == frei else (1, 0.2))
    F(p, zf, bh, "zahlungs-\nfreigegeben", ex=(0.6, 1), en=(0.6, 0))
    F(p, bh, ueb, "S-01 Export\n(end_mode finished)")
    F(p, ueb, bez, "S-06: OP in DATEV\nausgeglichen")
    F(p, bez, e1)
    p.box(xs[4] + SW + 20, R2 - 10, 1614 - (xs[4] + SW + 20), 110,
          "**Eskaliert** ist kein eigener Schritt: Die Aufgabe bleibt beim Bearbeiter; REB-Statusspalte zeigt Stufe 1/2 (Seite 12).", "note", extra="fontSize=10;")
    p.box(xs[0], R3 - 8, 300, 76, "**Übergabefehler** (Export an LDconnect gescheitert) → Fehlerschritt/Clearing, sichtbar im REB [S]. "
          "**Workflowstart fehlgeschlagen** → Administration [S].", "note", extra="fontSize=10;")

    rows = [["Status (fachlich, Kap. 10.7)", "Bedeutung / Auslöser", "Technische Grundlage", "Sichtbar im REB", "Grad"],
            ["Eingegangen / in Erkennung", "Beleg importiert (E-Mail, Scan, E-Rechnung, Upload), Erkennung läuft", "inbound / document reader, Stapel", "nein (Stapelübersicht M-01)", "S"],
            ["Workflowstart fehlgeschlagen", "Übergabe an smart invoice gescheitert", "Phase „Workflowstart ist fehlgeschlagen“", "ja (Administration)", "S"],
            ["In Verteilung", "Vorqualifikation durch Rechnungseingang R-02", "Schritt Verteilung (Aktueller Schritt, E-24)", "ja, Aktueller Schritt", "K"],
            ["Klärfall / Clearing", "Mandant unbekannt, Kreditor fehlt, Dublette / Korrektur nach Fehlzuordnung", "Schritt Klärfall, Standardmandant „Klärfall“ / Clearing-Modus", "ja („Clearing Modus“)", "K / S"],
            ["In sachlicher Prüfung", "Prüfung und Kontierung durch Fachbereich R-03", "Schritt Sachliche Prüfung", "ja", "K"],
            ["Transfer / Warten auf BIM4You", "Bau-Prüfung in BIM4You läuft (WF-02)", "Phase „aktiver Belegdatentransfer“, Fenster ≤ 28 Tage", "ja, als Transferzustand", "S / A"],
            ["In Freigabe Stufe n", "fachliche Freigabe gemäß Freigabematrix", "Schritt Fachliche Freigabe Stufe n", "ja", "K"],
            ["Eskaliert Stufe 1/2", "Frist überschritten (Zusatzstatus)", "Eskalation je Schritt / vor Fälligkeit", "ja, Status + Schnellzugriff", "S"],
            ["In Zahlungsfreigabe", "finanzielle Freigabe R-05 vor DATEV-Übergabe (AE-06)", "Schritt Zahlungsfreigabe", "ja", "K"],
            ["In Buchhaltung", "Kontrolle und Übergabe durch Trios R-06", "Schritt Buchhaltung", "ja", "K"],
            ["Übergabefehler", "Export an LDconnect fehlgeschlagen", "Fehlerschritt", "ja", "S"],
            ["Übergeben an DATEV", "Buchungsvorschlag + Beleglink in DATEV, Workflow beendet", "Ende „Übergeben“ (end_mode = finished)", "ja, Archiv (6/12 Monate)", "K"],
            ["Zurückgewiesen", "Rückweisung an Lieferant (S-11) oder Dublette (ohne Mail)", "Ende „Zurückgewiesen“ (aborted bzw. Endschritt), E-26", "ja, Archiv", "K"],
            ["Freigegeben / Abgelehnt (PM)", "Ergebnis WF-03 (Seite 15)", "Ende WF-03", "ja, Archiv", "K"],
            ["Bezahlt / teilbezahlt", "Zahlung in DATEV-OPOS ausgeglichen, Zahldatum", "DMS-Eigenschaft E-23 über BeSync (S-06, Phase 3)", "nein; Suche, Akte, evidanza", "A"]]
    p.table(40, 664, [230, 470, 490, 250, 134], rows, rowh=24)
    legend_row(p, 40, 1066, items=[("dvelop_l", "Status aus smart invoice (Konfiguration)"), ("mdis", "Status über BeSync"),
                                   ("ui_hint", "Zusatzstatus"), ("warn", "Endstatus Rückweisung")],
               edges=[("flow", "Übergang"), ("red", "Ablehnen / Zurückweisen"), ("assoc", "kann eintreten")])
    return p


# ======================================================================
# p15  Property-Manager-Freigabe (WF-03)
# ======================================================================
def page15(doc):
    p = doc.page("15 Property-Manager-Freigabe (WF-03)", "p15")
    p.header("15 · Property-Manager-Freigabe (WF-03)",
             "Freigabeanfragen der Property Manager über dem Schwellwert – Freigabe in smart invoice ohne Buchung und ohne Zahlung, Rückmeldung per E-Mail (AE-12, Katalog 4.1 = K/A)")
    X0, W, HW = 40, 1574, 140
    L = lanes_h(p, X0, 116, W, [("Property Manager\nR-09 (extern,\nohne Lizenz)", 160), ("d.velop\n(smart invoice)", 200),
                                 ("Asset Management\nR-04", 160), ("BeSync (MDIS)", 180)], head_w=HW)
    PM, DV, AM, BS = [l[1] for l in L]
    cx = lambda i: X0 + HW + 60 + i * 118
    tw, th = 108, 76
    st = EV(p, cx(0), PM, "Rechnung über\nSchwellwert", "start", r=30, lw=100, lh=28)
    t_mail = T(p, cx(1), PM, tw, th, "E-Mail an\nfreigabe-hv@…\n(Rechnung + Text)", "task_ext", fs=10)
    t_imp = T(p, cx(1), DV, tw, th + 6, "Import: eigenes Importprofil, E-25 = PM-Freigabe [S/K]", "task_d", fs=10)
    t_erk = T(p, cx(2), DV, tw, th + 6, "Erkennung: Mandant, Beträge, Rechnungsnr. [S]", "task", fs=10)
    t_ver = T(p, cx(3), DV, tw, th + 6, "Verteilung R-02: Objekt, Gesellschaft, PM (E-30); Plausi Schwellwert [K]", "task_d", fs=10)
    t_fr = T(p, cx(4), AM, tw, th + 6, "Freigabe M-13 (Matrix Mandant/Objekt, Grenze) [K]", "task_d", fs=10)
    g = GW(p, cx(5), AM, "Freigabe\nerteilt?", s=62)
    e_ok = EV(p, cx(6), DV - 45, "Ende „Freigegeben“", "end", r=28, pos="above", lw=120, lh=16)
    e_no = EV(p, cx(6), DV + 45, "Ende „Abgelehnt“ (Begründung Pflicht)", "end", r=28, pos="above", lw=190, lh=16)
    t_bs = T(p, cx(7), BS, tw + 10, th + 20, "S-11 Webhook an Endverbindung → Rückmeldemail (Vorlage) via Graph oder Messaging-API (OP-25); Mail als K-07 in Objektakte [A]", "task_mdis", fs=10)
    t_pm2 = T(p, cx(8), PM, tw, th, "PM erhält Ergebnis; bucht und zahlt im eigenen System", "task_ext", fs=10)
    e_pm = EV(p, cx(9) - 20, PM, "erledigt", "end", r=26, pos="below", lw=60, lh=16)

    F(p, st, t_mail)
    F(p, t_mail, t_imp, "E-Mail", "msg", ex=(0.5, 1), en=(0.5, 0))
    F(p, t_imp, t_erk)
    F(p, t_erk, t_ver)
    F(p, t_ver, t_fr, ex=(1, 0.5), en=(0.5, 0))
    F(p, t_fr, g)
    F(p, t_fr, t_ver, "Rückfrage", "red", ex=(0.3, 0), en=(0.7, 1))
    F(p, g, e_ok, "ja", ex=(0.5, 0), en=(0, 0.5), pts=[(cx(5), DV - 45)])
    F(p, g, e_no, "nein", "red", ex=(1, 0.5), en=(0.5, 1), pts=[(cx(6), AM)])
    F(p, e_ok, t_bs, "Export", "data", ex=(1, 0.5), en=(0.7, 0), pts=[(cx(7) + 17, DV - 45)])
    F(p, e_no, t_bs, "Export", "data", ex=(1, 0.5), en=(0.3, 0), pts=[(cx(7) - 17, DV + 45)])
    F(p, t_bs, t_pm2, "Rückmelde-Mail", "msg", ex=(1, 0.5), en=(0.5, 1), pts=[(cx(8), BS)])
    F(p, t_pm2, e_pm)
    p.box(cx(8) + 14, DV - 76, 168, 152, "**Keine DATEV-Übergabe (kein S-01), keine Zahlungsfreigabe, keine Zahlung über Livos** – WF-03 hat keinen Schritt Buchhaltung; Doppelbuchung ausgeschlossen (P4).",
          "warn", extra="fontSize=10;verticalAlign=middle;")
    # optional S-16
    gx = 1378
    p.box(gx, 124, 1604 - gx, 676, "Optional · Phase 3 · S-16", "group")
    o1 = T(p, (gx + 1604) / 2, PM + 10, 200, 56, "Monatspaket DATEV-Buchungsdaten der PM (bestehend, über Trios)", "task_ext", fs=10)
    o2 = T(p, (gx + 1604) / 2, BS - 26, 200, 56, "S-16 Upload/Postfach, Parser (Buchungsstapel, Kreditoren) [A]", "task_mdis", fs=10)
    o3 = T(p, (gx + 1604) / 2, BS + 40, 200, 44, "evidanza (BI): Auswertung", "task_ext", fs=10)
    F(p, o1, o2, "Datei", "data", ex=(0.12, 1), en=(0.12, 0))
    F(p, o2, o3)
    p.box(gx + 44, AM - 70, 1604 - gx - 50, 140, "**Vollständigkeit:** gebuchte Rechnungen über Schwellwert ohne WF-03-Freigabe. **Kreditorenmapping:** HV-Kreditoren (80000er) → Konsolidierungsnummer (Lieferanten-App).",
          "text", extra="fontSize=10;")

    y = L[-1][0] + L[-1][2] + 12
    legend_row(p, 40, y)
    y += 32
    w3 = (1574 - 2 * 16) / 3
    card(p, 40, y, w3, 180, "Warum ein eigener Prozess",
         "Ca. 10 Property Manager prüfen, buchen und zahlen rund 95 % ihrer Rechnungen selbst. Nur Rechnungen über dem Schwellwert brauchen die Freigabe "
         "durch das Livos Asset Management. PM dürfen nicht zur Nutzung eines Livos-Systems verpflichtet werden – deshalb bleibt die E-Mail der Kanal. "
         "Ergebnis: zentraler Nachweis, Vertretung, Transparenz („wo hängt die Rechnung“).", "info", fs=11)
    card(p, 40 + w3 + 16, y, w3, 180, "Regeln (Kapitel 11.2.3)",
         "Eine Rechnung je E-Mail, Objekt und Gesellschaft im Betreff · Absenderadresse = Rückmeldeadresse · Kreditor keine Pflicht · Ablehnung nur mit Begründung · "
         "Eskalation Freigabe 3 AT an Leitung AM (Vorschlag) · REB-Schnellzugriff „PM-Freigaben offen“ · Rechnungen zählen ins invoices-Volumen · Schwellwert legt Livos fest (OP-17).", "note", fs=11)
    card(p, 40 + 2 * (w3 + 16), y, w3, 180, "Rückmeldemail (Beispiel)",
         "Betreff: Freigabe RE-2026-1041 · Livos Objektgesellschaft Nord mbH · 14.756,00 €\n"
         "Ergebnis: Freigegeben / Abgelehnt · Begründung · Objekt · Freigeber · Datum · optional Teilen-Link auf den Beleg.\n"
         "Übergang bis BeSync produktiv: manuelle Antwort bzw. „Teilen per E-Mail“ [S].", "info", fs=11)
    return p


# ======================================================================
# p16  Vertragsprozess (WF-06)
# ======================================================================
def page16(doc):
    p = doc.page("16 Vertragsprozess (WF-06)", "p16")
    p.header("16 · Vertragsprozess (WF-06)",
             "Livos-Kette Eingang → Verarbeitung → Verteilung → Klassifizierung → Fachliche Freigabe → Archivierung mit d.velop contracts, process studio, sign und pilot (AE-20, Phase 4)")
    phases = [
        ("Eingang", [("Papier: Scan Poststelle (WF-07, Seite 17)", "S"), ("E-Mail: Funktionspostfach vertraege@… (Vorschlag)", "S"),
                     ("Outlook-Ablage, Upload in die Vertragsakte", "S")]),
        ("Verarbeitung", [("OCR + KI-Klassifizierung, Klasse „Vertrag“ (C1, ab business)", "S"),
                          ("d.velop pilot „Intelligenter Import“: Eckdaten, Zusammenfassung", "S"), ("Mandant E-01 Pflicht (P1)", "K")]),
        ("Verteilung", [("mail dispatcher: Aufgabe an Gruppe Vertragsmanagement der Gesellschaft/des Verbunds", "K"),
                        ("Vertretung über die Gruppe (R-11)", "S")]),
        ("Klassifizierung", [("d.velop contracts: geführte Vertragsanlage mit Laufzeitberechnung", "S"),
                             ("Vertragsart, Partner, Beginn/Ende, Kündigungsfrist, Verlängerung, Wert (E-28), Objekt", "K"),
                             ("Hierarchie Rahmen-/Einzelvertrag, Nachträge", "S")]),
        ("Fachliche Freigabe", [("process studio „Vertragsfreigabe“: Fachbereich → Freigabe nach Wertgrenze", "K"),
                                ("Standard-Freigabe in contracts? (OP-12)", "O"), ("d.velop sign: Signaturumlauf, auch extern", "S")]),
        ("Archivierung", [("Vertragsakte K-14 in Objekt-/Gesellschaftsakte (AE-19)", "S"),
                          ("Aufbewahrung ab Vertragsende (AE-24), Löschsperre", "K"), ("Rechte je Mandant (RS_Mandant)", "K")]),
    ]
    pw = 1574 / 6
    for i, (t, items) in enumerate(phases):
        x = 40 + i * pw
        p.box(x, 112, pw - 4, 44, f"{i + 1} {t}", "dvelop", extra="shape=step;perimeter=stepPerimeter;fixedSize=1;size=16;fontSize=13;")
        yy = 166
        for txt, tag in items:
            p.box(x + 6, yy, pw - 20, 64, f"{txt}  **[{tag}]**", TAGSTYLE[tag], extra="fontSize=10;")
            yy += 72
    # Lanes Freigabe + Fristen
    X0, W, HW = 40, 1574, 150
    LY = 420
    p.box(40, LY - 30, 700, 24, "Fachliche Freigabe (process studio + sign)", "h2", extra="fontSize=13;")
    L = lanes_h(p, X0, LY, W, [("Vertragsmanager\nR-11", 150), ("Freigeber\nR-04 / GF", 130), ("d.velop contracts /\nprocess studio / sign", 160)], head_w=HW)
    VM, FG, DC = [l[1] for l in L]
    cx = lambda i: X0 + HW + 55 + i * 116
    tw, th = 102, 64
    s0 = EV(p, cx(0), VM, "Vertrag/Entwurf\neingegangen", "start", r=30, lw=100, lh=28)
    a1 = T(p, cx(1), VM, tw, th, "Vertrag anlegen und prüfen (M-14) [S/K]", "task_d", fs=10)
    a2 = T(p, cx(2), DC, tw, th, "Prozess „Vertrags-freigabe“ starten, Status „In Genehmigung“ [K]", "task_d", fs=9)
    a3 = T(p, cx(3), FG, tw, th, "Freigabe nach Wertgrenze (Mandant) [K]", "task_d", fs=10)
    g1 = GW(p, cx(4), FG, "Frei-\ngegeben?", s=60)
    a4 = T(p, cx(5), DC, tw, th, "d.velop sign: Signatur (intern/extern) [S]", "task", fs=10)
    a5 = T(p, cx(6), DC, tw, th, "Vertragsakte K-14, Status „Aktiv“ [S]", "task", fs=10)
    F(p, s0, a1)
    F(p, a1, a2, ex=(0.5, 1), en=(0, 0.5))
    F(p, a2, a3, ex=(1, 0.5), en=(0.5, 1))
    F(p, a3, g1)
    F(p, g1, a4, "ja", ex=(1, 0.5), en=(0.5, 0))
    F(p, g1, a1, "nein: überarbeiten", "red", ex=(0.5, 0), en=(1, 0.4), pts=[(cx(4), VM - 6)])
    F(p, a4, a5)
    # Fristen
    sep = cx(6) + 70
    p.line(sep, LY, sep, LY + 440, "assoc")
    p.box(sep + 10, LY - 30, 600, 24, "Fristenüberwachung (d.velop contracts)", "h2", extra="fontSize=13;")
    b1 = T(p, cx(7) + 20, DC, tw + 10, th + 6, "Fristenkalender: Kündigungs-stichtag aus Laufzeit + Frist berechnet [S]", "task", fs=9)
    ti = EV(p, cx(8) + 20, DC, "Vorlauf erreicht\n(z. B. 90 Tage)", "inter", r=30, pos="below", lw=100, lh=28)
    b2 = T(p, cx(9) + 10, VM, tw + 10, th + 6, "Meldung an Verantwortliche; Klauseln mit d.velop pilot prüfen [S]", "task", fs=9)
    g2 = GW(p, cx(10), VM, "Kündigen /\nverlängern?", s=62)
    b3 = T(p, cx(10), FG, tw, th, "Freigabe Kündigung bzw. Nachtrag [K]", "task_d", fs=10)
    b4 = T(p, cx(11), DC, tw, th + 6, "Dokument in Vertragsakte, neue Laufzeit/Frist [S]", "task", fs=9)
    F(p, a5, b1, ex=(1, 0.5), en=(0, 0.5))
    F(p, b1, ti)
    F(p, ti, b2, ex=(1, 0.5), en=(0.5, 1))
    F(p, b2, g2)
    F(p, g2, b3, "ja", ex=(0.5, 1), en=(0.5, 0))
    F(p, b3, b4, ex=(1, 0.5), en=(0.5, 0))
    F(p, g2, b4, "Verlängerung", ex=(1, 0.5), en=(1, 0.3), pts=[(1596, VM), (1596, DC - 12)])
    F(p, b4, b1, "nächste Frist", "flow", ex=(0.5, 1), en=(0.5, 1), pts=[(cx(11), DC + 66), (cx(7) + 20, DC + 66)], extra="dashed=1;")

    y = LY + 440 + 10
    legend_row(p, 40, y)
    y += 32
    w3 = (1574 - 2 * 16) / 3
    card(p, 40, y, w3, 140, "d.velop pilot (AE-20, AE-27)",
         "Fragen an Vertragsinhalte, z. B. „Welche Kündigungsfrist gilt?“, „Gibt es eine Indexklausel?“; Zusammenfassung und Risikohinweise. "
         "Tokengrenze bei langen Verträgen im PoC testen, LLM-Region/AVV klären (OP-19).", "info", fs=11)
    card(p, 40 + w3 + 16, y, w3, 140, "Offene Punkte und Alternative",
         "Standard-Freigabeworkflow in d.velop contracts nicht belegt → process studio (OP-12); Kontingent 1.000 Ausführungen/Monat in business (OP-11). "
         "Mehrstufige Fristen-Eskalation nicht belegt → process-studio-Timer. Alternative: alphaflow Contracts (Genehmigungen, Eskalationen, Zahlungsreihen).", "note", fs=11)
    card(p, 40 + 2 * (w3 + 16), y, w3, 140, "Bezug zu Rechnungen",
         "Vertrags-/Auftragsnummer E-19 an der Eingangsrechnung (Pflicht bei Bau) · Vorgangsakte K-13 mit Auftrag, Abschlägen, Schlussrechnung · "
         "Rahmenvertrag zusätzlich in der Kreditorenakte K-12 · Schriftformverträge und Notarverträge bleiben außerhalb der elektronischen Signatur.", "info", fs=11)
    return p


# ======================================================================
# p17  Postverteilung (WF-07)
# ======================================================================
def page17(doc):
    p = doc.page("17 Postverteilung (WF-07)", "p17")
    p.header("17 · Postverteilung (WF-07)",
             "Eingang → Verarbeitung → Klassifizierung → Verteilung → Archivierung · KI-Trennung/-Klassifizierung (C1), d.velop mail dispatcher, Umleitung Rechnung/Vertrag (AE-21, Phase 4)")
    X0, W, HW = 40, 1574, 150
    L = lanes_h(p, X0, 116, W, [("Eingang", 92), ("Poststelle R-01 /\nScandienstleister", 150), ("d.velop inbound\n+ KI", 120),
                                 ("Zielprozesse", 104), ("d.velop\nmail dispatcher", 110), ("Fachbereich\n(Empfängergruppe)", 110)], head_w=HW)
    EIN, PS, DV, ZP, MD, FB = [l[1] for l in L]
    cx = lambda i: X0 + HW + 55 + i * 116
    tw, th = 102, 60
    s_pap = EV(p, cx(0), EIN, "Papierpost", "start", r=30, pos="right", lw=70, lh=20)
    s_mail = EV(p, cx(2), EIN + 8, "E-Mail an post@… / Funktionspostfach", "start", r=30, pos="above", lw=220, lh=16)
    t_vor = T(p, cx(0), PS, tw, th + 10, "Post öffnen, Rechnungen/ Verträge vorsortieren, Trennblätter [S]", "task", fs=9)
    g_scan = GW(p, cx(1), PS, "Scan\nintern?", s=56)
    t_si = T(p, cx(2), PS - 38, tw, 54, "inbound scan, Barcode Code 128 [S]", "task", fs=9)
    t_sd = T(p, cx(2), PS + 38, tw, 60, "Dienstleister: PDF + Metadaten (Postfach/API) [K/O]", "task_open", fs=9)
    t_imp = T(p, cx(3), DV, tw, th, "Import-Stapel, OCR, PDF/A (≤ 200 Seiten) [S]", "task", fs=9)
    t_ki = T(p, cx(4), DV, tw, th, "KI-Trennung + KI-Klassifizierung (Top 3) [S, C1]", "task", fs=9)
    g80 = GW(p, cx(5), DV, "≥ 80 %\nsicher?", s=58)
    t_un = T(p, cx(5), PS, tw, th + 6, "„Unbestimmt“: manuell klassifizieren, Mandant setzen (M-15) [S]", "task_d", fs=9)
    g_re = GW(p, cx(6), DV, "Rechnung?", s=58)
    g_vt = GW(p, cx(7), DV, "Vertrag?", s=58)
    t_er = T(p, cx(6), ZP, tw, th + 4, "ER-Strecke WF-01: in ER-Stapel verschieben / neu importieren [K/O]", "task_d", fs=9, link="data:page/id,p08")
    t_ct = T(p, cx(7), ZP, tw, th + 4, "Gruppe Vertrags-management → d.velop contracts (WF-06) [K]", "task_d", fs=9, link="data:page/id,p16")
    t_md = T(p, cx(8), MD, tw, th + 4, "Aufgabe an Empfänger-gruppe (Erstempfänger = Gruppe) [S/K]", "task_d", fs=9)
    i_er = EV(p, cx(10), MD, "Erinnerung 3 AT /\nEskalation (Priorität)", "inter", r=28, pos="below", lw=120, lh=28)
    t_fb = T(p, cx(9), FB, tw, th + 4, "übernehmen: „Es ist für mich“ oder weiterleiten [S]", "task", fs=9)
    t_ab = T(p, cx(10), FB, tw, th + 4, "Zielkategorie + Akte (AE-19), Aufbewahrung je Kategorie [S/K]", "task_d", fs=9)
    e_end = EV(p, cx(11), FB, "abgelegt", "end", r=28, pos="below", lw=70, lh=16)

    F(p, s_pap, t_vor, ex=(0.5, 1), en=(0.5, 0))
    F(p, t_vor, g_scan)
    F(p, g_scan, t_si, "ja", ex=(0.5, 0), en=(0, 0.5))
    F(p, g_scan, t_sd, "nein", ex=(0.5, 1), en=(0, 0.5))
    F(p, t_si, t_imp, ex=(1, 0.5), en=(0.3, 0))
    F(p, t_sd, t_imp, ex=(1, 0.5), en=(0.3, 0))
    F(p, s_mail, t_imp, "Importprofil", ex=(1, 0.5), en=(0.8, 0), pts=[(cx(3) + 20, EIN)])
    F(p, t_imp, t_ki)
    F(p, t_ki, g80)
    F(p, g80, t_un, "nein", ex=(0.5, 0), en=(0.5, 1))
    F(p, t_un, g_re, ex=(1, 0.5), en=(0.5, 0))
    F(p, g80, g_re, "ja")
    F(p, g_re, t_er, "ja", ex=(0.5, 1), en=(0.5, 0))
    F(p, g_re, g_vt, "nein")
    F(p, g_vt, t_ct, "ja", ex=(0.5, 1), en=(0.5, 0))
    F(p, g_vt, t_md, "nein: sonstige Post", ex=(1, 0.5), en=(0.5, 0))
    F(p, t_md, t_fb, ex=(1, 0.5), en=(0.5, 0))
    F(p, t_md, i_er, "", "assoc")
    F(p, t_fb, t_ab)
    F(p, t_fb, t_md, "an Kollegen / Posteingang", "red", ex=(0, 0.5), en=(0.5, 1), pts=[(cx(8), FB)])
    F(p, t_ab, e_end)
    # Hinweise in freien Bereichen
    T(p, (cx(8) + cx(11)) / 2 + 10, PS, cx(11) - cx(8) + 90, 110,
      "**Klassifizierungskatalog (Vorschlag, OP-17):** P-01 Rechnung → ER · P-03 Vertrag → contracts · Mahnung, FSB → R-02 · Angebot, Auftrag, Lieferschein → Fachbereich/Prüfer · "
      "Behörden, Steuer, Bank, Versicherung, Mieterpost → K-09 an Fachgruppen · Werbung nicht ablegen · „Unbestimmt“ → Clearing Poststelle.",
      "info", fs=10, extra="align=left;verticalAlign=middle;")
    T(p, (cx(9) + cx(11)) / 2 + 10, DV, cx(11) - cx(9) + 90, 90,
      "Rechnungspostfächer rechnung@… laufen nicht über die Post, sondern direkt in die ER-Strecke (AE-22). Rechnung an post@ → Weiterleitung an rechnung@.",
      "note", fs=10, extra="align=left;verticalAlign=middle;")

    y = L[-1][0] + L[-1][2] + 12
    legend_row(p, 40, y)
    y += 32
    w4 = (1574 - 3 * 14) / 4
    cards = [("KI nur in C1 (AE-01/AE-02)", "KI-Trennung und -Klassifizierung setzen Betriebsform C1 und Edition business voraus. Unter 80 % Sicherheit wird „Unbestimmt“ gesetzt; die drei wahrscheinlichsten Kategorien stehen zur Auswahl. In C2 nur Regel/Barcode.", "info"),
             ("mail dispatcher", "Erstempfänger immer eine Gruppe (sonst keine Aufgabe); erste Person übernimmt. Weiterleitung protokolliert. Erinnerung nach 3 AT (Vorschlag), Eskalation über Priorität. Cloud-Lizenz klären (OP-13). Alternative: VLOTT Postverteilung.", "info"),
             ("Scan intern oder Dienstleister (OP-13)", "Empfehlung: Start intern in der Poststelle (am Eingangstag, Qualitätskontrolle im Stapel). Dienstleister nur bei Engpass; Einlieferung per Postfach oder Inbound-API – SFTP nicht belegt.", "note"),
             ("Ablage (P1, AE-19)", "Mandant E-01 ist schon am Postdokument Pflicht (Trennblatt-Barcode, Alias oder manuell). Mit „Es ist für mich“ wählt der Empfänger Zielkategorie und Akte; Kreditor/Objekt nach Bedarf der Kategorie.", "info")]
    for i, (t, b, st_) in enumerate(cards):
        card(p, 40 + i * (w4 + 14), y, w4, 150, t, b, st_, fs=10)
    return p


# ======================================================================
def build(doc):
    page08(doc)
    page09(doc)
    page10(doc)
    page11(doc)
    page12(doc)
    page13(doc)
    page14(doc)
    page15(doc)
    page16(doc)
    page17(doc)
