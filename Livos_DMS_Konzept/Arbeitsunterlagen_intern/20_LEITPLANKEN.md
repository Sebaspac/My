# 20 — LEITPLANKEN für das Livos-DMS-Gesamtkonzept (verbindlich für alle Autoren)

Stand: 26.09.2026 · Herausgeber: Lead-Auditor (MDIS) · Status: freigegeben zur Konzepterstellung

Dieses Dokument ist die **einzige verbindliche Basis** für die Konzeptkapitel. Es fasst die auditierte Rechercheleistung (Dateien 01–15 in SP/work) zu Entscheidungen, ID-Katalogen und Bewertungen zusammen. Wer ein Kapitel schreibt, verwendet **exakt** die IDs, Namen und Bewertungen aus diesem Dokument. Abweichungen nur mit Begründung im Text und Hinweis im Rückgabebericht.

SP = /tmp/claude-0/-home-user-My/9b9087bc-2d0b-5088-b7bc-148ecd5c6c69/scratchpad

---

## 0. Schreibregeln

1. **Sprache:** Deutsch, sachlich, Beratungsstil, aktiv formuliert, kurze Sätze. Kein Marketing. Keine Emojis.
2. **Zielgruppe des Konzepts:** Livos (Projektleitung André Töpper, Finanz/Controlling, Buchhaltung, Geschäftsführung) und MDIS-Projektteam. Das Konzept ist **kundentauglich**. Interne MDIS-Hinweise (Preise, Korrekturen an eigenen Aussagen, Vertriebstaktik) gehören **nicht** ins Konzept, sondern ins Fazit-Dokument (interner Teil).
3. **Belegstatus** sichtbar machen, wo relevant, mit Kürzeln: **[S]** Standard belegt · **[K]** Konfiguration · **[A]** Anpassung/Entwicklung (meist MDIS BeSync) · **[O]** offen/zu verifizieren. Für Katalogbewertungen die Legende des Livos-Katalogs verwenden (S/K/A/N).
4. **Keine erfundenen Fakten.** Beispielwerte (Freigabegrenzen, Fristen, Gesellschaftsnamen) immer als „Vorschlag" oder „Beispiel" kennzeichnen. Die Gesellschaften NORD/SUED/BAUP/WEST sind fiktive Demo-Gesellschaften – im Konzept nur als Beispiel verwenden.
5. **Quellen:** Im Konzept keine internen Dateipfade. Bei harten Produktaussagen kurze Quellenangabe in Fußnote/Klammer, z.B. „(d.velop invoices Leistungsbeschreibung 12/2025)", „(smart invoice Cloud Handbuch 06/2026)", „(Workshop 22.09.2026)". Eine Quellenliste kommt in den Anhang.
6. **Format:** Markdown. Überschriften `#`/`##`/`###` mit Kapitelnummer (z.B. `## 8.3 Verteilung und Klärfall`). Tabellen als Pipe-Tabellen. Keine HTML-Tags. Aufzählungen sparsam, lieber Tabellen für strukturierte Inhalte.
7. **Terminologie:** „d.velop" (nie „Develop"), „Livos", „smart invoice" (Workflow-Komponente von d.velop invoices), „d.velop invoices" (Produkt), „d.velop documents" (DMS), „Rechnungseingangsbuch (REB)", „BeSync" (MDIS-Middleware-Plattform), „Lieferanten-App" (MDIS-App auf BeSync für Lieferantenstamm), „LDconnect" (DATEV-Konnektor von LIONDEER, von d.velop als Option „DATEV Rechnungswesen" vertrieben), „multicash" (Zahlungsverkehrssoftware von Omikron), „BIM4You" (Bau-Budgetcontrolling, BIB GmbH), „Property Manager (PM)"/„Hausverwaltung (HV)", „Trios" (externer Buchhaltungsdienstleister von Livos, bucht in DATEV), „Mandant" = Gesellschaft.

---

## 1. Ausgangslage in Stichworten (belegt)

- LIVOS Gruppe: >100 Gesellschaften (Segmente Bestand, Privatisierung, Bau), ca. 80 Anwender intern + extern, 20–30 Rechnungen/Tag (5.000–8.000/Jahr). Katalog vom Juli 2026, 29 Anforderungen (21 Must, 4 Should, 4 Could).
- DATEV ist operatives FiBu-System; Buchung durch Dienstleister Trios; DATEV läuft bei externem Hoster (Zugriff über „Riecken Cloud Gateway" – im Workshop „ricken Cloud"; Annahme stark). Livos kann/will keine Kreditoren in DATEV anlegen.
- Kreditoren: gleiche Lieferanten in vielen Gesellschaften mit unterschiedlichen Nummern; interne Kreditoren 70000er-Kreis, HV-Kreditoren 80000er-Kreis; keine Konsolidierung.
- ~10 wechselnde Property Manager buchen, prüfen und zahlen ~95 % ihrer Rechnungen selbst; Rechnungen über Schwellwert brauchen Freigabe durch Livos Asset Management. PM dürfen nicht zu einem Erfassungssystem verpflichtet werden (K.-o.-Randbedingung).
- MDIS ist bei Livos bereits tätig: BeSync-Middleware, Lieferanten-/Stammdaten-App, BI-Projekt; BI-Werkzeug bei Livos: evidanza. KI-Plattform MDIS: X.One.
- Livos steht Middleware-Eigenbau skeptisch gegenüber („bei Middleware ein bisschen vorsichtig"; eigene Middleware-Tabellen pflegen „werden wir bestimmt nicht tun"). → **Designprinzip P3.**
- Livos vergleicht mehrere Anbieter; erwartet Angebot mit Katalogbezug für ~80 Nutzer; Entscheidung mit Management; Prozess-Workshop (2–3 h) wurde angeboten.
- MDIS-Zielarchitektur (Folien): d.velop zentral für Eingangsrechnungen, Verträge, Post; DATEV (ER-Journale, Zahlungsjournale, Sonderbuchungsinfos → DATEV; Zahlungsrückmeldung ←); BIM4You (ER-Journale →; Einbehalt-/Kürzungsinfos, Umlageinfos, Freigabestatus ←). ER-Kette: Eingang → Verarbeitung & Vorqualifikation → Verteilung (DATEV: ER-Vorerfassungsjournal) → Fachliche Prüfung/Detailqualifikation (Bau → BIM4You: Budgetabgleich, Bearbeitung) → Fachliche Freigabe (DATEV: Verbuchung) → Zahlungsfreigabe (DATEV: Zahlungsdurchführung). Verträge: Eingang → Verarbeitung → Verteilung → Klassifizierung → Fachliche Freigabe → Archivierung. Post: Eingang → Verarbeitung → Klassifizierung → Verteilung → Archivierung.

---

## 2. Designprinzipien

| ID | Prinzip | Konsequenz |
|---|---|---|
| P1 | **Ein Beleg, ein Schlüssel:** Die Gesellschaft (Mandant) ist auf jedem Dokument und jeder Akte Pflicht. | Rechte, Aktenbildung, Workflow-Routing, DATEV-Mandant, Export bei Gesellschaftsverkauf hängen daran. |
| P2 | **Standard vor Konfiguration vor Entwicklung.** | Erst d.velop-Standard (smart invoice, documents, contracts), dann Konfiguration, erst dann BeSync. |
| P3 | **BeSync nur, wo der Standard endet – klar abgegrenzt und von MDIS betrieben.** Livos pflegt keine technischen Middleware-Tabellen; fachliche Pflege nur in der Lieferanten-App (existiert bereits). | Jede BeSync-Leistung wird im Konzept als [A] mit Zweck, Auslöser, Betrieb ausgewiesen (Schnittstellenkatalog S-xx). |
| P4 | **Ein führendes System je Datenobjekt und je Prozessschritt.** | DATEV führt Kreditorenkonten & Buchungen; Lieferanten-App führt Lieferantenidentität (Konsolidierungsnummer); d.velop führt Beleg, Workflow, Freigabe, Archiv; BIM4You führt Bau-Budget/VOB/Einbehalte; multicash führt Zahlungsausführung. Keine Doppelübergabe nach DATEV. |
| P5 | **Das Original bleibt unverändert** (GoBD, § 146 Abs. 4 AO; E-Rechnung: XML ist Original). | Kürzungen, Korrekturen, Anmerkungen nur als Workflow-Daten/Annotation; keine „lokale Bearbeitung" von Rechnungen. |
| P6 | **Gesellschaftsunterschiede über Regeln, nicht über Kopien.** | Max. 100 Workflowdefinitionen je Bucket → Workflows je Prozesstyp; Gesellschaftslogik über Freigabematrix (Spalte Mandant), Bedingungen, Gruppen. |
| P7 | **Automatisierung mit Mensch im Loop.** | Jede Automatik hat Klärfall/Clearing und manuelle Übersteuerung mit Protokoll (Katalog 1.8). |
| P8 | **Schrittweise Einführung.** | Rechnungseingang zuerst (größter Hebel), dann PM-Freigabe, Bau/BIM4You, Verträge, Post. |

---

## 3. Architekturentscheidungen (AE) — Empfehlung MDIS

Status: **E** = empfohlen, von Livos zu bestätigen · **F** = fachlich gesetzt (folgt aus Anforderungen/Recht) · **O** = Entscheidung offen (Optionen im Konzept darstellen).

| ID | Entscheidung | Begründung (Beleg) | Status |
|---|---|---|---|
| AE-01 | **d.velop Cloud, Betriebsform C1 (Multi-Tenant AWS, Frankfurt)**, ein produktiver Tenant + ein Test-/Abnahme-Tenant. | Nur in C1: KI-Kontierungsvorschläge, KI-Klassifizierung/-Trennung Post, DATEV-Optionen (ReWe C1/H/O; DUO C1/H), unbegrenzte Funktionspostfächer. T Cloud (C2) hätte process studio in invoices inkl., aber nicht die KI-Funktionen. Betriebsform der Demo-Instanz ist unbekannt (OP). | E |
| AE-02 | **Editionen:** d.velop invoices Paket **Medium** (750 Rechnungen/Monat, 10 Buchhaltungsuser, Freigabeuser beliebig) + d.velop documents platform edition **business** für DMS-Vollnutzer (Verträge, Post, Akten, mobile App, Outlook, d.velop pilot, process studio, Teilen mit Externen) + Option **DATEV Rechnungswesen** (LDconnect) + **d.velop contracts** (lesend/voll) für Vertragsnutzer. | Leistungsbeschreibungen d.velop invoices 12/2025, platform edition, contracts-Preise. basic reicht nicht (kein SSO/OIDC, API, process studio, externes Teilen). Mengen je Rolle in Phase 0 festlegen. | E |
| AE-03 | **Ein Repository, ein smart-invoice-Bucket; jede Gesellschaft = ein smart-invoice-Mandant** (bis 1.000 je Bucket). Gesellschaftsschlüssel = **Mandanten-ID** in der vorhandenen DMS-Eigenschaft **„Mandant"** (+ „Mandantenname"); keine zweite Eigenschaft „Gesellschaft". **Mandanten-ID = DATEV-Mandantennummer** (Vorschlag, eindeutig und DATEV-kompatibel; Format mit Trios abstimmen, z.B. „Beraternr-Mandantennr"). | smart-invoice-Onboarding legt Mandant/Mandantenname als Pflichtzuordnung an; Restriction Sets, Aktenbildung, Freigabematrix und LDconnect arbeiten mandantenbezogen. Limits: 1.000 Mandanten, 100.000 Kreditoren, 50.000 Sachkonten je Bucket – bei >100 DATEV-Mandanten Limits beobachten (Kreditoren je Mandant angelegt!). | E |
| AE-04 | **Rechnungsworkflows in smart invoice** (nicht process studio). Workflowdefinitionen je Prozesstyp, nicht je Gesellschaft: WF-01 Standard-ER, WF-02 Bau-ER (mit BIM4You-Schritt), WF-03 PM-Freigabe (ohne Buchung), WF-04 Klärfall; Gutschrift/Storno als Pfad in WF-01. | Max. 100 Workflowdefinitionen, je max. 50 Schritte; Freigabematrix mit Spalte Mandant; Eskalation, Vertretung, REB im Standard. | E |
| AE-05 | **Gesellschaftsindividuelle Freigaben über die Freigabematrix** (Spalten: Mandant, Kostenstelle/Objekt, Betrag von/bis, Stufe, Freigeber-Gruppe). Wertgrenzen gelten je **Kostenobjekt**, nicht je Rechnung (belegtes Verhalten – bei Splitbelegen beachten). Zweite Freigabe ab Betrag X: **Wertgrenzen-Verbindung** (Bedingung auf `voucher.net_amount` in Cent) als Standardweg; das Vorschau-Feature „Vier-Augen ab Betrag" nur nach d.velop-Freigabe. **Prüfer ≠ Freigeber** ist Standard. | smart invoice Cloud Handbuch 06/2026; Demo (10.000 € netto = 1000000). Die Demo-Doku sprach von brutto – im Produktivkonzept **netto** (Standard-Bedingung), Livos bestätigt. | E |
| AE-06 | **Schrittmodell Standard-ER (WF-01):** Eingang/Erkennung → **Verteilung** (Mandant/Kreditor/Kostenobjekt prüfen, Klärfall) → **Sachliche Prüfung & Kontierung** → **Fachliche Freigabe** (Matrix, 1–n Stufen) → **Zahlungsfreigabe** → **Buchhaltung** (Trios: Kontrolle, Übergabe Buchungsvorschlag an DATEV) → Ende „Übergeben". Nachgelagert: Status „bezahlt" per BeSync (S-06). Klärfall-/Clearing-Schritte und „Zurückgewiesen" als Endpfad. | Livos-Zielbild (Folie 3) + smart-invoice-Standard (Verteilung/Prüfung/Freigabe/Buchhaltung) + LDconnect überträgt keine Zahlungssperre → **Zahlungsfreigabe muss vor der DATEV-Übergabe liegen.** | E |
| AE-07 | **DATEV-Anbindung über d.velop invoices Option „DATEV Rechnungswesen" (LDconnect, DATEVconnect) mit Riecken-Datengateway** (Pflicht bei DATEVasp/SmartIT/gehostetem DATEV). Übergabe **ereignisgesteuert** am Schritt Buchhaltung: Buchungsvorschlag (16 Felder) + **Beleglink** (Beleganzeige Drittanbieter); Stammdaten (Kreditoren, Sachkonten, Steuerschlüssel, Zahlungsbedingungen, Bankverbindungen, KOST1/KOST2) **täglich** aus DATEV in den Bucket. Belegbild in DATEV optional über DATEV Unternehmen online (Option DUO). | Katalog 5.1 („nicht nur 1× pro Tag") erfüllt; Erfüllungsgrad **K** (Drittanbieter-Option, DATEV-Komponenten und Gateway nötig, Beleg als Link). Kosten: LDconnect Enterprise 75 Mandanten inkl., jeder weitere 3,45 €/Monat (Liste); Beleganzeige Drittanbieter DATEV-seitig kostenpflichtig. | E |
| AE-08 | **Einstufige DATEV-Übergabe (nach Zahlungsfreigabe)** statt des zweistufigen Folienbilds (Vorerfassungsjournal bei Verteilung + Verbuchung nach Freigabe). Transparenz über offene/unverbuchte Rechnungen („Vorerfassungsjournal") liefert das **REB** (Status, Beträge, CSV-Export zum Monatsende, z.B. für Rückstellungen). Option Phase 3: frühe Übergabe als Buchungsvorschlag mit Postensperre über BeSync/EXTF [A]. | LDconnect-Standard kennt nur eine Übergabe je Rechnung; zweistufig ist nicht Standard. | O (mit Trios/Livos entscheiden) |
| AE-09 | **Kreditoren-/Lieferantenmodell mit drei Nummernkreisen:** (1) **Lieferanten-Konsolidierungsnummer** (Lieferanten-App, führend für Identität, gesellschaftsübergreifend), (2) **DATEV-Kreditorennummer je Mandant** (70000er intern, führend für Buchung), (3) **HV-Kreditorennummer** (80000er, aus PM-Buchhaltungen). Mapping in der Lieferanten-App (Schlüssel „DATEV-Mandantennr + Kreditorennr", Vorschlag Trios). **Schreibend in den smart-invoice-Bucket nur LDconnect** (DATEV-Stammdaten täglich); die Konsolidierungsnummer kommt als DMS-Eigenschaft an den Beleg (BeSync-Webhook oder dynamische Wertemenge). Neuer Kreditor: Klärfall „Kreditor fehlt" → Anlage-Anforderung aus der Lieferanten-App an Trios → DATEV-Anlage → Sync am Folgetag → Beleg läuft weiter. Initiale Konsolidierung per KI-Mapping (MDIS X.One, kostenloser PoC angeboten). | Pro Bucket nur ein schreibendes System (Konfliktvermeidung LDconnect vs. BeSync); Livos legt keine DATEV-Kreditoren an; Trios bucht. | E (Alternative „BeSync schreibt Bucket, LDconnect nur Buchung" als Option O) |
| AE-10 | **Zahlungsprozess:** Zahlungsfreigabe in d.velop → Buchungsvorschlag nach DATEV → Trios bucht (OPOS) → Zahlungsvorschlag in DATEV → SEPA-XML an **multicash (Omikron)** → Unterschrift/Ausführung durch berechtigte Nutzer in multicash (EBICS, Unterschriftsklassen) → Kontoauszug zurück nach DATEV → **BeSync liest OPOS (DATEVconnect accounts-payable) und setzt „Zahlstatus = bezahlt/Zahldatum" als DMS-Eigenschaft** am archivierten Beleg (smart-invoice-Belege sind nach Abschluss nicht per API änderbar; DMS-Eigenschaft ja). | smart invoice erzeugt keine SEPA-Datei; keine Zahlungsfreigabe-Übergabe an DATEV im Standard; Katalog 5.5 = **A** (über DATEV-Standard + multicash-Standard + BeSync-Rückmeldung). Der Workshop-Gedanke „beim Buchen geht die Zahlung raus" [00:33:28] ist so nicht empfohlen (Vier-Augen/Unterschrift in multicash bleibt). | E |
| AE-11 | **BIM4You-Integration für Bau-Rechnungen (WF-02):** Erkennung Bau (Kreditor-Kennzeichen „Bauleistender", Objekt = Bauprojekt, Belegart Abschlag/Schluss) → **asynchroner Transfer** an einer Schrittverbindung („Warten auf BIM4You", bis 28 Tage) → BeSync übergibt Kopfdaten + PDF/XML + Beleg-ID als Barcode/Referenz an BIM4You (E-Rechnungsimport/Austauschordner) → BIM4You: Budgetabgleich, kumulierte VOB-Prüfung, Einbehalte, Nachträge, Prüfer-Workflow → BeSync pollt Ergebnis → setzt DMS-Eigenschaften (geprüfter Betrag, Einbehalt, Freigabestatus BIM4You) + legt Prüfbericht/Zahlungsfreigabe-PDF ab → meldet Transfer `successful` → Beleg läuft zur fachlichen Freigabe/Zahlungsfreigabe in d.velop. **Zahlbetrag** im smart-invoice-Beleg setzt die Rechnungsprüfung auf Basis des BIM4You-Ergebnisses (kein API-Schreibzugriff auf laufende Belege belegt – bei d.velop anfragen). **Nur d.velop übergibt ER nach DATEV**; BIM4You-DATEV-Export für ER deaktiviert. Sonderbuchungsinfos (ARAP/PARP, Rückstellungen, Anzahlungen) aus BIM4You: Folgeprojekt/offen. | BIM4You (BIB GmbH) hat Rechnungseingangsbuch, Freigabemanager, E-Rechnungsimport, DATEV-Connector, aber keine veröffentlichte API; Referenz Krieger + Schramm (DocuWare+BIM4You+DATEV mit Eigenschnittstellen). | E (führendes System je Rechnungstyp: O mit Livos) |
| AE-12 | **PM-Freigabeprozess (WF-03) in smart invoice:** eigenes Postfach `freigabe-hv@…` (Alias) mit eigenem Importprofil; Schritte: Verteilung (Objekt/Gesellschaft/PM zuordnen) → Freigabe Asset Management (Freigabematrix) → Ende „Freigegeben"/„Abgelehnt"; **keine DATEV-Übergabe, keine Zahlung**; Rückmeldung an den PM per E-Mail über BeSync (Webhook an Endverbindung, Vorlage, Begründung) [A]. Monatliche DATEV-Buchungsdaten der PM (bestehendes Monatspaket) optional per BeSync in das BI für Vollständigkeits- und Kreditorenabgleich (80000er → Konsolidierungsnummer) [A, Phase 3]. Direkte PM-ERP-Anbindungen: Folgeprojekt (5.4). | Workshop-Vorschlag Thomas Groß [00:21:26–00:22:19], von Livos positiv aufgenommen („kleines On-Top", Transparenz, Vollständigkeit). PM nicht zu Systemnutzung verpflichtbar → E-Mail-Kanal. Rechnungen zählen ins invoices-Volumen. | E |
| AE-13 | **Rückweisung an Lieferanten:** smart-invoice-Aktion „Ablehnen" mit Pflicht-Rückweisungsgrund (Werteliste, 5 Standardgründe, Custom Entity) → Webhook → BeSync versendet Vorlagen-Mail an `vendor.email` (Kreditorenstamm) über Microsoft Graph, legt die gesendete Mail als Kategorie „Korrespondenz" in der Kreditorenakte ab [A, klein]. Dubletten werden ohne Lieferantenmail abgelehnt (Begründungspflicht bei Annahme). Übergangslösung: „Teilen per E-Mail/Link" manuell [S]. | smart invoice/process studio senden nicht an externe Adressen (belegt). | E |
| AE-14 | **Kürzungen:** Rechnung bleibt unverändert. Kürzung über **Zahlbetrag** (`pay_amount`, Kopf- oder Positionsebene; Menge/Preis je Position mit Neuberechnung) + Pflichtfeld **Kürzungsgrund** (Werteliste) + Notiz/Annotation; Protokoll über Aktivitäten/Belegänderungsansicht. Optional automatische Kürzungsmitteilung an den Lieferanten (Mechanik AE-13). E-Rechnung: formale Fehler → Rückweisung und Neuanforderung; Leistungskürzung → Zahlbetrag (Rechnung bleibt formal gültig). Verarbeitung des gekürzten Zahlbetrags in DATEV/Zahlungsvorschlag mit Trios klären (LDconnect überträgt Bruttobetrag; OP). | P5; smart invoice Handbuch (pay_amount, Positionen, Summenprüfung). Workshop-Aussage „Rechnung lokal bearbeiten" ist nicht GoBD-konform und wird im Konzept nicht übernommen. | E |
| AE-15 | **Freistellungsbescheinigung § 48b EStG:** FSB als Dokument (Kategorie „Bescheinigung") in der Kreditorenakte mit „Gültig bis"; FSB-Status-Tabelle in BeSync (Kreditor × Gesellschaft × gültig bis, Prüfnachweis EIBE-Abfrage) → Prüfung bei Belegeingang für Bau-Kreditoren per Export/Webhook → Hinweis/Klärfall „FSB fehlt/abgelaufen" mit Vorschlag Einbehalt 15 % (Zahlbetrag) [A]. BZSt-Prüfung selbst bleibt manuell (EIBE-Portal, keine API). Katalog 2.7 = **A** (Could). | Kein FSB-Feld im Kreditorenstamm; BZSt ohne API. | E (Phase 3) |
| AE-16 | **Reporting:** Operativ und für das Management im **REB** (Spalten „Aktueller Schritt", „Aktueller Schritt seit", „Zugewiesen", „Status"; Schnellzugriffe je Rolle/Gesellschaftsgruppe; Gruppierung; CSV-Export; Freigabe je Mandant). **Historische Durchlauf-/Liegezeiten je Benutzer/Schritt**: BeSync protokolliert jeden Schrittwechsel (Export-Events an Verbindungen) in eine MS-SQL-Staging-Schicht → **evidanza** [A]. Aufgabenhistorie der Plattform wird nur 30–365 Tage gehalten → laufend abziehen. | Katalog 3.2 = S (aktueller Stand) / A (Historie, BI). Workshop-Frage Christian Weigel [00:35:18]. | E |
| AE-17 | **Eskalation & Vertretung:** smart-invoice-Eskalation (statisch je Schritt, dynamisch vor Skonto-/Nettofälligkeit, 2 Stufen, Empfänger regelbasiert je Mandant; REB „An mich eskalierte Rechnungen") [S/K; Mailkanal testen]. Vertretung über Abwesenheit im Benutzerprofil; **Administrator/Vorgesetzte können Abwesenheit für erkrankte Kollegen setzen** und Aufgaben gesammelt weiterleiten [S]; Einschränkung: Vertreter sieht nur persönlich zugestellte Aufgaben → Aufgaben möglichst an Personen, Gruppenaufgaben mit mehreren Mitgliedern. Vertretungen möglichst innerhalb derselben Gesellschaftsgruppe (Rechte-Governance). | Katalog 3.3 S/K, 3.4 S/K. | E |
| AE-18 | **Berechtigungen (Cloud):** Permission je **Kategorie × Rechtestufe** (Lesen/Schreiben/Löschen getrennt, ALLOWED/INHERITED/DENIED, DENIED gewinnt); Gesellschaftsbezug über **Restriction Set** `RS_Mandant` (Gruppe → Mandanten-IDs), Objektbezug über `RS_Objekt`; Workflowbeteiligte lesen ihre Belege über `@CURRENT_USER`/`@CURRENT_USER_IN_GROUP`. Identitäten aus **Microsoft Entra ID per SCIM**, SSO per OIDC, flache Gruppen. Rollengruppen `DMS_R_*`, Gesellschaftsgruppen `DMS_G_<MandantNr>`, Verbundgruppen `DMS_GF_<Verbund>`, Objektgruppen `DMS_O_<ObjektID>`, smart-invoice-Gruppen `dv_*`/`SI_<Rolle>_<MandantNr>`. ~50–70 Permissions unabhängig von der Gesellschaftszahl; neue Gesellschaft = 1 Dataset-Wert + 1 Gruppe + 1 Set-Zuordnung + 1 smart-invoice-Mandant (per API automatisierbar, REB-Berechtigung ggf. manuell). Kritische Annahme: Restriction Set zieht Werte aus allen Gruppen des Benutzers (Test T03). | DmsConfig API (Cloud), Funktions-/Leistungsbeschreibung. | E (Tests OP) |
| AE-19 | **Aktenplan (max. 4 Ebenen):** Gesellschaftsakte (Mandant) → Objektakte (Objekt-ID) → Vorgangsakte (Auftrag/Vergabeeinheit bzw. Vertragsakte); Gesellschaftsakte → Kreditorenakte (Mandant + Kreditor-Nr); Dokumente per Aktenbildungsregel **mehrfach** verknüpft (z.B. Rechnung in Kreditorenakte und Objektakte). Gesellschaftsübergreifende Lieferantensicht über gespeicherte Suche nach Konsolidierungsnummer (keine eigene Akte). Mandant in jeder Erkennungskombination; Erkennungsfelder Pflicht (leere Felder → keine Aktenverknüpfung). Livos liefert die fachliche Ordnerstruktur. | Cloud-Aktenbildungsregeln belegt; Workshop-Empfehlung 4–5 Ebenen. | E |
| AE-20 | **Verträge:** **d.velop contracts** (Cloud, auf documents; Vertragsakte, Laufzeit-/Fristenberechnung, Fristenkalender, Vertragshierarchien, d.velop sign) für Vertragsverwaltung; **fachliche Vertragsfreigabe** über process studio (falls contracts keinen Standard-Freigabeworkflow bietet – OP) ; Alternative alphaflow Contracts. KI-Fragen an Verträge über **d.velop pilot** (ab business; Grenze 20.000 Token je Dokument im PoC testen). | Produktrecherche 13; Workshop-Frage [01:08:46]. | E (Phase 4) |
| AE-21 | **Post:** Eingangskanäle Papier (zentraler Scan mit inbound scan **oder** Scandienstleister per Postfach/API – OP), E-Mail-Funktionspostfächer; **KI-Trennung/-Klassifizierung** (C1, ab business; < 80 % → „Unbestimmt" → manuelle Klassifizierung); Verteilung mit **d.velop mail dispatcher** (Erstempfänger = Gruppe, Erinnerung/Eskalation) an Fachbereiche; Rechnungen werden in die ER-Strecke umgeleitet, Verträge in contracts; Ablage in Akten. Alternative: VLOTT Postverteilung. | Recherche 13/04b. | E (Phase 4) |
| AE-22 | **Eingangskanäle ER:** zentrale Rechnungsadresse `rechnung@…` (M365, Graph) **plus Alias je Gesellschaft** (Vorbelegung Mandant über Importprofil/Schlüssel-Wert-Paar – Test), Papier über Scan, E-Rechnung (ZUGFeRD 2.x, XRechnung 3.0, Factur-X) über dieselben Postfächer; Peppol nicht erforderlich. Neuer Kommunikationsweg **inbound → document reader → smart invoice** von Beginn an (alter Weg wird 01.01.2027 abgeschaltet). Voraussetzung M365 bei Livos (IMAP nicht verfügbar) – OP. | Recherche 12/04b. | E |
| AE-23 | **Mandantenerkennung (2.2):** Standard erkennt Empfänger über **Name + Anschrift** (keine USt-IdNr./StNr./Kundennr. am Mandanten). Maßnahmenbündel: (1) Lieferantenanschreiben: exakte Gesellschaftsbezeichnung + Käuferreferenz (BT-10) bei E-Rechnungen, (2) Alias-Postfach je Gesellschaft mit Vorbelegung, (3) Mandantenname in smart invoice exakt wie auf Rechnungen, (4) Klärfall-Mandant/Clearing je Mandant, (5) **Test mit echten Livos-Belegen** (Trefferquote messen) vor Go-live. Katalog 2.2 = **K** mit Vorbehalt. | Recherchen 11/12/15; Workshop-Aussage „das ist korrekt" [00:31:41] ist so nicht belegt. | F |
| AE-24 | **Aufbewahrung je Kategorie** (Cloud: Frist in Jahren/Monaten ab Datumseigenschaft „Aufbewahrungsbeginn", Löschsperre): Buchungsbelege/Eingangsrechnungen **8 Jahre** (BEG IV, ab 2025), Bücher/Organisationsunterlagen 10 Jahre, Handels-/Geschäftsbriefe 6 Jahre, Verträge Vertragsende + Frist; Ablaufhemmung § 147 Abs. 3 S. 5 AO beachten → **automatisches Löschen zunächst aus**, jährlicher freigegebener Löschlauf. Fristen final mit Steuerberatung. Legal Hold nicht dokumentiert (OP). | Recherche 13/15. | E |
| AE-25 | **Export je Gesellschaft (Verkauf, 1.6):** repo export-API (Originale aller Versionen + JSON-Metadaten inkl. Notizen, Verknüpfungen, Aktivitäten; Delta-fähig; Cloud-Freischaltung über Support) + BeSync-Exportskript (Dokument-IDs per Suche nach Mandant, 100er-Pakete) + Workflowprotokolle/Rechnungsdaten aus smart invoice. Voraussetzung P1. Katalog 1.6 = **S** (Revisionssicherheit/Protokoll) / **A** (Export-Paket je Gesellschaft). | Recherche 13. | E |
| AE-26 | **Externe:** Kernpartner (Projektsteuerer, Architekten, ggf. PM mit Konto) als **Freigabeuser** in d.velop invoices (beliebig viele, rollenbeschränkt, 2FA/FIDO2) – lizenzrechtliche Zulässigkeit für Dritte klären (OP); Ad-hoc-Externe (4.2) über process-studio **„Externe Benutzeraufgabe"** (E-Mail-Link auf Formular, Timer, kein Konto; Formular ohne Dokumentzugriff → Beleg als zeitlich begrenzter Teilen-Link, max. 180 Tage) – Kopplung an smart invoice über BeSync [A]. Katalog 4.3 = **S** (Vorbehalt), 4.2 = **K/A**. | Recherche 11. | E |
| AE-27 | **KI:** d.velop-Standard-KI für Erkennung (document reader), KI-Kontierungsvorschläge (Sachkonto/Kostenstelle auf Belegebene, lernend, nur C1), KI-Postklassifizierung, **d.velop pilot** für Fragen an Dokumente/Verträge. MDIS X.One für Kreditorenkonsolidierung (PoC) und übergreifende Analysen über BeSync-Daten. | Korrektur der Workshop-Aussage „nicht über d.velop direkt" [01:09:07] – d.velop pilot kann das. | E |
| AE-28 | **Stammdaten Gesellschaften/Objekte:** führend Lieferanten-App/BeSync-Stammdaten (Gesellschaftsstamm: Mandanten-ID, Name exakt, Anschrift, USt-IdNr., StNr., DATEV-Berater/Mandantennr., Segment, Bauleistender-Kennzeichen § 13b, Verwaltungsart Eigen-/PM-verwaltet, PM-Name, Freigabeverbund; Objektstamm: Objekt-ID global eindeutig, Bezeichnung, Mandant, Adresse, Verwaltungsart, Bauprojekt ja/nein, BIM4You-Projekt-ID) → per API in smart-invoice-Mandanten (Name/Anschrift) und DMS-Datasets/Wertemengen (Mandant, Objekt) und Restriction Sets. | P4; DmsConfig/smart-invoice-API. | E |
| AE-29 | **Ist-Demo nicht 1:1 übernehmen:** Demo-Struktur („Livos …"-Kategorien, doppelte Eigenschaften Kreditor/Rechnungsnummer/IBAN/Belegart/Netto/Brutto, Kostenstelle/Kostenstellen, Gesellschaft/Mandant) wird **nicht** in Produktion übernommen; Produktivmodell baut auf smart-invoice-Onboarding-Eigenschaften auf (eine Eigenschaft je Fachbegriff). | As-built-Befund 03. | F |

---

## 4. ID-Kataloge (verbindlich)

### 4.1 Rollen (R)

| ID | Rolle | Organisation | Aufgaben | Lizenztyp (Vorschlag) |
|---|---|---|---|---|
| R-01 | Poststelle / Scan | Livos Zentrale | Papierpost scannen, Stapel prüfen, Post-Klassifizierung nachbearbeiten | documents business |
| R-02 | Rechnungseingang / Verteilung (Kreditorenbuchhaltung Livos) | Livos Zentrale | Erfassung prüfen, Mandant/Kreditor/Kostenobjekt zuordnen, Klärfälle, Dubletten, Rückweisung | invoices Buchhaltungsuser |
| R-03 | Sachliche Prüfer (Asset Manager, Objektbetreuer, Projektleiter, Fachbereich) | Livos | sachliche/rechnerische Prüfung, Kontierung ergänzen, Kürzung vorschlagen | invoices Freigabeuser |
| R-04 | Freigeber (Abteilungsleitung, Gesellschaftsverantwortliche, GF) | Livos | fachliche Freigabe gemäß Matrix | invoices Freigabeuser (GF ggf. documents business für DMS/pilot) |
| R-05 | Zahlungsfreigeber | Livos (GF/kaufm. Leitung/Treasury) | Zahlungsfreigabe in d.velop; Unterschrift in multicash | invoices Freigabeuser + multicash |
| R-06 | Buchhaltung (Trios) | extern (Dienstleister) | Buchhaltungsschritt, DATEV-Übergabe, Kreditorenanlage in DATEV | invoices Buchhaltungsuser (Zulässigkeit extern: OP) |
| R-07 | Controlling / Management | Livos | REB-Sichten, Auswertungen, evidanza | documents business (lesend) / Freigabeuser |
| R-08 | Externe Kernpartner (Projektsteuerer, Architekten) | extern | Prüfung/Freigabe Bau-Rechnungen im Web | invoices Freigabeuser (OP Dritte) |
| R-09 | Property Manager (HV) | extern | reichen Freigabe-Rechnungen per E-Mail ein, erhalten Freigabe-Mail | keine Lizenz |
| R-10 | Ad-hoc-Externe | extern | Einzelfreigabe per externer Benutzeraufgabe | keine Lizenz |
| R-11 | Vertragsmanager / Vertragsverantwortliche | Livos | Verträge anlegen, Fristen, Vertragsfreigabe | contracts voll |
| R-12 | Fachadministration / Key-User | Livos | Stammdatenpflege (Lieferanten-App), Freigabematrix, Gruppen, Vertretung setzen | documents business + Admin |
| R-13 | Technischer Benutzer BeSync | MDIS | API-Zugriff (Stammdaten, Webhooks, Export) | technischer Benutzer |
| R-14 | Betriebsprüfer (Z1) | extern, temporär | Nur-Lese-Zugriff gefiltert auf Gesellschaft | documents (temporär) |
| R-15 | MDIS Betrieb/Support | MDIS | Tenant-Administration, Monitoring BeSync | Admin |

### 4.2 Kategorien (K) — Dokumentarten (D) und Aktenarten (A)

| ID | Kategorie | Typ | Zweck | Quelle/Erzeugung |
|---|---|---|---|---|
| K-01 | Eingangsrechnung | D | Rechnungen, Gutschriften, Abschlags-/Schlussrechnungen (Belegart) | smart-invoice-Onboarding-Kategorie wiederverwenden |
| K-02 | Rechnungsanlage / Nachweis | D | Lieferschein, Aufmaß, Abnahmeprotokoll, Stundenzettel | manuell/Post |
| K-03 | Auftrag / Bestellung | D | Auftrag, Auftragsbestätigung, Bestellung | Post/Upload |
| K-04 | Angebot | D | Angebote, Angebotsvergleich | Post/Upload |
| K-05 | Vertrag | D | Verträge, Nachträge, Kündigungen (in contracts) | d.velop contracts |
| K-06 | Bescheinigung | D | Freistellungsbescheinigung § 48b, Unbedenklichkeit, Versicherungsnachweise | Post/Upload |
| K-07 | Korrespondenz | D | Briefe, E-Mails, Rückweisungs-/Kürzungsmitteilungen, PM-Freigabemails | Post/Mail/BeSync |
| K-08 | BIM4You-Prüfbericht | D | Prüf-/Zahlungsfreigabebericht, Einbehaltsnachweis aus BIM4You | BeSync |
| K-09 | Sonstiges Posteingangsdokument | D | Behörden, Steuer, Versicherung, Mieterpost (Phase 4 feiner) | Post |
| K-10 | Gesellschaftsakte | A | alle Dokumente einer Gesellschaft | Aktenbildung |
| K-11 | Objektakte | A | Dokumente je Objekt/Bauvorhaben | Aktenbildung |
| K-12 | Kreditorenakte | A | Dokumente je Kreditor und Gesellschaft (inkl. FSB, Rahmenvertrag) | Aktenbildung (smart-invoice-„Kreditorenvorgangsakte" prüfen/ersetzen) |
| K-13 | Vorgangsakte (Auftrag/Vergabeeinheit) | A | Auftrag + Abschläge + Schlussrechnung + Nachweise | Aktenbildung über Auftragsnummer |
| K-14 | Vertragsakte | A | Vertrag + Nachträge + Korrespondenz | d.velop contracts |

### 4.3 Eigenschaften (E) — Kern

| ID | Eigenschaft | Typ | Wertemenge/Quelle | Pflicht in | Zweck |
|---|---|---|---|---|---|
| E-01 | Mandant (Mandanten-ID) | Text | Dataset Gesellschaften (BeSync) / smart invoice | **alle** | Rechte, Akten, Workflow, DATEV, Export |
| E-02 | Mandantenname | Text | aus Stamm | – | Anzeige/Titel |
| E-03 | Objekt-ID | Text | Dataset Objekte (global eindeutig) | K-01 (wenn objektbezogen), K-02–K-05, K-11, K-13 | Objektakte, PL-Rechte |
| E-04 | Objektbezeichnung | Text | aus Stamm | – | Anzeige |
| E-05 | Kreditor-Nr (DATEV) | Text | smart-invoice-Bucket (LDconnect) | K-01, K-06, K-12 | Kreditorenakte, Buchung |
| E-06 | Kreditorname | Text | Bucket | – | Anzeige |
| E-07 | Lieferanten-Konsolidierungsnummer | Text | Lieferanten-App (BeSync) | – | gesellschaftsübergreifende Lieferantensicht |
| E-08 | Rechnungsnummer | Text | Erkennung | K-01 | Dublettenprüfung, Suche |
| E-09 | Rechnungsdatum | Datum | Erkennung | K-01 | § 14 UStG |
| E-10 | Leistungsdatum/-zeitraum | Text/Datum | Erkennung | K-01 | § 14 UStG |
| E-11 | Nettobetrag / Steuerbetrag / Bruttobetrag | Währung | Erkennung | K-01 | Prüfung, Wertgrenzen |
| E-12 | Zahlbetrag | Währung | smart invoice (`pay_amount`) | K-01 | Kürzung/Einbehalt |
| E-13 | Kürzungsgrund | Text | Werteliste Kürzungsgründe | K-01 bei Zahlbetrag ≠ Brutto | Nachvollziehbarkeit |
| E-14 | Belegart | Text | Rechnung · Gutschrift · Abschlagsrechnung · Schlussrechnung · Stornorechnung | K-01 | Routing (Bau), VOB |
| E-15 | Fälligkeit netto / Skontofrist / Skontobetrag | Datum/Währung | Erkennung/Zahlungsbedingung Stamm | K-01 | Eskalation, Skonto-Ampel |
| E-16 | IBAN (Beleg) | Text | Erkennung, Abgleich mit Stamm | K-01 | Betrugsprävention |
| E-17 | Kostenstelle(n) / Sachkonto / KOST2 | Text | Bucket (DATEV) | K-01 (Positionen) | Kontierung |
| E-18 | Gewerk / Vergabeeinheit (Los) | Text | BIM4You-Stamm (Custom Entity) | K-01 Bau, K-03, K-13 | BIM4You-Zuordnung |
| E-19 | Auftragsnummer / Vertragsnummer | Text | Erkennung/Stamm | K-03, K-13 (K-01 bei Bau) | Vorgangsakte, VOB-Kumulation |
| E-20 | Reverse Charge § 13b | Text | Wertemenge Ja/Nein (kein Boolean-Typ) | K-01 | Steuerschlüssel |
| E-21 | FSB gültig bis / FSB-Status | Datum/Text | Bescheinigung/BeSync | K-06 / K-01 Bau | § 48b |
| E-22 | Sicherheitseinbehalt / geprüfter Betrag BIM4You / Freigabestatus BIM4You | Währung/Text | BeSync (BIM4You) | K-01 Bau | Transparenz Bau |
| E-23 | Zahlstatus / Zahldatum | Text/Datum | BeSync (DATEV OPOS) | – | „bezahlt" |
| E-24 | Workflowstatus / aktueller Schritt | Text | smart invoice | – | Status (kein eigenes Statusfeld anlegen) |
| E-25 | Eingangskanal | Text | E-Mail · Scan · E-Rechnung · Upload · PM-Freigabe | K-01, K-09 | Auswertung |
| E-26 | Rückweisungsgrund | Text | Werteliste (5 Standardgründe) | bei Ablehnung | Lieferantenmail |
| E-27 | Dokumentdatum / Betreff / Absender | Datum/Text | Erkennung/manuell | K-02–K-09 | Suche |
| E-28 | Vertragsdaten (Partner, Beginn, Ende, Kündigungsfrist, Verlängerung, Vertragswert) | div. | d.velop contracts | K-05, K-14 | Fristen |
| E-29 | Aufbewahrungsbeginn | Datum | berechnet (31.12. des Belegjahres) | alle aufbewahrungspflichtigen | Retention |
| E-30 | Verwaltungsart / Property Manager | Text | Objektstamm | K-01 (WF-03), K-11 | PM-Prozess |
| E-31 | Segment | Text | Bestand · Privatisierung · Bau | – (aus Gesellschaftsstamm) | Auswertung, Matrix |
| E-32 | Workflowbeteiligte (IDs) | Text, mehrfach | smart invoice | – | Leserecht Beteiligte |

**Standard-Rückweisungsgründe (Vorschlag, von Livos zu bestätigen):** (1) Pflichtangaben § 14 UStG fehlen/fehlerhaft, (2) falscher Rechnungsempfänger/Gesellschaft, (3) Leistung nicht/nicht vollständig erbracht bzw. Nachweise fehlen, (4) Preis/Menge weicht von Auftrag/Vertrag ab, (5) formaler E-Rechnungsfehler/Format nicht verarbeitbar. Dubletten: interne Ablehnung ohne Lieferantenmail.
**Kürzungsgründe (Vorschlag):** Mengenabweichung · Preisabweichung · Mangel/Minderung · Einbehalt (Sicherheit/Gewährleistung) · Bauabzug 15 % (§ 48) · Skonto-/Nachlassdifferenz · Sonstiges (Freitext Pflicht).

### 4.4 Workflows / Prozesse (WF)

| ID | Prozess | Werkzeug | Phase |
|---|---|---|---|
| WF-01 | Standard-Eingangsrechnung (Verteilung → Sachliche Prüfung & Kontierung → Fachliche Freigabe 1..n → Zahlungsfreigabe → Buchhaltung/DATEV) | smart invoice | 1 |
| WF-02 | Bau-Eingangsrechnung (wie WF-01 + asynchroner BIM4You-Schritt nach Sachlicher Prüfung) | smart invoice + BeSync | 3 (Pilot-Bau in Phase 1 ohne BIM4You-Automatik möglich) |
| WF-03 | PM-Freigabe (Freigabe ohne Buchung/Zahlung, Rückmeldung per E-Mail) | smart invoice + BeSync | 2 |
| WF-04 | Klärfall Mandant/Kreditor unbekannt (Clearing je Mandant; Klärfall-Mandant; Kreditor-Anlage via Lieferanten-App/Trios) | smart invoice (+ Lieferanten-App) | 1 |
| WF-05 | Rückweisung/Kürzungsmitteilung an Lieferanten | smart invoice + BeSync | 2 |
| WF-06 | Vertragsprozess (Eingang → Verarbeitung → Verteilung → Klassifizierung → Fachliche Freigabe → Archivierung; Fristenüberwachung) | d.velop contracts + process studio | 4 |
| WF-07 | Postverteilung (Eingang → Verarbeitung → Klassifizierung → Verteilung → Archivierung) | inbound + KI-Klassifizierung + mail dispatcher | 4 |
| WF-08 | Ad-hoc-Aufgaben / Wiedervorlagen am Dokument | d.velop documents (Aufgaben) | 1 |
| WF-09 | Weitere Freigaben ohne Rechnung (z.B. Ausbuchungen auf Mietkonten) — Ausblick | process studio | 5 |
| WF-10 | Externe Ad-hoc-Freigabe (externe Benutzeraufgabe) | process studio + BeSync | 3 |

### 4.5 Schnittstellen (S)

| ID | Schnittstelle | Richtung | Technik | Auslöser | Status |
|---|---|---|---|---|---|
| S-01 | DATEV Buchungsvorschlag + Beleglink | d.velop → DATEV | Option DATEV Rechnungswesen (LDconnect, DATEVconnect, Riecken-Gateway) | Schritt Buchhaltung (ereignisgesteuert) | K |
| S-02 | DATEV-Stammdaten (Kreditoren, Sachkonten, Steuerschlüssel, Zahlungsbedingungen, Bankverbindungen, KOST1/2) | DATEV → smart invoice | LDconnect | täglich | K |
| S-03 | Belegbilder nach DATEV Unternehmen online (optional) | d.velop → DUO | Option DUO | Übergabe | K (optional) |
| S-04 | Lieferanten-App ↔ d.velop (Konsolidierungsnr., Gesellschafts-/Objektstamm, Datasets, Restriction Sets, smart-invoice-Mandanten) | BeSync ↔ d.velop | smart-invoice-Stammdaten-API, DmsConfig/DMS-API | nächtlich + bei Änderung | A |
| S-05 | Lieferanten-App ↔ DATEV (Kreditor-Mapping, Anlage-Anforderung an Trios) | BeSync ↔ DATEV/Trios | DATEVconnect lesen + Workflow/Mail an Trios | bei Neuanlage | A |
| S-06 | Zahlstatus „bezahlt" (OPOS) | DATEV → BeSync → d.velop | DATEVconnect accounts-payable → DMS-API | täglich | A |
| S-07 | Zahlungsdatei SEPA → multicash | DATEV → multicash | DATEV-Zahlungsverkehr/SEPA-XML, multicash-Import (Standard beider Hersteller) | Zahllauf | S (außerhalb d.velop) |
| S-08 | BIM4You Hinweg (Bau-Rechnung) | d.velop → BeSync → BIM4You | smart-invoice-Transfer (asynchron) → E-Rechnungsimport/Austauschordner | Schrittverbindung „Bauprüfung" | A |
| S-09 | BIM4You Rückweg (Prüfergebnis, Einbehalte, Freigabestatus, Prüfbericht) | BIM4You → BeSync → d.velop | Export/Polling → DMS-API + Transfer-Rückmeldung | Freigabe/Storno in BIM4You | A |
| S-10 | BIM4You-Stammdaten (Projekte, Vergabeeinheiten, Verträge) | BIM4You → smart invoice | Custom Entities / Stammdaten-API | nächtlich | A |
| S-11 | Rückweisungs-/Kürzungs-/PM-Rückmelde-Mail | d.velop → BeSync → Lieferant/PM | Webhook an Verbindung → Microsoft Graph | Ablehnen/Endverbindung | A |
| S-12 | Prozessereignisse → evidanza | d.velop → BeSync → MS SQL → evidanza | Export-Events je Schrittwechsel + nächtliche API-Abfrage | Schrittwechsel | A |
| S-13 | Identitäten (Benutzer, Gruppen) | Entra ID → d.velop | SCIM 2.0, OIDC | laufend | S/K |
| S-14 | E-Mail-Eingang (Rechnungen, PM-Freigabe, Post) | M365 → d.velop | email import (Graph) / inbound e-mail | laufend | S |
| S-15 | Export je Gesellschaft | d.velop → Archivpaket | repo export-API + BeSync-Skript | Anlass (Verkauf, Prüfung) | A |
| S-16 | PM-Buchungsdaten (monatlich) → BI | PM → BeSync → BI | Upload/Postfach, Parser | monatlich | A (Phase 3, optional) |
| S-17 | ERP/PM-Stammdatensync (perspektivisch) | bidirektional | d.velop REST-API | Folgeprojekt | A (5.4) |

### 4.6 Masken / Oberflächen (M) — für Kapitel 11 und draw.io

| ID | Maske | Rolle | Werkzeug |
|---|---|---|---|
| M-01 | Rechnung einlesen / Stapel (Upload, Erkennung, Stapelübersicht) | R-02 | d.velop invoices |
| M-02 | Verteilung (Belegmaske links, Beleg rechts; Mandant, Kreditor, Kostenobjekt, Sachl. Prüfer, Dublettenhinweis, IBAN-/Zahlungsbedingungs-Hinweis) | R-02 | smart invoice |
| M-03 | Sachliche Prüfung & Kontierung (Positionen, Kostenstellen-Split, Zahlbetrag, Kürzungsgrund, Nachweise anhängen) | R-03 | smart invoice |
| M-04 | Fachliche Freigabe / Zahlungsfreigabe (Freigabe, Ablehnen mit Grund, Rückfrage, Historie) | R-04, R-05 | smart invoice |
| M-05 | Klärfall (Mandant unbekannt / Kreditor fehlt / Dublette) | R-02 | smart invoice |
| M-06 | Rückweisungsdialog (Grund, Vorlage-Vorschau, Empfänger aus Kreditorenstamm) | R-02/R-03 | smart invoice + BeSync |
| M-07 | Buchhaltung (Kontrolle, Übergabe DATEV, Buchungsvorschau) | R-06 | smart invoice |
| M-08 | Rechnungseingangsbuch – Arbeitsansicht (Meine Aufgaben, Schnellzugriffe) | alle | REB |
| M-09 | Rechnungseingangsbuch – Managementsicht (Status, Zugewiesen, Aktueller Schritt seit, Gruppierung Gesellschaft, Export) | R-07 | REB |
| M-10 | Startseite/Dashboard je Rolle (Widgets: Meine Aufgaben, REB-Schnellzugriffe, Suche, Zuletzt bearbeitet, Favoriten) | alle | d.velop documents |
| M-11 | Aktenansicht Kreditorenakte / Objektakte (Mehrfachablage, Akteninhalt) | alle | d.velop documents |
| M-12 | Suche / gespeicherte Suchen (Kategorie + Eigenschaften, Konsolidierungsnummer) | alle | d.velop documents |
| M-13 | PM-Freigabe (Freigabe-Maske mit Objekt/PM/Schwellwert, Rückmeldetext) | R-04 | smart invoice |
| M-14 | Vertragsmaske (Stammdaten, Fristen, Verlängerung, Vertragsakte) | R-11 | d.velop contracts |
| M-15 | Postverteilung (Klassifizierung, Empfängergruppe, Weiterleitung) | R-01 | mail dispatcher |
| M-16 | Lieferanten-App (Lieferant, Konsolidierungsnr., Kreditor-Mapping je Mandant, FSB-Status, Anlage-Anforderung) | R-12 | BeSync-App |
| M-17 | Freigabematrix-Pflege (Administration) | R-12 | smart invoice Administration |
| M-18 | Vertretung / Abwesenheit (auch durch Admin für Dritte) | alle/R-12 | Benutzerprofil |
| M-19 | Externe Benutzeraufgabe (Formular für Ad-hoc-Externe) | R-10 | process studio forms |

---

## 5. Neue Bewertung Leistungskatalog (verbindlich)

Legende Katalog: S Standard · K Konfiguration · A Anpassung · N Nein. „MDIS alt" = in Spalte F eingetragene Bewertung vor dem Workshop.

| Nr. | Anforderung | Prio | MDIS alt | **Neu** | Kurzbegründung / Lösung |
|---|---|---|---|---|---|
| 1.1 | Echte Mandantenfähigkeit (>100 Ges.) | Must | K | **K** | 1 Tenant, Mandant je Gesellschaft (≤1.000/Bucket), Restriction Sets, Freigabematrix-Spalte Mandant, Clearing je Mandant (AE-03/18) |
| 1.2 | Webbasiert/Cloud | Must | S | **S** | Browser, responsiv, Cloud C1 |
| 1.3 | App | Could | S | **S** | d.velop mobile iOS/Android ab Edition business |
| 1.4 | Individuelle Workflows je Gesellschaft, Grenzen, Personenketten | Must | S | **K** | Freigabematrix je Mandant/Kostenobjekt + Wertgrenzen-Verbindungen; kein eigener Workflow je Gesellschaft (Limit 100); Vier-Augen ab Betrag X als Vorschau-Feature → Standard-Workaround (AE-05) |
| 1.5 | Rollen & Rechte intern/extern | Must | S | **K** | Standardmechanik, Livos-Modell per Konfiguration (AE-18) |
| 1.6 | Revisionssicherheit & GoBD, Export je Gesellschaft | Must | S | **S / A** | Protokoll, Versionierung, Aufbewahrung S; Exportpaket je Gesellschaft A (AE-25); PS-880-Testat Cloud anfordern |
| 1.7 | Ablage weiterer Nachweise | Should | S | **S** | Anlagen, Akten, Mehrfachablage |
| 1.8 | Händische Übersteuerung | Must | S | **S** | Werte/Kontierung/Workflow übersteuerbar mit Protokoll; Kürzung als Zahlbetrag (AE-14) |
| 2.1 | Automatischer Postfach-Import, Sammelpostfach | Must | S | **S** | email import (M365 Graph), Alias je Gesellschaft; Voraussetzung M365 |
| 2.2 | KI-Erkennung & Mandantenzuordnung | Must | S | **K** | Pflichtangaben S; Mandantenzuordnung nur Name+Anschrift → Maßnahmenbündel + Test (AE-23) |
| 2.3 | Unbekannte Gesellschaft → Prozess | Must | K | **K** | Clearing/Klärfall-Mandant (WF-04) |
| 2.4 | E-Rechnung ZUGFeRD/XRechnung + Visualisierung | Must | S | **S** | ZUGFeRD 2.x, XRechnung 3.0, Factur-X; Validierung nur XRechnung (ZUGFeRD-Profilprüfung A) |
| 2.5 | Lernende Kontierungsvorschläge | Must | S | **S** | KI-Kontierung Sachkonto/Kostenstelle auf Belegebene (C1); Projekt/Position K; kreditorenabhängige Vorlagen |
| 2.6 | Automatische steuerliche Prüfung + weitere Kriterien | Must | S | **S / A** | § 14-Grundprüfung, Dubletten, XRechnung-Validierung S; FSB-Kriterium A (AE-15) |
| 2.7 | Freistellungsbescheinigung automatisch, 15 % Abzug | Could | N | **A** | BeSync-FSB-Status + Hinweis/Vorschlag Zahlbetrag (AE-15) |
| 2.8 | Kostenstellen-Aufteilung + Standardschlüssel je Gesellschaft | Must | S | **S / K** | Split S; Standardschlüssel über Kontierungsvorlagen K (%-Logik testen) |
| 3.1 | Persönliches Dashboard/Inbox | Must | S | **S** | Aufgabenliste, REB-Schnellzugriffe, Startseite |
| 3.2 | Management-/Controlling-Dashboard (Status, Bearbeiter, Liegezeit) | Must | S | **S / A** | REB-Spalten + Export S; historische Durchlaufzeiten/BI A (AE-16) |
| 3.3 | Automatisches Eskalationsmanagement | Must | S | **S / K** | Eskalation je Schritt/Fälligkeit, 2 Stufen, Empfänger je Mandant; Mailkanal testen |
| 3.4 | Vertretungsregelungen | Must | K | **S / K** | Abwesenheit, Admin setzt für Dritte; Gruppenaufgaben-Einschränkung |
| 4.1 | Prozessunabhängigkeit Property Manager | Must | N | **K / A** | PM-Freigabeprozess WF-03 (K), Rückmeldemail + optional PM-Datenübernahme (A) |
| 4.2 | Ad-hoc-Freigabe per Mail/Link ohne Lizenz | Should | – | **K / A** | externe Benutzeraufgabe (process studio) + Teilen-Link; Kopplung an smart invoice A |
| 4.3 | Web-Zugang für Kern-Partner | Must | S | **S** | Freigabeuser beliebig (Vorbehalt Zulässigkeit Dritte) |
| 5.1 | DATEV-Schnittstelle, mehrfach täglich inkl. Beleg | Must | S | **K** | LDconnect ereignisgesteuert, Beleglink; Stammdaten täglich (AE-07) |
| 5.2 | Bau-Spezifika VOB & Einbehalte | Should | N | **N (d.velop) / A (über BIM4You)** | Kennzeichnung/Transparenz in d.velop K; Rechenlogik in BIM4You (AE-11) |
| 5.3 | Schnittstelle BIM4You | Should | – | **A** | BeSync, asynchroner Transfer, datei-/importbasiert (AE-11) |
| 5.4 | Perspektivische ERP-/PM-Anbindung | Could | – | **S / A** | offene REST-APIs S; konkrete Synchronisation Folgeprojekt A |
| 5.5 | Schnittstelle Zahlungsmanagement Omikron | Must | – | **A** | DATEV-Zahlungsvorschlag → multicash (Standard) + BeSync-Rückmeldung (AE-10) |
| 6.1 | DMS-Nutzung | Could | S | **S** | d.velop documents, contracts, Post |

Zählung neu: S 11 · S/A bzw. S/K 8 · K 7 · K/A 2 · A 3 · N/A 1 (Autoren: Zählung im Text selbst nachrechnen, nicht diese Zeile übernehmen).

---

## 6. Offene Punkte / Tests (Auswahl, verbindliche IDs)

| ID | Thema | Klärung mit | Prio |
|---|---|---|---|
| OP-01 | Betriebsform der Zielumgebung (C1 AWS) und der Demo-Instanz | d.velop | P1 |
| OP-02 | Mandantenerkennung: Test mit echten Livos-Belegen (gleiche Anschriften), Alias-Vorbelegung, BT-10 | Livos, Test | P1 |
| OP-03 | Lizenzrecht: Dritte (Trios, Projektsteuerer, PM) als Buchhaltungs-/Freigabeuser zulässig? Mischlizenz invoices/platform edition | d.velop | P1 |
| OP-04 | DATEV-Betrieb: wer betreibt/lizenziert DATEV (Livos/Trios/Hoster), Riecken-Gateway, DATEVconnect, Beleganzeige Drittanbieter, Preis Option DATEV + LDconnect >75 Mandanten | Trios, Hoster, d.velop, LIONDEER | P1 |
| OP-05 | DATEV-Übergabe ein- vs. zweistufig; Verarbeitung Zahlbetrag/Kürzung in DATEV/Zahlungsvorschlag | Trios | P1 |
| OP-06 | Führendes System je Rechnungstyp Bau (d.velop vs. BIM4You → DATEV); BIM4You-Import (PDF/ZUGFeRD), Export Prüfergebnis | Livos, BIB GmbH | P1 |
| OP-07 | Schreibzugriff auf laufende smart-invoice-Belege per API (Zahlbetrag nach BIM4You) | d.velop | P2 |
| OP-08 | Restriction Set über alle Gruppen (T03), Aktenbildung Mehrfachregel (T13), Verhalten leere Erkennungsfelder | Test-Tenant | P1 |
| OP-09 | Vier-Augen-Vorschau-Feature: Status/GA | d.velop | P2 |
| OP-10 | Eskalations-Mailkanal, IBAN-Abweichungswarnung, Zahlbetrag-Feld in Maske schaltbar, Kontierungsvorlagen mit %-Schlüssel | Test | P2 |
| OP-11 | process-studio-Kontingent (1.000 Ausführungen/Monat in business) – zählt smart invoice mit? | d.velop | P2 |
| OP-12 | d.velop contracts: Standard-Freigabeworkflow? Handbuch; alternativ alphaflow | d.velop | P3 |
| OP-13 | Post: Scan intern vs. Dienstleister; mail dispatcher Cloud-Lizenz | Livos, d.velop | P3 |
| OP-14 | IDW PS 880 / C5 für Cloud, Verfahrensdokumentation | d.velop | P2 |
| OP-15 | Legal Hold / Ablaufhemmung technisch | d.velop | P3 |
| OP-16 | Livos: M365 als Mailsystem? Entra ID? | Livos | P1 |
| OP-17 | Livos: Aktenstruktur/Folder Structure, Freigabegrenzen, Rollenbesetzung, Rückweisungs-/Kürzungsgründe, Scope PM-Freigabe | Livos (Prozess-Workshop) | P1 |
| OP-18 | Umlageinformationen aus BIM4You: Bedeutung/Format | Livos | P3 |
| OP-19 | d.velop pilot: Tokengrenze bei langen Verträgen, LLM-Region/AVV | d.velop | P3 |
| OP-20 | Test-Tenant-Lizenzierung | d.velop | P2 |

---

## 7. Konzept-Gliederung (Zielbild Dokument 2) und Autorenzuteilung

1. Dokumentinformationen & Lesehilfe (Zweck, Status, Legende) — Autor A
2. Management Summary (1–2 Seiten) — Lead (am Ende)
3. Ausgangslage und Zielsetzung (Unternehmen, Mengengerüst, Ist-Prozess & Systeme, Schmerzpunkte, Ziele, Scope/Nicht-Scope) — Autor A
4. Anforderungen und Abdeckung (Katalogbewertung neu inkl. Begründung; Zusatzanforderungen aus Workshop T-xx mit Lösung) — Autor A
5. Lösungsarchitektur (Systemlandschaft, d.velop-Bausteine, Betriebsform, Lizenzarchitektur ohne Preise, Designprinzipien, Architekturentscheidungen AE) — Autor B
6. Mandanten- und Organisationsmodell — Autor B
7. Informationsmodell (Kategorien, Eigenschaften, Wertemengen, Aktenplan, Aufbewahrung, Namenskonventionen) — Autor B
8. Stammdatenkonzept (Gesellschaften, Objekte, Lieferanten/Kreditoren mit 3 Nummernkreisen, Sachkonten/KST, BIM4You-Stamm, FSB) — Autor B
9. Prozesskonzept Eingangsrechnung (WF-01, WF-02, WF-04, WF-05 inkl. Sonderfälle: Dublette, Kürzung, Rückweisung, Abschlag/Schluss, § 13b, § 48b, Gutschrift, E-Rechnung-Korrektur, IBAN-Abweichung, Skonto) — Autor C
10. Freigabe- und Workflowkonzept (Freigabematrix, Wertgrenzen, Vier-Augen, Eskalation, Vertretung, Benachrichtigung, Statusmodell) — Autor C
11. Prozess Property-Manager-Freigabe (WF-03) und weitere Freigaben (WF-09, WF-10) — Autor C
12. Prozesskonzept Verträge (WF-06) und Posteingang (WF-07), DMS-Nutzung allgemein (Ablage, Suche, Aufgaben, Outlook, mobile, pilot) — Autor D
13. Rollen- und Berechtigungskonzept — Autor D
14. Masken- und Oberflächenkonzept (M-01…M-19: Zweck, Felder, Aktionen, Regeln) — Autor D
15. Schnittstellenkonzept (S-01…S-17 im Detail, Betriebsaspekte BeSync, Fehlerhandling) — Autor E
16. Reporting und Controlling (REB-Sichten, KPI-Katalog, evidanza) — Autor E
17. Compliance: GoBD, Aufbewahrung, Verfahrensdokumentation, E-Rechnung, Datenschutz/Sicherheit, Betriebsprüfung, Export je Gesellschaft — Autor E
18. Betrieb, Organisation, Change & Schulung — Autor E
19. Einführungsvorgehen und Roadmap (Phasen 0–5, Pilotgesellschaften, Migration, Test, Go-live, Hypercare) — Autor F
20. Risiken, Entscheidungsbedarfe, offene Punkte, Testplan — Autor F
21. Anhang: Glossar, Quellenverzeichnis, Workshop-Anforderungsliste T-01…T-46 mit Lösungsverweis — Autor F

Jedes Kapitel als eigene Datei SP/work/konzept/Kxx_<name>.md (xx = Kapitelnummer zweistellig).
