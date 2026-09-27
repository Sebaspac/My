# 04a – d.velop-Fähigkeitsmatrix (Teil A) für das Livos-DMS-Konzept

Stand: 26.09.2026 · Arbeitspaket 04a · Grundlage: allgemeine d.velop-Recherche (B_00, B_01, B_03)

---

## 0. Lesehilfe

### 0.1 Quellenumfang (vollständig gelesen)

| Kürzel | Datei (SP/txt/…) | Inhalt / Gliederung |
|---|---|---|
| **B00** | B_00_BEFUNDE_konsolidiert.md | Konsolidierte Befunde, Abschnitte **A–AU** (Teil 1 Anwender A–E, Teil 2 Admin F–M, Teil 3 Inventur N–T, Teil 4 Workflows U–W, Teil 5 Dashboards X–AF, Teil 6 Eingangsrechnungen AG–AQ, Teil 7 Post/Mailimport AR–AU) |
| **B01** | B_01_Anwendersicht_d3one_documents.md | Anwendersicht, Abschnitte 1–8, Editionsvergleich („EV"), Offene Punkte **OP1–OP12** |
| **B03** | B_03_Administration_Berechtigungen.md | Administration, Abschnitte 1–8, Offene Punkte **OP1–OP11**, „Drei Punkte" (Schluss) |

Nicht Teil dieser Auswertung (Teil B / andere Arbeitspakete): B_02 (smart invoice), B_04 (process studio), B_06 (Post/Mailimport), Transkript, A-Dateien. Wo B00 Inhalte daraus zusammenfasst, wird **B00** zitiert.

### 0.2 Zitierweise
- `[B00 §J]` = Datei B_00…, Abschnitt J · `[B01 §5.4]` · `[B03 §5b]` · `[B03 OP7]` = Offener Punkt 7.
- `[A]` = Handbuch „d.3one und d.velop documents: Anwenden", 2026.q3 (klassisch/On-Premises) · `[B]` = „d.velop documents: Anwenden", Version *cloud* – Definition nach [B00 §A], [B01 Quellenlage].
- `Uxx` = URL aus dem **Quellenverzeichnis (Anhang)**, so wie in den Quelldateien angegeben. `HB` = `https://help.d-velop.de/docs/de/pub`.

### 0.3 Kennzeichnung
- **F** = Fakt, in der Quelle als Beleg aus der d.velop-Doku ausgewiesen.
- **Abl.** = Ableitung/Annahme (der Recherche-Agenten oder von 04a). Nicht als Produkteigenschaft zusagen.
- **Offen** = nicht belegt / zu klären.
- Plattform: **C** = für Cloud belegt ([B] bzw. Cloud-Handbuch) · **O** = nur für On-Premises / d.3 admin / [A] belegt · **C+O** = beide · **?** = Betriebsform in den Quellen nicht angegeben.

### 0.4 Befunde mit der größten Tragweite (Vorwegnahme)
1. **Die Berechtigungs- und Mandantenmechanik ist nur für On-Premises öffentlich belegt.** Dokumentklassen, Makros (`@D3GROUP`, `@D3USER_OPTFIELD_XX`, `@D3SET`), dokumentartunabhängige Klasse, Sub-Administration und automatische Aktenbildung stehen in d.3 admin (On-Prem). Die Cloud-Admin-Doku ist nicht öffentlich [B00 §L; B03 §8a, §8c, OP7]. Livos plant Cloud [Briefing] → **das ist das Kernrisiko des Konzepts**.
2. **Mandantenfähigkeit:** Die Doku hat kein Kapitel dazu. Tragfähig ist (Abl.) *1 Repository + Pflicht-Eigenschaft „Gesellschaft" + Dokumentklasse mit Makro + Gruppe je Gesellschaft*. Belegt sind nur die Bausteine und die Doku-Beispiele „Dokumente eines Mandanten" / „eines Firmenstandorts" [B00 §J; B03 §4]. **smart invoice** hat ein eigenes Mandantenmodell mit Hierarchie (`parent_id`) [B00 §I].
3. **Änderungsprotokoll:** Es heißt „Aktivitäten" und ist nur in der Cloud belegt. Die Begriffe Historie, Änderungsprotokoll und Audit kommen in den Anwenderhandbüchern **nicht vor**. „Revisionssicherheit" kommt in der Anwenderdoku genau 1× vor (beim Schwärzen). Zur GoBD gibt es keine Aussage [B01 §7.2–7.3; B00 §B, §D2].
4. **Externe:** „Extern Teilen" (Link, Zeitraum, lesen/bearbeiten) gibt es **nur in der Cloud und nur mit der Edition d.velop documents business** [B00 §E; B01 §8.3]. Ein Lizenzmodell ist darüber hinaus **nicht belegt**.
5. **Hinter Login:** Die Handbücher zu DATEV (connect for datev), Standardaktenplänen, Lieferantenakte, Reporting und zur gesamten Cloud-Administration sind nur nach Login zugänglich [B00 §P].

---

## 1. Produkt-/Modullandkarte d.velop

Relevanzstufen für Livos: **Hoch** = Kern des Zielbilds (ER, Verträge, Post, >100 Gesellschaften, Cloud) · **Mittel** = unterstützend · **Gering** = nur On-Prem, Alternative oder Altwelt.

### 1.1 DMS-Kern, Oberflächen, Administration

| Produkt/Modul | Betrieb (belegt) | Funktion (kurz) | Relevanz Livos | Doku-Zugang | Quelle |
|---|---|---|---|---|---|
| **d.velop documents** | C+O (Cloud-Handbuch [B]; On-Prem-Installationshandbuch „Installieren und Aktualisieren von d.velop documents (On-Premises)") | DMS-Anwenderoberfläche: Ablage, Suche, Akten, Aufgaben. Nur Cloud [B] zusätzlich: Aktivitäten, Teilen, Scannen/Stapel, Layouts, d.velop pages | **Hoch** – Plattform des Zielbilds | Anwenden frei; Cloud-Admin **Login** | B00 §A, §E; B01 Quellenlage, EV; B03 §8a; U02, U35 |
| **Edition „d.velop documents business"** | C | Voraussetzung für „Extern Teilen" außerhalb der Organisation | **Hoch** – externe Beteiligte | – | B01 §8.3; B00 §E |
| **d.3one** | O ([A] 2026.q3) | Klassische Oberfläche für das d.3-Repository mit gleicher UI in Browser, Outlook, Microsoft Office und HCL Notes; Prozessportal; Facettensuche | Mittel (nur bei On-Prem/Hybrid; Outlook-/Office-Integration) | frei; Admin-Handbuch `one` 2026.q3 frei | B01 §1.1, Quellenlage; B00 §O; U01 |
| **d.3ecm / d.3-Repository / d.3 server** | O (Begriff in [A]) | Repository-Schicht: „Der Lebenszyklus eines Elements wird in d.3ecm mithilfe von verschiedenen Dokumentstatus … dargestellt"; d.3 server vergibt temporäre Dokumentklassen | Hoch (technischer Kern, Abl.) | – | B01 §7.1; B03 §5e |
| **d.3 admin** | O (Version 2026.q1, „hinkt hinterher") | Verwaltung von Dokument-/Aktenarten, Eigenschaften, Wertemengen, Dokumentklassen, Berechtigungsprofilen, Benutzern/Gruppen, Sub-Administration | Hoch als Referenzmodell; ob es in der Cloud ein Gegenstück gibt, ist **Offen** | frei | B00 §F, §K, §O, §R; B03 §1–7 |
| **d.3 admin folder scheme** | O (8.2.0) | Automatische Aktenbildung: Regelwerk, Erkennung, Vererbung | **Hoch** (Akten nach Gesellschaft/Kreditor/Objekt) | frei | B00 §K12, §O; B03 §7; U46 |
| **d.3 restriction set manager** | O (Doku 2023.q3) | Berechtigungsmengen für `@D3SET`, Pflege an Fachverantwortliche delegierbar | Mittel/Hoch (Delegation je Gesellschaft) | frei | B03 §5d; U42 |
| **d.3 inherit rights manager** | O | Ad-hoc-Rechtevererbung von Dokument auf Dokument | Gering | frei | B03 §5e; U41 |
| d.3 import · d.3 smart explorer · d.3 config · d.3 async job inspector · d.3 cockpit | O | Import-Dialog (öffnet sich bei fehlenden Pflichtfeldern) · Explorer · Konfiguration (z. B. 60er-Felder bis 2.000 Einträge) · asynchrone Jobs · Cockpit (Host des flow designer) | Gering (On-Prem-Werkzeuge) | – | B03 §3d, §3e, §7e, §7f, §8c; B00 §U |
| On-Prem-Infrastruktur: d.velop software manager, d.ecs http gateway, identity provider, jstore, d.3 process manager, d.ecs shell, d.ecs config | O | Voraussetzungen für den Betrieb (z. B. des Dashboards) | Gering (in der Cloud „bereitgestellt") | – | B00 §AD; B03 §8a |
| **d.velop cloud: Administrieren** (`cloud`) | C | Gesamte Cloud-Administration | **Hoch** – Pflichtlektüre für das Cloud-Konzept | **Login** | B00 §P; B03 §8a, OP7 |
| **d.velop usermanagement** (`usermanagement-cloud-on-premises`) | C (+O laut Slug) | Benutzerverwaltung | Hoch | frei, **nicht ausgewertet** | B00 §O |
| **d.ecs identity provider** / **d.ecs open id provider app** | O (Installationshandbuch) | Active Directory, Kerberos, OpenID Connect, Benutzeranmeldedaten; Anmeldung auf Gruppen einschränkbar; Sync stündlich; OIDC-Bereitstellung für Drittsysteme | Hoch (SSO) | frei | B03 §6e; U44 |
| **Dashboard / Startseite** (Home-App, `dashboard-admin` 1.9.1 = cloud) | C+O (Admin-PDFs byteidentisch) | Startseite mit Widgets, Sichtbarkeit je Benutzer/Gruppe, Verknüpfungs-/Listen-/iframe-Widgets | Mittel | frei | B00 §X–§AD |
| **Prozessportal** (Feature) | O (nur [A]) | Workflows und Formulare **ohne Dokumentbezug** starten, „Formulare als Übersichten und Auswertungen"; Bezeichnung durch Admin änderbar | Mittel (Kandidat für die Management-Sicht) | Handbuch „Processportal und Formularintegration": **Login** | B01 §1.4; B00 §E, §P |
| **d.velop pages** | C ([B] Kap. 1.3.6) | **Nicht ausgewertet** (evtl. native Dokumenterstellung) | Offen | frei | B01 §4.5, OP12 |

### 1.2 Eingang und Erfassung

| Produkt/Modul | Betrieb | Funktion | Relevanz Livos | Doku | Quelle |
|---|---|---|---|---|---|
| **d.velop inbound** | C | Rechnungseingang aus Mail, Scan und Dateiimport; Stapel | **Hoch** (ER-Eingang) | – | B00 §AG |
| **d.velop inbound e-mail** | C | Push-Modell: Anwender senden an vom Admin definierte Postfächer; zugelassene Absender mit Wildcards; **Outlook-Add-In** (Manifest `https://<TenantUri>/inboundoutlook/addin`) | Hoch | frei | B00 §AT, §O |
| **d.velop email import** | C | Überwacht Postfächer. Produktiv nur **Microsoft 365 (Graph)**; Exchange On-Prem über „d.velop email fetcher" (EWS); IMAP „zukünftig verfügbar"; nur **eine** Bereitstellungsform. **Alias-Adressen** mit je eigenem Importprofil und Schlüssel-Wert-Paaren | **Hoch** (Sammelpostfach mit Alias je Gesellschaft) | frei | B00 §AS; U55 |
| **d.velop inbound scan** | C+O | Scannen, Import-Widget (max. 4 Dropzones je Widget), Barcode-/Trennblatterkennung, Kategorien/Eigenschaften in der Cloud | Hoch (Papierpost) | frei | B00 §AC, §AU, §O; B03 §8b |
| **d.velop inbox management / d.velop mail dispatcher** | C | Posteingangsverteilung (Papierpost/Scan) – **nicht** E-Mail-Verteilung | Hoch (Postprozess) | frei | B00 §AR, §AU |
| **d.velop document reader** (Ausprägung **invoice**) | C+O (7.20.2 / 2.3.0) | OCR und Klassifizierung; erkennt Mandant/Lieferant über Stammdaten (Mandant über Name + Anschrift) | Hoch | reader frei; **invoice: Login** | B00 §AG, §AI, §O, §P |
| d.classify / d.capture batch | ? | Klassifizierung, Stapelerfassung | Mittel (Post/Verträge) | **Login** | B00 §P |
| d.ecs rendition service · d.ecs OCR (API) · classcon documentreader (API) | ? | Rendition, OCR | Mittel (Volltext) | API frei | B00 §AU, §Q |
| **d.velop eInvoice converter** | C | Konvertiert und validiert E-Rechnungen (ZUGFeRD, XRechnung) | Hoch (E-Rechnung) | frei | B00 §AG, §AP |

### 1.3 Prozesse, Aufgaben, Rechnungsbearbeitung

| Produkt/Modul | Betrieb | Funktion | Relevanz Livos | Doku | Quelle |
|---|---|---|---|---|---|
| **d.velop smart invoice** | C + O (2.11.9) + API | Prüf- und Freigabeworkflow für Eingangsrechnungen („das Herzstück"): Mandanten, Freigabematrix, Kontierung/Kostenobjekt, **Onboarding-Assistent** | **Hoch** | frei | B00 §I, §AG–§AM, §O |
| **d.velop invoices – Rechnungseingangsbuch** (`invoice-monitor`) | C | Arbeitsliste und Überblick über „Verbleib und Bearbeitungsfortschritt aller Rechnungen"; Filter, Gruppierung, Clearing-Modus | **Hoch** (Management-Sicht ER) | frei | B00 §AA, §AO |
| **d.velop process / process studio** (Bausteine: process modeler, forms, scripting, ab 2025.q1 actions eventbridge) | process: C (1.15.0) + O (1.22.0); studio Anwenden 2026.q3, Admin 2023.q4 | BPMN-2.0-Prozesse, Formulare, Skripte, Geschäftsregeln, Automatisierungen, Routinen | **Hoch** (Verträge/Post, Sonderfreigaben) | frei | B00 §U–§W, §O, §R |
| d.ecs kickstart4process | ? (1.0.1) | Einfache Prozesse ohne BPMN-Editor | Gering | – | B00 §U |
| d.3 flow designer / d.3 flow inspector | O | Klassische d.3-Workflows (Plugin für d.3 cockpit) | Gering (Altwelt) | **Login** | B00 §U, §P |
| **d.ecs task** / **d.ecs userprofile** | C+O (task 2.18.0) | Aufgabenverwaltung, Benachrichtigungen (Message-Center), Benutzerrollen / Abwesenheit, Vertretung | Hoch | frei | B00 §U, §V5, §V6; B03 §6c |
| d.ecs forms | ? | Formulare für das Prozessportal | Gering | **Login** | B00 §P |
| alphaflow Eingangsrechnungen · alphaflow App Studio | ? | Alternativprodukte: Organisationen statt Mandanten; filterbare Dashboards, eigene Lizenz | Gering („nicht unser Weg") | – | B00 §AG, §AE |

### 1.4 Archiv, Compliance, Konnektoren

| Produkt/Modul | Betrieb | Funktion | Relevanz Livos | Doku | Quelle |
|---|---|---|---|---|---|
| **d.ecs storage manager** (3.20.0) | ? | Revisionssicherheit, Retention, API-Endpunkt `extendretention` | **Hoch** (GoBD/Aufbewahrung) | frei, **nicht ausgewertet** | B00 §O, §T |
| **DSGVO / Datenkommunikation** (`dsgvo` 1.0) | ? | DSGVO-Handbuch | Hoch | frei, **nicht ausgewertet** | B00 §O |
| d.velop records management | ? | Nur als OpenAPI-Spezifikation erwähnt | Offen | – | B00 §X |
| **d.velop connect for datev** (Admin 5.3.0 / Anwenden 5.0.0) | ? | „Einzige echte DATEV-Doku" | **Hoch** (ER-Journale, Zahlungen) | **Login** | B00 §P, §AQ |
| connect for privatabrechner (Praxisleitfaden) | O | Beleg für das „connect for"-Muster; empfohlene Reihenfolge: Eigenschaften → Arten → Berechtigungsprofile | Gering (methodisch) | frei | B03 §2; U56 |
| Standardaktenpläne · d.3 Lieferantenakte (`supplier-file`) | ? | Vorlagen für Aktenstrukturen; Kreditorenakte | **Hoch** (Aktenplan) | **Login** | B00 §P |
| Reporting / Workflow-Auswertungen | ? | Management-Sicht | Hoch | **Login** | B00 §P |
| d.velop sign | ? | Nur als OpenAPI-Spezifikation erwähnt (ohne Widget-Registrierung) | Offen (Vertragssignatur?) | – | B00 §X |

### 1.5 In den Quellen B00/B01/B03 **nicht** belegt
- **d.velop contract, d.velop postbox, d.velop pilot, d.velop archive**, „d.velop mail" als eigenes Produkt, eine **Mobile App**, der Funktionsumfang eines DATEV-Konnektors und ERP-Konnektoren (z. B. connect for SAP) → **Offen**.
- Hinweis 04a (Stichwortsuche über SP/txt): „d.velop pilot" und „d.velop records management" erscheinen in **B_06**, „d.velop connect for datev" und „connect for Microsoft …" in **B_02** → mit Teil B abgleichen. „contract" bzw. „d.velop contract" steht in keiner Datei von SP/txt (0 Treffer).
- **Dokumentationslage insgesamt:** 310 Handbücher, davon 157 frei und 153 nur nach Login. Von 132 Livos-relevanten Handbüchern sind **52 frei, 80 nur nach Login** [B00 §N]. Alle 47 REST-APIs sind frei [B00 §Q].

---

## 2. Strukturmodell

### 2.0 Modell (belegt) und Begriffe

```
Repository (eigene Datenbank)
 └── Kategorie = Dokumentart | Aktenart   (max. 2.000 je Repository)
      └── Erweiterte Eigenschaften (max. 89 je Art; zentral angelegt, mehrfach zugeordnet)
           └── Wertemenge (optional, als Wertevorrat = Auswahlliste)
      └── Aktenbildung (Regelwerk der Über-/Unterordnung)
```
Quelle: [B03 §1] (Modell), [B00 §G].
**Begriffe (F):** In der Anwender-/Cloud-Oberfläche heißt es „Kategorie" (Oberbegriff für Dokumentart und Aktenart), in d.3 admin „Dokumentart"/„Aktenart" (Feld „Art"). Metadaten heißen „Eigenschaften": „allgemeine" (System) und „erweiterte" (kundenspezifisch) [B00 §B, §F; B01 §4.3; B03 §1]. „Element" steht für Dokument oder Akte [B01 §1.1].

### 2.1 Fähigkeitsmatrix Struktur

| # | Baustein | Belegte Fähigkeit (F) | Parameter / Grenzen (F) | Plattf. | Bedeutung für Livos (Abl.) | Quelle |
|---|---|---|---|---|---|---|
| S01 | **Repository** | „Zentraler Speicherort, um Dokumente und Akten systematisch zu sammeln und mithilfe von Metadaten zu verwalten"; eigene Datenbank; mehrere Repositories möglich | Server ID aus 1–2 Großbuchstaben (z. B. T/P); Anlage On-Prem über das Windows-Startmenü; für die Cloud **nicht dokumentiert** | O (Anlage), Cloud **Offen** | Ein Produktiv-Repository für alle Gesellschaften, siehe §3 | B03 §1, §4 (Mech. 1), §8a; U35 |
| S02 | **Kategorie** (Dokumentart/Aktenart) | Dokumentarten nehmen Dokumente auf; Aktenarten nehmen über- und untergeordnete Elemente auf („in eine Aktenart werden Dokumente nicht direkt abgelegt") | max. **2.000** je Repository; Name max. 50 Zeichen, eindeutig; **Kürzel max. 5, nachträglich nicht änderbar**; Lebensdauer (Standard 50 Jahre); nach Änderungen **neu anmelden** | O (Admin), C (Begriff) | Kürzel-Schema vor Anlage festlegen; keine dritte Ebene unterhalb der Kategorie, siehe S02a | B03 §1, §2; B00 §K1 |
| S02a | Klassifikationstiefe | „Eine dritte Ebene (z. B. ‚Dokumenttyp' unterhalb der Kategorie) gibt es in der Anwenderdoku nicht." | – | C+O | Feinere Unterscheidung (z. B. Belegart) über Eigenschaft + Wertemenge | B01 §4.3 |
| S02b | Optionen je Dokumentart | Ungeschützter Webzugriff · **4-Augen-Prinzip** („Prüfung durch andere Person als Bearbeiter") · **Vorbuchen** („Erfassung von Metadaten ohne Dokument") · Auslagerung auf Sekundärspeicher · Cache-Verweildauer · **Farbmarkierungen** (bis 24) · Repository-ID (Speicher-Pool) | Repository-ID: 2 Zeichen, **5 IDs**, **kein** Mandantenkonzept | O | 4-Augen-Prinzip für Verträge prüfen; „Ungeschützter Webzugriff" nicht aktivieren | B03 §2, §4 (Mech. 2); B00 §K1 |
| S03 | **Allgemeine Eigenschaften** | Werden beim Speichern automatisch erzeugt (z. B. Erstellungsdatum, Besitzer, Dokumentnummer) und „können nicht bearbeitet werden" | – | C+O | Zeitstempel und Besitzer sind systemseitig manipulationsfest (Abl.) | B01 §4.3; B03 §1 |
| S04 | **Erweiterte Eigenschaften** | Werden **zentral einmal angelegt** („Vorratskammer") und **mehreren Dokumentarten zugeordnet** | max. **89 je Art**: 49 alphanumerisch, 10 Datum, 10 Geld, 10 numerisch, 10 Mehrfach · Positionen 1–49 / 50–59 / 60–69 (Mehrfach) / 70–79 (Geld) / 80–89 (numerisch) · **Position nachträglich kaum änderbar** · Titel max. 50 Zeichen (nur `+ - _`, kein `:`) · Länge On-Prem 35 Bytes Standard, max. 250 Bytes; in der Cloud (inbound scan) bis 7.000, teils 2.000 Zeichen · Beschreibung max. 255 | O (d.3 admin); C: Eigenschaften anlegen belegt nur über inbound scan („Konfiguration > Import > Importoptionen > Kategorien und Eigenschaften") | Eigenschaftskatalog und **DB-Positionsplan** vor der ersten Ablage festschreiben. „Gesellschaft" in allen Kategorien auf **dieselbe Position** legen (nötig für die dokumentartunabhängige Klasse, §3/§4) | B03 §1, §2, §3c, §8b; B00 §G, §K3, §L |
| S05 | **Datentypen** | Genau fünf: Alphanumerisch, Numerisch, Datum, Datum und Uhrzeit, Geld (Cloud: „Währung") | **Kein Boolean**; „Auswahlliste" und „Mehrfachauswahl" sind **keine** Datentypen | C+O | Ja/Nein-Felder (z. B. §13b, „FSB geprüft") über eine Wertemenge „Ja/Nein" (Abl., nicht dokumentiert) | B03 §3a; B00 §H |
| S06 | **Wertemengen** | Vier Arten: manuell · aus Datenbanktabellen · aus Hook-Funktionen · vordefiniert dynamisch (z. B. Benutzer-/Gruppenlisten). Werden als **Wertevorrat** zugeordnet; eine Änderung „wirkt sich automatisch auf alle zugehörigen Dokumentarten aus". Doku-Beispiel: Wertemenge „Firmen" → Feld „Firma" | Bezeichnung max. 255 · Wert max. 250 Zeichen · Sortierung ab v7.1.1 · Übersetzung (Dokumente und Akten → Mehrsprachigkeit) · **ab v7 nur Zahlen als Werte + Übersetzung** möglich | O (Hooks nur O) | Gesellschaften, Belegarten, Objekte als Wertemengen; stabile numerische Schlüssel + Anzeigetext. Eine **Obergrenze an Einträgen ist nicht dokumentiert** | B03 §3b; B00 §K2 |
| S07 | **Mehrfacheigenschaften** | Mehrere Werte je Feld; in der Oberfläche mit Tabellensymbol gekennzeichnet | Nur Positionen 60–69 · Standard **100 Werte**, über d.3 config bis **2.000** (On-Prem) · alphanumerisch 250 Bytes · **ein Wert je Eintrag, keine Wertepaare** | O (Erweiterung), C? | „Kostenstelle mit Anteil" **nicht** in documents abbilden, sondern in smart invoice (Kostenobjekt) | B03 §3e; B00 §H, §AM |
| S08 | **Plausibilitätskontrolle** | Minimum/Maximum, **reguläre Ausdrücke**, Hook-Funktionen | **Keine Eindeutigkeitsprüfung** (Unique) dokumentiert | O (Hooks nur O) | Formatprüfung für Rechnungsnummer, USt-IdNr. usw. per RegEx; eine Dublettenprüfung muss aus smart invoice kommen (Teil B) | B03 §3c, §4, OP6; B00 §M |
| S09 | **Pflichtfelder** | Festgelegt **je Dokumentart** (nicht an der Eigenschaft): „muss beim Import (manuell oder Hostimport) … gefüllt werden. Bleibt es leer, wird eine Fehlermeldung erzeugt." Anwender prüfen über **„Eigenschaften überprüfen"**. Kann die automatische Ablage Pflichteigenschaften nicht übernehmen, wird der Anwender zur manuellen Ablage geleitet | Versteckte Felder nicht zugleich als Pflichtfelder definieren · **Wie Pflichtfelder in der Oberfläche gekennzeichnet werden, ist nicht beschrieben** | O (Konfig.), C+O (Anwender) | „Gesellschaft" in **allen** Kategorien Pflicht (Voraussetzung für Aktenbildung und Rechte) | B03 §3d; B01 §4.4, OP7; B00 §K4 |
| S10 | Feld-Details je Dokumentart | **Modifizierbar** (Änderung nur für Berechtigte = „geschützte Eigenschaft") · **Titelfelder** (Anzeige in Ergebnislisten) · **Ausblendbar** (Recht „Lesen versteckter Eigenschaften") · **Erweitert** (Großschreibung, Sichtbarkeit in d.3 import / smart explorer, Sortierung, Gruppierung, **dynamische Lebensdauerberechnung**) | – | O | „Gesellschaft" nach der Freigabe als nicht modifizierbar/geschützt einstellen (Abl.) | B03 §3d; B00 §K4 |
| S11 | **Akten / Aktenhierarchie** | „Akten bilden die logische Klammer um mehrere Dokumente und auch Akten" → **Akten in Akten**; Begriff „Hauptakte" = oberste Ebene | Aktennavigation lädt standardmäßig die **ersten 100 Elemente** (umstellbar: Zahnrad → Suchergebnisse und Aktennavigation → Akteninhalte immer vollständig laden) | C+O | Hierarchie Gesellschaft → Kreditor / Objekt → Vorgang möglich; große Kreditorenakten beachten (100er-Grenze) | B01 §5.1, §5.5; U08 |
| S12 | **Mehrfachzuordnung („Sichten")** | Dokument „nur ein einziges Mal … gespeichert, aber in alle Akten integriert"; „Verweise statt Redundanz"; verschiedene Aktenstrukturen über die **Hauptakte** umschaltbar | Der Begriff „Sicht" ist **kein** d.velop-Begriff | C+O | Eine Rechnung zugleich in Gesellschafts-, Kreditoren- und Objektakte → tragfähig | B01 §5.1, §5.5; B03 §1; B00 §C4 |
| S13 | Akte manuell erstellen | Feature **Aktenerstellung**; Kategorie oder **Vorlage** wählen; **Vorlagen zur Aktenerstellung** (Sternchen → „Als Vorlage speichern") | Feature sichtbar **nur für Mitglieder der „Gruppe zum Erstellen von Akten"**; Akte anlegen und Dokument einlegen sind getrennte Vorgänge | C+O | Aktenanlage auf einen kleinen Kreis beschränken; Standardfall = automatische Aktenbildung | B01 §5.2; B00 §C2; U04, U21 |
| S14 | Dokumente in Akten ablegen | Drei Dropzones: **Automatisch speichern** (Standardkategorie der Akte) · **Manuell speichern** (Kategorie und Eigenschaften je Element, Weiter/Zurück, „Nicht speichern", „Anwenden") · **Mit Vorlage speichern**; nachträglich **Verknüpfen** / **Lösen** | Optionen „vom d.3-Administrator eingerichtet und … abhängig von Ihren Berechtigungen" | C+O | Beleg erbt „Gesellschaft" aus der Akte (siehe S15) | B01 §5.3, §5.4; B00 §C3, §C4 |
| S15 | **Automatische Ablage** (Admin) | Regel: Dokument auf eine Akte der Aktenart X ziehen → Import mit den Akteneigenschaften in die Zieldokumentart. Füllen die Akteneigenschaften nicht alle Pflichtfelder, öffnet sich d.3 import | Menü: Dokumente und Akten → Automatische Ablage → Neu → Aktenart / Zieldokumentart | O (Admin), C (Dropzone „Automatisch speichern") | Vererbung „Gesellschaft/Objekt/Kreditor" beim Einlegen | B03 §7f; B00 §K13; U47, U06 |
| S16 | **Automatische Aktenbildung** | Modul **Aktenbildung** (d.3 admin folder scheme). Verknüpfungstypen: Akte–Dokument, Akte–Akte, Dokument–Akte, Dokument–Dokument. **Erkennung:** „Kombination der Werte der Erkennungseigenschaften muss übereinstimmen". **Vererbung** weiterer Eigenschaften, Überschreiben möglich; Regel **Kopieren** | „Sind die Erkennungseigenschaften leer, wird **keine** Akte erzeugt bzw. verknüpft." Voraussetzung: Eigenschaften und Arten sind angelegt. Weitere Kapitel: asynchrone Verarbeitung, HOSTIMP | **O** (Cloud **Offen**) | „Gesellschaft" gehört in jede Erkennungskombination (z. B. Objekt X/NORD ≠ Objekt X/SÜD). Mehrere Regeln je Dokumentart für Gesellschafts-, Kreditoren- und Objektakte = **Abl., zu testen** | B03 §7a–§7e; B00 §K12; B01 §5.6; U46 |
| S17 | **Aktenplan (vorgefertigt)** | Der smart-invoice-Onboarding-Assistent legt an: `Eingangsrechnung/-gutschrift`, `Kreditorenvorgangsakte`, `Rechnungsanlage`, `Workflowprotokoll ERV` sowie Eigenschaften (Mandant, Mandantenname, Kreditor, …), Gruppen und Importprofile | Handbücher „Standardaktenpläne" und „Lieferantenakte" nur nach **Login**; das Doku-Fallbeispiel (Lieferanten-/Bestellakte) gilt für **ein** Unternehmen | C (Onboarding) | Den ER-Aktenplan aus dem Onboarding übernehmen und um Gesellschaft/Objekt erweitern | B00 §AH, §P; B03 OP10 |
| S18 | **Versionierung / Status** | Status **Bearbeitung, Prüfung, Freigabe, Archiv**. Gleiche Dokument- und Variantennummer → Aktualisierungsmodus: bei Freigabe/Archiv **neue Version**, bei Bearbeitung/Prüfung **ersetzt**. **Perspektive Versionen**: Liste neu→alt, Status farblich, Name des Freigebenden/Archivierenden/Prüfenden, Erstellungsdatum. **Änderungstext** optional. Anzeige standardmäßig der freigegebenen Version | Änderungstext „muss von einem d.3-Administrator eingerichtet werden"; das Freigeben-Recht vergibt nur der d.3-Administrator | C+O | Vertragsversionen über Bearbeitung → Freigabe; Rechnungen nach Buchung in den Status Archiv (Abl.) | B01 §4.2, §7.1, §8.1–8.2; B00 §B, §C6; U11–U13, U16 |
| S19 | Aufbewahrung / Löschung | Lebensdauer je Dokumentart (Standard 50 Jahre; in Monaten oder ereignisorientiert); dynamische Lebensdauerberechnung; storage manager (Retention) → Details in **§6** | Löschlisten sind **nicht** belegt | O | siehe §6 | B03 §2, §3d; B00 §T |
| S20 | **Volltext** | Durchsucht [B]: Volltexte **und** Systemeigenschaften, Kommentare/Notizen und alle erweiterten Eigenschaften, gleichberechtigt. Syntax: Elasticsearch Simple Query String (`+`, Leerzeichen, `\|`, ` -`, `"…"`, `*` am Wortende, `( )`, `\`); Standard-Operator UND; Groß-/Kleinschreibung egal | [A]: nur, „wenn die Volltextsuchfunktionalität für Ihre Organisation installiert wurde" · Sonderzeichen werden ignoriert (keine gezielte Suche danach) · `*` nur am Wortende | C (Umfang), O (Vorbehalt) | In der Cloud Verfügbarkeit bestätigen; Suche nach Rechnungsnummern mit Sonderzeichen testen | B01 §6.3, §6.5b; B00 §C11 |
| S21 | **Suche / Facetten** | Kategorie wählen → **Bouquet**; Facetten zeigen nur Kriterien, die „garantiert zu einem Ergebnis führen" („116 verfügbar", „25+"); bei mehreren Kategorien die **gemeinsamen** Eigenschaften. Platzhalter in Eigenschaftsfeldern: `$`, `!$`, `!wort`, `\|`, `*`, `?`, `datum1..datum2` | „Ihr Administrator kann … Platzhalterzeichen definieren, die vom Standard abweichen" | C+O | Facette „Gesellschaft" ersetzt einen fehlenden Mandanten-Umschalter (Abl.) | B01 §6.1–§6.5; B00 §C11 |
| S22 | Ergebnisliste | Listen- oder Tabellenansicht; Kategorie, Titel + 4 weitere Eigenschaften; Spaltenreihenfolge wird **je Kategoriekombination** gespeichert; Gruppieren in der Tabellenansicht (Beschreibung im Extrakt abgeschnitten); **Layouts** ([B] 1.4.10, nicht ausgewertet) | – | C+O | Standardspalten je Kategorie definieren | B01 §6.7, OP10, OP12 |
| S23 | **Gespeicherte Suchen** | **Suchvorlagen** (in Ordnern) + **Suchverläufe** = „gespeicherte Suchvorgänge"; im Team teilen über „Link in Zwischenablage kopieren"; Suchvorlagen beobachten (Ereignis „Ein neues Element wurde erstellt") | Teilen nur als Link. Eine zentrale Vorgabe von Suchvorlagen für Rollen ist **nicht** beschrieben | C+O | Standardsuchen je Rolle als geteilte Links + Verknüpfungswidget (Abl.) | B01 §6.6, §7.4; B00 §C12; U10 |
| S24 | **Favoriten / Persönlicher Bereich** | **Persönlicher Bereich** mit Suchvorgängen, Ablagevorlagen, Beobachteten Elementen, **Favoritenlisten** (thematisch); Kontextaktion „Zur Liste hinzufügen" (Sternchen); Widgets „Favorisiert" und „Beobachtet" | – | C+O | – | B01 §1.5, §2, §8.4 |
| S25 | Mehrsprachigkeit | Übersetzung von Wertemengen und Eigenschaftsnamen | – | O (Wertemenge), C (Eigenschaft in inbound scan) | Gering | B03 §3b, §8b |

### 2.2 Namensregeln und Kennungen (belegt)

| Objekt | Regel (F) | Livos-Hinweis (Abl.) | Quelle |
|---|---|---|---|
| Dokument-/Aktenart – Name | Pflicht, max. 50 Zeichen, eindeutig, wird in allen Anwendungen angezeigt | Fachlich sprechende Namen („Eingangsrechnung", „Mietvertrag") | B03 §2 |
| Dokument-/Aktenart – Kürzel | Pflicht, max. 5 Zeichen, `a-zA-Z0-9-`, Groß-/Kleinschreibung zählt, **nicht änderbar** | Kürzel-Konvention vorab festlegen | B03 §2; B00 §K1 |
| Erweiterte Eigenschaft – Titel | max. 50 Zeichen, Sonderzeichen nur `+ - _`, kein `:` | – | B03 §3c |
| Wertemenge – Bezeichnung / Wert | Bezeichnung max. 255 (Sonderzeichen nur `+ - _`); Wert max. 250 Zeichen | – | B03 §3b |
| Dokumentklasse | Bezeichnung max. 255; technisches Kürzel max. 10, Groß-/Kleinschreibung zählt; Präfix `CLAS_` reserviert | – | B03 §5b |
| Benutzer | Benutzername max. 30 (`a-zA-Z0-9_`), **nicht änderbar**; vollständiger Name max. 50; Benutzer und Gruppe dürfen nicht gleich heißen | Namensschema für externe Benutzer festlegen | B03 §6a |
| Gruppe | max. 100 Zeichen; **muss sich in den ersten 8 Zeichen von allen anderen Benutzer- und Gruppennamen unterscheiden** | Bei >100 Gesellschaften × mehreren Funktionen müssen die ersten 8 Zeichen **Gesellschaft und Funktion** kodieren. `LIVOS_NORD_BUCH` und `LIVOS_NORD_FREI` würden kollidieren (beide `LIVOS_NO`) | B03 §6b; B00 §K9 |
| Dokumenttitel | „Titelfelder" als Feld-Detail je Dokumentart | Eine Regel zur **automatischen Titelbildung** aus Eigenschaften ist **nicht belegt** → Offen | B03 §3d |
| Stapelnamen (E-Mail-Import) | Platzhalter `%Sender%`, `%Subject%`, `%Timestamp%`, `%Date%` | – | B00 §AN, §AS |
| Prozessvariablen | Präfix `dv_` reserviert; max. 200 je Prozess | – | B00 §V3 |

### 2.3 Konsequenzen für das Livos-Strukturmodell (Abl. aus den belegten Grenzen)
1. **„Gesellschaft"** wird eine erweiterte Eigenschaft mit Wertemenge (numerischer Schlüssel + Übersetzung). Sie ist in **jeder** Kategorie Pflicht, liegt in allen Kategorien auf **derselben DB-Position** und ist nach der Freigabe nicht modifizierbar [B03 §3b, §3d, §5c].
2. **DB-Positionsplan** und **Kürzel** vor der ersten Ablage verbindlich festlegen, weil beides nachträglich nicht oder kaum änderbar ist [B03 §2, §3c].
3. **Aktenhierarchie** Gesellschaft → Kreditor/Objekt → Vorgang über automatische Aktenbildung mit „Gesellschaft" in jeder Erkennungskombination; Belege über Mehrfachzuordnung in mehreren Akten [B03 §7d; B01 §5.1].
4. **Ja/Nein** über Wertemenge, **Kostenstellen-Splitting** in smart invoice, **Dubletten** nicht über documents [B03 §3a, §3e, OP6].
5. **Vorhandenen Aktenplan** aus dem smart-invoice-Onboarding übernehmen statt neu zu bauen [B00 §AH].

---

## 3. Mandantenfähigkeit (>100 Gesellschaften)

### 3.1 „Mandant" ist bei d.velop dreifach belegt (F)

| Bedeutung | Definition (F) | Livos | Quelle |
|---|---|---|---|
| **Cloud-Tenant** | „Innerhalb der d.velop cloud erhält jeder Tenant eine eigene Subdomain unterhalb d-velop.cloud"; die tenant-id ist „eindeutig, lebenslang gültig" und trennt die Daten eines Tenants von anderen; typischerweise „ein Unternehmen … deren Daten unter allen Umständen von den Daten anderer Tenants getrennt werden müssen" | **Livos = 1 Tenant** (Trennung Kunde↔Kunde, nicht Gesellschaft↔Gesellschaft) | B03 §4 (Abgrenzung 1), §8a; B00 §I; U48 |
| **Mandant in smart invoice** | „entspricht typischerweise einem Mandanten oder Buchungskreis im ERP-System. **Jede Rechnung benötigt einen Mandanten.**" Stammdaten `id`, `name`, `parent_id` (Hierarchie), `address`, `city`, `zip_code`, `local_currency`, `country`; Übertragung per Stammdaten-API | **1 Gesellschaft = 1 Mandant** (Abl.); Konzernhierarchie über `parent_id` | B00 §I; B03 §4 (Abgrenzung 2); U49 |
| **Mandant als Eigenschaftswert** in documents | Eigenschaft (z. B. „Gesellschaft"/„Mandant") + Dokumentklassen | Träger der Zugriffstrennung im DMS | B03 §4 (Mech. 3); B00 §J |

### 3.2 Gestaltungsoptionen im Vergleich

| Kriterium | **A: 1 Repository + Eigenschaft + Dokumentklassen/Makros** | **B: Mehrere Repositories** | **C: Mehrere Tenants** | *(D: Repository-ID)* |
|---|---|---|---|---|
| Belegte Grundlage | Doku-Beispiele für Dokumentklassen: „Dokumente eines Mandanten", „Dokumente eines bestimmten Firmenstandorts", Standort-Beispiel („nur relevante Dokumente") [B03 §4 Mech. 3; U36] · Makros [B03 §4; U37] | „Sie [können] mehrere Repositorys einrichten"; separate Datenbank, physische Trennung; Zweck: „unterschiedliche Sicherheits- und Datensicherungskonzepte" [B03 §4 Mech. 1; U35] | Tenant-Definition [B03 §4, §8a; U48] | „Logische Archive (Pools) auf dem Sekundärspeicher", max. 5 IDs [B03 §4 Mech. 2] |
| Trennungsgrad | Logisch (Berechtigung); „ein explizites Verweigerungsrecht kann durch andere Zuordnungen NICHT aufgehoben werden" [B03 §5a] | Physisch (eigene DB) | Vollständig (eigene Subdomain/Daten) | **Keine** Mandantentrennung |
| Aufwand bei >100 Gesellschaften | Neue Gesellschaft = **Gruppe + Wertemengeneintrag**, keine neue Klasse (Abl. [B00 §J; B03 §4]) | Jede Konfigurationsänderung 100-fach; es gibt eine eigene FAQ „Konfiguration … auf ein anderes Repository übertragen" (Indiz für Sonderfall) – Bewertung = Abl. [B03 §4 Mech. 1] | Benutzer, Konfiguration, Lizenzen und Workflows je Tenant (Abl.) | – |
| Konzernweite Rollen (Konzern-FiBu, GF) | Über Mitgliedschaft in mehreren Gruppen oder Profil ohne einschränkende Klasse (Abl.) | Übergreifende Suche/Akten **nicht belegt**; nur FAQ „Wie gelange ich zu einem anderen d.3-Repository?" ([A] 1.5.28, Inhalt nicht ausgelesen) [B01 §1.7, OP9] | Nicht vorgesehen (Abl.) | – |
| Cloud-Beleg | Mechanik **nur On-Prem (d.3 admin) belegt**, Cloud **Offen** [B00 §L; B03 §8c] | Repository-Anlage in der Cloud **nicht dokumentiert** [B03 §8c] | Tenant ist Cloud-Grundprinzip | – |
| Fazit | **Empfohlen (Abl.)** | Nur als Ausnahme (z. B. Gesellschaft mit Sonder-Sicherheitskonzept) – Abl. | Nicht empfohlen – Abl. | Irrelevant [B03 §4] |

### 3.3 Bausteine der Option A (belegt, On-Prem)

| Baustein | Funktion (F) | Livos-Einsatz (Abl.) | Quelle |
|---|---|---|---|
| **Dokumentklasse** | „dynamische Menge von d.3-Dokumenten" über Restriktionen auf Eigenschaften; optional „Aufnahme der Filter als Suchbedingung"; jede Dokumentart erhält automatisch eine Standardklasse `CLAS_…` | Klasse „Belege Gesellschaft X" oder generisch mit Makro | B03 §5a, §5b; U38 |
| **Dokumentartunabhängige Klasse** | „Schablone mit schwarzen Bereichen, die über andere Klassen gelegt wird"; wirkt über alle Dokumentarten; Restriktion auf **Datenbankpositionen** (DOK_DAT_FELDER 1–89), nicht auf Feldnamen; „kann … nicht als einzige Dokumentklasse zugeordnet werden". Doku-Muster: Profil mit allen Standardklassen + unabhängige Klasse „Status = Freigabe" | **Eine** Klasse für die Gesellschaftstrennung über alle Kategorien → „Gesellschaft" muss überall auf derselben DB-Position liegen | B03 §5c; B00 §J; U40 |
| **@D3GROUP** | „prüft zur Laufzeit, ob eine Eigenschaft einen d.3-Gruppennamen enthält, dem der aktive Benutzer angehört" | Gruppe je Gesellschaft; der gespeicherte Eigenschaftswert muss dem Gruppennamen entsprechen → Schlüssel = Gruppenname (**zu testen**) | B03 §4; B00 §J; U37 |
| **@D3USER_OPTFIELD_XX** | Prüfung gegen ein benutzerspezifisches optionales Feld (1–10, je 50 Zeichen); Beispiel „Benutzer mit ‚23' in Feld 5 … nur Dokumente mit passender Abteilungsnummer" | Geeignet bei **1 Gesellschaft je Benutzer**. Für Benutzer mit vielen Gesellschaften (50 Zeichen) ungeeignet bzw. **Offen** | B03 §4, §6a |
| **@D3SET** + d.3 restriction set manager | Berechtigungsmengen mit globalen, benutzer-/gruppenbezogenen und OE-bezogenen Werten; **Fachverantwortliche** dürfen einzelne Mengen pflegen (Beispiel „Standorte") | Pflege der Zuordnung Benutzer↔Gesellschaft an Fachverantwortliche delegieren, ohne Adminrechte | B03 §5d; U42 |
| Weitere Makros | `@D3USER`, `@D3HOOK` (nur On-Prem, JPL), `@D3REGEXPR`, `@D3USER_LDAPDN`, `@D3USER_REALNAME`, `@D3USER_LONG`, `@D3SUP`, `@D3USER_EMAIL`, **`@D3IDPUSER`, `@D3IDPGROUP`** | `@D3IDPGROUP` könnte IdP-Gruppen (z. B. aus Entra/AD) direkt nutzen → **Offen** | B03 §4, §8c |
| Sub-Administration | Admin-Rechte je Menüpunkt (Lesen/Schreiben/Ignorieren); Sub-Admin kann keine Sub-Admins anlegen | Lokale Key-User je Gesellschaftsgruppe (Abl.) | B03 §6d; B00 §K11 |

### 3.4 Mandantenebene in smart invoice (belegt, Cloud)
- Jede Rechnung benötigt einen Mandanten. Für das Repository-Mapping sind mindestens **Mandant Nummer, Mandant Name, Workflowbeteiligte** nötig [B00 §I; B03 §4; U49].
- Das Onboarding legt die documents-Eigenschaften `Mandant` und `Mandantenname` an [B00 §AH] → **Abl.:** Diese Eigenschaft kann zugleich Träger der documents-Rechte (Option A) sein. Beide Ebenen dürfen **nicht** unterschiedliche Schlüssel verwenden.
- Mandantenerkennung per OCR über **Name + Anschrift, nicht Steuernummer**. Fallback ist der **Standardmandant**. d.velop empfiehlt **einen** Stammdatenbucket [B00 §AI].
- Die Freigabematrix kann die Spalte „Mandant" nutzen (bis 20 Zusatzspalten). Kostenstellen/Sachkonten gelten je `company_id` oder, ohne Mandant, für **alle** Mandanten [B00 §AK, §AM].
- **Belastbare Gesellschaftszuordnung beim Eingang:** ein physisches Postfach mit **Alias je Gesellschaft** (`rechnungen+nord@…`), eigenem Importprofil und Schlüssel-Wert-Paar `Gesellschaft=…` [B00 §AS]. Dieses Konstrukt ist belegt; die Anwendung auf Livos ist Abl.

### 3.5 Empfehlung (Abl.) und Prüfpunkte
**Empfehlung:** Option A. Ein Repository, Pflicht-Eigenschaft „Gesellschaft" (= smart-invoice-Mandant-ID), **eine** dokumentartunabhängige Klasse mit `@D3GROUP` (oder `@D3SET` für delegierte Pflege), eine Gruppe je Gesellschaft, explizites Verweigern für Sonderfälle [B00 §J; B03 §4, §5c, Schluss „Drei Punkte"].

**Prüfpunkte vor Zusage (alle Offen):**
1. Gibt es Dokumentklassen, Makros, dokumentartunabhängige Klassen und `@D3SET` in der **Cloud**, und wo werden sie konfiguriert? [B00 §L; B03 §8c]
2. Bedeutet „enthält" bei `@D3GROUP` Gleichheit oder Teilstring? Bei Teilstring-Logik droht Überschneidung (`G101` ⊂ `G1010`) → Schlüssel mit fester Länge verwenden (Abl.).
3. Wirkt `@D3GROUP` auch über **verschachtelte Gruppen** (Gruppen in Gruppen sind erlaubt [B03 §6b])?
4. Was sieht ein Benutzer bei Dokumenten mit **leerer** Gesellschaft? Nicht dokumentiert.
5. Obergrenzen und Performance für Klassen, Profile, Gruppen und Wertemengen-Einträge bei >100 Gesellschaften: **nicht dokumentiert** [B03 OP2; B00 §M].
6. **Vertretung:** „Als Vertretung eingetragene Benutzer übernehmen die Berechtigungen" [B00 §V6] → der Vertreter erhält fremde Gesellschaften. Governance-Regel nötig (Abl.).
7. Rechteänderungen wirken erst nach **Neuanmeldung**; der IdP synchronisiert Gruppen **stündlich** [B03 §5b, §6e] → Latenz beim On-/Offboarding.
8. Die Oberfläche hat **keinen Mandanten-/Gesellschaftsumschalter** (nicht beschrieben) → Facette/Suchvorlage je Gesellschaft (Abl.) [B01 §1.7, OP9].

---

## 4. Berechtigungskonzept

### 4.1 Architektur (F)
Zugriff wird über **Dokumentklassen** (das „Was") und **Berechtigungsprofile** (das „Wie") geregelt. Profile werden Benutzern, Gruppen oder Tätigkeitsprofilen zugeordnet. Die Rechte eines Benutzers ergeben sich aus den Profilen plus direkten Klassenzuordnungen; direkt vergebene Rechte übersteuern die Profile. **Ein explizites Verweigern ist durch keine andere Zuordnung aufhebbar** [B03 §5a; B00 §K6, §K7; U36, U39]. Belegt nur über d.3 admin (**O**); für die Cloud **Offen** [B00 §L].

### 4.2 Rechtearten im Berechtigungsprofil (F)

| Rechtegruppe | Umfang laut Doku | Zustände | Quelle |
|---|---|---|---|
| **Lesen** | Leseerlaubnis, **Export**, Ansicht von Aktivitäten und Attributen | erteilen / verweigern / ignorieren | B03 §5b |
| **Schreiben** | Änderungen an Eigenschaften, Dokumentaktualisierung, Import, Notizen und Redlining; laut Konzeptseite auch Anlage und **Löschung** | dto. | B03 §5a, §5b |
| **Statustransfer** | Statuswechsel zwischen Bearbeitung, Prüfung, Freigabe und Archiv | dto. | B03 §5b |
| **Verknüpfungen** | Dokumentverknüpfungen erstellen und auflösen | dto. | B03 §5b |
| **Aktivitäten** | Lesezugriff auf den Aktivitätsverlauf | dto. | B03 §5a, §5b |

### 4.3 Fähigkeitsmatrix Berechtigungen

| # | Fähigkeit | Belegt (F) | Grenzen / Vorbehalte (F) | Plattf. | Livos-Bedeutung (Abl.) | Quelle |
|---|---|---|---|---|---|---|
| R01 | **Benutzer** | Pflicht: vollständiger Name, Benutzername, Kennwort. Optional: Abteilung, Organisation, Telefon, E-Mail. Registerkarten: Erweiterte Eigenschaften, Gruppenzugehörigkeit, Berechtigungsprofile, Dokumentklassen direkt zuweisen, **10 optionale Felder** (je 50). Status gesperrt/deaktiviert; Registerkarte **„Lizenzierung"** | Benutzername nicht änderbar; nicht gleichnamig mit einer Gruppe | O | Die optionalen Felder tragen `@D3USER_OPTFIELD_XX` | B03 §6a; B00 §K8; U43 |
| R02 | **Gruppen** | Name, **Art der Dokumentenverteilung** (an alle Mitglieder / an **ein** Mitglied = „Tätigkeitsprofil" (Lastverteilung) / keine), Mitglieder (auch Gruppen), Profile an Gruppe | 8-Zeichen-Regel (siehe §2.2) | O | Eine Gruppe je Gesellschaft × Funktion; Klärungskorb als Gruppe | B03 §6b; B00 §K9 |
| R03 | **Tätigkeitsprofile** | Gruppe mit Verteilung „an ein Mitglied"; Profilzuordnung an Tätigkeitsprofile möglich | – | O | Lastverteilung in der Buchhaltung | B03 §5b (Schritt 4), §6b |
| R04 | **Rollen** | In d.3 admin gibt es **keine** Rollen (dort: Berechtigungsprofil). **„Benutzerrollen"** gibt es in d.ecs task und d.velop process (Feature Konfiguration → Benutzerrollen). process studio setzt „eingerichtete Benutzerrollen" voraus; nur die Rolle **Administration** darf Automatisierungen importieren | Im Prozessmodell ist „Rolle" **kein** Zuweisungsobjekt (nur Person/Gruppe); die Doku empfiehlt Zuweisung an **Gruppen** | C+O | Fachrollen (Sachbearbeitung, Prüfer, Freigeber, Buchhaltung, Management) als **Gruppen** abbilden | B03 §6c; B00 §K10, §V1, §V4, §V9, §AU; U45 |
| R05 | Rollen/Gruppen aus smart invoice | Onboarding legt an: `dv_Buchhaltung`, `dv_Freigeber`, `dv_Sachliche_Prüfer`, `dv_inbound`, `dv_inbound_Administratoren`, `dv_Service_Accounts`, `dv_Workflowteilnehmer`; Rechnungseingangsbuch „Rolle Buchhaltung" | – | C | Namensschema an die `dv_`-Gruppen anlehnen oder mappen | B00 §AH, §AA |
| R06 | **Berechtigungsprofile** | Bezeichnung + Dokumentklassen + Rechte (4.2); Zuordnung an Benutzer, Gruppen, Tätigkeitsprofile; neue Profile werden **hinzugefügt, nicht ersetzt** | Nach Änderungen **neu anmelden** | O | Profil je Fachrolle, kombiniert mit der Gesellschaftsklasse | B03 §5b; B00 §K6, §K7 |
| R07 | **Dokumentklassen** (Rechte auf Kategorien) | Standardklasse `CLAS_…` je Dokumentart; eigene Klassen mit Restriktionen (alphanumerisch `% _ * ?`; Datum mit Bereichen und relativ `{-28}-{+28}`; numerisch `-10000`, `10000-`, `10-100`); technische Felder (Dokumentnummer, Dokument-ID, Erstellt am, Frei/Gesperrt, **Status**, **Bearbeiter**, Dateierweiterung) | Damit eine Dokumentart in d.3 import zur Ablage angeboten wird, braucht der Benutzer **Schreibzugriff** auf deren Klasse | O | Kategorien je Fachrolle freischalten; Klasse „Rechnungen > 10.000 €" für die Management-Sicht möglich | B03 §5a, §5b; B00 §K5 |
| R08 | **Eigenschaftsbasierte Rechte** | Über Restriktionen und Makros (§3.3); **geschützte Eigenschaft** (Modifizierbar); **Ausblendbar** + Recht „Lesen versteckter Eigenschaften" | Restriktionen der unabhängigen Klasse wirken auf DB-Positionen | O | Gesellschaftstrennung; sensible Felder (z. B. Bankdaten) ausblenden | B03 §3d, §4, §5c |
| R09 | Rechte an Funktionen | Aktenerstellung nur für die „Gruppe zum Erstellen von Akten"; **Freigeben-Recht vergibt nur der d.3-Administrator**; Bearbeitung übernehmen nur mit Berechtigung; Workflow starten nur, wenn aktiviert und berechtigt; Office-Bearbeitung vom Admin bereitgestellt; Prozess-Start einschränkbar (Editor → Berechtigungen → Nutzung) | – | C+O | Funktionsrechte im Rollenkonzept explizit aufführen | B01 §5.2, §8.1, §8.2, §8.4, EV; B00 §V10 |
| R10 | **Rechtevererbung** | d.3 inherit rights manager: temporäre, vom d.3 server vergebene Klassen, vom Admin „NICHT manipulierbar" | Der Empfänger braucht die Dokumentart bereits im Profil | O | Nur Sonderfälle (z. B. Einsicht für externe Prüfer) | B03 §5e; U41 |
| R11 | **Admin-Rollen** | **d.3-Administrator** (Freigeben-Recht, Änderungstext, Schwärzen aktivieren, Prozessportal umbenennen) · **Sub-Administration** (je Menüpunkt Lesen/Schreiben/Ignorieren; kann keine Sub-Admins anlegen, keine Projekte/Meilensteine im-/exportieren) · **Mandanten-Administratoren** (allein berechtigt zur Repository-Konfiguration per DMS-Config-API) · process-Rolle **Administration** · **Fachverantwortliche** für Restriktionsmengen · Gruppe `dv_inbound_Administratoren` · Vorgesetzte „mit administrativen Rechten" setzen Abwesenheit für andere | Sub-Administration ist für die Cloud **nicht belegt** | O / C (je Baustein) | Dreistufig: Plattform-Admin (MDIS/IT), Fach-Admin (FiBu), Key-User je Gesellschaftsgruppe | B03 §6d, §8c, §8d; B00 §K11, §V6, §V9, §AH; B01 §1.4, §8.4; U43, U51 |
| R12 | **Externe Benutzer / Gäste** | **Extern Teilen**: externe Person darf „nur lesen oder auch bearbeiten", **Zeitraum** wählbar, Link kopierbar; Verwaltung unter „Geteilte Dokumente"; Ende automatisch nach Ablauf oder manuell. Externe Änderungen werden **nicht automatisch** übernommen (Änderungen anzeigen → Dokument aktualisieren → Speichern). Widgets kennen „externe Anwendende" (Sichtbarkeit / „Freigeben für externe Anwendende"). process studio kennt den Aktivitätstyp **„Externe Benutzeraufgabe"** | Teilen **nur Cloud**; außerhalb der Organisation **nur mit d.velop documents business**; kein „Freigeben im Workflow-Sinn". In [A] gibt es kein Teilen von Dokumenten | C | Externe Planer/Hausverwaltungen: Einsicht per Link; Mitwirkung im Workflow über „Externe Benutzeraufgabe" (Umfang **Offen**); Katalog 4.2 „Ad-hoc-Freigabe ohne Lizenz" bleibt **Offen** | B01 §8.3, EV; B00 §E, §Z, §V2; U17 |
| R13 | **Freigabelinks** | Teilen: **Kopie senden** (E-Mail mit Anhang in den Download-Ordner), **Link senden** (interner Link), **Extern Teilen** (externer Link); Suchvorlagen und Ablagevorlagen per „Link in Zwischenablage kopieren" | Ein Passwortschutz für Links ist **nicht beschrieben** | C (Dokumente), C+O (Vorlagen) | – | B01 §6.6, §8.3 |
| R14 | **Vertretung / Abwesenheit** | [B]: Konfiguration → Aufgabeneinstellungen → **Vertreter verwalten**. Abwesenheit: Profilbild → **Abwesenheitsstatus** → Start (oder Uhr = jetzt), optional Ende, Vertretung, Nachricht (geplant/ungeplant). Vorgesetzte können dies für Erkrankte tun. Vertreter „**übernehmen die Berechtigungen**". Regeln je Aufgabentyp (Konfiguration → Aufgaben und Prozesse → Vertretungsregeln); **Vertretungsausschluss** („Vertretung möglich" deaktivieren). Rechnungseingangsbuch: Schnellzugriff „Rechnungen in Vertretung" | Aufgaben laufen **nicht automatisch** zum Vertreter über; er sieht die Liste des Abwesenden unter „Vertretung" | C (+O über d.ecs task/userprofile) | Vertretungsregel gesellschaftsintern halten (Rechteübernahme!); Kommunikation „Vertreter sieht, nicht erhält" | B00 §C8, §V6, §AA, §AO; B01 §3.2 |
| R15 | **Lizenztypen** | Belegt nur: Edition **d.velop documents business** (für Extern Teilen); Registerkarte **„Lizenzierung"** am Benutzer (Inhalt nicht beschrieben); alphaflow App Studio „eigene Lizenz"; das Vier-Augen-Prinzip in smart invoice ist ein **Vorschau-Feature** (über den Support) | Named/Concurrent, Gast-, Leser- oder Externen-Lizenzen und Volumenlizenzen sind **nicht belegt** | – | → Rechercheauftrag R-06 | B01 §8.3; B03 §6a; B00 §E, §AE, §AL |
| R16 | **SSO / Verzeichnisdienst** | d.ecs identity provider: **Active Directory**, **Kerberos**, **OpenID Connect**, Benutzeranmeldedaten; Anmeldung auf bestimmte Gruppen beschränkbar („nur Gruppen mit entsprechenden Rollen können verknüpft werden; eine Auswahl einzelner Benutzer ist nicht möglich"); **Gruppen-Sync stündlich**; d.ecs open id provider app stellt Konten/Gruppen für Drittsysteme bereit; Makros `@D3IDPUSER`, `@D3IDPGROUP`, `@D3USER_LDAPDN`. [B]: **FIDO2** und **2-Schritt-Anmeldung** | **Microsoft Entra ID** ist nur als App-Registrierung für d.velop email import belegt (Mail.ReadWrite, User.ReadBasic.All), **nicht** als SSO für d.velop cloud. „Azure AD", „SAML", „SCIM" kommen **nicht vor** | O (IdP-Konfig.), C (FIDO2/2FA) | Entra-SSO für die Cloud ist **Offen** → R-07 | B03 §6e; B01 EV; B00 §AS; U44 |
| R17 | Sichtbarkeit ≠ Sicherheit | Widget-Sichtbarkeit je Benutzer/Gruppe „stellt **keine Sicherheits- oder Zugriffsbeschränkung** dar" | – | C+O | Rollen-Startseiten nie als Rechteersatz verkaufen | B00 §Y |

---

## 5. Anwenderfunktionen

| # | Funktion | Belegt (F) | Vorbehalt / Grenze (F) | Plattf. | Quelle |
|---|---|---|---|---|---|
| A01 | **Ablage** (Feature „Ablage") | Startseite → Ablage → Datei (Durchsuchen) + Kategorie → Perspektiven **Erweitert**, **Mehrfachwerte**, **Allgemein** → Speichern; danach „Neues Dokument speichern" / „Dokument anzeigen" | Gleiche Dokument-/Variantennummer → Aktualisierungsmodus (siehe S18) | C+O | B01 §4.1, §4.2; B00 §C1; U03 |
| A02 | **Drag & Drop** | Dropzones an Akten (Automatisch / Manuell / Mit Vorlage speichern); neue Version durch Ziehen auf ein Dokument; **Import-Widget** (inbound scan) mit max. 4 Dropzones, je Dropzone ein Importprofil, wahlweise Bearbeitungsmodus oder direkt Indexierung | – | C+O (Dropzones), C (Import-Widget) | B01 §5.3, §7.1; B00 §C3, §AC |
| A03 | **E-Mail-Ablage** | Dropzone nimmt „Element (Datei, E-Mail)" an; d.3one läuft **in der E-Mail-Anwendung** mit derselben UI; manche Kontextaktionen gibt es nur in der Integration (z. B. Outlook). Serverseitig: inbound e-mail (Push, **Outlook-Add-In**), email import (Postfachüberwachung). „Mailanhang als Dokument + Mail als Korrespondenz" im Importprofil (Registerkarte „E-Mails") konfigurierbar | Ob es für d.velop documents Cloud eine Outlook-Ablage gibt (außer dem inbound-Add-In), ist **Offen** | O (d.3one-Outlook), C (inbound) | B01 §1.1, §1.3, §5.3; B00 §AS, §AT, §AU |
| A04 | **Scannen / Stapel** | Feature „Scannen" ([B]); Barcode-/Trennblatterkennung | [B] Kap. 1.7 nicht im Detail ausgewertet | C | B01 §1.1, OP12; B00 §AU |
| A05 | **Dokumentvorschau** | Perspektive **Anzeige**: PDF, Bilder, Videos sowie DOC/DOCX/DOCM, XLS/XLSX/XLSM, PPT/PPTX/PPTM; standardmäßig die freigegebene Version; in Widgets per Klick | – | C+O | B01 §1.2, §2 |
| A06 | Perspektiven | **Anzeige, Eigenschaften, Notizen, Versionen**; kontextabhängig Erweitert, Allgemein, Mehrfachwerte, Suchvorgänge, Ablagevorlagen, Übersicht/Workflow ([A]), Prozess ([B]) | – | C+O | B01 §1.2 |
| A07 | **Bearbeitung / Check-in-out** | „Check-in/out" heißt **Bearbeitung beginnen** (Dokument „reservieren", Benutzer als Bearbeiter, Status Bearbeitung; andere sehen einen Hinweis mit Namen; Übernahme mit Berechtigung) und **Bearbeitung abschließen** (neue Version, Status Freigabe, optional Änderungstext). **Lokal in Microsoft Word/Excel/PowerPoint bearbeiten**. Außerdem „Bearbeitung mir zuweisen" | Office-Bearbeitung „wird Ihnen vom Administrator bereitgestellt", nicht bei geteiltem Windows-Benutzer; Status Freigabe nur mit Freigeben-Recht | C+O (Office: [A]) | B01 §8.1, §8.2, EV; B00 §C6; U16 |
| A08 | Eigenschaften / Kategorie ändern | Perspektive Eigenschaften → Eigenschaften bearbeiten → **Eigenschaften überprüfen** → Speichern; Kategoriewechsel analog, danach Zusatz „Geändert" | Fehlt die Funktion: erst „Bearbeitung beginnen" | C+O | B01 §8.1; B00 §C5 |
| A09 | **Notizen, Kommentare, Annotationen** | Perspektive Notizen (`1+`/`0`); **Kommentare und grafische Markierungen** in PDF; **Verschmelzen** von Kommentaren; Recht „Notizen und Redlining" (Schreiben) | Der Begriff „Annotation" wird nicht verwendet | C+O | B01 §1.2, §8.4; B03 §5b |
| A10 | **Stempel** | **Stempelvorlagen** (in PDF) | Details (z. B. „Eingangsstempel", Datumsfeld) **nicht ausgewertet** | C+O | B01 §8.4 |
| A11 | **Schwärzen** | PDF öffnen → Bereiche markieren → bestätigen → als **neues Dokument** oder **neue Version** ablegen; „Originaldokument bleibt unverändert … Revisionssicherheit" | **Standardmäßig deaktiviert**; Aktivierung unter Konfiguration → Anzeige > Kommentare | C+O | B01 §7.3, §8.4; U15 |
| A12 | **Aufgaben** | [A] „Aufgaben und Nachrichten" (Filter Alle/Aufgaben/Nachrichten; Sortierung; **Fälligkeits-Farbcode** grün/gelb/beige/rot; Perspektive Workflow). [B] **Aufgabenlisten**: Meine Aufgaben, An mich gesendet, An mich und andere gesendet, Meine geplanten Aufgaben, **eine Liste je Gruppe**, Meine erstellten/weitergeleiteten/erledigten Aufgaben, Meine Verantwortung; Suche und Sortierung (Erhalten, Betreff, Absender, Priorität, Fällig). **Aufgabe zum Dokument erstellen**, **Weiterleiten**, **Entziehen**; Gruppenaufgaben „Aufgabe übernehmen"; Perspektive **Prozess** | Erledigte Aufgaben nur „bis zum jeweiligen Aufbewahrungsende"; der Begriff „Postkorb" existiert nicht | C ([B]), O ([A]) | B01 §3.1, §3.2, OP11; B00 §C9, §V4 |
| A13 | Benachrichtigungen / Beobachten | **Beobachten** (Ereignisse: aktualisiert, Notiz, Eigenschaften geändert, Bearbeitung abgeschlossen, gelöscht, aktuelle Version gelöscht; bei Suchvorlagen: neues Element); Aufgaben-Benachrichtigungen global aktivierbar (Message-Center) | Keine Benachrichtigung über eigene Aktionen | C+O | B01 §7.4; B00 §V5 |
| A14 | **Workflow starten** | Kontextaktion „Workflow starten" / „Prozesse zum Dokument verwalten"; automatischer Start beim Import (process studio) | Nur wenn aktiviert und berechtigt | C+O | B01 §8.4; B00 §C7, §V7 |
| A15 | Weitere Kontextaktionen | Download · In Akte anzeigen · **In PDF-Datei zusammenfassen** (Container-PDF) · Eigenschaften exportieren · Verknüpfen/Lösen · Zur Liste hinzufügen · Beobachten | „**Akten können nicht exportiert werden**" (PDF-Zusammenfassung) | C+O | B01 §1.3, §8.4 |
| A16 | Dokument neu erstellen | **Word-Vorlage** (FAQ [A] 1.5.59); **d.velop pages** ([B]) | Ein generisches „Neues Dokument" im Browser ist nicht beschrieben | O / C | B01 §4.5, OP8 |
| A17 | **Outlook-/Office-Integration** | [A]: dieselbe UI „im Browser, in Ihrer E-Mail-Anwendung oder in Microsoft Office"; Integrationen Browser, Outlook, Office, HCL Notes; Kontextaktionen nur für die Integration; inbound-Outlook-Add-In (Cloud) | Für die Cloud ist eine documents-Integration in Outlook/Office jenseits des inbound-Add-Ins **nicht belegt** | O, C (Add-In) | B01 §1.1, §1.3, Quellenlage; B00 §AT |
| A18 | **Mobile App** | **Nicht belegt.** Die Klickwege sagen durchgängig „Tippen oder klicken Sie …" → Touch-Bedienung ist vorgesehen (Beobachtung 04a, keine Produktaussage) | – | – | B01 §5.4 (Wortlaut) |
| A19 | Startseite / Personalisierung | Kacheln bzw. **Widgets**, deren Reihenfolge änderbar ist; persönliches Dashboard; farbliches Design ([A] 1.3.19); **Layouts** ([B] 1.4.10); „eigene Bereiche" per URL für Anwender ([A] „Über d.3one") | Layouts und Design nicht ausgewertet | C+O | B01 §1.1, §2, §6.7, OP12; B00 §X |
| A20 | Anmeldung | FIDO2, 2-Schritt-Anmeldung ([B]) | – | C | B01 EV |

---

## 6. GoBD, Revisionssicherheit, Archivierung, Aufbewahrung, Löschung, DSGVO, Audit-Trail

| # | Thema | Belegt (F) | Nicht belegt / Offen | Plattf. | Livos-Konsequenz (Abl.) | Quelle |
|---|---|---|---|---|---|---|
| C01 | **GoBD** | Nur als Schlagwort am gesperrten Handbuch **document reader invoice** („ZUGFeRD, Factur-X, XRechnung, GoBD") | Es gibt **keine** GoBD-Aussage zu documents, keine Verfahrensdokumentation und kein Testat in den Quellen | – | Nachweis bei d.velop anfordern (R-08) | B00 §P |
| C02 | **Revisionssicherheit** | Anwenderdoku: 1× beim Schwärzen („Original bleibt unverändert"). **d.ecs storage manager** = „Revisionssicherheit, Retention", API `extendretention` (frei, **nicht ausgewertet**). Prozessprotokoll per „Export in Repository" = „revisionssichere Archivierung". In der Produktfamilie invoices ist documents als „revisionssichere Archivierung" benannt | Technik (WORM, Hash, Speicher), Cloud-Umsetzung und Zertifizierung **nicht belegt** | ? | storage-manager-Handbuch auswerten | B01 §7.3; B00 §T, §V8, §AG, §O |
| C03 | **Archiv-Status** | Status **Archiv** (Lebenszyklus Bearbeitung → Prüfung → Freigabe → Archiv); Recht **Statustransfer**; Klassen nach Status restriktierbar; Speichern auf ein Archiv-Dokument erzeugt eine **neue Version** statt zu überschreiben | Ob „Archiv" technisch unveränderbar ist, ist nicht belegt | C+O | Buchungsrelevante Belege nach Buchung in „Archiv" (Abl.) | B01 §4.2, §7.1; B03 §5b |
| C04 | **Aufbewahrungsfristen** | **Lebensdauer je Dokumentart** (Standard 50 Jahre; in Monaten oder **ereignisorientiert**); **dynamische Lebensdauerberechnung** als Feld-Detail; Auslagerung auf Sekundärspeicher; Repository-ID = Speicher-Pool; storage manager „Retention" | Wirkung bei Fristablauf (automatisch löschen? sperren? Liste?) **nicht beschrieben** | O | Fristenkatalog je Kategorie (z. B. Verträge ab Vertragsende) über ereignisorientierte Lebensdauer abbilden – **Umsetzbarkeit zu prüfen**; die gesetzlichen Fristen selbst sind **nicht** Gegenstand der Quellen | B03 §2, §3d, §4; B00 §K1, §T |
| C05 | **Löschung** | Recht **Schreiben** umfasst Löschung; Beobachten-Ereignisse „Element wurde gelöscht" / „aktuelle Version gelöscht"; Prozessversionen erst nach Ende aller Instanzen löschbar | **Löschlisten, Löschfreigabe, Löschprotokoll, Legal Hold: nicht belegt** | C+O | Löschen im Rollenkonzept restriktiv vergeben (nur Admin) | B03 §5a; B01 §7.4; B00 §V9 |
| C06 | **DSGVO** | Handbuch „DSGVO / Datenkommunikation" (`dsgvo` 1.0, frei, **nicht ausgewertet**); Schwärzen als Werkzeug; Tenant-Datentrennung | Auskunft, Löschkonzept, Rechenzentrumsstandort, AVV: **nicht belegt** | ? | R-09 | B00 §O; B01 §8.4; B03 §8a |
| C07 | **Audit-Trail „Aktivitäten"** | Nur [B]: „welche Änderungen … vorgenommen wurden und wer die Änderungen gemacht hat"; je Element „welcher Anwender welche Änderungen zu welchem Zeitpunkt"; neueste zuerst; Filter nach **Zeiträumen, Inhalten, Tätigkeitsbereichen**; Standard- und **erweiterte Ansicht**; persönliche Aktivitäten als Feature der Startseite; Recht „Aktivitäten" im Profil | In [A] **0 Treffer**; Vollständigkeit (auch Lesen/Download?), Aufbewahrungsdauer, Export und Manipulationsschutz **nicht belegt**; die Begriffe Historie/Änderungsprotokoll/Audit kommen **nicht vor** | **C** | Gegenüber Livos „Aktivitäten" + „Versionen" sagen, **nicht** „Audit-Trail" | B01 §7.2, §7.3, OP6; B00 §B, §C10; B03 §5b; U14 |
| C08 | Versionen / Änderungstext | Perspektive Versionen mit Status, Freigebendem/Archivierendem/Prüfendem und Datum; Änderungstext (Admin richtet ein) | Kein lückenloses Protokoll aller Änderungen | C+O | Ergänzt C07 | B01 §7.1; U11, U12 |
| C09 | Prozess-Nachweise | **Prozessprotokoll** (fachliche/technische Ansicht) je Prozess aktivierbar: Standard **30 Tage, bis 1 Jahr**, optional **Export ins Repository**; Perspektive **Prozess** an der Aufgabe; Rechnungseingangsbuch „**Historie anzeigen**"; smart-invoice-Aktenplan „Workflowprotokoll ERV" | Ohne Export ist die Protokolldauer auf ≤ 1 Jahr begrenzt | C+O | Freigabenachweise **immer** ins Repository exportieren (GoBD, Abl.) | B00 §V8, §AO, §AH; B01 §3.2 |
| C10 | 4-Augen-Prinzip | Option je Dokumentart („Prüfung durch andere Person als Bearbeiter"); in smart invoice ein **Vorschau-Feature** (> Minimalbetrag, je Kostenobjekt, Menüpfad nicht öffentlich) | – | O / C | Für ER über eine Schrittverbindung mit Bedingung statt Vorschau-Feature [B00 §AJ] | B03 §2; B00 §AL |
| C11 | Zugriffsschutz | Explizites Verweigern nicht aufhebbar; Tenant-Trennung; „Ungeschützter Webzugriff" als Option je Dokumentart | – | O / C | Option nicht aktivieren | B03 §2, §5a, §8a |

---

## 7. Reporting, Dashboards, Listen, Export

| # | Fähigkeit | Belegt (F) | Grenze (F) | Plattf. | Livos-Nutzung (Abl.) | Quelle |
|---|---|---|---|---|---|---|
| D01 | **Dashboard = Startseite** | Genau **4 Standard-Widgets**: Suche, Zuletzt bearbeitet, Beobachtet, Favorisiert; Admin-Pfad: Konfiguration > Erscheinungsbild > Startseite („Widgets erstellen", „Sichtbarkeit von Widgets"); Kacheln werden durch Widgets abgelöst; „Widget hinzufügen" ist über die Rechnungseingangsbuch-Doku belegt | „Zuletzt bearbeitet" zeigt **keine** Statuswechsel, Notizen oder Eigenschaftsänderungen; Klickweg zum Anordnen/Größenändern **nicht dokumentiert**; mehrere Dashboards je Benutzer nicht dokumentiert | C+O | Einstieg je Rolle | B00 §D1, §X, §AE, §AO; B01 §2 |
| D02 | **Rollen-Startseiten** | Sichtbarkeit je **Benutzer oder Gruppe** → „Zuordnungen anwenden"; Anwendungsfälle „abteilungsspezifische Ansichten", „vereinfachte Bedienoberflächen" | **Keine Sicherheitsfunktion**; ein vorgegebenes Layout ist nicht dokumentiert | C+O | Widget-Sets für Sachbearbeitung, Freigeber, Management | B00 §Y |
| D03 | **Eigene Widgets** | **Verknüpfungswidget** (Ziel-URL, Sichtbarkeit, Symbol, Farbe, Titel); **Listen-Widget** (URL liefert `ListContent`-JSON); **Erweitertes Widget** (iframe); „Freigeben für externe Anwendende"; API-Typen `shortcut`/`list`/`iframe`; **Badge** (Zähler, >99 → „99+") | **Kein Filterfeld**, kein Diagramm-/Chart-Typ; fachliche Filter nur **serverseitig hinter der URL** | C+O | Kennzahlen („offene ER NORD") nur über einen eigenen Listen-Dienst (Entwicklung) | B00 §Z, §AF |
| D04 | **Rechnungseingangsbuch** | Schnellzugriffe (eigene offene / in Vertretung / alle offenen / Archiv), **Filter mit Operatoren und logischen Verknüpfungen**, **Gruppierung** (z. B. je Gesellschaft), Clearing-Modus, Historie, Spalten hinzufügen/fixieren/sortieren, **eigene Schnellzugriffe** (Filter + Layout) | Eigene App (kein Widget); Archiv 6 Monate, mit „Erweiterte Liste" 12 Monate | C | **Management-Sicht ER** | B00 §AA, §AO |
| D05 | Prozessüberwachung | Betrieb → Überwachung: laufende/abgeschlossene/abgebrochene/**fehlerhafte** Instanzen, Filter nach Business Keys, Version, Status; Protokoll; Token-Erstellungszeit | **„Liegezeit" gibt es nirgends** (keine Spalte, kein Feld) | C+O | Liegezeit nur über eigene Auswertung (Katalog 3.2 → Vorbehalt) | B00 §V8, §AB |
| D06 | Ergebnislisten / Aufgabenlisten | Tabellenansicht, Gruppieren, Spaltenauswahl je Kategoriekombination; Aufgabenlisten mit Filtern/Sortierung (Priorität, Fällig) | – | C+O | Operative Listen je Rolle | B01 §3.2, §6.7 |
| D07 | **Prozessportal** | „Formulare als Übersichten und Auswertungen", ohne Dokumentbezug | Nur [A]; Formularintegration hinter Login | O | Option für Management-Übersichten | B01 §1.4; B00 §D1, §P |
| D08 | **Export** | **Eigenschaften exportieren** (Akteninhalte); **In PDF-Datei zusammenfassen**; Download; Recht „Export" in der Rechtegruppe Lesen; Automatisierungen herunterladen/hochladen (Transport); Prozessprotokoll ins Repository | Exportformat von „Eigenschaften exportieren" (CSV/Excel?) **nicht beschrieben**; Akten nicht als PDF exportierbar | C+O | Prüferexport (Belegliste je Gesellschaft) – Format klären | B01 §5.5, §8.4; B03 §5b; B00 §V9 |
| D09 | Reporting-Module | Handbuch „Reporting / Workflow-Auswertungen" (**Login**); alphaflow App Studio mit filterbaren Dashboards (Koordinaten, Entität, Filter; eigenes Produkt/Lizenz, Charts nicht dokumentiert) | – | ? | R-14 | B00 §P, §AE |
| D10 | Monitoring Eingang | email import **Jobübersicht** (Layouts „Standard"/„E-Mail"; Aktionen Aktualisieren, Löschen, **Neustarten**); Postfach-Ordner `dvelop_finished` / `dvelop_not_processed` | Abrufintervall **nicht dokumentiert** | C | Betriebsmonitoring | B00 §AS |

---

## 8. Integrationen, Schnittstellen, APIs

| # | Schnittstelle | Belegt (F) | Grenze / Vorbehalt (F) | Livos-Einsatz (Abl.) | Quelle |
|---|---|---|---|---|---|
| I01 | **REST-API-Verzeichnis** | 47 APIs, **alle frei**: `https://help.d-velop.de/dev/documentation` (developer.d-velop.de leitet dorthin weiter) | – | Grundlage für Bim4You/ERP-Kopplung | B00 §Q; U53 |
| I02 | **DMS-API** (dms-app) | Dokumente anlegen, Eigenschaften setzen; nötig sind **Dokumenttyp, Properties, Source-ID**; **Chunked Upload** (max. 100 MB Body, empfohlen 25 MB); Tutorial (DE) + C#-Beispiele (`PropertyDto`) | **multipart/form-data wird nicht unterstützt** | Datenübernahme/Migration, Ablage aus Fremdsystemen, Reset-Skripte | B00 §Q; U53, U54 |
| I03 | **DMS Config API** (dmsconfig) | Repository-Konfiguration per API | „Nur **Mandanten-Administratoren** sind berechtigt, Konfigurationen am Repository vorzunehmen" | Automatisierte Anlage von Wertemengen-Einträgen/Gesellschaften (**zu prüfen**) | B00 §Q; B03 §8d; U51 |
| I04 | **DMS Webhooks** (d3-server-webhook) | API vorhanden | Ereignisumfang nicht ausgewertet | Push an Bim4You/ERP bei Ablage/Statuswechsel (Abl.) | B00 §Q |
| I05 | Identity / Usermanagement / Process / Task / Dashboard (`dash`) / Inbound Scan / Document Reader / OCR – APIs | APIs vorhanden; Dashboard-API mit `ListContent` für Listen-Widgets | Keine Widget-Registrierung in den OpenAPI-Specs von task, process, shell, sign, dms-app, inbound scan, records management | Eigene Listen-Widgets, Benutzer-Provisionierung | B00 §Q, §X, §Z |
| I06 | **smart invoice API** | Stammdaten (Mandanten `companies` mit Hierarchie, Kreditoren mit `vat_id`/`registration_id`, Kostenstellen, Kostenträger, Sachkonten mit `company_id`) | – | Gesellschafts-/Kreditorenstammdaten aus DATEV/ERP synchronisieren | B00 §I, §AI, §AM; B03 §8d; U49 |
| I07 | **Ereignisse / Prozessstart** | process studio: Start bei **Dokumentimport** (Beispiel „Kategorie Rechnungen"), Bedingungen als JSON-Logik; Serviceaktivität; **d.velop actions eventbridge** (ab 2025.q1); Timer/CRON (min. 1 Stunde) | Welche Felder das Import-Ereignis liefert, ist **nicht dokumentiert** | Verträge/Post-Workflows automatisch starten | B00 §U, §V2, §V7 |
| I08 | **E-Mail** | email import: **Microsoft Graph** (Entra-App-Registrierung, Mail.ReadWrite, User.ReadBasic.All, Client-Secret); Exchange On-Prem über email fetcher (EWS); IMAP nur „zukünftig"; inbound e-mail mit Outlook-Add-In | Nur **eine** Bereitstellungsform je email import; Abrufintervall nicht dokumentiert | Livos-Mailsystem klären | B00 §AS, §AT |
| I09 | Postverteilung | Webhook-Start in der Postverteilung | nicht im Detail ausgewertet | – | B00 §AU |
| I10 | **DATEV** | Handbücher **d.velop connect for datev** Admin 5.3.0 / Anwenden 5.0.0 existieren | **Beide hinter Login**; Funktionsumfang (Journale, Zahlungsrückmeldung, Frequenz, Mandanten-Mapping) **nicht belegt** | Kern-Schnittstelle laut Zielarchitektur → R-11 | B00 §P, §AQ |
| I11 | **ERP** | smart-invoice-Mandant = „Mandant oder Buchungskreis im ERP-System"; Stammdaten-API | Kein ERP-Konnektor (SAP, Bim4You o. Ä.) in den Quellen | Bim4You über API/Webhooks/Serviceaktivität (Abl.) → R-12 | B00 §I |
| I12 | **E-Rechnung** | ZUGFeRD/XRechnung „liegen alle Daten direkt maschinenlesbar … vor"; d.velop eInvoice converter | Feldliste der Rechnungslesung hinter Login | – | B00 §AP |
| I13 | SSO / Verzeichnis | AD, Kerberos, OpenID Connect; open id provider app für Drittsysteme | Entra-SSO für die Cloud nicht belegt | → R-07 | B03 §6e |
| I14 | On-Prem-Erweiterung | **Hook-Funktionen (JPL)**, Hostimport (HOSTIMP), d.3 asynchrone Verarbeitung | Hooks in der Cloud **nicht gefunden** → dort `@D3SET` als Alternative | – | B03 §3b, §7e, §8c |
| I15 | Mapping zwischen Apps | Feature **Zuordnungen / Mappings** zwischen documents-Eigenschaften und Eigenschaften anderer Apps (Cloud, inbound scan) | – | smart invoice ↔ documents ↔ inbound konsistent halten | B03 §8b |

---

## 9. Explizit belegte Grenzen und Einschränkungen

| # | Grenze (F) | Wert / Wortlaut | Plattf. | Wirkung für Livos (Abl.) | Quelle |
|---|---|---|---|---|---|
| G01 | Kategorien je Repository | max. **2.000** Dokument-/Aktenarten | O | unkritisch | B03 §1 |
| G02 | Eigenschaften je Kategorie | max. **89** (49 alphanumerisch / 10 Datum / 10 Geld / 10 numerisch / 10 Mehrfach) | O | unkritisch; Positionsplan nötig | B03 §2; B00 §G |
| G03 | DB-Position einer Eigenschaft | „sorgfältige Planung nötig, … nachträgliche Änderungen … eingeschränkt" | O | vor dem Go-live fixieren | B03 §3c |
| G04 | Kürzel Dokumentart | max. 5 Zeichen, **nicht änderbar** | O | Konvention vorab | B03 §2 |
| G05 | Länge alphanumerisch | On-Prem 35 Bytes Standard, max. 250 Bytes; Cloud (inbound scan) bis 7.000, teils 2.000 Zeichen | O / C | Buchungstext/Betreff ausreichend dimensionieren | B03 §3c, §8b |
| G06 | Mehrfachfeld | Positionen 60–69; 100 Werte Standard, max. 2.000 (d.3 config, On-Prem); **ein Wert je Eintrag** | O | Keine Kostenstellen-Anteile in documents | B03 §3e |
| G07 | Datentypen | 5 Typen, **kein Boolean** | C+O | Ja/Nein per Wertemenge | B03 §3a |
| G08 | Eindeutigkeit | **Keine** Eindeutigkeitsprüfung auf Eigenschaftswerten | O | Dubletten über smart invoice (Teil B) | B03 OP6 |
| G09 | Wertemenge | Wert max. 250 Zeichen; Obergrenze an Einträgen **nicht dokumentiert** | O | >100 Gesellschaften prüfen | B03 §3b, OP2 |
| G10 | Gruppennamen | eindeutig in den **ersten 8 Zeichen**; nicht gleichnamig mit Benutzern | O | Namensschema Gesellschaft+Funktion in 8 Zeichen | B03 §6a, §6b |
| G11 | Benutzername | max. 30 Zeichen, **nicht änderbar** | O | Schema für Externe | B03 §6a |
| G12 | Optionale Benutzerfelder | 10 Felder à 50 Zeichen | O | `@D3USER_OPTFIELD` nur bei wenigen Gesellschaften je Benutzer | B03 §6a |
| G13 | Dokumentklasse | Kürzel max. 10, `CLAS_` reserviert; dokumentartunabhängige Klasse nicht allein zuordenbar, Restriktion auf **DB-Positionen** | O | „Gesellschaft" auf einheitlicher Position | B03 §5b, §5c |
| G14 | Repository-ID | 2 Zeichen, **5 IDs**, reiner Speicher-Pool | O | kein Mandantenmittel | B03 §4 |
| G15 | Wirksamkeit | Nach Änderungen an Arten und Rechten **neu anmelden**; IdP-Gruppen-Sync **stündlich**; IdP verknüpft nur Gruppen, keine Einzelbenutzer | O | On-/Offboarding-Latenz einplanen | B03 §2, §5b, §6e |
| G16 | Sub-Administration | Sub-Admin kann keine Sub-Admins anlegen; in der Cloud nicht belegt | O | Delegationsmodell prüfen | B03 §6d, §8c |
| G17 | Aktenbildung | Leere Erkennungseigenschaften → **keine** Akte | O | Pflichtfelder durchsetzen | B03 §7d |
| G18 | Aktennavigation | standardmäßig **erste 100 Elemente** | C+O | große Kreditorenakten | B01 §5.5 |
| G19 | Export | **Akten können nicht** als PDF zusammengefasst/exportiert werden | C+O | Prüferexport über Eigenschaften-Export/API | B01 §8.4 |
| G20 | Editionen | **Aktivitäten** nur Cloud; **Teilen** nur Cloud; **Extern Teilen** nur *documents business*; **Prozessportal** nur [A]; **Aufgabenlisten** nur [B] | C / O | Cloud-Entscheid bestimmt den Funktionsumfang | B00 §E; B01 EV |
| G21 | Volltext | [A] nur wenn installiert; Sonderzeichen werden ignoriert; `*` nur am Wortende | C+O | Suche nach Rechnungsnummern testen | B01 §6.3, §6.5 |
| G22 | Freigabe / Änderungstext / Schwärzen | Freigeben-Recht und Änderungstext nur durch den **d.3-Administrator**; Schwärzen standardmäßig aus | C+O | Admin-Tätigkeiten im Betriebskonzept | B01 §8.2, §8.4, EV |
| G23 | Dashboard | 4 Standard-Widgets; kein Filterfeld, kein Chart; Sichtbarkeit ≠ Sicherheit; „Zuletzt bearbeitet" ohne Statuswechsel | C+O | KPI-Wünsche nur über Entwicklung oder Rechnungseingangsbuch | B00 §X–§Z, §AF |
| G24 | Liegezeit | existiert **nirgends** | C+O | Katalog 3.2 nur mit Vorbehalt | B00 §AB |
| G25 | Vertretung | Aufgaben gehen **nicht automatisch** an den Vertreter über; der Vertreter übernimmt die **Berechtigungen** | C | Kommunikation + Mandanten-Governance | B00 §V6 |
| G26 | Prozesse | max. 200 Variablen; **kein Testmodus**; „Rolle" ist kein Zuweisungsobjekt; Timer min. 1 Stunde; Protokoll 30 Tage bis 1 Jahr; Zahlenvergleich im Ausdruck nicht dokumentiert | C+O | Test-/Transportkonzept | B00 §V3, §V4, §V7, §V8, §V10 |
| G27 | DMS-API | Upload max. 100 MB Body (empfohlen 25 MB); kein multipart | C+O | Migration großer Dateien in Chunks | B00 §Q |
| G28 | E-Mail-Import | produktiv nur M365/Graph; IMAP „zukünftig"; nur eine Bereitstellungsform; Intervall undokumentiert; Postfach vorher leeren | C | Livos-Mailsystem entscheidet | B00 §AS |
| G29 | smart invoice | Mandantenerkennung über **Name + Anschrift, nicht Steuernummer**; Beträge in **Cent**; Verbindungen Top-down; Freigabematrix max. 20 Zusatzspalten; Grenze je **Kostenobjekt**; Vier-Augen = Vorschau-Feature; **kein** Standard-Aufteilungsschlüssel | C | Alias-Postfach je Gesellschaft; Katalog 2.2/2.8 mit Vorbehalt | B00 §AI–§AM |
| G30 | Rechnungseingangsbuch | Archiv 6 Monate (erweitert 12) | C | Ältere Rechnungen über die documents-Suche | B00 §AO |
| G31 | Import-Widget | max. 4 Dropzones je Widget | C | mehrere Widgets möglich („beliebig viele") | B00 §AC |
| G32 | Klassifikation | keine dritte Ebene unterhalb der Kategorie | C+O | Belegart als Eigenschaft | B01 §4.3 |
| G33 | Hooks / d.3 config | nur On-Prem belegt | O | In der Cloud `@D3SET` statt `@D3HOOK` | B03 §8c |
| G34 | Dokumentationszugang | Cloud-Admin-Doku nicht öffentlich; 80 von 132 relevanten Handbüchern hinter Login | – | Portal-Zugang beschaffen | B00 §L, §N, §P; B03 OP7 |

---

## 10. Lücken der Recherche – konkrete Rechercheaufträge

Priorität: **P1** = blockiert die Konzeptfreigabe · **P2** = vor dem Angebot klären · **P3** = vor der Umsetzung klären.

| ID | Prio | Lücke (belegt als fehlend) | Warum für Livos kritisch | Konkreter Auftrag | Bezug |
|---|---|---|---|---|---|
| R-01 | **P1** | Cloud-Administration nicht öffentlich; Dokumentklassen/Makros/unabhängige Klassen/Sub-Admin/Aktenbildung/automatische Ablage nur für On-Prem belegt | Die Mandantentrennung für >100 Gesellschaften hängt daran | Zugang zum d.velop Service-Portal beschaffen; Handbuch `cloud` (HB/cloud/latest) auswerten; Liste „On-Prem-Baustein → Cloud-Äquivalent (ja/nein/Menüpfad)" erstellen; abgleichen mit dem Klickweg der Demo-Instanz (A_01, Teil B) | B00 §L, §P; B03 §8c, OP7, OP8 |
| R-02 | **P1** | Kein Kapitel zur Mandantenfähigkeit; Verhalten von `@D3GROUP` (Gleichheit/Teilstring, verschachtelte Gruppen, leere Werte) und Obergrenzen undokumentiert | Datenschutz zwischen Gesellschaften, Skalierung | **PoC auf mdisconsulting.d-velop.cloud:** 3 Gesellschaften, 3 Gruppen, 1 Klasse mit Makro; Tests: Teilstring-Schlüssel, Benutzer in 2 Gruppen, verschachtelte Gruppe, leeres Feld, Vertreter aus fremder Gesellschaft. Schriftliche Aussage von d.velop zu Grenzen (Klassen, Profile, Gruppen, Wertemengen-Einträge) bei 150 Gesellschaften | B00 §J, §M; B03 §4, OP1, OP2 |
| R-03 | **P1** | Lizenzmodell (Named/Concurrent, Leser, Externe, Editionen, Volumen smart invoice/email import/process) nicht belegt | ~80 Anwender intern+extern, 5.000–8.000 Belege/Jahr; Agenda-Frage „Lizenz/Mengengerüst" | d.velop-Preisliste/Partner-Lizenzhandbuch anfordern; klären: Edition *documents business* nötig? Lizenzfolge von „Extern Teilen" und „Externe Benutzeraufgabe"; ist Katalog 4.2 (Ad-hoc-Freigabe Externer ohne Lizenz) möglich? | B00 §E; B01 §8.3; B03 §6a |
| R-04 | **P1** | DATEV-Schnittstelle vollständig hinter Login | DATEV ist das operative FiBu-System (ER-/Zahlungsjournale, Rückmeldungen) | `connect-datev-admin` (5.3.0) + `connect-datev-user` (5.0.0) auswerten: Datenobjekte, Richtung, Frequenz, Mapping 100+ Gesellschaften ↔ DATEV-Mandanten/Beraternummern, Fehlerbehandlung; Abgleich mit B_02 (Teil B) | B00 §P, §AQ |
| R-05 | **P1** | GoBD/Revisionssicherheit nicht belegt (Anwenderdoku 1× Schwärzen; storage manager nicht ausgewertet) | Belegablage steuerrelevanter Rechnungen | `storage-manager` 3.20.0 auswerten (Retention, `extendretention`, Unveränderbarkeit, Cloud-Speicher); bei d.velop Testat/Zertifikat und Muster-Verfahrensdokumentation für d.velop cloud anfordern | B00 §O, §T; B01 §7.3 |
| R-06 | P2 | Aufbewahrung/Löschung: Wirkung der Lebensdauer, Löschlisten, Löschfreigabe, Legal Hold, Löschprotokoll nicht belegt | GoBD-Fristen vs. DSGVO-Löschpflichten | d.3-admin-Kapitel „Lebensdauer/ereignisorientiert" und storage manager lesen; klären: automatische Löschung oder Löschvorschlag? Löschung je Gesellschaft? | B03 §2, §3d; B00 §T |
| R-07 | P2 | SSO mit **Microsoft Entra ID** für d.velop cloud nicht belegt (nur OIDC/AD/Kerberos im On-Prem-IdP; Entra nur für email import) | Zentrale Identitäten, Gäste (B2B) für Externe | Cloud-Handbuch (`cloud`, `usermanagement-cloud-on-premises`) auswerten: SAML/OIDC mit Entra, Gruppen-Sync (Intervall, Verschachtelung), SCIM, Verhalten von `@D3IDPGROUP`, Entra-B2B-Gäste als externe Anwender | B03 §6e; B00 §AS |
| R-08 | P2 | Audit-Trail „Aktivitäten": Vollständigkeit, Aufbewahrung, Export, Manipulationsschutz, Leseprotokoll | Nachweis für Prüfer und Revision | Test in der Cloud-Instanz (Eigenschaft ändern, Kategoriewechsel, Verknüpfen, Download → erscheint das?); Doku-Frage an d.velop zu Aufbewahrungsdauer und Export | B01 §7.2, OP6 |
| R-09 | P2 | DSGVO-Handbuch nicht ausgewertet; Rechenzentrum/AVV/Auskunft offen | Personenbezogene Daten (Mieter, Mitarbeiter) | `dsgvo` 1.0 auswerten; AVV, RZ-Standort und Subunternehmer der d.velop cloud anfordern | B00 §O |
| R-10 | P2 | Automatische Aktenbildung in der Cloud; Standardaktenpläne und Lieferantenakte hinter Login | Aktenplan Gesellschaft/Kreditor/Objekt | `standardaktenplaene` + `supplier-file` auswerten; in der Demo-Instanz prüfen, ob Aktenbildungsregeln konfigurierbar sind und ob **mehrere Regeln je Dokumentart** (Mehrfachzuordnung zu drei Aktenarten) funktionieren | B00 §K12, §P; B03 §7 |
| R-11 | P2 | Reporting (Handbuch hinter Login), Prozessportal-Formularintegration, Liegezeit, Exportformat | Management-Sicht, Katalog 3.2 | `reporting` + `prozessportal-formularintegration` auswerten; Format von „Eigenschaften exportieren" testen; Aufwand für ein Listen-Widget (ListContent-Dienst) schätzen | B00 §AB, §AE, §P; B01 §5.5 |
| R-12 | P2 | ERP/Bim4You-Kopplung: kein Konnektor belegt; Ereignisumfang der Webhooks/Import-Ereignisse undokumentiert | Budgetabgleich, Freigabestatus zurück | API-Doku `d3-server-webhook`, `dms-app`, smart invoice API lesen; Ereigniskatalog erstellen; mit Bim4You Schnittstellenformat abstimmen | B00 §Q, §V7 |
| R-13 | P2 | Externe Anwender: Rechte, Mandantentrennung, Mitwirkung im Workflow | ~80 Anwender inkl. Externer | Klären: Unterliegen Externe den Dokumentklassen? Funktionsumfang von „Externe Benutzeraufgabe"? Sind Freigabelinks mit Passwort/Protokoll möglich? | B00 §E, §V2, §Z; B01 §8.3 |
| R-14 | P3 | Outlook/Office-Integration für d.velop documents **Cloud** (außer inbound-Add-In); Mobile App | Anwenderakzeptanz | Aktuelle Produktseite/Handbuch prüfen: Outlook-App für documents Cloud, Office-Bearbeitung in der Cloud, Mobile App (iOS/Android) oder responsives Web | B01 §1.1, EV; B00 §AT |
| R-15 | P3 | Produkte ohne Beleg: **d.velop contract, sign, postbox, pilot, archive, records management** | Vertragsmanagement ist Zielprozess (Briefing) | Existenz, Funktion, Cloud-Verfügbarkeit, Lizenz prüfen; Abgleich mit B_02/B_06 (Teil B, dort pilot/records management/connect for Microsoft erwähnt) | B00 §X; §1.5 dieses Dokuments |
| R-16 | P3 | Kleinere Doku-Lücken | Demo-/Schulungsqualität | Nachlesen: FAQ [A] 1.5.28 Repository-Wechsel; Gruppieren in der Tabellenansicht; [B] 1.4.10 Layouts; [B] 1.3.6 d.velop pages; [B] 1.7 Scannen; Kalenderfunktion; Kennzeichnung von Pflichtfeldern in der UI; automatische Titelbildung | B01 OP7–OP10, OP12 |
| R-17 | P3 | Volltext in der Cloud (standardmäßig aktiv? OCR für Bild-PDFs?) | Findbarkeit gescannter Post | In der Demo-Instanz testen; `decs-ocr`-API und rendition service prüfen | B01 §6.3; B00 §Q, §AU |
| R-18 | P3 | Beispiel „Berechtigungsverwaltung über Mengen" (restriction set manager) nur verdichtet gelesen | Delegation der Gesellschaftszuordnung | URL aus B03 OP9 vollständig lesen; Cloud-Verfügbarkeit von `@D3SET` klären | B03 §5d, OP9 |

---

## Anhang: Quellenverzeichnis (URLs wie in den Quelldateien angegeben)

`HB` = `https://help.d-velop.de/docs/de/pub`

| ID | Inhalt | URL | via |
|---|---|---|---|
| U01 | [A] d.3one und d.velop documents: Anwenden 2026.q3 (PDF 59 S.) | HB/one-documents/latest · https://help.d-velop.de/docs/api/documentations/de/one-documents/2026.q3/pdf | B00 §A; B01 |
| U02 | [B] d.velop documents: Anwenden (cloud) (PDF 52 S.) | HB/documents/latest · https://help.d-velop.de/docs/api/documentations/de/documents/cloud/pdf | B00 §A; B01 |
| U03 | Ablage | HB/one-documents/latest/weitere-funktionen-und-einstellungen/speichern-von-dateien-mit-dem-feature-ablage · HB/documents/latest/erste-schritte-beim-ablegen-und-speichern-von-dokumenten | B01 §4.1 |
| U04 | Akte erstellen | HB/one-documents/latest/weitere-funktionen-und-einstellungen/erstellen-einer-neuen-akte | B01 §5 |
| U05 | Verknüpfen mit Akte | HB/one-documents/latest/haufig-gestellte-fragen/wie-verknupfe-ich-ein-dokument-mit-einer-akte | B01 §5 |
| U06 | Automatisches Speichern in Akten | HB/one-documents/latest/weitere-funktionen-und-einstellungen/automatisches-speichern-von-dokumenten-in-akten · HB/documents/cloud/erste-schritte-beim-ablegen-und-speichern-von-dokumenten/automatisches-speichern-von-dokumenten-in-akten | B01 §5; B03 §7f |
| U07 | Manuelles Speichern in Akten | HB/one-documents/latest/weitere-funktionen-und-einstellungen/manuelles-speichern-von-elementen-in-akten | B01 §5 |
| U08 | Aktennavigation | HB/one-documents/latest/haufig-gestellte-fragen/wie-navigiere-ich-durch-akten · …/weitere-funktionen-und-einstellungen/anzeigen-eines-elements-in-der-zugehorigen-akte | B01 §5 |
| U09 | Suche, Facetten, Operatoren, Volltext | HB/one-documents/latest/erste-schritte/wissenswertes-zur-suche (…-mithilfe-von-facetten, …-zu-suchoperatoren-und-platzhalterzeichen, finden-von-inhalten-mithilfe-von-eigenschaften-und-kategorien, …-von-stichwortern) · HB/documents/latest/erste-schritte-beim-suchen-und-finden · HB/documents/latest/haufig-gestellte-fragen-rund-ums-arbeiten-mit-dvelop-documents/was-wird-bei-der-volltextsuche-durchsucht | B01 §6 |
| U10 | Suchvorlagen teilen | HB/one-documents/latest/tipps-und-tricks/teilen-von-suchvorlagen-im-team | B01 §6.6 |
| U11 | Perspektiven | HB/one-documents/latest/haufig-gestellte-fragen/was-ist-eine-perspektive-zu-einem-element | B01 §1, §7.1 |
| U12 | Änderungstext | HB/one-documents/latest/weitere-funktionen-und-einstellungen/erstellen-einer-neuen-version-eines-dokuments-mit-anderungstext | B01 §7.1 |
| U13 | Dokumentstatus | HB/one-documents/latest/haufig-gestellte-fragen/wozu-dient-der-status-eines-dokuments | B01 §7.1 |
| U14 | Aktivitäten | HB/documents/latest/haufig-gestellte-fragen-rund-ums-arbeiten-mit-dvelop-documents/was-sind-aktivitaten · …/wo-finde-ich-aktivitaten-zu-dokumenten-und-akten | B01 §7.2 |
| U15 | Schwärzen | HB/one-documents/latest/weitere-funktionen-und-einstellungen/schwarzen-von-dokumentinhalten | B01 §7.3 |
| U16 | Bearbeiten / Eigenschaften / Abschließen | HB/one-documents/latest/weitere-funktionen-und-einstellungen/bearbeiten-von-dokumenten · …/aktualisieren-von-eigenschaften · …/abschliessen-der-bearbeitung-eines-dokuments | B01 §8 |
| U17 | Teilen | HB/documents/latest/erste-schritte-beim-teilen-von-dokumenten-mit-anderen-personen | B01 §8.3 |
| U18 | Aufgaben | HB/one-documents/latest/haufig-gestellte-fragen/wozu-dient-das-feature-aufgaben-und-nachrichten · HB/documents/latest/erste-schritte-beim-arbeiten-mit-aufgaben/wissenswertes-zu-aufgabenlisten · …/erstellen-einer-aufgabe-zu-einem-dokument · HB/documents/latest/haufig-gestellte-fragen-rund-ums-arbeiten-mit-dvelop-documents/wozu-dient-die-perspektive-prozess | B01 §3 |
| U19 | Dashboard (Anwender) | HB/one-documents/latest/erste-schritte/arbeiten-mit-widgets-im-dashboard · HB/documents/latest/haufig-gestellte-fragen-rund-ums-arbeiten-mit-dvelop-documents/wie-arbeite-ich-mit-den-widgets-im-dashboard | B01 §2 |
| U20 | Bedienkonzept, Prozessportal, Persönlicher Bereich | HB/one-documents/latest/basisinformationen-zur-anwendung-und-zum-handbuch · …/haufig-gestellte-fragen/was-ist-eine-kontextaktion · …/was-ist-das-prozessportal · …/wozu-dient-das-feature-personlicher-bereich | B01 §1 |
| U21 | Vorlage zur Aktenerstellung | HB/one-documents/latest/tipps-und-tricks/erstellen-einer-vorlage-zur-aktenerstellung | B01 §5.2 |
| U30 | Struktur des d.3-Repository | HB/admin/latest/allgemeine-erlauterungen/struktur-des-elektronischen-d3-repository | B03 §1 |
| U31 | Dokumentarten (allgemein, Basiskonfiguration, Eigenschaften auswählen) | HB/admin/latest/administration/dokumente-und-akten/dokumentarten (…/dokumentarten-allgemein, …/angaben-zur-dokumentart/basiskonfiguration, …/erweiterte-eigenschaften-auswahlen) | B03 §1, §2 |
| U32 | Erweiterte Eigenschaften / Feldeigenschaften / Mehrfachfeld | HB/admin/latest/administration/dokumente-und-akten/erweiterte-eigenschaften (…/feldeigenschaften, …/feldeigenschaften/mehrfacheigenschaftsfeld) | B03 §3 |
| U33 | Wertemengen | HB/admin/latest/administration/dokumente-und-akten/wertemengen | B03 §3b |
| U34 | Pflicht | HB/admin/latest/administration/dokumente-und-akten/dokumentarten/positionen-der-erweiterten-eigenschaften/details-fur-die-eigenschaft-angeben/pflicht | B03 §3d |
| U35 | Repositorys erstellen/konfigurieren; Konfiguration übertragen | HB/installieren-aktualisieren-documents/2024.q3/erstellen-und-konfigurieren-von-repositorys · HB/installieren-aktualisieren-documents/annual%202024/haufig-gestellte-fragen/wie-kann-ich-die-konfiguration-eines-repositorys-auf-ein-anderes-repository-ubertragen | B03 §1, §4 |
| U36 | Berechtigungskonzept / Klassenkonzept | HB/admin/latest/allgemeine-erlauterungen/berechtigungskonzept · …/berechtigungskonzept/berechtigungsprofile-und-dokumentklassen/dokumentarten-und-klassenkonzept | B03 §4, §5 |
| U37 | Makros | HB/admin/latest/administration/berechtigungen/dokumentklassen/definition-der-restrikitionen/makros | B03 §4 |
| U38 | Dokumentklasse hinzufügen / Restriktionen | HB/admin/latest/administration/berechtigungen/dokumentklassen/dokumentklasse-hinzufugen · …/dokumentklassen/definition-der-restrikitionen | B03 §5 |
| U39 | Berechtigungsprofile / Zuordnung | HB/admin/latest/administration/berechtigungen/berechtigungsprofile · …/berechtigungsprofil-zuordnung | B03 §5 |
| U40 | Dokumentartunabhängige Klasse | HB/admin/latest/administration/berechtigungen/dokumentklassen/dokumentart-unabhangige-klasse | B03 §5c |
| U41 | d.3 inherit rights manager | HB/admin/latest/administration/berechtigungen/d3-inherit-rights-manager | B03 §5e |
| U42 | d.3 restriction set manager (+ Beispiel 2) | HB/admin/2023.q3/administration/berechtigungen/d3-restriction-set-manager · …/anwendungsfalle/beispiel-2-berechtigungsverwaltung-uber-mengen | B03 §5d, OP9 |
| U43 | Benutzer / Gruppen / Sub-Administration | HB/admin/latest/administration/berechtigungen/benutzer/benutzer-anlegen · …/gruppen/gruppe-anlegen · …/sub-administration | B03 §6 |
| U44 | Identity Provider / Gruppenbeschränkung / OIDC-App | HB/installieren-aktualisieren-documents/annual%202024/konfigurieren-der-dvelop-komponenten/konfigurieren-von-decs-identity-provider · HB/installieren-aktualisieren-documents/2023.q4/erste-schritte-beim-konfigurieren-eines-d3-repositorys/hinzufugen-eines-benutzerproviders-fur-die-authentifizierung · https://portal.d-velop.de/documentation/konfigguideinfrastructure/de/wie-schraenke-ich-die-anmeldung-auf-bestimmte-gruppen-ein-228787258.html · HB/open-id-provider-app/latest | B03 §6e |
| U45 | Benutzerrollen (task / process) | HB/task-admin/2.6.0/konfigurieren-von-decs-task/einrichten-von-benutzerrollen · HB/process-on-premises/1.14.0/konfigurieren-von-dvelop-process/einrichten-von-benutzerrollen-optional | B03 §6c |
| U46 | Aktenbildung / folder scheme | HB/admin/latest/administration/dokumente-und-akten/aktenbildung · HB/admin-folder-scheme/latest · HB/admin-folder-scheme/8.2.0/aktenbildung-durchfuhren/voruberlegungen · …/verknupfung-erstellen · …/das-modul-aktenbildung/aktenbildung-erkennung · …/aktenbildung-vererbung | B03 §7; B00 §K12 |
| U47 | Automatische Ablage | HB/admin/latest/administration/dokumente-und-akten/automatische-ablage | B03 §7f |
| U48 | Tenant-Grundlagen | https://portal.d-velop.de/dev/de/basics | B03 §4, §8 |
| U49 | smart invoice: Stammdaten-API / Berechtigungen Rechnungsdokumente / Objekte und Felder | HB/smart-invoice-developer/cloud/verwenden-der-api-funktionen/ubertragen-von-stammdaten-dvelop-smart-invoice · HB/smart-invoice-cloud/cloud/konfigurieren-von-dvelop-smart-invoice/interagieren-mit-dvelop-documents/erteilen-von-berechtigungen-fur-die-rechnungsdokumente · HB/smart-invoice-cloud/cloud/konfigurieren-von-dvelop-smart-invoice/wissenswertes-uber-bedingungen/wissenswertes-zu-objekten-und-feldern | B03 §3e, §4; B00 §I |
| U50 | inbound scan Cloud: Kategorien/Eigenschaften | HB/inbound-scan-admin-cloud/cloud/konfigurieren-von-dvelop-inbound-scan/wissenswertes-zu-kategorien-und-eigenschaften · …/konfigurieren-von-eigenschaften | B03 §1, §8b |
| U51 | DMS-API zur Repository-Konfiguration | https://portal.d-velop.de/documentation/dmscfgapi/de/dms-api-zur-konfiguration-von-d-3-repositorys-706506717.html | B03 §8d |
| U52 | d.3-Systemumgebung (FAQ) | HB/installieren-aktualisieren-documents/annual%202024/haufig-gestellte-fragen/wie-ist-eine-d3-systemumgebung-grundsatzlich-aufgebaut | B03 §8 |
| U53 | API-Verzeichnis / DMS / Config / Webhooks / Dashboard | https://help.d-velop.de/dev/documentation · …/dms-app · …/dmsconfig · …/d3-server-webhook · …/dash · (OpenAPI dash: help.d-velop.de/dev/api/openapi/dash) | B00 §Q, §Z |
| U54 | DMS-API Tutorial / Beispiele | portal.d-velop.de/dev/de/tutorials/dms-api-erste-schritte-zur-anbindung-eines-externen-systems-an-die-dms-app · github.com/d-velop/dvelop-examples-cs | B00 §Q |
| U55 | d.velop email import | HB/email-import/cloud | B00 §AS |
| U56 | connect for privatabrechner (Praxisleitfaden) | HB/connect-privatabrechner-admin/1.0.0/konfigurieren-der-akten-und-dokumentarten-und-eigenschaften-in-d3-admin | B03 §2 |
| U57 | Doku-Übersicht / URL-Schema / PDF-Export | https://help.d-velop.de/docs/de/explore · HB/{slug}/latest · https://help.d-velop.de/docs/api/documentations/de/<produkt>/<version>/pdf | B00 §A, §N |
| U58 | Handbuch-Slugs (frei) aus der Inventur | smart-invoice-cloud, smart-invoice-on-premises, smart-invoice-developer, invoice-monitor, process-cloud, process-on-premises, process-studio-user/-admin, mail-dispatcher-admin, email-import, inbound-e-mail, inbound-scan-user-cloud/-on-premises, admin, admin-folder-scheme, one, task-user/-admin, storage-manager, usermanagement-cloud-on-premises, document-reader, dsgvo | B00 §O |
| U59 | Handbuch-Slugs (Login) | connect-datev-admin, connect-datev-user, document-reader-invoice, standardaktenplaene, supplier-file, classify, capture-batch-admin, forms-admin, flow-designer, cloud, prozessportal-formularintegration, reporting | B00 §P |
