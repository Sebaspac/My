# 13 — Web-Recherche: Verträge, Post, Akten/Archiv, GoBD, Gesellschaftsverkauf (Stand 26.09.2026)

**Auftrag:** Die Nicht-Rechnungs-Säulen des Livos-DMS (Verträge, Post, Akten/Archiv, Aufbewahrung/Löschung, GoBD, Export je Gesellschaft, Datenzugriff der Finanzverwaltung) per Web-Recherche absichern.
**Kennzeichnung:** **F** = Fakt (mit Quelle belegt) · **A** = Annahme/Bewertung MDIS · **O** = offen (nicht belegt, muss geklärt werden).
**Quellenkürzel:** [Wxx] = Web-Quelle d.velop, [Rxx] = Rechtsquelle (Verzeichnis am Ende). Interne Quellen: [T hh:mm:ss Sprecher] = Transkript, [Kat. x.y] = Leistungskatalog, [04b §x] = Fähigkeitsmatrix Teil B, [B_0x §y] = Befunddateien.
**Lokale Kopien** der ausgewerteten PDFs/Texte: `SP/work/_web13/` (u. a. `documents-PE-LB.txt`, `documents-FB.txt`, `repo-export.txt`, `inbound-scan-LB.txt`, `mail-dispatcher.txt`, `gobd-2024.txt`, `gobd-2025.txt`).

---

## 0. Die wichtigsten Befunde auf einen Blick

| # | Befund | Art | Quelle |
|---|---|---|---|
| 1 | Es gibt ein Cloud-Vertragsprodukt auf d.velop documents: **d.velop contracts** (9 €/Nutzer/Monat lesend, 29 €/Nutzer/Monat voll). Es setzt d.velop documents platform edition voraus und läuft in AWS und T Cloud Public. Alternativ: **alphaflow Contracts** (9/39/49 €), bei dem Freigabe-Workflows und Fristen-Eskalation ausdrücklich genannt sind. | F | [W01][W02][W03] |
| 2 | **d.velop pilot** (LLM-Chat auf Dokumenten, „Fragen zum Dokumentinhalt“) ist in der platform edition **business/ultimate** enthalten. Damit ist die Livos-Frage „kann ich Develop zu dem Vertrag irgendwas fragen“ im d.velop-Standard beantwortbar. Im Termin wurde das verneint („Nicht über Develop direkt“). | F / Korrekturhinweis | [W09 §2.2.4][W15]; [T 01:08:50 André Töpper], [T 01:09:07 Sebastian Pachon] |
| 3 | KI-Dokumenttrennung und KI-Kategorisierung sind nur in der Betriebsform **AWS-Cloud (C1)** und Hybrid verfügbar, **nicht in T Cloud Public (C2)**, und erst ab Edition **business**. Die Wahl der Betriebsform entscheidet also über die Post-Automatisierung. | F | [W09 §2.2.1] |
| 4 | **Aufbewahrungsfristen je Kategorie** hängen an einer frei wählbaren **Datumseigenschaft**. Dazu kommen Löschsperre und automatisches Löschen nach Fristablauf. Änderungen an Frist und Löschsperre werden protokolliert. | F | [W10][W11] |
| 5 | Für die **Revisionssicherheit** sind vorhanden: Versionierung, Statuskonzept (Bearbeitung/Freigabe/Archiv), Aktivitätenprotokoll, automatische PDF/A-Rendition neben dem Original. Das **IDW-PS-880-Testat** ist laut d.velop-Zertifikatsseite für *d.velop documents (on-premises)* ausgewiesen. Ein Cloud-Testat ist öffentlich nicht belegt. | F / O | [W10][W25][W27] |
| 6 | **Export je Gesellschaft:** Die **d.velop documents repo export-API** exportiert Originaldateien aller Versionen und JSON-Metadaten inkl. Notizen, Verknüpfungen und **Aktivitäten**. Delta-Export ist möglich. Der Filter kennt aber **nur Zeit, Kategorie und Dokument-IDs (max. 100)**, **keine Eigenschaft wie „Gesellschaft“**. Freischaltung in der Cloud über den d.velop-Support. | F | [W21] |
| 7 | **BEG IV:** Buchungsbelege müssen seit 01.01.2025 **8 Jahre** aufbewahrt werden (§ 147 Abs. 3 AO, § 257 Abs. 4 HGB, § 14b UStG). Bücher, Jahresabschlüsse und Organisationsunterlagen bleiben bei 10 Jahren, Geschäftsbriefe bei 6. Die Frist **läuft nicht ab, solange die Festsetzungsfrist offen ist**. | F | [R01][R02][R03][R07] |
| 8 | **GoBD 2. Änderung (14.07.2025):** E-Rechnungen im Empfangsformat aufbewahren; bei E-Rechnungen genügt der strukturierte Teil. OCR-Anreicherungen sind nach Verifikation aufzubewahren. Z2 ist neu gefasst (Auswertung plus Nur-Lese-Zugriff möglich). | F | [R06] |

---

## 1. Vertragsmanagement

### 1.1 Produktlandschaft (Stand 09/2026)

| Produkt | Basis / Betrieb | Kernfunktionen (belegt) | Lizenz (Listenpreis) | Eignung Livos | Quelle |
|---|---|---|---|---|---|
| **d.velop contracts** | App auf d.velop documents platform edition (basic/business/ultimate) oder hybrid; **AWS-Cloud und T Cloud Public** | Dashboard mit Status und Laufzeitfortschritt, **Vertragsanlage inkl. Laufzeitberechnung**, Vertragsdetailansicht, **Fristenmanagement/Fristenkalender** („Kündigungs- und Verlängerungsfristen werden … zuverlässig erkannt und rechtzeitig gemeldet“), **Vertragshierarchien**, Archivierung im DMS als **Vertragsakte**, zentrales Aufgabenmanagement, Signaturumlauf mit **d.velop sign**, Outlook-Ablage | **Basic Restricted User 9 €/User/Monat** (lesend), **Basic Full User 29 €/User/Monat** | **hoch** (gleiche Plattform, gleiche Akten und Berechtigungen) | [W01][W02] |
| **alphaflow Contracts** (Partner alphaflow, d.velop store) | Cloud und On-Prem; setzt d.velop documents platform edition ab basic voraus; Hosting AWS Frankfurt | digitale Vertragsakte (versionssicher), individuelle Felder je Vertragstyp, **Fristen mit konfigurierbaren Erinnerungen und Eskalationen**, **„Flexible Genehmigungsprozesse“ ohne Programmierung**, Rahmenverträge, **Zahlungsreihen**, Finanzberichte/Excel-Export, **Organisationen** (Konfiguration), Klauseln; Advanced: KI-Metadatenerkennung, Risikobewertung, Vertrags-Chat | Basic 9 € / **Standard 39 €** / Advanced 49 € je User/Monat (Staffel) | **hoch**, besonders wenn Freigabe-Workflow und Zahlungsreihen (z. B. Mieten, Wartung) im Standard gebraucht werden | [W03][W04] |
| d.velop contracts for Microsoft 365 | SharePoint Online (Ablage in SharePoint-Bibliotheken) | Vertragsakte, Fristen/Stichtagsberechnung, Aufgaben, Signaturen, KI-gestützte Anlage aus Vertragsdokument | ab 39 €/Monat, 12 Monate Mindestlaufzeit | **gering** (zweite Ablageplattform neben d.velop documents) | [W05] |
| dbs \| case manager contract | **d.3ecm/d.3one (On-Prem)**; Kacheln „Neuer Vertrag“, Vertragsübersicht, Partnerverwaltung | Stammdaten (Rahmen-/Einzelvertrag, Vertragstyp, Status, Verantwortliche, Organisationseinheit, Vertragswert), Laufzeit/Fristen (befristet/unbefristet, Kündigungsfrist, einmalige/rollierende „stillschweigende Verlängerung“, Erinnerungen an „Verantwortlich“), Deckblatt, Aktenstruktur | nicht öffentlich | **nein** (On-Prem-Produkt) | [W06] |
| Weitere im Store | ecm:one Vertragsmanagement (Preis je aktivem Vertrag), edoc contract | – | – | nur Marktbeobachtung | Websuche 09/2026 (store.d-velop.com) |

**Bewertung (A):** Für Livos, das auf **d.velop documents Cloud** setzt, kommen nur **d.velop contracts** oder **alphaflow Contracts** in Frage. Die Handbücher zu d.velop contracts (Cloud) sind öffentlich **nicht** abrufbar (PDF-Export `contracts-user/cloud` liefert Fehler 400). Öffentlich dokumentiert sind nur die M365-Variante und alphaflow (v31). → Siehe Offene Punkte O-01.

### 1.2 Anforderungs-Check Verträge

| Livos-Bedarf | d.velop contracts | alphaflow Contracts | Eigenbau (Kategorien + Akten + process studio) |
|---|---|---|---|
| Vertragsakte | **F** „als Vertragsakten im zentralen Dokumentenmanagement-System d.velop documents“ [W01] | **F** digitale Vertragsakte [W03] | **F** Aktenart „Vertragsakte“ + automatische Aktenbildung [W10] |
| Metadaten (Partner, Laufzeit, Kündigungsfrist, Verlängerung, Wert) | **F** geführte Anlage, Laufzeitberechnung [W02]; Einzelfelder laut Blog: „Vertragspartner, Vertragsart, Vertragsnummer, Laufzeit, Kündigungsfristen, Vertragsstatus, Verantwortlichkeiten“ [W07] | **F** individuelle Felder je Vertragstyp [W03] | **F** frei definierbare Eigenschaften/Wertemengen [W10]; Demo hat schon `Livos Vertrag` mit Vertragsnummer und „Gültig bis“ [04_Chrome-Prompt §4] |
| Fristen/Wiedervorlage/Erinnerung | **F** Fristenkalender, automatische Meldung [W01] | **F** Erinnerungen **und Eskalationen** [W03] | **A** process studio Timer-Ereignis / Aufgabe mit Erinnerungsdatum [04b §2.4]; Kündigungsstichtag selbst berechnen (Skript) |
| Freigabe-/Genehmigungsworkflow | **F/O** Produktseite: „Genehmigungs- und Prüfprozesse laufen klar strukturiert …“ [W01]. Die Preistabelle nennt aber keinen Workflow-Baustein [W02] → vermutlich über process studio (**A**) | **F** „Flexible Genehmigungsprozesse“ [W03] | **F** process studio (BPMN, Formulare, Gateways) [04b §2] |
| Vertragserstellung aus Vorlagen | **O** nur im allgemeinen FAQ-Text („Erstellen & Bearbeiten von Verträgen auf Basis von Vorlagen“) [W01], nicht in der Preistabelle | **O** | **F** M365-Office-Dokumente aus d.velop documents erzeugen (business/ultimate) [W09] |
| Signatur | **F** d.velop sign integriert [W01] | **O** | **F** d.velop sign in platform edition business/ultimate: **50 bzw. 100 fortgeschrittene Siegel/Monat/Mandant**; weitere Signaturen kostenpflichtig [W09 §2.2.2]. QES „im Standard“ verfügbar, personenbezogene Signaturen brauchen Identifizierung (Pauschale **17 €/User**) [W08] |
| KI (Analyse, Chat) | **F** KI-Vertragsanalyse beworben [W01]; **d.velop pilot** Chat auf Dokumenten [W15] | **F** nur im Advanced-Plan [W03] | **F** d.velop pilot in business/ultimate enthalten, Token-Limits [W09 §2.2.4] |
| Mehrgesellschaft (>100) | **O** | **A** „Organisationen“ in der Konfiguration (Bedeutung nicht belegt) [W04] | **F** Eigenschaft Gesellschaft + Berechtigungsfilter [W10 „Rollen- und Attributbasierte Berechtigungsverwaltung“] |

### 1.3 Passt das zum Livos-Zielprozess „Eingang → Verarbeitung → Verteilung → Klassifizierung → Fachliche Freigabe → Archivierung“?

| Prozessschritt (Folie A_Livos_DMS_Business_Architektur) | d.velop-Baustein | Beleg |
|---|---|---|
| Eingang | Mail-Funktionspostfach/Alias, Scan (inbound scan), Upload, Outlook-Ablage | **F** [W10 §4.1.1], [W01] (Outlook) |
| Verarbeitung | OCR, KI-Klassifizierung (Kategorie **„Vertrag“** ist unter den erkannten Kategorien von *d.velop document classification*), LLM-Extraktion (d.velop pilot, „Intelligenter Import“) | **F** [W14 S. 11], [W15] |
| Verteilung | mail dispatcher (Aufgabe an Gruppe) oder process-studio-Aufgabe an Vertragsverantwortliche | **F** [04b §3.3], [W16] |
| Klassifizierung | Vertragsart/-typ, Metadaten in d.velop contracts (geführte Anlage) bzw. Kategorie „Vertrag“ | **F** [W02] |
| Fachliche Freigabe | process studio (Eigenbau) / Workflow in alphaflow / ggf. d.velop contracts; anschließend d.velop sign | **F/O** (siehe 1.2) |
| Archivierung | Vertragsakte in d.velop documents, Aufbewahrungsfrist je Kategorie | **F** [W01][W10] |

**Bewertung (A):** Die Schrittfolge lässt sich vollständig abbilden. Bei d.velop contracts ist nur die **Fachliche Freigabe** nicht sicher im Produktstandard belegt. Sie wäre notfalls mit process studio umzusetzen (platform edition business: **1.000 Workflowausführungen/Monat/Mandant**, ultimate unbegrenzt [W09 Fußnote 4]).

### 1.4 Alternative „Eigenbau“ mit Kategorien, Akten und process studio (A)
- **Pro:** keine Zusatzlizenz je Nutzer. Das gleiche Eigenschafts-/Aktenmodell wie bei Rechnungen (Gesellschaft, Kreditor, Objekt) und volle Kontrolle über Felder.
- **Contra:** Kündigungsstichtag, rollierende Verlängerung und Fristenkalender müssen selbst gebaut werden (Skript/Timer). Ein Dashboard „anstehende Fristen“ ist Eigenbau. Das Fristenmanagement muss dauerhaft gewartet werden.
- **Empfehlung:** Eigenbau nur, wenn Livos wenige Vertragsarten mit einfachen Fristen hat. Sonst d.velop contracts pilotieren, bei Workflow-Lücke alphaflow Contracts vergleichen.

---

## 2. Postverteilung in der Cloud

### 2.1 Bausteine

| Baustein | Was er leistet (belegt) | Status Cloud | Quelle |
|---|---|---|---|
| **d.velop inbound scan** | Stapelverarbeitung, Scanner über *d.velop scanner connector* (TWAIN → HTTPS in die Cloud), Importformate u. a. TIF/PDF/EML/ZUGFeRD/XRechnung/Office; Stapel bis 100 Seiten ausgelegt, Import **hart auf 200 Seiten** begrenzt; leere Stapel werden nach 7 Tagen gelöscht | Cloud | [W14 S. 2–4] |
| **KI-Trennung** (*document splitting*) und **KI-Klassifizierung** (*document classification*) | Klassifiziert u. a. Angebot, Auftragsbestätigung, Lieferschein, Eingangsrechnung, Mahnung, **Vertrag**, Protokoll, **Schriftwechsel**. „Erkennt d.velop document classification eine Dokumentart nur zu 80 %, wird das Dokument als ‚Unbestimmt‘ gekennzeichnet.“ Es werden „die drei wahrscheinlichsten Kategorien zur Auswahl angeboten“ | **nur C1 (AWS) und Hybrid, ab business** | [W14 S. 11–12], [W10 §4.1.1], [W09 §2.2.1] |
| **Funktionspostfächer** | „unbegrenzt viele Funktionspostfächer“ bei AWS; bei T Cloud Public über M365-Postfachüberwachung „ein M365-Postfach mit beliebig vielen Aliasen“; Limit **10.000 E-Mails/Monat/Postfach** (C1, H, O) | C1/C2 unterschiedlich | [W10 §4.1.1], [W09 Fußnote **] |
| Barcode/Trennblatt | Barcodeprofile (u. a. **Code 128**, QR, Data Matrix, EAN), Dokumententrennung per Barcode | Cloud | [W10 §4.1.1], [04b §3.4] |
| **d.velop pilot** | „Intelligenter Import“: Dokumentart und -eigenschaften per LLM ermitteln, Absender und Kurzzusammenfassung | Cloud (C1, C2, H), business/ultimate | [W15], [W09 §2.2.4] |
| **d.velop mail dispatcher** (Komponente von **d.velop inbox management**) | Posteingangsverteilung: Aufgabe an Gruppe, Weiterleitung, Erinnerung/Eskalation; **Cloud-Einrichtungsassistent** erzeugt Webhooks und Kategoriezuordnung. „Geben Sie zunächst immer eine Gruppe für den Empfang an.“ | Cloud-Konfiguration dokumentiert; Lizenz/Store-Angebot **O** | [W16 §1.1.1, §1.3.3, §1.4.1], [04b §3.3, §3.5] |
| **VLOTT Postverteilung** (Partner-App, d.velop store) | strukturierte Erfassung, KI über d.velop pilot (Absender, Dokumenttyp, Referenznummer, Datum, Zusammenfassung), **Empfängervorschläge durch KI**, Zuweisung an Benutzer/Gruppen, Ablage in d.velop documents | Cloud und Hybrid; Starter **449 €/Monat** (bis 100 User, 4.000 Dok./Jahr), Professional 5,32 €/User/Monat | [W17] |
| Scan-Limit | „Begrenzung von 10.000 Dokumenten pro Monat und Mandant/Tenant“ beim stapelbasierten Scannen | alle | [W09 Fußnote *] |

### 2.2 Scan-Dienstleister, SFTP, Postmappe
- **F:** inbound scan ist „eine selbständige Anwendung, die eine API zur Verfügung stellt, die es ermöglicht … Dokumente in ein Zielsystem zu importieren“ [W14 §1.3]. Das Entwicklerportal beschreibt die **Inbound-API** für den Import von Seiten aus externen Systemen; Aufruf auch ohne Benutzerkontext per App-Session [W18].
- **F:** Import in d.velop documents ist auch über die **Public REST API** mit Kategorie und Eigenschaften möglich [W10 §4.1.1 „Import per REST-API“].
- **O:** Ein **SFTP-Eingang** ist in keiner öffentlichen Quelle belegt. Einlieferwege für Scan-Dienstleister sind daher **(A)**: E-Mail an ein Funktionspostfach, Inbound-API oder DMS-API (Dienstleister liefert PDF + Metadaten, z. B. Gesellschaft/Empfängergruppe aus Trennblatt-Barcode).
- **O:** Eine „digitale Postmappe“ als Produktfunktion ist nicht belegt. Ersatz **(A)**: Gruppenpostkorb/Aufgabenliste im mail dispatcher [04b §3.3.5] oder VLOTT.

### 2.3 Abbildung Livos-Zielprozess Post „Eingang → Verarbeitung → Klassifizierung → Verteilung → Archivierung“

| Schritt | Baustein | Hinweis |
|---|---|---|
| Eingang | Papier: zentrale Poststelle scannt (Livos scannt schon heute Papierpost ein [T 00:38:42 André Töpper]); E-Mail: Funktionspostfächer je Zweck (z. B. post@, vertraege@, freigabe-rechnungen@ [T 00:21:26 Thomas Gross]) | Postfachmodell hängt von AWS vs. T Cloud Public ab (s. 2.1) |
| Verarbeitung | OCR, Barcode-/KI-Trennung, PDF/A-Rendition | KI-Trennung nur C1/H |
| Klassifizierung | document classification (Vorschlag Top 3) oder d.velop pilot; bei Unsicherheit „Unbestimmt“ → Clearingstelle | Regelwerk nach Absender/Betreff fehlt im mail dispatcher [04b §3.2.8] |
| Verteilung | mail dispatcher: Gruppe → Person, Erinnerung/Eskalation; alternativ VLOTT mit KI-Empfängervorschlag | Empfänger immer als Gruppe (Vertretung) |
| Archivierung | „Es ist für mich“ → Zielkategorie/Akte; Postdokument erbt Gesellschaft | Gesellschaft als Pflichtfeld schon am Postdokument (s. Kap. 6) |

---

## 3. Aktenmodell

### 3.1 Belegte Mechanik
- **F:** „Der Kunde kann in d.velop documents (hierarchische) Aktenstrukturen konfigurieren … Akten können Dokumente oder weitere Akten enthalten. **Eine Akte kann in einer oder mehreren Akten enthalten sein** … so konfigurier[bar], dass durch eingehende Dokumente automatisch anhand ihrer Dokumenteigenschaften passende Akten erstellt werden … Akten können … Metadaten … an eingehende Dokumente vererben.“ [W10 §4.1.2]
- **F:** Ein Dokument wird einmal gespeichert und in mehrere Akten integriert (Mehrfachablage ohne Redundanz) [W19 S. 4], [B_01 §5].
- **F (d.3-Regelwerk, Cloud-Übertragbarkeit A):** Bei der Erkennung muss die **Kombination** der Erkennungswerte übereinstimmen. „**Sind die Eigenschaften der Aktenerkennung leer, so wird keine Aktenverknüpfung ausgeführt.**“ Vererbung wirkt „im Regelfall nur eine Ebene nach oben … und eine Ebene nach unten“. Verknüpfung zu **mehreren übergeordneten Akten** geht über ein Mehrfachfeld („60er-Feld“) als Erkennungseigenschaft. „Akten unterhalb anlegen“ ist für Unterregister möglich, aber mit Einschränkungen (kein Mehrfachfeld, keine Vererbung nach oben) [W19 S. 6–10].
- **F:** Performance: In einer Akte wird standardmäßig mit den **ersten 100 Elementen** gearbeitet (umstellbar) [B_01 §5.5].
- **F (Branchenpraxis d.velop):** Für Immobilienunternehmen nennt d.velop Objektakte, Mieterakte, Bau(technik)akte, **Gesellschaftsakte** und Vertragsakte. Für die Dokumentart genüge „eine einzige Dokumentart …, das ‚Immobiliendokument‘“. Die Zuordnung in mehrere Aktenstrukturen läuft automatisch über Objektnummer, Finanzprojektnummer, Mietvertragsnummer und Mieter [W20, 07.02.2022].
- **Livos-Kontext:** André Töpper fragte nach der Zahl der Ebenen [T 00:57:09]. MDIS empfahl „zwischen 4 und 5 Ebenen allerhöchstens“ [T 00:57:22 Sebastian Pachon]. Die Demo nutzt drei Aktentypen als Sichten (Gesellschaft, Kreditor, Objekt) [A_06 §3.5].

### 3.2 Empfohlener Aktenplan Livos (A)

```
Gesellschaftsakte  [Erkennung: Gesellschaft (DATEV-Mandantennr.)]
 ├─ Objektakte     [Gesellschaft + Objekt-Nr.]
 │    ├─ Vertragsakte   [Gesellschaft + Vertrags-Nr.]   (Miet-, Bau-, Wartungs-, Kauf-, Darlehensvertrag)
 │    └─ (optional) Vorgangs-/Bauprojektakte [Gesellschaft + Objekt + Vorgang/Los]
 ├─ Kreditorenakte je Gesellschaft [Gesellschaft + DATEV-Kreditor-Nr.]  ← Rechnungen, Freistellungsbescheinigung, Rahmenvertrag
 └─ Gesellschaftsdokumente (Satzung, HR-Auszug, Jahresabschluss, Steuerbescheide, Korrespondenz)

Konzernsichten (zusätzlich, KEINE Ablageorte):
 • Lieferant (Konsolidierungsnummer aus MDIS-Stammdaten-App)  → verknüpft alle Kreditorenakten eines Lieferanten
 • Mieterakte (nur falls Livos selbst Mieterdokumente führt; heute buchen v. a. Property Manager)
```

**Designregeln (A):**
1. **Tiefe max. 3–4 Ebenen** (Gesellschaft → Objekt → Vertrag/Vorgang). Das liegt unter der MDIS-Obergrenze 4–5 [T 00:57:22].
2. **Jede Akte trägt die Gesellschaft als Erkennungs-/Pflichtmerkmal.** Die Kreditorenakte ist bewusst **je Gesellschaft** gebildet, weil die DATEV-Kreditorennummer ohnehin je Mandant verschieden ist [BRIEFING]. Die gesellschaftsübergreifende Sicht entsteht über die Konsolidierungsnummer. Grund: Beim Verkauf einer Gesellschaft darf keine Akte Dokumente anderer Gesellschaften mitziehen (Kap. 6).
3. Pflichtfelder so setzen, dass die Erkennungseigenschaften nie leer sind. Sonst wird die Akte nicht verknüpft [W19].
4. Gesellschaftsübergreifende Dokumente (z. B. Konzern-Rahmenvertrag) mit **Mehrfachwert Gesellschaft** ablegen und im Exportfall gesondert behandeln (Kopie/Schwärzung, O-10).

---

## 4. Aufbewahrung & Löschung

### 4.1 Rechtsrahmen (Stand 2026)

| Unterlagenart (Livos-Kategorie) | Frist | Rechtsgrundlage | Fristbeginn |
|---|---|---|---|
| Bücher, Journale, Inventare, **Jahresabschlüsse**, Lageberichte, Eröffnungsbilanz **sowie „die zu ihrem Verständnis erforderlichen Arbeitsanweisungen und sonstigen Organisationsunterlagen“** (→ **Verfahrensdokumentation**, Workflow-Definitionen) | **10 Jahre** | § 147 Abs. 1 Nr. 1, Abs. 3 AO; § 257 Abs. 1 Nr. 1, Abs. 4 HGB [R01][R02] | Schluss des Kalenderjahres (§ 147 Abs. 4 AO, § 257 Abs. 5 HGB) |
| **Buchungsbelege**: Eingangsrechnungen/Gutschriften, E-Rechnungs-XML, Zahlungsbelege, **Verträge als Buchungsgrundlage** | **8 Jahre** (seit 01.01.2025; gilt für alle Belege, deren 10-Jahres-Frist am 01.01.2025 noch lief; Belege ab 2015 dürfen nach 8 Jahren vernichtet werden) | § 147 Abs. 1 Nr. 4, Abs. 3 AO; § 257 Abs. 1 Nr. 4, Abs. 4 HGB; § 14b Abs. 1 UStG („acht Jahre“) [R01][R02][R03][R07] | Schluss des Kalenderjahres, in dem der Beleg entstanden ist (bei Rechnungen: ausgestellt) |
| **Empfangene Handels-/Geschäftsbriefe** (Post, Korrespondenz), Wiedergaben abgesandter Briefe | **6 Jahre** | § 147 Abs. 1 Nr. 2, 3, Abs. 3 AO; § 257 Abs. 1 Nr. 2, 3, Abs. 4 HGB | Schluss des Kalenderjahres des Empfangs/Versands |
| Empfangene Lieferscheine, die keine Buchungsbelege sind | bis Erhalt der Rechnung | § 147 Abs. 3 S. 3 AO | – |
| Sonstige steuerlich bedeutsame Unterlagen | 6 Jahre | § 147 Abs. 1 Nr. 5, Abs. 3 AO | – |
| **Verfahrensdokumentation** | läuft nicht ab, solange die Frist der Unterlagen läuft, die sie erklärt | GoBD Rz. 154 [R04] | – |
| **Ablaufhemmung (alle)** | „Die Aufbewahrungsfrist läuft jedoch nicht ab, soweit und solange die Unterlagen für Steuern von Bedeutung sind, für welche die **Festsetzungsfrist noch nicht abgelaufen** ist“ | § 147 Abs. 3 S. 5 AO [R01] | – |
| Außersteuerliche kürzere Fristen | verkürzen die steuerliche Frist nicht | § 147 Abs. 3 S. 2 AO | – |

**A:** Längere **zivilrechtliche** Aufbewahrungsinteressen gehen über das Steuerrecht hinaus, z. B. Bauverträge und Gewährleistung, Grundstückskaufverträge, Darlehen. Sie sind je Vertragsart mit der Livos-Rechtsabteilung festzulegen. Vertragsdokumente sollten erst nach **Vertragsende** in die Frist laufen (Datumseigenschaft „Vertragsende“ als Bezugsdatum, s. 4.2).

### 4.2 Umsetzung in d.velop documents (Cloud)
- **F:** „Für Kategorien können **Aufbewahrungsfristen** definiert werden, **Löschsperren** eingerichtet werden …“ [W10][W11].
- **F:** Die Frist ist „abhängig von einer vom Kunden gewählten **Datumseigenschaft** der Kategorie“ [W10][W11].
- **F – Achtung Formulierung:** Die LB Cloud (18.02.2025) schreibt: „Nach Ablauf der Aufbewahrungsfrist werden die Dokumente bzw. Akten dieser Kategorie **automatisch gelöscht**“ [W11]. Die neuere Funktionsbeschreibung (16.10.2025) schreibt: „**Es kann konfiguriert werden**, dass die Dokumente nach Ablauf … automatisch gelöscht werden. Während des Aufbewahrungszeitraums kann ein Löschen verhindert werden.“ [W10]
- **F:** „Änderungen an der Definition einer Kategorie bei der Aufbewahrungsdauer und Löschsperre werden ebenfalls **protokolliert**.“ [W10][W11]
- **F (On-Prem-Referenz):** Dort wird die Frist „pro Dokumentart in Monaten“ konfiguriert und bei neuen Versionen neu berechnet. Das automatische Löschen ist standardmäßig deaktiviert. Ereignisorientiertes Löschen läuft über `document_start_lifetime` [W31]. Einheit und Neuberechnung in der Cloud sind **O**.
- **F:** Papierkorb/Backup: Die Plattform hält gelöschte Daten noch **90 Tage** vor, bevor sie „endgültig und nicht wiederherstellbar gelöscht werden“. Backups werden 30 Tage vorgehalten [W13 §2.1–2.2].

### 4.3 Legal Hold / Ablaufhemmung
- **O:** Eine Funktion „Legal Hold“ für einzelne Dokumente oder Akten ist in keiner öffentlichen Cloud-Quelle belegt.
- **A (Umgehungslösung):** Das Bezugsdatum der Frist ist eine **frei gewählte Datumseigenschaft**. Daraus ergibt sich folgende Lösung:
  1. Eigene Eigenschaft „Aufbewahrung ab“ (bzw. „Fristbeginn“) je Kategorie anlegen. Standardwert = 31.12. des Belegjahres bzw. Vertragsende.
  2. Bei Betriebsprüfung, Rechtsstreit oder offener Festsetzungsfrist wird dieses Datum per Massenänderung/Workflow nach vorn geschoben (wirkt wie Legal Hold).
  3. **Automatisches Löschen anfangs nicht aktivieren.** Stattdessen einen jährlichen **Löschlauf mit Freigabe** (process studio: Kandidatenliste → Freigabe Steuer/Recht → Löschen, Protokoll ablegen). So bleibt § 147 Abs. 3 S. 5 AO (Ablaufhemmung) steuerbar.
  - Ob eine Änderung der Datumseigenschaft die Frist in der Cloud neu berechnet, ist mit d.velop zu klären (O-05).

### 4.4 DSGVO-Löschung
- **F:** Art. 17 Abs. 1 DSGVO verlangt Löschung, wenn die Daten „nicht mehr notwendig“ sind. Das gilt aber nicht, soweit die Verarbeitung „zur Erfüllung einer **rechtlichen Verpflichtung**“ (Abs. 3 lit. b) oder zur „Geltendmachung, Ausübung oder Verteidigung von **Rechtsansprüchen**“ (lit. e) erforderlich ist [R08].
- **F (d.velop-Leitlinie):** Bei Eingangsrechnungen wird die GoBD-Pflicht „als höher angesehen, als die Berücksichtigung eines Antrages auf Löschung“. Nach GoBD darf eine protokollierte Teilnahme an einem Freigabeprozess „nicht fristlos gelöscht werden“. Empfehlung: „nach Ablauf einer entsprechenden Zurückhaltungszeit **reguläre Löschläufe**“ laut individuellem **Löschkonzept** [W29 S. 29–31].
- **A:** Livos braucht ein **Löschkonzept je Kategorie** (Frist, Bezugsdatum, Verantwortlicher, Freigabe). Personenbezogene Nicht-Belege (z. B. Bewerbungen, Mieterselbstauskünfte) bekommen kurze Fristen und eigene Kategorien.

---

## 5. GoBD / Revisionssicherheit

### 5.1 Anforderungen (Auszug)
- **Unveränderbarkeit:** „Eine Buchung oder eine Aufzeichnung darf nicht in einer Weise verändert werden, dass der ursprüngliche Inhalt nicht mehr feststellbar ist“. Veränderungen und Löschungen „müssen … protokolliert werden“. Das gilt sinngemäß für aufbewahrungspflichtige elektronische Dokumente (GoBD Rz. 58–59). Unveränderbarkeit kann gewährleistet werden durch Hardware, Software („Sicherungen, Sperren, Festschreibung, Löschmerker, automatische Protokollierung, Historisierungen, **Versionierungen**“) oder organisatorisch („mittels Zugriffsberechtigungskonzepten“). „Auch eine Änderungshistorie darf nicht nachträglich veränderbar sein“ (Rz. 110–111) [R04].
- **Verfahrensdokumentation:** für jedes DV-System; beschreibt den Weg „von der Entstehung der Informationen über die Indizierung, Verarbeitung und Speicherung, dem eindeutigen Wiederfinden und der maschinellen Auswertbarkeit, der Absicherung gegen Verlust und Verfälschung und der Reproduktion“. Sie besteht aus allgemeiner Beschreibung, Anwender-, technischer System- und Betriebsdokumentation. Sie ist bei Änderungen zu versionieren (Rz. 151–154) [R04].
- **E-Rechnung/Format (2. Änderung 14.07.2025):** „Eingehende elektronische Handels- oder Geschäftsbriefe und Buchungsbelege müssen in dem Format aufbewahrt werden, in dem sie empfangen wurden“. Eine Konvertierung ist unter Rz. 135 zulässig. Durch OCR gewonnene Informationen sind „nach Verifikation und Korrektur ebenfalls aufzubewahren“. Bei E-Rechnungen genügt der strukturierte Teil. Der Bildteil ist nur nötig bei steuerlich relevanten Zusatzinhalten („z. B. Buchungsvermerke oder qualifizierte elektronische Signaturen“) (Rz. 131 n. F.). Strukturierte Belege brauchen „keiner bildlichen, sondern nur einer inhaltlichen Übereinstimmung“ (Rz. 118 n. F.). Anwendung ab 14.07.2025 (Rz. 185) [R06].

### 5.2 Was d.velop documents (Cloud) dafür liefert

| GoBD-Anforderung | d.velop-Funktion | Art | Quelle |
|---|---|---|---|
| Versionierung | „Jede Freigabe mit Änderung erzeugt eine neue Version“; Versionsübersicht | F | [W10 §4.1.2] |
| Festschreibung/Status | Statuskonzept **Bearbeitung → Freigabe → Archiv**; Vorversion wird automatisch „Archiv“ | F | [W10 §4.1.2] |
| Änderungsprotokoll | **Aktivitätenprotokoll**: „sämtliche Änderungen an der Datei oder den Eigenschaften“, filterbar | F | [W10 §4.1.2] |
| Originalformat + Lesbarkeit | Original bleibt; **PDF/A-Rendition** wird automatisch als abhängiges Dokument erzeugt; Annotationen werden separat gespeichert („keine Veränderung des Originaldokuments“) | F | [W10 §4.1.2] |
| Achtung: Versionslöschung | „Durch Löschen der aktuellen Version kann die jeweilige Vorgängerversion wieder als Basis … verwendet werden. Eine Version im Status Bearbeitung kann nach Löschung nicht wiederhergestellt werden.“ → Löschrechte auf Versionen streng begrenzen | F / A | [W10 §4.1.2] |
| Workflowprotokolle | smart invoice legt Kategorie **„Workflowprotokoll ERV“** an. Bei process studio ist das Protokoll standardmäßig nur **30 Tage bis 1 Jahr** verfügbar → **„Export in Repository“ aktivieren** | F | [B_00 §AH, §V8] |
| Zugriffs-/Sicherheitslogs | Plattform protokolliert Lese-/Schreibzugriffe, Logins, Rollen- und Konfigurationsänderungen; **Vorhaltezeit 180 Tage** | F | [W13 §3.5] |
| Verschlüsselung/Isolation | AES-256-GCM at rest, TLS ≥ 1.2, Mandantenisolation über Mandanten-ID | F | [W13 §3.1–3.3] |
| **Softwaretestat IDW PS 880** | Zertifikatsseite: „d.velop documents (on-premises)“ und „d.velop postbox (cloud)“ haben die Prüfung nach IDW PS 880 bestanden. Blog 20.04.2022: „d.velop documents ist nach IDW PS 880 zertifiziert“. T-Cloud-Seite: „Ausgehend vom IDW PS880 geprüften d.velop documents …“ | F / **O** für Cloud | [W25][W26][W27] |
| Infrastruktur-Zertifikate | T Cloud Public: **BSI C5 Typ 2**, ISO 27001/27017/27018/27701, ISO 22301, SOC 1/2/3, Trusted Cloud (Infrastrukturanbieter, nicht d.velop-App). d.velop AG selbst: ISO/IEC 27001:2022, ISO 9001, TISAX AL2 | F | [W27][W25] |
| Abgrenzung | Ein Softwaretestat bescheinigt, dass die Software GoBD-konform eingesetzt werden **kann**. Es ersetzt nicht die Verfahrensdokumentation und die ordnungsmäßige Anwendung beim Kunden | F | [W26] |

### 5.3 Verfahrensdokumentation
- **F:** Im d.velop store gibt es die Cloud-App **„GoBD-Verfahrensdokumentation“** (Hersteller **comdatis digital consulting**). Sie enthält eine „vollständige Vorlage für eine GoBD-konforme Verfahrensdokumentation für ausgewählte Funktionen der d.velop cloud Plattform“, die an das Unternehmen anzupassen ist. Preis **ab 199 €/Monat (erster Nutzer), 99 €/weiterer Nutzer**, 12 Monate Mindestlaufzeit. Voraussetzung: d.velop documents basic/business/ultimate [W28].
- **A:** Für Livos gehören **eine** Verfahrensdokumentation für das Gesamtsystem und prozessbezogene Anhänge dazu (ER-Prozess, Post, Verträge, Scan/ersetzendes Scannen, Export/Löschung, Datenzugriff). Sie wird selbst revisionssicher im DMS versioniert (Kategorie „Organisationsunterlage“, 10 Jahre plus Ablaufhemmung Rz. 154).

---

## 6. Export je Gesellschaft bei Verkauf (Katalog 1.6)

**Anforderung:** „Alle Protokolle / Unterlagen müssen z.B. bei Verkauf je Gesellschaft auch exportiert und revisionssicher weitergegeben werden können.“ [Kat. 1.6]. Die MDIS-Hypothese dazu lautet: „Möglich, aber kein Knopfdruck — eher ein Dienstleistungspaket aus Dokumenten, Metadaten und Protokoll in einem neutralen Format“ [Leistungskatalog, Blatt Tabelle1, 1.6].

### 6.1 Werkzeuge

| Werkzeug | Leistung (belegt) | Grenze (belegt) | Quelle |
|---|---|---|---|
| **d.velop documents repo export-API** (+ Kommandozeilen-Client *repo exporter*) | REST-Endpunkt in der Cloud (`https://<tenant>.d-velop.cloud/dmsdocs/r/<repo-id>/export`). Liefert Metadaten im **StandardDocumentImportFormat (JSON)** und Download-URLs; „Für jede Dokumentversion wird eine Datei exportiert“, dazu abhängige Dateien (PDF-/TIFF-Rendition). Die Metadaten enthalten allgemeine, erweiterte und Systemeigenschaften, **Versionsinformationen, Notizen, Verknüpfungsinformationen, Aktivitäten**. Delta-Export möglich; Stammdatenkonfiguration (Eigenschaften, Kategorien) exportierbar. Ausdrücklich als **Exit-Strategie** und für eigene Backups beschrieben | Filter nur **modifiedAfter/-Before, Kategorie, docIds (max. 100)**; Cloud: **Aktivierung je Mandant über d.velop-Support** („Aktivierung der Exportschnittstelle für Multi-Tenant-Mandanten“); Benutzer braucht Recht **„Datenexport“**; keine verschlüsselten Dokumentbäume | [W21 §1.1–1.2.9] |
| Eigenschaften exportieren | Ergebnisliste/Akteninhalt als Excel/CSV, inkl. Mehrfacheigenschaften | nur Metadaten | [W24], [B_01 §5.5] |
| PDF zusammenführen / d.velop documents collector | Sammel-PDF mit Deckblatt, Inhaltsverzeichnis, Seitenzahlen; Auswahl über Suche/Kategorie | Bildexport ohne strukturierte Metadaten; „Akten können nicht exportiert werden“ (Kontextaktion) | [W22], [B_01 §Kontextaktionen] |
| Prozessprotokolle | process studio: „Export in Repository“; platform edition: „Import / Export“ | – | [B_00 §V8], [W09 §2.2.5] |
| **d.velop cloud migration** (für den Käufer) | Importiert einen Export „aus einem beliebigen Drittsystem im vorgegebenen Format“ in ein d.velop-documents-Cloud-System, mit Migrationsbericht. Laut Export-Doku ist das Ausgabeformat „bereits im passenden Importformat für Cloud-Migrationen“ | Käufer braucht d.velop cloud; Kategorie-Mapping nötig | [W23 §1.1.1], [W21 §1.1.2] |
| Vertragsende d.velop | Ältere LB: „Im Falle der Vertragsbeendigung stehen dem Kunden seine Dokumente im gleichen (originären) Format … sowie eine Datei im ‚JSON‘-Format … zur Verfügung“ | In der aktuellen LB Cloud (18.02.2025) und FB (16.10.2025) **nicht mehr enthalten** → O-08 | [W12] |

### 6.2 Konsequenz für die Konzeption (A)
Weil der Exportfilter die **Gesellschaft nicht kennt**, braucht es einen **zweistufigen Export**:
1. Per DMS-Suche (Eigenschaft Gesellschaft = X, alle Kategorien inkl. Akten und Protokolle) die **docIds** ermitteln.
2. Diese in Paketen zu je 100 IDs über die Export-API ziehen. Alternativ die Kategorien exportieren und die JSON-Metadaten clientseitig nach Gesellschaft filtern.

Das ist ein **skriptbares Standardverfahren** (MDIS-Werkzeug), aber kein Knopfdruck. Damit bestätigt sich die Hypothese [Kat. Tabelle1 1.6].

**Konzeptionelle Vorbereitung ab Tag 1:**
1. **„Gesellschaft“ ist Pflichteigenschaft auf ALLEN Kategorien**: Dokumente, Akten, Postdokumente, Workflowprotokolle (smart invoice „Workflowprotokoll ERV“, process-studio-Exporte) und Verfahrensdokumentations-Anhänge. Der Schlüssel ist stabil (z. B. DATEV-Mandantennummer plus Name). Die smart-invoice-Eigenschaft `Mandant` wird darauf gemappt [B_00 §AH].
2. **Akten nie gesellschaftsübergreifend als Ablageort**. Gesellschaftsübergreifende Sichten nur als zusätzliche Akten (Kap. 3.2).
3. **Mehrgesellschafts-Dokumente** (Mehrfachwert Gesellschaft) kennzeichnen. Vor dem Export werden sie juristisch geprüft (Weitergabe fremder Gesellschaftsdaten, Datenschutz).
4. **Export-Runbook** mit Testexport je Quartal für eine Pilotgesellschaft: Vollständigkeit (Anzahl Dokumente/Versionen), Hashes, Übergabeprotokoll, Datenträger/Plattform.
5. **Nach dem Export:** Dokumente der verkauften Gesellschaft sperren (Berechtigung), nicht löschen. Die Aufbewahrungspflicht und Ablaufhemmung beim Veräußerer klären (O-11).
6. **Vertraglich** mit d.velop fixieren: Export-API-Freischaltung, keine Einzelfallgebühren, Verfügbarkeit über die Vertragslaufzeit (Katalog-Hinweis: sonst Vertragsverhandlung [Kat. Tabelle1 1.6]).

### 6.3 Rechtliche Einordnung (A – steuerlich/rechtlich zu bestätigen)
- Beim **Share Deal** bleibt die verkaufte Gesellschaft Trägerin ihrer Pflichten. Ihre Unterlagen müssen ihr (bzw. dem Käufer) daher vollständig, lesbar und maschinell auswertbar folgen (§ 147 Abs. 2 Nr. 2 AO: „während der Dauer der Aufbewahrungsfrist jederzeit verfügbar … maschinell ausgewertet werden können“) [R01].
- **§ 147 Abs. 6 S. 5 AO:** Bei einem Systemwechsel oder einer Auslagerung aus dem Produktivsystem genügt es, nach Ablauf des **fünften Kalenderjahres** nach Umstellung die Daten „ausschließlich auf einem maschinell lesbaren und maschinell auswertbaren Datenträger“ vorzuhalten, sofern noch keine Außenprüfung begonnen hat [R01]. Bis dahin muss der Käufer auch Z1/Z2 ermöglichen können. Das spricht für ein **Import-fähiges Format** (JSON + Originale) statt reiner PDF-Sammlungen.

---

## 7. Datenzugriff der Finanzverwaltung (Z1/Z2/Z3)

**Rechtsgrundlage:** § 147 Abs. 6 S. 1 Nr. 1–3 AO [R01]. Das Zugriffsrecht ist „auf den Rahmen der jeweiligen Außenprüfung beschränkt“ (GoBD Rz. 159 n. F. 2024) [R05].

| Zugriff | Inhalt (belegt) | Umsetzung im DMS (A, soweit nicht anders markiert) |
|---|---|---|
| **Z1** unmittelbar | „Einsicht in die gespeicherten Daten nehmen und das Datenverarbeitungssystem zur Prüfung … nutzen“ [R01] | Prüfer-Benutzer mit **Nur-Lese-Rolle**, Berechtigung gefiltert auf die geprüfte(n) Gesellschaft(en) und Zeiträume (attributbasierte Berechtigung **F** [W10]); Suche, Suchvorlagen und Aktennavigation nutzen. Lizenzfrage Prüfer-User **O** |
| **Z2** mittelbar | Livos wertet nach Vorgaben aus „oder [lässt] von einem beauftragten Dritten maschinell auswerten … und der Finanzbehörde die Datenauswertung im maschinell auswertbaren Format zur Verfügung stellt oder anschließend einen Nur-Lesezugriff ermöglicht“; nur mit vorhandenen Auswertungsmöglichkeiten (Rz. 166 n. F. 2025) [R06] | Gespeicherte Suchen + **„Eigenschaften exportieren“ (Excel/CSV)** **F** [W24]; smart-invoice-Rechnungseingangsbuch (CSV-Export) [04b §1.8] |
| **Z3** Datenüberlassung | Daten „einschließlich der jeweiligen Meta-, Stamm- und Bewegungsdaten sowie der internen und externen Verknüpfungen … und **elektronische Dokumente und Unterlagen** in einem maschinell lesbaren und auswertbaren Format“, auch über eine Datenaustauschplattform (Rz. 167 n. F. 2024) [R05] | **repo export-API** (Originale + JSON-Metadaten inkl. Verknüpfungen und Aktivitäten) **F** [W21] + Metadaten-CSV. Buchungsdaten kommen weiterhin aus **DATEV** (führendes FiBu-System [BRIEFING]); DMS-Belege über Belegnummer/Belegfeld verknüpfbar halten |

**A:** Im DMS müssen der **Beleglink** (DATEV-Belegnummer/Buchungsschlüssel) und die **Gesellschaft** an jedem Beleg stehen. Nur so kann der Prüfer einen Beleg im DMS einer Buchung in DATEV zuordnen (progressive/retrograde Prüfbarkeit).

---

## 8. Empfehlung für Livos

1. **Betriebsform und Edition früh festlegen: d.velop documents platform edition *business* oder *ultimate* in der AWS-Cloud (C1).**
   - Nur dort sind **KI-Trennung, KI-Kategorisierung, unbegrenzte Funktionspostfächer** und stammdatenbasierte Attributierung verfügbar [W09][W10].
   - Enthalten sind d.velop pilot, d.velop sign (50/100 Siegel) und process studio.
   - **Ultimate** wählen, wenn Post- und Vertragsworkflows zusammen mit weiteren Prozessen mehr als **1.000 Workflowausführungen/Monat** erzeugen (A; Mengengerüst prüfen).
   - Den Rechenzentrumsbetreiber der Demo-Instanz `mdisconsulting.d-velop.cloud` verifizieren.
2. **Verträge:** Pilot mit **d.velop contracts** (Full User nur für Vertragsverantwortliche, Restricted für Leser).
   - Parallel die Fragen zu Freigabe-Workflow, Vorlagen und Mehrgesellschaft klären (O-01).
   - Fehlt der Freigabe-Workflow im Standard: Freigabe mit **process studio** plus **d.velop sign**, oder **alphaflow Contracts Standard** vergleichen.
   - Kategorie „Vertrag“ mit Pflichtfeldern: Gesellschaft, Objekt, Vertragspartner/Kreditor, Vertragsart, Beginn, Ende, Kündigungsfrist, Verlängerungsart, Wert, Verantwortlich.
3. **KI-Fragen an Verträge** über **d.velop pilot** (Standard, business/ultimate) im Angebot aufnehmen. Die MDIS-KI-Plattform ist dann Ergänzung für systemübergreifende Fragen (DATEV + DMS). Die Aussage aus dem Termin [T 01:09:07] im Folgetermin richtigstellen.
4. **Post:**
   - **Wege:** Zentrale Poststelle scannt mit Barcode-Trennblättern (Code 128). Funktionspostfächer je Zweck (Post, Verträge, Freigabe-Rechnungen, je Gesellschaft optional per Alias).
   - **Verarbeitung:** KI-Klassifizierung als Vorschlag, „Unbestimmt“ geht in eine **Clearing-Gruppe**. Verteilung **immer an Gruppen**, Erinnerung/Eskalation aktivieren.
   - **Werkzeug:** mail dispatcher (Lizenz/Cloud klären) **oder VLOTT Postverteilung** (KI-Empfängervorschlag, Festpreis-Starter) gegenüberstellen.
   - **Scan-Dienstleister:** Einlieferung per Funktionspostfach oder Inbound-/DMS-API. SFTP nicht einplanen, solange es nicht belegt ist.
5. **Aktenplan:** Gesellschaft → Objekt → Vertrag/Vorgang, dazu die Kreditorenakte **je Gesellschaft**. Konzernsichten (Lieferant/Konsolidierungsnummer) nur als zusätzliche Verknüpfung. Tiefe ≤ 4. Erkennungsfelder als Pflichtfelder.
6. **Aufbewahrung:**
   - **Fristen je Kategorie:** Belege 8 J., Organisationsunterlagen/Abschlüsse 10 J., Post 6 J., Verträge ab Vertragsende.
   - **Bezugsdatum:** eigene Datumseigenschaft „Aufbewahrung ab“.
   - **Löschen:** Löschsperre aktiv, **automatisches Löschen zunächst aus**. Jährlicher, freigegebener Löschlauf (process studio) mit Protokoll. Legal Hold über das Verschieben von „Aufbewahrung ab“ (nach Klärung O-05).
7. **GoBD:**
   - Verfahrensdokumentation als eigenes Arbeitspaket einplanen; Vorlage z. B. comdatis-App oder MDIS-Vorlage.
   - process-studio-Protokolle „Export in Repository“ aktivieren.
   - Versions-Löschrechte nur für Admin.
   - E-Rechnungs-XML im Original aufbewahren.
   - IDW-PS-880-Nachweis **für die Cloud** bei d.velop anfordern.
8. **Verkaufsfähigkeit (Kat. 1.6):**
   - Gesellschaft ist Pflichtmerkmal auf allen Objekten; Export-Runbook plus **Export-Skript (MDIS)** auf Basis der repo export-API.
   - Jährlicher Probeexport.
   - Export-API-Freischaltung und Kostenfreiheit **vertraglich** sichern.
   - Im Angebot als „Standard + Dienstleistungspaket“ bewerten, nicht als Knopfdruck.
9. **Betriebsprüfung:** Rolle „Prüfer (Nur-Lesen)“ mit Gesellschaftsfilter vorbereiten, Z2-Suchvorlagen (z. B. „alle Eingangsrechnungen Gesellschaft X, Jahr Y“) und ein Z3-Exportverfahren (identisch mit Verkaufs-Export) dokumentieren.

---

## 9. Offene Punkte

| ID | Offene Frage | Warum | Weg |
|---|---|---|---|
| O-01 | **d.velop contracts (Cloud):** Enthält es einen Freigabe-/Genehmigungsworkflow, Vorlagen-Erstellung, Mehrgesellschaftsfähigkeit (Gesellschaft als Filter/Berechtigung), Anbindung an eigene Kategorien/Aktenplan? Handbuch (nicht öffentlich) beschaffen | Kernfrage Verträge (R-15) | d.velop Vertrieb/PL |
| O-02 | Ist **mail dispatcher / inbox management** als Cloud-Produkt buchbar (Store, Preis, Lizenzmetrik)? Zählt die Postverteilung auf die process-studio-Ausführungslimits? | Postverteilung (R-19) | d.velop |
| O-03 | Betriebsform der Livos-Instanz: **AWS (C1)** oder **T Cloud Public (C2)**? Welche nutzt die Demo-Instanz? | KI-Trennung/-Klassifizierung und Postfachmodell hängen davon ab | d.velop, IT-Check Demo |
| O-04 | Scan-Dienstleister: offizieller Einlieferweg (Inbound-API, Mail, **SFTP?**), Metadaten-Übergabe (Schlüssel-Wert-Paare), Referenzpartner | R-18 | d.velop, Dienstleister |
| O-05 | Aufbewahrung Cloud: Einheit der Frist, Verhalten bei Änderung der Datumseigenschaft (Neuberechnung?), gibt es Legal Hold/Löschsperre je Dokument, Löschprotokoll, Papierkorb? | Legal Hold, § 147 Abs. 3 S. 5 AO | d.velop PL, IT-Test |
| O-06 | **IDW-PS-880-Testat bzw. Prüfbericht für d.velop documents Cloud** (Umfang, Datum, Prüfer) und ggf. eigenes C5-Testat der d.velop-Plattform | GoBD-Nachweis ggü. Wirtschaftsprüfer | d.velop |
| O-07 | Aufbewahrungsdauer des **Aktivitätenprotokolls** in der Cloud (Plattform-Logs nur 180 Tage). Bleibt die Dokumenthistorie über die volle Aufbewahrungsfrist erhalten? | GoBD Rz. 111 („Änderungshistorie“) | d.velop |
| O-08 | Gilt die Zusage „Dokumente im Originalformat + JSON bei Vertragsbeendigung“ (LB 2022/2023) weiter? Kosten und Fristen der Datenrückgabe bei Kündigung (AGB/SLA 2026) | Exit-Strategie | d.velop, Vertrag |
| O-09 | repo export-API Cloud: Kosten der Freischaltung, Rate-Limits, Export großer Mengen, Filtern nach Eigenschaft geplant? | Kat. 1.6 | d.velop |
| O-10 | Umgang mit **gesellschaftsübergreifenden Dokumenten** beim Verkauf (Kopie, Schwärzung, Zustimmung) | Datenschutz/Vertraulichkeit | Livos Recht |
| O-11 | Steuerlich/rechtlich: Aufbewahrungspflicht und -umfang beim **Share Deal vs. Asset Deal**; muss Livos (Veräußerer/Konzern) Kopien behalten (Konzernabschluss, Organschaft, Haftung)? | Export-Umfang | Livos StB/Recht |
| O-12 | Zivilrechtliche Aufbewahrungsfristen je Vertragsart (Bau/Gewährleistung, Grundstück, Darlehen) und Fristbeginn | Kategorie-Fristen | Livos Recht |
| O-13 | Prüfer-Zugang Z1: Lizenzbedarf für einen zeitweisen Nur-Lese-Benutzer | Betriebsprüfung | d.velop |
| O-14 | GoBD-Randziffern gegen das BMF-Original 28.11.2019 prüfen. Das BMF-PDF war beim Abruf gesperrt (503/Bot-Schutz). Zitiert wurde aus einer Volltextkopie; Rz. 159, 166, 167, 118, 131 aus den BMF-Änderungsschreiben 2024/2025 direkt | Zitiergenauigkeit | MDIS |
| O-15 | d.velop pilot: Datenschutz/Anbieterwahl (Aleph Alpha, OpenAI u. a.), Tokenbudget für ~80 Nutzer, Einsatz auf Verträge mit Personenbezug | KI-Einsatz Verträge | d.velop, Livos DSB |

---

## Quellenverzeichnis

**d.velop / Hersteller (abgerufen 26.09.2026)**
- [W01] d.velop contracts – Produktseite: https://www.d-velop.de/software/vertragsmanagement
- [W02] d.velop contracts – Preise & Pläne: https://www.d-velop.de/software/vertragsmanagement/preise-plaene
- [W03] alphaflow Contracts (d.velop store): https://www.d-velop.de/store/alphaflow-vertragsmanagement
- [W04] alphaflow Vertragsmanagement Handbuch v31 (Konfiguration, Felder): https://help.d-velop.de/docs/de/pub/alphaflow-vertragsmanagement/31/konfiguration ; https://help.d-velop.de/docs/de/pub/alphaflow-vertragsmanagement/31/vertrage/vertrag-anlegen/verfugbare-felder-/vertragsbeginn-vertragsende
- [W05] d.velop contracts for Microsoft 365 – Store: https://store.d-velop.com/en/d.velop-contracts-for-Microsoft-365/10001747-en ; Handbuch PDF: https://help.d-velop.de/docs/api/documentations/de/contracts-m365-user/cloud/pdf
- [W06] dbs | case manager contract: Anwenden 3.3.1: https://help.d-velop.de/docs/api/documentations/de/case-manager-contract-user/3.3.1/pdf
- [W07] d.velop Blog „Digitale Vertragsakte mit KI“ (19.08.2026): https://blog.d-velop.de/prozesse-gestalten/digitale-vertragsakte
- [W08] d.velop sign – Preise: https://www.d-velop.de/software/digitale-unterschrift
- [W09] Leistungsbeschreibung d.velop documents platform edition, D010522551/2025-10-16: https://s3.eu-central-1.amazonaws.com/mediamanager.cloudcenter.service.d-velop.cloud/fe5f22d4-0b44-46d7-aed1-30067e47fe7a
- [W10] Funktionsbeschreibung d.velop documents, D010522543/2025-10-16: https://s3.eu-central-1.amazonaws.com/mediamanager.cloudcenter.service.d-velop.cloud/38b7589a-3cbc-4dfc-a7f5-db2ebb1838e1
- [W11] Leistungsbeschreibung d.velop documents (Cloud), 2025-02-18: https://s3.eu-central-1.amazonaws.com/mediamanager.cloudcenter.service.d-velop.cloud/71677a83-7cdb-4097-bfc1-bec37f37bc07
- [W12] Leistungsbeschreibung d.velop documents, 2023-07-05: https://s3.eu-central-1.amazonaws.com/mediamanager.cloudcenter.service.d-velop.cloud/6d5af2e7-5756-4b38-94ba-d2bd99346c51 (gleichlautend 2022-03-22: …/e1e3abd4-7626-47b1-bb47-580ac2a60ec8)
- [W13] Leistungsbeschreibung d.velop cloud platform, D003884552/2026-07-28: https://s3.eu-central-1.amazonaws.com/mediamanager.cloudcenter.service.d-velop.cloud/42f5a2ba-b16d-4e0c-be37-3f0d6d6f6bee
- [W14] Leistungsbeschreibung d.velop inbound scan: https://s3.eu-central-1.amazonaws.com/mediamanager.cloudcenter.service.d-velop.cloud/866742b8-4106-442c-80f4-567b56d5b922
- [W15] Leistungsbeschreibung d.velop pilot: https://s3.eu-central-1.amazonaws.com/mediamanager.cloudcenter.service.d-velop.cloud/f4f84925-7e60-4f02-8ed3-b34e133faf0b ; Store: https://store.d-velop.com/de/d.velop-pilot-LLM/10003299
- [W16] d.velop mail dispatcher: Administrieren (cloud): https://help.d-velop.de/docs/api/documentations/de/mail-dispatcher-admin/cloud/pdf
- [W17] VLOTT Postverteilung (d.velop store): https://www.d-velop.de/store/vlott-postverteilung
- [W18] Inbound-API (Entwicklerportal): https://portal.d-velop.de/documentation/inapi/de
- [W19] d.3 admin folder scheme 8.2.0: https://help.d-velop.de/docs/api/documentations/de/admin-folder-scheme/8.2.0/pdf
- [W20] d.velop Blog „Digitale Immobilienakte“ (07.02.2022): https://blog.d-velop.de/branchenprozesse/digitale-immobilienakte/
- [W21] d.velop documents repo export-API (cloud): https://help.d-velop.de/docs/api/documentations/de/documents-repo-export-developer/cloud/pdf
- [W22] d.velop documents collector: Anwenden: https://help.d-velop.de/docs/api/documentations/de/documents-collector-cloud/cloud/pdf
- [W23] d.velop cloud migration: Administrieren: https://help.d-velop.de/docs/api/documentations/de/cloud-migration-admin/cloud/pdf
- [W24] d.velop documents: Anwenden (cloud): https://help.d-velop.de/docs/api/documentations/de/documents/cloud/pdf
- [W25] d.velop Zertifizierungen: https://www.d-velop.com/certifications
- [W26] d.velop Blog „IDW PS 880“ (20.04.2022): https://blog.d-velop.de/compliance/idw-ps-880/
- [W27] d.velop documents in der T Cloud Public (Speicher/Zertifikate): https://www.d-velop.de/software/cloud/storage/otc
- [W28] GoBD-Verfahrensdokumentation (comdatis) – Store: https://store.d-velop.com/de/GoBD-Verfahrensdokumentation/10002670 ; LB: https://s3.eu-central-1.amazonaws.com/mediamanager.cloudcenter.service.d-velop.cloud/34521745-3100-4abd-a6c2-44c15431a7f5
- [W29] Informationen zur EU-DSGVO (d.velop): https://help.d-velop.de/docs/api/documentations/de/dsgvo/1.0/pdf
- [W30] d.velop Blog „Aufbewahrungsfristen 2026“ (06.01.2026): https://blog.d-velop.de/compliance/aufbewahrungsfristen/
- [W31] d.3 admin – Aufbewahrungsfristen und Löschen (2023.q3, On-Prem): https://help.d-velop.de/docs/de/pub/admin/2023.q3/aufbewahrungsfristen-und-loschen-von-dokumenten

**Recht**
- [R01] § 147 AO: https://www.gesetze-im-internet.de/ao_1977/__147.html
- [R02] § 257 HGB: https://www.gesetze-im-internet.de/hgb/__257.html
- [R03] § 14b UStG: https://www.gesetze-im-internet.de/ustg_1980/__14b.html
- [R04] GoBD, BMF-Schreiben 28.11.2019 (BStBl I S. 1269): https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Weitere_Steuerthemen/Abgabenordnung/2019-11-28-GoBD.pdf?__blob=publicationFile&v=4 (beim Abruf gesperrt). Wortlaut Rz. 58–59, 107–111, 151–155 zitiert aus der Volltextkopie https://sr-steuer.de/wp-content/uploads/2022/12/GoBD.pdf (Fassung 2014, in diesen Rz. inhaltsgleich; siehe O-14)
- [R05] GoBD 1. Änderung, BMF 11.03.2024: https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Weitere_Steuerthemen/Abgabenordnung/AO-Anwendungserlass/2024-03-11-aenderung-gobd.pdf?__blob=publicationFile&v=4
- [R06] GoBD 2. Änderung, BMF 14.07.2025: https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Weitere_Steuerthemen/Abgabenordnung/2025-07-14-GoBD-2-aenderung.pdf?__blob=publicationFile&v=4
- [R07] BDO zur Verkürzung nach BEG IV (BGBl. 2024 I Nr. 323 vom 29.10.2024): https://www.bdo.de/de-de/insights/accounting-it/hgb/verkuerzung-der-aufbewahrungsfristen-257-abs-4-hgb-durch-das-4-buerokratieentlastungsgesetz
- [R08] Art. 17 DSGVO: https://dsgvo-gesetz.de/art-17-dsgvo/
