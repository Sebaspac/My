# 01 – Transkript-Analyse Demo-Termin d.velop mit Livos

**Quelle:** `SP/txt/C_Transkript_Livos_Demo.txt`, 495 Zeilen, ca. 14.360 Wörter, Laufzeit [00:00:03] bis [01:14:13], also rund 74 Minuten. Das Transkript wurde vollständig und lückenlos gelesen.
**Ergänzend herangezogen:** `A_Leistungskatalog_Rechnungsmanagement_xlsx.txt` (Katalog-IDs, Prioritäten, MDIS-Spalte F), `A_Agenda_Livos_pptx.txt`, `00_LIESMICH_Zuerst-lesen.md`, `A_06_Architektur_Demo-Instanz.txt`, `A_07_Testdaten_alle.txt`. Die Recherchedateien `B_00`, `B_02`, `B_04` und `B_06` dienten nur dazu, die Aussagen in Kapitel 6 zu plausibilisieren.
**Stand:** 26.09.2026

**Legende**
- Zitierweise: `[hh:mm:ss Sprecher]`. Wörtliche Zitate stehen in „…" und enthalten die Transkriptionsfehler unverändert. Auslassungen sind mit „…" markiert, sinngemäße Ergänzungen mit [eckigen Klammern].
- **Fakt** = im Transkript belegt · **Annahme** = Schlussfolgerung der Analyse · **Offen** = im Termin nicht geklärt.
- **[RISIKO]** = Aussage mit Zusage- oder Haftungsrisiko · **[PRÜFEN]** = fachlich fragwürdig oder durch die Recherche (B-Dateien) nicht gedeckt · **[WIDERSPRUCH]** = widerspricht einer anderen Aussage im Termin oder dem Leistungskatalog.
- Die automatische Transkription enthält viele Hörfehler, etwa „Develop/Deveno/Development" für d.velop, „Libus" für Livos und „Mittelwehr/Windelware" für Middleware. Die Auflösung steht in Kapitel 11.

---

## 0 Vorab-Befunde und Korrekturen zum Briefing

1. **André Töpper gehört zu Livos (Kunde), nicht zu d.velop.** Das Briefing vermutete „d.velop/Consultant"; das ist widerlegt.
   - „Wir haben ja insgesamt über 100 … Gesellschaften, die wir betreuen" [00:05:51 und 00:06:00 André Töpper]
   - „wir haben noch andere Anbieter angehört und werden uns danach intern logischerweise austauschen" [00:23:21 André Töpper]
   - „wir haben an sich den Wunsch, in dieser Woche vielleicht mal ein Angebot zu erhalten" [01:10:22 André Töpper]
2. **Im Termin ist kein d.velop-Mitarbeiter erkennbar.** Die Demo führt **Sebastian Pachon (MDIS)**. Er steht nicht auf der Agenda-Folie, dort sind Thomas Groß, Valeria Filimonow und Annalena Groß aufgeführt. Annalena Groß spricht im gesamten Termin nicht.
3. **MDIS ist bereits Dienstleister von Livos** (Middleware, Stammdaten-App, BI-/Data-Warehouse-Projekt). Belege:
   - „Sie kennen sie ja" [00:00:03 Valeria Filimonow]
   - „im Rahmen des BI Projektes" [00:06:37 Thomas Gross]
   - „wir haben euch die Daten schon angebunden" [00:10:12 Thomas Gross]
   - „Das ist die App, die wir haben, Tanja. Die App, wo du die Stammdaten pflegst." [00:40:09 André Töpper]
4. **Der von MDIS ausgefüllte Leistungskatalog lag Livos zum Termin noch nicht vor.** „Den haben wir noch nicht von ihm." [01:11:36 André Töpper]. Thomas Gross ging davon aus, er sei schon verschickt [01:11:32].
5. **Die sechs offenen Fragen der Agenda-Folie 4 wurden nicht systematisch behandelt:** 1.1 Mandantenmodell, 2.2 Trefferquote, 4.2 Ad-hoc-Freigabe, 5.1 DATEV-Frequenz, 5.5 Omikron und das Lizenz-Mengengerüst. Der Begriff „Omikron" fällt im gesamten Transkript nicht. „BIM" fällt nur einmal, im Einstieg [00:00:22].
6. **Datum:** Das Transkript nennt kein Datum. Laut Briefing und LIESMICH fand der Termin am Dienstag, 22.09.2026, statt. Sebastian sagt allerdings „die aktuellste Rechnung ist der 23.9., Das ist nämlich die gleiche, die wir gerade eben auch im System hinterlegt haben" [00:26:35]. Das ist vermutlich ein Beleg- oder Eingangsdatum der Demo; **offen**.

---

## 1 Teilnehmer & Rollen

### 1.1 Personen und Organisationen

| Person (Label im Transkript) | Seite | Rolle / Funktion | Belege | Einordnung |
|---|---|---|---|---|
| **Valeria Filimonow** | MDIS | Sales (laut Agenda-Folie). Eröffnet den Termin, betont den interaktiven Charakter und übergibt an Sebastian. Später erinnert sie Thomas daran, den Bildschirm zu teilen. | [00:00:03], [00:01:05], [01:12:49] | Fakt; Rolle laut Agenda |
| **Sebastian Pachon** | MDIS | Präsentator und Consultant der gesamten d.velop-Demo, mit rund 6.800 Wörtern Hauptredner. Spricht von „unsere Middleware", „unsere Demo-Instanz" und „bei uns intern und auch bei unseren Kunden". Offene Fachfragen nimmt er zur Klärung „mit dem Herrn Groß" mit. | [00:01:09], [00:33:44], [00:36:37], [00:46:22], [01:09:48] | Fakt: MDIS. Titel/Funktion: Annahme |
| **Thomas Gross (Groß)** | MDIS | CEO (Agenda). Kommt verspätet dazu; André begrüßt ihn bei [00:05:51]. „ich war für den Termin gar nicht geplant" [00:22:50]. Verlässt den Termin kurz („ich komme gleich wieder dazu" [00:23:38]) und ist ab [01:05:44] bzw. [01:09:09] wieder aktiv. Themen: Stammdaten-Architektur, Lieferanten-App, KI-Integrationsplattform, DATEV-Schnittstelle, Angebot. | [00:06:37]–[00:23:38], [01:09:09]–[01:14:10] | Fakt |
| **Annalena Groß** | MDIS | ERP Consultant (Agenda). Keine Wortbeiträge. In der Demo erhält sie eine Aufgabe („Ich schick sie an Anna Lena"). | [00:59:49], [01:00:10] | Anwesenheit **offen** |
| **André Töpper** | **Livos** | Gesprächsführer der Kundenseite mit 169 Beiträgen. Stellt die meisten Fachfragen, fordert das Angebot an und kündigt die interne Management-Entscheidung an. Hat tiefe Prozesskenntnis (Kürzungen, Abschläge, Freistellung, Property Manager). | [00:00:22], [00:06:00], [00:23:21], [01:10:22] | Fakt: Livos. Funktion (z. B. Projektleitung, Leitung Rechnungswesen oder Asset/Bau): **Annahme** |
| **Christian Weigel** | **Livos** | Themen: Buchungen der Hausverwaltungen, bidirektionaler Kreditorenabgleich, Server-Hosting und DATEV-Zugriff, Auswertung von Prozesszeiten je Benutzer. André nennt ihn als jemanden, der „wenn er die Berechtigung hat" für Kranke eine Vertretung setzen könnte. | [00:12:13], [00:13:38], [00:14:00], [00:35:18], [01:05:21] | Fakt: Livos. Funktion (Finanzen/Controlling/IT-nah, evtl. Führungskraft): **Annahme** |
| **Tanja Brecht** | **Livos** | Operativer Rechnungs- und Zahlungsprozess: Zahllauf, Aufgabenliste, Rückweisung, Kürzung, Abschläge, Freistellungsbescheinigung, Ausbuchungen auf Mietkonten. Pflegt Stammdaten in der bestehenden App. André bittet sie, seine 95-%-Angabe zu korrigieren. | [00:15:18], [00:16:32], [00:26:27], [00:37:12], [00:40:09], [00:44:49], [00:48:12] | Fakt: Livos. Funktion (Buchhaltung/Rechnungsprüfung): **Annahme** |
| **„Trius"** (Sprecherlabel) | Livos-Seite | Fachliche Beiträge: DATEV-Schlüssel [00:11:26], 70000er/80000er-Kreditorenkreise [00:17:34], Freigabe von HV-Rechnungen durch das Asset Management [00:20:45], Vollständigkeit [00:22:41], E-Rechnung [00:46:54]. Daneben viele Störfragmente („I'm going", „Picking", „Football", „Cut"). Duzt André: „Andre, darf ich noch ganz kurz …" [00:20:37]. | s. links | Fakt: Kundenseite, per Du mit André. **Annahme:** Das Label ist eine Fehltranskription von „Trios", also Raum-, Geräte- oder Teilnehmername der Buchhaltungsgesellschaft Trios; womöglich teilen sich mehrere Personen ein Mikrofon. Identität **offen** |
| **Trios** (Organisation, nur erwähnt) | Livos-nah | Bucht in DATEV und prüft die PM-Buchungen [00:16:17]. Erhält die Rechnungen „im Monatspaket" [00:21:57]. Bezahlt die PM-Rechnungen nicht [00:21:46]. Die Server liegen „nicht bei Trios" [00:14:00]. | s. links | **Annahme:** Buchhaltungs- oder Servicegesellschaft (konzernintern oder extern) |
| Steuerberater (nur erwähnt) | extern | Die Buchen-Maske könnte eventuell nur „unsere Steuerberater" erhalten. | [00:33:28 André Töpper] | Verhältnis zu Trios **offen** |
| Property Manager / Hausverwaltungen | extern | Etwa „10 verschiedene Property Manager, die sich auch immer wieder wechseln können". Sie prüfen, geben frei und zahlen rund 95 % der bei ihnen eingehenden Rechnungen. | [00:13:08], [00:15:18] | Fakt |
| Asset Management (Livos) | Livos | Gibt HV-gebuchte Rechnungen ab „gewissen Größenordnungen" frei. So das Verständnis von „Trius"; Tanja relativiert. | [00:20:45], [00:21:07] | Fakt (Aussage); Details offen |
| Korsmeier | Livos | Von André als Beispiel für einen Vertreter genannt. | [01:05:21] | Name Fakt, Rolle offen |
| „Herr Walther", „Herr Michael" | Livos? | Thomas: „der Herr Walther hat das Recht" [00:17:07], „der Herr Michael hat dahingehend recht" [00:18:01]. Inhaltlich bezieht sich das auf Christian Weigels Einwand zu doppelten Kreditorennummern. | [00:17:07], [00:18:01] | **Annahme:** Fehltranskription von „Herr Weigel" |
| „Mardera" | MDIS | Thomas: „Mardera, kannst du mal schnell oder ich öffne mal". | [01:11:52] | **Annahme:** gemeint ist Valeria |
| Externer IT-Dienstleister | extern | Hostet die Server von Livos. Der Zugriff auf DATEV läuft über die „ricken Cloud". | [00:14:00 Christian Weigel] | Fakt; Name offen |
| Referenzkunde MDIS | – | „Deutschlands größter Schadensanierer, 130 Servicemitarbeiter", mit dedizierter DATEV-Schnittstelle. | [00:14:23 Thomas Gross] | Fakt (Aussage MDIS), nicht verifiziert |

### 1.2 Sprechanteile (automatisch gezählt)

| Sprecher | Beiträge | Wörter | Seite |
|---|---|---|---|
| Sebastian Pachon | 122 | 6.777 | MDIS |
| Thomas Gross | 106 | 2.461 | MDIS |
| André Töpper | 169 | 2.397 | Livos |
| Tanja Brecht | 37 | 509 | Livos |
| Christian Weigel | 24 | 415 | Livos |
| „Trius" | 33 | 272 (davon viele Störfragmente) | Livos-Seite |
| Valeria Filimonow | 4 | 80 | MDIS |

**Befund:** MDIS hat rund 72 % Redeanteil (9.318 von 12.911 Wörtern; Präsentation). Auf Kundenseite fragt fast nur André; Tanja bringt die operativen Detailfragen ein.

---

## 2 Chronologischer Ablauf

| Block | Zeit | Thema | Inhalt (2–4 Sätze) |
|---|---|---|---|
| B01 | [00:00:03]–[00:01:16] | Eröffnung und Rahmen | Valeria verweist auf die vorab verschickte Agenda und wünscht ausdrücklich Zwischenfragen („keine Frontbeschallung"). André möchte direkt einsteigen. Er stellt fest, dass MDIS noch keine Rückmeldung zu „den Punkten der Liste" gegeben hat, also zum Leistungskatalog, und dass im Angebot abgedeckte und noch zu klärende Punkte getrennt werden sollen, etwa die BIM-Anbindung. Danach Übergabe an Sebastian und Bildschirmfreigabe. |
| B02 | [00:01:20]–[00:04:13] | d.velop-Grundprinzip und Rechnungsupload | Sebastian zeigt das anpassbare Dashboard und erklärt: d.velop „legt … nicht in Ordnern ab, es beschriftet Dokumente und baut Ordner daraus selbst". Die Akten sind vorab definiert, hier Kreditorenakte und Objektakte mit den Dokumentarten Auftrag, Bescheinigung und Eingangsrechnung. Über den „Rechnungsleser" werden drei Testrechnungen hochgeladen, per OCR ausgelesen und klassifiziert. |
| B03 | [00:04:13]–[00:05:29] | Postfach-Import und Validierung | André fragt, ob alle Anhänge eines Mailpostfachs automatisch verarbeitet werden; Sebastian bejaht. In der Demo trägt Sebastian die Lieferantennummer **manuell** nach und speichert. Er nennt Hintergrund-Workflows (Dublettenprüfung, Umsatzsteuerprüfung) und erklärt den „Stapel" als offene Belege. |
| B04 | [00:05:29]–[00:12:13] | Stammdaten Lieferant/Kreditor I | André: Viele Kreditoren sind in vielen der über 100 Gesellschaften mit unterschiedlichen Nummern angelegt. Woher kommt die Lieferantennummer, was gilt bei Kreditoren, die in DATEV noch fehlen? Thomas empfiehlt einen zentralen Lieferantenstamm in einer eigenen App mit mandantenübergreifender Konsolidierungsnummer; die DATEV-Kreditorennummern werden dort nur referenziert. Auf Andrés Sorge vor dem Initialaufwand bietet er ein KI-Mapping über die MDIS-KI-Plattform als kostenlosen PoC an. |
| B05 | [00:12:13]–[00:20:29] | Stammdaten II: Hausverwaltungen | Christian: Die Hausverwaltungen buchen selbst, Livos übernimmt die Buchhaltungsdaten über eine Schnittstelle, neue Kreditoren entstehen dabei auch bei den HV. Er zweifelt, ob der Abgleich wegen des externen Hostings („ricken Cloud") funktioniert; Thomas: „Das muss man prüfen." Tanja umreißt den Scope: alle Nicht-Verwalter-Rechnungen durch d.velop bis zum Zahllauf. „Trius" erklärt die getrennten Kreditorenkreise 70000 (intern) und 80000 (HV); Thomas verortet die Konsolidierung in der Stammdaten-App und nicht in d.velop (drei Nummernkreise, Nummerngenerierung „aus Developer heraus", KI-Abgleich, PoC kostenlos). |
| B06 | [00:20:37]–[00:23:38] | HV-Rechnungen mit Asset-Management-Freigabe | „Trius": Größere HV-gebuchte Rechnungen werden vom Asset Management freigegeben. Thomas schlägt ein eigenes Freigabe-Postfach vor, einen reinen Freigabeprozess in d.velop und eine Freigabe-Mail an die HV. Tanja, „Trius" und André reagieren positiv (Transparenz, Vollständigkeit, „kleines On-Top"); Christian mahnt, dass dies ein separater Prozess ist. Thomas schlägt einen unbezahlten Prozess-Workshop von 2–3 Stunden vor. André will das erst nach der Anbieterentscheidung, der Prozess sei noch nicht festgelegt. |
| B07 | [00:23:40]–[00:25:23] | Datenquelle der Erkennung, IBAN | André fragt, ob die Werte aus dem Dokument oder aus den Stammdaten (DATEV/Middleware) kommen. Sebastian: „Sowohl als auch", eine Frage der Konfiguration; unbekannte Kreditoren können manuell angelegt werden, die Übertragung an DATEV übernimmt später eine Schnittstelle. Den Hinweis auf eine abweichende IBAN sagt er „selbstverständlich" zu, mit Human-in-the-loop. |
| B08 | [00:25:25]–[00:31:41] | Workflow: Verteilung und sachliche Prüfung | Gezeigt werden die E-Mail-Benachrichtigung zur neuen Aufgabe und das Rechnungseingangsbuch (226 Demo-Rechnungen) mit Filter und Gruppierung nach Schritt; Tanja fragt, ob die Mails abschaltbar sind (ja). Die Verteilungsmaske enthält Pflichtfelder, Zahlungsbedingungen/Skonto, Fälligkeit, Sachkonto, Kostenstelle, Kostenträger, Gesellschaft und den sachlichen Prüfer (Team). Andrés Fälligkeitsfrage beantwortet Sebastian mit „Einstellungssache". Die sachliche Prüfung ist schreibgeschützt und wird per Häkchen erteilt. Auf die Frage nach der Mandantenerkennung antwortet Sebastian: „Das ist korrekt." |
| B09 | [00:31:42]–[00:35:18] | Freigabe, Buchhaltung, Historie | Nach der Freigabe (Vier-Augen-Prinzip) wird der Beleg an die FiBu bzw. DATEV weitergeleitet; im Schritt „Buchhaltung" sind Historie, Notizen und Dokumentdetails sichtbar. André: Nachweise lassen sich anhängen (ja); die Buchen-Maske könnte nur der Steuerberater bekommen, die Zahlung beim Buchen auslösen. Sebastian: „über unsere Middleware". André nennt das ein „Gedankenspiel". Sebastian erwähnt Vertrags- und Dokumentprozesse sowie die Kopplung an ein Projektmanagementsystem. |
| B10 | [00:35:18]–[00:37:11] | Auswertung Durchlaufzeiten | Christian möchte Prozesszeiten je Schritt und je Benutzer auswerten. Sebastian: Das „kann … Develop insofern nicht abdecken", möglich sei es über eine eigene App oder ein Middleware-Dashboard. André fragt nach Evidanza; Sebastian nimmt das zur Klärung mit Herrn Groß mit. |
| B11 | [00:37:12]–[00:41:21] | Rückweisung, Dubletten, Mietkonten | Tanja fragt nach automatisierter Rückweisung per E-Mail an den Lieferanten und nach Freigaben für Ausbuchungen auf Mietkonten. André präzisiert: 5 Standardgründe und automatische Mail, ohne das eigene Mailprogramm zu öffnen. Sebastian: Ablehnen geht, die Kommunikation mit dem Kreditor aber „nicht über Develop direkt", sondern über die Middleware; d.velop sei „kein E-Mail-Kommunikationstool". André äußert Skepsis gegenüber der Middleware. Eine Dublette lässt sich nur mit Begründung annehmen. |
| B12 | [00:41:27]–[00:46:54] | Kürzungen und Abschlagsrechnungen | Kürzungen kommen „relativ häufig" vor. Laut Sebastian passt man Netto und Brutto an, bearbeitet die Rechnung (lokal) und setzt eine Notiz; Tanja stellt fest: keine Kürzungsmaske. Positionsweise Kürzung mit automatischer Neuberechnung „würde funktionieren", ist in der Demo-Instanz aber nicht zeigbar. Frühere Abschläge liegen in der Akte; eine automatische Prüfung kumulierter Abschläge ist **offen** und wird mit Herrn Groß geklärt. |
| B13 | [00:46:54]–[00:48:10] | E-Rechnung | „Trius": Bei E-Rechnungen sind Streichungen unzulässig, also Rückgabe und Neuanforderung. Sebastian: d.velop sei „sehr gut dafür ausgelegt", die Felder kämen automatisch mit; Ablehnung und Rückleitung liefen über den Eskalationsprozess. |
| B14 | [00:48:12]–[00:49:33] | Freistellungsbescheinigung | Tanja und André wünschen eine automatische Prüfung, ob eine Freistellungsbescheinigung vorliegt. Sebastian: ein Ja/Nein-Feld, „Nö, das geht alles über Develop". Die Entscheidung werde aber manuell abgehakt, eine Automatisierung ginge über die Middleware. André: Eine Middleware-Tabelle zu pflegen „werden wir bestimmt nicht tun". |
| B15 | [00:49:33]–[00:53:32] | Intelligente Postverteilung / Mailimport | Gezeigt werden Konfigurationsmenü und Postfachverwaltung mit drei angelegten Postfächern (u. a. „Invoices"), Importprofil und zugelassenen Absendern (Einzeladresse, Domain, alle – nicht empfohlen). Live-Versand einer Test-Mail mit Anhang. Das Ankommen im Stapel ist im Transkript **nicht bestätigt** („das ist noch nicht eingelesen" [00:53:26]). |
| B16 | [00:53:32]–[00:57:41] | Dokumentablage und Akten | Eine Auftragsbestätigung wird manuell abgelegt (Kategorie „Auftrag", Gesellschaft, Kreditor, Objekt). André: „Das würde er aber nicht automatisch erkennen." Antwort: beim automatischen Eingang schon. Der Akteninhalt zeigt das Dokument in der Kreditorenakte „Elektro Nordlicht GmbH" und in der Objektakte. Aktenebenen sind beliebig, empfohlen werden 4–5; Livos soll die „Folder Structure" liefern. |
| B17 | [00:57:41]–[01:03:29] | Eigenschaften, Aufgaben, Prozesse, Administration | Erklärt werden Eigenschaften, Kategorien und Wertemengen (Gewerke, Kostenstellen, Kreditoren, drei Objekte). Eine Aufgabe wird an Annalena erstellt, mit Priorität, Zustelldatum, Fälligkeit und Erinnerung; manuell startbar sind Prozesse wie „Angebot prüfen und vergleichen" und „Prüfung und Freigabe". Die Administration zeigt Dashboard (Belege im Umlauf), Onboarding, aufgetretene Probleme, Workflowstatus und Workflow-Einstellungen (Schritte, Prüfer, Eskalation, Start, Ausgleichspositionen, Zuschläge, Rechnungslesung). |
| B18 | [01:03:29]–[01:04:45] | Workflowvarianten, Fälligkeitsampel, Benutzer | Workflows sind unterschiedlich gestaltbar. Die Fälligkeitsampel steht auf grün, gelb bei 10 Tagen und rot bei 5 Tagen vor Netto-Fälligkeit. Benutzer und Gruppenberechtigungen werden in der Admin-Maske angelegt. |
| B19 | [01:04:47]–[01:06:16] | Vertretung und Berechtigungen | Vertretung über Abwesenheitsstatus, auch vorab planbar. Wie ein Admin für Erkrankte die Vertretung setzt, wird „im nächsten Gespräch" beschrieben. Der Admin sieht alles; Rechte lassen sich abteilungsbezogen vergeben (Marketing, Buchhaltung). |
| B20 | [01:06:16]–[01:08:13] | Suche und Kreditorenakte | Suche nach Kategorie („Livos Auftrag"), Kreditor, Auftragsnummer und Rechnungsdaten; Dokumente sind den Gesellschaften „Norden" und „Süden" zugeordnet. Die Kreditorenakte hat Unterakten (gelb = gefüllt, grau = leer); am Beispiel „Stadtwerke Beispielstadt AG" liegen dort Auftrag und Eingangsrechnung. |
| B21 | [01:08:13]–[01:09:45] | Lizenz und KI | André fragt, ob sich die Lizenz nach Aktenanzahl oder Dokumentgröße richtet; Sebastian muss nachschauen. KI-Fragen an Verträge gehen laut MDIS „nicht über Develop direkt", sondern über die MDIS-KI-Plattform; Thomas will sie beim nächsten Mal zeigen. |
| B22 | [01:09:48]–[01:14:13] | Abschluss und nächste Schritte | André wünscht ein Angebot noch diese Woche für etwa 80 Nutzer mit Bezug zum Leistungskatalog; die Entscheidung mit dem Management soll in der Folgewoche fallen. Thomas zeigt den ausgefüllten Katalog (Spalte F) und sagt die Zusendung zu. Thomas bestätigt, dass Evidanza über die Middleware angebunden werden kann, und wiederholt zwei Vorschläge: Test der KI-Plattform und ein Workflow-Termin zu Anbindung und Abgrenzung. Verabschiedung. |

---

## 3 Anforderungen des Kunden

Die Spalte „Priorität laut Kunde" gibt nur ausdrückliche Äußerungen im Termin wieder. Wo keine fiel, steht „k. A." mit der Katalogpriorität in Klammern.

| ID | Anforderung / Wunsch (eigene Worte) | Wörtliches Kurzzitat | Sprecher | Zeit | Katalog | Priorität laut Kunde | Themengebiet |
|---|---|---|---|---|---|---|---|
| T-01 | Alle Anhänge aus einem definierten Mailpostfach werden automatisch importiert und verarbeitet. | „…dass es quasi alle Anhänge aus dem Mailfach automatisch … verarbeitet werden" | André Töpper | 00:04:13–00:04:16 | 2.1 | k. A. (Must) | Erfassung |
| T-02 | Geklärt werden muss, woher die Lieferantennummer kommt und welches System führt. Dieselben Kreditoren haben in vielen Gesellschaften unterschiedliche Kreditorennummern. | „…Die haben aber in den verschiedenen Gesellschaften auch unterschiedliche … Nummern … woher kommt denn diese Lieferantennummer?" | André Töpper | 00:06:00 | 1.1, 2.2, 5.1 | k. A. | FiBu/DATEV |
| T-03 | Neue Kreditoren müssen ohne vorherige DATEV-Anlage verarbeitbar sein. Das Livos-Team kann bzw. will keine Kreditoren in DATEV anlegen. | „…wir selber möchten und können auch nicht in DATEV irgendeinen Kreditor … anlegen" | André Töpper | 00:07:41–00:07:57 | 5.1 (2.3 analog) | k. A. | FiBu/DATEV |
| T-04 | Der Initialaufwand für das Kreditoren-Mapping über mehr als 100 Gesellschaften soll gering bleiben. | „Es ist halt ein riesiger, einmaliger erster Aufwand" | André Töpper | 00:09:39 | 5.4 | implizit hoch (Aufwandssorge) | FiBu/DATEV |
| T-05 | Eindeutiger Schlüssel aus DATEV-Mandantennummer und Kreditorenkontonummer. | „…die Mandantennummern aus DATEV … mit den … Kreditorenkontennummern kombinieren, dann hätte man doch 'n Schlüssel" | „Trius" | 00:11:26 | 5.1, 5.4 | Vorschlag | FiBu/DATEV |
| T-06 | Bidirektionaler Stammdatenabgleich: Neue Kreditoren, auch von den HV angelegte, kommen mit Nummer aus DATEV in die Middleware. | „…dass aus DATEV dann neue Kreditoren mit Nummer in in die Mittelwehr kommen. Also es Funktioniert von beiden Seiten" | Christian Weigel | 00:13:38 | 5.1, 5.4 | k. A. | FiBu/DATEV |
| T-07 | Randbedingung: Die ca. 10 wechselnden Property Manager dürfen nicht zur Nutzung eines Erfassungssystems verpflichtet werden. | „Ich glaube nicht, dass wir das hinbekommen, die Hausverwalter … zu verpflichten" | André Töpper (bestätigt von Christian Weigel) | 00:13:02–00:13:16 | 4.1 | K.-o.-Randbedingung | Property Manager |
| T-08 | Der Stammdatenabgleich muss trotz externem Hosting und DATEV-Zugriff über die „ricken Cloud" funktionieren. | „…daher ist die Auswertmöglichkeit eingeschränkt … inwieweit diese Abgleiche alle so funktionieren" | Christian Weigel | 00:14:00–00:14:11 | 5.1 | k. A. | Betrieb |
| T-09 | **Scope:** Alle Rechnungen, die nicht über den Verwalter laufen, werden in d.velop erfasst, geprüft, freigegeben und an den Zahllauf übergeben. | „…über das Develop alle Rechnungen erfassen, prüfen, freigeben, weiter zum Zahllauf schieben, die nicht über den Verwalter erfasst werden" | Tanja Brecht | 00:16:32 | 1.4, 5.5 | Kernumfang (Annahme) | Workflow/Freigabe |
| T-10 | Transparente, konsolidierte Kreditorensicht: Derselbe Kreditor bei HV und Livos darf nicht mit unverbundenen Nummern geführt werden. | „…dass wir dann hinterher nicht unterschiedliche Kreditorennummern haben für … den gleichen Kreditor … das muss ja einigermaßen transparent sein" | Christian Weigel | 00:16:49–00:17:07 | 5.4 (4.1) | k. A. | FiBu/DATEV |
| T-11 | Prozess für Rechnungen mit unbekannter Kreditor- bzw. Lieferantennummer: Eine berechtigte Person prüft und legt an. | „…was passiert mit den Rechnungen, … wo die Nummer nicht bekannt ist? … Einer muss das immer noch mal prüfen" | André Töpper | 00:18:44–00:19:01 | 2.3 (analog für Kreditor) | k. A. | Erfassung |
| T-12 | Neue Lieferanten werden den später in DATEV angelegten Kreditorennummern automatisch, nicht manuell zugeordnet. | „…Ist das automatisiert oder müssen wir dann auch wieder manuell?" | André Töpper | 00:19:58 | 5.1, 5.4 | k. A. | FiBu/DATEV |
| T-13 | HV-gebuchte Rechnungen, die ab einer gewissen Größenordnung durch das Asset Management freizugeben sind, werden im System zur Freigabe geführt, ohne Buchung und Zahlung. | „…Rechnungen, die von Hausverwaltungen gebucht werden, Durch Asset Management freigegeben werden, wenn gewisse Größenordnungen durchlaufen werden" | „Trius"; Tanja Brecht | 00:20:45; 00:21:57 | 4.1 | „noch so ein kleines On-Top" [00:22:49–00:22:52 Tanja Brecht], also optional | Property Manager |
| T-14 | Auch für HV-Rechnungen: Transparenz („wo hängt die Rechnung"), Vollständigkeit und Einsicht durch den Vertreter. | „…die Transparenz, wo hängt die Rechnung und der Vertreter kann reingucken" | Tanja Brecht; „Trius" | 00:22:41–00:22:49 | 3.2, 3.4, 4.1 | wie T-13 | Property Manager |
| T-15 | Nachvollziehbar sein soll, woher die erkannten Werte stammen: aus dem Dokument oder aus den Stammdaten (DATEV/Middleware), z. B. die IBAN. | „…aus dem Rechnungsdokument selbst oder liest er die Stammdaten dann Aus Datev der Middleware … wie IBAN" | André Töpper | 00:23:40 | 2.2 | k. A. | Erfassung |
| T-16 | IBAN der Rechnung wird mit den Stammdaten abgeglichen; bei Abweichung gibt es einen Hinweis. | „…stellt aber in unseren Stammdaten 'ne andere IBAN fest, als auf der Rechnung steht … da könnte er uns drauf hinweisen" | André Töpper | 00:24:42 | 2.6 | k. A. | Erfassung |
| T-17 | E-Mail-Benachrichtigungen sind abschaltbar; gearbeitet wird nur über die Aufgabenliste im System. | „…E-Mail-Versand auch abstellen und nur immer gucken im Programm: Was habe ich für Aufgaben und Rechnungen?" | Tanja Brecht | 00:26:27 | 3.1 | k. A. | Workflow/Freigabe |
| T-18 | Die Fälligkeit kommt wahlweise aus der Rechnung oder aus den Stammdaten (Policy) und bleibt manuell änderbar. | „…ob wir dem Kreditor so vertrauen möchten, mit dem was er auf die Rechnung schreibt? Oder ob wir es aus unseren Stammdaten … selbst hinzufügen möchten" | André Töpper | 00:28:57–00:29:00 | 2.2, 1.8 | k. A. | Erfassung |
| T-19 | Der Mandant wird automatisch aus dem Beleg erkannt und der Mandantennummer zugeordnet, damit die DATEV-Übergabe stimmt. | „Den Mandanten erkennt er auch immer automatisch … Livos Objektgesellschaft Süd wäre Mandantennummer 12345. Und das würde er dann automatisch erkennen und zuordnen" | André Töpper | 00:31:16–00:31:36 | 2.2, 1.1, 5.1 | k. A. (Must) | Mandanten/Struktur |
| T-20 | Weitere Dokumente werden als Nachweis an die Rechnung angehängt. | „Ich könnte auch ein weiteres Dokument als Nachweis oder wie auch immer hinzufügen." | André Töpper | 00:33:21 | 1.7 | k. A. (Should) | Akten/Archiv |
| T-21 | Option: Den Buchungsschritt bzw. die Buchen-Maske bekommt nur der Steuerberater. | „…dass quasi diese Maske mit dem Buchen nur unsere Steuerberater haben" | André Töpper | 00:33:28 | 1.5 | „nur eine Option, ein Gedankenspiel" [00:33:53] | Berechtigungen |
| T-22 | Option: Mit dem Buchen wird die Zahlung automatisch ausgelöst. | „…sobald man hier auf Buchen klickt, dass die Zahlung auch schon rausgeht" | André Töpper | 00:33:28 | 5.5 | „nur eine Option, ein Gedankenspiel" [00:33:53] | Zahlung |
| T-23 | Durchlauf- und Liegezeiten werden je Prozessschritt und je Benutzer ausgewertet. | „…Benutzer A, der braucht keine Ahnung 5 Tage, um Rechnungen freizugeben. Benutzer B schafft es in einem Tag" | Christian Weigel | 00:35:18 | 3.2 | k. A. („übergeordnete Frage") | Sonstiges (Reporting) |
| T-24 | Auswertungen in Evidanza auf Basis der d.velop-Daten. | „…dass wir Auswertungen auf Basis von Develop fahren könnten, richtig?" | André Töpper | 00:36:32; 01:12:09–01:12:17 | 3.2, 5.4 | zweimal nachgefragt, also wichtig | Sonstiges (Reporting) |
| T-25 | Zeitvorgaben je Prüfer und Schritt, danach Eskalation. | „…welcher Prüfer in welchem Schritt wie viel Zeit vorgegeben hat, bevor es sozusagen eskaliert" | Tanja Brecht | 00:37:01–00:37:06 | 3.3 | k. A. (Must) | Workflow/Freigabe |
| T-26 | Rückweisung mit vorgefertigter, anpassbarer Standard-E-Mail an den Lieferanten: ca. 5 Standardgründe, Adresse wird automatisch ermittelt, das eigene Mailprogramm muss nicht geöffnet werden. | „…5 Standardgründe … eine vorher vorgefertigte für unsere fünf Fälle E-Mail rausschicken an den Auftragnehmer, ohne dass wir noch mal unser Mailfach öffnen" | Tanja Brecht; André Töpper | 00:37:12; 00:38:32; 00:38:42 | nicht im Katalog (nahe 2.6) | konkret ausgeführt; k. A. | Workflow/Freigabe |
| T-27 | Dubletten aus Doppeleingang (Mail und Post) werden ohne Lieferantenmail abgelehnt. | „…'ne Dublette kann ja recht häufig vorkommen, weil der Auftragnehmer einmal per E-Mail und einmal per Post seine Rechnung schickt" | André Töpper | 00:38:42 | 2.6 | „recht häufig" | Erfassung |
| T-28 | Freigabeworkflows auch für Vorgänge ohne Rechnung, z. B. Ausbuchungen auf Mietkonten. | „…Spielfreigaben für Ausbuchungen auf Mietkonten implementieren" | Tanja Brecht | 00:37:33 | nicht im Katalog (6.1/1.4) | „vollkommen fern vom Thema", also Ausblick | Workflow/Freigabe |
| T-29 | Rechnungskürzungen, z. B. 8.000 statt 10.000 zahlen, weil die Leistung mangelhaft war. | „Wie können wir denn Kürzungen oder so vornehmen? Kommt relativ häufig vor." | André Töpper; Tanja Brecht | 00:41:27; 00:41:36 | 1.8 | **„relativ häufig"**, also hoch | Workflow/Freigabe |
| T-30 | Positionsweise Kürzung (z. B. 4 auf 3 Stunden) mit automatischer Neuberechnung der Summe; die Originalrechnung bleibt erhalten. Betrifft Rechnungen mit bis zu 30 Seiten und etwa 8 gekürzten Positionen. | „…kann ich einfach auf drei Stunden in der Rechnung kürzen und er passt alles andere dahinter an und behält die Originalrechnung aber noch" | André Töpper | 00:42:32–00:42:59 | 1.8, 1.6 | hoch („da würde uns ja sonst nicht geholfen werden") | Workflow/Freigabe |
| T-31 | Bei Abschlagsrechnungen sind die bereits akzeptierten Beträge früherer Abschläge einsehbar. | „…kann ich dann sehen, was bei der ersten und zweiten schon akzeptiert wurden an an Beträgen?" | Tanja Brecht | 00:44:49 | 5.2 | k. A. (Should) | Sonstiges (Bau/VOB) |
| T-32 | Kumulierte Abschlagsrechnungen werden automatisch gegen die tatsächlich geleisteten Zahlungen geprüft (Beispiel 1 Mio. Leistungsstand, 700.000 gezahlt, 600.000 vom Auftragnehmer angegeben). | „Würden wir das automatisch geprüft bekommen oder müssten wir uns die vorherigen Abschlagsrechnungen anschauen?" | André Töpper | 00:45:47 | 5.2 (5.3 Bim4You-Budget) | k. A. | Sonstiges (Bau/VOB) |
| T-33 | E-Rechnung: Statt Streichungen gibt es einen Rückgabe- und Neuanforderungsprozess, der die E-Rechnungs-Rahmenbedingungen erfüllt. | „…Streichungen und Änderungen auf Rechnungen werden ja in der Form nicht mehr zulässig sein … Haben Sie das berücksichtigt" | „Trius" | 00:46:54 | 2.4 | k. A. (Must) | Erfassung |
| T-34 | Das System prüft bei Baurechnungen, ob eine Freistellungsbescheinigung vorliegt (hinterlegt am Kreditor). | „Aber nicht bei der Rechnung, sondern beim Lieferanten." / „Aber er soll ja prüfen, ob wir eine Freistellungsbescheinigung haben." | Tanja Brecht; André Töpper | 00:48:12–00:49:09 | 2.7, 2.6 | k. A. (Could) | Workflow/Freigabe |
| T-35 | Randbedingung: Standardfunktionen gehen vor Middleware-Eigenbau; Livos will keine eigenen Middleware-Tabellen pflegen. | „…bei Middleware ein bisschen vorsichtig" / „…das werden wir bestimmt nicht tun" | André Töpper | 00:40:13–00:40:21; 00:49:25–00:49:28 | übergreifend (5.4) | Randbedingung | Betrieb |
| T-36 | Kategorie, Gesellschaft, Kreditor und Objekt werden auch bei sonstigen Dokumenten (z. B. Auftragsbestätigung) automatisch erkannt. | „Das würde er aber nicht automatisch erkennen." | André Töpper | 00:54:49 | 6.1, 2.2 | k. A. | Post |
| T-37 | Mehrstufige Aktenhierarchie mit mehr als zwei Ebenen. | „Wie viele Ebenen können das sein? … oder sind es immer nur diese zwei Ebenen?" | André Töpper | 00:57:09 | 6.1 | k. A. | Akten/Archiv |
| T-38 | Unterschiedliche Rechnungsworkflows (Varianten). | „Die Workflows für die Rechnung exemplarisch kann man auch … unterschiedlich gestalten." | André Töpper | 01:03:29 | 1.4 | k. A. (Must) | Workflow/Freigabe |
| T-39 | Vertretungsregelung, bei Krankheit auch durch Admin oder Vorgesetzte aktivierbar. | „…könnte Christian Weigel, wenn er die Berechtigung hat, könnte sagen: ‚Hey'. André Töpper ist krank. Alles, was bei ihm liegt, soll es um Korsmeier geben." | André Töpper | 01:04:47; 01:05:21 | 3.4 | k. A. (Must) | Berechtigungen |
| T-40 | Transparentes Lizenzmodell: Gerechnet nach Aktenanzahl oder nach Dokumentgröße? | „…ob das nach Anzahl von Akten geht, … von den Lizenzgebühren her oder ob das nach Größe der Dokumente geht" | André Töpper | 01:08:13 | Lizenz (Agenda-Frage) | k. A. | Lizenz |
| T-41 | KI-gestützte Inhaltsabfrage bei Verträgen, z. B. „Haben wir Skonto vereinbart?". Im Transkript steht „Konto", gemeint ist vermutlich Skonto. | „…kann ich dann Develop zu dem Vertrag irgendwas fragen … Haben wir das Konto vereinbart?" | André Töpper | 01:08:46–01:09:07 | nicht im Katalog (Umfeld 6.1) | Interesse; „sinnvoll im zweiten Step" [01:09:35] | Verträge |
| T-42 | **Angebot noch diese Woche** für ca. 80 Nutzer (80–100), mit Bezug auf den Leistungskatalog; nicht abschätzbare Punkte dürfen ausgeklammert werden. | „…in dieser Woche vielleicht mal ein Angebot zu erhalten … zumindest mal für 80 bis 100 Nutzer irgendwie oder wahrscheinlich so 80 Nutzer" | André Töpper | 01:10:22 | alle | **dringend** | Lizenz |
| T-43 | Das Angebot weist aus, welche Katalogpunkte abgedeckt sind und wo Klärungsbedarf besteht (z. B. BIM-Anbindung), damit es mit anderen Angeboten vergleichbar ist. | „…welche Punkte sind mit dem Angebot abgedeckt, was sind vielleicht Punkte, die … detaillierter geklärt werden müssen … wie exemplarisch irgendwie Anbindung BIM" | André Töpper | 00:00:22 | 5.3 u. a. | Vergleichbarkeit wichtig | Lizenz; Bim4You |
| T-44 | Das Angebot berücksichtigt auch die im Termin besprochenen Themen, also den Abgleich mit DATEV und den Hausverwaltern. | „…inklusive natürlich der Themen, die wir heute so grob mitbesprochen haben" | André Töpper | 01:11:47 | 5.1, 4.1 | k. A. | Sonstiges |
| T-45 | Livos erhält den ausgefüllten Leistungskatalog (Spalte F). | „Den haben wir noch nicht von ihm. Haben Sie also schicken Sie ihn gerne mit" | André Töpper | 01:11:36 | alle | mit dem Angebot | Sonstiges |
| T-46 | Die KI-Plattform soll auch für die bestehende App, die Middleware und „E. V. R." (unklar) nutzbar sein. | „Die K.I.-Plattformen wären … auch interessant und relevant für die App und … die Middleware und E. V. R." | André Töpper | 01:13:55–01:14:02 | 5.4 | Interesse | Sonstiges |

---

## 4 Aktuelle Ist-Situation bei Livos

Alle Punkte sind Aussagen im Transkript (**Fakt**), soweit nicht als Annahme markiert.

### 4.1 Organisation und Beteiligte
- Livos betreut mehr als 100 Gesellschaften, darunter Objektgesellschaften [00:05:51–00:06:00 André Töpper; 00:09:05–00:09:14 André Töpper „für jede einzelne der 100 … Objektgesellschaften"].
- Es gibt 80 bis 100 Nutzer, „wahrscheinlich so 80" [01:10:22 André Töpper].
- Die DATEV-Anwender stehen „ganz am Ende in unserer Reihe" [00:07:41 André Töpper]. Livos bucht nicht selbst; das hält auch Thomas fest: „weil ihr bucht ja nicht selber" [00:08:01], von Livos nicht widersprochen.
- **Trios** bucht und prüft die PM-Buchungen [00:16:17 André Töpper] und erhält Rechnungen gebündelt im **Monatspaket** [00:21:57 Tanja Brecht].
- Ein **Steuerberater** wird als möglicher Inhaber des Buchungsschritts genannt [00:33:28 André Töpper]. Ob er mit Trios identisch ist, ist **offen**.
- Das **Asset Management** gibt größere HV-gebuchte Rechnungen frei; so das Verständnis von „Trius" [00:20:45]. Tanja sagt dazu: „die werden doch nicht über Develop erfasst, weil die werden ja trotzdem beim Verwalter gebucht" [00:21:07].
- Es gibt **etwa 10 verschiedene Property Manager**, die „sich auch immer wieder wechseln können" [00:13:08–00:13:11 André Töpper].
- Die Livos-Server liegen bei einem **externen Dienstleister**, nicht bei Trios [00:14:00 Christian Weigel].
- Das Auswahlverfahren läuft mit mehreren Anbietern; die Entscheidung trifft das „restliche Management" in der Woche nach dem Angebot [00:23:21, 01:10:22–01:11:18 André Töpper].
- Der Soll-Prozess ist noch nicht festgelegt: „da sind wir auch noch nicht komplett festgelegt, wie es wirklich ablaufen soll oder wird" [00:23:26–00:23:35 André Töpper].

### 4.2 Systeme
- **DATEV** ist das FiBu-System. Kreditoren werden je DATEV-Mandant geführt; nach MDIS-Verständnis ist DATEV das führende System [00:06:37 Thomas Gross]. Livos widerspricht nicht.
- DATEV wird über die **„ricken Cloud"** beim externen Dienstleister erreicht, deshalb ist die „Auswertmöglichkeit eingeschränkt" [00:14:00–00:14:11 Christian Weigel]. Die Bedeutung von „ricken Cloud" ist **offen** (s. Kap. 11).
- **Middleware und App von MDIS** sind bereits vorhanden; Tanja pflegt dort Stammdaten [00:40:09 André Töpper]. Thomas spricht von der „euch bekannten Technologieumgebung" [00:08:01] und „den Technologien, die ihr kennt" [00:09:51].
- Es gibt ein **BI-Projekt bzw. Data Warehouse** mit MDIS. Thomas vermutet: „wir werden die Kreditoren so einer so schon im Data B aus [Data Warehouse] haben im Rahmen des BI Projektes" [00:06:37] (**Annahme MDIS**). Er erwähnt „Bilanzauswertungen" in den Livos-Apps [01:13:26].
- **Evidanza** (BI/Reporting) ist vermutlich bei Livos im Einsatz oder geplant (**Annahme**), weil André zweimal danach fragt [00:36:32; 01:12:09].
- Die **Buchhaltungsdaten der HV** werden über eine Schnittstelle übernommen: „wir übernehmen ja die Buchhaltungsdaten sozusagen über die Schnittstelle" [00:12:46–00:12:49 Christian Weigel].
- Unklar: Thomas sagt, in der von Livos genutzten Technologie gebe es „ein Add on, das ist S One und i on, das sind so KI Tools" [00:10:12] (s. Kap. 11).
- **Nicht erwähnt:** ein bestehendes DMS, das Mailsystem, Omikron und BIM4You im Ist-Betrieb. Ob Livos BIM4You und Omikron heute nutzt, ergibt sich nur aus dem Katalog, nicht aus dem Termin.

### 4.3 Abläufe
- **Rechnungseingang** per E-Mail und per Post. Die Papierpost wird eingescannt, dadurch entstehen häufig Dubletten: „…weil der Auftragnehmer einmal per E-Mail und einmal per Post seine Rechnung schickt und die Post scannen wir auch noch ein" [00:38:42 André Töpper].
- **Rechnungen über Property Manager:** Etwa 95 % werden vom PM geprüft, freigegeben und bezahlt [00:15:18 André Töpper]. Die PM haben Freigabegrenzen, deren Höhe André nicht kennt („ich weiß nicht genau, wo die Grenzen liegen") [00:15:18]. Die PM buchen selbst; die Buchungsdaten gehen direkt in DATEV, und Livos „[hat] im Freigabeprozess eigentlich auch gar nichts mehr zu tun" [00:16:17 André Töpper].
- **Größere PM-Rechnungen** gibt nach Verständnis von „Trius" das Asset Management frei [00:20:45]. Auf Thomas' Frage, ob das per E-Mail geschieht, antwortet Tanja „Yep, yeah" [00:21:23–00:21:25]. Der heutige Weg ist damit vermutlich E-Mail (**Annahme**, Beleg schwach).
- **PM-Rechnungen** werden „nicht von Trios bezahlt, sondern vom Property Manager" [00:21:46 André Töpper] und sind „auch schon gebucht" [00:21:50 Christian Weigel].
- **Interne Rechnungen** durchlaufen Erfassung, Prüfung und Freigabe und gehen dann zum Zahllauf. So beschreibt Tanja den Soll-Umfang [00:16:32].
- **Kürzungen** kommen „relativ häufig" vor [00:41:27]. Heute rechnet man die Kürzungen bei mehreren Positionen „händisch zusammen" [00:42:36 André Töpper].
- **Abschlagsrechnungen** gibt es bei großen Baumaßnahmen. Auftragnehmer weisen zum Teil falsche bereits gezahlte Beträge aus [00:45:09–00:45:47 Tanja Brecht und André Töpper].
- **Freistellungsbescheinigungen** sind bei Baurechnungen relevant [00:48:12 Tanja Brecht].
- **Ausbuchungen auf Mietkonten** brauchen Freigaben [00:37:33 Tanja Brecht].
- **Kreditorenanlage:** Livos legt selbst keine Kreditoren in DATEV an [00:07:41]; die HV legen eigene Kreditoren an [00:12:13 Christian Weigel].
- Laut Thomas vergehen zwischen Rechnungseingang und Verbuchung „zum Teil … sicherlich Wochen" [00:08:01] (**Annahme MDIS**, nicht widersprochen).

### 4.4 Mengen und Kennzahlen
| Kennzahl | Wert | Beleg |
|---|---|---|
| Gesellschaften | über 100 | [00:06:00 André Töpper] |
| Property Manager | ca. 10, wechselnd | [00:13:08 André Töpper] |
| Anteil der PM-Rechnungen, die vom PM freigegeben und bezahlt werden | ca. 95 % | [00:15:18 André Töpper] |
| Nutzer | 80–100, „wahrscheinlich so 80" | [01:10:22 André Töpper] |
| Kreditorennummernkreise | 70000er intern, 80000er HV-Einzelkreditoren | [00:17:34 „Trius"] |
| Umfang gekürzter Rechnungen | bis 30 Seiten, ca. 8 gekürzte Positionen | [00:42:36 André Töpper] |
| Beispiel Abschlagsvolumen | 1 Mio. Leistungsstand kumuliert | [00:45:47 André Töpper] (Beispiel) |
| Beleg- bzw. Rechnungsvolumen | **im Termin nicht genannt**; laut Katalog 20–30/Tag, 5.000–8.000/Jahr | Katalog, Blatt „Übersicht" |

### 4.5 Stammdaten
- Dieselben Kreditoren haben in vielen Gesellschaften unterschiedliche Nummern und Kennzahlen [00:06:00 André Töpper].
- Interne Kreditoren liegen im 70000er-Bereich, HV-Einzelkreditoren im 80000er-Kreis; beide sind **nicht zusammengeführt** [00:17:34–00:17:50 „Trius"].
- In DATEV findet keine Kreditorenkonsolidierung statt [00:17:28–00:17:30 Thomas Gross, bestätigt von „Trius" 00:17:50].
- Tanja nahm an, die Kreditoren würden schon heute mit denen der HV „matchen" [00:17:18 Tanja Brecht]. Das trifft laut „Trius" nicht zu.

### 4.6 Schmerzpunkte (explizit oder implizit)
| Schmerzpunkt | Beleg |
|---|---|
| Uneinheitliche Kreditorennummern je Gesellschaft und für HV; hoher einmaliger Mapping-Aufwand | [00:06:00], [00:09:39], [00:17:34] |
| DATEV-Anlage erst am Ende der Kette; Livos kann keine Kreditoren anlegen | [00:07:41] |
| Eingeschränkter DATEV-Zugriff und eingeschränkte Auswertungen wegen externem Hosting | [00:14:00–00:14:11] |
| Keine Transparenz und Vollständigkeit bei HV-Rechnungen mit AM-Freigabe (implizit aus der positiven Reaktion) | [00:22:41–00:22:49] |
| Kürzungen werden händisch nachgerechnet, bei langen Rechnungen aufwendig | [00:42:36] |
| Fehlerhafte kumulierte Abschlagsrechnungen müssen manuell nachgeprüft werden | [00:45:47] |
| Dubletten durch Doppeleingang per Mail und Post | [00:38:42] |
| Rückweisungen kosten Aufwand, das Mailprogramm muss separat geöffnet werden | [00:38:42] |
| Schlechte Erfahrungen mit Middleware-Eigenentwicklung: „alles manuell zu programmieren und es läuft nicht alles so, wie man sich es immer erhofft" | [00:40:13 André Töpper] |
| Keine Transparenz über Bearbeitungszeiten je Benutzer | [00:35:18] |
| Vertretung im Krankheitsfall ist nicht geregelt | [01:05:21] |

---

## 5 Fragen des Kunden und gegebene Antworten

Bewertung: **B** = beantwortet · **T** = teilweise (pauschal, ohne Demo oder nur konzeptionell) · **O** = offen bzw. vertagt.

| Nr | Zeit | Frage (Sprecher) | Antwort (wer, was) | Bewertung |
|---|---|---|---|---|
| F-01 | 00:04:13–00:04:16 | Geht der Import auch automatisch, wenn man ein Mailfach definiert? (André) | Sebastian [00:04:28]: „Auf jeden Fall." Die Felder werden einmalig definiert; das System erkennt „je nach Rechnung oder je nach Angebot" und legt in der richtigen Akte ab. Live-Mailimport später gezeigt [00:49:33–00:53:32], Eingang im Stapel aber nicht sichtbar bestätigt. | T |
| F-02 | 00:05:29 | „Was ist das mit der Lieferantennummer?" (André) | Sebastian [00:05:35–00:05:48]: Lieferanten müssen mit einer Nummer gekennzeichnet sein, die mit „euren Daten" übereinstimmt. | T |
| F-03 | 00:06:00 | Woher kommt die Lieferantennummer? Selbst definieren, automatisch aus DATEV, oder was gilt, wenn der Kreditor in DATEV fehlt? (André) | Thomas [00:06:37–00:09:31]: Es ist ein Stammdatenthema; DATEV ist führend. Empfehlung: ein zentraler Lieferantenstamm in einer eigenen App mit einer mandantenübergreifenden Lieferanten- bzw. Konsolidierungsnummer, auf die die DATEV-Kreditorennummern referenzieren. „Kleine App bauen" [00:09:04]. | B (konzeptionell; Lösung liegt außerhalb von d.velop) |
| F-04 | 00:07:41 | Wie legt man Kreditoren an, die neu sind, wenn Livos nicht in DATEV anlegen kann? (André) | Thomas [00:08:01]: „ganz dringend empfehlen", den Lieferanten-Nummernkreis vom DATEV-Nummernkreis zu entkoppeln, zentral anzulegen und gegenseitig zu referenzieren. | B (konzeptionell) |
| F-05 | 00:09:05–00:09:14 | Heißt das, für jeden Lieferanten die DATEV-Nummer je Objektgesellschaft zu hinterlegen? (André) | Thomas: „Genau richtig", bei einer einzigen Lieferantennummer auf Managementebene. | B |
| F-06 | 00:10:46 | Würde das (das KI-Mapping) automatisch übernommen? (André) | Thomas [00:10:54–00:11:13]: Heraus kommt eine Tabelle als Vorbelegung der Lieferanten-App, teilweise mit Nacharbeit; als PoC zeigbar. | B |
| F-07 | 00:11:26 | Könnte man DATEV-Mandantennummer und Kreditorenkontonummer zu einem Schlüssel kombinieren? („Trius") | Thomas [00:11:39–00:12:13]: „Genau so würde ich es machen", zusätzlich eine Konsolidierungsnummer als führende Nummer. | B |
| F-08 | 00:14:00–00:14:11 | Funktionieren die Abgleiche, obwohl die Server beim externen Dienstleister liegen und DATEV über die „ricken Cloud" erreicht wird? (Christian) | Thomas [00:14:23]: „Das muss man prüfen." Verweis auf eine DATEV-Schnittstelle beim Referenzkunden; zu prüfen ist, ob sie „in der Rickencloud Umgebung auch läuft". | **O** |
| F-09 | 00:16:05 | Bekommen wir PM-Rechnungen überhaupt in d.velop? Das wäre neu. (André) | Thomas/Tanja [00:16:17–00:16:47]: Wenn nur Rechnungen ohne Verwalter in d.velop laufen, „haben wir das Problem nicht". Für eine konsolidierte Sicht braucht es trotzdem das Mapping der HV-Kreditorennummern, in der Stammdaten-App [00:17:50–00:18:39]. | B |
| F-10 | 00:17:14–00:17:18 | Haben wir das Matching nicht schon heute über DATEV? (Tanja) | Thomas [00:17:28]: In DATEV gibt es keine Kreditorenkonsolidierung. „Trius" [00:17:34]: 70000er- und 80000er-Kreise, nicht zusammengeführt. | B |
| F-11 | 00:18:44–00:19:01 | Was passiert mit Rechnungen, deren Nummer unbekannt ist? Muss das jemand in der App anlegen und prüfen? (André) | Thomas [00:19:01–00:19:49]: „Das macht das System schon selber." Das System prüft, ob es den Kreditor in einem DATEV-Nummernkreis gibt, und bietet an, per Klick eine Konsolidierungsnummer zu erzeugen. Der Lieferantenstamm wird danach in der App angelegt. | T (Konzept; Individualentwicklung) |
| F-12 | 00:19:31 | „Aber im Develop oder in der Mittelware?" (Christian) | Thomas [00:19:33–00:19:49]: Die Nummerngenerierung liegt in der Lieferanten-App; d.velop übernimmt die Nummer automatisch, angestoßen „aus Developer heraus". | B |
| F-13 | 00:19:58 | Wird ein neuer Lieferant dem später angelegten DATEV-Kreditor automatisch oder manuell zugeordnet? (André) | Thomas [00:20:11–00:20:21]: Nicht über den Namen, sondern KI-gestützt (Straße, Hausnummer, E-Mail); als kleiner, kostenloser PoC. | T |
| F-14 | 00:20:45–00:21:03 | Sind HV-gebuchte Rechnungen, die das Asset Management freigibt, berücksichtigt? („Trius") | Thomas [00:21:00–00:22:19]: „Die müssen wir erfassen." Vorschlag: Freigabe-Postfach, reiner Freigabeprozess in d.velop, formelle Freigabe per Mail an die HV. Tanja und Christian: Buchung und Zahlung bleiben beim PM, es ist ein separater Prozess. | T (Konzeptvorschlag; nicht entschieden) |
| F-15 | 00:20:29; 00:23:40 | Liest das System aus dem Rechnungsdokument oder aus den Stammdaten (DATEV/Middleware), z. B. die IBAN? (André) | Sebastian [00:24:10]: „Sowohl als auch", eine Frage der Konfiguration. Abgleich, ob der Kreditor existiert; wenn nicht, manuell anlegen, die Übertragung an DATEV erfolgt später über eine Schnittstelle. | T |
| F-16 | 00:24:42 | Kann das System bei abweichender IBAN warnen? (André) | Sebastian [00:25:02–00:25:05]: „Selbstverständlich"; Eskalationsprozesse, „human und der Loop". | T (Zusage ohne Demo) |
| F-17 | 00:26:27 | Kann man den E-Mail-Versand abstellen und nur im Programm arbeiten? (Tanja) | Sebastian [00:26:35]: „Klar, ja". | B |
| F-18 | 00:28:57–00:29:00 | Auf der Rechnung steht eine andere Fälligkeit (19.9.). Wird die ausgelesen, oder ist das eine Einstellung (Rechnung oder Stammdaten)? (André) | Sebastian [00:29:16–00:29:23]: „Einstellungssache", je nach Policy aus dem Dokument oder aus den Stammdaten; manuelle Eingabe bleibt möglich. | B (nicht demonstriert) |
| F-19 | 00:31:16–00:31:36 | Erkennt das System den Mandanten automatisch und ordnet ihn der Mandantennummer zu, damit er korrekt ins DATEV geht? (André) | Sebastian [00:31:41]: „Das ist korrekt." | B formal, inhaltlich **[RISIKO]** (s. Z-23) |
| F-20 | 00:33:21 | Kann ich ein weiteres Dokument als Nachweis hinzufügen? (André) | Sebastian [00:33:25]: „Ja, könnte man auch. Man könnte entsprechend hochladen und kabeln." | B |
| F-21 | 00:33:28 | Kann die Buchen-Maske nur der Steuerberater haben, und kann beim Buchen gleich die Zahlung rausgehen? (André) | Sebastian [00:33:44]: „Ja, das könnten wir über unsere Middleware machen und über unsere Technologie." André [00:33:53]: im Detail zu besprechen, nur ein Gedankenspiel. | T (Berechtigung implizit ja; Zahlung als Middleware-Projekt) |
| F-22 | 00:35:18 | Lassen sich Durchlaufzeiten je Schritt und Benutzer abfragen? (Christian) | Sebastian [00:36:13]: „…das kann … Develop insofern nicht abdecken", ginge über eine eigene App oder „weitere Schnittstelle", „sehr konfigurationsbedürftig". | T (für d.velop negativ) |
| F-23 | 00:36:32 | Wäre das über Evidanza möglich? (André) | Sebastian [00:36:37]: Das nimmt er mit und klärt es mit Herrn Groß. Möglich sei ein Dashboard über die Middleware; ob Evidanza das abdeckt, klärt man im nächsten Gespräch. | O (vertagt; s. F-42) |
| F-24 | 00:37:12–00:37:33 | (a) Lässt sich eine Rückweisung automatisiert mit E-Mail an den Lieferanten voreinstellen? (b) Eignet sich das Tool für Freigaben von Ausbuchungen auf Mietkonten? (Tanja) | Sebastian [00:37:45]: „sowohl als auch". Rechnungen lassen sich ablehnen und zurückgeben, am Beispiel der Dublettenprüfung. Zu (b) gibt es keine konkrete Antwort. | T (a), O (b) |
| F-25 | 00:38:42 | Lassen sich Standard-Rückweisungsgründe mit automatischer Mail an den Auftragnehmer hinterlegen, ohne das Mailfach zu öffnen? (André) | Sebastian [00:39:28–00:39:59]: d.velop erkennt die Unvollständigkeit und schickt in ein Postfach; die Kommunikation mit dem Kreditor liefe „über unsere Middleware", „Nicht über Developed Direction". [00:40:42–00:41:01]: d.velop sei „kein E-Mails-Kommunikationstool". | B (negativ für den Standard) **[PRÜFEN]** |
| F-26 | 00:40:01–00:40:09 | Habe ich Zugriff auf diesen Middleware-Automatismus? (Tanja) | André [00:40:09]: Gemeint ist die App, in der Tanja die Stammdaten pflegt. | B |
| F-27 | 00:40:38 | „Da ist kein E-Mail-Programm angeschlossen an dieses Develop." (Tanja, Feststellung bzw. Frage) | Sebastian [00:40:42]: „Jein". Die Post wird eingelesen, aber d.velop ist kein Kommunikationstool für Lieferantenerinnerungen. | B |
| F-28 | 00:41:27–00:41:39 | Wie werden Kürzungen umgesetzt (10.000 statt 8.000)? (André, Tanja) | Sebastian [00:41:44–00:42:12]: Netto- und Bruttobetrag anpassen, die Rechnung im Programm bearbeiten („gesamte Herd einmal installiert"), am besten mit Notiz. Tanja [00:42:00]: „es gibt keine Kürzungsmaske". | T |
| F-29 | 00:42:32–00:44:02 | Kann man positionsweise kürzen (4 auf 3 Stunden), sodass die Summe automatisch neu berechnet wird und das Original erhalten bleibt? (André) | Sebastian [00:43:01]: „Genau das würde funktionieren." In der Demo-Instanz nicht zeigbar; Aufteilung in Prozent je Position per Klick. [00:44:02]: „Selbstverständlich, richtig." | T (Zusage ohne Demo) **[RISIKO]** |
| F-30 | 00:44:02 | „Lokal bearbeiten" heißt: Es bleibt trotzdem eine Cloud-Lösung? (André) | Sebastian [00:44:13–00:44:32]: Lokal bearbeiten braucht „die gesamte Umgebung bei sich einmal auf der Hardware", gekoppelt mit der Cloud. | T (unklar) **[PRÜFEN]** |
| F-31 | 00:44:49 | Sehe ich bei der dritten Abschlagsrechnung, was bei der ersten und zweiten akzeptiert wurde? (Tanja) | Sebastian [00:45:13]: Die Abschlagsrechnungen 1–3 hängen in der Akte untereinander und sind nachvollziehbar. | T (nur Ablage, keine Betragsübersicht) |
| F-32 | 00:45:47 | Wird die kumulierte Abschlagsrechnung automatisch gegen die tatsächlich gezahlten Beträge geprüft? (André) | Sebastian [00:46:22]: „sowohl als auch … alles möglich … ob das alles tatsächlich über Develop abzubilden ist. Wissen wir grad noch nicht". Klärung mit Herrn Groß, nächstes Gespräch. | **O** |
| F-33 | 00:46:54 | Sind die Anforderungen der E-Rechnung (keine Streichungen, Rückgabe, neuer Prozess) berücksichtigt? („Trius") | Sebastian [00:47:29]: „Selbstverständlich". Die Felder werden automatisch mitgegeben, kein OCR nötig; ablehnen und über den Eskalationsprozess an den Ansprechpartner zurückleiten; der erneute Eingang läuft über Postfach, manuell oder automatisiert. | T **[WIDERSPRUCH]** zu F-25 |
| F-34 | 00:48:12–00:49:09 | Gibt es einen Abgleich, ob eine Freistellungsbescheinigung vorliegt (am Kreditor)? Prüft das System das selbst? (Tanja, André) | Sebastian [00:48:28–00:49:22]: Ein Ja/Nein-Feld wird vorab eingerichtet, „Nö, das geht alles über Develop". Die Entscheidung wird aber manuell abgehakt, eine Automatisierung ginge „ein Stück davor über die Middleware". | B (negativ: keine automatische Prüfung im Standard) **[WIDERSPRUCH]** |
| F-35 | 00:54:49 | Erkennt das System die Kategorie etc. einer manuell abgelegten Auftragsbestätigung nicht automatisch? (André) | Sebastian [00:54:52]: „Würde auch gehen … wenn es vom System automatisch reingeht, dann würde es auch automatisch erkennen." | T (nicht demonstriert) |
| F-36 | 00:57:09 | Wie viele Aktenebenen sind möglich? (André) | Sebastian [00:57:14–00:57:22]: beliebig viele, Empfehlung höchstens 4–5. | B |
| F-37 | 01:03:29 | Kann man die Rechnungsworkflows unterschiedlich gestalten? (André) | Sebastian [01:03:34]: „selbstverständlich". | B |
| F-38 | 01:04:47 | Gibt es eine Vertretungsregelung, etwa bei Krankheit? (André) | Sebastian [01:05:00]: Über den Abwesenheitsstatus, auch im Voraus, mit hinterlegter Vertretung; der Workflow ist entsprechend zu konfigurieren. | B |
| F-39 | 01:05:21 | Kann ein Admin die Vertretung für einen Erkrankten setzen? (André) | Sebastian [01:05:41–01:06:16]: Den genauen Prozess legt man im nächsten Gespräch fest; ein Admin hat Zugriff auf alles. | T |
| F-40 | 01:08:13 | Wird nach Aktenanzahl oder Dokumentgröße lizenziert? (André) | Sebastian [01:08:31]: „Das geht tatsächlich nach Lizenzgebühren." Er müsse nachschauen, wie viele Dokumente man speichern kann. | **O** |
| F-41 | 01:08:46 | Steckt eine KI dahinter, der man Fragen zu Verträgen stellen kann? (André) | Sebastian [01:09:07]: „Nicht über Develop direkt, aber über unsere Anwendungen." Thomas [01:09:09–01:09:35]: Die MDIS-KI-Plattform greift auf alle an die Middleware angebundenen Daten zu; Präsentation beim nächsten Mal. | T **[PRÜFEN]** |
| F-42 | 01:12:05–01:12:17 | Ist eine Verknüpfung d.velop–Evidanza möglich, um Auswertungen auf Basis von d.velop zu fahren? (André) | Thomas [01:12:20–01:12:39]: Ja; d.velop wird an die Middleware angebunden, darauf kann man zugreifen. | B (Zusage; Projektthema) |
| F-43 | 01:10:22 | Welche Informationen benötigt MDIS für das Angebot? (André) | Thomas [01:11:32]: Der Leistungskatalog sei „ausgefüllt … liegt uns vor"; er wird mitgeschickt. Welche Informationen MDIS noch braucht, bleibt unbeantwortet. | T |
| F-44 | 01:13:55–01:14:02 | Ist die KI-Plattform auch unabhängig von d.velop für App, Middleware und „E. V. R." relevant? (André) | Thomas [01:14:00–01:14:05]: „Komplett unabhängig. Da können wir alles anwenden." | B |

---

## 6 Aussagen von MDIS über Funktionen

Einordnung: **S** = als Standard dargestellt · **K** = als Konfiguration dargestellt · **P** = Projekt- oder Individualthema (MDIS-Middleware, App, KI-Plattform) · **N** = als nicht möglich dargestellt · **O** = offen gelassen. Aussagen von d.velop-Seite (Hersteller) gibt es keine, weil kein d.velop-Teilnehmer erkennbar ist. Alle Funktionsaussagen stammen von MDIS.

| Nr | Zeit | Sprecher | Aussage (verdichtet, mit Kurzzitat) | Einordnung | Bewertung / Risiko |
|---|---|---|---|---|---|
| Z-01 | 00:01:20 | Sebastian Pachon | Das Dashboard ist „beliebig" anpassbar: Widgets entfernen oder ergänzen, Kacheln vergrößern oder verkleinern. | S | **[PRÜFEN]** Laut LIESMICH gibt es „nur vier Standard-Widgets"; eine Managementsicht gehört ins Rechnungseingangsbuch. „Beliebig" ist überzogen. |
| Z-02 | 00:01:20 | Sebastian Pachon | „Develop legt tatsächlich nicht in Ordnern ab, es beschriftet Dokumente. und baut Ordner daraus selbst"; die Akten werden vorab definiert, ein Dokument liegt in mehreren Akten. | S | Fachlich zutreffend (A_06 Kap. 3.5 „Sichten, keine Ablageorte"). |
| Z-03 | 00:01:20 | Sebastian Pachon | OCR erkennt die Felder; „Das funktioniert alles automatisch, so dass die Dokumente auch entsprechend klassifiziert und qualifiziert werden". | S | **[RISIKO]** Überzeichnung. In derselben Demo musste die Lieferantennummer **manuell** nachgetragen werden [00:04:44]. |
| Z-04 | 00:04:28 | Sebastian Pachon | Mailpostfach-Import „Auf jeden Fall". Das System erkennt „je nach Rechnung oder je nach Angebot, was das ist" und legt in der richtigen Akte ab. | S/K | **[PRÜFEN]** Die automatische Klassifikation (Rechnung vs. Angebot) erfordert Regeln per RegEx oder KI-Dokumentanalyse (B_06 Z. 347, 371). Der Import selbst ist Standard. |
| Z-05 | 00:04:44 | Sebastian Pachon | Im Hintergrund laufen Workflows für Dublettenprüfung und Umsatzsteuerprüfung. | S | Weitgehend belegt: Duplikatsprüfung ist in smart invoice standardmäßig aktiv; § 14-Prüfung im document reader (B_02 Z. 355–390). |
| Z-06 | 00:08:01–00:09:31 | Thomas Gross | Er empfiehlt einen eigenen zentralen Lieferantenstamm in einer MDIS-App, entkoppelt vom DATEV-Nummernkreis, mit gegenseitiger Referenz und Konsolidierungsnummer. „Kleine App bauen" [00:09:04]. | P | **[RISIKO]** „Kleine App" unterschätzt den Umfang: drei Nummernkreise, bidirektionaler DATEV-Abgleich, mehr als 100 Mandanten, HV-Kreditoren. Der Aufwand muss ins Angebot. |
| Z-07 | 00:09:45–00:10:43 | Thomas Gross | Die MDIS-KI-Integrationsplattform („seit 4 Monaten") baut KI-gestützte Apps, Datenbereinigung und -anreicherung. Sie wird „ein paar Wochen kostenlos zur Verfügung" gestellt: „wir haben euch die Daten schon angebunden". | P (Zusage) | Kostenlose Zusage, im Angebot zu dokumentieren. |
| Z-08 | 00:11:13; 00:20:21 | Thomas Gross | Ein **Proof of Concept** für die KI-gestützte Lieferanten- bzw. Kreditorenkonsolidierung: „da verlangen wir auch nichts dafür". | P (Zusage) | **[RISIKO]** Kostenlose Leistungszusage ohne Umfang und Termin. |
| Z-09 | 00:13:50–00:13:53 | Thomas Gross | Der bidirektionale Kreditorenabgleich DATEV und Middleware „kriegen wir hin"; die DATEV-Schnittstelle sei „massiv aufgebohrt". | P | **[RISIKO]** Die Zusage kam, bevor der Hosting-Einwand geprüft war. Kurz darauf sagt Thomas selbst: „Das muss man prüfen" [00:14:23]. Die Doku zu d.velop connect for DATEV ist für uns nicht zugänglich (B_00 Z. 498–510). |
| Z-10 | 00:14:23 | Thomas Gross | Referenz: eine dedizierte DATEV-Schnittstelle bei „Deutschlands größtem Schadensanierer" mit 130 Servicemitarbeitern, mit „binär[em]" Abgleich inklusive Zahlungsstatus. Zu prüfen ist, ob sie in der „Rickencloud" läuft. | P/O | Referenz nicht verifiziert; die Lauffähigkeit beim externen Hoster ist **offen**. |
| Z-11 | 00:17:50–00:18:39 | Thomas Gross | Die Kreditorenkonsolidierung ist „nicht Aufgabe von Develop an der Stelle"; sie gehört in die Lieferantenstammdaten-App (BI-Zweck, drei Nummernkreise). | P | Saubere Abgrenzung. Für das Konzept wichtig: Die Konsolidierung liegt außerhalb von d.velop. |
| Z-12 | 00:19:01–00:19:49 | Thomas Gross | Das System prüft selbst, ob der Kreditor in den DATEV-Kreisen existiert. Per Klick „aus Developer heraus" wird eine Konsolidierungsnummer generiert, die d.velop automatisch übernimmt. | P | **[RISIKO]** Das ist eine Integration zwischen d.velop und der App (Individualentwicklung), kein Standard und nicht demonstriert. |
| Z-13 | 00:20:13–00:20:21 | Thomas Gross | Die Zuordnung zum DATEV-Kreditor soll KI-gestützt über Straße, Hausnummer und E-Mail laufen, nicht über den Namen. | P | Konzept; PoC-Zusage. |
| Z-14 | 00:21:26–00:22:35 | Thomas Gross | Für HV-Rechnungen gibt es ein eigenes Freigabe-Postfach und einen reinen Freigabeprozess in d.velop. Danach erhält die HV per Mail aus d.velop die formelle Freigabe: „kriegt er E-Mail aus Developer raus". | K/P | **[WIDERSPRUCH]** zu Z-32: d.velop sei „kein E-Mails-Kommunikationstool" [00:40:42–00:41:01]. **[PRÜFEN]** Eine Workflow-Aktion „E-Mail versenden" ist in der Doku nicht belegt (B_04 Z. 358, 561). Offen sind außerdem Lizenzen für Freigeber und Datenschutz. |
| Z-15 | 00:22:53 | Thomas Gross | Zusätzlicher Termin von 2–3 Stunden, „auch unbezahlt", um die Prozesse durchzugehen und zu skizzieren. | Zusage | Kostenlose Leistungszusage. |
| Z-16 | 00:24:10 | Sebastian Pachon | Die Werte werden „sowohl als auch" aus Rechnung und Stammdaten gelesen und abgeglichen. Fehlt ein Kreditor, legt man ihn manuell an; „eine nächste Schnittstelle" überträgt ihn später an DATEV. | K/P | **[PRÜFEN]** Kreditoranlage in d.velop mit Übertragung nach DATEV ist nicht belegt und widerspricht Thomas' Konzept, die Nummernvergabe in der App zu machen [00:19:36]. |
| Z-17 | 00:25:02–00:25:05 | Sebastian Pachon | Eine IBAN-Abweichung gegenüber den Stammdaten wird gemeldet: „Selbstverständlich", mit Eskalationsprozess und „human und der Loop". | S/K | **[PRÜFEN]** Belegt ist nur die Prüfung, *ob* eine IBAN auf dem Beleg steht (B_02 Z. 360–367). Ein Abgleich mit der Stammdaten-IBAN samt Warnung ist nicht belegt und wurde nicht gezeigt. |
| Z-18 | 00:26:35 | Sebastian Pachon | E-Mail-Benachrichtigungen lassen sich abschalten. Das Rechnungseingangsbuch filtert und gruppiert nach aktuellem Schritt. | S | Plausibel; das Rechnungseingangsbuch ist belegt (B_02). |
| Z-19 | 00:26:35 | Sebastian Pachon | Das Rechnungseingangsbuch zeigt, wie viel Zeit bis zur Zahlung bzw. bis zum Skonto-Ende bleibt („Opportunitätskosten"). | S | Nicht gezeigt; Fälligkeitsampel s. Z-51. |
| Z-20 | 00:29:16–00:29:23 | Sebastian Pachon | Ob die Fälligkeit aus dem Dokument oder den Stammdaten kommt, ist „Einstellungssache"; die manuelle Änderung bleibt immer möglich. | K | Plausibel (1.8). |
| Z-21 | 00:29:35–00:30:48 | Sebastian Pachon | Die Verteilungsmaske enthält Sachkonto, Kostenstelle, Kostenträger, Gesellschaft und sachliche Prüfer (Team oder Person). | S | Demonstriert. |
| Z-22 | 00:30:49 | Sebastian Pachon | In der sachlichen Prüfung sind die Felder bewusst schreibgeschützt; der Workflow sei „beliebig. Kann man so anpassen, wie man möchte". | K | **[PRÜFEN]** „Beliebig" ist überzogen. smart invoice hat feste Schritttypen und Regeln (B_02, B_04). |
| Z-23 | 00:31:41 | Sebastian Pachon | Auf die Frage, ob der Mandant automatisch erkannt und der Mandantennummer zugeordnet wird: „Das ist korrekt." | S | **[RISIKO] (hoch)** Nicht demonstriert. Laut Doku läuft die Mandantenerkennung **nur über Name und Anschrift**, nicht über die Steuernummer (B_02 Z. 167–175; LIESMICH). Mehrere Gesellschaften mit derselben Verwaltungsanschrift führen zu Fehlzuordnungen; die Agenda-Frage zur Trefferquote (2.2) blieb unbeantwortet. Must-Have. |
| Z-24 | 00:31:42 | Sebastian Pachon | Freigabe nach dem Vier-Augen-Prinzip; danach wird der Beleg an die FiBu bzw. DATEV weitergeleitet, „somit könnte die Buchung auch dort ausgelöst werden". | S/K | **[PRÜFEN]** Die DATEV-Übergabe wurde nicht gezeigt; Frequenz (5.1) und Übergabeweg sind nicht besprochen. Betragsgrenzen für die zweite Stufe wurden nicht gezeigt. |
| Z-25 | 00:31:42 | Sebastian Pachon | Die Historie des Dokuments zeigt Notizen, Titel, Bearbeiter, Besitzer und Erstellzeitpunkt. | S | Demonstriert (Teil von 1.6). |
| Z-26 | 00:33:25 | Sebastian Pachon | Weitere Dokumente lassen sich hochladen und verknüpfen. | S | Plausibel (1.7). |
| Z-27 | 00:33:44 | Sebastian Pachon | Die Zahlung beim Buchen auszulösen, „könnten wir über unsere Middleware machen und über unsere Technologie". | P | **[RISIKO]** Zahlungsauslösung ist Must-Have 5.5; Omikron wurde nicht angesprochen, die Katalognotiz nennt „BeSync". Das ist ein Projektthema und im Angebot auszuweisen. |
| Z-28 | 00:34:45 | Sebastian Pachon | Der Workflow lässt sich an das „Projektmanagementsystem" koppeln; eine Aufgabe erscheint dann auch dort. | P | **[PRÜFEN]** Vage und nicht belegt; das Zielsystem ist nicht benannt (Bim4You?). |
| Z-29 | 00:36:13 | Sebastian Pachon | Auswertung von Prozess- bzw. Liegezeiten je Benutzer: „…das kann … Develop insofern nicht abdecken", nur über eine eigene App oder ein Middleware-Dashboard. | N (Standard) / P | **[WIDERSPRUCH]** zum Leistungskatalog: 3.2 steht dort auf „S", die Liegezeit ist ausdrücklich gefordert. Die Aussage deckt sich mit der Recherche („Liegezeit existiert nirgends", B_00 AB; LIESMICH). Katalog 3.2 muss korrigiert werden. |
| Z-30 | 00:36:37; 01:12:20–01:12:39 | Sebastian Pachon; Thomas Gross | Evidanza: Sebastian lässt es zunächst offen, Thomas bestätigt es später über die Anbindung an die Middleware. | P | Projektthema; im Angebot auszuweisen. |
| Z-31 | 00:37:45 | Sebastian Pachon | Rechnungen lassen sich ablehnen und zurückgeben, automatisiert oder manuell; die Dublettenprüfung zeigt Duplikate an. | S | Belegt (B_02: Ablehnen-Aktion, Duplikatsprüfung). |
| Z-32 | 00:39:28–00:41:01 | Sebastian Pachon | Die Kommunikation mit dem Kreditor nach einer Rückweisung läuft „nicht über Develop direkt", sondern über die Middleware. d.velop sei „kein E-Mails-Kommunikationstool". | N (Standard) / P | **[PRÜFEN]** In der d.velop-Doku (alphaflow-Rechnungsmodul) gibt es die Aktionen „**Ablehnungsschreiben erstellen**" und „**Rechnungsmail versenden**" (B_02 Z. 96). Für smart invoice selbst ist das nicht belegt, aber auch nicht widerlegt. **[WIDERSPRUCH]** zu Z-14 und Z-39. |
| Z-33 | 00:41:01 | Sebastian Pachon | Eine Dublette lässt sich annehmen, aber nur mit Begründung. | S | Belegt (B_02 Z. 377–380: Warnung akzeptieren, Begründung, Protokoll). |
| Z-34 | 00:41:44–00:42:12 | Sebastian Pachon | Eine Kürzung erfolgt über angepassten Netto- und Bruttobetrag, „sofern das genehmigt ist". Zur Bearbeitung „braucht man nur die gesamte Herd einmal installiert zu haben". Am besten mit Notiz auf dem Dokument. | K | **[RISIKO]** Werden die Rechnungsbeträge selbst überschrieben statt einen Kürzungs- bzw. Zahlbetrag zu führen, ist das GoBD-kritisch (1.6). Die Aussage zur lokalen Installation widerspricht 1.2 („ohne lokale Installation"). |
| Z-35 | 00:43:01–00:44:02 | Sebastian Pachon | Positionsweise Kürzung „würde funktionieren", die Gesamtsumme wird „Selbstverständlich" automatisch neu berechnet. Die Demo-Instanz sei „nicht dafür ausgelegt"; eine prozentuale Aufteilung auf Positionen gehe per Klick. | S/K | **[RISIKO] (hoch)** Die Zusage kam ohne Demo, bei einem vom Kunden als häufig bezeichneten Vorgang. smart invoice kennt Positionszeilen und Zu- bzw. Abschläge (B_02 Z. 200–235); eine automatische Neuberechnung bei geänderter Menge und der Erhalt des Originals sind nicht belegt. Vor dem Angebot verifizieren. |
| Z-36 | 00:44:13–00:44:32 | Sebastian Pachon | „Lokal bearbeiten" erfordere „die gesamte Umgebung bei sich einmal auf der Hardware", gekoppelt mit der Cloud. | K | **[PRÜFEN]** Fachlich unklar und potenziell falsch. Gemeint sein könnte eine Desktop- oder Office-Integration. Klingt nach lokaler Installation, im Widerspruch zu 1.2. Klären. |
| Z-37 | 00:45:13 | Sebastian Pachon | Abschlagsrechnungen hängen über Rechnungsnummer bzw. Akteninhalt in der Akte untereinander (Abschlag 1, 2, 3). | S | Nur die Ablage; keine Betragskumulation (5.2 = N). |
| Z-38 | 00:46:22 | Sebastian Pachon | Kumulierte Prüfung: „es ist am Ende des Tages erfahrungsgemäß auch alles möglich … Wissen wir grad noch nicht. Haben ja den Fall so noch nicht gehabt". | O | **[WIDERSPRUCH]** zum Katalog (5.2 = N, „Bau-ERP-Funktion, Entwicklung nicht vorgesehen"). Mit „alles möglich" weckt MDIS eine Erwartung. |
| Z-39 | 00:47:29 | Sebastian Pachon | E-Rechnung: d.velop sei „sehr gut dafür ausgelegt", Felder und Positionen kämen automatisch mit, OCR entfällt. Ablehnung und Rückleitung „über den Eskalationsprozess … an dem jeweiligen Ansprechpartner". | S | Import von XRechnung/ZUGFeRD ist Standard. **[PRÜFEN]** Nicht demonstriert, auch nicht die kombinierte XML-Visualisierung (2.4). **[WIDERSPRUCH]** zu Z-32 (keine Lieferantenkommunikation aus d.velop). |
| Z-40 | 00:48:28–00:49:22 | Sebastian Pachon | Freistellungsbescheinigung: ein Ja/Nein-Feld („Kästchen und ein X"), „Nö, das geht alles über Develop". Die Entscheidung wird manuell abgehakt, eine Automatisierung ginge „über die Middleware". | K/P | **[WIDERSPRUCH]** in sich („geht alles über Develop" gegenüber manuell bzw. Middleware). **[PRÜFEN]** Einen Ja/Nein-Datentyp gibt es nicht, nur eine Wertemenge Ja/Nein (LIESMICH). Katalog 2.7 = N. |
| Z-41 | 00:49:33–00:53:32 | Sebastian Pachon | Beliebig viele Postfächer für verschiedene Zwecke (Angebote, Verträge, Rechnungen). Konfiguriert werden Importprofil und zugelassene Absender (Einzeladresse, Domain, alle); alle zuzulassen wird nicht empfohlen. E-Mail und Anhang werden importiert. | S | Belegt (B_06 Z. 304–307, Wildcards; „alle" = `*@*`). |
| Z-42 | 00:54:52 | Sebastian Pachon | Bei automatischem Eingang erkennt das System Kategorie, Gesellschaft, Kreditor und Objekt „selbstverständlich". | S | **[PRÜFEN]** Setzt Regeln bzw. KI-Konfiguration je Kategorie voraus (B_06). Nicht demonstriert. |
| Z-43 | 00:55:02 | Sebastian Pachon | Eine Auftragsbestätigung liegt automatisch in zwei Akten: Kreditorenakte „Elektro Nordlicht GmbH" und Objektakte. | S | Demonstriert. |
| Z-44 | 00:55:02; 00:57:22 | Sebastian Pachon | „Wir brauchen nur einmal von euch, wie diese Dokumentenstruktur aussehen sollte." Livos soll die „Folder Structure" liefern, MDIS bildet sie ab. | K | To-do für Livos. „nur einmal" unterschätzt den Konzeptionsaufwand. |
| Z-45 | 00:57:14–00:57:22 | Sebastian Pachon | Aktenebenen beliebig, Empfehlung höchstens 4–5. | S | Akten in Akten sind belegt (B_01 Z. 268). |
| Z-46 | 00:57:41 | Sebastian Pachon | Eigenschaften sagen dem System, was eine Eingangsrechnung ist: „…wenn ein Kreditor vorhanden ist, … der Mandant Mandantenname, Rechnungsnummer". Das System könne dann automatisch zuweisen. | K | **[PRÜFEN]** Vereinfacht dargestellt. Kategorien werden über Klassifikation bzw. Regeln zugewiesen, nicht dadurch, dass Eigenschaften vorhanden sind. |
| Z-47 | 00:59:47–01:00:10 | Sebastian Pachon | Aufgaben werden mit Priorität, Zustelldatum, Fälligkeit, Erinnerung und Selbstbenachrichtigung erstellt. | S | Demonstriert. |
| Z-48 | 01:00:10 | Sebastian Pachon | Prozesse lassen sich manuell starten („Angebot prüfen und vergleichen", „Prüfung und Freigabe", Rechnungseingangsprozess). | S | Demonstriert. |
| Z-49 | 01:00:10 | Sebastian Pachon | Das Admin-Dashboard zeigt Belege im Umlauf, verarbeitete Belege, Onboarding, aufgetretene Probleme und Workflowstatus: „bei euch würden selbstverständlich keine Probleme auftreten". | S | **[RISIKO]** Die Aussage „keine Probleme" ist nicht haltbar und könnte als Zusage ausgelegt werden. |
| Z-50 | 01:00:10 | Sebastian Pachon | Man kann „beliebig viele Workflows" anhängen (Dokumente, Schriftverkehr, Vertragsmanagement). Einstellbar sind Schritte, Zugriffe, Prüfer, Eskalation, Workflow-Start, Ausgleichspositionen, Zuschläge und das Abschalten der Rechnungslesung. | S/K | Plausibel. Eskalation nur benannt, nicht gezeigt (3.3). |
| Z-51 | 01:03:34 | Sebastian Pachon | Workflows sind unterschiedlich gestaltbar. Die Fälligkeitsampel steht in der Demo auf 10 Tage (gelb) bzw. 5 Tage (rot) vor Netto-Fälligkeit. | S/K | Demonstriert (Ampel). |
| Z-52 | 01:04:23 | Sebastian Pachon | Benutzer werden angelegt, Berechtigungen je Gruppe vergeben. | S | Gezeigt (Admin-Maske). |
| Z-53 | 01:05:00 | Sebastian Pachon | Vertretung „Selbstverständlich". Dafür müsse man „den Workflow entsprechend konfigurieren". Abwesenheitsstatus, auch im Voraus, mit Vertretung. | S/K | **[PRÜFEN]** Laut Doku ist Vertretung **keine** Workflow-Funktion, sondern eine Benutzereinstellung. Aufgaben laufen **nicht automatisch** an den Vertreter über; der Vertreter sieht sie unter „Vertretung". Der Vorgesetzte kann mit Adminrechten die Abwesenheit für Erkrankte setzen (B_00 V6). Sprachregelung korrigieren. |
| Z-54 | 01:05:45–01:06:16 | Sebastian Pachon | Der Admin hat Zugriff auf alle Tickets, offenen Rechnungen und Dokumente. Rechte lassen sich abteilungsweise vergeben (Marketing, Buchhaltung). | S | **[RISIKO]** Die Must-Have-Mandantentrennung (1.1) wurde **nicht** gezeigt; der geplante Beweis per Rolle U2 (A_06 R2) fehlte. |
| Z-55 | 01:06:18 | Sebastian Pachon | Suche nach Kategorie, Kreditor, Auftragsnummer und Rechnungsdaten; Akten gelb (gefüllt) oder grau (leer). | S | Demonstriert. |
| Z-56 | 01:08:31 | Sebastian Pachon | Lizenz „geht tatsächlich nach Lizenzgebühren"; Speichergrenzen müsse er nachschauen. | O | Nicht beantwortet; Lizenzmodell (Named User?) nicht genannt. |
| Z-57 | 01:09:07–01:09:35 | Sebastian Pachon; Thomas Gross | Inhaltliche KI-Fragen an Verträge gehen „Nicht über Develop direkt, aber über unsere Anwendungen", also über die MDIS-KI-Plattform. | P | **[PRÜFEN]** d.velop hat eigene KI-Bausteine (d.velop pilot, document intelligence hub, B_06 Z. 469–470). Ob es eine Frage-Antwort-Funktion gibt, ist in unseren Quellen nicht belegt. Die Positionierung „nicht über d.velop" sollte geprüft werden. |
| Z-58 | 01:09:48 | Sebastian Pachon | „Was Sie gesehen haben, ist jetzt kein Zukunftsbild. Das läuft auch schon … bei uns intern und auch bei unseren Kunden." | – | Referenzaussage, nicht belegt. |
| Z-59 | 01:11:32; 01:12:56 | Thomas Gross | Der Leistungskatalog ist in Spalte F ausgefüllt und geht mit dem Angebot raus. | – | **[RISIKO]** Mehrere Einträge in Spalte F widersprechen den Aussagen im Termin: 3.2 „S" gegenüber Z-29, 2.2 „S" ohne Vorbehalt gegenüber LIESMICH, 2.6 „S" gegenüber der manuellen Freistellungsprüfung. Vor dem Versand korrigieren. |
| Z-60 | 01:13:20–01:14:05 | Thomas Gross | Zwei Vorschläge: (1) die KI-Integrationsplattform im Kontext der Livos-Apps und Bilanzauswertungen testen, (2) ein Workflow-Termin zu Anbindung und Abgrenzung. Die KI-Plattform sei „komplett unabhängig" einsetzbar. | P | Nächste Schritte, s. Kap. 8. |

**Verdichtung Kapitel 6.** Viele Funktionen wurden als „selbstverständlich" oder „geht" bestätigt, ohne sie zu zeigen: Mandantenerkennung, IBAN-Abgleich, positionsweise Kürzung, E-Rechnung und automatische Klassifikation. Mehrere Kundenwünsche wurden an die **MDIS-Middleware bzw. -App** verwiesen: Kreditorenkonsolidierung, Nummerngenerierung, Lieferantenkommunikation bei Rückweisung, Zahlungsauslösung, Durchlaufzeit-Reporting, Evidanza, Freistellungsautomatik, KI-Vertragsanalyse. Das verschiebt Aufwand in Individualprojekte, und genau dort ist der Kunde skeptisch [00:40:13]. Die Aussagen zur E-Mail-Fähigkeit von d.velop sind in sich widersprüchlich (Z-14, Z-32, Z-39).

---

## 7 Einwände, Bedenken, Skepsis und positive Reaktionen des Kunden

### 7.1 Einwände, Bedenken, Skepsis
| Nr | Zeit | Sprecher | Einwand / Bedenken | Kontext |
|---|---|---|---|---|
| E-01 | 00:09:39–00:09:44 | André Töpper | „Es ist halt ein riesiger, einmaliger erster Aufwand, um diese das hinzubekommen." | Kreditoren-Mapping über mehr als 100 Gesellschaften |
| E-02 | 00:13:02–00:13:16 | André Töpper; Christian Weigel | Die HV zur Nutzung zu verpflichten, „wäre ein Riesending … administrativ ein unglaublich … großer Aufwand". Christian: „Glaub ich auch nicht." | Thomas' Idee, die HV über ein System scannen zu lassen |
| E-03 | 00:14:00–00:14:11 | Christian Weigel | Externes Hosting und „ricken Cloud" schränken die Auswertungen ein: „inwieweit diese Abgleiche alle so funktionieren". | DATEV-Abgleich |
| E-04 | 00:16:05–00:16:30 | André Töpper | PM-Rechnungen in d.velop „wäre ja eher neu"; „bei uns bleibt das hier eigentlich nicht". | Scope der PM-Rechnungen |
| E-05 | 00:16:49–00:17:07 | Christian Weigel | Derselbe Kreditor bei HV und Livos, „das muss ja einigermaßen transparent sein". | Doppelte Kreditorennummern |
| E-06 | 00:21:07 | Tanja Brecht | HV-Rechnungen „werden doch nicht über Develop erfasst, weil die werden ja trotzdem beim Verwalter gebucht". | Einwand gegen die Annahme von „Trius" |
| E-07 | 00:21:46–00:21:53 | André Töpper; Christian Weigel | „…sie werden ja auch nicht von Trios bezahlt, sondern vom Property Manager." / „…da muss man dann aufpassen, weil das ja ein separater Prozess ist." | Freigabe-Postfach für HV |
| E-08 | 00:23:21–00:23:35 | André Töpper | „wir haben noch andere Anbieter angehört … dann werden wir entscheiden, mit wem wir quasi weitergehen". Der Prozess ist noch nicht festgelegt. | Wettbewerb; der Prozess-Workshop kommt erst nach der Auswahl |
| E-09 | 00:33:53 | André Töpper | „hört sich grad sehr einfach an, ich glaube, das würde dann wahrscheinlich auch im Detail noch mal besprochen werden müssen" | Zahlung beim Buchen über die Middleware |
| E-10 | 00:39:57 | André Töpper | „Also nicht über Develop direkt." | Rückweisungsmail |
| E-11 | 00:40:13–00:40:21 | André Töpper | „…das ist halt alles manuell zu programmieren und es läuft nicht alles so, wie man sich es immer erhofft. Also, ich bin da immer bei Middleware ein bisschen vorsichtig" | **Zentrale Skepsis gegenüber Middleware-Lösungen** |
| E-12 | 00:40:38 | Tanja Brecht | „Da ist kein E-Mail-Programm angeschlossen an dieses Develop." | Enttäuschte Feststellung |
| E-13 | 00:42:00–00:42:04 | Tanja Brecht | „Also, es gibt keine Kürzungsmaske, sondern man würde einfach die Beträge anpassen" | Kürzungen |
| E-14 | 00:42:32–00:42:59 | André Töpper | Bei langen Rechnungen „müssten wir immer händisch zusammenrechnen … da würde uns ja sonst nicht geholfen werden". | Anforderung positionsweise Kürzung |
| E-15 | 00:44:02–00:44:13 | André Töpper | Er vergewissert sich: „lokal bearbeiten heißt …, es bleibt trotzdem 'ne Cloud-Lösung". | Irritation durch „lokal bearbeiten" |
| E-16 | 00:45:47 | André Töpper | Automatische Prüfung kumulierter Abschläge? Bleibt offen. | Bau/VOB |
| E-17 | 00:49:09 | André Töpper | „Das würde er nicht tun. Das müssten ja wir prüfen, richtig?" | Freistellungsbescheinigung |
| E-18 | 00:49:25–00:49:28 | André Töpper | „…Das, was wir in der Middleware unterlegen könnten … aber das werden wir bestimmt nicht tun." | Ablehnung, Middleware-Tabellen zu pflegen |
| E-19 | 00:54:49 | André Töpper | „Das würde er aber nicht automatisch erkennen." | Automatische Klassifikation |
| E-20 | 01:08:13 | André Töpper | Lizenz nach Akten oder Größe? | Kostensensibilität |

### 7.2 Positive Reaktionen
| Nr | Zeit | Sprecher | Reaktion | Bezug |
|---|---|---|---|---|
| P-01 | 00:10:41–00:11:08 | André Töpper | „OK." (mehrfach), Interesse an der automatischen Übernahme | KI-Mapping der Kreditoren |
| P-02 | 00:18:39 | André Töpper | „Ja, OK, verstehe. Müsste über die App erfahren." | Konsolidierung in der Stammdaten-App |
| P-03 | 00:21:57 | Tanja Brecht | „…dann wäre das natürlich auch eine transparente Geschichte, dass man auch diese Rechnungen verfolgen kann." | Freigabeprozess für HV-Rechnungen |
| P-04 | 00:22:41 | André Töpper | „Es wäre nicht verkehrt." | dto. |
| P-05 | 00:22:41–00:22:45 | „Trius" | „Hätte auch den Riesenvorteil, dass man die Vollständigkeit der Rechnungen hat." | dto. |
| P-06 | 00:22:46–00:22:52 | Tanja Brecht | „…die Transparenz, wo hängt die Rechnung und der Vertreter kann reingucken … kleines On-Top." | dto. |
| P-07 | 00:23:21 | André Töpper | „Nee, gerne." | Vorschlag eines Prozess-Workshops (nach der Auswahl) |
| P-08 | 00:25:23 | André Töpper | „Alles klar, super. Danke" | IBAN-Abgleich |
| P-09 | 00:48:10 | „Trius" | „OK, super." | Antwort zur E-Rechnung |
| P-10 | 01:09:35 | André Töpper | „…sicherlich sinnvoll im zweiten Step" | KI-Plattform |
| P-11 | 01:10:22 | André Töpper | „ganz lieben Dank an Sie alle, an Herrn Pachon, vor allem für die Vorstellungen" | Demo insgesamt |
| P-12 | 01:13:55–01:14:07 | André Töpper | KI-Plattform „wäre auch interessant und relevant für die App und … die Middleware"; „OK, super." | KI-Plattform unabhängig von d.velop |

**Gesamteindruck (Annahme):** Der Kunde reagiert freundlich und interessiert, aber abwartend. Explizite Begeisterung für einzelne d.velop-Funktionen gibt es nicht. Positiv aufgenommen wurden vor allem die **Transparenz bei HV-Freigaben** und die **KI-Plattform bzw. Stammdatenkonsolidierung**, beides MDIS-Themen. Skeptisch bleibt Livos bei allem, was „über die Middleware" gelöst werden soll, sowie bei Kürzungen und Abschlägen.

---

## 8 Entscheidungen, Vereinbarungen, nächste Schritte, To-dos

Förmliche Entscheidungen fielen im Termin nicht. Vereinbart bzw. zugesagt wurden:

| Nr | Was | Wer | Bis wann | Beleg | Status |
|---|---|---|---|---|---|
| A-01 | **Angebot** für ca. 80 Nutzer (80–100), mit Bezug und Referenz auf den Leistungskatalog; nicht abschätzbare Punkte dürfen ausgeklammert werden | MDIS (Thomas Gross; Sales Valeria Filimonow) | „in dieser Woche" (Wunsch Livos). Bei Termin am 22.09.2026 wäre das KW 39, also bis ca. 25.09.2026 (**Annahme**) | [01:10:22 André Töpper]; [01:13:20 Thomas Gross] „Wir melden uns mit dem Angebot" | zugesagt |
| A-02 | Den **ausgefüllten Leistungskatalog** (Spalte F) an Livos senden | MDIS | mit dem Angebot | [01:11:36 André Töpper]; [01:13:03 Thomas Gross] „dann schicken wir das schon mal zu" | zugesagt |
| A-03 | Im Angebot die im Termin besprochenen Zusatzthemen erwähnen, v. a. den **Abgleich mit DATEV und den Hausverwaltern** | MDIS | mit dem Angebot | [01:11:47 André Töpper]; [01:11:52 Thomas Gross] „die würde ich aber dann zusätzlich erwähnen" | zugesagt |
| A-04 | Interner Austausch und **Entscheidung mit dem Management**, Vergleich mit anderen Anbietern | Livos (André Töpper) | „in der kommenden Woche" nach Angebotseingang | [00:23:21], [01:10:22–01:11:18 André Töpper] | angekündigt |
| A-05 | Unbezahlter **Prozess-Termin (2–3 h)**, um die Prozesse im Detail durchzugehen und zu skizzieren (HV-Freigabe, Stammdaten usw.) | MDIS (Vorschlag Thomas); Livos | nach der Anbieterentscheidung (André) | [00:22:53 Thomas Gross]; [00:23:21–00:23:35 André Töpper] | vorgeschlagen, nicht terminiert |
| A-06 | **Workflow-Termin** „rund um Developer": Anbindung und Abgrenzung zu anderen Systemen und Arbeitsprozessen | MDIS/Livos | offen („kurzfristig") | [01:13:26–01:13:50 Thomas Gross] | vorgeschlagen |
| A-07 | **KI-Integrationsplattform** präsentieren bzw. testen (einige Wochen kostenlos), im Kontext der Livos-Apps und Bilanzauswertungen | MDIS (Thomas Gross) | „beim nächsten Mal" bzw. „im zweiten Step" | [00:10:12], [01:09:09], [01:13:20 Thomas Gross]; [01:09:35 André Töpper] | vorgeschlagen, angenommen als 2. Schritt |
| A-08 | **Kostenloser PoC KI-gestützte Kreditorenkonsolidierung**: DATEV-Kreditoren je Mandant in einen Konsolidierungsnummernkreis überführen | MDIS (Thomas Gross) | offen | [00:11:13] „vielleicht aufschreiben, dass man das als Proof of Concept mal zeigt"; [00:20:21] | angeboten, nicht terminiert |
| A-09 | Klären, ob **Evidanza** die Durchlaufzeit-Auswertung abdecken kann | Sebastian Pachon mit Thomas Gross | „im Rahmen des nächsten Gesprächs" | [00:36:37 Sebastian Pachon]; Teilantwort [01:12:20 Thomas Gross] | offen/teilweise |
| A-10 | Klären, ob die **automatische Prüfung kumulierter Abschlagsrechnungen** möglich ist | Sebastian Pachon mit Thomas Gross | „im nächsten Gespräch" | [00:46:22 Sebastian Pachon] | offen |
| A-11 | **Vertretungsprozess** (Admin setzt die Vertretung für Erkrankte) im Detail festlegen | MDIS/Livos | „im nächsten Gespräch" | [01:05:41 Sebastian Pachon] | offen |
| A-12 | **Workflow-Design** festlegen: Anzahl Stationen, Verantwortliche, Skalierung | MDIS/Livos | „kommendes Gespräch" | [00:26:35 Sebastian Pachon] | offen |
| A-13 | **Ordner- bzw. Aktenstruktur** („Folder Structure") liefern, damit MDIS Kategorien und Berechtigungen abbilden kann | Livos | offen | [00:55:02], [00:57:22 Sebastian Pachon] | gefordert |
| A-14 | **Speicher- und Dokumentgrenzen** je Instanz bzw. Lizenz nachschauen | Sebastian Pachon | offen | [01:08:31] | zugesagt |
| A-15 | Prüfen, ob die **DATEV-Schnittstelle** in der „Rickencloud"-Umgebung des externen Dienstleisters läuft | MDIS (Thomas Gross) | offen | [00:14:23] „das muss man sich einfach anschauen" | implizites To-do |
| A-16 | **Zahlungsauslösung beim Buchen** im Detail besprechen | MDIS/Livos | offen | [00:33:53 André Töpper] | offen |
| A-17 | Weitere Informationsbedarfe für das Angebot an Livos melden | MDIS | laufend | [01:13:16 André Töpper] „melden Sie sich gerne, wenn Sie noch Informationen benötigen" | offen |

---

## 9 Offene Punkte und ungeklärte Themen

**A. Agenda-Fragen, die unbeantwortet blieben (Agenda-Folie 4)**
1. **1.1 Mandantenmodell:** eine Instanz mit Gesellschaft als Eigenschaft oder getrennte Mandanten? Nicht besprochen; in der Demo nur „Norden/Süden" [01:06:18].
2. **2.2 Trefferquote Mandantenzuordnung** bei gleicher Verwaltungsanschrift: nicht besprochen. Sebastian bestätigte pauschal „Das ist korrekt" [00:31:41]; die Doku nennt nur Name und Anschrift (Z-23).
3. **4.2 Ad-hoc-Freigabe ohne Lizenz** für externe Projektbeteiligte: nicht angesprochen.
4. **5.1 DATEV-Übergabefrequenz und Übergabeweg** (inklusive Beleg): nicht angesprochen, die Übergabe nicht gezeigt.
5. **5.5 Zahlungsauslösung, Omikron:** Omikron nicht genannt. Nur „über unsere Middleware" [00:33:44].
6. **Lizenz- und Mengengerüst:** Lizenzmetrik (Named User? Akten? Speicher?) offen [01:08:13–01:08:31].

**B. Fachliche Themen, die offen blieben oder widersprüchlich beantwortet wurden**
7. **Führung der Kreditoren-Stammdaten:** Zielbild Lieferanten-App mit Konsolidierungsnummer und drei Nummernkreisen [00:18:01]. Offen sind Umfang, Kosten, Verantwortung und ob es Teil des d.velop-Angebots ist.
8. **Bidirektionaler DATEV-Abgleich** unter dem externen Hosting („ricken Cloud"): offen [00:14:00–00:14:23].
9. **Scope der PM-Rechnungen:** Sollen HV-gebuchte Rechnungen mit AM-Freigabe in d.velop laufen? Offen sind Postfach, Freigabemail an die HV, Lizenzen und die Betragsgrenzen der PM [00:15:18, 00:20:45–00:22:52].
10. **Rückweisung mit Lieferantenmail:** widersprüchliche Aussagen (Z-14, Z-32, Z-39). Ob der d.velop-Standard das kann, ist nicht geprüft.
11. **Positionsweise Kürzung mit Originalerhalt und automatischer Summenberechnung:** zugesagt, nicht gezeigt (Z-35). Offen ist, ob das GoBD-konform ist, wenn Beträge überschrieben werden (Z-34).
12. **„Lokal bearbeiten"**: Was genau ist gemeint, braucht es eine lokale Installation? Widerspruch zu 1.2 (Z-36).
13. **Kumulierte Abschlagsrechnungen, 5.2:** offen, Klärung mit Herrn Groß [00:46:22].
14. **Freistellungsbescheinigung, 2.7:** nur manuelles Abhaken; Automatik über die Middleware lehnt Livos ab [00:49:28].
15. **E-Rechnung:** Visualisierung (2.4) und Rückgabeprozess nicht gezeigt.
16. **Durchlaufzeit- bzw. Liegezeitauswertung je Benutzer (3.2):** nicht im d.velop-Standard, Weg über Evidanza bzw. Middleware; Katalogeintrag „S" widersprüchlich.
17. **Evidanza-Anbindung:** Umfang und Aufwand offen.
18. **Freigaben für Ausbuchungen auf Mietkonten:** nur pauschal „sowohl als auch" [00:37:45].
19. **Vertretung durch Admin bzw. Vorgesetzte:** vertagt [01:05:41]. Die Sprachregelung „Workflow konfigurieren" ist fachlich ungenau (Z-53).
20. **Eskalation (3.3):** nur erwähnt, nicht gezeigt; Fristen je Gesellschaft offen.
21. **Kostenstellenaufteilung mit Standardschlüsseln je Gesellschaft (2.8):** nicht behandelt.
22. **KI-Kontierungsvorschläge (2.5):** nicht behandelt.
23. **Klärfall unbekannte Gesellschaft (2.3):** nicht gezeigt; diskutiert wurde nur der unbekannte Kreditor.
24. **Strikte Mandantentrennung bei den Berechtigungen (1.1, 1.5):** nicht demonstriert.
25. **GoBD-Export je Gesellschaft bei Verkauf (1.6):** nicht behandelt.
26. **App iOS/Android (1.3):** nicht behandelt.
27. **Externe Kern-Partner mit Web-Zugang (4.3):** nicht behandelt.
28. **BIM4You (5.3):** nur im Einstieg genannt [00:00:22]. Die vage „Projektmanagementsystem"-Kopplung [00:34:45] ist unklar.
29. **REST-API bzw. ERP-Anbindung der PM (5.4):** nicht explizit.
30. **Verträge und Vertragsmanagement:** nur erwähnt [00:34:11, 01:00:10]; KI-Vertragsanalyse soll über die MDIS-Plattform laufen (Z-57).
31. **Papierpost, Scan und Postverteilung:** Livos scannt Post [00:38:42]; Scan bzw. mail dispatcher wurden nicht gezeigt, nur der Mailimport.

**C. Organisatorisch offen**
32. Rolle und Beziehung von **Trios** und Steuerberater: Wer bucht, wer zahlt, wer braucht welche Rechte?
33. Identität des Sprechers „Trius".
34. Wer entscheidet bei Livos, wer ist Projektverantwortlicher?
35. Welche Informationen braucht MDIS noch für das Angebot? Die Frage [01:10:22] wurde nicht konkret beantwortet.
36. Der ausgefüllte Leistungskatalog muss vor dem Versand konsistent zu den Termin-Aussagen gemacht werden (Z-59).
37. Kostenlose Zusagen (KI-Plattform-Test, PoC, Prozess-Workshop) sind nicht nach Umfang und Termin definiert.

---

## 10 Abgleich mit dem Leistungskatalog (alle 29 Nummern)

Legende „Behandelt": **ja** = ausdrücklich besprochen oder gezeigt · **teilw.** = gestreift bzw. pauschal · **nein** = nicht behandelt. „Kat." = Katalogpriorität / MDIS-Eintrag in Spalte F.

| ID | Anforderung | Kat. | Behandelt? | Ergebnis / Stand in 1 Zeile |
|---|---|---|---|---|
| 1.1 | Echte Mandantenfähigkeit | Must / K | teilw. | Über 100 Gesellschaften prägen die Stammdatendiskussion [00:06:00]; Gesellschaft als Eigenschaft, in der Demo „Norden/Süden" [01:06:18]. Mandantenmodell und strikte Trennung weder besprochen noch gezeigt. |
| 1.2 | Webbasierter Zugriff | Must / S | teilw. | Browser-Cloud implizit gezeigt; André: „es bleibt trotzdem 'ne Cloud-Lösung" [00:44:02]. **Widerspruch:** „lokal bearbeiten" mit Umgebung „auf der Hardware" [00:44:32]. |
| 1.3 | App | Could / S | nein | Nicht erwähnt. |
| 1.4 | Individuelle Workflows | Must / S | teilw. | Workflow „beliebig" anpassbar [00:30:49], Varianten möglich [01:03:34], Vier-Augen erwähnt [00:31:42]. Freigabegrenzen und Ketten je Gesellschaft nicht gezeigt; Details „kommendes Gespräch" [00:26:35]. |
| 1.5 | Rollen und Rechte | Must / S | teilw. | Admin und Gruppen [01:04:23], abteilungsbezogene Rechte [01:05:47]; Wunsch Buchen-Maske nur für Steuerberater [00:33:28]. Externe Partner und Mandantentrennung nicht gezeigt. |
| 1.6 | Revisionssicherheit und GoBD | Must / S | teilw. | Historie und Protokoll gezeigt [00:31:42]; Dublette nur mit Begründung [00:41:01]. Export je Gesellschaft nicht besprochen; die Kürzung per Betragsänderung ist GoBD-kritisch [00:41:44]. |
| 1.7 | Ablage weiterer Nachweise | Should / S | ja | Nachweis anhängen bestätigt [00:33:21–00:33:25]; Auftragsbestätigung in zwei Akten gezeigt [00:55:02]. |
| 1.8 | Händische Anpassbarkeit | Must / S | ja | Fälligkeit manuell [00:29:23], Beträge bei Kürzung [00:41:44], Kreditor manuell [00:24:10]. Protokollierung der Änderung nicht gezeigt. |
| 2.1 | Automatischer Postfach-Import | Must / S | ja | Frage und Zusage [00:04:13–00:04:28]; Postfachkonfiguration mit zugelassenen Absendern und Live-Mail gezeigt [00:49:33–00:53:32]. Sammelpostfach für mehrere Empfänger nicht explizit. |
| 2.2 | KI-Erkennung und Mandantenzuordnung | Must / S | teilw. | OCR-Upload gezeigt [00:01:20]; Lieferantennummer manuell nachgetragen [00:04:44]. Mandantenerkennung pauschal „korrekt" [00:31:41] ohne Demo; Trefferquote bei gleicher Anschrift offen. **[RISIKO]** |
| 2.3 | Unbekannte Gesellschaft (Klärfall) | Must / K | nein | Klärfall nicht gezeigt; diskutiert wurde nur der unbekannte **Kreditor** [00:18:44–00:19:49]. |
| 2.4 | E-Rechnung (ZUGFeRD, XRechnung) | Must / S | teilw. | Frage zum Rückgabeprozess [00:46:54], Antwort „sehr gut dafür ausgelegt" [00:47:29]. Import und XML-Visualisierung nicht gezeigt. |
| 2.5 | Buchungs- und Kontierungsvorschläge (KI) | Must / S | nein | Sachkonto, Kostenstelle und Kostenträger nur manuell in der Verteilung gezeigt [00:29:35]; lernende KI-Vorschläge nicht besprochen. |
| 2.6 | Rechnungsprüfung (steuerlich u. a.) | Must / S | teilw. | Dubletten- und USt-Prüfung erwähnt [00:04:44], IBAN-Abgleich zugesagt [00:25:02], sachliche Prüfung gezeigt [00:30:49]. Freistellungsprüfung nicht automatisch [00:49:09]. |
| 2.7 | Freistellungsbescheinigung | Could / N | ja | Nur Feld und manuelles Abhaken; Automatik über die Middleware, von Livos abgelehnt [00:48:12–00:49:33]. Deckt sich mit „N"; die Aussage „geht alles über Develop" widerspricht. |
| 2.8 | Aufteilung auf Kostenstellen | Must / S | nein (kaum) | Kostenstelle als Feld [00:29:35]; prozentuale Aufteilung auf Positionen nur erwähnt [00:43:06]. Standardschlüssel je Gesellschaft nicht behandelt. |
| 3.1 | Persönliches Dashboard | Must / S | ja | Dashboard anpassbar [00:01:20], Aufgaben und Mail-Benachrichtigung [00:25:25, 01:00:10], Mail abschaltbar [00:26:35], Fälligkeitsampel [01:03:34]. |
| 3.2 | Management- und Controlling-Dashboard | Must / S | teilw. | Rechnungseingangsbuch mit Filter nach Schritt [00:26:35], Admin-Workflowübersicht [01:00:10]. Liege- bzw. Durchlaufzeit laut MDIS **nicht** in d.velop [00:36:13], also Widerspruch zu „S". |
| 3.3 | Eskalationsmanagement | Must / S | teilw. | Von Tanja angesprochen [00:37:01]; „Eskalationsprozesse" pauschal [00:25:05], Einstellung benannt [01:00:10]. Nicht demonstriert. |
| 3.4 | Vertretungsregelungen | Must / K | ja | Abwesenheit und Vertretung bestätigt [01:05:00]; Admin-Vertretung für Kranke auf das nächste Gespräch vertagt [01:05:41]. |
| 4.1 | Prozessunabhängigkeit Property Manager | Must / N | ja (intensiv) | PM buchen, geben frei und zahlen 95 %; Kreditoren-Mapping; Idee eines Freigabe-Postfachs für AM-Freigaben [00:12:13–00:22:52]. Keine Entscheidung; die Datenübernahme vom PM ist nicht gelöst. |
| 4.2 | Ad-hoc-Freigabe per Mail/Link ohne Lizenz | Should / – | nein | Nicht angesprochen. Die HV-Freigabemail [00:22:19] betrifft nur die Benachrichtigung, nicht die Freigabe durch Externe. |
| 4.3 | Web-Anbindung Kern-Partner | Must / S | nein | Nicht angesprochen. |
| 5.1 | DATEV-Schnittstelle | Must / S | teilw. | Stammdaten- und Kreditorenabgleich intensiv [00:06:37–00:19:49]; Schnittstelle „massiv aufgebohrt", Hosting prüfen [00:13:50–00:14:23]; Übergabe nach Freigabe erwähnt [00:31:42]. Frequenz und Belegübergabe nicht besprochen, nicht gezeigt. |
| 5.2 | Bau-Spezifika (VOB, Einbehalte) | Should / N | ja | Abschläge in der Akte [00:45:13]; kumulierte Prüfung offen („wissen wir grad noch nicht") [00:46:22]; Einbehalte nicht besprochen. |
| 5.3 | Schnittstelle BIM4You | Should / – | nein (nur erwähnt) | Nur als Beispiel für Klärungsbedarf im Einstieg [00:00:22]; ggf. „Projektmanagementsystem" [00:34:45]. |
| 5.4 | Perspektivische ERP-/PM-Anbindung (API) | Could / – | teilw. | Middleware, Lieferanten-App, Evidanza und KI-Plattform als Integrationsschicht [00:09:04, 01:12:20]; REST-API nicht erwähnt. |
| 5.5 | Schnittstelle Zahlungsmanagement (Omikron) | Must / – | teilw. | Zahllauf als Ziel (Tanja) [00:16:32]; Zahlung beim Buchen „über unsere Middleware" [00:33:44]. Omikron nicht genannt; Zahlungsfreigabe nicht gezeigt. |
| 6.1 | DMS-Möglichkeit | Could / S | ja | Akten, Kategorien, Eigenschaften, Wertemengen, Suche, Aufgaben, Prozessstart und Postfächer ausführlich gezeigt [00:49:33–01:08:13]. |

**Bilanz:** 9 Nummern ausdrücklich bzw. ausführlich (1.7, 1.8, 2.1, 2.7, 3.1, 3.4, 4.1, 5.2, 6.1; davon 2.7, 4.1 und 5.2 ohne positives Ergebnis). 13 Nummern teilweise (1.1, 1.2, 1.4, 1.5, 1.6, 2.2, 2.4, 2.6, 3.2, 3.3, 5.1, 5.4, 5.5). 7 Nummern gar nicht (1.3, 2.3, 2.5, 2.8, 4.2, 4.3, 5.3). Von den 21 Must-Haves wurden nur 5 ausdrücklich behandelt (1.8, 2.1, 3.1, 3.4, 4.1), 4 gar nicht (2.3, 2.5, 2.8, 4.3).

**Geplant laut A_06, aber im Termin nicht gezeigt:** Klärfall (Beleg 08, W3), Zuordnung bei gleicher Anschrift (Beleg 04 BAUP), Beweis der Mandantentrennung als Rolle U2 (R2), zweistufige Freigabe über 10.000 € mit Benutzerwechsel (W2), Kostenstellenaufteilung 55/45 (Beleg 03), Managementsicht mit Liegezeit, XRechnung/ZUGFeRD (Belege 09/10), Kreditorenakte Musterbau mit Vertrag und Freistellungsbescheinigung, Änderungsprotokoll nach Übersteuerung. Gezeigt wurden stattdessen andere Beispielkreditoren (Elektro Nordlicht GmbH, Stadtwerke Beispielstadt AG).

---

## 11 Fachbegriffe, Systemnamen und Eigennamen

„Sicherheit" gibt an, wie sicher die Deutung ist: **sicher** / **wahrscheinlich** / **unklar**.

### 11.1 Hersteller, Produkte, Systeme
| Begriff im Transkript | Beispiel-Zeit | Korrigierte Deutung | Sicherheit |
|---|---|---|---|
| „Develop", „Deveno", „Developed", „Developer", „Development", „Developed Direction" | 00:01:20, 00:04:16, 00:16:05, 00:19:36, 00:21:26, 00:39:59 | **d.velop** (Hersteller bzw. Plattform: d.velop documents, d.velop cloud, smart invoice); „Developed Direction" = „d.velop direkt" | sicher |
| „Date", „STATEV", „Datev Phone", „Dativ" | 00:36:13, 00:24:10, 00:06:37, 00:17:28 | **DATEV** | sicher |
| „Libus", „Libos", „Libusauftrag", „Livos Auftrag" | 00:01:20, 00:55:02, 01:06:18 | **Livos**; „Livos Auftrag" ist eine Demo-Kategorie | sicher |
| „Mittelwert", „Mittelwehr", „Mittelware", „Windelware", „Middleware" | 00:08:01, 00:12:13, 00:19:31, 00:36:37, 00:24:42 | **Middleware**: die Integrationsschicht von MDIS bei Livos („euch bekannte Technologieumgebung") | sicher |
| „App", „Lieferanten-App", „Kreditoren-App", „Stammdaten-App", „Konsolidierungs-App" | 00:09:04, 00:11:00, 00:11:45, 00:18:01, 00:40:09 | Bestehende bzw. auszubauende **MDIS-App zur Stammdatenpflege** (Tanja pflegt dort schon heute Stammdaten) | sicher (bestehend) / Annahme (Ausbau) |
| „K.I.-Integrationsplattform", „KI-Plattform", „A.I. Plattform", „KI Framework" | 00:09:51, 00:10:12, 01:09:09, 01:13:26 | **KI-Integrationsplattform von MDIS**, laut Thomas seit ca. 4 Monaten verfügbar | sicher |
| „S One und i on" | 00:10:12 | KI-Add-ons der von Livos genutzten Technologie; nicht auflösbar (Produktnamen?) | **unklar** |
| „Data B aus" | 00:06:37 | **Data Warehouse**, im Rahmen des BI-Projekts | wahrscheinlich |
| „BI Projekt", „BI" | 00:06:37, 00:18:01 | Business-Intelligence-Projekt (vermutlich MDIS bei Livos) | wahrscheinlich |
| „Evidanza", „Vedanza" | 00:36:32, 00:36:37, 01:12:09 | **evidanza** (BI-, Reporting- und Planungssoftware) | sicher |
| „E. V. R." | 01:14:02 | unklar: evtl. „evidanza", „ERP" oder ein Livos-internes System | **unklar** |
| „ricken Cloud", „Rickencloud" | 00:14:00, 00:14:23 | Gehostete Cloud-Umgebung des externen IT-Dienstleisters, über die DATEV erreicht wird. Der Produktname ist nicht auflösbar (evtl. Rechenzentrums- bzw. Private-Cloud) | **unklar** |
| „DIBUS" | 00:14:23 | unklar: evtl. „DATEV-Umfeld" oder „Immobilien-Business" („Im DIBUS ist immer alles komplex") | **unklar** |
| „Rechnungsleser Business", „Rechnungsleser" | 00:01:20, 00:25:25, 01:00:10 | Rechnungslesung bzw. Erkennung, vermutlich d.velop document reader (invoice) bzw. Funktion „Rechnung einlesen" | wahrscheinlich |
| „Rechnungseingangsbuch" | 00:25:25 | d.velop invoices-**Rechnungseingangsbuch** | sicher |
| „Projektmanagementsystem" | 00:34:45 | Nicht benannt; evtl. BIM4You | **unklar** |
| „BIM" | 00:00:22 | **BIM4You** (Bau-Projektsteuerung, Budgetcontrolling) | wahrscheinlich |
| „Outlook" | 00:49:33 | Mailclient, mit dem Sebastian die Test-Mail verschickt | sicher |

### 11.2 Organisationen und Personen
| Begriff im Transkript | Beispiel-Zeit | Korrigierte Deutung | Sicherheit |
|---|---|---|---|
| „Trios" (in der Rede), „Trius" (Sprecherlabel) | 00:14:00, 00:16:17, 00:21:46, 00:21:57; Label ab 00:09:41 | **Trios**: Buchhaltungsgesellschaft bzw. -dienstleister, der für Livos in DATEV bucht. Das Label „Trius" steht vermutlich für einen Teilnehmer oder Raum von Trios bzw. einen Livos-Kollegen, der André duzt | wahrscheinlich / Identität unklar |
| „Herr Groß", „Herr Gross" | 00:05:51, 00:24:10 | Thomas Groß (CEO MDIS) | sicher |
| „Herr Pachon" | 00:23:40, 01:10:22 | Sebastian Pachon (MDIS) | sicher |
| „Anna Lena", „Annalena" | 00:59:49, 01:00:10 | Annalena Groß (MDIS) | sicher |
| „Mardera" | 01:11:52 | vermutlich Valeria (Filimonow) | wahrscheinlich |
| „Herr Walther", „Herr Michael" | 00:17:07, 00:18:01 | vermutlich Herr **Weigel** (Christian Weigel) | wahrscheinlich |
| „Tanja" | 00:15:18, 00:38:42 | Tanja Brecht (Livos) | sicher |
| „Korsmeier" | 01:05:21 | Livos-Mitarbeiter/in, Beispiel für einen Vertreter | sicher (Name) |
| „Hausverwaltung", „Hausverwalter", „Verwalter", „Property Manager" | 00:12:13 ff. | Externe **Property Manager** (ca. 10) | sicher |
| „Asset Management" | 00:20:45 | Livos-interne Freigabeinstanz | sicher |
| „Steuerberater" | 00:33:28 | Externer Steuerberater (Buchung); Verhältnis zu Trios offen | sicher (Begriff) |
| „Schadensanierer" | 00:14:23 | Referenzkunde von MDIS (Schadensanierung, 130 Servicemitarbeiter) | sicher |
| „Elektro Nordlicht GmbH" | 00:55:02 | Testkreditor der Demo (Kred.-Nr. 70044 laut A_07) | sicher |
| „Stadtwerke, Beispiel Stadt AG" | 01:06:18 | Testkreditor **Stadtwerke Beispielstadt AG** (70103 laut A_07) | sicher |
| „Objekt Norden/Süden", „Livos Objektgesellschaft Süd" | 00:29:35, 00:31:16, 01:06:18 | Test-Gesellschaften NORD/SÜD der Demo (A_06) | sicher |

### 11.3 d.velop- und Fachbegriffe
| Begriff im Transkript | Beispiel-Zeit | Korrigierte Deutung | Sicherheit |
|---|---|---|---|
| „Kreatorenakte", „Kreatur Akte", „Kretorenakte" | 00:01:20, 00:55:02, 00:57:41 | **Kreditorenakte** | sicher |
| „Objektenakte" | 00:55:02 | **Objektakte** | sicher |
| „Akte", „Unterakten", „Aktenplan", „Folder Structure" | 00:57:16, 01:06:18, 00:44:32, 00:57:22 | Akten bzw. Aktenstruktur in d.velop documents | sicher |
| „Foulder-Content", „Folder Content" | 00:55:02 | Perspektive **Akteninhalt** | wahrscheinlich |
| „Kategorie", „Dokumentenart" | 00:53:32, 00:57:41 | **Kategorie** ist der Cloud-Begriff für die Dokumentart (LIESMICH) | sicher |
| „Eigenschaften", „Wertemengen" | 00:57:41 | Metadatenfelder bzw. Auswahllisten in d.velop | sicher |
| „Stapel" | 00:04:44, 00:49:33 | **Stapel** (Batch) im Posteingang bzw. bei der Validierung | sicher |
| „Importprofil", „Standardprofil", „zugelassene E-Mail-Adressen" | 00:49:33, 00:53:24 | Konfiguration von d.velop inbound e-mail bzw. email import | sicher |
| „Invoices" | 00:49:33 | Name eines Import-Postfachs in der Demo | sicher |
| „Verteilung", „sachliche Prüfung", „Freigabe", „Buchhaltung" | 00:25:25–00:34:45 | Workflow-Schritte der Demo (Rechnungseingangsworkflow) | sicher |
| „Dublettenprüfung", „Doublette", „Duplikat" | 00:04:44, 00:38:29, 00:41:01 | **Duplikatsprüfung** in smart invoice bzw. Dublettenprüfung im document reader | sicher |
| „Human und der Loop" | 00:25:05 | **Human-in-the-loop** | sicher |
| „Onboarding", „aufgetretene Probleme", „Ausgleichspositionen", „Zuschläge" | 01:00:10 | Bereiche der smart-invoice-Administration bzw. Workfloweinstellungen | wahrscheinlich |
| „Ampelsystem", „Netto-Fälligkeit" | 01:03:34 | Fälligkeitsampel in der Aufgabenliste bzw. im Rechnungseingangsbuch | sicher |
| „Abwesenheitsstatus", „Vertretung" | 01:05:00 | Abwesenheit und Vertretung in d.velop (Benutzerprofil) | sicher |
| „Vier-Augen-Prinzip" | 00:31:42 | Zweistufige Freigabe | sicher |
| „Kreditor", „Lieferant", „Lieferantennummer", „Kreditorennummer", „Konsolidierungsnummer", „Referenznummer", „Nummernkreis", „Rechnungskreis" | 00:06:37–00:19:49 | Stammdatenbegriffe; Konsolidierungsnummer = mandantenübergreifende Lieferantennummer der App | sicher |
| „Creditoron Consolidierung", „Creditor" | 00:06:37 | **Kreditorenkonsolidierung**, Kreditor | sicher |
| „Kommandanten Nummer" | 00:11:39 | **Mandantennummer** | sicher |
| „Siebzigtausender/Achtzigtausender Bereich/Kreis" | 00:17:34 | Kreditorennummernkreise 70000 (intern) und 80000 (HV-Einzelkreditoren) | sicher |
| „Monatspaket" | 00:21:57 | Monatliche Belegübergabe an Trios | sicher |
| „Zahllauf" | 00:16:32 | Zahlungslauf (Ort DATEV bzw. Zahlungssystem offen) | sicher |
| „Ausbuchungen auf Mietkonten", „Spielfreigaben" | 00:37:33 | Freigabe von Ausbuchungen auf Mieterkonten; „Spielfreigaben" vermutlich Hörfehler (z. B. „beispielsweise Freigaben") | wahrscheinlich |
| „Abschlagsrechnung", „kumulierte Rechnung" | 00:44:49, 00:45:13 | Abschlagsrechnung bzw. kumulierte Abschlagsrechnung (VOB) | sicher |
| „Baufreistellungsbescheinigung", „Freistellungsbescheinigung" | 00:48:12 | Freistellungsbescheinigung nach § 48b EStG (Bauabzugsteuer) | sicher |
| „E-Rechnungen, die XML-Dateien" | 00:46:54 | XRechnung bzw. ZUGFeRD | sicher |
| „Proof of Concept" | 00:11:13, 00:20:21 | PoC (kostenlos angeboten) | sicher |
| „Lastschrift" | 01:12:04–01:12:08 | Nebenbemerkung Sebastians ohne erkennbaren Bezug („Lastschrift sehr selten eigentlich") | unklar |
| „Bilanzauswertungen" | 01:13:26 | Bilanz- bzw. BI-Auswertungen in den Livos-Apps (evtl. Hörfehler für „BI-Auswertungen") | unklar |

### 11.4 Weitere vermutliche Hörfehler
| Transkript | Zeit | Vermutlich gemeint |
|---|---|---|
| „Auto thematisiert" | 00:37:12 | automatisiert |
| „Ausdeckungssache" | 00:48:28 | Auslegungssache |
| „Beim Franken" | 00:49:08 | beim Lieferanten (Wiederholung von Tanjas Einwurf) |
| „Kommunikation … zum Editor" | 00:39:39 | zum Kreditor |
| „Bitte noch mal skalieren" | 00:39:39 | „eskalieren" bzw. „korrigieren" |
| „Kürzungen von Rechnungen in WIF" | 00:41:34 | vermutlich „in d.velop" |
| „die gesamte Herd einmal installiert" | 00:41:47 | „die gesamte Umgebung", ggf. „Hardware" |
| „Harman" | 00:42:12, 01:06:18 | „hat man" |
| „hochladen und kabeln" | 00:33:25 | hochladen und verknüpfen bzw. koppeln |
| „auf den aktuellen Sprint" | 00:26:35 | vermutlich „aktuellen Stand" bzw. „Tag" |
| „zu Dokumenten, zu Schrift" | 01:00:10 | vermutlich „Schriftverkehr" |
| „Demonstanz" | 01:00:10 | Demo-Instanz |
| „Rechnungseingangspunkt Prozess" | 00:34:11 | Rechnungseingangsprozess |
| „Haben wir das Konto vereinbart?" | 01:08:46 | „Haben wir Skonto vereinbart?" |
| „Reuters Wust", „I'm going", „Picking", „Football", „Cut", „Site", „Bye", „Pick" | diverse | Störgeräusche bzw. Fehltranskription, ohne Inhalt |
| „200 Pixel zusammen, sogar" | 00:13:35 | unklar (evtl. „200 Nummern" bzw. Kreditoren zusammen) |
| „Trieb ab sofort offen." | 01:12:00 | unklar, Nebengeräusch beim Öffnen des Katalogs |
