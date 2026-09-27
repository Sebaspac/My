"""Seiten 18–22 des draw.io-Konzeptdiagramms (Rollen/Rechte, Rechtemodell Cloud,
DATEV/Zahlung, Reporting/KPI, Roadmap). Aufruf: build(doc)."""
from dio import C, S, lanes, ui_window, ui_table, ui_buttons, ann, legend_box, status_legend

# Zellstile für Rechtestufen (Farben aus der Palette C)
_CELL = "fillColor=%s;strokeColor=" + C['grey_m'] + ";fontSize=11;align=center;verticalAlign=middle;fontStyle=1;"
RS = {
    "S":    _CELL % C['teal_l'],
    "L":    _CELL % C['blue_l'],
    "L*":   _CELL % C['yellow_l'],
    "S/Lö": _CELL % C['red_l'],
    "–":    (_CELL % "#FFFFFF") + "fontColor=%s;fontStyle=0;" % C['grey'],
}


def _hline(p, x1, x2, y, style="straight", label="", above=True, lw=None, extra=""):
    """Horizontaler Pfeil (Sequenzdiagramm) mit Beschriftung oberhalb."""
    p.line(x1, y, x2, y, style, extra=extra)
    if label:
        lo, hi = min(x1, x2), max(x1, x2)
        w = lw or (hi - lo - 10)
        cx = (lo + hi) / 2
        p.box(cx - w / 2, y - 34 if above else y + 2, w, 32, label, "textc",
              extra="fontSize=10;verticalAlign=bottom;" if above else "fontSize=10;verticalAlign=top;")


# ----------------------------------------------------------------------------------------------
def _rcell(v):
    """Zellstil nach höchster Rechtestufe (K13 §13.4)."""
    if v == "–":
        return RS["–"] + "fontSize=10;"
    if "Lö" in v:
        return RS["S/Lö"] + "fontSize=9;"
    if "S" in v.replace("(S", ""):
        return RS["S"] + "fontSize=9;"
    if v.strip() == "L (W)":
        return RS["L*"] + "fontSize=9;"
    return RS["L"] + "fontSize=9;"


def page18(doc):
    p = doc.page("18 Rollen und Berechtigungsmatrix", "p18")
    p.header("18 Rollen und Berechtigungsmatrix",
             "Berechtigungsmatrix Rolle × Kategorie × Recht gemäß Kapitel 13.4: Rollen R-01 … R-15 × Kategorien K-01 … K-15 – "
             "Besetzung und Mengen legt Livos in Phase 0 fest (OP-17, OP-03)")
    p.box(1250, 70, 220, 26, "VORSCHLAG – zur Abstimmung", "badge_o")

    cats = ["K-01\nRech-\nnung", "K-02\nNach-\nweis", "K-03\nAuf-\ntrag", "K-04\nAnge-\nbot", "K-05\nVer-\ntrag",
            "K-06\nBeschei-\nnigung", "K-07\nKorres-\npondenz", "K-08\nBIM4You-\nBericht", "K-09\nPost\nsonstig",
            "K-10\nGes.-\nakte", "K-11\nObjekt-\nakte", "K-12\nKredit.-\nakte", "K-13\nVor-\ngangsakte",
            "K-14\nVertrags-\nakte", "K-15\nOrga-\nunterlage"]
    colw = [44, 196, 176] + [60] * 15 + [258]
    head = ["ID", "Rolle", "Rollengruppe (Entra ID)"] + cats + ["Lizenztyp (Vorschlag)"]
    M = {  # K13 §13.4, Spalten K-01 … K-15
        "R-01": "– | L/S (A) | L/S (A) | L/S (A) | – | L/S (A) | L/S (A) | – | L/S (A) | – | – | – | – | – | –",
        "R-02": "L/S (A) | L/S (A) | L (A) | L (A) | – | L/S (A) | L/S (A) | L (A) | – | L (A) | L (A) | L (A) | L (A) | – | L (A)",
        "R-03": "L (W) + L (M) | L/S (M) | L/S (M) | L/S (M) | L (M) | L (M) | L/S (M) | L (M) | L/S (M) | L (M) | L (M) | L (M) | L (M) | L (M) | –",
        "R-04": "L (W) + L (M) | L (M) | L (M) | L (M) | L (M) | L (M) | L (M) | L (M) | L (M) | L (M) | L (M) | L (M) | L (M) | L (M) | L (M)",
        "R-05": "L (W) + L (M) | L (M) | – | – | – | L (M) | – | L (M) | L/S (M) | L (M) | – | L (M) | – | – | –",
        "R-06": "L/S (A) | L (A) | L (A) | – | – | L (A) | L (A) | L (A) | – | L (A) | L (A) | L (A) | L (A) | – | L (A)",
        "R-07": "L (M) | L (M) | L (M) | L (M) | L (M) | L (M) | L (M) | L (M) | – | L (M) | L (M) | L (M) | L (M) | L (M) | L (M)",
        "R-08": "L (W) | L/S (O) | L (O) | – | – | – | – | L (O) | – | – | L (O) | – | L (O) | – | –",
        "R-09": " | ".join(["–"] * 15),
        "R-10": " | ".join(["–"] * 15),
        "R-11": "L (M) | L (M) | L/S (M) | L/S (M) | L/S (M) | L (M) | L/S (M) | L (M) | L/S (M) | L (M) | L (M) | L (M) | L (M) | L/S (M) | –",
        "R-12": " | ".join(["L/S/Lö (A)"] * 15),
        "R-13": "L/S (A) | L (A) | L (A) | L (A) | L (A) | L (A) | L/S (A) | L/S (A) | L (A) | L (A) | L (A) | L (A) | L (A) | L (A) | L/S (A)",
        "R-14": "L (T) | L (T) | L (T) | – | L (T) | L (T) | L (T) | L (T) | – | L (T) | L (T) | L (T) | L (T) | L (T) | L (T)",
        "R-15": " | ".join(["–"] * 15),
    }
    roles = [
        ("R-01", "Poststelle / Scan", "DMS_R_Post", "documents business"),
        ("R-02", "Rechnungseingang / Verteilung (Kreditorenbuchhaltung)", "DMS_R_Rechnungseingang + dv_*", "invoices Buchhaltungsuser"),
        ("R-03", "Sachliche Prüfer (AM, Objektbetreuer, PL) ¹", "DMS_R_Pruefer + DMS_G_/DMS_GB_<Nr>", "invoices Freigabeuser (+ documents business)"),
        ("R-04", "Freigeber (Abteilungsleitung, GF) ²", "DMS_R_Freigeber + DMS_G_ / DMS_GF_", "invoices Freigabeuser (GF ggf. documents business)"),
        ("R-05", "Zahlungsfreigeber (GF, kfm. Leitung, Treasury)", "DMS_R_Zahlung + DMS_G_<Nr>", "invoices Freigabeuser + multicash"),
        ("R-06", "Buchhaltung (Trios)", "DMS_R_Buchhaltung_Extern", "invoices Buchhaltungsuser (OP-03)"),
        ("R-07", "Controlling / Management ³", "DMS_R_Controlling + DMS_G_<Nr>", "documents business (lesend) / Freigabeuser"),
        ("R-08", "Externe Kernpartner (Projektsteuerer, Architekten)", "DMS_R_Partner_Extern + DMS_O_<ObjektID>", "invoices Freigabeuser (OP-03)"),
        ("R-09", "Property Manager (HV) – E-Mail-Kanal (WF-03)", "–", "keine Lizenz"),
        ("R-10", "Ad-hoc-Externe – nur Stellungnahme (WF-10, M-19)", "–", "keine Lizenz"),
        ("R-11", "Vertragsmanager / Vertragsverantwortliche", "DMS_R_Vertrag + DMS_G_/DMS_GB_<Nr>", "contracts voll (+ documents business)"),
        ("R-12", "Fachadministration / Key-User ⁴", "DMS_R_Fachadmin", "documents business + Admin (fachlich)"),
        ("R-13", "Technischer Benutzer BeSync ⁵", "TEC_BeSync", "technischer Benutzer"),
        ("R-14", "Betriebsprüfer (Z1) ⁶", "DMS_R_Betriebspruefung + DMS_G_Pruefung_<Anlass>", "documents (temporär, OP-45)"),
        ("R-15", "MDIS Betrieb / Support ⁷", "– (Tenant-Administration)", "Admin"),
    ]
    x0, y0, hh, rh = 40, 112, 58, 34
    cx = x0
    for i, t in enumerate(head):
        p.box(cx, y0, colw[i], hh, t, "th", extra=("align=center;fontSize=9;spacingLeft=0;" if 3 <= i <= 17 else "") + ("fillColor=%s;" % C['teal'] if i == 17 else ""))
        cx += colw[i]
    y = y0 + hh
    for ri, (rid, rol, grp, liz) in enumerate(roles):
        base = "td_alt" if ri % 2 else "td"
        cells = [c.strip() for c in M[rid].split("|")]
        vals = [rid, rol, grp] + cells + [liz]
        cx = x0
        for ci, v in enumerate(vals):
            if 3 <= ci <= 17:
                p.box(cx, y, colw[ci], rh, v.replace(" + ", "\n+ "), _rcell(v), extra="spacingLeft=0;")
            else:
                extra = "fontStyle=1;" if ci == 0 else "fontSize=10;"
                p.box(cx, y, colw[ci], rh, v, base, extra=extra)
            cx += colw[ci]
        y += rh
    y_end = y  # 112 + 58 + 15*34 = 680

    ly = y_end + 14
    legend_box(p, 40, ly, [
        (RS["S"], "L/S = Lesen + Schreiben (bearbeiten, anlegen)"),
        (RS["L"], "L = Lesen"),
        (RS["L*"], "L (W) = nur als Workflowbeteiligte/r"),
        (RS["S/Lö"], "L/S/Lö = zusätzlich Löschen (nur R-12)"),
        (RS["–"], "– = kein Zugriff im DMS"),
    ], "Legende Rechtestufen", w=330)
    p.box(384, ly, 400, 150,
          "**Geltungsbereich**\n"
          "**(M)** eigene Gesellschaften über RS_Mandant_Lesen / _Bearbeiten\n"
          "**(A)** alle Gesellschaften (eigene Permission Kxx_A_Zentral ohne Filter)\n"
          "**(O)** nur freigegebene Objekte über RS_Objekt\n"
          "**(W)** nur als Workflowbeteiligter (K01_W_User / K01_W_Group)\n"
          "**(T)** temporär, gefiltert auf Gesellschaft und Prüfungszeitraum",
          "info", extra="fontSize=11;")
    p.box(798, ly, 816, 150,
          "**Anmerkungen (Kap. 13.4)**\n"
          "¹ R-03: Projektleitung/Objektbetreuung mit reinem Objektbezug (O) statt (M); Schreibrecht K-02 für Nachweise, K-09 für Übernahme verteilter Post.\n"
          "² R-04: GF erhält den Geltungsbereich über DMS_GF_<Verbund>.   ³ R-07: Konzern-Controlling ggf. (A) statt (M), Entscheidung Livos.\n"
          "⁴ R-12: Löschen nur im Status Bearbeitung; Löschsperre (preventDeletion) übersteuert alle Löschrechte (AE-24).\n"
          "⁵ R-13: Schreiben auf K-01 (E-07, E-21, E-22, E-23), K-07 (Mails), K-08 (BIM4You), K-15 (Prüfberichte); Lesen aller Kategorien für Export S-15.\n"
          "⁶ R-14: nur Lesen; K-04 und K-09 nur nach Einzelfreigabe der Steuerabteilung.   ⁷ R-15: Inhaltszugriff nur befristet mit Freigabe Livos.",
          "note", extra="fontSize=10;")
    p.box(40, ly + 164, 1574, 110,
          "**Umsetzung in d.velop documents (AE-18)** – je Kategorie und Rechtestufe eine Permission (read / write / delete; ALLOWED · INHERITED · DENIED, DENIED gewinnt); "
          "Muster Kxx_M_Lesen, Kxx_M_Bearbeiten, Kxx_A_Zentral, Kxx_O_…, K01_W_…, Kxx_Admin → ca. 50–70 Permissions für 15 Kategorien, unabhängig von der Zahl der Gesellschaften (Seite 19).\n"
          "**Außerhalb der DMS-Matrix:** smart-invoice-Rechte (Workflowrollen SI_<Rolle>_<MandantNr>, REB je Mandant, Clearing), d.velop contracts (VTR_<Organisation>_<Rolle>), "
          "mail dispatcher (POST_<Verbund>_<Funktion>), process studio (Modellierung R-15, Test R-12), Lieferanten-App (App-Rollen).\n"
          "**Unverträglich:** R-02 + R-05, R-06 + R-05 in einer Person; R-12 + R-05 nur mit GF-Freigabe; R-15 ohne Fachrollen. R-09/R-10 ohne DMS-Zugang; R-10 gibt nur eine Stellungnahme ab, die verbindliche Freigabe erfolgt intern (Kap. 11.5.3).",
          "text", extra="fontSize=11;fillColor=%s;strokeColor=%s;rounded=1;arcSize=6;verticalAlign=middle;spacingLeft=8;" % (C['grey_l'], C['grey_m']))
    return p


# ----------------------------------------------------------------------------------------------
def page19(doc):
    p = doc.page("19 Rechtemodell Cloud", "p19")
    p.header("19 Rechtemodell Cloud",
             "Mechanik (Kap. 13.2/13.3): Entra ID → SCIM → flache Gruppen → Restriction Sets → Permission je Kategorie × Rechtestufe (AE-18). "
             "Gesellschaftstrennung über die Pflichteigenschaft Mandant (E-01, Designprinzip P1)")

    top = 128
    # Spalte 1: Entra ID + BeSync
    entra = p.box(40, top + 40, 230, 110,
                  "Microsoft Entra ID\n\n__Benutzer und Sicherheitsgruppen__\n__führend, Pflege Livos-IT (OP-16)__", "ext")
    besync = p.box(40, top + 250, 230, 120,
                   "BeSync / Lieferanten-App (S-04)\n\n__legt je Gesellschaft Dataset-Wert, Gruppe, Set-Zuordnung und smart-invoice-Mandant per API an; prüft Governance__",
                   "mdis")

    # Spalte 2: Gruppen
    gx, gw = 340, 310
    p.box(gx, top, gw, 420, "d.velop Gruppen (flach)", "group_t")
    grp = {}
    specs = [("R", "DMS_R_*  Rollengruppen\n__Träger der Permissions (~10–12)__"),
             ("G", "DMS_G_ / DMS_GB_<MandantNr>  Gesellschaft\n__Werteträger RS_Mandant_Lesen / _Bearbeiten__"),
             ("GF", "DMS_GF_<Verbund>  Gesellschaftsverbund\n__Werteliste eigener Gesellschaften (GF)__"),
             ("O", "DMS_O_<ObjektID>  Objekt\n__Werteträger RS_Objekt (PL, Externe)__"),
             ("SI", "dv_* / SI_<Rolle>_<MandantNr>\n__smart-invoice-Workflowrollen, REB__")]
    gy = top + 40
    for k, t in specs:
        grp[k] = p.box(gx + 15, gy, gw - 30, 62, t, "dvelop_l")
        gy += 74
    p.edge(entra, grp["R"], "S-13 SCIM 2.0\n+ SSO (OIDC)", "data", exit=(1, 0.5), entry=(0, 0.5))
    p.edge(besync, grp["G"], "Gruppen anlegen\n(über Entra ID)", "data", exit=(1, 0.3), entry=(0, 0.5))

    # Spalte 3: Restriction Sets
    rx, rw = 720, 300
    p.box(rx, top, rw, 420, "Restriction Sets (Gruppe → Werteliste)", "group_t")
    rsm = p.box(rx + 15, top + 40, rw - 30, 170,
                "**RS_Mandant_Lesen**\nDMS_G_10010 → [10010]\nDMS_G_10020 → [10020]\nDMS_GF_Nord → [10010, 10020, 10050]\n**RS_Mandant_Bearbeiten**\nDMS_GB_10010 → [10010]\n"
                "__neue Gesellschaft = 1 Zuordnung__\n__(API POST …/assignments)__", "dvelop_l", extra="align=left;spacingLeft=10;")
    rso = p.box(rx + 15, top + 230, rw - 30, 80,
                "**RS_Objekt**\nDMS_O_4711 → [4711]\n__Projektleiter / Externe nur für ein Objekt__", "dvelop_l", extra="align=left;spacingLeft=10;")
    p.box(rx + 15, top + 322, rw - 30, 86,
          "Zwei Sets je Rechtestufe, damit jemand in Gesellschaft A bearbeiten und in B nur lesen kann (Werteliste aus allen Gruppen, T03).",
          "text", extra="fontSize=10;")
    p.edge(grp["G"], rsm, "Werte", "data", exit=(1, 0.5), entry=(0, 0.4))
    p.edge(grp["GF"], rsm, "", "data", exit=(1, 0.5), entry=(0, 0.8))
    p.edge(grp["O"], rso, "Werte", "data", exit=(1, 0.5), entry=(0, 0.5))

    # Spalte 4: Permissions
    px_, pw = 1090, 340
    p.box(px_, top, pw, 420, "Permissions: Kategorie × Rechtestufe", "group_t")
    perms = [
        ("K01_M_Lesen", "Mandant = @Filter(RS_Mandant_Lesen) → DMS_R_Freigeber, DMS_R_Controlling: read"),
        ("K01_M_Bearbeiten", "Mandant = @Filter(RS_Mandant_Bearbeiten) → DMS_R_Pruefer: read + write"),
        ("K01_A_Zentral", "nur CATEGORY (ohne Filter) → DMS_R_Buchhaltung_Extern: read + write"),
        ("K11_O_Lesen", "Objekt-ID = @Filter(RS_Objekt) → Projektleitung, DMS_R_Partner_Extern: read"),
        ("K01_W_User / K01_W_Group", "WorkflowbeteiligteIDs = @CURRENT_USER / @CURRENT_USER_IN_GROUP: read"),
        ("Kxx_Admin", "→ DMS_R_Fachadmin: read/write/delete (+ Löschsperre)"),
    ]
    pb = []
    py = top + 36
    for n, t in perms:
        pb.append(p.box(px_ + 12, py, pw - 24, 58, "**%s**\n%s" % (n, t), "dvelop_l", extra="align=left;spacingLeft=8;fontSize=10;"))
        py += 63
    p.edge(rsm, pb[0], "@Filter", "data", exit=(1, 0.2), entry=(0, 0.5))
    p.edge(rsm, pb[1], "", "data", exit=(1, 0.45), entry=(0, 0.5))
    p.edge(rso, pb[3], "@Filter", "data", exit=(1, 0.5), entry=(0, 0.5))
    p.edge(grp["R"], pb[0], "Zuordnung read/write/delete", "flow", exit=(0.9, 0), entry=(0.95, 0),
           points=[(gx + gw * 0.9, top - 8), (px_ + 12 + (pw - 24) * 0.95, top - 8)])

    # Spalte 5: Dokument + Regeln
    d = p.box(1470, top + 40, 144, 150,
              "Dokument K-01\n\nMandant (E-01)\nObjekt-ID (E-03)\nWorkflow-beteiligte (E-32)", "doc")
    for b in (pb[1], pb[4]):
        p.edge(b, d, "", "flow", exit=(1, 0.5), entry=(0, 0.5))
    p.box(1450, top + 220, 164, 200,
          "**Rechtestufen (Cloud)**\nread / write / delete getrennt\n\nALLOWED · INHERITED · DENIED\n\n**DENIED gewinnt** über alle Permissions einer Gruppe",
          "info", extra="fontSize=10;")

    # ---------------- Beispiel Sachbearbeiter Nord ----------------
    by = 580
    p.box(40, by - 6, 1574, 300, "Beispiel: Benutzerin „Asset Managerin Nord\" sieht und bearbeitet nur Mandant 10010", "group_g")
    u = p.box(60, by + 60, 240, 110,
              "**„Asset Managerin Nord\"** (Beispiel)\n\nMitglied in:\nDMS_R_Pruefer\nDMS_G_10010, DMS_GB_10010", "task")
    calc = p.box(360, by + 60, 270, 110,
                 "**RS_Mandant_Bearbeiten wertet alle Gruppen des Benutzers aus**\n\nDMS_GB_10010 → [10010]\nberechnete Werteliste = **[10010]**",
                 "dvelop_l")
    perm = p.box(690, by + 60, 290, 110,
                 "**Permission K01_M_Bearbeiten**\n(zugeordnet an DMS_R_Pruefer)\n\nPrüfung: Mandant des Dokuments ∈ [10010]?",
                 "dvelop_l")
    gw_ = p.box(1020, by + 80, 110, 70, "Mandant\nin Liste?", "gateway")
    d1 = p.box(1200, by + 40, 390, 56,
               "RE-2026-1041 · Musterbau GmbH · 14.756,00 €\nMandant 10010 · Livos Objektgesellschaft Nord mbH", "doc")
    d2 = p.box(1200, by + 120, 390, 50, "Eingangsrechnung Mandant 10020 (Livos Objektgesellschaft Süd mbH)", "doc")
    d3 = p.box(1200, by + 190, 390, 50, "Eingangsrechnung Mandant 10030 (Livos Bau & Projekt GmbH)", "doc")
    p.edge(u, calc, "", "flow")
    p.edge(calc, perm, "", "flow")
    p.edge(perm, gw_, "", "flow")
    p.edge(gw_, d1, "ja: lesen + bearbeiten", "green", exit=(0.5, 0), entry=(0, 0.5), points=[(1075, by + 68)])
    p.edge(gw_, d2, "nein: unsichtbar", "red", exit=(1, 0.5), entry=(0, 0.5))
    p.edge(gw_, d3, "nein", "red", exit=(0.5, 1), entry=(0, 0.5), points=[(1075, by + 215)])
    p.box(60, by + 190, 930, 96,
          "**Ausnahme Workflowbeteiligte:** Wird der Benutzer an einer Rechnung von Mandant 10020 beteiligt (z.B. als Vertretung), erhält er über "
          "„K01_W_User\" Leserecht auf genau diese Rechnung. Deshalb Vertretungen möglichst innerhalb derselben Gesellschaftsgruppe (AE-17).\n"
          "**Grenze des orthogonalen Modells:** Rolle × Gesellschaft gilt für alle Gesellschaften des Benutzers gleich – abweichende Rechte je Gesellschaft über getrennte Sets je Rechtestufe.",
          "text", extra="fontSize=11;")

    # ---------------- Warnung, Test, neue Gesellschaft ----------------
    wy = 900
    p.box(40, wy, 420, 200,
          "**Achtung: leere Werteliste = alle Werte**\n\n"
          "Eine Restriction-Set-Zuordnung mit leerer Liste (oder Typ NO_ASSIGNMENT) gibt Zugriff auf **alle** Mandanten.\n\n"
          "• Zentrale Buchhaltung/Controlling nie über leere Listen, sondern über eine eigene, sichtbare Permission ohne Mandant-Filter.\n"
          "• BeSync prüft täglich: keine leeren Listen, keine NO_ASSIGNMENT-Zuordnung; Rechteänderungen mit Vier-Augen-Freigabe und Protokoll [A].",
          "warn")
    p.box(480, wy, 420, 200,
          "**Test T03 (OP-08) – Kernannahme vor Go-live**\n\n"
          "Annahme: Die Werteliste eines Restriction Sets ergibt sich aus **allen** Gruppen des Benutzers – Permission an der Rollengruppe, Werte nur über die Gesellschaftsgruppe.\n\n"
          "Test im Test-Tenant: Benutzer in DMS_R_Pruefer + DMS_G_10010 sieht nur 10010.\n"
          "Falls widerlegt: kombinierte Gruppen DMS_<Rolle>_<MandantNr> (mehr Gruppen, weiterhin per API automatisierbar).",
          "open", extra="align=left;verticalAlign=top;spacing=6;fontSize=11;")
    p.box(920, wy, 380, 200,
          "**Neue Gesellschaft – 4 Schritte, per API automatisierbar (S-04)**\n\n"
          "1. Dataset-Wert Mandant (E-01)\n"
          "2. Entra-Gruppen DMS_G_/DMS_GB_<Nr> (SCIM)\n"
          "3. Zuordnung in RS_Mandant_Lesen/_Bearbeiten\n"
          "4. smart-invoice-Mandant im Bucket\n\n"
          "REB-Berechtigung je Mandant ggf. manuell (API nicht dokumentiert).\nMengengerüst: ca. 50–70 Permissions, unabhängig von der Gesellschaftszahl.",
          "info")
    status_legend(p, 1320, wy)
    return p


# ----------------------------------------------------------------------------------------------
def page20(doc):
    p = doc.page("20 DATEV- und Zahlungsintegration", "p20")
    p.header("20 DATEV- und Zahlungsintegration",
             "Sequenz vom Stammdatenabgleich bis zur Rückmeldung „bezahlt\" (AE-07, AE-08, AE-10): "
             "d.velop liefert die Freigabe, DATEV bucht, multicash zahlt, BeSync meldet den Zahlstatus zurück")

    names = [("d.velop invoices /\nsmart invoice", "dvelop"), ("LDconnect\n(Option DATEV ReWe)", "dvelop_l"),
             ("Riecken-\nDatengateway", "ext"), ("DATEV ReWe\n(Hoster · Trios)", "ext"),
             ("multicash\n(Omikron)", "ext"), ("Bank\n(EBICS)", "ext"), ("BeSync\n(MDIS)", "mdis")]
    x0, step, bw = 46, 152, 136
    X = []
    top, bottom = 122, 1100
    for i, (n, st) in enumerate(names):
        cx = x0 + i * step + bw / 2
        X.append(cx)
        p.line(cx, top + 50, cx, bottom, "assoc")
        p.box(cx - bw / 2, top, bw, 50, n, st)
    L = dict(dv=X[0], ld=X[1], gw=X[2], dt=X[3], mc=X[4], bk=X[5], bs=X[6])
    right = x0 + 6 * step + bw + 10   # rechter Rand Sequenzbereich (~1110)

    def frame(y, h, title):
        p.box(30, y, right - 30, h, "", "group")
        p.box(38, y + 4, 7 * len(title) + 16, 20, title, "text", extra="fillColor=#FFFFFF;fontStyle=1;fontSize=11;fontColor=%s;verticalAlign=middle;spacing=2;" % C['grey'])

    def act(key, y, h, text, st="task", w=150):
        return p.box(L[key] - w / 2, y, w, h, text, st, extra="fontSize=10;")

    # 1 Stammdaten täglich
    y = 196
    frame(y, 150, "① täglich · S-02 Stammdaten (Status K)")
    _hline(p, L["dt"], L["gw"], y + 62, "straight", "Kreditoren, Sachkonten,\nSteuerschl., Zahlungsbed.", lw=150)
    _hline(p, L["gw"], L["ld"], y + 62, "straight", "Bankverb.,\nKOST1/KOST2", lw=140)
    _hline(p, L["ld"], L["dv"], y + 62, "straight", "je Mandant\nin den Bucket", lw=140)
    act("dv", y + 80, 56, "Stammdaten im Bucket\n(IBAN-Abgleich, Kontierung)", "task_d")
    act("dt", y + 80, 40, "DATEVconnect\n(Beraternr-Mandantennr)", "task_ext")

    # 2 je Rechnung
    y = 362
    frame(y, 236, "② je Rechnung, ereignisgesteuert · S-01 Buchungsvorschlag + Beleglink (Status K)")
    act("dv", y + 26, 64, "WF-01: Prüfung, Freigabe,\n**Zahlungsfreigabe**\n(vor Übergabe, AE-06)")
    act("dv", y + 98, 40, "Schritt Buchhaltung\n(Trios, M-07)")
    _hline(p, L["dv"] + 75, L["ld"], y + 150, "straight", "integration.export", lw=140)
    _hline(p, L["ld"], L["gw"], y + 150, "straight", "Buchungs-\nvorschlag", lw=140)
    _hline(p, L["gw"], L["dt"], y + 150, "straight", "+ Beleglink\n(16 Felder)", lw=140)
    act("dt", y + 164, 62, "Trios übernimmt und\nbucht → **OPOS**\n(Takt Trios)", "task_ext")
    p.box(L["dv"] - 70, y + 176, 330, 40, "Beleg bleibt im d.velop-Archiv; Anzeige aus DATEV über den Beleglink (Beleganzeige Drittanbieter)",
          "info", extra="fontSize=10;verticalAlign=middle;")

    # 3 Zahllauf
    y = 614
    frame(y, 290, "③ Zahllauf · S-07 SEPA-Datei (Standard DATEV + multicash)")
    act("dt", y + 26, 50, "Zahlungsvorschlag\n(Fälligkeit, Skonto)", "task_ext")
    _hline(p, L["dt"], L["mc"], y + 104, "straight", "SEPA-XML\n(pain.001)", lw=140)
    act("mc", y + 116, 62, "Unterschrift berechtigter\nLivos-Nutzer (R-05),\nVier-Augen", "task_ext")
    _hline(p, L["mc"], L["bk"], y + 214, "straight", "EBICS\nZahlauftrag", lw=140)
    _hline(p, L["bk"], L["mc"], y + 252, "straight", "Kontoauszug\ncamt.053", lw=140, above=False)
    _hline(p, L["mc"], L["dt"], y + 252, "straight", "Kontoauszug →\nOP-Ausgleich (Trios)", lw=150, above=False)

    # 4 Rückmeldung
    y = 920
    frame(y, 170, "④ täglich (nachts, optional mehrfach) · S-06 Zahlstatus (Status A, BeSync, Phase 3)")
    _hline(p, L["bs"], L["dt"], y + 50, "msg", "OPOS lesen je Mandant\n(DATEVconnect accounts-payable)", lw=300)
    _hline(p, L["dt"], L["bs"], y + 84, "data", "ausgeglichene Posten, Zahldatum", lw=300, above=False)
    _hline(p, L["bs"], L["dv"], y + 140, "straight", "S-06: DMS-Eigenschaft Zahlstatus = bezahlt / teilbezahlt, Zahldatum (E-23) am archivierten Beleg", lw=700)

    # ---------------- rechte Spalte ----------------
    rx, rw = 1130, 484
    fields = ["Belegfeld 1", "Belegfeld 2", "Brutto-Betrag", "BU-Gegenkonto", "Buchungstext", "Datum",
              "Dokumentenlink", "Geschäftspartner", "Konto", "KOST1", "KOST2", "Leistungsdatum",
              "Steuersatz", "Steuerschlüssel (BU-Code)", "Waren und Dienstleistungen", "WKZ"]
    p.box(rx, 122, rw, 30, "S-01 Buchungsvorschlag: 16 Felder je Buchungssatz (LDconnect)", "h2", extra="fontSize=13;")
    rows = [["Nr", "Feld", "Nr", "Feld"]]
    for i in range(8):
        rows.append([str(i + 1), fields[i], str(i + 9), fields[i + 8]])
    p.table(rx, 156, [36, 206, 36, 206], rows, rowh=26)
    p.box(rx, 156 + 9 * 26 + 6, rw, 30, "Quelle: LDconnect-Leistungsbeschreibung; Beleg als Link, Belegbild optional über DUO (S-03)",
          "small")
    p.box(rx, 430, rw, 122,
          "**Nicht in der Feldliste – Konsequenzen**\n"
          "• **Fälligkeit, Skonto:** nicht übergeben; DATEV nutzt Zahlungsbedingungen aus dem Kreditorenstamm. Ob Belegfeld 2 für ein Fälligkeitsdatum nutzbar ist, ist offen [O] (OP-22).\n"
          "• **Postensperre:** fehlt → Zahlungsfreigabe muss **vor** der Übergabe liegen (AE-06).\n"
          "• **IBAN:** fehlt → IBAN-Abgleich in smart invoice gegen Stamm (S-02).\n"
          "• **Zahlbetrag/Kürzung:** übergeben wird der Bruttobetrag → Verarbeitung mit Trios klären (OP-05).",
          "warn")
    p.box(rx, 566, rw, 86,
          "**Einstufige Übergabe (AE-08, Entscheidung offen)**\n"
          "LDconnect übergibt je Rechnung einmal. Das „Vorerfassungsjournal\" des Zielbilds ersetzt das REB (offene, unverbuchte Rechnungen, CSV zum Monatsende). "
          "Frühe Übergabe mit Postensperre über BeSync/EXTF wäre eine Anpassung [A] (Option Phase 3).",
          "info")
    p.box(rx, 666, rw, 84,
          "**Voraussetzungen (OP-04)**\nDATEVconnect, dedizierter DATEV-Benutzer, Riecken-Datengateway beim Hoster (Pflicht bei gehostetem DATEV), "
          "Beleganzeige Drittanbieter; Zugriffsweg BeSync auf DATEVconnect (OPOS) beim Hoster klären.",
          "note")
    srow = [["Schnittstelle", "Richtung", "Grad"],
            ["S-02 Stammdaten", "DATEV → smart invoice, täglich", "K"],
            ["S-01 Buchungsvorschlag + Beleglink", "d.velop → DATEV, je Rechnung", "K"],
            ["S-07 SEPA-Datei", "DATEV → multicash, je Zahllauf", "S"],
            ["S-06 Zahlstatus (Phase 3)", "DATEV → BeSync → d.velop", "A"]]
    p.table(rx, 766, [200, 234, 50], srow, rowh=24, styles={(r, 2): "td_c" for r in range(1, 5)})
    status_legend(p, rx, 910)
    p.box(rx + 316, 910, 168, 150,
          "**Nicht empfohlen:** SEPA-Datei direkt aus d.velop/BeSync (Doppelzahlungsrisiko, DATEV bleibt führend)", "open",
          extra="align=left;verticalAlign=top;spacing=6;fontSize=10;")
    return p


# ----------------------------------------------------------------------------------------------
def page21(doc):
    p = doc.page("21 Reporting und KPI", "p21")
    p.header("21 Reporting und KPI",
             "Operativ und für das Management im Rechnungseingangsbuch (REB) [S]; historische Durchlauf- und Liegezeiten über "
             "BeSync-Ereignisprotokoll → MS SQL → evidanza [A] (AE-16, S-12)")

    # REB-Mockup
    wx, wy, ww, wh = 40, 118, 960, 340
    cx, cy, cw, ch = ui_window(p, wx, wy, ww, wh, "Rechnungseingangsbuch – Managementsicht (M-09)",
                               crumbs="Rechnungseingangsbuch  ›  Alle offenen Rechnungen  ›  Schnellzugriff „Gesellschaftsgruppe Nord\" (Beispiel)",
                               nav_items=["**Schnellzugriffe**", "", "Meine offenen Rechnungen  (12)", "Rechnungen in Vertretung  (2)",
                                          "An mich eskaliert  (1)", "Alle offenen Rechnungen", "", "__eigene (Beispiele):__",
                                          "Über 10.000 € netto", "Gesellschaftsgruppe Nord", "Skonto fällig ≤ 5 Tage",
                                          "Schritt Zahlungsfreigabe", "", "Archiv (6/12 Monate)"],
                               nav_w=200, user="Controlling (R-07)")
    p.box(cx, cy, 380, 24, "Gruppiert nach: Mandant ▾   ·   Filter: Status offen", "ui_input")
    ui_buttons(p, cx + cw - 250, cy - 2, [("CSV-Export (alle Spalten)", "ui_btn")], w=250)
    cols = [56, 112, 92, 76, 118, 80, 124, 78]
    rows = [["Mandant", "Kreditor", "Rechnungs-Nr", "Brutto €", "Aktueller Schritt", "Schritt seit", "Zugewiesen", "Status"],
            ["10010", "Musterbau GmbH", "RE-2026-1041", "14.756,00", "Zahlungsfreigabe", "3 Tage", "Zahlungsfreig. Nord", "offen"],
            ["10010", "Elektro Kühn KG", "2026-0877", "2.380,00", "Sachl. Prüfung", "9 Tage", "M. Berger", "Eskalation 1"],
            ["10020", "Blitz Reinigung", "GR-55120", "1.071,00", "Fachl. Freigabe", "2 Tage", "Freigeber Süd", "offen"],
            ["10030", "Dachtechnik Olsen", "D-2026-311", "8.925,00", "Verteilung", "1 Tag", "Rechnungseingang", "Clearing"],
            ["10030", "Stadtwerke Beispiel", "SW-99812", "642,60", "Buchhaltung", "0 Tage", "Trios", "offen"]]
    ui_table(p, cx, cy + 36, cols, rows, rowh=26)
    # Hervorhebung der vier Kernspalten
    kx = cx + sum(cols[:4])
    p.box(kx - 2, cy + 34, sum(cols[4:]) + 4, 26 * 6 + 4, "", "rounded=0;fillColor=none;strokeColor=%s;strokeWidth=3;" % C['orange'])
    ann(p, kx - 14, cy + 24, 1)
    ann(p, cx + 386, cy + 1, 2)
    ann(p, cx + cw - 280, cy + 1, 3)
    p.box(cx, cy + 36 + 26 * 6 + 12, cw, 64,
          "**1** Standardspalten Aktueller Schritt · Aktueller Schritt seit · Zugewiesen · Status (inkl. Clearing, Eskalationsstufe 1/2)   "
          "**2** Gruppierung nach Mandant/Datum, Freigabe je Mandant   **3** CSV-Export sichtbare/alle Spalten, Download 30 Tage "
          "(z.B. Monatsende: offene/unverbuchte Rechnungen für Rückstellungen)",
          "text", extra="fontSize=10;")

    # REB-Sichten je Rolle
    rx, rw = 1020, 594
    p.box(rx, 118, rw, 26, "REB-Sichten und Schnellzugriffe je Rolle (Vorschlag)", "h2")
    srows = [["Rolle", "Sicht / Schnellzugriff", "Filter · Gruppierung"],
             ["R-02 Rechnungseingang", "Alle offenen · Verteilung/Clearing", "Status Clearing, Mandant"],
             ["R-03 Sachl. Prüfer", "Meine offenen · In Vertretung", "Schritt seit (älteste zuerst)"],
             ["R-04 Freigeber", "Meine offenen · An mich eskaliert", "Betrag, Mandant"],
             ["R-05 Zahlungsfreigeber", "Schritt Zahlungsfreigabe", "Skontofälligkeit aufsteigend"],
             ["R-06 Trios", "Schritt Buchhaltung, alle Mandanten", "Mandant (DATEV-Bestand)"],
             ["R-07 Controlling", "Alle offenen (mandantenbezogen)", "Gesellschaft × Schritt, CSV"],
             ["R-12 Fachadmin", "Clearing · Eskalationsstufe 2", "Mandant, Zugewiesen"]]
    ye = p.table(rx, 148, [170, 232, 192], srows, rowh=28)
    p.box(rx, ye + 8, rw, 70,
          "**Grenze Startseite:** nur 4 Standard-Widgets (Suche, Zuletzt bearbeitet, Beobachtet, Favorisiert) plus Verknüpfungs-/Listen-Widgets – "
          "keine fachlichen KPI-Kacheln. Managementsicht daher im REB, Kennzahlen in evidanza. „Sichtbarkeit von Widgets\" ist keine Berechtigung.",
          "warn", extra="fontSize=10;")

    # KPI-Katalog
    ky = 520
    p.box(40, ky, 960, 26, "KPI-Katalog (Vorschlag, mit Livos-Controlling abzustimmen)", "h2")
    krow = [["ID", "Kennzahl (K16 §16.3)", "Quelle", "Grad", "ab Phase"],
            ["KPI-01", "Belege im Umlauf je Status (je Mandant, Segment)", "REB (Stichtag), BeSync (Verlauf)", "S / A", "1 / 2"],
            ["KPI-02", "Liegezeit aktueller Schritt", "REB", "S", "1"],
            ["KPI-03", "Durchlaufzeit Eingang → Freigabe", "BeSync", "A", "2"],
            ["KPI-04", "Durchlaufzeit Eingang → Übergabe DATEV", "BeSync", "A", "2"],
            ["KPI-05", "Durchlaufzeit Eingang → Zahlung", "BeSync + DATEV (S-06)", "A", "3"],
            ["KPI-06", "Liegezeit je Bearbeiter und Schritt", "BeSync (Bearbeiter offen: OP-26, T31)", "A", "2"],
            ["KPI-07", "Skontoquote", "BeSync + DATEV (S-06)", "A", "3"],
            ["KPI-08", "Verlorenes Skonto", "BeSync + DATEV (S-06)", "A", "3"],
            ["KPI-09", "Klärfallquote (je Klärgrund)", "BeSync", "A", "2"],
            ["KPI-10", "Dublettenquote", "BeSync (Endpfad, Begründung)", "A", "2"],
            ["KPI-11", "Automatisierungsquote Erkennung", "BeSync + d.velop invoices Statistik", "A / S", "2"],
            ["KPI-12", "E-Rechnungsquote", "REB, BeSync", "S / A", "1"],
            ["KPI-13", "Rückweisungsquote nach Grund (E-26)", "BeSync", "A", "2"],
            ["KPI-14", "Kürzungsvolumen (E-13)", "BeSync", "A", "2"],
            ["KPI-15", "PM-Freigaben offen (WF-03)", "REB", "S", "2"],
            ["KPI-16", "Eskalationen (Stufe 1/2)", "REB, BeSync", "S / A", "1"],
            ["KPI-17", "Offene Bau-Prüfungen (BIM4You-Transfers)", "BeSync", "A", "3"]]
    st = {}
    for r in range(1, len(krow)):
        st[(r, 3)] = "td_c"
        st[(r, 4)] = "td_c"
    ye = p.table(40, ky + 30, [66, 380, 380, 64, 70], krow, rowh=22, styles=st)
    p.box(40, ye + 6, 960, 26,
          "Grad: S = Standard im REB (Stichtag) · A = Anpassung über BeSync-Ereignisprotokoll/evidanza (Historie). KPI-06 nur nach Klärung mit Datenschutz/Betriebsrat (16.5).",
          "small", extra="fontSize=10;")
    p.box(40, ye + 36, 960, 56,
          "**Einführung (Kap. 16, 19):** Phase 1 REB-Sichten (KPI-01/02/12/16) und Protokollierung S-12 ab Pilot-Go-live · "
          "Phase 2 evidanza-Auswertungen (KPI-03, 04, 06, 09–11, 13–15) · Phase 3 nach S-06 bzw. BIM4You-Transfer (KPI-05, 07, 08, 17).",
          "info", extra="fontSize=11;")

    # evidanza-Pfad
    ex, ey, ew = 1020, 520, 594
    p.box(ex, ey, ew, 26, "evidanza-Pfad (S-12, AE-16) [A]", "h2")
    si = p.box(ex, ey + 40, 170, 90, "smart invoice\n\nExport-Event je\nSchrittverbindung\n(from_step / to_step)", "dvelop", extra="fontSize=11;")
    bs = p.box(ex + 212, ey + 40, 170, 90, "BeSync\nLogging-Webhook\n\n__sofort quittieren, Queue__", "mdis")
    api = p.box(ex, ey + 160, 170, 80, "Task-/Process-/DMS-API\n__nächtliche Abfrage__", "dvelop_l")
    sql = p.box(ex + 212, ey + 160, 170, 84, "MS SQL Staging\n__Beleg × Schritt × Zeit × Bearbeiter__", "db")
    ev = p.box(ex + 424, ey + 160, 170, 80, "evidanza\n__Kennzahlen, Berichte__", "ext")
    p.edge(si, bs, "Webhook", "data")
    p.edge(api, sql, "nächtlich", "data")
    p.edge(bs, sql, "", "data")
    p.edge(sql, ev, "SQL", "data")
    p.box(ex + 424, ey + 40, 170, 90,
          "Kennzahlen werden in SQL/evidanza berechnet – eine Spalte „Liegezeit\" gibt es in d.velop nicht.", "text", extra="fontSize=10;")
    p.box(ex, ey + 258, ew, 104,
          "**Betriebsaspekte**\n"
          "• Aufgabenhistorie der Plattform nur 30–365 Tage → laufend abziehen.\n"
          "• Ist der Webhook nicht erreichbar, läuft der Beleg in den Fehlerschritt → hochverfügbar auslegen oder nur an unkritischen Verbindungen exportieren.\n"
          "• Offen: handelnder Benutzer im Export-Event (sonst Task-API/E-32; OP-26, T31)",
          "note")
    status_legend(p, ex, ey + 378)
    p.box(ex + 316, ey + 378, 278, 150,
          "**Schnellstart ohne Entwicklung:** regelmäßiger CSV-Export „Alle offenen – alle Spalten\" als Stichtagssicht (manuell). "
          "Belastbare Historie nur über das Ereignisprotokoll.", "info", extra="fontSize=10;")
    return p


# ----------------------------------------------------------------------------------------------
def page22(doc):
    p = doc.page("22 Roadmap", "p22")
    p.header("22 Roadmap",
             "Schrittweise Einführung (P8) nach Kap. 19.2/19.8 – 12 Monate ab Beauftragung (M1); abhängig von DATEV-Anbindung, Phase-0-Entscheidungen, Key-Usern")
    p.box(250, 32, 290, 28, "VORSCHLAG – Zeitplan zur Abstimmung", "badge_o", extra="fontSize=12;")

    lx, lw = 40, 470
    tx0, mw, months = 520, 91, 12
    y0 = 116
    p.box(lx, y0, lw, 36, "Phase / Arbeitspaket (IDs)", "th")
    for m in range(months):
        p.box(tx0 + m * mw, y0, mw, 36, "M%d" % (m + 1), "th", extra="align=center;")
    # (Name, Start, Ende) in Monaten ab 0; Balken aus K19 §19.8
    phases = [
        ("Phase 0 Klärung & Setup (4–6 Wochen)", 0, 2, "M1–M2", [
            ("Prozess- und Detailworkshops; Entscheidungen AE-08, AE-09, AE-11, ED-01 ff.", 0, 2, "ext"),
            ("Test-Tenant, Entra ID (SCIM/OIDC); Plattformtests T01–T23 ff.", 0, 2, "open"),
            ("DATEV-Komponenten und Gateway bereitstellen (LDconnect, Riecken, OP-04)", 0, 3, "ext"),
            ("KI-PoC Kreditorenkonsolidierung; Mandantenerkennung vorab (OP-02)", 0, 2, "mdis"),
        ]),
        ("Phase 1 MVP Rechnungseingang (Aufbau + Pilot)", 1, 5, "Aufbau M2–M4 · Pilot M4–M5", [
            ("WF-01, WF-04, WF-08; Rechte, Aktenplan, Aufbewahrung", 1, 4, "dvelop_l"),
            ("S-01, S-02 DATEV · S-13 Identitäten · S-14 E-Mail (ER)", 1, 4, "dvelop_l"),
            ("S-04 Erstimport Pilotgesellschaften · S-05 Anforderung per E-Mail", 2, 4, "ext"),
            ("S-12 Protokollierung ab Pilot-Go-live · S-15 Voraussetzung P1", 3, 5, "mdis"),
            ("Pilotbetrieb 3–5 Gesellschaften (Bau über WF-01 ohne BIM4You-Automatik)", 3, 5, "dvelop"),
        ]),
        ("Phase 2 Rollout, PM-Freigabe, Rückweisung, Reporting", 4, 7, "M5–M7", [
            ("Rollout alle Gesellschaften in Wellen (20–30 je Welle)", 4, 7, "dvelop"),
            ("WF-03 PM-Freigabe · WF-05 Rückweisung/Kürzung (S-11)", 4, 7, "mdis"),
            ("S-04 / S-05 Automatik Lieferanten-App", 4, 7, "mdis"),
            ("S-12 Auswertungen in evidanza · S-15 Exportskript + Probeexport", 4, 7, "mdis"),
        ]),
        ("Phase 3 Bau/BIM4You, Zahlstatus, FSB", 6, 10, "M7–M10", [
            ("WF-02 Bau-ER mit BIM4You (S-08, S-09, S-10)", 6, 10, "mdis"),
            ("S-06 Zahlstatus „bezahlt\" aus DATEV-OPOS", 6, 10, "mdis"),
            ("FSB § 48b (AE-15) · WF-10 externe Ad-hoc-Freigabe (Stellungnahme)", 6, 10, "mdis"),
            ("optional: S-16 PM-Buchungsdaten → BI", 6, 10, "open"),
        ]),
        ("Phase 4 Verträge, Post, DMS-Ausbau", 8, 11, "M9–M11", [
            ("WF-06 Verträge mit d.velop contracts (AE-20)", 8, 11, "dvelop_l"),
            ("WF-07 Postverteilung, KI-Klassifizierung, mail dispatcher (AE-21)", 8, 11, "dvelop_l"),
            ("DMS-Ausbau, Outlook, mobile · d.velop pilot für Verträge (OP-19)", 8, 11, "open"),
        ]),
        ("Phase 5 Optimierung (fortlaufend)", 10, 12, "ab M11", [
            ("KI-Auswertung, MDIS X.One (AE-27) · WF-09 Freigaben ohne Rechnung", 10, 12, "dvelop_l"),
            ("S-17 ERP-/PM-Stammdatensync (Folgeprojekt)", 10, 12, "open"),
        ]),
    ]
    ph_h, sub_h = 26, 21
    y_end = y0 + 40 + sum(ph_h + len(sb) * sub_h + 4 for _, _, _, _, sb in phases)
    for m in range(months + 1):
        p.line(tx0 + m * mw, y0 + 36, tx0 + m * mw, y_end, "assoc", extra="strokeColor=%s;" % C['grey_m'])
    y = y0 + 40
    for name, a, b, lab, subs in phases:
        p.box(lx, y, lw, ph_h, name, "rounded=0;fillColor=%s;strokeColor=%s;fontColor=#FFFFFF;fontStyle=1;align=left;spacingLeft=8;fontSize=12;" % (C['navy'], C['navy']))
        p.box(tx0, y, months * mw, ph_h, "", "rounded=0;fillColor=%s;strokeColor=%s;opacity=60;" % (C['grey_l'], C['grey_m']))
        p.box(tx0 + a * mw, y + 3, (b - a) * mw, ph_h - 6, lab, "dvelop", extra="fontSize=11;arcSize=30;")
        y += ph_h
        for sname, sa, sb, stl in subs:
            p.box(lx, y, lw, sub_h, sname, "td", extra="fontSize=10;spacingLeft=14;")
            p.line(tx0, y + sub_h, tx0 + months * mw, y + sub_h, "line", extra="strokeColor=%s;" % C['grey_m'])
            p.box(tx0 + sa * mw + 2, y + 4, (sb - sa) * mw - 4, sub_h - 8, "", stl, extra="arcSize=30;")
            y += sub_h
        y += 4

    # Meilensteine / Qualitätstore (K19 §19.8)
    ms = [(2.0, "QG-0 Fein-\nkonzept, ED\n(Ende M2)"), (3.05, "QG-1a Pilot-\nGo-live\n(Anfang M4)"),
          (4.0, "QG-1b Frei-\ngabe Rollout\n(Ende M4/M5)"), (7.0, "QG-2 alle\nGesellschaften\n(Ende M7)"),
          (10.0, "QG-3 Bau/BIM4You\nproduktiv\n(Ende M10)"), (11.0, "QG-4 Verträge\n+ Post\n(Ende M11)")]
    for m, _ in ms:
        p.line(tx0 + m * mw, y0 + 36, tx0 + m * mw, y_end + 8, "assoc", extra="strokeColor=%s;dashed=1;" % C['orange'])
    my = y + 8
    p.box(lx, my, lw, 58, "Meilensteine / Qualitätstore (Vorschlag)\nQG-5 je Optimierungspaket", "th", extra="fontSize=12;")
    p.box(tx0, my, months * mw, 58, "", "rounded=0;fillColor=%s;strokeColor=%s;" % (C['yellow_l'], C['grey_m']))
    for i, (m, t) in enumerate(ms):
        xm = tx0 + m * mw
        p.box(xm - 8, my + 3, 16, 16, "", "gateway", extra="fillColor=%s;strokeColor=%s;" % (C['orange'], C['orange']))
        w = 84
        p.box(xm - w / 2, my + 18, w, 40, t, "textc", extra="fontSize=9;fontStyle=1;")

    ny = my + 70
    nh = min(150, 1120 - ny)
    p.box(lx, ny, 560, nh,
          "**Leitgedanken**\n"
          "• Rechnungseingang zuerst, dann PM-Freigabe, Bau/BIM4You, Verträge, Post (P8).\n"
          "• BeSync in Phase 1 nur für die Protokollierung (S-12); Lieferanten-App-Automatik (S-04/S-05), S-11 und Exportskript S-15 in Phase 2.\n"
          "• Phasen 3 und 4 können sich überschneiden (gemeinsame MDIS-Ressourcen).",
          "info", extra="fontSize=11;")
    p.box(lx + 580, ny, 560, nh,
          "**Kritischer Pfad und Abhängigkeiten**\n"
          "• DATEV-Anbindung in Woche 1 von Phase 0 anstoßen (Hoster, Trios, Gateway, OP-04).\n"
          "• Mandantenerkennung mit echten Belegen (OP-02) und Test T03 vor Pilot-Go-live.\n"
          "• Phase 3: ED-03, OP-06 (BIB GmbH), OP-07, OPOS-Zugriff (OP-04/OP-43). Projektstart Q4/2026 → Pilot-Go-live Q1/2027.",
          "note", extra="fontSize=11;")
    legend_box(p, lx + 1160, ny, [("dvelop", "Phase / d.velop Standard"), ("dvelop_l", "d.velop Konfiguration"),
                                   ("mdis", "MDIS BeSync (Anpassung)"), ("ext", "Livos / Trios / extern"),
                                   ("open", "Klärung / optional")], "Legende Balken", w=414)
    return p


def build(doc):
    page18(doc)
    page19(doc)
    page20(doc)
    page21(doc)
    page22(doc)
