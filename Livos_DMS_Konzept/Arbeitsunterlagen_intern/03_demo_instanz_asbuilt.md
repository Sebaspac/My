# 03 — Demo-Instanz „as-built": mdisconsulting.d-velop.cloud

Stand der Auswertung: 26.09.2026 · Bezug: Livos-Demo-Workshop (Agenda-Stand 22.09.2026)
Zweck: Festhalten, wie die Livos-Struktur in der d.velop-Cloud-Instanz aufgebaut wurde bzw. aufgebaut werden sollte. Dazu gehören die echten Begriffe der Cloud-Oberfläche, die Plattformgrenzen und die Abweichungen zum Architektur-Soll. Das Ergebnis ist die Grundlage für die Übertragung ins Produktivkonzept.

---

## 0 Quellenlage, Kennzeichnung, Vorbehalte

### 0.1 Kürzel der Quellen

| Kürzel | Datei | Inhalt |
|---|---|---|
| **KW-nn** | `SP/img/klickweg/nn_*.png` (36 Bilder) | Klickweg-Folien „Aufgabe 2 · Struktur anlegen": Titelbild und die Schritte 1/35 bis 35/35 |
| **KW-PDF** | `SP/txt/A_01_Klickweg_36_Schritte_pdf.txt` | Textauszug des PDF: 36 leere Seiten, **kein extrahierbarer Text**. Der Inhalt steht ausschließlich in den Bildern |
| **CP** | `SP/txt/04_Chrome-Prompt_Aufgabe-2.md` | Arbeitsauftrag für das Claude-Chrome-Plugin: 8 Wertemengen, 26 Eigenschaften, 9 Kategorien |
| **LM** | `SP/txt/00_LIESMICH_Zuerst-lesen.md` | Workshop-Readme vom 21.09.2026 mit Korrekturen und Grenzen |
| **KA** | `SP/txt/A_05_Konfigurationsanleitung.txt` | Konfigurationsanleitung, Phasen 0–7, Stand 19.09.2026 |
| **AR** | `SP/txt/A_06_Architektur_Demo-Instanz.txt` | Architektur der Demo-Instanz (Soll), Stand 18.09.2026 |
| **TD** | `SP/txt/A_07_Testdaten_alle.txt`, `A_07_Testdaten_LIESMICH.md` | Testbelege und Stammdaten-CSV |
| **TR** | `SP/txt/C_Transkript_Livos_Demo.txt` | Transkript des Demo-Termins, zitiert mit [hh:mm:ss] und Sprecher |
| **B00 / B03 / B06** | `SP/txt/B_00_…`, `B_03_…`, `B_06_…` | Doku-Recherche: konsolidiert, Administration/Berechtigungen, Postverteilung/Mailimport |

### 0.2 Kennzeichnung

- **Fakt (belegt):** steht wörtlich in einer der Quellen.
- **As-built belegt:** im Demo-Termin sichtbar vorgeführt oder vom Präsentator als angelegt benannt (TR).
- **Soll:** Vorgabe aus CP/KW/KA/AR. Dass es umgesetzt wurde, ist damit **nicht** belegt.
- **Annahme:** eigene Ableitung, ausdrücklich als solche markiert.
- **Offen:** in keiner Quelle belegt.

### 0.3 Drei wichtige Vorbehalte

1. **Die 36 „Screenshots" sind keine Bildschirmfotos der Cloud-Oberfläche.** Es sind gerenderte Anleitungsfolien. Jede Folie hat eine Kopfzeile „AUFGABE 2 · STRUKTUR ANLEGEN", die Angabe „Schritt n / 35", einen Menüpfad-Kasten, Feld/Wert-Zeilen und farbige Hinweiskästen: gelb für Warnung, grün für Tipp. Ein Fortschrittsbalken zeigt den Teil (0–6). Die UI-Begriffe auf den Folien gelten laut LM als **gegen die echte UI korrigiert**: „Datei 01 und 04 sind korrigiert" [Quelle: LM, Abschnitt „Drei Dinge…"]. Wörtlich verifiziert sind sie damit aber nicht. [Quelle: KW-00 bis KW-35; KW-PDF]
2. **Der Abschlussbericht von Aufgabe 2 fehlt.** Er sollte sieben Punkte enthalten: Inventur, Löschliste, Umbenennungen mit Fehlermeldung, Abbrüche, UI-Abweichungen im Wortlaut, Unerwartetes und eine Bestätigung [Quelle: CP §5; KW-34]. Deshalb ist **nicht belegt**, welche Eigenschaften tatsächlich den Zusatz „(Livos)" bekamen, welche Datentypen die Inventur ergab und ob Schritte abgebrochen wurden.
3. **As-built-Belege gibt es nur aus dem Transkript.** Im Termin wurden Teile der Struktur live gezeigt, zum Beispiel „Livos Auftrag", „Livos Kreditorenakte", die Objektakte und die Wertemenge „Livos Objekt" mit 3 Objekten. Andere Teile wurden nicht gezeigt, zum Beispiel Vertrag, Nachweis, Korrespondenz, Gesellschaftsakte, Benutzerwechsel und Freigabegrenze. Siehe die Statusspalten unten.

### 0.4 Einordnung: Aufgabenschnitt der Vorbereitung

| Aufgabe | Inhalt | Beleg |
|---|---|---|
| Aufgabe 1 | Vorangegangene Erkundung. Daraus stammen die „bekannten Stolpersteine" (Zwei-Schritt-Anmeldung, Zurück-Pfeil in smart invoice, Browser-Zurück) | [Quelle: CP §0 „Bekannte Stolpersteine aus Aufgabe 1"] |
| **Aufgabe 2** | **Struktur anlegen:** 8 Wertemengen, 26 Eigenschaften, 9 Kategorien, rein additiv | [Quelle: CP; KW-00] |
| Aufgabe 3 | Benutzer, Gruppen, Berechtigungen („die kritische") | [Quelle: CP §0 Regel 3; KW-03; KW-35] |
| Aufgabe 4 | Dokumente hochladen und importieren (Testdaten) | [Quelle: CP §0 Regel 4; KW-03; KW-35] |
| Danach | Die 7 Phasen der KA, „die **du** konfigurierst, nachdem die Struktur steht" | [Quelle: LM, Dateitabelle Nr. 05] |

Empfehlung aus LM für den Vorabend (Fakt): Zuerst nur den bestehenden Tenant durchüben. Wenn Zeit bleibt, aus Aufgabe 2 nur die 8 Wertemengen und `Livos Eingangsrechnung` anlegen. Die übrigen fünf Dokumentarten sind „Kür". Am Morgen des Termins werden keine Benutzer angelegt, keine Testdaten importiert und nichts in smart invoice geändert [Quelle: LM, „Heute Abend…", „Falls danach noch Luft ist…", „Morgen früh nicht mehr anfangen"].
**As-built belegt:** Im Termin gab es mehr als die Minimalvariante, nämlich die Kategorien Livos Auftrag, Livos Kreditorenakte und Objektakte [TR 00:01:20, 00:55:02, 01:06:18 Sebastian Pachon].

### 0.5 Bildinventar: was auf jeder der 36 Folien konkret zu sehen ist

| Datei | Schritt · Teil | Titel | Konkreter Inhalt (Menüpfad · Felder · Werte · Hinweise) |
|---|---|---|---|
| 00_Titelbild | Titel | Aufgabe 2 | „Struktur anlegen in mdisconsulting.d-velop.cloud · 8 Wertemengen · 26 Eigenschaften · 9 Kategorien · Rein additiv — kein bestehendes Objekt wird angefasst." Fußzeile: „Livos Kundenworkshop · Klickweg-Dokumentation · jeder Schritt einzeln nachvollziehbar" |
| 01_Anmelden | 1/35 · Teil 0 Einstieg | Anmelden | URL-Kasten `mdisconsulting.d-velop.cloud`. „Achtung: Ein Dialog „Anmeldung in zwei Schritten" kann blockierend erscheinen — wegklicken." Gelb: „Browser-Zurück führt NICHT auf die letzte Konfigurationsseite. Immer über das Menü navigieren." |
| 02_Navigation-Strukturverwaltung | 2/35 · Teil 0 | Zur Strukturverwaltung navigieren | Pfad `Konfiguration > Dokumentenmanagement > Verwaltung > Dokumenten- und Aktenstrukturen`. „Dort liegen: Wertemengen · Eigenschaften · Kategorien". „Angelegt wird über: +". Grün: „Das + heisst je nach Register „Wertemenge / Eigenschaft / Kategorie erstellen"." |
| 03_Die-vier-Verbote | 3/35 · Teil 1 Grundregeln | Die vier Verbote | (1) Kein bestehendes Objekt umbenennen, bearbeiten, löschen oder umhängen. (2) smart invoice / Rechnungsverarbeitung nur lesen. Nie speichern. (3) Keine Benutzer, Gruppen, Berechtigungen. Das ist Aufgabe 3. (4) Keine Dokumente hochladen oder importieren. Das ist Aufgabe 4. Gelb: „Der Tenant wird produktiv genutzt: 102 Belege im Umlauf, aktiver Workflow, vier si_-Gruppen. Jede Änderung trifft arbeitende Kollegen." |
| 04_Namensregel-und-Loeschliste | 4/35 · Teil 1 | Namensregel und Löschliste | „Kategorien, Wertemengen: Praefix Livos IMMER". „Eigenschaften: Erst den schlichten Namen versuchen. Lehnt die UI ihn als Dublette ab: (Livos) anhängen." „Löschliste: Jeden angelegten Namen in Anlagereihenfolge mitschreiben." Grün: „Die Löschliste ist die Versicherung: damit ist am Ende jedes Objekt von uns rückstandsfrei entfernbar." |
| 05_Inventur-vor-dem-Anlegen | 5/35 · Teil 1 | Inventur vor dem ersten Anlegen | Kasten: „Register Eigenschaften öffnen — nur lesen". Zu prüfen: Kreditor, Rechnungsnummer (BEIDE Vorkommen), IBAN, Belegart, Rechnungsdatum, Nettobetrag, Bruttobetrag. „Notieren: Datentyp und Anzahl der Werte je Eigenschaft". Gelb: „Nur Inventur. Nichts anklicken, was speichert. Das Ergebnis gehört in den Bericht." |
| 06_Muster-Wertemenge | 6/35 · Teil 2 Wertemengen | Muster: eine Wertemenge anlegen | Pfad `+ > Wertemenge erstellen`. Felder: „Name (Deutsch): der Name aus der jeweiligen Tafel, max. 50 Zeichen" · „Werte: zeilenweise eintragen, Reihenfolge wie gezeigt" · „Dann: Speichern". Grün: „Die nächsten acht Schritte sind genau dieses Muster, achtmal. Nur Name und Werte wechseln." |
| 07_WM_Livos-Gesellschaft | 7/35 · Teil 2 | Livos Gesellschaft | `+ > Wertemenge erstellen`. Name `Livos Gesellschaft`. Werte: Livos Objektgesellschaft Nord mbH · Livos Objektgesellschaft Süd mbH · Livos Bau & Projekt GmbH. Gelb: „Livos Projektentwicklung West GmbH fehlt ABSICHTLICH. Eine Testrechnung läuft darauf und muss in den Klärfall fallen. Nicht vervollständigen." |
| 08_WM_Livos-Kreditor | 8/35 · Teil 2 | Livos Kreditor | Name `Livos Kreditor`. Werte: Musterbau GmbH · Elektro Nordlicht GmbH · Stadtwerke Beispielstadt AG · Recht & Partner mbB · Reinigungsservice Blitzblank GmbH |
| 09_WM_Livos-Objekt | 9/35 · Teil 2 | Livos Objekt | Name `Livos Objekt`. Werte: BV Hafenstraße 22 · BV Leopoldstraße 108 · BV Königsallee 60 |
| 10_WM_Livos-Gewerk | 10/35 · Teil 2 | Livos Gewerk | Name `Livos Gewerk`. Werte: Rohbau · Elektro · Ausbau · Reinigung · Beratung · Versorgung |
| 11_WM_Livos-Belegart | 11/35 · Teil 2 | Livos Belegart | Name `Livos Belegart`. Werte: Normal · Abschlagsrechnung · Schlussrechnung · Gutschrift |
| 12_WM_Livos-Sachkonto | 12/35 · Teil 2 | Livos Sachkonto | Name `Livos Sachkonto`. Werte: 0700 Bauten auf eigenen Grundstücken · 4240 Strom, Gas, Wasser · 4250 Reinigung · 4260 Instandhaltung · 4950 Rechts- und Beratungskosten |
| 13_WM_Livos-Kostenstelle | 13/35 · Teil 2 | Livos Kostenstelle | Name `Livos Kostenstelle`. Werte: KST-1000 Verwaltung · KST-2000 Objektbetrieb Nord · KST-2100 Objektbetrieb Süd · KST-3000 Projektentwicklung |
| 14_WM_Livos-Ja-Nein | 14/35 · Teil 2 | Livos Ja Nein | Name `Livos Ja Nein`. Werte: Ja · Nein. Grün: „Ersetzt den fehlenden Ja/Nein-Datentyp. d.velop kennt nur Text, Zahl, Währung, Datum und Datum-und-Zeit — einen Booleschen Typ gibt es nicht." |
| 15_Muster-Eigenschaft | 15/35 · Teil 3 Eigenschaften | Muster: eine Eigenschaft anlegen | Pfad `+ > Eigenschaft erstellen`. Felder: „Name (Deutsch): Feldname" · „Datentyp: Text / Zahl / Währung / Datum" · „Vordefinierte Werte: Wertemenge — nur wo eine angegeben ist" · „Anzahl der Werte: Einzelwert, außer wo „Mehrere Werte" steht". Gelb: „Position, Beschreibung und Kürzel gibt es in der Cloud-UI NICHT. Diese drei Felder entfallen ersatzlos." |
| 16_Gruppe-A_Auswahllisten | 16/35 · Teil 3 | Gruppe A — Auswahllisten | Kasten „Datentyp Text + Vordefinierte Werte". Eigenschaft → Wertemenge: Gesellschaft → Livos Gesellschaft · Kreditor → Livos Kreditor · Objekt → Livos Objekt · Gewerk → Livos Gewerk · Belegart → Livos Belegart · Sachkonto → Livos Sachkonto. Gelb: „Kreditor und Belegart existieren bereits. Erwarte die Dublettenmeldung und lege sie als „Kreditor (Livos)" bzw. „Belegart (Livos)" an." |
| 17_Gruppe-B_Kostenstelle | 17/35 · Teil 3 | Gruppe B — Kostenstelle | Kasten „Datentyp Text + Vordefinierte Werte". Name `Kostenstelle` · Wertemenge `Livos Kostenstelle` · Anzahl der Werte `Mehrere Werte ← der einzige Mehrfachwert`. Grün: „Korrektur gegenueber dem Architekturdokument: „Kostenstelle mit Anteil" gibt es an Dokumenten nicht. Der Anteil lebt in den Belegpositionen von smart invoice." |
| 18_Gruppe-C_Ja-Nein-Felder | 18/35 · Teil 3 | Gruppe C — die Ja/Nein-Felder | Kasten „Datentyp Text + Wertemenge Livos Ja Nein". Reverse Charge 13b: „Bauleistung, betrifft Beleg 06 und 07". Freistellungsbescheinigung geprüft: „manueller Schritt statt Automatik, Katalog 2.7". Auf der Folie überlappen Label und Text (Layoutfehler). Grün: „Beide sind Textfelder mit zwei erlaubten Werten — kein Haken, keine Checkbox." |
| 19_Gruppe-D_Textfelder | 19/35 · Teil 3 | Gruppe D — freie Textfelder | Kasten „Datentyp Text, keine Wertemenge". Rechnungsnummer · Leistungszeitraum · Skonto · IBAN · Vertragsnummer · Auftragsnummer · Betreff · Absender. Gelb: „Rechnungsnummer und IBAN existieren bereits — Dublettenmeldung erwarten, dann mit ` (Livos)` anlegen." (mit übrig gebliebenen Backticks) |
| 20_Gruppe-E_Datumsfelder | 20/35 · Teil 3 | Gruppe E — Datumsfelder | Kasten „Datentyp Datum". Rechnungsdatum: „Pflichtangabe nach § 14 UStG" · Fälligkeitsdatum: „Basis fuer Eskalation" · Gültig bis: „Freistellungsbescheinigung" · Dokumentdatum: „generisch fuer die fuenf Nicht-Rechnungsarten". **Kein** Dublettenhinweis zu Rechnungsdatum, obwohl es in der Inventur (KW-05) als bestehend geführt wird |
| 21_Gruppe-F_Betraege | 21/35 · Teil 3 | Gruppe F — Betraege | Kasten „Datentyp Währung bzw. Zahl". Währung: Nettobetrag · Steuerbetrag · Bruttobetrag · Sicherheitseinbehalt. Zahl: Steuersatz. Gelb: „Nettobetrag und Bruttobetrag existieren bereits — ` (Livos)` anhängen." |
| 22_Kein-Status-Feld | 22/35 · Teil 3 | Kein Status-Feld anlegen | „Grund: Den Status steuert der Workflow. Die Eigenschaft Workflowstatus existiert bereits im Tenant." Grün: „Damit sind 26 Eigenschaften angelegt. Grenze pro Kategorie sind 89 — wir bleiben weit darunter." |
| 23_Muster-Kategorie | 23/35 · Teil 4 Kategorien | Muster: eine Kategorie anlegen | Pfad `+ > Kategorie erstellen`. „Zuerst: Auswahl Dokumentart oder Aktenart — beachten!" · „Name (Deutsch): mit Praefix Livos" · „Dann: Eigenschaften zuweisen unter Zugewiesene Eigenschaften". Grün: „Zuweisen ändert die Eigenschaft NICHT. Die Zuordnung lebt an der Kategorie — deshalb ist auch dieser Schritt rein additiv." |
| 24_KAT_Livos-Eingangsrechnung | 24/35 · Teil 4 | Livos Eingangsrechnung | Pfad `+ > Kategorie erstellen > Dokumentart`. Zugewiesene Eigenschaften 1–20 (siehe Kap. 4). „Titel (T-Button): Kreditor, Rechnungsnummer, Bruttobetrag" |
| 25_KAT_Livos-Vertrag | 25/35 · Teil 4 | Livos Vertrag | `> Dokumentart`. Gesellschaft, Kreditor, Vertragsnummer, Dokumentdatum, Gültig bis, Objekt. Titel: Kreditor, Vertragsnummer |
| 26_KAT_Livos-Auftrag | 26/35 · Teil 4 | Livos Auftrag | `> Dokumentart`. Gesellschaft, Kreditor, Auftragsnummer, Dokumentdatum, Objekt, Gewerk, Nettobetrag. Titel: Kreditor, Auftragsnummer |
| 27_KAT_Livos-Nachweis | 27/35 · Teil 4 | Livos Nachweis | `> Dokumentart`. Gesellschaft, Kreditor, Dokumentdatum, Objekt, Gewerk, Auftragsnummer. Titel: Kreditor, Dokumentdatum |
| 28_KAT_Livos-Korrespondenz | 28/35 · Teil 4 | Livos Korrespondenz | `> Dokumentart`. Gesellschaft, Kreditor, Dokumentdatum, Betreff, Absender, Objekt. Titel: Betreff, Dokumentdatum |
| 29_KAT_Livos-Bescheinigung | 29/35 · Teil 4 | Livos Bescheinigung | `> Dokumentart`. Kreditor, Dokumentdatum, Gültig bis. Titel: Kreditor, Gültig bis |
| 30_KAT_Die-drei-Aktenarten | 30/35 · Teil 4 | Die drei Aktenarten | Pfad `+ > Kategorie erstellen > Aktenart`. Livos Gesellschaftsakte: Gesellschaft · Livos Kreditorenakte: Kreditor, Gesellschaft · Livos Objektakte: Objekt, Gesellschaft. Grün: „Akten sind Sichten, keine Ablageorte. Dasselbe Dokument erscheint in mehreren Akten, ohne mehrfach zu existieren — das ist der Aha-Moment des Workshops." |
| 31_Reihenfolge-der-Maske | 31/35 · Teil 5 Feinschliff | Reihenfolge der Maske | Pfad `Zugewiesene Eigenschaften > Ziehgriff`. „Wie: Per Drag-and-drop in die Reihenfolge der Nummerierung bringen." „Warum: Position als Feld gibt es nicht — die Reihenfolge IST die Position." |
| 32_Pflichtfelder | 32/35 · Teil 5 | Pflichtfelder setzen | Pfad `▫ > Pflichtfeld`. Das Kästchen ist ein nicht darstellbares Glyph. Laut CP §4 ist es das Kebab-Menü `⋮`. Livos Eingangsrechnung: Gesellschaft, Kreditor, Rechnungsnummer, Rechnungsdatum, Nettobetrag, Bruttobetrag, Fälligkeitsdatum, Objekt, Kostenstelle, Belegart. „Alle übrigen Kategorien: nur das jeweils erste Feld der Liste". Gelb: „Alle anderen Felder bleiben optional. Eine Maske aus lauter Pflichtfeldern blockiert die Demo, sobald ein Wert fehlt." |
| 33_Titel-setzen | 33/35 · Teil 5 | Titel setzen | Pfad `T > Titel bearbeiten`. Eingangsrechnung: Kreditor, Rechnungsnummer, Bruttobetrag · Vertrag / Auftrag: Kreditor + jeweilige Nummer · Nachweis: Kreditor, Dokumentdatum · Korrespondenz: Betreff, Dokumentdatum · Bescheinigung: Kreditor, Gültig bis · Aktenarten: jeweils das erste zugewiesene Feld |
| 34_Bericht_sieben-Punkte | 34/35 · Teil 6 Abschluss | Der Bericht — sieben Punkte | 1 Inventur · 2 Angelegt (Löschliste in Anlagereihenfolge) · 3 Umbenannt (mit Fehlermeldung im Wortlaut) · 4 Nicht geschafft (Screenshot und Stelle) · 5 UI-Abweichungen (WÖRTLICH, nicht sinngemäß) · 6 Unerwartetes · 7 Bestätigung. Grün: „Punkt 5 ist der wichtigste: damit werden die Platzhalter in der Konfigurationsanleitung durch die echten Beschriftungen ersetzt." |
| 35_Hier-ist-Schluss | 35/35 · Teil 6 | Hier ist Schluss | „Nicht mehr tun: Kein Testdatenimport — das ist Aufgabe 4. Keine Benutzer, keine Gruppen — das ist Aufgabe 3. Nichts in smart invoice." Gelb: „Aufgabe 3 ist die kritische: ohne die Benutzer U1 und U3 gibt es keinen Benutzerwechsel und damit keine Freigabedemo." |

Zählung: Das Dokument heißt „36 Schritte". Es sind 36 Seiten: 1 Titelbild und 35 nummerierte Schritte [Quelle: KW-00 bis KW-35].

---

## 1 Navigations- und Menüpfade in der Cloud-Administration

### 1.1 Strukturverwaltung (Dokumentenmodell) — der Cloud-Klickweg

| Zweck | Pfad / UI-Element (Wortlaut der Folien) | Quelle | Status |
|---|---|---|---|
| Anmeldung | `mdisconsulting.d-velop.cloud`. Ein Dialog „Anmeldung in zwei Schritten" kann blockieren → wegklicken | KW-01; CP §0 | Fakt (Stolperstein aus Aufgabe 1) |
| Navigation allgemein | **Immer über das Menü**, nie über Browser-Zurück. Der Zurück-Pfeil in smart invoice springt direkt zur Konfigurationsübersicht | KW-01; CP §0 | Fakt |
| Einstieg Strukturverwaltung | **Konfiguration > Dokumentenmanagement > Verwaltung > Dokumenten- und Aktenstrukturen** | KW-02; CP §1 | Fakt (korrigierter Pfad lt. LM) |
| Register | **Wertemengen** · **Eigenschaften** · **Kategorien** | KW-02; CP §1 | Fakt |
| Anlegen | **`+`**, je Register „Wertemenge erstellen" / „Eigenschaft erstellen" / „Kategorie erstellen" | KW-02, KW-06, KW-15, KW-23 | Fakt |
| Wertemenge anlegen | `+ > Wertemenge erstellen` → **Name (Deutsch)** (max. 50 Zeichen) → **Werte** (zeilenweise, Reihenfolge wie gewünscht) → **Speichern** | KW-06 | Fakt |
| Eigenschaft anlegen | `+ > Eigenschaft erstellen` → **Name (Deutsch)** → **Datentyp** (Text / Zahl / Währung / Datum; zusätzlich gibt es Datum-und-Zeit lt. KW-14) → **Vordefinierte Werte** (→ Wertemenge wählen) → **Anzahl der Werte** (Einzelwert / **Mehrere Werte**) | KW-15; CP §3 | Fakt |
| Kategorie anlegen | `+ > Kategorie erstellen` → **zuerst Auswahl „Dokumentart" oder „Aktenart"** → **Name (Deutsch)** → Eigenschaften zuweisen unter **Zugewiesene Eigenschaften** | KW-23; KW-24 bis KW-30; CP §4 | Fakt |
| Maskenreihenfolge | **Zugewiesene Eigenschaften > Ziehgriff** (Drag-and-drop). Die Reihenfolge ist die Position | KW-31 | Fakt |
| Pflichtfeld | **`⋮` > Pflichtfeld** an der zugewiesenen Eigenschaft innerhalb der Kategorie. Auf KW-32 ist das Symbol als „▫" dargestellt | KW-32; CP §4 „Pflichtfelder" | Fakt |
| Titel (Titelregel) | **`T`-Button > „Titel bearbeiten"** in der Kategorie; Eigenschaften für den Titel wählen | KW-33; CP §4 „Titel" | Fakt |
| Inventur bestehender Eigenschaften | Register **Eigenschaften** öffnen, **nur lesen**: Datentyp und **Anzahl der Werte** notieren | KW-05; CP §1 | Fakt (Ergebnis: offen) |

### 1.2 Weitere Konfigurationsbereiche (aus KA, TR, Recherche)

| Zweck | Pfad / Beschreibung | Quelle | Status |
|---|---|---|---|
| smart invoice / Rechnungsverarbeitung | **Konfiguration > Rechnungsverarbeitung** (Workflow, Freigabematrix, `si_`-Gruppen, Belegmaske, Onboarding-Schritt) — in Aufgabe 2 **nur lesen** | CP §0 Regel 2; KW-03 | Fakt (Pfad) |
| smart invoice-Administrationsübersicht | Über „Administration": Dashboard mit Belegen im Umlauf und insgesamt verarbeiteten Belegen, „Onboarding", „aufgetretene Probleme", laufende Workflows je Schritt (z. B. „Verteilung") | TR [01:00:10] Sebastian Pachon (fortlaufender Beitrag) | As-built belegt (Pfad nicht wörtlich) |
| Konfigurationsübersicht | Linke Leiste mit Funktionspunkten, Favoriten per Sternchen anheftbar | TR [00:49:33] Sebastian Pachon | As-built belegt |
| E-Mail-Import: Verbindung | **Konfiguration > Dokumentenmanagement > E-Mail-Anbindung > Postfach-Verbindungseinstellungen** (Protokoll Microsoft Graph, vier Werte, „Verbindung testen", „Verarbeitung aktiviert") | KA §7.3; B06 Z. 245 | Doku-belegt, am System nicht verifiziert |
| E-Mail-Import: Postfächer | **Konfiguration > Dokumentenmanagement > E-Mail-Anbindung > Verwalten von Postfächern** → Hinzufügen, Anzeigename, Alias-Adresse, Importprofil, Stapelname, „Stapel nach Import abschließen", Schlüssel-Wert-Paare, Berechtigungen, Fehlerbenachrichtigung, Speichern | KA §7.4; B06 Z. 261–304 | Doku-belegt |
| E-Mail-Postfach (im Termin gezeigt) | 3 Postfächer angelegt, u. a. **„Invoices"**. Felder: **Beschreibung**, **Importprofil**, **zugelassene E-Mail-Adressen** (Einzeladresse, Domain oder „alle" per Platzhalter; nicht empfohlen) | TR [00:49:33] Sebastian Pachon; B06 Z. 304 („Zugelassene E-Mail-Adressen", Wildcards) | As-built belegt |
| Import / Stapel | Import und Stapelbearbeitung: Dokumente per Haken übernehmen oder ablehnen, dann indexieren. Bei manueller Ablage wird eine **Kategorie** gewählt, danach die Eigenschaften | TR [00:53:32] Sebastian Pachon | As-built belegt |
| Rechnungserfassung | „Rechnung einlesen" (vom Präsentator „Rechnungsleser Business" genannt): Einzel- oder Mehrfach-Upload, OCR, Stapel, „alle weiteren Dokumente im Stapel direkt speichern" | TR [00:01:20], [00:04:44] Sebastian Pachon | As-built belegt |
| Rechnungseingangsbuch | Doku: **Startseite d.velop documents > Widget hinzufügen > Widget „Rechnungseingangsbuch" > Hinzufügen**. Im Termin: Tabelle mit **226 Rechnungen**, Filter nach **aktuellem Schritt**, Gruppierung | KA §10.1; B00 AO; TR [00:25:25], [00:26:35] Sebastian Pachon | Doku-Pfad / As-built belegt (Nutzung) |
| Startseite / Dashboard | **Konfiguration > Erscheinungsbild > Startseite > Widgets erstellen** bzw. **> Sichtbarkeit von Widgets** (danach „Zuordnungen anwenden") | KA §10.2–10.3; B00 X–Z | Doku-belegt, am System nicht verifiziert |
| Dashboard (Anwendersicht) | Widgets entfernen, ergänzen, Kästchen größer/kleiner — pro Rolle anpassbar | TR [00:01:20] Sebastian Pachon | As-built belegt (verbal gezeigt) |
| Benutzer / Berechtigungen | In der „Admin-Maske": Benutzer anlegen, Berechtigungen für Gruppen zuteilen. **Konkreter Cloud-Pfad nicht benannt** | TR [01:04:23] Sebastian Pachon; KA §3.3, §9.2 („ungeprüft") | Offen (Pfad) |
| Aufgabe erstellen (ad hoc) | Am Dokument: Aufgabe an Person (Beispiel „Annalena") mit Priorität, Zustellung, Fälligkeit, Erinnerung, Selbstbenachrichtigung → „Aufgabe erstellen" | TR [00:59:49]–[01:00:10] Sebastian Pachon | As-built belegt |
| Prozess am Dokument starten | Verfügbare Prozesse u. a. „Angebot prüfen und vergleichen", „Prüfung und Freigabe" und der Eingangsprozess (Verteilung, sachliche Prüfung, Freigabe, Buchhaltung) | TR [01:00:10] Sebastian Pachon | As-built belegt |
| Suche | Filter nach **Kategorie** (z. B. „Livos Auftrag"), dann nach Eigenschaften (Kreditor, Auftragsnummer, Rechnungsdatum) | TR [01:06:18] Sebastian Pachon | As-built belegt |
| Akteninhalt | „Folder Content" rechts unten am Dokument: zeigt alle Akten, in denen das Dokument liegt. Akten-Symbol **gelb** = Inhalt vorhanden, **grau** = leer | TR [00:55:02], [01:06:18] Sebastian Pachon | As-built belegt |

### 1.3 Namensregeln, Löschliste, Aufbewahrung — Klarstellung

- **Namensregeln sind Projektregeln, kein Menüpunkt der UI.** Kategorien und Wertemengen tragen **immer** das Präfix „Livos". Eigenschaften bekommen zuerst den schlichten Namen. Lehnt die UI ihn als Dublette ab, wird „ (Livos)" angehängt und notiert [Quelle: CP §0 „Namensregel für Eigenschaften"; KW-04].
- **Die „Löschliste" ist ein Rückbauprotokoll, keine Aufbewahrungs- oder Löschfristen-Funktion der Plattform.** Jeder angelegte Name wird in Anlagereihenfolge mitgeschrieben, damit alles „rückstandsfrei entfernbar" bleibt [Quelle: CP §0 Regel 6; KW-04]. Die Liste selbst liegt nicht vor (siehe 0.3). Sie wäre gleich der Anlagereihenfolge in Kap. 2–4, sofern ohne Abbruch angelegt wurde (**Annahme**).
- **Aufbewahrung / Retention wurde in der Demo nicht konfiguriert** und kommt im Klickweg nicht vor [Quelle: KW-00 bis KW-35; CP]. Laut Doku-Recherche laufen Revisionssicherheit und Retention über den **d.ecs storage manager** (API `extendretention`). Das Änderungsprotokoll heißt in der Cloud **„Aktivitäten"** [Quelle: B00 T, Zeile „Revisionssicherheit/Retention"; B00 Z. 32, 124–126; KA §2.1]. Ein Cloud-Menüpfad für Aufbewahrungsfristen ist **offen**.

---

## 2 Wertemengen (8) — vollständig

Anlage über `+ > Wertemenge erstellen`, Feld **Name (Deutsch)**, Werte zeilenweise in der gezeigten Reihenfolge [Quelle: KW-06; CP §2].

| # | Name | Werte (in Reihenfolge) | Anz. | Genutzt von Eigenschaft | Hinweise | As-built-Beleg |
|---|---|---|---|---|---|---|
| 1 | **Livos Gesellschaft** | Livos Objektgesellschaft Nord mbH · Livos Objektgesellschaft Süd mbH · Livos Bau & Projekt GmbH | 3 | Gesellschaft | **Livos Projektentwicklung West GmbH fehlt absichtlich** (Klärfall, Beleg 08) — „Nicht vervollständigen" [KW-07; CP §2] | nicht explizit gezeigt. Dokumente „in verschiedenen Gesellschaften hinterlegt, Norden, Süden" [TR 01:06:18 Sebastian Pachon] |
| 2 | **Livos Kreditor** | Musterbau GmbH · Elektro Nordlicht GmbH · Stadtwerke Beispielstadt AG · Recht & Partner mbB · Reinigungsservice Blitzblank GmbH | 5 | Kreditor | Die Werte entsprechen den 5 Kreditoren aus `00_Stammdaten_Kreditoren.csv` (Nr. 70012–70355) [TD] | Kreditorenakten „Elektro Nordlicht GmbH" und „Stadtwerke Beispielstadt AG" gezeigt [TR 00:55:02, 01:06:18] |
| 3 | **Livos Objekt** | BV Hafenstraße 22 · BV Leopoldstraße 108 · BV Königsallee 60 | 3 | Objekt | BV Königsallee 60 ist das Objekt der bewusst fehlenden Gesellschaft WEST [TD, Beleg 08] | **„Libus Objekt … exemplarisch 3 Objekte angelegt"** [TR 00:57:41 Sebastian Pachon] |
| 4 | **Livos Gewerk** | Rohbau · Elektro · Ausbau · Reinigung · Beratung · Versorgung | 6 | Gewerk | — | „wie viele Gewerke" als Wertemenge erwähnt [TR 00:57:41] |
| 5 | **Livos Belegart** | Normal · Abschlagsrechnung · Schlussrechnung · Gutschrift | 4 | Belegart | AR §3.4 und KA §5.1 nennen nur 3 Werte (ohne Gutschrift) | nicht gezeigt |
| 6 | **Livos Sachkonto** | 0700 Bauten auf eigenen Grundstücken · 4240 Strom, Gas, Wasser · 4250 Reinigung · 4260 Instandhaltung · 4950 Rechts- und Beratungskosten | 5 | Sachkonto | Nummer und Bezeichnung in einem Wert | In der smart-invoice-Verteilungsmaske: „für die heutige Demo ein paar Sachkonten angelegt … Strom und Gas" [TR 00:29:35] — ob das die DMS-Wertemenge oder smart-invoice-Stammdaten sind: **offen** |
| 7 | **Livos Kostenstelle** | KST-1000 Verwaltung · KST-2000 Objektbetrieb Nord · KST-2100 Objektbetrieb Süd · KST-3000 Projektentwicklung | 4 | Kostenstelle (Mehrere Werte) | Testbeleg 03 teilt auf „Haus A 55 % / Haus B 45 %" auf. Diese Werte gibt es in der Wertemenge **nicht** [TD, Beleg 03] | Kostenstellen „Norden / Süden / Verwaltung" in der Verteilungsmaske [TR 00:29:35] — Quelle (DMS oder smart invoice) **offen** |
| 8 | **Livos Ja Nein** | Ja · Nein | 2 | Reverse Charge 13b; Freistellungsbescheinigung geprüft | Ersatz für den fehlenden booleschen Datentyp [KW-14; LM] | „ob es zu Libus gehört, der nein" [TR 00:57:41] — Bezug unklar (**Annahme:** gemeint ist „Livos Ja Nein") |

Offener Punkt aus LM (Fakt): Die Testbelege schreiben ASCII („Sued", „Hafenstrasse", „Leopoldstrasse", „Koenigsallee"). Die Wertemengen schreiben Umlaute („Süd", „Hafenstraße"). Treffen beide aufeinander, greift die automatische Zuordnung nicht. Die Entscheidung war an den Importstand geknüpft: Sind die Belege schon importiert, wird die Wertemenge auf ASCII gezogen, sonst werden die PDFs neu erzeugt [Quelle: LM „Was noch offen ist"; TD `00_Stammdaten_Gesellschaften.csv`, Belege 01–08]. **Wie das entschieden wurde, ist offen.** Außerdem schreibt KA §6.1 den Mandanten 20 als „Livos Objektgesellschaft **Süed** mbH" (Tippfehler).

---

## 3 Eigenschaften (26) — vollständig

Anlage über `+ > Eigenschaft erstellen`. Typ-Mapping: Text / Zahl / Währung / Datum. `Vordefinierte Werte` → Wertemenge, wo eine angegeben ist. Alle Felder sind Einzelwert, außer wo „Mehrere Werte" steht [Quelle: CP §3; KW-15].
Gruppen A–F nach KW-16 bis KW-21. Verwendung = Zuordnung zu Kategorien laut CP §4 / KW-24 bis KW-30. Abkürzungen: ER = Livos Eingangsrechnung, VT = Vertrag, AU = Auftrag, NW = Nachweis, KO = Korrespondenz, BE = Bescheinigung, GA = Gesellschaftsakte, KA = Kreditorenakte, OA = Objektakte.

| # | Name (Soll) | Erwarteter Anlagename | Datentyp | Wertemenge | Anzahl der Werte | Gruppe | Verwendet in | Zweck (Beleg) |
|---|---|---|---|---|---|---|---|---|
| 1 | Gesellschaft | Gesellschaft | Text | Livos Gesellschaft | Einzelwert | A | ER, VT, AU, NW, KO, GA, KA, OA (8) | Mandantenschlüssel, steuert Rechte und Workflow (Katalog 1.1) [AR §3.1, §3.4] |
| 2 | Kreditor | **Kreditor (Livos)** (Dublette erwartet) | Text | Livos Kreditor | Einzelwert | A | ER, VT, AU, NW, KO, BE, KA (7) | Kreditorenakte, Kontierungsvorschlag (2.5) [AR §3.4; KW-16] |
| 3 | Rechnungsnummer | **Rechnungsnummer (Livos)** (Dublette erwartet; im Tenant **zweimal** vorhanden) | Text | — | Einzelwert | D | ER | Dublettenprüfung, Suche [AR §3.4; KW-05; KW-19] |
| 4 | Rechnungsdatum | Rechnungsdatum — **offen**, ob „(Livos)" nötig war (in Inventur als bestehend geführt, kein Hinweis auf KW-20) | Datum | — | Einzelwert | E | ER | Pflichtangabe § 14 UStG [KW-20] |
| 5 | Leistungszeitraum | Leistungszeitraum | Text | — | Einzelwert | D | ER | Pflichtangabe, wird beim Prüfen vorgelesen [AR §3.4] |
| 6 | Nettobetrag | **Nettobetrag (Livos)** (Dublette erwartet) | Währung | — | Einzelwert | F | ER, AU | Rechnerische Prüfung, Freigabegrenze [AR §3.4; KW-21] |
| 7 | Steuersatz | Steuersatz | Zahl | — | Einzelwert | F | ER | Rechnerische Prüfung [KW-21] |
| 8 | Steuerbetrag | Steuerbetrag | Währung | — | Einzelwert | F | ER | Rechnerische Prüfung [KW-21] |
| 9 | Bruttobetrag | **Bruttobetrag (Livos)** (Dublette erwartet) | Währung | — | Einzelwert | F | ER | Freigabegrenze 10.000 € brutto [AR §3.6; KW-21] |
| 10 | Fälligkeitsdatum | Fälligkeitsdatum | Datum | — | Einzelwert | E | ER | „Basis fuer Eskalation" [KW-20] |
| 11 | Skonto | Skonto | Text | — | Einzelwert | D | ER | Zahlungsentscheidung [AR §3.4] |
| 12 | IBAN | **IBAN (Livos)** (Dublette erwartet) | Text | — | Einzelwert | D | ER | Zeigt Erkennungstiefe (2.2) [AR §3.4; KW-19] |
| 13 | Objekt | Objekt | Text | Livos Objekt | Einzelwert | A | ER, VT, AU, NW, KO, OA (6) | Objektakte, Kostenzuordnung [AR §3.4] |
| 14 | Gewerk | Gewerk | Text | Livos Gewerk | Einzelwert | A | ER, AU, NW | Feld, das BIM4You bräuchte (5.3) [AR §3.4] |
| 15 | Kostenstelle | Kostenstelle | Text | Livos Kostenstelle | **Mehrere Werte** (einziger Mehrfachwert) | B | ER | Aufteilung auf mehrere Kostenstellen (2.8), **ohne Anteil** [KW-17] |
| 16 | Sachkonto | Sachkonto | Text | Livos Sachkonto | Einzelwert | A | ER | Kontierungsvorschlag (2.5) [AR §3.4] |
| 17 | Belegart | **Belegart (Livos)** (Dublette erwartet) | Text | Livos Belegart | Einzelwert | A | ER | Unterscheidet Abschlagsrechnungen (5.2) [AR §3.4; KW-16] |
| 18 | Reverse Charge 13b | Reverse Charge 13b | Text | Livos Ja Nein | Einzelwert | C | ER | Bauleistung, Belege 06 und 07 [KW-18] |
| 19 | Sicherheitseinbehalt | Sicherheitseinbehalt | Währung | — | Einzelwert | F | ER | Macht das VOB-Thema sichtbar, ohne zu rechnen (5.2) [AR §3.4; KW-21] |
| 20 | Freistellungsbescheinigung geprüft | Freistellungsbescheinigung geprüft (in CP §4 abgekürzt „FSB geprüft") | Text | Livos Ja Nein | Einzelwert | C | ER | Manueller Schritt statt Automatik (2.7) [KW-18] |
| 21 | Gültig bis | Gültig bis | Datum | — | Einzelwert | E | VT, BE | Gültigkeit der Freistellungsbescheinigung [KW-20] |
| 22 | Vertragsnummer | Vertragsnummer | Text | — | Einzelwert | D | VT | Titel „Livos Vertrag" [KW-25] |
| 23 | Auftragsnummer | Auftragsnummer | Text | — | Einzelwert | D | AU, NW | Titel „Livos Auftrag". Suchfilter im Termin [TR 01:06:18] |
| 24 | Betreff | Betreff | Text | — | Einzelwert | D | KO | Titel „Livos Korrespondenz" [KW-28] |
| 25 | Absender | Absender | Text | — | Einzelwert | D | KO | — |
| 26 | Dokumentdatum | Dokumentdatum | Datum | — | Einzelwert | E | VT, AU, NW, KO, BE | „generisch fuer die fuenf Nicht-Rechnungsarten" [KW-20]. Im Termin bei Ablage der Auftragsbestätigung gesetzt [TR 00:55:02] |

**Kontrollsumme Gruppen:** A = 6 (Gesellschaft, Kreditor, Objekt, Gewerk, Belegart, Sachkonto) · B = 1 (Kostenstelle) · C = 2 (Reverse Charge 13b, FSB geprüft) · D = 8 (Rechnungsnummer, Leistungszeitraum, Skonto, IBAN, Vertragsnummer, Auftragsnummer, Betreff, Absender) · E = 4 (Rechnungsdatum, Fälligkeitsdatum, Gültig bis, Dokumentdatum) · F = 5 (Netto, Steuer, Brutto, Sicherheitseinbehalt [Währung]; Steuersatz [Zahl]) → **26**. Datentypen: 17 × Text, 4 × Datum, 4 × Währung, 1 × Zahl.

**Bewusst nicht angelegt:** kein `Status`-Feld. Den Status steuert der Workflow, im Tenant existiert bereits `Workflowstatus` [Quelle: CP §3; KW-22].

**Bestehende Eigenschaften im Tenant (Inventur-Soll, Ergebnis offen):** Kreditor, Rechnungsnummer (zwei Vorkommen), IBAN, Belegart, Rechnungsdatum, Nettobetrag, Bruttobetrag. Zu notieren waren Datentyp und Einzel-/Mehrfachwert [Quelle: CP §1; KW-05]. Laut Doku legt der smart-invoice-Onboarding-Assistent unter anderem Mandant, Mandantenname, Kreditor, Kreditorname, **Kostenstellen**, Kostenträger, **Sachkonten**, Bruttobetrag, Nettobetrag, MwSt Betrag, Rechnungsnummer, Rechnungsdatum, Leistungsdatum, Belegart, Buchungstext und Workflowstatus an [Quelle: KA §4]. **Annahme:** Die Dubletten stammen überwiegend aus dem smart-invoice-Onboarding. Dazu kommen fast gleichnamige Paare, die die UI **nicht** als Dublette ablehnt, die fachlich aber konkurrieren: „Kostenstelle" / „Kostenstellen", „Sachkonto" / „Sachkonten", „Gesellschaft" / „Mandant"/„Mandantenname", „Steuerbetrag" / „MwSt Betrag".

---

## 4 Kategorien (9) — vollständig

Anlage über `+ > Kategorie erstellen`, zuerst den Typ **Dokumentart** oder **Aktenart** wählen, dann **Name (Deutsch)** mit Präfix Livos. Eigenschaften zuweisen unter **Zugewiesene Eigenschaften**. Reihenfolge per Ziehgriff, Pflicht per `⋮ > Pflichtfeld`, Titel per `T > Titel bearbeiten` [Quelle: KW-23, KW-31 bis KW-33; CP §4].

### 4.1 Übersicht

| # | Kategorie | Typ | Zugewiesene Eigenschaften (Reihenfolge = Maskenposition) | Anz. | Pflichtfelder | Titel (T-Button) | As-built-Beleg (TR) |
|---|---|---|---|---|---|---|---|
| 1 | **Livos Eingangsrechnung** | Dokumentart | 1 Gesellschaft · 2 Kreditor · 3 Rechnungsnummer · 4 Rechnungsdatum · 5 Leistungszeitraum · 6 Nettobetrag · 7 Steuersatz · 8 Steuerbetrag · 9 Bruttobetrag · 10 Fälligkeitsdatum · 11 Skonto · 12 IBAN · 13 Objekt · 14 Gewerk · 15 Kostenstelle · 16 Sachkonto · 17 Belegart · 18 Reverse Charge 13b · 19 Sicherheitseinbehalt · 20 Freistellungsbescheinigung geprüft | 20 | **10:** Gesellschaft, Kreditor, Rechnungsnummer, Rechnungsdatum, Nettobetrag, Bruttobetrag, Fälligkeitsdatum, Objekt, Kostenstelle, Belegart | Kreditor, Rechnungsnummer, Bruttobetrag | „Eingangsrechnung" als Dokumentenart in den Akten erwähnt [00:01:20]. In der Konfiguration wurde eine „Eingangsrechnung" mit Kreditor, **Kreditorname, Mandant, Mandantenname**, Rechnungsnummer gezeigt [00:57:41]. **Annahme:** Das war die smart-invoice-Kategorie, nicht „Livos Eingangsrechnung" (die hat Gesellschaft statt Mandant). Eine Eingangsrechnung lag in der Kreditorenakte „Stadtwerke Beispielstadt AG" [01:06:18] |
| 2 | **Livos Vertrag** | Dokumentart | Gesellschaft · Kreditor · Vertragsnummer · Dokumentdatum · Gültig bis · Objekt | 6 | Gesellschaft | Kreditor, Vertragsnummer | nicht gezeigt |
| 3 | **Livos Auftrag** | Dokumentart | Gesellschaft · Kreditor · Auftragsnummer · Dokumentdatum · Objekt · Gewerk · Nettobetrag | 7 | Gesellschaft | Kreditor, Auftragsnummer | **Belegt:** Auftragsbestätigung live mit Kategorie „Auftrag" abgelegt (Gesellschaft, Kreditor, Objekt, Dokumentdatum), landete in Kreditorenakte Elektro Nordlicht GmbH **und** Objektakte [00:53:32–00:55:02]. Suche nach „Livos Auftrag" [01:06:18] |
| 4 | **Livos Nachweis** | Dokumentart | Gesellschaft · Kreditor · Dokumentdatum · Objekt · Gewerk · Auftragsnummer | 6 | Gesellschaft | Kreditor, Dokumentdatum | nicht gezeigt |
| 5 | **Livos Korrespondenz** | Dokumentart | Gesellschaft · Kreditor · Dokumentdatum · Betreff · Absender · Objekt | 6 | Gesellschaft | Betreff, Dokumentdatum | nicht gezeigt |
| 6 | **Livos Bescheinigung** | Dokumentart | Kreditor · Dokumentdatum · Gültig bis | 3 | Kreditor | Kreditor, Gültig bis | als Dokumentenart erwähnt [00:01:20] |
| 7 | **Livos Gesellschaftsakte** | Aktenart | Gesellschaft | 1 | Gesellschaft | Gesellschaft | nicht gezeigt |
| 8 | **Livos Kreditorenakte** | Aktenart | Kreditor · Gesellschaft | 2 | Kreditor | Kreditor | **Belegt:** „Livos Kreditorenakte … alle Kreditoren haben entsprechend auch Unterakten". Stadtwerke Beispielstadt AG enthält Auftrag und Eingangsrechnung [01:06:18]. Kreditorenakte Elektro Nordlicht GmbH [00:55:02] |
| 9 | **Livos Objektakte** | Aktenart | Objekt · Gesellschaft | 2 | Objekt | Objekt | **Belegt:** „Objektakte" als Ablageort der Auftragsbestätigung. In der Konfiguration: „Objektakte: Livos Auftrag" [00:55:02] |

Quellen der Tabelle: Eigenschaften und Reihenfolge [CP §4; KW-24 bis KW-30]; Pflicht [CP §4 „Pflichtfelder"; KW-32]; Titel [CP §4 „Titel"; KW-24 bis KW-29, KW-33]; As-built [TR, Sprecher Sebastian Pachon, Zeitstempel wie angegeben].

### 4.2 Regeln zu Pflicht, Reihenfolge und Titel

- **Pflichtfelder hängen an der Kategorie, nicht an der Eigenschaft.** Nur bei Livos Eingangsrechnung sind 10 der 20 Felder Pflicht. Bei allen übrigen Kategorien ist nur das jeweils erste Feld Pflicht. „Eine Maske aus lauter Pflichtfeldern blockiert die Demo, sobald ein Wert fehlt." [Quelle: KW-32; CP §4]. Das deckt sich mit der Doku-Aussage „Pflichtfelder werden je Dokumentart gesetzt, nicht an der Eigenschaft selbst" [Quelle: KA §5.3].
- **Die Reihenfolge ist die Position.** Ein Positionsfeld gibt es nicht [Quelle: KW-31; KW-15].
- **Titelregel:** Die Titel setzen sich aus Eigenschaftswerten zusammen, eingestellt per `T`-Button. Aktenarten bekommen jeweils das erste zugewiesene Feld [Quelle: KW-33].
- **Zuweisen ist additiv.** „Zuweisen ändert die Eigenschaft NICHT. Die Zuordnung lebt an der Kategorie" [Quelle: KW-23].

### 4.3 Aktenstruktur (Aktenbildung) — Lücke im Klickweg

- **As-built belegt:** Im Termin gab es eine Konfiguration, **welche Dokumentarten in welche Aktenart dürfen**: „Wir haben die Objektakte. Wir haben Libusauftrag und Kreatorenakte, ebenfalls Libusauftrag. Das heißt, wir schreiben einmal fest, in diese Akte dürfen Dokumentenarten reingehen, die Auftrag enthalten" [TR 00:55:02–00:56:45 Sebastian Pachon]. „Auftrag, Eingangsrechnungen und Angebote dürfen genau in diese Aktenstruktur reingehen" [TR 01:06:18 Sebastian Pachon]. Die Kreditorenakte hat **Unterakten je Kreditor** [TR 01:06:18]. Beliebig viele Ebenen sind möglich, empfohlen sind höchstens 4–5 [TR 00:57:14–00:57:22 Sebastian Pachon].
- **Lücke:** Der Klickweg (KW-00 bis KW-35) und CP enthalten **keinen Schritt** für diese Akten-Dokument-Zuordnung. Wo und wie das in der Cloud-UI eingestellt wurde, ist **offen**.
- **Offen:** „Angebote" gehört nicht zu den 9 Livos-Kategorien. **Annahme:** eine bereits bestehende Kategorie des Tenants oder eine ungenaue Aussage im Termin.
- **Doku-Hinweis (On-Prem, Übertragbarkeit auf die Cloud = Annahme):** Die Akten entstehen über „Erkennungseigenschaften". Sind diese leer, „wird keine Akte erzeugt bzw. verknüpft" [Quelle: B03 §7d]. Daraus folgt: Die Aktenschlüssel (Gesellschaft, Kreditor, Objekt) müssen in den Dokumentarten Pflicht sein. In der Demo gilt das nur für die Eingangsrechnung vollständig. Bei Vertrag, Auftrag, Nachweis und Korrespondenz ist nur Gesellschaft Pflicht, Kreditor und Objekt nicht.

---

## 5 Regeln („vier Verbote") und Plattformgrenzen

### 5.1 Die vier Verbote (wörtlich, KW-03)

1. „Kein bestehendes Objekt umbenennen, bearbeiten, löschen oder umhaengen."
2. „smart invoice / Rechnungsverarbeitung nur lesen. Nie speichern."
3. „Keine Benutzer, Gruppen, Berechtigungen. Das ist Aufgabe 3."
4. „Keine Dokumente hochladen oder importieren. Das ist Aufgabe 4."

Begründung auf der Folie: „Der Tenant wird produktiv genutzt: 102 Belege im Umlauf, aktiver Workflow, vier si_-Gruppen. Jede Änderung trifft arbeitende Kollegen." [Quelle: KW-03]

### 5.2 Weitere Arbeitsregeln (CP §0, KW)

| Regel | Wortlaut / Inhalt | Quelle |
|---|---|---|
| Absolute Regel 1 | „Niemals ein bestehendes Objekt umbenennen, bearbeiten, löschen, deaktivieren oder einer anderen Kategorie zuweisen." | CP §0 |
| Absolute Regel 2 | Nichts unter `Konfiguration > Rechnungsverarbeitung` / smart invoice: „kein Workflow, keine Freigabematrix, keine `si_`-Gruppe, keine Belegmaske, kein Onboarding-Schritt" | CP §0 |
| Absolute Regel 5 | Jedes neue Objekt trägt „Livos" im Namen | CP §0; KW-04 |
| Absolute Regel 6 | Löschliste in Anlagereihenfolge | CP §0; KW-04 |
| Absolute Regel 7 | Wenn ein Schritt nicht geht wie beschrieben: „abbrechen, nicht improvisieren", im Bericht festhalten, weitermachen | CP §0 |
| Inventur | Nur lesen, nichts anklicken, was speichert | KW-05 |
| WEST | Livos Projektentwicklung West GmbH nicht in die Wertemenge aufnehmen | KW-07; CP §2 |
| Kein Status-Feld | Workflowstatus existiert, Workflow steuert | KW-22; CP §3 |
| Pflichtfelder sparsam | Nur die festgelegten Felder | KW-32 |
| Abschluss | Nach dem Bericht nichts weiter tun: kein Import, keine Benutzer/Gruppen, nichts in smart invoice | KW-35; CP §5 |
| Workshop-Leitsatz | „Ein Workshop scheitert nicht an einer fehlenden Kategorie. Er scheitert daran, dass der Klickweg vor Publikum gesucht wird." / „Eine Konfiguration, die zwei Stunden vor dem Termin entsteht, ist im Workshop eine Fehlerquelle, kein Feature." | LM |

### 5.3 Plattformgrenzen und Eigenheiten der Cloud

| # | Grenze / Eigenheit | Beleg | Workaround / Konsequenz |
|---|---|---|---|
| G1 | **Kein Ja/Nein-(Boolean-)Datentyp.** Es gibt nur Text, Zahl, Währung, Datum, Datum-und-Zeit | KW-14; LM; KA §5.1; B03 Offene Punkte Nr. 4 | Wertemenge „Livos Ja Nein" + Datentyp Text. Keine Checkbox (KW-18) |
| G2 | **„Auswahlliste" ist kein Datentyp**, sondern Text + „Vordefinierte Werte" (Wertemenge) | KW-16; KA §5.2; B03 Nr. 5 | Wertemengen zuerst anlegen |
| G3 | **Mehrfachwert** nur über „Anzahl der Werte: Mehrere Werte" | KW-15, KW-17 | In der Demo nur Kostenstelle |
| G4 | **Kein Mehrfachfeld mit Zusatzwert** („Kostenstelle mit Anteil" gibt es nicht) | KW-17; KA §5.2, §11; LM; B03 Nr. 3 | Anteile / Splitting in den smart-invoice-Belegpositionen. Im Termin: Aufteilung in % auf Positionen [TR 00:43:06] |
| G5 | **Kein eigenes Status-Feld nötig oder sinnvoll**; `Workflowstatus` existiert | KW-22; CP §3 | Status aus dem Workflow bzw. Rechnungseingangsbuch |
| G6 | **Position, Beschreibung und Kürzel gibt es in der Cloud-UI nicht** | KW-15; LM | Reihenfolge per Ziehgriff = Position (KW-31). Die On-Prem-Regeln (Positionsbereiche 1–89, Kürzel max. 5 Zeichen) entfallen |
| G7 | **Eigenschaftsnamen sind tenantweit eindeutig.** Dubletten werden abgelehnt | KW-04, KW-16, KW-19, KW-21 | Demo: Suffix „ (Livos)". Produktiv: bestehende Eigenschaften wiederverwenden (Kap. 8) |
| G8 | **Name (Deutsch) max. 50 Zeichen** (Wertemenge). Die Doku (On-Prem) nennt für die Wertemengen-Bezeichnung 255 Zeichen, für Eigenschaftstitel 50 Zeichen mit Sonderzeichen nur `+ - _` | KW-06; KA §5.1–5.2 | Ob Klammern „(Livos)" und „&" in Namen erlaubt sind: in der Cloud **offen** (Werte mit „&" sind lt. KW-07/08 vorgesehen) |
| G9 | **Max. 89 Eigenschaften je Kategorie** | KW-22; KA §5.3 (On-Prem-Aufteilung 49/10/10/10/10) | Cloud-Aufteilung nach Typ: **offen** |
| G10 | **Pflichtfeld nur je Kategorie** (`⋮ > Pflichtfeld`) | KW-32; KA §5.3 | Pro Kategorie getrennt pflegen |
| G11 | **Dashboard: nur vier Standard-Widgets** (Suche, Zuletzt bearbeitet, Beobachtet, Favorisiert), keines fachlich. Kein Filterfeld in eigenen Widgets | LM; KA §10; B00 X, Z | Managementsicht → **Rechnungseingangsbuch** (Schnellzugriffe, Filter, Gruppierung). Eigene Widgets nur als Verknüpfungs-, Listen- (serverseitige URL) oder iframe-Widget |
| G12 | „Zuletzt bearbeitet" erfasst **keine Statuswechsel** | B00 X | Nicht als Statusmonitor verwenden |
| G13 | „Sichtbarkeit von Widgets" ist **keine Sicherheits- oder Zugriffsbeschränkung** | KA §10.2; B00 Y | Rechte getrennt über Berechtigungen |
| G14 | **Liegezeit** ist in keiner Doku als Feld oder Spalte belegt | LM; KA §11; B00 AB | Katalog 3.2 mit Vorbehalt. Ersatz: Sortierung nach Eingangsdatum. Im Termin: Auswertung nur über externe App/Middleware [TR 00:36:13 Sebastian Pachon] |
| G15 | **Mandantenerkennung (smart invoice) über Name + Anschrift, nicht über Steuernummer.** Mandantenfelder: id, name, parent_id, address, city, zip_code, local_currency, country | LM; KA §6 | NORD und BAUP haben dieselbe Anschrift → Risiko. Mandantenname exakt wie auf der Rechnung. Alias-Postfächer (KA §7) |
| G16 | **Mailimport:** produktiv nur Microsoft 365 (Graph). Exchange On-Prem über „d.velop email fetcher". IMAP „zukünftig verfügbar". Nur eine Bereitstellungsform. **Abrufintervall nicht dokumentiert** | KA §7.1, §7.4; B06 4g | Intervall selbst messen |
| G17 | **Vier-Augen-Prinzip von smart invoice = Vorschau-Feature** (Aktivierung über Support, Pfad undokumentiert) | KA §8, §11 | Freigabegrenze über eine eigene Verbindung (Phase 5) |
| G18 | Workflow-Bedingungen: **Beträge in Cent** (10.000,00 € = 1000000). Verbindungen werden **top-down** ausgewertet, die erste passende gewinnt | KA §8 | Grenzverbindung oberhalb der Standardverbindung |
| G19 | **Cloud-Administrationsdoku nicht öffentlich** (Login). Benutzer-, Gruppen- und Berechtigungsoberfläche ungeprüft | KA §3.3, §9.2; B03 §8c, Nr. 7–8 | Zugang zum d.velop Service Portal beschaffen |
| G20 | **Eskalation** (Aktionskatalog Mailversand undokumentiert) und **Standard-Aufteilungsschlüssel je Gesellschaft** nicht dokumentiert | KA §11 | Im Termin nur verbal; Ampel über Fälligkeit (s. u.) |
| G21 | Automatik Freistellungsbescheinigung = Individualentwicklung (Katalog 2.7 = A) | AR §7; TR [00:48:28]–[00:49:21] | Eigenschaft „FSB geprüft" + Bescheinigung mit „Gültig bis" am Kreditor, manuelle Prüfung |
| G22 | **Rückweisung per Mail an den Lieferanten** nicht direkt in d.velop | TR [00:39:59]–[00:41:01] Sebastian Pachon | Über die MDIS-Middleware |
| G23 | **Dokument-/Rechnungsbearbeitung** (Kürzen): Der nötige Bearbeitungsschritt war „bei unserer Demo-Umgebung nicht vorhanden" | TR [00:43:06] Sebastian Pachon | Produktiv als Workflowschritt einplanen |
| G24 | Hook-Funktionen (JPL), d.3 config, Sub-Administration: nur On-Prem dokumentiert | B03 §8c | Berechtigungslogik mit @D3HOOK nicht in die Cloud übertragen |
| G25 | UI-Navigation: Browser-Zurück unbrauchbar. Zwei-Schritt-Anmeldedialog kann blockieren. smart-invoice-Zurück-Pfeil springt zur Konfigurationsübersicht | KW-01; CP §0 | Schulungsinhalt für Admins |

**Beobachtete Einstellungen im Tenant (as-built, nicht von MDIS für Livos gebaut):**
- Aktiver Rechnungsworkflow mit den Schritten **Verteilung → sachliche Prüfung → Freigabe → Buchhaltung**. E-Mail-Benachrichtigung je Aufgabe. Sachliche Prüfung schreibgeschützt mit Häkchen „sachlich geprüft". Dublettenprüfung und USt-Prüfung laufen im Hintergrund. Eine Dublette kann nur mit Begründung angenommen werden [TR 00:04:44, 00:25:25, 00:29:54–00:34:11, 00:37:45, 00:41:01 Sebastian Pachon].
- **Fälligkeitsampel** in „Meine Aufgaben": „auf 10 Tage eingestellt" (gelb), rot ab 5 Tagen vor Netto-Fälligkeit [TR 01:03:34 Sebastian Pachon].
- Vertretung über **Abwesenheitsstatus** mit hinterlegter Vertretung, auch vorab [TR 01:05:00 Sebastian Pachon].
- Umfang: **102 Belege im Umlauf** (Stand der Folien) bzw. **226 Rechnungen** im Rechnungseingangsbuch am Termin [KW-03; TR 00:25:25].

---

## 6 Die Konfigurationsphasen aus der Konfigurationsanleitung (KA)

Die KA gilt „für Cloud und On-Premises" und beruht auf öffentlicher Doku. Nicht Belegtes ist als „ungeprüft" markiert [Quelle: KA Kopf, §1]. Sie hat **Phase 0 (Bestandsaufnahme) und die Phasen 1–7**. Phase 2 hat zwei Wege, A mit smart invoice und B manuell. Laut LM enthält die KA „an einigen Stellen noch die alten Begriffe" [Quelle: LM].

### Phase 0 — Bestandsaufnahme (30 min)

| Schritt | Inhalt | Ergebnis / As-built |
|---|---|---|
| 0.1 Cloud oder On-Prem erkennen | Indizien für die Cloud: Features „Aktivitäten", „Geteilte Dokumente", „Scannen" mit Stapeln, Aufgabenlisten „Meine Aufgaben". On-Prem: „Prozessportal", d.3 admin, „Aufgaben und Nachrichten" [KA §2.1] | **Cloud** (Tenant `*.d-velop.cloud`) [KW-00; CP]. „Meine Aufgaben" im Termin genannt [TR 01:00:10] |
| 0.2 Modulumfang | smart invoice (→ Weg A/B), Rechnungseingangsbuch, inbound/inbound scan, E-Mail-Anbindung, process studio, Erscheinungsbild > Startseite, Volltextsuche [KA §2.2] | smart invoice **aktiv** [CP Kopf; LM]. Rechnungseingangsbuch vorhanden [TR 00:25:25]. Postfächer vorhanden [TR 00:49:33]. process studio und Volltextsuche: **offen** |
| Konsequenz | Mit smart invoice gilt Weg A: Der Rechnungsworkflow wird nicht von Hand gebaut [KA §1] | Weg A faktisch gegeben (Onboarding bestand bereits) |

### Phase 1 — Benutzer und Gruppen (Pflicht, 45 min)

| Schritt | Inhalt (KA §3) |
|---|---|
| Anzulegen | U1 **Maria Lentz**, Buchhaltung/Rechnungseingang, Gruppe **LIV_BUCH** · U3 **Dr. Claudia Renner**, Geschäftsführung/2. Freigabestufe, **LIV_GF** · U2 **Jan Bergmann**, Projektleiter (empfohlen, Mandantenbeweis), **LIV_NORD_PL** |
| On-Prem (d.3 admin) | Berechtigungen > Benutzer > Neu: Vollständiger Name (max. 50), Benutzername (max. 30, a–z A–Z 0–9 _), Kennwort, Registerkarte Gruppenzugehörigkeit, Registerkarte Optionale Felder (Feld 5 = Gesellschaftskennung), OK. Gruppen: Berechtigungen > Gruppen > Neu, „Verteilung an alle Mitglieder (Gruppe)". Fallen: Benutzername unveränderlich; Gruppennamen müssen sich in den ersten 8 Zeichen unterscheiden |
| Cloud | „d.velop usermanagement — konkreter Klickweg … nicht beschrieben … **Ungeprüft**" |
| Prüfkriterium | Anmeldung als U1 und U3 in zwei Browsern gleichzeitig |
| **As-built** | **Nicht Teil von Aufgabe 2** (Verbot 3). Laut LM am Morgen keine Benutzer anlegen. Im Termin **kein Benutzerwechsel**: Der Präsentator war selbst Zuständiger für Verteilung und hinterlegt im Team der sachlichen Prüfer [TR 00:25:25, 00:29:54]. U1/U2/U3 kommen im Transkript nicht vor. Ein Benutzer „Annalena" existiert (Aufgabenempfängerin) [TR 00:59:49]. Die Admin-Maske für Benutzer und Gruppenrechte wurde nur gezeigt [TR 01:04:23]. Die smart-invoice-Gruppen im Tenant: **vier `si_`-Gruppen** [KW-03] |

### Phase 2, Weg A — Onboarding-Assistent (smart invoice)

| Schritt | Inhalt (KA §4) |
|---|---|
| Ergebnis lt. Doku | „funktionierender Eingangsrechnungsworkflow mit den Schritten Verteilung, Prüfung, Freigabe und Buchhaltung" |
| Automatisch angelegt | Aktenplan: Eingangsrechnung/-gutschrift · Kreditorenvorgangsakte · Rechnungsanlage · Workflowprotokoll ERV. Gruppen: dv_Buchhaltung · dv_Freigeber · dv_Sachliche_Prüfer · dv_inbound · dv_inbound_Administratoren · dv_Service_Accounts · dv_Workflowteilnehmer. Eigenschaften: Mandant … Workflowstatus (16). Importprofile und Eingangspostfächer: „Eingangsrechnung automatisch" / „… manuell". In smart invoice: Erkennungsbackend, Best-Practice-Workflow, Repository-Verbindung |
| Danach | „erst schauen, dann bauen": Nur Fehlendes nachlegen (Objekt/Bauvorhaben, Gewerk/Los, Sicherheitseinbehalt) |
| Prüfkriterium | 4 Schritte unter „Schritte" und 7 dv_-Gruppen vorhanden |
| **As-built** | Das Onboarding war im Tenant bereits erfolgt (aktiver Workflow, 102 Belege) [KW-03; LM]. **Workflow belegt:** Verteilung → sachliche Prüfung → Freigabe → Buchhaltung [TR 00:29:54–00:34:11; 01:00:10]. **Abweichungen:** 4 `si_`-Gruppen statt 7 `dv_`-Gruppen [KW-03 vs. KA §4]. **3** Postfächer (u. a. „Invoices") statt 2 „Eingangsrechnung automatisch/manuell" [TR 00:49:33 vs. KA §4]. Das Prinzip „nur Fehlendes nachlegen" wurde **nicht** umgesetzt: Aufgabe 2 legt eine eigene, parallele Livos-Struktur mit 26 Eigenschaften an, inkl. Dubletten mit Suffix „(Livos)" [CP §3; KW-16/19/21] |

### Phase 2, Weg B — Manueller Aufbau (ohne smart invoice)

| Schritt | Inhalt (KA §5, **On-Prem-Begriffe**) | Cloud-Realität (Aufgabe 2) |
|---|---|---|
| Reihenfolge | Wertemengen → Eigenschaften → Dokumentarten → Berechtigungen (Pflicht) | Gleiche Reihenfolge: Wertemengen → Eigenschaften → Kategorien → Feinschliff [KW Teile 2–5] |
| 5.1 Wertemengen | „Dokumente und Akten > Wertemengen": Bezeichnung (max. 255, Sonderzeichen `+ - _`), Datentyp, Werte (max. 250), Sortierung. Für Livos: **Gesellschaften** (NORD, SUED, BAUP), **Belegart** (Normal, Abschlagsrechnung, Schlussrechnung), **JaNein** | `Konfiguration > … > Dokumenten- und Aktenstrukturen > Wertemengen > +`, **Name (Deutsch)** max. 50. **8** Wertemengen mit Präfix Livos und ausgeschriebenen Werten (Kap. 2) |
| 5.2 Erweiterte Eigenschaften | „Dokumente und Akten > Erweiterte Eigenschaften > Neu": Titel, Datentyp (Alphanumerisch/Numerisch/Datum/Datum und Uhrzeit/Geld), **Position**, Länge, Wertevorrat, Plausibilitätskontrolle | Register **Eigenschaften**: Name (Deutsch), Datentyp **Text/Zahl/Währung/Datum**, **Vordefinierte Werte**, **Anzahl der Werte**. **Keine** Position, Beschreibung, Kürzel [KW-15] |
| 5.3 Dokumentart | „Dokumente und Akten > Dokumentarten > Neu": Name, Art, **Kürzel** (max. 5), 4-Augen-Option, Eigenschaften „< Einzeln / << Alle", Positionen per Drag & Drop, Details → Pflicht; Neuanmeldung aller Benutzer nach Speichern | Register **Kategorien** > `+ > Kategorie erstellen > Dokumentart/Aktenart`, **Zugewiesene Eigenschaften**, Ziehgriff, `⋮ > Pflichtfeld`, `T > Titel bearbeiten` [KW-23 bis KW-33]. Neuanmeldung: in der Cloud **offen** |
| Grenzen | max. 89 Eigenschaften je Dokumentart (49/10/10/10/10), max. 2.000 Dokumentarten je Repository. „Unsere 18 Eigenschaften passen mühelos" | 89 je Kategorie bestätigt (KW-22). Angelegt werden **26** Eigenschaften |

### Phase 3 — Stammdaten: Mandanten und Kreditoren

| Schritt | Inhalt (KA §6) |
|---|---|
| Kernkorrektur | Mandantenerkennung über **Name und Anschrift**, nicht über die Steuernummer. Die Steuernummer gibt es nur beim Kreditor (vat_id, registration_id) |
| 6.1 Mandanten | id 10 Livos Objektgesellschaft Nord mbH, Hafenstraße 22, 20359 Hamburg · id 20 Livos Objektgesellschaft „Süed" mbH, Leopoldstraße 108, 80802 München · id 30 Livos Bau & Projekt GmbH, Hafenstraße 22, 20359 Hamburg. Name exakt wie auf den Testrechnungen. **WEST nicht anlegen.** Standardmandant leer (Klärfall zeigen) oder NORD |
| 6.2 Kreditoren | Fünf Stück aus der CSV. Steuernummer und USt-IdNr steuern die Kreditorenerkennung. Kostenstellen/Kostenträger/Sachkonten: Felder company_id, nr, name; ohne Mandant gültig für alle |
| Prüfkriterium | Ein Testbeleg an NORD wird automatisch Mandant 10 zugeordnet |
| **As-built** | Nicht belegt, ob die Mandanten 10/20/30 angelegt wurden. Sachkonten „für die heutige Demo angelegt" und Kostenstellen (Norden/Süden/Verwaltung) sowie Kostenträger in der Verteilungsmaske sichtbar [TR 00:29:35–00:29:54]. Die automatische Mandantenzuordnung wurde nur verbal bestätigt, nicht am NORD/BAUP-Fall gezeigt [TR 00:31:16–00:31:41 André Töpper / Sebastian Pachon]. Die Lieferantennummer wurde bei der Erfassung manuell nachgetragen [TR 00:04:44]. Offene Stammdatenfrage: mandantenübergreifende Lieferantennummer mit DATEV-Kreditorennummer als Referenz [TR 00:08:01–00:11:39 Thomas Gross] |

### Phase 4 — Mailimport mit Alias-Adressen

| Schritt | Inhalt (KA §7) |
|---|---|
| 7.1 Voraussetzung | Microsoft 365 / Graph (Exchange On-Prem über email fetcher, IMAP „zukünftig") |
| 7.2 Microsoft Entra | App-Registrierung, Kontotyp „Nur Konten in diesem Organisationsverzeichnis", Graph-Anwendungsberechtigungen **Mail.ReadWrite**, **User.ReadBasic.All**, Clientschlüssel, Anzeigename/Verzeichnis-ID/Anwendungs-ID. Sicherheitshinweis: Die App kann auf jedes Postfach zugreifen → per Richtlinie einschränken |
| 7.3 Verbindung | Konfiguration > Dokumentenmanagement > E-Mail-Anbindung > Postfach-Verbindungseinstellungen: Microsoft Graph, 4 Werte, Speichern, Verbindung testen, Verarbeitung aktiviert |
| 7.4 Postfächer/Aliasse | … > Verwalten von Postfächern: Hinzufügen, Anzeigename, Alias (z. B. invoices+1@…), Importprofil, Stapelname mit %Sender% %Subject% %Timestamp% %Date%, „Stapel nach Import abschließen", Schlüssel-Wert-Paare (Gesellschaft = NORD), Berechtigungen, Fehlerbenachrichtigung, Speichern. Für Livos: rechnungen+nord@…, +sued@…, +baup@…. Testpostfach vorher leeren; Ordner dvelop_finished / dvelop_not_processed. Abrufintervall selbst messen |
| Prüfkriterium | Mail an …+nord@… erzeugt einen Beleg mit Gesellschaft = NORD |
| **As-built** | 3 Postfächer vorhanden, u. a. „Invoices", mit Beschreibung, Importprofil, zugelassenen E-Mail-Adressen [TR 00:49:33]. Eine vorbereitete Mail wurde live gesendet, das Einlesen „dauert ganz kurz" (nicht gemessen), Ankunft im Import unter „Standardprofil" [TR 00:49:33–00:53:32]. **Aliasse je Gesellschaft nicht belegt.** Erfassung zusätzlich per Upload „Rechnung einlesen" [TR 00:01:20] |

### Phase 5 — Freigabegrenze (Kernmoment)

| Schritt | Inhalt (KA §8) |
|---|---|
| Ablauf | Schritte > Neuer Schritt „Freigabe Geschäftsleitung" (Schritttyp Freigabe) → Bearbeiterfindung mit Gruppe LIV_GF → Aktionen/Verbindungen (Weitergabe an Buchhaltung) → in den Schritt Freigabe wechseln → Perspektive Aktionen → in der Aktion Freigeben neue Verbindung zu „Freigabe Geschäftsleitung" mit Bedingung `voucher.net_amount >= 1000000` → Verbindungseinstellungen > Freigabe > **Erteilen** aktivieren → neue Verbindung per Drag & Drop über die Standardverbindung ziehen |
| Fallen | Beträge in Cent. Top-down-Auswertung. Bei „Erteilen" das Feld „Sachlich richtig" beachten (`voucher.verified?`) |
| Hinweis | Die KA verwendet `net_amount` (netto). AR §3.6 definiert die Grenze aber als **10.000 € brutto**. Beleg 01: 14.756 € brutto = 12.400 € netto (Annahme bei 19 % USt), liegt also in beiden Fällen über der Grenze. **Widerspruch Netto/Brutto offen** |
| Prüfkriterium | Beleg 01 (14.756 €) geht nach der 1. Freigabe an U3, Beleg 02 (1.190 €) nicht |
| **As-built** | **Nicht umgesetzt / nicht gezeigt.** Verbot 2 (smart invoice nur lesen) [KW-03]. Im Termin nur der Standardschritt Freigabe mit verbalem Hinweis „Vier-Augen-Prinzip" [TR 00:31:42]. Keine 10.000-€-Grenze, kein Benutzerwechsel im Transkript |

### Phase 6 — Berechtigungen / Mandantentrennung

| Schritt | Inhalt (KA §9) |
|---|---|
| On-Prem | Berechtigungen > Dokumentklassen > Neu (Dokumentart, Bezeichnung, technischer Name max. 10 ohne Präfix `CLAS_`, Restriktion im Feld Gesellschaft) → Berechtigungsprofile > Neu (Recht erteilen/verweigern/ignorieren; Lesen, Schreiben, Statustransfer, Verknüpfungen, Aktivitäten) → Berechtigungsprofil-Zuordnung → Neuanmeldung. Skalierung: eine dokumentartunabhängige Klasse mit **@D3GROUP** bzw. **@D3USER_OPTFIELD_05**. „Ein explizites Verweigerungsrecht kann durch andere Zuordnungen nicht aufgehoben werden." |
| Cloud | „Berechtigungsoberfläche und Klickwege sind uns daher unbekannt. **Ungeprüft.**" |
| Prüfkriterium | Als U2 kein Süd-Beleg in der Suche |
| **As-built** | **Nicht umgesetzt** (Verbot 3; Aufgabe 3). Im Termin nur verbal: Admin kann Gruppen Berechtigungen zuteilen, z. B. „nur der Marketingabteilung … nur für Marketingdokumente" [TR 01:04:23, 01:05:47 Sebastian Pachon]. Die R2-Demo (U2 sieht keine SÜD-Belege) fand nicht statt |

### Phase 7 — Dashboard und Rechnungseingangsbuch

| Schritt | Inhalt (KA §10) |
|---|---|
| Korrektur | Die Managementsicht gehört nicht ins Dashboard. Es gibt nur 4 Standard-Widgets. Status, Betragsfilter und Gruppierung nach Gesellschaft leistet das Rechnungseingangsbuch |
| 10.1 Rechnungseingangsbuch | Startseite > Widget hinzufügen > „Rechnungseingangsbuch". Schnellzugriffe: Meine offenen Rechnungen · Rechnungen in Vertretung · Alle offenen Rechnungen · Archiv (6 Monate, erweiterbar auf 12). Filteroperatoren, sachliche Gruppierung, Spaltensteuerung, Clearing-Modus („Weitere Aktionen anzeigen"), eigene Schnellzugriffe über das Plus-Symbol. Für die Demo: „Über 10.000 Euro" und „Gesellschaft Nord" |
| 10.2 Rollen-Dashboards | Konfiguration > Erscheinungsbild > Startseite > Sichtbarkeit von Widgets → Hinzufügen → Benutzer/Gruppe → Widgets → Speichern → **Zuordnungen anwenden**. Keine Sicherheitsfunktion |
| 10.3 Eigene Widgets | … > Widgets erstellen > Neues Widget erstellen: Ziel-URL, Sichtbarkeit, Symbol (Pflicht, 48×48), Hintergrundfarbe, Titel je Sprache. Erweitert: Listen-Widget, Erweitertes Widget. Kein Filterfeld |
| Prüfkriterium | Das Rechnungseingangsbuch zeigt ≥ 4 Status. Schnellzugriff „über 10.000 Euro" liefert genau 3 Belege |
| **As-built** | Einstieg in den Termin über das Dashboard. Widgets anpassbar [TR 00:01:16–00:01:20]. **Rechnungseingangsbuch belegt:** 226 Rechnungen, Filter/Gruppierung nach aktuellem Schritt (Buchhaltung, Freigabe, Verteilung, sachliche Prüfung), Anzeige der Restzeit bis Zahlung und Skonto [TR 00:25:25–00:28:57]. Eigene Schnellzugriffe „Über 10.000 Euro" / „Gesellschaft Nord": **nicht belegt** |

### Prüfliste der KA (§12) mit As-built-Status

| Prüfpunkt | Status laut Quellen |
|---|---|
| Phase 0: Cloud/On-Prem und Module bekannt | erfüllt (Cloud, smart invoice aktiv) |
| Phase 1: U1 und U3 gleichzeitig angemeldet | nicht belegt, im Termin nicht gezeigt |
| Phase 2: Rechnungsworkflow mit Prüfung und Freigabe | erfüllt (bestehender smart-invoice-Workflow) |
| Phase 3: 3 Mandanten und 5 Kreditoren, WEST fehlt | Kreditoren als Wertemenge Soll. Mandanten nicht belegt |
| Phase 3: automatische Mandantenzuordnung | nur verbal bestätigt |
| Phase 4: Mail an Alias → richtige Gesellschaft | Mailimport gezeigt, Alias nicht |
| Phase 4: Abrufintervall bekannt | offen |
| Phase 5: Beleg 01 zweistufig, 02 einstufig | nicht gezeigt |
| Phase 5: Benutzerwechsel | nicht gezeigt |
| Phase 6: U2 sieht keine Süd-Belege | nicht gezeigt |
| Phase 7: ≥ 4 Status im Rechnungseingangsbuch | erfüllt (Verteilung, sachliche Prüfung, Freigabe, Buchhaltung) [TR 00:26:35] |
| Phase 7: Schnellzugriff „über 10.000 Euro" | nicht belegt |
| Vorschlagswert übersteuern, nachvollziehbar | teilweise: manuelle Änderungen und Historie gezeigt [TR 00:29:19, 00:31:42] |
| Kreditorenakte Musterbau mit Vertrag, Auftrag, Rechnungen, Bescheinigung | nicht belegt. Gezeigt wurden Kreditorenakten Stadtwerke (Auftrag + ER) und Elektro Nordlicht (Auftragsbestätigung) [TR 00:55:02, 01:06:18] |
| Screenshot-Fallback je Schritt | offen |

### Bewusst weggelassen (KA §11, AR §7)

Eskalation nach X Tagen · Standard-Aufteilungsschlüssel je Gesellschaft · Liegezeit-Auswertung · Vier-Augen-Prinzip smart invoice · Kostenstelle mit Anteil · Omikron-Zahlungsauslösung (5.5 = N) · BIM4You (5.3 = N) · Property-Manager-Übergabe (4.1 = N) · VOB-Kumulation/Einbehalte (5.2 = N) · Automatik Freistellungsbescheinigung (2.7 = A) · DATEV-Übergabe live (5.1) [Quelle: KA §11; AR §7].

---

## 7 Abweichungen: Architektur-Soll gegenüber Instanz- und Cloud-Realität

| # | Thema | Soll lt. Architektur-Doc (AR) | Realität / Korrektur | Konsequenz fürs Produktivkonzept |
|---|---|---|---|---|
| 1 | Instanz | „lokale d.velop-Instanz", „Bühne", Aufbau nach eigener Planung (AR §1) | Geteilter, **produktiv genutzter Cloud-Tenant** (102 Belege, aktiver Workflow, 4 si_-Gruppen), nur additive Änderungen erlaubt [KW-03; CP §0] | Eigener Livos-Tenant (plus Test-/Abnahme-Tenant). Keine Präfix-Krücken. Änderungen mit Change-Protokoll |
| 2 | Begriff | „Dokumentarten", „Aktentypen" (AR §3.3, §3.5) | Cloud-UI: **Kategorien** mit Typ **Dokumentart** oder **Aktenart**; **Eigenschaften** statt „erweiterte Eigenschaften" [LM; KW-23; B03 §8a] | Konzept durchgängig in Cloud-Begriffen schreiben. „Geld" heißt „Währung" |
| 3 | Umfang Eigenschaften | 18 Zeilen, nur Eingangsrechnung (AR §3.4) | **26** Eigenschaften, verteilt auf 9 Kategorien. Zusätzlich Vertragsnr., Auftragsnr., Betreff, Absender, Dokumentdatum, Gültig bis; Netto/Steuersatz/Steuer/Brutto einzeln [CP §3] | Eigenschaftskatalog über **alle** Dokumentklassen planen, nicht nur die ER |
| 4 | Typ „Auswahlliste" | Gesellschaft, Kreditor, Objekt, Gewerk, Sachkonto = „Auswahlliste" (AR §3.4) | Kein Datentyp: **Text + Vordefinierte Werte (Wertemenge)** [KW-16; KA §5.2] | Zuerst Wertemengen, dann Eigenschaften. Pflege der Wertemengen klären (statisch oder aus Stammdaten) |
| 5 | Betragstypen | Netto/Steuersatz/Steuer/Brutto = „Zahl"; Sicherheitseinbehalt „Zahl" (AR §3.4) | Netto, Steuer, Brutto, Sicherheitseinbehalt = **Währung**; Steuersatz = **Zahl** [KW-21] | Beträge immer als Währung. In Workflowbedingungen Cent-Logik beachten [KA §8] |
| 6 | Kostenstelle | „Kostenstelle mit Anteil", Mehrfachfeld, Pflicht (AR §3.4) | Gibt es nicht. **Kostenstelle = Text + Wertemenge, „Mehrere Werte", Pflicht**. Anteil nur in smart-invoice-Positionen [KW-17; LM; KA §5.2] | Kostenstellensplit (Katalog 2.8) in smart invoice (Kontierungszeilen) konzipieren, nicht im DMS-Index |
| 7 | Ja/Nein-Felder | Reverse Charge § 13b, FSB geprüft = „Ja / Nein" (AR §3.4) | Kein Boolean. **Text + Wertemenge „Livos Ja Nein"**. Name ohne „§": „Reverse Charge 13b" [KW-14; KW-18] | Ja/Nein-Wertemenge als Standardbaustein. Sonderzeichen in Namen vermeiden |
| 8 | Status | „Status, systemgesteuert, Pflicht" als Eigenschaft (AR §3.4) | **Kein Status-Feld**; `Workflowstatus` existiert, der Workflow steuert [KW-22] | Status nie als Indexfeld modellieren. Auswertung über Rechnungseingangsbuch / Workflowstatus |
| 9 | Fälligkeit / Liegezeit | „Fälligkeit: Liegezeit und Eskalation" (AR §3.4); Kacheln „Länger als 3 Tage", „Top 10 nach Liegezeit" (AR §4) | Eigenschaft heißt **Fälligkeitsdatum**. **Liegezeit ist nicht belegbar** [KW-20; LM; B00 AB]. Im Tenant: Fälligkeitsampel 10/5 Tage [TR 01:03:34] | Katalog 3.2 „Liegezeit" mit Vorbehalt. Ersatz: Ampel/Sortierung. Echte Durchlaufzeit-Analyse über externe App/BI [TR 00:36:13–00:37:01] |
| 10 | Pflichtfelder ER | Pflicht: Gesellschaft, Kreditor, Rechnungsnr., Rechnungsdatum, Netto/Steuersatz/Steuer/Brutto, Fälligkeit, Objekt, Kostenstelle, Belegart, Status (AR §3.4) | Pflicht: Gesellschaft, Kreditor, Rechnungsnummer, Rechnungsdatum, **Nettobetrag, Bruttobetrag** (Steuersatz/Steuerbetrag optional), Fälligkeitsdatum, Objekt, Kostenstelle, Belegart; **kein Status** [KW-32] | Pflichtfeldmatrix je Kategorie bewusst schlank halten und auf automatisch befüllbare Felder beschränken |
| 11 | Belegart-Werte | Normal / Abschlag / Schluss (AR §3.4; KA §5.1) | **Normal · Abschlagsrechnung · Schlussrechnung · Gutschrift** [KW-11] | Wertelisten mit dem Fachbereich finalisieren (z. B. Gutschrift, Stornorechnung) |
| 12 | Gesellschaftsschlüssel | Kürzel NORD/SUED/BAUP (AR §3.1; KA §5.1) | Wertemenge mit **ausgeschriebenen Firmennamen** [KW-07]. smart invoice arbeitet mit Mandanten-id/-name [KA §6] | Bei > 100 Gesellschaften: führender Schlüssel = Mandanten-ID (DATEV-Mandantennr.) plus Anzeigename. Pflege automatisieren (API) |
| 13 | Kreditor | „Auswahlliste" (AR §3.4) | Statische Wertemenge mit 5 Namen [KW-08]. Im Tenant existiert bereits „Kreditor" (smart invoice) → Dublette „(Livos)" [KW-16] | Keine statische Kreditoren-Wertemenge. Kreditor aus den smart-invoice-/DATEV-Stammdaten, mandantenübergreifende Lieferantennummer [TR 00:09:16–00:11:39 Thomas Gross] |
| 14 | Dubletten | nicht betrachtet | Tenant hat bereits Kreditor, Rechnungsnummer (2×), IBAN, Belegart, Rechnungsdatum, Nettobetrag, Bruttobetrag [CP §1]. Livos-Varianten mit „(Livos)" [KW-16/19/21] | Eine Eigenschaft je Fachbegriff. Die smart-invoice-Eigenschaften wiederverwenden bzw. per Mapping verbinden |
| 15 | Akten | Drei Aktentypen als „Sichten, keine Ablageorte" (AR §3.5) | 3 Aktenarten mit Eigenschaften. Zusätzlich eine Akten-Dokumentart-Zuordnung und **Unterakten je Kreditor**; Mehrfachablage belegt [TR 00:55:02, 01:06:18]. Klickweg ohne Schritt für diese Zuordnung (Kap. 4.3) | Aktenplan (Ebenen, zulässige Dokumentarten, Erkennungs-/Pflichtfelder) als eigenes Konzeptkapitel. Livos muss die „Folder Structure" liefern [TR 00:57:22] |
| 16 | Minimum-Akten | Gesellschaftsakte NORD, Kreditorenakte Musterbau, Objektakte BV Hafenstraße 22 (AR §3.5) | Gezeigt: Kreditorenakten Elektro Nordlicht GmbH und Stadtwerke Beispielstadt AG, eine Objektakte [TR 00:55:02, 01:06:18]. Musterbau und Gesellschaftsakte nicht gezeigt | — (Demo-Thema) |
| 17 | Benutzer/Rollen | U1–U5 mit Rollen, U1+U3 „härteste Abhängigkeit" (AR §3.2) | Nicht angelegt (Verbot 3, LM). Im Termin nur ein handelnder Benutzer, kein Benutzerwechsel [TR 00:25:25, 00:29:54] | Rollen-/Gruppenmodell (Buchhaltung, sachl. Prüfer, Freigeber je Stufe, Externe, Admin) im Konzept ausspezifizieren. Cloud-Usermanagement verifizieren |
| 18 | Workflows W1–W6 | Eigene Workflows (Standard, 2. Stufe > 10.000 €, Klärfall, Eskalation, Vertretung, Fremdverwaltung) (AR §3.6) | Bestehender smart-invoice-Workflow Verteilung → sachliche Prüfung → Freigabe → Buchhaltung. Keine Livos-Workflows gebaut (Verbot 2). Vertretung per Abwesenheitsstatus [TR 01:05:00]. Eskalation nur verbal [TR 00:25:05] | Workflowdesign auf dem smart-invoice-Best-Practice-Workflow aufsetzen: Freigabeverbindung mit Betragsgrenze (Cent, top-down), Clearing für Klärfälle, Vertretungsregeln |
| 19 | Freigabegrenze | 10.000 € **brutto** (AR §3.6) | KA-Bedingung nutzt `voucher.net_amount` (**netto**) [KA §8]. Nicht umgesetzt | Grenze fachlich festlegen (netto oder brutto) und mit dem passenden Feld umsetzen |
| 20 | Berechtigungen R1–R3 | U1 alle Gesellschaften, U2 nur NORD + 1 Objekt, U3 alles/freigeben (AR §3.7) | Nicht umgesetzt. Cloud-Berechtigungsoberfläche ungeprüft [KA §9.2; B03 Nr. 7] | Mandantentrennung (Katalog 1.1) als Muss-Thema: Cloud-Mechanismus mit d.velop verifizieren (Service-Portal-Zugang) |
| 21 | Dashboards | 3 rollenbezogene Dashboards mit 12 fachlichen Kacheln (AR §4) | **Nur 4 Standard-Widgets**, kein Filter-Widget. Managementsicht im Rechnungseingangsbuch [LM; KA §10; B00 AF: 2 von 12 Wünschen belegt] | Dashboard = Einstieg (Standard-Widgets + Verknüpfungs-Widget). Steuerung im Rechnungseingangsbuch (eigene Schnellzugriffe). Weitergehendes über BI/Middleware |
| 22 | Mandantenerkennung | Gesellschaftstabelle mit Steuernummer; Unterscheidung NORD/BAUP (AR §3.1; TD-LIESMICH „unterscheiden sich nur über Steuernummer und USt-IdNr") | Erkennung über **Name + Anschrift** [LM; KA §6]. Katalog 2.2 braucht einen Vorbehalt [LM] | Gesellschaften mit gleicher Anschrift: Alias-Postfächer je Gesellschaft bzw. manuelle Qualifizierung einplanen. Trefferquote als offene Frage |
| 23 | Mail-Eingang | „Testpostfach", Beleg 01 live per Mail (AR §2, §5) | 3 bestehende Postfächer („Invoices" u. a.) mit zugelassenen Absendern. Live-Mail gesendet. Aliasse nicht belegt [TR 00:49:33–00:53:32] | Postfachkonzept: je Gesellschaft/Belegklasse ein Alias mit Importprofil und Schlüssel-Wert-Paar. Absender-Whitelist. Abrufintervall messen |
| 24 | Datenbestand | Belege 02–07, 09 in Zielzuständen; 01 und 08 live; Nachweise 20–24 in Akten (AR §5) | Keine Testdaten importieren (Verbot 4, LM). Im Termin: 3 Rechnungen live hochgeladen, 1 Auftragsbestätigung live abgelegt, Bestand 226 Rechnungen aus anderen Tests [TR 00:01:20, 00:25:25, 00:53:32]. Klärfall WEST nicht gezeigt | — (Demo-Thema). Für die Produktivabnahme: Testdatenset mit Klärfall, Gleich-Anschrift-Fall und E-Rechnung |
| 25 | Schreibweisen | Umlaute (Süd, Hafenstraße) in AR/KW | Testdaten in ASCII (Sued, Hafenstrasse); KA §6.1 „Süed". Auflösung offen [LM] | Schreibweisen-Normierung der Stammdaten (eine führende Quelle, UTF-8) als Datenqualitätsregel |
| 26 | Kostenstellen im Testbeleg | Beleg 03 „Aufteilung auf Kostenstellen" (AR §5) | Beleg nennt „Haus A 55 % / Haus B 45 %"; die Wertemenge enthält nur KST-1000 bis KST-3000 [TD; KW-13] | Kostenstellenstamm aus DATEV übernehmen, nicht frei erfinden |
| 27 | smart-invoice-Gruppen | KA: 7 dv_-Gruppen (KA §4) | Tenant: **vier si_-Gruppen** [KW-03] | Gruppennamen und Mandantenbezug der smart-invoice-Gruppen am Zielsystem erheben |
| 28 | Dokumentbearbeitung/Kürzung | nicht betrachtet | Bearbeitungsschritt in der Demo-Umgebung nicht vorhanden. Kürzung über Positionen / Beträge + Notiz [TR 00:41:44–00:43:06] | Kürzungs-/Korrekturprozess (inkl. E-Rechnung: Rückweisung statt Änderung [TR 00:46:54–00:47:29]) konzipieren |
| 29 | Grenzen | nicht betrachtet | Max. 89 Eigenschaften je Kategorie; Namen max. 50 Zeichen [KW-22; KW-06] | Bei der Eigenschaftsplanung berücksichtigen |

---

## 8 Lessons Learned für das Produktivkonzept: wie was in der Cloud-UI abzubilden ist

### 8.1 Modellierung (Dokumenten- und Aktenstrukturen)

1. **In Cloud-Begriffen spezifizieren.** Ort: `Konfiguration > Dokumentenmanagement > Verwaltung > Dokumenten- und Aktenstrukturen`. Objekte: **Wertemengen → Eigenschaften → Kategorien (Dokumentart/Aktenart)**. Position, Kürzel und Beschreibung gibt es nicht. Die Maskenreihenfolge ergibt sich aus der Reihenfolge der zugewiesenen Eigenschaften [KW-02, KW-15, KW-31].
2. **Reihenfolge der Anlage einhalten:** Wertemengen → Eigenschaften → Kategorien → Reihenfolge/Pflicht/Titel → Aktenstruktur → Berechtigungen → Import/Postfächer → smart invoice → Startseite [KW Teile 2–5; KA §5].
3. **Eine Eigenschaft je Fachbegriff, tenantweit.** Namen sind eindeutig (Dublettenablehnung). Die „(Livos)"-Dubletten aus der Demo dürfen **nicht** in die Produktion. Die smart-invoice-Eigenschaften (Mandant, Mandantenname, Kreditor, Kreditorname, Kostenstellen, Kostenträger, Sachkonten, Beträge, Rechnungsnummer/-datum, Belegart, Workflowstatus) sind als führend zu übernehmen und fehlende Livos-Felder zu ergänzen (Objekt, Gewerk/Los, Sicherheitseinbehalt, Reverse Charge, FSB geprüft, Gültig bis, Vertrags-/Auftragsnummer, Betreff, Absender, Dokumentdatum). Das ist genau die KA-Empfehlung „erst schauen, dann bauen" [KA §4], die in der Demo nicht umgesetzt wurde.
4. **Konkurrierende Paare auflösen:** Gesellschaft ↔ Mandant/Mandantenname · Kostenstelle ↔ Kostenstellen · Sachkonto ↔ Sachkonten · Steuerbetrag ↔ MwSt Betrag. Je Paar ein führendes Feld festlegen und ggf. über „Zuordnungen / Mappings" verbinden [B03 §8b] (**Annahme:** das Mapping-Feature ist dafür geeignet; zu verifizieren).
5. **Datentypen nach Cloud-Katalog:** Text, Zahl, Währung, Datum, Datum-und-Zeit. Beträge als Währung. Ja/Nein als Text + Wertemenge „Ja/Nein". Auswahllisten als Text + Vordefinierte Werte. Mehrfachwerte über „Anzahl der Werte: Mehrere Werte" [KW-14 bis KW-21].
6. **Wertemengen nur für stabile, kleine Listen** (Belegart, Gewerk, Ja/Nein, ggf. Objektstatus). **Gesellschaften (> 100), Kreditoren, Kostenstellen, Sachkonten** nicht als statische Wertemengen pflegen. Sie kommen aus DATEV/Middleware bzw. den smart-invoice-Stammdaten (API) [B03 §8d]. Ob Wertemengen in der Cloud dynamisch befüllbar sind: **offen**.
7. **Pflichtfelder je Kategorie schlank halten.** Pflicht sind nur Felder, die automatisch befüllt werden oder die Aktenbildung und Berechtigung tragen (Gesellschaft, Kreditor, Objekt). Eine Maske voller Pflichtfelder blockiert den Import [KW-32]. Laut Doku entsteht bei leeren Erkennungseigenschaften keine Akte [B03 §7d].
8. **Titelregeln je Kategorie** per `T > Titel bearbeiten` definieren. Muster aus der Demo: Rechnungen „Kreditor, Rechnungsnummer, Bruttobetrag", Verträge/Aufträge „Kreditor + Nummer", Korrespondenz „Betreff, Dokumentdatum", Akten „Schlüsselfeld" [KW-33].
9. **Aktenplan als eigenes Konzeptkapitel.** Aktenarten (Gesellschafts-, Kreditoren-, Objektakte, ggf. Vertrags-/Projektakte), Hierarchie (höchstens 4–5 Ebenen [TR 00:57:22]), zulässige Dokumentarten je Akte [TR 00:55:02], Erkennungsfelder, Mehrfachablage („Sichten, keine Ablageorte" [KW-30]). Den Cloud-Klickweg für die Akten-Dokumentart-Zuordnung am System dokumentieren, denn er fehlt im Klickweg.
10. **Kein Status-Feld.** Den Status liefern Workflow/`Workflowstatus`. Status- und Fälligkeitsauswertung im Rechnungseingangsbuch [KW-22; KA §10].

### 8.2 Prozesse, Rechte, Oberfläche

11. **smart invoice als Prozesskern.** Workflow Verteilung → sachliche Prüfung → Freigabe → Buchhaltung ist vorhanden und im Termin akzeptiert [TR 00:29:54–00:34:11]. Livos-Varianten (Betragsgrenze, Hausverwaltungsfälle, Klärfall/Clearing, Vertretung) als Verbindungen und Schritte im smart-invoice-Workflow konfigurieren. Beträge in Cent, top-down-Reihenfolge der Verbindungen [KA §8].
12. **Kostenaufteilung** (Katalog 2.8) ausschließlich über smart-invoice-Belegpositionen/Kontierungszeilen [KW-17; TR 00:43:06].
13. **Mandantentrennung und Berechtigungen** sind das Risiko Nr. 1: Die Cloud-Oberfläche ist in der Recherche ungeprüft [KA §9.2; B03 Nr. 7]. Vor dem Konzeptabschluss mit d.velop bzw. über den Service-Portal-Zugang klären. On-Prem-Konstrukte (@D3GROUP, Hooks) nicht ungeprüft übertragen [B03 §8c].
14. **Startseite realistisch planen:** Standard-Widgets (Suche, Zuletzt bearbeitet, Beobachtet, Favorisiert) plus Rechnungseingangsbuch-Widget plus Verknüpfungs-Widgets. Rollensicht über „Sichtbarkeit von Widgets" (keine Sicherheitsfunktion). Managementkennzahlen (Liegezeit, Volumen je Gesellschaft, Durchlaufzeiten je Benutzer) über das Rechnungseingangsbuch oder externe BI (Evidanza/Middleware, offen) [LM; KA §10; TR 00:36:13–00:37:01].
15. **Posteingang:** ein physisches Postfach mit Alias je Gesellschaft bzw. Dokumentklasse, je Alias ein Importprofil mit Schlüssel-Wert-Paar (Gesellschaft) und Standardkategorie. „Zugelassene E-Mail-Adressen" restriktiv setzen [KA §7.4; B06; TR 00:49:33]. Abrufintervall im Zielsystem messen und dokumentieren.
16. **Stammdatenführung:** mandantenübergreifende Lieferantennummer mit Referenz auf die DATEV-Kreditorennummer je Mandant [TR 00:08:01–00:11:39 Thomas Gross]. Mandantennamen exakt wie auf den Rechnungen [KA §6]. Einheitliche Schreibweise (Umlaute) [LM].

### 8.3 Vorgehen und Betrieb

17. **Eigener Livos-Tenant plus Test-Tenant.** Den geteilten MDIS-Demo-Tenant nicht weiterverwenden. Namenspräfixe und Löschlisten waren Schutzmaßnahmen für einen Fremd-Tenant [KW-03; KW-04].
18. **As-built-Protokoll ist Pflicht.** Der 7-Punkte-Bericht aus Aufgabe 2 (Inventur, Angelegt, Umbenannt, Nicht geschafft, UI-Abweichungen wörtlich, Unerwartetes, Bestätigung) ist ein gutes Muster für die Produktivabnahme. In der Demo liegt er **nicht vor** [KW-34; CP §5].
19. **UI-Begriffe am System verifizieren, nicht aus Doku ableiten.** Die KA enthielt On-Prem-Pfade und -Felder (Dokumente und Akten > …, Position, Kürzel, Länge), die es in der Cloud nicht gibt [LM; KA §5 vs. KW-15].
20. **Aufbewahrung/Löschkonzept (GoBD) separat konzipieren.** In der Demo nicht behandelt. Laut Doku über d.ecs storage manager/Retention und „Aktivitäten" als Änderungsprotokoll [B00 T; KA §2.1]. Cloud-Konfigurationsweg offen.
21. **Konfiguration für 100+ Gesellschaften automatisieren:** DMS-API zur Repository-Konfiguration und smart-invoice-Stammdaten-API [B03 §8d]. Grenzen beachten: 89 Eigenschaften je Kategorie, Namen ≤ 50 Zeichen [KW-22; KW-06]. Obergrenzen für Wertemengen-Einträge, Gruppen und Berechtigungsobjekte sind undokumentiert [B03 Offene Punkte Nr. 2].

---

## 9 Offene Punkte (Sammelliste)

| # | Offener Punkt | Klärung durch |
|---|---|---|
| O1 | Abschlussbericht Aufgabe 2 (Löschliste, tatsächliche Namen mit „(Livos)", Fehlermeldungen, UI-Abweichungen, Inventur-Datentypen) | Durchführende Person / Chrome-Plugin-Protokoll |
| O2 | Wurden alle 9 Kategorien angelegt? Belegt sind nur Livos Auftrag, Livos Kreditorenakte, Objektakte (und Eingangsrechnung erwähnt) | Blick in den Tenant |
| O3 | Brauchte „Rechnungsdatum" den Zusatz „(Livos)"? (Inventur: bestehend; KW-20: kein Hinweis) | Tenant |
| O4 | Wo und wie wurde die Akten-Dokumentart-Zuordnung (inkl. „Angebote") in der Cloud-UI konfiguriert? | Tenant |
| O5 | Umlaut-/ASCII-Entscheidung Wertemengen gegenüber Testbelegen | MDIS |
| O6 | Sind die im Termin gezeigten Sachkonten/Kostenstellen smart-invoice-Stammdaten oder die DMS-Wertemengen? Wurden dafür Änderungen in smart invoice gemacht (Konflikt mit Verbot 2)? | MDIS |
| O7 | Cloud-Pfade für Benutzer, Gruppen, Berechtigungen, Aufbewahrung | d.velop / Service Portal |
| O8 | Freigabegrenze netto oder brutto | Livos-Fachbereich |
| O9 | Abrufintervall des Mailimports | Messung am Zielsystem |
| O10 | Dynamische Wertemengen und Obergrenzen in der Cloud | d.velop |
| O11 | Sind „(Livos)"-Klammern und „&" in Namen und Werten zulässig (On-Prem nur `+ - _`)? | Tenant |
| O12 | Ist nach Kategorieänderungen in der Cloud eine Neuanmeldung der Benutzer nötig (On-Prem: ja)? | Tenant |
