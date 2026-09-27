# 10 — Web-Recherche: DATEV-Integration und Zahlungsprozess (Livos)

Stand der Recherche: 26.09.2026. Rechercheur: Subagent „DATEV/Zahlung“.
Grundlage: Briefing `00_BRIEFING.md`, `04b_dvelop_faehigkeiten_B.md` §1.9 und §7 (R-01, R-02), `txt/B_02_Eingangsrechnungen_smart_invoice.md` §9, Leistungskatalog 5.1/5.5, Transkript, Livos-Zielarchitektur (MDIS-Folien).

**Kennzeichnung:** **[F]** = Fakt, mit URL belegt · **[F-S]** = Fakt nur aus Suchindex-Auszug belegt (Seite selbst nicht abrufbar, weil JS/Login) · **[A]** = Annahme/Ableitung des Rechercheurs · **[O]** = offene Frage.
Quellenkürzel in eckigen Klammern (z.B. [Q3]) verweisen auf das Quellenverzeichnis in Abschnitt 9. Lokale Kopien der ausgewerteten PDFs/Seiten liegen unter `SP/web_datev/`.

---

## 0. Kurzfazit

1. **Es gibt einen Standardweg d.velop → DATEV Rechnungswesen, aber er kommt von einem Drittanbieter.** d.velop führt „DATEV Rechnungswesen (standardisierte Schnittstelle)“ als kostenpflichtige Option von d.velop invoices (Cloud, Hybrid, On-Premises) [F][Q1]. Technisch ist das **LDconnect für DATEV Rechnungswesen** von LIONDEER (Lion & Deer GmbH), laut Leistungsbeschreibung „Hersteller der … DATEV Schnittstelle“ [F][Q2][Q3]. Übergeben wird ein **Buchungsvorschlag mit Dokumentenlink** über **DATEVconnect** in DATEV Kanzlei-Rechnungswesen oder Mittelstand Faktura mit Rechnungswesen. DATEV-Stammdaten kommen **täglich** zurück in die smart-invoice-Buckets [F][Q3].
2. **Ausgelöst wird die Übergabe durch ein Ereignis, nicht einmal täglich im Batch.** smart invoice exportiert an einer Schrittverbindung [F][B_02 §9]. LDconnect überträgt „für alle aus d.velop invoice übergebenen Rechnungen“ einen Buchungsvorschlag [F][Q3]. Eine Übergabe mehrmals am Tag ist damit realistisch [A]. Stammdaten gleicht LDconnect aber nur **täglich** ab [F][Q3]. Ein neu in DATEV angelegter Kreditor steht deshalb erst am Folgetag zur Verfügung [A].
3. **„Inkl. Belege“ heißt hier: Beleglink, nicht Belegbild.** Das Belegbild bleibt in d.velop. Aus DATEV wird es über die „DATEV Beleganzeige Drittanbieter“ aufgerufen [F][Q3][Q4]. Soll das Belegbild selbst in DATEV liegen, führt der Weg über DATEV Unternehmen online (DUO) mit Rechnungsdatenservice 1.0 oder Belegbilderservice [F][Q6][Q9].
4. **Beim extern gehosteten DATEV braucht es ein Gateway.** LDconnect verlangt einen DATEV-Server, der aus dem Internet erreichbar ist (IP-Whitelisting). Alternativ gibt es ein **Datengateway von Riecken**, das bei **DATEVasp und DATEV-SmartIT verpflichtend** ist [F][Q3]. Das Wort „**ricken Cloud**“ im Transkript [00:14:00] meint sehr wahrscheinlich das **Riecken Cloud Gateway für DATEVconnect** (Riecken Webservice & Application GmbH) [A, stark]. Dieses Gateway ist ausdrücklich für DATEVasp, DATEV-SmartIT und PARTNERasp gebaut [F][Q10][Q11].
5. **Über 100 Mandanten sind machbar, verursachen aber Kosten und brauchen Architekturentscheidungen.** LDconnect Enterprise enthält 75 Mandanten, jeder weitere kostet 3,45 €/Monat (Listenpreis) [F][Q4]. „LDconnect für DATEV Stammdaten“ gibt es ab 100 Mandanten nur als individuelles Angebot [F][Q5]. smart invoice erlaubt je Bucket 1.000 Mandanten, 100.000 Kreditoren und 50.000 Sachkonten, bei höchstens 50 Buckets [F][Q1]. Bei über 100 DATEV-Mandanten können die Kreditoren- und Sachkontenlimits eines Buckets erreicht werden [A].
6. **Den Zahlstatus aus DATEV (OPOS) liefert der Standard nicht zurück.** In der LDconnect-Leistungsbeschreibung steht keine OPOS- oder Zahlstatus-Rückmeldung [F][Q3]. Technisch geht es über DATEVconnect: `…/accounts-payable` liefert die offenen Posten der Kreditoren [F][Q14]. Umsetzen müsste das die MDIS-Middleware (**A**).
7. **smart invoice selbst erzeugt keine Zahlungsdatei.** Die aktuelle Leistungsbeschreibung d.velop invoices (15.12.2025) nennt weder SEPA noch Zahlungsdateien [F][Q1]. Die SEPA-Funktion, mit der d.velop auf der DATEV-Seite wirbt [F][Q7], gehört zur **ecm:one**-App „Invoices for DATEV“. Diese App ist ein eigenes Produkt auf d.velop documents und nicht smart invoice. Sie kostet 50 € je weiterem Mandanten und nutzt teils den abgekündigten Rechnungsdatenservice 2.0 [F][Q8][Q12][Q13].
8. **Omikron** ist die Omikron Systemhaus GmbH & Co. KG in Köln, Hersteller von **multicash** (classic / transfer). multicash importiert Zahlungsdateien aus ERP- und Buchhaltungssystemen und liefert Kontoinformationen zurück. Freigeben lässt sich über Unterschriftsklassen mit Vier-Augen-Prinzip, übertragen wird per EBICS [F][Q20][Q21]. DATEV unterstützt „MULTiCASH und Derivate“ für den Import von Kontoumsätzen [F][Q23].
9. **„BeSync“ ist die eigene Middleware-Plattform von MDIS** („Mit BeSync haben wir unsere eigene Middleware-Plattform entwickelt“) [F][Q24]. Der Katalogvermerk zu 5.5 „Schnittstelle über BeSync“ bedeutet also: MDIS setzt das als Projekt um. Aus d.velop-Sicht ist das eine **Anpassung (A)**.
10. **Empfohlener Zielprozess:** Freigabe in d.velop → Buchungsvorschlag nach DATEV (LDconnect) → Trios bucht (OPOS) → Zahlungsvorschlag in DATEV → SEPA-XML an multicash → Unterschrift der berechtigten Nutzer in multicash → Kontoauszug zurück nach DATEV → **BeSync liest OPOS und meldet „bezahlt“ an d.velop.** Das deckt sich mit der MDIS-Zielarchitektur: „Zahlungen werden über DATEV ausgelöst, auf Basis von d.velop Freigabeprozesse“ [F][A_Livos_DMS_Business_Architektur, S. 2].
11. **Empfohlene Erfüllungsgrade:** **5.1 = K** statt „S“. Grund: Drittanbieter-App, DATEV-Komponenten und Gateway müssen vorhanden sein, Beleg nur als Link. **5.5 = A.** Grund: kein d.velop-Standard, Umsetzung über MDIS BeSync. Ausführung über den DATEV- und Omikron-Standard. Details in Abschnitt 6.

---

## 1. Welche d.velop-Produkte bzw. Connectoren für DATEV gibt es? (Frage 1)

### 1.1 Produktübersicht

| Produkt | Anbieter | Zielsystem DATEV | Was wird übergeben / geholt | Status für Livos | Beleg |
|---|---|---|---|---|---|
| **d.velop invoices – Option „DATEV Rechnungswesen (standardisierte Schnittstelle)“** | d.velop (Technik: LIONDEER) | Kanzlei-Rechnungswesen / Mittelstand Faktura mit ReWe | Buchungsvorschläge + Belegübergabe/-link; Stammdaten | Verfügbar in Betriebsform C1 (Multi-Tenant AWS), H, O; **kostenpflichtig (€)** | [F][Q1] |
| **d.velop invoices – Option „DATEV Unternehmen Online (standardisierte Schnittstelle)“** | d.velop (Technik: LIONDEER) | DUO / Belege online | Belegbilder + Buchungsvorschläge | C1, H; **€** | [F][Q1] |
| **d.velop invoices for DATEV Rechnungswesen** (Bundle) | d.velop | ReWe | „DATEV Schnittstelle mit Belegübergabe und Übergabe der Buchungsvorschläge an DATEV Rechnungswesen“; Voraussetzung: „aus dem Internet erreichbares DATEV System … (DATEVconnect und DATEV Beleganzeige Drittanbieter)“; Hersteller der Schnittstelle: Lion & Deer | Leistungsbeschreibung von 2022; der Store-Link leitet inzwischen auf die Übersichtsseite d-velop.de/software/datev um [F] → vermutlich im Produkt d.velop invoices + Option aufgegangen [A] | [F][Q2][Q7] |
| **d.velop invoices for DATEV Unternehmen Online** (Bundle) | d.velop | DUO | „Übergabe der Buchungsvorschläge“, Belegübergabe an DUO | Leistungsbeschreibung vom 05.07.2023 | [F][Q6] |
| **LDconnect für DATEV Rechnungswesen (Cloud)** | LIONDEER | ReWe über **DATEVconnect** | Stammdaten täglich; Buchungsvorschlag je Rechnung (16 Felder inkl. Dokumentenlink); Rechnungseingangsbuch | Leistungsschein vom 17.11.2025; setzt d.velop invoices voraus | [F][Q3][Q4] |
| **LDconnect für DATEV Stammdaten** | LIONDEER | DATEVconnect | reine Stammdatensynchronisation nach d.velop | „Aktuell nur für d.velop Smart Invoice verfügbar“; ab 100 Mandanten „Individuelles Angebot“ | [F][Q5] |
| **LDconnect für DATEV Unternehmen Online** | LIONDEER | DUO (Belegbilderservice / Rechnungsdatenservice 1.0) | Szenario 1: nur Belegbilder; Szenario 2: Belegbilder + Rechnungsdaten | Preis nach Rechnungsanzahl, nicht nach Mandanten | [F][Q9] |
| **d.velop connect for DATEV** | d.velop / Partner (z.B. EITCO, tribus it) | ReWe | laut Referenz WIAG „nahtlose Kommunikation mit dem DATEV-Rechnungswesen“ (On-Premises, d.velop documents) | Handbücher „connect-datev-admin/-user“ nur nach Login [F][B_02 §9]; Details nicht öffentlich | [F][Q15] |
| **ecm:one Invoices for DATEV** | ecm:one (d.velop-Ökosystem) | DUO (Belegtransfer) oder **Rechnungsdatenservice 2.0** | Buchungssatz + Belegbild; Stammdaten per DATEV-CSV; **Zahlungsvorschlag + SEPA-XML** | **eigene App auf d.velop documents, nicht smart invoice**; 1 Mandant inkl., „zzgl. 50 € je weiterer Mandant“; RDS 2.0 abgekündigt | [F][Q8][Q12][Q13] |
| **DATEV-Marktplatz** | DATEV | – | Liste „DATEV Schnittstellen Anbieter“: „d3.documents von Lion and Deer GmbH“ mit Belegbilderservice Rechnungswesen und Rechnungsdatenservice 1.0 | **Kein** Eintrag „d.velop smart invoice“ oder „LDconnect“ für Buchungsdatenservice gefunden | [F][Q16] |

### 1.2 Welche DATEV-Schnittstellen es gibt und wer sie nutzt

| DATEV-Schnittstelle | Art | Richtung / Inhalt | Wo landen die Daten | Nutzung im d.velop-Umfeld | Beleg |
|---|---|---|---|---|---|
| **DATEVconnect** (Rechnungswesen) | On-Premises-REST-API auf dem DATEV-Server; 0,00 €/Monat | bidirektional: Stammdaten lesen (Kreditoren, Sachkonten, Kostenstellen, Zahlungsbedingungen), **Buchungsvorschläge Eingangsrechnungen schreiben**, OPOS lesen | Kanzlei-Rechnungswesen / Mittelstand Faktura mit ReWe | **LDconnect / d.velop invoices for DATEV ReWe** | [F][Q17][Q18][Q3] |
| **DATEV Beleganzeige Drittanbieter** | Erweiterung von DATEVconnect | Beleglink am Buchungssatz → Beleg wird aus DATEV heraus im d.velop-DMS angezeigt | ReWe | optional bei LDconnect | [F][Q18][Q4]; Preis: einmalig 1.575,00 € + Lizenz nach Staffel [F][Q19] |
| **Buchungsdatenservice** | DATEV-Cloud-Datenservice (EXTF-Buchungsstapel-CSV per API `accounting:extf-files`) | vollständige Buchungssätze, Stammdaten, Belegbilder | DATEV-Rechenzentrum → **muss in Kanzlei-ReWe per „Daten holen“ abgeholt und in der Stapelverarbeitung verarbeitet werden** | **kein d.velop-/LIONDEER-Standard gefunden** | [F][Q25]; [F-S][Q26][Q27] |
| **Rechnungsdatenservice 1.0** (früher „DATEVconnect online“) | Cloud-Datenservice (XML/DXSO, `accounting:dxso-jobs`) | strukturierte Belegdaten + Belegbild → **Buchungsvorschläge** | DUO „Belege online“, von dort in ReWe | d.velop invoices for DUO, LDconnect DUO | [F][Q28][Q29][F-S Q30] |
| **Belegbilderservice** (früher Teil von „DATEVconnect online“) | Cloud-Datenservice | nur Belegbilder | DUO Belege online | LDconnect DUO Szenario 1 | [F][Q9][F-S Q30] |
| **Rechnungsdatenservice 2.0** | Cloud-Datenservice | Rechnungsdaten → Buchungsvorschläge | ReWe/DUO | **abgekündigt: keine Neubestellung seit 01.2026, Einstellung 31.12.2026** → für Livos ungeeignet | [F][Q31][F-S Q32] |
| **EXTF-Buchungsstapel-Datei (DATEV-Format, CSV)** | Dateischnittstelle | Buchungsstapel inkl. Feld „Postensperre“ (0/1) | manueller Import in ReWe | Rückfallebene; nicht automatisiert | [F-S Q33] |

**Hinweis zur Frage nach „DATEVconnect online“:** Dieser Name gilt nicht mehr. DATEV hat den Dienst am 28.09.2020 in **Belegbilderservice** und **Rechnungsdatenservice 1.0** umbenannt [F-S][Q30]. „DATEVconnect“ ohne Zusatz ist die On-Premises-API.

### 1.3 Wie die Übergabe mit LDconnect im Detail läuft [F][Q3]

- **Stammdaten:** „Für alle in der Software konfigurierten DATEV Mandanten erfolgt **auf täglicher Basis**: Abruf der relevanten Stammdaten (**Kreditoren, Sachkonten, Steuerschlüssel, Zahlungsbedingungen, Kreditoren Bankverbindung, KOST1, KOST2**) … Einspielen der Stammdaten in die sogenannten ‚Buckets‘ von d.velop Invoice.“
  - Damit sind die **Kreditor-Bankverbindungen** in smart invoice vorhanden. Das ist die Grundlage für den IBAN-Abgleich Rechnung gegen Stammdaten, den Livos im Termin angefragt hat [A].
  - Mandantenschlüssel in DATEVconnect: Die Client-ID hat das Format `Beraternummer-Mandantennummer`, z.B. `29098-55003` [F][Q14 – Community-SDK, Sekundärquelle].
- **Buchungsvorschlag:** Für jede aus d.velop invoice übergebene Rechnung werden „maximal folgende Informationen je Buchungssatz übertragen: Belegfeld 1; Belegfeld 2; Brutto-Betrag; BU-Gegenkonto; Buchungstext; Datum; **Dokumentenlink**; Geschäftspartner; Konto; KOST1; KOST2; Leistungsdatum; Steuersatz; Steuerschlüssel (BU-Code); Waren und Dienstleistungen; WKZ.“
  - In dieser Feldliste **fehlen Fälligkeit, Skonto, Postensperre und IBAN** [F]. Ob Belegfeld 2, das in DATEV z.B. für ein Fälligkeitsdatum genutzt werden kann, frei belegbar ist, ist offen [O].
- **Rechnungseingangsbuch:** LIONDEER stellt eines bereit (Lieferant, Rechnungsnummer, Beträge, Zahlungsziel, Skonto, interne Buchungsnummer), derzeit kostenfrei, später möglicherweise kostenpflichtig.
- **Bekannte Einschränkungen:**
  - Stammdaten werden „mit der technischen Feldlänge“ übertragen, also mit führenden Nullen.
  - Nur Vorsteuerschlüssel werden synchronisiert.
  - „Buchungsvorschläge werden einem Geschäftsjahr anhand des Rechnungsdatums zugeordnet. Diese Zuordnung erfolgt auch, wenn der Abschluss bereits erfolgt ist.“
- **Voraussetzungen:**
  - DATEV Kanzlei-ReWe oder Mittelstand Faktura mit ReWe.
  - DATEVconnect, immer erforderlich.
  - Beleganzeige Drittanbieter, optional.
  - d.velop invoice.
  - „Der DATEV Server [muss] für uns aus dem Internet erreichbar und für eine bidirektionale Kommunikation freigeschaltet sein“, per IP-Whitelisting. Alternativ das **Datengateway** (Software auf dem DATEV-Server, baut die Verbindung zum Hersteller-Backend auf): „Zum Zeitpunkt der Erstellung ist der Einsatz des Datengateways bei der Nutzung von DATEV SmartIT oder DATEVasp **verpflichtend**.“
  - Ein „dedizierter und entsprechend berechtigter DATEV Benutzer“.
  - „In der Regel erfolgt die Bestellung der DATEV Komponenten durch den Steuerberater.“

### 1.4 Frequenz: ereignisgesteuert oder Batch?

- **smart invoice:** Der Export startet an einer **Schrittverbindung** über das Ereignis `integration.export`, **nicht zeitgesteuert**. Der Exportwert `default`, `validate` oder `book` ist wählbar [F][B_02 §9; 04b 1.9.2].
- **LDconnect:** Die Leistungsbeschreibung beschreibt die Übergabe je Rechnung. Ein Intervall nennt sie nicht [F][Q3]. Daraus folgt: Eine freigegebene Rechnung liegt kurz nach der Freigabe als Buchungsvorschlag in DATEV [A, bestätigen lassen]. Die Katalogforderung „nicht nur pauschal 1× pro Tag“ ist damit **technisch erfüllt** [A].
- **Stammdaten:** nur **täglich** [F][Q3]. Ob ein Abgleich im Tagesverlauf oder auf Knopfdruck möglich ist, ist offen [O].
- **Wichtige Einschränkung:** Der Buchungsvorschlag muss in DATEV von **Trios übernommen bzw. gebucht** werden. „Automatisiert ins DATEV gespielt“ heißt also: Der Vorschlag liegt in DATEV bereit, gebucht ist er damit noch nicht [A].
- **Zum Vergleich der Buchungsdatenservice:** Dort holt die Buchhaltung die Daten aktiv in Kanzlei-ReWe ab („Mandant ergänzen“ → „Daten holen“) und verarbeitet sie in der Stapelverarbeitung [F-S][Q26][Q27]. Bei über 100 Mandanten bedeutet das Arbeit je Mandant [A].

### 1.5 Belegbild und Buchungsvorschlag zusammen übergeben

- **Weg DATEVconnect (LDconnect):** Buchungsvorschlag plus **Dokumentenlink**. Das Belegbild bleibt im d.velop-Archiv. Aus DATEV ist es über die Beleganzeige Drittanbieter zu öffnen [F][Q3][Q4][Q18].
- **Weg DUO (Rechnungsdatenservice 1.0):** „strukturierte Belegdaten und die zugehörigen Belegbilder“ gehen nach Belege online. DATEV erzeugt daraus Buchungsvorschläge für die ReWe-Programme [F][Q28].
- **Kombination:** DATEVconnect „reine Stammdaten-Synchronisation“ plus Belegübergabe über Rechnungsdatenservice 1.0. d.velop beschreibt diese Kombination ausdrücklich [F][Q18].
  - Voraussetzung für Livos wäre, dass es **für jeden der über 100 Mandanten einen DUO-Bestand** gibt [A].
  - Kosten laut DATEV-Preisliste 08/2026: Rechnungsdatenservice 1.0 kostet 2,10 € je Bestand und Monat bis 200 Rechnungen [F][Q19]. Belege online kommt je Mandantenbestand hinzu [F][Q19].

### 1.6 Stammdaten je Mandant, Beraternummer und Mandantennummer

- **Datenmodell:** In DATEV ist jede Gesellschaft ein eigener **Bestand** (Beraternummer + Mandantennummer). LDconnect gleicht alle konfigurierten DATEV-Mandanten ab [F][Q3]. In smart invoice liegen Kreditoren, Sachkonten, Kostenstellen usw. je Bucket, mit Zuordnung zur Mandanten-ID [F][B_02].
- **Service-Limits je Bucket** (d.velop invoices, Leistungsbeschreibung vom 15.12.2025) [F][Q1]:
  - Mandanten: 1.000
  - Kreditoren: 100.000
  - Kreditorbankverbindungen: 100.000
  - Sachkonten: 50.000
  - Kostenstellen: 50.000
  - Buckets insgesamt: höchstens **50**
  - Import-Request: höchstens 30 MB JSON
- **Beispielrechnung [A]:**
  - 110 Mandanten × Ø 900 Kreditoren ≈ 99.000 Kreditoren → an der Grenze eines Buckets.
  - 110 Mandanten × Ø 500 Sachkonten = 55.000 Sachkonten → über der Grenze.
  - Folge: Die Mandanten müssen auf **mehrere Buckets** verteilt werden, oder es werden nur die genutzten Konten übertragen.
  - Zu klären: Livos-Mengengerüst [O] und ob LDconnect Mandanten verschiedenen Buckets zuordnen kann [O].
- **Kreditoren-Konsolidierung:** Ein Lieferant hat in jedem Mandanten eine andere Kreditorennummer, im 70000er- oder 80000er-Kreis [Transkript 00:17:34 Trius]. LDconnect übernimmt diese Nummern **je Mandant 1:1** [A]. Eine gruppenweite Lieferanten-ID mit Konsolidierungsnummer, wie von MDIS vorgeschlagen [Transkript 00:11:45 Thomas Gross], ist **nicht Teil von LDconnect**. Sie gehört in die MDIS-Lieferanten-App bzw. BeSync [A].

### 1.7 Rückmeldung des Zahlstatus (OPOS) aus DATEV

- **LDconnect:** Im Leistungsschein steht keine OPOS-, Zahlstatus- oder „bezahlt“-Rückmeldung [F][Q3]. Der Store nennt eine „Skontoprognose“ aus dem Rechnungseingangsbuch, also aus den d.velop-Daten, nicht aus DATEV-OPOS [F-S][Q4].
- **Technisch möglich über DATEVconnect:** Die Desktop-API „Accounting“ hat die Ressource `accounting/v1/clients/{client}/fiscal-years/{fy}/accounts-payable` (offene Posten der Kreditoren) [F][Q14, Sekundärquelle Community-SDK]. Laut DATEV-Community ist darüber der Zahlstatus bereits gebuchter Rechnungen abrufbar: voll, teilweise oder nicht bezahlt [F-S][Q34].
- **Vergleich mit Wettbewerbern:** DocuWare wirbt mit: „Sachkonten, Kostenstellen, Kreditoren, Debitoren sowie **OPOS, also bezahlte und offene Posten**, können zeitgesteuert automatisch an DocuWare übertragen werden“ [F][Q35]. Livos vergleicht Anbieter. Diese Lücke im d.velop-Standard sollte MDIS deshalb aktiv über BeSync schließen [A].
- **Zusage im Termin:** Thomas Gross verwies auf eine eigene MDIS-DATEV-Schnittstelle aus einem anderen Projekt, „mit auch mit Zahlungsstatus“. Ob sie „in der Rickencloud-Umgebung“ läuft, sei zu prüfen [Transkript 00:14:23 Thomas Gross].

---

## 2. Sonderfall: DATEV beim externen Hoster, Buchhaltung durch Trios (Frage 2)

### 2.1 Ausgangslage aus dem Transkript

- Christian Weigel [00:14:00]: „die Server liegen ja nicht bei Trios, sondern … bei einem externen Dienstleister, weshalb wir die **ricken Cloud** benötigen, um … auf DATEV zuzugreifen und daher ist die Auswertmöglichkeit eingeschränkt“.
- Thomas Gross [00:14:23]: „ob die in der **Rickencloud** Umgebung auch läuft“.
- **Deutung [A, hohe Plausibilität]:** „ricken“/„Ricken“ ist ein Transkriptionsfehler für **Riecken**. Gemeint ist das **Riecken Cloud Gateway für DATEVconnect**. Dafür spricht:
  - Riecken Webservice & Application GmbH (Wien, DATEV-Partner seit 01/2020) bietet genau diesen Dienst an: einen „sicheren Proxy“, der Cloud-Lösungen Zugriff auf DATEVconnect gibt [F][Q10][Q11].
  - DATEV selbst beschreibt den Einsatz in DATEVasp [F][Q36].
  - LIONDEER führt im Leistungsschein „Riecken **Datengateway**“ als Komponente für den Betrieb unter DATEVasp/SmartIT [F][Q3].
  - **Offen [O]:** Nutzt Livos Riecken bereits, und für welche Anwendung? Möglicherweise für die bestehende MDIS-Stammdaten-App [A].

### 2.2 Anbindungswege bei gehostetem DATEV

| Weg | Technik | Was wird benötigt | Pro | Contra | Eignung für Livos |
|---|---|---|---|---|---|
| **W1 – DATEVconnect über Riecken Cloud Gateway / Datengateway** (empfohlen) | LDconnect → Riecken → DATEVconnect auf dem gehosteten DATEV-Server | DATEVconnect auf dem Host-Server; bei DATEVasp das „Zusatzmodul Anbindung Drittanbieter“ (30,75 €/Monat, Art. 42595) [F][Q19][Q36]; Freigabe durch den **DATEV-Systembetreiber** mit Zeichnungsberechtigung per SmartCard/SmartLogin oder ID-Prüfung [F][Q37][Q38]; Festlegung der freigegebenen Mandanten über „Ordnungsbegriffe“ [F][Q37] | Standard-App (LDconnect); bidirektional (Stammdaten, Buchungsvorschläge, später OPOS über BeSync); VPN-verschlüsselt, keine Datenspeicherung im Gateway [F][Q36] | Abhängig von Hoster und DATEV-Systembetreiber; zusätzlicher Vertrag (Riecken/LIONDEER); Verfügbarkeit hängt an drei Parteien [F][Q36] | **Hoch**, falls der Hoster DATEVasp, SmartIT oder ein kompatibler PARTNERasp ist („diverse PARTNERasp Anbieter“) [F][Q36] |
| **W2 – DATEVconnect direkt** | Server des Hosters aus dem Internet erreichbar, IP-Whitelisting | Freischaltung beim Hoster (Firewall/NAT) | kein weiterer Dienstleister | Sicherheitsfreigabe beim Hoster oft nicht möglich [A]; bei DATEVasp/SmartIT nicht vorgesehen, dort ist das Datengateway Pflicht [F][Q3] | Mittel bis gering |
| **W3 – DATEV-Cloud-Datenservices** (Buchungsdatenservice oder Rechnungsdatenservice 1.0 über DUO) | Daten laufen über das DATEV-Rechenzentrum, unabhängig vom Serverstandort | Bestellung je Bestand über „MyDATEV Mandantenregistrierung“ [F][Q19]; DUO-Vertrag je Bestand (bei RDS 1.0); OAuth mit DATEV SmartLogin/SmartCard [F-S][Q39] | hostingunabhängig; Belegbild kann nach DATEV | **Kein d.velop-Standard für den Buchungsdatenservice gefunden**; Pull-Prinzip: Trios muss je Mandant „Daten holen“ [F-S][Q26]; bei über 100 Beständen hoher Einrichtungs- und Betriebsaufwand [A]; keine Stammdaten- und OPOS-Rückrichtung ohne Zusatz [A] | Mittel: Rückfallebene, oder Kombination DATEVconnect für Stammdaten + RDS 1.0 für den Beleg |
| **W4 – EXTF-Datei** | Buchungsstapel-CSV auf Fileshare, manueller Import | – | einfach | nicht automatisiert, fehleranfällig, keine Rückmeldung | nur Notfallweg |

### 2.3 Folgen von mehr als 100 DATEV-Mandanten

- **Lizenz und Preis (Listenpreise, keine Angebote):**
  - LDconnect ReWe Enterprise: 1.035 €/Monat mit 75 Mandanten und 3.000 Rechnungen, je weiterer Mandant 3,45 €, je weitere Rechnung 0,2875 €, Testsystem 49 €/Monat [F][Q4].
  - Rechenbeispiel für 110 Mandanten: 1.035 € + 35 × 3,45 € ≈ **1.156 €/Monat** [A]. Ob sich „Anzahl Rechnungen“ auf Monat oder Jahr bezieht, ist offen [O].
  - LDconnect Stammdaten: „100 oder mehr DATEV Mandanten – Individuelles Angebot“ [F][Q5].
- **DATEV-Rechte:**
  - Der technische DATEV-Benutzer (LDconnect bzw. „Cloudgateway1 DATEVconnect“) braucht Rechte für **alle** Bestände [F][Q3][Q36].
  - Die Datenfreigabe im Gateway steuert der Systembetreiber je Ordnungsbegriff [F][Q37].
  - **Offen [O]:** Liegen alle Livos-Mandanten auf **einem** DATEV-System bzw. unter einer Beraternummer, oder auf mehreren? Mehrere Systeme würden mehrere Gateway-Verbindungen bedeuten.
- **Wer ist DATEV-Systembetreiber und Lizenznehmer?** Livos selbst (selbstbuchend, mit „mandantengenutzter Beraternummer“) oder Trios als Kanzlei? Davon hängt ab, wer bestellt, wer freigibt und wer bezahlt. Laut LIONDEER bestellt „in der Regel … der Steuerberater“ die DATEV-Komponenten [F][Q3] → [O].
- **Buckets in smart invoice:** siehe 1.6. Voraussichtlich mehrere Buckets nötig [A].
- **Betrieb:** 110 Mandanten × täglicher Stammdatenabgleich über das Gateway. Laufzeit und Fehlerbild sind nicht dokumentiert [O].

---

## 3. Zahlungsfreigabe und Zahlungsauslösung (Frage 3)

### 3.1 Was d.velop smart invoice bzw. d.velop invoices beim Zahlen kann

| Aspekt | Befund | Beleg |
|---|---|---|
| Schritt „Zahlungsfreigabe“ im Workflow | Als Workflowschritt modellierbar: „ein Schritt ist … zum Beispiel die sachliche Prüfung oder die **Zahlungsfreigabe**“ | [F][B_02 §2] |
| Zahlungsdaten | Felder Zahlbetrag (`pay_amount`), Skonto (`cashback_percentage1`, `cashback_due_date1`), Zahlungskonditionen und Kreditorbankverbindungen als Stammdaten | [F][B_02; Q1] |
| Zahlungsdatei (SEPA) / Bankanbindung | **In der Leistungsbeschreibung d.velop invoices 2025-12-15 nicht aufgeführt**. Die Funktionsliste enthält weder „SEPA“ noch „Zahlung“ als Funktion | [F][Q1] |
| Übergabe einer Zahlungsfreigabe an DATEV | **Nicht im Standard**: Die LDconnect-Feldliste enthält keine Zahlungs- oder Sperrfelder | [F][Q3] |
| d.velop-Werbeaussage „Generierung von SEPA-Zahlungsdateien, auch außerhalb der DATEV Umgebung“ | Steht auf d-velop.de/software/datev [F][Q7]. Die einzige gefundene Umsetzung ist **ecm:one Invoices for DATEV**: „Fällige Rechnungen werden inklusive erkannter Zahlungsdaten wie IBAN, Skonto und Zahldatum in einem Zahlungsvorschlag bereitgestellt. Nach Freigabe kann eine SEPA-XML-Datei für Ihre Banking-Anwendung erzeugt werden.“ [F][Q8] | [F][Q7][Q8] |
| Eignung von ecm:one für Livos | eigene App auf „d.velop documents platform edition business oder ultimate“, **nicht smart invoice**; „1 Mandant inklusive … zzgl. 50 € je weiterer Mandant“ → bei 110 Mandanten ≈ 5.450 €/Monat nur für die Mandanten [A]; DATEV-Übergabe per Rechnungsdatenservice 2.0 (**abgekündigt zum 31.12.2026**) oder DUO-Belegtransfer; Beispiele für Banking-Software: „SFirm oder ProfiCash“ [F][Q8][Q12][Q31] → **für Livos nicht empfehlenswert** [A] | [F]/[A] |

**Beantwortung der Hypothese aus der Workshop-Vorbereitung** (Katalog Tabelle1, 5.5: „Kann doch eine SEPA-Datei erzeugt oder die Freigabe an DATEV durchgereicht werden, fällt 5.5 von N auf K“): Für **smart invoice** ist im Standard **weder** eine SEPA-Datei **noch** die Weitergabe einer Zahlungsfreigabe an DATEV belegt. Die Hypothese „N im Standard“ bestätigt sich [F/A].

### 3.2 Die DATEV-Seite: OPOS, Zahlungsvorschlag, Zahlungsverkehr

- **Zahlungsvorschlag in Kanzlei-Rechnungswesen:** über Buchführung > Zahlungen aus den fälligen offenen Posten (OPOS), mit Zahlungsbedingungen (Netto, bis zu zwei Skontostufen) [F-S][Q40].
  - Nach Übergabe an den Zahlungsverkehr bekommt der OP ein Zahlungskennzeichen (U* oder S*) und fällt aus weiteren Vorschlägen heraus [F-S][Q40].
- **Sperren:** Für gesperrte Posten erstellt DATEV keinen Zahlungsvorschlag (sinngemäß). Die EXTF-Buchung hat dafür das Feld **„Postensperre“** (1 = gesperrt) [F-S][Q33].
  - So ließe sich „erst buchen, später zur Zahlung freigeben“ abbilden: Buchung mit Postensperre, Sperre wird bei der Zahlungsfreigabe aufgehoben [A].
  - LDconnect überträgt die Postensperre nicht [F][Q3].
  - Ob sich die Sperre über DATEVconnect setzen oder aufheben lässt, ist offen [O].
- **DATEV Zahlungsverkehr:** „Mit dem Zahlungsverkehr können Sie sowohl Ihre eigenen Zahlungen abwickeln als auch Zahlungsaufträge für Ihre Mandanten vorbereiten.“ Übertragung per PIN/TAN, EBICS (bis zu 9 EU) oder Rechenzentrumsverfahren. Die Kanzlei erstellt Vorschläge, der Mandant prüft und gibt frei [F][Q41][Q42].
- **SEPA-Export für externe Bankprogramme:** „DATEV Zahlungsverkehr ermöglicht es, SEPA-Zahlungsaufträge als XML-Datei zu exportieren, die Sie in Bankprogramme oder Bankportale importieren oder als Datei bei Banken einreichen können“ (Hilfe-Dokument 1036491, aktualisiert 06.08.2025) [F-S][Q43]. **Das ist die Standardübergabe DATEV → multicash** [A].
- **Rückweg der Kontoumsätze:** Laut DATEV (LEXinform 1030312) unterstützte Bankprogramme für die Übernahme von Kontoumsätzen: „MULTiCASH und Derivate, MULTiCASH Light, Profi Cash, SFirm …“ [F][Q23]. Alternativ gibt es den DATEV Bankdatenservice [F][Q19].

### 3.3 Was ist Omikron?

- **Omikron Systemhaus GmbH & Co. KG**, Köln, jetzt unter der Marke **multicash** (multicash.com; omikron.de leitet dorthin um). „Seit mehr als 40 Jahren … Zahlungsverkehr und … Cash- & Treasury-Management für weltweit über 100.000 Unternehmen und mehr als 50 Banken.“ [F][Q20]
- **Produkte für Unternehmen:**
  - **multicash classic:** Multibank-Zahlungsverkehr, „Nationale und internationale Zahlungen lassen sich manuell erfassen oder direkt aus ERP- und Vorsystemen importieren … Welche Zahlungen welcher Mitarbeitende erfassen, freigeben und einreichen darf, bestimmt ein frei konfigurierbares Zahlungsklassen-Konzept … einfache digitale Unterschrift, Vier- oder Mehr-Augen-Prinzip“. EBICS/MCFT, webbasiert [F][Q21].
  - **multicash transfer:** Payment Factory, „kommuniziert direkt mit internen ERP-Systemen über standardisierte, unbediente Schnittstellen. So können alle Zahlungsdaten automatisch aus dem ERP entgegengenommen und Kontoinformationen direkt zurückgespielt werden.“ [F][Q22]
- **Anbindung:** „Über frei definierbare Import- und Exportschnittstellen lassen sich Zahldaten und Zahlläufe aus ERP-Systemen, Buchhaltungs- und Vorsystemen importieren, verarbeiten und zurückführen.“ [F][Q21]
- **Status:** Payment Status Reports (PSR, pain.002) lassen sich auswerten, „um fehlerhafte Transaktionen zeitnah nachzubearbeiten“ [F][Q44].
- **Typische Kopplung an DATEV [A, abgeleitet aus Q21/Q23/Q43]:**
  1. DATEV Zahlungsvorschlag → SEPA-XML (pain.001) als Datei.
  2. Import in multicash (Import-Profil bzw. Verzeichnis).
  3. Elektronische Unterschrift durch berechtigte Personen in multicash.
  4. EBICS an die Banken.
  5. Kontoauszüge (camt.053/MT940) aus multicash → Import in DATEV → Zahlungen buchen, OP ausgleichen.

### 3.4 Was ist „BeSync“?

- **BeSync ist die eigene Middleware-Plattform von MDIS:** „Mit BeSync haben wir unsere eigene Middleware-Plattform entwickelt. Während andere Partner auf teure iPaaS-Lösungen wie MuleSoft oder Boomi setzen, integrieren wir Ihre Systeme mit unserer proprietären Technologie.“ und „Nahtlose Integration von ERP, CRM, DMS, HR und beliebigen Drittsystemen … auf unserer BeSync-Plattform.“ [F][Q24]
- **Produktfamilie** laut besync.de, per Suchindex: DataSync (Middleware, „über 220 Vorsysteme“), XSync, AppSync/Appbuilder, LinkSync [F-S][Q45]. Die DataSync-Middleware wird auf wlw.com unter **MDIS Consulting** angeboten [F][Q46].
- **Hinweis:** besync.de selbst war bei der Recherche nicht erreichbar (HTTP 503).
- **Bedeutung für Katalogpunkt 5.5:** „Zahlungsprozess standart, schnittstelle über BeSync“ heißt: Die Omikron-Schnittstelle baut und betreibt MDIS mit der eigenen Middleware. **Das ist eine MDIS-Projektleistung, kein d.velop-Standard** [A]. Das passt zur Aussage im Termin: „das könnten wir über unsere Middleware machen“ [Transkript 00:33:44 Sebastian Pachon].
- **Nicht gefunden:** ein fertiger BeSync-Connector für DATEV oder multicash. BeSync-Referenzen nennen weder DATEV noch Banking [F-S][Q47] → [O].

### 3.5 Empfohlener Zielprozess: „Freigabe in d.velop → Buchung DATEV → Zahlvorschlag/Zahlungsfreigabe → Zahllauf Omikron → Rückmeldung bezahlt“

**Variante A (empfohlen): Zahlung über DATEV, d.velop liefert die fachliche Freigabe.** Sie entspricht der MDIS-Zielarchitektur („Zahlungen werden über DATEV ausgelöst, auf Basis von d.velop Freigabeprozesse“) [F][A_Livos_DMS_Business_Architektur S. 2].

| # | Schritt | System | Verantwortlich | Schnittstelle / Standard | Frequenz | Status in d.velop | Grad |
|---|---|---|---|---|---|---|---|
| 1 | Eingang, Erkennung, Mandant und Kreditor bestimmen, IBAN gegen Kreditorbankverbindung prüfen | smart invoice | System / Clearing | Stammdaten per LDconnect (täglich); Konsolidierungs-ID aus der MDIS-Lieferanten-App über BeSync | laufend | „Eingang“, „In Prüfung“ | S/K (+A für Konsolidierung) |
| 2 | Sachliche Prüfung, Kontierung, Freigabe nach Wertgrenze/Freigabematrix (Mandant) | smart invoice | Fachbereich, Asset Management | – | laufend | „Freigegeben“ | K |
| 3 | **Zahlungsfreigabe** (fachlich: „darf bezahlt werden“, Zahlungsziel, Skonto, Einbehalt/Kürzung, Zahlbetrag) als letzter Freigabeschritt **vor** dem Export | smart invoice | berechtigte Livos-Nutzer | – | laufend | „Zahlungsfreigegeben“ | K |
| 4 | Export → **Buchungsvorschlag + Beleglink** nach DATEV | smart invoice → LDconnect → Riecken Gateway → DATEVconnect | automatisch | LDconnect (Standard-App) | **ereignisgesteuert, je Rechnung** | „An DATEV übergeben“ (Exportstatus) | K |
| 5 | Buchungsvorschlag übernehmen, buchen → OP entsteht | DATEV Kanzlei-ReWe | **Trios** | – | Takt von Trios (mehrmals täglich möglich) | – (keine Rückmeldung im Standard) | Organisation |
| 6 | Zahlungsvorschlag aus OPOS (Fälligkeit, Skonto) → DATEV Zahlungsverkehr → **SEPA-XML-Export** | DATEV | Trios | DATEV-Standard | Zahllauf-Takt (z.B. täglich oder 2× wöchentlich) | – | DATEV-Standard |
| 7 | Import der SEPA-Datei in multicash, **Unterschrift durch berechtigte Livos-Nutzer** (Zahlungsklassen, Vier-Augen), EBICS an die Banken | Omikron multicash | Livos Treasury/Finanzen | multicash-Import; optional automatische Dateiübergabe per BeSync (Verzeichnis/SFTP) | je Zahllauf | – | Omikron-Standard (+A für automatische Dateiübergabe) |
| 8 | Kontoauszüge (camt.053/MT940) → DATEV, Zahlungen buchen, OP ausgleichen | multicash → DATEV | Trios | DATEV-unterstützte Bankprogramm-Schnittstelle bzw. Bankdatenservice | täglich | – | Standard |
| 9 | **Rückmeldung „bezahlt“** (Datum, Betrag, Teilzahlung) an die Rechnung in d.velop | BeSync liest DATEVconnect `accounts-payable` je Mandant → schreibt Eigenschaft „Zahlstatus“ über die d.velop-DMS-API; optional früher Status „ausgeführt“ aus multicash-PSR | automatisch | **BeSync (MDIS)** | z.B. stündlich oder nachts | „Bezahlt“ / „Teilbezahlt“ | **A** |

**Warum die Zahlungsfreigabe vor dem Export liegt [A]:** LDconnect kennt keine Postensperre. Übergibt man schon bei der fachlichen Freigabe, landet die Rechnung als OP ohne Sperre in DATEV. Sie könnte dann in einen Zahlungsvorschlag geraten, bevor die Zahlungsfreigabe in d.velop erteilt ist. Das zweistufige Livos-Bild (Vorerfassungsjournal bei der Verteilung → Verbuchung bei der fachlichen Freigabe → Zahlung bei der Zahlungsfreigabe) [F][A_Livos_DMS_Business_Architektur S. 3] lässt sich im Standard deshalb **nicht 1:1** abbilden. Es gibt zwei Möglichkeiten:
- **(a) Prozess vereinfachen:** Export erst nach der Zahlungsfreigabe. Der Buchungsvorschlag ist damit „zahlbar“, und das Vorerfassungsjournal entfällt oder ist das Rechnungseingangsbuch in d.velop.
- **(b) Anpassung:** BeSync übergibt Buchungen mit Postensperre bzw. einen zweiten Export. Das ist Aufwand und muss technisch geklärt werden [O].

**Variante B (nur auf ausdrücklichen Wunsch): Zahlungsdatei direkt aus d.velop/BeSync.** BeSync erzeugt aus zahlungsfreigegebenen Rechnungen pain.001 je Mandant und Bankkonto und legt sie in multicash ab. **Risiken [A]:**
- Doppelzahlung, wenn Trios parallel einen DATEV-Zahlungsvorschlag erstellt.
- In DATEV sind die Posten nicht als „in Zahlung“ gekennzeichnet.
- Skonto- und Teilzahlungslogik müsste doppelt gepflegt werden.
- Die Verantwortung der Buchhaltung (Trios) wird umgangen.

Variante B passt nicht zu „DATEV = führendes FiBu-System“ [F][Briefing; A_Livos_DMS_Business_Architektur]. Sie würde verbindliche Regeln brauchen, z.B. „d.velop-Rechnungen nie im DATEV-Zahlungsvorschlag“ und eine Postensperre.

---

## 4. Typische Architektur „Rechnungseingang d.velop + DATEV“ in Unternehmensgruppen (Frage 4)

### 4.1 Referenzen

- **Keine öffentliche Referenz** gefunden für d.velop smart invoice + DATEV in einer Gruppe mit über 100 Gesellschaften. Gesucht wurde auf d-velop.de, datev.de/marktplatz und allgemein [F: Suche ohne Treffer]. → **Referenz bei d.velop/LIONDEER anfragen** [O].
- **Gefundene Referenzen:**
  - WIAG Antriebstechnik: d.velop documents On-Premises, „d.velop connect for DATEV“, EITCO invoice processor. Einzelunternehmen [F][Q15].
  - Stiftung Haus Hall: 7 Gesellschaften, aber FiBu **Diamant**, nicht DATEV [F][Q48].
- **Wettbewerber-Maßstab:** DocuWare „Connect to DATEV“ bietet im Standard OPOS-Import und Statusrückgabe nach Stapelimport bzw. EXTF [F][Q35].

### 4.2 Best-Practice-Muster, abgeleitet aus Produktdoku und Limits [A]

```
                 +------------------- d.velop cloud (1 Instanz) --------------------+
 E-Mail/Scan/    | inbound/Mailimport -> smart invoice (1 Workflowdefinition,        |
 XRechnung  ---> |   Eigenschaft "Mandant" = DATEV "BeraterNr-MandantenNr",          |
                 |   Freigabematrix mit Spalte Mandant, Clearing je Mandant)         |
                 |   Buckets: n Stammdaten-Buckets (Mandanten gruppiert, <=50)       |
                 +------+-------------------------------^---------------------------+
        Export-Event    |                               | Stammdaten täglich
        (je Rechnung)   v                               |
                 +-----------------------------------------------+
                 | LDconnect (LIONDEER, Cloud) — Buchungsvorschlag|
                 | + Dokumentenlink; Rechnungseingangsbuch        |
                 +----------------------+------------------------+
                                        | Riecken Cloud Gateway / Datengateway (VPN)
                                        v
    Hoster (DATEVasp/PARTNERasp): DATEV Kanzlei-ReWe + DATEVconnect + Beleganzeige Drittanbieter
         (>100 Bestände, Buchhaltung Trios)  --OPOS-->  BeSync (MDIS)  --Zahlstatus--> d.velop
         DATEV Zahlungsverkehr --SEPA-XML--> Omikron multicash --EBICS--> Banken
         multicash --camt/MT940--> DATEV (OP-Ausgleich) ;  multicash PSR --(opt.)--> BeSync
    MDIS Lieferanten-App (BeSync): Konsolidierungs-ID <-> Kreditor-Nr. je DATEV-Mandant (70000/80000)
    Bim4You: integration.export-Webhook (smart invoice API) -> BeSync -> Bim4You (separat, R-07)
```

**Gestaltungsregeln [A]:**
1. **Eine d.velop-Instanz, eine Workflowdefinition.** Die Gesellschaft ist Pflichteigenschaft. Mandanten-ID = DATEV-Client-ID (`Beraternummer-Mandantennummer`), damit das Mapping zu DATEVconnect eindeutig ist [F für das Format: Q14].
2. **Buckets nach Mengengerüst planen:** Kreditoren und Sachkonten je Bucket begrenzen, z.B. nach Geschäftsbereich (Bestand, Privatisierung, Bau) gruppieren. Das deckt sich mit der Katalog-Übersicht „Bestand, Privatisierung, Bau“ [F][Leistungskatalog].
3. **Eine Connector-Instanz für alle Mandanten** (LDconnect). Keine Einzelschnittstellen je Gesellschaft.
4. **DATEV bleibt führend für Kreditoren je Mandant.** Die gruppenweite Lieferantenidentität kommt aus der MDIS-Lieferanten-App. d.velop bekommt beides: die DATEV-Nummer für die Buchung und die Konsolidierungs-ID für Auswertung und Dublettenprüfung.
5. **Rückmeldekanäle explizit bauen:** Buchungsstatus, OPOS/„bezahlt“ und Fehler (Schnittstellenprotokoll) über BeSync. Sonst fehlt Livos die durchgängige Statuskette „Eingang → … → Bezahlt“ (vgl. R-20 in 04b).
6. **Monitoring:** smart invoice erzeugt nach vier Fehlschlägen in Folge ein „Technisches Problem“ und deaktiviert die Integration nach 7 Tagen ohne Erfolg. Belegt ist das für die Standardintegration Dynamics [F][B_02 §9]. Ob es für LDconnect ebenso gilt, ist offen [O]. Überwachung einplanen.

---

## 5. Kosten-Indikationen (Listenpreise, zur Orientierung, keine Angebotspreise)

| Posten | Preis laut Quelle | Beleg |
|---|---|---|
| d.velop invoices, Edition medium | 750 Rechnungen/Monat, 10 Buchhaltungs-User, beliebig viele Freigabe-User (Preis nicht in der Leistungsbeschreibung) | [F][Q1] |
| Option DATEV Rechnungswesen (standardisierte Schnittstelle) | „€“ (zusätzliche Kosten, Betrag nicht genannt) | [F][Q1] |
| LDconnect für DATEV Rechnungswesen | XSmall 81 € / Small 150 € / Medium 322 € / Large 587 € / Enterprise 1.035 € pro Monat (1/10/25/50/75 Mandanten; 100/250/750/1.500/3.000 Rechnungen); +3,45 € je Mandant; +0,2875 € je Rechnung; Testsystem 49 €/Monat | [F][Q4] |
| LDconnect für DATEV Stammdaten | bis 99 Mandanten 58 €/Monat; ab 100 individuelles Angebot | [F][Q5] |
| DATEVconnect | 0,00 €/Monat (Art. 95280) | [F][Q17][Q19] |
| DATEV Beleganzeige Drittanbieter | einmalig 1.575,00 € + Lizenz nach Staffel (Art. 63183) | [F][Q19] |
| DATEVasp Zusatzmodul Anbindung Drittanbieter | 30,75 €/Monat je Stück (Art. 42595) | [F][Q19] |
| Riecken Cloud Gateway | Tarife Basic/Starter/Professional/Enterprise (Preise nicht erfasst); für den Systembetreiber „normalerweise keine Kosten“ | [F][Q11][Q37] |
| DATEV Buchungsdatenservice (Alternative W3) | je Bestand/Monat nach Staffel: 1,36 € bis 500 Buchungssätze … | [F][Q19] |
| DATEV Rechnungsdatenservice 1.0 (Alternative) | 2,10 € je Bestand/Monat bis 200 Rechnungen | [F][Q19] |
| DATEV Zahlungsverkehr | ab 8,72 €/Monat (Art. 92052) | [F][Q41] |
| ecm:one Invoices for DATEV (nur zum Vergleich) | 100 €/Monat, 1 Mandant inkl., +50 € je weiterer Mandant, +0,12 € je Seite | [F][Q12] |

---

## 6. Folgen für die Katalogpunkte 5.1 und 5.5 (Frage 5)

| ID | Anforderung (Livos) | Eintrag bisher | **Empfehlung** | Begründung | Bedingungen / Vorbehalte |
|---|---|---|---|---|---|
| **5.1** | DATEV-Schnittstelle, Must-Have: „Alle Rechnungen müssen inkl. Belege automatisiert ins DATEV gespielt werden können (nicht nur pauschal 1× pro Tag). Übernahmeprozess in DATEV ist abzustimmen.“ | **S** (Standard) | **K (Konfiguration)** | Übergabe ereignisgesteuert je Rechnung (smart invoice Export-Event [F] + LDconnect je Rechnung [F]) → mehrmals täglich erfüllt [A]. Das ist aber **kein Kernprodukt ohne Anpassung**: Nötig sind eine kostenpflichtige Zusatzoption bzw. die Drittanbieter-App LDconnect [F][Q1][Q4], DATEVconnect und Beleganzeige beim Hoster, ein Gateway (Riecken/Datengateway) und die Freigabe durch den DATEV-Systembetreiber [F][Q3][Q36][Q37]. „Inkl. Belege“ ist über den **Beleglink** erfüllt; ein **Belegbild in DATEV** gibt es nur über DUO/RDS 1.0 [F]. | (1) Der Hoster lässt Riecken bzw. das Datengateway zu (DATEVasp, SmartIT, PARTNERasp) [O]. (2) Trios übernimmt die Buchungsvorschläge; der „Übernahmeprozess in DATEV“ ist abgestimmt. (3) Stammdaten nur täglich. (4) Das **zweistufige Vorerfassungsjournal plus Verbuchung** ist nicht Standard (**A** oder Prozessvereinfachung). (5) Die OPOS-Rückmeldung gehört nicht zu 5.1, sondern zu 5.5/BeSync (**A**). (6) Mandanten mit mehr als 75 kosten extra; Bucket-Limits beachten. |
| **5.5** | Schnittstelle Zahlungsmanagementsystem, Must-Have: „Schnittstelle zu Omikron …, sodass Zahlungen nach Freigabe automatisch ausgelöst werden können für berechtigte Nutzer“ | leer; Notiz „Zahlungsprozess standart, schnittstelle über BeSync“ | **A (Anpassung)**, im d.velop-Standard **N** | smart invoice erzeugt **keine Zahlungsdatei** und gibt **keine Zahlungsfreigabe an DATEV** weiter [F][Q1][Q3]. Es gibt keinen d.velop- oder LIONDEER-Connector zu Omikron [F: nicht gefunden]. **Ausführen** lässt sich die Zahlung über den **DATEV- und Omikron-Standard**: Zahlungsvorschlag → SEPA-XML → multicash-Import → Unterschrift der berechtigten Nutzer → EBICS [F][Q21][Q43]. Die Automatisierung (Dateiübergabe, Status „bezahlt“ zurück nach d.velop) setzt MDIS mit **BeSync** um. Das ist Projektleistung [F][Q24] / [A]. | (1) Die Livos-Governance entscheidet, ob die Zahlungsfreigabe in d.velop (fachlich) plus Unterschrift in multicash (bankseitig) reicht. (2) Rolle von Trios im Zahllauf klären. (3) Variante B (pain.001 direkt aus d.velop) nur mit Regeln gegen Doppelzahlung. (4) Aufwand für BeSync schätzen: DATEVconnect OPOS-Lesen je Mandant, d.velop-DMS-API, multicash-Dateiablage bzw. PSR. |

**Vorschlag für die Anbieterspalte im Katalog:**
- **5.1 → „K“:** „Standardisierte DATEV-Rechnungswesen-Schnittstelle (d.velop/LIONDEER LDconnect über DATEVconnect): Buchungsvorschlag mit Beleglink ereignisgesteuert je freigegebener Rechnung, DATEV-Stammdaten täglich. Beim gehosteten DATEV Anbindung über Cloud Gateway/Datengateway. Belegbild in DATEV optional über DUO/Rechnungsdatenservice 1.0.“
- **5.5 → „A“:** „Fachliche Zahlungsfreigabe in d.velop (Standard-Workflowschritt). Zahlungsausführung über DATEV-Zahlungsvorschlag und SEPA-XML an Omikron multicash (Standard DATEV/Omikron). Automatische Übergabe und Rückmeldung ‚bezahlt‘ über die MDIS-Middleware BeSync (Projektleistung).“

---

## 7. Offene Punkte an d.velop, LIONDEER, DATEV, Livos, Trios, Hoster und Omikron

| ID | An | Frage | Warum / Bezug |
|---|---|---|---|
| OP-DV-01 | d.velop | Ist die Option „DATEV Rechnungswesen (standardisierte Schnittstelle)“ technisch identisch mit LDconnect? Preis und Vertragskonstrukt (Kauf über d.velop oder LIONDEER)? | 5.1; Angebot |
| OP-DV-02 | d.velop / LIONDEER | Handbücher LDconnect bzw. „connect-datev-admin“ bereitstellen (Partner-Login) | R-01 |
| OP-DV-03 | LIONDEER | Wird **sofort je Export-Event** übergeben oder im Batch-Intervall? Wie wirken die Exportwerte `validate` und `book`? Ist ein **zweiter Export** möglich (Vorerfassung, dann Verbuchung)? | 5.1; Livos-Zielbild Vorerfassungsjournal |
| OP-DV-04 | LIONDEER | Stammdaten-Sync **im Tagesverlauf oder auf Knopfdruck** möglich (neuer Kreditor)? Werden nur **genutzte** Sachkonten übertragen? Lassen sich Mandanten auf **mehrere Buckets** verteilen? | 1.6; Bucket-Limits |
| OP-DV-05 | LIONDEER | Ist **Belegfeld 2** frei belegbar (Fälligkeit)? Lässt sich die **Postensperre** übertragen? Gibt es Zusatzfelder (Fälligkeit, Skonto, Zahlweise)? | 3.2; Zahlungsfreigabe |
| OP-DV-06 | LIONDEER | Ist **OPOS/Zahlstatus-Rückmeldung** geplant oder auf Anfrage machbar? | 1.7; Wettbewerb DocuWare |
| OP-DV-07 | LIONDEER / Riecken | Kompatibilität mit dem **konkreten Livos-Hoster** (DATEVasp, SmartIT oder welcher PARTNERasp?). Ist das Datengateway Pflicht? SLA, Latenz, Fehlerhandling, Monitoring | 2.2 |
| OP-DV-08 | d.velop / LIONDEER | Preise ab 100 Mandanten; Bedeutung von „Anzahl Rechnungen“ (Monat oder Jahr?) | 5 |
| OP-DV-09 | d.velop | **Referenzkunde** mit smart invoice + DATEV und vielen Gesellschaften, möglichst Immobilien oder Bau | 4.1; Livos-Entscheidung |
| OP-DV-10 | d.velop | Verhalten bei Schnittstellenfehlern (Technisches Problem, automatische Deaktivierung) auch für LDconnect? | 4.2 Regel 6 |
| OP-LV-01 | Livos | **Wer ist der Hoster** (Name; DATEVasp, SmartIT, PARTNERasp)? Wird „Riecken Cloud Gateway“ schon genutzt, und wofür? | 2.1 (Transkript 00:14:00) |
| OP-LV-02 | Livos / Trios | **Wer ist DATEV-Systembetreiber und Lizenznehmer?** Livos (mandantengenutzte Beraternummer) oder Trios (Kanzlei)? Wer ist zeichnungsberechtigt für die Gateway-Freigabe? | 2.3 |
| OP-LV-03 | Livos / Trios | Liegen alle über 100 Mandanten auf **einem** DATEV-System bzw. einer Beraternummer? Liste der Mandanten mit Berater- und Mandantennummer | 2.3; Mandantenmodell |
| OP-LV-04 | Livos / Trios | Mengengerüst: Kreditoren und Sachkonten je Mandant, Kostenstellen (KOST1/KOST2) | 1.6 Bucket-Limits |
| OP-LV-05 | Livos / Trios | Soll das **Belegbild in DATEV** liegen (DUO) oder reicht der **Beleglink**? Wird DUO heute genutzt? | 1.5; 5.1 „inkl. Belege“ |
| OP-LV-06 | Livos / Trios | Übernahmeprozess in DATEV: Wer übernimmt die Buchungsvorschläge wie oft? Wird das „ER-Vorerfassungsjournal“ wirklich gebraucht? | 5.1; Zielbild S. 3 |
| OP-LV-07 | Livos | **Zahlungsgovernance:** Reicht die fachliche Zahlungsfreigabe in d.velop plus Unterschrift in multicash? Wer sind die „berechtigten Nutzer“? Zahllauf-Rhythmus? Wer erstellt den Zahlungsvorschlag in DATEV: Trios oder Livos? | 5.5; 3.5 |
| OP-LV-08 | Livos | Welches Omikron-Produkt und welche Version (multicash classic oder transfer, Cloud oder On-Prem)? Wie kommen Zahlungsdateien heute hinein (manueller Import oder Verzeichnis)? Gibt es PSR (pain.002)? | 3.3; 5.5 |
| OP-LV-09 | Livos | Wie kommen die Kontoauszüge heute nach DATEV (multicash-Export oder Bankdatenservice)? | 3.5 Schritt 8 |
| OP-DA-01 | DATEV (über Trios) | Lässt sich die **Postensperre** über DATEVconnect setzen bzw. aufheben? Sind `accounts-payable` und DATEVconnect Rechnungswesen in DATEVasp/PARTNERasp über das Gateway verfügbar? | 3.2; 1.7 |
| OP-OM-01 | Omikron | Standard-Importprofil für DATEV-SEPA-XML; automatischer Import aus Verzeichnis/SFTP; API für den Zahlstatus | 3.5 Schritte 7/9 |
| OP-MDIS-01 | MDIS intern | Kann die „dedizierte DATEV-Schnittstelle“ aus dem Projekt „Schadensanierer“ (inkl. Zahlungsstatus) wiederverwendet werden? Läuft sie über das Riecken Gateway? Aufwand BeSync für OPOS → d.velop und für multicash | Transkript 00:14:23; 5.5 |

---

## 8. Methodik und Grenzen der Recherche

- **Ausgewertet:**
  - Leistungsbeschreibungen (PDF) von d.velop invoices (2025-12-15), d.velop invoices for DATEV ReWe (2022-03-02) und DUO (2023-07-05).
  - LDconnect-Leistungsschein (17.11.2025).
  - DATEV-Preisliste für Unternehmen (Stand 08/2026).
  - DATEV-Dokument „Einsatz Cloud Gateway for DATEVconnect in DATEVasp“.
  - Store-Seiten d-velop.de, Seiten von Riecken, multicash.com und MDIS.
- **Nicht direkt abrufbar**, deshalb nur über Suchindex-Auszüge belegt [F-S]:
  - DATEV Wissensplattform bzw. Hilfe-Center (JavaScript, API mit Login).
  - developer.datev.de (JavaScript).
  - DATEV-Community (403).
  - besync.de (503).
  - help.d-velop.de DATEV-Handbücher (Login).
- Die DATEVconnect-Ressourcen (`accounts-payable`, `posting-proposals-incoming-invoices/batch`, `creditors`, `general-ledger-accounts`, `cost-centers`, `terms-of-payment`) stammen aus einem öffentlichen Community-SDK (MIT-Lizenz), also einer **Sekundärquelle**. Vor der Umsetzung im DATEV Developer Portal prüfen.
- Alle Preise sind Listenpreise laut Quelle und **ohne Gewähr**. Sie dienen nur zur Einordnung.

---

## 9. Quellenverzeichnis

| Nr | Quelle | URL |
|---|---|---|
| Q1 | Leistungsbeschreibung d.velop invoices, Version 2025-12-15 (Service Limits, DATEV-Optionen €) | https://s3.eu-central-1.amazonaws.com/mediamanager.cloudcenter.service.d-velop.cloud/573e2063-a5b1-4195-82a7-5ab9f93b46de |
| Q2 | Leistungsbeschreibung d.velop invoices for DATEV Rechnungswesen, Version 2022-03-02 | https://s3.eu-central-1.amazonaws.com/mediamanager.cloudcenter.service.d-velop.cloud/680f2d09-0a3a-49d5-a2c8-56f7165cc0ee |
| Q3 | Leistungsschein LDconnect für DATEV Rechnungswesen (Cloud), Stand 17.11.2025 | https://s3.eu-central-1.amazonaws.com/mediamanager.cloudcenter.service.d-velop.cloud/82f418b4-8a85-4687-a9ff-53f938f690a3 |
| Q4 | d.velop Store: LDconnect für DATEV Rechnungswesen (Preise, Voraussetzungen) | https://www.d-velop.de/store/liondeer-ldconnect-datev-rechnungswesen |
| Q5 | d.velop Store: LDconnect für DATEV Stammdaten | https://www.d-velop.de/store/liondeer-ldconnect-datev-stammdaten |
| Q6 | Leistungsbeschreibung d.velop invoices for DATEV Unternehmen Online, Version 2023-07-05 | https://s3.eu-central-1.amazonaws.com/mediamanager.cloudcenter.service.d-velop.cloud/be5e4349-ebfa-4fe2-ae4f-9608677d53b3 |
| Q7 | d.velop: „d.velop Produkte nahtlos in DATEV integriert“ (inkl. „Generierung von SEPA-Zahlungsdateien“) | https://www.d-velop.de/software/datev |
| Q8 | ecm:one: DATEV-Integration (Rechnungsdatenservice 2.0, SEPA-XML; aktualisiert 24.08.2026) | https://www.ecmone.de/integrationen/datev/ |
| Q9 | d.velop Store: LDconnect für DATEV Unternehmen Online | https://store.d-velop.com/de/LD-connect-fuer-DATEV-Unternehmen-Online/10002180 |
| Q10 | Riecken: Cloud Gateway & MCP for DATEV / Über uns | https://cloudgateway.riecken.io/ · https://cloudgateway.riecken.io/ueber-uns.html |
| Q11 | Riecken: Produkt Cloud Gateway (DATEVasp, SmartIT, On-Prem; SmartLogin) | https://cloudgateway.riecken.io/produkt.html |
| Q12 | d.velop Store: ecm:one Invoices for DATEV (Preise, Zahlungsvorschlag/SEPA) | https://www.d-velop.de/store/ecm-one-invoices-for-datev-e-rechnungen |
| Q13 | (wie Q8, Tabelle Schnittstellen/Voraussetzungen) | https://www.ecmone.de/integrationen/datev/ |
| Q14 | Community-SDK DATEV (PHP, MIT): Endpunkte DATEVconnect Accounting (`accounts-payable`, `posting-proposals-incoming-invoices/batch`, Client-ID-Format) – Sekundärquelle | https://github.com/Daniel-Jorg-Schuppelius/datev-php-sdk |
| Q15 | d.velop Referenz WIAG Antriebstechnik (d.velop connect for DATEV, EITCO) | https://www.d-velop.de/referenz/wiag-antriebstechnik |
| Q16 | DATEV-Marktplatz: DATEV Schnittstellen Anbieter („d3.documents von Lion and Deer GmbH“) | https://www.datev.de/web/de/marktplatz/datev-schnittstellen-anbieter |
| Q17 | DATEV Shop: DATEVconnect | https://www.datev.de/web/de/shop/produkt-details/datevconnect-95280 |
| Q18 | d.velop Blog: DATEV Schnittstellen im Rechnungswesen (10.05.2022) | https://www.d-velop.de/blog/software-erleben/datev-schnittstellen/ |
| Q19 | DATEV-Preisliste für Unternehmen, Stand 08/2026 | https://www.datev.de/content/dam/markenassets/preislisten/DATEV-Preisliste_fuer_Unternehmen.pdf |
| Q20 | multicash.com (Omikron Systemhaus GmbH & Co. KG) | https://www.multicash.com/ |
| Q21 | multicash classic | https://www.multicash.com/loesungen/unternehmen/multicash/ |
| Q22 | multicash transfer / ERP-Integration (Umleitung von omikron.de) | https://www.multicash.com/loesungen/unternehmen/multicash/erp-integration/ |
| Q23 | kmk: Übermittlung digitale Bankumsätze in das DATEV Rechnungswesen (zitiert LEXinform 1030312: „MULTiCASH und Derivate“) | https://www.kmk.info/common/images/uebersicht_uebertragung_digitale_bankdaten_tabelle.pdf |
| Q24 | MDIS: MDIS One („Mit BeSync haben wir unsere eigene Middleware-Plattform entwickelt“) | https://mdis-consulting.de/loesungen/mdis-one/ |
| Q25 | DATEV Shop: Buchungsdatenservice | https://www.datev.de/web/de/shop/produkt-details/datev-buchungsdatenservice-91000 |
| Q26 | Lexware Steuerkanzlei-Hilfe: DATEV Buchungsdatenservice („Daten holen“, Stapelverarbeitung) | https://steuerberater.help.lexware.de/de/articles/603501-datev-buchungsdatenservice |
| Q27 | DATEV Hilfe 1008036: Buchungsdatenservice – Buchungsstapel und Stammdaten im Rechenzentrum holen [F-S] | https://wissensplattform.apps.datev.de/help/document/1008036 |
| Q28 | DATEV Shop: Rechnungsdatenservice 1.0 | https://www.datev.de/web/de/shop/produkt-details/datev-rechnungsdatenservice-1 |
| Q29 | apideck: DATEV API Integration Guide (EXTF-/dxso-Jobs, asynchron) | https://www.apideck.com/blog/datev-api-integration-guide |
| Q30 | DATEV magazin: DATEVconnect online umbenannt [F-S] | https://www.datev-magazin.de/produkte-services/datevconnect-online-umbenannt-51888 |
| Q31 | JTL-Forum: Abkündigung DATEV Rechnungsdatenservice 2.0 (04.11.2025) | https://forum.jtl-software.de/threads/abkuendigung-datev-rechnungsdatenservice-2-0.241685/ |
| Q32 | DATEV Hilfe 1048511: Einstellung DATEV Rechnungsdatenservice 2.0 [F-S] | https://help-center.apps.datev.de/documents/1048511 |
| Q33 | DATEV Hilfe 1008722: Zahlungen erstellen – einzelne Konten/Posten fehlen (Postensperre) [F-S]; EXTF-Feld Postensperre | https://apps.datev.de/knowledge/redirects/v1/info-db/1008722 |
| Q34 | DATEV-Community: DATEVConnect Desktop API – Zahlungsstatus/Buchungen einer Rechnung [F-S] | https://www.datev-community.de/t5/Betriebliches-Rechnungswesen/DATEVConnect-Desktop-API-Zahlungsstatus-Buchungen-einer-Rechnung/td-p/416810 |
| Q35 | DocuWare: DocuWare in DATEV integrieren (OPOS zeitgesteuert, Statusrückgabe) | https://start.docuware.com/de/docuware-in-datev-integrieren |
| Q36 | DATEV: Einsatz Cloud Gateway for DATEVconnect in DATEVasp (PDF) | https://www.datev.de/content/dam/markenassets/themen-und-produktgruppen/mydatev/pdf/datevasp_smartit/einsatz_cloud_gateway_for_datevconnect_in_datevasp.pdf |
| Q37 | Riecken Docs: DATEV-System-Zugriff (Server-Owner) | https://docs.cloudgateway.riecken.io/docs/datev-server-owner/intro/ |
| Q38 | Riecken Docs: DATEV System anbinden | https://docs.cloudgateway.riecken.io/docs/general/add-datev-system/ |
| Q39 | Circula Help: DATEV-Datenservices für Mandanten bestellen (mandantengenutzte Beraternummer) [F-S] | https://help.circula.com/en/articles/279451-ordering-datev-data-services-for-clients |
| Q40 | DATEV Hilfe 1070428 OPOS – Fälligkeiten und Zahlungsbedingungen; 1036102 Zahlungen buchen [F-S] | https://help-center.apps.datev.de/documents/1070428 · https://apps.datev.de/help-center/documents/1036102 |
| Q41 | DATEV Shop: Zahlungsverkehr | https://www.datev.de/web/de/shop/produkt-details/zahlungsverkehr-92052 |
| Q42 | DATEV: Zahlungen einfach & sicher für Unternehmen abwickeln | https://www.datev.de/web/de/unternehmen/loesungen/rechnungswesen/mahnen-und-zahlen/zahlungen-einfach-und-sicher-abwickeln |
| Q43 | DATEV Hilfe 1036491: SEPA-Zahlungsaufträge exportieren und importieren (Stand 06.08.2025) [F-S] | https://apps.datev.de/help-center/documents/1036491 |
| Q44 | multicash Payment Formats + (PSR-Auswertung; Umleitung von omikron.de/…/payments-and-channels) | https://www.multicash.com/loesungen/unternehmen/multicash/payments-and-channels/ |
| Q45 | BeSync (Produktseiten DataSync/XSync/AppSync) [F-S; Seite 503] | https://besync.de/produkte/datasync |
| Q46 | wlw.com: MDIS Consulting – DataSync Middleware (BeSync) | https://www.wlw.com/en/company/mdis-consulting-1923195/products/datasync-middleware-fuer-effiziente-echtzeit-datenkommunikation-36053983 |
| Q47 | itiko/PresseBox: Autohaus Ostermaier – BI von MDIS, Middleware von BeSync (19.09.2024) | https://www.itiko.de/artikel/2125222/autohaus-ostermaier-gruppe-optimiert-seine-systemlandschaft-mit-bi-l-sung-von-mdis-und-middleware-von-besync.html |
| Q48 | d.velop Referenz Stiftung Haus Hall (7 Gesellschaften, Diamant) | https://www.d-velop.de/referenz/stiftung-haus-hall |

Interne Quellen: `SP/txt/C_Transkript_Livos_Demo.txt` (Zeitstempel wie zitiert), `SP/txt/A_Leistungskatalog_Rechnungsmanagement_xlsx.txt` (5.1, 5.5, Tabelle1), `SP/txt/A_Livos_DMS_Business_Architektur_pdf.txt` (S. 2–3), `SP/txt/B_02_Eingangsrechnungen_smart_invoice.md` §9, `SP/work/04b_dvelop_faehigkeiten_B.md` §1.9, §7.
