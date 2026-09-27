# 05 – ERP-Snapshot „Mocca_V14_108“: Einordnung und Relevanz für das Livos-DMS-Konzept

**Methode:** Die 527 `.adb`-Dateien sind binäre Acumatica-Snapshot-Tabellen: ein Header `ADB3`, das Tabellenschema als XML und danach die Datensätze im Binärformat. Ich habe die Dateien mit einem eigenen Python-Parser gelesen (`work/mocca_tmp/adb.py`). Alle 525 übrigen Tabellen ließen sich fehlerfrei lesen, darunter einige leere Wiki-Tabellen. `LoginTrace.adb` habe ich bewusst ausgelassen und nur per grep nach Maskenkennungen durchsucht. Personenbezogene Daten sind nur **aggregiert** wiedergegeben. „Aktiv“ heißt: `DeletedDatabaseRecord = 0`.

---

## 1 Was ist das? (Fakten)

| Merkmal | Befund | Quelle |
|---|---|---|
| System | Acumatica-basiertes ERP, Build 14.108.0000.149, Snapshot „Firma_2026-05-15_07-27“ (Beschreibung „Mai2026“, exportMode „Full“) | Manifest.xml |
| ERP-Produkt | **Haufe X360.** Belegt durch den Namespace `Haufe.PT.Extensions.*`, das Theme „X360“, die Mandantenvorlage `standard-de`/SKR04, 12 von 13 Benutzer-E-Mails auf den Domains haufe-lexware.com bzw. haufe-x360.de und die Importszenarien `lex2lexbizz_op*` | SYMapping, PreferencesGeneral, PTTenantInfo, Users (aggregiert) |
| Customizations | `ConnectorX360dvelop.2.3.2` (Assembly `Haufe.PT.Extensions.DMSConnector.dll`, Upgrade-Historie 2.2.0 → 2.3.0 → 2.3.1 → 2.3.2) und `AmcsSubSplit.1.0.2` (Kostenaufteilung nach Subaccount, Felder `UsrIsSplit*` in APTran/POLine; in keinem Datensatz genutzt) | UploadFile, APTran |
| Extern | Haufe X360 basiert auf Acumatica. Haufe und d.velop sind seit 04/2024 Partner; laut Haufe bekommen X360-Kunden die DMS-Kernfunktionen und 500 GB Speicher kostenlos. MDIS ist Haufe-X360-Gold-Partner | Web (siehe Quellenliste unten) |

## 2 Gesellschaften: Demofirma, nicht Livos

- **Fakt:** Der Snapshot enthält **1** Mandanten („Firma“, Schlüssel „Produktiv“, SKR04), **1** Organisation **„Mocca360 GmbH“** (Typ *WithoutBranches*) und **1** Branch (`G000000001`). Dazu kommen 2 Ledger: „Hauptbuch“ (Ist) und „Kostenrechnung“ (statistisch). [Quelle: Company.adb, Organization.adb, Branch.adb, Ledger.adb]
- **Fakt:** In BAccount stehen 105 Geschäftspartner: 61 Kunden, 38 Lieferanten, 5 Mitarbeiter und 1 Organisation. [Quelle: BAccount.adb]
- **Fakt:** Das Branchenprofil ist eine Demofirma für Kaffeemaschinen: Artikel wie Mahlwerke, Entsafter und Bedieneinheiten, das Projekt „Kaffeemaschine“ und Anlagen-Importdateien mit dem Namen „…MoccaX360.xlsx“. [Quelle: InventoryItem.adb, Contract.adb, UploadFile.adb]
- **Fakt:** Die Suche nach „Livos“ liefert **0 Treffer**. Es gibt keine Bau- oder Immobiliendaten und keine Objekte. Dem stehen bei Livos über 100 Gesellschaften gegenüber. → Der Snapshot ist eine **Fremd- bzw. Demofirma**, kein Livos-Datenbestand.

## 3 d.velop-Connector: das ist eingerichtet

| Bereich | Befund | Quelle |
|---|---|---|
| Verbindung | `DmsUrl = https://mocca360-x360.d-velop.cloud`. Repository-ID und Reader-ID sind gesetzt. **Das ist nicht** die MDIS-Demo-Instanz `mdisconsulting.d-velop.cloud`. | DmsConfiguration.adb |
| Funktionsschalter (alle = 1) | **ERP → DMS:** InvoiceExport, QuoteExport, SalesOrderExport, ShipmentExport, BillExport, VendorBaseData, PurchaseOrderBaseData, UserExport. **DMS → ERP:** BillImport, BillWithOrderImport, VendorImport, RoleImport. **Beidseitig:** GroupSync | DmsConfiguration.adb |
| Aktivierung | Features `UsrDvelopDmsIntegration` und `…Business` am **08.08.2025** eingeschaltet | FeaturesSet.adb, AuditHistory.adb |
| Masken | DV101000 „d.velop documents Integration“, DV301000 „DMS Suche“, DV302000 „DMS Übersicht“, DV303000 „DMS Import“, DV304000 „DMS Rechnungsleser“, DV504000 „DMS Outgoing Invoice“ sowie Sidepanels für Eingangsrechnung, Angebot, Auftrag, Lieferschein und Ausgangsrechnung. Die Sidepanels sind 5 Dashboards mit iFrame-Widgets. Dazu kommt ein Workspace „DMS“. | SiteMap, Dashboard, Widget, MUIWorkspace |
| Berechtigungen | 16 Rollen `[X360-DMS] <Kategorie> – Lese-/Schreibzugriff` für **8 DMS-Kategorien**: Angebot, Auftrag, Auftragsbestätigung, Kontaktakte, Lieferschein, Rechnung/Gutschrift, Schriftwechsel/E-Mail, Vertrag. Diese Rollen sind 2 von 13 Benutzern zugeordnet. | Roles, UsersInRoles (aggregiert) |
| SSO/API | OAuth-Client „d.velop documents“ (Flow *AuthorizationCode*, Lebensdauer 30 Tage), Redirect auf `openidgateway.service.d-velop.cloud/openidcallback` | OAuthClient, OAuthClientRedirectUri |
| Nutzung | In LoginTrace kommen DMS-Maskenkennungen etwa 29-mal vor (nur per grep gezählt). **Keine** AP-Rechnung wurde über eine DV-Maske angelegt. An genau 1 AP-Beleg hängen Anlagen (1 PDF und 1 XML, eine Test-E-Rechnung). | LoginTrace (grep), APRegister, NoteDoc |

- **Annahme:** Die Kategorie-Zuordnungen und die Ablagelogik liegen in der d.velop-Instanz, nicht im ERP. Im Snapshot gibt es keine Mapping-Tabelle und keine Usr-Felder für Dokument-IDs. Wahrscheinlich verknüpft der Connector ERP-Belege und Dokumente über `NoteID` bzw. die Belegnummer.
- **Annahme:** Der OAuth-Client dient der Anmeldung und dem API-Zugriff zwischen d.velop Cloud und X360.

## 4 Genutzte Module und Mengengerüst (aktive Datensätze)

| Modul | Mengengerüst | Bewertung |
|---|---|---|
| GL | 2.941 GLTran, 265 Batches (Module: IN 91, GL 89, AP 49, AR 29, CA 6, FA 1), 1.376 Konten (SKR04), Buchungen 12/2023 bis 03/2026 | genutzt |
| AP/Kreditoren | 111 aktive Belege (104 Rechnungen mit rund 194,8 T€, 7 Zahlungen) bei 23 Lieferanten, 141 Rechnungszeilen. 164 weitere Belege sind als gelöscht markiert. 217 Rechnungen stammen aus einem Import am 27.02.2025 („Import by Scenario“), mit Belegdaten von 10 bis 12/2024 | genutzt (Demo-Umfang) |
| AR | 75 Belege, 59 Kunden | genutzt |
| SO/PO/IN | 36 Verkaufsaufträge, 34 Lieferungen, 47 Bestellungen, 46 Wareneingänge, 115 Artikel, 8 Lager | genutzt |
| FA Anlagen | 49 Anlagen, 118 FA-Buchungen | genutzt |
| PM Projekte | 1 Projekt und 1 Vorlage, 6 Tasks; **kein** AP-Beleg ist einem Projekt zugeordnet | kaum genutzt |
| Manufacturing (AM) | 5 Fertigungsaufträge, 17 Stücklistenpositionen, 97 AM-Buchungen | Demo |
| Field Service (FS) | 2 Serviceaufträge, 1 Termin | Demo |
| Lokalisierung (Haufe „PT“) | DATEV-Export konfiguriert (Berater- und Mandantennummer gesetzt), ELSTER, E-Rechnung eingehend/ausgehend, BANKSapi, EBICS | konfiguriert |

[Quelle: counts.json aus Parser-Lauf; APRegister, APTran, Batch, FeaturesSet, PTCompanySettings]

**Annahme:** Die 217 importierten Rechnungen sind Offene-Posten-Migrationen („lex2lexbizz_opKred“). Mit dem d.velop-Connector haben sie nichts zu tun.

## 5 Kreditoren- und Rechnungsstruktur: Felder für ein DMS-Mapping

| DMS-Eigenschaft (Livos-Demo) | X360/Acumatica-Feld | Befund im Snapshot |
|---|---|---|
| Gesellschaft | `Organization.OrganizationCD` / `BranchID` | 1 Gesellschaft, 1 Branch |
| Kreditor | `BAccount.AcctCD` über `APRegister.VendorID` (+ `VendorLocationID`) | 5-stellig, **70007–70720** (DATEV-übliches 7xxxx-Schema); Klassen INLAND/EU/DRITTLAND/Mitarbeiter; USt-ID nirgends gepflegt |
| ERP-Beleg-ID | `DocType` + `RefNbr` (ER…, ZA…), `NoteID` (GUID) | eindeutiger Link zum DMS-Dokument |
| Rechnungsnummer / -datum | `APInvoice.InvoiceNbr` / `InvoiceDate` (`APRegister.DocDate`) | bei allen 104 Rechnungen gefüllt |
| Fälligkeit / Skonto | `APInvoice.DueDate`, `DiscDate`, `TermsID` | vorhanden |
| Beträge / Steuer | `CuryOrigDocAmt`, `APInvoice.LineTotal`/`TaxTotal`, `APTran.TaxCategoryID`, `TaxZoneID` | vorhanden |
| Sachkonto | `APTran.AccountID` (5400, 5100, 5425, 5900), Kreditorenkonto `APAccountID` = 3300 | vorhanden |
| Kostenstelle | `APSubID` / `APTran.SubID` (Segment „Subaccount (KST)“, 4-stellig: 1000–5000, 0000, 9999) | alle 111 aktiven Belege und alle 141 Zeilen auf „0000“ |
| Objekt / Gewerk | am ehesten `ProjectID` / `TaskID` / `CostCodeID` | **leer** (Annahme zur Zuordnung) |
| Bestellbezug | `APTran.PONbr` / `ReceiptNbr` | 81 von 141 Zeilen haben einen Bestellbezug |
| Status / Periode | `Status` (H/B/N/C/V), `Released`, `FinPeriodID` | Rückmeldung an das DMS möglich |

## 6 Bewertung für Livos

- **Fakt:** Der Snapshot enthält weder Livos-Daten noch die d.velop-Instanz aus dem Livos-Demo-Workshop. Er ist eine **Haufe-X360-Demoumgebung („Mocca360 GmbH“) mit produktiv konfiguriertem d.velop-Connector** und eigener d.velop-Cloud (`mocca360-x360`).
- **Annahme:** Es handelt sich um einen Haufe- bzw. Partner-Demomandanten. Darauf deuten die E-Mail-Domains der Benutzer und die Tatsache, dass MDIS Haufe-X360-Partner ist. MDIS nutzt ihn vermutlich als **Referenz für eine ERP–d.velop-Integration**. Wie der Snapshot in den Livos-Ordner kam, ist **nicht belegt**.
- **Relevanz für das aktuelle Konzept: gering.** Bei Livos ist **DATEV** das führende FiBu-System, dazu kommt Bim4You (Business-Architektur-Folien). Haufe X360 ist bei Livos nicht im Einsatz. Die 1-Gesellschafts-Demo sagt nichts über das Mandantenmodell für mehr als 100 Gesellschaften aus.
- **Relevanz für Katalogpunkt 5.4 bzw. Agenda-Punkt „Offene API und perspektivische ERP-Anbindung“: mittel, als Referenzmuster.** Katalogpunkt 5.4 meint die Synchronisation von Stammdaten (Kreditoren, Kontenrahmen) mit den ERP-Systemen der *externen Property Manager* (Could-Have; laut Katalog ein „Folgeprojekt“). Welche Systeme das sind, ist offen, und der X360-Connector lässt sich nicht direkt übertragen. Er zeigt aber als Blaupause, welche Objekte eine ERP-Anbindung abdecken muss:
  - Kreditoren- und Bestellstammdaten → smart invoice
  - geprüfte Rechnungen DMS → ERP (mit und ohne Bestellbezug)
  - ERP-Belege → DMS-Akte
  - Rollen- und Gruppen-Sync
  - SSO und Sidepanel im ERP

  Diese Punkte eignen sich als Checkliste für ein späteres Schnittstellenkonzept. [Quelle: A_Leistungskatalog_Rechnungsmanagement_xlsx.txt, Zeile 5.4; A_Agenda_Livos_pptx.txt]
- **Fakt (Risiko):** Der Snapshot enthält sensible Daten:
  - 13 Benutzerkonten mit Passwortfeldern
  - OAuth-Secret, Server-Key und Token
  - Passwörter von E-Mail- und BANKSapi-Konten
  - Kontakte und ein Login-Protokoll von 60 MB

  **Empfehlung:** Den Snapshot nicht an Livos weitergeben und ihn aus dem Kundenordner entfernen bzw. dort nicht ablegen.

**Offene Fragen:**
1. Wer hat den Snapshot in den Livos-Ordner gelegt, und zu welchem Zweck: Referenz, Angebot oder Versehen?
2. Soll Haufe X360 für Livos oder für die Property Manager perspektivisch positioniert werden?
3. Wer betreibt `mocca360-x360.d-velop.cloud`, und soll der Connector in einem Folgetermin demonstriert werden?

---

**Web-Quellen (extern, nicht aus Kundendaten):**
- [Haufe X360 – d.velop DMS](https://www.haufe-x360.de/schnittstellen/schnittstellen-detail/dvelop-dms)
- [Haufe X360 und d.velop verkünden Zusammenarbeit](https://www.haufe-x360.de/newsroom/haufe-x360-und-dvelop)
- [d.velop – Partnerschaft Haufe X360](https://www.d-velop.de/presse/partnerschaft-haufe-x360)
- [MDIS im Haufe-X360-Partnerverzeichnis](https://www.haufe-x360.de/partnersuche/partner-detail/gross-business-group-mdis-consulting)
- [MDIS – Haufe X360 Partner](https://mdis-consulting.de/en/)
