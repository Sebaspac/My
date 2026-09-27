# 12 — Web-Recherche: Detailfunktionen der Rechnungsverarbeitung (d.velop invoices / smart invoice / document reader / process studio)

**Projekt:** Livos d.velop DMS-Gesamtkonzept (MDIS Consulting)
**Stand der Recherche:** 26.09.2026
**Auftrag:** Die in `04b_dvelop_faehigkeiten_B.md` als **N** (nicht gefunden), **E** (eingeschränkt) oder **A** (Annahme) markierten Punkte zur Rechnungsverarbeitung per Web klären. Dazu kommen die Rechtsgrundlagen (E-Rechnung, §13b UStG, §§48/48b EStG, VOB/B, GoBD).

**Methode**
- Die öffentlichen PDF-Gesamthandbücher von help.d-velop.de habe ich heruntergeladen und im Volltext ausgewertet: smart invoice Cloud mit PDF-Stand 23.06.2026, Rechnungseingangsbuch, smart invoice API, eInvoice converter und inbound scan.
- Alle 1.004 deutschsprachigen Helpcenter-Artikel habe ich über die öffentliche Content-Schnittstelle des Helpcenters geladen und im Volltext durchsucht. Das waren Release Notes und Ankündigungen bis 25.09.2026.
- Außerdem ausgewertet: die Leistungsbeschreibung d.velop invoices (Version 2025-12-15), Gesetzestexte (gesetze-im-internet.de), BMF, BZSt und Herstellerseiten zu BIM4You.
- Zeitstempel aus dem Transkript stammen aus `SP/txt/C_Transkript_Livos_Demo.txt`.

**Legende Erfüllungsgrad** (wie im Livos-Leistungskatalog): **S** = Standard · **K** = Konfiguration · **A** = Anpassung/Entwicklung · **N** = nicht im Leistungsumfang.
**Aussagetyp:** **Fakt** = mit URL belegt · **Annahme** = MDIS-Ableitung, nicht belegt · **offen** = klären oder testen.

---

## 0. Quellenverzeichnis (Kürzel)

| Kürzel | Quelle | URL |
|---|---|---|
| **LB** | Leistungsbeschreibung d.velop invoices, Version 2025-12-15 (7 S.) | https://my.d-velop.cloud/center/a/dvelopinvoicesmedium/legal/sow?language=de |
| **SIC** | d.velop smart invoice Cloud: Administrieren (Gesamt-PDF, Stand 23.06.2026) | https://help.d-velop.de/docs/api/documentations/de/smart-invoice-cloud/cloud/pdf |
| SIC-Esk | dto., Kapitel „Arbeiten mit Eskalationen" (online) | https://help.d-velop.de/docs/de/pub/smart-invoice-cloud/cloud/konfigurieren-von-dvelop-smart-invoice/arbeiten-mit-eskalationen |
| **REB** | d.velop invoices – Rechnungseingangsbuch: Anwenden (PDF) | https://help.d-velop.de/docs/api/documentations/de/invoice-monitor/cloud/pdf |
| **API** | d.velop smart invoice API (PDF) | https://help.d-velop.de/docs/api/documentations/de/smart-invoice-developer/cloud/pdf |
| **EIC** | d.velop eInvoice converter: Administrieren (Cloud-PDF) | https://help.d-velop.de/docs/api/documentations/de/einvoice-converter/cloud/pdf |
| **ISA** | d.velop inbound scan: Administrieren (Cloud-PDF) | https://help.d-velop.de/docs/api/documentations/de/inbound-scan-admin-cloud/cloud/pdf |
| **DR** | d.velop document reader 7.20.2 – Dokumenterkennung | https://help.d-velop.de/docs/de/pub/document-reader/7.20.2/konfigurieren/dokumenterkennung |
| **PSU** | d.velop process studio: Anwenden 2026.q3 – Grundlegende Funktionen | https://help.d-velop.de/docs/de/pub/process-studio-user/2026.q3/funktionen/grundlegende-funktionen |
| **PSA** | d.velop process studio: Administrieren 2025.q1 (PDF) | https://help.d-velop.de/docs/api/documentations/de/process-studio-admin/2025.q1/pdf |
| **DOC-Mail** | d.velop documents Cloud – Senden einer Dokumentkopie per E-Mail | https://help.d-velop.de/docs/de/pub/documents/cloud/erste-schritte-beim-teilen-von-dokumenten-mit-anderen-personen/senden-einer-dokumentkopie-per-e-mail |
| H1 | HC 14.09.2026 „REB: Neuer Schnellzugriff für eskalierte Rechnungen" | https://help.d-velop.de/invoices/de/articles/cmtvssd4zeoct07uoaijon9b8 |
| H2 | HC 04.09.2026 „Der CSV-Export im REB steht produktiv zur Verfügung" | https://help.d-velop.de/invoices/de/articles/cms7m6f3dyddy07w4mmm35kqn |
| H3 | HC 04.09.2026 „Positionstabelle … dynamische Anzahl von Positionszeilen" | https://help.d-velop.de/invoices/de/articles/cmtlsnctpong407w4903d2ycp |
| H4 | HC 14.04.2026 „Mehr Transparenz und Flexibilität bei Zahlungszielen" | https://help.d-velop.de/invoices/de/articles/cmnww8gtnzqgz07uu6wue4mgi |
| H5 | HC 01.12.2025 „Neue Funktionen im REB" (ungelesen, Counter, Statusfilter) | https://help.d-velop.de/invoices/de/articles/cmiit1uiv16o907uov9lgus1b |
| H6 | HC 29.08.2025 „Updates zum REB" (Spalte Rechnungsformat) | https://help.d-velop.de/invoices/de/articles/cmeu9zzcea9s807w14tiy8gbl |
| H7 | HC 20.03.2026 „Schnellaktion Historie" | https://help.d-velop.de/invoices/de/articles/cmmw4yott50ee07uuiulu1j87 |
| H8 | HC 12.03.2026 „Anlage eigener Schnellzugriffe im REB" | https://help.d-velop.de/invoices/de/articles/cmmnepqg5tr6h08vzrpb81r6s |
| H9 | HC 09.09.2026 „Umstellung des Kommunikationswegs … innerhalb von d.velop invoices" | https://help.d-velop.de/invoices/de/articles/cmtiz5gdg4oxt06vyxjrm9kfk |
| H10 | HC 01.09.2026 „Anleitung: direkte Übergabe document reader → smart invoice" | https://help.d-velop.de/invoices/de/articles/cmtcuvh176abi06w7ktt6lvuz |
| H11 | Serviceportal-News „process studio und Aufgabenverwaltung – E-Mail-Versand per Messaging-App" (21.08.2026) | https://serviceportal.d-velop.de/de/news/dvelop-process-studio-und-aufgabenverwaltung-e-mail-versand-per-messaging-app |
| H12 | HC process studio, Anwendungsbeispiel/Aktion „E-Mail versenden" (13.08.2024) | https://help.d-velop.de/process-studio/de/articles/clsj1st9f12ov0auiglm6tcry |
| H13 | HC 03.09.2026 „Current 2026.Q3 – Die Highlights im Überblick" | https://help.d-velop.de/invoices/de/articles/cmtldcpoa8cyw07w7zsb9jejt |
| D1 | d.velop store – document reader invoice | https://store.d-velop.com/de/d.velop-document-reader-invoice/10001705 |
| D2 | d.velop – Funktionsübersicht d.velop invoices | https://www.d-velop.de/software/digitale-rechnungsverarbeitung/funktionsuebersicht-d-velop-invoices |
| D3 | d.velop – Themenseite Peppol | https://www.d-velop.de/themen/peppol |
| R1 | § 14 UStG | https://www.gesetze-im-internet.de/ustg_1980/__14.html |
| R2 | § 27 Abs. 38 UStG (Übergangsregelung E-Rechnung) | https://www.gesetze-im-internet.de/ustg_1980/__27.html |
| R3 | § 13b UStG | https://www.gesetze-im-internet.de/ustg_1980/__13b.html |
| R4 | § 48 EStG | https://www.gesetze-im-internet.de/estg/__48.html |
| R5 | § 48b EStG | https://www.gesetze-im-internet.de/estg/__48b.html |
| R6 | § 146 AO | https://www.gesetze-im-internet.de/ao_1977/__146.html |
| R7 | BMF – FAQ E-Rechnung (Stand März 2026) | https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html |
| R8 | BMF-Schreiben 15.10.2025 zur E-Rechnung (Zusammenfassung Haufe) | https://www.haufe.de/finance/steuern-finanzen/bmf-schreiben-v-15102025-zur-e-rechnung_190_669628.html |
| R9 | GoBD, 2. Änderung, BMF 14.07.2025 (Original-PDF beim Abruf HTTP 503; Inhalt nur aus Sekundärquelle, z.B. IHK Darmstadt) | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Weitere_Steuerthemen/Abgabenordnung/2025-07-14-GoBD-2-aenderung.pdf · https://www.ihk.de/darmstadt/produktmarken/recht-und-fair-play/steuerinfo/e-rechnung-gobd-bmf-schreiben-2025-6677714 |
| R10 | BZSt – Bauabzugsteuer / Freistellungsbescheinigungen; EIBE-Portal | https://www.bzst.de/DE/Unternehmen/Bauleistungen/bauleistungen.html · https://eibe.bff-online.de/eibe/index.xhtml |
| R11 | VOB/B § 16 (Zahlung) / § 17 (Sicherheitsleistung) – Sekundärquellen | https://www.haufe.de/id/norm/vobb-2016-16-zahlung-HI10559881_p16.html · https://dejure.org/gesetze/VOB-B/17.html |
| R12 | XRechnung BT-3 Rechnungsart (Codes 875/876/877) – Sekundärquelle | https://rechnex.de/ressourcen/xrechnung/bt-3 |
| B1 | BRZ-Shop – BIM4YOU-Module | https://shop.brz.eu/BRZ-Software/BIM4YOU/ |
| B2 | Wikipedia – Bim4you | https://de.wikipedia.org/wiki/Bim4you |

---

## 1. Wichtigste Erkenntnisse und Korrekturen gegenüber Vorrecherche (04b) und Demo-Termin

1. **Eskalation ist Standard in smart invoice.** In 04b stand dafür N (1.7.13); belegt ist es jetzt vollständig:
   - statische Frist je Schritt („Fixe Tage nach Erhalt der Aufgabe") und dynamische Frist („Tage vor Skonto/Nettofrist");
   - globale Eskalation 1. Stufe, schrittspezifische Eskalation 1. Stufe und globale Eskalation 2. Stufe;
   - die Empfänger werden per Bearbeiterfindung ermittelt; wahlweise wird in Arbeitstagen gezählt.

   [SIC §1.2.14; SIC-Esk] Neu seit 23.–30.09.2026: der REB-Schnellzugriff „An mich eskalierte Rechnungen" mit Anzeige der Eskalationsstufe. [H1]
2. **Die Liegezeit im aktuellen Schritt ist im Standard sichtbar.** Im Rechnungseingangsbuch (REB) gibt es die Spalten „Aktueller Schritt", „**Aktueller Schritt seit**", „Zugewiesen", „Status", „Mandant" usw. Das REB lässt sich nach Schritt und Mandant gruppieren und hat einen **CSV-Export** (produktiv seit 04.09.2026). [REB §1.2.3, §1.4.2; H2]
   → Die Workshop-Korrektur „3.2 Liegezeit nicht belegbar" und die MDIS-Aussage im Termin [00:36:13 Sebastian Pachon] gelten nur für **historische Durchlaufzeiten je Benutzer/Schritt**, nicht für den Gesamtüberblick.
3. **Kontierungsvorlagen und KI-Kontierungsvorschläge stehen in der Leistungsbeschreibung.** Genannt sind „Erstellung von kreditorenabhängigen Kontierungsvorlagen" (alle Betriebsformen) und „KI-basierte Kontierungsvorschläge (Ermittlung von Sachkonto und Kostenstelle auf Belegebene)" (C1/H/O). [LB §2.3] In 04b stand dafür N (1.6.5).
4. **Automatische Rückweisungs-Mail an den Lieferanten:** Die MDIS-Aussage „nicht über d.velop direkt" [00:39:57 André Töpper / 00:39:59 Sebastian Pachon] ist im Kern **bestätigt**. Es gibt keine dokumentierte Standardfunktion.
   - d.velop liefert aber alle Bausteine: die Lieferanten-E-Mail im Kreditorenstamm (`vendor.email`), eine Ablehnen-Aktion, Custom-Felder mit Wertelisten für Standardgründe und einen Webhook-Export an der Ablehnungsverbindung. [SIC §1.2.19; API §1.3.4, §1.3.1]
   - Damit bleibt eine **kleine Middleware-Erweiterung** (A) zu entwickeln, kein Großprojekt.
5. **Kürzungen dürfen nicht über „Dokument lokal bearbeiten" laufen.** Im Termin sagte MDIS, man könne die Rechnung „bearbeiten" bzw. „lokal bearbeiten" [00:41:47–00:44:32 Sebastian Pachon]. Eine Änderung des Rechnungsdokuments widerspricht § 146 Abs. 4 AO (ursprünglicher Inhalt muss feststellbar bleiben) [R6]. Bei E-Rechnungen ist das XML das Original [R7, R9].
   → **Empfehlung:** Die Kürzung wird nur in den Workflow-Daten erfasst: Zahlbetrag `pay_amount` auf Kopf- und Positionsebene, Kürzungsgrund als Custom-Feld, Notiz, Protokoll und Belegänderungsansicht. [SIC §1.2.19, §1.2.20; API §1.3.1]
6. **Mandantenerkennung:** Es bleibt bei Name und Adresse (API-Felder des Mandanten). Pro Importprofil lässt sich ein eigener Stammdaten-Bucket setzen (Stapeleigenschaft `Schema`) [SIC §1.2.22]. Es sind aber **höchstens 50 Buckets** zulässig [LB §3], bei Livos gibt es mehr als 100 Gesellschaften. Ein eigener Bucket je Gesellschaft ist also ausgeschlossen.
7. **Rückkanal von Bim4You oder DATEV in den smart-invoice-Beleg:** Die öffentliche API kennt **keinen Schreibzugriff auf laufende Belege**. Rückmeldungen gibt es nur als Erfolg/Fehler mit Meldetext beim Export. [API §1.3.1 „Zurückmelden von Ergebnissen"] Einbehalts-, Kürzungs- und Umlageinfos aus Bim4You (Zielarchitektur) kommen also nicht automatisch in smart invoice an. **Architekturrelevant.**
8. **Webhook-Export:** Er muss innerhalb von **30 s** quittiert werden, sonst läuft der Workflow in den Fehlerschritt. Der asynchrone Abhol-Transfer hält den Beleg 2 bis max. 28 Tage im Zustand „aktiver Belegdatentransfer" (ohne Benutzerinteraktion). Das lässt sich als „Warten auf Bim4You" nutzen. [API §1.3.1; SIC §1.2.10]
9. **Breaking Change 01.01.2027:** Der alte Kommunikationsweg wird abgeschaltet. Pflicht ist dann der direkte Weg inbound → document reader → smart invoice. Das ist auch Voraussetzung für die Prüfberichte der E-Rechnungs-Validierung. Livos sollte **direkt auf dem neuen Weg** aufgesetzt werden. [H9, H10]
10. **Nebenbefund Lizenz:** Die LB nennt Editionen nach **Rechnungen pro Monat** und **Buchhaltungsusern**, die Zahl der **Freigabeuser ist beliebig**. [LB §2.1, §2.4] Die Hypothese „Named-User für 80 Anwender" (Leistungskatalog, Blatt Tabelle1) ist damit zu korrigieren; Details in §12.

---

## 2. Frage 1 — Kürzungen (Zahlbetrag, Kürzungsgrund, positionsweise, GoBD, E-Rechnung)

**Befund (Fakt)**
- Der Beleg hat das Feld **Zahlbetrag** `pay_amount` bzw. `pay_amount_lcy` **auf Kopf- und auf Positionsebene**. [SIC §1.2.19 Urkel-Objekt „voucher"; API §1.3.1 JSON-Beispiel `line_items.pay_amount`]
- Die Aufteilungsprüfung kennt eigene Modi für den Zahlbetrag: `amount_allocated?(2)` = „Zahlbetrag muss stimmen", `(4)` = Brutto + Zahlbetrag, `(5)` = Netto + Zahlbetrag, `(6)` = alle drei. [SIC §1.2.19] Damit ist eine **positionsweise Zahlbetragsführung mit Summenkontrolle** im Datenmodell vorgesehen.
- Auf Positionsebene gibt es 7 Rabattfelder und eine automatische Nettobetragsberechnung (Menge × Einzelpreis / Preiseinheit − Rabatte). [SIC §1.2.24] Wird eine Menge von 4 auf 3 Stunden geändert, rechnet das System den Positionsbetrag neu (Beispiel André Töpper [00:42:36]).
- „Zuschläge" (Vorschau-Feature) „können auch eingesetzt werden, um Abschläge darzustellen" (Kopf- oder Positionszuschlag, negativ). [SIC §1.2.16]
- Die **Belegänderungsansicht** vergleicht Kopf- und Positionsdaten zwischen zwei konfigurierten Schritten farbig (rot gelöscht, gelb geändert, grün hinzugefügt). [SIC §1.2.20]
- Der Zahlbetrag wird exportiert (`pay_amount` im Export-JSON) und lässt sich einer DMS-Eigenschaft zuordnen (Mapping-Feld `pay_amount`). [API §1.3.1, §1.3.5]
- Es gibt 20 Custom-Felder im Kopf und 20 in den Positionen. Kopf-Custom-Felder lassen sich an „Zusätzliche Entitäten" binden, also an eine Werteliste, z.B. „Kürzungsgrund". [SIC §1.2.6; API „Custom Entities"]
- Ob `pay_amount` je Schritt als schreibbares Feld in der Workflow-Maske angeboten wird, steht nicht in der öffentlichen Doku (das Anwenderhandbuch der Workflow-Maske ist nicht öffentlich). → **offen (Test)**
- „Es gibt keine Kürzungsmaske" [00:42:00 Tanja Brecht]: bestätigt. Eine eigene Kürzungsfunktion ist nicht dokumentiert.

**GoBD / Recht (Fakt)**
- § 146 Abs. 4 AO: „Eine Buchung oder eine Aufzeichnung darf nicht in einer Weise verändert werden, dass der ursprüngliche Inhalt nicht mehr feststellbar ist." [R6]
- E-Rechnung: „Bei hybriden E-Rechnungen bilden nunmehr die im strukturierten Teil (z. B. XML) vorliegenden Rechnungsdaten den führenden Teil." Aufzubewahren ist der strukturierte Teil im Originalformat. [R7; R9 via Sekundärquelle]
- Korrekturen der Rechnung selbst erstellt nur der Aussteller, bei Pflicht wieder als E-Rechnung. [R7]
- Das BMF-Schreiben vom 15.10.2025 unterscheidet Format-, Geschäftsregel- und Inhaltsfehler. [R8]

**Bewertung / Empfehlung**

| Teilaspekt | Grad | Umsetzung |
|---|---|---|
| Kürzung als Metadatum (Zahlbetrag < Brutto), Originalbeleg bleibt unverändert | **K** | Feld Zahlbetrag (Kopf) im Schritt „Fachliche Prüfung" sichtbar und schreibbar machen. Kopf-Custom-Feld „Kürzungsgrund" mit Werteliste (Custom Entity) anlegen, dazu „Kürzungsbetrag" als Custom oder als Differenz Brutto − Zahlbetrag. Verbindung „Weiter" mit Bedingung `voucher.custom<n>.present?`, sobald Zahlbetrag ≠ Brutto (Pflichtbegründung). Notiz in der Historie. |
| Positionsweise Kürzung (30-Seiten-Rechnung, 8 Positionen) | **K** (Datenmodell B, Bedienung offen) | Variante a: `pay_amount` je Position, Summenprüfung `amount_allocated?(6)`. Variante b: Kürzungspositionen als negative Zeilen bzw. Abschlag-„Zuschlag" (Vorschau-Feature). Die Kopfsumme wird automatisch berechnet. Welche Variante DATEV sauber verarbeitet, klären mit Trios/DATEV-Connector (R-01). |
| Nachweis der Änderungen | **S** | Workflowprotokoll ERV, Historie mit Kommentaren (REB-Schnellaktion) [H7], Belegänderungsansicht z.B. „Verteilung" vs. „Buchhaltung" [SIC §1.2.20]. |
| E-Rechnung (XML führend) | **S/K** | Das XML bleibt unverändert im DMS; die Kürzung lebt nur in den Workflow-Daten. Bei inhaltlich falscher Rechnung (Betrag, Steuer) keine Kürzung, sondern **Rückweisung und berichtigte E-Rechnung** anfordern (Frage 2), wie im Termin gefordert [00:46:54 Trius]. |
| Steuerliche Folgen einer Kürzung (Minderung, Vorsteuer) | – | **Annahme:** Bei Entgeltminderung ist eine Vorsteuerkorrektur nach § 17 UStG zu prüfen. Nicht recherchiert, mit Trios/StB klären. |
| „Dokument lokal bearbeiten" (Termin) | **nicht empfehlen** | Das widerspricht § 146 Abs. 4 AO; stattdessen PDF-Annotationen nutzen (LB „PDF-Annotationen, Kommentare und Markierungen"). [LB §2.3] |

---

## 3. Frage 2 — Ablehnung/Rückweisung mit Grund und automatischer Lieferanten-E-Mail

**Befund (Fakt)**
- Ein Freigabeschritt **muss** mindestens je eine Aktion vom Typ „Bestätigen" und „Ablehnen" haben. Die Ablehnen-Verbindung kann auf einen beliebigen Schritt zeigen, im Beispiel „Zur sachlichen Prüfung". [SIC §1.2.5] Beliebige weitere Aktionen und Verbindungen sind in jedem Schritt modellierbar, jeweils mit Bedingung. [SIC §1.2.1]
- Ablehnungsgrund:
  - Pflichtfeldsteuerung je Schritt („verpflichtend") [SIC §1.2.7];
  - Bedingungen wie `voucher.custom5.present?` [SIC §1.2.19];
  - Werteliste für Kopf-Custom-Felder über „Custom Entities" (Typ frei, z.B. `reject_reason`, je Mandant oder global) [API §1.3.4].

  → **5 Standardgründe als Auswahlliste sind konfigurierbar.**
- Die E-Mail-Adresse des Lieferanten ist im Kreditorenstamm vorgesehen: `email` – „Wenn möglich, die Adresse, die der Kreditor auf seinen Rechnungen angibt" [API §1.3.4 Vendors]. In Bedingungen ist sie als `voucher.vendor.email` verfügbar [SIC §1.2.19]. Im Export-JSON-Beispiel steht nur Kreditor-Nr./-Name; die Middleware kann die Adresse aber aus dem eigenen Stamm ergänzen (**Annahme**).
- **Mail-Versand in d.velop:**
  - smart invoice: Außer Eskalationsbenachrichtigungen an interne Bearbeiter ist **kein E-Mail-Versand dokumentiert**. [SIC Volltext]
  - LB: „Teilen von Rechnungen per Link und E-Mail (Einfaches Teilen von Rechnungen mit Externen)" ist Standard [LB §2.3]. Das ist ein manueller Weg.
  - d.velop documents: „Kopie senden" erzeugt eine E-Mail mit Dokument als Anhang **im Downloadverzeichnis**; versendet wird über das eigene Mailprogramm. [DOC-Mail]
  - process studio: Das Anwendungsbeispiel/Aktion „E-Mail versenden" sendet Betreff, HTML-Body und optionalen Button an **„ein Benutzer- oder Gruppenobjekt"**, also nur an interne Identitäten. [H12]
  - Die „Externe Benutzeraufgabe" schickt an eine **E-Mail-Adresse** (statisch oder aus Variable), braucht aber **zwingend ein d.velop-forms-Formular und einen Timer**. [PSU]
  - Die Messaging-App (ab 2026) versendet nur Aufgaben- und Prozessfehler-Benachrichtigungen; externe Adressen nur bei Prozessfehlern; E-Mail-Templates werden „bald" individualisierbar. [H11, H13]
  - process-studio-Skripte können externe npm-Bibliotheken nutzen [PSA §1.6.2]; ein SMTP- oder Graph-Versand wäre darüber technisch denkbar (**Annahme**, nicht dokumentiert).
  - Die Kopplung smart invoice → process studio ist **nicht dokumentiert** (siehe 04b R-16).
- **Export an einer beliebigen Schrittverbindung:** „Wenn eine Rechnung von einem Workflowschritt in einen anderen übergeht, können Sie die Belegdaten an eine Integration übermitteln." Möglich sind Webhook (Quittung ≤ 30 s, HMAC-signiert) oder Abhol-API. [SIC §1.2.12; API §1.3.1]

**Bewertung**
- Ablehnen mit Pflichtgrund: **K**.
- Automatische, vorlagenbasierte Lieferanten-Mail: **A**, als Middleware-Baustein.
- Manueller Mailversand aus d.velop (Link/Kopie): **S**.
- Die MDIS-Aussage im Termin ist korrekt, sollte aber präzisiert werden: Der Auslöser, die Daten und die Gründe kommen aus d.velop per Konfiguration. Nur der Versand selbst ist Entwicklung.

**Umsetzungsvorschlag (Annahme, auf belegten Bausteinen)**
1. Schritt „Fachliche Prüfung" oder „Freigabe" bekommt die Aktion **„An Lieferant zurückweisen"**. Die Verbindung führt in einen Endschritt oder Schritt „Zurückgewiesen". Bedingung: `voucher.custom<Grund>.present?`.
2. An dieser Verbindung wird „Export durchführen" auf die Integration „MDIS-Middleware-Webhook" gesetzt.
3. Die Middleware wählt die Mail-Vorlage anhand des Grundes (5 Vorlagen) und nimmt die Empfängeradresse aus dem konsolidierten Kreditorenstamm (Fallback: `vendor.email`). Rechnungsnummer, Datum und Gesellschaft kommen aus dem JSON. Sie versendet über das Livos-M365-Postfach (Graph `sendMail`) und legt die gesendete Mail per inbound/DMS-API in der Kreditorenvorgangsakte ab. Die Webhook-Antwort muss innerhalb von 30 s erfolgen.
4. Vor dem Versand kann die Middleware eine vorbefüllte Mail zur Freigabe bereitstellen. Das entspricht dem Wunsch „vorgefertigte Standard-E-Mail, die ich noch anpassen kann" [00:38:32 Tanja Brecht].
5. Bei E-Rechnungen enthält die Vorlage den Hinweis, dass eine berichtigte **E-Rechnung** erforderlich ist [R7].

---

## 4. Frage 3 — Liegezeit, Durchlaufzeit, Reporting, BI-Anbindung

**Befund (Fakt)**
- **REB-Spalten** (belegt, keine vollständige Liste veröffentlicht): Aktueller Schritt, **Aktueller Schritt seit**, **Zugewiesen** (Benutzer/Gruppen), **Status** (u.a. „Clearing Modus", Eskalationsstufe 1/2), Mandant, Kreditor, Skontobetrag, Skonto- und Nettofälligkeit, Rechnungsdatum, Lieferscheine, **Rechnungsformat** (E-Rechnung/sonstige). [REB §1.2.3, §1.3.6, §1.4.1–1.4.3; H1; H6]
- Nach „verschiedenen Datumsspalten" lässt sich gruppieren. [H5]
- **Sichten:** Meine offenen Rechnungen, Rechnungen in Vertretung, **Alle offenen Rechnungen** (global oder **mandantenbezogen** berechtigt), Archiv (6 bzw. 12 Monate ab Rechnungsdatum). Eigene Schnellzugriffe mit Filtern gibt es seit 03/2026, dazu Counter-Badges und die Kennzeichnung „ungelesen". [REB §1.2.2; H5; H8]
- **CSV-Export** (produktiv seit 04.09.2026): „Sichtbare Spalten" oder „Alle Spalten", unter Berücksichtigung der Filter. Er läuft im Hintergrund, der Download bleibt 30 Tage verfügbar. [H2]
- **Historie** je Vorgang: Weg durch den Workflow, Kommentare und Notizen, auch für abgeschlossene Vorgänge. [H7] **Workflowprotokoll** als DMS-Dokument (Kategorie „Workflowprotokoll ERV"), das „Eigenschaften der Rechnung und Bearbeitungsschritte nachvollziehbar dokumentiert". [LB §2.3; SIC §1.2.2]
- Die Administration zeigt ein Dashboard mit „Belege in Umlauf / insgesamt verarbeitet" und Workflows je Schritt; im Termin gezeigt [01:00:10 Sebastian Pachon].
- **Nicht gefunden (N):** ein fertiger Bericht zu Durchlaufzeit oder Liegezeit **je Benutzer und Schritt historisch**, ein BI-/OData-Connector für d.velop invoices, ein „process insights"-Produkt für invoices. Die LB nennt als Statistik nur die „Analyse der Erkennungsqualität". [LB §2.3; D2; HC-Volltext „Power BI|OData|Reporting"]
- Das Export-Ereignis enthält `connection.from_step`/`to_step`, Workflow-Schritt und `end_mode`. [API §1.3.1] An **jeder** Schrittverbindung kann exportiert werden. [SIC §1.2.12]

**Bewertung**
- Katalog **3.2** (Gesamtüberblick über Status, aktuellen Bearbeiter und Liegezeit im aktuellen Schritt, mandantenbezogen): **S**.
- Historische Durchlaufzeiten je Benutzer und Schritt (Frage Christian Weigel [00:35:18]) sowie Management-KPIs: **A**.
- Anbindung evidanza/Power BI: **A** (kein Standard-Connector).

**Umsetzungsvorschlag (Annahme)**
- **Variante 1, schnell:** Regelmäßiger CSV-Export „Alle offene Rechnungen – alle Spalten" → evidanza. Das ergibt eine Stichtagssicht: Liegezeit aktuell, Bearbeiter, Schritt. Die Exporte starten manuell; ein API-Aufruf dafür ist nicht dokumentiert (offen).
- **Variante 2, belastbar:** An allen Schrittverbindungen einen Export an einen **Logging-Webhook** der MDIS-Middleware konfigurieren (sofort 200 quittieren, Nachricht in eine Queue).
  - Die Middleware speichert Zeitstempel, Beleg-ID, Mandant, from_step/to_step und Bearbeiter. Wer die Aktion ausgelöst hat, steht im Export-JSON nicht auf Kopfebene: **offen**. Möglicher Ersatz: Protokoll/Historie oder die Workflowbeteiligten-Eigenschaft.
  - Das Ergebnis ist eine Faktentabelle für evidanza.
  - **Risiko:** Ist der Webhook nicht erreichbar, läuft der Beleg in den Fehlerschritt. [API §1.3.1] Das braucht hochverfügbares Design oder den Export nur an unkritischen Verbindungen.
- **Variante 3:** Workflowprotokoll-Dokumente aus dem DMS per DMS-API auswerten. Der Inhalt bzw. das Format des Protokolls ist nicht öffentlich beschrieben: **offen**.

---

## 5. Frage 4 — Eskalation und Erinnerung

**Befund (Fakt)** [SIC §1.2.14; SIC-Esk]
- **Statische Frist:** „Wenn eine Aufgabe für mehr als x Tage in einem Schritt … verbleibt, wird eine Eskalation ausgelöst." Konfiguriert wird sie je Schritt unter Eskalation > Deadline > „Fixe Tage nach Erhalt der Aufgabe".
- **Dynamische Frist:** Tage vor Skonto- bzw. Nettofrist, abhängig von der Zahlungsbedingung. Bei Skonto- oder Nettofrist 0/NULL gibt es keine Eskalation.
- **Drei Arten:** globale Eskalation 1. Stufe, schrittspezifische 1. Stufe (ersetzt die globale 1. Stufe) und globale 2. Stufe (immer aktiv, nur global).
- **Empfänger** über eine **Bearbeiterfindung** (Urkel-Ausdruck), z.B. `user.name = "Buchhaltung"`. Mandantenabhängig ist das z.B. per Regex mit `voucher.company.nr` möglich (Syntax belegt: `/^Freigeber_#{voucher.company.nr}$/`). [SIC §1.2.19]
- Arbeitstage-Option: Das Wochenende wird berücksichtigt, **Feiertage nicht**.
- Wenn eine Eskalation auslöst, „erhält eine Person … eine Benachrichtigung". Der **Kanal** (E-Mail oder nur Aufgabe/REB) ist nicht spezifiziert. REB-Schnellzugriff „An mich eskalierte Rechnungen"; die Statusspalte zeigt Stufe 1/2 und den Zeitpunkt. [H1]
- In der LB steht: „Eskalationsmöglichkeit von Aufgaben nach festgelegten Regeln (z.B. abhängig von Bearbeitungszeit, Skontofristen oder der Nettofälligkeit)", in allen Betriebsformen. [LB §2.3]
- Eine **automatische Umleitung** (Neuzuweisung) der Aufgabe bei Eskalation ist **nicht dokumentiert**. Die Eskalation ist eine Benachrichtigung.

**Bewertung (Katalog 3.3)**
- Benachrichtigung nach X Tagen je Schritt: **S/K**.
- Unterschiedliche Fristen je Gesellschaft: **K**, nur über getrennte Workflowdefinitionen, weil die Frist je Workflow bzw. Schritt gilt (max. 100 Workflowabläufe [LB §3]).
- Weiterleitung statt Benachrichtigung: **N/offen**.
- „Per Mail": **offen (Test)**.

**Empfehlung:** Einheitliche Fristen für alle Gesellschaften, z.B. Prüfung 3 AT, Freigabe 3 AT, 2. Stufe an die Leitung Buchhaltung. Der Empfänger wird mandantenabhängig per Bearbeiterfindung bestimmt. Zusätzlich eine dynamische Eskalation 2 Tage vor Skonto. Ob die Eskalationsbenachrichtigung per E-Mail ankommt, in der Demo-Instanz testen.

---

## 6. Frage 5 — Bau-Spezifika: Abschlag/Schluss (kumuliert, VOB), Sicherheitseinbehalt, §13b, §48b, Umlagen, Rolle Bim4You

### 6.1 Abschlags- und Schlussrechnungen (kumuliert)
- **Recht (Fakt):**
  - § 14 Abs. 5 UStG: „Wird eine Endrechnung erteilt, sind in ihr die vor Ausführung … vereinnahmten Teilentgelte und die auf sie entfallenden Steuerbeträge abzusetzen …" [R1]
  - VOB/B § 16: Abschlagszahlungen binnen 21 Tagen nach Zugang der prüfbaren Aufstellung; Schlusszahlung alsbald nach Prüfung, spätestens 30 Tage nach Zugang der Schlussrechnung. [R11, Sekundärquelle]
  - XRechnung BT-3 kennt eigene Rechnungsarten: **875** Abschlagsrechnung (Bau), **876** Teilschlussrechnung, **877** Schlussrechnung. [R12, Sekundärquelle]
- **d.velop (Fakt):** Abschlags- und Schlussrechnung sowie eine kumulierte Prüfung sind **nicht dokumentiert** (bestätigt 04b 1.9.7; Volltext SIC/LB/HC ohne Treffer).
  - Verfügbar sind die Stammdaten-Entität **Belegart** (`document_type`, max. 1.000 [LB §3]), Custom-Felder, die Kreditorenvorgangsakte und die Aktenablage der Vorgänger-Abschläge (im Termin gezeigt [00:45:13]).
  - Die Aussage „bereits gezahlt laut Lieferant" (BT-113 „Bereits bezahlter Betrag") wird aus E-Rechnungen als Eigenschaft gelesen [ISA §1.3.4]. Einen Abgleich gegen tatsächlich Gezahltes gibt es nicht.
- **Bewertung Katalog 5.2 (Teil kumuliert):**
  - Kennzeichnung Abschlag/Schluss und Anzeige der Vorgänger: **K**.
  - Automatische Prüfung „kumulierter Leistungsstand − tatsächlich gezahlt" [00:45:47 André Töpper]: **A**. Die Zahlungsdaten liegen in DATEV bzw. Bim4You, nicht in d.velop.

### 6.2 Sicherheitseinbehalt
- **Recht (Fakt, Sekundärquelle):** VOB/B § 17 Abs. 6 Nr. 1 begrenzt den Einbehalt je Zahlung auf höchstens 10 %, bis die vereinbarte Sicherheitssumme erreicht ist. [R11]
- **d.velop:** Keine Einbehaltsverwaltung dokumentiert (N).
  - Erfassung je Rechnung ist möglich über Custom-Felder (Einbehalt %, Betrag, Art Vertragserfüllung/Gewährleistung, Rückgabedatum) und einen reduzierten Zahlbetrag: **K**.
  - Die **Vormerkung und Verwaltung über die Laufzeit** (Rückgabe nach Abnahme bzw. Gewährleistung, Summe je Auftrag) ist **A**: Bim4You, DATEV-OP oder ein process-studio-Wiedervorlageprozess (Timer-Datum aus Variable, 04b 2.4.5).

### 6.3 § 13b UStG (Reverse Charge Bauleistungen)
- **Recht (Fakt):** § 13b Abs. 2 Nr. 4: Bauleistungen „mit Ausnahme von Planungs- und Überwachungsleistungen". Abs. 5 Satz 2: Der Leistungsempfänger schuldet die Steuer, „wenn er ein Unternehmer ist, der nachhaltig entsprechende Leistungen erbringt". Nachweis durch eine Finanzamtsbescheinigung, „auf längstens drei Jahre befristet". [R3]
- **d.velop (Fakt):**
  - Steuerschlüssel-Stammdaten mit `percentage`, `tax_category_1/2` (je Mandant oder global).
  - **Automatische Steuerschlüsselermittlung** bei eindeutiger Übereinstimmung von `tax_category_1/2` zwischen Kreditor und Sachkonto bzw. Beschaffungskategorie.
  - Kreditoren sind **je `company_id`** angelegt („Muss je company_id eindeutig sein"). [API §1.3.4 Vendors/Tax Codes]
- **Bewertung: K.**
  - Einen §13b-Steuerschlüssel je Gesellschaft anlegen, z.B. `tax_category_1 = "BAU13B"` am Kreditor.
  - Das Kennzeichen ist je Kombination Gesellschaft × Bau-Kreditor setzbar. Das passt zur Anforderung, dass §13b vom **Status der empfangenden Livos-Gesellschaft** abhängt.
  - Den konkreten DATEV-BU-Schlüssel mit Trios abstimmen (**offen**).
  - Plausibilitätsregel als Bedingung: Bau-Kreditor und MwSt ≠ 0 → Klärschritt. Das ist mit `vat_amount` und Custom-Kennzeichen konfigurierbar (**Annahme**, Test).
- **Annahme:** Nur Livos-Bau- und Projektgesellschaften, die selbst nachhaltig Bauleistungen erbringen, sind §13b-Schuldner. Reine Bestandsgesellschaften sind es in der Regel nicht. Mit dem StB klären.

### 6.4 § 48 / § 48b EStG (Bauabzugsteuer, Freistellungsbescheinigung)
- **Recht (Fakt):**
  - § 48 Abs. 1: Der Leistungsempfänger (Unternehmer) muss „einen Steuerabzug in Höhe von 15 Prozent" der Gegenleistung vornehmen (Entgelt **zzgl. USt**, Abs. 3).
  - Ausnahme: Vermieter von „nicht mehr als zwei Wohnungen".
  - Abs. 2: Kein Abzug bei gültiger Freistellungsbescheinigung (FSB) „im Zeitpunkt der Gegenleistung" **oder** wenn die Gegenleistung im Kalenderjahr voraussichtlich höchstens **15.000 €** beträgt (Empfänger mit ausschließlich steuerfreien Umsätzen nach § 4 Nr. 12 S. 1 UStG), sonst **5.000 €**. Bauleistungen desselben Leistenden werden zusammengerechnet. [R4]
  - § 48b: Die FSB enthält u.a. **Geltungsdauer** und Umfang. Das BZSt „erteilt dem Leistungsempfänger … im Wege einer **elektronischen Abfrage** Auskunft". [R5]
- **BZSt (Fakt):** Die Prüfung läuft als „**registrierter Nutzer im EIBE Portal unter ‚Einzelabfrage FSB'**". Benötigt werden Bundesland, Steuernummer des Leistenden und die **Sicherheitsnummer** der FSB. Eine Abfrage nur nach Name oder Steuernummer ist nicht möglich. **Eine Massenabfrage oder API ist nicht dokumentiert.** Haftungsausschluss gilt, wenn eine FSB vorlag, „auf deren Rechtmäßigkeit er vertrauen durfte". [R10]
- **d.velop (Fakt):**
  - Der Kreditorenstamm in smart invoice hat **feste Felder** und kein freies Attribut. Ein FSB-Kennzeichen oder -Datum am Kreditor ist nicht vorgesehen (N). [API §1.3.4 Vendors]
  - In Urkel sind Vergleiche dokumentiert, Arithmetik nicht; eine automatische 15-%-Berechnung ist nicht belegt. [SIC §1.2.19]
- **Bewertung Katalog 2.6/2.7:**
  - FSB-Datenhaltung und Gültigkeitsprüfung: **A** (Middleware).
  - Hinweis im Workflow: **K + A**.
  - 15-%-Vorschlag: **A**.
  - Online-Verifikation beim BZSt: nur **manuell** (EIBE-Einzelabfrage). Das bestätigt die Einschätzung im Termin [00:48:45–00:49:28].
- **Umsetzungsvorschlag (Annahme):**
  1. FSB-Tabelle in der MDIS-Lieferanten-App je konsolidiertem Lieferanten führen: Steuernummer, Sicherheitsnummer, gültig bis, Umfang, Datum und Nachweis der letzten EIBE-Prüfung. Die FSB-PDF liegt in der Kreditorenakte im DMS.
  2. Export an der **Startverbindung** (Workflowstart ist wie eine Verbindung konfigurierbar [SIC §1.2.1]) an die Middleware. Fehlt bei einer Bau-Rechnung eine gültige FSB, antwortet sie mit 400 und dem Meldetext „Keine gültige Freistellungsbescheinigung – 15 % Bauabzug prüfen". Die Meldung wird angezeigt, der Beleg geht in den Fehler- bzw. Klärschritt. [API §1.3.1] Alternativ ein Custom-Feld „FSB-Status" (Werteliste), das in der Verteilung Pflicht ist.
  3. Die Bagatellgrenzen (5.000/15.000 € je Leistendem und Jahr) prüft die Middleware anhand der Zahlungsdaten aus DATEV (**A**).
  4. Den Abzug erfasst die Buchhaltung manuell (Zahlbetrag = 85 %, Custom „Bauabzugsteuer"); Anmeldung und Abführung laufen in DATEV.

### 6.5 Umlagen (Kostenverteilung nach Schlüssel)
- **Fakt:**
  - Das Splitting über Positionen mit eigener Kostenstelle, eigenem Kostenträger und Sachkonto ist Standard (04b 1.6.2).
  - Zusatzdimensionen je Position mit **Hierarchie** (`parent_dimension_type/id`, z.B. Projekt → Projektleiter) und je Mandant sind vorhanden. [API „Other Dimensions"]
  - Kopfzuschläge verteilen sich manuell, gleichmäßig, nach Betrag oder nach Menge; das ist nicht für Umlageschlüssel gedacht. [SIC §1.2.16]
  - „Kreditorenabhängige Kontierungsvorlagen" [LB]; „Vorlagen anwenden" legt mehrere Positionszeilen an. [H3]
  - Ob Vorlagen **Prozentschlüssel** (z.B. 40/35/25 % auf drei Objekte) auf den Rechnungsbetrag anwenden oder feste Beträge bzw. Zeilen setzen, ist nicht öffentlich beschrieben. → **offen (Test)**
- **Bewertung:** **K**, wenn Vorlagen Prozentanteile können, sonst **A** (Schlüssel in der Middleware, Aufteilung außerhalb).

### 6.6 Rolle Bim4You
- **Fakt (Hersteller-Shop BRZ):** BIM4You hat folgende Module:
  - „Controlling L1" mit „Budget Controlling … Vertragsmanager, Nachtragsmanager, **Rechnungseingangsbuch**, **Freigabemanager** … Budget-Historisierung";
  - „E-Rechnung": „Import von Eingangsrechnungen im Format XRechnung (UBL) sowie ZUGFeRD";
  - „**Fibu Connector DATEV REB Eingangsrechnungen**";
  - „Schnittstelle **DocuWare**" (nicht d.velop). [B1]
- Hersteller ist laut Wikipedia die BIB GmbH (vormals ALLbudget); die Hersteller-Domains leiten inzwischen auf BRZ/suiteify um. [B2]
- **Konsequenzen (Annahme):**
  1. Bim4You kann Bau-Rechnungen **selbst** prüfen, freigeben und an DATEV übergeben. Dieselbe Rechnung darf nicht aus d.velop **und** aus Bim4You nach DATEV gehen. Das **führende System je Rechnungstyp** muss festgelegt werden.
  2. Die fachlich richtige Stelle für kumulierte Abschlagsprüfung, Einbehalte, Nachträge und Budgetabgleich ist Bim4You (Vertrags- und Nachtragsmanager), nicht d.velop.
  3. **Integrationsmuster:**
     - d.velop erkennt die Bau-Rechnung (Kennzeichen am Kreditor/Belegart oder Kostenträger = Projekt).
     - An der Verbindung „Bau-Detailqualifikation" läuft ein **asynchroner Export** (Abhol-API). Der Beleg wartet im Status „aktiver Belegdatentransfer", bis die Middleware nach der Bim4You-Freigabe `successful: true` meldet, bei Ablehnung `false` mit Meldetext.
     - Das Zeitfenster beträgt bis zu **28 Tage** [API §1.3.1], danach landet der Beleg im Fehlerschritt.
     - Der Import in Bim4You wäre für XRechnung (UBL) belegt. Für PDF-Rechnungen und ZUGFeRD-CII ist ein Bim4You-Import oder eine API **offen**.
  4. **Rückkanal Einbehalt/Kürzung/Umlage → d.velop:** Die öffentliche smart-invoice-API kennt keinen Schreibzugriff auf Belege. Die Werte sind entweder in d.velop manuell nachzutragen oder direkt Bim4You → DATEV zu übergeben. Die Zielarchitektur (Folie „Bim4You ←: Einbehalt-/Kürzungsinfos, Umlageinfos, Freigabestatus") ist entsprechend anzupassen.

---

## 7. Frage 6 — Kontierung (Katalog 2.5, 2.8)

**Befund (Fakt)**
- **Aufteilung auf Kostenstellen:** Über mehrere Positionen, je mit Sachkonto, Kostenstelle, Kostenträger und individuellen Dimensionen. Die Freigabematrix wirkt je **Kostenobjekt**. Die Summenprüfung `amount_allocated_tolerance?` stellt sicher, dass vollständig verteilt wurde. [SIC §1.2.1, §1.2.19; LB „Kontierung über Sachkonten, Kostenstellen, Kostenträger sowie individuelle Buchungsdimensionen"]
- **Kontierungsvorlagen:** „Erstellung von kreditorenabhängigen Kontierungsvorlagen" (C1, C2, H, O). [LB §2.3; D2] Vorlagen erzeugen mehrere Positionszeilen. [H3] Kreditoren sind je Mandant angelegt [API]. Damit sind Vorlagen faktisch **je Gesellschaft × Kreditor** möglich (**Annahme**, Bedienung und Pflege nicht öffentlich dokumentiert).
- **Vorschläge/KI:**
  - „KI-basierte Kontierungsvorschläge (Ermittlung von Sachkonto und Kostenstelle **auf Belegebene**)", nur Betriebsformen **C1 (AWS), H, O**, nicht C2/OTC. [LB §2.3]
  - „Verbesserte Erkennungsquoten auf Basis eines Autotrainings durch KI" (C1, H, O). [LB §2.3]
  - document reader: „lernt selbstständig aus den manuellen Verbesserungen in der Indexierungsmaske"; „Ein integrierter Autotrainer verbessert die Erkennung … kontinuierlich". [D1]
  - Einstellung „Sachkonto/Kostenstelle vorschlagen" (04b 1.6.3).
  - Kostenträger/Projekt als KI-Vorschlag ist **nicht belegt**.
- Standard-Steuerschlüssel je Mandant und automatische Steuerschlüsselermittlung (siehe 6.3).

**Bewertung**
- **2.8** Aufteilung: **S**. Standardschlüssel je Gesellschaft: **K**, wenn die Vorlagen kreditorenunabhängig bzw. prozentual nutzbar sind, sonst **A** (offen).
- **2.5** Vorschläge Sachkonto und Kostenstelle auf Belegebene: **S** (Betriebsform C1).
  - Kreditorvorschlag: **S** (Erkennung).
  - Projektnummer oder positionsgenaue Vorschläge: **K/A** über Vorlagen bzw. Kontierung aus Bestellung, **nicht KI-belegt**.
  - Die Livos-Formulierung „lernt aus historischen Daten" deckt die LB nur allgemein ab („KI-basiert", „Autotraining"); die Lernbasis ist nicht beschrieben.

**Empfehlung:** In der Demo testen: Vorlage mit drei Kostenstellen anlegen und prüfen, ob sie prozentual oder absolut arbeitet. Die Betriebsform C1 (AWS) für Livos festhalten, weil die KI-Vorschläge in C2 fehlen.

---

## 8. Frage 7 — Mandantenerkennung (Rechnungsempfänger)

**Befund (Fakt)**
- **Mandanten-Stammdaten (API):**
  - `id`, `name` („für die automatische Mandantenermittlung … ein wichtiges Kriterium. Wenn möglich … wie er auf den Rechnungen zu finden ist");
  - `address` („ein wichtiges Kriterium"), `city`, `zip_code`, `country`, `local_currency`, `parent_id`.
  - **Keine USt-IdNr./Steuernummer, keine Kundennummer beim Mandanten.** [API §1.3.4 Companies]
- **Dokumentprüfung** Mandant: Name, PLZ, Ort, Straße (04b 1.2.5). Die DR-Seite „Dokumenterkennung" beschreibt nur Standardmandant, generische Adressdatenerkennung, Stammdatenschema und Positionsfilter, keine weiteren Kriterien. [DR]
- **E-Rechnung:** inbound liest aus dem XML u.a. **BT-10 „Leitweg-ID"** (Käuferreferenz), **BT-44 Unternehmen (Käufer)**, BT-50/52/53 Anschrift, BT-58 E-Mail des Käuferkontakts. [ISA §1.3.4] Ob der document reader invoice BT-10, BT-46 (Käuferkennung) oder BT-48 (Käufer-USt-IdNr.) zur Mandantenermittlung nutzt, ist **offen** (Handbuch `document-reader-invoice` nicht öffentlich).
- **Stammdaten-Bucket je Importprofil:** Stapeleigenschaft `Schema` = Bucket-ID. Beispiel „E-Mail-Rechnungen Firma 1 → Stammdaten Firma 1". [SIC §1.2.22] Grenzen: **max. 50 Buckets** [LB §3], Vorschau-Feature-Flag, d.velop empfiehlt einen Bucket (04b 1.2.9).
- **E-Mail-Eingang:** In C1/H/O gilt eine Begrenzung von 10.000 E-Mails pro Monat und Postfach; in C2 ist es „ein o365-Postfach mit beliebig vielen Aliasen". [LB §2.3] Alias je Postfach mit eigenem Importprofil und Schlüssel-Wert-Paaren (04b 1.1.2). Dokumenteigenschaften sind im Importprofil vorbelegbar (Release Notes Current 2023.Q1, InboundApp 1.13.0, IN-6049: https://help.d-velop.de/invoices/de/articles/clryrdyla0jbj0aw6zmgin4mw). Durch den neuen direkten Kommunikationsweg gehen „bestimmte Vorbelegungen" nicht mehr verloren. [H9, H10]
- **Kreditoren** sind je `company_id` angelegt. **Annahme:** Die Kreditorenerkennung hängt an der richtigen Mandantenerkennung.
- **Recht:** § 14 Abs. 4 Nr. 1 UStG verlangt „den vollständigen Namen und die vollständige Anschrift … des Leistungsempfängers". [R1] Livos darf und muss die korrekte Gesellschaftsbezeichnung auf der Rechnung verlangen.

**Bewertung Katalog 2.2:** **K**, nicht S.
- Für Gesellschaften mit eigener Anschrift ist die Erkennung Standard.
- Bei **gleicher Anschrift** ist nur der **Name** als dokumentiertes Merkmal übrig. USt-IdNr. oder Steuernummer des Empfängers werden nicht verwendet; Livos' Annahme im Katalog („anhand der Anschrift/Steuernummer") ist **nicht belegt**.

**Workarounds (Reihenfolge = Empfehlung)**
1. **Lieferantenanschreiben:** Pflicht zur exakten Gesellschaftsbezeichnung gemäß Stammdatenschreibweise (§ 14 Abs. 4 Nr. 1 UStG). Bei E-Rechnungen die **Käuferreferenz BT-10** mit der Livos-Gesellschaftsnummer befüllen lassen. Test, ob der document reader BT-10 für die Mandantenzuordnung auswertet (offen, R-03).
2. **Alias-Adresse je Gesellschaft oder Gesellschaftsgruppe** (z.B. `rechnung+<GesNr>@livos…`) mit eigenem Importprofil und einer Vorbelegung „Mandant" als Schlüssel-Wert-Paar. Test, ob der document reader den vorbelegten Mandanten übernimmt oder überschreibt (**offen**). Bei 100+ Aliasen den Pflegeaufwand und die Lieferantenkommunikation beachten.
3. **Standardmandant „Klärfall"** und Schritt „Verteilung" mit Pflichtprüfung Mandant. Clearing-Gruppe je Mandanten-ID (04b 1.7.11).
4. **Nicht empfohlen:** Buckets je Gesellschaft. Das Limit liegt bei 50, und die Stammdaten müssten mehrfach gepflegt werden.
5. **Messung:** Trefferquote mit echten Livos-Belegen, insbesondere mit Gesellschaften gleicher Anschrift (04b R-03).

---

## 9. Frage 8 — IBAN-Prüfung, Fälligkeit/Skonto, Dubletten

**IBAN (Fakt)**
- Kreditorbankverbindungen stehen im Stamm (mehrere je Kreditor, `primary`). Sie sind „sowohl für die Identifizierung des Kreditoren beim Auslesen der Rechnung als auch **zum Abgleich der auf der Rechnung angegebenen Informationen mit den Daten aus dem ERP-System** relevant". [API §1.3.4 Vendor Bank Accounts]
- smart invoice überträgt die Bankverbindungen an den document reader. [SIC §1.2.22]
- Die Dokumentprüfung prüft „IBAN vorhanden" (04b 1.3.1).
- Der Beleg führt `vendor_bank_account` (id/iban/bic aus dem Stamm). [API §1.3.1] Das DMS-Mapping kennt `iban` (Beleg) **und** `vba_iban` (Stammdaten-Bankverbindung). [API §1.3.5]
- **Nicht dokumentiert:** eine explizite **Warnung in der Workflow-Maske** bei abweichender IBAN. In Urkel-Bedingungen ist `vendor_bank_account` nicht als Eigenschaft gelistet, eine Regel-Prüfung ist also nicht belegt. [SIC §1.2.19]

**Bewertung (Frage André Töpper [00:24:42]):** **E/offen.** Der Abgleich ist laut API vorgesehen, die Anzeigeform ist ungeklärt.
- **Test:** Rechnung mit fremder IBAN einspielen und prüfen, ob die Maske warnt oder keine Bankverbindung zuordnet.
- **Fallback A:** Middleware-Check per Export an der Startverbindung (Beleg-IBAN aus der Erkennung gegen den konsolidierten Stamm), bei Abweichung Meldung und Klärschritt. Hinweis: Die Beleg-IBAN steht im Export-JSON nur als `vendor_bank_account` (Stamm). Ob die erkannte IBAN mitgeliefert wird, ist **offen**; alternativ über die DMS-Eigenschaft `iban`.

**Fälligkeit/Skonto (Fakt) – S**
- Fälligkeiten werden aus der **Zahlungsbedingung** (Stamm, am Kreditor `payment_terms_id`) berechnet. Optional „Manuelles Zahlungsziel"; wird aus der Erkennung Skonto-/Nettofälligkeit oder Skonto-% übermittelt, ist es automatisch vorausgewählt (Feature seit 21.04.2026 Standard). [H4; SIC §1.2.13]
- **Hinweis**, wenn die Zahlungsbedingung des Belegs von der Standard-Zahlungsbedingung des Kreditors abweicht (Direktvergleich). [H4]
- Skontoampel (gelb/rot/dunkelrot), REB-Spalten Skontobetrag, Skonto- und Nettofälligkeit. [SIC §1.2.13; REB]
- → Die Frage „Beleg oder Stammdaten?" [00:29:00 André Töpper] ist per Konfiguration je Workflow entscheidbar: Manuelle Zahlungsziele ja/nein, Übernahme aus Erkennung.
- VOB-Fristen (21/30 Tage, R11) als Zahlungsbedingung an Bau-Kreditoren hinterlegen (**K**).

**Dubletten (Fakt) – S**
- document reader (Rechnungsnummer, gegen validierte Belege) und smart invoice (Kreditor + Rechnungsnummer, 18 Monate, Akzeptanz nur mit Begründung) (04b 1.3.4/1.3.5). LB: „Automatisierte Dubletten Erkennung". [LB §2.3]
- Das entspricht dem Wunsch „Dublette annehmen nur mit Begründung" [00:41:01].

---

## 10. Frage 9 — E-Rechnung (Formate, Peppol, Visualisierung, Validierung, Pflichten)

**d.velop (Fakt)**
- **Formate** laut LB: „ZUGFeRD 2.X/basierend auf CII 16B, XRechnung 3.0/basierend auf UBL 2.1 & CII 16B … FR: Factur-X 1.0.x", dazu CFDI, eSLOG, Fattura PA, FA(1–3). Auslesen und Visualisierung als PDF in allen Betriebsformen. [LB §2.3]
- inbound verarbeitet: „ZUGFeRD 1.0, ZUGFeRD 2.1, xRechnungen (UBL u. CII)", Speicherung im Originalformat plus PDF-Version. [ISA §1.3.4]
- **Validierung:** „Es werden **ausschließlich XRechnungen** validiert." KoSIT-Validator (Syntax, EN16931, CIUS), Prüfbericht als Anhang im DMS, nicht sichtbar in inbound bzw. document reader. [EIC §1.3.3]
- REB-Spalte „Rechnungsformat". [H6]
- Die Validierungsberichte setzen den neuen Kommunikationsweg voraus (Abschaltung des alten 01.01.2027). [H9]
- **ZUGFeRD-Profile:** Eine Profilunterscheidung (MINIMUM/BASIC-WL vs. EN16931/EXTENDED) ist **nicht dokumentiert (N)**.
- **Peppol:** In LB, Helpcenter und Funktionsübersicht **nicht vorhanden (N)**. Die d.velop-Themenseite beschreibt Peppol allgemein, ohne eigenen Access Point. [D3; D2] Bekannt ist nur die edoc invoice suite (anderes Produkt), die Rechnungen „aus E-Rechnungsportalen des Peppol-Netzwerks" erfassen kann (Suchtreffer store.d-velop.com, nicht vertieft).

**Recht / Pflichten für Livos (Fakt)**
- **Empfang:** „seit dem 1. Januar 2025 besteht für inländische Unternehmen die Notwendigkeit, eine E-Rechnung empfangen zu können … Für den Empfang … genügt bereits ein E-Mail-Postfach." [R7] Peppol ist damit **nicht erforderlich**.
- **Übergang (Ausstellerseite)** nach § 27 Abs. 38 UStG:
  - Umsätze bis 31.12.2026: Papier oder sonstiges Format erlaubt.
  - Umsätze 2027: nur bei Vorjahresumsatz ≤ 800.000 € des Ausstellers (bzw. EDI) erlaubt.
  - ab 2028: E-Rechnung Pflicht.

  [R2] → Der XML-Anteil der Livos-Eingangsrechnungen steigt 2027 deutlich und ist ab 2028 die Regel.
- **Ausstellerpflicht Livos:** Die E-Rechnungspflicht gilt für B2B-Leistungen, „wenn der Umsatz nicht nach § 4 Nummer 8 bis 29 steuerfrei ist". [R1] **Annahme:** Steuerfreie Wohnraummiete (§ 4 Nr. 12) ist ausgenommen, optierte gewerbliche Vermietung bzw. steuerpflichtige Umsätze nicht. Das ist nicht Kern dieser Recherche, mit StB klären.
- **Formate:** XRechnung und ZUGFeRD ab 2.0.1 erfüllen die Anforderungen, „mit Ausnahme der Profile MINIMUM und BASIC-WL". [R7]
- **Hybrid:** XML führend [R7]. **Aufbewahrung:** Der strukturierte Teil ist im Originalformat aufzubewahren; der Bildteil nur, wenn er zusätzliche steuerrelevante Informationen enthält [R9, Sekundärquelle]. Aufbewahrungsfrist 8 Jahre [R7].
- **Fehlerklassen** (BMF 15.10.2025): Format-, Geschäftsregel- und Inhaltsfehler mit unterschiedlichen Folgen. [R8]

**Bewertung Katalog 2.4:**
- Empfang und Visualisierung ZUGFeRD/XRechnung: **S**.
- Validierung XRechnung: **S**. Validierung ZUGFeRD sowie Erkennung unzulässiger Profile (MINIMUM/BASIC-WL): **N → A**, z.B. Prüfung der Guideline-ID `urn:…:minimum` im XML durch Middleware oder document-reader-Regel (**Annahme**).
- Peppol-Empfang: **N** (rechtlich nicht nötig; bei Bedarf externer Access Point, der in ein Postfach liefert).

---

## 11. Frage 10 — Status-Modell, Workflowschritte, Rollen

**Befund (Fakt)**
- **Standardworkflow** (Onboarding): „Verteilung, Prüfung, Freigabe und Buchhaltung" [SIC §1.2.21]. In der LB heißt es: „Verteilung, **sachliche Prüfung**, Freigabe und Buchhaltung", konfigurierbar [LB §2.3 Fn. **].
- **Zahlungsfreigabe** ist kein Standardschritt; sie wird im Handbuch als Beispielschritt genannt und ist modellierbar. [SIC §1.2.1]
- **Schritttypen:** normal, Freigabe (Pflichtaktionen Bestätigen/Ablehnen), Prüfung (erweiterte Prüfung, Prüfermatrix), Warten auf Wareneingang. Die Verbindungswahl erfolgt Top-Down nach der ersten zutreffenden Bedingung. Eine Startverbindung ist konfigurierbar. [SIC §1.2.1, §1.2.5, §1.2.15]
- **Status und Phasen:**
  - Workflow aktiv → REB „offen"; beendet/abgebrochen → „Archiv". Export `end_mode` `finished`/`aborted`. [REB §1.2.2; API]
  - REB-Spalte „Status" mit u.a. **Clearing Modus** und **Eskalation Stufe 1/2**. [REB §1.3.6; H1] Kennzeichnung „ungelesen". [H5]
  - Phasen ohne Benutzerinteraktion: „Workflow startet", „Workflowstart ist fehlgeschlagen", „**Workflow hat einen aktiven Belegdatentransfer**", „wird beendet/abgebrochen", „ist beendet/abgebrochen"; Schritt „Warten auf Wareneingang". [SIC §1.2.10]
  - DMS-Eigenschaft „Workflowstatus" und Mapping-Feld `workflow_status`. [SIC §1.2.21; API §1.3.5] **Die vollständige Werteliste ist nicht veröffentlicht (offen).**
- **Gruppen (Onboarding):** dv_Buchhaltung, dv_Freigeber, dv_Sachliche_Prüfer, dv_Workflowteilnehmer, dv_inbound, dv_inbound_Administratoren, dv_Service_Accounts. [SIC §1.2.21]
- **Nutzerrollen laut Lizenz** [LB §2.4]:
  - **Buchhaltungsuser:** Erfassung/Import, Kreditor- und Rechnungsinformationen ergänzen, buchen, an ERP/FiBu übergeben, Dokumente und Akten verwalten.
  - **Freigabeuser:** Prüfer wählen, prüfen, Lieferscheine anhängen, Notizen/Kommentare, Annotationen, Positionsdaten ergänzen.
- **Grenzen** [LB §3]:
  - max. 100 Workflowabläufe mit je 50 Schritten;
  - 1.000 Mandanten, 50 Buckets, 2.500 Gruppen;
  - 5.000 Rechnungen/Tag, 500 Positionen je Rechnung;
  - 100.000 Kreditoren und 100.000 Kreditorbankverbindungen.

**Bewertung:** Standardschritte und Rollen: **S**. Livos-Statusmodell mit „Vorerfasst/Gebucht/Zahlungsfreigegeben/Bezahlt": **K** für die Schritte und **A** für „bezahlt". Für die Zahlungsrückmeldung aus DATEV gibt es keinen dokumentierten Rückkanal in den Beleg (siehe Erkenntnis 7).

**Vorschlag Livos-Schrittmodell (Annahme)**

Eingang (inbound/document reader) → **Verteilung/Vorqualifikation** (Buchhaltung Trios: Mandant, Kreditor, Belegart, FSB-Status; Export „validate" als DATEV-Vorerfassung, siehe R-01) → **Fachliche Prüfung** (Prüfermatrix; Kürzung/Rückweisung) → [nur Bau: **Warten auf Bim4You** = asynchroner Transfer] → **Freigabe** (Freigabematrix mit Spalte Mandant, Wertgrenze) → **Buchhaltung** (Export „book") → optional **Zahlungsfreigabe** → Ende. Zusätzlich: Endpfad **„Zurückgewiesen"** (Export → Middleware-Mail) und Clearing.

---

## 12. Nebenbefund Lizenz- und Mengengerüst (für Angebot relevant)

| Edition | Rechnungen/Monat | Buchhaltungsuser | Freigabeuser | Speicher (Cloud) |
|---|---|---|---|---|
| small | 250 | 5 | beliebig | 50 GB |
| medium | 750 | 10 | beliebig | 150 GB |
| large | 1.500 | 20 | beliebig | 300 GB |
| enterprise | 3.000 | 30 | beliebig | 600 GB |

[LB §2.1; Preisspannen je Edition laut D2: small 280–510 €/Monat bis enterprise 1.695–3.100 €/Monat]

- Livos mit 5.000–8.000 Belegen/Jahr (≈ 420–670/Monat) liegt in **medium**. Mehr als 10 Buchhaltungsuser (MDIS/Trios/Livos-Buchhaltung) führen zu **large**. Eine Overusage wird berechnet. [LB §2.1]
- Laut LB ist **process studio** in d.velop invoices nur in der Betriebsform C2 (OTC) enthalten und dort „eingeschränkt auf die Erkennung/Verarbeitung von Rechnungen". [LB §2 Fn. *] Für Nicht-Rechnungsprozesse (Verträge, Freigabe Hausverwaltung, Mietkonto-Ausbuchungen) ist eine eigene Lizenz einzuplanen (**Annahme**).
- Die DATEV-Schnittstellen (Rechnungswesen: C1, H, O; Unternehmen Online: C1, H) sind **kostenpflichtig (€)**. [LB §2.3]

---

## 13. Abschlusstabelle

| # | Punkt | Befund | Beleg | Erfüllungsgrad | Empfehlung |
|---|---|---|---|---|---|
| 1a | Kürzung als Zahlbetrag/Metadatum | `pay_amount` auf Kopf- und Positionsebene, Summenprüfung Modus 2/4/5/6, Belegänderungsansicht, Export `pay_amount`; keine eigene Kürzungsmaske | SIC §1.2.19/§1.2.20; API §1.3.1 | **K** | Zahlbetrag schreibbar, Custom „Kürzungsgrund" (Werteliste) als Pflicht bei Zahlbetrag ≠ Brutto; DATEV-Verarbeitung klären |
| 1b | Positionsweise Kürzung | Menge/Preis/Rabatt je Position mit Neuberechnung; Abschlag-„Zuschläge" (Vorschau) | SIC §1.2.24, §1.2.16 | **K** (Bedienung testen) | Variante `pay_amount` je Position vs. negative Kürzungszeile im Test entscheiden |
| 1c | GoBD/E-Rechnung bei Kürzung | AO § 146 Abs. 4; XML führend; Korrektur nur durch Aussteller | R6, R7, R9 | **S** (Archiv) | Keine Bearbeitung des Rechnungsdokuments („lokal bearbeiten" streichen), nur Annotation und Workflow-Daten |
| 2a | Ablehnen mit Grund | Aktionstyp Ablehnen, Pflichtfeld/Bedingung `present?`, Werteliste über Custom Entities | SIC §1.2.5, §1.2.7, §1.2.19; API | **K** | 5 Standardgründe als Custom Entity; Endpfad „Zurückgewiesen" |
| 2b | Automatische Lieferanten-Mail | Kein Mailversand in smart invoice; process-studio-Mail nur an Benutzer/Gruppen; Externe Benutzeraufgabe nur mit Formular + Timer; `vendor.email` im Stamm; Webhook-Export je Verbindung | SIC; H12; PSU; API §1.3.1/§1.3.4 | **A** (klein) | Webhook an Rückweisungsverbindung → Middleware versendet Vorlage (Graph), Ablage der Mail im DMS |
| 2c | Manuelles Teilen per Mail/Link | „Teilen per Link und E-Mail"; „Kopie senden" (EML) | LB §2.3; DOC-Mail | **S** | Übergangslösung bis 2b |
| 3a | Übersicht Status/Bearbeiter/Liegezeit aktuell (Kat. 3.2) | REB-Spalten Aktueller Schritt, **Aktueller Schritt seit**, Zugewiesen, Status; Gruppierung; mandantenbezogene Sicht | REB; H1, H5, H8 | **S** | Management-Schnellzugriffe je Gesellschaftsgruppe anlegen |
| 3b | Export CSV | produktiv seit 04.09.2026, sichtbare/alle Spalten, 30 Tage Download | H2 | **S** | Für Ad-hoc-Auswertungen nutzen |
| 3c | Historische Durchlaufzeit je Benutzer/Schritt, BI (evidanza) | Kein Bericht, kein OData/BI-Connector; Export-Events mit from/to_step möglich | LB; API §1.3.1; D2 | **A** | Logging-Webhook → Middleware → evidanza; Ausfallsicherheit (30 s/Fehlerschritt) beachten |
| 4 | Eskalation/Erinnerung (Kat. 3.3) | Statisch je Schritt, dynamisch vor Skonto/Netto, 2 Stufen, Empfänger per Bearbeiterfindung, Arbeitstage ohne Feiertage; REB „An mich eskalierte Rechnungen" | SIC §1.2.14; H1; LB | **S/K** (Mailkanal offen; keine Auto-Umleitung) | Einheitliche Fristen, Empfänger mandantenabhängig; Mailkanal testen |
| 5a | Abschlag/Schluss kumuliert (Kat. 5.2) | Nicht vorhanden; Belegart, Akte, BT-113 lesbar | LB/SIC Volltext; ISA; R1, R11, R12 | **K** (Kennzeichnung) / **A** (Prüfung) | Kumulierte Prüfung in Bim4You bzw. Middleware mit Zahlungsdaten aus DATEV |
| 5b | Sicherheitseinbehalt | Nicht vorhanden; Erfassung über Custom + Zahlbetrag | R11; SIC | **K** (Erfassung) / **A** (Verwaltung) | Einbehaltverwaltung in Bim4You/DATEV-OP; Wiedervorlage ggf. process studio |
| 5c | § 13b Reverse Charge | Steuerschlüssel + `tax_category`-Automatik; Kreditor je Gesellschaft | API Tax Codes/Vendors; R3 | **K** | §13b-Schlüssel je Gesellschaft; Kennzeichen am Bau-Kreditor; BU-Schlüssel mit Trios |
| 5d | § 48b FSB / 15 % Bauabzug (Kat. 2.6/2.7) | Kein FSB-Feld im Kreditorenstamm; BZSt nur EIBE-Einzelabfrage (keine API dokumentiert); Bagatellgrenzen 5.000/15.000 € | API; R4, R5, R10 | **A** (+ K) | FSB-Tabelle in Middleware, Check per Startverbindungs-Export mit Meldung; EIBE manuell mit Nachweis |
| 5e | Umlagen | Splitting S; kreditorenabhängige Kontierungsvorlagen; Prozentschlüssel nicht belegt | LB; H3; API | **K/offen** | Test Vorlage mit %-Schlüssel; sonst Schlüssel in Middleware |
| 5f | Rolle Bim4You | Bim4You hat eigenes Rechnungseingangsbuch, Freigabemanager, E-Rechnungsimport, DATEV-Connector; DMS-Schnittstelle DocuWare | B1, B2 | – | Führendes System je Rechnungstyp festlegen; Bau-Prüfung in Bim4You über asynchronen Transfer; kein Schreib-Rückkanal in smart invoice |
| 6a | Aufteilung Kostenstellen (Kat. 2.8) | Positionen + Kostenobjekt + Summenprüfung | SIC; LB | **S** | – |
| 6b | Standardschlüssel je Gesellschaft (Kat. 2.8) | Kreditorenabhängige Kontierungsvorlagen (Kreditor je Gesellschaft) | LB; H3; API | **K** (offen: %-Logik) | Vorlagen je Gesellschaft×Kreditor; Test |
| 6c | Lernende Vorschläge (Kat. 2.5) | KI-Kontierungsvorschlag Sachkonto/Kostenstelle **auf Belegebene** (nur C1/H/O); Autotraining; Lernen aus Korrekturen | LB; D1 | **S** (Sachkonto/Kostenstelle) / **K/A** (Projekt, Position) | Betriebsform C1 (AWS) festlegen; Erwartung „Belegebene" kommunizieren |
| 7 | Mandantenerkennung (Kat. 2.2) | Name + Adresse; keine USt-IdNr./Kundennr. beim Mandanten; Bucket je Importprofil (max. 50); BT-10/BT-44 aus E-Rechnung lesbar | API Companies; SIC §1.2.22; LB §3; ISA; R1 | **K** (bei gleicher Anschrift Risiko) | Lieferantenanschreiben (exakter Name, BT-10); Alias je Gesellschaft mit Vorbelegung testen; Klärfall-Mandant |
| 8a | IBAN-Abgleich | Bankverbindungen im Stamm „zum Abgleich" vorgesehen; `iban` vs. `vba_iban`; Warnung nicht dokumentiert | API §1.3.4/§1.3.5 | **E/offen** (→ S oder A) | Demo-Test fremde IBAN; Fallback Middleware-Check |
| 8b | Fälligkeit/Skonto Beleg vs. Stamm | Berechnung aus Zahlungsbedingung, manuelles Zahlungsziel aus Erkennung, **Hinweis bei Abweichung vom Kreditor-Standard**, Skontoampel | H4; SIC §1.2.13 | **S** | VOB-Zahlungsbedingungen hinterlegen |
| 8c | Dubletten | Zweistufig, Akzeptanz nur mit Begründung | LB; 04b 1.3.4/1.3.5 | **S** | – |
| 9a | E-Rechnung Empfang/Visualisierung (Kat. 2.4) | ZUGFeRD 2.x, XRechnung 3.0 (UBL/CII), Factur-X; PDF-Visualisierung; XML archiviert | LB; ISA | **S** | Neuer Kommunikationsweg von Beginn an (Abschaltung alt 01.01.2027) |
| 9b | Validierung | Nur XRechnung (KoSIT); ZUGFeRD und Profile MINIMUM/BASIC-WL nicht geprüft | EIC §1.3.3; R7 | **S** (XR) / **A** (ZUGFeRD) | Profilprüfung ergänzen; Rückweisung bei Formatfehler |
| 9c | Peppol | Nicht im Produkt; rechtlich nicht erforderlich (E-Mail reicht) | LB; D3; R7 | **N** | Nicht fordern; ggf. externer Access Point → Postfach |
| 9d | Pflichten Livos | Empfang seit 01.01.2025; Aussteller-Übergang bis Ende 2026/2027; steuerfreie § 4 Nr. 8–29 ausgenommen | R1, R2, R7, R8 | – | Lieferanten-Mix 2027/28 einplanen; Ausstellerseite mit StB |
| 10 | Status-Modell/Schritte/Rollen | Standard Verteilung/Prüfung/Freigabe/Buchhaltung; Status Clearing/Eskalation/Transfer; Buchhaltungs- vs. Freigabeuser | SIC; LB; REB; H1 | **S** (Standard) / **K** (Livos-Modell) / **A** („bezahlt") | Schrittmodell gemäß §11 in der Demo nachbauen |

---

## 14. Offene Punkte

| ID | Thema | Konkrete Klärung | Weg |
|---|---|---|---|
| O-01 | Zahlbetrag in der Workflow-Maske | Lässt sich `pay_amount` (Kopf/Position) je Schritt sichtbar und schreibbar schalten? Wie verarbeitet der DATEV-Connector `pay_amount` (Buchung Brutto + Zahlungsvorschlag gekürzt?) | Test Demo-Instanz; d.velop/DATEV-Handbuch (Partnerlogin) |
| O-02 | Kontierungsvorlagen | Prozentuale Verteilung möglich? Kreditorenunabhängige Vorlagen je Gesellschaft? Wo gepflegt, per API übertragbar? | Test; d.velop PM |
| O-03 | Eskalationskanal | Kommt die Eskalationsbenachrichtigung per E-Mail? Kann die Leitung die eskalierte Aufgabe übernehmen oder umleiten? | Test |
| O-04 | IBAN-Warnung | Verhalten der Maske bei IBAN ≠ Stamm; wird die erkannte IBAN im Export-JSON geliefert? | Test; d.velop |
| O-05 | Mandanten-Vorbelegung | Übernimmt der document reader einen per Alias/Importprofil vorbelegten Mandanten? Wird BT-10/BT-46/BT-48 aus E-Rechnungen zur Mandantenermittlung genutzt? | Test mit echten Livos-Belegen; Handbuch `document-reader-invoice` (Partnerlogin) |
| O-06 | Wer hat die Aktion ausgelöst? | Enthält das Export-JSON den handelnden Benutzer (für Durchlaufzeit je Benutzer)? Format des Workflowprotokolls | API-Test; d.velop |
| O-07 | Workflowstatus-Werteliste | Vollständige Werte der Eigenschaft `Workflowstatus` | Test/Partnerlogin |
| O-08 | Rückkanal in den Beleg | Gibt es eine (nicht öffentliche) API, um Custom-Felder oder `pay_amount` laufender Workflows zu setzen (Bim4You-Einbehalt, DATEV „bezahlt")? | d.velop Technology Partner Management |
| O-09 | Bim4You | Wird bei Livos der „Fibu Connector DATEV REB" genutzt? Import-API für PDF/ZUGFeRD-CII? Export von Freigabestatus/Einbehalt? Führendes System je Rechnungstyp | Livos; BRZ/BIB |
| O-10 | FSB/EIBE | Registrierung Livos im EIBE-Portal; Prüfintervall; gibt es beim BZSt eine Sammel- oder Schnittstellenabfrage (öffentlich nicht dokumentiert)? | BZSt-Hotline; Livos-Steuerabteilung |
| O-11 | §13b / Bauabzug steuerlich | Welche Livos-Gesellschaften sind §13b-Schuldner (USt 1 TG)? Bagatellgrenze 15.000 € (nur § 4 Nr. 12) je Gesellschaft; § 17 UStG bei Kürzungen/Einbehalten | Trios/StB |
| O-12 | ZUGFeRD-Profilprüfung | Kann der document reader oder eInvoice converter per Regel/Stylesheet MINIMUM/BASIC-WL erkennen und ablehnen? | d.velop |
| O-13 | Vier-Augen-Prinzip | LB nennt es als enthalten (●, alle Betriebsformen), das Cloud-Handbuch (Stand 06/2026) als Vorschau-Feature über den Support. Verbindlichen Status klären | d.velop Vertrieb |
| O-14 | process studio-Lizenz | Laut LB ist process studio in invoices nur in C2 und nur für Rechnungen enthalten. Lizenz für Vertrags-/Hausverwaltungs-/Mietkontoprozesse in C1? | d.velop Vertrieb |
| O-15 | Mail-Versand aus d.velop | Gibt es inzwischen eine d.velop-actions-Aktion „E-Mail an externe Adresse" (Messaging-App-Templates „bald")? Sonst Middleware | d.velop PM; Beobachtung Release Notes Q4/2026 |

---

## 15. Kurzfazit

- **Besser als im Termin dargestellt:**
  - Eskalation (S), Liegezeit im aktuellen Schritt mit Status und Bearbeiter im REB samt CSV-Export (S);
  - Hinweis auf abweichende Zahlungsbedingung (S);
  - kreditorenabhängige Kontierungsvorlagen und KI-Kontierungsvorschläge auf Belegebene (S/K);
  - Zahlbetrag auf Kopf- und Positionsebene als Träger für Kürzungen (K).
- **Bestätigt als nicht Standard:**
  - automatische Rückweisungs-Mail an Lieferanten (A, klein über Webhook);
  - historische Durchlaufzeit-Auswertung und BI (A);
  - kumulierte Abschlagsprüfung, Einbehaltverwaltung, FSB-Prüfung und Bauabzug (A, fachlich eher Bim4You bzw. Middleware);
  - Peppol (N, rechtlich nicht nötig);
  - ZUGFeRD-Validierung (A).
- **Architekturkritisch:**
  - kein öffentlicher Schreib-Rückkanal in laufende smart-invoice-Belege (Bim4You/DATEV → d.velop);
  - Mandantenerkennung nur über Name und Anschrift, Buckets ≤ 50;
  - Webhook-Timeout 30 s mit Fehlerschritt;
  - Pflicht zum neuen Kommunikationsweg ab 01.01.2027.
- **Korrektur für das Konzept:** Kürzungen nie durch Bearbeitung des Rechnungsdokuments (§ 146 Abs. 4 AO), sondern als Zahlbetrag, Grund und Protokoll im Workflow.
