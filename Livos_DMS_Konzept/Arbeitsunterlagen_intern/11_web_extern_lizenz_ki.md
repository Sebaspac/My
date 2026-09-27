# 11 — Web-Recherche: Externe Beteiligte, Lizenzmodell, Mandanten, Vier-Augen-Prinzip, KI, Mobile/Outlook, Vertretung, SSO/Hosting

**Projekt:** Livos d.velop DMS-Gesamtkonzept (MDIS Consulting)
**Stand der Recherche:** 26.09.2026 (alle URLs an diesem Tag abgerufen)
**Bezug:** Rechercheaufträge R-05 (Lizenz), R-06 (externe Freigabe), R-08 (Vier-Augen-Prinzip), R-16 (Kopplung smart invoice / process studio) aus `04b_dvelop_faehigkeiten_B.md` §7; Workshop-Agenda (Mandantenmodell, Ad-hoc-Freigabe ohne Lizenz, Lizenz/Mengengerüst); Transkript Demo 22.09.2026.
**Lokale Belegkopien:** Alle zitierten PDFs und Seiten liegen als PDF bzw. extrahierter Text in `SP/work/11_web_quellen/` (Dateinamen in Klammern im Quellenverzeichnis).

**Legende Status**
- **F** = Fakt, belegt (Herstellerquelle, wörtlich oder sinngemäß eng zitiert)
- **E** = belegt mit Einschränkung (ältere Version, nur Suchergebnis-Auszug, Marketingseite, Widerspruch zwischen Quellen)
- **A** = Annahme / MDIS-Ableitung (nicht belegt)
- **O** = offen, zu klären

---

## 0. Quellenverzeichnis (Kürzel W01 … W32)

| ID | Quelle (Version/Stand) | URL | lokale Kopie |
|---|---|---|---|
| W01 | Leistungsbeschreibung d.velop documents platform edition, D010522551/2025-10-16 | https://s3.eu-central-1.amazonaws.com/mediamanager.cloudcenter.service.d-velop.cloud/fe5f22d4-0b44-46d7-aed1-30067e47fe7a | lb_documents_platform_edition.* |
| W02 | Factsheet „d.velop documents platform edition – Leistungspakete im Überblick", Stand 11.12.2025 | https://s3.eu-central-1.amazonaws.com/mediamanager.cloudcenter.service.d-velop.cloud/c334d7ee-1509-47f4-b743-2190b47e2665 | factsheet_platform_edition.*, fs_p3/p6/p7/p8.png |
| W03 | Preise & Pläne d.velop documents platform edition | https://www.d-velop.de/software/dokumentenmanagement-system/preise-plaene | dms_preise.txt |
| W04 | d.velop store, documents platform edition (EN) | https://store.d-velop.com/en/d.velop-documents-platform-edition/10001602-en.3 | store_5afa20.txt |
| W05 | Leistungsbeschreibung d.velop invoices, Version 2025-12-15 | https://my.d-velop.cloud/center/a/dvelopinvoicesmedium/legal/sow?language=de | lb_invoices_2025-12-15.* |
| W06 | Preise & Pläne d.velop invoices / Produktseite Rechnungsverarbeitung | https://www.d-velop.de/software/digitale-rechnungsverarbeitung/funktionsuebersicht-d-velop-invoices ; https://www.d-velop.de/software/digitale-rechnungsverarbeitung | invoices_preise.txt, store_fced1c.txt |
| W07 | Funktionsbeschreibung d.velop documents, D010522543/2025-11-28 | https://s3.eu-central-1.amazonaws.com/mediamanager.cloudcenter.service.d-velop.cloud/00fdd0bf-d698-4e3d-8a46-34c864678fdc | fb_documents_2025-11-28.* |
| W08 | Leistungsbeschreibung d.velop documents (Cloud), 2025-02-18 | https://s3.eu-central-1.amazonaws.com/mediamanager.cloudcenter.service.d-velop.cloud/71677a83-7cdb-4097-bfc1-bec37f37bc07 | lb_documents_cloud_2025-02-18.* |
| W09 | Handbuch „d.velop documents: Anwenden" (Cloud), PDF erzeugt 17.09.2026; HTML-Seite „Teilen von Dokumenten außerhalb Ihrer Organisation" | https://help.d-velop.de/docs/api/documentations/de/documents/cloud/pdf ; https://help.d-velop.de/docs/de/pub/documents/cloud/erste-schritte-beim-teilen-von-dokumenten-mit-anderen-personen/teilen-von-dokumenten-auerhalb-ihrer-organisation | doc_cloud_user.* |
| W10 | Handbuch „d.velop process studio: Anwenden" 2026.q2 | https://help.d-velop.de/docs/api/documentations/de/process-studio-user/2026.q2/pdf | psu.* |
| W11 | Funktionsbeschreibung d.velop process studio, D010631279/2025-10-29 | https://my.d-velop.cloud/center/a/processstudiobusiness/legal/funktionsbeschreibung?language=de | fb_processstudio_2025-10-29.* |
| W12 | Produktseite d.velop process studio | https://www.d-velop.de/software/prozessmanagement-software | – |
| W13 | Handbuch „d.velop smart invoice: Administrieren" (Cloud), PDF erzeugt 23.06.2026 | https://help.d-velop.de/docs/api/documentations/de/smart-invoice-cloud/cloud/pdf | si_cloud.* |
| W14 | „d.velop smart invoice-API" (Cloud) | https://help.d-velop.de/docs/api/documentations/de/smart-invoice-developer/cloud/pdf | si_dev.* |
| W15 | Funktionsbeschreibung d.velop pilot, 2026-09-11/D008667433 | https://my.d-velop.cloud/center/a/inboundgpt/legal/sow?language=de | lb_pilot_current.* |
| W16 | Handbuch „d.velop pilot: Administrieren" 1.0.0 | https://help.d-velop.de/docs/api/documentations/de/pilot-admin/1.0.0/pdf | pilot_admin_de.* |
| W17 | Handbuch „d.velop pilot: Using the application" 1.0.0 | https://help.d-velop.de/docs/api/documentations/en/pilot-user/1.0.0/pdf | pilot_user.* |
| W18 | Leistungsbeschreibung d.velop pilot (LLM), 2023 (historisch) | https://s3.eu-central-1.amazonaws.com/mediamanager.cloudcenter.service.d-velop.cloud/f4f84925-7e60-4f02-8ed3-b34e133faf0b ; …/f5039abd-1798-46e7-adf6-4fdceb69e91e | lb_pilot_a.*, lb_pilot_b.* |
| W19 | d.velop AI – Übersicht und „KI sicher einsetzen" | https://www.d-velop.de/kuenstliche-intelligenz ; https://www.d-velop.de/kuenstliche-intelligenz/ki-sicher-einsetzen | store_pilot.txt |
| W20 | d.velop store, d.velop pilot (LLM) (EN) | https://store.d-velop.com/en/d.velop-pilot-LLM/10003299-en.1 | – |
| W21 | „Festlegungen zur Auftragsverarbeitung", Version 2023-09-12 | https://s3.eu-central-1.amazonaws.com/mediamanager.cloudcenter.service.d-velop.cloud/bb57b0a8-780f-44ae-9475-ab8cea2282be | avv_spec_2023-09-12.* |
| W22 | Leistungsbeschreibung d.velop cloud platform, D003884552/2026-07-28 | https://s3.eu-central-1.amazonaws.com/mediamanager.cloudcenter.service.d-velop.cloud/42f5a2ba-b16d-4e0c-be37-3f0d6d6f6bee | lb_cloudplatform_2026-07-28.* |
| W23 | Leistungsbeschreibung d.velop cloud platform, 2022-04-11 (historisch) | https://s3.eu-central-1.amazonaws.com/mediamanager.cloudcenter.service.d-velop.cloud/f660b553-c39d-42d7-bc40-6f86afa58a23 | lb_cloudplatform_2022.* |
| W24 | Zertifizierungen d.velop | https://www.d-velop.com/certifications | cert.txt |
| W25 | Knowledge Base: OIDC mit Azure AD / Entra ID; Bereitstellung von Benutzern/Gruppen aus Azure AD | https://kb.d-velop.de/s/article/000001933?language=de ; https://kb.d-velop.de/s/article/000001455?language=de ; https://kb.d-velop.de/s/article/000001740?language=de | – (nur Suchergebnis-Auszug, KB-Seite lädt ohne Login nicht) |
| W26 | Usermanagement-App (SCIM 2.0, Einladung per E-Mail) | https://portal.d-velop.de/documentation/usermanagementapp/de | – (Suchergebnis-Auszug) |
| W27 | Developer „Basics" (Tenant/Mandant) | https://help.d-velop.de/dev/getting-started-basics | – (Suchergebnis-Auszug) |
| W28 | d.velop mobile: App Store, Google Play, Leistungsbeschreibung 2022-05-09 | https://apps.apple.com/de/app/d-velop-mobile/id1464693393 ; https://play.google.com/store/apps/details?id=com.dvelop.mobile_ecm_android ; https://s3.eu-central-1.amazonaws.com/mediamanager.cloudcenter.service.d-velop.cloud/a94fdb50-5b53-4a1d-a037-817f78c9041e | lb_mobile_2022.* |
| W29 | Outlook-Integration (Cloud) | https://help.d-velop.de/docs/de/pub/documents-m365/cloud/installieren-und-einrichten-der-microsoft-outlook-integration ; https://help.d-velop.de/docs/de/pub/one-outlook-cloud/cloud/basisinformationen-zur-anwendung-und-zum-handbuch | – |
| W30 | d.ecs userprofile „Konfigurieren des Abwesenheitsstatus" (Version 1.9.0) | https://help.d-velop.de/docs/de/pub/userprofile/latest/erste-schritte/konfigurieren-des-abwesenheitsstatus | – |
| W31 | Preise & Pläne d.velop contracts | https://www.d-velop.de/software/vertragsmanagement/preise-plaene | contracts_preise.txt |
| W32 | d.velop sign for documents (Store) | https://store.d-velop.com/de/d.velop-sign-for-documents/10001827.3 | – (Suchergebnis-Auszug) |

**Hinweis zur Quellenlage:** Leistungs-/Funktionsbeschreibungen (W01, W05, W07, W11, W15, W22) sind Vertragsdokumente und haben Vorrang vor Marketingseiten. Wo sich Quellen widersprechen, ist das ausdrücklich vermerkt.

---

## 1. Externe Beteiligte (Projektsteuerer, Architekten, Property Manager)

### 1.1 Belegte Mechanismen

| Nr | Mechanismus | Belegte Aussage | Lizenz für Externe | Sicherheit | Status | Quelle |
|---|---|---|---|---|---|---|
| X1 | **Externe Benutzeraufgabe** (process studio) | „Eine externe Benutzeraufgabe innerhalb eines Prozesses wird immer an 1-n E-Mail-Adressen versendet. Die versendete E-Mail beinhaltet einen Link auf ein zugehöriges Bearbeitungsformular. Wenn die externe Benutzeraufgabe über das zugehörige Bearbeitungsformular abgeschlossen wurde, läuft der Prozess weiter." E-Mail-Adresse statisch oder per Prozessvariable (Typ Text); Betreff/Sprache einstellbar. | Empfänger ist eine **E-Mail-Adresse, kein Benutzerkonto** → keine Benutzerlizenz dokumentiert. Voraussetzung: process studio (in platform edition **business/ultimate**, business = 1.000 Workflowausführungen/Monat/Mandant) | **Zwingend Timer**: „Nach Ablauf des Timers wird der Prozessschritt abgebrochen und das Formular kann nicht mehr aufgerufen werden." Nur explizit gemappte Prozessdaten sichtbar („granular steuern, welche Informationen außerhalb der Organisation sichtbar sind"). Passwort/MFA für den Link: **nicht dokumentiert**. | F | W10 S. 10, 61–63; W12; W01 §2.2.5 |
| X1a | Wichtige Einschränkung X1 | „Der Zugriff auf Dokumenteninformationen oder auf weitere Services, die eine gültige Anmeldung benötigen, ist **nicht möglich**." → Der Externe sieht im Formular **nicht** das Rechnungsbild aus d.velop documents. | – | – | F | W10 S. 62 |
| X2 | **Extern Teilen** (d.velop documents) | „Um einer Person außerhalb Ihrer Organisation ein Dokument zur Verfügung zu stellen …" → Kontextaktion *Teilen* > *Extern Teilen* > Lesen oder Bearbeiten > Zeitraum > *Teilen*; Link kopieren oder per E-Mail. Bearbeitete Version wird **nicht automatisch** übernommen, sondern vom Teilenden geprüft und übernommen. Vorzeitiges Beenden unter *Geteilte Dokumente*. | „… mit externen Personen teilen, die **keine Lizenz** für d.velop documents besitzen." Funktion „nur in d.velop documents **business**" (Handbuch) bzw. platform edition business/ultimate („Teilen von Dateien per Cloudspeicher-Link", nicht basic). | Gültigkeit „max. **180 Tage**"; automatisches Ende nach Ablauf; manuelles Beenden. Passwortschutz: **nicht dokumentiert**. | F | W09 §1.8.3–1.8.5, §1.9.14; W08 S. 9; W01 §2.2.6 |
| X3 | **Teilen von Rechnungen per Link und E-Mail** (d.velop invoices) | „Teilen von Rechnungen per Link und E-Mail (Einfaches Teilen von Rechnungen mit Externen)" – in allen Betriebsformen enthalten. Eine **Freigabe** durch den Empfänger ist damit **nicht** beschrieben (nur Bereitstellung). | keine | wie X2 (A) | F (Freigabe über diesen Weg: N) | W05 §2.3; W06 |
| X4 | **Freigabeuser** (d.velop invoices) | Pakete Small/Medium/Large/Enterprise: „Anzahl Freigabeuser **beliebig**"; „Freigabeuser haben ein auf ihre Rolle beschränktes Nutzungsrecht in d.velop documents. Vollwertige d.velop documents User müssen bei Bedarf separat erworben werden." Freigabeuser dürfen: Prüfer auswählen, Rechnungen prüfen, Lieferscheine anhängen, Notizen/Kommentare, Annotationen, Positionsdaten ergänzen (nicht: buchen, an FiBu übergeben, Akten verwalten). | Keine Zusatzkosten je Freigabeuser | Normales Cloud-Konto: Anmeldung über d.velop cloud login, 2-Faktor (TOTP), FIDO2 oder eigener IdP (OIDC) | F | W05 §2.1, §2.4; W06; W09 §1.9.15, §1.9.28 |
| X5 | **Externe als reguläre Benutzer** (Kernpartner) | Benutzer können „direkt per E-Mail in die Cloud" eingeladen werden; Selbstregistrierung eines d.velop cloud-Kontos möglich; Berechtigung rollen- und attributbasiert über Kategorie/Eigenschaften (z.B. Gesellschaft). | Rolle Freigabeuser (X4) oder voller documents-User (27/39/55 €/User/Monat, s. §2) | 2FA/FIDO2, SSO via OIDC | F (Einladung: E) | W26 (Auszug); W09; W07 §4.1.6 |
| X6 | **d.velop sign** (Signatur durch Externe) | Externe Unterzeichner werden per E-Mail-Adresse eingeladen und unterschreiben „ohne Kosten und Installation"; Kontingent: platform edition business 50, ultimate 100 fortgeschrittene Siegel/Monat/Mandant; weitere Signaturen kostenpflichtig (Pakete, laut Store-Auszug z.B. 120/360/900 Signaturen/Jahr, 4,50 € je weitere). | keine Benutzerlizenz; Signaturkontingent | eIDAS-Signaturlevel | E (Store-Details nur Suchergebnis-Auszug) | W01 §2.2.2; W32 |
| X7 | **Portalanbindung per API** | „Nutzbarmachung von Dokumenten für Benutzer ohne d.velop documents-Zugang ist zahlungspflichtig" – 7,60 € je 1.000 über die Schnittstelle heruntergeladene Dokumente (Stand LB 2025-02-18). | kostenpflichtig je Download | eigene Portallösung | F | W08 Fußnote 4; W01 §2.2.1 |
| X8 | Gastbenutzer (#EXT#) | Nur für die **SharePoint-Variante** (d.velop documents for Microsoft 365) dokumentiert: Option „Gastbenutzer nicht synchronisieren". Für d.velop cloud (Livos-Szenario) **kein** Gast-Benutzertyp dokumentiert. | – | – | F (Relevanz für Livos: gering) | W13 §1.2.3 |

### 1.2 Bewertung für Livos (Annahmen)

- **A-1:** Eine echte „Freigabe per Link ohne Registrierung" **innerhalb** des smart-invoice-Workflows ist in der öffentlichen Doku **nicht** vorgesehen. Der dokumentierte Weg ist die process-studio-**Externe Benutzeraufgabe** (X1). Sie muss mit dem smart-invoice-Beleg gekoppelt werden (R-16 weiterhin offen): z.B. smart-invoice-Workflow übergibt an einen process-studio-Prozess, der das Rechnungsbild separat bereitstellt (X2-Link als Prozessvariable) und das Ergebnis (Freigabe/Ablehnung + Kommentar) zurückschreibt. **Machbarkeit und API für „Extern teilen" aus einem Prozess: nicht belegt → O-1.**
- **A-2:** Für Property Manager (≈10 Hausverwaltungen) und wiederkehrende Kernpartner ist der **Freigabeuser** (X4) der wirtschaftlich naheliegende Weg: kostenfrei, rollenbeschränkt, mit 2FA. Voraussetzung: Die Lizenzbedingungen erlauben Dritte (Nicht-Mitarbeitende) als Freigabeuser → **O-2**.
- **A-3:** Die im Workshop vorgeschlagene Variante „Freigabe-Postfach für Hausverwalter, Freigabe-Mail zurück" [Transkript 00:21:26–00:22:19, Thomas Groß] ist mit X4 (Asset Management intern als Freigeber) plus einer E-Mail-Rückmeldung (process-studio-Aktion oder Externe Benutzeraufgabe als reine Benachrichtigung) abbildbar; die Hausverwalter selbst brauchen dafür **keinen** Zugang.

---

## 2. Lizenzmodell d.velop Cloud (Stand 09/2026)

### 2.1 Belegte Lizenzmetriken und Listenpreise (AWS-Cloud)

| Produkt | Metrik | Listenpreis (Cloud AWS) | Enthalten / Limits | Status | Quelle |
|---|---|---|---|---|---|
| **d.velop documents platform edition** basic / business / ultimate | **pro Benutzer und Monat** („per user per month") | 27 € / 39 € / 55 € (Hybrid: 40,50 / 58,50 / 82,50 €; On-Prem: auf Anfrage) | Cloud-Speicher **100 / 1.000 / 2.000 GB „pro prod. Mandant"** (flexibel erweiterbar; PDF/A-Renditions nicht angerechnet); d.velop mobile, pilot, process studio, sign, Kollaboration, Teams **erst ab business**; process studio business 1.000 Workflowausführungen/Monat/Mandant, ultimate unlimitiert; sign 50/100 FES/Monat/Mandant; Dokumenteneingang max. **10.000 Dokumente/Monat/Mandant**; E-Mail-Import max. **10.000 E-Mails/Monat/Postfach** (AWS) | F | W01, W02, W03, W04 |
| **d.velop invoices** Small / Medium / Large / Enterprise | **Rechnungsvolumen-Paket** + Buchhaltungsuser; Freigabeuser beliebig | 340 € / 680 € / 1.145 € / 2.065 € pro Monat (T Cloud Public: 510 / 1.020 / 1.750 / 3.100 €) | 250 / 750 / 1.500 / 3.000 Rechnungen/Monat; Mehrmenge > 12-fache Monatsmenge je Vertragsjahr: **0,69 €/Rechnung**; Speicher 50/150/300/600 GB; Buchhaltungsuser 5/10/20/30 (+17 €/Monat je weiterem); Freigabeuser **beliebig**; DATEV-Schnittstellen (Unternehmen Online: C1/H; Rechnungswesen: C1/H/O) **kostenpflichtig, Preis nicht öffentlich**; Service-Limits s. §3 | F | W05 §2.1, §2.3, §3; W06 |
| d.velop pilot (Einzelbuchung) | pro Benutzer und Monat | 8,50 €/User/Monat; Overusage 0,15 € je 1.000 Seiten (Indexierung), 13,50 € je 1.000 Nachrichten | – | E (Store-Seite, Datum unklar, nennt noch OpenAI/Aleph Alpha) | W20 |
| d.velop contracts | pro Benutzer und Monat | Restricted User 9 €, Full User 29 € | setzt d.velop documents (basic/business/ultimate) voraus | F | W31 |
| Portalanbindung per API | je Download | 7,60 € / 1.000 Dokumente | – | F | W08 |

**Weitere Fakten zur Lizenzlogik**
- Umstellung „unabhängig von der Betriebsform, für alle Kunden einheitlich auf ein marktübliches Modell zur Software-Miete" mit „neuer Lizenzmetrik" [W02 S. 2] (F).
- **Kein** Concurrent-User-Modell in den öffentlichen Cloud-Preislisten gefunden (N). Die Metrik ist **benannte Benutzer** (Named User) je Edition bzw. rollenbasierte Benutzer bei invoices (E – „Named" nicht wörtlich, aber „per user per month").
- **Keine** Lizenzierung nach Anzahl Akten oder Dokumenten; Mengenbezug nur über **Speicher je produktivem Mandant** (Tenant), Import-/Workflow-/Token-Limits je Tenant und bei invoices über **Rechnungen/Monat** (F, W01–W06).
- Belegerkennung (OCR/KI) für Rechnungen ist im invoices-Paket enthalten; **keine separaten Seitenpakete** für die Rechnungserkennung dokumentiert. Für KI-Kategorisierung sonstiger Dokumente über den d.velop document reader „können weitere Kosten anfallen" (F, W01 Fußnote ****).
- invoices (Betriebsform OTC) enthält pilot/process studio nur eingeschränkt auf Rechnungen; in AWS **nicht** enthalten → process studio kommt über platform edition business/ultimate (F, W05 §2).

### 2.2 Rechnerische Einordnung für Livos (~80 Nutzer, 5.000–8.000 Belege/Jahr, >100 Gesellschaften)

Alle Werte **Listenpreise, AWS-Cloud, ohne Rabatte, ohne Einführungsdienstleistung, ohne DATEV-Schnittstelle** (Preis nicht öffentlich); MwSt.-Behandlung nicht angegeben (**A**: netto).

| Baustein | Rechnung | €/Jahr | Status |
|---|---|---|---|
| invoices **Medium** (9.000 Rechnungen/Jahr inkl., 10 Buchhaltungsuser, Freigeber unbegrenzt) | 680 € × 12 | **8.160 €** | F (Rechnung A) |
| Alternative invoices **Small** + Mehrmenge (3.000 inkl.; 5 Buchhaltungsuser) | 4.080 € + (2.000…5.000) × 0,69 € | **5.460 … 7.530 €** (+204 €/Jahr je zusätzlichem Buchhaltungsuser) | F (Rechnung A) |
| platform edition **business** für **alle 80** Nutzer | 39 € × 80 × 12 | 37.440 € | F (Rechnung A) |
| platform edition **business** nur für DMS-Vollnutzer, Annahme **20** (Buchhaltung, Asset Management, Vertrags-/Postbearbeitung) | 39 € × 20 × 12 | 9.360 € | A |
| platform edition **ultimate** (unlimitierte Workflows) für 20 Nutzer | 55 € × 20 × 12 | 13.200 € | A |

**Schlussfolgerungen (A):**
1. Der **Rechnungsteil** ist **volumengetrieben**, nicht nutzergetrieben: Mit „Freigabeuser beliebig" verursachen die ~80 Prüfer/Freigeber (intern **und** extern) keine Nutzerkosten; kostenrelevant sind die Buchhaltungsuser (Trios + interne Buchhaltung).
2. Der **DMS-Teil** (Verträge, Post, Akten, Suche über alle Dokumente, mobile App, pilot, process studio) ist **nutzergetrieben** (39 €/User/Monat in business). Hier entscheidet der Zuschnitt „wer braucht einen vollen documents-User?" über den Preis.
3. Die **>100 Gesellschaften treiben den Preis nicht**, solange sie in **einem** Tenant abgebildet werden (Speicher, Workflow-, Import- und Token-Kontingente gelten je produktivem Mandant/Tenant).
4. Die Arbeitshypothese der Agenda („Named User für 80 Anwender, Preis von Nutzerzahl getrieben, nicht vom Volumen") [A_Leistungskatalog, Blatt Tabelle1] ist damit **nur für den DMS-Teil** richtig; für invoices gilt das Gegenteil.
5. Speicherbedarf (A): 8.000 Rechnungen × ~0,5 MB ≈ 4 GB/Jahr; auch mit Verträgen/Post deutlich unter 150 GB (invoices Medium) bzw. 1.000 GB (business).
6. **Korrektur zur Aussage im Termin:** Auf André Töppers Frage, ob nach Anzahl Akten oder Dokumentgröße lizenziert wird, antwortete Sebastian Pachon „Das geht tatsächlich nach Lizenzgebühren … müsste nochmal nachschauen, wie viele Dokumente man auf der Instanz … abspeichern kann" [Transkript 01:08:13–01:08:31]. Belegt ist: **nicht nach Akten**, sondern pro Benutzer (DMS) bzw. Rechnungsvolumen (invoices), mit **Speicherkontingent je Tenant** (erweiterbar).

---

## 3. Mandanten-/Tenant-Modell

### 3.1 Begriffe (F)

| Begriff | Bedeutung | Quelle |
|---|---|---|
| **d.velop cloud-Mandant (Tenant)** | Eigener abgesicherter Cloudbereich je Kunde, eigene Subdomain unter d-velop.cloud, lebenslange tenant-id; „strikte Trennung der Daten unterschiedlicher Mandanten" über eine führende Mandanten-ID. Mehrere Tenants lassen sich im d.velop cloud center in einer **Organisation** verwalten. | W22 §1.1, §3.3; W27 (Auszug) |
| **Mandant in smart invoice / invoices** | Stammdaten-Entität „Companies (Mandanten)": „Mandanten sind Empfänger von Rechnungen. Üblicherweise entspricht ein Mandant … einem Mandanten oder Buchungskreis im ERP-System. Jede Rechnung benötigt einen Mandanten." Felder: `id`, `name`, `address`, `city`, `zip_code`, `local_currency`, `country`. **Kein Feld für USt-IdNr./Steuernummer.** Name und Adresse sind „für die automatische Mandantenermittlung … ein wichtiges Kriterium". | W14 S. 20–21 |
| Kreditoren je Mandant | `company_id` verpflichtend; Kreditor-ID „muss je company_id eindeutig sein" → gleiche Lieferanten mit unterschiedlichen Kreditorennummern je Gesellschaft sind Standard. Sachkonten, Kostenstellen, Steuerschlüssel usw. mandantenspezifisch **oder** ohne `company_id` für alle Mandanten gültig. | W14 S. 21 ff. |
| Bucket | Stammdatenspeicher; „beliebig viele" (Handbuch) bzw. max. 50 (Service-Limit); d.velop **empfiehlt**, Stammdaten „möglichst in einem Stammdatenbucket zu organisieren"; Synchronisation mehrerer Buckets mit dem document reader = **Vorschau-Feature**. | W13 §1.2.11, S. „Synchronisieren mehrerer Buckets"; W05 §3 |

### 3.2 Belegte Grenzen (Service Limits d.velop invoices, W05 §3) (F)

| Limit | Wert | Relevanz Livos (A) |
|---|---|---|
| Mandanten je Bucket | **1.000** | >100 Gesellschaften unkritisch |
| Kreditoren je Bucket | **100.000** (Bankverbindungen 100.000) | Kreditoren zählen **je Gesellschaft** → bei 100 Gesellschaften × Ø 500–1.000 Kreditoren = 50.000–100.000 → **Grenze beobachten (O-6)** |
| Workflowabläufe | max. **100** verschiedene, je max. 50 Schritte | **„Ein eigener Workflow je Gesellschaft" (Katalog 1.4) würde das Limit sprengen** → Gesellschaftsunterschiede über Freigabematrix (Spalte Mandant), Bedingungen und Gruppen abbilden, nicht über >100 Workflowdefinitionen |
| DMS-Repositorys | max. 50 | ein Repository reicht |
| Gruppen | max. 2.500 | z.B. 100 Gesellschaften × 5 Rollen = 500 Gruppen unkritisch |
| Rechnungen | max. 5.000/Tag, 100 MB, 500 Positionen | unkritisch |
| Dokumenteneingang platform edition | 10.000 Dokumente/Monat/Tenant | unkritisch (~700 Rechnungen/Monat) |
| process studio business | 1.000 Workflowausführungen/Monat/Mandant | knapp, falls Post- **und** Rechnungs-Nebenprozesse über process studio laufen (A) |

### 3.3 Mandantenfunktionen in smart invoice (F)

- Freigabematrix mit Spalten **Mandant**, Kostenstelle, Kostenträger (Beispiel „Susanne Meyer … für den Mandanten docures Deutschland AG") [W13 S. 10].
- **Clearing je Mandant:** „Sie können für jeden Mandanten individuelle Gruppen für die Bearbeitung von Belegen im Clearingmodus berechtigen" (Einstellungen > Clearing > Berechtigung hinzufügen > Mandanten-ID + Gruppe) [W13 §1.2.10, S. 30].
- Bedingungen/Gruppennamen über `voucher.company.nr` (z.B. `/^Freigeber_#{voucher.company.nr}$/`) [W13 Anhang Ausdrücke].
- Mandantenermittlung: nur **Name + Adresse** als dokumentierte Kriterien (s.o.) → Problem gleicher Verwaltungsanschriften bleibt (R-03, weiter offen).

### 3.4 Empfehlung (A)

**Ein produktiver Tenant, ein Repository, ein Stammdaten-Bucket**, Gesellschaften als Mandant-Entität (smart invoice) und Pflichteigenschaft „Gesellschaft" (documents); Trennung über attributbasierte Berechtigungsprofile und gesellschaftsbezogene Gruppen. Begründung: (a) d.velop-Empfehlung „ein Bucket", (b) Limits (100 Workflows) sprechen gegen Workflow-je-Gesellschaft, (c) Kontingente (Speicher, WFL, Signaturen, Tokens) und Administration gelten je Tenant, (d) gesellschaftsübergreifende Auswertung (Katalog 3.2) nur im selben Tenant sinnvoll. Separater **Test-Tenant** empfehlenswert – Lizenzierung eines Test-Tenants nicht öffentlich dokumentiert (**O-5**).

---

## 4. Vier-Augen-Prinzip / Freigabematrix (R-08)

| Nr | Aussage | Status | Quelle |
|---|---|---|---|
| V1 | Leistungsbeschreibung invoices (2025-12-15) listet **„Vier-Augen-Prinzip (Sicherstellung, dass Prüfung & Freigabe nicht von der gleichen Person vorgenommen werden)"** als enthalten (●) in allen Betriebsformen C1/C2/H/O. | F | W05 §2.3; W06 |
| V2 | Handbuch smart invoice Cloud (PDF 23.06.2026) führt **„Erzwingen eines Vier-Augen-Prinzips in der Freigabe (Vorschau-Feature)"** weiterhin als Vorschau-Feature: „Wenn Sie das Vorschau-Feature testen möchten, wenden Sie sich an den d.velop-Support". Wirkung: „für freizugebende Beträge über 10.000,00 EUR …, dass immer eine zweite Freigabe erforderlich ist"; gilt **pro Kostenobjekt**; Strategien „Direkt" und „Von Unten zum Freigeber" beschrieben; sachliche Prüfer werden bei aktivem Vier-Augen-Prinzip nicht als Freigeber berücksichtigt; Minimalbetrag konfigurierbar. | F | W13 S. 19–21 |
| V3 | **Einordnung:** V1 (Trennung Prüfer ≠ Freigeber) ist **GA/Standard**; V2 (zweite Freigabe ab Betrag X erzwingen) ist **Preview** (Stand Handbuch 06/2026). Beide Begriffe dürfen gegenüber Livos nicht vermischt werden. | A (Einordnung) | W05, W13 |
| V4 | Weitere Vorschau-Features im selben Handbuch: Ad-hoc-Gruppen (Beleg an mehrere Empfänger), manuelle Zuschläge, mehrere Buckets im document reader. | F | W13 |
| V5 | Fallback ohne Preview: Freigabestrategie „Von Unten zum Freigeber" (mehrstufig) oder zweiter Freigabeschritt mit Wertgrenzen-Bedingung an der Schrittverbindung (bereits in 04b §1.7 belegt). | F (aus 04b) / A (Eignung) | W13; 04b §1.7 |

---

## 5. KI bei d.velop (d.velop pilot, d.velop AI)

### 5.1 Fähigkeiten (F)

| Fähigkeit | Belegte Aussage | Quelle |
|---|---|---|
| Chat mit **einem Dokument** | Kontextaktion (Stern-Symbol) in der Dokumentansicht; „In the chat you can ask questions about the document"; Chatverlauf 30 Tage, speicherbar in Notizen; „binnen Sekunden beispielsweise eine Zusammenfassung eines Dokuments oder die Angabe zur Laufzeit eines Vertrages". Einzeldokumentansicht „ohne jegliche Konfiguration direkt verwenden, sobald d.velop pilot in einem Mandanten gebucht ist". | W16 §1.1.1, §1.4.1; W17 §1.2.1 |
| Prompt-Katalog | Zusammenfassung, Sentiment, Action Items, **Risikoanalyse** (rechtlich/finanziell), FAQ, personenbezogene Daten | W17 §1.2.1 |
| Chat mit **bis zu 10 Dokumenten** | Auswahl in der Ergebnisliste → Kontextaktion Assistent | W17 §1.3 |
| **Assistenten / Knowledge Bases** | Admin definiert Datenquelle (Repository, Kategorie, bis 10 Metadaten als Filter, Datumsfilter, automatische Aktualisierung); Antworten mit Quellenangabe; **„Es werden immer nur die neuesten 5.000 Dokumente verarbeitet"**; aktuell: „bis zu **5 Knowledge Bases** … je … bis zu 5.000 Dokumente" pro Tenant | W16 §1.3.2; W15 §5 |
| process studio | Aktionen „d.velop pilot – Dokument-Prompt" (Prompt + Dokument als Base64, PDF/JPEG/PNG/TIFF/Text) und „Assistent-Prompt"; aktuell „Dokumenten-basierte Agenten … können innerhalb des d.velop process studio definiert und in Prozessabläufe eingebunden werden" | W16 §1.3.3; W15 §2 |
| Berechtigungen | Chat/Assistent berücksichtigen Dokumentberechtigungen; **aber:** „Da Prozesse im Hintergrund ablaufen, prüft der Assistent in Prozessen keine Dokumentberechtigungen." | W16 §1.3.2; W19 |
| Dokumentgröße | „Verarbeitung derzeit auf Dokumente mit einer Länge von weniger als **20.000 Token** beschränkt. Längere Dokumente werden … unmittelbar abgelehnt." (Handbuch 1.0.0; ob noch aktuell: **O-7**) | W16 §1.4.3 |
| Kontingente | platform edition: 50 Mio. Token/Tenant/Monat für Indexierung (≈100.000 Seiten), 500 Nachrichten je lizenziertem Nutzer/Monat, 250 Mio. Token/Tenant/Monat für Chat (≈500.000 Seiten); Preisseite nennt abweichend „100.000 Token je User" pro Monat | F (Widerspruch W01/W02 ↔ W03 → E) |
| Verfügbarkeit | platform edition **business/ultimate**, Betriebsformen AWS (C1), OTC (C2), Hybrid; **nicht basic**, nicht rein On-Prem | W01 §2.2.4; W02 |
| Weitere KI im Standard | documents: KI-Dokumententrennung („documentsplitting") und KI-Kategorisierung („documentclassification", 3 Vorschläge) ab business (C1/H); invoices: Autotraining der Erkennung, **KI-basierte Kontierungsvorschläge (Sachkonto, Kostenstelle auf Belegebene)** (C1/H/O, nicht C2) | W07 §4.1.1; W01; W05 §2.3 |
| Ausblick | d.velop AI / „agent center", Partner (Otera, Parashift, PlanB., amberSearch) – Marketingaussagen | W19 (E) |

### 5.2 Datenschutz / Hosting der KI

| Aussage | Status | Quelle |
|---|---|---|
| Aktuelle Funktionsbeschreibung (2026-09-11): Dokumente und Nutzereingaben werden verschlüsselt per API an den „jeweiligen KI-Anbieter" übertragen; „Nähere Informationen sind dem Auftragsverarbeitungsvertrag inkl. Anlagen zu entnehmen." **Konkreter Anbieter/Region im Dokument nicht genannt.** | F | W15 §3 |
| d.velop AI: „Datenhaltung und Verarbeitung erfolgen ausschließlich im EU-Rechtsraum"; freie Modellwahl („OpenAI, Anthropic, Google", Open-Source); „Im Standard stellt d.velop passende KI-Modelle bereit"; „EU AI Act-ready". | E (Marketingseite) | W19 |
| AVV-Festlegungen (2023-09-12): Unterauftragsverarbeiter pilot = **Aleph Alpha GmbH** (Heidelberg) und **Microsoft Azure OpenAI Service** (Microsoft Ireland Operations Ltd.); „Alle Partner … verpflichten sich, die … Daten … nicht zum weiteren Training des LLM zu nutzen"; Infrastruktur in der EU, „in der Regel innerhalb von Deutschland"; SCC 2021. | E (Stand 2023) | W21 §4–6 |
| Historisch (2023): Option **OpenAI OpCo, LLC** mit ausdrücklichem Hinweis auf Drittlandübermittlung; Eingaben bis 90 Tage anonymisiert zur Produktverbesserung gespeichert. **Aktueller Stand dieser Regelungen: O-8.** | E (veraltet) | W18 |
| Handbuch 1.0.0: „Trainieren andere KI-Modelle mit meinen Daten? Nein … nur mit KI-Anbietern …, deren Verarbeitungsrichtlinien eine Verwendung von Eingaben für Trainingszwecke explizit ausschließen." | F | W16 §1.4.5 |
| Haftung: keine Gewähr für Richtigkeit, Halluzinationen möglich; Prüfung der Zulässigkeit liegt beim Kunden. | F | W15 §4–5 |

### 5.3 Konsequenz für die Livos-Frage „20-seitiger Vertrag – kann ich d.velop fragen?"

- **Fakt:** d.velop kann das inzwischen **im Standard** über d.velop pilot (Kontextaktion Chat, Prompt „Zusammenfassung"/„Risikoanalyse", Assistent über Vertragskategorie), enthalten in platform edition business/ultimate [W01, W16, W17, W04: „Ask your documents questions in natural language … whether summaries or contract terms"].
- **Transkript:** André Töpper fragte [01:08:46–01:09:07]; Sebastian Pachon: „Nicht über Develop direkt, aber über unsere Anwendungen"; Thomas Groß: „Über unsere KI Plattform" [01:09:09–01:09:14]. **Diese Aussage ist nach aktuellem Stand zu korrigieren/präzisieren.**
- **A:** Positionierung: d.velop pilot für Fragen an Dokumente **innerhalb** d.velop (berechtigungssensitiv); MDIS-KI-Plattform als Ergänzung für **systemübergreifende** Analysen (DATEV, Stammdaten-App, BI, Kreditorenkonsolidierung).
- **A (Risiko):** 20 Seiten Vertragstext ≈ 8.000–10.000 Wörter ≈ 12.000–20.000 Token (deutsch); bei der dokumentierten 20.000-Token-Grenze kann ein 20-seitiger Vertrag **abgelehnt** werden → im PoC mit echten Livos-Verträgen testen (O-7).

---

## 6. Mobile App und Outlook/Office-Integration

| Thema | Belegte Aussage | Status | Quelle |
|---|---|---|---|
| Browser/responsiv | „Die Oberflächen … auch auf mobilen Endgeräten … über den Browser angezeigt (Responsives Design)" – alle Editionen; invoices: „Mit verschiedenen Endgeräten nutzbar (Smartphone, Tablet, PC)". Browser: Chrome, Safari, Edge (process studio), Firefox/Chrome/Edge (pilot). | F | W07 §4.1.6; W05 §2.3; W11 §4.4 |
| Lokales Bearbeiten | benötigt „eine lokale Client-Anwendung" auf dem Rechner (einzige Installationsanforderung) | F | W07 §4.1.2 |
| **d.velop mobile** (native App) | iOS/iPadOS (App Store id1464693393) **und Android** (Google Play `com.dvelop.mobile_ecm_android`, „Aktualisiert am 13.08.2026"); Funktionen: Login-Profile, Face ID/Touch ID, Offline-Akten, Push, Versionierung offline, iOS-Dokumentscanner, **Abwesenheitsstatus setzen**, Zugriff auf alle d.velop cloud Apps; Play-Beschreibung: „Von überall können Sie Ihre Aufgaben erledigen". | F | W28; W01 §2.2.3; W08 |
| Lizenz mobile | in platform edition **business/ultimate** enthalten, **nicht in basic** | F | W01; W02 S. 7 |
| smart-invoice-Aufgaben in der App | Bedienbarkeit der smart-invoice-Workflowmaske in d.velop mobile **nicht dokumentiert** | O-9 | – |
| **Outlook** | COM-Add-In (Desktop-Outlook M365): Mehrfachablage in vordefinierte Kategorien, Suche im Kontext der Mail, Ablageordner; **Web-Add-In** (Outlook im Web, „neues Outlook"): ohne Mehrfachablage und ohne direkte Suche. Verteilung organisationsweit über Microsoft 365 Admin Center (bis 6 h). Enthalten ab **business** (C1, C2, H, O). | F | W07 §4.1.4; W29; W01 §2.2.1 |
| Office | Erstellen/Bearbeiten von M365-Office-Dokumenten im Browser ab business, **setzt Microsoft 365 Business-Abo voraus**; „Integration in Microsoft Office" (Add-In) laut LB nur H/O | F | W01; W02 S. 5–6 |
| Teams | Registerkarte + Link-Teilen ab business | F | W01 §2.2.8 |

---

## 7. Vertretung / Abwesenheit (plattformweit)

| Nr | Aussage | Status | Quelle |
|---|---|---|---|
| T1 | Userprofile-App = Basis-App jedes Cloud-Tenants („Verwaltung von Abwesenheiten"). | F | W22 §1.2 |
| T2 | **Administrator/Vorgesetzter setzt Abwesenheit für andere:** „Wenn Sie entsprechende administrative Berechtigungen (z.B. bei Vorgesetzten) besitzen, können Sie auch die Abwesenheitsstatus anderer Benutzer konfigurieren." Start „jetzt" per Uhrensymbol, Ende optional (sonst unbegrenzt), Vertretung, Nachricht; Vertretung „übernimmt die Berechtigungen". | F (Doku-Version 1.9.0, auch als „latest" ausgeliefert) | W30; 04b §2.6 |
| T3 | Vertretungsregeln je Aufgabentyp/Kontext (z.B. „Rechnung"), Vertretungsausschluss (z.B. „Personal"), Standardvertreter; in allen Editionen enthalten. | F | W09 §1.6.1–1.6.7; W01 §2.2.1 |
| T4 | **Aufgabenlisten anderer überwachen und Aufgaben (auch gesammelt) weiterleiten** durch berechtigte Personen; fachlich Verantwortliche sehen alle Aufgaben ihres Kontextes. | F | W07 §4.1.3 |
| T5 | **smart invoice:** „Ihre Vertretung kann nur Aufgaben sehen, die persönlich an Sie adressiert wurden … keine Aufgaben …, die Ihnen im Rahmen einer Gruppenmitgliedschaft zugestellt wurden." Beim Öffnen wird die Vertretung Workflowbeteiligte; Vertretung braucht passendes Berechtigungsprofil für das Rechnungsdokument. | F | W13 §1.2.2 |
| T6 | invoices: „Abwesenheits- und Vertretungsregeln" und „Eskalationsmöglichkeit von Aufgaben nach festgelegten Regeln" enthalten. | F | W05 §2.3 |
| T7 | process studio: max. **50 Vertretungsregeln**, 100 Kontextregeln. | F | W11 §7.2 |

**Konsequenz (A):** Die im Termin gestellte Frage „kann ein Admin für einen erkrankten Kollegen die Vertretung setzen?" [Transkript 01:05:21, André Töpper; Antwort offen gelassen 01:05:41, Sebastian Pachon] ist **mit Ja** zu beantworten (T2), ergänzend über „Aufgaben gesammelt weiterleiten" (T4). Einschränkung T5 beachten: Gruppenaufgaben sieht die Vertretung nicht (sind aber für alle Gruppenmitglieder ohnehin sichtbar).

---

## 8. SSO, Hosting, Zertifizierungen, DSGVO

| Thema | Belegte Aussage | Status | Quelle |
|---|---|---|---|
| SSO | „Single Sign-on via OpenID Connect" (alle Editionen); „Authentifizierung über weitere Identity Provider (via OpenID Connect)" und AD-Integration (ADFS, LDAP) **ab business**; Identityprovider-App: „Vertrauensstellung zu externen Identitätssystemen via OpenID Connect". | F | W01 §2.2.1; W07 §4.1.6; W22 §1.3 |
| Microsoft Entra ID | KB-Artikel „Wie konfiguriere ich die Anmeldung an d.velop documents mithilfe von OpenID Connect und einem Azure AD?" und „Werte für den OpenID Connect-Provider von Microsoft Azure Active Directory"; zyklische Synchronisation/Provisionierung von Benutzern und Gruppen aus Azure AD in den Tenant; Usermanagement-App mit **SCIM 2.0**-Schnittstelle. | E (nur Suchergebnis-Auszüge; KB ohne Login nicht lesbar) | W25; W26 |
| MFA | 2-Faktor (TOTP-App), FIDO2 (Sicherheitsschlüssel/Passkey); d.velop „empfiehlt die Verwendung der bereitgestellten Single Sign On (SSO) Mechanismen" (Verantwortung Identitätsmanagement beim Kunden). | F | W09 §1.9.15, §1.9.28; W22 §3.1 |
| Betriebsformen | Multi-Tenant-Cloud **AWS (C1)** oder **T Cloud Public/OTC (C2)**, Hybrid, On-Prem. AWS „mit Standorten u.a. in Frankfurt"; T Cloud Public „rein europäischer Anbieter". Auch bei T Cloud Public laufen Billing-Apps bei AWS. | F | W06; W22 §1.2 |
| Datenstandort | LB 2022: Betrieb „in Gescher als auch vom externen IT-Dienstleister im Großraum Frankfurt am Main"; Inhalte „grundsätzlich in Deutschland" (Ausnahme eingehende E-Mails: EU). **In der LB 2026-07-28 ist der Abschnitt „Datenstandort" nicht mehr enthalten** → aktuelle Standortzusage im AVV prüfen (O-10). | E | W23 §3.1; W22 |
| Backup/DR | tägliche Backups, RPO 24 h, Vorhaltung 30 Tage, halbjährliche DR-Tests, RTO-Ziel 48 h; Löschung nach Weisung + 90 Tage Vorhaltung; AES-256-GCM at rest, TLS ≥ 1.2; Audit-Trail sicherheitsrelevanter Ereignisse (inkl. Lese-/Schreibzugriffe) 180 Tage. | F | W22 §2–3 |
| Zertifizierungen d.velop AG | ISO/IEC 27001:2022 (ISMS), ISO 9001:2015, ISO 14001, ISO 50001, **TISAX® AL2** (Informationssicherheit hoher Schutzbedarf, Datenschutz Art. 28 DSGVO). | F | W24 |
| IDW PS 880 | „d.velop documents and d.velop postbox have passed the audit according to the guidelines of IDW PS 880 … suitable for audit-proof archiving in accordance with the GoBD standard." Prüfbericht auf Anfrage. **Ob der Bericht die Cloud-Betriebsform abdeckt: O-11.** | F / O | W24 |
| Rechenzentren | Rechenzentren des Dienstleisters zertifiziert u.a. ISO 9001, 27001, 27017, 27018, **C5** (LB 2022). | E (Stand 2022, bezieht sich auf RZ-Dienstleister) | W23 §3.1; W24 |
| BSI C5 / IDW PS 951 für d.velop selbst | **Nicht gefunden.** (C5 nur für RZ-Dienstleister belegt.) | N → O-11 | – |
| DSGVO/AVV | AVV mit „Festlegungen zur Auftragsverarbeitung": Unterauftragsverarbeiter u.a. AWS EMEA SARL (Luxemburg), Microsoft Ireland (Office Online, Azure OpenAI), Telekom Deutschland (OTC), Aleph Alpha; Verarbeitung „grundsätzlich innerhalb der EU, in der Regel innerhalb von Deutschland"; SCC 2021 + 256-Bit-Verschlüsselung wegen US-Muttergesellschaften. | E (Stand 2023-09-12) | W21 |

---

## 9. Konsequenzen für Katalogpunkte

| Kat. | Anforderung (Prio) | Bisheriger Eintrag | Empfehlung Erfüllungsgrad | Begründung / Formulierungsvorschlag für Spalte „Notizen" | Belege |
|---|---|---|---|---|---|
| **1.1** | Echte Mandantenfähigkeit >100 Gesellschaften (Must) | K | **K** (bestätigt) | „Ein d.velop-Cloud-Tenant; jede Gesellschaft als Mandant-Stammsatz in d.velop invoices (bis 1.000 je Bucket) und als Pflichteigenschaft im DMS; Kreditoren, Sachkonten, Kostenstellen je Gesellschaft; Trennung über attributbasierte Berechtigungen, Freigabematrix-Spalte Mandant und Clearing-Gruppen je Mandant. Getrennte Tenants je Gesellschaft sind technisch möglich, aber wegen Kontingenten je Tenant und fehlender Gesamtsicht nicht empfohlen." Hinweis: Limit 100 Workflowdefinitionen → gesellschaftsspezifische Regeln über Matrix/Bedingungen, nicht über eigene Workflows (wirkt auch auf 1.4). | W05 §3, W13, W14, W22 |
| **1.2** | Webbasiert, responsiv, ohne Installation (Must) | S | **S** | „Web-Client im Browser, responsives Design für Smartphone/Tablet/PC; Installation nur für optionales lokales Bearbeiten und Outlook-COM-Add-In. Betrieb in der d.velop Cloud (AWS Frankfurt oder T Cloud Public)." | W07, W05, W06 |
| **1.3** | App Android/iOS (Could) | S | **S (ab platform edition business)** | „Native App d.velop mobile für iOS/iPadOS und Android (Offline-Akten, Aufgaben, Abwesenheit); in d.velop documents business/ultimate enthalten, nicht in basic und nicht im reinen invoices-Paket. Bedienung der Rechnungsfreigabe in der App vor Zusage im Test verifizieren." | W28, W01 |
| **1.5** | Rollen & Rechte intern + extern (Must) | S | **S** | „Rollen- und attributbasierte Berechtigungsprofile (Kategorie + Eigenschaft Gesellschaft), Gruppen/globale Gruppen, Sub-Administration; Externe als rollenbeschränkte Freigabeuser (invoices) oder volle Benutzer; SSO über Microsoft Entra ID (OIDC), 2FA/FIDO2." | W07 §4.1.6, W05 §2.4, W25 |
| **1.4** (Querbezug) | Vier-Augen ab Betrag X je Gesellschaft (Must) | S | **K** | „Freigabematrix mit Betragsgrenzen je Mandant/Kostenstelle; Trennung Prüfer ≠ Freigeber Standard; erzwungene zweite Freigabe ab Betrag X ist laut Handbuch (06/2026) Vorschau-Feature – bis GA über mehrstufige Freigabestrategie bzw. zweiten Freigabeschritt mit Wertgrenze." | W05, W13 |
| **3.4** | Vertretung geplant/ungeplant (Must) | K | **S/K** (S für Mechanik, K für Vertretungsregeln je Kontext) | „Abwesenheit mit Start/Ende und Vertretung im Benutzerprofil (auch App); Vorgesetzte/Administratoren können die Abwesenheit für erkrankte Mitarbeitende setzen; zusätzlich Aufgaben anderer gesammelt weiterleiten; Vertretungsregeln je Aufgabentyp (z.B. ‚Rechnung'). Einschränkung: Vertretung sieht nur persönlich zugestellte Aufgaben." | W30, W09, W07, W13 |
| **4.2** | Ad-hoc-Freigabe per Mail/Link ohne Lizenz (Should) | leer | **K mit Anpassungsanteil (K/A)** | „Externe Benutzeraufgabe in d.velop process studio: E-Mail mit Link auf ein Web-Formular, keine Registrierung/Lizenz für den Empfänger, zeitlich begrenzt über Pflicht-Timer, nur freigegebene Prozessdaten sichtbar. Das Rechnungsbild ist im Formular nicht direkt verfügbar und wird z.B. per zeitlich begrenztem externen Freigabelink (max. 180 Tage) bereitgestellt. Kopplung an den smart-invoice-Freigabeschritt erfordert Prozessmodellierung/Skript. Voraussetzung: documents platform edition business (process studio, Kontingent 1.000 Workflowausführungen/Monat). Kein Passwort/MFA für den Link dokumentiert." | W10, W09, W08, W01 |
| **4.3** | Web-Zugang Kernpartner (Must) | S | **S** | „Kernpartner (z.B. Property Manager, Projektsteuerer) erhalten ein eigenes d.velop-Cloud-Konto (Einladung per E-Mail, 2FA/FIDO2 oder eigener IdP) und arbeiten als Freigabeuser im Rechnungseingangsbuch/in der Aufgabenliste; Freigabeuser sind in d.velop invoices in beliebiger Zahl enthalten; Sicht auf die eigenen Gesellschaften per Berechtigungsprofil." (Vorbehalt O-2) | W05 §2.1/2.4, W26 |
| **Lizenz** | Lizenz-/Mengengerüst (Agenda) | Hypothese „Named User, volumenunabhängig" | – | **Zweiteilig:** (1) Rechnungen: d.velop invoices nach Rechnungsvolumen (Medium 750/Monat = 9.000/Jahr, 680 €/Monat Liste) + Buchhaltungsuser; Prüfer/Freigeber unbegrenzt. (2) DMS: d.velop documents platform edition pro Benutzer/Monat (business 39 €, ultimate 55 €), Speicher/Workflows/KI-Kontingente je Tenant. DATEV-Schnittstelle kostenpflichtig (Preis auf Anfrage). >100 Gesellschaften sind preisneutral bei einem Tenant. Richtwert Liste: ~8.200 €/Jahr (invoices Medium) + 39 € × Anzahl DMS-Vollnutzer × 12. | W01–W06 |
| **2.5** (Nebenbefund) | KI-Kontierungsvorschläge (Must) | S | **S (nur AWS/Hybrid/On-Prem, nicht T Cloud Public)** | „KI-basierte Kontierungsvorschläge (Sachkonto, Kostenstelle auf Belegebene) und Autotraining der Erkennung in C1/H/O." → spricht für Betriebsform **AWS** (auch DATEV Unternehmen Online nur C1/H). | W05 §2.3 |
| **KI-Frage Verträge** (Transkript) | Fragen an 20-seitigen Vertrag | „nur über MDIS-KI-Plattform" | – | Korrigieren: „d.velop pilot (in business/ultimate enthalten) beantwortet Fragen zu Einzeldokumenten, bis zu 10 ausgewählten Dokumenten und über Assistenten (bis 5 × 5.000 Dokumente); MDIS-KI-Plattform ergänzend für systemübergreifende Analysen." Token-Grenze pro Dokument im PoC prüfen. | W15–W17, W01 |

---

## 10. Offene Punkte

| ID | Prio | Offener Punkt | Warum | Weg |
|---|---|---|---|---|
| O-1 | P1 | **Kopplung smart invoice ↔ process studio für externe Freigabe:** Kann der smart-invoice-Workflow einen process-studio-Prozess mit Externer Benutzeraufgabe starten und das Ergebnis (freigegeben/abgelehnt/Kommentar) als Freigabe zurückschreiben? Kann ein Prozess per API einen externen Freigabelink (documents „Extern teilen") erzeugen? Revisionssichere Protokollierung der externen Entscheidung? | Katalog 4.2; R-06/R-16 | d.velop PM/Support, Test Demo-Tenant |
| O-2 | P1 | **Lizenzrechtliche Zulässigkeit:** Dürfen Dritte (Property Manager, Projektsteuerer, Trios) als **Freigabeuser** bzw. Buchhaltungsuser genutzt werden? Gilt „Freigabeuser beliebig" auch für externe Personen? | Katalog 4.3, Mengengerüst | d.velop Vertrieb (AGB/Nutzungsbedingungen) |
| O-3 | P1 | **Mischlizenzierung** invoices + platform edition: Müssen alle Benutzer im Tenant eine platform-edition-Lizenz haben, sobald documents business gebucht ist, oder nur die DMS-Vollnutzer? Staffel-/Mengenrabatte ab 80 Nutzern? | Angebot | d.velop Vertrieb |
| O-4 | P1 | **DATEV-Schnittstelle:** Preis und Metrik (je Mandant/Beraternummer? je Buchung?) für „d.velop invoices for DATEV Rechnungswesen/Unternehmen Online" bei >100 DATEV-Mandanten | Lizenz, Katalog 5.1 | d.velop Vertrieb |
| O-5 | P2 | Test-/Staging-Tenant: Kosten und Lizenzbedingungen | Betrieb | d.velop Vertrieb |
| O-6 | P2 | Service-Limit 100.000 Kreditoren je Bucket bei Kreditoren je Gesellschaft – reale Anzahl bei Livos (DATEV-Export) ermitteln; ggf. Erhöhung vereinbaren („Die Parteien können eine Erhöhung der Beschränkung vereinbaren") | Katalog 1.1 | Livos/Trios, d.velop |
| O-7 | P2 | d.velop pilot: gilt die **20.000-Token-Grenze** je Dokument noch (Handbuch 1.0.0)? PoC mit echtem 20-seitigem Livos-Vertrag | KI-Frage Livos | PoC im Demo-Tenant |
| O-8 | P2 | Aktuelle **LLM-Anbieter und Region** des d.velop pilot (AVV-Anlage 2026), Speicherung von Eingaben zur Produktverbesserung (2023: 90 Tage) – für Livos-Datenschutzprüfung | DSGVO | d.velop Datenschutz / AVV anfordern |
| O-9 | P2 | Bedienung der **smart-invoice-Freigabeaufgabe in d.velop mobile** (Android/iOS) | Katalog 1.3 | Test Demo-Tenant |
| O-10 | P2 | Aktuelle **Datenstandortzusage** (Deutschland vs. EU) für AWS-Betrieb, da die LB 2026 keinen Abschnitt „Datenstandort" mehr enthält | DSGVO, Ausschreibung | AVV/TOM anfordern |
| O-11 | P2 | **IDW PS 880-Bericht** für d.velop documents: Abdeckung Cloud? Eigenes **BSI-C5-Testat / IDW PS 951** der d.velop AG vorhanden? | GoBD (Katalog 1.6), Wirtschaftsprüfer | d.velop (Prüfbericht anfordern) |
| O-12 | P2 | **Vier-Augen-Prinzip (Preview):** GA-Termin, Freischaltung im Livos-Tenant, Konfigurierbarkeit des Schwellwerts je Mandant (nicht nur 10.000 € Beispiel) | Katalog 1.4, R-08 | d.velop Support |
| O-13 | P3 | Passwortschutz/MFA für externe Freigabelinks und Formular-Links (nicht dokumentiert) | Sicherheitskonzept 4.2 | d.velop PM |
| O-14 | P3 | Entra-ID-B2B-Gäste als Login-Weg für externe Partner (OIDC mit Livos-Entra) statt d.velop-cloud-Konten | Katalog 1.5/4.3 | Test, Livos-IT |
| O-15 | P3 | Widerspruch pilot-Kontingente (50 Mio. Token/Tenant + 500 Nachrichten/User laut LB/Factsheet vs. „100.000 Token je User" laut Preisseite) | Mengengerüst KI | d.velop Vertrieb |

---

## 11. Kurzfazit

- **Externe:** Für **registrierte Kernpartner** (4.3) ist d.velop invoices mit **unbegrenzten Freigabeusern** der Standardweg (Vorbehalt: Nutzungsrecht für Dritte). Für **nicht registrierte Ad-hoc-Beteiligte** (4.2) gibt es die process-studio-**Externe Benutzeraufgabe** (E-Mail-Link, Pflicht-Timer, keine Lizenz für den Empfänger), aber **ohne Dokumentzugriff im Formular** und ohne dokumentierte Kopplung an smart invoice → **K mit Anpassungsanteil**.
- **Lizenz:** Rechnungen **volumenbasiert** (Medium: 9.000/Jahr, 680 €/Monat Liste), DMS **pro Benutzer** (business 39 €/Monat), Kontingente **je Tenant**; nicht nach Akten. >100 Gesellschaften kostenneutral in **einem** Tenant.
- **Mandanten:** Ein Tenant, ein Bucket, Gesellschaften als Mandant-Entität (bis 1.000); Limit **100 Workflowdefinitionen** verbietet „Workflow je Gesellschaft".
- **Vier-Augen:** Prüfer ≠ Freigeber = Standard; „zweite Freigabe ab Betrag X erzwingen" = weiterhin **Vorschau-Feature**.
- **KI:** d.velop pilot beantwortet Fragen zu Verträgen **im Standard** (business/ultimate) – die Workshop-Aussage „nur über MDIS-KI-Plattform" ist zu korrigieren; Token-Grenze je Dokument und aktuelle LLM-Region sind offen.
- **Mobile/Outlook/Vertretung/SSO:** App für iOS **und Android** (ab business), Outlook COM-/Web-Add-In (ab business), Admin kann Abwesenheit für Erkrankte setzen, SSO via OIDC/Entra ID, 2FA/FIDO2; ISO 27001, TISAX, IDW PS 880 (documents); eigenes C5/PS 951 nicht gefunden.
