# 04b — d.velop-Fähigkeitsmatrix (Teil B): Eingangsrechnungen, Workflows, Postverteilung

**Projekt:** Livos d.velop DMS-Gesamtkonzept (MDIS Consulting)
**Stand:** 26.09.2026
**Grundlage:** allgemeine d.velop-Recherche aus der öffentlichen Doku (help.d-velop.de, Recherchestand 18.09.2026), ausgewertet aus drei Dateien:

| Kürzel | Datei | Inhalt |
|---|---|---|
| **B_02** | SP/txt/B_02_Eingangsrechnungen_smart_invoice.md | d.velop invoices / smart invoice / document reader / eInvoice converter / alphaflow (§1–§10, „Offene Punkte", „Kurzfazit") |
| **B_04** | SP/txt/B_04_Workflows_process_studio.md | d.velop process studio (BPMN), d.3 flow, d.ecs task, d.ecs userprofile (§0–§10, „Offene Punkte", „Aufwandseinschätzung") |
| **B_06** | SP/txt/B_06_Postverteilung_Mailimport.md | d.velop mail dispatcher, inbound suite/scan, email import, inbound e-mail, OCR, eInvoice converter, Vertretung (§1–§10, „Offene Punkte") |

**URL-Kürzel für Handbuchverweise** (alle Präfix `https://help.d-velop.de/docs/de/pub/`, sofern nicht anders angegeben):

| Kürzel | Handbuch / Pfad |
|---|---|
| SI: | `smart-invoice-cloud/cloud/konfigurieren-von-dvelop-smart-invoice/…` (d.velop smart invoice Cloud: Administrieren) |
| SIB: | `smart-invoice-cloud/cloud/basisinformationen-zur-anwendung/…` |
| SID: | `smart-invoice-developer/cloud/…` (d.velop smart invoice API) |
| REB | `https://help.d-velop.de/docs/api/documentations/de/invoice-monitor/cloud/pdf` (d.velop invoices – Rechnungseingangsbuch: Anwenden) |
| DR: | `document-reader/latest/konfigurieren/…` (d.velop document reader: Administrieren) |
| EIC: | `einvoice-converter/latest/…` bzw. `einvoice-converter/cloud/…` (d.velop eInvoice converter: Administrieren) |
| IEM: | `inbound-e-mail/latest/…` bzw. `/cloud/…` (d.velop inbound e-mail: Administrieren) |
| EMI: | `email-import/cloud/…` (d.velop email import: Administrieren) |
| ISA: / ISU: | `inbound-scan-admin-cloud/cloud/…` / `inbound-scan-user-cloud/cloud/…` |
| MDA: / MDU: | `mail-dispatcher-admin/cloud/…` / `mail-dispatcher-user/cloud/…` |
| DIH | `document-intelligence-hub/cloud` |
| PSU: | `process-studio-user/2026.q3/…` (d.velop process studio: Anwenden) |
| PSA: | `process-studio-admin/2025.q1/…` |
| PA: | `process-admin/1.11.0/…` (Administrationshandbuch d.velop process, On-Premises) |
| TU: / TA: | `task-user/2.18.0/…` / `task-admin/2.18.0/…` (d.ecs task) |
| UP: | `userprofile/1.9.0/…` (d.ecs userprofile) |
| ONE: | `one-documents/2026.q3/…` |
| AF: | `alphaflow-eingangsrechnungen/9/…` |
| HC | Helpcenter `https://help.d-velop.de/invoices/de/articles/…` |

**Status-Legende in den Matrizen**
- **B** = Fakt, belegt (öffentliche Doku, in der Quelldatei wörtlich zitiert)
- **E** = belegt, aber mit Einschränkung (Vorschau-Feature, Doku-Widerspruch, nur On-Prem-Beleg, nur Beispiel)
- **N** = in der Recherche ausdrücklich **nicht gefunden** / nicht dokumentiert
- **A** = **Annahme** bzw. MDIS-Ableitung (nicht belegt, zu verifizieren)

**Grundsätzlicher Vorbehalt:** Mehrere für Livos zentrale Handbücher sind **nicht öffentlich** (Login `login.d-velop.de`): `document-reader-invoice`, `connect-datev-admin`/`-user`, `invoice-processing-admin`/`-user` (ecspand), `flow-designer`, `flow-inspector`, `rendition-service`, `smart-inbox-admin`/`-user`, `inbound-scan-admin-on-premises`, `mobile-android-admin`, `webindex-designer`. [B_02 Vorbemerkung; B_04 §0; B_06 §9a, Offene Punkte 4]

---

## 0. Einordnung: Produktbausteine und Abbildung auf den Livos-Zielprozess

### 0.1 Produktbausteine (Fakt)

| Baustein | Rolle laut Doku | Quelle |
|---|---|---|
| **d.velop invoices** | „Lösung für die digitale Verarbeitung eingehender Rechnungen auf der d.velop platform"; eigenständiges Produkt, Cloud und On-Premises | [B_02 §1A; HC „Was ist d.velop invoices?"] |
| d.velop inbound | Rechnungs-/Posteingang (Mail, Scan, Dateiimport), Stapelbildung | [B_02 §1A; B_06 §3] |
| d.velop document reader (Ausprägung invoice) | Auslesen und Klassifizieren (OCR), Mandanten-/Lieferantenerkennung, Dokumentprüfung | [B_02 §1A, §3, §4] |
| **d.velop smart invoice** | „zentrale Komponente zur (automatischen) Prüfung und Freigabe von Eingangsrechnungen" – eigener Workflow-Editor (Schritte/Verbindungen/Bedingungen) | [B_02 §1A, §2; SIB:uber-dvelop-smart-invoice] |
| Rechnungseingangsbuch | Einstiegspunkt/Arbeitsliste für Anwendende | [B_02 §1A, §2; REB] |
| d.velop eInvoice converter | E-Rechnungs-Konvertierung (XML→PDF) und XRechnungs-Validierung | [B_02 §7; B_06 §9b] |
| d.velop documents | revisionssichere Archivierung | [B_02 §1A] |
| **d.velop process studio** | BPMN-2.0-Prozessautomatisierung (process, process modeler, forms, scripting, ab 2025.q1 actions eventbridge) | [B_04 §1B; PSU:softwareuberblick/kurze-einfuhrung-in-die-software; PSA:konfigurieren-von-dvelop-process-studio] |
| d.3 flow designer / flow inspector | klassische d.3-Workflow-Welt (Plugin für d.3 cockpit), Doku nicht öffentlich | [B_04 §1A, §0] |
| d.ecs task / d.ecs userprofile | Aufgabenverwaltung, Vertretungs-/Verantwortungsregeln / Abwesenheit | [B_04 §1D, §7] |
| **d.velop inbox management** = d.velop mail dispatcher (Verteilung) + inbound (Erfassung) | Posteingangsverteilung (Papier, E-Mail, andere Kanäle) | [B_06 §1, §3; MDA:basisinformationen-zur-anwendung/uber-dvelop-mail-dispatcher] |
| d.velop email import | Pull-Überwachung eines M365-Postfachs, Import als Stapel in inbound | [B_06 §4a; EMI:basisinformationen-zur-anwendung/uber-dvelop-email-import] |
| alphaflow Eingangsrechnungen | separates, schlankeres Produkt (Organisationen statt Mandanten, Squeeze-OCR, keine Freigabematrix/E-Rechnung/DATEV dokumentiert) | [B_02 §1B, Kurzfazit] |

**Fakt:** smart invoice (eigener Rechnungsworkflow mit Urkel-Bedingungen wie `voucher.net_amount`) und process studio (BPMN-Engine) sind **zwei getrennte Workflow-Welten**. [B_02 §2, §6; B_04 §1]
**Annahme (A):** Für Livos wird der ER-Prozess in smart invoice abgebildet; process studio dient für Nicht-Rechnungsprozesse (Verträge, Klärfälle außerhalb smart invoice, Sonderabläufe). Eine dokumentierte Kopplung smart invoice ↔ process studio wurde in den drei Quellen **nicht** gefunden.

### 0.2 Abbildung auf den Livos-ER-Zielprozess (MDIS-Zuordnung = Annahme)
Livos-Prozess laut 00_BRIEFING (Zusammenfassung A_Livos_DMS_Business_Architektur): Eingang → Verarbeitung & Vorqualifikation → Verteilung (DATEV ER-Vorerfassungsjournal) → Fachliche Prüfung/Detailqualifikation (Bauprojekte: Bim4You) → Fachliche Freigabe (DATEV Verbuchung) → Zahlungsfreigabe (DATEV Zahlungsdurchführung).

| Livos-Schritt | d.velop-Baustein (belegt) | Status | Beleg / Hinweis |
|---|---|---|---|
| Eingang | inbound e-mail / email import (Alias je Gesellschaft), inbound scan, Dateiimport | B | [B_06 §4, §7] |
| Verarbeitung & Vorqualifikation | document reader (OCR, Mandant/Kreditor, §14-Prüfung, Dublette), eInvoice converter | B | [B_02 §3, §4, §7, §8] |
| Verteilung (+ DATEV-Vorerfassung) | smart invoice Schritt „Verteilung" (Onboarding); Export an Integration an **jeder** Schrittverbindung möglich, Exportwert `default`/`validate`/`book` | B / **A** für DATEV | Export-Mechanik belegt [B_02 §9]; dass damit eine DATEV-Vorerfassung + spätere Verbuchung (zwei Exporte) funktioniert, ist **Annahme** – DATEV-Connector-Doku nicht öffentlich |
| Fachliche Prüfung (Bim4You) | smart invoice Prüfung/erweiterte Prüfung; Integration per Webhook/API | B / **A** für Bim4You | [B_02 §8, §9]; Bim4You-Anbindung in keiner Quelle erwähnt |
| Fachliche Freigabe | smart invoice Freigabe (Wertgrenze / Freigabematrix / Vier-Augen) | B / E | [B_02 §6] |
| Zahlungsfreigabe | smart invoice-Schritt „Zahlungsfreigabe" als Beispiel genannt; Felder Zahlbetrag/Skonto | E | [B_02 §2, §10]; Zahlungsdatei/Omikron **N** |

---

## 1. Eingangsrechnungsverarbeitung (d.velop invoices / smart invoice & Co.)

### 1.1 Eingangskanäle

| Nr | Fähigkeit | Belegte Funktion (Fakt) | Status | Hinweis für Livos | Quelle |
|---|---|---|---|---|---|
| 1.1.1 | E-Mail (Push) | **d.velop inbound e-mail**: Admin legt Postfächer an, Anwender/Absender senden dorthin; **pro E-Mail ein Stapel**; Zugelassene Absender mit Wildcards (`*@*`, `*@<domain>.de`, `?`); Stapelname mit `%Sender%`, `%Subject%`, `%Timestamp%`; Schlüssel-Wert-Paare als Stapeleigenschaften; Fehlerbenachrichtigung an Benutzer/Gruppe | B | Auch aus Microsoft 365 (Outlook) heraus; Outlook-Add-In mit Manifest-URL `https://<TenantUri>/inboundoutlook/addin` | [B_02 §3; B_06 §4h; IEM:konfigurieren-von-dvelop-inbound-e-mail/verwalten-von-postfachern] |
| 1.1.2 | E-Mail (Pull, zentrales Postfach) | **d.velop email import**: überwacht M365-Postfach via **Microsoft Graph**, pro E-Mail ein Stapel; **Alias-Adressen je Postfach** (z.B. `invoices+1@…`) mit eigenem Importprofil, Stapelnamen (`%Sender%`, `%Subject%`, `%Timestamp%`, `%Date%`), Schlüssel-Wert-Paaren (Stapel- oder Dokumenteigenschaften), Berechtigungsgruppe | B | Kernbaustein „ein Rechnungspostfach, Alias je Gesellschaft". Die Nutzung für Mandantentrennung ist die Ableitung der Recherche (B_06 §4d „Livos-Antwort") = **A** | [B_06 §4a–4d; EMI:konfigurieren-von-dvelop-email-import/konfigurieren-von-postfachern] |
| 1.1.3 | IMAP / Exchange On-Prem | IMAP „Zukünftig verfügbar"; Exchange On-Prem über „d.velop email fetcher" (EWS) im Konfigurationskapitel beschrieben, in der Produktübersicht aber ebenfalls „Zukünftig verfügbar" | E | **Doku-Widerspruch**; nur **eine** Verbindung/Bereitstellungsform je Instanz | [B_06 §4a, §4c, Offene Punkte 2] |
| 1.1.4 | Scan (Papier) | inbound scan: „Papierbelege werden einem Scanner zugeführt, als PDF-Datei digitalisiert und dann importiert"; d.velop scanner connector (TWAIN) sendet Seiten per HTTP an die Inbound-App | B | Scan am Arbeitsplatz; „Scannen in Akte" möglich | [B_02 §3; B_06 §7a, §7d; ISU:erste-schritte/installieren-von-dvelop-scanner-connector] |
| 1.1.5 | Upload | Dateiimport aus Dateisystem, Drag & Drop, ZIP/RAR entpacken (Alt+Shift+U), Import-Widget mit max. 4 Dropzones je Widget (je Dropzone ein Importprofil), „Schnelles Importieren" | B | Dropzones je Gesellschaftsgruppe denkbar (**A**) | [B_06 §7b, §7c, §7e; ISA:import-widget-und-dropzones] |
| 1.1.6 | API-Import | „Öffentliche Schnittstelle zum Importieren von Dokumenten" (inbound suite) | B | Weg für Scandienstleister/Fremdsysteme (**A**) | [B_06 §3] |
| 1.1.7 | E-Rechnung XRechnung | Import als XML (CII und UBL); Konvertierung zu PDF-Ansicht durch eInvoice converter; Original-XML wird in das PDF integriert; Metadaten direkt aus XML für die Erkennung | B | Formatliste inbound: „ZUGFeRD, XML (nur xRechnungen vom Typ CII und UBC [sic])" | [B_02 §7; B_06 §5, §9b; ISA:konfigurieren-von-dvelop-inbound-scan/konfigurieren-von-importprofilen; EIC:tipps-und-tricks/integration-in-die-inbound-app] |
| 1.1.8 | E-Rechnung ZUGFeRD | In den Handbüchern technisch als **UN/CEFACT Cross Industry Invoice (CII)**; Name „ZUGFeRD" nur im Helpcenter-Artikel und in der inbound-Formatliste; bei hybrider PDF mit valider E-Rechnung werden **nur die XML-Metadaten** verwendet | E | ZUGFeRD-Profile (BASIC/EN16931/EXTENDED) **N** | [B_02 §7; HC cm7x5vm8dtzbi07upt6zu1j3d; EIC:tipps-und-tricks/integration-in-dvelop-document-reader] |
| 1.1.9 | Weitere E-Rechnungsformate | UBL 2.1 Invoice; national CFDI 4.0 (MX), FA(3) (PL); zusätzliche Namespaces per eigenem XSLT-Stylesheet | B | – | [B_02 §7; EIC:konfigurieren/konvertieren-von-e-rechnungen-in-ein-allgemeingultiges-format] |
| 1.1.10 | **Peppol** | in keiner der drei Quellen erwähnt | **N** | Recherchelücke (siehe §7) | [B_02, B_04, B_06 – Volltextsuche] |
| 1.1.11 | Unterstützte Dateiformate inbound | TIF, BMP, JPG, HEIC, HEIF, PDF, EML, MSG, DGIX, DGI, DGIM, DGIA, ZUGFeRD, XML (nur XRechnung CII/UBL), ausgewählte Office-Formate (DOCX, PPTX, XLSX) | B | – | [B_06 §5; ISA:…/konfigurieren-von-importprofilen] |
| 1.1.12 | Mail-Textkörper / Anlagen | Importprofil Registerkarte „E-Mails": Textkörper am Anfang/Ende außerhalb oder innerhalb der Trenner; eigene **Standardkategorie für den Textkörper**; „Anlagen dem PDF-Anhang hinzufügen" (nur mit Dateiformat „PDF-Datei mit Quelldatei im Anhang"; „z.B. beim Export von XRechnungen sinnvoll") | B | Mail als eigenes Dokument (z.B. Kategorie Korrespondenz – Begriff selbst **N**) | [B_02 §7; B_06 §5] |
| 1.1.13 | Standard-Importprofile | Standardprofil (manuell), Dateiimport-Profil (größtenteils automatisiert, manuelles Speichern), Automatisches Dateiimport-Profil; Onboarding legt Importprofile/Eingangspostfächer „Eingangsrechnung automatisch" / „Eingangsrechnung manuell" an | B | – | [B_02 §2, §3] |

### 1.2 Erkennung / KI

| Nr | Fähigkeit | Belegte Funktion (Fakt) | Status | Hinweis für Livos | Quelle |
|---|---|---|---|---|---|
| 1.2.1 | OCR-Rechnungslesung | document reader (Ausprägung invoice) erfasst Daten gescannter Dokumente; On-Prem OCR-Engine **ABBYY FineReader**; in der Cloud-inbound ist OCR ein Schalter „Texterkennung" im Importprofil, Engine-Name **N** | B / N | – | [B_02 §3; B_06 §8] |
| 1.2.2 | Erkannte Felder (belegt) | Kopf: `netto_betrag1/2/3`, `vat_rate1/2/3`, `vat_amount1/2/3`, `gl_account`, `cost_center`; Position: `tax_code`, `vat_rate`, `vat_amount`; Skontofälligkeit, Nettofälligkeit, Skontoprozentsatz; aus document reader: Mandant, Lieferant, Bestellnummer, Positionen (Menge/Einzelpreis), IBAN; Rechnungsdatum/-nummer (Dokumentprüfung) | E | **Vollständige Feldliste N** (Seite „Übertragen von Daten aus der Erkennung" gesperrt) | [B_02 §3, Offene Punkte 1; SI:einrichten-der-rechnungslesung] |
| 1.2.3 | **Lernfähigkeit** (Lernen aus Korrekturen) | in keiner der drei Quellen beschrieben | **N** | Für Trefferquoten-Zusage relevant | – |
| 1.2.4 | KI-Klassifikation/-Extraktion (allgemein) | inbound „Seitenanalyse" (OCR, Barcodes, erste Dokumentseite per KI); KI-Dokumentanalyse → Prozesskategorie/Prozesseigenschaft; **document intelligence hub**: KI-Anbieter pro Dokumentart, bei dynamischen Anbietern eigene **Prompts**, Ausgabeformat; Dienst **d.velop pilot** standardmäßig verfügbar; „d.velop document analysis" für PDF-/Papierrechnungen (kein eigenes Handbuch) | B | Alternative/Ergänzung zum document reader für Nicht-Rechnungen (**A**) | [B_06 §6e, §8; DIH; ISA:…/verwalten-von-kategorien-der-dokumentanalyse] |
| 1.2.5 | **Mandantenerkennung** (Rechnungsempfänger) | „Die Erkennung von Mandant und Lieferant eines Belegs erfolgt zunächst über die **Stammdaten**." Kriterien Mandant laut API: **`name`** („wie er auf den Rechnungen zu finden ist") und **`address`** – je „wichtiges Kriterium"; zusätzlich `city`, `zip_code`, `country` (Regelsatz lokaler Landesregeln), `local_currency`, `id`, `parent_id`. Dokumentprüfung prüft beim Mandanten **Name, PLZ, Ort, Straße** | B | **USt-IdNr/Steuernummer sind beim Mandanten NICHT als Stammdatenfeld vorgesehen.** Bei Gesellschaften mit identischer Anschrift bleibt der **Name** einziges dokumentiertes Unterscheidungsmerkmal → Trefferquote offen | [B_02 §4; DR:dokumenterkennung; SID:verwenden-der-api-funktionen/ubertragen-von-stammdaten-dvelop-smart-invoice] |
| 1.2.6 | Kreditorenerkennung | `vat_id` (USt-IdNr) „wichtig für die automatische Erkennung des Kreditoren"; `registration_id` (Steuernummer); Dokumentprüfung Lieferant: Name, PLZ, Ort, Straße, USt-ID oder Steuernummer; smart invoice überträgt „Kreditoren mit Adress- und Steuerinformationen, Bankverbindungen von Kreditoren" an den document reader | B | Ob IBAN aktiv zur Kreditorenermittlung genutzt wird: **A** | [B_02 §4] |
| 1.2.7 | Generische Adressdatenerkennung | Fallback, wenn Stammdaten kein Ergebnis liefern; standardmäßig **deaktiviert**; setzt **keine** Mandanten-/Lieferantennummern; „mit Vorsicht" aktivieren | B | Für Livos eher nicht geeignet (**A**) | [B_02 §4; DR:dokumenterkennung] |
| 1.2.8 | Standardmandant (Fallback) | „wird verwendet, wenn kein anderer Mandant durch die Klassifizierung ermittelt werden kann"; Auswahl aus Schema **Standard** | B | Klärfall-Gesellschaft als Standardmandant denkbar (**A**) | [B_02 §4] |
| 1.2.9 | Mehrmandantenfähigkeit Stammdaten | Stammdaten in **Schemata**/**Buckets** teilbar; mehrere Buckets → mehrere Workflowdefinitionen (Beispiel „ERV Firma 1"/„ERV Firma 2"); Einstellung **Einstellungen > Rechnungslesung > General > Stammdaten-Bucket für die Rechnungslesung**; im Inbound-Importprofil Stapeleigenschaft `Schema` = Bucket-ID; Vorschau-Feature-Flag `multiple_buckets_in_document_reader`; **Empfehlung d.velop: möglichst ein Stammdatenbucket** | E | Bei >100 Gesellschaften: ein Bucket + Mandant als Feld (**A**, deckt sich mit d.velop-Empfehlung) | [B_02 §4; SI:wissenswertes-zum-prozess-der-stammdatenubertragung] |
| 1.2.10 | Korrektur erkannter Werte | document reader: **Sichtprüfung** (Indexierung), Bearbeitungsprofile **Indexing**/**FullAccess**; Einstellung **Exportvalidierung** am Zielsystem – „nur d.velop smart invoice [bietet] die Validierung durch das Zielsystem an" → Korrektur in der smart-invoice-Workflow-Maske | B | Anwenderhandbuch der Workflow-Maske **N** | [B_02 §3; DR:zielsysteme] |
| 1.2.11 | Stammdaten-Upload in document reader | Formate CSV, JSON, ZIP; Tabellenname = Dateiname (z.B. `CC_COMPANIES.csv`); „Beispiel-Zip-Paket herunterladen"; Prüfung „Ausfüllen der wichtigsten Eigenschaften" (z.B. USt-IdNr) | B | Initialbefüllung 100+ Gesellschaften (**A**) | [B_02 §3; DR:stammdaten] |

### 1.3 Validierung, Dublettenprüfung, rechnerische Prüfung

| Nr | Fähigkeit | Belegte Funktion (Fakt) | Status | Hinweis | Quelle |
|---|---|---|---|---|---|
| 1.3.1 | §14-UStG-Prüfung | document reader „Rechnungsprüfung … im Sinne der Prüfung nach §14": Mandantendaten (Name, PLZ, Ort, Straße), Lieferant in Stammdaten, Lieferantendaten inkl. USt-ID/Steuernummer, IBAN vorhanden, Rechnungsdatum/-nummer, Rechnungsbeträge (Netto 1–3, Brutto); zusätzlich „Formal Correctness-App"; „Erweiterung … auf Anfrage" | E | Keine Einzelzuordnung zu allen §14-Pflichtangaben; Formal Correctness-App ohne Handbuch | [B_02 §8, Offene Punkte 7; DR:dokumentprufung] |
| 1.3.2 | XRechnungs-Validierung | Schalter **Validierung von XRechnungen** (eInvoice converter); Syntaxschema, EN16931, XRechnungsregeln (CIUS) mit **KoSIT Validator** (Port 18081); Prüfbericht als **Anhang** in der Dokumentvorschau; Ergebniswerte `Ok`/`Fail`/`Warning`/`Error`/`Skipped` (CML `InvoiceValidationStatus`, JSON `validationStatus`) | B | **Nur XRechnung wird validiert**, ZUGFeRD nicht; Prüfbericht in inbound/document reader visuell nicht sichtbar | [B_02 §7; B_06 §9b; EIC:konfigurieren/validieren-von-xrechnungen-und-erstellen-von-prufberichten] |
| 1.3.3 | XML-Visualisierung | seit 12.02.2025 (Cloud) überarbeitete Visualisierung + tabellarische Übersicht aller potenziellen XRechnungs-Felder, ohne Aktivierung; Zusatzfelder per Custom-Stylesheet | B | BT-Feldliste nur als Bild (**N** als Text) | [B_02 §7; HC cmg4z5vv7xqvr07w42jl1qa43 u.a.] |
| 1.3.4 | Dublettenprüfung (document reader) | über **Rechnungsnummer**; nur gegen **validierte** Belege; anpassbar über d.velop webindex designer | B | webindex-designer-Doku nicht öffentlich | [B_02 §8; DR:dokumentprufung] |
| 1.3.5 | Duplikatsprüfung (smart invoice) | **Workfloweinstellungen > Duplikatsprüfung**; bei neuen Workflows standardmäßig aktiv; Kriterien **Kreditornummer + Rechnungsnummer**, älterer Workflow **≤ 18 Monate**, sonst jüngere abgeschlossene; Warnung muss mit **Begründung** akzeptiert werden (Protokoll); Neuprüfung bei Änderung von Kreditor-/Rechnungsnummer | B | Kein Blockieren, sondern Warnung mit Begründungspflicht | [B_02 §8; SI:durchfuhren-der-duplikatsprufung] |
| 1.3.6 | Rechnerische Prüfung | als **Eigenschaft einer Schrittverbindung** („Rechnerisch Richtig: Erteilen"), Zeitpunkt + Benutzer protokolliert | B | – | [B_02 §8; SI:einrichten-der-rechnerischen-und-sachlichen-prufungen] |
| 1.3.7 | Aufteilungsprüfung | `voucher.amount_allocated?(mode)` (0=Brutto … 6=alle drei), `voucher.amount_allocated_tolerance?(mode, tolerance)` (Toleranz in Cent) | B | Sicherstellen vollständiger Kontierung vor Freigabe | [B_02 §5; SI:wissenswertes-uber-bedingungen/wissenswertes-zu-objekten-und-feldern] |
| 1.3.8 | Rundung | horizontale Methode, kaufmännisch auf 2 Stellen | B | – | [B_02 §8; SI:wissenswertes-zu-berechnungen-in-dvelop-smart-invoice] |

### 1.4 Kreditorenstammdaten-Abgleich / Stammdatenversorgung

| Nr | Fähigkeit | Belegte Funktion (Fakt) | Status | Hinweis | Quelle |
|---|---|---|---|---|---|
| 1.4.1 | Stammdatenentitäten | Mandanten (`companies`), Kreditoren (`vat_id`, `registration_id`, Adresse), Kreditorbankverbindungen, Kostenstellen/Kostenträger/Sachkonten (`company_id`, `nr`, `name`), Steuerschlüssel (`tax_codes` mit `percentage`, `tax_category_1/2`), Bestellungen, Wareneingänge, Zahlungsbedingungen, Währungen, Beschaffungskategorien, Zusatzdimensionen, Zuschlagstypen | B | Kostenstelle/Sachkonto **ohne Mandant gilt für alle Mandanten** – gemeinsame vs. gesellschaftsspezifische Konten abbildbar | [B_02 §5, §9, §10; SID:…/ubertragen-von-stammdaten-dvelop-smart-invoice] |
| 1.4.2 | Stammdatenquelle ERP | „Integration" stellt Stammdaten bereit (z.B. Kreditoren, Sachkonten, Bestellungen); Standardintegration **d.velop connect for Microsoft Dynamics 365** (BC, F&O): Sync **stündlich**, **Sachkonten täglich**; 4 Fehler in Folge → „Technisches Problem", nach 7 Tagen ohne Erfolg Deaktivierung | B | DATEV als Stammdatenquelle: Produktseite nennt „Stammdaten für die Buchhaltung", „Validierung gegen die DATEV Stammdaten" – Mechanik **N** | [B_02 §9; SI:konfigurieren-von-integrationen; www.d-velop.de/software/datev] |
| 1.4.3 | Stammdatenquelle ohne ERP | **Buckets**: Neuer Bucket > Daten bearbeiten > Entität wählen; „Beispieldaten importieren"; Anbindung über Workfloweinstellungen > Integrationen > Neue Integration > Bucket; Felder > Datenquelle `Stammdaten` | B | Übergangs-/Demo-Lösung, Pflege manuell oder per API (**A**) | [B_02 §9; SI:konfigurieren-von-buckets] |
| 1.4.4 | Weitergabe an Erkennung | smart invoice → document reader: Mandanten mit Adressinformationen, Kreditoren mit Adress-/Steuerinformationen, Bankverbindungen, Bestelldaten, Wareneingänge – asynchron nach Oberflächenänderung, ERP-Import per API, Abruf, manueller Übertragung | B | – | [B_02 §4] |

### 1.5 Bestellbezug

| Nr | Fähigkeit | Belegte Funktion (Fakt) | Status | Hinweis | Quelle |
|---|---|---|---|---|---|
| 1.5.1 | Bestell-/Wareneingangsdaten | Positionsfelder `order_number`/`order_line`, `goods_receipt_nr`; Bestellzeilen tragen `gl_account`, `cost_center`, `cost_unit` (Kontierung aus Bestellung) | B | Relevanz bei Bau/Immobilien gering bzw. Bim4You-Thema (**A**) | [B_02 §5] |
| 1.5.2 | Bestellabgleich im Workflow | Bedingungen `voucher.matches_po?`, `voucher.matches_po_or_verified?`; Schritttyp **Warten auf Wareneingang**; Schnellaktion „Warten auf Wareneingang abbrechen" | B | **Erweiterte Prüfung funktioniert nicht mit automatischem Bestellabgleich** | [B_02 §2, §8] |

### 1.6 Kontierung

| Nr | Fähigkeit | Belegte Funktion (Fakt) | Status | Hinweis | Quelle |
|---|---|---|---|---|---|
| 1.6.1 | Kontierungsfelder | Position: Sachkonto (`gl_account`), Kostenstelle (`cost_center`), Kostenträger (`cost_unit`), Beschaffungskategorie, Steuerschlüssel, Beträge, Menge, Einheit, Preis; Onboarding-Eigenschaften Kostenstellen/Kostenträger/Sachkonten als **Mehrfachfelder**, Buchungstext, Leistungsdatum, Belegart | B | – | [B_02 §2, §5] |
| 1.6.2 | Splitting | über **mehrere Belegpositionen**, jeweils eigenes Sachkonto/Kostenstelle/Kostenträger; Gruppierung **Kostenobjekt** (Mandant + Kostenstelle + Kostenträger); Doku-Beispiel 25.000 = 17.000 (KSt 5000) + 8.000 (KSt 2000) | B | – | [B_02 §5; SI:informationen-zu-komplexen-freigaben-freigabeschritt-mit-freigabematrix] |
| 1.6.3 | Kontierungsvorschläge | **Einstellungen > Rechnungslesung**: „Belegzeilen für jeden Steuersatz automatisch erstellen" (nur ohne Positionsdaten), „Sachkonto vorschlagen"/„Kostenstelle vorschlagen" (nur mit vorgenannter Option), „Steuerschlüssel aus den erkannten Rechnungspositionen nutzen", „Steuerbeträge aus der Erkennung nutzen", Standard-Steuerschlüssel (optional je Mandanten-ID) | B | – | [B_02 §5; SI:einrichten-der-rechnungslesung] |
| 1.6.4 | Automatische Steuerschlüsselermittlung | Abgleich `tax_category_1`/`tax_category_2` von Kreditor und Sachkonto bzw. Beschaffungskategorie; bei eindeutiger Übereinstimmung automatisch | B | §13b/Reverse Charge darüber **denkbar (A)**, als Begriff **N** | [B_02 §5, §10] |
| 1.6.5 | Aufteilungsschlüssel/Kontierungsvorlagen | in d.velop invoices **kein** benannter Aufteilungsschlüssel dokumentiert; nur Vorschläge, Kontierung aus Bestellung, **Zuschläge** mit Verteilung manuell/gleichmäßig/nach Betrag/nach Menge; alphaflow hat **Kontierungsvorlagen** | N (invoices) / B (alphaflow) | Wiederkehrende Umlagen (Livos) nicht als Vorlage belegt | [B_02 §5; AF:konfiguration/kontierungsvorlagen] |
| 1.6.6 | Feldsteuerung je Schritt | je Schritt und Feld **Sichtbar**, **Schreibbar**, verpflichtend; Position **Schreibbar wenn geprüft** (Nachkontierung durch Buchhaltung) | B | – | [B_02 §3; SI:konfigurieren-von-feldern] |
| 1.6.7 | Kundenspezifische Felder | 20 kundenspezifische Felder Kopf/Zeile, „Custom 1 bis Custom 10 bzw. Custom 20", je Workflow umbenennbar | B | Träger für Bau-Spezifika (Einbehalt, Abschlag, Objekt/Projekt) = **A** | [B_02 §10; SI:konfigurieren-von-feldern] |

### 1.7 Prüf- und Freigabeworkflow (smart invoice)

| Nr | Fähigkeit | Belegte Funktion (Fakt) | Status | Hinweis | Quelle |
|---|---|---|---|---|---|
| 1.7.1 | Best-Practice-Workflow | Onboarding liefert Workflow mit Schritten **Verteilung, Prüfung, Freigabe, Buchhaltung**, Aktenplan (Eingangsrechnung/-gutschrift, Kreditorenvorgangsakte, Rechnungsanlage, Workflowprotokoll ERV), Gruppen `dv_Buchhaltung`, `dv_Freigeber`, `dv_Sachliche_Prüfer`, `dv_inbound`, `dv_inbound_Administratoren`, `dv_Service_Accounts`, `dv_Workflowteilnehmer` | B | Guter Startpunkt für Livos-Blueprint | [B_02 §2; SI:wissenswertes-zum-onboarding] |
| 1.7.2 | Modellierung | Schritte + Verbindungen; Schritttypen: normal, **Freigabe**, **Prüfung**, **Warten auf Wareneingang**; Verbindungsauswahl **Top-Down, erstes zutreffendes Kriterium** (Drag & Drop Reihenfolge) | B | – | [B_02 §2, §6A; SI:konfigurieren-von-schritten-und-verbindungen] |
| 1.7.3 | Zuständigkeit (Bearbeiterfindung) | je Schritt eine **Bearbeiterfindung** (Benutzergruppe oder Bedingung, z.B. `user.name IN voucher.outstanding_verifiers`, Regex `/^SP_.*$/ ~= user.name`, „Alle Treffer verwenden") | B | Dynamische Zuständigkeit aus Belegdaten möglich | [B_02 §6A, §8] |
| 1.7.4 | Sachliche Prüfung | Feld „Sachl. richtig"; `voucher.verified?` (alle Zeilen), `voucher.verifications_completed?` | B | – | [B_02 §8] |
| 1.7.5 | Erweiterte Prüfung (mehrstufig) | Einstellungen > **Prüfen** > Prüfung hinzufügen (Prüfungstyp, Prüfer, aktiv, Reihenfolge per Drag & Drop); Schritttyp **Prüfung**, optional **Prüfungsmatrix**; Felder „geprüft?"/„Prüfung" ersetzen „sachlicher Prüfer"/„sachlich richtig" | E | **Nur ein Prüfungsschritt pro Workflow**; nicht mit automatischem Bestellabgleich | [B_02 §8; SI:einrichten-der-erweiterten-prufung] |
| 1.7.6 | Betragsgrenze (einfach) | Schrittverbindung mit Bedingung, z.B. `voucher.net_amount >= 500000` (Doku-Beispiel 5.000 EUR); **Beträge in Cent** → 10.000 EUR = `1000000`; Verbindung oberhalb der Standardverbindung; „Freigabe: Erteilen" erfordert „Sachlich richtig" | B | Livos-Grenze 10.000 EUR direkt abbildbar | [B_02 §6A; SI:einrichten-einer-einfachen-freigabe-mit-begrenzter-komplexitat] |
| 1.7.7 | Freigabematrix | feste Spalten **Bearbeiter**, **Freigabegrenze** + bis zu **20** weitere Spalten (z.B. **Mandant**, Kostenstelle, Kostenträger); Platzhalter `*` (Präfix), leer (alle), `$` (muss leer sein); **case-sensitive**; Strategien **Direkt** und **Von Unten zum Freigeber**; Hierarchie über Kostenstellenstruktur oder Spalte **Rang** (0–99); Grenze bezogen auf Netto oder Brutto; **Grenze gilt pro Kostenobjekt**, nicht pro Rechnung | B | Mandant als Matrixspalte → gesellschaftsspezifische Freigeber bei >100 Gesellschaften (**A**: Pflegeaufwand prüfen) | [B_02 §6B; SI:informationen-zu-komplexen-freigaben-freigabeschritt-mit-freigabematrix] |
| 1.7.8 | Freigabeschritt-Regeln | mind. eine Aktion **Bestätigen** und eine **Ablehnen**; eingehende Verbindung „Freigabe: Kein Einfluss" | B | Ablehnung als Pfad modellierbar | [B_02 §6B] |
| 1.7.9 | **Vier-Augen-Prinzip** | „für freizugebende Beträge über 10.000,00 EUR … immer eine zweite Freigabe"; wirkt pro Kostenobjekt; Reihenfolgelogik bei Strategie Direkt; **sachliche Prüfer werden nicht berücksichtigt**; optionaler **Minimalbetrag** (darunter Überspringen möglich) | **E (Vorschau-Feature)** | Aktivierung nur über d.velop-Support; **Menüpfad/Schalter N** | [B_02 §6 „Vier-Augen-Prinzip", Offene Punkte 4] |
| 1.7.10 | Freigabe überspringen | Standardaktion + „Automatisch Freigaben für Prüfer erzeugen" | B | – | [B_02 §6 „Freigabe überspringen"] |
| 1.7.11 | Klärfall / Fehlerkorrektur | **Clearingstelle/Clearing-Modus**: fehlgeleitete Rechnung, falsche Kontierung, falsche Freigabe; im Clearingmodus alle Felder beschreibbar, Änderungen im Workflowprotokoll; Clearing-Gruppe global und **je Mandanten-ID** | B | Klärfall „falsche Gesellschaft" = Clearing (**A**); ein separater „Klärungskorb" als Schritt ist ebenfalls modellierbar (**A**) | [B_02 §8; SI:wissenswertes-zur-clearingstelle] |
| 1.7.12 | Vertretung | Rechnungseingangsbuch-Ansicht „**Rechnungen in Vertretung**"; plattformweit Abwesenheit/Vertretung über d.ecs userprofile/d.ecs task (siehe §2.6) | B / A | Dass die d.ecs-task-Vertretungsregeln auch smart-invoice-Aufgaben erfassen, ist **A** (Ansichtsname deutet darauf hin) | [B_02 §2; B_04 §7] |
| 1.7.13 | Eskalation / Erinnerung in smart invoice | in B_02 **nicht beschrieben** | **N** | Livos-Anforderung Liegezeit/Eskalation für Rechnungen offen | [B_02 – kein Treffer] |
| 1.7.14 | Externe Freigabe ohne Lizenz | in B_02 **nicht beschrieben** | **N** | process studio kennt „Externe Benutzeraufgabe" (E-Mail + d.velop forms), Lizenzfrage und Kopplung an smart invoice **offen** | [B_04 §3, §6c] |

### 1.8 Rechnungseingangsbuch, Status, Protokoll

| Nr | Fähigkeit | Belegte Funktion (Fakt) | Status | Hinweis | Quelle |
|---|---|---|---|---|---|
| 1.8.1 | Arbeitsliste | Schnellzugriffe **Meine offenen Rechnungen** (direkt oder über Gruppe), **Rechnungen in Vertretung**, **Alle offenen Rechnungen** (mit Berechtigung), **Archiv** (mit Berechtigung); eigene Schnellzugriffe mit Filter + Layout | B | – | [B_02 §2; REB] |
| 1.8.2 | Archiv-Zeitfenster | Archiv zeigt **6 Monate** ab Rechnungsdatum, per „Erweiterte Liste" **12 Monate** | E | Ältere Rechnungen nur über DMS-Recherche (**A**) | [B_02 §2] |
| 1.8.3 | Schnellaktionen | Dokument anzeigen, Historie anzeigen, Clearing-Modus aktivieren, Warten auf Wareneingang abbrechen | B | – | [B_02 §2] |
| 1.8.4 | Berechtigung | Rechnungseingangsbuch-Berechtigung „global" oder „mandantenbezogen" | B | Gesellschaftsbezogene Sicht für >100 Gesellschaften | [B_02 §4] |
| 1.8.5 | CSV-Export | Kontextmenü der Vorgangsliste: „Sichtbare Spalten exportieren"/„Alle Spalten exportieren", Filter berücksichtigt, Download **30 Tage** verfügbar | B | Basis für Liegezeit-/Status-Auswertungen außerhalb (**A**) | [B_02 §9; HC cms7m6f3dyddy07w4mmm35kqn] |
| 1.8.6 | Status-Modell | Eigenschaft **Workflowstatus** (Onboarding); Export-`end_mode` `finished`/`aborted`; Sichten „offen" vs. „Archiv"; Sonderzustände Clearing-Modus, Warten auf Wareneingang; E-Rechnung `validationStatus` | E | **Eine definierte Werteliste des Workflowstatus ist N**; Livos-Statusmodell muss aus Schritten abgeleitet werden (**A**) | [B_02 §2, §7, §9] |
| 1.8.7 | Protokoll | Workflowprotokoll (Duplikat-Begründung, Clearing-Änderungen, Rechnerisch richtig mit Benutzer/Zeit); Kategorie „Workflowprotokoll ERV" im Aktenplan | B | Revisionsnachweis | [B_02 §2, §8] |
| 1.8.8 | Liegezeit-Auswertung | nicht dokumentiert | **N** | Siehe §7 | [B_02 – kein Treffer; B_04 §9] |

### 1.9 Exporte / Buchhaltungsübergabe / Zahlungsfreigabe

| Nr | Fähigkeit | Belegte Funktion (Fakt) | Status | Hinweis | Quelle |
|---|---|---|---|---|---|
| 1.9.1 | Übergabeprinzip | „Am Ende des Workflows wird entweder ein **finaler Buchungssatz** oder ein **Buchungsvorschlag** … übergeben." | B | – | [B_02 §9] |
| 1.9.2 | Auslösung | **ereignisgesteuert an einer Schrittverbindung** („Export durchführen" → Integration), **nicht zeitgesteuert**; Exportwert `default`/`validate`/`book` wird ins JSON übernommen | B | Für die generische Integration erfüllt das „mehr als ein Lauf pro Tag"; für DATEV **offen** | [B_02 §9; SI:konfigurieren-von-integrationen] |
| 1.9.3 | Technische Schnittstelle | Ereignis `integration.export` mit `workflow.voucher` (Kopf + Positionen), `connection.from_step`/`to_step`/`end_mode`, `_links.dmsobject` (Link auf Rechnung im DMS), `_links.report_results_async`; synchron/asynchron (Webhook + Abhol-API) | B | Weg für Bim4You/Individualanbindung (**A**) | [B_02 §9; SID:verwenden-der-api-funktionen/empfangen-von-belegdaten-dvelop-smart-invoice] |
| 1.9.4 | ERP-Standardconnector | d.velop connect for Microsoft Dynamics 365 (BC, F&O) | B | Nicht Livos-Zielsystem | [B_02 §9] |
| 1.9.5 | **DATEV** | Produkte existieren: „d.velop connect for datev", „d.velop invoices for DATEV Rechnungswesen", „… for DATEV Unternehmen Online", „LD Connect for DATEV Unternehmen Online"; Produktseite: „Übergabe der Buchungsdaten mit Beleglinks", „Stammdaten für die Buchhaltung", „Validierung gegen die DATEV Stammdaten" | E | **Handbücher nicht öffentlich; Format (z.B. EXTF), Mapping, Auslösung, Intervall N** | [B_02 §9, Offene Punkte 3; www.d-velop.de/software/datev] |
| 1.9.6 | Zahlungsfreigabe | „Zahlungsfreigabe" als Beispiel eines Workflowschritts; Felder Zahlbetrag (`pay_amount`, `pay_amount_lcy`), Skonto (`cashback_percentage1`, `cashback_due_date1`), Skonto-/Nettofälligkeit aus Erkennung; Zahlungsbedingungen als Stammdaten | E | Schritt modellierbar; **Zahlungsdatei, Zahlungsrückmeldung, Omikron N** | [B_02 §2, §3, §9, §10] |
| 1.9.7 | Bau-Spezifika | **Abschlagsrechnungen, §13b Reverse Charge, Sicherheitseinbehalte: nicht gefunden**; „Zuschläge" können Abschläge im Sinne wertmindernder Positionen darstellen (≠ Abschlagsrechnung) | **N** | Nur über Custom-Felder/Customizing (**A**) | [B_02 §10; SI:arbeiten-mit-zuschlagen] |

---

## 2. Workflows / d.velop process studio

### 2.1 Werkzeuglandschaft

| Nr | Fähigkeit | Belegte Funktion (Fakt) | Status | Quelle |
|---|---|---|---|---|
| 2.1.1 | Modellierung BPMN 2.0 | process studio: „Prozesse mithilfe der Spezifikationssprache BPMN … modellieren"; webbasierter Modeller, **Drag & Drop**; Oberfläche Navigation (Modellierung, Betrieb, Hilfe, Einstellungen), Palette / Modellierungsbereich / Konfigurationsbereich | B | [B_04 §1B, §2; PSU:bedienung/grundlegende-bedienung] |
| 2.1.2 | Komponententypen | Automatisierungen, Routinen, Prozesse, Formulare, Skripte, Geschäftsregeln | B | [B_04 §1B] |
| 2.1.3 | On-Premises | Administrationshandbuch d.velop process (On-Prem) beschreibt Modellierung als **BPMN-XML von Hand** (`camunda:`-Attribute); Empfehlung process modeler | E | [B_04 §2; PA:modellieren-von-prozessen/wissenswertes-zur-prozessmodellierung] |
| 2.1.4 | Klassische d.3-Workflows | d.3 flow designer (Plugin für d.3 cockpit), d.3 flow inspector; Anwender: Kontextaktion „Workflow starten"; Fälligkeitsfarben (grün/gelb/beige/rot) | E (Doku gesperrt) | [B_04 §1A; ONE:tipps-und-tricks/arbeiten-mit-workflows-und-dokumenten] |
| 2.1.5 | Einsteigerwerkzeug | d.ecs kickstart4process (Aktivitäten auswählen, Formulare, kein BPMN-Editor; Einmalausführung) | B | [B_04 §1C, §10] |
| 2.1.6 | „smart process" | nicht gefunden | N | [B_04 §1D] |

### 2.2 BPMN-Bausteine, Parallelität, Bedingungen

| Nr | Fähigkeit | Belegte Funktion (Fakt) | Status | Hinweis | Quelle |
|---|---|---|---|---|---|
| 2.2.1 | Ereignisse | Start (auch Timer-Start; Eskalations-/Fehler-Start in Ereignis-Subprozessen), Ende (Terminierung, Eskalation, Fehler), angeheftete Timer-/Fehler-Zwischenereignisse (unterbrechend/nicht unterbrechend), eintretendes Timer-, ausgelöstes Eskalations-Zwischenereignis | B | – | [B_04 §3; PSU:funktionen/grundlegende-funktionen] |
| 2.2.2 | Aktivitätstypen | Benutzeraufgabe, **Externe Benutzeraufgabe** (Empfänger = E-Mail, zwingend d.velop forms + Timer), Sendenaktivität (synchroner Service), Empfangenaktivität (asynchron), Serviceaktivität (Variablenzuweisung), Geschäftsregel-Aufgabe, **Aktion** (wiederverwendbar, nicht BPMN-Standard) | B | Externe Benutzeraufgabe = möglicher Baustein für externe Freigeber (**A**, Lizenz offen) | [B_04 §3] |
| 2.2.3 | Parallel/Sequenziell | Exklusive, **Parallele**, Inklusive Verzweigung; Subprozesse, Ereignis-Subprozesse, **Parallele**/**Sequenzielle Multi-Instanz** | B | Parallelprüfung mehrerer Fachbereiche möglich | [B_04 §3] |
| 2.2.4 | Pools/Lanes | max. **ein Pool** je Prozessdiagramm | E | – | [B_04 §3] |
| 2.2.5 | Prozessvariablen | Datentypen Text, Zahl, Wahrheitswert, DMS-Dokument, Identität, Objekt, Datei (Tabellen zusätzlich URL); Pflicht-/Start-/Mehrfachwert; max. **200** Variablen; Präfix `dv_` reserviert; Zahl ±1e16, 5 Nachkommastellen, 15 Stellen Genauigkeit | B | – | [B_04 §4a] |
| 2.2.6 | Bedingungen | Ausgangspfade exklusiver Verzweigungen brauchen Bedingung; Zugriff `{Variablenname}`; Operatoren `+ - * / % = ! < > & | ? ( ) [ ]`, Keywords `div mod eq ne lt gt le ge and or not empty`; Standardsequenzfluss | E | Nur String-Beispiel `{check} == "yes"` im Web-Editor; Zahlenvergleich nur On-Prem-XML `#{variables.get("amount") > 1000}` → **Syntax testen** | [B_04 §4b, §4c; PA:modellieren-von-prozessen/verwenden-von-verzweigungen] |
| 2.2.7 | Geschäftsregeln | Vergleichsoperatoren, Bereich `[10..20]`, `REGEX(…)`; Entscheidungsrichtlinien Beliebige/Erste/Eindeutige Übereinstimmung, Sammeln (Summe/Anzahl/Min/Max); Einsatz u.a. zur **Empfängerbestimmung** | B | Fachbereich kann Schwellen/Zuständigkeiten pflegen (z.B. Gesellschaft → Freigeber) (**A**) | [B_04 §4d] |

### 2.3 Formulare, Aufgaben, Zuständigkeiten

| Nr | Fähigkeit | Belegte Funktion (Fakt) | Status | Hinweis | Quelle |
|---|---|---|---|---|---|
| 2.3.1 | Formulare | Benutzeraufgabe: Formulartyp Kein Formular / **d.velop forms** / Externes Formular; Startformular zusätzlich **Generiertes Formular** (aus Startvariablen); Vorschaufunktion für Formulare | B | Formularfeldtypen/-logik in Quelle nicht detailliert (**N**) | [B_04 §5, §8c, §10] |
| 2.3.2 | Aufgaben | Benutzeraufgabe an **1–n Personen und/oder Gruppen** → Aufgabe in der Aufgabenverwaltung (d.ecs task); Gruppen haben eigene Aufgabenliste; „Aufgabe übernehmen" nur bei Gruppenaufgaben; Aktionen Erledigen/Weiterleiten/Aufgabe übernehmen ein-/ausblendbar; Abschluss in Details/Liste; **Aufbewahrungszeit** 30 Tage (0–365) | B | Klärungskorb = Gruppenaufgabe (**A**) | [B_04 §5; TU:weitere-funktionen-und-einstellungen/wissenswertes-zu-aufgabenlisten] |
| 2.3.3 | Zuständigkeit statisch | Feld **Versenden an** (Person/Gruppe) | E | Label-Widerspruch „Empfänger" vs. „Versenden an" in der Doku | [B_04 §2, §5] |
| 2.3.4 | Zuständigkeit dynamisch | Variablenmodus über Button (X); nur Variablen vom Typ **Identität** (`identity:///identityprovider/scim/users/<id>` bzw. `/groups/<id>`); Details `{Var[scim.name.familyName]}`, `{Var[identity.isGroup]}` | B | Zuständigkeit aus Dokumenteigenschaft (z.B. Gesellschaft → Gruppe) via Geschäftsregel/Startvariable (**A**) | [B_04 §5] |
| 2.3.5 | Rollen | „Rolle" als Zuweisungsobjekt **nicht dokumentiert**; Rollen nur als Berechtigungsrollen (z.B. „Administration") | N | Rollen über Gruppen abbilden (**A**) | [B_04 §5; B_06 §10c] |
| 2.3.6 | Vorgesetzten-Ermittlung | Begriff in d.ecs userprofile (LDAP-Attribut `manager`), **Prozesszugriff nicht dokumentiert** | N | Workaround Geschäftsregel „Abteilung → Vorgesetzter" | [B_04 §6c, Offene Punkte 3] |
| 2.3.7 | Systemvariablen | `dv_initiator`, `dv_sender`, `dv_attachment` (Dokument/Akte als Anhang), `dv_comment`, `dv_decision`, `dv_start_time` | B | Beleganzeige in Aufgabe über `dv_attachment` | [B_04 §5] |
| 2.3.8 | Aufgabenmetadaten | Beschriftung/Typ/Schlüssel/Wert (statisch oder Variable, gemischt) | B | Basis für Vertretungsregeln je Kontext/Metadatum (z.B. Gesellschaft) (**A**) | [B_04 §5] |

### 2.4 Start, Fristen, Eskalation, Benachrichtigung

| Nr | Fähigkeit | Belegte Funktion (Fakt) | Status | Hinweis | Quelle |
|---|---|---|---|---|---|
| 2.4.1 | Automatischer Start bei Dokumentimport | Startereignis > **Start über Ereignis** > Ereignis wählen > **Bedingungen** (auch **JSON-Logik**, Beispiel: „Dokument … das zur Kategorie Rechnungen gehört") > **Startvariablenzuordnung** (auch **JSON-Pfad**) | B | Welche Felder das Ereignis liefert: **N** | [B_04 §8a, Offene Punkte 6] |
| 2.4.2 | Manueller Start am Dokument | **Start über Integration**: „Prozesse zum Dokument verwalten" (keine Einschränkung auf Gruppe/Benutzer möglich); „Start als Aktion bereitstellen" (Aufruf aus anderem Prozess) | B / E | – | [B_04 §8b] |
| 2.4.3 | Start über Formular | Kein Formular / d.velop forms / Externes Formular / Generiertes Formular | B | – | [B_04 §8c] |
| 2.4.4 | Zeitgesteuerter Start | Timer-Startereignis Stunde/Tage/Wöchentlich/Benutzerdefiniert (CRON, 7 Felder); **kleinstes Intervall 1 Stunde** | B | – | [B_04 §8d; PSU:funktionen/erweiterte-funktionen] |
| 2.4.5 | Fristen | angeheftetes Timer-Zwischenereignis: **Dauer** (Minuten … Monate bzw. ISO 8601, z.B. `P5D`) oder **Datum**; unterbrechend vs. nicht unterbrechend (Erinnerung ohne Aufgabenentzug) | B | „X Tage unbearbeitet" abbildbar | [B_04 §6a] |
| 2.4.6 | Eskalation | Eskalationsereignis (Name, Code) am Prozess; ausgelöstes Eskalations-Zwischenereignis; Ereignis-Subprozess mit Eskalations-Startereignis (nicht unterbrechend), optional Variable für Eskalationscode | B | Fünf Konfigurationsschritte an vier Elementen (aufwendig) | [B_04 §6b; PA:modellieren-von-prozessen/verwenden-von-eskalationen] |
| 2.4.7 | Benachrichtigung | d.ecs task: „Versenden von Benachrichtigungen aktivieren" (neue Aufgaben, **Erinnerung an existierende Aufgabe**) über Message-Center; Externe Benutzeraufgabe = E-Mail an Adresse; Aktion „Versenden einer Benachrichtigung" nur als Beispiel | E | **Aktionskatalog (E-Mail-Aktion) N**, umgebungsabhängig | [B_04 §6c, Offene Punkte 2; TA:tipps-und-tricks/konfigurieren-von-benachrichtigungen] |

### 2.5 Skripte, Aktionen, Integration, Betrieb

| Nr | Fähigkeit | Belegte Funktion (Fakt) | Status | Hinweis | Quelle |
|---|---|---|---|---|---|
| 2.5.1 | Skripte | d.velop scripting; Testbereich über „Testen" | B | JavaScript-Kenntnisse nötig (Einschätzung B_04) | [B_04 §1B, §10, Aufwand W3] |
| 2.5.2 | Aktionen | Bereich **Aktion** → Aktion wählen, Eingangs-/Ausgangsmappings, Parameter, „Ausführung durch" = Benutzerdefiniertes Konto; Aktionen verfügbar, „sobald die zugehörige d.velop-Komponente in der Umgebung vorhanden ist"; d.velop actions eventbridge | E | Katalog N | [B_04 §1B, §6c] |
| 2.5.3 | HTTP/REST-Integration | Sendenaktivität (synchroner Service, „nur für fortgeschrittene Prozesserstellende"), Empfangenaktivität (asynchron); konkrete HTTP-Konfiguration (URL, Auth) **nicht beschrieben** | E | Detail-Klickweg N | [B_04 §3] |
| 2.5.4 | Mandantenlogik | kein eigenes Mandantenkonzept in process studio dokumentiert; Stammdaten-Lookup „Rechnungsempfänger ist hinterlegte Gesellschaft" als Baustein **N** – machbar über Geschäftsregel/Skript/Aktion | N / A | – | [B_04 Offene Punkte 11] |
| 2.5.5 | Überwachung | Betrieb > Überwachung > **Prozessüberwachung**: Instanzen laufend/abgeschlossen/abgebrochen/fehlerhaft, Suche Business Keys/Versionen/Aktivitäten, Filter Status; Instanz abbrechen (mit Grund), Diagramm (aktueller Schritt), Protokoll, Variablen bearbeiten, Migration; Tokenliste mit **Erstellungszeit**, Token verschieben | B | Liegezeit-Spalte **N** | [B_04 §9] |
| 2.5.6 | Protokollierung | pro Prozess aktivieren (Bereitstellen > Prozessprotokollierung und Aufbewahrung); Export der Protokolle ins Repository (revisionssicher); Löschung nach Aufbewahrungszeit; fachliche/technische Ansicht; Standard 30 Tage, bis 1 Jahr | B | Protokollexport ins DMS für Revision | [B_04 §9] |
| 2.5.7 | Versionierung/Transport | Bereitstellen erzeugt Versionen; Migrieren offener Instanzen; Version löschen erst nach Beenden aller Instanzen; Export/Import von **Automatisierungen** (Prozesse, Formulare, Skripte, Geschäftsregeln) – Import nur Rolle **Administration** | B | Test→Produktiv-Transport möglich | [B_04 §10] |
| 2.5.8 | Testen | **kein Testmodus/Simulation/Sandbox** für Prozesse; Ersatz: Berechtigungen > **Nutzung** nur für Testkreis | N | Test-Instanz/Testkreis einplanen | [B_04 §10] |

### 2.6 Vertretung (plattformweit, d.ecs userprofile / d.ecs task)

| Nr | Fähigkeit | Belegte Funktion (Fakt) | Status | Hinweis | Quelle |
|---|---|---|---|---|---|
| 2.6.1 | Abwesenheit | Profilbild > **Abwesenheitsstatus**: Start (Uhrensymbol = jetzt), optional Ende (ohne Ende unbegrenzt), Vertretung, Nachricht; für andere Benutzer mit administrativen Rechten (z.B. Vorgesetzte) | B | Geplant (Urlaub) und ungeplant (Krankheit, durch Vorgesetzten) abbildbar | [B_04 §7a; UP:erste-schritte/konfigurieren-des-abwesenheitsstatus] |
| 2.6.2 | Wirkung | Vertretung „übernimmt die Berechtigungen"; Vertreter **sieht** in der Aufgabenliste (Bereich Vertretung) Aufgaben, die dem Abwesenden **als alleinigem Empfänger** zugestellt wurden – **kein automatischer Übergang** | E | Sprachregelung gegenüber Livos | [B_04 §7b; TU:weitere-funktionen-und-einstellungen/vertreten-einer-person] |
| 2.6.3 | Vertretung je Aufgabentyp | Admin: Konfiguration > Aufgaben > Aufgaben und Prozesse > **Vertretungsregeln** (Kontext, z.B. „Rechnung", + Metadaten-Bedingungen per technischem Schlüssel); Anwender: … > **Vertretung**; sonst Standardvertretung; **Vertretungsausschluss** („Vertretung möglich" deaktivieren) hebt andere Regeln auf | B | Nur **interne Aufgabenmetadaten** nutzbar, keine Dokumenteigenschaften | [B_04 §7c–7e; B_06 §10e] |
| 2.6.4 | Verantwortungsregeln | verantwortliche Personen/Gruppen sehen alle Aufgaben eines Kontextes und können weiterleiten | E | **nur für per API erstellte Aufgaben** | [B_04 §7f] |

---

## 3. Postverteilung / Mailimport / inbound

### 3.1 Posteingangsszenarien

| Nr | Fähigkeit | Belegte Funktion (Fakt) | Status | Hinweis | Quelle |
|---|---|---|---|---|---|
| 3.1.1 | Papierpost-Prozess | 8 Arbeitsschritte (u.a. Vorbereiten, Stapelbildung + Barcodes, inbound-Stapel, Scannen, Nachbearbeitung, Indexieren, Ablage als Postdokument, automatische Verteilung per Aufgabe); **pro Empfangsgruppe ein Stapel**; Prüfkriterien Trennung, Seitenreihenfolge, Vollständigkeit, Lesbarkeit | B | Zentrale Poststelle Livos (**A**) | [B_06 §2a, §2c; MDU:aufgabenstellung-von-dvelop-mail-dispatcher/prozess-der-posteingangsbearbeitung] |
| 3.1.2 | Nicht im Standard | „E-Mail-Eingänge via Funktionspostfächer", „Online-Anträge", „intelligenter Posteingang", „ersetzendes Scannen nach TR-RESISCAN" – nur in gesonderten Projekten | E | E-Mail-Post in mail dispatcher = Projekterweiterung | [B_06 §2a] |
| 3.1.3 | Mail-Postfächer | email import (M365/Graph, Alias je Postfach) bzw. inbound e-mail (Push, zugelassene Absender) – siehe 1.1.1–1.1.3; Ordner **dvelop_finished**/**dvelop_not_processed**; **alle vorhandenen** Mails im Posteingang werden importiert | B | Vor Aktivierung Postfach bereinigen | [B_06 §4e; EMI:informationen-zur-verarbeitung-der-e-mails-im-postfach] |
| 3.1.4 | Import-Intervall | **nicht dokumentiert** (Suche „Intervall/Abruf/Zyklus/Polling/Minuten…") | **N** | – | [B_06 §4g] |
| 3.1.5 | Monitoring Mailimport | **Jobübersicht**: Status (Datei wird hochgeladen, In Warteschlange, In Verarbeitung, Erfolgreich, Fehler), Fehlertext, Service, Exportreferenz, Zeitstempel; Layout E-Mail mit Betreff/Absender/Postfach/Empfangsdatum; Aktionen Aktualisieren/Löschen/Neustarten | B | – | [B_06 §4f; EMI:uberwachen-von-e-mails-in-der-jobubersicht] |
| 3.1.6 | Manuelle Mailablage | Outlook/HCL-Notes-Add-In: „E-Mail ablegen", „Anlagen ablegen", Drag & Drop (Schnellaktionen „Ablegen"/„Ablegen In"); Speicherung in standardisiertem XML-Format | B | – | [B_06 §5; e-mail-integrationen/1.28.0] |
| 3.1.7 | Mobiles Scannen | d.velop mobile existiert, Doku gesperrt | N | – | [B_06 §7g] |
| 3.1.8 | **Scandienstleister** | nicht beschrieben | **N** | Einlieferung über inbound-API, E-Mail-Postfach oder Dateiimport denkbar (**A**) | [B_06 §3 (API), Volltext] |

### 3.2 Klassifizierung

| Nr | Fähigkeit | Belegte Funktion (Fakt) | Status | Hinweis | Quelle |
|---|---|---|---|---|---|
| 3.2.1 | Standardkategorie je Importprofil | „mit welcher Kategorie neue Dokumente standardmäßig … importiert werden" | B | Alias/Postfach → Importprofil → Kategorie | [B_06 §6b] |
| 3.2.2 | RegEx auf OCR-Text → Kategorie | Konfiguration > Import > Importoptionen > Kategorien und Eigenschaften > Regulärer Ausdruck; Seite: alle oder feste Seite 1–99 | E | **Treffen mehrere RegEx verschiedener Kategorien, wird keine Kategorie gesetzt** | [B_06 §6c; ISA:…/verwalten-von-regularen-ausdrucken-fur-kategorien] |
| 3.2.3 | RegEx → Eigenschaft | Konfiguration > Dokumentaufbereitung > Kategorien und Eigenschaften; Format/Zeitzone für Datum | B | – | [B_06 §6d] |
| 3.2.4 | KI-Dokumentanalyse | Kategorie → **Prozesskategorie**, Eigenschaft → **Prozesseigenschaft** | B | Liste verfügbarer Prozesskategorien **N** | [B_06 §6e] |
| 3.2.5 | Barcode → Eigenschaft | Eigenschaft > Barcode > Barcodeprofil, Seite, optional RegEx | B | – | [B_06 §6f] |
| 3.2.6 | Vorbelegung Zielkategorie | technisches Feld `MailPreselectedCategoryId` („Angabe der Zielkategorie direkt aus d.velop document reader") | E | Nur als Feldbeschreibung belegt | [B_06 §10d] |
| 3.2.7 | Manuelle Klassifizierung | Konzept: Kategorie „Posteingang/Postdokument" ohne Attribute; Klassifizierung im Nachgang manuell (Kategorie Postdokument → Zielkategorie); „Es ist für mich" > Archiv > Kategorie > **Ablegen** (Aufgabe automatisch quittiert) | B | – | [B_06 §2b, §2e; MDU:hauptansicht-bearbeitungsansicht] |
| 3.2.8 | Regelwerk Absender/Betreff | **keine eigene Regeloberfläche**; `%Sender%`/`%Subject%` nur Platzhalter für Stapelnamen und Schlüssel-Wert-Paare | N | Absenderbasierte Steuerung nur via Alias/Postfach (**A**) | [B_06 §6, Offene Punkte 10] |
| 3.2.9 | Records-Management-Klassifizierung | Projekttemplate: „Posteingänge durch d.velop records management klassifizieren" | E | nur als Funktionsliste belegt | [B_06 §1] |

### 3.3 Verteilung, Aufgaben, Ablage

| Nr | Fähigkeit | Belegte Funktion (Fakt) | Status | Hinweis | Quelle |
|---|---|---|---|---|---|
| 3.3.1 | Verteilung an Gruppen | Best Practice: an **(Funktions-)Gruppen**, nicht an Personen („reduziert Liegezeiten im Krankheits- und Vertretungsfall"); **Person als Erstempfänger → keine Aufgabe** („Geben Sie zunächst immer eine Gruppe … an") | B | Gesellschafts-/Funktionsgruppen für Livos (**A**) | [B_06 §10a; MDA:haufig-gestellte-fragen/warum-wird-keine-aufgabe-erstellt] |
| 3.3.2 | Empfängerquellen | Identity Provider (empfohlen; dann **keine dedizierten Eskalationsmanager**, immer Fallback-Gruppe) oder individuelle Listen / d.velop business objects („Eskalationsobjekte anlegen"); Wertemengenhook `dv.maildispatcher.recipients`; globale Gruppen in User Management-App | B | – | [B_06 §10b] |
| 3.3.3 | Fallback/Clearingstelle | ohne Empfängergruppe → feste Gruppe (**Clearingstelle**); On-Prem-Option **Fallback-ID/Fallback-Name** | B | Livos-Klärungskorb Post | [B_06 §2b, §2g] |
| 3.3.4 | Weiterleitung | Optionen **Es ist für mich**, **An Kollegen\*in senden** (Benutzer oder Abteilung + Unterverteilung, vordefinierter/individueller Kommentar), **An Posteingang senden** (ohne eigene Beschreibung); Mehrfachweiterleitung mit Protokoll; bis **20 Schnellaktionen** (Favoriten) | B / E | – | [B_06 §2e, §2g, Offene Punkte 11] |
| 3.3.5 | Aufgaben | Widget **Aufgaben**; Betreff z.B. „Digitaler Posteingang: Empfänger:in prüfen", Kontext „Postverteilung"; Seitenleiste Meine Aufgaben / An mich gesendet / An mich und andere gesendet / **Gruppenpostkörbe**; erste öffnende Person übernimmt (Sperre); Felder Betreff, Kontext, Fällig, Erinnerung, Erhalten, Zugestellt an, Versendet von | B | – | [B_06 §2d, §10d; MDU:seitenleiste-aufgabenubersicht] |
| 3.3.6 | Erinnerung/Eskalation | systemseitige Erinnerung an Empfängergruppe nach definierbarem Zeitraum (Tage); `MailPriority` „normal" = **14 Tage** bis Eskalation | B | Liegezeit-Steuerung Post | [B_06 §2b, §10d, §10e] |
| 3.3.7 | Ablage in Akten | Projekttemplate: „mit d.velop object transfer service in die Zielakte umhängen"; „Es ist für mich" mit abweichendem Archiv + Kategorie; „Scannen in Akte" aus geöffneter Akte | E | Automatische Aktenzuordnung über Kategorie/Eigenschaften (**A**, Aktenlogik s. B_03) | [B_06 §1, §2e, §7d] |
| 3.3.8 | Vertretung | kein eigener Dialog im mail dispatcher; Plattform-Vertretung (d.ecs userprofile/task); inbound: Vertretungen bei Sichtbarkeit von Stapeln optional, ggf. verzögert wirksam | E | – | [B_06 §10e; ISA:…/erteilen-von-berechtigungen] |

### 3.4 Trennblätter, Barcodes, Scantechnik

| Nr | Fähigkeit | Belegte Funktion (Fakt) | Status | Quelle |
|---|---|---|---|---|
| 3.4.1 | Dokumenttrennung | Importprofil „Seiten und Dokumente": Trennung nach importierten Dateien, Seitenzahl, **Barcodes**, RegEx oder **KI**; Trennung nach wechselndem Barcodewert (erfordert RegEx, deaktiviert „Seite mit Barcode verwerfen") | B | [B_06 §7] |
| 3.4.2 | Barcodeprofile | Konfiguration > Dokumentenmanagement > Import > Barcodeprofile > Verwalten von Barcodeprofilen > Neues Profil (Typen, Ausrichtungen); Standardprofil erkennt alle unterstützten Barcodes | B | [B_06 §7; ISA:…/erstellen-von-barcodeprofilen] |
| 3.4.3 | Trennblatt-Praxis | Barcode als Dokumententrenner, bei Urkunden auf leerem Vorblatt; eindeutig kodiert; **Code 128** | B | [B_06 §7] |
| 3.4.4 | Manuelle/KI-Trenner | Pluszeichen zwischen Seiten; Farben orange (möglicherweise unzutreffend), blau (wahrscheinlich korrekt), grün (manuell); Hand-Symbol | B | [B_06 §7; ISU:weitere-funktionen-und-einstellungen/arbeiten-mit-dokumenttrennern] |
| 3.4.5 | OCR/PDF | „Texterkennung", „Durchsuchbare PDF-Dateien erzeugen" (Datei ggf. größer), „erweiterte Dokumentanalyse"; Seitenanalyse-Neustart über Ausrufezeichen | B | [B_06 §8] |
| 3.4.6 | Volltextsuche Repository | d.3 search (eigenes Produkt) | B | [B_06 §8] |

### 3.5 Technische Einrichtung mail dispatcher (Fakt)
- Servicebenutzer per **API-Schlüssel**; Benutzer/Gruppe **nicht** in der d.velop-documents-Benutzerverwaltung anlegen; d.3-Benutzerkontenprovider im identity provider nicht unterstützt. [B_06 §1]
- Postdokumente müssen **im Status Freigabe** importiert werden. [B_06 §1]
- Best-Practice-Kategorie **Postdokument (DPOST)** mit Pflichtfeldern `mailid`, `mailtype` (scanned/physical), `mailpriority`, `mailidpid`; optional `mailcomment`, `mailbarcode`, `mailreceiptdate`. [B_06 §1; MDA:konfigurieren-von-dvelop-mail-dispatcher]
- Start per **Webhook** („Nach dem Erstellen eines Dokuments oder einer Akte", URI `/maildispatcher/api/v1/webhook/start_workflow`, Timeout z.B. 5.500 ms). Cloud: **Einrichtungsassistent** erstellt Webhooks. [B_06 §2f, §2h]
- **Zuordnungen**: Quelle „Mail Dispatcher Workflow" → nur **eine** Postkategorie. [B_06 §2h]
- Installation „ausschließlich über d.velop software manager" (inbox management) + d.velop object transfer service – steht im Cloud-Handbuch, wirkt On-Prem-orientiert (**E**, für Cloud klären). [B_06 §1]

---

## 4. Vertragsmanagement

**Befund:** In B_02, B_04 und B_06 wird **kein Vertragsmanagement-Produkt** (z.B. „d.velop contract") erwähnt. [Volltextsuche „Vertrag|contract" in B_02/B_04/B_06: kein Treffer]

Indirekt nutzbare, belegte Bausteine (Zuordnung = **Annahme**):
- Erfassung von Vertragsdokumenten über inbound (Scan, Mail-Alias, Upload) mit Kategoriezuordnung per Standardkategorie, RegEx oder KI-Dokumentanalyse. [B_06 §6]
- Verteilung/Klassifizierung über mail dispatcher (Postdokument → Zielkategorie „Vertrag"). [B_06 §2b, §2e]
- Fachliche Freigabe von Verträgen als process-studio-Prozess (Benutzeraufgaben, Gateways, Formulare, Fristen via Timer, z.B. Kündigungsfristen-Erinnerung per Timer-Datum aus Prozessvariable). [B_04 §3, §6a, §8]
- Querverweis außerhalb dieses Teils: B_03 §7d „Aktenbildung Erkennung" nennt „Mietvertragsakte Objekt X / Gesellschaft" als Beispiel für Akten mit Erkennungseigenschaft „Gesellschaft". [B_03 §7d]

**Lücke:** Fristenmanagement, Vertragsakte, Wiedervorlage, Vertragsstammdaten, Lizenz eines Vertragsprodukts – siehe §7 (R-15).

---

## 5. Belegte Grenzen / Einschränkungen

| ID | Bereich | Einschränkung (Fakt) | Wirkung auf Livos (Bewertung) | Quelle |
|---|---|---|---|---|
| G-01 | Mandantenerkennung | Kriterien sind **Name + Adresse**; USt-IdNr/Steuernummer nur beim Kreditor | Gesellschaften mit gleicher Anschrift nur über Namen unterscheidbar → Trefferquote offen | [B_02 §4] |
| G-02 | Generische Adressdatenerkennung | standardmäßig aus, setzt keine Mandanten-/Lieferantennummern | kein sinnvoller Fallback für Mandanten | [B_02 §4] |
| G-03 | Mehrere Stammdatenbuckets | nur Vorschau-Feature-Flag; d.velop empfiehlt einen Bucket | Ein Bucket für alle Gesellschaften planen | [B_02 §4] |
| G-04 | E-Rechnungsvalidierung | **nur XRechnung** wird validiert; ZUGFeRD nicht | ZUGFeRD-Prüfung organisatorisch/anders lösen | [B_02 §7] |
| G-05 | Prüfbericht | in inbound und document reader visuell nicht verfügbar, nur als Anhang im Repository | Prüfbericht erst nach Ablage sichtbar | [B_02 §7; B_06 §9b] |
| G-06 | Dublette document reader | nur gegen **validierte** Belege | Dubletten vor Validierung unentdeckt | [B_02 §8] |
| G-07 | Duplikatsprüfung smart invoice | Zeitfenster **18 Monate**; nur Warnung (mit Begründung), kein Stopp | – | [B_02 §8] |
| G-08 | Erweiterte Prüfung | nur **ein** Prüfungsschritt pro Workflow; nicht mit automatischem Bestellabgleich | Mehrstufige Fachprüfung über Prüfungstypen innerhalb eines Schritts | [B_02 §8] |
| G-09 | Freigabematrix | max. **20** Zusatzspalten; Auswertung **case-sensitive** | Stammdatendisziplin nötig | [B_02 §6B] |
| G-10 | Freigabegrenze | gilt **pro Kostenobjekt**, nicht pro Rechnung | Gesamtbetrag > Grenze kann durch Teilfreigaben freigegeben werden | [B_02 §6B] |
| G-11 | Vier-Augen-Prinzip | **Vorschau-Feature** (Support); sachliche Prüfer nicht berücksichtigt; Menüpfad nicht dokumentiert | Nicht als GA-Feature zusagen; Alternative: Wertgrenze per Schrittverbindung | [B_02 §6] |
| G-12 | Beträge in Bedingungen | in **Cent** | Konfigurationsfehlerquelle | [B_02 §6A] |
| G-13 | Rechnungseingangsbuch-Archiv | 6 Monate, erweiterbar auf 12 Monate | Langfristrecherche außerhalb REB | [B_02 §2] |
| G-14 | CSV-Export REB | Download 30 Tage verfügbar | – | [B_02 §9] |
| G-15 | D365-Integration | nach 7 Tagen erfolgloser Sync deaktiviert | Analog für andere Integrationen prüfen | [B_02 §9] |
| G-16 | DATEV | Handbücher nicht öffentlich; Format/Intervall unbekannt | Must-have 5.1 nicht belegbar | [B_02 §9] |
| G-17 | Bau-Spezifika | Abschlag, §13b, Einbehalt nicht dokumentiert | Customizing (Custom-Felder) | [B_02 §10] |
| G-18 | Aufteilungsschlüssel | in d.velop invoices nicht vorhanden (nur alphaflow) | Umlagen manuell/über Positionen | [B_02 §5] |
| G-19 | process studio – Pool | max. ein Pool je Diagramm | – | [B_04 §3] |
| G-20 | process studio – Variablen | max. 200; `dv_` reserviert; Zahl ±1e16 / 15 Stellen | – | [B_04 §4a] |
| G-21 | process studio – Timer-Start | kleinstes Intervall **1 Stunde** | – | [B_04 §8d] |
| G-22 | process studio – Test | kein Testmodus/Simulation/Sandbox | Testkreis über Berechtigungen „Nutzung" | [B_04 §10] |
| G-23 | process studio – Migration | Typwechsel von Variablen zwischen Versionen → Fehler möglich; Versionslöschung erst nach Ende aller Instanzen | Versionierungsdisziplin | [B_04 §10] |
| G-24 | process studio – Transport | Import von Automatisierungen nur Rolle Administration | – | [B_04 §10] |
| G-25 | process studio – Start am Dokument | „Prozesse zum Dokument verwalten" nicht auf Gruppe/Benutzer einschränkbar | – | [B_04 §8b] |
| G-26 | process studio – Aufbewahrung | Protokoll Standard 30 Tage, max. 1 Jahr; Aufgaben-Aufbewahrung 0–365 Tage | Revisionsprotokolle ins Repository exportieren | [B_04 §5, §9] |
| G-27 | Externe Benutzeraufgabe | zwingend d.velop-forms-Formular und Timer | – | [B_04 §3] |
| G-28 | Rollen | keine Rolle als Aufgabenempfänger (nur Person/Gruppe) | Rollen als Gruppen abbilden | [B_04 §5; B_06 §10c] |
| G-29 | Vertretung | kein automatischer Aufgabenübergang; Vertreter sieht nur Aufgaben, bei denen Abwesender **alleiniger** Empfänger ist; Regeln nur mit internen Aufgabenmetadaten | Erwartungsmanagement | [B_04 §7b; B_06 §10e] |
| G-30 | Verantwortungsregeln | nur für per API erstellte Aufgaben | – | [B_04 §7f] |
| G-31 | email import | nur **eine** Verbindung/Bereitstellungsform; IMAP „zukünftig"; Exchange On-Prem widersprüchlich | M365-Voraussetzung für Pull-Import | [B_06 §4a] |
| G-32 | email import | importiert **alle vorhandenen** Mails; Graph-Berechtigung greift auf **jedes Postfach** (per PowerShell-Richtlinie einschränken) | IT-Security-Freigabe nötig | [B_06 §4b, §4e] |
| G-33 | email import | Abrufintervall nicht dokumentiert | Durchlaufzeit nicht zusagbar | [B_06 §4g] |
| G-34 | RegEx-Klassifizierung | bei Mehrfachtreffern verschiedener Kategorien keine Kategorie | Regeln trennscharf halten | [B_06 §6c] |
| G-35 | Import-Widget | max. 4 Dropzones je Widget | – | [B_06 §7c] |
| G-36 | Scanner connector | max. 1000 Scannereinträge | – | [B_06 §7] |
| G-37 | mail dispatcher | Person als Erstempfänger → keine Aufgabe; Identity-Provider-Option schließt dedizierte Eskalationsmanager aus; nur eine Postkategorie in Zuordnung; max. 20 Schnellaktionen | Gruppenmodell zwingend | [B_06 §2g, §2h, §10a, §10b] |
| G-38 | mail dispatcher | E-Mail-Eingänge via Funktionspostfächer, intelligenter Posteingang, TR-RESISCAN nicht im Standard | Projekterweiterung | [B_06 §2a] |
| G-39 | Stapel-Vertretung | Vertretungen können verzögert wirksam werden | – | [B_06 §10e] |
| G-40 | Öffentliche Doku | Workflow-Masken-Anwenderhandbuch smart invoice, document-reader-invoice, DATEV, d.3 flow, rendition service, smart inbox, mobile nicht öffentlich | Partnerzugang erforderlich | [B_02 Vorbemerkung, Offene Punkte 2; B_04 §0; B_06 Offene Punkte 3–6] |

---

## 6. Dokumentierte Konfigurationsschritte (Menüpfade)

### 6.1 d.velop invoices / smart invoice / document reader / eInvoice converter

| # | Ziel | Menüpfad / Schritte (laut Doku) | Quelle |
|---|---|---|---|
| K-01 | Grundaufbau | Onboarding-Assistent: erzeugt Workflow (Verteilung, Prüfung, Freigabe, Buchhaltung), Aktenplan, Gruppen, Eigenschaften, Importprofile, Eingangspostfächer, Erkennungsbackend | [B_02 §2; SI:wissenswertes-zum-onboarding] |
| K-02 | Schritt anlegen | Schritte > Neuer Schritt > Titel > Bearbeiterfindung > Schritttyp > Hinzufügen | [B_02 §2] |
| K-03 | Wertgrenze 10.000 EUR | Schritt „Freigabe Geschäftsleitung" + Bearbeiterfindung Gruppe; in Schritt „Freigabe Einkauf" > Perspektive Aktionen > Aktion „Freigeben" > neue Verbindung mit Bedingung `voucher.net_amount >= 1000000` > Freigabe: Erteilen > Verbindung per Drag & Drop über Standardverbindung | [B_02 §6A] |
| K-04 | Freigabematrix | Administration > Freigabematrizen > Neue Matrix > Name > Spalte (z.B. Kostenstelle/Mandant) hinzufügen > Speichern; Zeile hinzufügen > Person > Grenze > Kostenstelle > Speichern | [B_02 §6B] |
| K-05 | Freigabeschritt mit Matrix | Workflowablauf > Schritte > Neuer Schritt > Schritttyp Freigabe > Bearbeiter: Matrix > Strategie Direkt > Netto/Brutto > Hinzufügen; Strategie ändern: Allgemein > Strategie > „Von Unten zum Freigeber" | [B_02 §6B] |
| K-06 | Freigabe überspringen | Workflowablauf > Workflowdefinition > Schritte > Freigabe > Aktionen > „Rechnung freigeben" > Bearbeiten > Standardaktion aktivieren > Allgemein > „Automatisch Freigaben für Prüfer erzeugen" | [B_02 §6] |
| K-07 | Rechnerisch richtig | Schritt „Sachliche Prüfung" > Aktionen > Verbindung zu „Freigabe" > Bearbeiten > Rechnerisch Richtig: Erteilen | [B_02 §8] |
| K-08 | Sachliche Prüfer | Schritt: Bearbeiterfindung `user.name IN voucher.outstanding_verifiers`, „Alle Treffer verwenden"; Workfloweinstellungen > Sachliche Prüfung > Plus > Bedingung `/^SP_.*$/ ~= user.name` | [B_02 §8] |
| K-09 | Erweiterte Prüfung | Workflow > Einstellungen > Prüfen > Prüfung hinzufügen (Prüfungstyp, Prüfer, aktiv, Reihenfolge); Schritt Typ Prüfung, optional Prüfungsmatrix; Felder „geprüft?"/„Prüfung" | [B_02 §8] |
| K-10 | Clearing | Workflowdefinition > Einstellungen > Clearing > aktivieren; Berechtigungen Standard für Alle > Gruppe; Berechtigung hinzufügen > Mandanten-ID > Gruppe | [B_02 §8] |
| K-11 | Duplikatsprüfung | Workfloweinstellungen > Abschnitt Duplikatsprüfung aktivieren > speichern | [B_02 §8] |
| K-12 | Rechnungslesung | Einstellungen > Rechnungslesung: Belegzeilen je Steuersatz; Sachkonto/Kostenstelle vorschlagen; Steuerschlüssel/-beträge aus Erkennung; Standard-Steuerschlüssel (Neuer Standard-Steuerschlüssel > Mandanten-ID > Sts > Sts ID); General > Stammdaten-Bucket | [B_02 §4, §5] |
| K-13 | Buckets | Buckets > Neuer Bucket > Daten bearbeiten > Entität wählen; Beispieldaten importieren; Workfloweinstellungen > Integrationen > Neue Integration > Bucket; Felder > Datenquelle „Stammdaten" (Kreditor, Sachkonto) | [B_02 §9] |
| K-14 | Export an ERP | Workfloweinstellungen > Schritt „Buchhaltung" > Aktionen > Verbindung (Workflowende) > Export durchführen: Integration; Exportwert `default`/`validate`/`book` | [B_02 §9] |
| K-15 | Rechnungseingangsbuch | Startseite d.velop documents > Widget hinzufügen > Rechnungseingangsbuch > Hinzufügen; CSV-Export über Kontextmenü der Vorgangsliste | [B_02 §2, §9] |
| K-16 | Multi-Bucket-Erkennung | Importprofil: Stapeleigenschaft `Schema` = Bucket-ID; Feature-Flag `multiple_buckets_in_document_reader` | [B_02 §4] |
| K-17 | document reader | Stammdaten-Upload (CSV/JSON/ZIP, Beispiel-Zip); Option Generische Adressdatenerkennung; Standardmandant; Zielsystem > Exportvalidierung; Bearbeitungsprofile Indexing/FullAccess | [B_02 §3, §4] |
| K-18 | eInvoice converter | Config-App > Rechnungsverarbeitung > einvoice converter: Validierung von XRechnungen; Stylesheet für weiteren Namespace/Sprache hinzufügen | [B_02 §7; B_06 §9b] |

### 6.2 inbound / email import / mail dispatcher

| # | Ziel | Menüpfad / Schritte (laut Doku) | Quelle |
|---|---|---|---|
| K-19 | inbound e-mail Postfach | Konfiguration > Eingehende Post > Eingangspostfächer > E-Mail-Speichereinstellungen > Plus > Gruppe > Fehlerempfänger > Importprofil > Stapelname > Zugelassene E-Mail-Adressen > Schlüssel-Wert-Paare | [B_02 §3; B_06 §4h] |
| K-20 | email import (M365) | Entra Admin Center > App-Registrierungen > Neue Registrierung (nur Organisationsverzeichnis) > API-Berechtigungen Graph `Mail.ReadWrite`, `User.ReadBasic.All` > Geheimer Clientschlüssel; d.velop: Konfiguration > Dokumentenmanagement > E-Mail-Anbindung > Postfach-Verbindungseinstellungen > Microsoft Graph > Anzeigename, Verzeichnis-ID, Anwendungs-ID, API-Zugriffsschlüssel > Verbindung testen / Verarbeitung aktiviert | [B_06 §4b, §4c] |
| K-21 | Alias je Gesellschaft | Konfiguration > Dokumentenmanagement > E-Mail-Anbindung > Verwalten von Postfächern > Hinzufügen > Anzeigename > Alias-Adresse > Importprofil > Stapelname > „Stapel nach Import abschließen" > Schlüssel-Wert-Paare > Berechtigte > Fehlerempfänger | [B_06 §4d] |
| K-22 | Importprofil | Registerkarten „E-Mails" (Textkörper-Platzierung, Standardkategorie Textkörper), „Seiten und Dokumente" (Barcodeerkennung, Trennung, Texterkennung, durchsuchbare PDF, erweiterte Dokumentanalyse), „Zielsystem" (PDF mit Quelldatei, Anlagen dem PDF-Anhang hinzufügen, automatischer/manueller Export); Standardkategorie | [B_06 §5, §6b, §7, §8] |
| K-23 | Kategorie per RegEx | Konfiguration > Import > Importoptionen > Kategorien und Eigenschaften > Kategorie > Regulärer Ausdruck > Seite > Speichern | [B_06 §6c] |
| K-24 | Eigenschaft per RegEx | Konfiguration > Dokumentaufbereitung > Kategorien und Eigenschaften > Regulärer Ausdruck | [B_06 §6d] |
| K-25 | KI-Dokumentanalyse | … Kategorien und Eigenschaften > Verfügbare Kategorien/Eigenschaften > Dokumentanalyse > Prozesskategorie/-eigenschaft | [B_06 §6e] |
| K-26 | document intelligence hub | Dokumentart wählen > KI-Anbieter zuweisen (ggf. Modell/Prompts) > Ausgabeformat | [B_06 §8; DIH] |
| K-27 | Barcodeprofil | Konfiguration > Dokumentenmanagement > Import > Barcodeprofile > Verwalten von Barcodeprofilen > Neues Profil hinzufügen | [B_06 §7] |
| K-28 | Import-Widget | Konfiguration > Dashboardverwaltung > Import-Widget (max. 4 Dropzones, je Importprofil) | [B_06 §7c] |
| K-29 | Scanner | Stapel > Scanner-Symbol > d.velop scanner connector herunterladen > Basisadresse; Admin: Scannen > Scanner | [B_06 §7a] |
| K-30 | mail dispatcher Webhook | d.3 admin > Webhook > Dokumente oder Akten erstellen > Nach dem Erstellen … > Hinzufügen > Name MailDispatcher > URI `/maildispatcher/api/v1/webhook/start_workflow` > aktivieren > Statuscode berücksichtigen > Kategorie Postdokument (DPOST) > API-Key > Timeout | [B_06 §2f] |
| K-31 | Postverteiloptionen Cloud | Postverteiloptionen > Einrichtungsassistent > Repository + API-Schlüssel > Standardkategorie Mail oder eigene > Zuordnung | [B_06 §2h] |
| K-32 | Postverteiloptionen On-Prem | Konfiguration > Aufgaben und Prozesse > Postverteilungsoptionen > Fallback-ID/-Name, Archiv, Basis-URL, API-Schlüssel, Favoriten als Schnellaktionen (max. 20), weitere Optionen | [B_06 §2g] |
| K-33 | Zuordnungen | Startseite > Zuordnungen > Plus > Name > Quelle „Mail Dispatcher Workflow" > Kategorien und Eigenschaften zuordnen | [B_06 §2h] |

### 6.3 process studio / d.ecs task / userprofile

| # | Ziel | Menüpfad / Schritte (laut Doku) | Quelle |
|---|---|---|---|
| K-34 | Prozess anlegen | Komponenten > Prozesse > NEU > Neue Komponente erstellen > Name > Erstellen > Aktivität per Drag & Drop > Typ Benutzeraufgabe > Endereignis > Sequenzflüsse > Allgemein: Name/Betreff > Aufgabeninformationen: Empfänger (z.B. `dv_initiator`) > Speichern | [B_04 §2; PSU:funktionen/grundlegende-funktionen] |
| K-35 | Prozessvariable | weiße Fläche > Prozessvariablen > Prozessvariable hinzufügen > Name, Datentyp, Pflicht/Start/Mehrfach > Hinzufügen | [B_04 §4a] |
| K-36 | Verzweigung + Bedingung | Palette > Gateway > platzieren > Sequenzfluss > Bedingung > Ausdruck (`{var} …`) > Speichern | [B_04 §4b] |
| K-37 | Geschäftsregel-Aufgabe | Aktivität > Typ Geschäftsregel-Aufgabe > Geschäftsregel wählen > Ergebnisvariable > Eingangsmappings > Speichern | [B_04 §4d] |
| K-38 | Empfänger dynamisch | Benutzeraufgabe > Aufgabeninformationen > Versenden an > Button (X) > Variable (Typ Identität) | [B_04 §5] |
| K-39 | Aufgabenmetadaten | Benutzeraufgabe > Aufgabenmetadaten > Metadatum hinzufügen (Beschriftung, Typ, Schlüssel, Wert) | [B_04 §5] |
| K-40 | Frist | Palette > Zwischenereignis > an Kante der Benutzeraufgabe > Typ Timer > Dauer/Datum (ISO 8601) > Speichern | [B_04 §6a] |
| K-41 | Eskalation | leerer Bereich > Eskalationsereignisse > hinzufügen (Name, Code); ausgelöstes Eskalations-Zwischenereignis > Eskalation wählen; Ereignis-Subprozess > Eskalations-Startereignis (nicht unterbrechend) > Eskalation | [B_04 §6b] |
| K-42 | Start bei Dokumentimport | Startereignis > Start über Ereignis > Ereignis hinzufügen > Ereignis wählen > Bedingungen (JSON-Logik) > Startvariablenzuordnung (JSON-Pfad) > Speichern | [B_04 §8a] |
| K-43 | Protokollierung | Bereitstellen > Prozessprotokollierung und Aufbewahrung > Protokollierung, Export ins Repository, Löschung, Aufbewahrungszeit > Bereitstellen | [B_04 §9] |
| K-44 | Transport | Modellierung > Automatisierungen > ⋮ > Herunterladen; Import: Neu > Automatisierung hochladen | [B_04 §10] |
| K-45 | Testkreis | Editor > Berechtigungen > Nutzung | [B_04 §10] |
| K-46 | Zugang process studio | Konfiguration > Aufgaben und Prozesse > Prozessstudio > Zugangsberechtigungen | [B_04 Aufwandseinschätzung] |
| K-47 | Benachrichtigungen | Konfiguration > Aufgabeneinstellungen > Benachrichtigungen > Versenden von Benachrichtigungen aktivieren | [B_04 §6c; TA] |
| K-48 | Abwesenheit | Startseite > Profilbild > Abwesenheitsstatus > Benutzer > Start/Ende > Vertretung > Nachricht > Speichern | [B_04 §7a; B_06 §10e] |
| K-49 | Vertretungs-/Verantwortungsregeln | Konfiguration > Aufgaben > Aufgaben und Prozesse > Vertretungsregeln / Vertretung / Verantwortungsregeln | [B_04 §7c–7f] |

---

## 7. Lücken der Recherche — Rechercheaufträge für das Livos-Produktivkonzept

Priorität: **P1** = entscheidet über Must-have/Architektur, **P2** = beeinflusst Design/Aufwand, **P3** = Feinkonzept.
Weg: **DV** = d.velop (Vertrieb/Produktmanagement/Support), **PL** = Partner-Login help.d-velop.de, **IT** = Test in Demo-Instanz `mdisconsulting.d-velop.cloud`, **LV** = Livos.

| ID | Prio | Thema | Konkreter Rechercheauftrag | Warum (Bezug) | Weg |
|---|---|---|---|---|---|
| R-01 | P1 | **DATEV-Übergabe** | Handbücher „d.velop connect for datev: Administrieren/Anwenden" und „d.velop invoices for DATEV Rechnungswesen" beschaffen. Klären: Exportformat (EXTF-Buchungsstapel? DATEVconnect?), Beleglink/Belegbild-Übergabe, **Auslösung ereignisgesteuert je Schrittverbindung vs. Batch**, Frequenz (>1×/Tag), Vorerfassungs-/Buchungsvorschlag vs. finale Buchung (Exportwert `validate`/`book`), zweifacher Export (Vorerfassung + Verbuchung), Stammdatenrückfluss (Kreditoren, Sachkonten, Kostenstellen je Gesellschaft/Beraternummer/Mandantennummer), Fehlerhandling | Livos-Katalog 5.1; G-16 | PL, DV |
| R-02 | P1 | **Zahlungsfreigabe / Omikron** | Gibt es einen Standardweg Zahlungsfreigabe → Zahlungsdatei/DATEV-Zahlungsverkehr → Omikron? Rückmeldung „bezahlt" (DATEV → d.velop) als Status? Felder `pay_amount`, Skonto nutzbar? | Katalog 5.5 (Must-have); 1.9.6 | DV |
| R-03 | P1 | **Mandantenerkennung bei gleicher Anschrift** | Testlauf mit echten Livos-Belegen (Gesellschaften mit identischer Adresse); Trefferquote messen; klären, ob weitere Merkmale (USt-IdNr/Steuernummer des Empfängers, Kundennummer beim Kreditor, Alias-Postfach als Vorbelegung via Schlüssel-Wert-Paar) in die **Mandantenermittlung** einfließen können; Verhalten bei Mehrdeutigkeit (Standardmandant/Clearing) | Agenda 2.2; G-01 | IT, DV |
| R-04 | P1 | **Mandantenmodell >100 Gesellschaften** | Ein Bucket vs. mehrere Buckets/Workflowdefinitionen; Auswirkung auf Freigabematrix (Spalte Mandant), Clearing je Mandanten-ID, REB-Berechtigung mandantenbezogen, DATEV-Export je Gesellschaft | Agenda 1.1; G-03 | DV, IT |
| R-05 | P1 | **Lizenzmodell** | Lizenzmetrik für smart invoice, inbound, document reader (Seiten/Belege?), process studio, mail dispatcher, email import; Staffel für ~80 Nutzer intern+extern und 5.000–8.000 Belege/Jahr; Systemgrenzen | Agenda „Lizenz- und Mengengerüst"; in B_02/B_04/B_06 **keinerlei** Lizenzangaben | DV |
| R-06 | P1 | **Externe Freigabe ohne Lizenz** | Kann ein Externer eine smart-invoice-Freigabe per sicherem Link erteilen? Ist die process-studio-„Externe Benutzeraufgabe" (E-Mail + d.velop forms + Timer) mit smart invoice koppelbar? Lizenzbedingungen? | Agenda 4.2; 1.7.14, 2.2.2 | DV, IT |
| R-07 | P1 | **Bim4You-Anbindung** | Mapping ER-Journale → Bim4You, Rückfluss Einbehalt-/Kürzungs-/Umlageinfos und Freigabestatus; technisch über `integration.export`-Webhook + API (smart invoice API) – Machbarkeit und Aufwand; existiert ein Connector? | Katalog 5.3; 1.9.3 | DV, Bim4You-Hersteller |
| R-08 | P1 | **Vier-Augen-Prinzip** | Status des Vorschau-Features (GA-Termin, Cloud-Verfügbarkeit), Menüpfad/Schalter, Minimalbetrag-Einstellung; Alternative Wertgrenze per Schrittverbindung als Fallback bestätigen | G-11 | DV, IT |
| R-09 | P2 | **Liegezeit-Reporting / Eskalation Rechnungen** | Gibt es in smart invoice/REB Spalten für Eingangsdatum/Schritteintritt/Liegezeit, Erinnerungen, Eskalationen? Falls nein: Auswertung über CSV-Export, Workflowprotokoll oder Reporting-Produkt? | Workshop-Korrektur 3.2; 1.7.13, 1.8.8 | PL, IT |
| R-10 | P2 | **Vollständige Erkennungsfeldliste + Lernfähigkeit** | Handbuch `document-reader-invoice` („Übertragen von Daten aus der Erkennung") beschaffen; lernt die Erkennung aus Korrekturen (Kreditor-/Layout-Lernen)? Trefferquoten-Referenzen | 1.2.2, 1.2.3 | PL, DV |
| R-11 | P2 | **Bau-Spezifika** | Abschlags-/Teil-/Schlussrechnungen, §13b (Steuerschlüssel-Logik `tax_category`), Sicherheits-/Gewährleistungseinbehalt, Umlagen/Aufteilungsschlüssel – Standard oder Customizing (Custom-Felder)? Referenzkunden Bau/Immobilien | G-17, G-18 | DV |
| R-12 | P2 | **E-Rechnung Peppol / ZUGFeRD** | Peppol-Empfang (Access Point?) unterstützt? ZUGFeRD-Profile (BASIC/EN16931/EXTENDED); ZUGFeRD-Validierung (derzeit nur XRechnung) | 1.1.8, 1.1.10, G-04 | DV |
| R-13 | P2 | **Mailimport-Betrieb** | Abrufintervall email import; IMAP/Exchange-On-Prem-Status (Doku-Widerspruch); Livos-Mailsystem (M365?) klären; Einschränkung der Graph-Berechtigung auf Postfächer | G-31–G-33 | DV, LV |
| R-14 | P2 | **process studio offene Punkte** | Aktionskatalog (E-Mail-Aktion?), Vorgesetztenermittlung, Zahlenvergleich im Feld „Ausdruck", Felder des Dokument-Import-Ereignisses (JSON-Pfade), Label „Empfänger" vs. „Versenden an" | B_04 Offene Punkte 2–6 | IT |
| R-15 | P2 | **Vertragsmanagement** | Existiert ein d.velop-Vertragsprodukt (z.B. „d.velop contract")? Handbuch, Funktionsumfang (Fristen, Wiedervorlage, Vertragsakte, Freigabe), Lizenz; sonst Umsetzung mit process studio + Akten | §4 | DV, PL |
| R-16 | P2 | **Kopplung smart invoice ↔ process studio** | Kann smart invoice process-studio-Prozesse starten (z.B. Klärfall, externe Freigabe) bzw. umgekehrt? Gemeinsame Aufgabenliste (d.ecs task)? Greifen Vertretungsregeln für smart-invoice-Aufgaben? | 0.1, 1.7.12 | DV, IT |
| R-17 | P3 | **Anwenderhandbuch Workflow-Maske smart invoice** | Bedienung Prüfen/Kontieren/Freigeben/Ablehnen (für Schulung und Maskenkonzept/draw.io) | B_02 Offene Punkte 2 | PL, IT |
| R-18 | P3 | **Scandienstleister** | Standardweg für externe Scandienstleister (inbound-API, SFTP?, Mail); Barcode-/Trennblattvorgaben (Code 128) | 3.1.8 | DV |
| R-19 | P3 | **mail dispatcher Cloud** | Installations-/Lizenzvoraussetzungen in der Cloud (Handbuch nennt software manager); E-Mail-Post im mail dispatcher (Projekterweiterung); „An Posteingang senden"; smart inbox (Doku gesperrt) als Alternative | 3.5, G-38 | DV, PL |
| R-20 | P3 | **Status-Modell** | Werteliste der Eigenschaft `Workflowstatus`; Abbildung Livos-Status (Eingang, Vorerfasst, In Prüfung, Freigegeben, Gebucht, Zahlungsfreigegeben, Bezahlt, Klärfall) | 1.8.6 | IT, PL |
| R-21 | P3 | **Archiv-/Recherchezeitraum** | Zugriff auf Rechnungen älter als 12 Monate (REB-Grenze) über d.velop documents-Suche/Kreditorenvorgangsakte | G-13 | IT |

---

## Kurzfazit (Teil B)

- **Belegt und tragfähig:** Eingang über Mail (inkl. Alias je Gesellschaft bei M365), Scan und Upload; XRechnung-Import mit KoSIT-Validierung; §14-Grundprüfung; zweistufige Dublettenprüfung; Kontierung mit Splitting über Positionen; Freigabe mit Wertgrenze (Cent!) oder Freigabematrix inkl. Spalte Mandant; Clearing je Mandant; Rechnungseingangsbuch mit mandantenbezogener Berechtigung; ereignisgesteuerter Export per Webhook/API; BPMN-Prozesse mit Fristen/Eskalation/Parallelität; Postverteilung an Gruppen mit Erinnerung.
- **Kritisch für Livos:** Mandantenerkennung nur über Name + Anschrift (gleiche Anschriften!), Vier-Augen-Prinzip nur Vorschau-Feature, DATEV/Omikron/Bim4You/Lizenz nicht öffentlich belegt, Bau-Spezifika fehlen, keine Liegezeit-Auswertung, kein Vertragsmanagement in den Quellen.
