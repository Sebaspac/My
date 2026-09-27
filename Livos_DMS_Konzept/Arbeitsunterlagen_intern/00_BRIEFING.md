# BRIEFING für alle Subagents — Projekt „Livos d.velop DMS-Gesamtkonzept"

## Kontext
- Wir sind **MDIS Consulting** (Beratungshaus, d.velop-/ERP-Partner). Kunde: **Livos** (Immobilien-/Bau-Unternehmensgruppe mit >100 Gesellschaften, ~80 Anwender intern+extern, 5.000–8.000 Eingangsbelege/Jahr).
- Livos will ein DMS auf Basis **d.velop** (Cloud: d.velop documents / d.3one, smart invoice, process studio, inbound/Postverteilung, ggf. d.velop contract etc.).
- Es gab am 22.09.2026 einen Demo-Workshop auf der Demo-Instanz `mdisconsulting.d-velop.cloud`. Teilnehmer MDIS u.a.: Thomas Groß (CEO), Valeria Filimonow (Sales), Annalena Groß (ERP Consultant), André Töpper (vermutl. d.velop/Consultant – aus Transkript verifizieren).
- Ziel des Gesamtprojekts: ein **ganzheitliches DMS-Konzept** für Livos. Drei Enddokumente: (1) Zusammenfassung/Fazit, (2) vollständiges Konzept, (3) Konzept als draw.io (alle Sichten/Masken).
- Sprache aller Arbeitsergebnisse: **Deutsch**. Sachlich, präzise, mit Quellenangaben.

## Quellen (alle als Text vorbereitet) — Verzeichnis: SP/txt
SP = /tmp/claude-0/-home-user-My/9b9087bc-2d0b-5088-b7bc-148ecd5c6c69/scratchpad
- A_Leistungskatalog_Rechnungsmanagement_xlsx.txt — Anforderungskatalog von Livos (29 Anforderungen, Prioritäten, Erfüllungsgrade)
- A_Livos_DMS_Business_Architektur_pdf.txt — MDIS-Folien Zielarchitektur (Bilder: SP/img/arch_1..5.png — ansehen!). Kernaussagen: d.velop zentral für Eingangsrechnungen, Verträge, Post. DATEV = operatives FiBu-System (ER-Journale, Zahlungsjournale, Sonderbuchungsinfos ARAP/PARP, Rückstellungen, Anzahlungen → DATEV; Zahlungsrückmeldung ← DATEV). Bim4You (Bau-Projektsteuerung): ER-Journale →, Einbehalt-/Kürzungsinfos, Umlageinfos, Freigabestatus ←. ER-Prozess: Eingang → Verarbeitung & Vorqualifikation → Verteilung (DATEV: ER-Vorerfassungsjournal) → Fachliche Prüfung/Detailqualifikation (Bauprojekt-Rechnungen an Bim4You: Budgetabgleich, Bearbeitung) → Fachliche Freigabe (DATEV: Verbuchung) → Zahlungsfreigabe (DATEV: Zahlungsdurchführung). Verträge: Eingang → Verarbeitung → Verteilung → Klassifizierung → Fachliche Freigabe → Archivierung. Post: Eingang → Verarbeitung → Klassifizierung → Verteilung → Archivierung.
- A_Agenda_Livos_pptx.txt — Workshop-Agenda inkl. Katalognummern und offene Fragen (Mandantenmodell, Trefferquote, Ad-hoc-Freigabe ohne Lizenz, DATEV-Frequenz, Omikron, Lizenz/Mengengerüst)
- A_06_Architektur_Demo-Instanz.txt — Architektur der Demo-Instanz (Gesellschaften, Rollen, Kategorien, Eigenschaften, Akten, Workflows W1–W6, Berechtigungen R1–R3, Dashboards, bewusst nicht Eingerichtetes)
- A_05_Konfigurationsanleitung.txt — Konfigurationsphasen der Demo
- 04_Chrome-Prompt_Aufgabe-2.md — tatsächlich angelegte Struktur: 8 Wertemengen, 26 Eigenschaften, 9 Kategorien
- 00_LIESMICH_Zuerst-lesen.md — Workshop-Readme inkl. Korrekturen (kein Ja/Nein-Datentyp; „Kategorien" statt Dokumentarten; 3.2 Liegezeit nicht belegbar; 2.2 Mandantenerkennung nur über Name/Anschrift)
- A_01_Klickweg_36_Schritte_pdf.txt + Bilder SP/img/klickweg/*.png — 36 Screenshots der Konfiguration in der echten Cloud-Instanz
- A_07_Testdaten_alle.txt, A_07_Testdaten_LIESMICH.md — Testbelege, Stammdaten Gesellschaften/Kreditoren
- B_00_BEFUNDE_konsolidiert.md … B_06_Postverteilung_Mailimport.md — allgemeine d.velop-Recherche (aus ~310 Handbüchern): Anwendersicht, smart invoice, Administration/Berechtigungen, process studio/Workflows, Postverteilung/Mailimport
- C_Transkript_Livos_Demo.txt — Transkript des Demo-Termins mit Livos (Sprecher + Zeitstempel). WICHTIGSTE Quelle für Kundenanforderungen, Fragen, Einwände, Zusagen.
- Zusätzlich: SP/mocca/ — Acumatica-ERP-Snapshot „Mocca_V14_108" (527 .adb-XML-Tabellen, Customization „ConnectorX360dvelop.2.3.2"), Relevanz unklar.

## Arbeitsregeln
- Schreibe Ergebnisse als Markdown in SP/work/<vorgegebener Dateiname>.
- Jede Aussage mit Quelle: [Quelle: Datei, Abschnitt/Zeitstempel]. Transkript immer mit Zeitstempel [hh:mm:ss] und Sprecher.
- Trenne strikt: **Fakt (belegt)** / **Annahme** / **offene Frage**.
- Keine Erfindungen. Wenn etwas nicht belegt ist, als offen markieren.
- Keine Dateien außerhalb SP/work ändern.

## Erkenntnisse aus dem Transkript (vom Lead-Auditor, Kurzfassung für Rechercheure)
- Teilnehmer Livos: André Töpper (Projektleitung Kunde), Christian Weigel, Tanja Brecht, Sprecher „Trius" (vermutl. Buchhaltungsdienstleister „Trios", bucht in DATEV). MDIS: Thomas Groß (CEO), Valeria Filimonow (Sales), Sebastian Pachon (Consultant, Präsentator), Annalena Groß (ERP-Consultant).
- DATEV ist führendes FiBu-System; Buchhaltung macht Dienstleister „Trios"; DATEV läuft bei einem externen Dienstleister (Zugriff über dessen Cloud, eingeschränkte Auswertmöglichkeiten).
- Kreditoren: gleiche Lieferanten in vielen Gesellschaften mit unterschiedlichen Kreditorennummern; interne Kreditoren 70000er-Kreis, Kreditoren aus Hausverwaltungen 80000er-Kreis; keine Konsolidierung. MDIS-Vorschlag: zentrale Lieferanten-Stammdaten-App (MDIS-„Middleware"/App, existiert bei Livos bereits für Stammdaten) mit Konsolidierungsnummer, Referenz auf DATEV-Kreditorennummer je Mandant; KI-gestützte Konsolidierung als kostenloser PoC.
- ~10 Property Manager (Hausverwaltungen) buchen ~95 % ihrer Rechnungen selbst; Rechnungen über Schwellwert brauchen Freigabe durch Livos Asset Management → Vorschlag: eigenes Postfach „Freigabe-Rechnungen" in d.velop, reiner Freigabe-Workflow ohne Buchung/Zahlung, Freigabe-Mail zurück an Hausverwalter.
- Kundenfragen im Termin: IBAN-Abgleich Rechnung vs. Stammdaten; Fälligkeit aus Beleg vs. Stammdaten; Liegezeit-/Durchlaufzeit-Auswertung je Benutzer/Schritt (MDIS sagte: nicht in d.velop, über eigene App/Evidanza-BI); Rückweisung mit 5 Standardgründen + automatischer E-Mail an Lieferanten (MDIS sagte: nicht direkt in d.velop, über Middleware); Kürzungen von Rechnungen auch positionsweise (MDIS sagte: möglich „lokal"); kumulierte Abschlagsrechnungen automatisch gegen bereits Gezahltes prüfen (offen); E-Rechnung-Korrektur nur per Rückweisung; Freistellungsbescheinigung-Abgleich beim Kreditor; Vertretung auch durch Admin für erkrankte Kollegen; Aktenebenen (Empfehlung 4–5); Lizenz nach Akten/Speicher?; KI-Fragen an Vertragsinhalte (MDIS: über eigene KI-Plattform); Evidanza-Anbindung; Freigaben für Ausbuchungen auf Mietkonten als weiterer Workflow; Dublette annehmen nur mit Begründung.
- Nächste Schritte: Angebot für ~80 Nutzer mit Bezug auf Leistungskatalog; Livos vergleicht mehrere Anbieter, Entscheidung mit Management; Prozessworkshop 2–3 h; KI-Plattform-Demo/PoC.
