# 02 – Anforderungen & Zielbild Livos (Konsolidierung der Kundendaten)

Stand: 26.09.2026 · Arbeitspaket „Anforderungen / Zielbild" · **ohne** Transkript (wird separat ausgewertet)

**Kennzeichnung:** **[F]** = Fakt, in der Quelle belegt · **[A]** = Annahme / eigene Ableitung · **[O]** = offene Frage

**Quellenkürzel** (alle unter `SP/txt/`, Originale unter `SP/src/livos/Livos/`):

| Kürzel | Datei | Zitierweise |
|---|---|---|
| KAT | `A_Leistungskatalog_Rechnungsmanagement_xlsx.txt` (Original: `Kopie von 260715_Leistungskatalog_Rechnungsmanagement_.xlsx`) | Blatt + Zelle bzw. Anforderungs-ID |
| ARCH | `A_Livos_DMS_Business_Architektur_pdf.txt` + `SP/img/arch_1..5.png` (Original: `Livos_DMS_Business Architektur.pdf`) | Folie 1–5 |
| AG | `A_Agenda_Livos_pptx.txt` (Original: `20250404_Agenda Livos.pptx`) | Folie 1–4 |
| A06 | `A_06_Architektur_Demo-Instanz.txt` (inhaltsgleich in allen drei docx-Fassungen, geprüft) | Kapitel |
| TD | `A_07_Testdaten_alle.txt` | Dateiname des Testbelegs |
| TDL | `A_07_Testdaten_LIESMICH.md` | Abschnitt |
| LM | `00_LIESMICH_Zuerst-lesen.md` | Abschnitt |
| A05 | `A_05_Konfigurationsanleitung.txt` (nur ergänzend für Kap. 8) | Kapitel |
| CP | `04_Chrome-Prompt_Aufgabe-2.md` (nur ergänzend für Kap. 5/8) | Abschnitt |
| B00 | `B_00_BEFUNDE_konsolidiert.md` (nur ergänzend für Kap. 8) | Abschnitt (Buchstabe) |
| META | Eigene Auswertung der Original-Dateien (xlsx-XML, PDF-/pptx-/docx-Metadaten, eingebettetes XML, IBAN-Prüfziffern) | – |

---

## 0 Kurzfassung (Kernaussagen)

1. **Livos** ist eine Immobilien-/Bau-Gruppe („LIVOS Gruppe") mit **über 100 Gesellschaften** in den Segmenten **Bestand, Privatisierung, Bau**, **ca. 80 Anwendern (intern & extern)** und **ca. 20–30 Rechnungen/Tag (5.000–8.000/Jahr)** [F: KAT Übersicht C5–C7; ARCH Folie 1].
2. Der Katalog ist eine **Softwareauswahl „Digitales Rechnungsmanagement"** mit **29 Anforderungen** (21 Must, 4 Should, 4 Could). MDIS hat 19× S, 3× K, 0× A, 3× N eingetragen, **4 Zeilen sind leer** (4.2, 5.3, 5.4, **5.5 – ein Must-Have**) [F: KAT].
3. **Kritische Must-Haves:** 4.1 Property-Manager-Prozess (**N**), 5.5 Omikron-Zahlungsauslösung (**leer**), 3.2 Liegezeit (S nicht belegbar), 2.2 Mandantenerkennung „anhand Steuernummer" (S nur mit Vorbehalt), 2.8 Standardschlüssel je Gesellschaft (S fraglich) [F: KAT; LM; B00 AB/AI/AM].
4. Die **MDIS-Zielarchitektur** geht über den Katalog hinaus: d.velop als Drehscheibe für **Eingangsrechnungen, Verträge und Post**; **DATEV** als operatives FiBu-System (ER-/Zahlungs-Journale, Sonderbuchungsinfos → DATEV; Zahlungsrückmeldung ←); **Bim4You** als bidirektionale Bau-Integration (ER-Journale →; Einbehalt-/Kürzungs-, Umlageinfos, Freigabestatus ←) [F: ARCH Folie 2–5].
5. **Omikron und die Property Manager kommen in der Zielarchitektur nicht vor**; die Folien sagen „Zahlungen werden über DATEV ausgelöst" – der Katalog fordert die Auslösung über Omikron [F: ARCH Folie 2; KAT 5.5].
6. **Verträge und Post** haben **keine eigene Katalog-Anforderung** (nur 1.7 „Nachweise anhängen", 6.1 „DMS-Möglichkeit" als Could) – das Zielbild erweitert den Scope deutlich [F/A].
7. Die Testdaten (fiktiv) belegen reale Bau-/Immobilien-Sonderfälle: **§ 13b UStG, kumulierte VOB-Abschlagsrechnungen, 5 % Sicherheitseinbehalt, Freistellungsbescheinigung § 48b EStG, XRechnung/ZUGFeRD, Kostenstellensplit 55/45, zwei Gesellschaften mit identischer Anschrift, unbekannte Gesellschaft** [F: TD, TDL].
8. In den Testdaten stecken **eigene Fehler** (ungültige IBANs in beiden E-Rechnungen, rechnerisch nicht herleitbarer Sicherheitseinbehalt, Dubletten 09/02 und 10/01, Rahmenvertrag der NORD für Auftrag der SUED, §13b-Logik widersprüchlich) – als Prüffälle wertvoll, als „Demo-Wahrheit" riskant [F: META, TD].
9. Das Demo-Architekturdokument (A06) ist in mehreren Punkten von der Cloud-Realität überholt (kein Ja/Nein-Typ, keine „Kostenstelle mit Anteil", nur 4 Standard-Widgets, Managementsicht gehört ins Rechnungseingangsbuch, Mandantenerkennung nicht über Steuernummer) [F: LM; A05; B00].

---

## 1 Unternehmensprofil Livos

### 1.1 Identität, Branche, Geschäftsmodell

| Merkmal | Inhalt | Typ | Quelle |
|---|---|---|---|
| Name / Auftritt | „LIVOS Gruppe" (Logo auf der Titelfolie „DMS-Kernprozesse") | F | ARCH Folie 1 (arch_1.png) |
| Branche | Immobilien- und Bau-Unternehmensgruppe; Gesellschaften in den Segmenten „Bestand, Privatisierung, Bau" | F | KAT Übersicht C5 |
| Segment „Bestand" | Bestandshaltung von Immobilien; ein Teil der Assets ist „rein verwaltet" und wird von **externen Property Managern** mit „autarken Systemen/Prozessen" betreut | F (Property Manager) / A (Deutung „Bestand" = Vermietung) | KAT 4.1, 5.4 |
| Segment „Privatisierung" | Vermutlich Wohnungsprivatisierung (Aufteilung, Einzelverkauf von Einheiten) | A | KAT Übersicht C5 |
| Segment „Bau" | Bauprojekte mit **Budgetcontrolling in BIM4You**, VOB-Abrechnung, Sicherheitseinbehalten, Freistellungsbescheinigungen, externen Projektsteuerern und Architekten | F | KAT 2.7, 4.2, 5.2, 5.3; ARCH Folie 3 |
| Verkauf von Gesellschaften | Protokolle/Unterlagen müssen „z.B. bei Verkauf je Gesellschaft auch exportiert und revisionssicher weitergegeben werden können" → Gesellschaften sind Transaktionsobjekte (vermutlich Objekt-/Projektgesellschaften im Share Deal) | F (Anforderung) / A (Share-Deal-Modell) | KAT 1.6 |
| Organisation | „dezentral/deutschlandweit verteilte Teams" | F | KAT 1.2 |
| Anlass | Softwareauswahl „Auswahl einer Software für Digitales Rechnungsmanagement"; Katalog „Erstellungsdatum: Juli 2026" (Dateiname 260715 → vermutlich 15.07.2026). Livos ist ausschreibende Partei, MDIS füllt als „Anbieter" die Spalten „Erfüllung Anbieter" und „Notizen" | F / A (Datum aus Dateiname) | KAT Übersicht B2–C9; META |
| Zielplattform | d.velop (Cloud) | F | ARCH Folie 2–5; LM |

### 1.2 Gesellschaftsstruktur

| Aussage | Typ | Quelle |
|---|---|---|
| „Über 100 Mandanten (Bestand, Privatisierung, Bau)" | F | KAT Übersicht C5; KAT 1.1 |
| Die realen Gesellschaftsnamen, Rechtsformen, Anschriften und Steuernummern sind **in keiner Quelle genannt**. Die Gesellschaften NORD/SUED/BAUP/WEST sind **erfunden** („Alle Firmen … sind erfunden") | F | TDL Kopf; A06 Kopf („fiktiver Kunde, Workshop-Szenario") |
| Mehrere Gesellschaften teilen sich dieselbe (Verwaltungs-)Anschrift | A (von MDIS unterstellt, nicht von Livos bestätigt) | AG Folie 4 (2.2); KAT Tabelle1 Zeile 2.2 |
| Rechnungen gehen auch an Gesellschaften ein, die (noch) nicht im System hinterlegt sind | F (als Anforderung) | KAT 2.3 |
| Gesellschaftsbestand ist dynamisch (Neugründungen, Verkäufe) | A | KAT 1.6, 2.3 |
| Konzernhierarchie (Holding, Zwischengesellschaften, Segment-Zuordnung je Gesellschaft) | O | – |
| Eigene Buchhaltung je Gesellschaft in DATEV (= ein DATEV-Mandant je Gesellschaft) | A | KAT Übersicht C5 verwendet „Mandanten" synonym zu Gesellschaften |

### 1.3 Mengengerüst

| Kennzahl | Wert | Typ | Quelle |
|---|---|---|---|
| Gesellschaften / Mandanten | über 100 | F | KAT Übersicht C5 |
| Anwender gesamt | ca. 80 (intern & extern) | F | KAT Übersicht C6; KAT 3.1 |
| Eingangsrechnungen | ca. 20–30 pro Tag, ca. 5.000–8.000 pro Jahr | F | KAT Übersicht C7 |
| Plausibilisierung | 20–30 × ca. 250 Arbeitstage ≈ 5.000–7.500 → konsistent | A | eigene Rechnung |
| Belege je Gesellschaft | Ø nur ca. 50–80 pro Jahr (5.000–8.000 / >100) → KI-Lernen je Mandant hat wenig Historie; Lernen muss kreditor- bzw. gesellschaftsübergreifend funktionieren | A | eigene Rechnung, Bezug KAT 2.5 |
| Aufteilung intern/extern der 80 Anwender | unbekannt | O | – |
| Volumen Verträge / Post | unbekannt (Zielarchitektur umfasst beides) | O | ARCH Folie 4–5 |
| Freigabegrenzen | Katalog nur „Vier-Augen-Prinzip ab Betrag X"; Demo nutzt 10.000 € | F (Demo-Wert) / O (Livos-Wert) | KAT 1.4; A06 3.6 |
| Eskalationsfrist | Katalog „mehr als X Tage", je Gesellschaft/Workflow; Demo 3 Tage | F (Demo) / O (Livos) | KAT 3.3; A06 3.6 |
| DATEV-Übergabefrequenz | „nicht nur pauschal 1x pro Tag" | F | KAT 5.1 |

### 1.4 Anwender und Rollen (aus dem Katalog)

| Rolle | Kontext im Katalog | Intern/Extern | Quelle |
|---|---|---|---|
| Buchhaltung | Rechtevergabe; (Demo: Rechnungseingang, Kontierung) | intern | KAT 1.5; A06 3.2 |
| Projektleiter | Rechtevergabe; sachliche Prüfung | intern | KAT 1.5 |
| Geschäftsführer | Rechtevergabe; Management-Überblick | intern | KAT 1.5, 3.2 |
| Abteilungsleiter | Management-Überblick; Eskalationsempfänger | intern | KAT 3.2, 3.3 |
| Gesellschafts-Verantwortliche | Management-Überblick je Gesellschaft | intern (A) | KAT 3.2 |
| Vertretung | Eskalations-/Vertretungsempfänger | intern | KAT 3.3, 3.4 |
| „Prüfer" | Visualisierung der E-Rechnungs-XML | intern (A) | KAT 2.4 |
| „berechtigte Nutzer" für Zahlungsauslösung | Zahlungen nach Freigabe auslösen | intern | KAT 5.5 |
| Externe Projektbeteiligte (Projektsteuerer, Architekten) | Ad-hoc-Freigabe per Mail/Link ohne Lizenz | extern | KAT 4.2 |
| Kern-Partner | standardisierter Web-Zugang: einsehen und freigeben | extern | KAT 4.3 |
| Property Manager | eigene autarke Systeme/Prozesse, kein interner Workflow | extern | KAT 4.1, 5.4 |

### 1.5 Systemlandschaft (Ist und Ziel)

| System | Rolle | Richtung / Schnittstelle | Katalog | Quelle | Status |
|---|---|---|---|---|---|
| **d.velop** (Cloud) | Zielsystem: zentrale Drehscheibe für Eingangsrechnungen, Verträge, Post | Hub zu DATEV und Bim4You | 1.2, 6.1 | ARCH Folie 2 | F |
| **DATEV** | „operatives FiBu-System"; ER- und Zahlungsbuchungen werden automatisiert; „Zahlungen werden über DATEV ausgelöst, auf Basis von d.velop Freigabeprozesse" | d.velop → DATEV: ER-Journale, Zahlungs-Journale, Sonderbuchungsinfos; DATEV → d.velop: Zahlungsrückmeldung | 5.1 | ARCH Folie 2, 3; KAT Übersicht C8 | F |
| DATEV-Produkt (Rechnungswesen, Unternehmen online, Kanzlei-Rechnungswesen beim Steuerberater?) | unbekannt; „Übernahmeprozess in DATEV ist abzustimmen" | – | 5.1 | KAT 5.1 | O |
| **BIM4You / Bim4You** | Bau-Projektsteuerung / **Budgetcontrolling**; hat ein eigenes „Rechnungseingangsbuch" | d.velop → Bim4You: ER-Journale bzw. Bauprojekt-Rechnungen; Bim4You → d.velop: Einbehalt-/Kürzungsinfos, Umlageinfos, Freigabestatus | 5.3 | KAT 5.3, Übersicht C8; ARCH Folie 2, 3 | F |
| **Omikron** | „Zahlungsmanagementsystem"; Zahlungen sollen nach Freigabe automatisch ausgelöst werden | Schnittstelle gefordert; MDIS-Notiz: „schnittstelle über BeSync" | 5.5 | KAT 5.5 | F (Anforderung) / O (Anbindung) |
| **BeSync** | Von MDIS als Schnittstellenweg für 5.5 genannt; was BeSync ist (Middleware/Produkt), ist in keiner Quelle erklärt | – | 5.5 | KAT 5.5 Notiz | O |
| **Systeme/ERP der externen Property Manager** | „autarke Systeme/Prozesse"; perspektivisch Stammdaten-Sync (Kreditoren, Kontenrahmen) | Rechnungen → PM; Daten ← PM | 4.1, 5.4 | KAT 4.1, 5.4 | F (Anforderung) / O (welche Systeme, wie viele PM) |
| E-Mail-Postfächer | zentrale Rechnungspostfächer; ein Sammelpostfach für mehrere Empfänger | Eingang | 2.1 | KAT 2.1; TD 23 (Test: `rechnungseingang@livos-test.de`, fiktiv) | F / O (Mailsystem, z.B. Microsoft 365) |
| Mobile Endgeräte | Android / Apple | App | 1.3 | KAT 1.3 | F |
| Eigenes ERP von Livos | in keiner Kundenquelle genannt | – | – | – | O |
| Acumatica-Snapshot „Mocca_V14_108" | im Projektordner vorhanden, **kein einziger Treffer „Livos"** in den 527 Tabellen; Bezug zu Livos nicht belegt | – | – | META (grep) | O |
| Bestehendes DMS/Archiv, Altdatenübernahme | nicht genannt | – | 6.1 | – | O |

---

## 2 Vollständiger Leistungskatalog

### 2.1 Aufbau der Datei und Legende

**Blätter** [F: META]: `Übersicht` (B2:C16), `Leistungskatalog` (A1:G30, Excel-Tabelle „Tabelle3" mit Autofilter, nach ID sortiert), `Tabelle1` (A1:D9). Keine ausgeblendeten Zeilen/Spalten, keine Kommentare, keine Formeln. Aktives Blatt beim Speichern: `Leistungskatalog`. Zuletzt gespeichert 22.09.2026 12:18 (Tag des Workshops) [F: META].

**Kopfdaten (Blatt Übersicht)** [F: KAT Übersicht]:

| Feld | Wert |
|---|---|
| Titel | Leistungskatalog & Anforderungsprofil – Auswahl einer Software für Digitales Rechnungsmanagement |
| Anzahl Gesellschaften | Über 100 Mandanten (Bestand, Privatisierung, Bau) |
| Nutzeranzahl gesamt | Ca. 80 Anwender (intern & extern) |
| Rechnungsvolumen | Ca. 20-30 Rechnungen pro Tag (ca. 5.000 - 8.000 / Jahr) |
| Schnittstellen-Fokus | DATEV, BIM4You (Budgetcontrolling), offene Schnittstellen |
| Erstellungsdatum | Juli 2026 |

**Legende Erfüllungsgrad** („Ausfüllhinweise für Anbieter (Spalte Erfüllungsgrad)", Übersicht B12–C16) [F]:

| Code | Bedeutung (wörtlich) |
|---|---|
| **S** | Standard (Im Kernprodukt ohne Anpassung enthalten) |
| **K** | Konfiguration (Durch Einstellungen/Workflows flexibel abbildbar) |
| **A** | Anpassung (Individuelle Programmierung/Entwicklung notwendig) |
| **N** | Nein (Nicht im Leistungsumfang enthalten) |

Die Spalte F („Erfüllung Anbieter") hat eine Dropdown-Validierung auf `Übersicht!$C$13:$C$16`, daher stehen in den Zellen die **Langtexte** der Legende, nicht die Codes [F: META, x14:dataValidation für F2:F30 und – vermutlich versehentlich – G18].

**Priorität:** Werte „Must-Have", „Should-Have", „Could-Have" (MoSCoW ohne „Won't"). Eine Legende dazu enthält die Datei **nicht** [F]. Deutung: Must = zwingend (K.-o.), Should = wichtig, Could = wünschenswert [A].

### 2.2 Katalog – alle 29 Zeilen, alle Spalten (Texte wörtlich, inkl. Original-Schreibfehler)

Spalte „Erfüllung" = Code + Kurzform (Langtext siehe Legende). „Agenda" = wo der Punkt in der Workshop-Agenda adressiert ist [F: AG]. „Konsolidierungshinweis" = Befund aus den übrigen Quellen (Details Kap. 8).

| ID | Kategorie | Anforderung / Funktion | Priorität | Detailvorgabe / Beschreibung (vollständig) | Erfüllung Anbieter | Notizen / Bermerkungen (wörtlich) | Agenda | Konsolidierungshinweis |
|---|---|---|---|---|---|---|---|---|
| 1.1 | Systemarchitektur | Echte Mandantenfähigkeit | Must-Have | Vollständige Abbildung von über 100 Gesellschaften. Daten, Workflows und Berechtigungen müssen pro Mandant strikt getrennt, aber zentral verwaltet werden können. | **K** – Konfiguration | wird über Strukturen, Eigenschaften und Berechtigungen eingerichtet. | F2 (Dokumentenmodell), F4 (Frage 1.1) | Hypothese „eine Instanz", Konfidenz hoch; bei Instanztrennung K→A (KAT Tabelle1). smart invoice hat eigenes Mandantenkonzept (id, name, parent_id, address …) [B00 I] |
| 1.2 | Systemarchitektur | Webbasierter Zugriff (Cloud/SaaS) | Must-Have | Die Software muss ortsunabhängig und ohne lokale Installation über gängige Webbrowser (vollständig responsiv) für dezentral/deutschlandweit verteilte Teams nutzbar sein. | **S** – Standard | – | F2 (d.velop im Überblick) | Demo-Instanz ist Cloud (`mdisconsulting.d-velop.cloud`) [LM] |
| 1.3 | Systemarchitektur | App | Could-Have | App-basierte Übersicht / Bearbeitung auf Android / Apple sollte möglich sein. | **S** – Standard | – | F2 | – |
| 1.4 | Systemarchitektur | Individuelle Workflow-Konfiguration | Must-Have | Je Gesellschaft/Mandant müssen komplett eigenständige Prüf- und Freigabeworkflows sowie Freigabegrenzen (z.B. Vier-Augen-Prinzip ab Betrag X) und Personenketten hinterlegt werden können. | **S** – Standard | – | F2 (Freigabeprozess, Workflows & Freigaben) | Fachlich eher **K** (Freigabematrix / Schrittverbindungen); Vier-Augen-Prinzip von smart invoice ist Vorschau-Feature [A05 Kap. 8; B00 AK, AL] |
| 1.5 | Systemarchitektur | Strikte Rollen- & Rechteverwaltung | Must-Have | Detaillierte Rechtevergabe für interne Mitarbeiter (Buchhaltung, Projektleiter, Geschäftsführer) und externe Partner. | **S** – Standard | – | F2 (Dokumentenmodell) | Cloud-Berechtigungsoberfläche in öffentlicher Doku nicht beschrieben [A05 9.2; B00 L] |
| 1.6 | Systemarchitektur | Revisionssicherheit & GoBD | Must-Have | Lückenlose, manipulationssichere Protokollierung des gesamten Rechnungsverlaufs (wer hat wann was geprüft/freigegeben/geändert). Erfüllung aller GoBD-Kriterien. Alle Protokolle / Unterlagen müssen z.B. bei Verkauf je Gesellschaft auch exportiert und revisionssicher weitergegeben werden können. | **S** – Standard | – | F2 (Speichern & Archivieren) | Export je Gesellschaft „kein Knopfdruck", eher Dienstleistungspaket (Hypothese, Konfidenz mittel) [KAT Tabelle1] |
| 1.7 | Systemarchitektur | Ablage | Should-Have | Möglichkeit neben den Rechnungen noch weitere Nachweise anzuhängen (z.B. Verträge, Aufträge, E-Mails, etc.). | **S** – Standard | – | F2 (Erfassung und Ablage; Postverteilung) | Demo: Kategorien Vertrag/Auftrag/Nachweis/Korrespondenz, Akten als Sichten [A06 3.3, 3.5] |
| 1.8 | Systemarchitektur | Händische Anpassbarkeit | Must-Have | Trotz Automatisierung muss es berechtigten Nutzern jederzeit möglich sein, Werte, Kontierungen oder Workflows manuell zu übersteuern oder anzupassen. | **S** – Standard | Übersteuern von Werten, Kontierung und Workflow durch berechtigte Nutzer ist Kernfunktion, inklusive Protokollierung der Änderung | F2 (Prüfung) | Änderungsprotokoll „Aktivitäten" nur in der Cloud [A05 2.1] |
| 2.1 | Rechnungseingang & KI | Automatischer Postfach-Import | Must-Have | Direktes, automatisiertes Auslesen von zentralen E-Mail-Postfächern und automatisierte Anlage des Belegs im System. Möglichkeit, dass Rechnungen mehrerer Empfänger auf nur ein Postfach gesendet werden und dann im System verarbeitet / zugeordnet werden. | **S** – Standard | Mail-Import ist Standard. Die Aufteilung mehrerer Empfänger aus einem Sammelpostfach läuft über die Zuordnungsregeln und ist Konfigurationsanteil. | F2 (Erfassung; Postverteilung) | Notiz beschreibt selbst einen K-Anteil; Alias-Adressen je Gesellschaft als Lösungsweg [A05 Kap. 7] |
| 2.2 | Rechnungseingang & KI | KI-Erkennung & Mandantenzuordnung | Must-Have | Intelligente OCR/KI-Erkennung der Pflichtangaben (Kreditor, Beträge, Steuersätze, IBAN). Besonders wichtig: Automatische Erkennung und Zuordnung zum korrekten Rechnungsempfänger (Zuordnung zur richtigen der 100+ Gesellschaften anhand der Anschrift/Steuernummer). | **S** – Standard | – | F2 (KI-Erkennung inkl. Mandantenzuordnung), F4 (Frage 2.2) | **S nur mit Vorbehalt**: Mandantenerkennung über Name + Anschrift, **nicht** Steuernummer [LM „Was noch offen ist"; A05 Kap. 6; B00 AI] |
| 2.3 | Rechnungseingang & KI | Rechnungserkennung | Must-Have | Wenn Rechnungsempfänger eine Gesellschaft, die nicht bekannt / hinterlegt ist, muss auch hierfür ein Prozess / Workflow eingesteuert werden können, der es dem Bearbeiter ermöglicht entsprechende Schlussfolgerungen zu ziehen. | **K** – Konfiguration | Abdeckbar mit Worflow mit Einschränkungen | F2 („Verteilung inkl. Klärfall unbekannte Gesellschaft (2.3)- X") | Einschränkungen nicht benannt; Kandidaten: Standardmandant, Clearing-Modus im Rechnungseingangsbuch [A05 6.1, 10.1] |
| 2.4 | Rechnungseingang & KI | E-Rechnungs-Konformität | Must-Have | Volle Unterstützung aller gängigen E-Rechnungs-Formate (ZUGFeRD, XRechnung) inklusive kombinierter Visualisierung der XML-Daten für den Prüfer. | **S** – Standard | – | F2 (ZUGFeRD/XRechnung) | Testbelege 09/10 nicht validiert (kein KoSIT-Check, kein PDF/A-3) [TDL 5; META] |
| 2.5 | Rechnungseingang & KI | Buchungs- & Kontierungsvorschläge | Must-Have | Die KI muss aus historischen Daten lernen und automatische Vorschläge für Sachkonten, Kreditoren und Kostenstellen (oder Projektnummern) generieren. | **S** – Standard | – | F2 (Kreditorenbuch & Kontierung) | Vorschläge Sachkonto/Kostenstelle dokumentiert; „Projektnummern" ≈ Kostenträger [B00 AM] |
| 2.6 | Rechnungseingang & KI | Rechnungsprüfung | Must-Have | Rechnung muss auf steuerliche Richtigkeit und weitere Kriterien (z.B. Freistellungsbescheinigung) automatisch (auch nach individueller Anpassungen) geprüft werden. | **S** – Standard | – | F2 (Prüfung (2.6, 1.8)) | **Widerspruch zu 2.7 (N)**: die FSB-Prüfung ist in 2.6 als Beispiel genannt und dort mit S bewertet |
| 2.7 | Rechnungseingang & KI | Freistellungsbescheinigung | Could-Have | Möglichkeit Freistellungsbescheinigungen im System zu hinterlegen, sodass automatisch erkannt wird (bei einer Baurechnung, die das erforderlich machen), ob eine Freistellungsbescheinigung vorliegt - andernfalls Vorschlag mit 15% Abzug automatisch einarbeiten. | **N** – Nein | Eigentlich machbar über code, dennoch keine Zeit | – (nicht auf der Agenda) | A06 Kap. 7, TDL 3 und Testbeleg 24 führen 2.7 als **„A"** |
| 2.8 | Rechnungseingang & KI | Aufteilung von Rechnungen auf Kostenstellen | Must-Have | Rechnungen müssen auf vorgegebene Kostenstellen aufgeteilt werden können. Standardschlüssel für die Aufteilung müssen systemisch je Gesellschaft hinterlegt werden können. | **S** – Standard | – | F2 (Kreditorenbuch & Kontierung) | Aufteilung ja (Belegpositionen), benannter Standardschlüssel je Gesellschaft **nicht dokumentiert** → S fraglich, eher K [KAT Tabelle1; A05 Kap. 11; B00 AM] |
| 3.1 | Workflows & Dashboards | Persönliches Nutzer-Dashboard | Must-Have | Übersichtliche 'Inbox' / Dahsboard für jeden der ca. 80 Nutzer, die dem Anwender sofort die aktuell zur Prüfung/Freigabe zugewiesenen Rechnungen anzeigt. | **S** – Standard | – | – (nicht auf der Agenda) | „Meine Aufgaben" / Rechnungseingangsbuch „Meine offenen Rechnungen" [A05 10.1] |
| 3.2 | Workflows & Dashboards | Management- & Controlling-Dashboard | Must-Have | Berechtigte Personen (Abteilungsleiter, Geschäftsführer, Gesellschafts-Verantwortliche) benötigen einen Gesamtüberblick über alle im Umlauf befindlichen Rechnungen (Status, aktueller Bearbeiter, Liegezeit). | **S** – Standard | – | – (nicht auf der Agenda) | **„Liegezeit" in keiner Doku belegt → S ist Zusage ohne Beleg** [LM; B00 AB]; Managementsicht = Rechnungseingangsbuch, nicht Dashboard [LM; A05 Kap. 10] |
| 3.3 | Workflows & Dashboards | Automatisches Eskalationsmanagement | Must-Have | Wenn eine Rechnung mehr als X Tage (Wert je Gesellschaft/Workflow flexibel definierbar) unberührt bleibt, muss automatisch eine Benachrichtigung oder Weiterleitung an definierte Personen (z.B. Vertretung oder Abteilungsleiter) per Mail erfolgen. | **S** – Standard | Fristen, Eskalationsstufen und Empfänger werden je Workflow konfiguriert | F2 („Eskalation & Vertretung (3.3, 3.4) - X") | Notiz beschreibt Konfiguration (→ K); Aufbau 3–6 h, Mail-Aktionskatalog nicht dokumentiert [A05 Kap. 11] |
| 3.4 | Workflows & Dashboards | Vertretungsregelungen | Must-Have | Einfache Aktivierung von Vertretungen (geplant bei Urlaub oder ungeplant bei Krankheit) mit automatischer Weiterleitung oder temporärer Freigabe der Aufgabenmappe. | **K** – Konfiguration | Abwesenheits- und Vertretungsregelung je Nutzer, geplant | F2 („… - X") | Notiz deckt nur „geplant" ab – der ungeplante Fall (Krankheit, Aktivierung durch Dritte) ist offen |
| 4.1 | Externe Partner | Prozessunabhängigkeit Property Manager | Must-Have | Abbildung eines Prozesses, bei dem Rechnungen für rein verwaltete Immobilienassets direkt ohne internen Workflow an die autarken Systeme/Prozesse der Property Manager verbunden werden und die Daten vom Property Manager eingespielt werden können/zugänglich gemacht werden können. | **N** – Nein | – | F3 (Offene Schnittstellenthemen) | **Einziges Must-Have mit N.** A06 W6 „Fremdverwaltung" deckt den Prozesszweig „teilw." ab |
| 4.2 | Externe Partner | Ad-hoc Freigabe per Mail/Link (Ohne Lizenz) | Should-Have | Externe Projektbeteiligte (z. B. Projektsteuerer, Architekten) müssen per E-Mail oder über einen sicheren, temporären Web-Link in den Freigabeprozess eingebunden werden können, ohne dass sie als feste Nutzer im System registriert sind oder Software installieren müssen. | *(leer)* | falls Gastzugang bzw. sicherer Freigabe-Link existiert; sonst Anpassung notwendig. Erst nach Klärung eintragen. | F4 (Frage 4.2) | „Extern Teilen" (Link, Zeitraum, lesen/bearbeiten) nur Cloud + Edition documents business, **kein Freigeben im Workflow-Sinn** [B00 E] |
| 4.3 | Externe Partner | Direkte Web-Anbindung für Kern-Partner | Must-Have | Wichtige externe Partner sollen über einen standardisierten, sicheren Web-Zugang direkt im System arbeiten, Rechnungen einsehen und freigeben können. | **S** – Standard | – | F2 (Freigabe (4.3)) | Externe = reguläre (lizenzpflichtige) Nutzer → gehört ins Lizenz-Mengengerüst [KAT Tabelle1 4.2] |
| 5.1 | Schnittstellen & Bauspezifika | DATEV-Schnittstelle | Must-Have | Flexible Anbindung an DATEV. Alle Rechnungen müssen inkl. Belege automatisiert ins DATEV gespielt werden können (nicht nur pauschal 1x pro Tag). Übernahmeprozess in DATEV ist abzustimmen. | **S** – Standard | – | F2 („DATEV Übergabe (5.1) - X"), F4 (Frage 5.1) | DATEV-Doku von d.velop nicht öffentlich; Frequenz/Format unbelegt [B00 P, AQ]; in der Demo nicht live [A06 Kap. 7] |
| 5.2 | Schnittstellen & Bauspezifika | Bau-Spezifika (VOB & Einbehalte) | Should-Have | Logische Abbildung und rechnerische Prüfung von Abschlags- und Schlussrechnungen (kumulierte Abrechnung nach VOB) sowie die Verwaltung und Vormerkung von Sicherheitseinbehalten (Gewährleistung/Vertragserfüllung). | **N** – Nein | Kumulierte VOB-Abrechnung und Sicherheitseinbehalte sind Bau-ERP-Funktionen. Entwicklung ist nicht vorgesehen. | – (nicht auf der Agenda) | Zielarchitektur: Einbehalt-/Kürzungsinfos kommen **aus Bim4You** zurück → Lösungsweg über 5.3 [ARCH Folie 2] |
| 5.3 | Schnittstellen & Bauspezifika | Schnittstelle zu BIM4You | Should-Have | Optionale Möglichkeit zur Verknüpfung mit dem Budgetcontrolling von BIM4You. Idealerweise Erkennung von Feldern wie 'Gewerk / Los' durch KI und automatisierter Export ins Rechnungseingangsbuch von BIM4You. | *(leer)* | ggf. über API möglich, selber Anpassung | F3 (Offene Schnittstellenthemen) | Notiz entspricht faktisch **A**; A06/A05 führen 5.3 als „N"; Zielarchitektur macht Bim4You zur Kernintegration |
| 5.4 | Schnittstellen & Bauspezifika | Perspektivische ERP-/PM-Anbindung | Could-Have | Offene API-Schnittstellen, um perspektivisch Stammdaten (Kreditoren, Kontenrahmen) mit den ERP-Systemen der externen Property Manager zu synchronisieren. | *(leer)* | Rest API in Standart.  Die konkrete Synchronisation wäre ein Folgeprojekt. | F2 (d.velop im Überblick), F3 | Notiz entspricht S (API) + A (Synchronisation); 47 REST-APIs öffentlich dokumentiert [B00 Q] |
| 5.5 | Schnittstellen & Bauspezifika | Schnittstelle Zahlungsamangementsystem | Must-Have | Schnittstelle zu Omikron (Zahlungsmanagementsystem), sodass Zahlungen nach Freigabe automatisch ausgelöst werden können für berechtigte Nutzer | *(leer)* | Zahlungsprozess standart, schnittstelle über BeSync | F2 („Zahlung mit Zahlungsfreigaben (Teil von 5.5)"), F3, F4 (Frage 5.5) | **Must-Have ohne Bewertung.** Vier verschiedene Lesarten in den Quellen (Kap. 8, W20) |
| 6.1 | DMS | DMS-Möglichkeit | Could-Have | Möglichkeit, dass das System auch als DMS nutzbar ist | **S** – Standard | – | F2 (Postverteilung; Dokumenten- & Aktenerstellung) | Zielarchitektur macht DMS (Verträge, Post) zum Kern – im Katalog nur Could |

### 2.3 Auswertung des Katalogs

**Priorität × Erfüllung (Stand Datei)** [F: KAT, eigene Zählung]:

| Priorität | S | K | A | N | leer | Summe |
|---|---|---|---|---|---|---|
| Must-Have | 16 (1.2, 1.4, 1.5, 1.6, 1.8, 2.1, 2.2, 2.4, 2.5, 2.6, 2.8, 3.1, 3.2, 3.3, 4.3, 5.1) | 3 (1.1, 2.3, 3.4) | 0 | **1 (4.1)** | **1 (5.5)** | 21 |
| Should-Have | 1 (1.7) | 0 | 0 | 1 (5.2) | 2 (4.2, 5.3) | 4 |
| Could-Have | 2 (1.3, 6.1) | 0 | 0 | 1 (2.7) | 1 (5.4) | 4 |
| **Summe** | **19** | **3** | **0** | **3** | **4** | **29** |

**Je Kategorie:** Systemarchitektur 8 (1.1–1.8) · Rechnungseingang & KI 8 (2.1–2.8) · Workflows & Dashboards 4 (3.1–3.4) · Externe Partner 3 (4.1–4.3) · Schnittstellen & Bauspezifika 5 (5.1–5.5) · DMS 1 (6.1) [F].

**Befunde:**
- Kein einziges „A" eingetragen, obwohl die Notizen zu 2.7 („machbar über code"), 5.3 („selber Anpassung") und 5.4 („Synchronisation wäre ein Folgeprojekt") genau Anpassung beschreiben [F/A].
- **Zwei Must-Haves sind heute nicht erfüllt bzw. unbewertet: 4.1 (N) und 5.5 (leer)** [F].
- **Fünf S-Bewertungen bei Must-Haves stehen unter Vorbehalt** laut den übrigen Quellen: 2.2, 2.8, 3.2, 5.1 (Doku gesperrt), 1.6 (Export je Gesellschaft) – dazu 1.4/3.3 (fachlich K statt S) [F: LM; KAT Tabelle1; B00].
- **Nicht auf der Agenda:** 2.7, 3.1, 3.2, 5.2 – also u.a. beide Dashboard-Must-Haves [F: AG Folie 2–4].

### 2.4 Blatt „Tabelle1" – MDIS-interne Hypothesen (vollständig, wörtlich)

> Hinweis [A]: Das Blatt ist eine **interne Arbeitshilfe von MDIS** (Hypothesen, Konfidenz, Rückfallposition). Es liegt in derselben Datei, die als Anbieterantwort an Livos zurückgeht → vor Versand entfernen.

| Frage | Hypothese | Konfidenz | Wenn sie nicht hält |
|---|---|---|---|
| 1.1 Mandantenmodell — eine Instanz oder über 100 getrennte Mandanten? | Eine Instanz. Gesellschaft als Pflichteigenschaft am Beleg, Trennung über Berechtigungen und Sichten. Dafür spricht, dass der Katalog ausdrücklich „zentral verwaltet" fordert und getrennte Instanzen bei über 100 Gesellschaften in Betrieb und Lizenz kaum beherrschbar wären. | hoch | Bei echter Instanztrennung steigen Lizenz- und Betriebsaufwand deutlich, und die gesellschaftsübergreifende Auswertung (3.2) wird schwierig. 1.1 fällt dann von K auf A. |
| 2.2 Trefferquote Mandantenzuordnung | Kreditor, Beträge und Steuersätze werden zuverlässig erkannt. Die Zuordnung zum richtigen Rechnungsempfänger bricht ein, sobald mehrere Gesellschaften dieselbe Verwaltungsanschrift führen; d.velop wird Steuernummer oder USt-IdNr. als Unterscheidungsmerkmal anbieten. | mittel bis hoch | Ohne belastbares Unterscheidungsmerkmal bleibt ein manueller Zuordnungsschritt je Beleg. Bei 20 bis 30 Belegen am Tag tragbar, aber das Automatisierungsversprechen schrumpft spürbar. |
| 2.8 Standardschlüssel je Gesellschaft | Die Aufteilung auf Kostenstellen ist Standard, fest hinterlegte Verteilungsschlüssel je Gesellschaft sind es nicht. Wahrscheinlich gibt es Kontierungsvorlagen, die den Schlüssel mitbringen. | mittel | Ohne Vorlagen wird der Schlüssel je Beleg manuell gewählt und 2.8 fällt von S auf K. |
| 4.2 Ad-hoc Freigabe ohne Lizenz | Technisch möglich über zeitlich begrenzten Link oder Mail-Freigabe, aber nicht kostenlos. Erwartung: eine günstige Gelegenheits- oder Kontingentlizenz statt echter Lizenzfreiheit. | mittel | Kein Blocker, da Should-Have. Dann laufen externe Freigeber als reguläre Nutzer (4.3) und die Kosten gehören ins Mengengerüst. |
| 5.1 DATEV-Übergabefrequenz | Die Übergabe ist zeitgesteuert und auf kurze Intervalle stellbar. Echte Ereignissteuerung „sofort bei Freigabe" ist seltener, mehrfach täglich aber praktisch sicher erfüllbar. | hoch | Der Katalog fordert „nicht nur pauschal 1x pro Tag", also mehrfach täglich und nicht Echtzeit. Die Anforderung ist damit so oder so erfüllt. |
| 1.6 Archivexport je Gesellschaft | Möglich, aber kein Knopfdruck — eher ein Dienstleistungspaket aus Dokumenten, Metadaten und Protokoll in einem neutralen Format. | mittel | Läuft der Export nur über den Hersteller und kostenpflichtig je Fall, gehört das bei über 100 Gesellschaften mit Verkaufsabsicht in die Vertragsverhandlung, nicht nur in Spalte F. |
| 5.5 Zahlungsauslösung ohne Omikron | d.velop liefert Zahlungsfreigabe und Zahlungsvorschlag, aber keine Zahlungsdatei und keine Bankanbindung. Der Zahllauf bleibt in DATEV oder im Zahlungssystem. | hoch | Kann doch eine SEPA-Datei erzeugt oder die Freigabe an DATEV durchgereicht werden, fällt 5.5 von N auf K und das Must-Have ist ohne Omikron erfüllbar. Gezielt danach fragen. |
| Lizenz- und Mengengerüst | Named-User-Lizenzen für die rund 80 Anwender. 5.000 bis 8.000 Belege im Jahr sind unkritisch und liegen im untersten Staffelbereich; der Preis wird von Nutzerzahl und Mandantenmodell getrieben, nicht vom Volumen. | hoch | Bei volumen- oder mandantenbasierter Lizenzierung schlagen die über 100 Gesellschaften voll durch. Dann ist Frage 1.1 auch eine Preisfrage. |

---

## 3 Zielarchitektur laut MDIS-Folien („Livos_DMS_Business Architektur.pdf")

Dokument: 5 Folien (Querformat), erzeugt aus „Microsoft PowerPoint - DMS_Business Architektur", Autor „ThomasGross", **erstellt 28.05.2025** [F: META PDF-Metadaten]. Farbcode auf Folie 3–5 (Legende „= d.velop"): **lila = Prozessschritt in d.velop**, hellgrün = Eingangsobjekt, dunkeltürkis = Fremdsystem/Integration [F: arch_3–5.png].

### 3.1 Folie 1 – Titel
„DMS-Kernprozesse" mit Logo „LIVOS Gruppe" und MDIS-Logo [F: arch_1.png].

### 3.2 Folie 2 – „DMS-Systemarchitekturen" (Systemlandschaft, Datenflüsse)

```
   [Eingangsrechnungen]   [Verträge]   [Post]        (Eingangsobjekte, oben)
            └───────────────┬───────────────┘        (Sammellinie, EIN Pfeil nach unten)
                            ▼
 ┌──────────────────────────────── d.velop ───────────────────────────────────┐
 └──┬──────────┬──────────────┬──────────▲──────────┬──────────▲──────────▲───┘
    │D1        │D2            │D3        │D4        │B1        │B2        │B3
    ▼          ▼              ▼          │          ▼          │          │
 ┌──────────────── DATEV ─────────────────┐   ┌─────────────── Bim4You ────────┐
 └────────────────────────────────────────┘   └────────────────────────────────┘
```

| # | Von → Nach | Inhalt (wörtlich) | Darstellung | Typ |
|---|---|---|---|---|
| E1 | Eingangsrechnungen, Verträge, Post → d.velop | (drei Eingangsobjekte) | drei Kästen, Sammellinie, **ein** Pfeil in d.velop | F |
| D1 | d.velop → DATEV | „Eingangs-rechnungs-Journale" | Pfeil abwärts | F |
| D2 | d.velop → DATEV | „Zahlungs-Journale" | Pfeil abwärts | F |
| D3 | d.velop → DATEV | „Sonder-Buchungs-Informationen: → ARAP/PARP → Rückstellungen → Anzahlungen → …" | Pfeil abwärts | F |
| D4 | DATEV → d.velop | „Zahlungs-Rückmeldung" | Pfeil aufwärts | F |
| B1 | d.velop → Bim4You | „Eingangs-rechnungs-Journale" | Pfeil abwärts | F |
| B2 | Bim4You → d.velop | „Einbehalt- und Kürzungs-Informationen" **und** „Umlageinformationen" | **ein** Pfeil aufwärts mit zwei Aufzählungspunkten | F |
| B3 | Bim4You → d.velop | „Freigabe-Status" | Pfeil aufwärts | F |
| – | DATEV ↔ Bim4You | **keine direkte Verbindung**; d.velop ist einzige Drehscheibe | – | F |

**Fußnoten der Folie (wörtlich)** [F]:
- „DATEV als operatives FiBu-System"
- „Eingangsrechnungs- und Zahlungsbuchungen werden automatisiert."
- „Zahlungen werden über DATEV ausgelöst, auf Basis von d.velop Freigabeprozesse"

**Fachliche Erläuterung der Begriffe** [A, nicht in der Quelle erklärt]:
- **ARAP/PARP** = aktive / passive Rechnungsabgrenzungsposten (periodengerechte Abgrenzung, z.B. vorausbezahlte Versicherungen, Wartungsverträge).
- **Rückstellungen** = z.B. für ausstehende Rechnungen, Gewährleistung, Prozesskosten.
- **Anzahlungen** = geleistete Anzahlungen (bei Bau: ggf. auch „Anlagen im Bau").
- **Einbehalt- und Kürzungsinformationen** = Sicherheitseinbehalte und Rechnungskürzungen aus der Bau-Rechnungsprüfung (passt zu KAT 5.2 und Testbeleg 07).
- **Umlageinformationen** = unklar: entweder Kostenumlage auf Bauabschnitte/Häuser/Einheiten (Bau-Controlling) oder Umlagefähigkeit auf Mieter (Betriebskosten). → [O]
- **Freigabe-Status** = Ergebnis der Rechnungsprüfung/Budgetfreigabe in Bim4You.

### 3.3 Folie 3 – „Eingangs-Rechnungsprozess" (Prozesskette ER)

| # | Schritt (wörtlich) | System | Anbindung / Verzweigung (wörtlich bzw. beschrieben) | Typ |
|---|---|---|---|---|
| 0 | „Eingangs-rechnungen (ER)" | Eingangsobjekt (hellgrün) | Pfeil → Eingang | F |
| 1 | „Eingang" | d.velop | – | F |
| 2 | „Verarbeitung& Vor-Qualifikation" | d.velop | – | F |
| 3 | „Verteilung" | d.velop | Darüber gestapelt: Kasten „DTEV Integration" und darüber „ER Vorerfassungs-Journal" – **ohne Verbindungspfeile** (nur räumlich zugeordnet) | F |
| 4 | „Fachliche Prüfung/ Detail-Qualifikation" | d.velop | Pfeil abwärts mit Text: „Rechnungen bezüglich Bauprojekte werden an bim4you zur Bearbeitung übergeben" → Kasten **„Bim4You"** → verzweigt in **„Budget Abgleich"** und **„Bearbeitung"**; unter „Bearbeitung": „Sonder-Buchungs-Informationen: → ARAP/PARP → Rückstellungen → Anzahlungen → …" | F |
| 4a | Rückführung aus Bim4You | Bim4You → d.velop | Linie vom Kasten „Bim4You" nach rechts und mit Pfeil **von unten in „Fachliche Freigabe"** | F |
| 5 | „Fachliche Freigabe" | d.velop | Pfeil aufwärts → „DTEV Integration" → Pfeil → **„Verbuchung von ER"** | F |
| 6 | „Zahlungs-freigabe" | d.velop | Pfeil aufwärts → „DTEV Integration" → Pfeil → **„Durchführung der Zahlung"** | F |

Schreibweise „DTEV" (statt DATEV) steht dreimal auf der Folie [F: arch_3.png; Tippfehler].

**Lesart der ER-Kette** [A]:
1. DATEV wird **zweistufig** bedient: (a) frühe Vorerfassung („ER Vorerfassungs-Journal") schon bei der Verteilung – vor der Freigabe –, (b) endgültige „Verbuchung von ER" nach der fachlichen Freigabe; (c) Zahlung wird nach Zahlungsfreigabe in DATEV durchgeführt. Ob die Vorerfassung eine echte Buchung (offener Posten, Liquiditätsplanung, Periodenabgrenzung) oder ein Vorerfassungsstapel ist, bleibt offen [O].
2. Bau-Rechnungen durchlaufen zwischen fachlicher Prüfung und fachlicher Freigabe eine **Schleife über Bim4You** (Budgetabgleich + Bearbeitung inkl. Sonderbuchungsinfos); der Freigabestatus aus Bim4You fließt in die fachliche Freigabe in d.velop zurück.
3. **Zahlungsfreigabe ist ein eigener d.velop-Schritt**, getrennt von der fachlichen Freigabe (Funktionstrennung sachlich/finanziell).
4. Nicht dargestellt: Zahlungsrückmeldung (D4) im Prozessbild, Omikron, Property-Manager-Zweig (KAT 4.1), Klärfall unbekannte Gesellschaft (KAT 2.3), Eskalation/Vertretung.

### 3.4 Folie 4 – „Verträge" (Prozesskette)

„Verträge" (Eingangsobjekt) → **Eingang → Verarbeitung → Verteilung → Klassifizierung → Fachliche Freigabe → Archivierung** – alle sechs Schritte lila = d.velop; **keine Integration zu DATEV/Bim4You dargestellt** [F: arch_4.png].

### 3.5 Folie 5 – „Post" (Prozesskette)

„Post" (Eingangsobjekt) → **Eingang → Verarbeitung → Klassifizierung → Verteilung → Archivierung** – alle fünf Schritte d.velop; **keine Freigabe, keine Integration** [F: arch_5.png].

Auffällig: Bei Verträgen steht **Verteilung vor Klassifizierung**, bei Post **Klassifizierung vor Verteilung** [F]. Ob fachlich gewollt (Verträge werden von der Fachabteilung klassifiziert) oder Inkonsistenz, ist offen [O].

### 3.6 Abgleich Zielarchitektur ↔ Katalog

| Element der Zielarchitektur | Katalog-Bezug | Befund |
|---|---|---|
| Eingang / Verarbeitung & Vorqualifikation | 2.1, 2.2, 2.4, 2.5 | abgedeckt |
| Verteilung | 2.1 (Sammelpostfach), 2.3 (Klärfall) | Klärfall nicht in der Folie |
| DATEV-Vorerfassungsjournal bei Verteilung | 5.1 („alle Rechnungen inkl. Belege …, nicht nur 1x pro Tag") | Zeitpunkt/Zweistufigkeit nicht im Katalog |
| Fachliche Prüfung / Detailqualifikation | 1.8, 2.6, 2.8 | abgedeckt |
| Bim4You-Schleife (Budgetabgleich, Bearbeitung, Freigabestatus) | 5.3 (Should, „optional") | Folie macht Should-Have zur Kernintegration |
| Einbehalt-/Kürzungsinfos aus Bim4You | 5.2 (Should, N) | Architektur bietet Lösungsweg für 5.2 |
| Sonderbuchungsinfos (ARAP/PARP, Rückstellungen, Anzahlungen) | – | **keine Katalog-Anforderung** |
| Fachliche Freigabe → Verbuchung | 1.4, 4.3, 5.1 | abgedeckt |
| Zahlungsfreigabe → Durchführung der Zahlung in DATEV | 5.5 (Omikron!) | **Widerspruch**: Katalog will Auslösung über Omikron |
| Zahlungsrückmeldung DATEV → d.velop | – | keine Katalog-Anforderung |
| Verträge-Prozess | 1.7 (Nachweise), 6.1 (Could) | **keine eigene Anforderung** |
| Post-Prozess | 2.1, 1.7, 6.1 (laut Agenda) | **keine eigene Anforderung** |
| Property Manager | 4.1 (Must), 5.4 | **fehlt in der Architektur** |
| Externe Freigeber | 4.2, 4.3 | fehlt in der Architektur |
| Dashboards/Reporting | 3.1, 3.2 | fehlt in der Architektur |

---

## 4 Offene Fragen aus der Agenda (Folie 4) mit Erläuterung

Die Agenda-Datei hat 4 Folien: Folie 1 = Agenda ohne Katalogbezüge (Vorversion), Folie 2 = dieselbe Agenda mit Katalognummern und drei „- X"-Markierungen, Folie 3 = „Diskussion & weiteres Vorgehen", **Folie 4 = offene Fragen** (Titel ebenfalls „Agenda"). Referenten laut Folie: Thomas Groß (CEO), Valeria Filimonow (Sales), Annalena Groß (ERP Consultant) [F: AG]. Die Antworten aus dem Workshop stehen im Transkript (separate Auswertung).

### 4.1 Die sechs Fragen

| # | Frage (wörtlich, AG Folie 4) | Bezug | Warum entscheidend (Erläuterung) | MDIS-Hypothese (KAT Tabelle1) | Stand der Recherche (ergänzend) |
|---|---|---|---|---|---|
| Q1 | **1.1 Mandantenmodell** – „Werden über 100 Gesellschaften in einer Instanz über Eigenschaften und Berechtigungen abgebildet oder als getrennte Mandanten? Davon hängen zentrale Verwaltbarkeit, Lizenzierung und der Export je Gesellschaft ab." | 1.1 Must/K; wirkt auf 1.6, 3.2, Lizenz | Grundsatzentscheidung des gesamten Konzepts: bestimmt Berechtigungsmodell, Workflow-Varianten je Gesellschaft (1.4), gesellschaftsübergreifendes Reporting (3.2), Export bei Verkauf (1.6) und Lizenzkosten | Eine Instanz, Gesellschaft als Pflichteigenschaft, Trennung über Berechtigungen/Sichten (Konfidenz hoch); sonst K→A | „Mandant" ist bei d.velop dreifach belegt: Cloud-Tenant, smart-invoice-Mandant (Buchungskreis, mit `parent_id`-Hierarchie), Eigenschaftswert [B00 I] |
| Q2 | **2.2 Trefferquote Mandantenzuordnung** – „Wie zuverlässig wird der richtige Rechnungsempfänger erkannt, wenn viele Gesellschaften dieselbe Anschrift teilen? Referenzwert oder Testlauf mit echten Belegen notwendig." | 2.2 Must/S | Kern des Automatisierungsversprechens; bei >100 Gesellschaften mit gemeinsamer Verwaltungsanschrift entscheidet die Trefferquote über manuellen Aufwand je Beleg | Kreditor/Beträge/Steuersätze zuverlässig; Zuordnung bricht bei gleicher Anschrift ein; d.velop bietet Steuernummer/USt-IdNr. an (mittel bis hoch) | **Hypothese widerlegt**: Mandantenerkennung über **Name + Anschrift**, Steuernummer/USt-IdNr. nur beim Kreditor [LM; B00 AI]. Ausweg: Alias-Postfächer je Gesellschaft [A05 Kap. 7]; bei E-Rechnungen stehen Käufer-USt-IdNr./BuyerReference strukturiert im XML [META Testbelege 09/10] |
| Q3 | **4.2 Ad-hoc Freigabe ohne Lizenz** – „Können Externe über einen sicheren, temporären Link freigeben, ohne als Nutzer angelegt zu sein? Falls ja, zu welchen lizenzrechtlichen Bedingungen? Die Antwort entscheidet, ob der Punkt in die Agenda kommt." | 4.2 Should/leer; 4.3 | Projektsteuerer/Architekten sind je Bauprojekt wechselnd; feste Lizenzen treiben Kosten und Admin-Aufwand | Technisch möglich, aber nicht kostenlos (Gelegenheits-/Kontingentlizenz) (mittel) | „Extern Teilen" (Link mit Zeitraum, lesen/bearbeiten) nur Cloud + Edition documents business, **kein Workflow-Freigeben** [B00 E] |
| Q4 | **5.1 DATEV-Übergabefrequenz** – „Der Katalog fordert ausdrücklich mehr als einen Lauf pro Tag. Ereignisgesteuerte oder mehrfach tägliche Übergabe inklusive Beleg bestätigen lassen." | 5.1 Must/S | Aktualität der FiBu (Liquidität, OP-Liste, Zahllauf); Zielarchitektur verlangt zusätzlich Vorerfassung, Verbuchung, Zahlungsjournal, Sonderbuchungen und Rückmeldung | Zeitgesteuert, kurze Intervalle; mehrfach täglich praktisch sicher (hoch) | DATEV-Handbücher von d.velop hinter Login; Format/Intervall unbelegt [B00 P, AQ] |
| Q5 | **5.5 Zahlungsauslösung** – „Gibt es einen d.velop-seitigen Weg zur Zahlungsdatei oder zur Zahlungsfreigabe in DATEV, der Omikron einbindet? Sonst bleibt dieses Must-Have unerfüllt." | 5.5 Must/leer | Einziges Must-Have ohne Bewertung; Zielarchitektur sieht Zahlung über DATEV, Katalog über Omikron | d.velop liefert Zahlungsfreigabe/-vorschlag, keine Zahlungsdatei/Bankanbindung; Zahllauf in DATEV/Zahlungssystem (hoch) | MDIS-Notiz im Katalog nennt „BeSync" – nicht erläutert [O] |
| Q6 | **Lizenz- und Mengengerüst** – „Rund 80 Anwender intern und extern, 5.000 bis 8.000 Belege im Jahr: Lizenzmodell, Staffelung und Systemgrenzen bestätigen lassen." | Übersicht C6/C7; 4.2, 4.3 | Preis wird durch Nutzer- und Mandantenmodell getrieben; Externe (4.3) zählen mit | Named-User; Volumen unkritisch (hoch); bei mandantenbasierter Lizenzierung schlagen >100 Gesellschaften durch | – |

### 4.2 Weitere offene Themen aus Folie 3 und Tabelle1

| Thema | Quelle | Erläuterung |
|---|---|---|
| Zahlungsauslösung Omikron (5.5) | AG Folie 3 | siehe Q5 |
| Property-Manager-Anbindung (4.1) | AG Folie 3 | Must-Have mit N; Prozesszweig „ohne internen Workflow" + Datenrückfluss vom PM |
| BIM4You (5.3) | AG Folie 3 | in der Zielarchitektur Kernintegration, im Katalog Should/leer |
| Offene API und perspektivische ERP-Anbindung (5.4) | AG Folie 3 | Stammdaten-Sync (Kreditoren, Kontenrahmen) mit PM-ERPs |
| 2.8 Standardschlüssel je Gesellschaft | KAT Tabelle1 | nicht auf Folie 4, aber MDIS-intern als Risiko geführt |
| 1.6 Archivexport je Gesellschaft | KAT Tabelle1 | nicht auf Folie 4; relevant bei Verkaufsabsicht |

Die Antworten aus dem Termin werden in der Transkript-Auswertung behandelt; soweit die Briefing-Kurzfassung Annahmen dieses Dokuments bereits berührt, steht das in Kap. 8.8.

### 4.3 Zusätzliche offene Fragen (aus der Konsolidierung abgeleitet) [O]

1. Welches DATEV-Produkt wird genutzt (Rechnungswesen inhouse, Unternehmen online, Kanzlei beim Steuerberater)? Ein DATEV-Mandant je Gesellschaft?
2. Was genau ist das „ER Vorerfassungs-Journal" (Buchung vor Freigabe?) und wer erzeugt die Sonderbuchungsinfos (ARAP/PARP, Rückstellungen, Anzahlungen) – d.velop (Folie 2) oder Bim4You (Folie 3)?
3. Zahlungsweg: d.velop-Zahlungsfreigabe → DATEV-Zahlungsvorschlag → Omikron (Bankübertragung)? Rolle von „BeSync"?
4. Bim4You: vorhandene API? Welche Felder (Projekt, Gewerk/Los, Budgetposition)? Was sind „Umlageinformationen"?
5. Property Manager: Anzahl, Systeme, Anteil „rein verwalteter" Assets, Kennzeichen „fremdverwaltet" am Objekt; sollen deren Rechnungen überhaupt in d.velop archiviert werden?
6. Verträge und Post: Volumen, Vertragsarten, Fristenmanagement (Laufzeit, Kündigung, Wiedervorlage), Papierpost/Scan-Standorte?
7. Kreditorenstamm: je Gesellschaft (DATEV-Mandant) oder konzernweit einheitliche Kreditorennummern? (Testbelege nutzen dieselbe Kreditorennr. 70012 für drei Gesellschaften; die Transkript-Kurzfassung im Briefing spricht von unterschiedlichen Nummern je Gesellschaft und ohne Konsolidierung – siehe Kap. 8.8.)
8. Kontenrahmen (SKR03/SKR04/branchenspezifisch) – einheitlich über alle Gesellschaften?
9. Gesellschaftshierarchie / Segmentzuordnung (Bestand, Privatisierung, Bau) und Verantwortliche je Gesellschaft.
10. Mailsystem (Microsoft 365?) – laut Recherche ist nur M365/Graph für den Mailimport produktiv dokumentiert [A05 7.1].
11. Welche Gesellschaften sind Bauleistende i.S.v. § 13b UStG, welche Objektgesellschaften vermieten nur steuerfrei (relevant für § 13b und die Bauabzugsteuer-Freigrenze) – siehe Kap. 6.4.
12. Altdaten/Archivübernahme, bestehendes DMS.

---

## 5 Bestehendes Demo-Konzept (A06 „Demo-Instanz Livos – Architektur, Konfiguration und Aufbauplan")

Kopfdaten: Kunde „Livos (fiktiver Kunde, Workshop-Szenario)"; Workshop 22.09.2026; Grundlage „Leistungskatalog Rechnungsmanagement (29 Anforderungen), Agenda-Folie, Testdatenset"; Gültigkeit „Nur für die Demo-Instanz. Keine Spezifikation für den Produktivbetrieb."; Stand 18.09.2026 [F: A06 Kopf]. Alle drei docx-Fassungen im Projektordner sind inhaltsgleich [F: META].

### 5.1 Grundsätze [F: A06 Kap. 1]
- „Nichts wird gezeigt, was nicht dreimal funktioniert hat."
- „Was im Leistungskatalog auf N steht, wird nicht eingerichtet" – nur benannt (Kap. 7).
- „Drei Gesellschaften genügen, nicht hundert" – entscheidend: zwei davon mit **derselben Anschrift**.

### 5.2 Roter Faden Agenda ↔ Use Case ↔ Instanz [F: A06 Kap. 2]

| Agenda-TOP (A06-Zählung) | Use Case | In der Instanz nötig | Katalog |
|---|---|---|---|
| 1 d.velop im Überblick | – | Browserzugang, Anmeldung, Mobilansicht | 1.2, 1.3, 5.4 |
| 2 Dokumentenmodell und Strukturen | – | Mandantenmodell, Dokumentarten, Rollen und Rechte | 1.1, 1.5 |
| 3.1 Erfassung und Ablage | UC1, UC2, UC9 | Testpostfach, Belegerkennung, sechs Dokumentarten | 2.1, 2.2, 2.4, 1.7 |
| 3.2 Freigabeprozess | UC3–UC6 | Workflow mit Betragsgrenze, Klärungskorb, Vertretung | 1.4, 1.8, 2.3, 2.6, 3.3, 3.4, 4.3 |
| 3.3 Integration in die Fibu | UC7 | Kontierung, Kostenstellenaufteilung, Exportziel | 2.5, 2.8, 5.1 |
| 3.4 Dashboards und Steuerung | UC8 | Rollendashboards, Belege in vier Zuständen | 3.1, 3.2 |
| 4 Intelligente Postverteilung | UC1, UC9 | Posteingang, Aufgabenzuweisung, Ablage | 2.1, 1.7, 6.1 |
| 5 Dokumenten- und Aktenerstellung | UC9 | Drei Aktentypen, Änderungsprotokoll, Suche | 1.6, 1.4, 6.1 |
| 6 Diskussion und Vorgehen | – | nichts einrichten | 5.4 und die N-Themen |

Die Use Cases UC1–UC9 sind nirgends als Liste definiert; aus der Zuordnung ableitbar [A]: UC1 Erfassung/Mailimport · UC2 Mandantenzuordnung (Beleg 04) · UC3 Klärfall (Beleg 08) · UC4 Prüfung/Kontierung/Aufteilung (Belege 03, 06, 07) · UC5 Freigabe ein-/zweistufig (Belege 01, 02) · UC6 Eskalation/Vertretung · UC7 FiBu-Übergabe · UC8 Dashboards · UC9 Akten/Postverteilung (Dateien 20–24).

### 5.3 Gesellschaften (Mandantenmodell) [F: A06 3.1]

| Kürzel | Gesellschaft | Anschrift | Steuernummer | Rolle in der Demo |
|---|---|---|---|---|
| NORD | Livos Objektgesellschaft Nord mbH | Hafenstraße 22, 20359 Hamburg | 43/123/45678 | Hauptgesellschaft, Kernbeleg |
| SUED | Livos Objektgesellschaft Süd mbH | Leopoldstraße 108, 80802 München | 143/456/78901 | beweist die Trennung |
| BAUP | Livos Bau & Projekt GmbH | Hafenstraße 22, 20359 Hamburg | 43/987/65432 | gleiche Anschrift wie NORD – „der Härtetest" |
| WEST | Livos Projektentwicklung West GmbH | Königsallee 60, 40212 Düsseldorf | — | **NICHT anlegen** – erzeugt den Klärfall |

Kernmaßnahme: Eigenschaft „Gesellschaft" ist Pflichtfeld aus Auswahlliste; Berechtigungen und Workflow-Verzweigung hängen daran („vollständige Antwort auf Anforderung 1.1") [F: A06 3.1].

### 5.4 Benutzer und Rollen [F: A06 3.2]

| Kürzel | Name | Rolle | Aufgabe in der Demo | Status |
|---|---|---|---|---|
| U1 | Maria Lentz | Buchhaltung, Rechnungseingang | prüft Erfassung, kontiert, erste Freigabestufe | Pflicht |
| U2 | Jan Bergmann | Projektleiter | sachliche Prüfung, sieht nur NORD und nur ein Objekt | Empfohlen |
| U3 | Dr. Claudia Renner | Geschäftsführung | zweite Freigabestufe über 10.000 € | Pflicht |
| U4 | Tobias Herwig | Externer Projektsteuerer | Freigabe über Web-Zugang (4.3) | Optional |
| U5 | (Admin) | Administrator | Aufbau/Reset, unsichtbar | Pflicht |

„Härteste Abhängigkeit": ohne U1 und U3 kein Benutzerwechsel, keine Freigabedemo. (A05 ergänzt Gruppen LIV_BUCH, LIV_GF, LIV_NORD_PL.) [F: A06 3.2; A05 3.1]

### 5.5 Dokumentarten (Cloud: „Kategorien") [F: A06 3.3]

| Dokumentart | Wofür | Testdaten | Katalog |
|---|---|---|---|
| Eingangsrechnung | Kernobjekt | Belege 01–10 | 2.1–2.8 |
| Vertrag | Rahmenverträge mit Kreditoren | Datei 20 | 1.7 |
| Auftrag | Auftragsbestätigungen als Prüfgrundlage | Datei 21 | 1.7 |
| Nachweis | Lieferscheine, Aufmaße, Abnahmen | Datei 22 | 1.7 |
| Korrespondenz | E-Mails zum Vorgang | Datei 23 | 1.7 |
| Bescheinigung | Freistellungsbescheinigung mit Gültigkeitsdatum | Datei 24 | 2.7 |

### 5.6 Eigenschaften der Eingangsrechnung (Plan A06) [F: A06 3.4]

| Eigenschaft | Typ (A06) | Pflicht | Zweck | Katalog |
|---|---|---|---|---|
| Gesellschaft | Auswahlliste | ja | Mandantenschlüssel, steuert Rechte und Workflow | 1.1 |
| Kreditor | Auswahlliste | ja | Kreditorenakte, Kontierungsvorschlag | 2.5 |
| Rechnungsnummer | Text | ja | Dublettenprüfung, Suche | – |
| Rechnungsdatum | Datum | ja | Pflichtangabe § 14 UStG | 2.6 |
| Leistungszeitraum | Text | nein | Pflichtangabe | – |
| Netto / Steuersatz / Steuer / Brutto | Zahl | ja | rechnerische Prüfung, Freigabegrenze | – |
| Fälligkeit | Datum | ja | Liegezeit und Eskalation | 3.3 |
| Skonto | Text | nein | Zahlungsentscheidung | – |
| IBAN | Text | nein | Tiefe der Erkennung | 2.2 |
| Objekt / Bauvorhaben | Auswahlliste | ja | Objektakte, Kostenzuordnung | – |
| Gewerk / Los | Auswahlliste | nein | „Genau das Feld, das BIM4You bräuchte" | 5.3 |
| Kostenstelle mit Anteil | Mehrfachfeld | ja | Aufteilung auf mehrere Kostenstellen | 2.8 |
| Sachkonto | Auswahlliste | nein | Kontierungsvorschlag | 2.5 |
| Belegart | Normal / Abschlag / Schluss | ja | Abschlagsrechnungen | 5.2 |
| Reverse Charge § 13b | Ja / Nein | nein | Belege 06, 07 | – |
| Sicherheitseinbehalt | Zahl | nein | VOB sichtbar machen, ohne zu rechnen | 5.2 |
| Freistellungsbescheinigung geprüft | Ja / Nein | nein | manueller Schritt statt Automatik | 2.7 |
| Status | systemgesteuert | ja | Dashboard und Managementsicht | 3.2 |

**Tatsächlich im Cloud-Tenant vorgesehen** (CP, laut LM umgesetzt als 8 Wertemengen, 26 Eigenschaften, 9 Kategorien) [F: CP Abschn. 2–4; LM]:
- Wertemengen: Livos Gesellschaft (3 Werte, WEST bewusst fehlend) · Livos Kreditor (5) · Livos Objekt (BV Hafenstraße 22, BV Leopoldstraße 108, BV Königsallee 60) · Livos Gewerk (Rohbau, Elektro, Ausbau, Reinigung, Beratung, Versorgung) · Livos Belegart (Normal, Abschlagsrechnung, Schlussrechnung, Gutschrift) · Livos Sachkonto (0700 Bauten auf eigenen Grundstücken, 4240 Strom/Gas/Wasser, 4250 Reinigung, 4260 Instandhaltung, 4950 Rechts- und Beratungskosten) · Livos Kostenstelle (KST-1000 Verwaltung, KST-2000 Objektbetrieb Nord, KST-2100 Objektbetrieb Süd, KST-3000 Projektentwicklung) · Livos Ja Nein.
- 26 Eigenschaften (u.a. Beträge als **Währung**, Kostenstelle als Text mit **Mehrere Werte**, Reverse Charge 13b / FSB geprüft über Wertemenge Ja/Nein, zusätzlich Gültig bis, Vertragsnummer, Auftragsnummer, Betreff, Absender, Dokumentdatum); **kein Status-Feld** („Workflowstatus" existiert).
- 9 Kategorien: 6 Dokumentarten (Livos Eingangsrechnung, Vertrag, Auftrag, Nachweis, Korrespondenz, Bescheinigung) + 3 Aktenarten (Livos Gesellschaftsakte, Kreditorenakte, Objektakte).
- Pflichtfelder Eingangsrechnung: Gesellschaft, Kreditor, Rechnungsnummer, Rechnungsdatum, Nettobetrag, Bruttobetrag, Fälligkeitsdatum, Objekt, Kostenstelle, Belegart.

### 5.7 Akten [F: A06 3.5]
Drei Aktentypen, **„Sichten, keine Ablageorte"** – dasselbe Dokument erscheint in mehreren Akten:
- **Gesellschaftsakte**: alle Dokumente einer Gesellschaft, quer über Kreditoren und Objekte.
- **Kreditorenakte**: alle Dokumente eines Lieferanten inkl. Rahmenvertrag und Freistellungsbescheinigung.
- **Objektakte**: alle Dokumente zu einem Bauvorhaben, quer über Kreditoren.
Minimum: Gesellschaftsakte NORD, Kreditorenakte Musterbau GmbH (Rahmenvertrag, AB, drei Rechnungen, FSB nebeneinander – „verkauft 1.7 und 6.1"), Objektakte BV Hafenstraße 22.

### 5.8 Workflows [F: A06 3.6]

| ID | Workflow | Auslöser | Ablauf | Katalog | Status |
|---|---|---|---|---|---|
| W1 | Standardfreigabe | Beleg mit gültiger Gesellschaft | Erfassung → Prüfung U1 → Kontierung U1 → Freigabe U3 → Export | 1.4, 2.6 | Pflicht |
| W2 | Zweite Freigabestufe | Bruttobetrag über 10.000 € | zusätzliche Freigabe durch U3 | 1.4 | Pflicht |
| W3 | Klärfall | Gesellschaft nicht zuordenbar | Klärungskorb bei U1, kein Freigabelauf | 2.3 | Pflicht |
| W4 | Eskalation | Beleg länger als 3 Tage unbearbeitet | Benachrichtigung an Vertretung | 3.3 | Empfohlen |
| W5 | Vertretung | Abwesenheit aktiviert | Aufgaben laufen an Vertreter | 3.4 | Empfohlen |
| W6 | Fremdverwaltung | Objekt als fremdverwaltet markiert | kein interner Lauf, Ausleitung in Sammelkorb | 4.1 teilw. | Optional |

„Die wichtigste Zahl der ganzen Instanz: 10.000 Euro brutto" – Belege 01, 06, 07 zweistufig, übrige einstufig. W4 wird nur gezeigt (Einstellung), nicht live abgewartet [F: A06 3.6].

### 5.9 Berechtigungen [F: A06 3.7]

| Regel | Wer | Sieht | Belegt |
|---|---|---|---|
| R1 | U1 Buchhaltung | Eingangsrechnungen aller drei Gesellschaften | zentrale Verwaltbarkeit (1.1) |
| R2 | U2 Projektleiter | nur NORD, nur Objekt BV Hafenstraße 22 | strikte Trennung (1.1, 1.5) |
| R3 | U3 Geschäftsführung | alles, darf freigeben, aber nicht kontieren | Rollentrennung (1.5) |

„Regel R2 ist die wertvollste Minute des Workshops" – als U2 existieren SÜD-Belege nicht.

### 5.10 Dashboard-Konzept [F: A06 Kap. 4]
- **U1 Sachbearbeiter:** Meine Aufgaben (3.1) · Neu eingegangen · Klärfälle (Beleg 08) · Zuletzt bearbeitet · Schnellsuche.
- **U3 Freigeber:** Meine Freigaben · Freigaben über 10.000 € (1.4) · Länger als 3 Tage bei mir (3.3).
- **Management/Controlling:** Alle Belege nach Status (3.2) · Belege je Gesellschaft · Top 10 nach Liegezeit · Volumen laufender Monat.
- Vorbehalt im Dokument selbst: Widget-Typen „nicht geprüft"; nicht verhandelbar: jede Kachel gefüllt, Managementsicht filterbar nach Gesellschaft. (**Überholt**, siehe Kap. 8 W38.)

### 5.11 Datenbestand und Ausgangszustände [F: A06 Kap. 5]

| Beleg | Gesellschaft | Brutto | Zustand am Workshop-Morgen | Zweck |
|---|---|---|---|---|
| 01 RE-2026-1041 | NORD | 14.756,00 € | NICHT im System | kommt live per Mail – Kernbeleg |
| 02 RE-2026-1042 | NORD | 1.190,00 € | Abgeschlossen | Historie, Kreditorenakte |
| 03 RE-2026-0338 | SUED | 3.570,00 € | In Kontierung | Kostenstellenaufteilung |
| 04 RE-2026-0077 | BAUP | 2.380,00 € | In Prüfung | Zuordnungsbeweis gleiche Anschrift |
| 05 RE-2026-5510 | NORD | 476,00 € | Abgeschlossen | Kleinbetrag, einstufig |
| 06 RE-2026-1039 | SUED | 25.000,00 € | Freigegeben | Reverse Charge § 13b |
| 07 RE-2026-1055 | SUED | 31.500,00 € | Wartet auf Freigabe Stufe 2 | Betragsgrenze im Dashboard |
| 08 RE-2026-1060 | WEST (unbekannt) | 4.998,00 € | NICHT im System | kommt live, Klärfall |
| 09 XRechnung | NORD | 1.190,00 € | Importiert, abgeschlossen | E-Rechnungsfähigkeit (2.4) |
| 10 ZUGFeRD | NORD | 14.756,00 € | nur wenn Import getestet | sonst weglassen |
| 20–24 Nachweise | – | – | in den Akten abgelegt | Aktendemo (UC9) |

Faustregel: mindestens vier verschiedene Zustände gleichzeitig sichtbar.

### 5.12 Demo-Ablauf (45 Minuten) [F: A06 Kap. 6]
0–3 TOP 1 Anmelden/Dashboard (U1) · 3–8 TOP 2 Beleg/Eigenschaften, kurz als U2: SÜD unsichtbar · 8–12 TOP 3.1 Mail → Beleg 01 erscheint · 12–15 TOP 3.2 Beleg 08 Klärfall, manuell zuordnen · 15–20 Beleg 01 prüfen, Vorschlagswert übersteuern, auf zwei Kostenstellen aufteilen · 20–25 Freigabe U1 → Benutzerwechsel → U3 · 25–28 TOP 3.3 Kontierung/Übergabeziel, Zahlungsfreigabe benennen (U3) · 28–32 TOP 3.4 Managementsicht (U3) · 32–38 TOP 4 Nicht-Rechnungsdokument erfassen/qualifizieren/zuweisen · 38–45 TOP 5 Kreditorenakte Musterbau, Volltextsuche, Änderungsprotokoll · ab 45 TOP 6 Schnittstellenthemen nur ansprechen.

### 5.13 Bewusst nicht eingerichtet [F: A06 Kap. 7]

| Thema | Katalog (laut A06) | Warum nicht | Sprachregelung |
|---|---|---|---|
| Zahlungsauslösung Omikron | 5.5 — N | eigene Schnittstelle | „Prozess endet mit der Zahlungsfreigabe, Auslösung nachgelagert" |
| BIM4You | 5.3 — N | eigene Schnittstelle | „Gewerk und Los werden erfasst und stehen über die offene API bereit" |
| Property-Manager-Übergabe | 4.1 — N | je System eigene Schnittstelle | „Prozesszweig abbildbar, Datenübergabe ist Projektthema" |
| VOB-Kumulation, Einbehalte | 5.2 — N | Funktion eines Bau-ERP | „Belegart und Einbehalt als Eigenschaft, gerechnet wird außerhalb" |
| Automatik Freistellungsbescheinigung | 2.7 — **A** | Individualentwicklung | „Bescheinigung liegt am Kreditor mit Gültigkeitsdatum, Prüfung bleibt Workflowschritt" |
| DATEV-Übergabe live | 5.1 — S | Connector womöglich nicht konfiguriert | „Exportergebnis/Screenshot zeigen, Frequenz zusagen lassen" |

### 5.14 Aufbauplan und Abnahme [F: A06 Kap. 8–9]
- **P0 (blockierend):** Cloud vs. On-Prem klären · U1/U3 anlegen · aktive Module prüfen (documents, inbound, mail dispatcher, Rechnungsmodul) · Testpostfach/Importintervall · bestehenden Freigabeworkflow prüfen.
- **P1 (Fundament):** 3 Gesellschaften (WEST nicht) · 5 Kreditoren · Dokumentart Eingangsrechnung (2 h) · 5 weitere Dokumentarten · Freigabegrenze 10.000 € · W1 (2 h) · W3 · R2 · 3 Akten.
- **P2 (Daten/Dashboards):** Belege 02–07 und 09 importieren und in Zielzustände bringen · Nachweise 20–24 ablegen · Dashboards U1/U3/Management · W4/W5 · XRechnung/ZUGFeRD testen.
- **P3 (Probe):** Ablauf 2× mit Stoppuhr · Fallback-Screenshots · Generalprobe · Reset (Belege 01/08 entfernen) · zweiter Browser mit U3. Summe Pflichtaufgaben ca. 16 Stunden.
- **Abnahme-Checkliste (13 Punkte):** Beleg 01 per Mail → NORD · Beleg 08 → Klärungskorb, manuell zuordenbar · Beleg 04 → BAUP trotz gleicher Anschrift · Übersteuerung im Protokoll sichtbar · Beleg 01 auf zwei Kostenstellen · Freigabe U1 → U3 in einem Durchlauf · U2 sieht keine SÜD-Belege · Dashboard U1 ≥ 3 gefüllte Kacheln · Managementsicht ≥ 4 Status · filterbar nach Gesellschaft · Kreditorenakte Musterbau vollständig · Volltextsuche über Rechnungsnummer/Betrag · Fallback-Screenshots.

**Rahmenbedingung Demo-Tenant** [F: LM; CP Abschn. 0]: `mdisconsulting.d-velop.cloud` ist produktiv genutzt (102 Belege im Umlauf, ein aktiver Workflow, gefülltes Rechnungseingangsbuch), Kollegen arbeiten darin; nur additiv anlegen, alles mit „Livos" im Namen; smart-invoice-Konfiguration (Workflow, Freigabematrix, `si_`-Gruppen) **nicht anfassen**; keine Benutzer/Berechtigungen im Rahmen von „Aufgabe 2".

---

## 6 Testdaten

Allgemein: 15 Belege/Nachweise + LIESMICH + 2 Stammdaten-CSV = 18 Dateien; alle Firmen, Personen, Adressen, Steuernummern, Bankverbindungen **erfunden**; jedes PDF mit Fußzeile „TESTBELEG" [F: TDL Kopf; LM Tabelle Nr. 07]. Kopien der Belege liegen zusätzlich in `_Upload_Rechnungen` (01–10) und `_Upload_Dokumente` (20–24), angelegt am 22.09.2026 [F: META].

### 6.1 Gesellschaften (`00_Stammdaten_Gesellschaften.csv`, alle Felder) [F: TD]

| Kürzel | Gesellschaft | Straße | PLZ | Ort | Steuernummer | USt-IdNr | Kundennummer | Hinweis |
|---|---|---|---|---|---|---|---|---|
| NORD | Livos Objektgesellschaft Nord mbH | Hafenstrasse 22 | 20359 | Hamburg | 43/123/45678 | DE311222333 | LOG-NORD-0041 | Hauptgesellschaft der Demo |
| SUED | Livos Objektgesellschaft Sued mbH | Leopoldstrasse 108 | 80802 | Muenchen | 143/456/78901 | DE322333444 | LOG-SUED-0022 | Zweite Gesellschaft, fuer Benutzer- und Mandantentrennung |
| BAUP | Livos Bau & Projekt GmbH | Hafenstrasse 22 | 20359 | Hamburg | 43/987/65432 | DE333444555 | LBP-0007 | ACHTUNG gleiche Anschrift wie NORD - Testfall fuer Anforderung 2.2 |
| WEST | Livos Projektentwicklung West GmbH | Koenigsallee 60 | 40212 | Duesseldorf | 133/555/12345 | DE344555666 | -- nicht angelegt -- | NICHT anlegen - erzeugt den Klaerfall in UC3 |

„Kundennummer" = Kundennummer der Gesellschaft **beim Lieferanten** (steht auf den Rechnungen) [F: TD Belege].

### 6.2 Kreditoren (`00_Stammdaten_Kreditoren.csv`, alle Felder + Angaben aus den Belegen) [F: TD]

| Kreditorennr | Name | Straße | PLZ | Ort | USt-IdNr | Steuernummer | IBAN | BIC | E-Mail | Bank (Beleg) | Tel. / Vertretung / Register (Beleg) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 70012 | Musterbau GmbH | Gewerbestrasse 14 | 21079 | Hamburg | DE201456789 | 41/222/33445 | DE34 2005 0550 1234 5678 90 | HASPDEHHXXX | rechnung@musterbau-test.de | Hamburger Sparkasse | +49 40 5550-140 · Katrin Ohlsen · HRB 118234 AG Hamburg |
| 70044 | Elektro Nordlicht GmbH | Lindenweg 7 | 22765 | Hamburg | DE202567890 | 42/333/44556 | DE88 2004 0000 8765 4321 00 | COBADEHHXXX | buchhaltung@nordlicht-test.de | Commerzbank Hamburg | +49 40 4441-77 · Sven Rieckmann · HRB 92117 AG Hamburg |
| 70103 | Stadtwerke Beispielstadt AG | Energieplatz 1 | 80331 | Muenchen | DE203678901 | 143/111/22334 | DE67 7015 0000 1111 2222 33 | SSKMDEMMXXX | service@stadtwerke-test.de | Stadtsparkasse Muenchen | +49 89 2000-500 · Vorstand Dr. Petra Lang · HRB 45012 AG Muenchen |
| 70210 | Recht & Partner mbB | Ballindamm 3 | 20095 | Hamburg | DE204789012 | 41/777/88990 | DE65 2003 0000 5555 6666 77 | HYVEDEMM300 | office@recht-partner-test.de | HypoVereinsbank | +49 40 3030-10 · Partner Dr. Malte Brinkmann · PR 2210 AG Hamburg |
| 70355 | Reinigungsservice Blitzblank GmbH | Industriestrasse 55 | 21107 | Hamburg | DE205890123 | 41/444/55667 | DE51 2001 0020 0099 8877 66 | PBNKDEFFXXX | fakturierung@blitzblank-test.de | Postbank Hamburg | +49 40 7788-0 · Ayse Demir · HRB 134902 AG Hamburg |

IBAN-Prüfziffern der Stammdaten: alle fünf gültig [F: META].

### 6.3 Belege und Nachweise

**Eingangsrechnungen** [F: TD, TDL 2]:

| Nr | Rechnungsnr. / Typ | Kreditor (Nr.) | Empfänger | Re-Datum | Leistungszeitraum | Netto | USt | Brutto | Fällig | Skonto | Objekt / Gewerk | Besonderheit | UC / Katalog |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 01 | RE-2026-1041, Rechnung | Musterbau (70012) | NORD | 12.09.2026 | 01.08.–31.08.2026 | 12.400,00 | 19 % = 2.356,00 | 14.756,00 | 26.09.2026 | 2 % bis 19.09.2026 | BV Hafenstrasse 22, Sanierung Treppenhaus / Rohbau, Los 3 | Kernbeleg, > 10.000 € → zweistufig; 4 Positionen (Abbruch, Stahlbetontreppe, Malerarbeiten, Baustelleneinrichtung/Gerüst) | UC1, 2, 4, 5 |
| 02 | RE-2026-1042, Rechnung | Elektro Nordlicht (70044) | NORD | 11.09.2026 | 03.09.2026 | 1.000,00 | 19 % = 190,00 | 1.190,00 | 25.09.2026 | – | BV Hafenstrasse 22, Allgemeinstrom | einstufig | UC5 |
| 03 | RE-2026-0338, Rechnung | Stadtwerke (70103) | SUED | 05.09.2026 | 01.08.–31.08.2026 | 3.000,00 | 19 % = 570,00 | 3.570,00 | 19.09.2026 | – | „Aufteilung auf Kostenstellen Haus A / Haus B / Allgemein" | Aufteilung nach Verbrauch Haus A 55 %, Haus B 45 % | UC4 / 2.8 |
| 04 | RE-2026-0077, Rechnung | Recht & Partner (70210) | BAUP | 10.09.2026 | August 2026 | 2.000,00 | 19 % = 380,00 | 2.380,00 | 24.09.2026 | – | Ankauf Objekt Neue Strasse 4 | Zuordnungstest: Anschrift identisch mit NORD (Hinweistext auf dem Beleg) | UC2 / 2.2 |
| 05 | RE-2026-5510, Rechnung | Blitzblank (70355) | NORD | 01.09.2026 | August 2026 | 400,00 | 19 % = 76,00 | 476,00 | 15.09.2026 | – | BV Hafenstrasse 22, Unterhaltsreinigung | Dashboard-Füllmaterial | – |
| 06 | RE-2026-1039, **Abschlagsrechnung Nr. 1** | Musterbau (70012) | SUED | 28.08.2026 | 01.07.–31.08.2026 | 25.000,00 | 0,00 (**§ 13b Abs. 2 Nr. 4 i.V.m. Abs. 5 UStG**) | 25.000,00 | 11.09.2026 | – | BV Leopoldstrasse 108, Neubau Haus C / Rohbau | Leistungsstand 25 % der Auftragssumme, Bezug Auftrag A-2026-0912 | UC4 |
| 07 | RE-2026-1055, **Abschlagsrechnung Nr. 2, kumuliert** | Musterbau (70012) | SUED | 15.09.2026 | 01.09.–14.09.2026 | 31.500,00 (= 60.000 kumuliert − 25.000 1. Abschlag − 3.500 „5 % Sicherheitseinbehalt Gewaehrleistung") | 0,00 (§ 13b) | 31.500,00 | 29.09.2026 | – | BV Leopoldstrasse 108, Neubau Haus C / Rohbau | „Kumulierte Abrechnung nach VOB/B"; Sicherheitseinbehalt 5 % bis 30.09.2028; zeigt bewusst die Grenze (5.2 = N) | UC4 / 5.2 |
| 08 | RE-2026-1060, Rechnung | Musterbau (70012) | **WEST** (nicht angelegt) | 16.09.2026 | 07.09.–14.09.2026 | 4.200,00 | 19 % = 798,00 | 4.998,00 | 30.09.2026 | – | BV Koenigsallee 60, Projektentwicklung | Klärfall; Kundennummer „-- nicht angelegt --" | UC3 / 2.3 |
| 09 | RE-2026-1042 als **XRechnung** (UBL, `xrechnung_3.0`, Peppol-Profil) | Elektro Nordlicht | NORD | 2026-09-11 | – | 1.000,00 | 190,00 | 1.190,00 | 2026-09-25 | – | Note „BV Hafenstrasse 22" | reines XML; BuyerReference = LOG-NORD-0041; Käufer-USt-IdNr DE311222333; **Zahlungs-IBAN DE45200400008765432100** | UC1 / 2.4 |
| 10 | RE-2026-1041 als **ZUGFeRD/Factur-X** (EN16931) | Musterbau | NORD | 12.09.2026 | Lieferdatum 31.08.2026 | 12.400,00 | 2.356,00 | 14.756,00 | 26.09.2026 | (nur im PDF) | wie 01 | PDF mit eingebettetem `factur-x.xml`, **kein PDF/A-3**; XML mit nur **einer** Sammelposition; **Zahlungs-IBAN DE02200505501234567890** | UC1 / 2.4 |

**Nachweise** [F: TD, TDL 3]:

| Nr | Dokument | Kerninhalt |
|---|---|---|
| 20 | Rahmenvertrag Bauleistungen RV-2026-004 | Auftraggeber **NORD**, Auftragnehmer Musterbau; Beginn 01.01.2026; Laufzeit 24 Monate, Verlängerung je 12 Monate; Kündigungsfrist 3 Monate zum Quartalsende; „Naechster Pruefungstermin: 01.10.2027"; Einheitspreise (Anlage 1); Abschläge kumuliert nach VOB/B; Zahlungsziel 14 Tage netto, 2 % Skonto binnen 7 Tagen; 5 % **der Auftragssumme** Sicherheit für Gewährleistung; Gewährleistung 4 Jahre ab Abnahme; § 13b: AG schuldet USt bei Bauleistungen; AN legt FSB § 48b EStG vor; unterzeichnet 18.12.2025 |
| 21 | Auftragsbestätigung A-2026-0912 | Auftraggeber **SUED**; BV Leopoldstrasse 108, Neubau Haus C; Gewerk/Los: Rohbau, **Los 1**; Auftragsdatum 24.06.2026; Ausführung 01.07.–31.12.2026; Auftragssumme netto 100.000 €; § 13b; „Grundlage: Rahmenvertrag RV-2026-004"; Abschläge kumuliert gem. VOB/B § 16; Sicherheitseinbehalt 5 % **der jeweiligen Abschlagssumme**; Liste der gestellten Rechnungen 1039 (25 %) und 1055 (60 %) |
| 22 | Lieferschein LS-2026-0451 | Elektro Nordlicht an NORD, 03.09.2026, BV Hafenstrasse 22 Technikraum UG, zu RE-2026-1042, „Leistung erbracht und abgenommen" |
| 23 | E-Mail Rechnungsübersendung | Von `buchhaltung@musterbau-test.de` an `rechnungseingang@livos-test.de`, Sa 12.09.2026 09:14, Betreff „Rechnung RE-2026-1041 - BV Hafenstrasse 22, Treppenhaus", Anlage RE-2026-1041.pdf |
| 24 | Freistellungsbescheinigung § 48b Abs. 1 Satz 1 EStG | Finanzamt Hamburg-Mitte; Sicherheitsnummer HH 41222 33445 / 2026; Musterbau, StNr 41/222/33445; gültig 01.01.–31.12.2026; Umfang: alle Bauleistungen, unbeschränkt; berechtigt, vom Steuerabzug 15 % abzusehen |

### 6.4 Was die Testdaten über reale Anforderungen verraten

Die Daten sind fiktiv, bilden aber typische Livos-Fälle nach, die der Katalog nennt oder impliziert. Ableitungen sind als [A] gekennzeichnet, soweit sie über den Wortlaut hinausgehen.

| # | Befund aus den Testdaten | Abgeleitete Anforderung an das Zielbild | Katalog / Architektur |
|---|---|---|---|
| T1 | NORD und BAUP haben **identische Anschrift**, unterscheiden sich aber in **Name, Kundennummer (LOG-NORD-0041 vs. LBP-0007), Steuernummer, USt-IdNr.** | Mandantenerkennung muss neben Anschrift den **Namen** (d.velop-Logik) und idealerweise die **Kundennummer** auswerten; Alternative: Alias-Postfach je Gesellschaft. Bei E-Rechnungen stehen **Käufer-USt-IdNr. und BuyerReference strukturiert** im XML → dort ist eine eindeutige Zuordnung möglich [A] | 2.1, 2.2 |
| T2 | Rechnung an **nicht angelegte Gesellschaft** (WEST) | Klärfall-Prozess mit Zuordnungsmöglichkeit, ggf. Anlage einer neuen Gesellschaft; Fallback „Standardmandant" vs. bewusster Klärkorb | 2.3 |
| T3 | **§ 13b UStG** (06, 07): USt 0, Pflichthinweis „Steuerschuldnerschaft des Leistungsempfängers" | Erkennung RC-Kennzeichen; Plausibilitätsprüfung (RC nur zulässig, wenn der Empfänger selbst nachhaltig Bauleistungen erbringt – § 13b Abs. 5 S. 2 UStG) → **Stammdatum je Gesellschaft „Bauleistender ja/nein"**; korrekter DATEV-Steuerschlüssel für § 13b [A] | 2.6, 5.1 |
| T4 | **Kumulierte Abschlagsrechnungen nach VOB/B** (06 → 07), Leistungsstand %, Abzug Vorabschläge, Bezug auf Auftrag | Belegart (Abschlag/Schluss), Verknüpfung Auftrag ↔ Rechnungen, rechnerische Prüfung gegen Auftragssumme und bisherige Abschläge – laut Zielarchitektur in **Bim4You** (Budgetabgleich), Ergebnis als Einbehalt-/Kürzungsinfo zurück | 5.2, 5.3; ARCH Folie 2/3 |
| T5 | **Sicherheitseinbehalt 5 %** „bis 30.09.2028" | Vormerkung/Fristüberwachung für die spätere Auszahlung; Übergabe an DATEV (Einbehaltkonto) [A] | 5.2; ARCH „Einbehalt- und Kürzungs-Informationen" |
| T6 | **Freistellungsbescheinigung § 48b EStG** mit Gültigkeit bis 31.12.2026, sonst 15 % Steuerabzug | FSB am Kreditor mit Gültigkeitsdatum; bei Bauleistungen automatische Prüfung „gültige FSB liegt vor"; sonst Abzugsvorschlag 15 %; Wiedervorlage vor Ablauf. Fachlich zu berücksichtigen: Freigrenzen nach § 48 Abs. 2 EStG (5.000 € bzw. 15.000 € bei ausschließlich steuerfrei vermietenden Empfängern) [A] | 2.6, 2.7 |
| T7 | **XRechnung (UBL, XRechnung 3.0)** und **ZUGFeRD/Factur-X (EN16931)** | Formatvalidierung, Visualisierung, **Abgleich XML ↔ PDF** (bei ZUGFeRD weicht die Positionsstruktur ab) und **IBAN-Abgleich gegen Kreditorenstamm** (beide XML-IBANs weichen ab und sind ungültig) [F: META] | 2.4, 2.6 |
| T8 | **Kostenstellensplit nach Verbrauch** Haus A 55 % / Haus B 45 % (03) | Positions-/Prozentaufteilung; Standardschlüssel je Objekt/Gesellschaft; Kostenstellen auf Ebene **Haus/Objekt** [A] | 2.8 |
| T9 | Jede Rechnung trägt „Objekt / Projekt" und teils „Gewerk / Los" | Objekt-/Projekt- und Gewerk/Los-Erkennung als Kernmetadaten (Objektakte, Bim4You-Übergabe) | 5.3; A06 3.4 |
| T10 | **Skonto** (01: 2 % bis 19.09.2026) | Skontofrist in Zahlungsfreigabe/Priorisierung, Eskalation vor Skontoablauf [A] | 3.3, 5.5 |
| T11 | „Kreditorennr. beim Empfaenger" steht auf jeder Rechnung; **dieselbe Nummer 70012** für NORD, SUED und WEST | Kreditorennummern im DATEV-Kreditorenbereich (7xxxx). Die gleiche Nummer über drei Gesellschaften ist eine **Testvereinfachung**: laut Transkript-Kurzfassung im Briefing hat derselbe Lieferant in verschiedenen Gesellschaften **unterschiedliche** Kreditorennummern (70000er intern, 80000er aus Hausverwaltungen) → Kreditorenerkennung braucht eine gesellschaftsübergreifende Lieferantenidentität mit Mapping auf die DATEV-Kreditorennummer je Mandant [A; Hinweis: 00_BRIEFING „Erkenntnisse aus dem Transkript"] | 2.2, 2.5, 5.4 |
| T12 | Rahmenvertrag, Auftragsbestätigung, Lieferschein, Begleit-E-Mail | Nachweise am Vorgang/in der Akte; Vertragsdaten mit **Fristen** (Laufzeit, Verlängerung, Kündigung, Prüfungstermin) → Vertragsmanagement im Verträge-Prozess | 1.7, 6.1; ARCH Folie 4 |
| T13 | Zentrale Eingangsadresse `rechnungseingang@…`; Absender `buchhaltung@musterbau-test.de` ≠ Stamm-E-Mail `rechnung@…` | Sammelpostfach; Absender-Whitelist/Kreditorenerkennung darf nicht nur an der Stamm-E-Mail hängen [A] | 2.1 |
| T14 | **Dubletten**: 09 = RE-2026-1042 (wie 02), 10 = RE-2026-1041 (wie 01) | Dublettenprüfung über Kreditor + Rechnungsnummer + Betrag, auch **kanalübergreifend** (PDF vs. E-Rechnung) [A] | 2.6 |
| T15 | Leistungsarten: Instandhaltung (01, 02, 05), Neubau (06, 07), Ankaufsberatung (04), Versorgung (03) | Kontierungslogik muss **Aktivierung (Herstellungs-/Anschaffungsnebenkosten) vs. Aufwand** unterscheiden; Sachkonten-Wertemenge ist SKR03-nah (42xx, 4950) [A] | 2.5 |
| T16 | Freigabegrenze 10.000 € (01, 06, 07 zweistufig) | Betragsabhängige Freigabestufen je Gesellschaft | 1.4 |
| T17 | Beleg 04: Projektgesellschaft (BAUP) mit Rechtsberatung zum **Ankauf** | Transaktions-/Ankaufskosten je Gesellschaft; passt zum Geschäftsmodell mit Käufen/Verkäufen [A] | 1.6 |

**Nicht in den Testdaten abgedeckt** (TDL 6 bietet Erweiterungen an) [F/A]: Gutschrift, Mahnung, Schlussrechnung, Rechnung mit fehlender Pflichtangabe, gescannte Papierbelege (OCR-Realismus), mehrere Steuersätze, ausländische Kreditoren (§ 13b Abs. 1), Rechnungen für fremdverwaltete Objekte (4.1), Umlagefälle, Vertrags- und Postdokumente außerhalb des Rechnungskontexts.

---

## 7 Anforderungs-Clustering

### 7.1 Cluster-Übersicht

| # | Cluster | Kernanforderung (verdichtet) | Must-Haves | Weitere Katalog-IDs | Zusätzliche Anforderungen aus Architektur / Testdaten | Konsolidierte Einschätzung |
|---|---|---|---|---|---|---|
| C1 | **Struktur / Mandanten** | >100 Gesellschaften in einem zentral verwalteten System, Daten/Workflows/Rechte je Gesellschaft strikt getrennt | **1.1** | (1.4, 2.8, 3.3 „je Gesellschaft") | Gesellschaft als Pflicht-Metadatum; Hierarchie (smart invoice `parent_id`); Stammdatum „Bauleistender § 13b" je Gesellschaft (T3) | K; Grundsatzfrage Q1 offen |
| C2 | **Erfassung / Eingang** | Automatischer Import aus zentralen Postfächern inkl. Sammelpostfach; E-Rechnungen voll unterstützt | **2.1, 2.4** | – | Eingangskanäle für Verträge und Post (ARCH Folie 4/5); Absender ≠ Stamm-E-Mail (T13) | S/K; Alias-Postfächer als Lösung für Sammelpostfach |
| C3 | **Klassifizierung / KI / Prüfung** | Erkennung Pflichtangaben + Empfänger-Gesellschaft; Klärfall; lernende Kontierungsvorschläge; automatische steuerliche Prüfung | **2.2, 2.3, 2.5, 2.6** | (5.3 KI-Erkennung Gewerk/Los) | Vorqualifikation / Detailqualifikation (ARCH Folie 3); Dubletten (T14); IBAN-Abgleich (T7); §13b-Plausibilität (T3) | 2.2 nur mit Vorbehalt (Name + Anschrift) |
| C4 | **Workflow / Freigabe** | Eigenständige Prüf-/Freigabeworkflows je Gesellschaft, Betragsgrenzen, Personenketten, Übersteuerung, Eskalation, Vertretung | **1.4, 1.8, 3.3, 3.4** | – | Trennung fachliche Freigabe / Zahlungsfreigabe (ARCH Folie 3); Bim4You-Freigabestatus als Eingang in die fachliche Freigabe | S/K; Eskalation aufwendig, ungeplante Vertretung offen |
| C5 | **FiBu / DATEV** | Automatisierte, mehrfach tägliche Übergabe aller Rechnungen inkl. Beleg; Kostenstellenaufteilung mit Standardschlüsseln je Gesellschaft | **2.8, 5.1** | – | ER-Vorerfassungsjournal, Verbuchung nach Freigabe, Sonderbuchungsinfos ARAP/PARP, Rückstellungen, Anzahlungen (ARCH Folie 2/3); Aktivierung vs. Aufwand (T15) | S laut Katalog, aber DATEV-Doku gesperrt; 2.8-Standardschlüssel fraglich |
| C6 | **Zahlung / Omikron** | Zahlungen nach Freigabe automatisch auslösen (berechtigte Nutzer) | **5.5** | – | Zahlungsfreigabe in d.velop, Zahlungsjournal → DATEV, Durchführung in DATEV, Zahlungsrückmeldung ← DATEV (ARCH); Skonto (T10) | **Must-Have unbewertet**; Architektur (DATEV) ≠ Katalog (Omikron) |
| C7 | **Bim4You / Bau** | Budgetcontrolling-Anbindung, VOB-Abschläge, Sicherheitseinbehalte, Freistellungsbescheinigung | – | 2.7 (Could), 5.2 (Should), 5.3 (Should) | Bidirektionale Integration: ER-Journale →, Einbehalt-/Kürzungs-, Umlageinfos und Freigabestatus ← (ARCH Folie 2); Bau-Schleife im ER-Prozess (Folie 3); T3–T6 | Katalog „optional", Architektur „Kern" → Priorität klären |
| C8 | **Property Management** | Rechnungen fremdverwalteter Assets ohne internen Workflow an PM-Systeme; Datenrückfluss; perspektivisch Stammdaten-Sync | **4.1** | 5.4 (Could) | Kennzeichen „fremdverwaltet" am Objekt (A06 W6) | **Must-Have mit N**; fehlt in der Zielarchitektur |
| C9 | **Verträge** | (keine eigene Katalog-Anforderung) Eingang → Verarbeitung → Verteilung → Klassifizierung → fachliche Freigabe → Archivierung | – | (1.7, 6.1) | Vertragsfristen (T12); Kategorie „Vertrag" mit Gültig bis (CP) | Scope-Erweiterung durch MDIS; Anforderungen erst zu erheben |
| C10 | **Post** | (keine eigene Katalog-Anforderung) Eingang → Verarbeitung → Klassifizierung → Verteilung → Archivierung | – | (2.1, 1.7, 6.1 laut AG Folie 2) | Aufgabenzuweisung bei Verteilung (AG Folie 2, A06 Kap. 6 TOP 4) | Scope-Erweiterung; Volumen/Kanäle offen |
| C11 | **Akten / Archiv / GoBD** | Lückenlose, manipulationssichere Protokollierung; GoBD; Export je Gesellschaft bei Verkauf; Nachweise anhängen; DMS-Nutzung | **1.6** | 1.7 (Should), 6.1 (Could) | Akten als Sichten (Gesellschaft, Kreditor, Objekt) (A06 3.5); Archivierung als Endschritt aller drei Prozesse (ARCH) | S; Export je Gesellschaft = Aufwand/Vertragsthema |
| C12 | **Berechtigungen / Externe** | Feingranulare Rechte intern/extern; Kern-Partner mit Web-Zugang; Ad-hoc-Freigabe ohne Lizenz | **1.5, 4.3** | 4.2 (Should) | Rollentrennung Freigeben ≠ Kontieren (A06 R3); Sicht nur auf eigene Gesellschaft/Objekt (R2) | 4.2 ungeklärt (kein Workflow-Freigeben per Link belegt) |
| C13 | **Reporting / Dashboards** | Persönliche Inbox je Nutzer; Management-Gesamtüberblick mit Status, Bearbeiter, Liegezeit | **3.1, 3.2** | – | Managementsicht im Rechnungseingangsbuch (LM, A05 Kap. 10) | 3.2 „Liegezeit" unbelegt; beide nicht auf der Agenda |
| C14 | **Lizenz / Betrieb / API** | Cloud/SaaS, responsiv, App; offene API; Lizenzmodell für ~80 Nutzer | **1.2** | 1.3 (Could), 5.4 (Could) | Lizenz- und Mengengerüst (AG Folie 4); Editionsabhängigkeiten (z.B. „documents business" für Extern Teilen) | S; Lizenzmodell offen (Q6) |

### 7.2 Zuordnung aller 29 Katalog-IDs (Primärcluster; Sekundär in Klammern)

| ID | Primär | Sekundär | ID | Primär | Sekundär |
|---|---|---|---|---|---|
| 1.1 | C1 | (C12) | 2.8 | C5 | (C1) |
| 1.2 | C14 | – | 3.1 | C13 | (C4) |
| 1.3 | C14 | – | 3.2 | C13 | (C1) |
| 1.4 | C4 | (C1) | 3.3 | C4 | (C1) |
| 1.5 | C12 | (C1) | 3.4 | C4 | – |
| 1.6 | C11 | (C1) | 4.1 | C8 | (C4) |
| 1.7 | C11 | (C2, C9) | 4.2 | C12 | (C4, C14) |
| 1.8 | C4 | (C3, C5) | 4.3 | C12 | (C4) |
| 2.1 | C2 | (C1, C10) | 5.1 | C5 | – |
| 2.2 | C3 | (C1) | 5.2 | C7 | (C3) |
| 2.3 | C3 | (C4) | 5.3 | C7 | (C3) |
| 2.4 | C2 | (C3) | 5.4 | C14 | (C8) |
| 2.5 | C3 | (C5) | 5.5 | C6 | (C4) |
| 2.6 | C3 | (C7) | 6.1 | C11 | (C9, C10) |
| 2.7 | C7 | (C3) | | | |

Primärverteilung: C1: 1 · C2: 2 · C3: 4 · C4: 4 · C5: 2 · C6: 1 · C7: 3 · C8: 1 · C9: 0 · C10: 0 · C11: 3 · C12: 3 · C13: 2 · C14: 3 = **29**.

### 7.3 Must-Haves nach Risiko (konsolidiert)

| Risiko | Must-Haves | Begründung |
|---|---|---|
| **hoch** (nicht erfüllt / unbewertet) | 4.1, 5.5 | N bzw. leer; Architektur deckt beide nicht ab |
| **mittel** (S unter Vorbehalt) | 2.2, 2.8, 3.2, 5.1, 1.6 | Steuernummer-Zuordnung, Standardschlüssel, Liegezeit, DATEV-Doku gesperrt, Export je Gesellschaft |
| **mittel** (K/S mit Aufwand) | 1.1, 1.4, 2.3, 3.3, 3.4 | Grundsatzentscheidung Mandantenmodell; Konfigurationsaufwand; ungeplante Vertretung |
| **gering** | 1.2, 1.5, 1.8, 2.1, 2.4, 2.5, 2.6*, 3.1, 4.3 | Standard; *2.6 ohne FSB-Automatik (Widerspruch zu 2.7) |

---

## 8 Widersprüche und Inkonsistenzen zwischen den Quellen

### 8.1 Innerhalb des Leistungskatalogs

| Nr | Thema | Befund | Konsequenz |
|---|---|---|---|
| W1 | 2.6 vs. 2.7 | 2.6 (S) fordert automatische Prüfung „z.B. Freistellungsbescheinigung"; 2.7 (N) sagt, FSB-Automatik ist nicht im Leistungsumfang [F: KAT] | 2.6 auf S mit Vorbehalt (ohne FSB) oder 2.7 anheben |
| W2 | 2.1 Bewertung vs. Notiz | Bewertet S, Notiz: Sammelpostfach-Aufteilung „ist Konfigurationsanteil" [F: KAT] | S/K präzisieren |
| W3 | 1.4 und 3.3 | Bewertet S, beschrieben wird Konfiguration je Workflow; smart-invoice-Vier-Augen ist Vorschau-Feature [F: KAT; A05 Kap. 8; B00 AL] | eher K |
| W4 | 3.4 | K mit Notiz „je Nutzer, geplant" – Anforderung umfasst ausdrücklich den **ungeplanten** Fall (Krankheit) [F: KAT] | Lücke benennen |
| W5 | 2.3 | K „mit Einschränkungen" – Einschränkungen nicht benannt [F: KAT] | konkretisieren |
| W6 | Leere Bewertungen | 4.2, 5.3, 5.4, **5.5 (Must)** leer; Notizen implizieren A (5.3), S+A (5.4), S/„BeSync" (5.5) [F: KAT] | vor Abgabe füllen |
| W7 | 2.7 | N, obwohl Notiz „Eigentlich machbar über code, dennoch keine Zeit" = A [F: KAT] | A statt N (Aufwand ausweisen) |
| W8 | Tabelle1 vs. Spalte F | Tabelle1 unterstellt für 5.5 den Wert N („fällt von N auf K"), die Zelle ist leer [F: KAT] | abgleichen |
| W9 | Tabelle1 in Anbieterdatei | MDIS-interne Hypothesen/Konfidenzen im selben Workbook wie die Anbieterantwort [F: KAT] | vor Versand entfernen |
| W10 | Formales | Übersicht spricht von „Spalte Erfüllungsgrad", Spalte heißt „Erfüllung Anbieter"; Kopf „Bermerkungen"; Tippfehler „Dahsboard", „Worflow", „Standart", „Zahlungsamangementsystem"; Dropdown auch auf G18 [F: KAT; META] | kosmetisch |

### 8.2 Katalog-Bewertung vs. LIESMICH-Korrekturen und Recherche

| Nr | Katalog | Gegenquelle | Konsequenz |
|---|---|---|---|
| W11 | 3.2 = S („Liegezeit") | „3.2 Liegezeit steht in keiner Dokumentation, ein ‚S' dort ist eine Zusage ohne Beleg" [LM]; „Liegezeit existiert nirgends" [B00 AB]; A05 Kap. 11: „Sortierung nach Eingangsdatum" als Ersatz | auf K herabstufen oder Vorbehalt |
| W12 | 2.2 = S („anhand der Anschrift/Steuernummer") | „2.2 Mandantenerkennung läuft über Name und Anschrift, nicht über die Steuernummer, und braucht einen Vorbehalt" [LM]; Mandantenstamm hat kein Steuernummernfeld [A05 Kap. 6; B00 AI] | Vorbehalt ins Angebot |
| W13 | 2.8 = S | Standard-Aufteilungsschlüssel „in d.velop invoices nicht dokumentiert" [A05 Kap. 11; B00 AM]; MDIS-Hypothese selbst: „fällt von S auf K" [KAT Tabelle1] | K |
| W14 | 5.1 = S | DATEV-Handbücher gesperrt, Format/Intervall unbelegt [B00 P, AQ]; A06 Kap. 7: „Connector womöglich nicht konfiguriert" | S nur nach Bestätigung durch d.velop |
| W15 | 1.6 = S | Export je Gesellschaft „kein Knopfdruck" [KAT Tabelle1]; Änderungsprotokoll „Aktivitäten" nur Cloud [A05 2.1] | Vorbehalt/Dienstleistung |
| W16 | 4.2 leer | „Extern Teilen" nur Cloud + documents business, kein Workflow-Freigeben [B00 E] | eher A oder über 4.3 (Lizenz) |

### 8.3 Katalog vs. Demo-Architektur (A06), Testdaten und A05

| Nr | Thema | Katalog | Andere Quelle(n) | Konsequenz |
|---|---|---|---|---|
| W17 | 2.7 Bewertung | **N** | **A** in A06 Kap. 7, TDL 3 und Beleg 24 („Katalog-Anforderung 2.7 steht auf A") | vereinheitlichen |
| W18 | 5.3 Bewertung | leer (Notiz ≈ A) | **N** in A06 Kap. 7 und A05 Kap. 11 („die auf N stehen: Omikron … und BIM4You") | vereinheitlichen |
| W19 | 5.5 Bewertung | leer (Notiz „standart … über BeSync") | **N** in A06 Kap. 7/A05 Kap. 11; Tabelle1 „N→K"; AG Folie 4 „sonst bleibt dieses Must-Have unerfüllt"; ARCH Folie 2 „Zahlungen werden über DATEV ausgelöst" | **vier Lesarten** – zentrale Klärung (Q5) |
| W20 | 4.1 Bewertung | **N** | A06 W6 „Fremdverwaltung … 4.1 teilw." und Kap. 7 „Der Prozesszweig ist abbildbar" | eher K (Prozesszweig) + A (Datenübergabe) |
| W21 | 5.1 | S | A06 Kap. 7 führt DATEV-Übergabe unter „bewusst nicht eingerichtet" | Demo-Nachweis fehlt |
| W22 | A05 „N-Themen" | tatsächliche N: 2.7, 4.1, 5.2 | A05 Kap. 11 nennt Omikron und BIM4You als „die beiden Themen … die auf N stehen" | A05 falsch zitiert |

### 8.4 Katalog vs. MDIS-Zielarchitektur

| Nr | Thema | Katalog | Zielarchitektur (ARCH) | Konsequenz |
|---|---|---|---|---|
| W23 | Scope | „Digitales Rechnungsmanagement"; DMS nur Could (6.1) | „DMS-Kernprozesse": Eingangsrechnungen **+ Verträge + Post** | Scope-Erweiterung bewusst machen; Anforderungen für Verträge/Post erheben |
| W24 | Bim4You | Should, „optionale Möglichkeit" | bidirektionale Kernintegration, Bau-Rechnungen laufen durch Bim4You | Priorität mit Livos klären |
| W25 | Zahlungsauslösung | über Omikron (5.5) | über DATEV; Omikron nicht dargestellt | Zahlungskette klären (d.velop → DATEV → Omikron?) |
| W26 | 5.2 VOB/Einbehalte | N, „Bau-ERP-Funktion" | Einbehalt-/Kürzungsinfos kommen aus Bim4You zurück | 5.2 über Bim4You-Integration lösbar – Bewertung überdenken |
| W27 | Sonderbuchungsinfos, Vorerfassungsjournal, Zahlungsrückmeldung | nicht gefordert | gefordert (D3, D4, Folie 3) | zusätzliche Anforderungen dokumentieren |
| W28 | Property Manager | Must (4.1) | fehlt | Architektur ergänzen |
| W29 | Externe Freigeber, Dashboards, Klärfall, Eskalation | gefordert (4.2, 4.3, 3.1–3.4, 2.3) | nicht dargestellt | Architektur ergänzen |
| W30 | Aktualität | Katalog Juli 2026 | PDF erstellt 28.05.2025 (Autor ThomasGross) [META] | Zielbild ist älter als der Katalog – auf Aktualität prüfen |

### 8.5 Innerhalb der Zielarchitektur

| Nr | Befund | Quelle |
|---|---|---|
| W31 | Sonderbuchungsinfos: Folie 2 als Fluss d.velop → DATEV; Folie 3 als Ergebnis der Bim4You-„Bearbeitung"; auf Folie 2 fehlt ein Fluss Bim4You → d.velop für Sonderbuchungsinfos | ARCH Folie 2/3 |
| W32 | d.velop → Bim4You: Folie 2 „Eingangsrechnungs-Journale" (pauschal), Folie 3 nur „Rechnungen bezüglich Bauprojekte" | ARCH Folie 2/3 |
| W33 | Verteilung ↔ „DTEV Integration / ER Vorerfassungs-Journal" ohne Pfeile (bei Freigabe/Zahlung mit Pfeilen); „DTEV" 3× Tippfehler | arch_3.png |
| W34 | Zahlungsrückmeldung (Folie 2) im Prozessbild Folie 3 nicht enthalten | ARCH |
| W35 | Reihenfolge Verteilung/Klassifizierung bei Verträgen umgekehrt zu Post | ARCH Folie 4/5 |

### 8.6 Architektur-Dokument (A06) vs. tatsächliche Cloud-Möglichkeiten

| Nr | A06 (Stand 18.09.2026) | Tatsächlich (Cloud-Tenant / Recherche) | Quelle |
|---|---|---|---|
| W36 | „Dokumentarten", „Eigenschaften" mit Position/Kürzel | Cloud: „Kategorien", „Eigenschaften"; Position, Beschreibung, Kürzel gibt es nicht; A05/A06 enthalten noch alte Begriffe | LM „Drei Dinge"; B00 F, L |
| W37 | Reverse Charge / FSB geprüft als „Ja / Nein"-Typ | kein Ja/Nein-Datentyp; nur Text, Zahl, Währung, Datum, Datum-und-Zeit → Wertemenge „Livos Ja Nein" | LM; CP 2; B00 H |
| W38 | Dashboards mit 12 fachlichen Kacheln (Kap. 4) | nur vier Standard-Widgets (Suche, Zuletzt bearbeitet, Beobachtet, Favorisiert); Managementsicht gehört ins **Rechnungseingangsbuch** (Schnellzugriffe, Filter, Gruppierung); rollenbezogen nur als Sichtbarkeitssteuerung | LM; A05 Kap. 10; B00 X, AA |
| W39 | „Kostenstelle mit Anteil" als Mehrfachfeld | nicht baubar; Splitting über Belegpositionen/Kostenobjekt in smart invoice | LM; A05 5.2; B00 H, AM |
| W40 | Eigenschaft „Status" systemgesteuert | nicht anlegen; „Workflowstatus" existiert bereits | CP 3 |
| W41 | Beträge und Sicherheitseinbehalt als „Zahl" | Datentyp „Währung" | CP 3 |
| W42 | Belegart „Normal / Abschlag / Schluss" | Wertemenge zusätzlich „Gutschrift" | CP 2 |
| W43 | Mandantenzuordnung NORD/BAUP über Steuernummer (A06 3.1, TDL 1) | Erkennung über Name + Anschrift; Steuernummer nur beim Kreditor; Alias-Postfach als Alternative | A05 Kap. 6/7; B00 AI |
| W44 | Freigabegrenze „10.000 Euro brutto" | Klickweg nutzt `voucher.net_amount >= 1000000` (**netto**, Cent); gleiches Ergebnis für die Testbelege, fachlich aber anderer Maßstab | A05 Kap. 8 |
| W45 | W1 „Erfassung → Prüfung → Kontierung → Freigabe → Export" selbst gebaut | smart invoice bringt Best-Practice-Workflow „Verteilung, Prüfung, Freigabe, Buchhaltung"; im geteilten Tenant darf smart-invoice-Konfiguration nicht angefasst werden → W1–W6 wie geplant nicht umsetzbar | A05 Kap. 4; CP 0 |
| W46 | R1–R3 über Berechtigungen | Cloud-Berechtigungs-UI nicht öffentlich dokumentiert; On-Prem-Konstrukte (@D3GROUP, Dokumentklassen) nicht übertragbar | A05 9.2; B00 J, L |
| W47 | P0 „Klären: Cloud oder On-Premises" | geklärt: Cloud, smart invoice aktiv, produktiv geteilter Tenant (102 Belege) | LM; CP |
| W48 | Kopf: „Livos (fiktiver Kunde, Workshop-Szenario)" | Livos ist realer Interessent (Katalog, MDIS-Folien mit LIVOS-Logo); fiktiv sind nur die Testgesellschaften | KAT; ARCH Folie 1 |
| W49 | A06 Agenda-Struktur mit „TOP 3.4 Dashboards und Steuerung" | reale Agenda (AG) hat **keinen** Dashboard-Punkt; 3.1, 3.2, 2.7, 5.2 fehlen auf der Agenda | AG Folie 2–4 |
| W50 | W4 Eskalation (3 Tage) „Empfohlen" | A05 streicht Eskalation (3–6 h, Mail-Aktion nicht dokumentiert); AG markiert „Eskalation & Vertretung - X" | A05 Kap. 11; AG Folie 2 |
| W51 | Pflichtfelder: Netto/Steuersatz/Steuer/Brutto alle Pflicht, Status Pflicht | CP: Steuersatz und Steuerbetrag optional, kein Status | CP 4 |

### 8.7 Testdaten – intern und gegenüber A06

| Nr | Befund | Quelle |
|---|---|---|
| W52 | TDL: „17 Dokumente plus zwei Stammdatenlisten" – tatsächlich 15 Dokumente (01–10, 20–24) + 2 CSV + LIESMICH = 18 Dateien | TDL Kopf; META |
| W53 | Umlaute: Testbelege/CSV „Sued", „Hafenstrasse", „Muenchen"; Wertemengen „Süd", „Hafenstraße"; A05 sogar „Süed" – automatische Zuordnung greift sonst nicht | LM „Was noch offen ist"; A05 6.1 |
| W54 | Ausgangszustände: TDL (02, 03, 05 komplett durchlaufen; 06 durchlaufen; 07 „in Prüfung") ≠ A06 Kap. 5 (03 „In Kontierung", 04 „In Prüfung", 06 „Freigegeben", 07 „Wartet auf Freigabe Stufe 2") | TDL 4; A06 Kap. 5 |
| W55 | WEST: CSV mit Steuernummer 133/555/12345; A06 3.1 „—" | TD; A06 |
| W56 | **Dubletten**: 09 ist RE-2026-1042 (wie 02), 10 ist RE-2026-1041 (wie 01); A06 plant 02 **und** 09 als „abgeschlossen" → Doppelerfassung; Schnellzugriff „über 10.000 €" liefert nur dann „genau die drei Belege", wenn 10 nicht importiert ist | A06 Kap. 5; A05 Kap. 12; META |
| W57 | **IBANs**: XRechnung `DE45200400008765432100` und ZUGFeRD `DE02200505501234567890` sind **prüfziffernungültig** und weichen von PDF/Stamm ab – widerspricht „Die IBANs sind prüfsummenvalide" | META; TDL Kopf |
| W58 | ZUGFeRD: kein PDF/A-3 (keine XMP-Metadaten), XML mit einer Sammelposition statt vier Positionen | META; TDL 5 |
| W59 | **Sicherheitseinbehalt 3.500 €** (07) passt zu keiner Bemessungsgrundlage: 5 % der Abschlagssumme 35.000 = 1.750; 5 % kumuliert 60.000 = 3.000; 5 % Auftragssumme 100.000 = 5.000. Rahmenvertrag „5 % der Auftragssumme" ≠ AB „5 % der jeweiligen Abschlagssumme"; auf Abschlag 1 (06) wurde gar nichts einbehalten | TD 07, 20, 21 |
| W60 | Einbehalt „bis 30.09.2028" ≠ Rahmenvertrag „Gewährleistungsfrist 4 Jahre ab Abnahme" (Abnahme frühestens nach 31.12.2026) | TD 07, 20, 21 |
| W61 | Rahmenvertrag RV-2026-004 hat Auftraggeber **NORD**, dient aber als Grundlage der AB für **SUED** → gesellschaftsübergreifender Vertrag kollidiert mit strikter Mandantentrennung (R2) bzw. Kreditorenakte „quer über Gesellschaften" | TD 20, 21; A06 3.5, 3.7 |
| W62 | § 13b: Rahmenvertrag § 4 „bei Bauleistungen … schuldet der Auftraggeber (NORD) die Umsatzsteuer", Beleg 01 (Bauleistung an NORD) weist aber 19 % USt aus; SUED (ebenfalls Objektgesellschaft) erhält RC-Rechnungen. Fachlich gilt RC nur, wenn der Empfänger selbst Bauleistender ist [A] | TD 01, 06, 07, 20 |
| W63 | Rahmenvertrag: Laufzeit bis 31.12.2027, Kündigung 3 Monate zum Quartalsende → letzter Kündigungstermin 30.09.2027; „Naechster Pruefungstermin: 01.10.2027" liegt **danach** | TD 20 (eigene Fristrechnung) |
| W64 | Testbeleg 03 verlangt Split „Haus A / Haus B"; Wertemenge „Livos Kostenstelle" kennt nur KST-1000/2000/2100/3000 → Split mit Demo-Stammdaten nicht abbildbar. Beleg 04 „Ankauf Objekt Neue Strasse 4" fehlt in Wertemenge „Livos Objekt" (Objekt ist Pflichtfeld) | TD 03, 04; CP 2, 4 |
| W65 | Gewerk/Los: Beleg 01 „Rohbau, Los 3" enthält Malerarbeiten; Wertemenge „Livos Gewerk" hat kein „Los" | TD 01; CP 2 |
| W66 | Begleitmail von `buchhaltung@musterbau-test.de`, Kreditorenstamm `rechnung@musterbau-test.de` | TD 23; CSV |
| W67 | Agenda-Datei heißt „20250404_…", wurde aber am 18.09.2026 bearbeitet (Vorlage von 2023); Folie 1 ist eine Vorversion von Folie 2 ohne Katalognummern; Bedeutung der „- X"-Markierungen nicht erklärt (Deutung [A]: in der Demo nicht live gezeigt – deckt sich mit A06 Kap. 7 / A05 Kap. 11 für Eskalation und DATEV, **nicht** aber für den Klärfall 2.3, der in A06 als Pflicht-Workflow W3 geführt wird) | AG; META |

### 8.8 Abgleich mit der Transkript-Kurzfassung im Briefing (keine eigene Transkriptauswertung)

Quelle: `SP/work/00_BRIEFING.md`, Abschnitt „Erkenntnisse aus dem Transkript" (Lead-Auditor). Die Einträge dort sind ohne Zeitstempel; die belastbare Belegung liefert die Transkript-Auswertung. Hier steht nur, welche Annahmen dieses Dokuments davon berührt werden.

| Annahme / Frage in diesem Dokument | Hinweis aus der Briefing-Kurzfassung | Wirkung |
|---|---|---|
| DATEV-Produkt/Betrieb offen (Kap. 1.5, 4.3 Nr. 1) | DATEV ist führendes FiBu-System; gebucht wird durch den Dienstleister „Trios", DATEV läuft bei einem externen Dienstleister (Zugriff über dessen Cloud) | Q4/5.1 und die DATEV-Flüsse der Zielarchitektur müssen mit dem Dienstleister abgestimmt werden |
| Kreditorennummern „konzernweit einheitlich?" (T11, 4.3 Nr. 7) | gleicher Lieferant in vielen Gesellschaften mit **unterschiedlichen** Kreditorennummern; 70000er intern, 80000er aus Hausverwaltungen; keine Konsolidierung | Testdaten (70012 für drei Gesellschaften) sind hier unrealistisch; Anforderung „Lieferanten-Konsolidierung / Mapping je Mandant" kommt hinzu |
| Property Manager: Anzahl, Rolle offen (Kap. 1.5, 4.3 Nr. 5; 4.1) | ca. 10 Property Manager (Hausverwaltungen) buchen ca. 95 % ihrer Rechnungen selbst; Rechnungen über Schwellwert brauchen Freigabe durch das Livos Asset Management; MDIS-Vorschlag: eigenes Postfach „Freigabe-Rechnungen", reiner Freigabe-Workflow ohne Buchung/Zahlung | 4.1 wird als **Freigabe-only-Prozess** greifbar → Bewertung N ist zu überprüfen (eher K) |
| 3.2 Liegezeit (W11) | Kunde fragte nach Liege-/Durchlaufzeit je Benutzer/Schritt; MDIS: nicht in d.velop, über eigene App bzw. Evidanza-BI | bestätigt den Vorbehalt zu 3.2 |
| 3.4 ungeplante Vertretung (W4) | Vertretung auch durch Admin für erkrankte Kollegen gefragt | bestätigt die Lücke in der Notiz zu 3.4 |
| 2.7 / T6 Freistellungsbescheinigung | FSB-Abgleich beim Kreditor gefragt | stützt die Priorität über „Could" hinaus |
| 5.2 / T4 kumulierte Abschläge | automatische Prüfung gegen bereits Gezahltes gefragt (offen); positionsweise Kürzungen | stützt 5.2 und die Bim4You-Rückflüsse „Kürzungsinformationen" |
| T7 IBAN-Abgleich, T14 Dubletten | IBAN-Abgleich Rechnung vs. Stammdaten gefragt; Dublette nur mit Begründung annehmen | bestätigt T7/T14 als reale Anforderungen |
| Neu (nicht im Katalog) | Rückweisung mit Standardgründen und automatischer Lieferanten-Mail; Freigaben für Ausbuchungen auf Mietkonten; KI-Fragen an Vertragsinhalte; Aktenebenen; Lizenz nach Akten/Speicher | Katalog um diese Punkte ergänzen |

---

## Anhang – Metadaten der Originaldateien [F: META]

| Datei | Erstellt | Zuletzt geändert | Autor / geändert von | Bemerkung |
|---|---|---|---|---|
| Kopie von 260715_Leistungskatalog_Rechnungsmanagement_.xlsx | 07.07.2026 (Creator „openpyxl") | 22.09.2026 12:18 | lastModifiedBy „Sebastian Pachon" | 3 Blätter; Dropdown-Validierung F2:F30 → Übersicht!C13:C16 |
| Livos_DMS_Business Architektur.pdf | 28.05.2025 | 28.05.2025 | Author „ThomasGross" | aus PowerPoint „DMS_Business Architektur" |
| 20250404_Agenda Livos.pptx | 06.03.2023 | 18.09.2026 | Simona Röhrl / Sebastian Pachon | 4 Folien, keine Notizen, keine ausgeblendeten Folien |
| 06_Architektur_Demo-Instanz.docx (3 Kopien) | 18.09.2026 bzw. 21.09.2026 | – | „Workshop-Vorbereitung" | Textinhalt aller Kopien identisch |
| 07_Testdaten (testdaten/, _Upload_Rechnungen/, _Upload_Dokumente/) | 22.09.2026 | – | – | Upload-Ordner = Kopien der Belege 01–10 bzw. 20–24 |
| Mocca_V14_108 (Acumatica) | – | – | – | 527 Tabellen, kein Treffer „Livos" |
