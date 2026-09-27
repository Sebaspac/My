# 14 – Web-Recherche: Umsysteme und Schnittstellen des Livos-DMS (Stand 26.09.2026)

**Auftrag:** Umsysteme rund um d.velop bei Livos: BIM4You, Property Manager, d.velop-APIs, evidanza, Acumatica/X360, MDIS.
**Methode:** Web-Recherche mit WebSearch/WebFetch/curl. Hersteller-PDFs wurden heruntergeladen und im Volltext ausgewertet (BIM4You-Changelogs 2022–2026, d.velop smart invoice-API-PDF, OpenAPI-Spezifikationen der d.velop-Apps, process-studio-Leistungsbeschreibungen). Rohdaten liegen in `SP/web/`.
**Kennzeichnung:** **Fakt** = mit Quelle belegt ([Q#] → Quellenliste in Kap. 9, jeweils mit URL). **Annahme** = eigene Ableitung ohne direkten Beleg. **Offen** = zu klären.
**Zielarchitektur (angesehen):** `SP/img/arch_2.png` (DMS-Systemarchitekturen) und `SP/img/arch_3.png` (Eingangs-Rechnungsprozess).

---

## 0. Kernaussagen (Kurzfassung)

1. **BIM4You** kommt von der **BIB GmbH (Offenburg)** und ist ein Bau-Projektsteuerungs- und Kostencontrolling-System. Es bringt **Rechnungseingangsbuch, Budget-Controlling je Vergabeeinheit, Verträge/Nachträge, Zahlungsfreigaben mit Abzügen/Einbehalten, 4-/6-Augen-Prüfworkflow, §48-Prüfung** und eine **DATEV-Buchungsstapel-Schnittstelle** mit [Q1–Q4, Q6]. Damit deckt BIM4You fachlich genau die Bau-Spezifika ab, die im Katalog für d.velop mit „N“ bewertet sind (5.2 VOB/Einbehalte).
2. **Eine REST-API von BIM4You ist öffentlich nicht dokumentiert.** Belegt sind nur Datei-/Lizenz-Schnittstellen: E-Rechnungs-Import (XRechnung/ZUGFeRD), DATEV-Export (CSV/XML), DocuWare-Schnittstelle (Austauschordner plus Barcode), Scanordner, GAEB, IFC und SEPA [Q1–Q3]. Eine Anbindung an d.velop braucht deshalb eine **Middleware**. Referenzfall: Krieger + Schramm hat DocuWare, BIM4You und DATEV mit **selbst programmierten** Schnittstellen gekoppelt [Q7].
3. **Die smart invoice-API passt gut als Übergabepunkt an BIM4You.** Ein Export wird an einer **Schrittverbindung** ausgelöst, per Webhook (Quittung in 30 s) oder per Abhol-API (Zeitfenster bis 28 Tage). Die Gegenseite meldet Erfolg oder Fehler zurück. Ein Fehler leitet den Beleg an die Fehlerstelle [Q11]. **Die API bietet aber keinen dokumentierten Endpunkt, mit dem ein Fremdsystem Beträge oder Felder eines laufenden Belegs ändern kann** [Q11, Q14]. Das ist das zentrale technische Risiko für den Rückfluss „Einbehalt/Kürzung“.
4. **d.velop-Plattform:** Authentifizierung per **API-Key als Bearer-Token** (Identity Provider) [Q17, Q30]. Cloud-Limits der DMS-API: **600 Updates bzw. 1.600 Neuanlagen je Minute und Mandant**, darüber HTTP 429 [Q16]. Der **Power-Automate-Konnektor** erlaubt 100 Calls je 60 s [Q30]. **process studio business (Cloud)** enthält **1.000 Workflowausführungen je produktivem Mandanten und Monat** [Q26]. Aufgabendetails werden **standardmäßig 30 Tage, höchstens 365 Tage** aufbewahrt [Q20, Q27].
5. **Property Manager:** Die Hausverwaltungs-ERP-Landschaft ist heterogen (Aareon Wodis/RELion/Karthago/PowerHaus, DOMUS, iX-Haus, immoware24, casavi …). Gemeinsam ist fast allen nur der **DATEV-Export** [Q55, Q57, Q58]. **Empfehlung:** (a) Freigabe-Postfach plus Rückmeldung per E-Mail (MDIS-Vorschlag) und (b) Import der ohnehin gelieferten DATEV-Buchungsdaten in die MDIS-Middleware (Vollständigkeits- und Kreditorenabgleich). Direkte API-Anbindungen je PM-System erst als Folgeprojekt (5.4).
6. **evidanza** ist eine BI-/Planungsplattform (Straubing, seit 2022 CSS-Gruppe, >275 Kunden). Sie läuft auf **MS SQL Server** oder eigener In-Memory-DB und hat mit **data.SYNAPSE** über 250 Konnektoren und REST-basierte Datenkommunikation [Q36–Q38]. Einen fertigen d.velop-Konnektor gibt es nicht. **Empfehlung:** Die Middleware protokolliert die Prozessereignisse aus d.velop in einer SQL-Staging-Schicht, evidanza liest von dort (Katalog 3.2).
7. **„ConnectorX360dvelop“** ist die **Haufe-X360-Customization** der Partnerschaft Haufe X360 und d.velop (seit 04/2024; Haufe X360 = deutsches Acumatica) [Q41–Q43]. Im Snapshot trägt die Assembly den Namen `Haufe.PT.Extensions.DMSConnector.dll` [SP/work/05_mocca_snapshot.md]. **Dass MDIS der Hersteller ist, ist nicht belegt.** Für 5.4 taugt der Connector nur als Muster.
8. **MDIS** ist eine Marke der Groß Business Group GmbH (Salching): Haufe-X360-Gold-Partner 2026, eigene Plattform „MDIS One“ bzw. KI-Plattform „X.One“ mit Middleware. d.velop und evidanza nennt MDIS als Technologiepartner [Q46–Q50]. **Im d.velop-Partnerverzeichnis ist MDIS nicht nachgewiesen (offen).**

---

## 1. BIM4You

### 1.1 Hersteller, Historie, Einordnung

| Aussage | Status | Quelle |
|---|---|---|
| Hersteller und Vertrieb: **BIB GmbH, Offenburg**. Seit 1994 entwickelt (zuerst „BT-Control“, dann „ALLbudget“), 2014 umbenannt in „Bim4you“. Ab 2008 Vertrieb auch durch **BRZ Deutschland** („Sf-Bau“). Windows, Client-Server oder Einzelplatz. Nach Wikipedia rund 3.000 deutsche Nutzerfirmen | Fakt | [Q5] |
| „Client + Web“. Das Jahresrelease 2026 (Stand Januar 2026) beschreibt Neuerungen bis Version 26.00.017 | Fakt | [Q1] |
| Die Datenhaltung ist eine **SQL-Datenbank** („Verwendung von diesem Sonderzeichen können innerhalb der SQL-Datenbank zu Folgefehlern … führen“) | Fakt | [Q1, Kap. 1.10.2] |
| Zielgruppe: Projektentwickler, Bauträger, Bauunternehmen, Investoren; „Projektcontrolling (Budget und Erlöse)“; Schnittstellen zu BRZ-ERP und GAEB | Fakt | [Q8], [Q9] |
| `bib-gmbh.de` und `brz.eu/de/loesungen/bim4you` leiten am 26.09.2026 auf **suiteify.com/loesungen/erp/bau-erp/bim** weiter („Suiteify BIM“). Infoniqa, Käufer von BRZ, firmiert seit 15.09.2026 als **Suiteify** | Fakt (Redirect beobachtet; Umfirmierung belegt) | [Q9], [Q10] |
| BIM4You bzw. BIB gehören inzwischen zur Suiteify-Gruppe oder werden dort vermarktet. Die Suiteify-Pressemitteilung nennt BIB/BIM4You nicht | **Annahme** | [Q10] |

### 1.2 Funktionsumfang mit Bezug zu Livos

| Funktion | Details (belegt) | Quelle | Katalog |
|---|---|---|---|
| **Budget-Controlling** | Einzelbudgets, Excel-Import, Budget-Split; Auswertung nach **Vergabeeinheiten**, DIN 276/277, StLB, BKI; Ur-, genehmigte und aktive Budgets je Vergabeeinheit | [Q6] | 5.3 |
| **Verträge/Vergaben** | Vergaben/Verträge mit Konditionen, Prognose der Endsumme; Zahlungspläne, **Rückstellungen, Nachträge**, Zuschüsse | [Q6] | 5.2 |
| **Rechnungseingangsbuch (REB)** | Projektbezogene **und projektübergreifende** Erfassung von Eingangsrechnungen; Spalten u. a. **Barcode** (2023) und Leistungsdatum (2026). Eine Rechnung lässt sich samt Dokumenten kopieren und mehreren Projekten/Gewerken zuordnen, wenn sie „über den Scanordner“ eingelesen wurde | [Q6], [Q3], [Q1] | 5.3 |
| **Rechnungsprüfung/Freigabe** | „Freigabe von Rechnungen (Vier-Augen-Prinzip)“. Aufgabenworkflow Rechnungsprüfer 1 → 2, optional **RP3 ab Betragsgrenze** (6-Augen); Vertretungen je Prüfer; Stornos schließen die Aufgaben automatisch | [Q6], [Q2, 2.5.14–2.5.17] | 1.4, 3.4 |
| **Zahlungsfreigaben mit Abzügen/Einbehalten** | Abzüge anteilig auch bei Abschlagszahlungen (Variable `AutoAbzugAZ`); Summen „Rechnungsbetrag geprüft“, „**Abzüge/Einbehalte**“, „Kostenfeststellung“; **Sicherheits- und Gewährleistungseinbehalte** je Abschlagszahlung bzw. Teilschlusszahlung; Vorauszahlungen und Nachlass | [Q4, 1.7.6], [Q3, Bugfixes .031/.038/.043], [Q1, 1.3.6, 1.10.7] | **5.2** |
| **Rechnungssplits** | MwSt.-Übernahme in Splits; „Splits aus RE-Verteiler“, „Splits aus Einheiten“, „Splits aus Budget“ | [Q4, 1.7.4] | 2.8 |
| **§48 EStG** | Variable `REFreigabe48`: Bei der Freigabe wird geprüft, ob die Freistellungsbescheinigung vorliegt bzw. noch gilt. Das ist **nur ein Hinweis, die Freigabe wird nicht gestoppt** („ob nun Bauabzugssteuer fällig wird“) | [Q3] | 2.6, 2.7 |
| **Mandanten/Kreditoren** | `FibuKtoMand` bzw. `FibuKtoNoKredDebNewMand`: **mandantenbezogene Kreditoren-/Debitorennummern** | [Q2, 2.2.3] | 2.2, 5.4 |
| **Liquidität/Forecast** | Rollierender Zahlungsplan, Forecast, Liquiditätsplan. Die Zahlungsplan-Spalten „Umlage …“ heißen seit 2024 „Forecast …“ | [Q2, 2.5.3–2.5.5], [Q1, 1.9] | – |
| **Infoserver-Jobs** | E-Mail-Versand (z. B. unbezahlte Rechnungen, Freistellungsbescheinigungen, Reporting) | [Q2, 2.9] | 3.3 |

### 1.3 Schnittstellen von BIM4You (belegt)

| Schnittstelle | Richtung / Technik | Quelle |
|---|---|---|
| **E-Rechnungsschnittstelle** (Zusatzlizenz) | **Import von XRechnung/ZUGFeRD ins Rechnungseingangsbuch** per Button. Enthält die E-Rechnung im Feld „Contract Number“ die BIM4You-Vertragsnummer, wird sie **automatisch der Vergabeeinheit zugewiesen**. Prüfung dann „über den Aufgabenworkflow oder direkt im BudgetControlling“. XML und eingebettetes PDF werden angehängt. Export von XRechnung-Ausgangsrechnungen möglich | [Q1, 1.1] |
| **DATEV-Schnittstelle** (Zusatzlizenz) | Export von Rechnungen „in Form eines **Buchungsstapels (CSV oder XML)** Richtung DATEV-FiBu“. XML auch im **„Ledger“-Format (Belegsatzdatendatei)**. Monatsdateien, Buchungsmonat wahlweise nach Rechnungs-, Eingangs-, Leistungs- oder Freigabedatum, optional „als bezahlt markieren“. Gesperrte Datensätze werden nicht exportiert | [Q2, 2.11], [Q1, 1.7] |
| **DocuWare-Schnittstelle** (Zusatzlizenz) | „Import von Rechnungen aus DocuWare“; Archivierung von BIM4You-Dokumenten in DocuWare. Die **Zahlungsfreigabe-PDF geht über einen UNC-Übergabeordner** (`DMSAblagepfad`) an DocuWare und wird dort **über den Barcode** mit der Rechnung verknüpft | [Q1, 1.8] |
| **DMS-Link** | Globale Variable `DMSApiUrl`: Aus URL und Barcode der Rechnung wird ein Link zum Beleg im DMS gebaut (wenn `DWVIEWPATH` leer ist) | [Q2, 2.5.18] |
| Scanordner | Rechnungen „über den Scanordner einlesen“, Scanpfad im REB | [Q3] |
| GAEB / IFC / SEPA / BRZ | GAEB X31 (Aufmaß), X86, D82; IFC-Import (ArchiCAD, Allplan, Revit); SEPA-Zahlungsdatei; BRZ-Projektverwaltung | [Q2], [Q1], [Q3], [Q4] |
| **REST-API** | In Changelogs 2022–2026, Wikipedia, BRZ-Akademie und Suiteify-Seite **nicht erwähnt** | **Offen** |
| **Anbindung an d.velop** | **Nicht dokumentiert.** d.velop listet BIM4You in der Integrationsübersicht nicht [Q32] | **Offen** |

**Referenzfall (Fakt, [Q7]):** Krieger + Schramm (Immobilien/Wohnungsbau) hat DocuWare „in enger Integration mit … der Bauplanungssoftware BIM4YOU implementiert, wobei die Schnittstellen vom eigenen IT-Orga-Team programmiert wurden“. Ablauf: Erkennung in DocuWare → Belegprüfung in der Buchhaltung → **fachliche Prüfung in BIM4YOU** → BIM4YOU gibt ein **Prüfprotokoll** aus, das den nächsten DocuWare-Workflowschritt auslöst → betragsabhängige Zusatzfreigaben → Buchung in DATEV. Das entspricht fast genau dem Livos-Zielbild in arch_3.

### 1.4 Deutung der Flüsse in der Livos-Zielarchitektur

Die Folien arch_2 und arch_3 zeigen: d.velop → Bim4You „Eingangsrechnungsjournale“; Bim4You → d.velop „Einbehalt- und Kürzungsinformationen, Umlageinformationen“ und „Freigabestatus“. arch_3: „Rechnungen bezüglich Bauprojekte werden an Bim4You zur Bearbeitung übergeben“ (am Schritt *Fachliche Prüfung/Detail-Qualifikation*) → Bim4You „Budget Abgleich“ und „Bearbeitung“ mit „Sonder Buchungsinformationen: ARAP/PARP, Rückstellungen, Anzahlungen“ → d.velop *Fachliche Freigabe* (DATEV-Verbuchung) → *Zahlungsfreigabe* (DATEV-Zahlung). [Quelle: SP/img/arch_2.png, SP/img/arch_3.png]

| Fluss | Deutung | Status |
|---|---|---|
| **d.velop → Bim4You: ER-Journale** | Die in d.velop erfassten und vorqualifizierten **Bau-Eingangsrechnungen** gehen einzeln oder als Journal mit Kopfdaten (Mandant, Kreditor, RE-Nr., Datum, Leistungsdatum, Netto/USt/Brutto), **Projekt, Vergabeeinheit/Vertrag** und Beleglink (Barcode = d.velop-Dok-ID) ins **Rechnungseingangsbuch** von BIM4You. BIM4You kann „Contract Number“ aus E-Rechnungen automatisch zuordnen [Q1] | Annahme (fachlich plausibel, durch [Q1] und [Q7] gestützt) |
| **Bim4You → d.velop: Einbehalt- und Kürzungsinformationen** | Ergebnis der BIM4You-Zahlungsfreigabe: **geprüfter Betrag**, **Abzüge/Einbehalte** (Sicherheits-/Gewährleistungseinbehalt), Nachlass, Vorauszahlungsabzug, ggf. Hinweis auf Bauabzugsteuer → daraus der **Freigabe- bzw. Zahlbetrag** (≠ Rechnungsbrutto). d.velop und DATEV brauchen das für Buchung und Zahlung | Annahme, gestützt durch [Q2–Q4] |
| **Bim4You → d.velop: Umlageinformationen** | **Variante A (wahrscheinlicher):** Aufteilung der Rechnung auf Einheiten, Budgets oder Projekte („Splits aus RE-Verteiler/Einheiten/Budget“ [Q4]) → Kostenstellen/KOST1/KOST2 für DATEV (Katalog 2.8). **Variante B:** Umlagefähigkeit auf Mieter (Betriebskosten), im Baukontext eher unwahrscheinlich. **Hinweis:** In BIM4You hießen bis 2024 auch Forecast-Spalten „Umlage“ [Q2] | **Offen**, im Prozessworkshop klären |
| **Bim4You → d.velop: Freigabestatus** | Status der Rechnungsprüfung (RP1/RP2/RP3), Zahlungsfreigabe (1./2. Freigabe), **Storno**, Sperre; Freigeber und Datum | Annahme, gestützt durch [Q2, 2.5.14–2.5.16], [Q1, 1.3.9] |
| **Sonderbuchungsinfos (ARAP/PARP, Rückstellungen, Anzahlungen)** | Kommen aus BIM4You (Rückstellungen und Vorauszahlungen sind dort geführt [Q6], [Q1]) und gehen nach arch_2 **über d.velop** nach DATEV. Das Format ist offen: Buchungsstapel oder Beleg mit Buchungsanweisung | **Offen** |

**Wichtiger Abgrenzungspunkt (Empfehlung):** BIM4You kann Rechnungen **selbst** als DATEV-Buchungsstapel exportieren (Zusatzlizenz) [Q1, Q2]. Laut Zielarchitektur bucht aber **d.velop** die ER-Journale nach DATEV (arch_2). Deshalb darf für Eingangsrechnungen **genau ein Buchungskanal** aktiv sein, sonst drohen Doppelbuchungen. Empfehlung: Der BIM4You-DATEV-Export bleibt für ER **deaktiviert**; ob er für Sonderbuchungen genutzt wird, ist offen.

### 1.5 Vorschlag Schnittstellendesign d.velop ⇄ BIM4You (Zielbild, Annahme)

**Architekturprinzip:** d.velop Cloud und BIM4You (Windows/SQL, i. d. R. On-Prem oder gehostet) werden über die **MDIS-Middleware** gekoppelt. Gründe: keine dokumentierte BIM4You-API, Cloud-d.velop kann keinen UNC-Ordner beschreiben, und die Middleware hält ohnehin die Stammdaten.

```
smart invoice (Schritt "Vorqualifikation" ─► Verbindung "an Bauprüfung")
   │  integration.export (Webhook: HMAC-signiert, Quittung ≤30 s   |   oder Abhol-API, Fenster ≤28 Tage)
   ▼
MDIS-Middleware ──► BIM4You-Import (E-Rechnung XRechnung/ZUGFeRD mit "Contract Number"
   ▲                 ODER PDF über Scanordner + Metadaten-CSV; Barcode = d.velop-Dok-ID)
   │                         │  Prüfung RP1/RP2(/RP3), Budgetabgleich, Abzüge/Einbehalte, Zahlungsfreigabe
   │◄── Polling (z. B. 15 min): Zahlungsfreigabe-PDF + Freigabedaten (Export/Übergabeordner; DB-Lesen nur mit BIB-Freigabe)
   ▼
d.velop: DMS-API (Eigenschaften der Rechnung aktualisieren, Zahlungsfreigabe-PDF als "Rechnungsanlage" verknüpfen)
       + Rückmeldung an den smart-invoice-Transfer (successful=true → Workflow läuft weiter; false + Meldung DE/EN → Fehlerstelle)
```

| Element | Vorschlag | Beleg / Status |
|---|---|---|
| **Auslöser Hinweg** | Schrittverbindung in smart invoice, z. B. „Vorqualifikation → Bauprüfung“, mit **Exportaktion an Integration „BIM4You“**. Weiche nur für Bau-Rechnungen (Eigenschaft/Kategorie „Bauprojekt“, Projekt-Nr. gefüllt) | Export an Schrittverbindung: Fakt [Q11]; Weichenlogik: Annahme |
| **Datenobjekt Hinweg** | `workflow.voucher`: company.nr, vendor.nr, net/vat/gross_amount, document_date, date_of_supply, external_number, **barcode**, `custom1–20` (Projekt, Vergabeeinheit, Vertrag, Gewerk/Los), line_items; `_links.dmsobject` (Link auf das Dokument) | Felder: Fakt [Q11] |
| **Übergabe an BIM4You** | Bevorzugt **E-Rechnung** (XRechnung/ZUGFeRD) mit Vertragsnummer im Feld „Contract Number“. Bei Papier/PDF baut die Middleware eine EN-16931-konforme XML aus den smart-invoice-Daten oder legt PDF plus Metadaten in den **Scanordner**. Barcode = d.velop-Dok-ID, damit `DMSApiUrl` + Barcode auf das d.velop-Dokument verlinkt | Importwege: Fakt [Q1, Q3, Q2]; XML-Generierung und Barcode-Konvention: Annahme |
| **Rückweg-Auslöser** | 2. (bzw. 3.) Freigabe in BIM4You oder Storno. Die Middleware pollt, weil BIM4You laut öffentlichen Unterlagen keine Webhooks hat. Alternativ ein Infoserver-Job, der die Zahlungsfreigabe-PDF in einen Übergabeordner schreibt | Infoserver/Übergabeordner: Fakt [Q1, Q2]; Polling: Annahme |
| **Datenobjekt Rückweg** | Freigabestatus (RP1/RP2/RP3, Datum, Freigeber), geprüfter Betrag, **Einbehalte/Abzüge (Art, Betrag)**, Nachlass/Skonto, Zahlbetrag, Kostenaufteilung (Splits → KOST), Zahlungsfreigabe-PDF, Sonderbuchungsinfos | Annahme |
| **Schreiben in d.velop** | DMS-API: Eigenschaften am Rechnungsdokument aktualisieren und PDF als verknüpftes Dokument ablegen. Limits beachten: 600 Updates/min je Mandant, `Origin`-Header bei Schreibzugriffen [Q16] | Fakt (API) |
| **Weiterlauf des smart-invoice-Workflows** | **Variante 1 (empfohlen, prüfen):** Hinweg über die **Abhol-API**. Die Middleware meldet den Transfer erst dann als `successful`, wenn BIM4You freigegeben hat. Der Workflow läuft dann automatisch weiter, bei Ablehnung geht der Beleg mit Meldung an die Fehlerstelle. Das Zeitfenster lässt sich auf **bis zu 28 Tage** einstellen; d.velop empfiehlt aber, es „so klein wie möglich“ zu halten [Q11]. **Variante 2:** Hinweg per Webhook mit sofortiger Quittung; der Beleg wartet in einem Schritt „Warten auf BIM4You“, und ein Buchhaltungsbenutzer setzt ihn fort, sobald die Freigabe-PDF und die Eigenschaften sichtbar sind | Transfer-Mechanik: Fakt [Q11]; Eignung: **Offen** |
| **Kritischer Punkt** | Für das **Überschreiben von Beträgen/Kontierung in einem laufenden smart-invoice-Beleg** (z. B. Zahlbetrag nach Einbehalt) ist **kein API-Endpunkt dokumentiert**. Die API umfasst nur Belegexport, Freigabe-/Prüfermatrix, Stammdaten, SharePoint-Mappings und Erkennungsdaten [Q11, Q14, Q15]. Das Beispiel-JSON enthält ein Feld `pay_amount`, beschrieben ist es nicht [Q11] | **Offen, mit d.velop klären** (Technology Partner Management) |
| **Schlüssel** | d.velop `doc_id` (= Barcode in BIM4You) ↔ BIM4You-REB-Datensatz; **Mandant** = DATEV-Mandantennr. ↔ BIM4You-Mandant/Geschäftsstelle; **Kreditor** = DATEV-Kreditornr. je Mandant ↔ BIM4You-Adresse mit mandantenbezogener Kreditorennr. [Q2, 2.2.3] ↔ Konsolidierungsnr. (MDIS-App); **Projekt/Vergabeeinheit/Vertrag** = BIM4You-Nummern | Annahme |
| **Stammdaten BIM4You → smart invoice** | Projekte, Vergabeeinheiten/Gewerke/Lose, Verträge als **`custom_entities`** (Kopffelder) bzw. **`other_dimensions`** (Positionsfelder, hierarchisch über `parent_dimension_type/_id`) je `company_id` in den Stammdaten-Bucket. Damit sind die Felder in smart invoice auswählbar und für die KI-Kontierung nutzbar (Katalog 5.3 „Gewerk/Los“). Optional **Verträge als `purchase_orders`** für einen Abgleich Rechnung ↔ Auftragswert | Endpunkte: Fakt [Q11, Q12]; Nutzung für BIM4You: Annahme |
| **Fehlerhandling** | Idempotenz über `doc_id`; Webhook-Signatur prüfen (HMAC-SHA256, Zeitstempel ±5 min) [Q11]; HTTP 400 mit Meldung DE/EN → Fehlerstelle mit Klartext für den Anwender, HTTP 500 bei technischem Fehler [Q11]; Wiederholung mit Backoff bei 429; Dead-Letter-Queue; **tägliche Abstimmliste** d.velop ↔ BIM4You (Anzahl, Beträge, offene Übergaben); **Storno-Spiegelung** in beide Richtungen (`end_mode = aborted` [Q11] bzw. BIM4You-Storno [Q2]) | API-Verhalten: Fakt; Betriebskonzept: Annahme |
| **Aufwand** | **Mittel bis hoch** (grob 20–40 PT inkl. Tests; ohne BIM4You-Lizenzen). Treiber: fehlende BIM4You-API, Rückweg-Mechanik, Abstimmung mit BIB | **Annahme** (MDIS-intern verifizieren) |

---

## 2. Property Manager (Hausverwaltungen), Katalog 4.1 und 5.4

### 2.1 Ausgangslage (aus dem Transkript)

- Die Property Manager (PM) **buchen selbst**. Livos „übernimmt die Buchhaltungsdaten … über die Schnittstelle“ [C_Transkript, 00:12:46, Christian Weigel]; die Daten „werden in DATEV gebucht“ [00:16:17, André Töpper]; sie kommen „im Monatspaket … zu Trios“ [00:21:57, Tanja Brecht].
- Die Kreditoren aus Hausverwaltungen liegen im **80000er-Kreis**, interne im 70000er-Kreis, bisher **ohne Zusammenführung** [00:17:34, Trius].
- „95 % der Rechnungen, die beim Property Manager landen“, werden dort geprüft, freigegeben und bezahlt [00:15:18, André Töpper]. Über einer Grenze gibt das Asset Management frei [00:20:45, Trius].
- MDIS-Vorschlag: Postfach „Freigabe-Rechnungen“ und reiner Freigabeprozess in d.velop ohne Buchung und Zahlung, danach „E-Mail aus [d.velop] raus mit der formellen Freigabe“ [00:21:26 und 00:22:19, Thomas Groß]. Livos sieht darin Vorteile bei Vollständigkeit und Transparenz [00:22:41, Trius; 00:22:46, Tanja Brecht].
- Die PM „können … immer wieder wechseln“, und Livos hält es für unrealistisch, dass sie Rechnungen in Livos-Systemen erfassen [00:13:02–00:13:11, André Töpper].

### 2.2 Marktüberblick Hausverwaltungs-ERP (DE) mit Schnittstellenbezug

| Produkt | Hersteller | Relevante Schnittstellen (belegt) | Quelle |
|---|---|---|---|
| Wodis Sigma / **Wodis Yuneo** | Aareon | **Aareon Rechnungsportal**: Rechnungsdaten aus E-Rechnung/PDF, „vollständig ins ERP-System integrierter Webservice“; **Mareon**: Handwerkerportal, >50 zertifizierte Schnittstellen | [Q53], [Q54] |
| **RELion** / RELion ONE | Aareon (auf MS Dynamics 365 Business Central) | d.velop listet RELion als Integration | [Q32], [Q60] |
| **Karthago** | Aareon/UTS | „offene API, casavi, DATEV, DMS“; digitaler Rechnungseingang mit KI | [Q57] |
| PowerHaus, axera, wowinex | seit 2024 **Aareon** (Übernahme Haufe-Lexware Real Estate); axera wird nicht weiterentwickelt | d.velop nennt „Aareon PowerHaus“ auf der Branchenseite | [Q59], [Q35] |
| **DOMUS** 1000/4000 bzw. DOMUS ERP | DOMUS Software AG | d.velop listet DOMUS 1000 & 4000 als Integration | [Q32] |
| **iX-Haus** | CREM SOLUTIONS | DATEV-Schnittstelle: **CSV-Export aller Sachkontenbuchungen** (Monatsdateien), in der Premium-Variante **auch Personen-/Kreditoren-/Debitorenstammdaten**; Import von Rechnungs-CSV (GVC 701/709) | [Q55], [Q56] |
| **immoware24** | Immoware24 GmbH | DATEV-Export als CSV mit **Kontenmapping** auf den DATEV-Kontenrahmen, Berater-/Mandantennr., KOST | [Q58] |
| **casavi** (Portal, kein ERP) | casavi GmbH | offene API; d.velop-Partnerlösung (Dokumente teilen) | [Q52], [Q32] |

**Ergebnis:** Den kleinsten gemeinsamen Nenner bilden **DATEV-Buchungsexporte** (CSV/DATEV-Format) und **E-Rechnung**. Die APIs sind produktspezifisch, und bei ~10 wechselnden PM ist eine API-Einzelanbindung nicht wirtschaftlich (Annahme).

### 2.3 Lösungsoptionen

| Option | Beschreibung | Technik (Beleg) | Aufwand | Robust bei PM-Wechsel | Katalog |
|---|---|---|---|---|---|
| **A – Freigabe-Postfach + E-Mail-Rückmeldung** (MDIS-Vorschlag) | PM mailt Rechnungen über dem Schwellwert an ein Livos-Postfach. d.velop importiert sie (Kategorie „PM-Freigaberechnung“), ein process-studio-Workflow ermittelt den Freigeber (Objekt/PM/Betrag über **Entscheidungstabelle**) und gibt ohne Buchung frei oder lehnt ab. Danach geht eine E-Mail mit Entscheidung, Begründung und Link oder gestempeltem PDF an die PM-Adresse | Mailimport: SP/txt/B_06; Entscheidungstabellen und Aufgaben: [Q27]; E-Mail an externe Adressen über **Messaging-API** („external email addresses“, Idempotency-Key) [Q23] oder **Externe Benutzeraufgabe** [Q29], [SP/txt/B_04 Z.135] | niedrig–mittel | hoch | 4.1, 4.2 |
| **B – Portal / externe Benutzeraufgabe** | Statt E-Mail lädt der PM über ein **Formular** hoch (Pflichtfelder Objekt, PM-Kreditornr., Betrag, RE-Nr.). Rückfragen laufen als **externe Benutzeraufgabe** (E-Mail mit Formularlink, schreibt in den Prozess zurück). Technisch kann ein Prozess auch **ohne Authentifizierung** gestartet werden | Externe Benutzeraufgabe: [Q29]; `POST /anonymous/processes/{processId}/instances`: [Q21]; externe Benutzeraufgabe braucht Formular und Timer [SP/txt/B_04 Z.135] | mittel | hoch | 4.1, 4.2, 4.3 |
| **C – Import der PM-Buchungsdaten (DATEV-Format)** | Die ohnehin monatlich gelieferten Buchungsdaten (DATEV-Buchungsstapel, ggf. Kreditorenstamm) gehen **zusätzlich** in die MDIS-Middleware: (1) Mapping der **80000er-Kreditoren** auf Konsolidierungsnummern; (2) **Vollständigkeitsabgleich**, ob jede gebuchte Rechnung über dem Schwellwert eine Freigabe aus Option A hat; (3) BI-Auswertung | DATEV-Format: Buchungsstapel (Datenkategorie 21) und Debitoren/Kreditoren (16) [Q63]; PM-seitige Exporte [Q55], [Q58] | mittel | hoch (Format stabil) | 4.1, 5.4 |
| **D – Standardformate vertraglich festlegen** | Im Verwaltervertrag: Lieferung **DATEV-Format** (Buchungsstapel + Stammdaten, Belegbilder) monatlich; Rechnungsweiterleitung als **E-Rechnung**; für Objekt- und Mietdaten perspektivisch **gif-IDA** (XML/XSD-Standard für den Datenaustausch Asset/Property Manager) | gif-IDA: [Q62]; DATEV-Format: [Q63] | niedrig (organisatorisch) | sehr hoch | 4.1, 5.4 |
| **E – Direkte API-Anbindung je PM-ERP** | Bidirektionaler Stammdaten-Sync mit Karthago-API, RELion (BC), casavi-API usw. | [Q57], [Q52] | hoch je PM | niedrig | 5.4 (Folgeprojekt) |
| **Ergänzung zu 4.1 – Weiterleitung eingehender PM-Rechnungen** | Rechnungen für **rein PM-verwaltete Assets**, die bei Livos eingehen, werden nach Klassifizierung (Objekt = PM-verwaltet) **nur archiviert und automatisch an das Rechnungspostfach des PM weitergeleitet**, ohne internen Workflow | process studio (Start nach Import) [Q27] + Messaging-API [Q23]. Anhänge an externe Mails sind in der Messaging-API **nicht dokumentiert** → Link oder SMTP über Skript (Annahme) | niedrig | hoch | 4.1 |

**Empfehlung (Annahme, fachlich begründet):** **A + C als Zielbild**, **D** als organisatorische Flankierung, **B** optional für „Kern-PM“ (4.3). **E** nur als Folgeprojekt, falls sich einzelne PM-Systeme dauerhaft durchsetzen.
Begründung: A und C setzen auf Abläufe auf, die Livos und die PM heute schon haben (E-Mail, Monatspaket DATEV). Beide überstehen einen PM-Wechsel ohne Neuentwicklung und liefern Transparenz und Vollständigkeit, wie es das Transkript fordert.

**5.4 realistisch zugeschnitten:** eine **einseitige** Übernahme der PM-Kreditoren (aus dem DATEV-Format oder CSV) in die MDIS-Lieferanten-App. Einen Rückschreib-Sync in die PM-Systeme gibt es vorerst nicht, entsprechend der Katalognotiz „konkrete Synchronisation wäre ein Folgeprojekt“.

---

## 3. d.velop-APIs und Integration

### 3.1 API-Überblick (Cloud)

| API / App | Zweck | Auth / Besonderheiten | Limits | Quelle |
|---|---|---|---|---|
| **Identity Provider** | Login, Validierung, App-Sessions | **API-Key im Header `Authorization: Bearer`** → Login liefert `AuthSessionId` + `Expire`; alternativ Basic-Login mit API-Key als Passwort. **Impersonation-Session 30 min** (nach Admin-Freigabe „Manage app trusts“); `/validate` mit Cache-Hinweis (MaxAge) | – | [Q17] |
| API-Key-Erzeugung | Konfiguration → Anmeldung → Einstellungen → Fingerabdruck → „+“ → Service-User wählen | Pro Integration einen eigenen technischen Benutzer mit minimalen Rechten (Annahme, Best Practice) | – | [Q30] |
| **DMS-API** (`/dms`) | Dokumente/Akten anlegen, ändern, suchen; Mappings; Upload | REST, HAL+JSON; Bearer; **`Origin`-Header bei POST/PUT/PATCH/DELETE Pflicht** (sonst 403) | **600 Updates/min**, **1.600 Neuanlagen/min** je Mandant (Cloud) → **HTTP 429** | [Q16] |
| **DMS-Webhooks** (Repository) | Ereignisse vor/nach Suche, Import („Ablagedialog überprüfen“, Vor/Nach Erstellen), neue Version, **Eigenschaften überprüfen/aktualisieren**, Löschen, Verknüpfen, **Statuswechsel**, Freigabe, generiertes Dokument; **dynamische Wertemenge** | „Vor“-Ereignisse können Eigenschaften in der Response ändern (Validierung/Anreicherung). Header neu `Authorization: Bearer APIKEY` | Wertemengen-Webhook: konfigurierbarer Timeout, **max. 3 Versuche** | [Q18], [Q19] |
| **smart invoice-API** | Belegexport (Transfers), Freigabe-/Prüfermatrix, **Stammdaten-Buckets**, Erkennungsdaten, SharePoint-Mappings | Webhook-Signatur `X-Smart-Invoice-Signature` (HMAC-SHA256), Quittung ≤30 s; Abhol-API mit `integration_key` (kein Auth-Merkmal), Fenster 2 Tage (bis 28 Tage) | Batch-Stammdaten asynchron (Job-ID); **Einzel-PUT synchron mit Rate Limit (429)**, „ausschließlich im Rahmen einer Anwendungsinteraktion“ | [Q11–Q15] |
| **Task-API** (`/task`) | Aufgaben anlegen, ändern, abschließen, weiterleiten, **suchen** | Suche über alle Aufgaben mit Rolle „Service user“ | `retentionTime` **Standard 30 Tage, 0–365**; 429 | [Q20] |
| **Process-API** (`/process`) | Prozesse starten (auch **anonym**), Instanzen suchen (`startTime`, `endTime`, `state`), Tokens suchen, externe Services | Suche mit Rolle Process-Editor/-Administrator | siehe process studio | [Q21] |
| **Actions-API** (`/actions`) | Zentrale Registry für Aktionen und **Events**, Trigger/„Routinen“, synchrone und **asynchrone Aktionen (202 + Callback-URL)**, dynamische Wertemengen | CloudEvents-Header beim Senden von Events | – | [Q22] |
| **Messaging-API v2** | E-Mails an Benutzer, Gruppen, **externe Adressen**; Nachrichtentypen; **Idempotency-Key** | On-Prem braucht SMTP-Konfiguration; Anhänge nicht dokumentiert | – | [Q23] |
| **Inbound-API** | Importprozesse (Blob-Upload, Eigenschaften, Kategorien) | – | – | [Q24] |
| **Power Platform-Konnektor** | Aktionen: Dokument ablegen/aktualisieren, Akte anlegen/aktualisieren, Aktion ausführen; Trigger „d.velop event (Webhook)“ | API-Key; zusätzlich „Trusted App“ unter `/integrationplatform/config` | **100 Calls / 60 s je Verbindung** | [Q30] |
| **process studio** | BPMN, Formulare, **Entscheidungstabellen**, Scripting (Node.js mit npm-Bibliotheken), Aufgaben, Monitoring; „Alle Werkzeuge verfügen über eine … REST-API“; REST-APIs für „individuelle Berichterstattung und Analyse“ | Business: **1.000 Workflowausführungen je produktivem Mandanten/Monat** (Cloud/Hybrid) | Skripte: 100.000/Tag, 10 gleichzeitig synchron, 55 s synchron / 14 min asynchron, Payload 100 MB; 1.000 neue Aufgaben/min; Aufgabenaufbewahrung 365 Tage | [Q26], [Q27] |

**Auswirkung auf Livos:** Bei 5.000–8.000 Belegen pro Jahr (≈ 420–670 pro Monat) passt ein **process-studio-Workflow je Beleg** in das Kontingent von 1.000 Ausführungen im Monat. Kommen PM-Freigaben, Verträge, Post und Rückweisungen dazu, wird es **eng** (Annahme). Ob smart-invoice-Workflows auf dieses Kontingent zählen, ist **offen**. Die Leistungsbeschreibung nennt nur „Process Studio-Services“ [Q26].

### 3.2 „d.velop connect“-Produkte und Integrationsplattformen

- Integrationswege laut d.velop: standardisierte Schnittstellen, Apps der Plattform, offene REST-API, **über 500 Konnektoren**; namentlich DMS-API, invoices-API, inbound-API; als iPaaS wird **nur Microsoft Power Automate** genannt [Q31].
- Die Integrationsübersicht listet u. a. **DATEV** (mehrere Varianten), **Casavi, RELion, DOMUS 1000/4000**, **Acumatica, Haufe X360** und **Power BI**. **Nicht** gelistet sind Wodis, iX-Haus, immoware24, Karthago, **evidanza** und **BIM4You** [Q32].
- **DATEV-Anbindung (nur zur Einordnung, Details in der DATEV-Recherche):** Ein Drittanbieterprodukt ist **LDconnect für DATEV Rechnungswesen (LIONDEER)**. Es lädt **täglich** für alle konfigurierten DATEV-Mandanten Kreditoren, Sachkonten, Steuerschlüssel, Zahlungsbedingungen, Bankverbindungen, KOST1/KOST2 in die smart-invoice-**Buckets** und übergibt Buchungsvorschläge. Voraussetzungen: **DATEVconnect**, DATEV-Server **aus dem Internet erreichbar** oder LIONDEER-**Datengateway** auf dem DATEV-Server [Q33, Q34]. Für Livos ist das kritisch, weil DATEV bei einem externen Dienstleister läuft (Briefing).
- `d.velop connect for Microsoft Dynamics 365` synchronisiert Stammdaten stündlich, Sachkonten täglich [SP/txt/B_02 Z.429].

### 3.3 Anbindung der MDIS-Middleware (Lieferanten-Stammdaten-App, Kreditorenkonsolidierung): Zielbild

| Baustein | Vorschlag | Beleg / Status |
|---|---|---|
| **Führende Daten** | DATEV je Mandant bleibt führend für Kreditorennummern (70000er intern, 80000er PM). Die **MDIS-App** führt den **Golden Record** mit **Konsolidierungsnummer** und Mapping-Tabelle `Konsolidierungsnr ↔ (DATEV-Mandant, Kreditornr) ↔ (PM, PM-Kreditornr)` | Transkript [00:11:00, 00:18:01, Thomas Groß]; Design: Annahme |
| **Mandantenstamm → smart invoice** | `companies/batch`: `id` = DATEV-Mandantennr., `name`/`address` **so wie auf Rechnungen** (wichtig für die automatische Mandantenermittlung), `parent_id` für die Konzernstruktur, `local_currency`, `country` | Fakt [Q11], [Q12] (Katalog 1.1, 2.2) |
| **Kreditoren → smart invoice** | `vendors/batch` **je company_id** (ID muss je Mandant eindeutig sein): `id` = **DATEV-Kreditornr.** (für die Buchung nötig), `vat_id` („wichtig für die automatische Erkennung“), E-Mail, Zahlungsbedingung; `vendor_bank_accounts` (IBAN, `primary`) für den **IBAN-Abgleich** | Fakt [Q11] (Kundenfrage IBAN [00:24:42, André Töpper]) |
| **Konsolidierungsnummer** | Das Kreditorobjekt in smart invoice hat **kein freies Feld** [Q11]. Deshalb: (a) Konsolidierungsnr. als DMS-Eigenschaft „Lieferant (konsolidiert)“ am Beleg, gesetzt per DMS-Webhook „Ablagedialog überprüfen / Vor dem Aktualisieren“ oder per Skript-Lookup; (b) optional als `custom_entities` (Typ „konsolidierung“) für ein Kopffeld | Webhook-Mechanik: Fakt [Q18]; Einsatz: Annahme |
| **Wertemengen in d.velop documents** | Gesellschaft, Kreditor (konsolidiert), Objekt/Projekt als **dynamische Wertemengen per Webhook** aus der Middleware (API-Key, Timeout, 3 Versuche) statt manueller Pflege | Fakt [Q18], [Q19] |
| **Akten** | Gesellschafts-, Kreditoren- und Objektakten legt die Middleware per DMS-API an bzw. aktualisiert sie (Limits beachten) | [Q16] |
| **Sync-Muster** | **Nächtlicher Delta-Batch** (asynchron, Job-Status pollen `masterdata/import_jobs/{id}`); **Einzel-PUT** nur bei Neuanlage aus einer Benutzerinteraktion (Rate Limit) | Fakt [Q11] |
| **Ein Schreiber je Bucket** | Wenn LDconnect oder ein d.velop-DATEV-Konnektor die Buckets täglich füllt, **darf die Middleware nicht dieselben Entitäten überschreiben**. Also entweder ist die Middleware **der einzige Schreiber** (liest DATEV selbst), oder sie schreibt nur ergänzende Entitäten (custom_entities, other_dimensions für BIM4You-Projekte) | LDconnect-Verhalten: Fakt [Q33]; Regel: Annahme; **Offen** |
| **Ereignisse zurück an die Middleware** | Unbekannter Kreditor bzw. Mandant (Katalog 2.3), Rückweisung mit 5 Standardgründen → **E-Mail an den Lieferanten**: smart-invoice-Export an der Rückweisungsverbindung oder DMS-Webhook „Nach Statuswechsel“ → Middleware → Messaging-API (externe Adresse) | Fakt [Q11], [Q18], [Q23]; Umsetzung: Annahme |
| **Sicherheit/Betrieb** | Technischer Benutzer je Integration, API-Key im Secret-Store, Rotation; Signaturprüfung; Backoff bei 429; Monitoring und Alerting (MDIS-Middleware bietet „Error detection, logging, and alerts“ [Q47]) | Annahme / [Q47] |

---

## 4. evidanza (BI/Planung)

| Aussage | Status | Quelle |
|---|---|---|
| evidanza GmbH, gegründet 2004, Sitz Straubing, ca. 20–30 Mitarbeiter, >275 Kunden (DACH), seit 2022 eigenständige Tochter der **CSS-Gruppe** | Fakt | [Q36] |
| Umfang: **Business Intelligence, Unternehmensplanung, Business Process Management**; Planung auch für ERP-Systeme und MS Power BI | Fakt | [Q36], [Q39] |
| Architektur: Betrieb mit **Microsoft SQL Server** oder eigener **In-Memory-DB** (relationale DB zur Persistierung) | Fakt | [Q36] |
| Datenanbindung: **data.SYNAPSE**, „mehr als 250 Standard-Connectoren“ (Middleware-Seite: „>200“); „**Rest API basierte Datenkommunikation**“; ETL-Prozesse, workflowbasierte Datenintegration, Monitoring, Python-Integration | Fakt | [Q37], [Q38] |
| DATEV-Standardlösung: „alle relevanten Finanzdaten wie GuV, Kostenstellen und offene Posten automatisch übernommen“. Technischer Weg nicht beschrieben | Fakt / technischer Weg offen | [Q40] |
| **OData** als Quelle oder Ziel | **Nicht belegt** | Offen |
| **Fertiger d.velop-Konnektor** | Nicht belegt: evidanza fehlt in der d.velop-Integrationsübersicht [Q32], d.velop wird auf den evidanza-Seiten nicht genannt | Offen |
| evidanza ist Technologiepartner von MDIS | Fakt | [Q46], [Q50] |

**Empfohlener Weg d.velop → evidanza (Annahme, Katalog 3.2 und 3.3):**
1. **Ereignisprotokoll in Echtzeit:** In smart invoice werden an **allen relevanten Schrittverbindungen** Integrations-Exporte an die Middleware konfiguriert und sofort quittiert. Jeder Export enthält `from_step`/`to_step`, Belegdaten und Positionen mit `verified_by`/`verified_at` [Q11]. Die Middleware schreibt daraus eine Tabelle *Beleg × Schritt × Zeitpunkt × Bearbeiter*. **Offen:** ob viele Exporte je Workflow zulässig sind und die Performance tragen.
2. **Nächtliche Abfragen:** Task-API-Suche (Service-User; Eingang, Abschluss, Bearbeiter) [Q20], Process-API-Instanzsuche (`startTime`/`endTime`/`state`) [Q21], DMS-Suche nach Status-Eigenschaften [Q16]. Weil Aufgabendetails **nach 30 bzw. höchstens 365 Tagen gelöscht** werden [Q20], muss **laufend** extrahiert werden.
3. **Staging in MS SQL** (Middleware-DWH). evidanza bindet diese Tabellen über den SQL-Standardweg an. Kennzahlen wie Liegezeit je Schritt/Benutzer, Durchlaufzeit, Überfälligkeit und Skontoverlust werden dort **berechnet**. Eine Spalte „Liegezeit“ gibt es in d.velop nicht [SP/txt/B_00 Z.712].
4. Aufwand **mittel** (Annahme: 10–20 PT plus evidanza-Modellierung).

---

## 5. Acumatica / Haufe X360 + d.velop („ConnectorX360dvelop“)

| Aussage | Status | Quelle |
|---|---|---|
| Der Acumatica-Snapshot „Mocca“ enthält die Customizations **`AmcsSubSplit.1.0.2, ConnectorX360dvelop.2.3.2`** | Fakt | [SP/mocca/Manifest.xml] |
| Im Snapshot finden sich Screens `DV101000` „d.velop documents Integration“ und `DV503000` „DMS Shipment Sidepanel“, ein OAuth-Client „d.velop documents“ sowie die Features `UsrDvelopDmsIntegration(Business)` | Fakt | [SP/mocca/SiteMap.adb, OAuthClient.adb, FeaturesSet.adb] |
| Assembly `Haufe.PT.Extensions.DMSConnector.dll`, Upgrade-Historie 2.2.0 → 2.3.2; `DmsUrl = mocca360-x360.d-velop.cloud` | Fakt | [SP/work/05_mocca_snapshot.md] |
| **Haufe X360 ist die deutsche Version von Acumatica** | Fakt | [Q43] |
| Partnerschaft Haufe X360 und d.velop, angekündigt am **24.04.2024**: bidirektionale Integration über APIs und Customization in X360; E-Rechnungen (PDF/XRechnung/ZUGFeRD) werden als Eingangsrechnungen in X360 gebucht; DMS-Grundfunktionen und 500 GB für X360-Kunden kostenlos | Fakt | [Q42], [Q41] |
| Entwickler laut Haufe: „Haufe X360 in Zusammenarbeit mit d.velop“ | Fakt | [Q41] |
| Partnerbeschreibung: Status- und Buchungsspiegelung in beiden Systemen, Stammdaten (Kreditoren, Sachkonten, Kostenstellen) per Live-Sync | Fakt (Partnerblog, nicht Hersteller) | [Q44] |
| **MDIS als Hersteller des Connectors** | **Nicht belegt.** Namespace `Haufe.PT` spricht für Haufe als Hersteller. MDIS ist Haufe-X360-Partner und setzt ihn vermutlich ein | Annahme |
| Acumatica-Schnittstellen: vertragsbasierte REST-API (versionierte Endpunkte) und OData-Feeds aus Generic Inquiries | Fakt | [Q45] |

**Relevanz für 5.4 (Annahme):** Der Connector zeigt, **welche Objekte eine ERP-Kopplung** mit d.velop abdeckt: Stammdaten-Sync, Belegübergabe, Status-Spiegelung, Sidepanel/Belegansicht im ERP, Rollen/Kategorien. Übertragbar ist nur das **Muster**. Bei Livos ist DATEV führend, und die PM-Systeme sind nicht Acumatica.

---

## 6. MDIS Consulting (Einordnung, ohne Personendaten)

| Aussage | Quelle |
|---|---|
| MDIS ist Marke bzw. Geschäftsbereich der **Groß Business Group GmbH, Salching**. Zur Gruppe gehören u. a. MDIS, Ga_digital und Gross Immobilien (laut Suchergebnis) | [Q50], [Q46] |
| **Haufe X360 Gold Partner 2026**; Auszeichnungen beim Haufe X360 Summit 2026 (umsatzstärkster Partner, am schnellsten wachsend, Kundenprojekt des Jahres) | [Q46] |
| **MDIS One**: „ERP, Integrationsplattform, Business Intelligence, Dokumentenmanagement, Business Planning und Low-Code-Entwicklung“; Hauptpartner Haufe X360/Acumatica, **d.velop**, **evidanza** | [Q50] |
| Technologiepartner u. a. Microsoft (Power BI, Azure), d.velop, ELO, **BeSync** (Middleware/Business Apps), eGECKO, evidanza, ANKER; Branchen u. a. **Bau & Immobilien** | [Q46] |
| **MDIS Middleware**: „universal integration platform“; REST, SOAP, GraphQL, FTP, SQL, CSV, JSON, XML, Webhooks; Echtzeit-Sync; Cloud, On-Prem, Hybrid; Monitoring/Alerts | [Q47] |
| **MDIS X.One (KI-Plattform)**: G.One (Generierung, z. B. Rechnungsprüfung), A.One (Analyse), S.One (Service), Middleware (Haufe X360 in Echtzeit), App Builder, UI.One | [Q48] |
| DMS-Beratung mit d.velop und ELO; „zahlreiche Standardschnittstellen und REST-APIs“ | [Q49] |
| **d.velop-Partnerstatus:** MDIS nennt d.velop als Technologiepartner. Ein Eintrag im öffentlichen d.velop-Partnerverzeichnis wurde **nicht gefunden** (URL-Proben liefern 404) | **Offen** |

Hinweis: Die process-studio-Leistungsbeschreibung 2023 schränkte Modellierung und Skripting in der Edition „basic“ auf „d.velop selbst oder autorisierte d.velop Partner“ ein [Q28]. In der Fassung 2025 fehlt diese Fußnote [Q26], [Q27]. Das ist für die Frage wichtig, wer Workflows bauen und pflegen darf.

---

## 7. Schnittstellenmatrix

| # | System | Richtung | Datenobjekte | Auslöser | Technik | Aufwand / Komplexität | Katalog |
|---|---|---|---|---|---|---|---|
| B1 | **BIM4You** | d.velop → BIM4You | ER-Kopfdaten (Mandant, Kreditor, Beträge, RE-Nr./-Datum, Leistungsdatum), Projekt, Vergabeeinheit/Vertrag, Gewerk/Los, `doc_id` als Barcode, PDF/XML | smart-invoice-Schrittverbindung „→ Bauprüfung“ (nur Bau-Belege) | smart-invoice-Transfer (Abhol-API oder Webhook) → MDIS-Middleware → BIM4You-E-Rechnungsimport („Contract Number“) oder Scanordner | mittel–hoch | 5.3, 5.2 |
| B2 | **BIM4You** | BIM4You → d.velop | Freigabestatus (RP1–3, 1./2. Freigabe, Storno), geprüfter Betrag, **Einbehalte/Abzüge**, Nachlass, Zahlbetrag, **Kostenaufteilung („Umlage“)**, Zahlungsfreigabe-PDF | Freigabe oder Storno in BIM4You (Polling durch Middleware) | Übergabeordner/Export (DB nur mit BIB-Freigabe) → Middleware → DMS-API (Eigenschaften, Anlage) + Transfer-Rückmeldung `successful` | **hoch** (Rückschreiben in smart invoice nicht dokumentiert) | 5.2, 5.3, 2.8 |
| B3 | **BIM4You** | BIM4You → smart invoice (Stammdaten) | Projekte, Vergabeeinheiten/Lose, Verträge (Nr., Auftragswert) | nächtlich + bei Neuanlage | Stammdaten-API `custom_entities` / `other_dimensions` (hierarchisch), optional `purchase_orders` | mittel | 5.3, 2.5 |
| B4 | **BIM4You** | BIM4You → (d.velop) → DATEV | Sonderbuchungsinfos: ARAP/PARP, Rückstellungen, Anzahlungen | Monatsabschluss / Anlass | **offen**: Buchungsstapel über Middleware oder Beleg mit Buchungsanweisung; BIM4You-DATEV-Export **nicht parallel** für ER | hoch / offen | 5.1, 5.2 |
| P1 | **Property Manager** | PM → d.velop → PM | Rechnung über Schwellwert (PDF/E-Rechnung), Freigabeentscheidung, Begründung | E-Mail an Postfach „Freigabe-Rechnungen“ | d.velop-Mailimport → process-studio-Workflow (Entscheidungstabelle Objekt/PM/Betrag) → Messaging-API bzw. externe Benutzeraufgabe | niedrig–mittel | 4.1, 4.2 |
| P2 | **Property Manager** | Livos-Posteingang → PM | Rechnungen für rein PM-verwaltete Assets | Klassifizierung „Objekt PM-verwaltet“ | Ablage „zur Kenntnis“ + automatische Weiterleitung (E-Mail/Link) | niedrig | 4.1 |
| P3 | **Property Manager** | PM → MDIS-Middleware (→ BI) | DATEV-Buchungsstapel (Kat. 21), Kreditorenstamm (Kat. 16) je Objektgesellschaft | monatlich (bestehendes Monatspaket) | Upload/SFTP/E-Mail → Parser; Mapping 80000er → Konsolidierungsnr.; Abgleich mit P1-Freigaben | mittel | 4.1, 5.4 |
| P4 | **PM-ERP** (RELion, Karthago, casavi …) | bidirektional | Kreditoren, Kontenrahmen | Folgeprojekt | produktspezifische APIs | hoch je PM | 5.4 |
| M1 | **MDIS Lieferanten-App** | Middleware → smart invoice | companies (+`parent_id`), vendors je `company_id`, Bankverbindungen, Zahlungsbedingungen, Sachkonten, KOST | nächtlicher Delta-Batch; Einzel-PUT bei Neuanlage | smart-invoice-Stammdaten-API (Bearer/API-Key; Jobs; 429) | mittel (Konflikt mit LDconnect klären) | 2.2, 2.5, 2.6, 5.4 |
| M2 | **MDIS-Middleware** | Middleware ↔ d.velop documents | Wertemengen Gesellschaft/Kreditor konsolidiert/Objekt; Akten; Konsolidierungsnr. am Beleg | zur Laufzeit (dynamische Wertemenge, Webhook) / nächtlich | DMS-Webhooks, DMS-API | mittel | 1.1, 2.2, 2.3 |
| M3 | **MDIS-Middleware** | d.velop → Middleware → Lieferant | Rückweisung (5 Standardgründe), unbekannter Kreditor/Mandant, Dublette mit Begründung | Schrittverbindung „Rückweisung“ bzw. Statuswechsel | smart-invoice-Export / DMS-Webhook → Messaging-API (externe E-Mail) | mittel | 2.3, (Rückweisung) |
| E1 | **evidanza** | d.velop → Middleware-DWH → evidanza | Ereignisprotokoll (Beleg, Mandant, Schritt von/nach, Zeit, Bearbeiter, Status, Betrag) | Webhook je Schrittwechsel + nächtliche API-Abfragen | smart-invoice-Transfers, Task-/Process-/DMS-API → MS SQL → evidanza | mittel | 3.2, 3.3 |
| D1 | **DATEV** (Verweis) | d.velop ↔ DATEV | ER-Journale, Zahlungsjournale, Zahlungsrückmeldung, Stammdaten | Freigabe / Zahlungsfreigabe / täglich | d.velop-DATEV-Konnektor bzw. LDconnect (DATEVconnect, Datengateway) | mittel–hoch (externer DATEV-Betrieb) | 5.1 |
| Z1 | **Omikron** | d.velop → Omikron | Zahlungsfreigaben | Zahlungsfreigabe | laut Katalog „über BeSync“; **nicht recherchiert** | offen | 5.5 |
| A1 | **ERP (Acumatica/Haufe X360)** | bidirektional | Muster: Stammdaten, Belege, Status | – | ConnectorX360dvelop (Haufe) als Referenz | – (Referenz) | 5.4 |

---

## 8. Offene Punkte

| # | Offener Punkt | Adressat |
|---|---|---|
| 1 | **BIM4You-Schnittstellen:** Gibt es eine (nicht öffentliche) API oder einen Web-Service? Dürfen Dritte in die SQL-DB lesen oder schreiben? Kann die DocuWare-Schnittstelle (Austauschordner + Barcode) auch mit anderen DMS genutzt werden? Welche Lizenzen hat Livos (E-Rechnung, DATEV, DocuWare-Schnittstelle)? | BIB GmbH / Suiteify, Livos |
| 2 | **Betriebsform BIM4You bei Livos** (On-Prem, Hosting, Version) und Erreichbarkeit für die Middleware | Livos-IT |
| 3 | **„Umlageinformationen“:** Kostenaufteilung (Splits auf Einheiten/Budgets → KOST) oder Umlagefähigkeit? | Livos (Prozessworkshop) |
| 4 | **Sonderbuchungsinfos (ARAP/PARP, Rückstellungen, Anzahlungen):** Quelle, Format, Buchungskanal (d.velop oder BIM4You-DATEV-Export) | Livos, Trios |
| 5 | **smart invoice:** Kann ein Fremdsystem Beträge oder Felder eines laufenden Belegs ändern (Zahlbetrag nach Einbehalt, Kontierung aus BIM4You)? Sind lange Transfer-Zeitfenster (bis 28 Tage) für die Bauprüfung zulässig und supportet? | d.velop (Technology Partner Management) |
| 6 | Zählen smart-invoice-Workflows auf das process-studio-Kontingent (**1.000 Ausführungen/Monat**)? Welche Edition braucht Livos? | d.velop / MDIS-Vertrieb |
| 7 | **Ein Schreiber je Bucket:** Füllt LDconnect bzw. der d.velop-DATEV-Konnektor die Kreditoren, oder die MDIS-Middleware? Wie wird die Konsolidierungsnummer am Beleg geführt? | MDIS-Architektur |
| 8 | **DATEV beim externen Dienstleister:** Sind DATEVconnect bzw. Datengateway dort erlaubt? Das entscheidet über Stammdaten-Sync und Buchungsübergabe | Livos, DATEV-Dienstleister |
| 9 | **PM-Freigabe:** Schwellwerte je Objekt/PM, Stammdaten „Objekt ↔ PM ↔ Freigeber“, Form der Rückmeldung (E-Mail mit PDF-Stempel oder Link), Nachweisführung | Livos Asset Management |
| 10 | **PM-Buchungsdaten:** Welches Format liefern die PM heute (DATEV-Format EXTF? Belegbilder?), welche PM-Systeme sind im Einsatz, und liefern sie über Trios? | Livos, Trios |
| 11 | **Externe Benutzer:** Lizenzfrage externe Benutzeraufgabe bzw. anonymer Formularstart (4.2); Sicherheitskonzept für anonyme Formulare | d.velop |
| 12 | **Messaging-API:** Sind Anhänge möglich (Freigabe-PDF an PM oder Lieferanten)? Sonst SMTP über Skript oder Link | d.velop |
| 13 | **evidanza:** Welche Konnektoren sind lizenziert (SQL, REST)? Gibt es ein bestehendes evidanza-Modell bei Livos (Bilanzauswertungen laut Transkript [01:13:26])? | Livos, evidanza, MDIS |
| 14 | **Liegezeit-Protokoll:** Sind viele Integrations-Exporte je smart-invoice-Workflow zulässig (Performance, Fehlerschritt bei Nichtquittierung)? | d.velop |
| 15 | **MDIS-Partnerstatus bei d.velop** (Zertifizierung, Berechtigung für process studio und Store-Apps) | MDIS intern |
| 16 | **Omikron-Anbindung über BeSync (5.5):** nicht Teil dieser Recherche | eigene Recherche |

---

## 9. Quellen

**Web (abgerufen 26.09.2026)**

| ID | Quelle | URL |
|---|---|---|
| Q1 | BIB GmbH: Changelog „BIM4You 2026 – Neues in Client + Web“ (Stand Januar 2026) | https://bibdata.bib-gmbh.de/info/Neues_in_BIM4You_2026.pdf |
| Q2 | BIB GmbH: Changelog „BIM4You 2024“ (Stand Januar 2025) | https://bibdata.bib-gmbh.de/info/Neues_in_BIM4You_2024.pdf |
| Q3 | BIB GmbH: Changelog „BIM4You 2023“ (Stand Juli 2023) | https://bibdata.bib-gmbh.de/info/Neues_in_BIM4You_2023.pdf |
| Q4 | BIB GmbH: Changelog „BIM4You 2022“ (Stand September 2022) | https://bibdata.bib-gmbh.de/info/Neues_in_BIM4You_2022.pdf |
| Q5 | Wikipedia: Bim4you | https://de.wikipedia.org/wiki/Bim4you |
| Q6 | BRZ-Akademie: BIM4You Budget-Controlling | https://shop-akademie.brz.eu/products/bim4you-budget-controlling |
| Q7 | DocuWare Case Study Krieger + Schramm | https://start.docuware.com/de/case-studies/krieger-schramm |
| Q8 | Computer Spezial 01/2019: Kostensicherheit in jeder Bauphase | https://www.computer-spezial.de/artikel/kostensicherheit-in-jeder-bauphase-3337544.html |
| Q9 | Suiteify: BIM (Weiterleitungsziel von bib-gmbh.de / brz.eu/…/bim4you) | https://www.suiteify.com/loesungen/erp/bau-erp/bim |
| Q10 | Suiteify: „Aus Infoniqa wird Suiteify“ (15.09.2026) | https://www.suiteify.com/news/aus-infoniqa-wird-suiteify-softwareanbieter-baut-vollstandig-integrierte-business-suite-fur-den-mittelstand |
| Q11 | d.velop: smart invoice-API (PDF, Cloud) | https://help.d-velop.de/docs/api/documentations/de/smart-invoice-developer/cloud/pdf |
| Q12 | d.velop: Übertragen von Stammdaten (smart invoice) | https://help.d-velop.de/docs/de/pub/smart-invoice-developer/cloud/verwenden-der-api-funktionen/ubertragen-von-stammdaten-dvelop-smart-invoice |
| Q13 | d.velop: Empfangen von Belegdaten (smart invoice) | https://help.d-velop.de/docs/de/pub/smart-invoice-developer/cloud/verwenden-der-api-funktionen/empfangen-von-belegdaten-dvelop-smart-invoice |
| Q14 | d.velop: Funktionsumfang smart invoice-API | https://help.d-velop.de/docs/de/pub/smart-invoice-developer/cloud/basisinformationen/funktionsumfang-von-dvelop-smart-invoice |
| Q15 | d.velop: Übertragen von Daten aus der Erkennung | https://help.d-velop.de/docs/de/pub/smart-invoice-developer/cloud/verwenden-der-api-funktionen/ubertragen-von-daten-aus-der-erkennung |
| Q16 | d.velop: DMSApp OpenAPI (Limits, Auth, Origin) | https://help.d-velop.de/dev/api/openapi/dms-app (Doku: https://help.d-velop.de/dev/documentation/dms-app) |
| Q17 | d.velop: Identityprovider API (OpenAPI) | https://help.d-velop.de/dev/api/openapi/identityprovider |
| Q18 | d.velop: DMS Webhooks (Implementierung von Webhooks in d.3-Repositorys) | https://help.d-velop.de/dev/documentation/d3-server-webhook |
| Q19 | d.velop: Wertemengen-Webhooks (Admin 2023.q3) | https://help.d-velop.de/docs/de/pub/admin/2023.q3/administration/wertemengen-webhooks |
| Q20 | d.velop: Task-App API (OpenAPI) | https://help.d-velop.de/dev/api/openapi/decs-task |
| Q21 | d.velop: Process-App API (OpenAPI) | https://help.d-velop.de/dev/api/openapi/dvelop-process |
| Q22 | d.velop: Actions API (OpenAPI) | https://help.d-velop.de/dev/api/openapi/dvelop-actions |
| Q23 | d.velop: Messaging API v2 (OpenAPI) | https://help.d-velop.de/dev/api/openapi/messaging |
| Q24 | d.velop: Inbound API (OpenAPI) | https://help.d-velop.de/dev/api/openapi/dvelop-inbound-scan |
| Q25 | d.velop: API-Übersicht | https://help.d-velop.de/dev/documentation |
| Q26 | d.velop: Leistungsbeschreibung process studio (Version 2025-11-04) | https://s3.eu-central-1.amazonaws.com/mediamanager.cloudcenter.service.d-velop.cloud/adadb5ed-d2b9-49b5-88a2-69b49b6eeaf4 |
| Q27 | d.velop: Funktionsbeschreibung process studio (D010631279/2025-10-29) | https://my.d-velop.cloud/center/a/processstudiobusiness/legal/funktionsbeschreibung?language=de (→ https://s3.eu-central-1.amazonaws.com/mediamanager.cloudcenter.service.d-velop.cloud/153fd738-4a10-4e15-b4d9-c20c87595b9e) |
| Q28 | d.velop: Leistungsbeschreibung process studio (Version 2023-11-29) | https://s3.eu-central-1.amazonaws.com/mediamanager.cloudcenter.service.d-velop.cloud/48affd42-32cd-4def-a73d-38b79e00b616 |
| Q29 | d.velop: process studio Produktseite (externe Benutzeraufgaben) | https://www.d-velop.de/software/prozessmanagement-software |
| Q30 | Microsoft Learn: d.velop Connector (Power Platform) | https://learn.microsoft.com/en-us/connectors/dvelop/ |
| Q31 | d.velop: Integrationen | https://www.d-velop.de/software/integrationen |
| Q32 | d.velop: Übersicht Integrationen & Konnektoren | https://www.d-velop.de/software/integrationen/uebersicht |
| Q33 | LIONDEER: Leistungsschein LDconnect für DATEV Rechnungswesen (Cloud), Stand 11/2025 | https://s3.eu-central-1.amazonaws.com/mediamanager.cloudcenter.service.d-velop.cloud/82f418b4-8a85-4687-a9ff-53f938f690a3 |
| Q34 | d.velop Store: LDconnect für DATEV Rechnungswesen | https://www.d-velop.de/store/liondeer-ldconnect-datev-rechnungswesen |
| Q35 | d.velop: Branche Wohnungswirtschaft | https://www.d-velop.de/branchen/wohnungswirtschaft |
| Q36 | BARC: evidanza Reviews | https://barc.com/de/review/evidanza/ |
| Q37 | evidanza: Daten-Management | https://evidanza.de/fachthemen/daten-management/ |
| Q38 | evidanza: data.SYNAPSE Middleware | https://evidanza.de/produkte/synapse/middleware/ |
| Q39 | evidanza: Produkte | https://evidanza.de/produkte/ |
| Q40 | evidanza: Standardlösung DATEV | https://evidanza.de/produkte/standardloesungen/datev/ |
| Q41 | Haufe X360: Schnittstelle d.velop DMS | https://www.haufe-x360.de/schnittstellen/schnittstellen-detail/dvelop-dms |
| Q42 | d.velop Presse: Partnerschaft Haufe X360 (24.04.2024) | https://www.d-velop.de/presse/partnerschaft-haufe-x360 |
| Q43 | Haufe X360: Acumatica | https://www.haufe-x360.de/acumatica |
| Q44 | S+S SoftwarePartner: Haufe X360 – d.velop-Schnittstelle | https://www.softwarepartner.net/blog/haufe-x360-d-velop-schnittstelle-xrechnung-zugferd-peppol |
| Q45 | Acumatica Blog: Web Services, REST API, OData | https://www.acumatica.com/blog/acumatica-web-services-rest-api-odata-and-integration-best-practices/ |
| Q46 | MDIS (EN) | https://mdis-consulting.de/en/ |
| Q47 | MDIS: Middleware | https://mdis-consulting.de/en/solutions/middleware/ |
| Q48 | MDIS: Haufe X360 meets MDIS X.One | https://mdis-consulting.de/ihr-erp-kann-mehr-als-es-heute-zeigt/ |
| Q49 | MDIS: DMS | https://mdis-consulting.de/loesungen/dms/ |
| Q50 | Groß Business Group: MDIS | https://gross-businessgroup.de/mdis/ |
| Q52 | casavi: Partnerlösung d.velop | https://casavi.com/de/partnerloesungen/dvelop/ |
| Q53 | Aareon: Rechnungsportal | https://www.aareon.de/aareon-rechnungsportal |
| Q54 | Aareon: Mareon | https://www.aareon.de/mareon |
| Q55 | CREM SOLUTIONS iX-Wiki: DATEV-Schnittstelle | https://wiki.crem-solutions.de/Version.20.23.1/doku.php?id=schnittstellen%3Adatev_schnittstelle%3Astart |
| Q56 | CREM SOLUTIONS: iX-Haus | https://www.crem-solutions.de/softwareloesungen/ix-haus/ |
| Q57 | Aareon: Karthago | https://www.aareon.de/immomanagement/karthago |
| Q58 | Immoware24: DATEV-Schnittstelle | https://www.immoware24.de/funktionen/datev/ |
| Q59 | Immobilien Zeitung: Axera, Wowinex und Powerhaus gehören jetzt zu Aareon | https://www.iz.de/innovationen/news/-axera-wowinex-und-powerhaus-gehoeren-jetzt-zu-aareon-2000026282 |
| Q60 | Aareon: RELion ONE | https://www.aareon.de/relion-one |
| Q62 | gif e. V.: Richtlinie Immobilien-Daten-Austausch (gif-IDA) | https://zgif.org/en/ ; https://gif-ev.com/datenmanagement/ |
| Q63 | DATEV Developer: DATEV-Format – Buchungsstapel | https://developer.datev.de/de/file-format/details/datev-format/format-description/booking-batch |

**Lokale Quellen:** `SP/img/arch_2.png`, `SP/img/arch_3.png` (Zielarchitektur); `SP/txt/C_Transkript_Livos_Demo.txt` (Zeitstempel wie zitiert); `SP/txt/A_Leistungskatalog_Rechnungsmanagement_xlsx.txt` (Katalog 1.1–6.1); `SP/txt/B_00_BEFUNDE_konsolidiert.md`, `B_02_Eingangsrechnungen_smart_invoice.md`, `B_04_Workflows_process_studio.md`, `B_06_Postverteilung_Mailimport.md`; `SP/work/05_mocca_snapshot.md`; `SP/mocca/Manifest.xml`, `SiteMap.adb`, `OAuthClient.adb`, `FeaturesSet.adb`. Rohdaten der Web-Recherche: `SP/web/` (Changelog- und API-Volltexte `bim_20xx.txt`, `si_api.txt`, `spec_*.txt`, `ps_*.txt`, `ldconnect.txt`).
