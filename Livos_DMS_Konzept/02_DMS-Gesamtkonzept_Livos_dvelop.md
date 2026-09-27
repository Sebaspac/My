# 1 Dokumentinformationen und Lesehilfe

## 1.1 Zweck des Dokuments

Dieses Dokument beschreibt das Gesamtkonzept für ein Dokumentenmanagement- und Rechnungseingangssystem der LIVOS Gruppe auf Basis der d.velop Cloud. Es verbindet drei Ebenen:

- die **fachlichen Anforderungen** von Livos (Leistungskatalog und Workshop),
- die **Lösung** auf Basis der d.velop-Standardprodukte, ihrer Konfiguration und klar abgegrenzter Ergänzungen über die MDIS-Integrationsplattform BeSync,
- die **Umsetzung** in Phasen, mit offenen Punkten, Tests und Entscheidungsbedarfen.

Das Konzept dient Livos als Entscheidungsgrundlage und dem gemeinsamen Projektteam als verbindliche Arbeitsgrundlage für Prozess-Workshop, Feinkonzept und Einrichtung. Es beantwortet jede Anforderung des Leistungskatalogs einzeln und nachvollziehbar (Kapitel 4).

## 1.2 Geltungsbereich

| Bereich | Inhalt |
|---|---|
| Organisation | LIVOS Gruppe mit über 100 Gesellschaften in den Segmenten Bestand, Privatisierung und Bau, einschließlich der Zusammenarbeit mit Trios (Buchhaltung), Property Managern und externen Projektbeteiligten |
| Prozesse | Eingangsrechnungen (Kern), Freigabe von Property-Manager-Rechnungen, Bau-Rechnungen mit BIM4You, Verträge, Posteingang, allgemeine DMS-Nutzung |
| Systeme | d.velop Cloud (d.velop documents, d.velop invoices mit smart invoice, d.velop contracts, d.velop pilot, process studio), DATEV, BIM4You, multicash (Omikron), Lieferanten-App auf BeSync, evidanza, Microsoft 365 |
| Nicht Gegenstand | Preise und Vertragskonditionen (separates Angebot), Detailspezifikation der BeSync-Programmierung (Feinkonzept), Konfiguration der Umsysteme selbst |

Die genaue Abgrenzung des Leistungsumfangs steht in Kapitel 3.6.

## 1.3 Status und Versionierung

| Merkmal | Wert |
|---|---|
| Dokument | Livos DMS – Gesamtkonzept |
| Version | 0.9 |
| Stand | 26.09.2026 |
| Status | Entwurf zur Abstimmung mit Livos |
| Herausgeber | MDIS Consulting |
| Empfänger | LIVOS Gruppe, Projektleitung Kunde: André Töpper |

| Version | Datum | Änderung |
|---|---|---|
| 0.9 | 26.09.2026 | Erstfassung auf Basis Leistungskatalog, Demo-Workshop und Produktrecherche; zur Abstimmung |
| 1.0 | geplant nach Prozess-Workshop | Einarbeitung der Livos-Rückmeldungen und der Entscheidungen zu den offenen Punkten (Kapitel 20) |

Aussagen, die ausdrücklich als „Vorschlag" oder „Beispiel" gekennzeichnet sind (Freigabegrenzen, Fristen, Zielwerte, Gesellschaftsnamen), sind von Livos zu bestätigen oder zu ersetzen.

## 1.4 Grundlagen

| Grundlage | Stand | Verwendung im Konzept |
|---|---|---|
| Leistungskatalog & Anforderungsprofil „Digitales Rechnungsmanagement" (Livos) | 07/2026 | 29 Anforderungen; Bewertung in Kapitel 4 |
| Demo-Workshop Livos und MDIS auf der d.velop-Demo-Instanz | 22.09.2026 | Zusätzliche Anforderungen, Fragen und Rahmenbedingungen (T-01 bis T-46) |
| MDIS-Zielarchitektur „DMS-Kernprozesse" (Systemlandschaft, Prozessketten Eingangsrechnung, Verträge, Post) | 05/2025 | Architekturrahmen (Kapitel 5), Prozessketten (Kapitel 9 und 12) |
| d.velop-Produktdokumentation (Leistungsbeschreibungen, Handbücher, API-Dokumentation) | 09/2026 | Belegung der Produktaussagen; Einzelnachweise im Quellenverzeichnis (Anhang) |
| Herstellerinformationen zu DATEV-Anbindung (LDconnect), multicash und BIM4You | 09/2026 | Schnittstellenkonzept (Kapitel 15) |

Beispieldaten im Konzept (etwa die Demo-Gesellschaften NORD, SUED, BAUP und WEST) sind fiktiv und dienen nur der Veranschaulichung.

## 1.5 Legende

### 1.5.1 Erfüllungsgrad je Katalogpunkt

Für die Bewertung der Katalogpunkte verwendet das Konzept die Legende des Livos-Leistungskatalogs.

| Kürzel | Bedeutung (Livos-Katalog) |
|---|---|
| S | Standard – im Kernprodukt ohne Anpassung enthalten |
| K | Konfiguration – durch Einstellungen oder Workflows abbildbar |
| A | Anpassung – individuelle Programmierung oder Entwicklung notwendig (im Konzept in der Regel als MDIS-Leistung über BeSync) |
| N | Nein – nicht im Leistungsumfang enthalten |

Kombinierte Angaben wie „S / A" bedeuten: Der Kern der Anforderung ist im Standard erfüllt, ein benannter Teilaspekt erfordert eine Anpassung. Die Teilung ist in Kapitel 4.2 je Punkt begründet.

### 1.5.2 Belegstatus einzelner Aussagen

| Kürzel | Bedeutung |
|---|---|
| [S] | Standardfunktion, in der Produktdokumentation belegt |
| [K] | durch Konfiguration umsetzbar |
| [A] | Anpassung oder Entwicklung, meist MDIS-Leistung über BeSync |
| [O] | offen, im Test oder mit dem Hersteller zu verifizieren |

Die Kürzel stehen dort, wo die Einordnung für die Entscheidung relevant ist. Offene Punkte sind mit einer OP-Nummer verknüpft und in Kapitel 20 gesammelt.

## 1.6 ID-Systematik

Alle Konzeptelemente tragen eindeutige Kennungen. Sie werden in allen Kapiteln und in der draw.io-Datei einheitlich verwendet.

| Präfix | Element | Beispiel | Definiert in |
|---|---|---|---|
| P | Designprinzip | P3 BeSync nur, wo der Standard endet | Kapitel 5 |
| AE | Architekturentscheidung | AE-03 Ein Bucket, jede Gesellschaft ein Mandant | Kapitel 5 |
| R | Rolle | R-02 Rechnungseingang / Verteilung | Kapitel 13 |
| K | Kategorie (Dokumentart D, Aktenart A) | K-01 Eingangsrechnung, K-12 Kreditorenakte | Kapitel 7 |
| E | Eigenschaft | E-01 Mandant (Mandanten-ID) | Kapitel 7 |
| WF | Workflow / Prozess | WF-01 Standard-Eingangsrechnung | Kapitel 9 bis 12 |
| S | Schnittstelle | S-01 DATEV Buchungsvorschlag + Beleglink | Kapitel 15 |
| M | Maske / Oberfläche | M-02 Verteilung | Kapitel 14 |
| OP | Offener Punkt / Test | OP-02 Test Mandantenerkennung mit echten Belegen | Kapitel 20 |
| T | Anforderung aus dem Workshop 22.09.2026 (mit Bindestrich) | T-26 Rückweisung mit Standardgründen | Kapitel 4.4, Anhang |
| T (ohne Bindestrich) | Plattformtest im Test-Tenant | T03 Restriction Set über alle Gruppen | Kapitel 20.4 |
| RI | Risiko | RI-01 Mandantenerkennung | Kapitel 20.1 |
| ED | Entscheidungsbedarf Livos | ED-01 DATEV-Übergabe ein- oder zweistufig | Kapitel 20.2 |
| KPI | Kennzahl | KPI-07 Skontoquote | Kapitel 16.3 |

Katalogpunkte behalten die Nummerierung des Livos-Katalogs (1.1 bis 6.1).

## 1.7 Aufbau des Dokuments

| Kapitel | Titel | Inhalt |
|---|---|---|
| 1 | Dokumentinformationen und Lesehilfe | Zweck, Status, Legende, ID-Systematik |
| 2 | Management Summary | Kernaussagen und Empfehlungen auf ein bis zwei Seiten |
| 3 | Ausgangslage und Zielsetzung | Unternehmen, Mengengerüst, Ist-Systeme und -Abläufe, Schmerzpunkte, Ziele, Scope |
| 4 | Anforderungen und Abdeckung | Bewertung aller 29 Katalogpunkte, Zusatzanforderungen aus dem Workshop, nicht-funktionale Anforderungen |
| 5 | Lösungsarchitektur | Systemlandschaft, d.velop-Bausteine, Betriebsform, Lizenzarchitektur, Designprinzipien, Architekturentscheidungen |
| 6 | Mandanten- und Organisationsmodell | Abbildung der über 100 Gesellschaften |
| 7 | Informationsmodell | Kategorien, Eigenschaften, Wertemengen, Aktenplan, Aufbewahrung, Namenskonventionen |
| 8 | Stammdatenkonzept | Gesellschaften, Objekte, Lieferanten und Kreditoren mit drei Nummernkreisen, Kontierung, BIM4You-Stamm, Freistellungsbescheinigungen |
| 9 | Prozesskonzept Eingangsrechnung | WF-01, WF-02, WF-04, WF-05 mit allen Sonderfällen |
| 10 | Freigabe- und Workflowkonzept | Freigabematrix, Wertgrenzen, Vier-Augen-Prinzip, Eskalation, Vertretung, Statusmodell |
| 11 | Property-Manager-Freigabe und weitere Freigaben | WF-03, WF-09, WF-10 |
| 12 | Verträge, Posteingang und DMS-Nutzung | WF-06, WF-07, Ablage, Suche, Aufgaben, Outlook, mobile Nutzung, d.velop pilot |
| 13 | Rollen- und Berechtigungskonzept | Rollen R-01 bis R-15, Gruppen, Restriction Sets |
| 14 | Masken- und Oberflächenkonzept | M-01 bis M-19 |
| 15 | Schnittstellenkonzept | S-01 bis S-17, Betrieb BeSync, Fehlerbehandlung |
| 16 | Reporting und Controlling | Sichten im Rechnungseingangsbuch, Kennzahlen, evidanza |
| 17 | Compliance | GoBD, Aufbewahrung, Verfahrensdokumentation, E-Rechnung, Datenschutz, Betriebsprüfung, Export je Gesellschaft |
| 18 | Betrieb, Organisation, Change und Schulung | Betriebsmodell, Verantwortlichkeiten, Schulung |
| 19 | Einführungsvorgehen und Roadmap | Phasen 0 bis 5, Pilot, Migration, Test, Go-live |
| 20 | Risiken, Entscheidungsbedarfe, offene Punkte, Testplan | OP-Liste, Tests, Entscheidungen |
| 21 | Anhang | Glossar, Quellenverzeichnis, Workshop-Anforderungsliste T-01 bis T-46 |

**Lesehinweis:** Entscheider lesen Kapitel 2, 3.5, 4.2/4.3 und 20. Fachbereiche finden ihre Abläufe in den Kapiteln 9 bis 12 und die Oberflächen in Kapitel 14. IT und Betrieb lesen die Kapitel 5, 13, 15, 17 und 18.

## 1.8 Begleitende draw.io-Datei

Zum Konzept gehört eine draw.io-Datei. Sie enthält alle grafischen Sichten des Konzepts:

- Systemlandschaft und Schnittstellen (S-01 bis S-17),
- Prozessdiagramme der Workflows WF-01 bis WF-10,
- Mandanten-, Aktenplan- und Berechtigungsmodell,
- Maskenentwürfe M-01 bis M-19.

Die Diagramme verwenden dieselben IDs wie dieses Dokument. Bei Abweichungen gilt der Text dieses Dokuments.

## 1.9 Beteiligte

| Organisation | Rolle im Projekt |
|---|---|
| LIVOS Gruppe | Auftraggeber; Projektleitung Kunde: André Töpper. Fachbereiche Finanzen/Controlling, Buchhaltung und Rechnungsprüfung, Asset Management, Bau/Projektleitung, Geschäftsführung |
| Trios | Buchhaltungsdienstleister von Livos; bucht in DATEV, legt Kreditoren an; beteiligt an DATEV-Übergabe und Zahllauf |
| Externer IT-Dienstleister (Hoster) | Betrieb der DATEV-Umgebung von Livos; beteiligt an der Gateway-Anbindung |
| Property Manager (Hausverwaltungen) | Externe Verwalter der rein verwalteten Bestände; Beteiligte im Prozess WF-03 |
| MDIS Consulting | Konzeption, Einrichtung der d.velop-Lösung, Entwicklung und Betrieb der BeSync-Erweiterungen und der Lieferanten-App |
| d.velop AG | Hersteller und Cloud-Betreiber; Klärung produktseitiger offener Punkte |
| Weitere Hersteller | LIONDEER (LDconnect), BIB GmbH (BIM4You), Omikron (multicash), evidanza – bei Bedarf für Schnittstellenfragen |

# 2 Management Summary

## 2.1 Ausgangslage

Die LIVOS Gruppe führt über 100 Gesellschaften in den Segmenten Bestand, Privatisierung und Bau. Rund 80 interne und externe Anwender bearbeiten 20–30 Eingangsrechnungen am Tag. Die Finanzbuchhaltung läuft in DATEV bei einem externen Dienstleister (Trios), Zahlungen über multicash (Omikron), das Bau-Budgetcontrolling in BIM4You. Rund zehn Property Manager buchen und bezahlen die Rechnungen der von ihnen verwalteten Objekte selbst. Heute fehlen eine durchgängige Sicht auf Rechnungen im Umlauf, eine einheitliche Kreditorenidentität über alle Gesellschaften und ein digitaler, revisionssicherer Freigabeweg.

## 2.2 Empfehlung

MDIS empfiehlt eine Lösung auf der **d.velop Cloud** mit **d.velop invoices** für den Rechnungsprozess und **d.velop documents** als DMS – in **einem** Tenant für alle Gesellschaften. Jede Gesellschaft ist ein Mandant; Rechte, Akten, Freigabewege und DATEV-Übergabe hängen an diesem Schlüssel (Kapitel 5–7).

| Ziel | Lösung | Kapitel |
|---|---|---|
| Alle Rechnungen digital und vollständig erfassen | E-Mail-Postfächer (eines je Gesellschaft möglich), Scan, E-Rechnung; KI-Erkennung, Dubletten- und Pflichtangabenprüfung | 9 |
| Richtige Gesellschaft, richtiger Kreditor | Mandantenerkennung mit Maßnahmenbündel und Klärfall; Lieferanten-App mit gesellschaftsübergreifender Lieferantennummer | 6, 8, 9 |
| Klare, gesellschaftsindividuelle Freigaben | Freigabematrix je Gesellschaft, Kostenobjekt und Betrag; Vier-Augen-Prinzip; Eskalation und Vertretung | 10 |
| Transparenz für Management und Controlling | Rechnungseingangsbuch mit Status, Bearbeiter und Liegezeit; historische Kennzahlen in evidanza | 16 |
| Nahtlose Buchung und Zahlung | Zahlungsfreigabe in d.velop, Buchungsvorschlag mit Beleglink nach DATEV, Zahlung über multicash, Rückmeldung „bezahlt" | 9, 15 |
| Property Manager einbinden, ohne sie zu belasten | Freigabepostfach mit E-Mail-Rückmeldung, keine Buchung in d.velop | 11 |
| Bau-Spezifika korrekt behandeln | Prüfung kumulierter Abschläge und Einbehalte in BIM4You, Steuerung und Archiv in d.velop | 9 |
| GoBD und Gesellschaftsverkauf | revisionssichere Ablage, Aufbewahrung je Kategorie, Exportpaket je Gesellschaft | 17 |
| DMS über Rechnungen hinaus | Verträge mit d.velop contracts, KI-gestützte Postverteilung, Fragen an Dokumente mit d.velop pilot | 12 |

## 2.3 Abdeckung des Leistungskatalogs

Von 29 Anforderungen sind 17 mit Standard (davon 7 mit Konfigurations- oder Anpassungsanteil), 6 mit Konfiguration, 2 mit Konfiguration plus Anpassung und 3 mit Anpassung erfüllbar; die Bau-Rechenlogik (5.2) liegt in BIM4You. **Alle 21 Must-Haves sind abgedeckt.** Die Anpassungsanteile liefert und betreibt MDIS über die bei Livos bereits eingesetzte Middleware BeSync; sie sind klein, klar abgegrenzt und verlangen von Livos keine technische Pflege (Kapitel 4, 15).

## 2.4 Kritische Erfolgsfaktoren

1. **Gesellschaftszuordnung bei gemeinsamer Anschrift** – Test mit echten Belegen vor dem Go-live (Kapitel 9, 20).
2. **Kreditorenstammdaten** – Konsolidierung über die Lieferanten-App, geregelter Anlageweg über Trios (Kapitel 8).
3. **DATEV-Anbindung beim Hoster** – Datengateway und DATEV-Komponenten früh beauftragen (Kapitel 15).
4. **Klare Entscheidungen** zu Freigabegrenzen, Rollen, Aktenstruktur und führendem System für Bau-Rechnungen (Kapitel 20).

## 2.5 Vorgehen

Die Einführung erfolgt stufenweise: Phase 0 klärt Entscheidungen und Technik, Phase 1 startet den Rechnungseingang mit Pilotgesellschaften, Phase 2 rollt auf alle Gesellschaften aus und bindet die Property Manager ein, Phase 3 ergänzt BIM4You und die Zahlungsrückmeldung, Phase 4 bringt Verträge und Post, Phase 5 optimiert (Kapitel 19). Erster Schritt ist ein gemeinsamer Prozess-Workshop.

# 3 Ausgangslage und Zielsetzung

## 3.1 Unternehmen und Mengengerüst

Die LIVOS Gruppe ist eine Immobilien- und Bau-Unternehmensgruppe. Sie führt über 100 Gesellschaften in den Segmenten **Bestand**, **Privatisierung** und **Bau**. Viele davon sind Objekt- und Projektgesellschaften. Gesellschaften werden gegründet und verkauft; Unterlagen müssen deshalb je Gesellschaft vollständig und revisionssicher übergeben werden können (Katalog 1.6). Die Teams arbeiten dezentral und deutschlandweit verteilt.

Ein Teil des Bestands ist „rein verwaltet": Externe Property Manager (Hausverwaltungen) verwalten diese Objekte mit eigenen Systemen und Prozessen.

| Kennzahl | Wert | Quelle |
|---|---|---|
| Gesellschaften (Mandanten) | über 100 | Leistungskatalog 07/2026; Workshop 22.09.2026 |
| Anwender gesamt (intern und extern) | ca. 80 (Workshop: 80 bis 100) | Leistungskatalog; Workshop |
| Eingangsrechnungen | ca. 20 bis 30 pro Tag, ca. 5.000 bis 8.000 pro Jahr | Leistungskatalog |
| Rechnungen je Gesellschaft (rechnerisch) | Ø ca. 50 bis 80 pro Jahr | abgeleitet |
| Property Manager | ca. 10, wechselnd | Workshop |
| Anteil der PM-Rechnungen, die der PM selbst prüft, freigibt und zahlt | ca. 95 % | Workshop |
| Kreditorennummernkreise in DATEV | 70000er-Kreis (Livos intern), 80000er-Kreis (Kreditoren aus Hausverwaltungen) | Workshop |
| Umfang gekürzter Rechnungen (Beispiel) | bis 30 Seiten, ca. 8 gekürzte Positionen | Workshop |
| Volumen Verträge und Post | nicht bekannt – in Phase 0 zu erheben | [O] |
| Aufteilung der Anwender nach Rolle und intern/extern | nicht bekannt – in Phase 0 zu erheben (Grundlage für Lizenzmengen) | [O] |

**Folgerung für das Konzept:** Das Rechnungsvolumen ist moderat, die strukturelle Komplexität hoch. Die Lösung muss vor allem viele Gesellschaften, uneinheitliche Kreditorennummern und mehrere Beteiligte (Livos, Trios, Property Manager, externe Projektbeteiligte) sauber abbilden. Weil je Gesellschaft nur wenige Belege anfallen, müssen Erkennung und Kontierungsvorschläge gesellschaftsübergreifend lernen können.

## 3.2 Heutige Systemlandschaft

| System | Funktion heute | Betreiber / Nutzer | Bezug zum Konzept |
|---|---|---|---|
| **DATEV** (Rechnungswesen) | Operatives Finanzbuchhaltungssystem; Kreditoren je DATEV-Mandant; Buchung der Eingangsrechnungen | Betrieb bei einem externen IT-Dienstleister; gebucht wird durch Trios | Führend für Kreditorenkonten und Buchungen (P4); Anbindung über S-01/S-02 |
| Zugang zur DATEV-Umgebung | Zugriff über eine Cloud-Umgebung des Hosters (im Workshop als „Riecken Cloud" bezeichnet); Auswertungsmöglichkeiten dadurch eingeschränkt | Hoster | Voraussetzung für die DATEV-Schnittstelle; Klärung OP-04 [O] |
| **Trios** | Buchhaltungsdienstleister: bucht in DATEV, prüft die Buchungen der Property Manager, erhält Belege heute gebündelt im Monatspaket, legt Kreditoren in DATEV an | extern | Rolle R-06 im Schritt Buchhaltung |
| **BIM4You** (BIB GmbH) | Budgetcontrolling für Bauprojekte; eigenes Rechnungseingangsbuch und Freigabemanager | Livos Bau | Anbindung für Bau-Rechnungen (WF-02, S-08 bis S-10) |
| **multicash** (Omikron) | Zahlungsverkehrssoftware; Ausführung der Zahlungen | Livos | Zahlungsausführung nach DATEV-Zahlungsvorschlag (S-07) |
| **Systeme der Property Manager** | Eigene Buchhaltung und Zahlung der verwalteten Objekte; Buchungsdaten gehen an Livos bzw. nach DATEV | extern (ca. 10 Verwalter) | Keine Systemintegration in der ersten Ausbaustufe; E-Mail-Kanal (WF-03) |
| **BeSync** und **Lieferanten-App** (MDIS) | Integrationsplattform und bestehende App zur Stammdatenpflege bei Livos | MDIS betreibt, Livos pflegt Stammdaten in der App | Führend für Lieferantenidentität (Konsolidierungsnummer); Integrationsleistungen [A] |
| **evidanza** | BI-Werkzeug; laufendes BI-Projekt mit MDIS | Livos Controlling | Auswertung historischer Durchlaufzeiten (S-12) |
| **E-Mail** | Rechnungseingang, Abstimmung und Freigaben per E-Mail | Livos | Mailsystem Microsoft 365 und Identitäten über Microsoft Entra ID sind Voraussetzungen (OP-16) [O] |
| Dokumentenmanagement | Kein bestehendes DMS benannt; Papierpost wird eingescannt | – | Altdatenübernahme in Phase 0 klären [O] |

## 3.3 Heutige Abläufe und Rahmenbedingungen

| Thema | Heutige Situation | Quelle |
|---|---|---|
| Rechnungseingang | Rechnungen kommen per E-Mail und per Post. Papierpost wird eingescannt. Lieferanten senden dieselbe Rechnung häufig auf beiden Wegen, dadurch entstehen Dubletten. | Workshop |
| Kreditoren-Nummernkreise | Derselbe Lieferant hat in vielen Gesellschaften unterschiedliche Kreditorennummern. Livos-Kreditoren liegen im 70000er-Kreis, Kreditoren aus den Hausverwaltungen im 80000er-Kreis. Eine gesellschaftsübergreifende Konsolidierung gibt es nicht. | Workshop |
| Kreditorenanlage | Livos legt selbst keine Kreditoren in DATEV an. Trios legt Kreditoren an; die Hausverwaltungen legen eigene Kreditoren an. | Workshop |
| Rechnungen der Property Manager | Ca. 95 % der Rechnungen für verwaltete Objekte prüft, bucht und zahlt der Property Manager selbst. Livos ist daran nicht beteiligt. Rechnungen ab einer bestimmten Größenordnung gibt das Livos Asset Management frei; nach Aussage im Workshop geschieht das per E-Mail (zu bestätigen). Die Wertgrenzen der Property Manager sind nicht dokumentiert. | Workshop |
| Interne Rechnungen | Rechnungen, die nicht über einen Verwalter laufen, sollen erfasst, geprüft, freigegeben und an den Zahllauf übergeben werden. Freigaben laufen heute ohne durchgängiges System. | Workshop |
| Kürzungen | Kürzungen kommen häufig vor, etwa bei mangelhafter Leistung. Bei mehreren Positionen wird heute händisch nachgerechnet. | Workshop |
| Abschlagsrechnungen Bau | Bei großen Baumaßnahmen gehen kumulierte Abschlagsrechnungen ein. Auftragnehmer weisen teils falsche bereits gezahlte Beträge aus; die Prüfung erfolgt manuell anhand der Vorrechnungen. | Workshop |
| Freistellungsbescheinigungen | Für Bau-Rechnungen ist zu prüfen, ob eine gültige Freistellungsbescheinigung nach § 48b EStG vorliegt. | Workshop; Katalog 2.7 |
| Weitere Freigaben | Auch Vorgänge ohne Rechnung brauchen Freigaben, etwa Ausbuchungen auf Mietkonten. | Workshop |
| Buchung und Zahlung | Trios bucht in DATEV. Zahlungen werden über multicash ausgeführt. Zwischen Rechnungseingang und Verbuchung vergehen nach Einschätzung im Workshop teils Wochen. | Workshop; Katalog 5.5 |

## 3.4 Schmerzpunkte

| Nr. | Schmerzpunkt | Auswirkung | Adressiert in |
|---|---|---|---|
| SP-1 | Keine durchgängige Transparenz, wo eine Rechnung liegt und wer sie bearbeitet | Rückfragen, verzögerte Freigaben, Skontoverluste möglich | Kap. 10, 16 (Rechnungseingangsbuch, Eskalation) |
| SP-2 | Uneinheitliche Kreditorennummern je Gesellschaft und für Hausverwaltungen; keine konsolidierte Lieferantensicht | Keine gesellschaftsübergreifende Auswertung je Lieferant; hoher einmaliger Aufwand für die Zuordnung | Kap. 8 (AE-09) |
| SP-3 | Neue Kreditoren entstehen erst am Ende der Kette in DATEV; Livos kann sie nicht selbst anlegen | Rechnungen neuer Lieferanten bleiben liegen | Kap. 8, 9 (WF-04) |
| SP-4 | Eingeschränkter Zugriff auf DATEV durch das externe Hosting | Abgleiche und Auswertungen nur eingeschränkt möglich | Kap. 15 (S-01, S-02, S-06) |
| SP-5 | Dubletten durch Doppeleingang per E-Mail und Post (Workshop: „recht häufig") | Prüfaufwand, Risiko der Doppelzahlung | Kap. 9 (Duplikatsprüfung) |
| SP-6 | Kürzungen werden händisch nachgerechnet, bei langen Rechnungen aufwendig | Zeitaufwand, Rechenfehler, fehlende Nachvollziehbarkeit | Kap. 9 (AE-14) |
| SP-7 | Kumulierte Abschlagsrechnungen werden manuell gegen Vorrechnungen geprüft | Risiko von Überzahlungen | Kap. 9 (WF-02, AE-11) |
| SP-8 | Rückweisungen an Lieferanten erfordern manuelle E-Mails außerhalb des Prozesses | Aufwand, uneinheitliche Begründungen, keine Ablage am Vorgang | Kap. 9 (WF-05, AE-13) |
| SP-9 | Freigaben von PM-Rechnungen durch das Asset Management per E-Mail | Keine Vollständigkeitskontrolle, keine Vertreterregelung | Kap. 11 (WF-03) |
| SP-10 | Keine Auswertung der Bearbeitungszeiten je Schritt und je Benutzer | Engpässe bleiben unsichtbar | Kap. 16 (AE-16) |
| SP-11 | Vertretung im Krankheitsfall nicht geregelt | Aufgaben bleiben liegen | Kap. 10 (AE-17) |
| SP-12 | Unterlagen je Gesellschaft nicht auf Knopfdruck übergabefähig | Aufwand beim Verkauf von Gesellschaften und bei Betriebsprüfungen | Kap. 17 (AE-25) |

## 3.5 Ziele des DMS

Die Ziele sind so formuliert, dass sie nach der Einführung messbar sind. Die Zielwerte sind **Vorschläge von MDIS**. Livos legt die verbindlichen Werte im Prozess-Workshop fest; wo heute keine Ist-Werte vorliegen, wird in Phase 0 bzw. im Pilot eine Basismessung durchgeführt.

| Nr. | Ziel | Messgröße | Zielwert (Vorschlag) | Messung über |
|---|---|---|---|---|
| Z-1 | **Transparenz**: Jede Eingangsrechnung ist mit Status, aktuellem Schritt und Bearbeiter sichtbar | Anteil der Rechnungen im Rechnungseingangsbuch mit Status am Tag nach Eingang | 100 % der Rechnungen im Scope | Rechnungseingangsbuch |
| Z-2 | **Kurze Liegezeiten** | Anteil der Rechnungen, die länger als die Eskalationsfrist in einem Schritt liegen | unter 10 %; Eskalationsfrist Vorschlag 5 Arbeitstage je Schritt | Rechnungseingangsbuch („Aktueller Schritt seit"), evidanza |
| Z-3 | **Durchlaufzeit** vom Eingang bis zur Zahlungsfreigabe | Median in Arbeitstagen | höchstens 10 Arbeitstage (Basismessung im Pilot) | evidanza (S-12) |
| Z-4 | **Skonto nutzen** | Anteil skontofähiger Rechnungen, die vor Ablauf der Skontofrist zahlungsfreigegeben sind | mindestens 95 % | Rechnungseingangsbuch, evidanza |
| Z-5 | **Vollständigkeit** | Anteil der freigabepflichtigen PM-Rechnungen, die über WF-03 laufen | 100 % ab Einführung WF-03 | Rechnungseingangsbuch, Abgleich mit PM-Buchungsdaten (optional S-16) |
| Z-6 | **Automatisierungsgrad Erfassung** | Anteil der Rechnungen, deren Gesellschaft (Mandant) ohne manuelle Korrektur richtig zugeordnet wird | mindestens 90 %; Wert nach Test mit echten Livos-Belegen festlegen (OP-02) | Clearing-Quote im Rechnungseingangsbuch |
| Z-7 | **Automatisierungsgrad Kontierung** | Anteil der Kontierungsvorschläge (Sachkonto, Kostenstelle), die unverändert übernommen werden | mindestens 70 % nach 6 Monaten Betrieb | Stichprobe, Belegänderungsansicht |
| Z-8 | **Mandantentrennung** | Zugriffe auf Dokumente außerhalb der berechtigten Gesellschaften | 0; Berechtigungstest vor Go-live bestanden (OP-08) | Testprotokoll, Stichproben |
| Z-9 | **GoBD-Konformität** | Verfahrensdokumentation, unveränderte Originale, vollständige Protokolle | Verfahrensdokumentation vor Go-live freigegeben; 100 % der Originale unverändert archiviert | Verfahrensdokumentation, Prüfung |
| Z-10 | **Keine Doppelzahlungen** | Doppelt gezahlte Rechnungen | 0 | Duplikatsprüfung, Stichprobe DATEV-OPOS |
| Z-11 | **Aktuelle Buchhaltung** | Zeit von der Zahlungsfreigabe bis zur Übergabe des Buchungsvorschlags an DATEV | am selben Arbeitstag (ereignisgesteuert) | Protokoll S-01 |
| Z-12 | **Übergabefähigkeit je Gesellschaft** | Zeit bis zur Bereitstellung eines vollständigen Exportpakets einer Gesellschaft | höchstens 10 Arbeitstage nach Anforderung | Probeexport (jährlich) |

## 3.6 Scope

### 3.6.1 Im Scope, nach Phasen

Die Phasen folgen dem Prinzip der schrittweisen Einführung (P8). Details, Zeitplan und Pilotgesellschaften stehen in Kapitel 19.

| Phase | Inhalt | Wesentliche Bausteine |
|---|---|---|
| 0 | Vorbereitung | Entscheidungen zu den offenen P1-Punkten, Test-Tenant, Test Mandantenerkennung mit echten Belegen, Mengengerüst je Rolle, Aktenstruktur, Stammdaten Gesellschaften und Objekte |
| 1 | Rechnungseingang Standard | Eingangskanäle (E-Mail, Scan, E-Rechnung), WF-01 Standard-Eingangsrechnung, WF-04 Klärfall Mandant/Kreditor, WF-08 Ad-hoc-Aufgaben, DATEV-Anbindung (S-01, S-02), Erstbefüllung der Gesellschafts- und Objektstammdaten, Kreditor-Anlage-Anforderung an Trios (zunächst per E-Mail), Protokollierung der Schrittwechsel (S-12), Berechtigungen, Kreditoren- und Objektakten |
| 2 | Rollout, Freigabe PM-Rechnungen und Lieferantenkommunikation | Rollout auf alle Gesellschaften, WF-03 PM-Freigabe, WF-05 Rückweisung und Kürzungsmitteilung, automatische Anbindung der Lieferanten-App (S-04, S-05), Auswertungen in evidanza (S-12), Exportverfahren je Gesellschaft (S-15) |
| 3 | Bau und Erweiterungen | WF-02 Bau-Eingangsrechnung mit BIM4You (S-08 bis S-10), Rückmeldung „bezahlt" (S-06), Freistellungsbescheinigungen (AE-15), WF-10 externe Ad-hoc-Freigabe, optional PM-Buchungsdaten ins BI (S-16) |
| 4 | Verträge und Post | WF-06 Vertragsprozess mit d.velop contracts, WF-07 Postverteilung, KI-Klassifizierung, d.velop pilot für Fragen an Verträge |
| 5 | Ausblick | WF-09 weitere Freigaben ohne Rechnung (z. B. Ausbuchungen auf Mietkonten), perspektivische ERP-/PM-Anbindung (S-17) |

Die Protokollierung der Schrittwechsel (S-12) läuft ab dem Pilot-Go-live in Phase 1, damit die Historie vollständig ist; die Auswertungen in evidanza folgen in Phase 2 (Kapitel 19).

### 3.6.2 Nicht im Scope (Vorschlag, von Livos zu bestätigen)

| Thema | Begründung | Hinweis |
|---|---|---|
| Ausgangsrechnungen und Debitorenprozesse | Katalog und Zielarchitektur betreffen nur Eingangsrechnungen | Pflichten zur Ausstellung von E-Rechnungen sind mit Trios bzw. Steuerberatung zu klären |
| Buchung und Zahlung der Rechnungen, die Property Manager selbst verarbeiten (ca. 95 %) | Property Manager arbeiten in eigenen Systemen und dürfen nicht zur Systemnutzung verpflichtet werden | Freigabepflichtige PM-Rechnungen sind im Scope (WF-03) |
| Zahlungsausführung und Bankkommunikation | Verbleibt in DATEV und multicash | d.velop liefert die Zahlungsfreigabe; der Status „bezahlt" kommt zurück (S-06) |
| Bau-Budgetcontrolling, kumulierte VOB-Rechenlogik, Einbehaltverwaltung | Fachlich führend ist BIM4You | d.velop übergibt und übernimmt Ergebnisse (AE-11) |
| Sonderbuchungsinformationen (ARAP/PARP, Rückstellungen, Anzahlungen) | In der Zielarchitektur vorgesehen, aber fachlich nicht spezifiziert | Folgeprojekt; Monatsabschluss-Unterstützung zunächst über Export aus dem Rechnungseingangsbuch (AE-08) |
| Personalakten und Personaldokumente | Nicht Gegenstand von Katalog und Zielarchitektur; besondere Datenschutzanforderungen | Eigenes Vorhaben |
| Mieterkorrespondenz und Mieterakten | Fachprozesse der Bestandsverwaltung liegen weitgehend bei den Property Managern | Eingehende Mieterpost wird in Phase 4 nur klassifiziert und verteilt (K-09) |
| Übernahme von Altdaten aus Fremdsystemen | Kein Altsystem benannt | In Phase 0 zu klären; ggf. eigenes Arbeitspaket |
| Direkte Anbindung der ERP-Systeme der Property Manager | Katalog 5.4 „perspektivisch" | Folgeprojekt (S-17) |

## 3.7 Rahmenbedingungen und Prämissen

| Nr. | Rahmenbedingung | Konsequenz für das Konzept |
|---|---|---|
| RB-1 | **Standard zuerst, Erweiterungen klar abgegrenzt.** Livos erwartet Lösungen im Produktstandard und will keine technischen Middleware-Tabellen pflegen. | Designprinzipien P2 und P3: erst d.velop-Standard, dann Konfiguration, erst dann BeSync. Jede BeSync-Leistung ist mit Zweck, Auslöser und Betrieb als [A] ausgewiesen (Kapitel 15). MDIS betreibt und überwacht BeSync. Livos pflegt fachliche Daten ausschließlich in der bereits vorhandenen Lieferanten-App. |
| RB-2 | **Property Manager sind nicht zur Systemnutzung verpflichtbar.** | Der PM-Prozess (WF-03) funktioniert über E-Mail: Einreichung an ein Funktionspostfach, Rückmeldung per E-Mail. Ein Systemzugang für Property Manager ist optional. |
| RB-3 | **Livos legt keine Kreditoren in DATEV an.** Kreditoren legt Trios an. | Neue Lieferanten laufen in einen Klärfall; die Anlage-Anforderung geht aus der Lieferanten-App an Trios, der Beleg läuft nach dem nächsten Stammdatenabgleich weiter (AE-09, WF-04). |
| RB-4 | **DATEV wird extern gehostet** und von Trios bebucht. | Die DATEV-Anbindung erfordert ein zugelassenes Gateway beim Hoster und die Abstimmung mit Trios (AE-07, OP-04). |
| RB-5 | **E-Rechnungspflicht.** Seit 01.01.2025 müssen Unternehmen E-Rechnungen empfangen können; die Pflicht zur Ausstellung folgt in Übergangsstufen bis Ende 2026 bzw. 2027. Bei E-Rechnungen ist die XML-Datei das Original; Streichungen oder Änderungen durch den Empfänger sind nicht zulässig. | E-Rechnungen (ZUGFeRD, XRechnung, Factur-X) sind von Beginn an im Scope. Korrekturen laufen über Rückweisung und Neuanforderung beim Lieferanten; Leistungskürzungen über den Zahlbetrag (AE-14). |
| RB-6 | **GoBD und Unveränderbarkeit** (§ 146 Abs. 4 AO). | Originale bleiben unverändert (P5); Kürzungen, Korrekturen und Anmerkungen nur als Workflow-Daten oder Annotation. |
| RB-7 | **Cloud-Betrieb.** Die Lösung läuft als Software-as-a-Service im Browser ohne lokale Installation. | Betriebsform d.velop Cloud C1 (AWS, Frankfurt), da nur dort alle benötigten KI-Funktionen verfügbar sind (AE-01, OP-01). |
| RB-8 | **Microsoft 365 und Entra ID** als Mail- und Identitätsplattform (Prämisse). | E-Mail-Import über Microsoft Graph, Single Sign-on über OpenID Connect, Benutzerabgleich über SCIM. Zu bestätigen (OP-16). |
| RB-9 | **Soll-Prozesse sind noch nicht final festgelegt.** | Das Konzept macht begründete Vorschläge (Freigabegrenzen, Fristen, Gründe). Livos bestätigt sie im Prozess-Workshop (OP-17). |
| RB-10 | **Neuer Eingangsweg bei d.velop.** Der bisherige Kommunikationsweg für die Rechnungserkennung wird zum 01.01.2027 abgeschaltet. | Einrichtung von Beginn an über den neuen Weg inbound → document reader → smart invoice (AE-22). |

# 4 Anforderungen und Abdeckung

## 4.1 Überblick über den Leistungskatalog

Livos hat im Juli 2026 den Leistungskatalog „Digitales Rechnungsmanagement" vorgelegt. Er umfasst 29 Anforderungen in sechs Themenbereichen.

| Themenbereich | Katalognummern | Anzahl | Must | Should | Could |
|---|---|---|---|---|---|
| Systemarchitektur | 1.1 – 1.8 | 8 | 6 | 1 | 1 |
| Rechnungseingang & KI | 2.1 – 2.8 | 8 | 7 | 0 | 1 |
| Workflows & Dashboards | 3.1 – 3.4 | 4 | 4 | 0 | 0 |
| Externe Partner | 4.1 – 4.3 | 3 | 2 | 1 | 0 |
| Schnittstellen & Bauspezifika | 5.1 – 5.5 | 5 | 2 | 2 | 1 |
| DMS | 6.1 | 1 | 0 | 0 | 1 |
| **Summe** | | **29** | **21** | **4** | **4** |

Die Bewertung verwendet die Legende des Katalogs: **S** Standard, **K** Konfiguration, **A** Anpassung, **N** Nein (Kapitel 1.5). Kombinierte Werte wie „S / A" bedeuten: Der Kern ist Standard, ein benannter Teilaspekt erfordert eine Anpassung. Anpassungen setzt MDIS über die Integrationsplattform BeSync um; sie sind im Schnittstellenkatalog (Kapitel 15) mit Zweck, Auslöser und Betrieb beschrieben.

Die Bewertung berücksichtigt die Erkenntnisse aus dem Demo-Workshop vom 22.09.2026 und die Prüfung der d.velop-Produktdokumentation (Stand 09/2026). Sie ist konservativ: Wo eine Funktion nur mit Zusatzoption, Konfiguration oder Test belegbar ist, steht K oder ein Vorbehalt, nicht S.

## 4.2 Abdeckungsmatrix

| Nr. | Anforderung | Prio | Erfüllung | Lösung im Konzept | Verweis |
|---|---|---|---|---|---|
| 1.1 | Echte Mandantenfähigkeit (über 100 Gesellschaften, strikt getrennt, zentral verwaltet) | Must | **K** | Ein d.velop-Tenant, jede Gesellschaft als smart-invoice-Mandant (bis 1.000 je Bucket) und als Pflichteigenschaft „Mandant" auf jedem Dokument. Trennung über Restriction Sets, Freigabematrix-Spalte Mandant und Clearing je Mandant. | Kap. 5, 6, 13; AE-03, AE-18 |
| 1.2 | Webbasierter Zugriff (Cloud/SaaS, responsiv, ohne Installation) | Must | **S** | Browser-Client mit responsivem Design, Betrieb in der d.velop Cloud C1 (AWS, Frankfurt). | Kap. 5; AE-01 |
| 1.3 | App (Android/Apple) | Could | **S** | Native App d.velop mobile für iOS und Android, enthalten ab Edition documents business. Rechnungsfreigabe in der App wird im Test bestätigt (OP-38). | Kap. 12; AE-02; OP-38 |
| 1.4 | Individuelle Workflows je Gesellschaft, Freigabegrenzen, Personenketten | Must | **K** | Workflows je Prozesstyp (WF-01 bis WF-04), gesellschaftsindividuelle Freigaben über die Freigabematrix je Mandant und Kostenobjekt sowie Wertgrenzen-Verbindungen. Zweite Freigabe ab Betrag X über Wertgrenzen-Verbindung; das Hersteller-Feature „Vier-Augen ab Betrag" wird genutzt, sobald es allgemein freigegeben ist. | Kap. 10; AE-04, AE-05; OP-09 |
| 1.5 | Strikte Rollen- und Rechteverwaltung (intern und extern) | Must | **K** | Standardmechanik aus Berechtigungen je Kategorie und Rechtestufe, Restriction Sets für Gesellschaft und Objekt, Rollengruppen aus Microsoft Entra ID. Das Livos-Rollenmodell wird konfiguriert. | Kap. 13; AE-18 |
| 1.6 | Revisionssicherheit & GoBD, Export je Gesellschaft bei Verkauf | Must | **S / A** | Protokollierung, Versionierung, Aufbewahrung und Löschsperre sind Standard. Das Exportpaket je Gesellschaft (Originale, Metadaten, Protokolle) erstellt ein BeSync-Exportskript auf Basis der Export-API [A]. IDW-PS-880-Nachweis für die Cloud wird angefordert. | Kap. 17; AE-24, AE-25; S-15; OP-14 |
| 1.7 | Ablage weiterer Nachweise (Verträge, Aufträge, E-Mails) | Should | **S** | Anlagen am Beleg, eigene Kategorien für Nachweise, Aufträge, Verträge und Korrespondenz; automatische Mehrfachablage in Kreditoren-, Objekt- und Vorgangsakte. | Kap. 7; K-02 bis K-07; AE-19 |
| 1.8 | Händische Übersteuerung von Werten, Kontierung und Workflow | Must | **S** | Berechtigte Nutzer übersteuern Werte, Kontierung und Workflowweg; jede Änderung wird protokolliert. Kürzungen werden als Zahlbetrag mit Kürzungsgrund erfasst, das Original bleibt unverändert. | Kap. 9, 10; AE-14 |
| 2.1 | Automatischer Postfach-Import, Sammelpostfach für mehrere Empfänger | Must | **S** | E-Mail-Import über Microsoft Graph aus einer zentralen Rechnungsadresse plus Alias je Gesellschaft mit Vorbelegung des Mandanten. Voraussetzung: Microsoft 365. | Kap. 9; AE-22; S-14; OP-16 |
| 2.2 | KI-Erkennung der Pflichtangaben und Zuordnung zur richtigen Gesellschaft | Must | **K** | Pflichtangaben erkennt der document reader im Standard. Die Gesellschaft erkennt der Standard über Name und Anschrift. Bei gleichen Anschriften sichert ein Maßnahmenbündel die Zuordnung: exakte Gesellschaftsnamen, Käuferreferenz in E-Rechnungen, Alias-Postfächer, Klärfall. Trefferquote wird vor Go-live mit echten Livos-Belegen gemessen. | Kap. 6, 9; AE-23; OP-02 |
| 2.3 | Prozess für Rechnungen an unbekannte Gesellschaften | Must | **K** | Klärfall-Workflow WF-04 mit Clearing je Mandant und Klärfall-Mandant; Bearbeiter ordnet zu, weist zurück oder stößt die Anlage einer neuen Gesellschaft an. | Kap. 9; WF-04; M-05 |
| 2.4 | E-Rechnung (ZUGFeRD, XRechnung) mit Visualisierung für den Prüfer | Must | **S** | Empfang von ZUGFeRD 2.x, XRechnung 3.0 und Factur-X, Visualisierung als lesbares Dokument, Archivierung des XML-Originals. Formale Validierung erfolgt im Standard für XRechnung; eine Profilprüfung für ZUGFeRD kann ergänzt werden [A]. | Kap. 9, 17; AE-22 |
| 2.5 | Lernende Buchungs- und Kontierungsvorschläge | Must | **S** | KI-Kontierungsvorschläge für Sachkonto und Kostenstelle auf Belegebene, lernend aus Korrekturen (nur Betriebsform C1). Projekt- und Positionsbezug sowie kreditorenabhängige Kontierungsvorlagen per Konfiguration. | Kap. 8, 9; AE-01, AE-27 |
| 2.6 | Automatische steuerliche Prüfung und weitere Kriterien | Must | **S / A** | Standard: Prüfung der Pflichtangaben nach § 14 UStG, Duplikatsprüfung, XRechnung-Validierung, Hinweis bei abweichender Zahlungsbedingung. Das Kriterium „Freistellungsbescheinigung liegt vor" prüft eine BeSync-Erweiterung [A]. | Kap. 9; AE-15 |
| 2.7 | Freistellungsbescheinigung hinterlegen, automatische Erkennung, Vorschlag 15 % Abzug | Could | **A** | Bescheinigung als Dokument in der Kreditorenakte; BeSync führt den Gültigkeitsstatus je Kreditor und Gesellschaft, prüft Bau-Rechnungen beim Eingang und erzeugt Hinweis bzw. Klärfall mit Vorschlag Einbehalt 15 % als Zahlbetrag. Die Abfrage beim Bundeszentralamt für Steuern bleibt manuell. | Kap. 8, 9; AE-15; K-06, E-21 |
| 2.8 | Aufteilung auf Kostenstellen, Standardschlüssel je Gesellschaft | Must | **S / K** | Aufteilung auf mehrere Kostenstellen über Belegpositionen und Kostenobjekte ist Standard. Standardschlüssel je Gesellschaft werden über Kontierungsvorlagen konfiguriert; die prozentuale Logik wird im Test bestätigt. | Kap. 8, 9; OP-10 |
| 3.1 | Persönliches Dashboard / Inbox je Nutzer | Must | **S** | Aufgabenliste „Meine Aufgaben", Schnellzugriffe im Rechnungseingangsbuch je Rolle, Startseite mit Suche, Favoriten und zuletzt bearbeiteten Dokumenten. | Kap. 14, 16; M-08, M-10 |
| 3.2 | Management- und Controlling-Dashboard (Status, Bearbeiter, Liegezeit) | Must | **S / A** | Rechnungseingangsbuch mit Status, aktuellem Schritt, zugewiesenem Bearbeiter, „Aktueller Schritt seit" (aktuelle Liegezeit), Gruppierung je Gesellschaft und CSV-Export. Historische Durchlauf- und Liegezeiten je Schritt und Benutzer liefert eine BeSync-Protokollierung nach evidanza [A]. | Kap. 16; AE-16; M-09; S-12 |
| 3.3 | Automatisches Eskalationsmanagement | Must | **S / K** | Eskalation je Workflowschritt und dynamisch vor Skonto- und Nettofälligkeit, zwei Stufen, Empfänger regelbasiert je Mandant; Fristen per Konfiguration. Der Mailkanal wird im Test bestätigt. | Kap. 10; AE-17; OP-10 |
| 3.4 | Vertretungsregelungen (geplant und ungeplant) | Must | **S / K** | Abwesenheit mit Vertretung im Benutzerprofil. Administratoren und Vorgesetzte setzen die Abwesenheit auch für erkrankte Kollegen und leiten Aufgaben gesammelt weiter. Vertretungsregeln und Aufgabenzuordnung an Personen werden konfiguriert. | Kap. 10; AE-17; M-18 |
| 4.1 | Prozessunabhängigkeit Property Manager | Must | **K / A** | Eigener Freigabeprozess WF-03 für freigabepflichtige PM-Rechnungen: Einreichung per E-Mail an ein eigenes Postfach, Freigabe durch das Asset Management, keine Buchung und Zahlung in d.velop [K]. Rückmeldung an den Property Manager per E-Mail und optionale Übernahme der monatlichen PM-Buchungsdaten ins BI über BeSync [A]. | Kap. 11; AE-12; WF-03; S-11, S-16 |
| 4.2 | Ad-hoc-Freigabe per Mail/Link ohne Lizenz | Should | **K / A** | Externe Benutzeraufgabe in process studio: E-Mail mit Link auf ein Web-Formular, ohne Benutzerkonto, zeitlich begrenzt; Beleg als befristeter Teilen-Link [K]. Die Kopplung an den smart-invoice-Freigabeschritt übernimmt BeSync [A]. | Kap. 11; AE-26; WF-10; M-19 |
| 4.3 | Direkte Web-Anbindung für Kern-Partner | Must | **S** | Kernpartner arbeiten als Freigabeuser in d.velop invoices (Anzahl nicht begrenzt), mit Zwei-Faktor-Anmeldung und Sicht nur auf ihre Gesellschaften. Die lizenzrechtliche Zulässigkeit für Dritte wird mit d.velop bestätigt. | Kap. 11, 13; AE-26; OP-03 |
| 5.1 | DATEV-Schnittstelle, mehrfach täglich, inklusive Beleg | Must | **K** | Option „DATEV Rechnungswesen" (LDconnect über DATEVconnect) mit Gateway beim Hoster: Buchungsvorschlag mit Beleglink ereignisgesteuert je Rechnung, DATEV-Stammdaten täglich. Belegbild in DATEV optional über DATEV Unternehmen online. | Kap. 15; AE-07, AE-08; S-01 bis S-03; OP-04, OP-05 |
| 5.2 | Bau-Spezifika (kumulierte VOB-Abrechnung, Sicherheitseinbehalte) | Should | **N (d.velop) / A (über BIM4You)** | d.velop enthält keine VOB-Rechenlogik. Kennzeichnung (Belegart Abschlag/Schluss), Vorgangsakte und Anzeige der Ergebnisse sind in d.velop konfigurierbar. Rechnerische Prüfung und Einbehaltverwaltung erfolgen in BIM4You; die Ergebnisse übernimmt BeSync an den Beleg. | Kap. 9; AE-11; WF-02; E-14, E-22 |
| 5.3 | Schnittstelle zu BIM4You | Should | **A** | BeSync übergibt Bau-Rechnungen asynchron aus einem Wartezustand in smart invoice an BIM4You und übernimmt Prüfergebnis, Einbehalte, Freigabestatus und Prüfbericht. Datei- bzw. importbasiert, da BIM4You keine veröffentlichte API hat. | Kap. 15; AE-11; S-08 bis S-10; OP-06 |
| 5.4 | Perspektivische ERP-/PM-Anbindung über offene APIs | Could | **S / A** | Offene, dokumentierte REST-APIs sind Standard. Die konkrete Synchronisation mit Systemen der Property Manager ist ein Folgeprojekt. | Kap. 15; S-17 |
| 5.5 | Schnittstelle Zahlungsmanagement (Omikron), Zahlung nach Freigabe | Must | **A** | Zahlungsfreigabe als eigener Schritt in d.velop vor der DATEV-Übergabe. Zahlungsausführung über DATEV-Zahlungsvorschlag, SEPA-Datei und multicash mit Unterschrift berechtigter Nutzer (Standard von DATEV und Omikron). Den Status „bezahlt" mit Zahldatum setzt BeSync am Beleg [A]. | Kap. 9, 15; AE-06, AE-10; S-06, S-07 |
| 6.1 | Nutzung als DMS | Could | **S** | d.velop documents für Akten, Suche, Aufgaben, Outlook-Integration und Post; d.velop contracts für Verträge; d.velop pilot für Fragen an Dokumente. | Kap. 12; AE-20, AE-21 |

## 4.3 Auswertung

### 4.3.1 Verteilung der Erfüllungsgrade

| Erfüllung | Anzahl | Katalognummern |
|---|---|---|
| S | 10 | 1.2, 1.3, 1.7, 1.8, 2.1, 2.4, 2.5, 3.1, 4.3, 6.1 |
| S / K | 3 | 2.8, 3.3, 3.4 |
| S / A | 4 | 1.6, 2.6, 3.2, 5.4 |
| K | 6 | 1.1, 1.4, 1.5, 2.2, 2.3, 5.1 |
| K / A | 2 | 4.1, 4.2 |
| A | 3 | 2.7, 5.3, 5.5 |
| N (d.velop) / A (über BIM4You) | 1 | 5.2 |
| **Summe** | **29** | |

### 4.3.2 Erfüllung nach Priorität

| Priorität | S | S / K | S / A | K | K / A | A | N / A | Summe |
|---|---|---|---|---|---|---|---|---|
| Must | 7 | 3 | 3 | 6 | 1 | 1 | 0 | **21** |
| Should | 1 | 0 | 0 | 0 | 1 | 1 | 1 | **4** |
| Could | 2 | 0 | 1 | 0 | 0 | 1 | 0 | **4** |
| **Summe** | **10** | **3** | **4** | **6** | **2** | **3** | **1** | **29** |

### 4.3.3 Kernaussagen

1. **Alle 21 Must-Have-Anforderungen sind abgedeckt.** Kein Must-Have ist mit „N" bewertet.
2. **16 der 21 Must-Haves** erfüllt die Lösung ausschließlich mit d.velop-Standard und Konfiguration (S, K oder S / K).
3. **5 Must-Haves** enthalten einen Anpassungsanteil. In vier Fällen betrifft er nur einen klar benannten Teilaspekt, der Kern ist Standard oder Konfiguration:
   - 1.6 Exportpaket je Gesellschaft,
   - 2.6 Prüfkriterium Freistellungsbescheinigung,
   - 3.2 historische Durchlaufzeiten in evidanza,
   - 4.1 Rückmeldung an Property Manager und optionale Datenübernahme.
   Nur 5.5 (Zahlungsauslösung) ist insgesamt als Anpassung bewertet, weil die Kopplung d.velop – DATEV – multicash und die Rückmeldung „bezahlt" keine Standardfunktion eines einzelnen Produkts ist. Die Zahlungsausführung selbst bleibt im Standard von DATEV und multicash.
4. **5.2 Bau-Spezifika** ist die einzige Anforderung mit N-Anteil: d.velop rechnet keine VOB-Kumulation. Das Konzept verlagert die Rechenlogik bewusst in BIM4You, das dafür vorgesehen ist, und bindet es über BeSync an (P4).
5. **Eine Anforderung mit Vorbehalt:** 2.2 (Zuordnung zur Gesellschaft) ist als K bewertet, weil der Standard die Gesellschaft über Name und Anschrift erkennt. Der Test mit echten Livos-Belegen (OP-02) vor Go-live ist deshalb Pflicht.

### 4.3.4 Anpassungen (A) als MDIS-Leistung über BeSync

Alle Anpassungsanteile setzt MDIS auf der bestehenden Integrationsplattform BeSync um und betreibt sie (P3). Livos pflegt dafür keine technischen Tabellen; fachliche Pflege erfolgt nur in der Lieferanten-App.

| Katalog | Anpassungsanteil | BeSync-Leistung | Schnittstelle | Phase (Vorschlag) |
|---|---|---|---|---|
| 1.6 | Exportpaket je Gesellschaft | Exportskript über die Export-API, Pakete je Gesellschaft | S-15 | Voraussetzung (Mandant auf jedem Dokument) ab 1, Exportskript 2; danach anlassbezogen, Probeexport jährlich |
| 2.6 / 2.7 | Prüfung Freistellungsbescheinigung, Vorschlag 15 % | Gültigkeitsstatus je Kreditor und Gesellschaft, Prüfung beim Eingang, Hinweis/Klärfall | S-04 | 3 |
| 3.2 | Historische Durchlauf- und Liegezeiten | Protokollierung jedes Schrittwechsels, Staging-Datenbank, Anbindung evidanza | S-12 | Protokollierung ab 1, Berichte in evidanza ab 2 |
| 4.1 | PM-Rückmeldung, PM-Buchungsdaten | E-Mail-Versand an Property Manager; optional monatliche Buchungsdaten ins BI | S-11, S-16 | 2 bzw. 3 |
| 4.2 | Kopplung externe Freigabe an smart invoice | Start der externen Benutzeraufgabe und Rückführung des Ergebnisses | – (WF-10) | 3 |
| 5.2 / 5.3 | BIM4You-Anbindung | Übergabe Bau-Rechnung, Übernahme Prüfergebnis, Einbehalt, Freigabestatus, Prüfbericht; BIM4You-Stammdaten | S-08, S-09, S-10 | 3 |
| 5.4 | Synchronisation mit PM-Systemen | Folgeprojekt auf Basis der REST-APIs | S-17 | 5 |
| 5.5 | Rückmeldung „bezahlt" | Lesen der offenen Posten aus DATEV, Setzen von Zahlstatus und Zahldatum am Beleg | S-06 | 3 |

Hinzu kommen BeSync-Leistungen, die keinem Katalogpunkt direkt zugeordnet sind, aber aus dem Workshop folgen: Anbindung der Lieferanten-App (S-04, S-05) und die Lieferantenmail bei Rückweisung und Kürzung (S-11, WF-05).

## 4.4 Zusätzliche Anforderungen aus dem Workshop

Im Demo-Workshop am 22.09.2026 hat Livos Anforderungen genannt, die über den Katalog hinausgehen oder ihn präzisieren. Die folgende Tabelle führt sie sachlich zusammengefasst mit der Lösung im Konzept. Die vollständige Liste T-01 bis T-46 mit Einzelnachweis steht im Anhang (Kapitel 21).

### 4.4.1 Anforderungen und Lösungen

| T-Nr. | Anforderung | Katalogbezug | Lösung im Konzept | Status | Verweis |
|---|---|---|---|---|---|
| T-01 | Alle Anhänge aus einem definierten Postfach werden automatisch importiert und verarbeitet | 2.1 | E-Mail-Import über Microsoft Graph mit Importprofil je Postfach; zulässige Absender konfigurierbar | [S] | Kap. 9; AE-22; S-14 |
| T-02, T-05, T-10 | Eindeutige Lieferantenidentität trotz unterschiedlicher Kreditorennummern je Gesellschaft und für Hausverwaltungen; Schlüssel aus DATEV-Mandantennummer und Kreditorennummer; konsolidierte Sicht | 1.1, 5.1, 5.4 | Drei Nummernkreise: Konsolidierungsnummer in der Lieferanten-App (führend für die Identität), DATEV-Kreditorennummer je Mandant (führend für die Buchung), HV-Kreditorennummer. Mapping über den Schlüssel „DATEV-Mandantennummer + Kreditorennummer". Konsolidierungsnummer als Eigenschaft am Beleg; gesellschaftsübergreifende Suche. | [A] | Kap. 8; AE-09; E-07; S-04 |
| T-03, T-11 | Rechnungen neuer Lieferanten verarbeiten, obwohl Livos keine Kreditoren in DATEV anlegt; Prüfung durch eine berechtigte Person | 2.3 analog | Klärfall „Kreditor fehlt" → Anlage-Anforderung aus der Lieferanten-App an Trios → Anlage in DATEV → Stammdatenabgleich am Folgetag → Beleg läuft weiter | [K] / [A] | Kap. 8, 9; WF-04; M-05, M-16; S-05 |
| T-04 | Geringer Initialaufwand für die Zuordnung der Kreditoren über mehr als 100 Gesellschaften | 5.4 | KI-gestützte Erstkonsolidierung mit der MDIS-KI-Plattform X.One als Vorbelegung der Lieferanten-App, fachliche Nacharbeit durch Livos | [A] | Kap. 8, 19 |
| T-06, T-12 | Neue Kreditoren aus DATEV (auch aus Hausverwaltungen) kommen automatisch in den Lieferantenstamm; automatische Zuordnung zu neu angelegten DATEV-Kreditoren | 5.1, 5.4 | Täglicher Stammdatenabgleich aus DATEV in smart invoice (S-02); Lieferanten-App liest neue DATEV-Kreditoren und schlägt die Zuordnung zur Konsolidierungsnummer vor (S-05) | [K] / [A] | Kap. 8, 15 |
| T-07 | Property Manager dürfen nicht zur Nutzung eines Erfassungssystems verpflichtet werden | 4.1 | Rahmenbedingung RB-2; PM-Prozess ausschließlich über E-Mail | – | Kap. 3.7, 11 |
| T-08 | Abgleiche müssen trotz extern gehostetem DATEV funktionieren | 5.1 | Anbindung über ein vom Hoster zugelassenes Gateway (Riecken-Datengateway bzw. Cloud Gateway); Klärung mit Hoster und Trios vor Phase 1 | [K] / [O] | Kap. 15; AE-07; OP-04 |
| T-09 | Alle Rechnungen, die nicht über einen Verwalter laufen, werden in d.velop erfasst, geprüft, freigegeben und an den Zahllauf übergeben | 1.4, 5.5 | Scope von WF-01 und WF-02 | [S] / [K] | Kap. 3.6, 9 |
| T-13, T-14 | Freigabepflichtige PM-Rechnungen werden im System freigegeben, ohne Buchung und Zahlung; Transparenz, Vollständigkeit, Einsicht durch Vertreter | 4.1, 3.2, 3.4 | WF-03 mit eigenem Postfach, Freigabe durch das Asset Management gemäß Freigabematrix, Rückmeldung per E-Mail an den Property Manager | [K] / [A] | Kap. 11; AE-12; M-13; S-11 |
| T-15 | Nachvollziehbar, ob ein Wert aus dem Beleg oder aus den Stammdaten stammt | 2.2 | Erkannte Belegwerte und Stammdaten aus DATEV werden getrennt geführt; Abweichungen werden in der Verteilungsmaske als Hinweis angezeigt | [S] / [O] | Kap. 9, 14; M-02 |
| T-16 | Hinweis, wenn die IBAN der Rechnung von den Stammdaten abweicht | 2.6 | Beleg-IBAN (E-16) gegen Bankverbindungen aus DATEV; Warnung in der Verteilung. Verhalten im Standard wird getestet, sonst Prüfung über BeSync | [O] → [S] oder [A] | Kap. 9; OP-10 |
| T-17 | E-Mail-Benachrichtigungen abschaltbar, Arbeit nur über die Aufgabenliste | 3.1 | Benachrichtigungen je Benutzer einstellbar | [S] | Kap. 10 |
| T-18 | Fälligkeit wahlweise aus der Rechnung oder aus den Stammdaten, manuell änderbar | 1.8 | Fälligkeit aus der Zahlungsbedingung des Kreditors; Hinweis bei Abweichung vom Beleg; manuelle Änderung protokolliert | [S] | Kap. 9; E-15 |
| T-19 | Gesellschaft wird automatisch erkannt und der DATEV-Mandantennummer zugeordnet | 2.2, 5.1 | Mandanten-ID = DATEV-Mandantennummer (Vorschlag); Erkennung über Name und Anschrift mit Maßnahmenbündel und Test | [K] | Kap. 6; AE-03, AE-23; OP-02 |
| T-20 | Weitere Dokumente als Nachweis an die Rechnung anhängen | 1.7 | Anlagen am Beleg und Kategorie K-02 in der Vorgangsakte | [S] | Kap. 7 |
| T-21 | Der Buchungsschritt ist nur für die Buchhaltung (Trios bzw. Steuerberatung) zugänglich | 1.5 | Schritt Buchhaltung nur für Buchhaltungsuser der Rolle R-06 | [K] | Kap. 10, 13; R-06 |
| T-22 | Zahlung soll möglichst ohne Medienbruch nach dem Buchen ausgelöst werden | 5.5 | Getrennte Zahlungsfreigabe in d.velop vor der DATEV-Übergabe; Ausführung im DATEV-Zahlungsvorschlag und in multicash mit Unterschrift berechtigter Nutzer. Das Vier-Augen-Prinzip der Bankfreigabe bleibt erhalten. | [S] / [A] | Kap. 9, 15; AE-06, AE-10 |
| T-23, T-24 | Durchlauf- und Liegezeiten je Schritt und je Benutzer; Auswertung in evidanza | 3.2 | Aktuelle Liegezeit im Rechnungseingangsbuch; Historie über BeSync-Protokollierung nach evidanza | [S] / [A] | Kap. 16; AE-16; S-12 |
| T-25 | Zeitvorgaben je Prüfer und Schritt, danach Eskalation | 3.3 | Eskalationsfristen je Schritt und vor Fälligkeit, Empfänger je Mandant | [S] / [K] | Kap. 10; AE-17 |
| T-26 | Rückweisung mit ca. 5 Standardgründen und automatischer, vorformulierter E-Mail an den Lieferanten, ohne eigenes Mailprogramm | – (nahe 2.6) | Aktion „Ablehnen" mit Pflicht-Rückweisungsgrund aus einer Werteliste mit 5 Standardgründen [K]; Versand der Vorlagen-Mail an die Lieferantenadresse aus dem Kreditorenstamm und Ablage in der Kreditorenakte über BeSync [A] | [K] / [A] | Kap. 9; AE-13; WF-05; E-26; M-06; S-11 |
| T-27 | Dubletten aus Doppeleingang (E-Mail und Post) ohne Lieferantenmail ablehnen; Annahme nur mit Begründung | 2.6 | Duplikatsprüfung im Standard; Annahme nur mit Begründung und Protokoll; Ablehnung als Dublette ohne Lieferantenmail | [S] | Kap. 9 |
| T-28 | Freigaben auch für Vorgänge ohne Rechnung, z. B. Ausbuchungen auf Mietkonten | – (6.1) | Eigener Freigabeprozess in process studio | [K] | Kap. 11; WF-09 (Ausblick, Phase 5) |
| T-29, T-30 | Kürzungen (häufig), auch positionsweise mit automatischer Neuberechnung; Originalrechnung bleibt erhalten | 1.8, 1.6 | Rechnung bleibt unverändert. Kürzung über den Zahlbetrag auf Kopf- oder Positionsebene (Menge und Preis je Position mit Neuberechnung), Pflichtfeld Kürzungsgrund, Notiz; Protokoll über die Belegänderungsansicht. Optional Kürzungsmitteilung an den Lieferanten. | [K] | Kap. 9; AE-14; E-12, E-13; M-03; OP-05 |
| T-31 | Bei Abschlagsrechnungen die bereits akzeptierten Beträge früherer Abschläge einsehen | 5.2 | Vorgangsakte je Auftrag mit allen Abschlägen; geprüfte Beträge und Einbehalte aus BIM4You als Eigenschaften am Beleg | [K] / [A] | Kap. 7, 9; K-13; E-22 |
| T-32 | Kumulierte Abschlagsrechnungen automatisch gegen die geleisteten Zahlungen prüfen | 5.2, 5.3 | Rechnerische Prüfung in BIM4You; Ergebnis über BeSync an den Beleg | [A] | Kap. 9; AE-11; OP-06 |
| T-33 | E-Rechnung: Korrektur nur über Rückgabe und Neuanforderung | 2.4 | Formale Fehler → Rückweisung mit Grund „formaler E-Rechnungsfehler"; Leistungskürzungen über den Zahlbetrag, die E-Rechnung bleibt formal gültig | [K] / [A] | Kap. 9, 17; AE-13, AE-14 |
| T-34 | Prüfung, ob für Bau-Rechnungen eine Freistellungsbescheinigung beim Kreditor vorliegt | 2.6, 2.7 | Bescheinigung in der Kreditorenakte, Gültigkeitsstatus in BeSync, Prüfung beim Eingang | [A] | Kap. 8, 9; AE-15 |
| T-35 | Standardfunktionen vor Eigenentwicklung; keine Pflege technischer Middleware-Tabellen durch Livos | übergreifend | Designprinzipien P2 und P3; BeSync nur mit klarer Abgrenzung, Betrieb durch MDIS | – | Kap. 3.7, 5 |
| T-36 | Kategorie, Gesellschaft, Kreditor und Objekt auch bei sonstigen Dokumenten (z. B. Auftragsbestätigung) automatisch erkennen | 6.1, 2.2 | KI-Klassifizierung und Attributierung im Posteingang; bei Unsicherheit manuelle Klassifizierung | [S] / [O] | Kap. 12; AE-21; WF-07 |
| T-37 | Aktenhierarchie mit mehr als zwei Ebenen | 6.1 | Aktenplan mit bis zu 4 Ebenen: Gesellschaft → Objekt → Vorgang bzw. Vertrag; Kreditorenakte je Gesellschaft; Mehrfachablage | [K] | Kap. 7; AE-19; OP-17 |
| T-38 | Unterschiedliche Rechnungsworkflows | 1.4 | Workflows je Prozesstyp WF-01 bis WF-04 | [K] | Kap. 9 bis 11; AE-04 |
| T-39 | Vertretung bei Krankheit auch durch Administrator oder Vorgesetzte aktivierbar | 3.4 | Abwesenheit für Dritte setzen, Aufgaben gesammelt weiterleiten | [S] | Kap. 10; AE-17; M-18 |
| T-40 | Transparentes Lizenzmodell (Abrechnung nach Aktenanzahl oder Speichergröße?) | – | Lizenzierung nach Rechnungsvolumen und Buchhaltungsusern (d.velop invoices; Prüfer und Freigeber ohne Mengengrenze) sowie nach Benutzern für das DMS (platform edition); keine Abrechnung nach Aktenanzahl. Speicher- und Workflowkontingente je Tenant werden im Angebot ausgewiesen. | [S] | Kap. 5 (Lizenzarchitektur); AE-02 |
| T-41 | Fragen an Vertragsinhalte stellen (z. B. „Ist Skonto vereinbart?") | – (6.1) | d.velop pilot (enthalten ab Edition business) für Fragen an einzelne oder mehrere Dokumente; Grenzen bei langen Verträgen im Test prüfen | [S] / [O] | Kap. 12; AE-20, AE-27; OP-19 |

Die Anforderungen T-42 bis T-45 betreffen Angebot und Vertrieb und sind nicht Gegenstand des Konzepts. T-46 (Nutzung der MDIS-KI-Plattform für weitere Livos-Anwendungen) liegt außerhalb des DMS-Scopes und wird hier nicht weiter betrachtet.

### 4.4.2 Ergänzende Anforderungen aus der MDIS-Zielarchitektur

Die Zielarchitektur „DMS-Kernprozesse" enthält Elemente, die der Katalog nicht fordert. Das Konzept nimmt sie wie folgt auf.

| Element | Lösung im Konzept | Status | Verweis |
|---|---|---|---|
| DATEV-Vorerfassungsjournal bei der Verteilung, Verbuchung nach Freigabe (zweistufig) | Empfehlung: einstufige Übergabe nach der Zahlungsfreigabe; Transparenz über unverbuchte Rechnungen über das Rechnungseingangsbuch mit Export zum Monatsende; zweistufige Variante als Option | [K] / [O] | Kap. 5, 15; AE-08; OP-05 |
| Zahlungsrückmeldung DATEV → d.velop | Zahlstatus und Zahldatum am Beleg über BeSync | [A] | AE-10; S-06 |
| Freigabestatus, Einbehalt- und Kürzungsinformationen aus BIM4You | Eigenschaften und Prüfbericht am Beleg über BeSync | [A] | AE-11; S-09 |
| Umlageinformationen aus BIM4You | Bedeutung und Format mit Livos klären | [O] | OP-18 |
| Sonderbuchungsinformationen (ARAP/PARP, Rückstellungen, Anzahlungen) | Folgeprojekt | [O] | Kap. 3.6.2 |
| Prozessketten Verträge und Post | WF-06 mit d.velop contracts, WF-07 mit KI-Klassifizierung und Postverteilung | [S] / [K] | Kap. 12; AE-20, AE-21 |

## 4.5 Nicht-funktionale Anforderungen

Der Katalog enthält nur wenige ausdrückliche nicht-funktionale Anforderungen (1.2 Web, 1.3 App, 1.6 Revisionssicherheit). Die folgenden Anforderungen leiten sich daraus, aus dem Mengengerüst und aus der Produktdokumentation ab. Werte ohne Produktbeleg sind als Vorschlag gekennzeichnet.

| Nr. | Bereich | Anforderung | Lösung / Beleg | Status |
|---|---|---|---|---|
| NFA-01 | Verfügbarkeit | Hohe Verfügbarkeit während der Geschäftszeiten; zugesicherte Werte vertraglich festhalten | Betrieb durch d.velop in der Cloud C1; Verfügbarkeitszusage laut d.velop-Leistungsbeschreibung im Vertrag prüfen. Für BeSync-Leistungen: Überwachung und Wiederanlauf durch MDIS; Ausfall von BeSync hält den Rechnungsworkflow nicht an (Wartezustände, Nachverarbeitung). | [O] |
| NFA-02 | Datensicherung und Wiederherstellung | Tägliche Sicherung, definierte Wiederherstellungszeiten | d.velop: tägliche Backups, RPO 24 Stunden, Vorhaltung 30 Tage, RTO-Ziel 48 Stunden, halbjährliche Wiederherstellungstests (d.velop Cloud Leistungsbeschreibung) | [S] |
| NFA-03 | Informationssicherheit | Stand der Technik bei Verschlüsselung, Zertifizierung und Protokollierung | Verschlüsselung AES-256 bei Speicherung und TLS ab 1.2 bei Übertragung; d.velop zertifiziert nach ISO/IEC 27001 und TISAX; Audit-Trail sicherheitsrelevanter Ereignisse 180 Tage | [S] |
| NFA-04 | Revisionssicherheit | GoBD-konforme Archivierung, Nachweis durch Testat | IDW-PS-880-Prüfung für d.velop documents vorhanden; Geltung für die Cloud-Betriebsform bei d.velop anfordern; Verfahrensdokumentation als eigenes Arbeitspaket | [S] / [O] (OP-14) |
| NFA-05 | Anmeldung und Identitäten | Single Sign-on mit dem Livos-Konto; Benutzer und Gruppen zentral gepflegt | SSO über OpenID Connect mit Microsoft Entra ID, Benutzer- und Gruppenabgleich über SCIM 2.0 (ab Edition business) | [S] / [K] (OP-16) |
| NFA-06 | Externe Zugänge | Sichere Anmeldung für Externe ohne Livos-Konto | Einladung per E-Mail mit Zwei-Faktor-Anmeldung (TOTP oder FIDO2); Ad-hoc-Externe nur über befristete Links und Formulare | [S] |
| NFA-07 | Datenschutz | DSGVO-konforme Auftragsverarbeitung, Verarbeitung in der EU | Auftragsverarbeitungsvertrag mit d.velop; Verarbeitung grundsätzlich in der EU, in der Regel in Deutschland; Unterauftragsverarbeiter und Datenstandort im aktuellen AVV prüfen. Für d.velop pilot: Region des Sprachmodells und AVV klären. Für BeSync: AVV mit MDIS. | [S] / [O] (OP-19) |
| NFA-08 | Mengen und Skalierung | 5.000 bis 8.000 Eingangsrechnungen pro Jahr, über 100 Gesellschaften, ca. 80 Anwender; Wachstum bei neuen Gesellschaften ohne Umbau | d.velop invoices Paket Medium mit 750 Rechnungen pro Monat (einschließlich PM-Freigaberechnungen); Grenzen je Bucket: 1.000 Mandanten, 100.000 Kreditoren, 50.000 Sachkonten, 100 Workflowdefinitionen. Neue Gesellschaft mit wenigen, automatisierbaren Konfigurationsschritten (AE-18). process-studio-Kontingent beobachten (OP-11). | [S] / [O] |
| NFA-09 | Antwortzeiten | Flüssige Bearbeitung im Browser, auch bei langen Rechnungen (bis 30 Seiten) | Vorschlag: Öffnen einer Rechnung in der Bearbeitungsmaske in unter 3 Sekunden bei üblicher Büroanbindung; Messung im Pilot | Vorschlag |
| NFA-10 | Verarbeitungszeit Eingang | Rechnungen stehen zeitnah nach Eingang zur Bearbeitung bereit | Vorschlag: E-Mail-Rechnungen innerhalb von 60 Minuten nach Eingang im Stapel bzw. in der Verteilung; Messung im Pilot | Vorschlag |
| NFA-11 | Mobilität | Bearbeitung ortsunabhängig im Browser, Übersicht und Freigabe mobil | Responsiver Web-Client; App d.velop mobile für iOS und Android ab Edition business; Freigabe in der App im Test bestätigen | [S] / [O] |
| NFA-12 | Aufbewahrung | Gesetzliche Fristen je Dokumentart, keine vorzeitige Löschung | Aufbewahrung je Kategorie mit Löschsperre; automatisches Löschen zunächst deaktiviert, jährlicher freigegebener Löschlauf | [S] / [K] (AE-24) |
| NFA-13 | Betrieb der Erweiterungen | Klare Verantwortung für BeSync-Schnittstellen | Betrieb, Überwachung und Fehlerbehandlung durch MDIS; Fehler landen als Klärfall oder Hinweis im Prozess, nicht unbemerkt (P7) | [A] (Kap. 15, 18) |
| NFA-14 | Barrierefreiheit (optional) | Bedienbarkeit für Menschen mit Einschränkungen | Vorschlag: Konformität des Web-Clients mit gängigen Barrierefreiheitsstandards bei d.velop erfragen, falls Livos dies fordert | Vorschlag / [O] |
| NFA-15 | Bedienbarkeit | Einheitliche Oberfläche, geringer Schulungsaufwand | Rollenbezogene Startseiten und Schnellzugriffe (M-08 bis M-10); Arbeit überwiegend in Aufgabenliste und Rechnungseingangsbuch; Outlook-Integration | [S] / [K] |

# 5 Lösungsarchitektur

Dieses Kapitel beschreibt die Zielarchitektur des Livos-DMS. Es legt fest, welche Systeme beteiligt sind, welches System für welche Daten führend ist, welche d.velop-Bausteine eingesetzt werden und wie die Daten zwischen den Systemen fließen. Außerdem enthält es die Betriebsform, die Lizenzarchitektur, die Designprinzipien P1–P8 und die Architekturentscheidungen AE-01 bis AE-29. Die fachlichen Prozesse folgen in Kapitel 9 bis 12, die Schnittstellen im Detail in Kapitel 15.

Belegstatus: **[S]** Standard belegt · **[K]** Konfiguration · **[A]** Anpassung/Entwicklung (meist MDIS BeSync) · **[O]** offen/zu verifizieren.

## 5.1 Architekturüberblick

### 5.1.1 Systemlandschaft in Worten

Im Zentrum steht **d.velop** in der d.velop Cloud. d.velop ist die gemeinsame Plattform für drei Dokumentströme: Eingangsrechnungen, Verträge und Post. Alle Dokumente liegen in **einem** Repository von d.velop documents. Jedes Dokument und jede Akte trägt die Gesellschaft (Mandant) als Pflichtmerkmal (P1).

- **Eingangsrechnungen** kommen per E-Mail (Microsoft 365), als E-Rechnung oder als Scan an. Die Erkennung übernimmt der d.velop document reader, E-Rechnungen verarbeitet der eInvoice converter. Prüfung, Kontierung und Freigabe laufen in **smart invoice**, der Workflow-Komponente von d.velop invoices. Das **Rechnungseingangsbuch (REB)** zeigt den Stand aller Rechnungen.
- **DATEV** bleibt das operative FiBu-System. Der Buchhaltungsdienstleister **Trios** bucht dort. DATEV läuft bei einem externen Hoster und ist über das **Riecken Cloud Gateway** erreichbar. d.velop übergibt freigegebene Rechnungen als Buchungsvorschlag mit Beleglink über **LDconnect** (Option „DATEV Rechnungswesen") und erhält täglich die DATEV-Stammdaten zurück.
- Die **Zahlung** wird in DATEV vorbereitet und in **multicash (Omikron)** ausgeführt. Der Zahlstatus „bezahlt" kommt über BeSync zurück an den archivierten Beleg.
- **BIM4You** führt Bau-Budget, VOB-Prüfung und Einbehalte. Bau-Rechnungen durchlaufen einen asynchronen Prüfschritt in BIM4You. Das Ergebnis kommt als DMS-Eigenschaften und Prüfbericht zurück.
- **BeSync** ist die Middleware-Plattform von MDIS. Sie ist bei Livos bereits im Einsatz und trägt die **Lieferanten-App**. BeSync verbindet die Systeme dort, wo der d.velop-Standard endet (P3). MDIS betreibt BeSync; Livos pflegt keine technischen Middleware-Tabellen.
- **Property Manager (PM)** arbeiten in eigenen Systemen weiter. Sie reichen Rechnungen über Schwellwert per E-Mail zur Freigabe ein und erhalten die Entscheidung per E-Mail zurück (WF-03). Sie brauchen keinen Zugang.
- **evidanza** ist das BI-Werkzeug von Livos. Es erhält die Prozessereignisse aus d.velop über eine SQL-Staging-Schicht in BeSync.
- **Microsoft 365 / Entra ID** liefert Postfächer, Benutzer und Gruppen (SCIM) sowie die Anmeldung (SSO per OIDC). Die Nutzung von M365 und Entra ID bei Livos ist noch zu bestätigen (OP-16).

### 5.1.2 Systeme, Rolle und Datenhoheit

| System | Rolle in der Zielarchitektur | Führend für | Nicht führend für | Betrieb |
|---|---|---|---|---|
| d.velop documents (Cloud) | DMS, Archiv, Akten, Suche, Aufgaben, Rechte | Dokumente (Original, Versionen), Akten, DMS-Eigenschaften, Aufbewahrung | Buchungen, Kreditorenkonten | d.velop (C1) |
| d.velop invoices / smart invoice | Rechnungserkennung, Rechnungsworkflow, REB | Rechnungsbeleg im Workflow, Kontierungsvorschlag, Freigabe- und Workflowstatus, Freigabematrix | Kreditorenstamm, Sachkonten (kommen aus DATEV) | d.velop (C1) |
| d.velop contracts | Vertragsverwaltung, Fristen | Vertragsdaten, Fristen, Vertragsakte | – | d.velop (C1) |
| DATEV Rechnungswesen | operatives FiBu-System | Kreditorenkonten je Mandant, Sachkonten, KOST1/KOST2, Steuerschlüssel, Zahlungsbedingungen, Bankverbindungen, Buchungen, OPOS, Zahlungsvorschlag | Beleg, Freigabe | externer Hoster; Buchung durch Trios |
| Riecken Cloud Gateway | sicherer Zugang zu DATEVconnect beim Hoster | – (Transport) | – | Riecken / Hoster [O: OP-04] |
| LDconnect (LIONDEER) | DATEV-Konnektor, vertrieben als Option „DATEV Rechnungswesen" | Übergabe Buchungsvorschlag, täglicher Stammdatenabgleich DATEV → Bucket | – | LIONDEER / d.velop |
| multicash (Omikron) | Zahlungsverkehr (EBICS, Unterschriftsklassen) | Zahlungsausführung, elektronische Unterschrift | Zahlungsfreigabe (liegt in d.velop) | Livos |
| BIM4You (BIB GmbH) | Bau-Budgetcontrolling | Bau-Budget, Vergabeeinheiten, VOB-Kumulation, Einbehalte, Bau-Prüfergebnis | Rechnungsübergabe an DATEV (für Eingangsrechnungen deaktiviert) | Livos |
| BeSync (MDIS) mit Lieferanten-App | Middleware, Stammdaten-App | Lieferantenidentität (Konsolidierungsnummer), Kreditor-Mapping, Gesellschafts- und Objektstamm, FSB-Status, Prozessereignis-Historie | Buchung, Beleg | MDIS |
| Property-Manager-Systeme | Buchung und Zahlung der PM-verwalteten Rechnungen | ~95 % der PM-Rechnungen | Freigabe über Schwellwert (liegt in d.velop, WF-03) | je PM |
| evidanza | BI, Management-Auswertung | Kennzahlen, historische Durchlaufzeiten | operative Status (liegen im REB) | Livos / MDIS |
| Microsoft 365 / Entra ID | Postfächer, Identitäten, SSO | Benutzer, Gruppenmitgliedschaften, Postfächer | Rechte im DMS (liegen in d.velop) | Livos |

Grundregel (P4): Je Datenobjekt und Prozessschritt gibt es genau ein führendes System. Es gibt **keine** Doppelübergabe von Eingangsrechnungen nach DATEV. Nur d.velop übergibt Eingangsrechnungen an DATEV.

## 5.2 d.velop-Bausteine und ihr Zweck

Phasen gemäß Einführungsvorgehen (Kapitel 19): **1** Rechnungseingang · **2** PM-Freigabe und Rückmeldungen · **3** Bau/BIM4You, Zahlstatus, externe Ad-hoc-Freigabe · **4** Verträge und Post · **5** Ausblick.

| Baustein | Zweck bei Livos | Edition/Voraussetzung | Status | Phase |
|---|---|---|---|---|
| **d.velop invoices / smart invoice** | Rechnungsworkflows WF-01 bis WF-05, Freigabematrix mit Spalte Mandant, Clearing je Mandant, Eskalation, Kontierung, KI-Kontierungsvorschläge | invoices-Paket (AE-02); KI-Kontierung nur C1 | [S]/[K] | 1 |
| **Rechnungseingangsbuch (REB)** | Arbeits- und Managementsicht über alle Rechnungen, Schnellzugriffe je Rolle, CSV-Export | Teil von d.velop invoices | [S] | 1 |
| **d.velop document reader** | OCR und KI-Erkennung von Pflichtangaben, Mandant, Kreditor, Positionen | Teil von d.velop invoices | [S] (Mandantenerkennung [K], AE-23) | 1 |
| **d.velop eInvoice converter** | Verarbeitung und Visualisierung von ZUGFeRD 2.x, XRechnung 3.0, Factur-X; Validierung XRechnung | Teil von d.velop invoices | [S] | 1 |
| **d.velop inbound / email import** | Abruf der Rechnungspostfächer (M365 Graph), Alias je Gesellschaft mit eigenem Importprofil, Scan-Import; neuer Kommunikationsweg inbound → document reader → smart invoice | platform edition; M365 bei Livos (OP-16) | [S] | 1 (Post: 4) |
| **d.velop documents** (platform edition business) | Archiv, Akten, Suche, Aufgaben (WF-08), Rechte, Aufbewahrung, Teilen mit Externen | business für DMS-Vollnutzer (AE-02) | [S]/[K] | 1 |
| **d.velop process studio** | Prozesse außerhalb von smart invoice: externe Ad-hoc-Freigabe (WF-10), Vertragsfreigabe (WF-06, falls contracts keinen Standard bietet), jährlicher Löschlauf, Ausblick WF-09 | ab business; 1.000 Ausführungen/Monat (OP-11) | [K] | 3–5 |
| **d.velop contracts** | Vertragsverwaltung, Laufzeit- und Fristenberechnung, Fristenkalender, Vertragsakte (K-14) | contracts-Lizenz lesend/voll; setzt platform edition voraus | [S]/[K] (Freigabe OP-12) | 4 |
| **d.velop mail dispatcher** | Postverteilung an Gruppen mit Erinnerung und Eskalation (WF-07) | Cloud-Lizenz zu klären (OP-13) | [K] | 4 |
| **KI-Trennung und KI-Klassifizierung** | Trennung und Klassifizierung von Papierpost; < 80 % Sicherheit → „Unbestimmt" | nur C1, ab business | [S] | 4 |
| **d.velop pilot** | Fragen an Dokumente und Verträge, Zusammenfassungen, intelligenter Import | ab business | [S] (Grenzen OP-19) | 1 verfügbar, fachlicher Einsatz 4 |
| **d.velop mobile** | Aufgaben, Akten, Abwesenheit unterwegs (iOS, Android) | ab business | [S]; smart-invoice-Aufgaben in der App testen (OP-38) | 1 |
| **Outlook-Integration** | Ablage von E-Mails und Anhängen aus Outlook in Akten und Kategorien | ab business | [S] | 1 |
| **d.velop sign** | elektronische Signatur von Verträgen, auch durch Externe | Kontingent in business | [S] | 4 |
| **Teilen mit Externen** | zeitlich begrenzter Link (max. 180 Tage) für Rückweisung, Ad-hoc-Freigabe | ab business | [S] | 1/3 |
| **DmsConfig API, DMS-API, smart-invoice-API, Webhooks** | automatisierte Pflege von Mandanten, Datasets, Restriction Sets; Schnittstellen S-04 bis S-15 | ab business (API) | [S] (Nutzung durch BeSync [A]) | 1–5 |

Nicht eingesetzt werden: eigene Workflows je Gesellschaft (Limit 100 Workflowdefinitionen, P6), Zahlungsdateien aus d.velop (smart invoice erzeugt keine SEPA-Datei), die ecm:one-App „Invoices for DATEV" (eigenes Produkt, nicht smart invoice) und eine Buchung von Eingangsrechnungen aus BIM4You nach DATEV.

## 5.3 Umsysteme

| Umsystem | Funktion für Livos | Anbindung | Richtung | Schnittstellen | Status |
|---|---|---|---|---|---|
| **DATEV Rechnungswesen** mit **Trios** und **Riecken-Gateway** | FiBu, Kreditorenkonten je Mandant, Buchung, OPOS, Zahlungsvorschlag. Trios kontrolliert im Schritt Buchhaltung und bucht in DATEV. Livos legt keine Kreditoren in DATEV an (Workshop 22.09.2026) | LDconnect über DATEVconnect; bei gehostetem DATEV ist das Datengateway Pflicht (LDconnect Leistungsschein 11/2025) | beidseitig | S-01, S-02, S-03 (optional), S-05, S-06, S-07 | [K] (S-01/S-02); [A] (S-05/S-06) |
| **LDconnect** (LIONDEER) | Buchungsvorschlag mit 16 Feldern inkl. Dokumentenlink; Stammdaten täglich in den Bucket | Option „DATEV Rechnungswesen" von d.velop invoices | beidseitig | S-01, S-02 | [K] |
| **multicash** (Omikron) | Ausführung der Zahlungen aus dem DATEV-Zahlungsvorschlag (SEPA-XML, EBICS, Unterschriftsklassen) | Standard DATEV → multicash | DATEV → multicash | S-07 | [S] (außerhalb d.velop) |
| **BIM4You** (BIB GmbH) | Bau-Budgetcontrolling, kumulierte VOB-Prüfung, Einbehalte, Nachträge | keine veröffentlichte API; Import über E-Rechnungsimport/Austauschordner, Rückweg über Export/Polling durch BeSync | beidseitig | S-08, S-09, S-10 | [A] (OP-06) |
| **Property Manager** | buchen und zahlen PM-Rechnungen selbst; Freigabe über Schwellwert durch Livos Asset Management | E-Mail an eigenes Freigabepostfach; Rückmeldung per E-Mail über BeSync | beidseitig | S-14, S-11, S-16 (optional) | [K]/[A] |
| **BeSync / Lieferanten-App** (MDIS) | Konsolidierungsnummer, Kreditor-Mapping, Gesellschafts- und Objektstamm, FSB-Status, Ereignisprotokoll, Mailversand, Export | REST-APIs von d.velop (smart invoice, DMS, DmsConfig), Webhooks | beidseitig | S-04, S-05, S-06, S-08, S-09, S-10, S-11, S-12, S-15, S-16 | [A] |
| **evidanza** | Management-Auswertungen, historische Durchlauf- und Liegezeiten je Benutzer und Schritt | MS-SQL-Staging in BeSync; evidanza liest per SQL | d.velop → evidanza | S-12 | [A] |
| **Microsoft 365 / Entra ID** | Postfächer, Benutzer, Gruppen, SSO | email import (Graph); SCIM 2.0; OIDC | M365 → d.velop | S-13, S-14 | [S]/[K] (OP-16) |

Hinweise zu den Umsystemen:

- **DATEV-Betrieb:** Wer DATEV betreibt und lizenziert (Livos, Trios oder Hoster), wer das Gateway beauftragt und ob alle Livos-Mandanten unter einer Beraternummer liegen, ist offen (OP-04). Davon hängen Bestellung, Freigabe und Kosten der DATEV-Komponenten ab.
- **LDconnect-Grenzen:** Der Buchungsvorschlag enthält keine Fälligkeit, kein Skonto, keine Postensperre und keine IBAN. Stammdaten werden nur täglich abgeglichen. Ein neu in DATEV angelegter Kreditor steht deshalb erst am Folgetag in smart invoice zur Verfügung (Kapitel 8.2).
- **BIM4You:** BIM4You bringt ein eigenes Rechnungseingangsbuch, einen Freigabemanager und einen DATEV-Connector mit. Für Eingangsrechnungen wird der DATEV-Export aus BIM4You deaktiviert, damit es keine Doppelbuchung gibt (P4, AE-11). Welches System je Rechnungstyp Bau führend ist, entscheidet Livos mit der BIB GmbH (OP-06).

## 5.4 Datenflüsse

### 5.4.1 Datenflusstabelle

| Nr. | Von → Nach | Objekt | Auslöser | Schnittstelle | Status |
|---|---|---|---|---|---|
| F-1 | Lieferant → M365 → d.velop | Rechnung als PDF, ZUGFeRD, XRechnung | E-Mail an `rechnung@…` oder Alias je Gesellschaft | S-14 | [S] |
| F-2 | Poststelle (Scan) → d.velop | gescannte Rechnung, Post | Scan-Stapel | inbound scan (kein Schnittstellen-ID, Standard) | [S] |
| F-3 | PM → M365 → d.velop | Rechnung über Schwellwert zur Freigabe | E-Mail an `freigabe-hv@…` | S-14 | [S] |
| F-4 | Entra ID → d.velop | Benutzer, Gruppen | laufend (SCIM) | S-13 | [S]/[K] |
| F-5 | DATEV → Bucket | Kreditoren je Mandant, Sachkonten, Steuerschlüssel, Zahlungsbedingungen, Bankverbindungen, KOST1/KOST2 | täglich | S-02 | [K] |
| F-6 | Lieferanten-App → d.velop | Gesellschaftsstamm (smart-invoice-Mandanten, Dataset Mandant), Objektstamm (Dataset Objekt), Restriction-Set-Werte, Konsolidierungsnummer | nächtlich und bei Änderung | S-04 | [A] |
| F-7 | Lieferanten-App ↔ DATEV/Trios | Kreditor-Mapping, Anlage-Anforderung neuer Kreditor | bei Neuanlage | S-05 | [A] |
| F-8 | BIM4You → Bucket | Projekte, Vergabeeinheiten, Verträge (Custom Entities) | nächtlich | S-10 | [A] |
| F-9 | smart invoice → BeSync → BIM4You | Kopfdaten, PDF/XML, Beleg-ID als Referenz | Schrittverbindung „Bauprüfung" (asynchroner Transfer) | S-08 | [A] |
| F-10 | BIM4You → BeSync → d.velop | geprüfter Betrag, Einbehalt, Freigabestatus BIM4You als **DMS-Eigenschaften**; Prüfbericht als K-08; Transfer-Rückmeldung `successful` | Freigabe oder Storno in BIM4You (Polling) | S-09 | [A] |
| F-11 | smart invoice → DATEV | Buchungsvorschlag (16 Felder) + Beleglink | Schritt Buchhaltung nach Zahlungsfreigabe (ereignisgesteuert) | S-01 | [K] |
| F-12 | d.velop → DATEV Unternehmen online | Belegbild (optional) | Übergabe | S-03 | [K] optional |
| F-13 | DATEV → multicash | SEPA-XML aus Zahlungsvorschlag | Zahllauf durch Trios/Livos | S-07 | [S] |
| F-14 | multicash → DATEV | Kontoauszug | Bankabruf | Standard DATEV/multicash | [S] |
| F-15 | DATEV → BeSync → d.velop | Zahlstatus „bezahlt", Zahldatum als **DMS-Eigenschaften** am archivierten Beleg | täglich | S-06 | [A] |
| F-16 | smart invoice → BeSync → Lieferant/PM | Rückweisungs-, Kürzungs- und PM-Rückmeldemail; Ablage als K-07 | Ablehnen / Endverbindung | S-11 | [A] |
| F-17 | smart invoice → BeSync → evidanza | Schrittwechsel (Beleg, Mandant, Schritt, Zeit, Bearbeiter) | jeder Schrittwechsel + nächtliche Abfrage | S-12 | [A] |
| F-18 | d.velop → Archivpaket | Originale, Metadaten, Protokolle einer Gesellschaft | Anlass (Verkauf, Prüfung) | S-15 | [A] |
| F-19 | PM → BeSync → BI | monatliche DATEV-Buchungsdaten der PM | monatlich | S-16 | [A] optional, Phase 3 |
| F-20 | PM-ERP ↔ d.velop | Stammdaten | Folgeprojekt | S-17 | [A] Ausblick |

### 5.4.2 Anpassungen gegenüber der Folie „Zielarchitektur"

Die MDIS-Folie „DMS-Systemarchitekturen" (05/2025) zeigt d.velop als Drehscheibe zwischen DATEV und BIM4You. Diese Grundidee bleibt. Nach der Detailanalyse ändern sich einzelne Flüsse. Die folgende Tabelle stellt Folie und Zielbild gegenüber.

| Fluss laut Folie | Zielbild im Konzept | Grund |
|---|---|---|
| d.velop → DATEV: „ER-Vorerfassungsjournal" bei der Verteilung **und** „Verbuchung von ER" nach der fachlichen Freigabe (zweistufig) | **Empfehlung: einstufige Übergabe** als Buchungsvorschlag nach der Zahlungsfreigabe (S-01). Die Transparenz über noch nicht verbuchte Rechnungen liefert das REB (Status, Beträge, CSV-Export zum Monatsende, z. B. für Rückstellungen). Option für Phase 3: frühe Übergabe mit Postensperre über BeSync/EXTF [A] | LDconnect kennt nur eine Übergabe je Rechnung. LDconnect überträgt keine Zahlungssperre. Deshalb muss die Zahlungsfreigabe vor der DATEV-Übergabe liegen (AE-06, AE-08). Entscheidung mit Trios und Livos: **O** (OP-05) |
| d.velop → DATEV: „Zahlungs-Journale" | Zahlungen entstehen in DATEV aus dem Zahlungsvorschlag und werden in multicash ausgeführt (S-07). d.velop liefert die Zahlungsfreigabe als Workflowschritt vor der Übergabe | smart invoice erzeugt keine Zahlungsdatei. Unterschrift und Vier-Augen-Prinzip bleiben in multicash (AE-10) |
| d.velop → DATEV: „Sonderbuchungsinformationen" (ARAP/PARP, Rückstellungen, Anzahlungen) | nicht Teil des ersten Ausbaus. Rückstellungsbedarf für offene Rechnungen über REB-Export; Sonderbuchungsinfos aus BIM4You als Folgeprojekt | kein Standardweg belegt; Format und Bedarf offen (AE-11) |
| DATEV → d.velop: „Zahlungsrückmeldung" | BeSync liest die offenen Posten aus DATEV (DATEVconnect accounts-payable) und setzt **Zahlstatus/Zahldatum als DMS-Eigenschaften** am archivierten Beleg (S-06) | LDconnect liefert keinen Zahlstatus. Abgeschlossene smart-invoice-Belege sind per API nicht änderbar, DMS-Eigenschaften schon (AE-10) |
| BIM4You → d.velop: „Einbehalt- und Kürzungsinformationen", „Freigabestatus" | BeSync schreibt das Ergebnis als **DMS-Eigenschaften** (E-22) und legt den Prüfbericht als K-08 ab. Den **Zahlbetrag** im laufenden smart-invoice-Beleg setzt die Rechnungsprüfung auf Basis des BIM4You-Ergebnisses. Ein automatisches Schreiben in laufende smart-invoice-Belege ist nicht belegt (OP-07) | Die smart-invoice-API bietet keinen dokumentierten Endpunkt zum Ändern laufender Belege (AE-11) |
| BIM4You → d.velop: „Umlageinformationen" | offen, bis Bedeutung und Format geklärt sind | OP-18 |
| d.velop → BIM4You: „ER-Journale" | asynchroner Transfer nur für Bau-Rechnungen (WF-02) an der Schrittverbindung „Bauprüfung" (S-08) | smart-invoice-Transfer mit Wartezeit bis 28 Tage belegt |
| (nicht auf der Folie) Stammdatenflüsse | DATEV → Bucket täglich (S-02); Lieferanten-App → d.velop (S-04); BIM4You-Stamm → Bucket (S-10) | ohne Stammdaten keine Erkennung, Kontierung und Rechte (Kapitel 8) |
| (nicht auf der Folie) Property Manager, evidanza, Entra ID | ergänzt als F-3, F-16, F-17, F-19, F-4 | Anforderungen 4.1, 3.2, 1.5 |

## 5.5 Betriebsform und Umgebungen

### 5.5.1 Empfehlung

Livos nutzt die **d.velop Cloud in der Betriebsform C1 (Multi-Tenant, AWS, Standort Frankfurt)** mit einem produktiven Tenant und einem getrennten Test- und Abnahme-Tenant (AE-01).

| Kriterium | C1 (AWS) | C2 (T Cloud Public) | Bewertung für Livos |
|---|---|---|---|
| KI-Kontierungsvorschläge (Katalog 2.5, Must) | ja | nein | nur C1 erfüllt 2.5 im Standard |
| KI-Trennung und KI-Klassifizierung Post | ja (ab business) | nein | nur C1 erfüllt den Postprozess (WF-07) automatisiert |
| DATEV-Optionen | Rechnungswesen: C1/H/O; Unternehmen online: C1/H | nicht angeboten | nur C1 erlaubt die DATEV-Anbindung (AE-07) |
| Funktionspostfächer | unbegrenzt | ein M365-Postfach mit Aliasen | C1 flexibler |
| process studio im invoices-Paket | nicht enthalten (kommt über platform edition) | enthalten | kein Nachteil, da platform edition business ohnehin nötig ist (AE-02) |
| Datenstandort | AWS mit Standorten u. a. in Frankfurt | europäischer Anbieter | aktuelle Standortzusage im Auftragsverarbeitungsvertrag prüfen [O] |

Quellen: d.velop invoices Leistungsbeschreibung 12/2025; d.velop documents platform edition Leistungsbeschreibung 10/2025; d.velop cloud platform Leistungsbeschreibung 07/2026.

### 5.5.2 Umgebungen

| Umgebung | Zweck | Inhalt | Hinweise |
|---|---|---|---|
| **Produktiv-Tenant** (z. B. `livos.d-velop.cloud`, Name Vorschlag) | Betrieb aller Gesellschaften | ein Repository, ein smart-invoice-Bucket, alle Kategorien, Workflows, Anbindungen | Speicher- und Workflowkontingente gelten je produktivem Tenant |
| **Test- und Abnahme-Tenant** | Konfigurationstests, Abnahme, Schulung, Tests der offenen Punkte (z. B. OP-08, OP-10) | gleiche Konfiguration, anonymisierte oder fiktive Testdaten, Test-Anbindungen (LDconnect-Testsystem, BeSync-Testinstanz) | Lizenzierung des Test-Tenants klären (OP-20); Konfigurationstransport über DmsConfig-Pakete zu prüfen |
| **Demo-Instanz** `mdisconsulting.d-velop.cloud` | nur Vorführung | geteilter MDIS-Tenant | wird **nicht** weiterverwendet; die Demo-Struktur wird nicht übernommen (AE-29) |

Begründung für einen einzigen Produktiv-Tenant: Ein Tenant trennt Kunden, nicht Gesellschaften. Die Trennung der Gesellschaften erfolgt datensatzgenau über die Eigenschaft Mandant und Berechtigungen (Kapitel 6 und 13). Mehrere Tenants würden Kontingente, Konfiguration, Benutzer und Workflows vervielfachen und die gesellschaftsübergreifende Sicht (Katalog 3.2) verhindern.

Offen ist, in welcher Betriebsform die Demo-Instanz läuft (OP-01). Die Aussagen zu KI-Funktionen sind deshalb im Test-Tenant in C1 zu bestätigen.

## 5.6 Lizenzarchitektur

### 5.6.1 Lizenzmetriken

Die Lizenzierung besteht aus zwei Teilen mit unterschiedlicher Logik. Preise stehen im Angebot, nicht in diesem Konzept.

| Baustein | Metrik | Enthalten (laut Leistungsbeschreibung) | Wer braucht es bei Livos | Quelle |
|---|---|---|---|---|
| **d.velop invoices**, Paket Medium (AE-02) | **Rechnungsvolumen je Monat** (Medium: 750 Rechnungen/Monat) + Anzahl **Buchhaltungsuser** (Medium: 10) | **Freigabeuser in beliebiger Zahl**, Rechnungserkennung, smart invoice, REB, Teilen von Rechnungen per Link; Mehrmenge über das 12-fache der Monatsmenge wird je Rechnung berechnet | Buchhaltungsuser: Rechnungseingang/Verteilung (R-02), Trios (R-06). Freigabeuser: Prüfer, Freigeber, Zahlungsfreigeber, Kernpartner (R-03, R-04, R-05, R-08) | d.velop invoices Leistungsbeschreibung 12/2025 |
| **d.velop documents platform edition business** | **je benanntem Benutzer und Monat** | Archiv, Akten, Suche, mobile App, Outlook, d.velop pilot, process studio (1.000 Ausführungen/Monat), d.velop sign (50 Siegel/Monat), Teilen mit Externen, SSO/OIDC, API | DMS-Vollnutzer: Poststelle (R-01), Controlling (R-07), Fachadministration (R-12), Geschäftsführung bei Bedarf (R-04), Vertragsbearbeitung | Leistungsbeschreibung platform edition 10/2025 |
| **d.velop contracts** | je Benutzer und Monat, **lesend** (restricted) oder **voll** | Vertragsverwaltung, Fristen, Vertragsakte | Vertragsmanager voll (R-11), Vertragsleser lesend | d.velop contracts Preise & Pläne |
| **Option DATEV Rechnungswesen** (LDconnect) | Option zu d.velop invoices; LDconnect nach Mandanten und Rechnungen gestaffelt | Buchungsvorschlag, Stammdatenabgleich | zentral für alle Mandanten | LDconnect Preisliste; Metrik bei >100 Mandanten klären (OP-04) |
| DATEV-seitige Komponenten | DATEV-Preisliste | DATEVconnect, ggf. Beleganzeige Drittanbieter, Zusatzmodul für Drittanbieter bei DATEVasp | Betreiber des DATEV-Systems | DATEV-Preisliste 08/2026; Zuständigkeit OP-04 |
| Riecken Cloud Gateway | Vertrag Riecken/LIONDEER | Gateway-Betrieb | Betreiber des DATEV-Systems | OP-04 |
| BeSync-Leistungen | MDIS-Leistung (Betrieb und Entwicklung) | S-04 bis S-16 gemäß Kapitel 15 | MDIS | Angebot MDIS |

Wichtige Folgerungen:

- Der Rechnungsteil ist **volumengetrieben**. Prüfer und Freigeber verursachen keine Benutzerkosten.
- Der DMS-Teil ist **benutzergetrieben**. Entscheidend ist, wer einen vollen documents-Zugang braucht.
- Lizenziert wird **nicht** nach Anzahl Akten oder Dokumenten. Mengenbezug entsteht nur über Speicher, Import-, Workflow- und KI-Kontingente je Tenant.
- Die über 100 Gesellschaften treiben die d.velop-Lizenz nicht, solange sie in einem Tenant liegen. Kostenrelevant sind sie bei LDconnect (Mandantenstaffel) und bei DATEV-Komponenten.

### 5.6.2 Kontingente je Tenant (Beobachtungsgrößen)

| Kontingent | Wert (Edition) | Erwartung Livos | Bewertung |
|---|---|---|---|
| Rechnungen je Monat (invoices Medium) | 750 | 5.000–8.000 Rechnungen/Jahr (≈ 420–670/Monat) zuzüglich PM-Freigabebelege (WF-03 zählen ins Volumen) | ausreichend, Reserve für PM-Freigaben prüfen |
| Buchhaltungsuser (Medium) | 10 | Kreditorenbuchhaltung Livos + Trios | Anzahl in Phase 0 festlegen |
| Speicher invoices Medium / platform edition business | 150 GB / 1.000 GB je produktivem Tenant | Rechnungen ca. 4 GB/Jahr (Annahme 0,5 MB je Beleg) | unkritisch |
| Dokumenteneingang | 10.000 Dokumente/Monat/Tenant | Rechnungen + Post | unkritisch |
| E-Mail-Import | 10.000 E-Mails/Monat/Postfach | Rechnungspostfach | unkritisch |
| process studio (business) | 1.000 Workflowausführungen/Monat/Tenant | WF-06, WF-07 (falls process studio), WF-10, Löschlauf | knapp, falls Post und Rechnungsnebenprozesse über process studio laufen; ob smart invoice mitzählt, ist offen (OP-11); sonst Edition ultimate prüfen |
| d.velop sign (business) | 50 fortgeschrittene Siegel/Monat/Tenant | Vertragsunterschriften | Bedarf in Phase 4 erheben |
| d.velop pilot | Token-/Nachrichtenkontingent je Tenant/Benutzer | Fragen an Verträge | Kontingentangaben in d.velop-Unterlagen widersprüchlich; mit d.velop klären (OP-19) |
| Rechnungen je Tag | max. 5.000 | 20–30 | unkritisch |

### 5.6.3 Offene Mengen- und Lizenzfragen

| Frage | Klärung mit | Bezug |
|---|---|---|
| Anzahl Buchhaltungsuser (Livos intern, Trios) | Livos, Trios | R-02, R-06 |
| Anzahl DMS-Vollnutzer (platform edition business) je Rolle | Livos (Prozess-Workshop) | R-01, R-04, R-07, R-11, R-12 |
| Müssen alle Benutzer im Tenant eine platform-edition-Lizenz haben, sobald business gebucht ist (Mischlizenz)? | d.velop | OP-03 |
| Dürfen Dritte (Trios, Projektsteuerer, Architekten, PM) als Buchhaltungs- oder Freigabeuser arbeiten? | d.velop | OP-03 |
| Metrik und Preis Option DATEV und LDconnect bei >100 DATEV-Mandanten | d.velop, LIONDEER | OP-04 |
| Anzahl contracts-Nutzer lesend/voll | Livos | R-11 |
| Kontingent process studio und Zählweise | d.velop | OP-11 |
| Lizenz Test-Tenant | d.velop | OP-20 |
| Zeitweiser Nur-Lese-Zugang für Betriebsprüfer (Z1) | d.velop | R-14, Kapitel 17 |
| Cloud-Lizenz mail dispatcher | d.velop | OP-13 |

## 5.7 Designprinzipien

| ID | Prinzip | Konsequenz im Konzept | Umsetzung in Kapitel |
|---|---|---|---|
| P1 | **Ein Beleg, ein Schlüssel:** Die Gesellschaft (Mandant) ist auf jedem Dokument und jeder Akte Pflicht. | Rechte, Aktenbildung, Workflow-Routing, DATEV-Mandant und Export bei Gesellschaftsverkauf hängen an der Eigenschaft Mandant (E-01). | 6, 7, 13, 17 |
| P2 | **Standard vor Konfiguration vor Entwicklung.** | Erst smart invoice, documents, contracts im Standard, dann Konfiguration, erst dann BeSync. | alle |
| P3 | **BeSync nur, wo der Standard endet – klar abgegrenzt und von MDIS betrieben.** Livos pflegt keine technischen Middleware-Tabellen; fachliche Pflege nur in der Lieferanten-App. | Jede BeSync-Leistung ist als [A] mit Zweck, Auslöser und Betrieb im Schnittstellenkatalog S-xx ausgewiesen. | 8, 15, 18 |
| P4 | **Ein führendes System je Datenobjekt und je Prozessschritt.** | DATEV führt Kreditorenkonten und Buchungen, die Lieferanten-App die Lieferantenidentität, d.velop Beleg, Workflow, Freigabe und Archiv, BIM4You Bau-Budget, VOB und Einbehalte, multicash die Zahlungsausführung. Keine Doppelübergabe nach DATEV. | 5.1, 8 |
| P5 | **Das Original bleibt unverändert** (GoBD, § 146 Abs. 4 AO; bei E-Rechnungen ist das XML das Original). | Kürzungen, Korrekturen und Anmerkungen nur als Workflowdaten oder Annotation. | 9, 17 |
| P6 | **Gesellschaftsunterschiede über Regeln, nicht über Kopien.** | Workflows je Prozesstyp; Gesellschaftslogik über Freigabematrix (Spalte Mandant), Bedingungen und Gruppen. | 6, 10 |
| P7 | **Automatisierung mit Mensch im Loop.** | Jede Automatik hat einen Klärfall und eine manuelle Übersteuerung mit Protokoll (Katalog 1.8). | 9, 10 |
| P8 | **Schrittweise Einführung.** | Rechnungseingang zuerst, dann PM-Freigabe, Bau/BIM4You, Verträge, Post. | 19 |

## 5.8 Architekturentscheidungen

Status: **E** = empfohlen, von Livos zu bestätigen · **F** = fachlich gesetzt (folgt aus Anforderungen oder Recht) · **O** = offen, Optionen sind im Konzept dargestellt.

| ID | Entscheidung | Begründung (kurz) | Status | Kapitel |
|---|---|---|---|---|
| AE-01 | d.velop Cloud C1 (AWS, Frankfurt); ein Produktiv-Tenant und ein Test-/Abnahme-Tenant | nur C1 bietet KI-Kontierung, KI-Postklassifizierung und die DATEV-Optionen | E | 5.5 |
| AE-02 | invoices Medium + platform edition business für DMS-Vollnutzer + Option DATEV Rechnungswesen + d.velop contracts | Rechnungsvolumen passt zu Medium; basic hat kein SSO, keine API, kein process studio, kein externes Teilen | E | 5.6 |
| AE-03 | ein Repository, ein Bucket; jede Gesellschaft = ein smart-invoice-Mandant; Schlüssel = Mandanten-ID in der DMS-Eigenschaft „Mandant"; Vorschlag Mandanten-ID = DATEV-Mandantennummer | ein einheitlicher Schlüssel für Rechte, Akten, Freigabematrix und LDconnect; Limits je Bucket beobachten | E | 6 |
| AE-04 | Rechnungsworkflows in smart invoice je Prozesstyp (WF-01 bis WF-04), nicht je Gesellschaft | max. 100 Workflowdefinitionen; Matrix, Eskalation, Vertretung und REB im Standard | E | 9, 10 |
| AE-05 | gesellschaftsindividuelle Freigaben über die Freigabematrix; zweite Freigabe ab Betrag über Wertgrenzen-Verbindung (netto); Prüfer ≠ Freigeber | Vier-Augen-Automatik ist Vorschau-Feature; Wertgrenzen gelten je Kostenobjekt | E | 10 |
| AE-06 | Schrittmodell WF-01: Verteilung → Sachliche Prüfung & Kontierung → Fachliche Freigabe → Zahlungsfreigabe → Buchhaltung | Zahlungsfreigabe muss vor der DATEV-Übergabe liegen, da LDconnect keine Zahlungssperre überträgt | E | 9 |
| AE-07 | DATEV-Anbindung über Option DATEV Rechnungswesen (LDconnect) mit Riecken-Gateway; Übergabe ereignisgesteuert, Stammdaten täglich | erfüllt Katalog 5.1 („nicht nur 1× pro Tag") als K; Beleg als Link | E | 15 |
| AE-08 | einstufige DATEV-Übergabe nach Zahlungsfreigabe; Transparenz über das REB; frühe Übergabe mit Postensperre als Option Phase 3 | LDconnect kennt nur eine Übergabe je Rechnung | O | 5.4, 9 |
| AE-09 | drei Nummernkreise (Konsolidierungsnummer, DATEV-Kreditor je Mandant, HV-Kreditor); DATEV-Stammdaten im Bucket nur über LDconnect; neuer Kreditor über Klärfall → Lieferanten-App → Trios → DATEV → Sync | ein schreibendes System je Stammdatenobjekt; Livos legt keine DATEV-Kreditoren an | E (Alternative O) | 8 |
| AE-10 | Zahlung: Zahlungsfreigabe in d.velop → DATEV bucht → Zahlungsvorschlag → multicash → Status „bezahlt" per BeSync als DMS-Eigenschaft | smart invoice erzeugt keine Zahlungsdatei; Unterschrift bleibt in multicash | E | 9, 15 |
| AE-11 | BIM4You-Integration für Bau-Rechnungen (WF-02) über asynchronen Transfer und BeSync; Ergebnis als DMS-Eigenschaften; Zahlbetrag setzt die Rechnungsprüfung; nur d.velop übergibt ER an DATEV | BIM4You ohne veröffentlichte API; kein API-Schreibzugriff auf laufende Belege belegt | E (führendes System je Rechnungstyp: O) | 9, 15 |
| AE-12 | PM-Freigabeprozess WF-03 in smart invoice mit eigenem Postfach, ohne Buchung und Zahlung; Rückmeldung per E-Mail über BeSync | PM nicht zur Systemnutzung verpflichtbar | E | 11 |
| AE-13 | Rückweisung an Lieferanten mit Pflichtgrund; Mail über BeSync und Microsoft Graph oder d.velop-Messaging-API (Festlegung in Phase 0, OP-25); Ablage als Korrespondenz | smart invoice sendet nicht an externe Adressen | E | 9 |
| AE-14 | Kürzungen über Zahlbetrag + Kürzungsgrund + Notiz; Original bleibt unverändert | P5, GoBD | E | 9 |
| AE-15 | Freistellungsbescheinigung als Dokument in der Kreditorenakte, FSB-Status in BeSync, Hinweis/Klärfall bei Bau-Kreditoren | kein FSB-Feld im Kreditorenstamm; BZSt ohne API | E (Phase 3) | 8, 9 |
| AE-16 | Reporting im REB; historische Durchlaufzeiten über BeSync-Staging und evidanza | Aufgabenhistorie nur 30–365 Tage | E | 16 |
| AE-17 | Eskalation und Vertretung im Standard; Admin setzt Abwesenheit für erkrankte Kollegen | Katalog 3.3, 3.4 | E | 10 |
| AE-18 | Berechtigungen je Kategorie × Rechtestufe mit Restriction Sets `RS_Mandant`, `RS_Objekt`; Identitäten aus Entra ID per SCIM | Anzahl Berechtigungen unabhängig von der Gesellschaftszahl | E (Tests OP) | 6, 13 |
| AE-19 | Aktenplan mit max. 4 Ebenen; Mehrfachablage per Aktenbildungsregeln; Lieferantensicht über gespeicherte Suche | Cloud-Strukturregeln belegt; Workshop-Empfehlung 4–5 Ebenen | E | 7.6 |
| AE-20 | Verträge in d.velop contracts; Vertragsfreigabe über process studio, falls kein Standard; KI-Fragen über d.velop pilot | gleiche Plattform, gleiche Akten und Rechte | E (Phase 4) | 12 |
| AE-21 | Post: Scan und Funktionspostfächer, KI-Trennung/-Klassifizierung, Verteilung mit mail dispatcher | nur C1, ab business | E (Phase 4) | 12 |
| AE-22 | zentrale Rechnungsadresse plus Alias je Gesellschaft; E-Rechnung über dieselben Postfächer; neuer Weg inbound → document reader → smart invoice | alter Kommunikationsweg wird zum 01.01.2027 abgeschaltet | E | 9 |
| AE-23 | Mandantenerkennung über Maßnahmenbündel (Anschreiben, Alias, exakter Name, Klärfall, Test mit echten Belegen) | Standard erkennt Empfänger nur über Name und Anschrift | F | 6.8, 9 |
| AE-24 | Aufbewahrung je Kategorie ab Datumseigenschaft „Aufbewahrungsbeginn"; Löschsperre; automatisches Löschen zunächst aus | BEG IV (8 Jahre Buchungsbelege); Ablaufhemmung § 147 Abs. 3 S. 5 AO | E | 7.7, 17 |
| AE-25 | Export je Gesellschaft über repo export-API und BeSync-Skript | Exportfilter kennt keine Eigenschaft; P1 ist Voraussetzung | E | 17 |
| AE-26 | Kernpartner als Freigabeuser; Ad-hoc-Externe über externe Benutzeraufgabe in process studio | Freigabeuser beliebig; Zulässigkeit für Dritte offen | E | 11, 13 |
| AE-27 | KI: document reader, KI-Kontierung, KI-Postklassifizierung, d.velop pilot; MDIS X.One für Kreditorenkonsolidierung | d.velop pilot beantwortet Fragen an Dokumente im Standard | E | 8, 12 |
| AE-28 | Gesellschafts- und Objektstamm führend in der Lieferanten-App/BeSync; Verteilung per API an smart invoice, Datasets und Restriction Sets | P4; APIs belegt | E | 6, 8 |
| AE-29 | Ist-Demo nicht 1:1 übernehmen; Produktivmodell baut auf den smart-invoice-Onboarding-Eigenschaften auf | doppelte und konkurrierende Eigenschaften in der Demo | F | 7 |

# 6 Mandanten- und Organisationsmodell

Livos verwaltet über 100 Gesellschaften in den Segmenten Bestand, Privatisierung und Bau. Das Mandantenmodell legt fest, wie diese Gesellschaften in d.velop abgebildet, getrennt, erkannt, neu angelegt und bei Verkauf herausgelöst werden. Es setzt die Architekturentscheidungen AE-03, AE-18, AE-23 und AE-28 um. Die Rechte im Detail beschreibt Kapitel 13, die Stammdaten Kapitel 8.

## 6.1 Begriffe

Das Wort „Mandant" hat bei d.velop und DATEV mehrere Bedeutungen. Das Konzept verwendet die Begriffe wie folgt.

| Begriff | Bedeutung | Anzahl bei Livos | Quelle |
|---|---|---|---|
| **Organisation** (d.velop cloud center) | Verwaltungseinheit für Verträge und Tenants eines Kunden | 1 | d.velop cloud platform Leistungsbeschreibung 07/2026 |
| **Tenant** (d.velop cloud-Mandant) | abgesicherter Cloudbereich mit eigener Subdomain und lebenslanger Tenant-ID; trennt Kunden voneinander, nicht Gesellschaften | 1 produktiv + 1 Test/Abnahme (AE-01) | ebd. |
| **Repository** | Dokumentenspeicher in d.velop documents mit Kategorien, Eigenschaften, Akten und Berechtigungen | 1 (Service-Limit: max. 50) | d.velop invoices Leistungsbeschreibung 12/2025 |
| **Bucket** | Stammdatenspeicher von smart invoice (Mandanten, Kreditoren, Sachkonten, Kostenstellen, Custom Entities) | 1 (d.velop empfiehlt einen Bucket; Limit max. 50) | smart invoice Cloud Handbuch 06/2026 |
| **smart-invoice-Mandant** (Company) | Rechnungsempfänger im Bucket; „jede Rechnung benötigt einen Mandanten"; Felder: ID, Name, Anschrift, PLZ, Ort, Währung, Land | ein Mandant je Gesellschaft | smart-invoice-API (Cloud) |
| **DMS-Eigenschaft Mandant** (E-01) | Eigenschaft an Dokumenten und Akten; vom smart-invoice-Onboarding angelegt; Träger von Rechten, Aktenbildung und Export | Pflicht auf allen Kategorien | smart invoice Cloud Handbuch 06/2026 |
| **DATEV-Bestand** | Buchhaltung einer Gesellschaft in DATEV, adressiert über Beraternummer und Mandantennummer | ein Bestand je Gesellschaft (Annahme, zu bestätigen) | DATEVconnect |
| **Gesellschaft** | rechtliche Einheit der LIVOS Gruppe | >100 | Leistungskatalog 07/2026 |
| **Segment** (E-31) | fachliche Gruppierung der Gesellschaften: Bestand · Privatisierung · Bau | 3 | Leistungskatalog |
| **Freigabeverbund** | Gruppe von Gesellschaften mit gemeinsamer Freigabe- und Leseverantwortung (z. B. gleiche Geschäftsführung) | nach Bedarf | Vorschlag MDIS |

**Festlegung:** Im Konzept gilt **Gesellschaft = smart-invoice-Mandant = Wert der DMS-Eigenschaft Mandant**. Es gibt keine zweite Eigenschaft „Gesellschaft" (AE-03, AE-29).

## 6.2 Grundmodell

```
Organisation Livos (d.velop cloud center)
 ├─ Produktiv-Tenant (C1)
 │   ├─ Repository (d.velop documents)
 │   │    Eigenschaft Mandant (E-01) auf jedem Dokument und jeder Akte
 │   │    Restriction Set RS_Mandant, RS_Objekt · Aktenbildung · Aufbewahrung
 │   └─ smart invoice
 │        Bucket (1) ── Mandanten 1..n ── Kreditoren/Sachkonten/KOST je Mandant
 │        Workflows je Prozesstyp (WF-01 … WF-04) · Freigabematrix mit Spalte Mandant
 │        Clearing je Mandant · REB-Berechtigung je Mandant
 └─ Test-/Abnahme-Tenant (gleiche Struktur)
```

Die Gesellschaft wird nicht über eigene Tenants, Repositories, Buckets oder Workflows getrennt. Die Trennung entsteht über **einen** Schlüssel, der in allen Bausteinen gleich ist (P1, P6). Begründung:

- Die Service-Limits (1.000 Mandanten je Bucket, 100 Workflowdefinitionen) lassen einen Workflow je Gesellschaft nicht zu (d.velop invoices Leistungsbeschreibung 12/2025).
- Kontingente und Administration gelten je Tenant. Mehrere Tenants würden sie vervielfachen und die gesellschaftsübergreifende Sicht für Buchhaltung, Controlling und Management verhindern.
- Das smart-invoice-Onboarding legt die Eigenschaften Mandant und Mandantenname als Pflichtzuordnung zum DMS an. Rechte, Aktenbildung und LDconnect arbeiten mandantenbezogen. Ein abweichender Schlüssel im DMS würde ein Mapping erfordern und Fehler erzeugen.

## 6.3 Mandanten-ID-Schema

### 6.3.1 Vorschlag

**Mandanten-ID = DATEV-Mandantennummer** der Gesellschaft (AE-03, Vorschlag). Sie ist eindeutig, stabil und in DATEV, bei Trios und in LDconnect bereits bekannt. Die Anzeige erfolgt über den Mandantennamen (E-02).

| Anforderung an den Schlüssel | Umsetzung | Begründung |
|---|---|---|
| eindeutig über alle Gesellschaften | DATEV-Mandantennummer; liegen die Gesellschaften unter mehreren Beraternummern, dann Format „Beraternummer-Mandantennummer" | DATEVconnect adressiert Bestände als „Beraternummer-Mandantennummer" |
| identisch mit dem Schlüssel, den LDconnect im Bucket verwendet | Format mit LIONDEER abstimmen; LDconnect überträgt Werte mit technischer Feldlänge (führende Nullen) | Kreditoren und Sachkonten hängen im Bucket an der Mandanten-ID (OP-04, ED-04) |
| feste Länge, nur Ziffern (und ggf. Bindestrich) | z. B. fünfstellig mit führenden Nullen | vermeidet Teilstring-Treffer in Berechtigungsfiltern (`100` in `1001`; Test T08) und Probleme mit Groß-/Kleinschreibung in der Freigabematrix |
| unveränderlich | Mandanten-ID wird nie umgenummeriert; Umfirmierung ändert nur den Namen | Rechte, Akten und Export hängen am Schlüssel |
| Gesellschaften ohne DATEV-Bestand | eigener Nummernbereich nach Abstimmung mit Trios (z. B. vorläufige Nummer, die bei DATEV-Anlage nicht wechselt) | Rechnungen können vor der DATEV-Anlage eingehen (Katalog 2.3) |

**Beispiel (fiktiv):** Livos Objektgesellschaft Nord mbH → Mandanten-ID `10010`, Mandantenname „Livos Objektgesellschaft Nord mbH". Gruppen: `DMS_G_10010`, `SI_Freigeber_10010`.

### 6.3.2 Abstimmungsbedarf mit Trios und LIONDEER

| Frage | Bezug |
|---|---|
| Liegen alle Livos-Bestände unter einer Beraternummer und auf einem DATEV-System? | OP-04 |
| Welches Format verwendet LDconnect als Mandanten-ID im Bucket? Ist es konfigurierbar? | OP-04 |
| Gibt es Gesellschaften ohne eigenen DATEV-Bestand (z. B. in Gründung)? Wie werden sie nummeriert? | OP-17 |
| Wie werden die PM-Buchhaltungen (80000er-Kreditoren) den DATEV-Beständen zugeordnet? | Kapitel 8.2 |

## 6.4 Gesellschaftsstamm (AE-28)

Führend für den Gesellschaftsstamm ist die Lieferanten-App auf BeSync. Livos pflegt die fachlichen Felder dort. BeSync verteilt die Werte per API an die d.velop-Bausteine (S-04).

| Feld | Pflicht | Beispiel (fiktiv) | Ziel in d.velop | Zweck |
|---|---|---|---|---|
| Mandanten-ID | ja | 10010 | smart-invoice-Mandant `id`; Dataset Mandant; Restriction Set; Gruppenname | Schlüssel (P1) |
| Name exakt wie auf Rechnungen | ja | Livos Objektgesellschaft Nord mbH | smart-invoice-Mandant `name`; Mandantenname (E-02) | Mandantenerkennung, Anzeige |
| Anschrift (Straße, PLZ, Ort, Land) | ja | Hafenstraße 22, 20359 Hamburg, DE | smart-invoice-Mandant `address`, `zip_code`, `city`, `country` | Mandantenerkennung |
| Währung | ja | EUR | `local_currency` | Belegverarbeitung |
| USt-IdNr. | ja, falls vorhanden | DE311222333 | nur BeSync (kein Feld am smart-invoice-Mandanten) | Abgleich E-Rechnung, Prüfhinweis |
| Steuernummer | ja | 43/123/45678 | nur BeSync | § 14 UStG, Prüfhinweis |
| DATEV-Beraternummer / Mandantennummer | ja | – / 10010 | LDconnect-Konfiguration | DATEV-Zuordnung |
| Segment | ja | Bestand | Dataset Segment (E-31) | Auswertung, Matrix |
| Bauleistender-Kennzeichen § 13b | ja | Nein | BeSync, Prüfregel | Plausibilität Reverse Charge (E-20) |
| Verwaltungsart | ja | PM-verwaltet | BeSync; auf Objektebene E-30 | Routing WF-03 |
| Property Manager (bei PM-Verwaltung) | bedingt | Hausverwaltung Beispiel GmbH | BeSync | PM-Rückmeldung |
| Freigabeverbund | ja | Verbund Nord | Gruppe `DMS_GF_<Verbund>`, Freigabematrix | Lese- und Freigaberechte |
| Käuferreferenz für E-Rechnungen (BT-10) | empfohlen | Vorgabe je Gesellschaft | Lieferantenanschreiben | Mandantenerkennung |
| Alias-Postfach | empfohlen | `rechnung+10010@…` (Format Vorschlag) | Importprofil mit Vorbelegung Mandant | Mandantenerkennung |
| Status | ja | aktiv · in Gründung · verkauft · gesperrt | BeSync; steuert Onboarding/Offboarding | Lebenszyklus |
| Gültig ab / bis | ja | 01.01.2027 / – | BeSync | Historie |

Der smart-invoice-Mandant kennt ein Feld `parent_id`. Seine Bedeutung ist nicht dokumentiert. Es wird erst genutzt, wenn d.velop die Semantik bestätigt [O].

## 6.5 Segmente und Freigabeverbünde

| Gruppierung | Zweck | Abbildung | Status |
|---|---|---|---|
| **Segment** (Bestand, Privatisierung, Bau) | Auswertung im REB und in evidanza; Steuerung von Prozessvarianten (z. B. Bau → WF-02) | Eigenschaft E-31, abgeleitet aus dem Gesellschaftsstamm; Wertemenge statisch | [K] |
| **Freigabeverbund** | gemeinsame Geschäftsführung oder Verantwortliche für mehrere Gesellschaften sehen und freigeben deren Rechnungen | Gruppe `DMS_GF_<Verbund>` mit Werteliste der Mandanten-IDs in `RS_Mandant`; Freigabematrix-Zeilen je Mandant, erzeugt aus der Verbunddefinition | [K]; Zeilenpflege per API [A] |
| **Gesellschaftsgruppe** | Werteträger für eine einzelne Gesellschaft | Gruppe `DMS_G_<MandantNr>` in `RS_Mandant` | [K] |
| **Zentrale Funktionen** (Kreditorenbuchhaltung, Trios, Controlling) | Sicht auf alle Gesellschaften | eigene Berechtigung ohne Mandant-Filter, smart invoice „Globale Rechnungsliste" | [S]/[K] |

Regeln:

- Die Freigabematrix hat eine Spalte Mandant. Eine Zeile gilt für einen Mandanten. Ob Platzhalter oder Mehrfachwerte in der Spalte möglich sind, ist nicht dokumentiert. Deshalb erzeugt BeSync die Matrixzeilen je Mandant aus der Verbunddefinition in der Lieferanten-App [A]. Die Matrix ist per API pflegbar (smart-invoice-API).
- Die REB-Workflowberechtigung ist je Eintrag an eine Mandantennummer gebunden. Für Verbünde entstehen daher mehrere Einträge. Ob mehrere Mandanten je Eintrag möglich sind, wird im Test-Tenant geprüft (Test T20). Eine API dafür ist nicht dokumentiert; die Pflege kann manuell nötig sein.
- Vertretungen sollen innerhalb desselben Freigabeverbunds liegen. Eine Vertretung wird bei Öffnen der Aufgabe zu den Workflowbeteiligten hinzugefügt und erhält damit Leserecht auf die Rechnung (AE-17).

## 6.6 Limits und ihre Beobachtung

| Limit (je Bucket bzw. Tenant) | Wert | Erwartung Livos | Risiko | Beobachtung und Maßnahme |
|---|---|---|---|---|
| Mandanten je Bucket | 1.000 | >100 | gering | jährliche Prüfung |
| Kreditoren je Bucket (Kreditoren zählen **je Mandant**) | 100.000 | >100 Mandanten × Ø Kreditoren je Mandant; Rechenbeispiel 110 × 900 ≈ 99.000 (Annahme) | **mittel bis hoch** | Ist-Zahl aus DATEV vor Projektstart ermitteln; nur aktive Kreditoren übertragen (Filter in LDconnect zu klären); Frühwarnung bei 70 % (Vorschlag); Erhöhung mit d.velop vereinbaren (laut Leistungsbeschreibung möglich) |
| Kreditor-Bankverbindungen je Bucket | 100.000 | wie Kreditoren | mittel | wie oben |
| Sachkonten je Bucket | 50.000 | 110 Mandanten × Ø 500 Konten = 55.000 (Annahme) | **hoch** | Mengengerüst je Mandant erheben (OP-21); Sachkonten ohne Mandantenbezug für alle Mandanten gültig anlegen, wenn der Kontenrahmen einheitlich ist (smart invoice erlaubt das) – ob LDconnect das unterstützt, ist offen (OP-22); nur bebuchte Konten übertragen; Erhöhung vereinbaren; mehrere Buckets nur als letzte Option (siehe Zeile Buckets) |
| Kostenstellen je Bucket | 50.000 | abhängig von KOST-Struktur (Haus-/Objektebene) | mittel | wie Sachkonten |
| Workflowdefinitionen | 100, je max. 50 Schritte | 4 (WF-01 bis WF-04) + Varianten | gering | Gesellschaftslogik nur über Matrix und Bedingungen (P6) |
| Buckets | max. 50 | 1 | gering | mehrere Buckets (z. B. je Segment) nur als letzte Option, falls die Maßnahmen bei Kreditoren und Sachkonten nicht reichen: Synchronisation mehrerer Buckets mit dem document reader ist ein Vorschau-Feature und erfordert zusätzliche Workflowdefinitionen; Entscheidung mit LIONDEER und d.velop (OP-04) |
| Repositories | max. 50 | 1 | gering | – |
| Gruppen | max. 2.500 | ~100–150 Gesellschaftsgruppen + Rollen-, Verbund-, smart-invoice-Gruppen | gering bis mittel | Gruppenzahl im Monitoring; flaches Gruppenmodell |
| Dynamische Wertemengen | max. 100 Vorschläge je Wertemenge | >100 Mandanten, viele Objekte | mittel | Mandant und Objekt als per API gepflegte Datasets; Bedienbarkeit mit >100 Werten im Test-Tenant testen (OP-40, Test T19) |
| Rechnungen | max. 5.000/Tag | 20–30/Tag | gering | – |

Quellen: d.velop invoices Leistungsbeschreibung 12/2025 (Service-Limits); d.velop documents Funktionsbeschreibung 11/2025 (Wertemengen).

MDIS überwacht die Limits im Betrieb (R-15). Grundlage ist ein monatlicher Zähllauf von BeSync über die smart-invoice-Stammdaten und die Gruppen [A]. Die Kennzahlen gehen in das Betriebsreporting (Kapitel 18).

## 6.7 Trennungsmechanismen

Die Gesellschaften sind durch mehrere, voneinander unabhängige Mechanismen getrennt.

| Ebene | Mechanismus | Wirkung | Status |
|---|---|---|---|
| DMS-Dokumente und Akten | Berechtigung je Kategorie und Rechtestufe; Eigenschaft Mandant gegen Restriction Set `RS_Mandant` (Gruppe → Mandanten-IDs) | Benutzer sehen und bearbeiten nur Dokumente ihrer Gesellschaften | [K]; Wirkung über alle Gruppen eines Benutzers testen (OP-08) |
| Objektbezug | Eigenschaft Objekt-ID gegen `RS_Objekt` | Projektleiter sehen nur ihr Objekt | [K] |
| Workflowbeteiligte | Leserecht über `WorkflowbeteiligteIDs` (E-32) | Prüfer und Freigeber sehen die ihnen zugewiesenen Rechnungen, auch gesellschaftsübergreifend (bewusste Ausnahme) | [S] |
| Rechnungseingangsbuch | Workflowberechtigung je Gruppe und Mandantennummer; „Globale Rechnungsliste" nur für zentrale Rollen | Übersicht nur über berechtigte Gesellschaften | [K] |
| Clearing | Clearing-Berechtigung je Mandant und Gruppe | Klärfälle einer Gesellschaft nur für deren Klärgruppe | [K] |
| Freigabe | Freigabematrix mit Spalte Mandant; Bearbeiterfindung über `voucher.company.nr` (z. B. Gruppe `SI_Freigeber_<MandantNr>`) | Freigaben nur durch die zuständigen Personen der Gesellschaft | [K]; eine Regel für alle Gesellschaften im Test-Tenant testen (OP-08) |
| Stammdaten | Kreditoren, Sachkonten, KOST je Mandant im Bucket | Kontierung nur mit Stammdaten der richtigen Gesellschaft | [S] |
| DATEV | LDconnect übergibt je Mandant in den zugehörigen DATEV-Bestand | Buchung im richtigen Bestand | [K] |
| Export | Export je Gesellschaft über Mandant (AE-25) | vollständige Herauslösung einer Gesellschaft | [A] |

Leere Werte sind ein Risiko: Ein Dokument ohne Mandant ist entweder für niemanden oder für alle sichtbar (Test im Test-Tenant, OP-08). Deshalb ist E-01 in allen Kategorien Pflicht, und Restriction-Set-Zuordnungen mit leerer Werteliste sind verboten, denn eine leere Liste erlaubt alle Werte (DmsConfig API). BeSync prüft das bei jeder Pflege [A].

## 6.8 Mandantenerkennung (AE-23)

smart invoice erkennt den Rechnungsempfänger über **Name und Anschrift** des Mandanten. USt-IdNr., Steuernummer und Kundennummer sind keine Erkennungsmerkmale am Mandanten (smart-invoice-API; smart invoice Cloud Handbuch 06/2026). Mehrere Livos-Gesellschaften teilen sich vermutlich dieselbe Verwaltungsanschrift. Katalog 2.2 ist deshalb **K mit Vorbehalt**.

| Nr. | Maßnahme | Wirkung | Verantwortlich | Status |
|---|---|---|---|---|
| 1 | Lieferantenanschreiben: exakte Gesellschaftsbezeichnung, Rechnungsadresse (Alias) und bei E-Rechnungen die Käuferreferenz (BT-10) je Gesellschaft | bessere Erkennung, strukturierte Zuordnung bei E-Rechnungen | Livos | [K] |
| 2 | Alias-Postfach je Gesellschaft mit eigenem Importprofil und Vorbelegung des Mandanten | eindeutige Zuordnung bei korrekt adressierten Rechnungen | Livos IT, MDIS | [S]; Vorbelegung testen (OP-02) |
| 3 | Mandantenname in smart invoice exakt wie auf den Rechnungen, einheitliche Schreibweise (Umlaute) | höhere Trefferquote | Fachadministration (Lieferanten-App) | [K] |
| 4 | Klärfall Mandant und Clearing je Mandant (WF-04) | kein Beleg geht verloren; unbekannte Gesellschaften werden bearbeitet (Katalog 2.3) | Rechnungseingang (R-02) | [K] |
| 5 | Test mit echten Livos-Belegen vor Go-live, inkl. Gesellschaften mit gleicher Anschrift; Trefferquote messen | belastbare Aussage zur Automatisierungsquote | Livos, MDIS | offen (OP-02) |

Die Details des Klärfalls beschreibt Kapitel 9.

## 6.9 Onboarding einer neuen Gesellschaft

Eine neue Gesellschaft erfordert keine neue Kategorie, keinen neuen Workflow und keine neue Berechtigung. Die Schritte sind überwiegend per API automatisierbar.

| Nr. | Schritt | System | Wer | Automatisierbar | Hinweis |
|---|---|---|---|---|---|
| 1 | Gesellschaft mit Mandanten-ID, Name, Anschrift, Segment, Verbund, Verwaltungsart anlegen | Lieferanten-App | Fachadministration (R-12) | – (fachliche Eingabe) | Vier-Augen-Freigabe empfohlen |
| 2 | DATEV-Bestand anlegen bzw. bestätigen | DATEV | Trios | nein | Voraussetzung für Buchung |
| 3 | Mandant in LDconnect-Konfiguration aufnehmen; Gateway-Freigabe des Bestands | LDconnect, Riecken-Gateway | Trios/DATEV-Betreiber, LIONDEER | nein | Kosten je weiterem Mandanten (OP-04) |
| 4 | smart-invoice-Mandant anlegen (ID, Name, Anschrift) | smart invoice | BeSync (S-04) | ja (Stammdaten-API) | – |
| 5 | Wert im Dataset Mandant ergänzen | d.velop documents | BeSync (S-04) | ja (DmsConfig API) | – |
| 6 | Gruppen `DMS_G_<MandantNr>` und `SI_<Rolle>_<MandantNr>` anlegen und Mitglieder zuordnen | Entra ID → SCIM | Livos IT | ja (Entra, SCIM) | flache Gruppen |
| 7 | Zuordnung im Restriction Set `RS_Mandant` (Gesellschafts- und Verbundgruppe) | d.velop documents | BeSync (S-04) | ja (DmsConfig API) | keine leere Werteliste |
| 8 | Freigabematrix-Zeilen für den Mandanten | smart invoice | BeSync | ja (Matrix-API) | Werte aus Verbunddefinition |
| 9 | Clearing-Berechtigung je Mandant | smart invoice Administration | Fachadministration | nicht dokumentiert → manuell | – |
| 10 | REB-Workflowberechtigung je Mandant | smart invoice Administration | Fachadministration | nicht dokumentiert → manuell | Test im Test-Tenant (Test T20) |
| 11 | Alias-Postfach und Importprofil mit Vorbelegung | M365, d.velop inbound | Livos IT, MDIS | teilweise | optional |
| 12 | Gesellschaftsakte (K-10) | d.velop documents | Aktenbildung | ja (automatisch beim ersten Dokument) | – |
| 13 | Lieferanten informieren (Rechnungsadresse, BT-10) | Livos | Kreditorenbuchhaltung | teilweise (Serienbrief) | Maßnahme 1 aus 6.8 |
| 14 | Kontrolle: Testbeleg durchläuft Erkennung, Workflow, Rechte | Test | R-02, MDIS | – | Abnahme der Gesellschaft |

Richtwert (Annahme): Die d.velop-seitigen Schritte 4 bis 8 laufen automatisch nach Freigabe in der Lieferanten-App. Die Dauer bestimmen die manuellen Schritte bei DATEV, Gateway und smart-invoice-Administration.

## 6.10 Offboarding und Verkauf einer Gesellschaft

Der Verkauf einer Gesellschaft ist in Kapitel 17 (Export je Gesellschaft, AE-25) beschrieben. Für das Mandantenmodell gelten folgende Regeln:

| Nr. | Schritt | Wirkung |
|---|---|---|
| 1 | Status der Gesellschaft in der Lieferanten-App auf „verkauft" setzen | Auslöser für alle Folgeschritte |
| 2 | Neue Rechnungseingänge für die Gesellschaft stoppen (Alias abschalten, Mandant für neue Belege sperren) | keine neuen Belege |
| 3 | Offene Workflows abschließen oder an den Käufer übergeben | keine offenen Belege im Export |
| 4 | Exportpaket erzeugen: Originale aller Versionen, Metadaten, Notizen, Verknüpfungen, Aktivitäten, Workflowprotokolle (S-15) | revisionssichere Weitergabe (Katalog 1.6) |
| 5 | Gesellschaftsübergreifende Dokumente (Mehrfachwert Mandant) gesondert prüfen | Schutz der Daten anderer Gesellschaften |
| 6 | Rechte der Gesellschaftsgruppe entziehen; Dokumente **sperren, nicht löschen** | Aufbewahrungspflicht beim Veräußerer bleibt zu klären (Kapitel 17) |
| 7 | Mandant in LDconnect und Freigabematrix deaktivieren | keine Übergaben mehr |

Voraussetzung ist P1: Nur wenn jede Akte und jedes Dokument den Mandanten trägt und keine Akte Dokumente mehrerer Gesellschaften als Ablageort enthält, lässt sich eine Gesellschaft vollständig herauslösen.

# 7 Informationsmodell

Das Informationsmodell beschreibt, wie Dokumente und Akten in d.velop documents strukturiert werden: Kategorien, Eigenschaften, Wertemengen, Aktenplan, Aufbewahrung und Namenskonventionen. Es verwendet durchgängig die Begriffe der d.velop Cloud: **Kategorie** mit Typ **Dokumentart** (D) oder **Aktenart** (A), **Eigenschaft**, **Wertemenge** (Dataset) und **Aktenbildungsregel** (Strukturregel).

## 7.1 Grundsätze

| Nr. | Grundsatz | Konsequenz | Beleg |
|---|---|---|---|
| G1 | **Beschriften statt Ordner.** Dokumente werden über Kategorie und Eigenschaften beschrieben. Akten entstehen automatisch aus diesen Eigenschaften. | Ein Dokument wird einmal gespeichert und in mehreren Akten angezeigt (Mehrfachablage). Suche, Rechte und Aufbewahrung arbeiten mit Eigenschaften, nicht mit Ablagepfaden. | d.velop documents Funktionsbeschreibung 11/2025; DmsConfig API |
| G2 | **Eine Eigenschaft je Fachbegriff.** Eigenschaftsnamen sind im Tenant eindeutig. | Keine Varianten wie „Kreditor (Livos)" neben „Kreditor", keine konkurrierenden Paare wie „Kostenstelle"/„Kostenstellen" oder „Gesellschaft"/„Mandant". | Demo-Befund (AE-29) |
| G3 | **Wiederverwendung der smart-invoice-Onboarding-Eigenschaften.** | Das Onboarding legt u. a. Mandant, Mandantenname, Kreditor, Kreditorname, Kostenstellen, Kostenträger, Sachkonten, Nettobetrag, Bruttobetrag, MwSt Betrag, Rechnungsnummer, Rechnungsdatum, Leistungsdatum, Belegart, Buchungstext, Workflowstatus und Workflowbeteiligte an. Diese Eigenschaften sind führend; Livos-spezifische Felder werden ergänzt. | smart invoice Cloud Handbuch 06/2026 |
| G4 | **Keine Übernahme der Demo-Struktur** (AE-29). | Die Kategorien „Livos …" und die Eigenschaften mit Zusatz „(Livos)" aus der Demo-Instanz werden nicht übernommen. Der Produktiv-Tenant wird neu aufgebaut. | As-built-Analyse der Demo-Instanz |
| G5 | **Kein Boolean-Datentyp.** Die Cloud kennt Text, Zahl, Währung, Datum und Datum-mit-Uhrzeit. | Ja/Nein-Felder als Text mit Wertemenge „Ja/Nein". | DmsConfig API |
| G6 | **Kein eigenes Statusfeld.** | Den Bearbeitungsstatus liefert smart invoice (Workflowstatus, E-24) bzw. das REB. Fachliche Zustände aus Umsystemen (Zahlstatus E-23, Freigabestatus BIM4You E-22) sind eigene, klar benannte Eigenschaften. | Demo-Befund; smart invoice |
| G7 | **Beträge als Währung, Anteile nicht im DMS.** | Kostenaufteilungen mit Prozent oder Betrag laufen in den smart-invoice-Belegpositionen, nicht in DMS-Eigenschaften. Ein Mehrfachfeld mit Zusatzwert gibt es nicht. | Demo-Befund |
| G8 | **Pflichtfelder schlank und automatisch befüllbar.** | Pflicht sind Felder, die Rechte, Aktenbildung oder Recht tragen. Eine Maske voller Pflichtfelder blockiert den Import. Bei Rechnungen (K-01) setzt der smart-invoice-Workflow die fachliche Pflicht durch (Kennzeichen „P(SI)" in 7.5). | Demo-Befund; Aktenbildung braucht gefüllte Erkennungsfelder |
| G9 | **Mandant überall** (P1). | E-01 ist in jeder Kategorie Pflicht, auch bei Akten, Post und Protokollen. | AE-03, AE-25 |
| G10 | **Namen kurz und ohne Sonderzeichen.** | Namen bis 50 Zeichen; keine Paragraphenzeichen oder Klammern (Kapitel 7.8). | Demo-Befund |

## 7.2 Kategorienkatalog

Aufbewahrungsfristen sind Vorschläge und werden mit der Steuerberatung festgelegt (AE-24, Kapitel 7.7). Phasen gemäß Kapitel 19.

| ID | Kategorie | Typ | Zweck | Pflichteigenschaften | Titelregel (Vorschlag) | Aufbewahrung (Vorschlag) | Phase |
|---|---|---|---|---|---|---|---|
| K-01 | Eingangsrechnung | D | Rechnungen, Gutschriften, Abschlags-, Schluss- und Stornorechnungen; Archivkategorie von smart invoice (Onboarding-Kategorie wiederverwenden) | E-01, E-25, E-29 (E-02, E-32 automatisch aus smart invoice); fachlich in smart invoice: E-05, E-08, E-09, E-10, E-11, E-14, E-15, E-16, E-17, E-20 | Kreditorname · Rechnungsnummer · Rechnungsdatum · Bruttobetrag | 8 Jahre ab E-29 | 1 |
| K-02 | Rechnungsanlage / Nachweis | D | Lieferschein, Aufmaß, Abnahmeprotokoll, Stundenzettel | E-01, E-03, E-27 (Dokumentdatum) | Kreditorname · Betreff · Dokumentdatum | 8 Jahre ab E-29 (als Teil des Buchungsbelegs) | 1 |
| K-03 | Auftrag / Bestellung | D | Auftrag, Auftragsbestätigung, Bestellung | E-01, E-03, E-19 (Auftragsnummer), E-27 (Dokumentdatum) | Kreditorname · Auftragsnummer | 6 Jahre ab E-29; bei Bauaufträgen zivilrechtliche Frist prüfen | 1 |
| K-04 | Angebot | D | Angebote, Angebotsvergleich | E-01, E-03, E-27 (Dokumentdatum) | Kreditorname · Betreff · Dokumentdatum | 6 Jahre ab E-29 | 1 |
| K-05 | Vertrag | D | Verträge, Nachträge, Kündigungen (verwaltet in d.velop contracts) | E-01, E-03, E-28 (Partner, Beginn) | Vertragspartner · Vertragsart · Vertragsnummer | ab Vertragsende, Dauer je Vertragsart (Kapitel 7.7) | 4 |
| K-06 | Bescheinigung | D | Freistellungsbescheinigung § 48b EStG, Unbedenklichkeitsbescheinigung, Versicherungsnachweise | E-01, E-05, E-21 (Gültig bis), E-27 (Dokumentdatum) | Kreditorname · Betreff · Gültig bis | 8 Jahre ab Ende der Gültigkeit | 1 (Automatik Phase 3) |
| K-07 | Korrespondenz | D | Briefe, E-Mails, Rückweisungs- und Kürzungsmitteilungen, PM-Freigabemails | E-01, E-27 (Dokumentdatum, Betreff) | Betreff · Dokumentdatum | 6 Jahre ab E-29 | 1 (automatische Ablage Phase 2) |
| K-08 | BIM4You-Prüfbericht | D | Prüf- und Zahlungsfreigabebericht, Einbehaltsnachweis aus BIM4You | E-01, E-03, E-05, E-19 | Objektbezeichnung · Auftragsnummer · Dokumentdatum | 8 Jahre ab E-29 | 3 |
| K-09 | Sonstiges Posteingangsdokument | D | Behörden, Steuer, Versicherung, Mieterpost; wird in Phase 4 feiner unterteilt | E-01, E-25, E-27 (Dokumentdatum, Absender) | Absender · Betreff · Dokumentdatum | 6 Jahre ab E-29; personenbezogene Unterlagen kürzer (Löschkonzept) | 4 |
| K-10 | Gesellschaftsakte | A | alle Dokumente einer Gesellschaft; oberste Ebene | E-01, E-02 | Mandantenname · Mandant | unbegrenzt; Löschung nur manuell, wenn leer | 1 |
| K-11 | Objektakte | A | Dokumente je Objekt bzw. Bauvorhaben | E-01, E-03, E-04 | Objektbezeichnung · Objekt-ID | unbegrenzt; Löschung nur manuell, wenn leer | 1 |
| K-12 | Kreditorenakte | A | Dokumente je Kreditor und Gesellschaft (inkl. FSB, Rahmenvertrag, Korrespondenz) | E-01, E-05, E-06 | Kreditorname · Kreditor-Nr · Mandant | unbegrenzt; Löschung nur manuell, wenn leer | 1 |
| K-13 | Vorgangsakte (Auftrag/Vergabeeinheit) | A | Auftrag, Abschläge, Schlussrechnung, Nachweise eines Vorgangs | E-01, E-03, E-19 | Objektbezeichnung · Auftragsnummer · Gewerk | unbegrenzt; Löschung nur manuell, wenn leer | 1 (Bau-Ausbau 3) |
| K-14 | Vertragsakte | A | Vertrag, Nachträge, Korrespondenz (Struktur von d.velop contracts) | E-01, E-28 | Vertragspartner · Vertragsnummer | gemäß d.velop contracts; unbegrenzt bis Löschlauf | 4 |
| K-15 | Organisationsunterlage | D | Verfahrensdokumentation, Arbeitsanweisungen, Stände von Workflowdefinitionen und Freigabematrix, Lösch-, Berechtigungs- und Rezertifizierungsprotokolle (Kapitel 13, 17, 18) | E-01, E-27 (Dokumentdatum, Betreff), E-29 | Betreff · Dokumentdatum | 10 Jahre ab E-29 | 1 |

Hinweise:

- **K-01** ist die Archivkategorie, die das smart-invoice-Onboarding anlegt. Sie wird umbenannt bzw. wiederverwendet, nicht dupliziert. Das Onboarding legt weitere Kategorien an, z. B. für Workflowprotokolle und die „Kreditorenvorgangsakte". Die Workflowprotokolle behalten die Onboarding-Kategorie und erhalten ebenfalls E-01 (Export je Gesellschaft). Die Onboarding-Kreditorenvorgangsakte wird durch K-12 ersetzt oder zu K-12 umgebaut; das wird im Test-Tenant entschieden [O].
- **K-05 und K-14** gehören zu d.velop contracts. contracts bringt eine eigene Struktur aus Vertragsakte und Vertragsdokumenten mit einer internen Vertrags-ID als verbindendem Element mit. Das Konzept ergänzt dort E-01 und E-03 (d.velop contracts Administrationshandbuch Cloud). Die genaue Abbildung legt Kapitel 12 fest.
- **PM-Freigaberechnungen (WF-03)** werden als K-01 mit Eingangskanal „PM-Freigabe" abgelegt. Sie sind bei Livos keine Buchungsbelege; ihre Aufbewahrungsfrist legt Livos mit der Steuerberatung fest (OP-46). Bis dahin gilt vorsorglich die Frist von K-01.
- **K-09** bleibt in Phase 1 bis 3 eine Sammelkategorie. In Phase 4 entscheidet der Postprozess (WF-07), ob weitere Kategorien nötig sind (z. B. Steuerbescheid, Behördenpost).
- **K-15 Organisationsunterlage** nimmt Verfahrensdokumentation und Organisationsunterlagen auf (10 Jahre, Kapitel 17.2 und 17.3). Gruppenweite Unterlagen tragen als Mandant die Gesellschaft, die das Verfahren verantwortet (Vorschlag: Obergesellschaft); gesellschaftsbezogene Protokolle den jeweiligen Mandanten.

## 7.3 Eigenschaftenkatalog

Typen: Text, Zahl, Währung, Datum. „Mehrfach" = Eigenschaft mit mehreren Werten. Einige IDs bündeln fachlich zusammengehörige Eigenschaften (z. B. E-11 = drei Betragsfelder); jede Teileigenschaft ist in d.velop eine eigene Eigenschaft. Die Spalte „Name in d.velop" nennt den vorgeschlagenen Eigenschaftsnamen; wo das smart-invoice-Onboarding bereits eine Eigenschaft anlegt, wird deren Name übernommen (Kennzeichen SI).

| ID | Eigenschaft | Name in d.velop | Typ | Einzel/Mehrfach | Wertemenge / Quelle | Pflicht in | Zweck |
|---|---|---|---|---|---|---|---|
| E-01 | Mandant (Mandanten-ID) | Mandant (SI) | Text | Einzel (Mehrfach nur in begründeten Ausnahmen, z. B. Konzern-Rahmenvertrag) | Dataset Mandanten, gepflegt durch BeSync (S-04); bei K-01 aus smart invoice | **alle** | Rechte, Akten, Workflow, DATEV, Export |
| E-02 | Mandantenname | Mandantenname (SI) | Text | Einzel | Gesellschaftsstamm; bei K-01 aus smart invoice; sonst Vererbung aus K-10 | K-10 | Anzeige, Titel |
| E-03 | Objekt-ID | Objekt-ID | Text | Einzel | Dataset Objekte (global eindeutig), gepflegt durch BeSync (S-04) | K-01 (wenn objektbezogen, in smart invoice), K-02–K-05, K-08, K-11, K-13 | Objektakte, Rechte Projektleiter |
| E-04 | Objektbezeichnung | Objektbezeichnung | Text | Einzel | Objektstamm; Vererbung aus K-11 | K-11 | Anzeige |
| E-05 | Kreditor-Nr (DATEV) | Kreditor (SI) | Text | Einzel | smart-invoice-Bucket (DATEV über LDconnect); für Nicht-Rechnungen Auswahl über BeSync-Wertemenge | K-01 (in smart invoice), K-06, K-08, K-12 | Kreditorenakte, Buchung |
| E-06 | Kreditorname | Kreditorname (SI) | Text | Einzel | Bucket; Vererbung aus K-12 | K-12 | Anzeige, Titel |
| E-07 | Lieferanten-Konsolidierungsnummer | Lieferant konsolidiert | Text | Einzel | Lieferanten-App (BeSync); an K-12 gesetzt und an Dokumente vererbt | – | gesellschaftsübergreifende Lieferantensicht |
| E-08 | Rechnungsnummer | Rechnungsnummer (SI) | Text | Einzel | Erkennung | K-01 (in smart invoice) | Dublettenprüfung, Suche |
| E-09 | Rechnungsdatum | Rechnungsdatum (SI) | Datum | Einzel | Erkennung | K-01 (in smart invoice) | Pflichtangabe § 14 UStG, Basis E-29 |
| E-10 | Leistungsdatum/-zeitraum | Leistungsdatum (SI); Leistungszeitraum | Datum; Text | Einzel | Erkennung | K-01 (in smart invoice) | Pflichtangabe § 14 UStG |
| E-11 | Nettobetrag / Steuerbetrag / Bruttobetrag | Nettobetrag (SI); MwSt Betrag (SI); Bruttobetrag (SI) | Währung | Einzel | Erkennung | K-01 (in smart invoice) | rechnerische Prüfung, Wertgrenzen |
| E-12 | Zahlbetrag | Zahlbetrag | Währung | Einzel | smart invoice (`pay_amount`), Mapping ins DMS | K-01 | Kürzung, Einbehalt |
| E-13 | Kürzungsgrund | Kürzungsgrund | Text | Mehrfach | Wertemenge Kürzungsgründe | K-01, wenn Zahlbetrag ≠ Bruttobetrag (in smart invoice) | Nachvollziehbarkeit |
| E-14 | Belegart | Belegart (SI) | Text | Einzel | Wertemenge Belegart | K-01 (in smart invoice) | Routing Bau, VOB, Gutschrift |
| E-15 | Fälligkeit netto / Skontofrist / Skontobetrag | Fälligkeit netto; Skontofrist; Skontobetrag | Datum; Datum; Währung | Einzel | Erkennung oder Zahlungsbedingung aus Stamm (Policy je Gesellschaft) | K-01 (Fälligkeit netto, in smart invoice) | Eskalation, Skonto-Ampel |
| E-16 | IBAN (Beleg) | IBAN | Text | Einzel | Erkennung; Abgleich mit Kreditor-Bankverbindung im Bucket | K-01 (in smart invoice, außer Lastschrift) | Betrugsprävention |
| E-17 | Kostenstelle(n) / Sachkonto / KOST2 | Kostenstellen (SI); Sachkonten (SI); Kostenträger (SI) | Text | Mehrfach | Bucket (DATEV KOST1, Sachkonten, KOST2); Aufteilung in smart-invoice-Positionen | K-01 (Positionen, in smart invoice) | Kontierung, Suche |
| E-18 | Gewerk / Vergabeeinheit (Los) | Gewerk; Vergabeeinheit | Text | Einzel | BIM4You-Stamm (Custom Entity in smart invoice, S-10); im DMS Wertemenge aus BeSync | K-01 Bau, K-03, K-13 | BIM4You-Zuordnung |
| E-19 | Auftragsnummer / Vertragsnummer | Auftragsnummer; Vertragsnummer | Text | Einzel | Erkennung; BIM4You-/Vertragsstamm | K-03, K-08, K-13 (K-01 bei Bau) | Vorgangsakte, VOB-Kumulation |
| E-20 | Reverse Charge § 13b | Reverse Charge 13b | Text | Einzel | Wertemenge Ja/Nein | K-01 (in smart invoice) | Steuerschlüssel |
| E-21 | FSB gültig bis / FSB-Status | Gültig bis; FSB-Status | Datum; Text | Einzel | Bescheinigung (K-06); FSB-Status aus BeSync (AE-15) | K-06 (Gültig bis) / K-01 Bau (FSB-Status) | § 48b EStG |
| E-22 | Sicherheitseinbehalt / geprüfter Betrag BIM4You / Freigabestatus BIM4You | Sicherheitseinbehalt; Geprüfter Betrag BIM4You; Freigabestatus BIM4You | Währung; Währung; Text | Einzel | BeSync (S-09) | K-01 Bau (nach BIM4You-Schritt) | Transparenz Bau |
| E-23 | Zahlstatus / Zahldatum | Zahlstatus; Zahldatum | Text; Datum | Einzel | BeSync aus DATEV-OPOS (S-06) | – | Status „bezahlt" |
| E-24 | Workflowstatus / aktueller Schritt | Workflowstatus (SI) | Text | Einzel | smart invoice | – | Status (kein eigenes Statusfeld) |
| E-25 | Eingangskanal | Eingangskanal | Text | Einzel | Wertemenge Eingangskanal; vorbelegt über Importprofil | K-01, K-09 | Auswertung |
| E-26 | Rückweisungsgrund | Rückweisungsgrund | Text | Einzel | Wertemenge Rückweisungsgründe (in smart invoice als Custom Entity) | K-01 bei Ablehnung (in smart invoice) | Lieferantenmail, Auswertung |
| E-27 | Dokumentdatum / Betreff / Absender | Dokumentdatum; Betreff; Absender | Datum; Text; Text | Einzel | Erkennung, KI-Klassifizierung oder manuell | K-02–K-09 (Dokumentdatum); Betreff bei K-07; Absender bei K-09 | Suche, Titel |
| E-28 | Vertragsdaten (Partner, Beginn, Ende, Kündigungsfrist, Verlängerung, Vertragswert) | gemäß d.velop contracts | div. | Einzel | d.velop contracts | K-05, K-14 | Fristen |
| E-29 | Aufbewahrungsbeginn | Aufbewahrungsbeginn | Datum | Einzel | berechnet: 31.12. des Belegjahres (bzw. Vertragsende, Ende Gültigkeit), gesetzt beim Import per Webhook/BeSync [A] | alle aufbewahrungspflichtigen Dokumentarten | Basis der Aufbewahrungsfrist |
| E-30 | Verwaltungsart / Property Manager | Verwaltungsart; Property Manager | Text | Einzel | Objektstamm (BeSync) | K-01 (WF-03), K-11 | PM-Prozess |
| E-31 | Segment | Segment | Text | Einzel | Wertemenge Segment; aus Gesellschaftsstamm | – | Auswertung, Matrix |
| E-32 | Workflowbeteiligte (IDs) | Workflowbeteiligte (SI); WorkflowbeteiligteIDs (SI) | Text | Mehrfach | smart invoice | K-01 (automatisch) | Leserecht der Beteiligten |

Hinweise zum Katalog:

- **Pflicht „in smart invoice"**: Diese Felder sind fachlich Pflicht. Die Pflicht setzt der smart-invoice-Workflow in den Masken M-02 bis M-04 durch. Im DMS werden sie nicht als Pflichtfelder der Kategorie K-01 gesetzt, damit die Archivierung aus smart invoice nicht an einem leeren Feld scheitert [A, im Test-Tenant zu prüfen].
- **E-05 Kreditor-Nr** ist nur zusammen mit E-01 eindeutig, weil die Kreditorennummern je DATEV-Mandant vergeben werden. Deshalb enthält jede Aktenbildung über den Kreditor auch den Mandanten.
- **E-12 Zahlbetrag** und **E-13 Kürzungsgrund**: Ob smart invoice den Zahlbetrag über die Standardzuordnung ins DMS schreibt, ist zu prüfen (OP-10). Andernfalls setzt BeSync die Werte beim Abschluss des Workflows [A].
- **E-14 Belegart**: Die Werte Abschlags- und Schlussrechnung unterscheidet smart invoice ggf. nicht im Standard-Belegtyp. Dann wird die Belegart als Kopffeld (Custom Entity) in smart invoice geführt und ins DMS gemappt [O, Test].
- **E-17**: Die Kontierung mit Anteilen bleibt in den smart-invoice-Positionen (G7). Im DMS stehen die verwendeten Werte als Mehrfachwerte zur Suche.
- **E-22 und E-23** werden am **archivierten Dokument** gesetzt, nicht im laufenden smart-invoice-Beleg (Kapitel 5.4).
- Die Eigenschaften Buchungstext, Steuersatz und Kostenträger aus dem Onboarding bleiben bestehen und werden ohne eigene ID geführt, sofern Livos sie nutzt.

## 7.4 Wertemengen

d.velop unterscheidet statische Wertemengen (Dataset mit festen Werten, per Oberfläche oder API pflegbar) und dynamische Wertemengen (Werte zur Laufzeit aus einer Quelle, z. B. per Webhook von BeSync oder aus business objects). Dynamische Vorschlagswerte sind auf **100 Einträge je Wertemenge** begrenzt (d.velop documents Funktionsbeschreibung 11/2025). Große Listen werden deshalb als per API gepflegte Datasets oder über die smart-invoice-Stammdaten geführt.

| Wertemenge | Art | Werte (Vorschlag, von Livos zu bestätigen) | Genutzt von | Pflege |
|---|---|---|---|---|
| **Mandanten** | Dataset, per API gepflegt | Mandanten-IDs aller Gesellschaften | E-01 | BeSync aus Gesellschaftsstamm (S-04) |
| **Objekte** | Dataset, per API gepflegt | Objekt-IDs | E-03 | BeSync aus Objektstamm (S-04) |
| **Kreditoren** (für Nicht-Rechnungen) | dynamisch über BeSync-Webhook, abhängig vom gewählten Mandanten [A] | Kreditor-Nr je Mandant | E-05 in K-02 bis K-08 | BeSync aus Bucket/DATEV-Stamm |
| **Gewerk / Vergabeeinheit** | Custom Entity in smart invoice; im DMS dynamisch über BeSync [A] | aus BIM4You | E-18 | BeSync (S-10) |
| **Belegart** | statisch | Rechnung · Gutschrift · Abschlagsrechnung · Schlussrechnung · Stornorechnung | E-14 | Fachadministration |
| **Ja/Nein** | statisch | Ja · Nein | E-20 und weitere Ja/Nein-Felder | fest |
| **Rückweisungsgründe** | statisch; in smart invoice als Custom Entity | (1) Pflichtangaben § 14 UStG fehlen/fehlerhaft · (2) falscher Rechnungsempfänger/Gesellschaft · (3) Leistung nicht/nicht vollständig erbracht bzw. Nachweise fehlen · (4) Preis/Menge weicht von Auftrag/Vertrag ab · (5) formaler E-Rechnungsfehler/Format nicht verarbeitbar | E-26 | Fachadministration |
| **Kürzungsgründe** | statisch; in smart invoice als Custom Entity oder Werteliste | Mengenabweichung · Preisabweichung · Mangel/Minderung · Einbehalt (Sicherheit/Gewährleistung) · Bauabzug 15 % (§ 48) · Skonto-/Nachlassdifferenz · Sonstiges (Freitext Pflicht) | E-13 | Fachadministration |
| **Segment** | statisch | Bestand · Privatisierung · Bau | E-31 | Fachadministration |
| **Verwaltungsart** | statisch | Eigenverwaltet · PM-verwaltet | E-30 | Fachadministration |
| **Property Manager** | Dataset, per API gepflegt | Namen der ~10 PM | E-30 | BeSync aus Objektstamm |
| **Eingangskanal** | statisch | E-Mail · Scan · E-Rechnung · Upload · PM-Freigabe | E-25 | fest; Vorbelegung über Importprofil |
| **Zahlstatus** | statisch | offen · teilbezahlt · bezahlt | E-23 | fest; gesetzt durch BeSync |
| **FSB-Status** | statisch | gültig · abgelaufen · fehlt · nicht erforderlich | E-21 | fest; gesetzt durch BeSync |
| **Freigabestatus BIM4You** | statisch | in Prüfung · freigegeben · teilweise freigegeben · abgelehnt · storniert | E-22 | fest; Werte mit BIB GmbH abstimmen (OP-06) |

Nicht als DMS-Wertemengen geführt werden Kreditoren für Rechnungen, Sachkonten, Kostenstellen und KOST2. Sie kommen aus den smart-invoice-Stammdaten, die LDconnect täglich aus DATEV füllt (Kapitel 8). Statische Kopien würden veralten.

## 7.5 Zuordnungsmatrix Kategorie × Eigenschaft

Legende: **P** = Pflicht in der Kategorie · **P(SI)** = fachliche Pflicht, durchgesetzt im smart-invoice-Workflow · **B** = bedingt Pflicht (Bedingung in Kapitel 7.3) · **o** = optional · **V** = wird per Vererbung oder System gesetzt · leer = nicht zugeordnet.

| Eigenschaft | K-01 | K-02 | K-03 | K-04 | K-05 | K-06 | K-07 | K-08 | K-09 | K-10 | K-11 | K-12 | K-13 | K-14 | K-15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E-01 Mandant | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P |
| E-02 Mandantenname | V | V | V | V | V | V | V | V | V | P | V | V | V | V | V |
| E-03 Objekt-ID | B | P | P | P | P | | o | P | o | | P | | P | o | |
| E-04 Objektbezeichnung | V | V | V | V | V | | V | V | | | P | | V | V | |
| E-05 Kreditor-Nr | P(SI) | o | o | o | o | P | o | P | | | | P | o | o | |
| E-06 Kreditorname | V | V | V | V | V | V | V | V | | | | P | | | |
| E-07 Konsolidierungsnummer | V | V | V | V | | V | V | | | | | V | | | |
| E-08 Rechnungsnummer | P(SI) | o | | | | | | o | | | | | | | |
| E-09 Rechnungsdatum | P(SI) | | | | | | | | | | | | | | |
| E-10 Leistungsdatum/-zeitraum | P(SI) | | | | | | | | | | | | | | |
| E-11 Beträge | P(SI) | | o | o | | | | o | | | | | | | |
| E-12 Zahlbetrag | P(SI) | | | | | | | o | | | | | | | |
| E-13 Kürzungsgrund | B | | | | | | | | | | | | | | |
| E-14 Belegart | P(SI) | | | | | | | | | | | | | | |
| E-15 Fälligkeit/Skonto | P(SI) | | | | | | | | | | | | | | |
| E-16 IBAN | P(SI) | | | | | | | | | | | | | | |
| E-17 Kostenstellen/Sachkonto/KOST2 | P(SI) | | | | | | | | | | | | | | |
| E-18 Gewerk/Vergabeeinheit | B | o | P | o | | | | o | | | | | P | | |
| E-19 Auftrags-/Vertragsnummer | B | o | P | o | o | | o | P | | | | | P | o | |
| E-20 Reverse Charge 13b | P(SI) | | | | | | | | | | | | | | |
| E-21 FSB gültig bis/Status | B | | | | | P | | | | | | o | | | |
| E-22 Einbehalt/BIM4You | B | | | | | | | o | | | | | | | |
| E-23 Zahlstatus/Zahldatum | V | | | | | | | | | | | | | | |
| E-24 Workflowstatus | V | | | | | | | | | | | | | | |
| E-25 Eingangskanal | P | o | o | o | | | o | | P | | | | | | |
| E-26 Rückweisungsgrund | B | | | | | | | | | | | | | | |
| E-27 Dokumentdatum/Betreff/Absender | | P | P | P | o | P | P | P | P | | | | | | P |
| E-28 Vertragsdaten | | | | | P | | | | | | | | | P | |
| E-29 Aufbewahrungsbeginn | P | P | P | P | P | P | P | P | P | | | | | | P |
| E-30 Verwaltungsart/PM | B | | | | | | | | | | P | | | | |
| E-31 Segment | V | V | V | V | V | V | V | V | V | V | V | V | V | V | V |
| E-32 Workflowbeteiligte | V | | | | | | | | | | | | | | |

Bedingungen: E-03 bei K-01 Pflicht, wenn die Rechnung objektbezogen ist. E-13 Pflicht, wenn Zahlbetrag ≠ Bruttobetrag. E-18, E-19, E-21 (FSB-Status), E-22 Pflicht bei Bau-Rechnungen (WF-02). E-26 Pflicht bei Ablehnung. E-30 Pflicht in WF-03. E-29 wird automatisch gesetzt; die Pflicht sichert, dass kein Dokument ohne Fristbeginn archiviert wird. E-31 wird aus dem Gesellschaftsstamm vererbt oder von BeSync gesetzt [A].

## 7.6 Aktenplan

### 7.6.1 Hierarchie

Der Aktenplan hat höchstens vier Ebenen (AE-19). Akten sind **Sichten**; ein Dokument wird einmal gespeichert und über Aktenbildungsregeln in mehreren Akten angezeigt.

```
Ebene 1   Gesellschaftsakte (K-10)                 [Mandant]
Ebene 2    ├─ Objektakte (K-11)                    [Mandant + Objekt-ID]
Ebene 3    │    ├─ Vorgangsakte (K-13)             [Mandant + Objekt-ID + Auftragsnummer]
Ebene 4    │    │     └─ Dokumente: K-01, K-02, K-03, K-08
Ebene 3    │    ├─ Vertragsakte (K-14)             [Vertrags-ID aus d.velop contracts]
Ebene 4    │    │     └─ Dokumente: K-05, K-07
Ebene 3    │    └─ Dokumente direkt: K-01, K-02, K-04, K-07
Ebene 2    ├─ Kreditorenakte (K-12)                [Mandant + Kreditor-Nr]
Ebene 3    │     └─ Dokumente: K-01, K-02, K-03, K-04, K-06, K-07, K-08
Ebene 2    └─ Dokumente direkt: K-07, K-09 (Gesellschaftspost), K-15

Zusatzsicht (keine Akte): gespeicherte Suche „Lieferant" über E-07 Konsolidierungsnummer
```

Livos liefert die fachliche Ordnerstruktur im Prozess-Workshop (OP-17). Die hier gezeigte Struktur ist der Vorschlag von MDIS.

### 7.6.2 Aktenbildungsregeln

Die Regeln S1 bis S6 bilden den Kern. S7 bis S10 ergänzen sie für Vorgangsakten und Gesellschaftspost [A]. Die Bezeichnung „S" steht hier für Strukturregel und ist nicht mit den Schnittstellen S-01 bis S-17 zu verwechseln.

| Regel | Übergeordnet → untergeordnet | Erkennungseigenschaften | Vererbung (von oben nach unten) | Status |
|---|---|---|---|---|
| S1 | K-10 Gesellschaftsakte → K-12 Kreditorenakte | E-01 | E-02, E-31 | [K] |
| S2 | K-10 Gesellschaftsakte → K-11 Objektakte | E-01 | E-02, E-31 | [K] |
| S3 | K-12 Kreditorenakte → K-01 Eingangsrechnung | E-01 + E-05 | E-06, E-07 | [K] |
| S4 | K-11 Objektakte → K-01 Eingangsrechnung | E-01 + E-03 | E-04, E-30 | [K]; zweite Regel für dieselbe Dokumentart, Mehrfachablage testen (OP-08) |
| S5 | K-11 Objektakte → K-14 Vertragsakte → K-05 Vertrag | E-01 + E-03 bzw. Vertrags-ID (contracts) | E-04; Vertragsdaten (E-28) von K-14 an K-05 | [K]; Muster d.velop contracts |
| S6 | K-12 Kreditorenakte → K-06 Bescheinigung | E-01 + E-05 | E-06, E-07 | [K] |
| S7 | K-11 Objektakte → K-13 Vorgangsakte | E-01 + E-03 | E-04 | [K] (Ergänzung) |
| S8 | K-13 Vorgangsakte → K-01, K-02, K-03, K-08 | E-01 + E-03 + E-19 | E-18 | [K] (Ergänzung); nur wenn E-19 gefüllt |
| S9 | K-12 Kreditorenakte → K-02, K-03, K-04, K-07, K-08 | E-01 + E-05 | E-06, E-07 | [K] (Ergänzung) |
| S10 | K-10 Gesellschaftsakte → K-07, K-09, K-15 | E-01 | E-02 | [K] (Ergänzung) |

Regeln für die Aktenbildung:

1. **E-01 Mandant ist Teil jeder Erkennungskombination.** Kreditor- und Objektnummern können sich zwischen Gesellschaften überschneiden.
2. **Erkennungseigenschaften müssen gefüllt sein.** Bei leeren Erkennungsfeldern wird keine Aktenverknüpfung erzeugt (belegtes Verhalten On-Premises; Cloud-Verhalten im Test-Tenant prüfen, OP-08). Deshalb sind die Erkennungsfelder Pflicht oder werden automatisch gesetzt.
3. **Akten nie gesellschaftsübergreifend als Ablageort.** Die gesellschaftsübergreifende Lieferantensicht entsteht über eine gespeicherte Suche nach E-07, nicht über eine eigene Akte (Export je Gesellschaft, P1).
4. **Konsolidierungsnummer über Vererbung:** BeSync setzt E-07 an der Kreditorenakte (K-12). Die Regeln S3, S6 und S9 vererben den Wert an alle Dokumente der Akte [A]. So braucht der einzelne Beleg keinen eigenen Abgleich.
5. **Akten sind eigene Kategorien** und erhalten eigene Berechtigungen nach demselben Muster wie Dokumente (Kapitel 13).
6. Die Option „bei Änderung neu zuordnen" wird aktiviert, damit korrigierte Eigenschaften (z. B. nach Klärfall) die Akte wechseln.
7. Eine Akte zeigt standardmäßig die ersten 100 Elemente (umstellbar). Für große Kreditorenakten sind Filter und gespeicherte Suchen vorzusehen.

### 7.6.3 Beispiel (fiktiv)

Die folgenden Werte stammen aus den fiktiven Demo-Testdaten und dienen nur der Veranschaulichung.

| Element | Werte |
|---|---|
| Gesellschaft | Livos Objektgesellschaft Nord mbH, Mandanten-ID `10010` (Beispiel) |
| Objekt | BV Hafenstraße 22, Objekt-ID `10010-0001` (Beispiel für global eindeutige ID mit Gesellschaftspräfix) |
| Kreditor | Musterbau GmbH, Kreditor-Nr `70012` im Mandanten 10010, Konsolidierungsnummer `L-000123` (Beispiel) |
| Vorgang | Auftrag `A-2026-0815` (Beispiel), Gewerk Rohbau, Los 3 |
| Rechnung | RE-2026-1041 vom 12.09.2026, 14.756,00 € brutto |

Ablage der Rechnung RE-2026-1041 (ein Dokument, drei Fundorte):

```
Gesellschaftsakte „Livos Objektgesellschaft Nord mbH" (10010)
 ├─ Kreditorenakte „Musterbau GmbH · 70012"                 ← RE-2026-1041 (Regel S3)
 │     └─ Freistellungsbescheinigung, gültig bis 31.12.2026   (Regel S6)
 └─ Objektakte „BV Hafenstraße 22"                           ← RE-2026-1041 (Regel S4)
       └─ Vorgangsakte „A-2026-0815 · Rohbau Los 3"          ← RE-2026-1041 (Regel S8)
             ├─ Auftragsbestätigung A-2026-0815              (Regel S8)
             └─ Aufmaß zur RE-2026-1041                      (Regel S8)

Gespeicherte Suche „Lieferant L-000123": zeigt alle Dokumente der Musterbau GmbH
in allen Gesellschaften, für die der Benutzer berechtigt ist.
```

## 7.7 Aufbewahrung und Löschung je Kategorie

Die Aufbewahrung ist in der Cloud eine Einstellung der Kategorie: Frist in Jahren oder Monaten ab einer Datumseigenschaft, dazu eine Löschsperre für freigegebene und archivierte Dokumente (DmsConfig API). Änderungen an Frist und Löschsperre werden protokolliert (AE-24).

| Kategorie | Rechtsgrundlage (Vorschlag) | Frist | Beginn (`basedOn`) | Löschsperre | Automatisches Löschen |
|---|---|---|---|---|---|
| K-01 Eingangsrechnung (inkl. E-Rechnungs-XML) | Buchungsbeleg: § 147 Abs. 1 Nr. 4, Abs. 3 AO; § 257 HGB; § 14b UStG (BEG IV ab 2025) | 8 Jahre | E-29 (31.12. des Rechnungsjahres) | ja | aus |
| Workflowprotokolle smart invoice (Onboarding-Kategorie) | Teil des Buchungsbelegs / Nachweis der Freigabe | 8 Jahre | E-29 | ja | aus |
| K-02 Rechnungsanlage / Nachweis | als Bestandteil des Buchungsbelegs | 8 Jahre | E-29 | ja | aus |
| K-03 Auftrag / Bestellung | Handels- und Geschäftsbrief (§ 147 Abs. 1 Nr. 2, 3 AO); bei Bau zivilrechtlich länger | 6 Jahre (Bau: nach Vorgabe Recht) | E-29 | ja | aus |
| K-04 Angebot | Geschäftsbrief, wenn angenommen | 6 Jahre | E-29 | ja | aus |
| K-05 Vertrag | Buchungsgrundlage mind. 8 Jahre; zivilrechtlich je Vertragsart (Bau/Gewährleistung, Grundstück, Darlehen) | nach Festlegung Livos Recht | Vertragsende (E-28) | ja | aus |
| K-06 Bescheinigung | Nachweis zum Steuerabzug § 48 ff. EStG | 8 Jahre | Ende der Gültigkeit (E-21) | ja | aus |
| K-07 Korrespondenz | Handels- und Geschäftsbrief | 6 Jahre | E-29 | ja | aus |
| K-08 BIM4You-Prüfbericht | Bestandteil des Buchungsbelegs | 8 Jahre | E-29 | ja | aus |
| K-09 Sonstiges Posteingangsdokument | Geschäftsbrief bzw. sonstige Unterlage; personenbezogene Unterlagen nach Löschkonzept | 6 Jahre (Vorschlag) | E-29 | ja | aus |
| K-10 bis K-13 Akten | keine eigene Pflicht | unbegrenzt (0) | – | ja | aus; leere Akten im Löschlauf entfernen |
| K-14 Vertragsakte | wie K-05 | wie K-05 | Vertragsende | ja | aus |
| K-15 Organisationsunterlage | Bücher und Organisationsunterlagen: § 147 Abs. 1 Nr. 1, Abs. 3 AO; § 257 Abs. 1 Nr. 1 HGB | 10 Jahre | E-29 (31.12. des Jahres der letzten Änderung bzw. Ablage) | ja | aus |

Regeln:

1. **Fristbeginn über E-29:** Steuerliche Fristen beginnen mit Ablauf des Kalenderjahres. E-29 wird beim Import auf den 31.12. des Beleg- bzw. Dokumentjahres gesetzt [A]. Rückfallebene, falls die Berechnung nicht umsetzbar ist: Frist ab Rechnungs- bzw. Dokumentdatum um ein Jahr verlängern (z. B. 9 statt 8 Jahre); das hält die Mindestfrist sicher ein [A].
2. **Automatisches Löschen zunächst aus.** Die Aufbewahrungsfrist läuft nicht ab, solange die Festsetzungsfrist für die betroffenen Steuern offen ist (§ 147 Abs. 3 S. 5 AO). Deshalb gibt es einen **jährlichen, freigegebenen Löschlauf**: Kandidatenliste → Freigabe durch Steuer/Recht → Löschen → Protokoll (process studio, Kapitel 17).
3. **Legal Hold** ist in der Cloud nicht dokumentiert (OP-15). Ersatzweise wird E-29 bei Betriebsprüfung oder Rechtsstreit nach vorn gesetzt; die Änderung ist im Aktivitätenprotokoll nachvollziehbar [A, mit d.velop zu bestätigen].
4. **Löschrecht** haben nur Fachadministration und MDIS-Betrieb; die Löschsperre übersteuert alle Löschrechte.
5. Die endgültigen Fristen legt Livos mit der Steuerberatung fest. Zivilrechtliche Fristen für Verträge legt die Livos-Rechtsabteilung fest.

## 7.8 Namens- und Pflegekonventionen

### 7.8.1 Namen

| Objekt | Konvention | Beispiel |
|---|---|---|
| Kategorie | Fachbegriff im Singular, ohne Präfix „Livos" (eigener Tenant), max. 50 Zeichen | Eingangsrechnung, Kreditorenakte |
| Eigenschaft | Fachbegriff, einmal im Tenant; Onboarding-Namen von smart invoice übernehmen; keine Zusätze in Klammern; keine Sonderzeichen wie § oder & | Reverse Charge 13b, Zahlbetrag |
| Wertemenge | Name der Eigenschaft bzw. Fachliste | Belegart, Kürzungsgründe |
| Werte | ausgeschrieben, einheitliche Schreibweise (UTF-8, Umlaute) | Schlussrechnung |
| Rollengruppen DMS | `DMS_R_<Rolle>` | `DMS_R_Buchhaltung` |
| Gesellschaftsgruppen | `DMS_G_<MandantNr>` | `DMS_G_10010` (Beispiel) |
| Verbundgruppen | `DMS_GF_<Verbund>` | `DMS_GF_Nord` (Beispiel) |
| Objektgruppen | `DMS_O_<ObjektID>` | `DMS_O_10010-0001` (Beispiel) |
| smart-invoice-Gruppen | `dv_*` aus dem Onboarding; `SI_<Rolle>_<MandantNr>` | `SI_Freigeber_10010` |
| Restriction Sets | `RS_<Bezug>` | `RS_Mandant`, `RS_Objekt` |
| Berechtigungen | `<Kategorie> – <Geltungsbereich> – <Stufe>` | `Eingangsrechnung – Mandant – Lesen` |
| Postfächer | Funktion, Alias je Gesellschaft | `rechnung@…`, `freigabe-hv@…`, Alias je Gesellschaft (Format mit Livos IT) |
| Gespeicherte Suchen | `<Rolle> – <Inhalt>` | `Buchhaltung – offene Rechnungen Mandant` |

### 7.8.2 Änderungsprozess für die Struktur

Änderungen an Kategorien, Eigenschaften, Wertemengen, Aktenbildungsregeln, Aufbewahrung und Berechtigungen folgen einem festen Ablauf.

| Schritt | Inhalt | Verantwortlich |
|---|---|---|
| 1 | Änderungsantrag mit fachlicher Begründung, betroffenen Kategorien und Gesellschaften | Fachbereich, Key-User (R-12) |
| 2 | Bewertung: Auswirkung auf Rechte, Akten, smart-invoice-Zuordnung, Schnittstellen, Aufbewahrung | Fachadministration (R-12) mit MDIS (R-15) |
| 3 | Umsetzung und Test im Test-Tenant | MDIS |
| 4 | Abnahme | Fachadministration |
| 5 | Übernahme in den Produktiv-Tenant (Konfigurationspaket per API, sonst dokumentierte manuelle Schritte) | MDIS |
| 6 | Dokumentation im Änderungsprotokoll und in der Verfahrensdokumentation | MDIS, Fachadministration |

Feste Regeln:

- Datentyp und Einzel-/Mehrfachwert einer Eigenschaft werden nach Produktivstart nicht geändert. Bei Bedarf wird eine neue Eigenschaft angelegt und migriert.
- Eigenschaften und Kategorien werden nicht gelöscht, solange sie zugeordnet sind oder Dokumente tragen; sie werden stillgelegt.
- Umbenennungen werden vorab auf gespeicherte Suchen, smart-invoice-Zuordnungen und Schnittstellen geprüft.
- Wertemengen aus Stammdaten (Mandanten, Objekte, Property Manager) werden nur über die Lieferanten-App geändert, nie direkt in d.velop (P3, P4).
- Änderungen an Aufbewahrung und Löschsperre erfordern die Freigabe durch Finanzleitung bzw. Steuerberatung.

# 8 Stammdatenkonzept

Stammdaten entscheiden, ob Rechnungen automatisch erkannt, richtig kontiert, der richtigen Gesellschaft zugeordnet und korrekt an DATEV übergeben werden. Bei Livos kommen drei Besonderheiten zusammen: über 100 Gesellschaften mit eigenen DATEV-Beständen, dieselben Lieferanten mit unterschiedlichen Kreditorennummern je Gesellschaft und ein externer Buchhaltungsdienstleister (Trios), der die Kreditoren in DATEV anlegt. Dieses Kapitel legt fest, welches System welche Stammdaten führt, wie Lieferanten und Kreditoren verbunden werden und wie die Qualität der Stammdaten gesichert wird. Es setzt AE-09, AE-15 und AE-28 um.

Bezüge zu den Workshop-Anforderungen: T-02 (führendes System der Lieferantennummer), T-03 (keine Kreditoranlage durch Livos), T-04 (geringer Initialaufwand), T-05 (Schlüssel aus Mandanten- und Kreditorennummer), T-06 (bidirektionaler Abgleich), T-08 (Abgleich trotz externem Hosting), T-10 (konsolidierte Kreditorensicht), T-11 (Prozess für unbekannte Kreditoren), T-12 (automatische Zuordnung nach DATEV-Anlage), T-15/T-16 (Herkunft und Abgleich der IBAN), T-18 (Fälligkeit aus Rechnung oder Stamm).

## 8.1 Übersicht: führende Systeme je Stammdatenobjekt

| Stammdatenobjekt | Führendes System | Pflege durch | Verteilung an | Weg / Frequenz | Schnittstelle | Status |
|---|---|---|---|---|---|---|
| Gesellschaft (Mandant) | Lieferanten-App (BeSync) | Fachadministration Livos (R-12) | smart-invoice-Mandant, Dataset Mandant, Restriction Set, Gruppen | nächtlich und bei Änderung | S-04 | [A] |
| Objekt | Lieferanten-App (BeSync) | Fachadministration Livos | Dataset Objekt, Restriction Set `RS_Objekt`, Objektakte | nächtlich und bei Änderung | S-04 | [A] |
| Lieferant (gesellschaftsübergreifend, Konsolidierungsnummer) | Lieferanten-App (BeSync) | Fachadministration Livos | DMS-Eigenschaft E-07 an Kreditorenakte und Dokumenten | nächtlich und bei Änderung | S-04 | [A] |
| Kreditor je Mandant (DATEV-Kreditorennummer) | DATEV | Trios | smart-invoice-Bucket | täglich über LDconnect | S-02 | [K] |
| Mapping Lieferant ↔ Kreditor je Mandant ↔ HV-Kreditor | Lieferanten-App (BeSync) | Fachadministration Livos; Vorschläge per KI | BeSync-intern; E-07 | bei Änderung | S-05 | [A] |
| Sachkonto | DATEV | Trios | Bucket | täglich | S-02 | [K] |
| Kostenstelle (KOST1) / KOST2 | DATEV | Trios (Anlage auf Anforderung Livos Controlling) | Bucket | täglich | S-02 | [K] |
| Steuerschlüssel | DATEV (nur Vorsteuerschlüssel werden übertragen) | Trios | Bucket | täglich | S-02 | [K] |
| Zahlungsbedingung | DATEV | Trios | Bucket | täglich | S-02 | [K] |
| Bankverbindung des Kreditors (IBAN) | DATEV | Trios, mit Vier-Augen-Prüfung (8.6) | Bucket | täglich | S-02 | [K] |
| Projekt, Vergabeeinheit, Vertrag, Gewerk (Bau) | BIM4You | Bau-Projektsteuerung Livos | Bucket (Custom Entities), DMS-Wertemenge | nächtlich | S-10 | [A] |
| Freistellungsbescheinigung (FSB-Status) | Lieferanten-App / BeSync (FSB-Tabelle) | Kreditorenbuchhaltung Livos | Hinweis im Workflow, E-21 | bei Belegeingang und bei Änderung | S-04 | [A], Phase 3 |
| Benutzer und Gruppen | Microsoft Entra ID | Livos IT | d.velop usermanagement | laufend (SCIM) | S-13 | [S]/[K] |
| Freigabematrix | smart invoice | Fachadministration Livos; Zeilen aus Verbunddefinition per API | – | bei Änderung | S-04 (Zeilenpflege) | [K]/[A] |
| Rückweisungs- und Kürzungsgründe | smart invoice (Werteliste/Custom Entity) | Fachadministration Livos | DMS-Wertemenge | bei Änderung | – | [K] |

Grundregeln:

- **Livos legt keine Kreditoren in DATEV an** (T-03). DATEV bleibt führend für alle buchhalterischen Stammdaten (P4).
- **Kreditoren werden nicht in d.velop angelegt.** smart invoice nutzt ausschließlich die Kreditoren aus DATEV. So entstehen keine Kreditoren, die DATEV nicht kennt, und keine Doppelpflege.
- **Livos pflegt fachliche Stammdaten nur in der Lieferanten-App.** Technische Tabellen in BeSync pflegt MDIS (P3).

## 8.2 Lieferanten- und Kreditorenmodell (AE-09)

### 8.2.1 Drei Nummernkreise

Heute hat derselbe Lieferant in jeder Gesellschaft eine eigene Kreditorennummer. Interne Kreditoren liegen im 70000er-Kreis, Kreditoren aus den Buchhaltungen der Property Manager im 80000er-Kreis. Eine Konsolidierung gibt es nicht, auch nicht in DATEV (Workshop 22.09.2026). Das Konzept unterscheidet deshalb drei Nummern mit klarer Führung.

| Nr. | Nummer | Bedeutung | Führendes System | Eindeutig | Verwendung |
|---|---|---|---|---|---|
| 1 | **Lieferanten-Konsolidierungsnummer** | Identität des Lieferanten über alle Gesellschaften und Kreise | Lieferanten-App | in der ganzen Gruppe | gesellschaftsübergreifende Sicht (E-07), Auswertungen in evidanza, FSB-Status, Dublettenerkennung |
| 2 | **DATEV-Kreditorennummer je Mandant** (70000er) | Kreditorenkonto in der Buchhaltung der Gesellschaft | DATEV | je Mandant (Schlüssel „Mandanten-ID + Kreditorennummer") | Erkennung und Kontierung in smart invoice, Buchung, Kreditorenakte (E-05) |
| 3 | **HV-Kreditorennummer** (80000er) | Kreditorenkonto aus der Buchhaltung eines Property Managers | Buchhaltung des PM (über DATEV) | je Mandant und PM | Abgleich der PM-Buchungen, konsolidierte Sicht (T-10), PM-Freigabe (WF-03) |

Der Schlüssel für Nummer 2 und 3 ist die Kombination aus DATEV-Mandantennummer und Kreditorennummer (Vorschlag Trios, T-05). Die Lieferanten-App ordnet jedem dieser Schlüssel genau eine Konsolidierungsnummer zu. Eine Konsolidierungsnummer hat beliebig viele Kreditorennummern.

Das smart-invoice-Kreditorobjekt hat kein freies Feld für die Konsolidierungsnummer. Sie wird deshalb nicht in den Bucket geschrieben, sondern als DMS-Eigenschaft E-07 an der Kreditorenakte gesetzt und an die Dokumente vererbt (Kapitel 7.6) [A].

### 8.2.2 Beispiel-Mapping (fiktiv)

Alle Werte sind erfunden und dienen nur der Veranschaulichung.

| Konsolidierungsnr. | Lieferant (Name in der App) | USt-IdNr. | Mandant | Mandantenname | Kreditor-Nr | Kreis | Quelle | Status |
|---|---|---|---|---|---|---|---|---|
| L-000123 | Musterbau GmbH | DE201456789 | 10010 | Livos Objektgesellschaft Nord mbH | 70012 | intern | DATEV | bestätigt |
| L-000123 | Musterbau GmbH | DE201456789 | 10020 | Livos Objektgesellschaft Süd mbH | 70388 | intern | DATEV | bestätigt |
| L-000123 | Musterbau GmbH | DE201456789 | 10020 | Livos Objektgesellschaft Süd mbH | 80417 | HV | PM-Buchhaltung | KI-Vorschlag, offen |
| L-000124 | Elektro Nordlicht GmbH | DE202567890 | 10010 | Livos Objektgesellschaft Nord mbH | 70044 | intern | DATEV | bestätigt |
| L-000124 | Elektro Nordlicht GmbH | DE202567890 | 10030 | Livos Bau & Projekt GmbH | 70102 | intern | DATEV | bestätigt |
| L-000125 | Stadtwerke Beispielstadt AG | DE203678901 | 10020 | Livos Objektgesellschaft Süd mbH | 70103 | intern | DATEV | bestätigt |
| (neu) | Recht & Partner mbB | DE204789012 | 10030 | Livos Bau & Projekt GmbH | – | – | Klärfall „Kreditor fehlt" | Anlage angefordert |

### 8.2.3 Prozess „Neuanlage Kreditor"

Ausgangslage: Eine Rechnung kommt für eine Gesellschaft, in deren DATEV-Bestand der Lieferant noch kein Kreditorenkonto hat (T-11, T-12).

| Schritt | Tätigkeit | System | Rolle | Dauer (Richtwert, Vorschlag) |
|---|---|---|---|---|
| 1 | Erkennung findet keinen Kreditor im Mandanten; Beleg geht in den Klärfall „Kreditor fehlt" (WF-04, Maske M-05) | smart invoice | automatisch | Tag 0 |
| 2 | Prüfen: Gibt es den Lieferanten schon mit Konsolidierungsnummer (in anderer Gesellschaft)? Die Lieferanten-App schlägt Treffer vor (Name, Anschrift, USt-IdNr., IBAN, E-Mail) | Lieferanten-App (M-16) | Rechnungseingang (R-02) | Tag 0 |
| 3a | Treffer: Lieferant bestätigen | Lieferanten-App | R-02 | Tag 0 |
| 3b | Kein Treffer: neuen Lieferanten mit Konsolidierungsnummer anlegen (Stammdaten aus der Rechnung, Nachweise) | Lieferanten-App | R-02, Freigabe durch Fachadministration (R-12) bei neuer Bankverbindung | Tag 0 |
| 4 | Anlage-Anforderung „Kreditor für Mandant X" an Trios, mit Lieferantendaten und Bankverbindung | Lieferanten-App → Trios (Aufgabe oder E-Mail) | automatisch aus Schritt 3 | Tag 0 |
| 5 | Kreditor in DATEV anlegen, Bankverbindung im Vier-Augen-Prinzip prüfen (8.6) | DATEV | Trios (R-06) | Ziel: bis Tag 1 (Service-Level mit Trios vereinbaren) |
| 6 | Mapping: BeSync liest den neuen Kreditor über DATEVconnect und ordnet ihn der Konsolidierungsnummer zu (Schlüssel Mandant + Kreditorennummer, Abgleich USt-IdNr./IBAN) | BeSync (S-05) | automatisch; bei Unsicherheit Bestätigung durch R-02 | Tag 1 |
| 7 | Täglicher Stammdatenabgleich überträgt den Kreditor in den Bucket | LDconnect (S-02) | automatisch | Nacht auf Tag 2 (Folgetag nach DATEV-Anlage) |
| 8 | Beleg im Klärfall wird erneut geprüft; Kreditor wird zugeordnet; der Beleg läuft in die sachliche Prüfung | smart invoice | R-02 (Zuordnung bestätigen) | Tag 2 |

Durchlaufzeit: Die fachliche Prüfung des Belegs kann parallel beginnen. Die DATEV-Übergabe ist erst nach Schritt 7 möglich. Realistisch sind **ein bis drei Arbeitstage** vom Eingang bis zur Kreditorzuordnung, abhängig von der Reaktionszeit von Trios und dem täglichen Abgleich. Ob LDconnect einen Abgleich im Tagesverlauf oder auf Anforderung erlaubt, ist offen (OP-22). Bei Skonto-kritischen Belegen priorisiert R-02 die Anforderung.

Die im Workshop angesprochene Variante, einen Kreditor zunächst in d.velop anzulegen und später an DATEV zu übertragen, wird nicht empfohlen. Sie widerspricht P4 (DATEV führt die Kreditorenkonten) und würde ein zweites schreibendes System im Bucket erfordern (Kapitel 8.7).

### 8.2.4 Initiale Konsolidierung per KI-PoC

Für über 100 Gesellschaften ist die erste Zusammenführung der Kreditoren der größte Aufwand (T-04). MDIS bietet dafür einen Proof of Concept mit der KI-Plattform **X.One** an (Workshop 22.09.2026, AE-27).

| Schritt | Inhalt | Ergebnis |
|---|---|---|
| 1 | Export der Kreditorenstämme aller DATEV-Bestände (70000er und 80000er) inkl. Anschrift, USt-IdNr., Steuernummer, IBAN, E-Mail | Rohdatenbestand, Mengengerüst (auch für das Bucket-Limit, Kapitel 6.6) |
| 2 | KI-gestütztes Matching; Merkmale: USt-IdNr., IBAN, Straße/Hausnummer, E-Mail-Domain, Name (Name allein genügt nicht) | Vorschlagstabelle Konsolidierungsnummer ↔ Kreditorennummern mit Trefferwahrscheinlichkeit |
| 3 | Fachliche Prüfung unsicherer Treffer in der Lieferanten-App | bestätigtes Mapping |
| 4 | Übernahme als Anfangsbestand der Lieferanten-App; Setzen von E-07 an den Kreditorenakten | konsolidierte Sicht ab Pilot (einmaliger Import), laufend gepflegt ab Phase 2 (S-04) |
| 5 | Messung: Anteil automatisch bestätigter Treffer, Aufwand der Nacharbeit | Entscheidungsgrundlage für die laufende KI-Unterstützung |

Der Umfang des PoC (Datenmenge, Termin, Erfolgskriterien) wird vor Projektstart schriftlich festgelegt.

### 8.2.5 Pflegeverantwortung

| Objekt | Anlegen | Ändern | Prüfen/Freigeben | Löschen/Sperren |
|---|---|---|---|---|
| Lieferant (Konsolidierungsnummer) | R-02 (bei Klärfall), R-12 | R-12 | R-12 | R-12 (sperren, nicht löschen) |
| Mapping Kreditor ↔ Lieferant | BeSync (Vorschlag), R-02 | R-12 | R-02/R-12 bei Unsicherheit | R-12 |
| DATEV-Kreditor | Trios (R-06) | Trios | Trios (Vier-Augen bei Bankdaten) | Trios |
| HV-Kreditor | Property Manager | Property Manager | Mapping durch R-12 | – |
| FSB-Status | R-02 | R-02 | R-12 (Stichprobe) | – |
| Technische Tabellen BeSync | MDIS (R-15) | MDIS | MDIS | MDIS |

## 8.3 Gesellschafts- und Objektstamm (AE-28)

Der Gesellschaftsstamm ist in Kapitel 6.4 beschrieben. Der Objektstamm folgt demselben Muster.

| Feld Objektstamm | Pflicht | Beispiel (fiktiv) | Ziel in d.velop | Zweck |
|---|---|---|---|---|
| Objekt-ID (global eindeutig) | ja | 10010-0001 | Dataset Objekt (E-03), `RS_Objekt`, Gruppe `DMS_O_<ObjektID>` | Schlüssel Objektakte, Rechte |
| Objektbezeichnung | ja | BV Hafenstraße 22 | E-04, Titel der Objektakte | Anzeige, Erkennung auf Rechnungen |
| Mandant | ja | 10010 | E-01 der Objektakte | Zuordnung zur Gesellschaft |
| Adresse | ja | Hafenstraße 22, 20359 Hamburg | BeSync | Erkennung des Objekts auf Rechnungen [A] |
| Verwaltungsart | ja | Eigenverwaltet | E-30 | Routing WF-03 |
| Property Manager | bedingt | – | E-30 | PM-Rückmeldung |
| Bauprojekt ja/nein | ja | Ja | BeSync, Weiche WF-02 | Erkennung Bau-Rechnung |
| BIM4You-Projekt-ID | bedingt | P-2026-014 | BeSync, Mapping S-08/S-10 | BIM4You-Zuordnung |
| Kostenstelle(n) des Objekts | empfohlen | KOST1 der Hausebene | Kontierungsvorlage (8.4) | Vorbelegung der Kontierung |
| Status, gültig ab/bis | ja | aktiv | BeSync | Lebenszyklus (Verkauf von Objekten) |

Regeln:

- Die Objekt-ID ist über alle Gesellschaften eindeutig, z. B. mit Gesellschaftspräfix (Vorschlag). Wechselt ein Objekt die Gesellschaft, entsteht eine neue Objekt-ID; die alte wird gesperrt.
- Objekte mit mehreren Häusern (z. B. Haus A/Haus B) werden über Kostenstellen im DATEV-Stamm abgebildet, nicht über zusätzliche Objekt-IDs [Vorschlag].
- Objekt- und Gesellschaftsstamm werden **nie** direkt in d.velop geändert. Änderungen erfolgen in der Lieferanten-App und werden verteilt (S-04).

## 8.4 Kontierungsstammdaten und Kontierungsvorlagen

| Stammdatum | Quelle | Verwendung in smart invoice | Hinweise |
|---|---|---|---|
| Sachkonten | DATEV je Mandant (LDconnect) | Kontierung je Position; KI-Kontierungsvorschlag auf Belegebene | Kontenrahmen je Gesellschaft klären (einheitlich SKR?); Bucket-Limit 50.000 beachten (Kapitel 6.6) |
| KOST1 (Kostenstellen) | DATEV | Kostenstellen-Split je Position (Betrag oder Prozent) | Struktur auf Objekt- bzw. Hausebene; neue Kostenstellen legt Trios auf Anforderung an |
| KOST2 (Kostenträger) | DATEV | zweite Kontierungsdimension | Nutzung bei Livos klären |
| Steuerschlüssel | DATEV (Vorsteuerschlüssel); Standard-Steuerschlüssel je Mandant in smart invoice | Steuerberechnung; § 13b über eigenen Schlüssel | § 13b nur, wenn die Gesellschaft Bauleistender ist (Gesellschaftsstamm, E-20) |
| Zahlungsbedingungen | DATEV je Kreditor | Fälligkeit und Skonto, wenn die Rechnung keine Angaben enthält | Policy „Rechnung vor Stamm" oder „Stamm vor Rechnung" je Gesellschaft festlegen (T-18); Wert bleibt manuell änderbar |
| Custom Entities Bau | BIM4You (S-10) | Kopf- und Positionsfelder Projekt, Vergabeeinheit, Gewerk | Kapitel 8.5 |

**Kontierungsvorlagen (Katalog 2.8 = S/K):**

| Vorlagentyp | Inhalt | Beispiel (fiktiv) | Status |
|---|---|---|---|
| kreditorenabhängige Vorlage | Standard-Sachkonto und -Kostenstelle für wiederkehrende Rechnungen eines Kreditors | Stadtwerke → Sachkonto Strom/Gas, Kostenstelle Objekt | [K] |
| Standardschlüssel je Gesellschaft bzw. Objekt | prozentuale Aufteilung auf Kostenstellen | Haus A 55 % / Haus B 45 % | [K]; %-Logik der Vorlagen im Test-Tenant prüfen (OP-10) |
| KI-Kontierungsvorschlag | lernt aus bestätigten Kontierungen (Sachkonto, Kostenstelle auf Belegebene) | – | [S], nur C1 |

Hinweis: Je Gesellschaft gehen im Schnitt nur 50 bis 80 Rechnungen im Jahr ein. Die KI hat je Gesellschaft wenig Historie. Kreditorenabhängige Vorlagen und Standardschlüssel sind deshalb wichtig für eine hohe Vorbelegungsquote [A].

## 8.5 BIM4You-Stammdaten

| Objekt | Führend | Ziel in d.velop | Weg | Zweck |
|---|---|---|---|---|
| Bauprojekt | BIM4You | Custom Entity je Mandant im Bucket; Verknüpfung mit Objekt-ID über BIM4You-Projekt-ID im Objektstamm | S-10, nächtlich | Erkennung Bau-Rechnung, Kontierung |
| Vergabeeinheit / Los / Gewerk | BIM4You | Custom Entity bzw. Positionsdimension (hierarchisch unter dem Projekt); DMS-Wertemenge E-18 | S-10 | Zuordnung zur Vergabeeinheit, Übergabe an BIM4You |
| Vertrag / Auftrag (Nummer, Auftragswert) | BIM4You | Custom Entity; E-19 | S-10 | Vorgangsakte, VOB-Kumulation |
| Kreditor-Kennzeichen „Bauleistender" | Lieferanten-App | Weiche WF-02, FSB-Prüfung | S-04 | Erkennung Bau-Rechnung, § 48b |
| Schlüsselabgleich Mandant, Kreditor | Lieferanten-App | Mapping d.velop ↔ BIM4You (Mandanten-ID ↔ BIM4You-Mandant, DATEV-Kreditor ↔ BIM4You-Adresse) | S-08/S-09 | eindeutige Übergabe |

Da BIM4You keine veröffentlichte API hat, liest BeSync die Stammdaten über Export oder Austauschordner. Mit der BIB GmbH wird geklärt, welche Exporte verfügbar sind und ob ein Datenbankzugriff freigegeben wird (OP-06).

**Freistellungsbescheinigungen (AE-15, Phase 3):** Die FSB liegt als Dokument K-06 in der Kreditorenakte, mit „Gültig bis" (E-21). BeSync führt eine FSB-Status-Tabelle (Kreditor × Gesellschaft × gültig bis × Nachweis der Abfrage im BZSt-Portal). Bei Belegeingang eines Bau-Kreditors prüft BeSync den Status und setzt E-21. Fehlt die FSB oder ist sie abgelaufen, erhält der Beleg einen Hinweis bzw. Klärfall mit dem Vorschlag, 15 % einzubehalten (Zahlbetrag). Die Prüfung beim BZSt bleibt manuell, weil es dafür keine API gibt. Eine Wiedervorlage vor Ablauf der Gültigkeit erinnert die Kreditorenbuchhaltung.

## 8.6 Stammdatenqualität und Governance

### 8.6.1 Qualitätsregeln

| Regel | Umsetzung | Verantwortlich |
|---|---|---|
| Keine Dubletten bei Lieferanten | Dublettenprüfung in der Lieferanten-App (USt-IdNr., IBAN, Anschrift, E-Mail); KI-Vorschlag, menschliche Bestätigung | R-02, R-12 |
| Einheitliche Schreibweise | UTF-8, Umlaute, keine ASCII-Ersatzschreibweisen; Mandantenname exakt wie auf Rechnungen | R-12 |
| Vollständigkeit Gesellschafts- und Objektstamm | Pflichtfelder in der Lieferanten-App; Verteilung erst nach Vollständigkeitsprüfung | R-12, BeSync |
| Keine leeren Rechtewerte | BeSync verhindert leere Restriction-Set-Zuordnungen | MDIS |
| Aktualität DATEV-Stamm | Monitoring des täglichen LDconnect-Abgleichs; Fehlermeldung an MDIS und Trios | MDIS (R-15) |
| Nur aktive Kreditoren im Bucket | inaktive Kreditoren in DATEV kennzeichnen; Übertragung filtern, falls LDconnect das erlaubt [O] | Trios, MDIS |
| Stammdatenkennzahlen | Anzahl Klärfälle „Kreditor fehlt" und „Mandant unbekannt", offene Mapping-Vorschläge, Dubletten | Controlling (R-07), evidanza |

### 8.6.2 Bankverbindungen: Schutz vor Zahlungsbetrug

Geänderte Bankverbindungen sind ein bekanntes Betrugsmuster (gefälschte Rechnungen oder Mitteilungen mit neuer IBAN). Das Konzept setzt deshalb mehrere Kontrollen.

| Nr. | Kontrolle | Wo | Status |
|---|---|---|---|
| 1 | **Abgleich IBAN der Rechnung mit der Kreditor-Bankverbindung** aus DATEV; bei Abweichung Hinweis in der Verteilungsmaske (M-02) und kein automatischer Weiterlauf | smart invoice | [K]; Verhalten der Abweichungswarnung testen (OP-10) |
| 2 | **Bankdatenänderung nur in DATEV durch Trios, im Vier-Augen-Prinzip**; eine Person erfasst, eine zweite gibt frei | DATEV / Trios | organisatorisch, mit Trios vereinbaren |
| 3 | **Rückbestätigung beim Lieferanten** über eine bekannte, unabhängige Kontaktangabe (nicht über die Kontaktdaten der Änderungsmitteilung) | Trios / Livos | organisatorisch |
| 4 | Keine Übernahme einer neuen IBAN aus einer Rechnung in den Stamm ohne Kontrolle 2 und 3 | Lieferanten-App / DATEV | organisatorisch |
| 5 | **Änderungsprotokoll der Bankverbindungen** über den Stammdatenabgleich; BeSync meldet geänderte IBANs der letzten Tage an die Kreditorenbuchhaltung [A] | BeSync | [A] |
| 6 | Unterschrift der Zahlungen in multicash nach Unterschriftsklassen (Vier-Augen) | multicash | [S] |

### 8.6.3 Verantwortlichkeiten (Governance)

| Rolle | Verantwortung |
|---|---|
| Fachadministration Livos (R-12) | Eigentümer von Gesellschafts-, Objekt- und Lieferantenstamm in der Lieferanten-App; Freigabe neuer Lieferanten und Bankverbindungen; Freigabematrix |
| Rechnungseingang (R-02) | Klärfälle, Anlage-Anforderungen, Bestätigung von Mapping-Vorschlägen |
| Trios (R-06) | DATEV-Kreditoren, Sachkonten, Kostenstellen, Zahlungsbedingungen, Bankverbindungen im Vier-Augen-Prinzip; Service-Level für Kreditoranlage |
| Controlling (R-07) | Anforderungen an Kostenstellen und Kontierungsvorlagen; Stammdatenkennzahlen |
| Livos IT | Entra-ID-Gruppen, Postfächer |
| MDIS (R-15) | Betrieb BeSync und Lieferanten-App, Schnittstellenmonitoring, Limitüberwachung (Kapitel 6.6), technische Tabellen |

## 8.7 Konflikt „ein schreibendes System je Bucket" und Optionen

LDconnect schreibt täglich die DATEV-Stammdaten in den smart-invoice-Bucket. Würde BeSync dieselben Objekte ebenfalls schreiben, würden sich beide Systeme gegenseitig überschreiben. AE-09 legt deshalb fest: **DATEV-Stammdaten schreibt nur LDconnect.**

Präzisierung: BeSync muss dennoch in den Bucket schreiben, und zwar Objekte, die LDconnect laut Leistungsschein nicht überträgt: smart-invoice-Mandanten (Name und Anschrift für die Erkennung, AE-28) und Custom Entities aus BIM4You (S-10). Die Regel lautet daher genauer: **je Objekttyp im Bucket genau ein schreibendes System.**

| Objekttyp im Bucket | Schreibendes System (Option A, Empfehlung) | Schreibendes System (Option B) |
|---|---|---|
| Mandanten (Companies) | BeSync (aus Gesellschaftsstamm) | BeSync |
| Kreditoren, Bankverbindungen | LDconnect | BeSync (liest DATEV selbst über DATEVconnect) |
| Sachkonten, KOST1, KOST2, Steuerschlüssel, Zahlungsbedingungen | LDconnect | BeSync |
| Custom Entities (BIM4You, Rückweisungs-/Kürzungsgründe) | BeSync bzw. Fachadministration | BeSync bzw. Fachadministration |
| Buchungsvorschlag an DATEV | LDconnect | LDconnect |

Vergleich der Optionen:

| Kriterium | Option A: LDconnect schreibt DATEV-Stamm (Empfehlung) | Option B: BeSync schreibt den gesamten Bucket, LDconnect nur Buchung |
|---|---|---|
| Standardnähe (P2) | hoch: Stammdatenabgleich ist Teil der Option DATEV Rechnungswesen | geringer: Stammdatenabgleich als MDIS-Entwicklung |
| Aufwand und Betrieb | gering für MDIS; Betrieb bei LIONDEER | höher: DATEVconnect-Lesezugriff, Mapping, Fehlerbehandlung durch BeSync |
| Konsolidierungsnummer im Bucket | nicht möglich (kein freies Feld); nur als DMS-Eigenschaft | ebenfalls kein freies Feld; nur als DMS-Eigenschaft oder Custom Entity |
| Filter (nur aktive Kreditoren, Bucket-Limits) | abhängig von LDconnect-Konfiguration [O] | frei steuerbar |
| Aktualität | täglich | frei wählbar (z. B. mehrfach täglich oder bei Anforderung) |
| Voraussetzung | – | LDconnect-Stammdatenabgleich muss abschaltbar sein [O]; Absprache mit LIONDEER |
| Abhängigkeit vom Gateway | ja (LDconnect über Riecken) | ja (BeSync über Riecken oder Gateway) |
| Livos-Haltung zu Middleware (P3) | passt: weniger BeSync-Umfang | weniger passend: mehr Eigenbau |

**Empfehlung:** Option A (AE-09, Status E). Option B bleibt als Alternative (Status O) für den Fall, dass sich im Test zeigt, dass LDconnect die Bucket-Limits nicht einhalten kann (Filter) oder der tägliche Abgleich für den Klärfallprozess zu träge ist. Entscheidungsgrundlage sind das Mengengerüst aus dem Kreditorenexport (8.2.4, OP-21) und die Antworten von LIONDEER (OP-22). Die Entscheidung trifft Livos als ED-02.

Offene Punkte zur Klärung:

| Frage | Klärung mit | Bezug |
|---|---|---|
| Welche Mandanten-ID verwendet LDconnect im Bucket? Legt LDconnect selbst Mandanten an? | LIONDEER | OP-04 |
| Kann LDconnect nur aktive Kreditoren bzw. nur bebuchte Sachkonten übertragen? Sachkonten ohne Mandantenbezug? | LIONDEER | OP-22 |
| Ist ein Stammdatenabgleich im Tagesverlauf oder auf Anforderung möglich? | LIONDEER | OP-22 |
| Sollen die 80000er-HV-Kreditoren in den Bucket? (Nutzen: PM-Freigabe WF-03; Risiko: falsche Zuordnung interner Rechnungen) | Livos, Trios | OP-17 |
| Service-Level von Trios für die Kreditoranlage | Trios | OP-17 |
| Liegen alle DATEV-Bestände auf einem System unter einer Beraternummer (ein Gateway)? | Trios, Hoster | OP-04 |

# 9 Prozesskonzept Eingangsrechnung

Dieses Kapitel beschreibt den Soll-Prozess für Eingangsrechnungen der LIVOS Gruppe vom Eingang bis zur Rückmeldung „bezahlt". Es setzt die Architekturentscheidungen AE-04, AE-06 bis AE-15 und AE-22/AE-23 fachlich um. Die Freigabelogik (Matrix, Vier-Augen, Eskalation, Vertretung, Statusmodell) steht in Kapitel 10, der Property-Manager-Prozess in Kapitel 11.

Belegstatus: **[S]** Standard belegt · **[K]** Konfiguration · **[A]** Anpassung/Entwicklung (MDIS BeSync) · **[O]** offen/zu verifizieren.

## 9.1 Prozessüberblick

### 9.1.1 Livos-Zielkette und Umsetzung in smart invoice

Die MDIS-Zielarchitektur (Folie „Eingangs-Rechnungsprozess") definiert sechs d.velop-Schritte: Eingang → Verarbeitung & Vorqualifikation → Verteilung → Fachliche Prüfung/Detailqualifikation (Bau: BIM4You) → Fachliche Freigabe → Zahlungsfreigabe. Die folgende Tabelle ordnet jedem Schritt den smart-invoice-Baustein, die Systeme und die Rollen zu.

| Nr. | Livos-Zielkette (Folie) | Umsetzung in d.velop (WF-01/WF-02) | Systeme | Rolle | Status |
|---|---|---|---|---|---|
| 1 | Eingang | E-Mail-Import (zentrale Adresse + Alias je Gesellschaft), Scan, Upload; Stapelbildung | d.velop inbound, email import (M365) | System; R-01 (Scan) | [S] |
| 2 | Verarbeitung & Vorqualifikation | Erkennung (document reader), E-Rechnung-Konvertierung/-Validierung, § 14-Grundprüfung, Dublettenprüfung, Mandanten- und Kreditorenerkennung | document reader, eInvoice converter | System | [S]/[K] |
| 3 | Verteilung | Schritt **Verteilung**: Mandant, Kreditor, Belegart, Kostenobjekt und Sachlichen Prüfer bestätigen; Klärfall (WF-04) | smart invoice | R-02 | [S]/[K] |
| 4 | Fachliche Prüfung / Detailqualifikation | Schritt **Sachliche Prüfung & Kontierung**; Bau: zusätzlich asynchroner Schritt **Warten auf BIM4You** (WF-02) | smart invoice; BIM4You über BeSync | R-03, R-08 | [K] / Bau [A] |
| 5 | Fachliche Freigabe | Schritt **Fachliche Freigabe** 1..n Stufen nach Freigabematrix (Kapitel 10) | smart invoice | R-04 | [K] |
| 6 | Zahlungsfreigabe | Schritt **Zahlungsfreigabe** | smart invoice | R-05 | [K] |
| 7 | (Folie: DATEV-Integration an Verteilung und Freigabe) | Schritt **Buchhaltung**: Kontrolle, Übergabe Buchungsvorschlag + Beleglink an DATEV (einstufig, AE-08) | smart invoice, LDconnect, DATEV | R-06 (Trios) | [K] |
| 8 | (Folie: Durchführung der Zahlung) | Buchung, Zahlungsvorschlag, SEPA-Datei, Unterschrift und Ausführung | DATEV, multicash | R-06, R-05 | [S] außerhalb d.velop |
| 9 | (nicht auf Folie) | Rückmeldung „bezahlt" an den Beleg (S-06) | BeSync, DATEVconnect | System (R-13) | [A] |

**Zwei Abweichungen von der Folie, jeweils begründet:**

| Abweichung | Folienbild | Konzept | Begründung |
|---|---|---|---|
| DATEV-Übergabe | zweistufig: ER-Vorerfassungsjournal bei der Verteilung, Verbuchung nach fachlicher Freigabe | **einstufig** nach der Zahlungsfreigabe (AE-08, Status O) | LDconnect übergibt je Rechnung einen Buchungsvorschlag und überträgt keine Postensperre (LDconnect Leistungsschein 11/2025). Eine frühe Übergabe würde einen zahlbaren offenen Posten erzeugen, bevor die Zahlungsfreigabe erteilt ist. Die Transparenz des „Vorerfassungsjournals" liefert das Rechnungseingangsbuch (REB). |
| Reihenfolge Buchhaltung | Verbuchung zwischen Freigabe und Zahlungsfreigabe | Zahlungsfreigabe **vor** dem Schritt Buchhaltung (AE-06) | wie oben: Die Zahlungsfreigabe ist die letzte Kontrolle, bevor ein zahlbarer Posten in DATEV entsteht. |

### 9.1.2 Workflowdefinitionen im Überblick

| ID | Prozess | Einsatz | Phase |
|---|---|---|---|
| WF-01 | Standard-Eingangsrechnung | alle Rechnungen, die nicht Bau-/BIM4You-relevant und nicht PM-Freigaben sind | 1 |
| WF-02 | Bau-Eingangsrechnung | Bauprojekt-Rechnungen mit BIM4You-Prüfung | 3 (Pilot-Bau in Phase 1 ohne BIM4You-Automatik) |
| WF-03 | PM-Freigabe | Freigabeanfragen der Property Manager (Kapitel 11) | 2 |
| WF-04 | Klärfall Mandant/Kreditor | Belege ohne eindeutigen Mandanten oder Kreditor, Dubletten | 1 |
| WF-05 | Rückweisung/Kürzungsmitteilung an Lieferanten | automatische Lieferantenmail | 2 |

WF-04 (Klärfall) und WF-05 (Rückweisung/Kürzungsmitteilung) sind fachlich eigene Prozesse mit eigener ID (AE-04). Technisch werden sie als Schritte, Pfade und Aktionen innerhalb von WF-01 bis WF-03 umgesetzt (Klärfall-Schritt, Clearing, Endpfad „Zurückgewiesen" mit Export an BeSync, Kapitel 10.1.2); eine eigene Workflowdefinition für den Klärfall bleibt möglich, falls der Test es nahelegt.

### 9.1.3 Ablauf WF-01 (Schrittfolge)

| Schritt | Bezeichnung | Bearbeiterfindung | Ausgänge (Verbindungen, top-down ausgewertet) |
|---|---|---|---|
| 0 | Workflowstart | System | Startverbindung (optional Export an BeSync für FSB-/IBAN-Prüfung, Phase 3) |
| 1 | Verteilung | Gruppe `SI_Verteilung` bzw. Clearing-Gruppe (Kapitel 13.5.4) | → Klärfall · → Sachliche Prüfung · → Zurückgewiesen (Dublette/Formfehler) |
| 1a | Klärfall (WF-04) | Gruppe Rechnungseingang (R-02) | → Verteilung (nach Klärung) · → Zurückgewiesen |
| 2 | Sachliche Prüfung & Kontierung | Sachliche Prüfer je Kostenobjekt (Prüfermatrix oder Auswahl in Verteilung) | → Fachliche Freigabe · → Rückfrage Verteilung · → Zurückgewiesen · (WF-02: → Warten auf BIM4You) |
| 3 | Fachliche Freigabe (1..n) | Freigabematrix (Kapitel 10) | → nächste Freigabestufe (Wertgrenzen-Verbindung) · → Zahlungsfreigabe · Ablehnen → Sachliche Prüfung |
| 4 | Zahlungsfreigabe | Gruppe Zahlungsfreigeber je Mandant (R-05) | → Buchhaltung · Ablehnen → Sachliche Prüfung/Freigabe |
| 5 | Buchhaltung | Trios (R-06) | Export „book" an LDconnect → Ende „Übergeben" · → Clearing (Fehler) |
| E1 | Ende „Übergeben an DATEV" | – | Beleg archiviert; Zahlstatus folgt über S-06 |
| E2 | Ende „Zurückgewiesen" | – | Export an BeSync (S-11, Lieferantenmail außer bei Dublette) |

## 9.2 Eingang

### 9.2.1 Eingangskanäle

| Kanal | Technik | Vorbelegung | Kennzeichnung E-25 | Status |
|---|---|---|---|---|
| Zentrale Rechnungsadresse `rechnung@…` | d.velop email import über Microsoft Graph (M365), je E-Mail ein Stapel | Mandant leer → Erkennung | E-Mail | [S] (Voraussetzung M365, OP-16) |
| Alias je Gesellschaft (Vorschlag `rechnung+<MandantNr>@…`) | Alias-Adresse am selben Postfach mit eigenem Importprofil | Schlüssel-Wert-Paar „Mandant = <Mandanten-ID>" | E-Mail | [K] (Übernahme der Vorbelegung durch die Erkennung testen, OP-02) |
| E-Rechnung (XRechnung 3.0, ZUGFeRD 2.x, Factur-X) | über dieselben Postfächer; XML ist das Original | wie Postfach | E-Rechnung | [S] |
| Papier | zentraler Scan (R-01) mit inbound scan bzw. Scandienstleister (OP-13) | Importprofil „Scan" | Scan | [S] |
| Upload | „Rechnung einlesen" (M-01), Drag & Drop, Import-Widget mit Dropzones | je Dropzone ein Importprofil | Upload | [S] |
| PM-Freigabe | eigenes Postfach `freigabe-hv@…` → WF-03 (Kapitel 11) | Importprofil PM | PM-Freigabe | [K] |

Peppol ist nicht erforderlich. Für den Empfang von E-Rechnungen genügt ein E-Mail-Postfach (BMF FAQ E-Rechnung 03/2026). d.velop bietet keinen eigenen Peppol-Zugang an.

### 9.2.2 Postfächer, Aliasse und Importprofile

| Element | Empfehlung | Begründung |
|---|---|---|
| Postfachanzahl | ein M365-Rechnungspostfach mit Aliassen, zusätzlich ein PM-Postfach | email import unterstützt Alias-Adressen je Postfach mit eigenem Importprofil (email import Handbuch Cloud). In C1 gilt eine Grenze von 10.000 E-Mails je Monat und Postfach (d.velop invoices Leistungsbeschreibung 12/2025) – für 20–30 Rechnungen/Tag unkritisch. |
| Alias je Gesellschaft | für Gesellschaften mit gleicher Anschrift **zwingend**, für alle anderen empfohlen | Die Mandantenerkennung arbeitet nur über Name und Anschrift (AE-23). |
| Importprofile | „ER automatisch" (Mail/E-Rechnung), „ER Scan", „ER manuell", je Alias ein Profil mit Mandant-Vorbelegung, „PM-Freigabe" | Profile steuern Texterkennung, Trennung, Standardkategorie K-01 und Vorbelegung. |
| Mail-Textkörper | als eigenes Dokument (Kategorie K-07 Korrespondenz) oder nicht übernehmen; Anlagen einer E-Rechnung dem PDF-Anhang hinzufügen | vermeidet, dass Begleittexte als Rechnung erkannt werden. |
| Absenderfilter | alle Absender zulassen (`*@*`); keine Whitelist | Lieferanten senden oft von anderen Adressen als der Stamm-E-Mail (Testdaten Beleg 23). |
| Kommunikationsweg | **inbound → document reader → smart invoice** von Beginn an | Der bisherige Weg wird zum 01.01.2027 abgeschaltet; nur der neue Weg liefert die Prüfberichte der XRechnung-Validierung (Helpcenter 09/2026). |
| IT-Sicherheit | Graph-Berechtigung per Exchange-Richtlinie auf die Rechnungspostfächer einschränken | Die App-Registrierung hätte sonst Zugriff auf jedes Postfach (email import Handbuch). |

### 9.2.3 Scan und Stapel

| Thema | Regel |
|---|---|
| Stapelbildung | E-Mail: je E-Mail ein Stapel; Scan: je Scanvorgang ein Stapel mit Trennung per Trennblatt oder Barcode. |
| Stapelprüfung | R-01 prüft Seitenzahl, Trennung und Lesbarkeit in der Stapelübersicht (M-01). |
| Mehrere Rechnungen in einer Mail | werden als getrennte Dokumente im Stapel erkannt; Trennung prüft R-02 bei Auffälligkeiten. |
| Papieroriginal | nach Scan gemäß Verfahrensdokumentation (ersetzendes Scannen, Kapitel 17). |
| Stapelname | `%Sender% – %Subject% – %Timestamp%` für Nachvollziehbarkeit. |

## 9.3 Verarbeitung und Vorqualifikation

Die Vorqualifikation läuft vollautomatisch vor dem ersten Benutzerschritt. Ergebnis ist ein Beleg mit Kopf- und Positionsdaten, Mandant, Kreditor und Hinweisen.

| Prüfung | Funktion | Ergebnis bei Abweichung | Status |
|---|---|---|---|
| Erkennung | document reader liest Kopf- und Positionsdaten (Rechnungsnummer, -datum, Leistungsdatum, Beträge je Steuersatz, Skonto-/Nettofälligkeit, IBAN, Positionen). Lernt aus Korrekturen in der Maske (Autotraining, C1). | manuelle Ergänzung in der Verteilung | [S] |
| E-Rechnung | Metadaten direkt aus dem XML; Visualisierung als PDF; XML bleibt Original | – | [S] |
| XRechnung-Validierung | eInvoice converter prüft Syntax, EN 16931 und XRechnung-Regeln (KoSIT); Prüfbericht als Anlage | Fehler → Rückweisung mit Grund 5 (Sonderfall 9.11.9) | [S] |
| ZUGFeRD-Profilprüfung | nicht im Standard; Profile MINIMUM/BASIC-WL sind keine gültige E-Rechnung | Prüfung über BeSync oder organisatorisch | [A]/[O] (OP-41) |
| Pflichtangaben § 14 UStG | Dokumentprüfung: Mandantendaten (Name, Anschrift), Lieferant im Stamm, USt-IdNr./Steuernummer, IBAN vorhanden, Rechnungsdatum/-nummer, Beträge | Hinweis; bei fehlenden Pflichtangaben Rückweisung Grund 1 | [S] (Grundprüfung; keine vollständige Einzelprüfung aller Pflichtangaben) |
| Dublettenprüfung Stufe 1 | document reader: Rechnungsnummer gegen bereits validierte Belege | Hinweis | [S] |
| Dublettenprüfung Stufe 2 | smart invoice: Kreditornummer + Rechnungsnummer gegen Workflows der letzten 18 Monate; Warnung nur mit Begründung akzeptierbar; Neuprüfung bei Änderung | Klärfall Dublette (9.4) | [S] |
| Mandantenerkennung | Name + Anschrift gegen smart-invoice-Mandanten; Alias-Vorbelegung; bei E-Rechnung Käuferdaten | kein Treffer → Standardmandant „Klärfall" (WF-04) | [K] (AE-23) |
| Kreditorenermittlung | USt-IdNr., Steuernummer, Name, Anschrift, Bankverbindung gegen Kreditoren des Mandanten (aus DATEV über LDconnect, S-02) | kein Treffer → Klärfall „Kreditor fehlt" | [S] |
| Lieferanten-Konsolidierungsnummer | BeSync ergänzt E-07 aus der Lieferanten-App als DMS-Eigenschaft (S-04) | leer → Hinweis an R-12 | [A] |
| IBAN-Abgleich | Kreditor-Bankverbindungen liegen im Bucket (S-02) und sind laut API „zum Abgleich" vorgesehen; Beleg-IBAN (`iban`) und Stamm-IBAN (`vba_iban`) sind als DMS-Eigenschaften abbildbar | Anzeigeform der Warnung ungeklärt → Test; Fallback BeSync-Prüfung (9.11.10) | [O] (OP-10) |
| Zahlungsbedingung / Fälligkeit | Fälligkeit wird aus der Zahlungsbedingung des Kreditors berechnet; erkannte Skonto-/Nettofälligkeit wird als „manuelles Zahlungsziel" vorausgewählt; **Hinweis bei Abweichung** vom Kreditor-Standard; Skontoampel | Bearbeiter entscheidet in der Verteilung | [S] (Helpcenter 04/2026) |

**Regel Fälligkeit (Vorschlag, von Livos zu bestätigen):** Führend ist die Zahlungsbedingung aus dem DATEV-Kreditorenstamm. Weicht der Beleg günstiger für Livos ab (längeres Ziel, höheres Skonto), übernimmt R-02 den Belegwert. Weicht er ungünstiger ab, gilt der Stammwert, und R-03 klärt die Abweichung. Damit ist die Workshop-Frage „Beleg oder Stamm?" (Workshop 22.09.2026, [00:29:00]) als Konfiguration je Workflow entschieden.

## 9.4 Verteilung und Klärfall

### 9.4.1 Schritt Verteilung

Rolle R-02 (Rechnungseingang/Kreditorenbuchhaltung Livos) bearbeitet den Beleg in der Maske M-02 (Belegdaten links, Beleg rechts).

| Aufgabe | Pflicht | Hinweis |
|---|---|---|
| Mandant prüfen/bestätigen (E-01) | ja | Mandant ist Schlüssel für Rechte, Akten, Routing, DATEV (P1). |
| Kreditor prüfen (E-05) | ja | Kreditoren sind je Mandant angelegt; ein falscher Mandant führt zu falschem Kreditor. |
| Belegart (E-14) | ja | Rechnung, Gutschrift, Abschlags-, Schluss-, Stornorechnung; steuert Bau-Routing und Buchung. |
| Rechnungsnummer, -datum, Leistungsdatum, Beträge | ja | Korrektur erkannter Werte; Änderungen werden protokolliert. |
| Objekt-ID / Kostenobjekt (E-03, E-17) | ja, wenn objektbezogen | Grundlage für Sachlichen Prüfer und Freigabematrix. |
| Sachlicher Prüfer | ja | Vorschlag aus Prüfermatrix (Objekt/Kostenstelle → Prüfer); Übersteuerung möglich. |
| Hinweise quittieren | ja | Dublette (Begründung), abweichende Zahlungsbedingung, IBAN-Hinweis, § 13b-Plausibilität. |
| Rückweisung | optional | Formfehler, falscher Empfänger (Grund 1, 2, 5). |

Bearbeiterfindung Sachlicher Prüfer [K]: Die Verteilung setzt den Prüfer über die Positionen (Kostenobjekt) oder die Prüfermatrix. Der Folgeschritt nutzt die Bearbeiterfindung `user.name IN voucher.outstanding_verifiers` mit „Alle Treffer verwenden" (smart invoice Cloud Handbuch 06/2026). Bei mehreren Kostenobjekten erhalten mehrere Prüfer je ihre Positionen.

### 9.4.2 Klärfall (WF-04)

| Klärfall | Auslöser | Behandlung | Rolle | Status |
|---|---|---|---|---|
| Mandant unbekannt | Erkennung findet keine Gesellschaft; Standardmandant „Klärfall" | R-02 ordnet den richtigen Mandanten zu. Ist die Gesellschaft nicht angelegt: Anlage im Gesellschaftsstamm (Lieferanten-App/BeSync, R-12) → smart-invoice-Mandant, Dataset, Gruppe (AE-18/AE-28) → Beleg läuft weiter. Ist Livos nicht Empfänger: Rückweisung Grund 2. | R-02, R-12 | [K] / Anlage [A] |
| Kreditor fehlt | Lieferant im Mandanten nicht vorhanden | R-02 stößt in der Lieferanten-App (M-16) die Anlage-Anforderung an; Trios legt den Kreditor in DATEV an; LDconnect synchronisiert am Folgetag; BeSync ergänzt die Konsolidierungsnummer; Beleg wird im Klärfall-Schritt wiedervorgelegt und mit Kreditor weitergeleitet (AE-09). Livos legt keine Kreditoren in DATEV an. | R-02, R-06, R-12 | [K] / Anforderung [A] (S-05) |
| Dublette | Warnung Stufe 1 oder 2 | R-02 prüft Original vs. Dublette. Echte Dublette → Ablehnen ohne Lieferantenmail (9.11.1). Keine Dublette (z. B. gleiche Nummer, anderer Lieferant) → Warnung mit Pflichtbegründung akzeptieren. | R-02 | [S] |
| Falsch zugeordnet (nach Verteilung erkannt) | Prüfer oder Freigeber stellt falschen Mandanten/Kreditor fest | Clearing-Modus: Clearing-Gruppe des Mandanten korrigiert; alle Felder beschreibbar; Änderungen im Workflowprotokoll | R-02 (Clearing-Gruppe) | [S] |

**Clearing je Mandant [K]:** smart invoice erlaubt eine globale Clearing-Gruppe und Clearing-Gruppen je Mandanten-ID (smart invoice Cloud Handbuch 06/2026). Vorschlag: global `SI_Clearing_Zentral` (Kreditorenbuchhaltung Livos), zusätzlich je Gesellschaftsgruppe/Verbund eine Clearing-Gruppe nur dort, wo eine eigene Buchhaltungsverantwortung besteht. Der Clearing-Status ist im REB sichtbar („Clearing Modus").

**Klärfall-Frist (Vorschlag):** Klärfall „Kreditor fehlt" wird nach 2 Arbeitstagen an die Leitung Kreditorenbuchhaltung eskaliert (Kapitel 10.4), da Skontofristen laufen.

## 9.5 Sachliche Prüfung und Kontierung

Rolle R-03 (Asset Manager, Objektbetreuer, Projektleiter, Fachbereich) prüft in Maske M-03, ob Leistung, Menge und Preis stimmen, und vervollständigt die Kontierung.

| Tätigkeit | Umsetzung | Status |
|---|---|---|
| Sachlich richtig bestätigen | Feld „Sachl. richtig" je Position; Bedingung `voucher.verified?` vor Weitergabe | [S] |
| Rechnerisch richtig | als Eigenschaft der Schrittverbindung „Weiter" („Rechnerisch Richtig: Erteilen"), Benutzer und Zeitpunkt protokolliert | [S] |
| Positionen prüfen | Menge, Einzelpreis, Rabatte je Position; automatische Neuberechnung der Summe | [S] |
| Kostenstellen-Split | mehrere Positionen mit eigenem Sachkonto, Kostenstelle (KOST1), Kostenträger (KOST2) bzw. Objekt; Summenprüfung `amount_allocated_tolerance?` vor der Freigabe | [S] |
| Standardschlüssel | kreditorenabhängige Kontierungsvorlagen je Gesellschaft × Kreditor (z. B. Verbrauchsaufteilung Haus A 55 % / Haus B 45 % – Beispiel aus Testdaten) | [K] (prozentuale Logik testen, OP-10) |
| Kontierungsvorschlag KI | Sachkonto und Kostenstelle **auf Belegebene**, lernend (nur Betriebsform C1); Projekt/Position über Vorlagen | [S] (C1) |
| Zahlbetrag / Kürzung | Zahlbetrag `pay_amount` (Kopf/Position) + Pflichtfeld Kürzungsgrund E-13 (9.11.3) | [K] (Feld schreibbar schalten, OP-10) |
| Nachweise anhängen | Lieferschein, Aufmaß, Abnahmeprotokoll, Stundenzettel als K-02 am Beleg; Mehrfachablage in Objekt-/Vorgangsakte | [S] |
| Notizen, Annotationen | Kommentare in der Historie; PDF-Annotationen auf dem Beleg (Original bleibt unverändert) | [S] |
| Rückfrage | Aktion „Rückfrage an Verteilung" (zurück zu R-02) oder Ad-hoc-Weiterleitung an einen Kollegen; Rückfrage an Lieferant manuell per „Teilen per E-Mail/Link" | [S]/[K] |
| Rückweisung | Aktion „An Lieferant zurückweisen" mit Pflichtgrund (9.11.2) | [K] + [A] Mail |
| Mehrstufige Fachprüfung | erweiterte Prüfung mit Prüfungstypen innerhalb **eines** Prüfungsschritts (z. B. Objektbetreuer, dann Technik) | [S] (nur ein Prüfungsschritt je Workflow) |

**Grundsatz Kontierungsverantwortung (Vorschlag):** R-03 kontiert fachlich (Objekt, Kostenstelle, Leistungsart). Trios (R-06) prüft und ergänzt steuerlich (Sachkonto, Steuerschlüssel, BU-Schlüssel) im Schritt Buchhaltung; dafür sind Positionsfelder dort „schreibbar wenn geprüft".

## 9.6 Bau-Variante WF-02 mit BIM4You

Die Bau-Variante setzt AE-11 um. Kumulierte VOB-Prüfung, Budgetabgleich, Nachträge und Einbehalte rechnet BIM4You (BIB GmbH), nicht d.velop. d.velop führt Beleg, Workflow, Freigabe und die DATEV-Übergabe (P4).

### 9.6.1 Erkennung Bau

Ein Beleg läuft in WF-02, wenn eine der Bedingungen zutrifft (Startverbindung oder Verbindung nach Verteilung, top-down):

| Kriterium | Quelle | Status |
|---|---|---|
| Objekt-ID ist im Objektstamm als „Bauprojekt = ja" mit BIM4You-Projekt-ID geführt (AE-28) | Dataset Objekte / Custom Entity | [K] |
| Belegart = Abschlagsrechnung oder Schlussrechnung (E-14) | Verteilung / Erkennung (XRechnung BT-3 Codes 875/877) | [K] |
| Kreditor ist als „Bauleistender" gekennzeichnet (Steuerkategorie am Kreditor, z. B. `BAU13B`) | Kreditorenstamm | [K] |
| Gewerk/Vergabeeinheit (E-18) oder Auftragsnummer (E-19) gefüllt | Verteilung, BIM4You-Stamm (S-10) | [K]/[A] |

### 9.6.2 Ablauf

| Nr. | Schritt | System | Beschreibung | Status |
|---|---|---|---|---|
| 1 | Verteilung | smart invoice | wie WF-01; zusätzlich Projekt, Vergabeeinheit/Gewerk, Auftragsnummer | [K] |
| 2 | Sachliche Prüfung (Vorprüfung) | smart invoice | Projektleitung prüft Zuordnung und Vollständigkeit der Nachweise | [K] |
| 3 | Übergabe an BIM4You | smart invoice → BeSync → BIM4You | Export an der Verbindung „Bauprüfung" als **asynchroner Transfer** (Abhol-API); BeSync übergibt Kopfdaten, PDF/XML und Beleg-ID als Barcode/Referenz an BIM4You (E-Rechnungsimport bzw. Austauschordner, S-08) | [A] |
| 4 | Warten auf BIM4You | smart invoice | Beleg im Zustand „aktiver Belegdatentransfer" ohne Benutzerinteraktion; Zeitfenster bis **28 Tage** (smart invoice API-Handbuch) | [S] Mechanik / [A] Nutzung |
| 5 | Prüfung in BIM4You | BIM4You | Budgetabgleich, kumulierte VOB-Prüfung gegen Auftrag und bisherige Abschläge, Einbehalte, Nachträge, Prüfer-Workflow RP1/RP2 | BIM4You-Standard |
| 6 | Rückweg | BIM4You → BeSync → d.velop | BeSync pollt das Ergebnis, setzt DMS-Eigenschaften E-22 (geprüfter Betrag, Sicherheitseinbehalt, Freigabestatus BIM4You), legt Prüfbericht/Zahlungsfreigabe-PDF als K-08 ab und meldet den Transfer `successful` (S-09). Ablehnung in BIM4You → `successful = false` mit Meldetext → Beleg geht in den Fehler-/Klärschritt | [A] |
| 7 | Zahlbetrag setzen | smart invoice | Die Rechnungsprüfung (R-03 bzw. R-02) überträgt den BIM4You-Zahlbetrag in `pay_amount` mit Kürzungsgrund „Einbehalt" bzw. „Bauabzug". Ein API-Schreibzugriff auf laufende Belege ist nicht dokumentiert (OP-07). | [K] manuell / [O] automatisch |
| 8 | Fachliche Freigabe, Zahlungsfreigabe, Buchhaltung | smart invoice | wie WF-01 | [K] |

### 9.6.3 Regeln und Abgrenzung

| Regel | Inhalt |
|---|---|
| Führendes System | d.velop führt Beleg, Workflow und DATEV-Übergabe; BIM4You führt Budget, Vertrag/Nachtrag, VOB-Kumulation, Einbehalte (P4). Die Festlegung je Rechnungstyp ist mit Livos offen (OP-06). |
| Keine Doppelübergabe | Nur d.velop übergibt Eingangsrechnungen an DATEV. Der BIM4You-DATEV-Export für Eingangsrechnungen bleibt deaktiviert. |
| Zeitfenster | Das Transferfenster wird so kurz wie fachlich möglich gewählt (Vorschlag 14 Tage). Läuft es ab, geht der Beleg in den Fehlerschritt; R-02 prüft den BIM4You-Stand und startet den Transfer erneut. |
| Transparenz | Im REB ist der Beleg während der BIM4You-Prüfung als „aktiver Belegdatentransfer" sichtbar; BeSync liefert eine tägliche Abstimmliste d.velop ↔ BIM4You (offene Übergaben, Beträge). |
| Storno | Storno in BIM4You wird gespiegelt: Transfer `false` mit Meldung; Abbruch in d.velop (`end_mode = aborted`) wird an BIM4You gemeldet. |
| Sonderbuchungsinfos | ARAP/PARP, Rückstellungen, Anzahlungen aus BIM4You sind nicht Teil von WF-02 (Folgeprojekt, OP-06/OP-18). |
| Übergang Phase 1 | Bis zur BIM4You-Automatik (Phase 3) laufen Bau-Rechnungen über WF-01 ohne Transfer (Pilot-Bau, Kapitel 19.2.3); der Prüfbericht aus BIM4You wird manuell als K-08 angehängt, der Zahlbetrag manuell mit Kürzungsgrund gesetzt. |

## 9.7 Fachliche Freigabe

Die fachliche Freigabe erfolgt durch R-04 nach der Freigabematrix (Spalten Mandant, Kostenobjekt, Betragsgrenze, Stufe, Freigeber-Gruppe) mit 1..n Stufen, Vier-Augen-Prinzip (Prüfer ≠ Freigeber) und Wertgrenzen-Verbindungen. Details, Beispielgrenzen, Eskalation und Vertretung: **Kapitel 10**.

Aktionen in der Maske M-04: Freigeben, Ablehnen (zurück an Sachliche Prüfung, Pflichtkommentar), Rückfrage, Historie anzeigen.

## 9.8 Zahlungsfreigabe

| Aspekt | Festlegung |
|---|---|
| Zweck | Finanzielle Kontrolle unabhängig von der fachlichen Freigabe: Zahlbetrag (inkl. Kürzung/Einbehalt), Bankverbindung, Fälligkeit/Skonto, Liquidität. Funktionstrennung sachlich/finanziell (Livos-Folie). |
| Rolle | R-05 Zahlungsfreigeber (GF/kaufmännische Leitung/Treasury), Gruppe je Mandant bzw. Gesellschaftsverbund (`SI_Zahlung_<MandantNr>`, Kapitel 13.5.2). |
| Position im Workflow | **vor** dem Schritt Buchhaltung/DATEV-Übergabe (AE-06). LDconnect überträgt keine Zahlungssperre; jeder übergebene Buchungsvorschlag wird nach Buchung zum zahlbaren offenen Posten. |
| Umsetzung | Schritt vom Typ Freigabe mit Aktionen Bestätigen/Ablehnen; Bearbeiterfindung über Gruppe je Mandant (Regex auf `voucher.company.nr`) [K]. |
| Vier-Augen | Zahlungsfreigeber ≠ letzter fachlicher Freigeber für denselben Beleg (Vorschlag, Test T41). Die Unterschrift in multicash nach Unterschriftsklassen bleibt als zweite Kontrolle bestehen (AE-10). |
| Sammelfreigabe | nicht vorgesehen; smart invoice gibt je Beleg frei. REB-Schnellzugriff „Zur Zahlungsfreigabe, sortiert nach Skontofälligkeit" unterstützt die Abarbeitung. [K] |
| Nicht empfohlen | „Beim Buchen geht die Zahlung raus" (Workshop 22.09.2026, [00:33:28]) – würde Unterschrift und Vier-Augen-Prinzip im Zahlungsverkehr umgehen. |

## 9.9 Buchhaltung und DATEV-Übergabe

| Aspekt | Festlegung | Status |
|---|---|---|
| Rolle | R-06 Buchhaltung (Trios), invoices-Buchhaltungsuser (Zulässigkeit für Externe: OP-03) | [O] |
| Tätigkeit | Kontrolle Kontierung, Steuerschlüssel (inkl. § 13b), Sachkonto; Buchungsvorschau (M-07); Aktion „An DATEV übergeben" | [S] |
| Technik | Option „DATEV Rechnungswesen" (LDconnect) über DATEVconnect und Riecken-Datengateway (Pflicht bei DATEVasp/SmartIT) (S-01) | [K] |
| Auslösung | ereignisgesteuert je Rechnung an der Verbindung „Buchhaltung → Ende" (Exportwert `book`); damit mehrfach täglich, erfüllt Katalog 5.1 | [K] |
| Inhalt | Buchungsvorschlag mit bis zu 16 Feldern (u. a. Belegfeld 1/2, Bruttobetrag, Konto, Gegenkonto, BU-Schlüssel, KOST1/KOST2, Leistungsdatum, Buchungstext, **Dokumentenlink**) (LDconnect Leistungsschein 11/2025) | [K] |
| Beleg | Beleglink; Anzeige aus DATEV über „Beleganzeige Drittanbieter". Belegbild in DATEV optional über DUO (S-03). | [K] |
| Stammdaten | Kreditoren, Sachkonten, Steuerschlüssel, Zahlungsbedingungen, Bankverbindungen, KOST1/KOST2 **täglich** aus DATEV (S-02) | [K] |
| Nicht übertragen | Fälligkeit, Skonto, Postensperre, IBAN sind nicht in der Feldliste; Verarbeitung des gekürzten Zahlbetrags mit Trios klären (OP-05) | [O] |
| Buchung | Der Buchungsvorschlag liegt in DATEV bereit; Trios übernimmt und bucht ihn (offener Posten entsteht). | Organisation |

**Fehlerfälle:**

| Fehler | Erkennung | Behandlung |
|---|---|---|
| Kreditor/Sachkonto in DATEV unbekannt | Rückmeldung Fehler an der Exportverbindung | Beleg geht in den Fehlerschritt; R-06 korrigiert und übergibt erneut. |
| Gateway/DATEVconnect nicht erreichbar | Exportfehler | automatische Wiederholung bzw. manuelle Neuübergabe; Monitoring durch MDIS Betrieb (R-15). |
| Geschäftsjahr abgeschlossen | LDconnect ordnet nach Rechnungsdatum zu, auch bei abgeschlossenem Jahr | Trios prüft Periodenzuordnung vor Übernahme. |
| Doppelte Übergabe | Beleg-ID/Belegfeld 1 bereits vorhanden | Trios verwirft Duplikat; Ursache im Workflowprotokoll prüfen. |

**Einstufig vs. zweistufig (AE-08, Entscheidung offen mit Trios/Livos):**

| Variante | Ablauf | Vorteile | Nachteile | Status |
|---|---|---|---|---|
| Einstufig (Empfehlung) | eine Übergabe nach Zahlungsfreigabe | LDconnect-Standard; keine ungesperrten zahlbaren Posten; einfacher Betrieb | offene/unverbuchte Rechnungen nicht in DATEV sichtbar → Transparenz über REB inkl. CSV-Export zum Monatsende (Rückstellungen) | [K] |
| Zweistufig (Folienbild) | Vorerfassung bei Verteilung mit Postensperre, Freigabe entsperrt | Periodengerechte Erfassung in DATEV | nicht LDconnect-Standard; Postensperre per EXTF/BeSync; Doppelverarbeitungsrisiko | [A] Option Phase 3 |

## 9.10 Zahlung und Rückmeldung

Der Zahlungsprozess folgt AE-10. d.velop liefert die Freigabe, DATEV und multicash führen die Zahlung aus.

| Nr. | Schritt | System | Verantwortlich | Status |
|---|---|---|---|---|
| 1 | Zahlungsfreigabe | smart invoice | R-05 | [K] |
| 2 | Buchungsvorschlag + Beleglink an DATEV | LDconnect (S-01) | automatisch | [K] |
| 3 | Buchung, offener Posten | DATEV | Trios | Organisation |
| 4 | Zahlungsvorschlag aus OPOS (Fälligkeit, Skonto) → DATEV Zahlungsverkehr → SEPA-XML | DATEV | Trios | [S] (DATEV) |
| 5 | Import der SEPA-Datei in multicash; Unterschrift nach Unterschriftsklassen; EBICS an Banken | multicash (S-07) | R-05 / Treasury | [S] (Omikron) |
| 6 | Kontoauszug zurück nach DATEV, OP-Ausgleich | multicash → DATEV | Trios | [S] |
| 7 | Rückmeldung „bezahlt": BeSync liest OPOS (DATEVconnect `accounts-payable`) je Mandant und setzt E-23 „Zahlstatus = bezahlt/teilbezahlt" und „Zahldatum" als DMS-Eigenschaft am archivierten Beleg | BeSync (S-06) | automatisch (täglich) | [A] |

Hinweis: smart-invoice-Belege sind nach Workflowende nicht per API änderbar. Der Zahlstatus wird daher als DMS-Eigenschaft geführt und ist in Suche, Akte und evidanza sichtbar, nicht als Workflowschritt. Katalog 5.5 = **A**.

## 9.11 Sonderfälle

Jeder Sonderfall ist mit Auslöser, Behandlung, Rolle und Belegstatus beschrieben.

### 9.11.1 Dublette (Doppeleingang Mail und Post)

| Merkmal | Inhalt |
|---|---|
| Auslöser | Lieferant sendet dieselbe Rechnung per E-Mail und per Post bzw. als PDF und E-Rechnung („kommt recht häufig vor", Workshop 22.09.2026, [00:38:42]). |
| Behandlung | Dublettenwarnung Stufe 1/2 → Klärfall. R-02 vergleicht mit dem Original (Link in der Warnung/REB-Suche). Echte Dublette: Ablehnen mit Grund „Dublette" **ohne Lieferantenmail**, Beleg bleibt als abgelehnter Vorgang archiviert und mit dem Original verknüpft. Keine Dublette: Warnung mit Pflichtbegründung akzeptieren (Protokoll). |
| Organisatorisch | Lieferantenanschreiben: Rechnungen nur noch elektronisch an die Rechnungsadresse. |
| Rolle | R-02 |
| Status | [S] (Prüfung, Begründungspflicht) / [K] (Ablehnungspfad ohne Mail) |

### 9.11.2 Rückweisung an den Lieferanten (WF-05, AE-13)

| Merkmal | Inhalt |
|---|---|
| Auslöser | Pflichtangaben fehlen, falscher Empfänger, Leistung nicht erbracht, Preis/Menge weicht ab, E-Rechnungsfehler. |
| Standardgründe (E-26, Vorschlag, Livos bestätigt) | (1) Pflichtangaben § 14 UStG fehlen/fehlerhaft · (2) falscher Rechnungsempfänger/Gesellschaft · (3) Leistung nicht/nicht vollständig erbracht bzw. Nachweise fehlen · (4) Preis/Menge weicht von Auftrag/Vertrag ab · (5) formaler E-Rechnungsfehler/Format nicht verarbeitbar |
| Behandlung | Aktion „An Lieferant zurückweisen" in Verteilung oder Sachlicher Prüfung; Pflichtfeld Rückweisungsgrund (Werteliste als Custom Entity) und optional Freitext; Bedingung `present?` an der Verbindung. Die Verbindung führt zum Ende „Zurückgewiesen" und löst einen Export an BeSync aus. BeSync wählt die Vorlage zum Grund, nimmt die Empfängeradresse aus dem Kreditorenstamm (`vendor.email`, Fallback Lieferanten-App), versendet aus einem Livos-Absenderpostfach über Microsoft Graph oder d.velop-Messaging-API (Festlegung in Phase 0, OP-25) und legt die gesendete Mail als K-07 Korrespondenz in der Kreditorenakte ab (S-11). Optional erzeugt BeSync zunächst einen Entwurf zur Freigabe durch den Bearbeiter („vorgefertigte Mail, die ich anpassen kann", [00:38:32]). |
| Übergangslösung | bis WF-05 produktiv ist: „Teilen per E-Mail/Link" manuell aus d.velop [S]. |
| Rolle | R-02, R-03 (M-06) |
| Status | [K] Ablehnung mit Grund / [A] automatische Lieferantenmail (smart invoice und process studio senden nicht an externe Adressen) |

### 9.11.3 Kürzung (AE-14)

| Merkmal | Inhalt |
|---|---|
| Auslöser | Leistung mangelhaft oder unvollständig, Menge oder Preis zu hoch (z. B. 8.000 € statt 10.000 € zahlen; 3 statt 4 Stunden). „Kommt relativ häufig vor" ([00:41:27]). |
| Grundsatz | **Die Rechnung wird nicht bearbeitet.** Das Rechnungsdokument bleibt unverändert (§ 146 Abs. 4 AO, GoBD; bei E-Rechnungen ist das XML das Original). Eine Bearbeitung des Rechnungsdokuments selbst (auch lokal) ist ausgeschlossen. |
| Behandlung | Kürzung als Workflow-Daten: Zahlbetrag `pay_amount` auf Kopf- oder Positionsebene; positionsweise über Menge/Preis mit automatischer Neuberechnung; Pflichtfeld Kürzungsgrund E-13 (Werteliste: Mengenabweichung · Preisabweichung · Mangel/Minderung · Einbehalt · Bauabzug 15 % · Skonto-/Nachlassdifferenz · Sonstiges mit Pflichtfreitext); Notiz und PDF-Annotation als Erläuterung. Die Verbindung „Weiter" verlangt den Kürzungsgrund, sobald Zahlbetrag ≠ Brutto. Nachweis über Historie, Workflowprotokoll und Belegänderungsansicht. |
| Lieferantenmitteilung | optional automatische Kürzungsmitteilung über WF-05 (gleiche Mechanik wie Rückweisung). |
| Abgrenzung | Ist die Rechnung formal oder steuerlich falsch (Betrag, Steuersatz), wird nicht gekürzt, sondern zurückgewiesen und eine berichtigte Rechnung angefordert. |
| Offen | Verarbeitung in DATEV: LDconnect überträgt den Bruttobetrag; wie Trios den gekürzten Zahlbetrag im OP/Zahlungsvorschlag abbildet und ob eine Vorsteuerkorrektur (§ 17 UStG) nötig ist, ist zu klären (OP-05). Schreibbarkeit von `pay_amount` in der Maske testen (OP-10). |
| Rolle | R-03 schlägt vor, R-04 bestätigt mit der Freigabe, R-06 bucht |
| Status | [K] |

### 9.11.4 Abschlags- und Schlussrechnung (kumuliert, Bau)

| Merkmal | Inhalt |
|---|---|
| Auslöser | Belegart Abschlagsrechnung oder Schlussrechnung nach VOB/B, meist kumuliert (Leistungsstand abzüglich bisheriger Abschläge und Einbehalte; Beispiel Testbeleg: 60.000 € kumuliert − 25.000 € 1. Abschlag − 3.500 € Einbehalt = 31.500 €). |
| Behandlung d.velop | Belegart setzen; Auftragsnummer E-19 und Vergabeeinheit E-18 zuordnen; Aktenbildung in die **Vorgangsakte K-13** (Auftrag + alle Abschläge + Schlussrechnung + Nachweise) – damit sind die Vorgänger-Abschläge und ihre akzeptierten Beträge in einer Sicht einsehbar (Workshop-Wunsch [00:44:49]). Prüfung und Rechenlogik in BIM4You (WF-02). |
| Automatische Prüfung | Die automatische Prüfung „kumulierter Leistungsstand gegen tatsächlich gezahlt" ([00:45:47]) leistet d.velop nicht. Sie erfolgt in BIM4You (Vertrag, Zahlungsplan) [A über S-08/S-09]; die tatsächlichen Zahlungen stehen in DATEV. |
| Schlussrechnung | § 14 Abs. 5 UStG: vereinnahmte Teilentgelte und Steuern sind abzusetzen; Prüfung in BIM4You, Kontrolle durch Trios. |
| Rolle | R-02 (Zuordnung), R-03/R-08 (Prüfung in BIM4You), R-04 |
| Status | [K] Kennzeichnung und Vorgangsakte / [A] Prüfung über BIM4You-Integration; Katalog 5.2 = N (d.velop) / A (über BIM4You) |

### 9.11.5 Sicherheitseinbehalt

| Merkmal | Inhalt |
|---|---|
| Auslöser | Vertrag sieht Sicherheits- oder Gewährleistungseinbehalt vor (VOB/B § 17: je Zahlung höchstens 10 % bis zur vereinbarten Sicherheitssumme). |
| Behandlung | BIM4You berechnet den Einbehalt je Abschlag. d.velop zeigt ihn als E-22 und reduziert den Zahlbetrag mit Kürzungsgrund „Einbehalt". Die Verwaltung über die Laufzeit (Summe je Auftrag, Rückgabe nach Abnahme/Gewährleistung) bleibt in BIM4You bzw. im DATEV-OP. |
| Rolle | R-03/R-08, R-06 |
| Status | [K] Erfassung / [A] Übernahme aus BIM4You |

### 9.11.6 Reverse Charge § 13b UStG

| Merkmal | Inhalt |
|---|---|
| Auslöser | Bauleistung an eine Livos-Gesellschaft, die selbst nachhaltig Bauleistungen erbringt; Rechnung ohne Umsatzsteuer mit Hinweis „Steuerschuldnerschaft des Leistungsempfängers". |
| Behandlung | Steuerschlüssel § 13b je Mandant; Kennzeichnung am Bau-Kreditor (`tax_category`), automatische Steuerschlüsselermittlung bei eindeutiger Übereinstimmung Kreditor × Sachkonto; E-20 = Ja. Plausibilitätsregel: Bau-Kreditor und Mandant § 13b-Schuldner, aber USt ≠ 0 → Hinweis/Klärfall; umgekehrt USt = 0 bei Nicht-Schuldner → Rückweisung Grund 1. Kennzeichen „Bauleistender § 13b" am Gesellschaftsstamm (AE-28). |
| Offen | Welche Gesellschaften § 13b-Schuldner sind und welcher DATEV-BU-Schlüssel gilt: mit Trios/Steuerberatung klären. |
| Rolle | R-02, R-06 |
| Status | [K] |

### 9.11.7 Freistellungsbescheinigung § 48b EStG fehlt oder ist abgelaufen (AE-15)

| Merkmal | Inhalt |
|---|---|
| Auslöser | Bauleistung ohne gültige Freistellungsbescheinigung (FSB) zum Zeitpunkt der Zahlung → Pflicht zum Steuerabzug 15 % (§ 48 EStG), außer Bagatellgrenzen (5.000 € bzw. 15.000 € je Leistendem und Jahr). |
| Behandlung | FSB liegt als K-06 in der Kreditorenakte mit „Gültig bis". BeSync führt eine FSB-Status-Tabelle (Kreditor × Gesellschaft × gültig bis, Nachweis der EIBE-Abfrage) in der Lieferanten-App. Bei Bau-Rechnungen prüft BeSync über einen Export an der Startverbindung den FSB-Status; fehlt eine gültige FSB, meldet BeSync einen Hinweis bzw. Klärfall „FSB fehlt/abgelaufen" mit Vorschlag Zahlbetrag = 85 % (Kürzungsgrund „Bauabzug 15 %"). Anmeldung und Abführung erfolgen in DATEV durch Trios. |
| Manuell | Die Prüfung beim Bundeszentralamt für Steuern erfolgt manuell im EIBE-Portal (Einzelabfrage, keine API). |
| Übergang | Bis Phase 3: DMS-Eigenschaft E-21 „FSB-Status" als Pflichtfeld in der Verteilung für Bau-Kreditoren [K]. |
| Rolle | R-02, R-12 (FSB pflegen), R-06 |
| Status | [A] (Katalog 2.7 = A, Could) |

### 9.11.8 Gutschrift und Storno

| Merkmal | Inhalt |
|---|---|
| Auslöser | Lieferantengutschrift, Stornorechnung oder Rechnungskorrektur des Lieferanten. |
| Behandlung | Belegart Gutschrift/Stornorechnung (E-14); Verweis auf die Ursprungsrechnung (Rechnungsnummer in Notiz/Custom-Feld). Kurzer Ablauf: Verteilung → Sachliche Prüfung (Bestätigung) → Buchhaltung; keine Zahlungsfreigabe. Umsetzung als eigener Pfad in WF-01 (Bedingung auf Belegart, Empfehlung) oder als separate Workflowdefinition „Gutschrift/Storno" (AE-04). Die ID WF-04 bleibt dem Klärfall vorbehalten. Ist die Ursprungsrechnung noch im Workflow, wird sie mit Verweis auf die Stornorechnung abgelehnt. |
| Rolle | R-02, R-03, R-06 |
| Status | [K] |

### 9.11.9 E-Rechnung formal fehlerhaft

| Merkmal | Inhalt |
|---|---|
| Auslöser | XRechnung-Validierung „Fail/Error", unzulässiges ZUGFeRD-Profil (MINIMUM/BASIC-WL), XML fehlt, XML und PDF widersprechen sich. |
| Behandlung | Keine Korrektur durch Livos. Rückweisung mit Grund 5 und Aufforderung zur **Neuausstellung als E-Rechnung** (WF-05). Der Prüfbericht liegt als Anlage am Beleg. Bei inhaltlichen Fehlern gilt Sonderfall 9.11.2; bei Leistungskürzung 9.11.3 (die E-Rechnung bleibt formal gültig). |
| Fristen | Bis 31.12.2026 dürfen Lieferanten noch Papier/PDF senden, 2027 eingeschränkt, ab 2028 ist die E-Rechnung Pflicht (§ 27 Abs. 38 UStG). |
| Rolle | R-02 |
| Status | [S] XRechnung-Validierung / [A] ZUGFeRD-Profilprüfung |

### 9.11.10 IBAN-Abweichung (Betrugsprävention)

| Merkmal | Inhalt |
|---|---|
| Auslöser | IBAN auf der Rechnung weicht von den Bankverbindungen des Kreditors (DATEV-Stamm) ab. Typisches Betrugsmuster (gefälschte Rechnung, geänderte Bankverbindung). |
| Behandlung | Die Bankverbindungen liegen im Bucket; Beleg- und Stamm-IBAN werden am Beleg geführt. Verhalten der Maske bei Abweichung testen (OP-10). Fallback: BeSync prüft über einen Export an der Startverbindung und leitet bei Abweichung in den Klärfall mit Meldung. Vorgehen im Klärfall: Rückruf beim Lieferanten über die **im Stamm hinterlegte** Telefonnummer, nicht über die Rechnung; Änderung der Bankverbindung nur durch Trios in DATEV nach Vier-Augen-Prüfung. Gezahlt wird immer auf die DATEV-Stammbankverbindung. |
| Rolle | R-02, R-06 |
| Status | [O] Standardwarnung / [A] Fallback |

### 9.11.11 Skonto-Priorisierung

| Merkmal | Inhalt |
|---|---|
| Auslöser | Rechnung mit Skonto (z. B. 2 % bei Zahlung binnen 7 Tagen). |
| Behandlung | Skontofälligkeit aus Zahlungsbedingung bzw. Beleg; Skontoampel und REB-Spalten Skontobetrag/Skontofälligkeit; Schnellzugriff „Skonto in den nächsten 5 Tagen"; dynamische Eskalation vor Skontoablauf (Kapitel 10.4). Zahlungsfreigabe und Übergabe müssen so früh erfolgen, dass Trios den Zahllauf vor Skontoablauf erreicht (Vorschlag: Übergabe spätestens 3 Arbeitstage vor Skontofrist). |
| Rolle | alle Workflowbeteiligten; Controlling R-07 |
| Status | [S] Anzeige/Ampel / [K] Eskalation |

### 9.11.12 Rechnung ohne Objekt oder Kostenstelle

| Merkmal | Inhalt |
|---|---|
| Auslöser | Rechnung ohne Objektbezug (Verwaltungskosten, Beratung, Gesellschaftskosten) oder Objekt nicht erkennbar. |
| Behandlung | Gesellschaftsbezogene Kostenstelle „Verwaltung" bzw. Standard-Kostenobjekt je Mandant; Sachlicher Prüfer aus Matrix auf Ebene Mandant (Zeile mit leerer Kostenstelle). Ist das Objekt unklar: Rückfrage an Objektbetreuung über die Verteilung; nach 2 Arbeitstagen Eskalation. Aktenbildung nur in Gesellschafts- und Kreditorenakte (keine Objektakte). |
| Rolle | R-02, R-03 |
| Status | [K] |

### 9.11.13 Rechnungen für PM-verwaltete Objekte

| Merkmal | Inhalt |
|---|---|
| Auslöser | Eine Rechnung geht bei Livos ein, das Objekt ist aber im Objektstamm als PM-verwaltet (E-30) gekennzeichnet. |
| Behandlung | (a) Rechnung liegt über dem Schwellwert und der PM bittet um Freigabe → WF-03 (Kapitel 11). (b) Reguläre PM-Rechnung → keine Bearbeitung in WF-01; Ablage „zur Kenntnis" in Objekt-/Gesellschaftsakte und Weiterleitung an das Rechnungspostfach des PM (Katalog 4.1, Kapitel 11.4). Ende ohne DATEV-Übergabe. |
| Rolle | R-02 |
| Status | [K] Erkennung/Pfad / [A] automatische Weiterleitung |

### 9.11.14 Übersicht

| Nr. | Sonderfall | Schritt | Rolle | Status |
|---|---|---|---|---|
| 9.11.1 | Dublette | Verteilung/Klärfall | R-02 | [S]/[K] |
| 9.11.2 | Rückweisung (WF-05) | Verteilung, Sachliche Prüfung | R-02, R-03 | [K]/[A] |
| 9.11.3 | Kürzung | Sachliche Prüfung | R-03 | [K] |
| 9.11.4 | Abschlag/Schluss kumuliert | WF-02 | R-03, R-08 | [K]/[A] |
| 9.11.5 | Sicherheitseinbehalt | WF-02 | R-03, R-06 | [K]/[A] |
| 9.11.6 | § 13b | Verteilung, Buchhaltung | R-02, R-06 | [K] |
| 9.11.7 | § 48b FSB | Start/Verteilung | R-02, R-12 | [A] |
| 9.11.8 | Gutschrift/Storno | Pfad in WF-01 | R-02, R-06 | [K] |
| 9.11.9 | E-Rechnung fehlerhaft | Verarbeitung/Verteilung | R-02 | [S]/[A] |
| 9.11.10 | IBAN-Abweichung | Verteilung/Klärfall | R-02, R-06 | [O]/[A] |
| 9.11.11 | Skonto | alle Schritte | alle | [S]/[K] |
| 9.11.12 | ohne Objekt/Kostenstelle | Verteilung | R-02, R-03 | [K] |
| 9.11.13 | PM-verwaltetes Objekt | Verteilung | R-02 | [K]/[A] |

## 9.12 Mengen- und Zeitannahmen

Die folgenden Werte sind **Annahmen** für Dimensionierung, Lizenz und Test. Livos bestätigt oder korrigiert sie im Prozess-Workshop (OP-17).

| Kennzahl | Annahme | Grundlage |
|---|---|---|
| Eingangsrechnungen gesamt | 20–30 je Arbeitstag, 5.000–8.000 je Jahr (≈ 420–670 je Monat) | Livos-Angabe (Katalog/Workshop) |
| Davon PM-Freigaben (WF-03) | Annahme 5–10 % (nur Rechnungen über Schwellwert von ~10 PM) | Workshop; zählt ins invoices-Volumen |
| Anteil Bau (WF-02) | Annahme 15–25 %, projektabhängig schwankend | Annahme MDIS; mit Livos klären |
| Anteil E-Rechnung | Annahme 2026: 20–30 %; 2027: > 50 %; ab 2028: Regelfall | Übergangsregeln § 27 Abs. 38 UStG |
| Anteil Papier/Scan | Annahme 2026: 20–30 %, danach stark sinkend | Annahme |
| Klärfälle (Mandant/Kreditor) | Annahme Start 10–15 %, nach Stammdatenbereinigung < 5 % | Annahme; Test mit echten Belegen (OP-02) |
| Dubletten | Annahme 2–5 % | Workshop „recht häufig" |
| Durchlaufzeit Ziel | Eingang bis Übergabe an DATEV ≤ 10 Arbeitstage; Skonto-Rechnungen ≤ 5 Arbeitstage | Vorschlag |
| Liegezeit je Schritt (Ziel) | Verteilung 1 AT, Sachliche Prüfung 3 AT, Freigabe je Stufe 2 AT, Zahlungsfreigabe 1 AT, Buchhaltung 1 AT | Vorschlag, Grundlage für Eskalation (Kapitel 10.4) |
| Positionen je Rechnung | Ø 1–10, einzelne Bau-Rechnungen bis 30 Seiten / 50 Positionen | Workshop [00:42:59]; smart-invoice-Grenze 500 Positionen |
| Lizenzpaket | d.velop invoices Medium (750 Rechnungen/Monat) reicht mit Reserve (AE-02) | d.velop invoices Leistungsbeschreibung 12/2025 |

# 10 Freigabe- und Workflowkonzept

Dieses Kapitel legt fest, wie Freigaben, Wertgrenzen, Vier-Augen-Prinzip, Eskalation, Vertretung, Benachrichtigungen und Status für alle Rechnungsworkflows funktionieren. Es setzt AE-04, AE-05, AE-06 und AE-17 um und beantwortet Katalog 1.4, 1.8, 3.1, 3.3 und 3.4.

Belegstatus: **[S]** Standard belegt · **[K]** Konfiguration · **[A]** Anpassung/Entwicklung (MDIS BeSync) · **[O]** offen/zu verifizieren.

## 10.1 Workflowarchitektur

### 10.1.1 Grundsatz

Alle Rechnungsworkflows laufen in **smart invoice**, der Workflow-Komponente von d.velop invoices (AE-04). process studio wird nur für Prozesse ohne Rechnungsbeleg genutzt (WF-06, WF-07, WF-09, WF-10). Beide Welten sind technisch getrennt; eine Kopplung erfolgt, wo nötig, über BeSync.

Gesellschaftsunterschiede werden **über Regeln, nicht über Kopien** abgebildet (P6): Es gibt eine Workflowdefinition je Prozesstyp, nicht je Gesellschaft. Die Gesellschaftslogik liegt in der Freigabematrix (Spalte Mandant), in Bedingungen auf `voucher.company.nr` und in Gruppen je Mandant.

### 10.1.2 Workflowdefinitionen

| ID | Workflowdefinition | Schritte (Kurzform) | Auslöser/Weiche | Phase |
|---|---|---|---|---|
| WF-01 | Standard-ER | Verteilung → Sachliche Prüfung & Kontierung → Fachliche Freigabe 1..n → Zahlungsfreigabe → Buchhaltung → Ende | Standard für alle ER | 1 |
| WF-02 | Bau-ER | wie WF-01 + Warten auf BIM4You (asynchroner Transfer) nach Sachlicher Prüfung | Objekt = Bauprojekt, Belegart Abschlag/Schluss, Kreditor Bauleistender | 3 (Pilot ohne Automatik in 1) |
| WF-03 | PM-Freigabe | Verteilung → Freigabe Asset Management → Ende „Freigegeben"/„Abgelehnt" | Importprofil PM-Postfach | 2 |
| WF-04 | Klärfall | als Schritt/Clearing in WF-01 bis WF-03 | Mandant unbekannt, Kreditor fehlt, Dublette | 1 |
| (optional) | Gutschrift/Storno | Verteilung → Prüfung → Buchhaltung | Belegart Gutschrift/Storno; Empfehlung: Pfad in WF-01 | 1 |
| (Test) | Kopien für Test-Tenant | – | – | 0 |

### 10.1.3 Plattformgrenzen

| Grenze | Wert | Konsequenz für Livos | Quelle |
|---|---|---|---|
| Workflowdefinitionen | max. 100 je Bucket | ein Workflow je Gesellschaft (> 100) ist ausgeschlossen → P6 | d.velop invoices Leistungsbeschreibung 12/2025 |
| Schritte je Workflow | max. 50 | ausreichend (WF-02 ca. 10–12 Schritte) | dto. |
| Mandanten | max. 1.000 je Bucket | ausreichend für > 100 Gesellschaften | dto. |
| Gruppen | max. 2.500 | Gruppen je Mandant und Rolle (z. B. `SI_Freigeber_<MandantNr>`) bleiben im Rahmen | dto. |
| Prüfungsschritt | nur **ein** erweiterter Prüfungsschritt je Workflow | mehrstufige Fachprüfung über Prüfungstypen in diesem Schritt | smart invoice Cloud Handbuch 06/2026 |
| Freigabematrix | feste Spalten Bearbeiter und Freigabegrenze + bis zu 20 Zusatzspalten; Auswertung case-sensitive | Stammdatendisziplin bei Mandanten-ID und Kostenstellen | dto. |
| Beträge in Bedingungen | in Cent (10.000,00 € = `1000000`) | Konfigurationsfehlerquelle, Vier-Augen-Test in der Abnahme | dto. |
| Verbindungsauswertung | top-down, erste zutreffende Bedingung gewinnt | Wertgrenzen-Verbindungen über der Standardverbindung anordnen | dto. |

### 10.1.4 Konfigurationsprinzipien

| Nr. | Prinzip |
|---|---|
| 1 | Schrittnamen sind fachlich und einheitlich (Verteilung, Sachliche Prüfung, Fachliche Freigabe Stufe 1/2/3, Zahlungsfreigabe, Buchhaltung). Sie erscheinen im REB als „Aktueller Schritt" und ersetzen ein eigenes Statusfeld (10.7). |
| 2 | Bearbeiterfindung über Gruppen oder Matrix, nie über Einzelpersonen im Workflow. Personen stehen in Gruppen und Matrixzeilen. |
| 3 | Jeder Freigabeschritt hat Bestätigen und Ablehnen; Ablehnen verlangt einen Kommentar. |
| 4 | Jede automatische Weiche hat einen Klärfall-Ausgang (P7). |
| 5 | Änderungen an Workflows erfolgen zuerst im Test-Tenant, dann per Transport/Nachbau im Produktiv-Tenant mit Änderungsprotokoll (Kapitel 18). |

## 10.2 Freigabematrix

### 10.2.1 Aufbau

Die Freigabematrix bestimmt je Beleg und Kostenobjekt, wer freigibt (AE-05). smart invoice bietet feste Spalten (Bearbeiter, Freigabegrenze) und bis zu 20 Zusatzspalten mit Platzhaltern (`*` Präfix, leer = alle, `$` = muss leer sein) (smart invoice Cloud Handbuch 06/2026).

| Spalte | Typ | Inhalt | Beispielwert |
|---|---|---|---|
| Mandant | Zusatzspalte | Mandanten-ID (= DATEV-Mandantennummer, AE-03) | `10010` |
| Kostenstelle / Objekt | Zusatzspalte | KOST1 bzw. Objekt-ID; leer = alle Kostenobjekte des Mandanten | `HH-HAF22` |
| Kostenträger | Zusatzspalte (optional) | KOST2 / Projekt | leer |
| Rang / Stufe | Zusatzspalte „Rang" (0–99) | Freigabestufe für Strategie „Von unten zum Freigeber" | `1` |
| Bearbeiter | fest | Person oder Gruppe | `SI_Freigeber_10010` |
| Freigabegrenze | fest | Betragsgrenze je Kostenobjekt (netto, AE-05) | `5.000,00` |

**Strategie:** „Von unten zum Freigeber" – smart invoice sammelt Freigaben aufsteigend nach Rang, bis ein Freigeber mit ausreichender Grenze erreicht ist [S]. Alternativ „Direkt" (nur der Freigeber mit passender Grenze).

**Bezugsgröße:** netto (Standardbedingung `voucher.net_amount`); Livos bestätigt die Bemessung (AE-05, ED-05).

### 10.2.2 Beispielmatrix

**Alle Grenzen und Gesellschaften in dieser Tabelle sind Beispiele.** Die Gesellschaften NORD, SUED, BAUP sind fiktive Demo-Gesellschaften. Livos definiert die tatsächlichen Grenzen und Personenketten im Prozess-Workshop (OP-17).

| Mandant | Kostenstelle/Objekt | Rang | Bearbeiter (Gruppe) | Freigabegrenze netto (Beispiel) | Bedeutung (Beispiel) |
|---|---|---|---|---|---|
| NORD | `*` (alle) | 1 | Asset Manager NORD | bis 5.000 € | eine Freigabe bis 5.000 € |
| NORD | `*` | 2 | Leitung Asset Management | bis 25.000 € | zweite Stufe 5.000–25.000 € |
| NORD | `*` | 3 | Geschäftsführung NORD | unbegrenzt | über 25.000 € GF |
| SUED | `*` | 1 | Asset Manager SUED | bis 5.000 € | wie NORD |
| SUED | `*` | 2 | Leitung Asset Management | bis 25.000 € | wie NORD |
| SUED | `*` | 3 | Geschäftsführung SUED | unbegrenzt | wie NORD |
| BAUP | `*` | 1 | Projektleitung Bau | bis 10.000 € | Bau mit höherer 1. Stufe (Beispiel) |
| BAUP | `*` | 2 | Leitung Projektentwicklung | bis 50.000 € | |
| BAUP | `*` | 3 | Geschäftsführung BAUP | unbegrenzt | |
| NORD | `VERW` (Verwaltung) | 1 | Kaufmännische Leitung | bis 25.000 € | abweichende Kette für Verwaltungskosten |

**Pflegeaufwand:** Bei > 100 Gesellschaften mit je 3 Stufen entstehen mehrere hundert Zeilen. Empfehlungen:

| Maßnahme | Wirkung |
|---|---|
| Gruppen statt Personen in der Spalte Bearbeiter | Personalwechsel ändert Gruppen in Entra ID, nicht die Matrix. |
| Gesellschaftsverbünde über Präfix-Platzhalter (`*`), wenn Mandanten-IDs verbundweise nummeriert sind | eine Zeile für mehrere Gesellschaften [K] |
| Pflege durch Fachadministration R-12 in M-17; Export/Import über API | Massenpflege, Nachweis der Änderungen |
| Jährliche Rezertifizierung der Matrix durch Controlling | Governance |

### 10.2.3 Wertgrenzen je Kostenobjekt

Die Freigabegrenze gilt **je Kostenobjekt** (Mandant + Kostenstelle + Kostenträger), nicht je Rechnung (smart invoice Cloud Handbuch 06/2026). Beispiel aus der Dokumentation: Eine Rechnung über 25.000 € aufgeteilt in 17.000 € (Kostenstelle A) und 8.000 € (Kostenstelle B) wird je Kostenobjekt gegen die Grenzen geprüft.

**Folge:** Eine Rechnung über der Gesamtgrenze kann durch Aufteilung auf Kostenobjekte mit Teilfreigaben unterhalb der Grenze laufen. Gegenmaßnahme: zusätzliche Wertgrenzen-Verbindung auf den **Rechnungsnettobetrag** (10.2.5), die unabhängig von der Aufteilung ab Betrag X eine Stufe erzwingt.

### 10.2.4 Personenketten

| Kette (Beispiel) | Anwendung |
|---|---|
| Asset Manager → Leitung AM → GF | Bestand/Privatisierung, objektbezogene Kosten |
| Projektleitung → Leitung Projektentwicklung → GF | Bau (nach BIM4You-Prüfung) |
| Kaufmännische Leitung → GF | Verwaltungs- und Gesellschaftskosten |
| Asset Management (WF-03) | PM-Freigaben (Kapitel 11) |

### 10.2.5 Bedingungen in Cent und top-down-Auswertung

Wertgrenzen-Verbindungen sind der Standardweg für betragsabhängige Zusatzstufen [K] (AE-05). Beispiel (Grenzen als Beispiel):

| Reihenfolge | Verbindung aus „Fachliche Freigabe Stufe 1" | Bedingung | Ziel |
|---|---|---|---|
| 1 | > 25.000 € netto | `voucher.net_amount > 2500000` | Freigabe GF |
| 2 | > 5.000 € netto | `voucher.net_amount > 500000` | Freigabe Stufe 2 |
| 3 | Standard | – | Zahlungsfreigabe |

Regeln: Beträge in Cent; die spezifischste (höchste) Grenze steht oben, weil die erste zutreffende Verbindung gewinnt; „Freigabe: Erteilen" an der Verbindung setzen; Test jeder Grenze mit Beträgen knapp darunter/darüber in der Abnahme.

## 10.3 Vier-Augen-Prinzip

| Aspekt | Festlegung | Status |
|---|---|---|
| Prüfer ≠ Freigeber | Sachliche Prüfung und fachliche Freigabe desselben Belegs erfolgen durch verschiedene Personen. In der Leistungsbeschreibung als Standard enthalten (alle Betriebsformen). | [S] (d.velop invoices Leistungsbeschreibung 12/2025) |
| Zweite Freigabe ab Betrag X | über Wertgrenzen-Verbindung (10.2.5) oder Matrix-Strategie „Von unten zum Freigeber" | [K] |
| Vorschau-Feature „Vier-Augen-Prinzip in der Freigabe" | erzwingt ab Betrag (Handbuch-Beispiel 10.000 €) eine zweite Freigabe je Kostenobjekt; sachliche Prüfer werden als Freigeber ausgeschlossen; Minimalbetrag konfigurierbar. Aktivierung nur über d.velop-Support, Status Vorschau (smart invoice Cloud Handbuch 06/2026). | [O] (OP-09) – nur nach d.velop-Freigabe nutzen |
| Freigeber ≠ Zahlungsfreigeber | Vorschlag: Zahlungsfreigabe durch eine andere Person als die letzte fachliche Freigabe | [K] (Bedingung/Gruppentrennung, Test T41) |
| Zahlungsausführung | Unterschrift in multicash nach Unterschriftsklassen (Vier-Augen) | [S] (Omikron) |
| Selbstfreigabe | Einreicher/Prüfer in Freigabegruppe: Ausschluss über Prüfer ≠ Freigeber; zusätzlich Gruppenbildung ohne Überschneidung für kritische Stufen | [K] |
| Freigabe überspringen | Die Standardaktion „Freigabe überspringen" und „Automatisch Freigaben für Prüfer erzeugen" werden **nicht** aktiviert. | [K] |

## 10.4 Eskalation

smart invoice bietet Eskalation im Standard (smart invoice Cloud Handbuch 06/2026; AE-17): statische Frist je Schritt („fixe Tage nach Erhalt der Aufgabe"), dynamische Frist („Tage vor Skonto-/Nettofälligkeit"), globale 1. Stufe, schrittspezifische 1. Stufe (ersetzt die globale) und globale 2. Stufe. Empfänger werden per Bearbeiterfindung bestimmt, auch mandantenabhängig. Arbeitstage zählen das Wochenende nicht, Feiertage schon.

### 10.4.1 Fristen-Vorschlag

**Alle Fristen sind Vorschläge**; Livos bestätigt sie im Prozess-Workshop. Die Fristen gelten einheitlich für alle Gesellschaften (P6).

| Schritt | 1. Stufe (statisch, Arbeitstage) | Empfänger 1. Stufe | 2. Stufe (global) | Empfänger 2. Stufe |
|---|---|---|---|---|
| Verteilung / Klärfall | 2 AT | Leitung Kreditorenbuchhaltung Livos | 4 AT | Leitung Finanzen |
| Sachliche Prüfung | 3 AT | Vorgesetzte/Teamleitung des Prüfers (Gruppe je Mandant) | 6 AT | Leitung Asset Management bzw. Projektentwicklung |
| Fachliche Freigabe (je Stufe) | 3 AT | nächsthöhere Freigabestufe des Mandanten | 6 AT | Geschäftsführung des Mandanten |
| Zahlungsfreigabe | 1 AT | Stellvertretung Zahlungsfreigabe | 2 AT | Leitung Finanzen/Treasury |
| Buchhaltung (Trios) | 2 AT | Teamleitung Trios | 4 AT | Leitung Finanzen Livos |
| Warten auf BIM4You (WF-02) | Transferfenster (Vorschlag 14 Tage), danach Fehlerschritt | R-02 | – | – |

**Dynamische Eskalation (Vorschlag):** 3 Tage vor Skontofälligkeit bzw. 5 Tage vor Nettofälligkeit an den aktuellen Bearbeiter und die Leitung Kreditorenbuchhaltung. Bei Skontofrist oder Nettofrist 0/leer erfolgt keine dynamische Eskalation.

### 10.4.2 Empfänger je Mandant

Die Bearbeiterfindung der Eskalation nutzt die Mandanten-ID, z. B. Regex auf Gruppennamen `/^SI_Eskalation_#{voucher.company.nr}$/` (Syntax belegt im smart invoice Cloud Handbuch 06/2026) [K]. Für jede Gesellschaft bzw. jeden Verbund existiert eine Eskalationsgruppe; Pflege über Entra ID (AE-18).

### 10.4.3 Wirkung und Grenzen

| Thema | Festlegung | Status |
|---|---|---|
| Sichtbarkeit | REB-Schnellzugriff „An mich eskalierte Rechnungen" mit Eskalationsstufe; Statusspalte zeigt Stufe 1/2 und Zeitpunkt | [S] (Helpcenter 09/2026) |
| Benachrichtigungskanal | ob die Eskalation zusätzlich per E-Mail zugestellt wird, ist nicht dokumentiert → im Test-Tenant prüfen | [O] (OP-10) |
| Umleitung | Eskalation benachrichtigt, sie weist die Aufgabe nicht automatisch neu zu. Der Eskalationsempfänger klärt mit dem Bearbeiter oder leitet über Vertretung/Weiterleitung um. | [S] (Einschränkung) |
| Unterschiedliche Fristen je Gesellschaft | nur über getrennte Workflowdefinitionen → nicht vorgesehen | – |
| Feiertage | werden nicht berücksichtigt; Fristen entsprechend großzügig setzen | [S] (Einschränkung) |

## 10.5 Vertretung

| Aspekt | Festlegung | Status |
|---|---|---|
| Geplante Abwesenheit | Benutzer setzt Abwesenheit im Profil (Start, Ende, Vertretung, Nachricht) (M-18) | [S] |
| Ungeplante Abwesenheit | **Administrator oder Vorgesetzte mit administrativer Berechtigung setzen die Abwesenheit für den erkrankten Kollegen** (Workshop-Frage [01:05:21]) | [S] (userprofile Handbuch) |
| Gesammelte Weiterleitung | berechtigte Personen leiten offene Aufgaben gesammelt weiter | [S] |
| REB-Sicht | Schnellzugriff „Rechnungen in Vertretung" | [S] |
| Einschränkung smart invoice | Die Vertretung sieht nur Aufgaben, die dem Abwesenden **persönlich** zugestellt wurden, nicht Gruppenaufgaben (die sehen ohnehin alle Gruppenmitglieder) (smart invoice Cloud Handbuch 06/2026) | [S] (Einschränkung) |
| Konsequenz Modell | Freigabe-Aufgaben möglichst an Personen (Matrixzeile mit Person) oder an Gruppen mit mindestens zwei Mitgliedern; keine Ein-Personen-Gruppen | [K] |
| Berechtigung | Vertretung übernimmt die Berechtigungen; beim Öffnen wird der Vertreter Workflowbeteiligter und erhält Leserecht auf den Beleg | [S] |
| Governance | Vertretungen möglichst innerhalb derselben Gesellschaftsgruppe; Vertretung für Freigaben nur durch Personen mit mindestens gleicher Freigabestufe; keine Vertretung Prüfer ↔ Freigeber desselben Vorgangs; Vertretungsausschluss für sensible Kontexte konfigurierbar | [K] |
| Nachweis | Vertretungshandlungen sind im Workflowprotokoll mit handelndem Benutzer dokumentiert | [S] |

## 10.6 Benachrichtigungen

| Kanal | Inhalt | Steuerung | Status |
|---|---|---|---|
| Aufgabenliste / „Meine Aufgaben" | neue Aufgaben, Rückfragen, Eskalationen | immer aktiv; Startseiten-Widget je Rolle (M-10) | [S] |
| REB-Schnellzugriffe | Meine offenen Rechnungen, In Vertretung, An mich eskaliert, eigene Filter (z. B. „Skonto in 5 Tagen") mit Counter-Badges und „ungelesen" | je Benutzer/Rolle | [S] |
| E-Mail-Benachrichtigung | Hinweis auf neue Aufgaben | **abschaltbar**; Livos-Wunsch, nur über die Aufgabenliste zu arbeiten ([00:26:27]) | [S] |
| Fälligkeitsampel | grün/gelb/rot nach Restzeit bis Nettofälligkeit; in der Demo eingestellt auf **gelb ab 10 Tagen, rot ab 5 Tagen** vor Nettofälligkeit (Workshop [01:03:34]) – Übernahme als Vorschlag | [S]/[K] |
| Skontoampel | gelb/rot/dunkelrot nach Skontofälligkeit | [S] |
| Eskalationsbenachrichtigung | siehe 10.4 | [S]/[O] Kanal |
| Lieferanten-/PM-Mails | Rückweisung, Kürzung, PM-Freigabe über BeSync (S-11) | [A] |

Empfehlung: E-Mail-Benachrichtigung standardmäßig **aus** für Rollen mit täglicher Arbeit im System (R-02, R-06), **an** für seltene Freigeber (R-04 GF, R-05) und Externe (R-08), damit Aufgaben nicht übersehen werden.

## 10.7 Statusmodell der Rechnung

smart invoice kennt kein frei definierbares Statusfeld; der Status ergibt sich aus dem aktuellen Schritt, dem Workflowzustand und Sonderzuständen (AE-29, E-24). Die vollständige Werteliste der DMS-Eigenschaft „Workflowstatus" ist nicht veröffentlicht (OP-26). Das Livos-Statusmodell wird deshalb aus Schrittnamen und Endverbindungen abgeleitet [K]; „Bezahlt" kommt über BeSync [A].

| Status (fachlich) | Bedeutung | Technische Grundlage / Schritt | Sichtbar im REB | Status |
|---|---|---|---|---|
| Eingegangen / in Erkennung | Beleg importiert, Erkennung läuft | inbound/document reader, Stapel | nein (Stapelübersicht M-01) | [S] |
| Workflowstart fehlgeschlagen | Übergabe an smart invoice gescheitert | Phase „Workflowstart ist fehlgeschlagen" | ja (Administration) | [S] |
| In Verteilung | Vorqualifikation durch Rechnungseingang | Schritt Verteilung | ja, Aktueller Schritt | [K] |
| Klärfall | Mandant unbekannt, Kreditor fehlt, Dublette | Schritt Klärfall / Standardmandant „Klärfall" | ja | [K] |
| Clearing | Korrektur nach falscher Zuordnung | Clearing-Modus | ja, Spalte Status „Clearing Modus" | [S] |
| In sachlicher Prüfung | Prüfung und Kontierung durch Fachbereich | Schritt Sachliche Prüfung | ja | [K] |
| Transfer / Warten auf BIM4You | Bau-Prüfung in BIM4You läuft | Phase „aktiver Belegdatentransfer" | ja, als Transferzustand | [S] Mechanik / [A] |
| In Freigabe Stufe n | fachliche Freigabe gemäß Matrix | Schritt Fachliche Freigabe Stufe n | ja | [K] |
| Eskaliert Stufe 1/2 | Frist überschritten | Eskalation | ja, Status + Schnellzugriff | [S] |
| In Zahlungsfreigabe | finanzielle Freigabe | Schritt Zahlungsfreigabe | ja | [K] |
| In Buchhaltung | Kontrolle und Übergabe durch Trios | Schritt Buchhaltung | ja | [K] |
| Übergabefehler | Export an LDconnect fehlgeschlagen | Fehlerschritt | ja | [S] |
| Übergeben an DATEV | Buchungsvorschlag in DATEV; Workflow beendet | Ende „Übergeben" (`end_mode = finished`) | ja, Archiv (6/12 Monate) | [K] |
| Zurückgewiesen | Rückweisung an Lieferant oder Dublette | Ende „Zurückgewiesen" (`aborted` bzw. eigener Endschritt) | ja, Archiv | [K] |
| Freigegeben / Abgelehnt (PM) | Ergebnis WF-03 | Ende WF-03 | ja, Archiv | [K] |
| Bezahlt / teilbezahlt | Zahlung in DATEV-OPOS ausgeglichen | DMS-Eigenschaft E-23 über BeSync (S-06) | nicht im REB (abgeschlossener Beleg); in Suche, Akte, evidanza | [A] |

## 10.8 Übersteuerung und Protokollierung

Katalog 1.8 verlangt händische Übersteuerung mit Nachvollziehbarkeit. Jede Automatik hat einen manuellen Eingriff mit Protokoll (P7).

| Übersteuerung | Wer | Wie | Protokoll | Status |
|---|---|---|---|---|
| Erkannte Werte ändern (Mandant, Kreditor, Beträge, Daten) | R-02 | Verteilungsmaske | Belegänderungsansicht (Vergleich zweier Schritte, farbig), Workflowprotokoll | [S] |
| Kontierung ändern | R-03, R-06 | Positionen; Buchhaltung „schreibbar wenn geprüft" | Workflowprotokoll | [S] |
| Zahlbetrag / Kürzung | R-03 | `pay_amount` + Kürzungsgrund | Protokoll, Notiz, Belegänderungsansicht | [K] |
| Dublettenwarnung übergehen | R-02 | Akzeptieren mit Pflichtbegründung | Workflowprotokoll | [S] |
| Fälligkeit/Zahlungsziel übersteuern | R-02 | manuelles Zahlungsziel | Protokoll | [S] |
| Sachlichen Prüfer oder Freigeber ändern | R-02 / Clearing-Gruppe | Verteilung bzw. Clearing | Protokoll | [S] |
| Fehlzuordnung korrigieren | Clearing-Gruppe je Mandant | Clearing-Modus, alle Felder beschreibbar | Protokoll | [S] |
| Workflow abbrechen | Administration/Clearing | Abbruch mit Grund | `end_mode = aborted`, Protokoll | [S] |
| Freigabematrix, Gruppen, Fristen ändern | R-12 | Administration (M-17) | Änderungsnachweis außerhalb smart invoice (Ticket/Änderungsprotokoll) | [K] |

**Revisionsnachweis:** Jede Rechnung erhält das Dokument „Workflowprotokoll ERV" im DMS mit Eigenschaften und Bearbeitungsschritten [S]. Die Historie im REB zeigt Weg, Kommentare und Notizen auch für abgeschlossene Vorgänge [S]. Historische Durchlauf- und Liegezeiten je Benutzer und Schritt protokolliert BeSync für evidanza (AE-16, S-12) [A], weil die Aufgabenhistorie der Plattform nur 30–365 Tage gehalten wird.

# 11 Property-Manager-Freigabe und weitere Freigabeprozesse

Dieses Kapitel beschreibt den Freigabeprozess für Rechnungen der Property Manager (WF-03, AE-12), den Umgang mit PM-Rechnungen, die bei Livos eingehen, externe Freigaben (AE-26, WF-10) und den Ausblick auf Freigaben ohne Rechnung (WF-09). Es beantwortet Katalog 4.1, 4.2 und 4.3.

Belegstatus: **[S]** Standard belegt · **[K]** Konfiguration · **[A]** Anpassung/Entwicklung (MDIS BeSync) · **[O]** offen/zu verifizieren.

## 11.1 Ausgangslage Property Manager

| Merkmal | Befund | Quelle |
|---|---|---|
| Anzahl | ca. 10 Property Manager (Hausverwaltungen), die wechseln können | Workshop 22.09.2026 [00:13:02] |
| Eigenständigkeit | ca. 95 % der Rechnungen für PM-verwaltete Objekte werden beim PM geprüft, freigegeben, gebucht und bezahlt | [00:15:18] |
| Schwellwert | Rechnungen über einem Schwellwert brauchen die Freigabe durch das Livos Asset Management | [00:20:45] |
| Buchhaltungsdaten | PM buchen in eigenen Systemen; Buchungsdaten kommen im Monatspaket (DATEV-Format) über Trios nach DATEV; Kreditoren der PM im 80000er-Kreis, ohne Konsolidierung mit dem 70000er-Kreis | [00:16:17], [00:17:34], [00:21:57] |
| Randbedingung | PM dürfen **nicht** zur Nutzung eines Livos-Erfassungssystems verpflichtet werden (K.-o.-Randbedingung) | [00:13:02–00:13:16] |
| Livos-Erwartung | Transparenz („wo hängt die Rechnung"), Vollständigkeit, Einsicht durch Vertreter; von Livos als „kleines On-Top" bewertet | [00:22:41–00:22:52] |
| Katalog | 4.1 Prozessunabhängigkeit PM (Must) – bewertet **K/A** | Kapitel 4.2 |

Heute laufen die Freigabeanfragen der PM per E-Mail an einzelne Personen im Asset Management. Es gibt keinen zentralen Nachweis, keine Vertretung und keine Vollständigkeitskontrolle.

## 11.2 Zielprozess WF-03 (PM-Freigabe)

### 11.2.1 Grundidee

Der PM sendet die Freigabeanfrage wie bisher per E-Mail, aber an ein zentrales Livos-Postfach. d.velop führt die Freigabe als eigenen smart-invoice-Workflow **ohne Buchung und ohne Zahlung** durch und meldet das Ergebnis per E-Mail an den PM zurück (AE-12). Der PM braucht kein Konto und keine Lizenz (R-09).

### 11.2.2 Ablauf

| Nr. | Schritt | System | Rolle | Beschreibung | Status |
|---|---|---|---|---|---|
| 1 | Eingang | M365 → email import | R-09 (PM) | PM sendet Rechnung (PDF oder E-Rechnung) mit Begleittext an `freigabe-hv@…` (Alias am Rechnungspostfach, eigenes Importprofil, E-25 = PM-Freigabe). Absenderadresse wird als Rückmeldeadresse gespeichert. | [S]/[K] |
| 2 | Erkennung | document reader | System | Mandant, Kreditor (PM-Sicht, soweit vorhanden), Beträge, Rechnungsnummer | [S] |
| 3 | Verteilung | smart invoice (WF-03) | R-02 | Objekt-ID, Gesellschaft und PM zuordnen (E-03, E-01, E-30); Plausibilität Schwellwert; Freigeber aus Matrix. Kreditor ist keine Pflicht (Buchung erfolgt beim PM). | [K] |
| 4 | Freigabe Asset Management | smart invoice (M-13) | R-04 (Asset Management) | Freigeben oder Ablehnen mit Pflichtbegründung; Rückfrage an R-02. Freigabematrix wie Kapitel 10 (Spalten Mandant/Objekt, Grenze); bei hohen Beträgen zweite Stufe (Beispiel: > 25.000 € netto Leitung AM – Grenze als Beispiel). | [K] |
| 5a | Ende „Freigegeben" | smart invoice → BeSync | System | Export an der Endverbindung; BeSync sendet Freigabe-Mail (Vorlage mit Rechnungsnummer, Objekt, Betrag, Freigeber, Datum) an die PM-Adresse, optional mit Link auf den Beleg (Teilen-Link) (S-11). Gesendete Mail als K-07 in der Objektakte. | [A] |
| 5b | Ende „Abgelehnt" | smart invoice → BeSync | System | wie 5a mit Ablehnungsbegründung | [A] |
| 6 | Buchung und Zahlung | PM-System | R-09 | PM bucht und zahlt wie bisher in seinem System. **Keine DATEV-Übergabe, keine Zahlungsfreigabe in d.velop.** | – |

### 11.2.3 Regeln

| Regel | Festlegung |
|---|---|
| Keine Buchung | WF-03 hat keinen Schritt Buchhaltung und keinen Export an LDconnect. Damit ist eine Doppelbuchung (PM-Monatspaket + d.velop) ausgeschlossen (P4). |
| Nachweis im Archiv | Rechnung, Workflowprotokoll ERV und Freigabe-Mail liegen revisionssicher in d.velop (Kategorien K-01 mit E-25 = PM-Freigabe, K-07). Aktenbildung in Objekt- und Gesellschaftsakte. Aufbewahrung: Die Rechnung ist bei Livos kein Buchungsbeleg; Frist als Geschäftsunterlage mit Steuerberatung festlegen (Kapitel 17.2, OP-46). |
| Transparenz | REB-Schnellzugriff „PM-Freigaben offen" (Filter Workflow WF-03) mit Spalten Objekt, PM, Betrag, Aktueller Schritt seit, Zugewiesen [S]. |
| Vollständigkeit | Jede Freigabeanfrage ist ein Vorgang mit Status; Abgleich mit PM-Buchungsdaten optional (11.3). |
| Vertreter-Einsicht | Vertretung und Eskalation wie Kapitel 10 (Vorschlag: Freigabe 3 AT, Eskalation an Leitung Asset Management). Workshop-Wunsch „der Vertreter kann reingucken" [00:22:49] ist damit erfüllt [S]. |
| Rückfragen an PM | manuell per Antwort-E-Mail oder „Teilen per E-Mail/Link" aus d.velop [S]; eine automatisierte Rückfrage mit Antwortformular ist über WF-10 möglich (11.5) [A]. |
| Volumen | PM-Freigaben zählen ins Rechnungsvolumen von d.velop invoices (Paket Medium, AE-02). |
| Schwellwert | Der Schwellwert je PM/Objekt steht im Verwaltervertrag; Livos definiert ihn (OP-17). d.velop prüft ihn nur als Plausibilität (Hinweis bei Beträgen unter Schwellwert). |
| Scope-Entscheidung | Livos bewertet WF-03 als „On-Top". Einführung in Phase 2 nach Stabilisierung WF-01 (P8). |

### 11.2.4 Kommunikation an die PM

| Maßnahme | Inhalt |
|---|---|
| Rundschreiben an die PM | neue Adresse `freigabe-hv@…`; eine Rechnung je E-Mail; Objektbezeichnung und Livos-Gesellschaft im Betreff; Rückmeldung erfolgt per E-Mail |
| Verwaltervertrag (perspektivisch) | Freigabeweg, Schwellwert, Lieferung der Buchungsdaten im DATEV-Format monatlich (S-16) |

## 11.3 Optionale Vollständigkeitskontrolle über PM-Buchungsdaten

Die PM liefern ihre Buchungsdaten ohnehin monatlich im DATEV-Format. Diese Daten können zusätzlich zwei Kontrollen speisen (S-16, Phase 3, optional) [A]:

| Kontrolle | Inhalt | Ergebnis |
|---|---|---|
| Vollständigkeit | BeSync liest den Buchungsstapel je Objektgesellschaft und gleicht gebuchte Rechnungen über dem Schwellwert gegen WF-03-Freigaben ab (Kreditor, Rechnungsnummer, Betrag). | Liste „gebucht ohne Freigabe" für das Asset Management in evidanza |
| Kreditorenmapping | BeSync ordnet die HV-Kreditoren (80000er-Kreis) über die Lieferanten-App einer Lieferanten-Konsolidierungsnummer zu (AE-09). | gesellschafts- und verwalterübergreifende Lieferantensicht (Workshop-Wunsch [00:16:49]) |

| Aspekt | Festlegung |
|---|---|
| Eingang | Upload/Postfach durch Trios oder PM; Parser in BeSync (Buchungsstapel Datenkategorie 21, Kreditoren Kategorie 16) |
| Pflege durch Livos | keine technischen Tabellen; fachliche Zuordnung nur in der Lieferanten-App (P3) |
| Voraussetzung | Format der PM-Lieferungen klären (OP-29) |
| Abgrenzung | Direkte Anbindungen einzelner PM-Systeme (Aareon, DOMUS, iX-Haus u. a.) sind Folgeprojekt (Katalog 5.4, S-17). |

## 11.4 Rechnungen für PM-verwaltete Objekte, die bei Livos eingehen

Lieferanten senden Rechnungen für PM-verwaltete Objekte teilweise an Livos statt an den PM. Katalog 4.1 verlangt, dass diese Rechnungen den PM erreichen, ohne dass Livos sie bearbeitet.

| Nr. | Schritt | Beschreibung | Status |
|---|---|---|---|
| 1 | Erkennung | Rechnung kommt über den normalen ER-Eingang; Objekt-ID wird erkannt oder in der Verteilung zugeordnet; Objektstamm zeigt Verwaltungsart = PM-verwaltet und den zuständigen PM (E-30, AE-28) | [K] |
| 2 | Weiche | Verbindung „PM-verwaltet" in WF-01 (Bedingung auf Objekt/Verwaltungsart) zum Ende „An PM weitergeleitet" | [K] |
| 3 | Weiterleitung | Export an BeSync; BeSync sendet die Rechnung an das Rechnungspostfach des PM (Adresse aus Objekt-/PM-Stamm) mit Standardtext (Mechanik S-11); Übergangslösung: manuelles „Teilen per E-Mail" durch R-02 | [A] / Übergang [S] |
| 4 | Ablage | Rechnung „zur Kenntnis" in Objekt- und Gesellschaftsakte; keine DATEV-Übergabe | [S] |
| 5 | Lieferanteninformation | optional Hinweis an den Lieferanten, künftig direkt an den PM zu fakturieren (Vorlage wie WF-05) | [A] |

Ausnahme: Handelt es sich um eine Freigabeanfrage über dem Schwellwert, läuft der Beleg in WF-03 (11.2).

## 11.5 Externe Freigaben

AE-26 unterscheidet zwei Gruppen externer Beteiligter.

### 11.5.1 Kernpartner als Freigabeuser (R-08)

| Aspekt | Festlegung | Status |
|---|---|---|
| Zielgruppe | Projektsteuerer, Architekten, ggf. PM mit Konto, die regelmäßig Bau-Rechnungen prüfen oder freigeben | – |
| Mechanik | Freigabeuser in d.velop invoices: Anzahl beliebig, rollenbeschränktes Nutzungsrecht (prüfen, Nachweise anhängen, kommentieren, Positionsdaten ergänzen); Einbindung als Sachlicher Prüfer oder Freigeber über Matrix/Gruppe | [S] (d.velop invoices Leistungsbeschreibung 12/2025) |
| Zugang | Einladung per E-Mail in die Cloud; Anmeldung mit Zwei-Faktor (TOTP) oder FIDO2; keine Aufnahme in das Livos-Entra-ID nötig | [S] |
| Rechte | nur Belege, an denen der Externe beteiligt ist (`@CURRENT_USER`) bzw. Objektgruppe `DMS_O_<ObjektID>`; keine Recherche im Gesamtbestand (AE-18) | [K] |
| Lizenzrecht | Zulässigkeit von Dritten (Nicht-Mitarbeitenden) als Freigabeuser mit d.velop klären | [O] (OP-03) |
| Katalog | 4.3 = **S** (Vorbehalt Lizenz) | – |

### 11.5.2 Ad-hoc-Externe über externe Benutzeraufgabe (WF-10, R-10)

| Aspekt | Festlegung | Status |
|---|---|---|
| Zielgruppe | einmalige oder seltene Freigeber ohne Konto (z. B. Gutachter, Miteigentümer, Fachplaner) | – |
| Mechanik | process studio „Externe Benutzeraufgabe": E-Mail an 1–n Adressen mit Link auf ein d.velop-forms-Formular (M-19); nach Abschluss läuft der Prozess weiter. Zwingend mit Timer; nach Ablauf ist das Formular nicht mehr aufrufbar. | [S] (process studio Handbuch 2026.q2) |
| Belegansicht | Das Formular hat keinen Zugriff auf Dokumente. Der Beleg wird als zeitlich begrenzter Teilen-Link (Lesen, max. 180 Tage, Vorschlag 14 Tage) im Formular bereitgestellt. | [S]/[K] |
| Kopplung an smart invoice | Aktion „Externe Freigabe anfordern" im Prüf-/Freigabeschritt → Export an BeSync → BeSync startet den process-studio-Prozess mit Belegdaten und Link → Ergebnis (Zustimmung/Ablehnung/Kommentar) legt BeSync als Notiz bzw. K-07 am Beleg ab und benachrichtigt den internen Bearbeiter, der im smart-invoice-Schritt entscheidet. Die interne Entscheidung bleibt im smart-invoice-Protokoll. | [A] |
| Lizenz/Kontingent | process studio ab platform edition business (1.000 Ausführungen/Monat); Anrechnung smart invoice offen (OP-11) | [O] |
| Katalog | 4.2 = **K/A** | – |

### 11.5.3 Sicherheitsaspekte

| Risiko | Maßnahme |
|---|---|
| Weitergabe des Links | Timer und Link-Gültigkeit kurz halten; nur Leserecht auf den Beleg; keine weiteren Dokumente |
| Keine Authentifizierung am Formular | Passwort/MFA für den Link ist nicht dokumentiert → externe Ad-hoc-Freigabe nur als **Stellungnahme**; die verbindliche Freigabe erfolgt intern durch R-03/R-04 |
| Falsche Empfängeradresse | Adresse aus Stammdaten (Lieferanten-App) oder Vier-Augen-Eingabe; Protokoll der Versendung |
| Kernpartner-Konten | 2FA/FIDO2 verpflichtend; Befristung und jährliche Rezertifizierung durch R-12; Deaktivierung bei Projektende |
| Datenschutz | nur notwendige Belegdaten im Formular (explizites Mapping); AVV/Informationspflichten prüfen (Kapitel 17) |

## 11.6 Ausblick: weitere Freigaben ohne Rechnung (WF-09)

Livos möchte Freigabeworkflows auch für Vorgänge ohne Eingangsrechnung nutzen, z. B. **Ausbuchungen auf Mietkonten** (Workshop [00:37:33]). Dafür ist smart invoice nicht geeignet, weil es auf Rechnungsbelege ausgerichtet ist.

| Aspekt | Festlegung | Status |
|---|---|---|
| Werkzeug | d.velop process studio (BPMN), ab platform edition business | [S] |
| Muster | Startformular (Mandant, Objekt, Mieter/Konto, Betrag, Grund, Anlagen) → Geschäftsregel (Entscheidungstabelle Mandant × Betrag → Freigeber) → Benutzeraufgabe(n) Freigabe mit Timer-Erinnerung → Ablage des Antrags mit Entscheidung als Dokument in der Objekt-/Gesellschaftsakte → Benachrichtigung an Antragsteller | [K] |
| Wertgrenzen | Geschäftsregel pflegbar durch Fachadministration; Beispielgrenzen analog Kapitel 10, von Livos zu definieren | [K] |
| Übergabe an Buchhaltung | Ausbuchung selbst erfolgt im führenden System (PM-System bzw. DATEV) durch die zuständige Stelle; optional Übergabe per E-Mail/Aufgabe an Trios | [K]/[A] |
| Protokoll | process-studio-Protokoll mit Export ins Repository (revisionssicher), da Standardaufbewahrung 30 Tage bis max. 1 Jahr | [K] |
| Weitere Kandidaten | Freigabe von Aufträgen/Bestellungen, Budgetfreigaben, Mietnachlässe, Vertragsfreigaben (WF-06) | – |
| Phase | 5 (nach Rechnungseingang, PM-Freigabe, Bau, Verträge, Post; P8) | – |
| Offen | process-studio-Lizenz/Kontingent in C1 (OP-11) | [O] |

# 12 Verträge, Posteingang und allgemeine DMS-Nutzung

Dieses Kapitel beschreibt die drei Nutzungsbereiche außerhalb der Eingangsrechnung: den Vertragsprozess (WF-06), den Posteingang (WF-07) und die allgemeine Arbeit mit d.velop documents (Ablage, Suche, Aufgaben, mobile Nutzung, KI). Beide Prozesse gehören zur Einführungsphase 4 (Designprinzip P8). Die allgemeine DMS-Nutzung steht ab Phase 1 zur Verfügung, weil Rechnungsanlagen, Nachweise und Akten von Beginn an genutzt werden.

Kennzeichnung: **[S]** Standard belegt · **[K]** Konfiguration · **[A]** Anpassung/Entwicklung (meist BeSync) · **[O]** offen/zu verifizieren. Katalogbezug: 6.1 DMS-Nutzung (Could, Bewertung **S**), 1.3 App (**S**), 1.7 Nachweise (**S**).

---

## 12.1 Vertragsprozess (WF-06)

### 12.1.1 Ziel und Werkzeugwahl

Livos will Verträge zentral in d.velop führen, Fristen überwachen, Verträge fachlich freigeben und Fragen an Vertragsinhalte stellen (Workshop 22.09.2026, T-41). Die Architekturentscheidung AE-20 setzt dafür auf **d.velop contracts**. Die Anwendung baut auf d.velop documents auf und trennt die fachliche Vertragsverwaltung (Metadaten, Fristen, Status) von der revisionssicheren Dokumentablage (d.velop contracts: Administrieren, cloud).

| Baustein | Aufgabe im Livos-Vertragsprozess | Status |
|---|---|---|
| d.velop contracts | Vertragsanlage mit Laufzeitberechnung, Vertragsdetailansicht, Fristenmanagement/Fristenkalender, Vertragshierarchien, Vertragsakte, Aufgaben, Outlook-Ablage | [S] |
| d.velop documents | Speicherung der Vertragsdokumente (Kategorien „Vertragsakte" und „Vertragsdokumente"), Versionierung, Aufbewahrung, Berechtigungen | [S] |
| d.velop business objects | Stammdaten der Vertragspartner (Modell „contracts" mit den Entitäten account und contact) | [S] |
| d.velop process studio | fachliche Vertragsfreigabe, sofern contracts keinen eigenen Freigabeworkflow mitbringt | [K] / [O] (OP-12) |
| d.velop sign | Signaturumlauf, auch mit externen Unterzeichnern ohne Lizenz | [S] |
| d.velop pilot | Fragen an Vertragsinhalte, Zusammenfassung, Risikoanalyse | [S] (Tokengrenze [O], OP-19) |
| alphaflow Contracts | Alternative mit ausdrücklich beschriebenen Genehmigungsprozessen, Fristen-Eskalation und Zahlungsreihen | Option |

Voraussetzung ist d.velop documents platform edition (Livos: **business**, AE-02). Vertragsverantwortliche (R-11) erhalten eine volle contracts-Lizenz, reine Leser eine lesende Lizenz (Mengen in Phase 0 festlegen).

### 12.1.2 Livos-Zielkette und Abbildung

Die Livos-Zielarchitektur beschreibt Verträge als Kette „Eingang → Verarbeitung → Verteilung → Klassifizierung → Fachliche Freigabe → Archivierung". Die Kette lässt sich vollständig abbilden. Nur die fachliche Freigabe ist im contracts-Standard nicht sicher belegt.

| Schritt (Livos) | Umsetzung d.velop | Rolle | Status |
|---|---|---|---|
| 1 Eingang | Papier: Scan in der Poststelle (WF-07). E-Mail: Funktionspostfach, z. B. `vertraege@…` (Vorschlag). Outlook: Ablage aus Outlook in contracts. Eigenerstellung: Upload in die Vertragsakte | R-01, R-11 | [S] |
| 2 Verarbeitung | OCR, KI-Klassifizierung (die Klasse „Vertrag" gehört zum Standardkatalog der KI-Klassifizierung), optional Extraktion von Eckdaten mit d.velop pilot („Intelligenter Import") | System | [S] (KI nur C1, ab business) |
| 3 Verteilung | mail dispatcher: Aufgabe an die Gruppe Vertragsmanagement der Gesellschaft bzw. des Verbunds (WF-07) | R-01 → R-11 | [K] |
| 4 Klassifizierung | Vertragsanlage in contracts: Vertragstyp, Vertragsart, Mandant, Objekt, Partner, Laufzeit, Fristen. Das Dokument wird der Vertragsakte als Vertragsdokument mit Dokumententyp zugeordnet | R-11 | [S] / [K] |
| 5 Fachliche Freigabe | process-studio-Prozess „Vertragsfreigabe" (Prüfung Fachbereich → Freigabe gemäß Wertgrenze → optional Signatur mit d.velop sign). Status in contracts: „In Genehmigung" → „Aktiv" | R-11, R-04 | [K] / [O] |
| 6 Archivierung | Vertragsakte (K-14) in der Objekt- oder Gesellschaftsakte; Aufbewahrung ab Vertragsende (AE-24); Fristenüberwachung läuft bis Vertragsende weiter | System | [S] / [K] |

### 12.1.3 Vertragsmetadaten (E-28)

d.velop contracts gibt für die DMS-Seite ein Eigenschaftsset und zwei Kategorien vor. Das Livos-Modell übernimmt diese Standardstruktur und ergänzt nur die Livos-Pflichtmerkmale (P1, P2). Die Kategorie K-05 „Vertrag" wird als contracts-Kategorie **„Vertragsdokumente"** umgesetzt, K-14 „Vertragsakte" als contracts-Kategorie **„Vertragsakte"**.

| Feld | Quelle / Wertemenge | Vertragsakte (K-14) | Vertragsdokument (K-05) | Status |
|---|---|---|---|---|
| Vertrags-ID (intern) | contracts, systemseitig; verknüpft Akte und Dokumente | Pflicht | Pflicht | [S] |
| Vertrags-ID (extern) | manuell (Nummer des Vertragspartners) | optional | optional | [S] |
| Vertragsgegenstand | manuell | Pflicht | Pflicht | [S] |
| Vertragstyp | Wertemenge aus contracts (Livos-Vorschlag: Bauvertrag, Architekten-/Ingenieurvertrag, Wartungsvertrag, Dienstleistungsvertrag, Versorgungsvertrag, Versicherungsvertrag, Mietvertrag, Kaufvertrag, Darlehensvertrag, Rahmenvertrag Lieferant, Sonstiger Vertrag) | Pflicht | Pflicht (übernommen) | [S] Mechanik / [K] Werte (OP-17) |
| Vertragsart | Einzelvertrag · Rahmenvertrag · Einzelvertrag mit Rahmenvertrag | Pflicht | Pflicht | [S] |
| Vertragsstatus | Entwurf · In Genehmigung · Aktiv · Gekündigt · Abgelaufen | Pflicht | Pflicht | [S] |
| Vertragspartner | business objects (account/contact) | optional im Standard, Livos: Pflicht | übernommen | [S] / [K] |
| Verantwortlicher (intern) | Person | optional, Livos: Pflicht | übernommen | [S] / [K] |
| Organisation | Wertemenge aus contracts; steuert contracts-Rechte je Organisation × Vertragstyp | optional | optional | [S], Belegung siehe 12.1.9 |
| Vertragsbeginn / Vertragsende | Datum | optional, Livos: Beginn Pflicht | übernommen | [S] |
| Kündigungsfrist, Verlängerungsart (einmalig/rollierend), Verlängerungszeitraum, Vertragswert | contracts-Metadaten (Fristenmanagement) | – (in contracts geführt) | – | [S] laut Produktbeschreibung; Feldnamen und Übertragung ins DMS [O] |
| Dokumententyp | Wertemenge aus contracts (Vorschlag: Vertrag, Nachtrag, Kündigung, Anlage, Protokoll, Korrespondenz, Bürgschaft) | – | Pflicht | [S] / [K] |
| **Mandant (E-01)** + Mandantenname (E-02) | Dataset Gesellschaften | **Pflicht** | **Pflicht** (vererbt) | [K], Aufnahme in contracts-Kategorien [O] |
| **Objekt-ID (E-03)** | Dataset Objekte | Pflicht, wenn objektbezogen | vererbt | [K] |
| Kreditor-Nr (E-05) | smart-invoice-Bucket | bei Lieferanten-/Bauverträgen | vererbt | [K] |
| Aufbewahrungsbeginn (E-29) | abgeleitet aus Vertragsende | – | berechnet | [K] (AE-24) |

Wichtig für die Konfiguration: Die Werte der Wertemengen Vertragstyp, Vertragsstatus, Vertragsart, Organisation und Dokumententyp müssen in d.velop documents **exakt** mit den Werten in contracts übereinstimmen (Schreibweise, Groß-/Kleinschreibung, Leerzeichen). Sonst scheitert die Anlage der Vertragsakte mit Fehlermeldung (d.velop contracts: Administrieren, cloud). Datentyp und Anzahl der Werte einer contracts-Eigenschaft lassen sich nachträglich nicht ändern. Das Modell ist daher vor dem Pilot abschließend festzulegen.

### 12.1.4 Fristen und Wiedervorlage

| Frist / Termin | Mechanismus | Empfänger | Status |
|---|---|---|---|
| Kündigungsfrist (Kündigungsstichtag) | contracts-Fristenmanagement: Frist wird aus Laufzeit und Kündigungsfrist berechnet und gemeldet; Fristenkalender | Verantwortlicher (intern), Vertretung über Plattform | [S] (Vorlaufzeiten konfigurierbar [O]) |
| Vertragsende / Verlängerungsoption | contracts-Laufzeitberechnung, Statuswechsel „Abgelaufen" | Verantwortlicher | [S] |
| Gewährleistungsende Bau, Rückgabe Sicherheit/Bürgschaft | Datum als zusätzliche Eigenschaft je Vertragstyp (contracts „Details") + Wiedervorlage-Aufgabe (WF-08) oder process-studio-Timer | Vertragsverantwortliche, Bau | [K] |
| Indexanpassung, Preisgleitklausel (Wartung, Versorgung) | Wiedervorlage-Aufgabe (WF-08) am Vertrag | Vertragsverantwortliche | [K] |
| Gültigkeit Versicherungsnachweis / Bescheinigung (K-06) | Eigenschaft „Gültig bis" + gespeicherte, beobachtete Suche „läuft in 60 Tagen ab" (Vorschlag) | Kreditorenbuchhaltung (R-02) | [K] |
| Freistellungsbescheinigung § 48b | AE-15 (BeSync-FSB-Status) | R-02 | [A] (Phase 3) |

Eskalation: contracts beschreibt die rechtzeitige Meldung von Fristen. Eine mehrstufige Eskalation (z. B. an die Geschäftsführung, wenn 14 Tage vor Stichtag nichts passiert ist) ist öffentlich nicht belegt [O]. Falls nötig, übernimmt ein process-studio-Timer diese Aufgabe [K]. alphaflow Contracts nennt Erinnerungen **und** Eskalationen ausdrücklich.

### 12.1.5 Vertragshierarchie: Rahmenvertrag und Einzelauftrag

d.velop contracts unterstützt Vertragshierarchien über die Vertragsart (Einzelvertrag, Rahmenvertrag, Einzelvertrag mit Rahmenvertrag). Für Livos gilt folgende Zuordnung (Vorschlag):

| Livos-Fall | Vertragsart | Verknüpfung | Aktenbezug |
|---|---|---|---|
| Rahmenvertrag mit einem Lieferanten für eine Gesellschaft (z. B. Wartung aller Aufzüge) | Rahmenvertrag | übergeordnet | Gesellschaftsakte (K-10) und Kreditorenakte (K-12) |
| Konzern-Rahmenvertrag für mehrere Gesellschaften | Rahmenvertrag, Mandant als **Mehrfachwert** | übergeordnet | je Gesellschaft sichtbar (Test T04); beim Export einer Gesellschaft gesondert behandeln |
| Einzelauftrag/Abruf unter einem Rahmenvertrag, z. B. je Objekt | Einzelvertrag mit Rahmenvertrag | Verweis auf den Rahmenvertrag | Objektakte (K-11), Vorgangsakte (K-13) |
| Bauvertrag je Vergabeeinheit (Los) | Einzelvertrag | Auftragsnummer/Vertragsnummer (E-19) = Schlüssel der Vorgangsakte | Objektakte (K-11) → Vorgangsakte (K-13) |
| Nachtrag, Kündigung, Protokoll | kein eigener Vertrag, sondern Vertragsdokument mit Dokumententyp | gleiche Vertrags-ID (intern) | Vertragsakte (K-14) |

Die Aktenebenen bleiben innerhalb der Obergrenze aus AE-19 (höchstens vier Ebenen): Gesellschaftsakte → Objektakte → Vertragsakte bzw. Vorgangsakte.

### 12.1.6 Signatur mit d.velop sign

| Aspekt | Festlegung | Status |
|---|---|---|
| Einsatz | Signaturumlauf aus contracts heraus, intern und mit externen Unterzeichnern (per E-Mail eingeladen, ohne Lizenz und Installation) | [S] |
| Signaturniveau | fortgeschrittene Signatur/Siegel für Standardverträge; qualifizierte elektronische Signatur (QES) nur bei Schriftformerfordernis. Personenbezogene Signaturen erfordern eine einmalige Identifizierung | [S] |
| Kontingent | Die platform edition business enthält ein Monatskontingent fortgeschrittener Siegel je Mandant (Leistungsbeschreibung platform edition 10/2025). Mehrbedarf wird zugekauft | [S], Mengengerüst Phase 0 |
| Formerfordernis | Grundstückskauf (notarielle Beurkundung) und Schriftformverträge (z. B. langfristige Mietverträge) bleiben außerhalb der elektronischen Signatur. Das signierte Papieroriginal wird gescannt und als Vertragsdokument abgelegt | organisatorisch (Livos Recht) |
| Ablage | Das signierte Dokument wird neue Version des Vertragsdokuments (Status Freigabe) | [S] |

### 12.1.7 Vertragsakte (K-14) und Ablage

- Die **Vertragsakte** ist das übergeordnete Objekt je Vertrag. Vertragsdokumente liegen darunter. Die Eigenschaft „Vertrags-ID (intern)" verknüpft beide. Die übrigen Eigenschaften werden von der Akte auf die Dokumente vererbt (d.velop contracts: Administrieren, cloud) [S].
- Strukturregel (AE-19): Objektakte → Vertragsakte über **Mandant + Objekt-ID**. Verträge ohne Objekt (Gesellschaftsebene, z. B. Versicherungen, IT) hängen direkt an der Gesellschaftsakte. Lieferantenverträge werden zusätzlich in der Kreditorenakte verknüpft (**Mandant + Kreditor-Nr**) [K], Mehrfachregel siehe Test T13 (OP-08).
- Korrespondenz zum Vertrag (K-07) wird im Posteingang mit Dokumententyp „Korrespondenz" als Vertragsdokument abgelegt, damit sie in der Vertragsakte erscheint.
- Aufbewahrung: Frist ab Datumseigenschaft „Vertragsende" plus Frist je Vertragsart; Löschsperre aktiv; automatisches Löschen zunächst aus (AE-24). Zivilrechtliche Fristen (Bau/Gewährleistung, Grundstück, Darlehen) legt die Livos-Rechtsabteilung fest.

### 12.1.8 Bezug zu Rechnungen und Abschlägen

| Bezug | Umsetzung | Status |
|---|---|---|
| Rechnung ↔ Vertrag | Auftrags-/Vertragsnummer (E-19) an der Eingangsrechnung (Pflicht bei Bau-Rechnungen, sonst optional). Eine gespeicherte Suche „Alle Rechnungen zu Vertrag X" verbindet beide Sichten | [K] |
| Rechnung in der Vorgangsakte | Aktenbildung über Mandant + Auftragsnummer: Auftrag, Abschläge, Schlussrechnung und Nachweise liegen in einer Vorgangsakte (K-13) | [K] |
| Abschlags- und Schlussrechnungen, kumulierte VOB-Prüfung, Einbehalte | fachlich in BIM4You (AE-11, WF-02). d.velop zeigt das Ergebnis (E-22) und legt den Prüfbericht (K-08) in der Vorgangsakte ab | [A] |
| Sichtbarkeit früherer Abschläge beim Prüfen (T-31) | Vorgangsakte und Aktenansicht aus der Rechnung heraus; Zahlstatus (E-23) je Abschlag | [K] / [A] (E-23 über S-06) |
| Vertragswert gegen abgerechnete Summe | nicht im d.velop-Standard. Auswertung in evidanza aus Vertragswert und Rechnungsdaten (S-12) | [A], optional |
| Zahlungsreihen (Mieten, Wartung ohne Rechnung) | nicht in d.velop contracts belegt; alphaflow Contracts nennt Zahlungsreihen | Option / [O] |
| Rahmenvertrag in der Kreditorenakte | Verknüpfung über Mandant + Kreditor-Nr (K-12 enthält laut Kategorienkatalog auch Rahmenverträge) | [K] |

### 12.1.9 Rechte in d.velop contracts

d.velop contracts vergibt Rechte **gruppenbasiert je Organisation und Vertragstyp** (Lesen, Schreiben, Löschen). Zusätzlich brauchen Anwender die Rechte auf die Kategorien in d.velop documents (d.velop contracts: Administrieren, cloud). Daraus ergibt sich eine Gestaltungsfrage:

| Option | Organisation = | Wirkung | Bewertung |
|---|---|---|---|
| A | Gesellschaft (Mandant) | feinste Trennung, aber >100 Organisationen × Vertragstypen × Gruppen in einer manuell gepflegten Matrix | nicht empfohlen (Pflegeaufwand, keine Pflege-API belegt) |
| **B (Vorschlag)** | Gesellschaftsverbund bzw. Freigabeverbund (wenige Werte) | contracts-Übersicht zeigt Verträge des Verbunds; die Dokumente sind zusätzlich über die DMS-Berechtigung mit `RS_Mandant` je Gesellschaft geschützt (Kapitel 13) | empfohlen, Test im Pilot |
| C | eine Organisation „Livos" | Trennung nur über DMS-Rechte; contracts-Übersicht zeigt allen Vertragsnutzern alle Vertragsmetadaten | nur bei kleinem Nutzerkreis |

### 12.1.10 KI-Fragen an Verträge mit d.velop pilot

d.velop pilot ist in der platform edition business enthalten (AE-27). Fragen an Vertragsinhalte beantwortet damit bereits der d.velop-Standard, für einzelne Dokumente und über Assistenten auch für mehrere Dokumente. Die MDIS-KI-Plattform X.One ergänzt systemübergreifende Analysen (DATEV, Lieferanten-App, BI).

| Funktion | Nutzen für Livos | Status |
|---|---|---|
| Chat mit einem Dokument (Kontextaktion) | „Ist Skonto vereinbart?", „Wie lang ist die Kündigungsfrist?" (T-41). Chatverlauf 30 Tage, als Notiz speicherbar | [S] |
| Prompt-Katalog | Zusammenfassung, Risikoanalyse (rechtlich/finanziell), FAQ, Action Items, personenbezogene Daten | [S] |
| Chat mit bis zu 10 Dokumenten | Vergleich Vertrag – Nachtrag – Angebot | [S] |
| Assistent / Knowledge Base | Fragen über alle Verträge einer Kategorie mit Quellenangabe. Grenzen: bis zu 5 Knowledge Bases je Tenant, je bis zu 5.000 neueste Dokumente | [S] |
| Berechtigungen | Chat und Assistent beachten die Dokumentrechte des Benutzers. In process-studio-Prozessen prüft der Assistent keine Dokumentrechte → Prozess-KI nur für unkritische Inhalte | [S] |
| **Tokengrenze** | Laut Handbuch werden nur Dokumente unter **20.000 Token** verarbeitet, längere sofort abgelehnt. Ein 20-seitiger deutscher Vertrag liegt nahe an dieser Grenze | [O] (OP-19) |

**Tokengrenze-Test (Vorschlag für den Pilot, OP-19):**

| Testfall | Dokument (Livos stellt bereit) | Erwartung | Konsequenz bei Misserfolg |
|---|---|---|---|
| P1 | Wartungsvertrag, ca. 5 Seiten | Antwort mit Fundstelle | – |
| P2 | Bau-/Architektenvertrag, ca. 20 Seiten | Antwort ohne Ablehnung | Vertragsdokument und Anlagen getrennt ablegen; Assistent statt Einzeldokument-Chat testen |
| P3 | Vertrag mit Anlagen, 40–60 Seiten | Ablehnung wahrscheinlich | Zusammenfassung je Anlage; X.One für Langdokumente |
| P4 | Gescannter Altvertrag (OCR) | Antwortqualität bei OCR-Text | Scanqualität, OCR-Nachbearbeitung |
| P5 | Frage mit Berechtigungsgrenze (Vertrag fremder Gesellschaft im Assistenten) | kein Treffer für nicht berechtigte Nutzer | Assistent je Gesellschaftsverbund |

Datenschutz: Anbieter und Region der KI-Verarbeitung ergeben sich aus dem Auftragsverarbeitungsvertrag mit d.velop. Livos-Datenschutz prüft den Einsatz vor dem Pilot, besonders bei Verträgen mit Personenbezug (OP-19).

### 12.1.11 Alternative alphaflow Contracts

alphaflow Contracts (Partner-App im d.velop store, Cloud AWS Frankfurt, setzt d.velop documents platform edition voraus) beschreibt ausdrücklich: flexible Genehmigungsprozesse ohne Programmierung, Fristen mit Erinnerungen und Eskalationen, Rahmenverträge, Zahlungsreihen, Finanzberichte und individuelle Felder je Vertragstyp. KI-Funktionen enthält nur der höchste Plan.

Entscheidungsregel (Vorschlag): Liefert d.velop contracts nach Klärung von OP-12 keinen Standard-Freigabeworkflow **und** braucht Livos Zahlungsreihen (z. B. Wartungs- oder Versorgungsverträge ohne Einzelrechnung), wird alphaflow Contracts im Pilot gegen d.velop contracts plus process studio verglichen.

### 12.1.12 Offene Punkte Verträge (OP-12)

| Nr. | Frage an d.velop / Livos | Bezug |
|---|---|---|
| OP-12.1 | Enthält d.velop contracts (Cloud) einen Standard-Freigabeworkflow, oder ist process studio nötig? Kann ein Prozess den Vertragsstatus in contracts setzen? | 12.1.2 Schritt 5 |
| OP-12.2 | Lassen sich eigene Eigenschaften (Mandant, Objekt-ID, Kreditor-Nr) in die contracts-Kategorien aufnehmen und über Strukturregeln in Livos-Akten verknüpfen? | 12.1.3, 12.1.7 |
| OP-12.3 | Mehrgesellschaftsfähigkeit: Bedeutung und Grenzen von „Organisation"; Pflege-API für Rechte je Organisation × Vertragstyp | 12.1.9 |
| OP-12.4 | Fristenlogik im Detail: rollierende Verlängerung, Vorlaufzeiten, Empfänger, Eskalationsstufen; Übertragung der Fristfelder ins DMS (Suche) | 12.1.4 |
| OP-12.5 | Vorlagenbasierte Vertragserstellung (nur in allgemeinen FAQ genannt) | 12.1.2 |
| OP-12.6 | API für Vertragsanlage/-status (BeSync, z. B. Übernahme Vertragswert nach evidanza) | 12.1.8 |
| OP-12.7 | Zugang zum Anwenderhandbuch d.velop contracts (Cloud) | allgemein |
| OP-12.8 | Livos: Vertragstypen, Verantwortlichkeiten, Freigabegrenzen für Verträge, Bestand Altverträge (Migrationsmenge) | OP-17 |

---

## 12.2 Posteingang (WF-07)

### 12.2.1 Ziel

Livos scannt Papierpost bereits heute (Workshop 22.09.2026). Ziel ist ein digitaler Posteingang mit der Livos-Kette „Eingang → Verarbeitung → Klassifizierung → Verteilung → Archivierung" (AE-21). Rechnungen verlassen den Postweg früh und laufen in die ER-Strecke (WF-01), Verträge in d.velop contracts (WF-06). Alle übrigen Schriftstücke werden klassifiziert, an Fachgruppen verteilt und in Akten abgelegt.

### 12.2.2 Eingangskanäle

| Kanal | Umsetzung | Grenzen / Hinweise | Status |
|---|---|---|---|
| Papierpost zentral | Poststelle (R-01) scannt mit d.velop inbound scan. Scanner über d.velop scanner connector; Trennung per Barcode-Trennblatt (Code 128) oder KI-Trennung | Stapel auf 100 Seiten ausgelegt, Import hart auf 200 Seiten begrenzt; stapelbasiertes Scannen bis 10.000 Dokumente je Monat und Tenant | [S] |
| Papierpost über Scandienstleister | Dienstleister liefert PDF plus Metadaten (z. B. Gesellschaft aus Trennblatt-Barcode) per Funktionspostfach oder über Inbound-API/DMS-API | SFTP-Eingang ist nicht belegt und wird nicht eingeplant | [K] / [O] (OP-13) |
| E-Mail-Funktionspostfächer | M365-Postfach mit Aliasen je Zweck, z. B. `post@…`, `vertraege@…` (Vorschlag); je Alias Importprofil mit Standardkategorie und Schlüssel-Wert-Paar (Mandant) | C1: unbegrenzte Funktionspostfächer, 10.000 E-Mails je Monat und Postfach. Alle vorhandenen Mails im Posteingang werden importiert → Postfach vor Aktivierung bereinigen | [S] (Voraussetzung M365, OP-16) |
| Rechnungspostfächer | `rechnung@…` und Aliase je Gesellschaft laufen **nicht** über den Postprozess, sondern direkt in die ER-Strecke (AE-22) | – | [S] |
| Outlook-Ablage durch Mitarbeiter | Outlook-Add-In (Kapitel 12.3) | – | [S] |

**Scan intern oder Dienstleister (OP-13):**

| Kriterium | Interner Scan (Poststelle) | Scandienstleister |
|---|---|---|
| Durchlaufzeit | am Eingangstag | abhängig vom Abholrhythmus (meist +1 Tag) |
| Qualitätskontrolle | Poststelle prüft Trennung und Lesbarkeit im Stapel | vertraglich geregelt; Stichproben durch R-01 |
| Technik | Scanner + scanner connector, Trennblätter | Einlieferweg Postfach oder API; Metadatenformat vereinbaren |
| Ersetzendes Scannen (Vernichtung Papier) | Verfahrensdokumentation Livos | zusätzlich Dienstleisterzertifizierung prüfen |
| Empfehlung | Start intern (Poststelle existiert, Volumen moderat); Dienstleister nur bei Volumen- oder Personalengpass | – |

### 12.2.3 Verarbeitung und KI-Klassifizierung

| Funktion | Beschreibung | Status |
|---|---|---|
| OCR, durchsuchbares PDF, PDF/A-Rendition | im Importprofil aktiv | [S] |
| KI-Dokumenttrennung | trennt Mehrdokument-Scans ohne Trennblatt; Trenner werden farbig markiert und sind manuell korrigierbar | [S] nur **C1**/Hybrid, ab **business** |
| KI-Klassifizierung | ordnet Dokumentarten zu, u. a. Angebot, Auftragsbestätigung, Lieferschein, Eingangsrechnung, Mahnung, Vertrag, Protokoll, Schriftwechsel. Bietet die drei wahrscheinlichsten Kategorien zur Auswahl an | [S] nur C1/Hybrid, ab business |
| **Schwelle 80 %** | Erkennt die Klassifizierung eine Dokumentart nur mit 80 % Sicherheit, wird das Dokument als **„Unbestimmt"** gekennzeichnet (Leistungsbeschreibung d.velop inbound scan). „Unbestimmt" geht an die Clearing-Gruppe der Poststelle zur manuellen Klassifizierung (P7) | [S] / [K] |
| RegEx- und Barcode-Regeln | ergänzend, z. B. Barcode „Gesellschaft" auf dem Trennblatt → Mandant. Treffen mehrere RegEx verschiedener Kategorien zu, wird keine Kategorie gesetzt | [S] / [K] |
| Absender-/Betreff-Regelwerk | im mail dispatcher nicht vorhanden; Steuerung nur über Postfach/Alias | Grenze |
| d.velop pilot „Intelligenter Import" | Dokumentart, Absender und Kurzzusammenfassung per LLM | [S], Option |

Konsequenz: KI-Trennung und KI-Klassifizierung setzen die Betriebsform **C1** voraus (AE-01, OP-01). In T Cloud (C2) bleibt nur die regel- und barcodebasierte Verarbeitung.

### 12.2.4 Klassifizierungskatalog Post (Vorschlag)

Der Katalog ist ein Vorschlag für den Prozess-Workshop (OP-17). Die Empfängergruppen folgen dem Gruppenmodell aus Kapitel 13 (Beispielnamen).

| Nr. | Postklasse (KI-Klasse bzw. manuell) | Zielkategorie | Weg | Empfängergruppe (Beispiel) | Aktenbezug | Aufbewahrung |
|---|---|---|---|---|---|---|
| P-01 | Eingangsrechnung, Gutschrift | K-01 | **Umleitung in die ER-Strecke** (siehe 12.2.6) | R-02 Rechnungseingang | Kreditoren-/Objektakte | 8 Jahre |
| P-02 | Mahnung, Zahlungserinnerung | K-07 | Verteilung | R-02 Rechnungseingang | Kreditorenakte | 6 Jahre |
| P-03 | Vertrag, Nachtrag, Kündigung | K-05 | **Umleitung in d.velop contracts** | Vertragsmanagement (R-11) der Gesellschaft | Vertragsakte | ab Vertragsende |
| P-04 | Angebot | K-04 | Verteilung | Fachbereich/Projektleitung | Objekt-/Vorgangsakte | 6 Jahre |
| P-05 | Auftragsbestätigung, Bestellung | K-03 | Verteilung | Fachbereich/Projektleitung | Vorgangsakte | 6 Jahre (8, wenn Buchungsgrundlage) |
| P-06 | Lieferschein, Aufmaß, Abnahmeprotokoll, Stundenzettel | K-02 | Verteilung | Sachliche Prüfer des Objekts | Vorgangs-/Objektakte | bis 8 Jahre |
| P-07 | Freistellungsbescheinigung, Unbedenklichkeit, Versicherungsnachweis | K-06 | Verteilung | R-02 Rechnungseingang | Kreditorenakte | 8 Jahre ab „Gültig bis" (wie K-06, Kapitel 7.7) |
| P-08 | Schriftwechsel Lieferant/Dienstleister | K-07 | Verteilung | Fachbereich | Kreditoren- oder Objektakte | 6 Jahre |
| P-09 | Behördenpost, Steuerbescheid | K-09 | Verteilung | Geschäftsführung / Steuer | Gesellschaftsakte | 10 Jahre (Vorschlag) |
| P-10 | Versicherungspost (Police, Schaden) | K-09 | Verteilung | Versicherungsverantwortliche | Gesellschafts-/Objektakte | nach Vorgabe Livos |
| P-11 | Mieterpost | K-09 | Verteilung | Asset Management; bei PM-Objekten Weiterleitung an den PM außerhalb d.velop | Objektakte | nach Vorgabe Livos |
| P-12 | Bank, Darlehen | K-09 | Verteilung | Treasury (R-05) | Gesellschaftsakte | 6–10 Jahre |
| P-13 | Gerichts- und Anwaltspost, Fristsachen | K-09 | Verteilung mit Priorität „hoch" | Recht / Geschäftsführung | Gesellschaftsakte | nach Vorgabe Livos |
| P-14 | Werbung, Irrläufer | – | nicht ablegen | – | – | – |
| P-15 | **Unbestimmt** (< 80 %) | – | Clearing | Poststelle (R-01) | – | – |

Die feinere Aufteilung von K-09 (Behörden, Steuer, Versicherung, Mieterpost) ist für Phase 4 vorgesehen (Kategorienkatalog K-09). Bis dahin gilt für K-09 die Frist aus Kapitel 7.7 (6 Jahre); abweichende Fristen in der Tabelle (z. B. Steuerbescheide) setzen eine eigene Unterkategorie voraus. Aufbewahrungsfristen legt die Steuerberatung abschließend fest (AE-24).

### 12.2.5 Verteilung mit d.velop mail dispatcher

| Regel | Festlegung | Status |
|---|---|---|
| Erstempfänger | **immer eine Gruppe**, nie eine Person. Bei einer Person als Erstempfänger entsteht keine Aufgabe (d.velop mail dispatcher: Administrieren, cloud) | [S] |
| Gruppenzuschnitt | Funktionsgruppe je Gesellschaftsverbund bzw. Fachbereich (Beispiel `POST_<Verbund>_<Funktion>`); Vertretung ergibt sich aus der Gruppe | [K] |
| Bearbeitung | Die erste Person, die die Aufgabe öffnet, übernimmt sie (Sperre für andere) | [S] |
| Weiterleitung | „Es ist für mich" (Ablage mit Zielkategorie und Akte, Aufgabe wird quittiert), „An Kollegen*in senden" (Person oder Abteilung, mit Kommentar), „An Posteingang senden"; bis zu 20 Schnellaktionen als Favoriten; jede Weiterleitung wird protokolliert | [S] |
| Erinnerung | systemseitige Erinnerung an die Empfängergruppe nach definierbarer Zahl Tage (Vorschlag: 3 Arbeitstage) | [S] / [K] |
| Eskalation | über die Priorität; Priorität „normal" eskaliert nach 14 Tagen. Livos-Vorschlag: Priorität „hoch" für Fristsachen (P-13) mit kürzerer Frist | [S] / [K] |
| Fallback | Dokumente ohne Empfängergruppe gehen an die Clearingstelle (Poststelle) | [S] |
| Postkategorie | Der mail dispatcher arbeitet mit genau einer Postkategorie (Best Practice „Postdokument" mit den Feldern Post-ID, Posttyp, Priorität, Eingangsdatum, Kommentar, Barcode). Postdokumente werden im Status Freigabe importiert. Im Livos-Modell übernimmt **K-09** diese Rolle: Nach der Verteilung wechselt das Dokument bei „Es ist für mich" in die Zielkategorie | [S] / [K] |
| Einrichtung | Cloud-Einrichtungsassistent erzeugt Webhooks und Kategoriezuordnung | [S] |
| Lizenz | Buchbarkeit von mail dispatcher / inbox management in der Cloud und Anrechnung auf process-studio-Kontingente sind zu klären | [O] (OP-13) |

E-Mail-Eingänge über Funktionspostfächer sind im mail-dispatcher-Standard als Projekterweiterung beschrieben. Für Livos gilt daher: E-Mail-Post wird über Importprofile direkt der Zielkategorie oder der Postkategorie zugeordnet. Die Verteilung per mail dispatcher ist für E-Mail-Post im Pilot zu testen [O]. Alternative mit KI-Empfängervorschlag ist die Partner-App **VLOTT Postverteilung** (d.velop store).

### 12.2.6 Umleitung von Rechnungen und Verträgen

| Fall | Weg | Status |
|---|---|---|
| Papierrechnung in der Post (Regelfall) | Vorsortierung beim Öffnen der Post: Rechnungen kommen in einen eigenen Scanstapel mit dem ER-Importprofil (inbound → document reader → smart invoice). Sie werden nicht als Postdokument verteilt | [K] |
| Rechnung im allgemeinen Poststapel erkannt (KI-Klasse „Eingangsrechnung") | Poststelle verschiebt das Dokument im Stapel in den ER-Stapel bzw. importiert es über das ER-Importprofil neu. Eine direkte, automatische Übergabe vom Postdokument an smart invoice ist nicht belegt | [K] / [O] |
| Rechnung per E-Mail an `post@…` | Weiterleitung an `rechnung@…` durch die Poststelle | [S] (organisatorisch) |
| Rechnung als Anlage zu Korrespondenz | Rechnung in die ER-Strecke, Anschreiben als K-07 in die Kreditorenakte | [K] |
| Vertrag, Nachtrag, Kündigung | Verteilung an die Gruppe Vertragsmanagement; dort Zuordnung zur Vertragsakte in contracts (neu anlegen oder bestehender Vertrag) | [K] |
| Dublette durch Doppeleingang (Mail und Post, T-27) | Dublettenprüfung in smart invoice; Ablehnung ohne Lieferantenmail mit Begründung (AE-13) | [S] |

### 12.2.7 Ablage in Akten

Mit „Es ist für mich" wählt der Empfänger die Zielkategorie und ergänzt die Pflichtmerkmale. Die Aktenbildung ordnet das Dokument danach automatisch zu (AE-19):

- **Mandant (E-01)** ist schon am Postdokument Pflicht. Die Poststelle setzt ihn aus Trennblatt-Barcode, Alias-Vorbelegung oder manuell. Ohne Mandant keine Akte und keine Rechte (P1).
- Kreditor-Nr (E-05) und Objekt-ID (E-03) ergänzt der Fachbereich, sofern die Zielkategorie sie verlangt (Kapitel 14, M-15).
- Gesellschaftsübergreifende Post (z. B. Konzernschreiben) bekommt den Mandanten der Holding und wird bei Bedarf manuell mit weiteren Gesellschaftsakten verknüpft.

### 12.2.8 Prozessablauf WF-07 im Überblick

| Nr. | Schritt | Rolle | Werkzeug | Ergebnis |
|---|---|---|---|---|
| 1 | Post öffnen, Rechnungen und Verträge vorsortieren, Trennblätter einlegen | R-01 | – | Stapel je Zweck |
| 2 | Scannen, Stapel prüfen (Trennung, Seitenfolge, Lesbarkeit) | R-01 | inbound scan (M-15 Teil A) | Dokumente mit OCR |
| 3 | KI-Klassifizierung prüfen, „Unbestimmt" manuell klassifizieren, Mandant setzen | R-01 | inbound scan | Postdokument mit Klasse und Mandant |
| 4 | Verteilung an Empfängergruppe | System | mail dispatcher | Gruppenaufgabe |
| 5 | Übernehmen, weiterleiten oder „Es ist für mich" | Fachbereich | mail dispatcher (M-15 Teil B) | Zielkategorie, Akte |
| 6 | Erinnerung/Eskalation bei Liegezeit | System | mail dispatcher | Erinnerung, Eskalation |
| 7 | Archivierung mit Aufbewahrung je Kategorie | System | d.velop documents | Dokument in Akte |

---

## 12.3 Allgemeine DMS-Nutzung

### 12.3.1 Funktionsübersicht mit Editionsvoraussetzungen

| Funktion | Beschreibung für Livos | Edition | Status |
|---|---|---|---|
| Ablage über Feature „Ablage" | Datei wählen, Kategorie wählen, Eigenschaften erfassen, speichern | alle | [S] |
| Drag & Drop | Dropzones an Akten (automatisch, manuell, mit Vorlage); neue Version durch Ziehen auf ein Dokument; Import-Widget mit bis zu 4 Dropzones je Importprofil | alle | [S] |
| Outlook-Add-In (Desktop, M365) | E-Mail oder Anlagen ablegen, Mehrfachablage in vordefinierte Kategorien, Suche im Kontext der Mail; organisationsweite Verteilung über das Microsoft 365 Admin Center | ab business | [S] |
| Outlook-Web-Add-In | Ablage aus Outlook im Web und „neuem Outlook", **ohne** Mehrfachablage und direkte Suche | ab business | [S] |
| Mehrfachablage in Akten | automatisch über Strukturregeln (z. B. Rechnung in Kreditoren- **und** Objektakte) oder manuell („Zum Verknüpfen markieren" → „Markierte Elemente verknüpfen"). Das Dokument wird nur einmal gespeichert | alle | [S] Mechanik, automatische Mehrfachregel [O] (T13) |
| Suche | Volltext inkl. OCR, Facetten, Filter nach Kategorie und Eigenschaften, Recherche in Aktenstrukturen | alle | [S] |
| Gespeicherte Suchen (Suchvorlagen) | persönliche Ordnerstruktur, per Link teilbar; beobachtbar mit E-Mail-Benachrichtigung bei neuen Treffern. Eine zentrale Zuweisung an Rollen ist nicht belegt → Standard-Suchen werden als Link verteilt (Startseite, M-10) | Beobachten ab business | [S] / [O] |
| Versionierung | jede Freigabe mit Änderung erzeugt eine neue Version; Status Bearbeitung, Prüfung, Freigabe, Archiv; Versionsübersicht; Check-in/Check-out konfigurierbar | alle | [S] |
| Office-Bearbeitung | lokal (Client-Anwendung nötig) oder im Browser (M365-Business-Abo erforderlich) | Browser ab business | [S] |
| Notizen, Kommentare, Annotationen | Notizen am Dokument; Kommentare und grafische Markierungen in PDF. Annotationen werden getrennt gespeichert, das Original bleibt unverändert (P5) | alle | [S] |
| Schwärzen | erzeugt ein neues Dokument oder eine neue Version; Original bleibt unverändert; standardmäßig deaktiviert | alle | [S] / [K] |
| Aufgaben und Wiedervorlagen (WF-08) | siehe 12.3.3 | alle | [S] |
| Beobachten | Benachrichtigung bei Änderung, Notiz, neuer Version, Löschung | alle | [S] |
| Teilen intern | „Link senden" (interner Link), „Kopie senden" (E-Mail mit Anhang über das eigene Mailprogramm) | alle | [S] |
| Teilen extern | „Extern teilen": lesen/herunterladen oder neue Version hochladen, Gültigkeit max. 180 Tage, jederzeit beendbar; externe Änderungen werden erst nach Prüfung übernommen. Passwortschutz nicht dokumentiert | ab business | [S] |
| Aktivitäten | Protokoll aller Änderungen an Datei und Eigenschaften, filterbar | alle | [S] |
| Eigenschaften exportieren | Ergebnisliste oder Akteninhalt als Excel/CSV | alle | [S] |
| PDF zusammenführen | Sammel-PDF mit Deckblatt und Inhaltsverzeichnis (nicht für Akten) | ab business | [S] |
| Mobile App d.velop mobile | iOS/iPadOS und Android: Aufgaben, Suche, Akten (auch offline), Dokumentscanner (iOS), Push, Abwesenheit setzen. Die Bedienung der smart-invoice-Workflowmaske in der App ist nicht dokumentiert → Rechnungsfreigabe mobil über den Browser (responsiv); App-Freigabe im Test prüfen (OP-38, Test T36) | ab business | [S] / [O] |
| d.velop pilot | Chat mit Dokumenten, Assistenten (siehe 12.1.10) | ab business | [S] |

Die Tabelle bestätigt AE-02: DMS-Vollnutzer brauchen die Edition **business**. Freigabeuser aus d.velop invoices haben nur ein rollenbeschränktes Nutzungsrecht in d.velop documents (prüfen, Lieferscheine anhängen, Notizen, Annotationen, Positionsdaten ergänzen) und keine volle DMS-Nutzung (Leistungsbeschreibung d.velop invoices 12/2025).

### 12.3.2 Ablageregeln für Anwender

| Regel | Begründung |
|---|---|
| Immer über Kategorie und Eigenschaften ablegen, nie in „Ordner". d.velop bildet die Akten aus den Eigenschaften selbst (Workshop 22.09.2026) | Aktenbildung, Rechte |
| Mandant ist immer Pflicht (P1) | Rechte, Export je Gesellschaft |
| Nachweise zu einer Rechnung (Lieferschein, Aufmaß) als K-02 mit Mandant, Kreditor, Objekt, Auftragsnummer ablegen oder im Workflow an den Beleg anhängen | Vorgangsakte, T-20 |
| E-Mails mit Rechnung nicht per Outlook ablegen, sondern an `rechnung@…` weiterleiten | ER-Strecke, Dublettenvermeidung |
| Rechnungen und E-Rechnungen nie lokal bearbeiten; Anmerkungen nur als Notiz/Annotation | P5, GoBD |
| Dokumente mit Personenbezug (z. B. Mieterselbstauskunft) nur in dafür vorgesehenen Kategorien | Löschkonzept |

### 12.3.3 Aufgaben und Wiedervorlagen (WF-08)

Ad-hoc-Aufgaben am Dokument wurden im Workshop gezeigt (Aufgabe an eine Person mit Priorität, Zustelldatum, Fälligkeit, Erinnerung und Selbstbenachrichtigung).

| Element | Festlegung | Status |
|---|---|---|
| Aufgabe zum Dokument | Kontextaktion am Dokument oder an der Akte; Empfänger Person oder Gruppe | [S] |
| Felder | Betreff, Empfänger, Priorität, Zustelldatum (= Wiedervorlage), Fälligkeit, Erinnerung, Beschreibung, Benachrichtigung bei Erledigung | [S] |
| Aufgabenlisten | Meine Aufgaben, An mich gesendet, An mich und andere gesendet, Meine geplanten Aufgaben, je Gruppe eine Liste, Meine erstellten/weitergeleiteten/erledigten Aufgaben | [S] |
| Aktionen | Weiterleiten, Entziehen, Gruppenaufgabe übernehmen | [S] |
| Wiedervorlage | Aufgabe an sich selbst mit Zustelldatum in der Zukunft (z. B. Gewährleistungsende, Indexanpassung) | [S] |
| Prozesse am Dokument | manuell startbare process-studio-Prozesse (im Workshop gezeigt: „Angebot prüfen und vergleichen", „Prüfung und Freigabe") | [K] |
| Nicht für Rechnungen | Rechnungsaufgaben laufen ausschließlich in smart invoice; keine Ad-hoc-Aufgaben als Ersatz für Freigaben | Regel |
| Aufbewahrung erledigter Aufgaben | nur bis zum jeweiligen Aufbewahrungsende der Aufgabenliste; Nachweise gehören als Notiz oder Dokument an den Vorgang | [S] |

### 12.3.4 Vertretung in der DMS-Nutzung

Die Plattform-Vertretung gilt für DMS-Aufgaben, Postaufgaben und smart-invoice-Aufgaben gleichermaßen (Abwesenheitsstatus, Vertretungsregeln je Aufgabentyp, Setzen durch Administrator/Vorgesetzte). Regeln und Rechtefolgen beschreibt Kapitel 13.7, die Maske Kapitel 14 (M-18).

### 12.3.5 Einführungsreihenfolge

| Phase | Nutzung |
|---|---|
| 1 | Ablage von Nachweisen (K-02), Aufträgen (K-03), Bescheinigungen (K-06), Korrespondenz (K-07); Akten K-10 bis K-13; Suche; Aufgaben (WF-08); Outlook-Add-In für Rechnungsbeteiligte |
| 2–3 | mobile App für Freigeber und Projektleitung; gespeicherte Suchen je Rolle; Extern teilen für Kernpartner |
| 4 | Verträge (WF-06) mit d.velop contracts, Posteingang (WF-07), d.velop pilot für Verträge |

# 13 Rollen- und Berechtigungskonzept

Dieses Kapitel legt fest, wer in d.velop documents, d.velop invoices (smart invoice), d.velop contracts und im Posteingang was sehen und tun darf. Es setzt die Architekturentscheidung AE-18 um und erfüllt die Katalogpunkte 1.1 (Mandantenfähigkeit, **K**), 1.5 (Rollen und Rechte intern/extern, **K**), 3.4 (Vertretung, **S/K**), 4.2 (Ad-hoc-Freigabe, **K/A**) und 4.3 (Web-Zugang Kernpartner, **S**).

Kennzeichnung: **[S]** Standard belegt · **[K]** Konfiguration · **[A]** Anpassung (BeSync) · **[O]** offen/zu testen. Gruppennamen, Grenzwerte und Intervalle sind **Vorschläge**, die Livos im Prozess-Workshop bestätigt (OP-17).

Leitsätze:

1. **Rechte hängen am Mandanten** (P1). Jedes Dokument und jede Akte trägt die Eigenschaft „Mandant" (E-01). Ohne Mandant keine Sichtbarkeit (Test T05).
2. **Rechte werden an Gruppen vergeben, nie an Personen.** Personen bekommen Rechte nur über Gruppenmitgliedschaft aus Microsoft Entra ID.
3. **Die Zahl der Berechtigungen wächst nicht mit der Zahl der Gesellschaften.** Neue Gesellschaften erweitern nur Wertelisten (Restriction Sets), nicht das Rechtemodell.
4. **Löschen ist die Ausnahme.** Freigegebene und archivierte Dokumente sind durch die Löschsperre der Kategorie geschützt (AE-24).
5. **Sichtbarkeit von Widgets ist keine Sicherheitsfunktion.** Startseiten je Rolle (M-10) erleichtern die Arbeit, schützen aber nichts.

---

## 13.1 Rollenkatalog

| ID | Rolle | Organisation | Aufgaben | Hauptwerkzeuge | Lizenztyp (Vorschlag) |
|---|---|---|---|---|---|
| R-01 | Poststelle / Scan | Livos Zentrale | Papierpost scannen, Stapel prüfen, Post-Klassifizierung nachbearbeiten („Unbestimmt"), Mandant setzen, Rechnungen in die ER-Strecke geben | inbound scan, mail dispatcher (M-15) | documents business |
| R-02 | Rechnungseingang / Verteilung (Kreditorenbuchhaltung Livos) | Livos Zentrale | Erfassung prüfen, Mandant/Kreditor/Kostenobjekt zuordnen, Klärfälle, Dubletten, Rückweisung, Kreditor-Anlage anfordern | smart invoice (M-01, M-02, M-05, M-06), REB, Lieferanten-App | invoices Buchhaltungsuser |
| R-03 | Sachliche Prüfer (Asset Manager, Objektbetreuer, Projektleiter, Fachbereich) | Livos | sachliche und rechnerische Prüfung, Kontierung ergänzen, Kürzung erfassen, Nachweise anhängen, Post des Fachbereichs bearbeiten | smart invoice (M-03), documents, mail dispatcher | invoices Freigabeuser; documents business, wenn Post/Akten aktiv genutzt werden |
| R-04 | Freigeber (Abteilungsleitung, Gesellschaftsverantwortliche, Geschäftsführung) | Livos | fachliche Freigabe gemäß Freigabematrix, PM-Freigabe (WF-03) | smart invoice (M-04, M-13), REB | invoices Freigabeuser (GF ggf. documents business für DMS/pilot) |
| R-05 | Zahlungsfreigeber | Livos (GF, kaufmännische Leitung, Treasury) | Zahlungsfreigabe in d.velop; Unterschrift in multicash | smart invoice (M-04), multicash | invoices Freigabeuser + multicash |
| R-06 | Buchhaltung (Trios) | extern (Dienstleister) | Buchhaltungsschritt, Übergabe an DATEV, Kreditorenanlage in DATEV | smart invoice (M-07), DATEV | invoices Buchhaltungsuser (Zulässigkeit extern: OP-03) |
| R-07 | Controlling / Management | Livos | REB-Sichten, Auswertungen, evidanza | REB (M-09), evidanza | documents business (lesend) / Freigabeuser |
| R-08 | Externe Kernpartner (Projektsteuerer, Architekten) | extern | Prüfung/Freigabe von Bau-Rechnungen im Web | smart invoice (M-03/M-04) | invoices Freigabeuser (Zulässigkeit Dritte: OP-03) |
| R-09 | Property Manager (HV) | extern | reichen Freigabe-Rechnungen per E-Mail ein, erhalten Freigabe-Mail | E-Mail | keine Lizenz |
| R-10 | Ad-hoc-Externe | extern | Stellungnahme zu einer Rechnung per externer Benutzeraufgabe; die verbindliche Freigabe erfolgt intern (Kapitel 11.5.3) | E-Mail-Link, Formular (M-19) | keine Lizenz |
| R-11 | Vertragsmanager / Vertragsverantwortliche | Livos | Verträge anlegen, Fristen, Vertragsfreigabe | d.velop contracts (M-14) | contracts voll (+ documents business) |
| R-12 | Fachadministration / Key-User | Livos | Stammdatenpflege (Lieferanten-App), Freigabematrix, Gruppenanträge, Vertretung für Dritte setzen, Rezertifizierung | Lieferanten-App (M-16), smart-invoice-Administration (M-17), M-18 | documents business + Admin-Rechte (fachlich) |
| R-13 | Technischer Benutzer BeSync | MDIS | API-Zugriff: Stammdaten, Datasets, Restriction Sets, Webhooks, Export | APIs | technischer Benutzer |
| R-14 | Betriebsprüfer (Z1) | extern, temporär | Nur-Lese-Zugriff, gefiltert auf Gesellschaft und Prüfungszeitraum | Suche, Akten | documents (temporär; Lizenzfrage OP-45) |
| R-15 | MDIS Betrieb / Support | MDIS | Tenant-Administration, Monitoring BeSync, Konfigurationsänderungen nach Freigabe | Administration | Admin |

Rollen sind **kombinierbar**. Eine Person kann z. B. R-03 für ein Objekt und R-04 für eine Gesellschaft sein. Die Kombination Prüfer = Freigeber für denselben Beleg verhindert smart invoice im Standard (AE-05).

**Trennung unverträglicher Rollen (Vorschlag):**

| Kombination | Regel |
|---|---|
| R-02 und R-05 in derselben Person | nicht zulässig (Erfassung und Zahlungsfreigabe getrennt) |
| R-06 (Trios) und R-05 | nicht zulässig |
| R-12 und R-05 | nur mit Freigabe der Geschäftsführung; Rechteänderungen dann durch Dritte |
| R-15 mit fachlichen Rollen | nicht zulässig; MDIS erhält keine Fachrechte im Produktivsystem |

---

## 13.2 Grundmodell der Cloud-Berechtigungen

### 13.2.1 Bausteine

Die Cloud-Berechtigungen sind über die öffentliche DmsConfig API vollständig beschrieben (DmsConfig API, d.velop). Die Funktionsbeschreibung nennt das Prinzip „Rollen- und attributbasierte Berechtigungsverwaltung".

| Baustein | Bedeutung | Status |
|---|---|---|
| **Permission** | gilt für **genau eine Kategorie** und kann über weitere Eigenschaftswerte eingeschränkt werden. Sie wird Gruppen oder Apps zugeordnet | [S] |
| **Rechtestufe** | `read` (Lesen), `write` (Bearbeiten **und Anlegen**), `delete` (Löschen), je Zuordnung getrennt | [S] |
| **Zustände** | `ALLOWED` (erteilt), `INHERITED` (nicht erteilt; andere Permissions entscheiden, sonst wie verweigert), `DENIED` (verweigert; **setzt sich immer durch**) | [S] |
| Abhängigkeiten | `write` und `delete` setzen `read` voraus; `read = DENIED` erzwingt auch `write` und `delete = DENIED` | [S] |
| **Restriction Set** | dynamische Werteliste je Gruppe (z. B. Mandanten-IDs). Ein Benutzer ist berechtigt, wenn der Eigenschaftswert in der Liste liegt, die sich aus seinen Gruppenmitgliedschaften ergibt. Einbindung in der Permission über `@Filter([Filter-ID])` | [S] |
| **Platzhalter** | `@CURRENT_USER` (ID des angemeldeten Benutzers), `@CURRENT_USER_EMAIL`, `@CURRENT_USER_IN_GROUP` (Gruppen-ID, in der der Benutzer Mitglied ist) | [S] |
| Operatoren | Bereich `|-`, `*`, `?` (z. B. Datumsbereich für Betriebsprüfer) | [S] |
| Systemeigenschaften | `STATUS`, `OWNER`, `EDITOR`, `CATEGORY` u. a. sind in Permissions nutzbar (z. B. „nur Status Freigabe") | [S] |
| Löschsperre der Kategorie | `preventDeletion` verhindert das Löschen freigegebener und archivierter Elemente und **übersteuert alle Löschrechte** | [S] |

Eigene Rechte für Statuswechsel, Verknüpfen, Export oder Aktivitäten-Lesen kennt die Cloud-API nicht. Ob die Oberfläche mehr anbietet, klärt Test T11 [O]. Der Menüpfad für Berechtigungen, Restriction Sets und Strukturregeln ist öffentlich nicht dokumentiert und wird am Test-Tenant erhoben (Test T01).

### 13.2.2 Muster: Permission je Kategorie × Rechtestufe

Für jede Kategorie K-01 bis K-15 entstehen dieselben Permission-Typen. Nicht jede Kategorie braucht jeden Typ.

| Permission-Typ (Namensmuster) | Einschränkung (Restrictions) | Zuordnung | Zweck |
|---|---|---|---|
| `Kxx_M_Lesen` | `CATEGORY = Kxx`; `Mandant = @Filter(RS_Mandant_Lesen)` | Rollengruppen mit Leserecht | Lesen nur eigene Gesellschaften |
| `Kxx_M_Bearbeiten` | `CATEGORY = Kxx`; `Mandant = @Filter(RS_Mandant_Bearbeiten)` | Rollengruppen mit Schreibrecht | Bearbeiten nur eigene Gesellschaften |
| `Kxx_A_Zentral` | `CATEGORY = Kxx` (ohne Mandant-Filter) | zentrale Rollen (R-02, R-06, R-12, R-13) | bewusst vergebenes „alle Gesellschaften" |
| `Kxx_O_Lesen` / `Kxx_O_Bearbeiten` | `CATEGORY = Kxx`; `Objekt-ID = @Filter(RS_Objekt)` | Projektleitung, externe Kernpartner | nur freigegebene Objekte |
| `K01_W_User` / `K01_W_Group` | `CATEGORY = K-01`; `WorkflowbeteiligteIDs = @CURRENT_USER` bzw. `@CURRENT_USER_IN_GROUP` | alle Workflowteilnehmer | Beteiligte lesen „ihre" Rechnung (bewusste Ausnahme von der Gesellschaftstrennung) |
| `Kxx_Admin` | `CATEGORY = Kxx` | `DMS_R_Fachadmin` | Lesen, Schreiben, Löschen (Löschsperre wirkt weiter) |
| `Kxx_Sperre` (optional) | `CATEGORY = Kxx`; z. B. `Vertraulichkeit = hoch` | nicht berechtigte Gruppen: `DENIED` | harte Sperre (Wirkung über Gruppen: Test T07) |

Das smart-invoice-Onboarding legt für Rechnungen bereits Berechtigungsprofile nach dem Muster „[ALL] / [Group] / [User]" und die Mehrfacheigenschaften „Workflowbeteiligte" und „WorkflowbeteiligteIDs" an (smart invoice: Administrieren, cloud). Diese Profile werden übernommen und an das Livos-Modell angepasst. Ihre exakte Einschränkung wird vorher nur lesend dokumentiert (Test T12).

**Mengengerüst:** 15 Kategorien × 3 bis 6 Permission-Typen ergeben etwa **50 bis 70 Permissions**, unabhängig von der Zahl der Gesellschaften.

### 13.2.3 Restriction Sets

| Set | Zuordnung (Gruppe → Werte), Beispiel | Zweck | Status |
|---|---|---|---|
| `RS_Mandant_Lesen` | `DMS_G_10010 → [10010]`; `DMS_GF_Nord → [10010, 10020, 10050]` | Leserecht je Gesellschaft bzw. Verbund | [S] Mechanik |
| `RS_Mandant_Bearbeiten` | `DMS_GB_10010 → [10010]` | Schreibrecht nur dort, wo bearbeitet wird | [S] Mechanik |
| `RS_Objekt` | `DMS_O_4711 → [4711]` | Projektleitung und Kernpartner nur für ein Objekt | [S] Mechanik |

Warum zwei Mandanten-Sets: Die Werteliste ergibt sich aus **allen** Gruppen eines Benutzers (Kernannahme, Test T03). Wer in Gesellschaft A bearbeitet und in B nur liest, bekäme mit einem einzigen Set auch in B Schreibrechte. Getrennte Sets je Rechtestufe verhindern das.

**Achtung – leere Liste = alle Werte.** Laut API erlaubt eine leere Werteliste **alle** Werte („An empty array allows all values"). Eine Zuordnung ohne Gruppe (`NO_ASSIGNMENT`) gilt für alle Gruppen. Daher gelten verbindlich:

| Regel | Umsetzung |
|---|---|
| Keine leeren Wertelisten | BeSync prüft täglich alle Zuordnungen und meldet leere Listen als Fehler [A] |
| Keine `NO_ASSIGNMENT`-Zuordnung | Prüfung wie oben |
| „Alle Gesellschaften" nie über das Set | zentrale Rollen erhalten eine eigene Permission ohne Mandant-Filter (`Kxx_A_Zentral`), damit „alle" sichtbar und bewusst vergeben ist |
| Schlüssel mit fester Länge | Mandanten-IDs einheitlich formatieren (AE-03), damit kein Teilstring-Treffer entsteht (Test T08) |
| Dokumente ohne Mandant | Pflichtfeld in allen Kategorien; Verhalten leerer Werte testen (Test T05) |

---

## 13.3 Gruppenmodell

### 13.3.1 Identitäten aus Microsoft Entra ID

| Element | Festlegung | Status |
|---|---|---|
| Identitätsquelle | Microsoft Entra ID (Voraussetzung M365/Entra bei Livos, OP-16) | [K] |
| Anmeldung | Single Sign-on über OpenID Connect (ab Edition business) | [S] |
| Provisionierung | SCIM 2.0 an `https://<Tenant>/usermanagement/scim` mit dem Provisioning-Benutzer; Entra stellt Benutzer und Gruppen bereit, deaktiviert bei Scope-Verlust | [S] |
| **Flache Gruppen** | Entra stellt nur **direkte** Mitglieder zugewiesener Gruppen bereit, keine verschachtelten. Alle DMS-Gruppen sind daher flach | [S] (Microsoft) |
| Gruppentypen d.velop | Rollengruppen als Berechtigungsgruppen; Gesellschafts- und Objektgruppen als „Hidden" (reine Werteträger) | [S] / [K] |
| Globale Gruppen | nur wenn zwingend nötig (Leistung, nicht umkehrbar) | [S] |
| Technische Benutzer | technische Benutzergruppe ohne interaktive Anmeldung, nur API-Schlüssel (R-13) | [S] |
| Externe ohne Entra | Kernpartner per Einladung in die d.velop cloud oder als Entra-B2B-Gast (per SCIM bereitstellbar) | [S] / [K] |

### 13.3.2 Gruppenarten und Namenskonvention

| Gruppenart | Muster | Beispiel | Zweck | Anzahl (Schätzung) |
|---|---|---|---|---|
| Rollengruppen DMS | `DMS_R_<Rolle>` | `DMS_R_Post`, `DMS_R_Rechnungseingang`, `DMS_R_Pruefer`, `DMS_R_Freigeber`, `DMS_R_Zahlung`, `DMS_R_Buchhaltung_Extern`, `DMS_R_Controlling`, `DMS_R_Partner_Extern`, `DMS_R_Vertrag`, `DMS_R_Fachadmin`, `DMS_R_Betriebspruefung` | Träger der Permissions (welche Kategorie, welches Recht) | 10–12 |
| Gesellschaftsgruppen (Lesen) | `DMS_G_<MandantNr>` | `DMS_G_10010` | Werteträger in `RS_Mandant_Lesen` | eine je Gesellschaft (>100) |
| Gesellschaftsgruppen (Bearbeiten) | `DMS_GB_<MandantNr>` | `DMS_GB_10010` | Werteträger in `RS_Mandant_Bearbeiten` | nach Bedarf |
| Verbundgruppen | `DMS_GF_<Verbund>` | `DMS_GF_Nord` (Beispiel) | Werteliste aller Gesellschaften eines Verbunds, z. B. für die Geschäftsführung | nach Bedarf |
| Objektgruppen | `DMS_O_<ObjektID>` | `DMS_O_4711` | Werteträger in `RS_Objekt` | nur wo Objektzugriff nötig |
| smart invoice (Onboarding) | `dv_*` | `dv_Buchhaltung`, `dv_Freigeber`, `dv_Sachliche_Prüfer`, `dv_Workflowteilnehmer`, `dv_inbound`, `dv_inbound_Administratoren`, `dv_Service_Accounts` | Standardrollen des Rechnungsworkflows | 7 |
| smart invoice je Mandant | `SI_<Rolle>_<MandantNr>` | `SI_Pruefer_10010`, `SI_Freigeber_10010`, `SI_Clearing_10010`, `SI_REB_10010` | Bearbeiterfindung, Clearing, REB je Mandant | Rollen × Gesellschaften |
| Post | `POST_<Verbund>_<Funktion>` | `POST_Nord_Asset` | Empfängergruppen im mail dispatcher | nach Postkatalog |
| contracts | `VTR_<Organisation>_<Rolle>` | `VTR_Nord_Leser` | Rechte je Organisation × Vertragstyp | nach Kapitel 12.1.9 |
| Technisch | `TEC_BeSync` | – | API-Zugriff (R-13) | 1–3 |

Grenzen: smart invoice erlaubt bis zu **2.500 Gruppen** je Bucket (Leistungsbeschreibung d.velop invoices 12/2025). Bei 120 Gesellschaften und vier `SI_`-Rollen entstehen rund 480 Gruppen. Das liegt innerhalb der Grenze. Obergrenzen für DMS-Gruppen, Permissions und Restriction-Set-Zuordnungen sind nicht dokumentiert und werden bei d.velop angefragt [O, OP-40].

### 13.3.3 Zusammenspiel Rolle × Gesellschaft (Beispiel)

| Person (Beispiel) | Gruppen | Wirkung |
|---|---|---|
| Asset Managerin Gesellschaft 10010 und 10020 | `DMS_R_Pruefer`, `DMS_G_10010`, `DMS_G_10020`, `DMS_GB_10010`, `DMS_GB_10020`, `SI_Pruefer_10010`, `SI_Pruefer_10020` | liest und bearbeitet Dokumente beider Gesellschaften; erhält Prüfaufgaben beider Gesellschaften |
| Geschäftsführer Verbund Nord | `DMS_R_Freigeber`, `DMS_GF_Nord`, `SI_Freigeber_<Nr>` je Gesellschaft | liest alle Dokumente des Verbunds, gibt gemäß Matrix frei |
| Projektleiter Objekt 4711 | `DMS_R_Pruefer`, `DMS_O_4711` | liest Objekt- und Vorgangsdokumente nur dieses Objekts; Rechnungen als Workflowbeteiligter |
| Mitarbeiterin Trios | `DMS_R_Buchhaltung_Extern`, `dv_Buchhaltung` | alle Gesellschaften (zentrale Buchhaltung), keine Verträge, keine Post |

---

## 13.4 Berechtigungsmatrix Rolle × Kategorie × Recht

**Legende:** L = Lesen · S = Schreiben (Bearbeiten und Anlegen) · Lö = Löschen · – = kein Zugriff.
Geltungsbereich in Klammern: **(M)** eigene Gesellschaften über `RS_Mandant_Lesen`/`_Bearbeiten` · **(A)** alle Gesellschaften (eigene Permission ohne Filter) · **(O)** nur freigegebene Objekte über `RS_Objekt` · **(W)** nur als Workflowbeteiligter · **(T)** temporär, gefiltert auf Gesellschaft und Prüfungszeitraum.
Kategorien: K-01 Eingangsrechnung · K-02 Rechnungsanlage/Nachweis · K-03 Auftrag/Bestellung · K-04 Angebot · K-05 Vertrag · K-06 Bescheinigung · K-07 Korrespondenz · K-08 BIM4You-Prüfbericht · K-09 Sonstiges Posteingangsdokument · K-10 Gesellschaftsakte · K-11 Objektakte · K-12 Kreditorenakte · K-13 Vorgangsakte · K-14 Vertragsakte · K-15 Organisationsunterlage.

| Rolle | K-01 | K-02 | K-03 | K-04 | K-05 | K-06 | K-07 | K-08 | K-09 | K-10 | K-11 | K-12 | K-13 | K-14 | K-15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R-01 Poststelle | – | L/S (A) | L/S (A) | L/S (A) | – | L/S (A) | L/S (A) | – | L/S (A) | – | – | – | – | – | – |
| R-02 Rechnungseingang | L/S (A) | L/S (A) | L (A) | L (A) | – | L/S (A) | L/S (A) | L (A) | – | L (A) | L (A) | L (A) | L (A) | – | L (A) |
| R-03 Sachliche Prüfer ¹ | L (W) + L (M) | L/S (M) | L/S (M) | L/S (M) | L (M) | L (M) | L/S (M) | L (M) | L/S (M) | L (M) | L (M) | L (M) | L (M) | L (M) | – |
| R-04 Freigeber (inkl. GF) ² | L (W) + L (M) | L (M) | L (M) | L (M) | L (M) | L (M) | L (M) | L (M) | L (M) | L (M) | L (M) | L (M) | L (M) | L (M) | L (M) |
| R-05 Zahlungsfreigeber | L (W) + L (M) | L (M) | – | – | – | L (M) | – | L (M) | L/S (M) | L (M) | – | L (M) | – | – | – |
| R-06 Buchhaltung Trios | L/S (A) | L (A) | L (A) | – | – | L (A) | L (A) | L (A) | – | L (A) | L (A) | L (A) | L (A) | – | L (A) |
| R-07 Controlling/Management ³ | L (M) | L (M) | L (M) | L (M) | L (M) | L (M) | L (M) | L (M) | – | L (M) | L (M) | L (M) | L (M) | L (M) | L (M) |
| R-08 Externe Kernpartner | L (W) | L/S (O) | L (O) | – | – | – | – | L (O) | – | – | L (O) | – | L (O) | – | – |
| R-09 Property Manager | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – |
| R-10 Ad-hoc-Externe | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – |
| R-11 Vertragsmanager | L (M) | L (M) | L/S (M) | L/S (M) | L/S (M) | L (M) | L/S (M) | L (M) | L/S (M) | L (M) | L (M) | L (M) | L (M) | L/S (M) | – |
| R-12 Fachadministration ⁴ | L/S/Lö (A) | L/S/Lö (A) | L/S/Lö (A) | L/S/Lö (A) | L/S/Lö (A) | L/S/Lö (A) | L/S/Lö (A) | L/S/Lö (A) | L/S/Lö (A) | L/S/Lö (A) | L/S/Lö (A) | L/S/Lö (A) | L/S/Lö (A) | L/S/Lö (A) | L/S/Lö (A) |
| R-13 Technischer Benutzer BeSync ⁵ | L/S (A) | L (A) | L (A) | L (A) | L (A) | L (A) | L/S (A) | L/S (A) | L (A) | L (A) | L (A) | L (A) | L (A) | L (A) | L/S (A) |
| R-14 Betriebsprüfer ⁶ | L (T) | L (T) | L (T) | – | L (T) | L (T) | L (T) | L (T) | – | L (T) | L (T) | L (T) | L (T) | L (T) | L (T) |
| R-15 MDIS Betrieb ⁷ | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – |

Anmerkungen:

1. **R-03:** Für Projektleitung und Objektbetreuung mit reinem Objektbezug gilt (O) statt (M). Schreibrecht auf K-02 dient dem Anhängen von Nachweisen, auf K-09 der Übernahme verteilter Post („Es ist für mich" wechselt die Kategorie). Rechnungsdaten ändert R-03 nur im smart-invoice-Workflow, nicht als DMS-Eigenschaft.
2. **R-04:** Die Geschäftsführung erhält den Geltungsbereich über `DMS_GF_<Verbund>`.
3. **R-07:** Zentrales Konzern-Controlling kann (A) statt (M) erhalten; Entscheidung Livos.
4. **R-12:** Löschen wirkt nur auf Elemente im Status Bearbeitung. Freigegebene und archivierte Elemente schützt die Löschsperre (`preventDeletion`), die alle Löschrechte übersteuert. Versions-Löschrechte nur für R-12 (GoBD).
5. **R-13:** Schreibrecht auf K-01 für die DMS-Eigenschaften aus BeSync (E-07, E-21, E-22, E-23); auf K-15 für BeSync-Prüfberichte (Restriction Sets, Rezertifizierung); auf K-07 für abgelegte Rückweisungs-/PM-Mails (AE-12, AE-13); auf K-08 für BIM4You-Prüfberichte. Leserecht auf alle Kategorien für den Export je Gesellschaft (S-15); zusätzlich Recht „Datenexport" für die repo export-API.
6. **R-14:** Nur Lesen, Filter auf die geprüfte(n) Gesellschaft(en) über eine eigene Gruppe `DMS_G_Pruefung_<Anlass>` und auf den Prüfungszeitraum über einen Datumsbereich (z. B. Rechnungsdatum `01.01.2022|-31.12.2024`, Beispiel). K-04 und K-09 nur nach Einzelfreigabe durch die Steuerabteilung.
7. **R-15:** Tenant-Administration ohne Fachrechte. Inhaltszugriff nur anlassbezogen über eine befristete Supportgruppe mit Freigabe durch Livos (13.8).

**Zusätzliche Rechte außerhalb der DMS-Matrix:**

| System | Recht | Rollen |
|---|---|---|
| d.velop contracts | Lesen/Schreiben/Löschen je Organisation × Vertragstyp (Kapitel 12.1.9) | R-11 (L/S), R-04/R-07 (L), R-12 (L/S/Lö) |
| mail dispatcher | Mitglied einer Empfängergruppe `POST_*` | R-01, R-03, R-05, R-11 und Fachbereiche |
| process studio | Zugangsberechtigung zum Modellieren (Konfiguration > Aufgaben und Prozesse > Prozessstudio > Zugangsberechtigungen); Prozessstart einschränkbar | R-15 (Modellierung), R-12 (Test) |
| d.velop pilot | Nutzung im gebuchten Mandanten; Assistenten je Kategorie/Filter | alle documents-business-Nutzer; Assistenten nach Verbund (12.1.10) |
| Lieferanten-App (BeSync) | App-eigene Rollen: Lesen, Pflegen, Mapping bestätigen | R-02 (Anlage anfordern), R-12 (Pflege), R-06 (Rückmeldung Anlage) |

---

## 13.5 Rechte in smart invoice

### 13.5.1 Lizenzrollen

| Lizenzrolle | Darf (Leistungsbeschreibung d.velop invoices 12/2025) | Darf nicht | Livos-Rollen |
|---|---|---|---|
| **Buchhaltungsuser** | Erfassung/Import, Kreditor- und Rechnungsinformationen ergänzen, buchen, an ERP/FiBu übergeben, Dokumente und Akten verwalten | – | R-02, R-06 (Paket Medium: bis 10 Buchhaltungsuser) |
| **Freigabeuser** | Prüfer auswählen, Rechnungen prüfen, Lieferscheine anhängen, Notizen/Kommentare, Annotationen, Positionsdaten ergänzen | buchen, an FiBu übergeben, Akten verwalten; volle DMS-Nutzung | R-03, R-04, R-05, R-07, R-08 (Anzahl beliebig) |

Ob Dritte (Trios, Projektsteuerer, PM mit Konto) Buchhaltungs- oder Freigabeuser sein dürfen, ist lizenzrechtlich mit d.velop zu klären (OP-03).

### 13.5.2 Bearbeiterfindung und Freigabematrix

| Element | Festlegung | Status |
|---|---|---|
| Sachliche Prüfer | Bearbeiterfindung je Mandant über die Gruppe `SI_Pruefer_<MandantNr>` bzw. über die Auswahl in der Verteilung. Eine Regel für alle Gesellschaften: Gruppenname gegen `voucher.company.nr` (Muster laut Handbuch) | [S] Mechanik / [O] Test T21 |
| Freigabematrix | Spalten: Bearbeiter (Person/Gruppe) und Freigabegrenze (fest) plus bis zu 20 weitere Spalten, z. B. **Mandant**, Kostenstelle, Kostenträger/Objekt. Grenze gilt je **Kostenobjekt**. Groß-/Kleinschreibung der Werte ist relevant | [S] |
| Pflege der Matrix | durch R-12 in der smart-invoice-Administration (M-17) oder per API-Import (Zeilen im Batch) aus der Lieferanten-App/BeSync [A]; jede Änderung mit Vier-Augen-Freigabe (13.8) | [S] / [K] |
| Prüfer ≠ Freigeber | Standard in smart invoice | [S] |
| Zahlungsfreigabe | eigener Schritt mit Bearbeiterfindung `SI_Zahlung_<MandantNr>` bzw. je Verbund (Vorschlag) | [K] |

### 13.5.3 Rechnungseingangsbuch je Mandant

| Sicht | Berechtigung | Rollen |
|---|---|---|
| Meine offenen Rechnungen, Rechnungen in Vertretung, An mich eskalierte Rechnungen | automatisch für Workflowbeteiligte | alle Workflowrollen |
| **Alle offenen Rechnungen – global** | Settings > Berechtigung > „Globale Rechnungsliste" je Gruppe | R-02, R-06, R-12, zentrales Controlling |
| **Alle offenen Rechnungen – je Mandant** | Settings > Berechtigung > Workflowberechtigungen > Neue Berechtigung: Gruppe + Mandantennummer (Beispiel `SI_REB_10010` → 10010) | R-04 Gesellschaftsverantwortliche, R-07 |
| Archiv | wie oben, 6 Monate (erweiterbar auf 12 Monate) | wie oben |

Je Eintrag ist laut Beispiel **eine** Mandantennummer möglich. Ob mehrere Mandanten oder Platzhalter je Eintrag gehen, klärt Test T20. Eine API für diese Berechtigungen ist nicht dokumentiert. Bei neuen Gesellschaften pflegt R-12 sie daher manuell (13.9) [O].

### 13.5.4 Clearing-Gruppen

Das Clearing wird je Workflowdefinition aktiviert. Es berechtigt „individuelle Gruppen für jeden Mandanten" (Mandanten-ID → Gruppe) (smart invoice: Administrieren, cloud).

| Clearing-Fall | Gruppe (Vorschlag) | Rolle |
|---|---|---|
| Standard für alle Mandanten | `SI_Clearing_Zentral` | R-02 |
| je Mandant bzw. Verbund, wenn dezentral geklärt wird | `SI_Clearing_<MandantNr>` | Gesellschaftsverantwortliche |
| Klärfall-Mandant (Mandant unbekannt, WF-04) | `SI_Clearing_Zentral` | R-02 |

---

## 13.6 Externe Beteiligte

### 13.6.1 Zugangswege

| Externe | Rolle | Zugang | Rechte | Befristung | Status |
|---|---|---|---|---|---|
| Trios (Buchhaltungsdienstleister) | R-06 | benanntes d.velop-Konto je Mitarbeiter (Einladung oder Entra-B2B-Gast), SSO nur, wenn Trios-Identitäten angebunden werden | smart invoice Buchhaltungsschritt, DMS lt. Matrix (A), keine Verträge/Post | Vertragslaufzeit Dienstleistung; Rezertifizierung halbjährlich | [S] / OP-03 |
| Externe Kernpartner (Projektsteuerer, Architekten) | R-08 | Einladung per E-Mail in die d.velop cloud, Freigabeuser | Rechnungen als Workflowbeteiligter (W), Objektdokumente (O) | an Projektlaufzeit gebunden; Ablaufdatum im Antrag | [S] / OP-03 |
| Property Manager | R-09 | kein Konto; E-Mail an `freigabe-hv@…`, Rückmeldung per E-Mail (AE-12) | keine | – | [K] / [A] |
| Ad-hoc-Externe | R-10 | externe Benutzeraufgabe (E-Mail-Link auf Formular, kein Konto), Beleg als Teilen-Link | nur die im Formular freigegebenen Daten; Formular ohne Dokumentzugriff | Timer der Aufgabe (Pflicht); Teilen-Link max. 180 Tage | [S] / [A] (Kopplung) |
| Betriebsprüfer | R-14 | temporäres Konto, Nur-Lesen | (T) lt. Matrix | Dauer der Außenprüfung; Deaktivierung am Prüfungsende | [K] / OP-45 |
| MDIS Support | R-15 | Supportzugang über *Infrastruktur und Sicherheit > Supportzugang* | nur Administration | Support max. 7 Tage, benannte Consultants max. 12 Monate; nur durch Livos vergebbar; Zugriffe werden protokolliert | [S] |

### 13.6.2 Sicherheitsvorgaben für externe Konten

| Vorgabe | Festlegung | Status |
|---|---|---|
| Zweiter Faktor | Pflicht für alle externen Konten: TOTP-2FA (alle Editionen) oder FIDO2-Anmeldung | [S] |
| FIDO2 | empfohlen für R-06 und R-08 mit Freigaberecht | [S] |
| Konto je Person | keine Sammelkonten; Namenskennzeichnung „(extern)" im Anzeigenamen | [K] |
| Befristung | jedes externe Konto hat ein Ablaufdatum im Antrag; Fachadministration deaktiviert zum Ablauf (Entra: Zugriffsüberprüfung, falls genutzt) | [K] |
| Minimalrechte | Kernpartner nur (W)/(O); keine Suche über Gesellschaften | [K] |
| Teilen-Links | nur „Lesen", kürzeste nötige Laufzeit, Übersicht „Geteilte Dokumente" monatlich prüfen | [K] |
| Protokoll | Anmeldungen, Rollen- und Konfigurationsänderungen protokolliert die Plattform (Vorhaltezeit 180 Tage) → quartalsweiser Export für die Rezertifizierung [A] | [S] / [A] |
| Offboarding | Deaktivieren statt Löschen (beim Löschen geht die eindeutige Benutzer-ID verloren) | [S] |

---

## 13.7 Vertretung und Rechte (Governance)

| Regel | Beschreibung | Status |
|---|---|---|
| Vertretung übernimmt Rechte | Die Vertretung übernimmt die Berechtigungen des Abwesenden für dessen Aufgaben. In smart invoice wird sie beim Öffnen der Aufgabe den Workflowbeteiligten hinzugefügt und liest damit die Rechnung, **auch über die Gesellschaftsgrenze hinweg** | [S] |
| Vertretung innerhalb des Verbunds | Vertretungen möglichst innerhalb derselben Gesellschaftsgruppe bzw. desselben Verbunds (AE-17) | Regel |
| Admin/Vorgesetzte setzen Abwesenheit | Benutzer mit administrativen Rechten (z. B. Vorgesetzte) setzen den Abwesenheitsstatus anderer Benutzer, z. B. bei Krankheit (T-39) | [S] |
| Aufgaben gesammelt weiterleiten | berechtigte Personen überwachen Aufgabenlisten anderer und leiten Aufgaben gesammelt weiter | [S] |
| Einschränkung Gruppenaufgaben | Die Vertretung sieht in smart invoice nur **persönlich** zugestellte Aufgaben. Gruppenaufgaben sehen ohnehin alle Gruppenmitglieder. Folge: Gruppen mit mindestens zwei Mitgliedern | [S] |
| Vertretungsausschluss | je Aufgabentyp abschaltbar (z. B. Zahlungsfreigabe nur durch benannte Zahlungsfreigeber-Vertretung) | [S] |
| Zahlungsfreigabe | Vertretung nur durch eine Person, die selbst R-05 hat | Regel |
| Prüfer ≠ Freigeber gilt auch in Vertretung | Vertretung darf nicht eigene Prüfung freigeben (Standardprüfung smart invoice) | [S] / Test |
| Nachweis | Abwesenheiten und Vertretungen sind in der Aufgabenhistorie sichtbar; Vertretungsliste je Quartal an die Rezertifizierung | [S] / [K] |

---

## 13.8 Administration

### 13.8.1 Administrationsebenen

| Ebene | Wer | Rechte | Status |
|---|---|---|---|
| Tenant-Administration | R-15 (MDIS Betrieb) und 1–2 benannte Livos-IT-Administratoren | Mitglied der Gruppe „Administrative group for the tenant". Nur Tenant-Administratoren konfigurieren das Repository (DmsConfig API): Kategorien, Eigenschaften, Permissions, Restriction Sets, Strukturregeln, Aufbewahrung | [S] |
| Fachadministration / Key-User | R-12 (Livos) | smart-invoice-Administration (Workflow-Einstellungen nach Absprache, Freigabematrix, REB-Berechtigungen, Clearing), Lieferanten-App, Abwesenheit für Dritte, Antrag von Rechteänderungen | [S] (smart invoice) / [K] |
| Technische Administration | R-13 (BeSync) | API-Schlüssel für Stammdaten, Datasets, Restriction-Set-Werte, Webhooks. Weil die DmsConfig API Tenant-Administratorrechte verlangt, ist der BeSync-Schlüssel hoch privilegiert → getrennter Schlüssel, Tresor, Rotation, Protokollierung | [S] / [A] |

**Keine delegierte DMS-Administration belegt.** Eine Sub-Administration (z. B. „Key-User pflegt nur Restriction Sets seiner Gesellschaften") ist für die Cloud nicht dokumentiert. Delegation gibt es nur fachlich: smart-invoice-Berechtigungen, business-objects-Rechte je Modell, contracts-Berechtigungsmatrix, Supportzugang. Das Konzept löst das so: Fachliche Rechteänderungen beantragt R-12. BeSync setzt die Werte automatisch aus dem Gesellschafts- und Objektstamm (S-04). Strukturelle Änderungen führt die Tenant-Administration durch.

### 13.8.2 Rechteänderungen mit Vier-Augen-Prinzip

| Schritt | Beschreibung | Wer |
|---|---|---|
| 1 Antrag | Antrag mit Person, Rolle, Gesellschaften/Objekten, Befristung, Begründung (Formular oder Ticket; Vorschlag: process-studio-Formular) | Führungskraft / R-12 |
| 2 Freigabe | Freigabe durch Gesellschaftsverantwortlichen bzw. Datenverantwortlichen, nicht durch den Antragsteller | R-04 / GF |
| 3 Umsetzung | Entra-Gruppenmitgliedschaft (IT) → SCIM; bei neuen Werten Restriction-Set-Zuordnung durch BeSync; smart-invoice-Gruppen/REB durch R-12 | Livos IT, R-13, R-12 |
| 4 Kontrolle | Testanmeldung oder Stichprobe; Protokoll (Antrag, Freigabe, Umsetzung) wird als Organisationsunterlage im DMS abgelegt | R-12 |
| Notfall | Sofortsperre ohne Vier-Augen zulässig (Deaktivierung), Nachdokumentation binnen 1 Arbeitstag (Vorschlag) | IT |

### 13.8.3 Rezertifizierung (Vorschlag)

| Prüfgegenstand | Intervall | Verantwortlich | Werkzeug |
|---|---|---|---|
| Mitglieder der Rollengruppen `DMS_R_*`, `SI_*`, `dv_*` | halbjährlich | Gesellschaftsverantwortliche | Export Gruppenmitglieder (usermanagement/SCIM) |
| Externe Konten (R-06, R-08, R-14) | quartalsweise | R-12 | Liste mit Ablaufdatum |
| Restriction-Set-Zuordnungen, leere Listen, `NO_ASSIGNMENT` | monatlich automatisch, Bericht halbjährlich | R-13 / R-12 | BeSync-Prüfbericht [A] |
| Freigabematrix | jährlich und bei Organisationsänderung | GF / R-12 | Matrix-Export |
| Teilen-Links, Supportzugänge | monatlich | R-12 | „Geteilte Dokumente", Supportzugang |
| Vertretungsregeln | halbjährlich | R-12 | Vertretungsübersicht |

---

## 13.9 Onboarding neuer Gesellschaften und Benutzer

### 13.9.1 Neue Gesellschaft

| Nr. | Schritt | Wer / wie | Automatisierbar |
|---|---|---|---|
| 1 | Gesellschaft im Gesellschaftsstamm der Lieferanten-App anlegen (Mandanten-ID = DATEV-Mandantennummer, Name exakt wie auf Rechnungen, Anschrift, Segment, Verbund, Verwaltungsart) | R-12 | – |
| 2 | Dataset-Wert „Mandant" in d.velop documents | BeSync (S-04) | ja [A] |
| 3 | Entra-Gruppen `DMS_G_<Nr>` (ggf. `DMS_GB_<Nr>`) anlegen, per SCIM bereitstellen | Livos IT | ja (Entra) |
| 4 | Restriction-Set-Zuordnung `DMS_G_<Nr> → [<Nr>]`; Verbundgruppe `DMS_GF_<Verbund>` um den Wert ergänzen | BeSync (S-04) | ja [A] |
| 5 | smart-invoice-Mandant (ID, Name, Anschrift) im Bucket | BeSync (S-04; Kapitel 8.7) | ja [A] |
| 6 | Gruppen `SI_Pruefer_<Nr>`, `SI_Freigeber_<Nr>`, ggf. `SI_Clearing_<Nr>`; Freigabematrix-Zeilen | Livos IT / R-12 (Matrix per API-Import [A]) | teilweise |
| 7 | REB-Workflowberechtigung je Mandant | R-12 manuell (keine API dokumentiert) | nein [O] |
| 8 | DATEV-Mandant in LDconnect (Stammdatenabruf, Übergabe) | Trios / LIONDEER | – |
| 9 | optional Alias-Postfach je Gesellschaft mit Mandanten-Vorbelegung (AE-22) | Livos IT / R-15 | – |
| 10 | Gesellschaftsakte entsteht automatisch mit dem ersten Dokument | System | ja [S] |
| 11 | Abnahmetest: Testbeleg, Sichtbarkeit (Mitglied/Nichtmitglied), REB, Freigabe | R-12 | – |

Aufwand je Gesellschaft: ein Dataset-Wert, eine bis zwei Gruppen, eine Set-Zuordnung, ein smart-invoice-Mandant, Matrix-Zeilen, eine REB-Berechtigung (AE-18).

**Gesellschaft verkauft oder liquidiert:** Export (AE-25, S-15), danach Zugriff über Entfernen der Set-Werte sperren, nicht löschen. Aufbewahrung beim Veräußerer klären.

### 13.9.2 Neuer Benutzer, Rollenwechsel, Austritt

| Anlass | Schritte | Wer |
|---|---|---|
| Neuer interner Benutzer | Antrag (13.8.2) → Entra-Gruppen (Rolle + Gesellschaften) → SCIM → Lizenzrolle in d.velop invoices/contracts zuordnen → Startseite (M-10) über Gruppensichtbarkeit → Kurzschulung | Führungskraft, IT, R-12 |
| Neuer Externer | wie oben, zusätzlich Ablaufdatum, 2FA/FIDO2-Pflicht, Einladung | R-12 |
| Rollenwechsel | alte Gruppen entfernen, neue Gruppen zuordnen; offene Aufgaben vorher weiterleiten | Führungskraft, R-12 |
| Austritt | offene Aufgaben weiterleiten, Abwesenheit mit Vertretung bis zur Deaktivierung, Entra-Deaktivierung → SCIM deaktiviert; Konto nicht löschen | Führungskraft, IT |
| Wirksamkeit | Zeit bis zur Wirksamkeit von Gruppenänderungen (Neuanmeldung nötig?) wird gemessen (Test T10) | R-12 |

---

## 13.10 Kritische Tests (OP-08)

Die Mechanik ist dokumentiert. Einige Verhaltensweisen sind aber nur durch Test zu bestätigen. Diese Tests laufen im Test-/Abnahme-Tenant (AE-01), nicht im MDIS-Demo-Tenant. Hinweis zur Benennung: Die Testnummern (T01 ff.) sind nicht identisch mit den Workshop-Anforderungen T-01 ff. im Anhang.

| Test | Aufbau | Erwartung | Folge bei negativem Ergebnis | Prio |
|---|---|---|---|---|
| **T03** Orthogonalität Rolle × Gesellschaft | Permission an `DMS_R_Pruefer` mit `Mandant = @Filter(RS_Mandant_Lesen)`; Werte nur über `DMS_G_10010`. Testbenutzer in beiden Gruppen | Benutzer sieht nur Dokumente von 10010; die Werteliste ergibt sich aus allen Gruppen des Benutzers | Kombinierte Gruppen `DMS_<Rolle>_<MandantNr>` (deutlich mehr Gruppen, weiter automatisierbar) | P1 |
| **T07** DENIED über Gruppen | Benutzer in zwei Gruppen, eine mit `DENIED` auf einer Kategorie | `DENIED` setzt sich gruppenübergreifend durch | Sperren nicht über DENIED, sondern über fehlende Zuordnung abbilden | P1 |
| **T12** smart-invoice-Profile (nur lesen) | vorhandene Profile „ERV – … [ALL]/[Group]/[User]" öffnen und dokumentieren | exakte Einschränkung (Platzhalter, Eigenschaft `WorkflowbeteiligteIDs`) bekannt | Profile `K01_W_*` gemäß Befund nachbauen | P1 |
| **T13** Aktenbildung Mehrfachregel | zwei Strukturregeln mit gleichem Kind (K-01) und verschiedenen Eltern (K-12, K-11); leeres Erkennungsfeld; `createSiblingDossiers` | Rechnung liegt automatisch in Kreditoren- **und** Objektakte; bei leerem Feld keine Verknüpfung | Objektakte über Mehrfachfeld oder manuelle Verknüpfung; Pflichtfelder verschärfen | P1 |
| T02 | Permission mit `RS_Test`, Benutzer in `DMS_G_10010` | Trennung in Suche, Akte und REB | Grundmodell überarbeiten | P1 |
| T04 | Mehrfachwert Mandant [10010, 10020] (Konzern-Rahmenvertrag) | sichtbar für beide Gesellschaften | Konzerndokumente je Gesellschaft ablegen | P2 |
| T05 | Dokument ohne Mandant | niemand außer Zentralrollen sieht es | Validierung per Webhook `validateimport` [A] | P1 |
| T06 | leere Werteliste, `NO_ASSIGNMENT` | bestätigt „alle Werte" → Governance-Regel 13.2.3 | – | P1 |
| T08 | `100` gegen `1001` | exakter Vergleich | feste Schlüssellänge | P2 |
| T10 | Gruppenänderung → Wirksamkeit | Minuten, keine Neuanmeldung | Onboarding-Hinweis | P2 |
| T11 | `write` ohne `delete`; Statuswechsel, Verknüpfen, Export | Rechtearten der Oberfläche bekannt | Matrix anpassen | P2 |
| T20 | REB-Workflowberechtigung mit mehreren Mandanten | ein Eintrag je Verbund möglich | Einträge je Gesellschaft pflegen | P2 |
| T21 | Bearbeiterfindung über Gruppenname und `voucher.company.nr` | eine Regel für alle Gesellschaften | Freigabematrix/Prüfermatrix je Mandant | P2 |
| T22 | Entra-SCIM + OIDC, B2B-Gast, Deaktivierung | Identitätskonzept bestätigt | Einladung statt B2B | P1 |

Die Ergebnisse gehen in die Abnahme des Berechtigungskonzepts ein. Solange T03 und T13 nicht bestätigt sind, bleiben Katalogpunkt 1.1 und die Mehrfachablage unter Vorbehalt.

# 14 Masken- und Oberflächenkonzept

Dieses Kapitel spezifiziert alle Masken und Oberflächen M-01 bis M-19. Es ist die fachliche Vorlage für die draw.io-Masken-Mockups: Feldnamen, Reihenfolge, Bereiche, Aktionen und Regeln sind so konkret angegeben, dass je Maske ein Mockup-Blatt entstehen kann. Die Feldnamen folgen den smart-invoice-Standardfeldern und dem Eigenschaftskatalog E-01 bis E-32.

Kennzeichnung: **[S]** Standard belegt · **[K]** Konfiguration · **[A]** Anpassung/Entwicklung (BeSync) · **[O]** offen/zu verifizieren. Beispielwerte (Grenzen, Fristen, Namen) sind Vorschläge.

---

## 14.0 Grundsätze

### 14.0.1 Gestaltungsregeln

| Nr. | Grundsatz | Konsequenz für die Masken |
|---|---|---|
| G-1 | **Standardmasken nutzen** (P2) | smart-invoice-Belegmaske, Rechnungseingangsbuch (REB), d.velop-documents-Ablage/Suche/Akte, contracts, mail dispatcher und Benutzerprofil werden konfiguriert, nicht nachgebaut. Eigene Oberflächen gibt es nur in der bestehenden Lieferanten-App (M-16) und im Formular für Ad-hoc-Externe (M-19) |
| G-2 | **Feldreihenfolge = Arbeitsreihenfolge** | Oben steht, was zuerst geprüft wird: Zuordnung (Mandant, Kreditor) → Belegkopf (Nummer, Datum, Beträge) → Zahlung (Bedingung, Fälligkeit, Bank) → Kostenobjekt und Routing → Positionen. In smart invoice ist der Kopfbereich ein Raster mit zwölf Spalten je Zeile, frei per Drag & Drop anzuordnen; es gibt ein globales Layout und schrittspezifische Layouts (smart invoice: Administrieren, cloud). In d.velop documents ergibt die Reihenfolge der zugewiesenen Eigenschaften die Maskenposition |
| G-3 | **Pflichtfelder sparsam** | Pflicht sind nur Felder, die Rechte, Aktenbildung, Routing oder Buchung tragen (Mandant, Kreditor, Belegkopf nach § 14 UStG, Kostenobjekt) und Begründungen bei Abweichungen (Kürzung, Rückweisung, Dublette). Pflicht wird je Schritt gesetzt (sichtbar/schreibbar/verpflichtend) |
| G-4 | **Hinweise statt Blockaden** (P7) | Abweichungen (IBAN, Zahlungsbedingung, Leistungsdatum fehlt, Skonto läuft ab) erscheinen als Hinweis oder Ampel. Blockiert wird nur, wo Recht oder Nachvollziehbarkeit es verlangen: Kürzungsgrund bei Zahlbetrag ≠ Brutto, Grund bei Rückweisung, Begründung bei Dublettenannahme |
| G-5 | **Links Daten, rechts Beleg** | Bearbeitungsmasken zeigen links die Belegdaten, rechts die Belegvorschau (PDF bzw. visualisierte E-Rechnung). Positionen unter dem Kopfbereich |
| G-6 | **Original bleibt unverändert** (P5) | Keine Maske bietet „Dokument bearbeiten" für Rechnungen. Korrekturen nur in Workflowdaten, Notizen, Annotationen |
| G-7 | **Dashboard-Grenze** | Die Startseite (M-10) nutzt nur die Standard-Widgets (Suche, Zuletzt bearbeitet, Beobachtet, Favorisiert), das Aufgaben- und REB-Widget sowie Verknüpfungs-Widgets auf REB-Schnellzugriffe und gespeicherte Suchen. Keine Kennzahlen-Diagramme in d.velop; Kennzahlen liefert das REB (M-09) bzw. evidanza (AE-16) |
| G-8 | **Sichtbarkeit ist keine Sicherheit** | Rollenabhängige Startseiten und ausgeblendete Felder ersetzen keine Berechtigung (Kapitel 13) |
| G-9 | **Einheitliche Begriffe** | Feldbezeichnungen in allen Masken gleich (Katalog E-xx). smart-invoice-Felder lassen sich je Workflow umbenennen, z. B. Kostenträger → „Objekt/KOST2" |

### 14.0.2 Legende der Feldtabellen

| Spalte | Werte |
|---|---|
| Quelle | **ERK** Erkennung (document reader, KI, E-Rechnung) · **STA** Stammdaten DATEV im smart-invoice-Bucket (LDconnect, S-02) · **LAP** Lieferanten-App/BeSync-Stamm (S-04) · **BES** BeSync-Rückmeldung (S-06, S-09) · **SYS** System/Workflow · **BER** berechnet · **MAN** manuell |
| Pflicht | ja · nein · bedingt (Bedingung im Hinweis) |
| Editierbar | **S** schreibbar · **R** nur lesen · **–** ausgeblendet |

### 14.0.3 Gemeinsamer Aufbau der smart-invoice-Belegmaske (M-02 bis M-07, M-13)

| Bereich | Position im Mockup | Inhalt | Status |
|---|---|---|---|
| Kopfzeile | oben, volle Breite | Schrittname, Mandantenname, Kreditorname, Rechnungsnummer, Bruttobetrag, Skontoampel, Status (z. B. „Clearing Modus", „Eskalation Stufe 1") | [S] |
| Hinweisleiste | unter der Kopfzeile | Dublettenhinweis, Hinweis Zahlungsbedingung weicht ab, E-Rechnungs-Prüfbericht, Hinweise aus Klärfall | [S] / [K] |
| Kopfdaten | links oben, Raster 12 Spalten | Felder in Arbeitsreihenfolge (Blöcke A–E, siehe 14.0.4) | [S] Layout / [K] Belegung |
| Positionsdaten | links unten, Tabelle | Positionen/Kontierungszeilen (Menge, Preis, Betrag, Steuerschlüssel, Sachkonto, Kostenstelle, KOST2, Zahlbetrag, Sachl. richtig) | [S] / [K] |
| Belegvorschau | rechts, volle Höhe | PDF bzw. visualisierte E-Rechnung; Annotationen; Anlagen (Lieferschein, Nachweis) | [S] |
| Register | rechts über der Vorschau | Beleg · Anlagen · Historie · Notizen · Belegänderungsansicht (wo konfiguriert) | [S] |
| Aktionsleiste | unten, rechtsbündig | schrittabhängige Aktionen (Schaltflächen); Standardaktion hervorgehoben | [S] / [K] |

### 14.0.4 Feldmatrix je Workflowschritt (Konfiguration „sichtbar/schreibbar/verpflichtend")

Schritte: **V** Verteilung (M-02) · **P** Sachliche Prüfung & Kontierung (M-03) · **F** Fachliche Freigabe (M-04) · **Z** Zahlungsfreigabe (M-04) · **B** Buchhaltung (M-07) · **K** Klärfall (M-05) · **H** PM-Freigabe (M-13, WF-03).
Werte: **P** = Pflicht und schreibbar · **S** = schreibbar · **R** = nur lesen · **–** = ausgeblendet · **b** = bedingt Pflicht.

| Block | Feld | Katalog | V | P | F | Z | B | K | H |
|---|---|---|---|---|---|---|---|---|---|
| A Zuordnung | Mandant | E-01 | P | R | R | R | R | P | P |
| A | Mandantenname | E-02 | R | R | R | R | R | R | R |
| A | Kreditor (Nr. und Name) | E-05/E-06 | P | R | R | R | S | P | S |
| A | Eingangskanal | E-25 | R | R | – | – | R | R | R |
| B Belegkopf | Belegart | E-14 | P | R | R | R | S | S | R |
| B | Rechnungsnummer | E-08 | P | R | R | R | R | S | S |
| B | Rechnungsdatum | E-09 | P | R | R | R | R | S | S |
| B | Leistungsdatum/-zeitraum | E-10 | S | R | R | – | S | S | – |
| B | Währung | – | S | R | R | R | R | S | R |
| B | Nettobetrag | E-11 | P | R | R | R | R | S | P |
| B | Steuerbetrag | E-11 | P | R | R | R | R | S | R |
| B | Bruttobetrag | E-11 | P | R | R | R | R | S | P |
| B | § 13b Reverse Charge | E-20 | S | R | R | – | S | S | – |
| C Zahlung | Zahlbetrag | E-12 | R | S | R | R | R | – | – |
| C | Kürzungsgrund | E-13 | – | b | R | R | R | – | – |
| C | Zahlungsbedingung | E-15 | S | R | R | R | S | S | – |
| C | Skontofälligkeit, Skontobetrag, Nettofälligkeit | E-15 | R | R | R | R | R | R | – |
| C | IBAN (Beleg) | E-16 | R | – | – | R | R | R | – |
| C | Bankverbindung (Stamm) | – | S | – | – | R | R | S | – |
| D Kostenobjekt | Objekt-ID / Objektbezeichnung | E-03/E-04 | b | S | R | R | R | S | P |
| D | Auftrags-/Vertragsnummer | E-19 | b | S | R | – | R | S | – |
| D | Gewerk / Vergabeeinheit | E-18 | b | S | R | – | R | S | – |
| D | Sachlicher Prüfer | – | P | S | R | – | – | S | – |
| D | Buchungstext | – | – | S | R | – | S | – | – |
| E Steuerung | Klärgrund | – | S | – | – | – | S | P | – |
| E | Rückweisungsgrund | E-26 | b | b | b | – | b | b | – |
| E | PM-Rückmeldetext / Ablehnungsgrund PM | – | – | – | – | – | – | – | b |
| Positionen | Positionstext | – | R | R | R | – | R | – | – |
| Positionen | Menge, Einzelpreis | – | R | S | R | – | R | – | – |
| Positionen | Positionsbetrag netto | – | R | R (berechnet) | R | – | R | – | – |
| Positionen | Steuerschlüssel | – | S | R | R | – | S | – | – |
| Positionen | Sachkonto | E-17 | S | S | R | – | S ¹ | – | – |
| Positionen | Kostenstelle | E-17 | S | S | R | – | S ¹ | – | – |
| Positionen | KOST2 / Kostenträger (Objekt) | E-17 | S | S | R | – | S ¹ | – | – |
| Positionen | Zahlbetrag (Position) | E-12 | – | S | R | – | R | – | – |
| Positionen | Sachl. richtig | – | – | S (b) | R | – | R | – | – |

¹ Option „Schreibbar wenn geprüft" für die abschließende Kontrolle durch die Buchhaltung [S].

**Custom-Felder (Budget):** smart invoice bietet je 20 Custom-Felder in Kopf und Positionen; Kopf-Custom-Felder lassen sich an Wertelisten („Custom Entities") binden [S]. Livos belegt im Kopf (Vorschlag): Objekt-ID, Auftrags-/Vertragsnummer, Gewerk/Vergabeeinheit, § 13b, Kürzungsgrund, Rückweisungsgrund, Klärgrund, Eingangskanal, PM-Rückmeldetext, Ablehnungsgrund PM. Das sind zehn von zwanzig Feldern.

**Nicht in der Belegmaske:** Lieferanten-Konsolidierungsnummer (E-07), FSB-Status (E-21), BIM4You-Ergebnis (E-22) und Zahlstatus (E-23) kommen über BeSync als **DMS-Eigenschaften** an den Beleg. Ein Schreibzugriff auf laufende smart-invoice-Belege per API ist nicht belegt (OP-07). Diese Werte sind in Akte, Suche und DMS-Eigenschaften sichtbar, nicht im Workflowformular.

### 14.0.5 Maskenübersicht

| ID | Maske | Rolle | Werkzeug | Umsetzung | Phase |
|---|---|---|---|---|---|
| M-01 | Rechnung einlesen / Stapel | R-02 | d.velop invoices, inbound | S/K | 1 |
| M-02 | Verteilung | R-02 | smart invoice | S/K | 1 |
| M-03 | Sachliche Prüfung & Kontierung | R-03, R-08 | smart invoice | S/K | 1 |
| M-04 | Fachliche Freigabe / Zahlungsfreigabe | R-04, R-05, R-08 | smart invoice | S/K | 1 |
| M-05 | Klärfall | R-02 | smart invoice + Lieferanten-App | K/A | 1 |
| M-06 | Rückweisungsdialog | R-02, R-03 | smart invoice + BeSync | K/A | 2 |
| M-07 | Buchhaltung | R-06 | smart invoice | S/K | 1 |
| M-08 | REB – Arbeitsansicht | alle | REB | S/K | 1 |
| M-09 | REB – Managementsicht | R-07 | REB | S/K | 1 |
| M-10 | Startseite/Dashboard je Rolle | alle | d.velop documents | S/K | 1 |
| M-11 | Aktenansicht Kreditoren-/Objektakte | alle | d.velop documents | S/K | 1 |
| M-12 | Suche / gespeicherte Suchen | alle | d.velop documents | S/K | 1 |
| M-13 | PM-Freigabe | R-04 | smart invoice (+ BeSync) | K/A | 2 |
| M-14 | Vertragsmaske | R-11 | d.velop contracts | S/K | 4 |
| M-15 | Postverteilung | R-01 (+ Fachbereiche) | inbound scan, mail dispatcher | S/K | 4 |
| M-16 | Lieferanten-App | R-12, R-02 | BeSync-App | A | 1 (Erweiterung) |
| M-17 | Freigabematrix-Pflege | R-12 | smart-invoice-Administration | S/K | 1 |
| M-18 | Vertretung / Abwesenheit | alle, R-12 | Benutzerprofil | S | 1 |
| M-19 | Externe Benutzeraufgabe | R-10 | process studio forms | K/A | 3 |

---

## 14.1 M-01 Rechnung einlesen / Stapel

| Merkmal | Beschreibung |
|---|---|
| Zweck | Rechnungen aus Upload, Scan und Postfach annehmen, Trennung und Vollständigkeit prüfen, an die Erkennung und smart invoice übergeben |
| Rolle | R-02 (Rechnungseingang); R-01 für Papierrechnungen aus der Post |
| Werkzeug / Aufruf | d.velop invoices „Rechnung einlesen" (Einzel- oder Mehrfach-Upload, im Workshop gezeigt); inbound-Stapelübersicht; Import-Widget auf der Startseite. Kommunikationsweg inbound → document reader → smart invoice (AE-22) |
| Umsetzung | [S] Funktion, [K] Importprofile, Postfächer, Schlüssel-Wert-Paare |

**Aufbau**

| Bereich | Position | Inhalt |
|---|---|---|
| Upload-Zone | oben | Drag & Drop, Schaltfläche „Dateien wählen", Scanner-Symbol (scanner connector) |
| Stapelliste | links | Stapel je Quelle mit Status |
| Stapelinhalt | Mitte | Seitenminiaturen mit Dokumenttrennern (Farben: KI-Vorschlag / manuell), Dokumentliste |
| Vorschau | rechts | Seite in Großansicht |

**Felder**

| Nr. | Feld | Quelle | Pflicht | Editierbar | Hinweis / Validierung |
|---|---|---|---|---|---|
| 1 | Stapelname | SYS (Postfach, Platzhalter Absender/Betreff) | ja | R | automatisch |
| 2 | Quelle / Postfach bzw. Alias | SYS | ja | R | z. B. `rechnung@…`, Alias je Gesellschaft |
| 3 | Importprofil | SYS | ja | R | bestimmt Standardkategorie, Trennung, OCR |
| 4 | Eingangsdatum/-zeit | SYS | ja | R | Grundlage für Durchlaufzeit |
| 5 | Mandant (Vorbelegung) | SYS (Schlüssel-Wert-Paar am Alias) | nein | R | nur bei Alias-Postfach; Test OP-02 |
| 6 | Anzahl Dokumente / Seiten | BER | – | R | Import hart auf 200 Seiten begrenzt |
| 7 | Dokumenttyp je Dokument (Rechnung / Anlage) | ERK / MAN | ja | S | Anlagen werden dem Rechnungs-PDF angehängt (Importprofil-Option) |
| 8 | Format | ERK | – | R | PDF, ZUGFeRD, XRechnung, Factur-X |
| 9 | E-Rechnungs-Prüfbericht | SYS | – | R | Validierung XRechnung; Voraussetzung neuer Kommunikationsweg |
| 10 | Status Stapel | SYS | – | R | offen · in Verarbeitung · abgeschlossen · Fehler |

**Aktionen**

| Aktion | Wirkung | Status |
|---|---|---|
| Hochladen / Scannen | legt Stapel an | [S] |
| Trenner setzen / entfernen | Dokumente trennen oder zusammenführen | [S] |
| Seite drehen / löschen | nur vor Übergabe (Fehlscan) | [S] |
| Dokument übernehmen / ablehnen | Haken je Dokument | [S] |
| Stapel abschließen / exportieren | Übergabe an Erkennung und Workflowstart; bei Postfächern automatisch („Stapel nach Import abschließen") | [S] / [K] |

**Regeln / Hinweise**

| Regel | Verhalten | Status |
|---|---|---|
| Postfach vor Aktivierung bereinigen | alle vorhandenen Mails werden importiert | [S] |
| Fehlermails | Ordner „dvelop_not_processed", Jobübersicht mit Neustart | [S] |
| Keine Nicht-Rechnungen | Post, Verträge nicht über ER-Postfach; Weiterleitung an `post@…` | Regel |

---

## 14.2 M-02 Verteilung

| Merkmal | Beschreibung |
|---|---|
| Zweck | Erkennungsergebnis prüfen und ergänzen, Mandant, Kreditor und Kostenobjekt zuordnen, sachlichen Prüfer bestimmen, Dubletten und Abweichungen erkennen, Klärfälle auslösen |
| Rolle | R-02 |
| Werkzeug / Aufruf | smart invoice, Schritt „Verteilung"; Aufruf aus „Meine Aufgaben", REB oder E-Mail-Benachrichtigung (abschaltbar, T-17) |
| Umsetzung | [S] Schritt und Maske, [K] Layout, Feldkonfiguration, Bedingungen, Custom-Felder |

**Aufbau:** gemeinsamer Aufbau 14.0.3. Kopfdaten in fünf Blöcken A–E, darunter Positionen, rechts Beleg.

**Felder (Reihenfolge = Mockup-Reihenfolge)**

| Nr. | Feld | Quelle | Pflicht | Editierbar | Hinweis / Validierung |
|---|---|---|---|---|---|
| A1 | Mandant | ERK (Name + Anschrift) / SYS (Alias) | ja | S | Auswahl aus Mandantenstamm. Leer oder unsicher → Aktion „Klärfall" (Mandant unbekannt). Erkennung nur über Name und Anschrift (AE-23) |
| A2 | Mandantenname | STA | – | R | zur Kontrolle |
| A3 | Kreditor | ERK (USt-IdNr., IBAN, Name) + STA | ja | S | Auswahl aus Kreditoren **des Mandanten**. Fehlt der Kreditor → „Klärfall" (Kreditor fehlt), WF-04 |
| A4 | Eingangskanal | SYS | – | R | E-Mail · Scan · E-Rechnung · Upload |
| B1 | Belegart | ERK / MAN | ja | S | Rechnung · Gutschrift · Abschlagsrechnung · Schlussrechnung · Stornorechnung; Abschlag/Schluss steuert Bau-Routing (WF-02) |
| B2 | Rechnungsnummer | ERK | ja | S | Dublettenprüfung (Kreditor + Rechnungsnummer) |
| B3 | Rechnungsdatum | ERK | ja | S | nicht in der Zukunft |
| B4 | Leistungsdatum/-zeitraum | ERK | nein | S | Hinweis, wenn leer (§ 14 UStG), keine Blockade |
| B5 | Währung | ERK | ja | S | Standard EUR |
| B6 | Nettobetrag | ERK | ja | S | Summenprüfung Kopf/Positionen |
| B7 | Steuerbetrag | ERK | ja | S | – |
| B8 | Bruttobetrag | ERK | ja | S | Netto + Steuer = Brutto |
| B9 | § 13b Reverse Charge | ERK / MAN | nein | S | Hinweis, wenn Kreditor als Bauleistender gekennzeichnet und Steuer > 0 [K]/[O] |
| C1 | Zahlungsbedingung | STA (Kreditor) / ERK | nein | S | **Hinweis, wenn die Zahlungsbedingung des Belegs von der Standardbedingung des Kreditors abweicht** [S] |
| C2 | Skontofälligkeit / Skontobetrag / Nettofälligkeit | BER | – | R | aus Zahlungsbedingung; manuelles Zahlungsziel nur, wenn im Workflow zugelassen (T-18) |
| C3 | IBAN (Beleg) | ERK | – | R | Abgleich mit Stamm-Bankverbindung; **Warnung bei Abweichung** (Anzeigeform Test OP-10) |
| C4 | Bankverbindung (Stamm) | STA | nein | S | Auswahl nur aus Stamm-Bankverbindungen des Kreditors |
| D1 | Objekt-ID / Objektbezeichnung | MAN / Custom Entity (LAP) | bedingt | S | Pflicht bei objektbezogenen Kosten und Bau; trägt Aktenbildung und Bearbeiterfindung |
| D2 | Auftrags-/Vertragsnummer | ERK / MAN | bedingt | S | Pflicht bei Abschlags-/Schlussrechnung |
| D3 | Gewerk / Vergabeeinheit | Custom Entity (BIM4You-Stamm, S-10) | bedingt | S | Pflicht bei Bau (WF-02) |
| D4 | Sachlicher Prüfer | SYS (Bearbeiterfindung) / MAN | ja | S | Vorschlag je Mandant/Objekt; Team oder Person |
| E1 | Klärgrund | MAN | bedingt | S | Pflicht bei Aktion „Klärfall" |
| Pos. | Positionen: Positionstext · Menge · Einzelpreis · Betrag · Steuerschlüssel · Sachkonto · Kostenstelle · KOST2/Kostenträger | ERK / STA / KI-Vorschlag | Sachkonto, Kostenstelle: ja | S | KI-Kontierungsvorschlag (C1) und kreditorenabhängige Kontierungsvorlagen; Split über mehrere Zeilen |

**Aktionen**

| Aktion | Wirkung | Status |
|---|---|---|
| Weiter zur sachlichen Prüfung (Standard) | Verbindung zu „Sachliche Prüfung"; Bau-Belege zusätzlich Routing WF-02 | [S] / [K] |
| Klärfall | Verbindung zu „Klärfall" (M-05) mit Klärgrund; Status „Clearing Modus" im REB | [S] / [K] |
| Dublette ablehnen | interner Abschluss „Abgelehnt – Dublette", **ohne** Lieferantenmail, Begründung Pflicht | [S] / [K] |
| Dublette annehmen | nur mit Begründung | [S] |
| An Lieferant zurückweisen | öffnet M-06 | [K] / [A] |
| Notiz hinzufügen | Notiz in der Historie | [S] |
| Teilen | Link/E-Mail (manuell) | [S] |

**Regeln / Hinweise**

| Regel | Auslöser | Verhalten | Status |
|---|---|---|---|
| Dublettenwarnung | gleicher Kreditor + Rechnungsnummer innerhalb von 18 Monaten; zusätzlich Prüfung im document reader | Hinweisleiste; Annahme nur mit Begründung | [S] |
| IBAN-Abweichung | Beleg-IBAN ≠ Stamm-Bankverbindung | Warnhinweis, Bankverbindung nicht automatisch übernehmen; Fallback BeSync-Prüfung mit Klärfall [A] | [O] (OP-10) |
| Zahlungsbedingungs-Abweichung | Belegbedingung ≠ Kreditorenstandard | Hinweis; Bearbeiter entscheidet | [S] |
| Mandant/Kreditor fehlt | Pflichtfeld leer | „Weiter" nicht möglich; Klärfall | [S] / [K] |
| Summenprüfung | Kopf ≠ Positionen | Hinweis bzw. Verbindungsbedingung (Aufteilungsprüfung) | [S] |
| Skontoampel | Skontofrist nahe | gelb/rot/dunkelrot | [S] |

---

## 14.3 M-03 Sachliche Prüfung & Kontierung

| Merkmal | Beschreibung |
|---|---|
| Zweck | Leistung sachlich und rechnerisch prüfen, Kontierung ergänzen/aufteilen, Kürzungen als Zahlbetrag mit Grund erfassen, Nachweise anhängen |
| Rolle | R-03; R-08 bei Bau-Rechnungen mit Kernpartnern |
| Werkzeug / Aufruf | smart invoice, Schritt „Sachliche Prüfung"; Aufruf aus „Meine Aufgaben", REB |
| Umsetzung | [S] Schritt, sachl. richtig, Positionen; [K] Zahlbetrag schreibbar (OP-10), Kürzungsgrund als Custom-Feld mit Werteliste, Bedingung |

**Aufbau:** 14.0.3. Kopfdaten Block A/B nur lesen und eingeklappt (eine Zeile). Block C „Zahlung und Kürzung" hervorgehoben. Positionen in voller Breite. Rechts Beleg mit Register „Anlagen" (Lieferschein, Aufmaß, BIM4You-Prüfbericht K-08).

**Felder**

| Nr. | Feld | Quelle | Pflicht | Editierbar | Hinweis / Validierung |
|---|---|---|---|---|---|
| 1 | Mandant, Kreditor, Rechnungsnummer, Rechnungsdatum, Belegart | aus Verteilung | – | R | Zusammenfassung |
| 2 | Netto-/Steuer-/Bruttobetrag | ERK | – | R | – |
| 3 | Zahlbetrag (Kopf) | SYS (Vorbelegung = Brutto) | ja | S | darf Brutto nicht übersteigen; bei Positionskürzung automatisch Summe der Positions-Zahlbeträge |
| 4 | Kürzungsbetrag | BER (Brutto − Zahlbetrag) | – | R | Anzeige |
| 5 | Kürzungsgrund | MAN (Werteliste) | bedingt | S | **Pflicht, wenn Zahlbetrag ≠ Brutto**. Werte (Vorschlag): Mengenabweichung · Preisabweichung · Mangel/Minderung · Einbehalt (Sicherheit/Gewährleistung) · Bauabzug 15 % (§ 48) · Skonto-/Nachlassdifferenz · Sonstiges (Notiz Pflicht) |
| 6 | Objekt-ID, Auftrags-/Vertragsnummer, Gewerk/Vergabeeinheit | aus Verteilung | bedingt | S | Korrektur möglich, protokolliert |
| 7 | Buchungstext | MAN | nein | S | Vorschlag: „Kreditorname Rechnungsnummer Leistung" |
| 8 | Weitere Prüfer | MAN | nein | S | zusätzlicher Prüfer (z. B. Kernpartner) |
| Pos. 1 | Positionstext | ERK | – | R | – |
| Pos. 2 | Menge, Einzelpreis | ERK | – | S | Änderung berechnet den Positionsbetrag neu (z. B. 4 → 3 Stunden, T-30) |
| Pos. 3 | Positionsbetrag netto | BER | – | R | Menge × Einzelpreis − Rabatte |
| Pos. 4 | Zahlbetrag (Position) | BER / MAN | – | S | positionsweise Kürzung; Summenprüfung Brutto/Netto/Zahlbetrag |
| Pos. 5 | Sachkonto | KI-Vorschlag / Vorlage | ja | S | – |
| Pos. 6 | Kostenstelle | Vorschlag / MAN | ja | S | Split: Position teilen oder Kontierungsvorlage mit %-Schlüssel (Test OP-10) |
| Pos. 7 | KOST2 / Kostenträger (Objekt) | MAN | bedingt | S | – |
| Pos. 8 | Sachl. richtig | MAN | ja (über Bedingung) | S | Vollständigkeit über Bedingung „alle Positionen geprüft", nicht über Pflichtschalter (Handbuchhinweis) |

**Aktionen**

| Aktion | Wirkung | Status |
|---|---|---|
| Sachlich richtig & weiter (Standard) | Verbindung zur Freigabe; erteilt rechnerisch/sachlich richtig | [S] |
| Nachweis anhängen | Lieferschein/Aufmaß an den Beleg; Ablage als K-02 | [S] |
| Kontierungsvorlage anwenden | übernimmt Kontierung des Kreditors | [S] |
| Rückfrage an Verteilung | Verbindung zurück mit Pflichtnotiz | [K] |
| Weiteren Prüfer hinzufügen | paralleler/weiterer Prüfer | [S] |
| An Lieferant zurückweisen | öffnet M-06 | [K] / [A] |
| Notiz / Annotation | Anmerkung am Beleg ohne Änderung des Originals | [S] |

**Regeln / Hinweise**

| Regel | Auslöser | Verhalten | Status |
|---|---|---|---|
| **Kürzungsgrund Pflicht** | Zahlbetrag ≠ Bruttobetrag | Aktion „weiter" nur mit Kürzungsgrund (Bedingung an der Verbindung, z. B. „Custom-Feld Kürzungsgrund vorhanden"); Meldetext im Test prüfen | [K] / [O] |
| Sonstiges erfordert Notiz | Kürzungsgrund = Sonstiges | Pflichtnotiz | [K] |
| Zahlbetrag > Brutto | Eingabe | nicht zulässig (Hinweis) | [K] |
| E-Rechnung mit Formfehler | Prüfbericht/fachliche Prüfung | Rückweisung statt Kürzung (AE-14) | Regel |
| Bau-Rechnung | Belegart Abschlag/Schluss | Zahlbetrag auf Basis BIM4You-Prüfbericht (K-08) setzen (AE-11) | [K] / [A] |
| Kürzungsmitteilung | Kürzung erfasst | optional Mail an Lieferant über BeSync (WF-05) | [A] |

---

## 14.4 M-04 Fachliche Freigabe / Zahlungsfreigabe

| Merkmal | Beschreibung |
|---|---|
| Zweck | Fachliche Freigabe gemäß Freigabematrix (1–n Stufen) und getrennte Zahlungsfreigabe vor der DATEV-Übergabe (AE-06) |
| Rolle | R-04 (Fachliche Freigabe), R-05 (Zahlungsfreigabe), R-08 (Bau-Freigabe durch Kernpartner) |
| Werkzeug / Aufruf | smart invoice, Schritttyp „Freigabe" (Pflichtaktionen Bestätigen/Ablehnen); Aufruf aus „Meine Aufgaben", REB, E-Mail, Browser mobil |
| Umsetzung | [S] Freigabeschritt, Matrix, Wertgrenzen-Verbindung; [K] Layout, Zahlungsfreigabe-Schritt |

**Aufbau:** 14.0.3. Kopfzeile zusätzlich mit **Freigabestufe** („Stufe 1 von 2"). Block C (Zahlbetrag, Kürzungsgrund, Fälligkeit) oben. Rechts Register „Historie" (wer hat wann geprüft) und „Belegänderungsansicht" (Verteilung gegenüber aktuellem Schritt: rot gelöscht, gelb geändert, grün hinzugefügt).

**Felder**

| Nr. | Feld | Quelle | Pflicht | Editierbar | Hinweis / Validierung |
|---|---|---|---|---|---|
| 1 | Mandant / Mandantenname | aus Verteilung | – | R | – |
| 2 | Kreditor | aus Verteilung | – | R | – |
| 3 | Rechnungsnummer, Rechnungsdatum, Belegart | ERK | – | R | – |
| 4 | Nettobetrag, Bruttobetrag | ERK | – | R | Wertgrenzen gelten netto je Kostenobjekt (AE-05) |
| 5 | Zahlbetrag / Kürzungsgrund | aus Prüfung | – | R | hervorgehoben, wenn Zahlbetrag ≠ Brutto |
| 6 | Objekt-ID, Kostenobjekte mit Beträgen | aus Prüfung | – | R | Grundlage der Matrix |
| 7 | Sachliche Prüfer (Historie) | SYS | – | R | Prüfer ≠ Freigeber |
| 8 | Skontofälligkeit / Nettofälligkeit / Skontobetrag | BER | – | R | Ampel |
| 9 | Freigabestufe | SYS | – | R | – |
| 10 | Kommentar | MAN | bedingt | S | Pflicht bei Ablehnen und Rückfrage |
| Z1 | IBAN (Beleg) / Bankverbindung (Stamm) | ERK / STA | – | R | **nur Zahlungsfreigabe**: Warnung bei Abweichung erneut anzeigen |
| Z2 | Fälligkeit für Zahllauf | BER | – | R | – |

**Aktionen**

| Aktion | Wirkung | Status |
|---|---|---|
| Freigeben (Standard) | nächste Stufe oder Zahlungsfreigabe; ab Wertgrenze zweite Stufe über Verbindung mit Bedingung auf den Nettobetrag (in Cent, Beispiel 10.000 € = 1000000) | [S] / [K] |
| Ablehnen | zurück zur sachlichen Prüfung, Kommentar Pflicht | [S] |
| Rückfrage | Verbindung an Prüfer/Verteilung mit Kommentar; Rückkehr in denselben Freigabeschritt | [K] |
| An Lieferant zurückweisen | nur in Ausnahmefällen; öffnet M-06 | [K] / [A] |
| Zahlung freigeben (Z) | Verbindung zur Buchhaltung | [K] |
| Zahlung zurückstellen (Z) | Verbindung „Klärfall Zahlung" mit Grund (z. B. IBAN klären) | [K] |

**Regeln / Hinweise**

| Regel | Verhalten | Status |
|---|---|---|
| Vier-Augen | Prüfer ≠ Freigeber (Standard); Vorschau-Feature „Vier-Augen ab Betrag" nur nach d.velop-Freigabe (OP-09) | [S] / [O] |
| Grenze je Kostenobjekt | Splitbeleg kann mehrere Freigeber erzeugen | [S] |
| Eskalation | statisch je Schritt oder dynamisch vor Skonto/Netto; REB „An mich eskalierte Rechnungen" | [S] |
| Zahlungsfreigabe vor DATEV | LDconnect überträgt keine Zahlungssperre → Zahlungsfreigabe liegt vor der Übergabe (AE-06) | Regel |

---

## 14.5 M-05 Klärfall

| Merkmal | Beschreibung |
|---|---|
| Zweck | Belege mit unbekanntem Mandanten, fehlendem Kreditor, Dublettenverdacht oder sonstiger Unklarheit klären und in den Regelprozess zurückführen (WF-04, P7) |
| Rolle | R-02; Clearing-Gruppe je Mandant (Kapitel 13.5.4) |
| Werkzeug / Aufruf | smart invoice: Clearing (Status „Clearing Modus" im REB) bzw. Schritt „Klärfall"; Klärfall-Mandant für nicht erkannte Gesellschaften; Lieferanten-App (M-16) für Kreditor-Anlage |
| Umsetzung | [S] Clearing, [K] Klärschritt und Klärgrund, [A] Anlage-Anforderung und Status aus der Lieferanten-App |

**Aufbau:** 14.0.3 mit Hinweisleiste „Klärgrund" ganz oben. Zusätzlicher Block „Klärung" über den Kopfdaten.

**Felder**

| Nr. | Feld | Quelle | Pflicht | Editierbar | Hinweis / Validierung |
|---|---|---|---|---|---|
| 1 | Klärgrund | SYS / MAN | ja | S | Mandant unbekannt · Kreditor fehlt · Dublettenverdacht · IBAN klären · Sonstiges |
| 2 | Klärhinweis (Freitext) | MAN | nein | S | als Notiz |
| 3 | Mandant | ERK / MAN | ja | S | Klärfall-Mandant durch echten Mandanten ersetzen |
| 4 | Kreditor | STA | ja | S | nach Anlage in DATEV und Sync am Folgetag auswählbar |
| 5 | Anlage-Anforderung (Status) | LAP | – | R | angefordert · bei Trios · angelegt · synchronisiert (Anzeige in M-16; im Beleg als Notiz) [A] |
| 6 | Wiedervorlage am | MAN | nein | S | eigene Erinnerung |
| 7 | Rechnungsnummer, Datum, Beträge | ERK | ja | S | Korrektur von Erkennungsfehlern |
| 8 | Dubletten-Referenz | SYS | – | R | Verweis auf Ursprungsbeleg |

**Aktionen**

| Aktion | Wirkung | Status |
|---|---|---|
| Zurück in Verteilung (Standard) | nach Klärung weiter im Regelprozess | [K] |
| Kreditor-Anlage anfordern | öffnet Lieferanten-App mit vorbelegten Daten (Mandant, Kreditorname, Anschrift, USt-IdNr., IBAN) | [A] |
| Dublette ablehnen / annehmen | mit Begründung | [S] |
| Zurückweisen an Lieferant | z. B. falscher Rechnungsempfänger (Grund 2), öffnet M-06 | [K] / [A] |
| Zurückstellen | bleibt im Klärfall bis zur Wiedervorlage | [K] |

**Regeln / Hinweise**

| Regel | Verhalten | Status |
|---|---|---|
| Keine Kreditoranlage in d.velop | Livos legt keine DATEV-Kreditoren an; Anlage durch Trios, Sync über LDconnect (AE-09) | Regel |
| Klärfall-Mandant | eigener Mandant im Bucket für nicht zuordenbare Belege; Rechte nur Zentralrollen | [K] |
| Liegezeit | Eskalation für Klärfälle nach 5 Arbeitstagen (Vorschlag) | [K] |

---

## 14.6 M-06 Rückweisungsdialog

| Merkmal | Beschreibung |
|---|---|
| Zweck | Rechnung mit einem von fünf Standardgründen an den Lieferanten zurückweisen und eine vorlagenbasierte E-Mail auslösen, ohne das eigene Mailprogramm zu öffnen (T-26, WF-05) |
| Rolle | R-02, R-03 (ausnahmsweise R-04) |
| Werkzeug / Aufruf | smart invoice: Aktion „An Lieferant zurückweisen" mit Pflichtgrund; Versand und Ablage über BeSync (Webhook an der Verbindung → Microsoft Graph oder d.velop-Messaging-API (Festlegung in Phase 0, OP-25), S-11) |
| Umsetzung | [K] Aktion, Grund, Endpfad; [A] Mailversand, Vorlagen, Ablage als Korrespondenz |

**Aufbau**

| Bereich | Position | Inhalt |
|---|---|---|
| Dialog | über der Belegmaske bzw. Block E | Grund, Zusatztext, Empfängeranzeige |
| Vorschau | rechts | Mailvorschau – nur in Variante B (siehe unten) |
| Aktionsleiste | unten | Zurückweisen · Abbrechen |

**Felder**

| Nr. | Feld | Quelle | Pflicht | Editierbar | Hinweis / Validierung |
|---|---|---|---|---|---|
| 1 | Rückweisungsgrund | MAN (Werteliste, Custom Entity) | ja | S | (1) Pflichtangaben § 14 UStG fehlen/fehlerhaft · (2) falscher Rechnungsempfänger/Gesellschaft · (3) Leistung nicht/nicht vollständig erbracht bzw. Nachweise fehlen · (4) Preis/Menge weicht von Auftrag/Vertrag ab · (5) formaler E-Rechnungsfehler/Format nicht verarbeitbar |
| 2 | Ergänzender Text | MAN | nein | S | wird in die Mail übernommen |
| 3 | Empfänger | LAP (Rechnungskorrespondenz-Adresse) / STA (`vendor.email`) | – | R | fehlt die Adresse → Hinweis, Versand manuell (Teilen per E-Mail) |
| 4 | Mandantenname, Rechnungsnummer, Rechnungsdatum, Bruttobetrag | aus Beleg | – | R | Platzhalter der Vorlage |
| 5 | Hinweis E-Rechnung | SYS | – | R | bei E-Rechnungen: berichtigte E-Rechnung anfordern |
| 6 | Versandstatus | BES | – | R | versendet / Fehler (in Notiz bzw. Korrespondenz K-07) |

**Aktionen**

| Aktion | Wirkung | Status |
|---|---|---|
| Zurückweisen (Variante A, Standardvorschlag) | Endpfad „Zurückgewiesen"; Export an BeSync; BeSync versendet die Vorlagenmail sofort und legt sie als K-07 in der Kreditorenakte ab | [K] / [A] |
| Zurückweisen mit Prüfung (Variante B) | BeSync erzeugt einen Mailentwurf zur Kontrolle in der Lieferanten-App bzw. einer BeSync-Oberfläche; Versand nach Bestätigung (Wunsch „anpassbare Standard-E-Mail") | [A] |
| Abbrechen | zurück zur Maske | [S] |

**Regeln / Hinweise**

| Regel | Verhalten | Status |
|---|---|---|
| Grund Pflicht | Aktion nur mit Grund (Verbindungsbedingung) | [K] |
| Dubletten | keine Lieferantenmail; interne Ablehnung (M-02) | Regel |
| Quittierung | Webhook muss innerhalb von 30 s quittieren, sonst Fehlerschritt → BeSync quittiert sofort und versendet asynchron | [S] / [A] |
| Vorschau in smart invoice | nicht möglich (keine Mailfunktion im Standard) | Grenze |

---

## 14.7 M-07 Buchhaltung

| Merkmal | Beschreibung |
|---|---|
| Zweck | Abschließende Kontrolle der Buchungsdaten durch Trios und ereignisgesteuerte Übergabe des Buchungsvorschlags mit Beleglink an DATEV (S-01) |
| Rolle | R-06 |
| Werkzeug / Aufruf | smart invoice, Schritt „Buchhaltung"; Aufruf aus „Meine Aufgaben"/REB (Globale Rechnungsliste) |
| Umsetzung | [S] Schritt, Historie, Notizen; [K] Export an die Integration DATEV Rechnungswesen (LDconnect) |

**Aufbau:** 14.0.3. Kopfdaten kompakt, Positionen als **Buchungsvorschau** in voller Breite. Rechts Register Historie und Notizen (im Workshop gezeigt).

**Felder** (in der Reihenfolge der DATEV-Übergabe; LDconnect überträgt je Buchungssatz höchstens: Belegfeld 1, Belegfeld 2, Brutto-Betrag, BU-Gegenkonto, Buchungstext, Datum, Dokumentenlink, Geschäftspartner, Konto, KOST1, KOST2, Leistungsdatum, Steuersatz, Steuerschlüssel, Waren und Dienstleistungen, WKZ)

| Nr. | Feld | Entspricht DATEV | Quelle | Pflicht | Editierbar | Hinweis / Validierung |
|---|---|---|---|---|---|---|
| 1 | Mandant | DATEV-Mandant | aus Verteilung | ja | R | Übergabeziel |
| 2 | Kreditor | Konto / Geschäftspartner | STA | ja | S | nur Stammkreditoren |
| 3 | Rechnungsnummer | Belegfeld 1 | ERK | ja | R | – |
| 4 | Rechnungsdatum | Datum | ERK | ja | R | – |
| 5 | Leistungsdatum | Leistungsdatum | ERK | nein | S | – |
| 6 | Belegart | – | aus Verteilung | ja | S | Gutschrift → Vorzeichen |
| 7 | Bruttobetrag | Brutto-Betrag | ERK | ja | R | – |
| 8 | Zahlbetrag / Kürzungsgrund | – (wird nicht übertragen) | aus Prüfung | – | R | **Hinweis bei Zahlbetrag ≠ Brutto**: Behandlung in DATEV/Zahlungsvorschlag gemäß Abstimmung mit Trios (OP-05) |
| 9 | Buchungstext | Buchungstext | aus Prüfung | nein | S | – |
| 10 | Währung | WKZ | ERK | ja | R | – |
| Pos. | Sachkonto (BU-Gegenkonto) · Steuerschlüssel · Steuersatz · Kostenstelle (KOST1) · KOST2 · Betrag | wie links | aus Prüfung | ja | S (schreibbar wenn geprüft) | Steuerschlüssel § 13b prüfen |
| 11 | Dokumentenlink | Dokumentenlink | SYS | – | R | Beleganzeige aus DATEV |
| 12 | Exportstatus | – | SYS | – | R | „An DATEV übergeben" / Fehler |

**Aktionen**

| Aktion | Wirkung | Status |
|---|---|---|
| An DATEV übergeben (Standard) | Verbindung zum Ende „Übergeben" mit Export an die Integration | [K] |
| Zurück an Prüfung | Korrektur Kontierung durch Fachbereich | [K] |
| Klärfall Buchhaltung | z. B. Kreditor in DATEV gesperrt | [K] |
| Notiz | Buchungshinweis | [S] |

**Regeln / Hinweise**

| Regel | Verhalten | Status |
|---|---|---|
| Einstufige Übergabe | Übergabe erst nach Zahlungsfreigabe (AE-08, Entscheidung O) | Regel / [O] |
| Exportfehler | Beleg läuft in den Fehlerschritt; Meldung im Administrations-Dashboard | [S] |
| Separate Buchungsvorschau | eine eigene DATEV-Vorschaumaske ist nicht belegt; die Positionsansicht dient als Vorschau | [O] |

---

## 14.8 M-08 Rechnungseingangsbuch – Arbeitsansicht

| Merkmal | Beschreibung |
|---|---|
| Zweck | Persönliche Arbeitsliste: eigene offene Rechnungen, Vertretungen, Eskalationen; Einstieg in die Bearbeitung |
| Rolle | alle Workflowrollen |
| Werkzeug / Aufruf | REB als Widget auf der Startseite oder eigene App |
| Umsetzung | [S] Schnellzugriffe, Spalten, Filter, Gruppierung, CSV-Export; [K] eigene Schnellzugriffe |

**Aufbau**

| Bereich | Position | Inhalt |
|---|---|---|
| Schnellzugriffe | links | Standard- und eigene Schnellzugriffe mit Zähler (Badge) |
| Filterleiste | oben | Filter mit Operatoren und logischen Verknüpfungen, Gruppierung |
| Liste | Mitte | Vorgänge; ungelesene fett |
| Detail/Historie | rechts (bei Auswahl) | Weg durch den Workflow, Kommentare, Notizen |

**Schnellzugriffe**

| Schnellzugriff | Inhalt | Status |
|---|---|---|
| Meine offenen Rechnungen | persönlich und über Gruppen zugestellt | [S] |
| Rechnungen in Vertretung | Aufgaben abwesender Kollegen | [S] |
| An mich eskalierte Rechnungen | mit Eskalationsstufe | [S] |
| Alle offenen Rechnungen | global oder je Mandant berechtigt | [S] |
| Archiv | abgeschlossene Vorgänge (6 bzw. 12 Monate) | [S] |
| Eigene (Vorschlag): „Skonto in 5 Tagen", „Klärfälle", „Kürzungen dieses Monats", „Bau – wartet auf BIM4You" | Filter + Layout gespeichert | [K] |

**Felder (Spalten, Standardreihenfolge)**

| Nr. | Spalte | Quelle | Hinweis |
|---|---|---|---|
| 1 | Status (inkl. ungelesen, Clearing Modus, Eskalation Stufe 1/2) | SYS | – |
| 2 | Mandant | SYS | gruppierbar |
| 3 | Kreditor | STA | – |
| 4 | Rechnungsnummer | ERK | – |
| 5 | Rechnungsdatum | ERK | – |
| 6 | Bruttobetrag | ERK | – |
| 7 | Skontobetrag / Skontofälligkeit | BER | Ampel |
| 8 | Nettofälligkeit | BER | – |
| 9 | Aktueller Schritt | SYS | gruppierbar |
| 10 | Aktueller Schritt seit | SYS | Liegezeit im aktuellen Schritt |
| 11 | Zugewiesen | SYS | Benutzer/Gruppe |
| 12 | Rechnungsformat | SYS | E-Rechnung / sonstige |

**Aktionen:** Öffnen (Belegmaske) · Historie anzeigen · Filter/Gruppieren · Spalten wählen/fixieren · eigenen Schnellzugriff speichern · CSV-Export (sichtbare oder alle Spalten, Download 30 Tage) [S].

**Regeln:** Sichtbarkeit folgt der REB-Berechtigung (Kapitel 13.5.3). E-Mail-Benachrichtigungen je Aufgabe sind abschaltbar; gearbeitet wird über diese Liste (T-17).

---

## 14.9 M-09 Rechnungseingangsbuch – Managementsicht

| Merkmal | Beschreibung |
|---|---|
| Zweck | Gesamtüberblick über offene Rechnungen je Gesellschaft, Schritt, Bearbeiter und Liegezeit im aktuellen Schritt (Katalog 3.2, **S**); Export für Monatsabschluss/Rückstellungen (AE-08) |
| Rolle | R-07; R-04 Gesellschaftsverantwortliche; R-02 |
| Werkzeug / Aufruf | REB, Schnellzugriff „Alle offenen Rechnungen" mit Gruppierung |
| Umsetzung | [S] REB; [K] Schnellzugriffe; historische Durchlaufzeiten [A] in evidanza (S-12) |

**Aufbau:** wie M-08, Liste gruppiert nach **Mandant**, darunter nach **Aktueller Schritt**; Gruppenzeilen mit Anzahl.

**Schnellzugriffe (Vorschlag)**

| Schnellzugriff | Filter | Gruppierung |
|---|---|---|
| Offen je Gesellschaft | Status offen | Mandant → Aktueller Schritt |
| Liegezeit > 10 Tage | „Aktueller Schritt seit" älter als 10 Tage (Beispiel) | Aktueller Schritt → Zugewiesen |
| Eskalationen | Status Eskalation Stufe 1/2 | Mandant |
| Klärfälle | Status Clearing Modus | Mandant |
| Zahlungsfreigabe offen | Aktueller Schritt = Zahlungsfreigabe | Nettofälligkeit |
| Monatsende unverbucht | Rechnungsdatum ≤ Monatsende, nicht übergeben | Mandant |

**Felder (Spalten):** wie M-08, zusätzlich Nettobetrag, Zahlbetrag (sofern als Spalte verfügbar [O]) und Belegart.

**Aktionen:** Gruppieren, Filtern, CSV-Export (alle Spalten) → evidanza (Stichtagssicht) [S].

**Regeln:** Archiv nur 6 bzw. 12 Monate; historische Durchlauf- und Liegezeiten je Benutzer/Schritt nur über BeSync-Protokollierung und evidanza (AE-16, T-23).

---

## 14.10 M-10 Startseite / Dashboard je Rolle

| Merkmal | Beschreibung |
|---|---|
| Zweck | Einstieg je Rolle mit Aufgaben, Rechnungslisten, Suche und Schnellzugriffen (Katalog 3.1) |
| Rolle | alle |
| Werkzeug / Aufruf | d.velop documents Startseite; Administration: Konfiguration > Erscheinungsbild > Startseite (Widgets erstellen, Sichtbarkeit von Widgets → Zuordnungen anwenden) |
| Umsetzung | [S] Widgets; [K] Verknüpfungs-Widgets und Sichtbarkeit je Gruppe |

**Aufbau (Raster, Beispiel R-03)**

| Zeile | Links | Mitte | Rechts |
|---|---|---|---|
| 1 | Aufgaben (Meine Aufgaben) | Rechnungseingangsbuch (Meine offenen Rechnungen) | Suche |
| 2 | Zuletzt bearbeitet | Favorisiert | Beobachtet |
| 3 | Verknüpfungs-Widgets: gespeicherte Suchen, Objektakten | – | – |

**Widgets je Rolle (Vorschlag)**

| Widget | Typ | R-01 | R-02 | R-03 | R-04/R-05 | R-06 | R-07 | R-11 | R-12 |
|---|---|---|---|---|---|---|---|---|---|
| Aufgaben | Standard | x | x | x | x | x | – | x | x |
| Rechnungseingangsbuch | Standard | – | x | x | x | x | x | – | x |
| Suche | Standard | x | x | x | x | x | x | x | x |
| Zuletzt bearbeitet | Standard | x | x | x | – | x | – | x | x |
| Beobachtet | Standard | – | x | x | – | – | – | x | x |
| Favorisiert | Standard | – | x | x | x | – | x | x | x |
| Import-Widget (Dropzones) | Standard | x | x | – | – | – | – | x | – |
| Link „Klärfälle" (REB-Schnellzugriff) | Verknüpfung | – | x | – | – | – | – | – | x |
| Link „Offen je Gesellschaft" (REB) | Verknüpfung | – | – | – | x | – | x | – | – |
| Link Lieferanten-App | Verknüpfung | – | x | – | – | x | – | – | x |
| Link d.velop contracts / Fristen | Verknüpfung | – | – | – | – | – | – | x | – |
| Links gespeicherte Suchen der Rolle | Verknüpfung | – | x | x | x | – | x | x | – |
| Link evidanza-Bericht | Verknüpfung | – | – | – | x | – | x | – | – |

**Regeln / Grenzen**

| Regel | Status |
|---|---|
| Nur vier Standard-Widgets mit Fachinhalt (Suche, Zuletzt bearbeitet, Beobachtet, Favorisiert) plus Aufgaben-, REB- und Import-Widget; keine Diagramm-Widgets | [S] Grenze |
| Eigene Widgets nur als Verknüpfung (Ziel-URL, Symbol Pflicht), Liste (serverseitige URL) oder erweitertes Widget (Webseite, iframe); Listen-/iframe-Widgets mit Fachdaten wären Entwicklung | [S] / [A] |
| Sichtbarkeit je Benutzer/Gruppe ist keine Zugriffsbeschränkung | [S] |
| „Zuletzt bearbeitet" zeigt keine Statuswechsel | [S] |
| Anwender können Widgets ergänzen, entfernen, vergrößern (im Workshop gezeigt) | [S] |

---

## 14.11 M-11 Aktenansicht Kreditorenakte / Objektakte

| Merkmal | Beschreibung |
|---|---|
| Zweck | Alle Dokumente zu einem Kreditor (je Gesellschaft) bzw. zu einem Objekt an einem Ort; Mehrfachablage sichtbar |
| Rolle | alle mit Leserecht (Kapitel 13.4) |
| Werkzeug / Aufruf | d.velop documents: Akte aus Suche, aus Dokument („In Akte anzeigen", Akteninhalt am Dokument) oder als Favorit |
| Umsetzung | [S] Akte, [K] Aktenarten K-10 bis K-14, Strukturregeln |

**Aufbau**

| Bereich | Position | Inhalt |
|---|---|---|
| Aktenkopf | oben | Titel und Akteneigenschaften |
| Aktenbaum | links | Unterakten (gelb = Inhalt, grau = leer) |
| Akteninhalt | Mitte | Dokumentliste (standardmäßig die ersten 100 Elemente, umstellbar) |
| Vorschau / Eigenschaften | rechts | Dokumentvorschau, Eigenschaften, Notizen, Versionen, Aktivitäten |
| Dropzone | unten in der Akte | Ablage per Drag & Drop (automatisch, manuell, mit Vorlage) |

**Felder – Aktenkopf Kreditorenakte (K-12)**

| Nr. | Feld | Quelle | Pflicht | Editierbar | Hinweis |
|---|---|---|---|---|---|
| 1 | Mandant | Aktenbildung | ja | R | Erkennungsmerkmal |
| 2 | Mandantenname | vererbt | – | R | – |
| 3 | Kreditor-Nr (DATEV) | Aktenbildung | ja | R | Erkennungsmerkmal |
| 4 | Kreditorname | vererbt | – | R | Titel |
| 5 | Lieferanten-Konsolidierungsnummer | LAP (BeSync) | – | R | Link „alle Gesellschaften" = gespeicherte Suche |
| 6 | FSB gültig bis / FSB-Status | BES | – | R | Phase 3 (AE-15) |

**Felder – Aktenkopf Objektakte (K-11)**

| Nr. | Feld | Quelle | Pflicht | Editierbar | Hinweis |
|---|---|---|---|---|---|
| 1 | Mandant | Aktenbildung | ja | R | – |
| 2 | Objekt-ID | Aktenbildung | ja | R | global eindeutig |
| 3 | Objektbezeichnung | LAP | – | R | Titel |
| 4 | Verwaltungsart / Property Manager | LAP | – | R | Eigen-/PM-verwaltet |
| 5 | Segment | LAP | – | R | Bestand · Privatisierung · Bau |

**Spalten Akteninhalt:** Kategorie · Titel · Dokument-/Rechnungsdatum · Kreditor bzw. Absender · Bruttobetrag (bei K-01) · Workflowstatus (E-24) · Zahlstatus (E-23) · Status (Bearbeitung/Freigabe/Archiv).

**Aktionen:** Ablegen per Drag & Drop · Dokument öffnen · „In Akte anzeigen" (alle Akten eines Dokuments) · Verknüpfen/Lösen · Eigenschaften exportieren (Excel/CSV) · Beobachten · Favorisieren · Aufgabe zur Akte erstellen [S].

**Regeln:** Aktenkategorien werden automatisch angelegt, nicht manuell. Mehrfachablage Rechnung in Kreditoren- und Objektakte unter Vorbehalt Test T13. Akten sind nicht als PDF exportierbar.

---

## 14.12 M-12 Suche / gespeicherte Suchen

| Merkmal | Beschreibung |
|---|---|
| Zweck | Dokumente nach Kategorie und Eigenschaften, im Volltext und gesellschaftsübergreifend über die Konsolidierungsnummer finden; Standard-Suchen je Rolle bereitstellen |
| Rolle | alle |
| Werkzeug / Aufruf | d.velop documents Suche (Widget, Suchleiste), Outlook-Add-In (Desktop) |
| Umsetzung | [S]; [K] Eigenschaften je Kategorie für Suche, Facetten, Ergebnisliste |

**Aufbau**

| Bereich | Position | Inhalt |
|---|---|---|
| Suchleiste | oben | Volltext (inkl. OCR) |
| Kategorie | links oben | Auswahl der Kategorie(n), danach passende Eigenschaftsfelder |
| Facetten | links | z. B. Mandant, Kategorie, Jahr, Kreditor |
| Ergebnisliste | Mitte | Spalten je Kategoriekombination |
| Vorschau | rechts | Dokument |

**Suchfelder je Kategorie (Auszug, Reihenfolge)**

| Kategorie | Suchfelder |
|---|---|
| K-01 Eingangsrechnung | Mandant · Kreditor · Konsolidierungsnummer · Rechnungsnummer · Rechnungsdatum (von–bis) · Bruttobetrag (von–bis) · Objekt-ID · Auftrags-/Vertragsnummer · Belegart · Workflowstatus · Zahlstatus |
| K-02 bis K-04, K-07 | Mandant · Kreditor · Objekt-ID · Auftragsnummer · Dokumentdatum · Betreff · Absender |
| K-05 / K-14 Vertrag | Mandant · Vertragspartner · Vertragstyp · Vertragsstatus · Vertragsbeginn/-ende · Objekt-ID |
| K-06 Bescheinigung | Mandant · Kreditor · Gültig bis |
| K-09 Post | Mandant · Absender · Betreff · Dokumentdatum · Eingangskanal |
| Akten | Mandant · Kreditor-Nr · Objekt-ID · Vertrags-ID |

**Gespeicherte Suchen (Vorschlag, per Link an Rollen verteilt)**

| Name | Kriterien | Rolle | Beobachten |
|---|---|---|---|
| Lieferant gesellschaftsübergreifend | Konsolidierungsnummer = X, alle Kategorien | R-02, R-07 | – |
| Rechnungen zu Vertrag/Auftrag | Auftrags-/Vertragsnummer = X | R-03, R-11 | – |
| Bescheinigungen laufen ab | K-06, Gültig bis ≤ heute + 60 Tage | R-02 | ja |
| Unbezahlte Rechnungen über Fälligkeit | K-01, Zahlstatus ≠ bezahlt, Nettofälligkeit < heute | R-07 | ja |
| Z2 – Eingangsrechnungen Gesellschaft X, Jahr Y | K-01, Mandant, Rechnungsdatum | R-14-Betreuung | – |
| Meine Objekte – neue Dokumente | Objekt-ID der eigenen Objekte | R-03 | ja |

**Aktionen:** Suchen · Filtern · Suche speichern (persönlicher Ordner) · Link kopieren · Beobachten (E-Mail bei neuen Treffern, ab business) · Eigenschaften exportieren · In PDF zusammenfassen · Zur Liste hinzufügen [S].

**Regeln:** Eine zentrale Zuweisung von Suchvorlagen an Rollen ist nicht belegt [O]; Verteilung über Link und Verknüpfungs-Widgets (M-10). Suchergebnisse zeigen nur berechtigte Dokumente.

---

## 14.13 M-13 PM-Freigabe (WF-03)

| Merkmal | Beschreibung |
|---|---|
| Zweck | Von Property Managern gebuchte Rechnungen über Schwellwert durch das Asset Management freigeben; keine Buchung, keine Zahlung; Rückmeldung per E-Mail an den PM (AE-12) |
| Rolle | R-04 (Asset Management); Verteilung durch R-02 |
| Werkzeug / Aufruf | smart invoice, eigene Workflowdefinition WF-03 mit Postfach `freigabe-hv@…` und eigenem Importprofil; Rückmeldemail über BeSync (S-11) |
| Umsetzung | [S] Freigabeschritt, [K] Workflow, Felder, Matrix; [A] Rückmeldemail |

**Aufbau:** 14.0.3, Kopfzeile mit Kennzeichnung „PM-Freigabe – keine Zahlung". Keine Positionskontierung; Positionsbereich ausgeblendet.

**Felder**

| Nr. | Feld | Quelle | Pflicht | Editierbar | Hinweis / Validierung |
|---|---|---|---|---|---|
| 1 | Mandant | ERK / MAN | ja | S (Verteilung) / R (Freigabe) | – |
| 2 | Objekt-ID / Objektbezeichnung | MAN / LAP | ja | S / R | Matrix-Spalte |
| 3 | Verwaltungsart / Property Manager | LAP (Objektstamm) | – | R | Plausibilität PM ↔ Objekt |
| 4 | Absender (PM-E-Mail) | SYS (Mail-Eingang) | ja | R | Empfänger der Rückmeldung |
| 5 | Kreditorname | ERK | ja | S | Kreditor-Nr nicht Pflicht (HV-Kreditor, 80000er-Kreis) [O] |
| 6 | Rechnungsnummer / Rechnungsdatum | ERK | ja | S | – |
| 7 | Nettobetrag / Bruttobetrag | ERK | ja | S | Schwellwert netto (Freigabematrix) |
| 8 | Leistungsbeschreibung (Kurztext) | MAN | nein | S | – |
| 9 | Rückmeldetext an PM | MAN | nein | S | wird in die Mail übernommen |
| 10 | Ablehnungsgrund | MAN (Werteliste) | bedingt | S | Pflicht bei Ablehnung |

**Aktionen**

| Aktion | Wirkung | Status |
|---|---|---|
| Freigeben | Ende „Freigegeben", Webhook → BeSync-Mail an PM mit Freigabevermerk | [S] / [A] |
| Ablehnen | Ende „Abgelehnt", Mail mit Grund | [S] / [A] |
| Rückfrage an PM | Mail mit Frage, Beleg wartet (Wiedervorlage) | [A] / [O] |

**Regeln:** Beleg zählt ins invoices-Volumen. Keine DATEV-Übergabe. Scope und Schwellwerte legt Livos fest (OP-17).

---

## 14.14 M-14 Vertragsmaske

| Merkmal | Beschreibung |
|---|---|
| Zweck | Vertrag anlegen und pflegen, Fristen überwachen, Dokumente in der Vertragsakte führen, Freigabe und Signatur starten (WF-06) |
| Rolle | R-11; Leser R-04, R-07 |
| Werkzeug / Aufruf | d.velop contracts: Dashboard (Status, Laufzeitfortschritt), „Neuer Vertrag", Vertragsdetailansicht, Fristenkalender |
| Umsetzung | [S] contracts; [K] Vertragstypen, Wertemengen, Zusatzfelder; [O] Freigabe-Workflow (OP-12) |

**Aufbau**

| Bereich | Position | Inhalt |
|---|---|---|
| Kopf | oben | Vertragsgegenstand, Vertragsstatus, Laufzeitbalken |
| Register „Stammdaten" | links | Felder Block 1 |
| Register „Laufzeit & Fristen" | links | Felder Block 2 |
| Register „Dokumente" | Mitte | Vertragsdokumente mit Dokumententyp, Vorschau |
| Register „Aufgaben/Verlauf" | rechts | Fristen, Aufgaben, Aktivitäten |

**Felder**

| Nr. | Feld | Quelle | Pflicht | Editierbar | Hinweis / Validierung |
|---|---|---|---|---|---|
| 1.1 | Vertragsgegenstand | MAN | ja | S | [S] |
| 1.2 | Vertrags-ID (intern) | SYS | ja | R | verknüpft Akte und Dokumente [S] |
| 1.3 | Vertrags-ID (extern) | MAN | nein | S | [S] |
| 1.4 | Vertragstyp | MAN (Wertemenge) | ja | S | Werte exakt wie in documents [S] |
| 1.5 | Vertragsart | MAN | ja | S | Einzelvertrag · Rahmenvertrag · Einzelvertrag mit Rahmenvertrag [S] |
| 1.6 | Übergeordneter Rahmenvertrag | MAN | bedingt | S | bei „Einzelvertrag mit Rahmenvertrag" [S] (Vertragshierarchie) |
| 1.7 | Vertragsstatus | MAN / SYS | ja | S | Entwurf · In Genehmigung · Aktiv · Gekündigt · Abgelaufen [S] |
| 1.8 | Mandant / Mandantenname | Dataset | ja | S | Livos-Pflicht (P1) [K]/[O] |
| 1.9 | Organisation | Wertemenge | nein | S | Gesellschaftsverbund (Vorschlag, Kapitel 12.1.9) [S] |
| 1.10 | Objekt-ID | Dataset | bedingt | S | bei objektbezogenen Verträgen [K] |
| 1.11 | Vertragspartner | business objects | ja | S | Übernahme aus Lieferanten-App über BeSync (Vorschlag) [A]/[O] |
| 1.12 | Kreditor-Nr | STA | bedingt | S | bei Lieferantenverträgen [K] |
| 1.13 | Verantwortlicher (intern) | Person | ja | S | Empfänger der Fristmeldungen [S] |
| 2.1 | Vertragsbeginn | MAN | ja | S | [S] |
| 2.2 | Vertragsende | MAN / BER | bedingt | S | leer = unbefristet [S] |
| 2.3 | Kündigungsfrist | MAN | bedingt | S | Laufzeit-/Fristberechnung [S] (Feldname [O]) |
| 2.4 | Verlängerungsart / -zeitraum | MAN | bedingt | S | einmalig / rollierend [S]/[O] |
| 2.5 | Kündigungsstichtag | BER | – | R | [S]/[O] |
| 2.6 | Vertragswert | MAN | nein | S | [S] |
| 2.7 | Gewährleistungsende / Sicherheit bis (Bau) | MAN | bedingt | S | Zusatzfeld je Vertragstyp [K] |
| 3.1 | Dokumententyp (je Dokument) | MAN | ja | S | Vertrag · Nachtrag · Kündigung · Anlage · Protokoll · Korrespondenz · Bürgschaft [K] |

**Aktionen**

| Aktion | Wirkung | Status |
|---|---|---|
| Vertrag anlegen / speichern | legt Vertragsakte in documents an | [S] |
| Dokument hinzufügen (Upload, Outlook) | Vertragsdokument in der Akte | [S] |
| Freigabe starten | process-studio-Prozess „Vertragsfreigabe" | [K] / [O] |
| Signatur starten | d.velop sign | [S] |
| Frist-Erinnerung / Aufgabe | Wiedervorlage (WF-08) | [S] |
| Mit d.velop pilot fragen | Chat zum Vertragsdokument | [S] |

**Regeln:** Fehlerhafte Werte in Wertemengen (Schreibweise) verhindern die Aktenanlage. Datentyp/Anzahl der Werte nachträglich nicht änderbar. Rechte je Organisation × Vertragstyp plus DMS-Rechte.

---

## 14.15 M-15 Postverteilung

| Merkmal | Beschreibung |
|---|---|
| Zweck | Teil A: gescannte Post prüfen und klassifizieren. Teil B: verteilte Post übernehmen, weiterleiten und ablegen (WF-07) |
| Rolle | Teil A: R-01; Teil B: Empfängergruppen (R-02, R-03, R-05, R-11, Fachbereiche) |
| Werkzeug / Aufruf | Teil A: inbound scan (Stapelbearbeitung); Teil B: d.velop mail dispatcher (Aufgaben-Widget, Hauptansicht/Bearbeitungsansicht) |
| Umsetzung | [S]; [K] Importprofile, Klassifizierung, Empfängergruppen, Schnellaktionen; KI nur C1 |

**Aufbau Teil A (Stapel)**

| Bereich | Position | Inhalt |
|---|---|---|
| Stapelliste | links | Poststapel des Tages |
| Seiten mit Trennern | Mitte | KI-Trenner (orange/blau), manuelle Trenner (grün) |
| Klassifizierung | rechts | KI-Vorschlag (Top 3), Eigenschaften |

**Felder Teil A**

| Nr. | Feld | Quelle | Pflicht | Editierbar | Hinweis / Validierung |
|---|---|---|---|---|---|
| A1 | Postklasse (Kategorie) | ERK (KI, Top 3) | ja | S | < 80 % → „Unbestimmt" → manuell (Katalog 12.2.4) |
| A2 | Mandant | SYS (Trennblatt-Barcode) / MAN | ja | S | ohne Mandant keine Verteilung |
| A3 | Empfängergruppe | BER (aus Postklasse + Mandant) / MAN | ja | S | immer Gruppe |
| A4 | Priorität | MAN | ja | S | normal · hoch |
| A5 | Posttyp | SYS | ja | R | gescannt / physisch |
| A6 | Eingangsdatum | SYS | ja | R | – |
| A7 | Absender | ERK / MAN | nein | S | – |
| A8 | Kommentar | MAN | nein | S | – |

**Aufbau Teil B (mail dispatcher)**

| Bereich | Position | Inhalt |
|---|---|---|
| Aufgabenlisten | links | Meine Aufgaben · An mich gesendet · An mich und andere gesendet · Gruppenpostkörbe |
| Dokument | Mitte | Vorschau |
| Postdaten und Ablage | rechts | Felder Teil B, Schnellaktionen |

**Felder Teil B**

| Nr. | Feld | Quelle | Pflicht | Editierbar | Hinweis / Validierung |
|---|---|---|---|---|---|
| B1 | Betreff der Aufgabe | SYS | – | R | z. B. „Digitaler Posteingang: Empfänger:in prüfen" |
| B2 | Fällig / Erinnerung | SYS | – | R | Erinnerung nach Tagen; Eskalation über Priorität |
| B3 | Zielkategorie | aus A1 | ja | S | bei „Es ist für mich" |
| B4 | Mandant | aus A2 | ja | S | – |
| B5 | Kreditor-Nr | MAN | bedingt | S | Pflicht für K-06, K-07 (Lieferant) |
| B6 | Objekt-ID | MAN | bedingt | S | Pflicht für K-02, K-03, K-04 mit Objektbezug |
| B7 | Dokumentdatum, Betreff, Absender | ERK / MAN | ja | S | Titel „Betreff, Dokumentdatum" |
| B8 | Weiterleitungskommentar | MAN | nein | S | vordefiniert oder frei |

**Aktionen**

| Aktion | Wirkung | Status |
|---|---|---|
| Übernehmen | Gruppenaufgabe übernehmen (Sperre) | [S] |
| Es ist für mich | Zielkategorie + Ablegen; Aufgabe quittiert; Aktenbildung | [S] |
| An Kollegen*in senden | Person/Abteilung mit Kommentar | [S] |
| An Posteingang senden | zurück an die Poststelle | [S] |
| Schnellaktionen (max. 20) | z. B. „An Rechnungseingang", „An Vertragsmanagement", „An Recht" | [S] / [K] |
| Rechnung in ER-Strecke | Import über ER-Importprofil (12.2.6) | [K] / [O] |

**Regeln:** Postdokumente im Status Freigabe; Person als Erstempfänger erzeugt keine Aufgabe; jede Weiterleitung protokolliert.

---

## 14.16 M-16 Lieferanten-App

| Merkmal | Beschreibung |
|---|---|
| Zweck | Führende Pflege der Lieferantenidentität mit Konsolidierungsnummer, Mapping auf DATEV-Kreditoren je Mandant und HV-Kreditoren, FSB-Status, Anlage-Anforderung an Trios (AE-09, AE-15) |
| Rolle | R-12 (Pflege), R-02 (Anforderung), R-06 (Rückmeldung Anlage) |
| Werkzeug / Aufruf | bestehende MDIS-App auf BeSync (Erweiterung); Link aus Startseite und aus Klärfall (M-05) |
| Umsetzung | [A]; Oberfläche an die bestehende App anpassen – die folgende Struktur ist ein Vorschlag |

**Aufbau**

| Bereich | Position | Inhalt |
|---|---|---|
| Lieferantenliste | links | Suche nach Name, Konsolidierungsnummer, USt-IdNr., Kreditor-Nr |
| Lieferantenstamm | Mitte oben | Felder Block 1 |
| Kreditor-Mapping | Mitte unten | Tabelle je Mandant |
| FSB / Anforderungen | rechts | Block 3 und 4 |

**Felder**

| Nr. | Feld | Quelle | Pflicht | Editierbar | Hinweis / Validierung |
|---|---|---|---|---|---|
| 1.1 | Konsolidierungsnummer | SYS (App) | ja | R | gesellschaftsübergreifend eindeutig |
| 1.2 | Name, Anschrift | MAN / DATEV | ja | S | – |
| 1.3 | USt-IdNr. / Steuernummer | MAN / DATEV | nein | S | Dublettenprüfung |
| 1.4 | E-Mail Rechnungskorrespondenz | MAN | nein | S | Empfänger Rückweisungsmail |
| 1.5 | Bankverbindungen | DATEV | – | R | Anzeige; führend DATEV |
| 1.6 | Bauleistender (§ 13b/§ 48) | MAN | nein | S | Kennzeichen für WF-02 |
| 2.1 | Mandant | DATEV | ja | R | je Zeile |
| 2.2 | DATEV-Kreditornummer (70000er) | DATEV (S-05) | ja | R | Schlüssel „Mandantennr + Kreditornr" |
| 2.3 | HV-Kreditornummer (80000er) | PM-Daten | nein | S | – |
| 2.4 | Mapping-Status | SYS | – | R | vorgeschlagen (KI) · bestätigt · abgelehnt |
| 3.1 | FSB gültig bis | MAN | bedingt | S | Pflicht für Bauleistende |
| 3.2 | FSB-Prüfnachweis (EIBE-Abfrage, Datum) | MAN | bedingt | S | Prüfung manuell im BZSt-Portal |
| 3.3 | FSB-Dokument | Link auf K-06 | – | R | – |
| 4.1 | Anlage-Anforderung: Mandant, Beleg-ID, angefordert von/am | SYS / aus M-05 | ja | R | – |
| 4.2 | Anforderungsstatus | SYS / R-06 | – | S (R-06) | angefordert · bei Trios · angelegt · synchronisiert |

**Aktionen:** Lieferant anlegen · Mapping bestätigen/ablehnen (KI-Vorschlag X.One) · Dubletten zusammenführen · FSB erfassen · Anlage anfordern (Mail/Aufgabe an Trios) · Änderungsprotokoll anzeigen [A].

**Regeln:** DATEV-Stammdaten schreibt nur LDconnect in den smart-invoice-Bucket; BeSync schreibt dort nur Mandanten und ergänzende Entitäten (Kapitel 8.7). Die Konsolidierungsnummer kommt als DMS-Eigenschaft an den Beleg (AE-09). Livos pflegt keine technischen Middleware-Tabellen (P3).

---

## 14.17 M-17 Freigabematrix-Pflege

| Merkmal | Beschreibung |
|---|---|
| Zweck | Gesellschaftsindividuelle Freigabegrenzen und Freigeber pflegen (AE-05, Katalog 1.4) |
| Rolle | R-12 (Pflege), GF (Freigabe der Änderung) |
| Werkzeug / Aufruf | smart invoice Administration > Freigabematrizen > Matrix wählen; alternativ API-Import (Zeilen im Batch) aus einer Excel-Vorlage über BeSync [A] |
| Umsetzung | [S] Matrix; [K] Spalten und Zeilen |

**Aufbau:** Matrixliste links; Tabelle der gewählten Matrix in der Mitte; Zeileneditor rechts; oben „Spalte hinzufügen", „Zeile hinzufügen", „Speichern".

**Felder (Spalten der Matrix)**

| Nr. | Spalte | Quelle | Pflicht | Editierbar | Hinweis / Validierung |
|---|---|---|---|---|---|
| 1 | Bearbeiter (Person oder Gruppe) | MAN | ja | S | feste Spalte; Gruppen bevorzugt (`SI_Freigeber_<Nr>`) |
| 2 | Freigabegrenze | MAN | ja | S | feste Spalte; Grenze gilt je Kostenobjekt; netto |
| 3 | Mandant | MAN | ja | S | Zusatzspalte; Groß-/Kleinschreibung beachten |
| 4 | Kostenstelle | MAN | nein | S | Zusatzspalte |
| 5 | Kostenträger / Objekt | MAN | nein | S | Zusatzspalte |
| 6 | Segment | MAN | nein | S | optionale Zusatzspalte (Vorschlag) |

„Stufe" und „Betrag von/bis" aus AE-05 werden nicht als eigene Spalten geführt: Jede Freigabestufe erhält eine eigene Matrix (z. B. „Freigabe Stufe 1", „Freigabe Stufe 2") bzw. eine Wertgrenzen-Verbindung. Die Untergrenze ergibt sich aus der Strategie „Von unten zum Freigeber" [S]/[K].

**Aktionen:** Zeile hinzufügen/ändern/löschen · Spalte hinzufügen (bis 20) · Speichern · Export der Matrix für die Rezertifizierung [S]/[O].

**Regeln:** Änderungen nur nach Vier-Augen-Freigabe (Kapitel 13.8.2). Jede Gesellschaft braucht mindestens eine Zeile je Stufe (Prüfung durch BeSync [A]).

---

## 14.18 M-18 Vertretung / Abwesenheit

| Merkmal | Beschreibung |
|---|---|
| Zweck | Abwesenheit mit Vertretung setzen – selbst oder durch Administrator/Vorgesetzte für erkrankte Kollegen (T-39, AE-17) |
| Rolle | alle; R-12 und Vorgesetzte mit administrativen Rechten für Dritte |
| Werkzeug / Aufruf | Startseite > Profilbild > Abwesenheitsstatus; d.velop mobile; Vertretungsregeln unter Konfiguration > Aufgaben und Prozesse > Vertretungsregeln |
| Umsetzung | [S] |

**Aufbau:** Dialog mit Benutzerwahl (nur für Berechtigte), Zeitraum, Vertretung, Nachricht.

**Felder**

| Nr. | Feld | Quelle | Pflicht | Editierbar | Hinweis / Validierung |
|---|---|---|---|---|---|
| 1 | Benutzer | SYS (eigenes Konto) / MAN (Berechtigte) | ja | S | Auswahl anderer Benutzer nur mit administrativen Rechten |
| 2 | Start | MAN (oder „jetzt" per Uhrsymbol) | ja | S | auch vorab planbar |
| 3 | Ende | MAN | nein | S | leer = unbegrenzt |
| 4 | Vertretung | MAN | ja | S | Hinweis: möglichst derselbe Gesellschaftsverbund; Zahlungsfreigabe nur an R-05 |
| 5 | Nachricht | MAN | nein | S | Abwesenheitsnotiz |

**Aktionen:** Speichern · Abwesenheit beenden · Aufgaben gesammelt weiterleiten (Berechtigte) [S].

**Regeln:** Die Vertretung übernimmt die Rechte für die Aufgaben. In smart invoice sieht sie nur persönlich zugestellte Aufgaben. Vertretungsausschluss je Aufgabentyp möglich (Kapitel 13.7).

---

## 14.19 M-19 Externe Benutzeraufgabe

| Merkmal | Beschreibung |
|---|---|
| Zweck | Stellungnahme (Zustimmung, Ablehnung, Rückfrage) durch Ad-hoc-Externe ohne Lizenz und ohne Konto (Katalog 4.2, WF-10); die verbindliche Freigabe erteilt der interne Bearbeiter in smart invoice (Kapitel 11.5.3) |
| Rolle | R-10 |
| Werkzeug / Aufruf | process studio „Externe Benutzeraufgabe": E-Mail mit Link auf ein d.velop-forms-Formular; Beleg als zeitlich begrenzter Teilen-Link; Kopplung an smart invoice über BeSync |
| Umsetzung | [S] externe Aufgabe und Formular; [K] Formular; [A] Kopplung smart invoice ↔ process studio |

**Aufbau**

| Bereich | Position | Inhalt |
|---|---|---|
| Kopf | oben | Livos-Kennzeichnung (Logo), Titel „Stellungnahme zur Rechnung", Frist |
| Belegdaten | Mitte | nur gemappte Prozessdaten |
| Entscheidung | unten | Auswahl, Kommentar, Absenden |

**Felder**

| Nr. | Feld | Quelle | Pflicht | Editierbar | Hinweis / Validierung |
|---|---|---|---|---|---|
| 1 | Gesellschaft (Mandantenname) | SYS (Prozessvariable) | – | R | – |
| 2 | Kreditorname | SYS | – | R | – |
| 3 | Rechnungsnummer / Rechnungsdatum | SYS | – | R | – |
| 4 | Brutto- und Zahlbetrag | SYS | – | R | – |
| 5 | Objekt / Leistung | SYS | – | R | – |
| 6 | Link zum Beleg | SYS (Teilen-Link) | – | R | gültig bis Datum; max. 180 Tage; nur Lesen |
| 7 | Antwort bis | SYS (Timer) | – | R | nach Ablauf ist das Formular nicht mehr aufrufbar |
| 8 | Entscheidung | MAN | ja | S | Zustimmung · Ablehnung · Rückfrage |
| 9 | Kommentar | MAN | bedingt | S | Pflicht bei Ablehnen/Rückfrage |
| 10 | Name der entscheidenden Person | MAN | ja | S | Bestätigung (kein Login) |

**Aktionen:** Absenden (Prozess läuft weiter; BeSync legt das Ergebnis als Notiz bzw. K-07 am Beleg ab und benachrichtigt den internen Bearbeiter, der im smart-invoice-Schritt entscheidet) [S]/[A].

**Regeln:** Im Formular ist kein Zugriff auf Dokumente in d.velop möglich; der Beleg kommt nur über den Teilen-Link. Passwortschutz für Link und Formular ist nicht dokumentiert (OP-39) → Einsatz nur für bekannte Empfänger; das Ergebnis ist eine Stellungnahme, keine Freigabe [O]. Ausführungen zählen auf das process-studio-Kontingent (OP-11).

# 15 Schnittstellenkonzept

Dieses Kapitel beschreibt alle Schnittstellen des Livos-DMS im Detail. Grundlage sind die Designprinzipien P2 (Standard vor Konfiguration vor Entwicklung), P3 (BeSync nur, wo der Standard endet) und P4 (ein führendes System je Datenobjekt). Jede Schnittstelle hat eine feste ID (S-01 bis S-17). Diese IDs verwenden auch die Prozesskapitel 9 bis 12, die Roadmap in Kapitel 19 und die Offene-Punkte-Liste in Kapitel 20.

Legende Belegstatus: **[S]** Standard belegt · **[K]** Konfiguration · **[A]** Anpassung/Entwicklung (in der Regel MDIS BeSync) · **[O]** offen/zu verifizieren.

## 15.1 Überblick

### 15.1.1 Systemlandschaft und Datenflüsse

d.velop ist das zentrale System für Beleg, Workflow, Freigabe und Archiv. Um d.velop herum liegen sechs Umsysteme: DATEV (Finanzbuchhaltung), multicash (Zahlungsausführung), BIM4You (Bau-Budgetcontrolling), die Lieferanten-App auf BeSync (Lieferantenidentität und Stammdaten), evidanza (BI) und Microsoft 365/Entra ID (E-Mail und Identitäten). Die Property Manager sind keine angebundenen Systeme, sondern E-Mail-Partner.

| Datenobjekt | Führendes System (P4) | Empfänger | Schnittstelle |
|---|---|---|---|
| Beleg (Bild, XML, Workflowdaten, Freigabe) | d.velop (smart invoice, documents) | DATEV (Buchungsvorschlag + Link), BIM4You (Bau) | S-01, S-08 |
| Kreditorenkonto, Sachkonto, Steuerschlüssel, Zahlungsbedingung, Bankverbindung, KOST1/KOST2 | DATEV (je Mandant) | smart-invoice-Bucket | S-02 |
| Lieferantenidentität (Konsolidierungsnummer), Gesellschafts- und Objektstamm | Lieferanten-App (BeSync) | d.velop documents, smart invoice | S-04 |
| Buchung, offener Posten, Zahlstatus | DATEV | d.velop (Eigenschaft Zahlstatus) | S-06 |
| Zahlungsausführung, Unterschrift, Bankstatus | multicash | DATEV (Kontoauszug) | S-07 |
| Bau-Budget, VOB-Kumulation, Einbehalte, Nachträge | BIM4You | d.velop (Eigenschaften, Prüfbericht) | S-09, S-10 |
| Benutzer und Gruppen | Microsoft Entra ID | d.velop | S-13 |
| Prozessereignisse, Kennzahlen | d.velop (Ereignisse), BeSync (Historie) | evidanza | S-12 |

### 15.1.2 Schnittstellenkatalog

Richtung: → = aus d.velop heraus, ← = nach d.velop hinein, ↔ = beide Richtungen. Phasen gemäß Roadmap (Kapitel 19, Vorschlag).

| ID | Name | Richtung | Datenobjekte | Auslöser | Technik | Standard/Konfig/Anpassung | Phase | Betreiber |
|---|---|---|---|---|---|---|---|---|
| S-01 | DATEV Buchungsvorschlag + Beleglink | d.velop → DATEV | Buchungsvorschlag (16 Felder) mit Dokumentenlink | Schrittverbindung „Übergabe" im Schritt Buchhaltung (ereignisgesteuert, je Rechnung) | Option „DATEV Rechnungswesen" (LDconnect) → Riecken-Gateway → DATEVconnect; Beleganzeige Drittanbieter | **K** | 1 | LIONDEER (Konnektor), Hoster (DATEV-Seite), MDIS (Konfiguration, Monitoring) |
| S-02 | DATEV-Stammdaten | DATEV → smart invoice | Kreditoren, Sachkonten, Steuerschlüssel, Zahlungsbedingungen, Kreditor-Bankverbindungen, KOST1, KOST2 | täglich | LDconnect, Import in den smart-invoice-Bucket | **K** | 1 | LIONDEER, Hoster |
| S-03 | Belegbilder nach DATEV Unternehmen online (optional) | d.velop → DUO | Belegbild (+ ggf. Rechnungsdaten) | Übergabe | Option „DATEV Unternehmen Online" (LDconnect DUO, Belegbilderservice oder Rechnungsdatenservice 1.0) | **K** (optional) | nach Bedarf | LIONDEER, Trios (DUO-Bestände) |
| S-04 | Lieferanten-App ↔ d.velop | BeSync ↔ d.velop | Konsolidierungsnummer, Gesellschafts- und Objektstamm, Datasets/Wertemengen, Restriction Sets, smart-invoice-Mandanten | nächtlich (Delta) + bei Änderung | smart-invoice-Stammdaten-API (`companies`, `custom_entities`), DmsConfig-/DMS-API, DMS-Webhooks (dynamische Wertemenge) | **A** | 1 (Erstbefüllung per Import), 2 (automatische Pflege) | MDIS |
| S-05 | Lieferanten-App ↔ DATEV/Trios | BeSync ↔ DATEV/Trios | Kreditor-Mapping (Konsolidierungsnr. ↔ Mandant + Kreditornr.), Anlage-Anforderung | bei Neuanlage/Klärfall „Kreditor fehlt" | DATEVconnect lesend (über Gateway) + Anforderung an Trios (Aufgabe/E-Mail) | **A** | 1 (Anforderung per E-Mail), 2 (automatisiert) | MDIS |
| S-06 | Zahlstatus „bezahlt" (OPOS) | DATEV → BeSync → d.velop | Zahlstatus, Zahldatum, gezahlter Betrag, Teilzahlung | täglich (Vorschlag: nachts, optional mehrfach) | DATEVconnect `accounts-payable` → DMS-API (Eigenschaft E-23) | **A** | 3 | MDIS |
| S-07 | Zahlungsdatei SEPA → multicash | DATEV → multicash | SEPA-XML (pain.001); Rückweg Kontoauszug (camt.053/MT940) → DATEV | Zahllauf | DATEV Zahlungsverkehr (SEPA-Export), multicash-Import; Standard beider Hersteller | **S** (außerhalb d.velop) | 1 | Trios/Livos Treasury |
| S-08 | BIM4You Hinweg (Bau-Rechnung) | d.velop → BeSync → BIM4You | Kopfdaten, Projekt, Vergabeeinheit/Vertrag, PDF/XML, Beleg-ID als Barcode | Schrittverbindung „Bauprüfung" in WF-02 | smart-invoice-Transfer (asynchron) → E-Rechnungsimport bzw. Austausch-/Scanordner BIM4You | **A** | 3 | MDIS |
| S-09 | BIM4You Rückweg | BIM4You → BeSync → d.velop | Freigabestatus, geprüfter Betrag, Einbehalte, Prüfbericht/Zahlungsfreigabe-PDF | Freigabe oder Storno in BIM4You | Polling Export/Übergabeordner → DMS-API + Transfer-Rückmeldung | **A** | 3 | MDIS |
| S-10 | BIM4You-Stammdaten | BIM4You → smart invoice | Projekte, Vergabeeinheiten/Lose, Verträge | nächtlich | smart-invoice-Stammdaten-API (`custom_entities`, `other_dimensions`) | **A** | 3 | MDIS |
| S-11 | Rückweisungs-, Kürzungs- und PM-Rückmelde-Mail | d.velop → BeSync → Lieferant/PM | Vorlagen-Mail mit Grund, Beleg-Referenz; Ablage als K-07 | Aktion „Ablehnen", Endverbindung WF-03, Kürzung | Export/Webhook an Verbindung → Mailversand über Microsoft Graph oder d.velop-Messaging-API (Festlegung in Phase 0, OP-25) → DMS-API (Ablage) | **A** | 2 | MDIS |
| S-12 | Prozessereignisse → evidanza | d.velop → BeSync → MS SQL → evidanza | Beleg × Schritt × Zeitpunkt × Bearbeiter × Status × Betrag | jeder Schrittwechsel + nächtliche Abfrage | Export-Events an Verbindungen, Task-/Process-/DMS-API → MS-SQL-Staging → evidanza | **A** | 1 (Protokoll ab Go-live), 2 (Auswertungen) | MDIS |
| S-13 | Identitäten | Entra ID → d.velop | Benutzer, Gruppen, Mitgliedschaften; Anmeldung | laufend (Provisioning-Zyklus) | SCIM 2.0, OIDC | **S/K** | 0/1 | Livos IT |
| S-14 | E-Mail-Eingang | M365 → d.velop | Rechnungen, PM-Freigaberechnungen, Post | laufend | email import (Microsoft Graph) / inbound e-mail | **S** | 1 (ER), 2 (PM), 4 (Post) | Livos IT (Postfächer), MDIS (Importprofile) |
| S-15 | Export je Gesellschaft | d.velop → Archivpaket | Originale aller Versionen, JSON-Metadaten, Protokolle | Anlass (Verkauf, Prüfung Z3) | repo export-API + BeSync-Exportskript | **A** | 1 (Voraussetzung P1), 2 (Exportskript) | MDIS |
| S-16 | PM-Buchungsdaten → BI (optional) | PM → BeSync → BI | DATEV-Buchungsstapel und Kreditorenstamm der PM | monatlich | Upload/Postfach, Parser, Mapping 80000er-Kreditoren | **A** | 3 (optional) | MDIS |
| S-17 | ERP/PM-Stammdatensync (perspektivisch) | ↔ | Kreditoren, Objekte, Kontenrahmen | Folgeprojekt | d.velop REST-APIs + Hersteller-APIs | **A** | Folgeprojekt (Katalog 5.4) | offen |

**Zählung:** 17 Schnittstellen. Davon sind 5 Standard oder Konfiguration mit Herstellerkomponenten (S-01, S-02, S-03, S-13, S-14), eine liegt vollständig im Standard außerhalb von d.velop (S-07), und 11 sind BeSync-Leistungen [A] (S-04 bis S-06, S-08 bis S-12, S-15 bis S-17).

### 15.1.3 Leitregeln für alle Schnittstellen

| Nr. | Regel | Begründung |
|---|---|---|
| L1 | Die Gesellschaft (Mandanten-ID, E-01) ist in jeder Nachricht Pflichtfeld. | P1; DATEV-Mandant, Rechte und Export hängen daran |
| L2 | Je smart-invoice-Bucket gibt es genau **einen schreibenden Stammdatenlieferanten** für DATEV-Entitäten: LDconnect. BeSync schreibt nur ergänzende Entitäten (Mandanten, `custom_entities`, `other_dimensions`) und DMS-Eigenschaften. | Konfliktvermeidung (AE-09) |
| L3 | Es gibt genau **einen Buchungskanal** für Eingangsrechnungen nach DATEV: d.velop über S-01. Der DATEV-Export von BIM4You bleibt für Eingangsrechnungen deaktiviert. | P4; keine Doppelbuchung (AE-11) |
| L4 | Laufende smart-invoice-Belege werden nicht per API verändert. Rückmeldungen gehen als DMS-Eigenschaft oder als Transfer-Rückmeldung (erfolgreich/Fehler) an den Beleg. | Kein Schreib-Endpunkt für laufende Belege dokumentiert (OP-07) |
| L5 | Jede BeSync-Schnittstelle hat einen technischen Benutzer mit minimalen Rechten, ein Protokoll und eine Überwachung durch MDIS. Livos pflegt keine technischen Tabellen. | P3; Randbedingung Livos (Workshop 22.09.2026) |

## 15.2 DATEV-Anbindung (S-01, S-02, S-03)

### 15.2.1 Komponenten

d.velop bietet die DATEV-Anbindung als kostenpflichtige Option „DATEV Rechnungswesen (standardisierte Schnittstelle)" zu d.velop invoices an. Technisch ist das der Konnektor **LDconnect für DATEV Rechnungswesen** von LIONDEER (d.velop invoices Leistungsbeschreibung 12/2025; LDconnect Leistungsschein 11/2025). Die Option ist in der Betriebsform C1 verfügbar (AE-01, AE-07).

| Komponente | Hersteller | Zweck | Pflicht | Bereitstellung |
|---|---|---|---|---|
| d.velop invoices + Option „DATEV Rechnungswesen" (LDconnect) | d.velop / LIONDEER | Buchungsvorschlag je Rechnung, täglicher Stammdatenabruf | ja | Bestellung über d.velop; kostenpflichtige Option |
| DATEVconnect (Rechnungswesen) | DATEV | REST-Schnittstelle auf dem DATEV-Server; Stammdaten lesen, Buchungsvorschläge schreiben, OPOS lesen | ja | Bestellung in der Regel über den Steuerberater (Trios) |
| DATEV Beleganzeige Drittanbieter | DATEV | Öffnet den Beleg aus dem DATEV-Buchungssatz im d.velop-Archiv (Beleglink) | optional, empfohlen | DATEV-seitig kostenpflichtig; Bestellung über Steuerberater |
| Riecken-Datengateway / Riecken Cloud Gateway für DATEVconnect | Riecken | Gesicherter Zugang (VPN, keine Datenspeicherung im Gateway) zu DATEVconnect beim Hoster | ja bei DATEVasp, DATEV-SmartIT und gehostetem DATEV | Vertrag Riecken/LIONDEER; Freigabe durch den DATEV-Systembetreiber |
| DATEVasp-Zusatzmodul „Anbindung Drittanbieter" | DATEV | Freischaltung der Drittanbieter-Anbindung in DATEVasp | falls Hoster = DATEVasp | über DATEV/Hoster |
| Dedizierter DATEV-Benutzer | DATEV/Hoster | Technischer Benutzer mit Rechten auf alle angebundenen Bestände | ja | DATEV-Systembetreiber |
| Option „DATEV Unternehmen Online" (S-03) | d.velop / LIONDEER | Belegbild in DATEV (Belege online) | optional | kostenpflichtige Option; DUO-Bestand je Mandant nötig |

**Gateway-Freigabe.** Der DATEV-Systembetreiber gibt die Verbindung frei (Zeichnungsberechtigung per SmartCard/SmartLogin oder ID-Prüfung) und legt über „Ordnungsbegriffe" fest, welche Mandanten erreichbar sind (Riecken-Dokumentation; DATEV: Einsatz Cloud Gateway in DATEVasp). Im Workshop nannte Livos den Zugriff über die „ricken Cloud" (Workshop 22.09.2026, 00:14:00). Wir gehen mit hoher Wahrscheinlichkeit davon aus, dass damit das Riecken Cloud Gateway gemeint ist [O, OP-04].

**Voraussetzungen, die Livos und Trios klären** (OP-04): Name und Typ des Hosters (DATEVasp, SmartIT oder PARTNERasp), wer DATEV-Systembetreiber und Lizenznehmer ist (Livos oder Trios), ob alle Mandanten auf einem DATEV-System unter einer Beraternummer liegen, und ob das Riecken-Gateway bei Livos bereits für eine andere Anwendung genutzt wird. Liegen die Mandanten auf mehreren DATEV-Systemen, sind mehrere Gateway-Verbindungen nötig.

### 15.2.2 Ablauf der Übergabe (S-01)

1. Der Beleg durchläuft in WF-01 die Schritte bis zur **Zahlungsfreigabe** (AE-06).
2. Im Schritt **Buchhaltung** kontrolliert Trios (R-06) Kontierung und Steuerschlüssel in der Maske M-07.
3. An der Schrittverbindung „Übergabe" löst smart invoice das Ereignis `integration.export` aus. Die Übergabe ist **ereignisgesteuert je Rechnung**, nicht zeitgesteuert (smart invoice API-Handbuch).
4. LDconnect überträgt den Buchungsvorschlag über das Gateway in DATEV Kanzlei-Rechnungswesen. Der Beleg geht als Dokumentenlink mit.
5. Trios übernimmt den Buchungsvorschlag in DATEV und bucht. Erst dann entsteht der offene Posten. „Automatisch in DATEV" bedeutet also: Der Vorschlag liegt bereit; gebucht wird durch Trios.
6. Der Workflow endet im Status „Übergeben". Der Status „bezahlt" folgt später über S-06.

Die Katalogforderung 5.1 „nicht nur pauschal 1× pro Tag" ist damit erfüllt. Ob LDconnect sofort je Ereignis oder in einem kurzen Intervall überträgt, bestätigt LIONDEER im Projekt [O, OP-22].

### 15.2.3 Feldliste Buchungsvorschlag

LDconnect überträgt je Buchungssatz höchstens die folgenden 16 Felder (LDconnect Leistungsschein 11/2025). Die Spalte „Quelle in smart invoice" ist ein Mapping-Vorschlag, der im Test-Tenant bestätigt wird.

| Nr. | DATEV-Feld | Inhalt / Quelle in smart invoice (Vorschlag) | Eigenschaft |
|---|---|---|---|
| 1 | Belegfeld 1 | Rechnungsnummer des Lieferanten | E-08 |
| 2 | Belegfeld 2 | frei belegbar? (z. B. Fälligkeit) – Belegung mit LIONDEER klären [O, OP-22] | – |
| 3 | Brutto-Betrag | Bruttobetrag der Rechnung | E-11 |
| 4 | BU-Gegenkonto | Kreditorenkonto je Mandant (70000er/80000er) | E-05 |
| 5 | Buchungstext | Kreditorname / Kurztext (Konvention im Prozess-Workshop festlegen) | E-06 |
| 6 | Datum | Rechnungsdatum (bestimmt auch das Geschäftsjahr) | E-09 |
| 7 | Dokumentenlink | Link auf den Beleg im d.velop-Archiv (Beleganzeige Drittanbieter) | – |
| 8 | Geschäftspartner | Kreditor | E-05 |
| 9 | Konto | Sachkonto (Positions- bzw. Kontierungszeile) | E-17 |
| 10 | KOST1 | Kostenstelle | E-17 |
| 11 | KOST2 | Kostenträger/Objekt | E-17 |
| 12 | Leistungsdatum | Leistungsdatum/-zeitraum | E-10 |
| 13 | Steuersatz | aus Kontierung | – |
| 14 | Steuerschlüssel (BU-Code) | aus Kontierung; bei § 13b der entsprechende Schlüssel | E-20 |
| 15 | Waren und Dienstleistungen | Kennzeichen aus Kontierung | – |
| 16 | WKZ | Währung | – |

**Bekannte Einschränkungen (belegt):** Stammdaten kommen mit technischer Feldlänge, also mit führenden Nullen. Es werden nur Vorsteuerschlüssel synchronisiert. Buchungsvorschläge werden dem Geschäftsjahr nach Rechnungsdatum zugeordnet, auch wenn der Abschluss dieses Jahres bereits erfolgt ist (LDconnect Leistungsschein 11/2025). Für den Jahreswechsel braucht Trios deshalb eine Regel, wie Vorschläge für abgeschlossene Jahre behandelt werden [O, OP-05].

### 15.2.4 Fehlende Felder und Konsequenzen

| Nicht übertragenes Feld | Konsequenz | Lösung im Konzept |
|---|---|---|
| Fälligkeit | DATEV berechnet die Fälligkeit aus der Zahlungsbedingung des Kreditorenkontos | Zahlungsbedingung in DATEV pflegen (Trios); Abweichung am Beleg zeigt smart invoice als Hinweis [S]; ggf. Belegfeld 2 [O] |
| Skonto | wie Fälligkeit; Skonto aus der DATEV-Zahlungsbedingung | Skontoüberwachung vor der Übergabe über Eskalation und Skontoampel in smart invoice (Kapitel 10) |
| Postensperre | Ein übergebener Posten ist in DATEV sofort zahlbar | Übergabe erst **nach** der Zahlungsfreigabe (AE-06, AE-08) |
| IBAN | DATEV nutzt die Bankverbindung des Kreditorenkontos | IBAN-Abgleich Beleg gegen Stamm vor der Freigabe in smart invoice (Kapitel 9, OP-10) |
| Zahlbetrag (Kürzung/Einbehalt) | LDconnect überträgt den Bruttobetrag | Behandlung gekürzter Zahlbeträge in DATEV und im Zahlungsvorschlag mit Trios festlegen (AE-14, OP-05) |

### 15.2.5 Stammdatenabruf (S-02)

LDconnect ruft **täglich** für alle konfigurierten DATEV-Mandanten Kreditoren, Sachkonten, Steuerschlüssel, Zahlungsbedingungen, Kreditor-Bankverbindungen, KOST1 und KOST2 ab und spielt sie in den smart-invoice-Bucket ein (LDconnect Leistungsschein 11/2025). Daraus folgt:

- Ein neu in DATEV angelegter Kreditor steht erst am **Folgetag** in smart invoice zur Verfügung. Der Klärfall „Kreditor fehlt" (WF-04) wartet so lange. Ob LIONDEER einen Abruf im Tagesverlauf oder auf Knopfdruck anbietet, ist offen [O, OP-22].
- Die Kreditor-Bankverbindungen sind die Grundlage des IBAN-Abgleichs.
- Die Kreditoren sind je Mandant angelegt. Die Service-Limits je Bucket (1.000 Mandanten, 100.000 Kreditoren, 100.000 Kreditor-Bankverbindungen, 50.000 Sachkonten, 50.000 Kostenstellen; höchstens 50 Buckets) werden bei über 100 Mandanten relevant (d.velop invoices Leistungsbeschreibung 12/2025). Beispielrechnung: 110 Mandanten mit durchschnittlich 500 Sachkonten ergeben 55.000 Sachkonten und liegen über dem Limit. Das Mengengerüst (Kreditoren und Sachkonten je Mandant) erhebt Trios in Phase 0 (OP-21). Ist das Limit erreicht, werden zuerst nur genutzte Konten übertragen bzw. Sachkonten ohne Mandantenbezug angelegt (OP-22); erst als letzte Option werden die Mandanten auf mehrere Buckets verteilt, z. B. je Segment (Kapitel 6.6, OP-04).

### 15.2.6 Mandantenschlüssel

In DATEVconnect wird ein Mandant über die Kombination **Beraternummer-Mandantennummer** angesprochen (Beispiel: „29098-55003"). Nach AE-03 ist die Mandanten-ID in d.velop gleich diesem DATEV-Schlüssel. Das Format stimmt MDIS mit Trios ab. Der Schlüssel ist identisch in smart invoice (Mandant), in der DMS-Eigenschaft E-01, in der Freigabematrix, in den Restriction Sets, in der Lieferanten-App und in allen BeSync-Nachrichten.

### 15.2.7 Fehlerhandling DATEV-Übergabe

| Fehlerbild | Erkennung | Behandlung | Verantwortlich |
|---|---|---|---|
| Übergabe technisch gescheitert (Gateway, DATEVconnect nicht erreichbar) | Beleg bleibt im Exportzustand bzw. läuft in den Fehlerschritt; Schnittstellenprotokoll LDconnect | automatische Wiederholung laut LDconnect; bei Dauerstörung Ticket an LIONDEER/Hoster | MDIS (Monitoring), LIONDEER, Hoster |
| Fachlich abgelehnt (Konto gesperrt, Steuerschlüssel ungültig, Kreditor fehlt) | Fehlermeldung am Beleg | Beleg zurück an Buchhaltung (Trios), Korrektur, erneute Übergabe | Trios |
| Wiederholte Fehler | smart invoice meldet bei der Standardintegration nach vier Fehlschlägen in Folge ein „Technisches Problem" und deaktiviert die Integration nach sieben Tagen ohne Erfolg. Belegt ist das für die Standardintegration Dynamics; für LDconnect bestätigt d.velop [O, OP-22] | tägliche Prüfung der Fehlerliste; Eskalation nach 24 h | MDIS |
| Stammdatenabruf gescheitert | fehlende Aktualisierung (Datum letzter Abruf) | Nachlauf; Klärfälle „Kreditor fehlt" prüfen | MDIS, LIONDEER |
| Abweichung d.velop ↔ DATEV | Abstimmliste: übergebene Belege je Mandant und Tag gegen Buchungsvorschläge in DATEV | Klärung zwischen Trios und MDIS | Trios, MDIS |

### 15.2.8 Mengen- und Kostenhinweis

Die Anbindung verursacht laufende Kosten bei mehreren Herstellern. Die Option „DATEV Rechnungswesen" ist kostenpflichtig. LDconnect wird nach Anzahl der Mandanten und Rechnungen lizenziert; über 75 Mandanten fällt je weiterem Mandant eine Zusatzgebühr an. Die DATEV Beleganzeige Drittanbieter und das DATEVasp-Zusatzmodul sind DATEV-seitig kostenpflichtig. Das Gateway wird separat vertraglich geregelt. Ein Testsystem für LDconnect ist verfügbar und für die Abnahme einzuplanen. Die konkreten Konditionen enthält das Angebot, nicht dieses Konzept.

### 15.2.9 Zweistufige gegenüber einstufiger Übergabe

Das Livos-Zielbild zeigt zwei DATEV-Kontakte: ein **ER-Vorerfassungsjournal** bei der Verteilung und die **Verbuchung** nach der fachlichen Freigabe. Der LDconnect-Standard kennt je Rechnung nur eine Übergabe. MDIS empfiehlt deshalb die einstufige Übergabe (AE-08, Status O).

| Kriterium | Einstufig (Empfehlung) | Zweistufig (Option Phase 3) |
|---|---|---|
| Ablauf | Übergabe nach Zahlungsfreigabe im Schritt Buchhaltung | frühe Übergabe als Buchungsvorschlag **mit Postensperre**, Aufhebung der Sperre nach Zahlungsfreigabe |
| Technik | LDconnect-Standard [K] | BeSync über EXTF-Buchungsstapel (Feld „Postensperre") oder DATEVconnect [A]; ob sich die Sperre per DATEVconnect setzen und aufheben lässt, ist offen [O] |
| Transparenz über unverbuchte Rechnungen | Rechnungseingangsbuch (Status, Beträge, CSV-Export zum Monatsende, z. B. für Rückstellungen) | DATEV-Vorerfassung |
| Risiko | gering; Zahlung erst nach d.velop-Freigabe möglich | Doppelpflege, Sperrlogik, zweiter Kanal |
| Entscheidung | mit Trios und Livos (OP-05) | nur bei nachgewiesenem Bedarf |

## 15.3 Zahlungsprozess (S-06, S-07)

### 15.3.1 Zielprozess

smart invoice erzeugt keine Zahlungsdatei und gibt keine Zahlungsfreigabe an DATEV weiter (d.velop invoices Leistungsbeschreibung 12/2025; LDconnect Leistungsschein 11/2025). Die Zahlung läuft deshalb über den DATEV- und den multicash-Standard. BeSync schließt den Rückweg nach d.velop (AE-10, Katalog 5.5 = A).

| Nr. | Schritt | System | Verantwortlich | Schnittstelle | Status in d.velop |
|---|---|---|---|---|---|
| 1 | Zahlungsfreigabe (darf gezahlt werden, Zahlbetrag, Skonto) | smart invoice | R-05 Zahlungsfreigeber | – | Zahlungsfreigegeben |
| 2 | Buchungsvorschlag + Beleglink | smart invoice → DATEV | automatisch, Kontrolle Trios | S-01 | Übergeben |
| 3 | Buchen, offener Posten entsteht | DATEV Kanzlei-Rechnungswesen | Trios | – | – |
| 4 | Zahlungsvorschlag aus OPOS (Fälligkeit, Skonto) | DATEV | Trios (bzw. Livos, OP-04) | – | – |
| 5 | Export SEPA-XML (pain.001) | DATEV Zahlungsverkehr | Trios | S-07 | – |
| 6 | Import in multicash, Unterschrift nach Unterschriftsklassen, Versand per EBICS | multicash | R-05 (Livos Treasury/GF) | S-07 | – |
| 7 | Kontoauszug (camt.053/MT940) → DATEV, Ausgleich des offenen Postens | multicash → DATEV | Trios | S-07 (Rückweg) | – |
| 8 | Zahlstatus lesen und am Beleg setzen | DATEV → BeSync → d.velop | automatisch (MDIS) | S-06 | Zahlstatus „bezahlt"/„teilbezahlt", Zahldatum |

### 15.3.2 multicash (S-07)

multicash (Omikron) importiert Zahlungsdateien aus Buchhaltungssystemen. Welche Mitarbeitenden Zahlungen erfassen, freigeben und einreichen dürfen, steuert ein frei konfigurierbares Konzept von Zahlungs- bzw. Unterschriftsklassen mit einfacher Unterschrift, Vier- oder Mehr-Augen-Prinzip. Die Übertragung an die Banken läuft über EBICS (multicash, Herstellerangaben). DATEV exportiert SEPA-Zahlungsaufträge als XML-Datei für Bankprogramme und übernimmt Kontoumsätze aus „MULTiCASH und Derivaten" (DATEV-Hilfe).

Die Unterschrift in multicash bleibt die bankseitige Kontrolle. Die fachliche Zahlungsfreigabe in d.velop ersetzt sie nicht. Der Gedanke „beim Buchen geht die Zahlung raus" (Workshop 22.09.2026, 00:33:28) wird deshalb nicht umgesetzt. Eine automatische Dateiablage der SEPA-Datei in ein multicash-Importverzeichnis ist als BeSync-Erweiterung möglich [A, optional]. Voraussetzung sind Angaben zu Produkt, Version und Importweg bei Livos [O, OP-24].

**Nicht empfohlen:** eine SEPA-Datei direkt aus d.velop bzw. BeSync. Sie würde am DATEV-Zahlungsvorschlag vorbeilaufen. Das Risiko von Doppelzahlungen und doppelter Skontologik widerspricht P4.

### 15.3.3 Zahlstatus-Rückmeldung (S-06)

| Element | Festlegung |
|---|---|
| Quelle | DATEVconnect Rechnungswesen, Ressource `accounting/v1/clients/{client}/fiscal-years/{fy}/accounts-payable` (offene Posten der Kreditoren). Darüber ist der Zahlstatus bereits gebuchter Rechnungen abrufbar: voll, teilweise oder nicht bezahlt. Die Ressource wird vor der Umsetzung im DATEV Developer Portal verifiziert [O, OP-43; Test T40]. |
| Zugang | über dasselbe Riecken-Gateway wie S-01; eigener technischer DATEV-Benutzer mit Leserecht (Vorschlag) |
| Abgleichsschlüssel | Mandanten-ID (Beraternr.-Mandantennr.) + Kreditor-Nr. + Belegfeld 1 (Rechnungsnummer) + Betrag; ergänzend der Dokumentenlink, falls DATEV ihn am Posten zurückliefert; Festlegung mit Trios [O, OP-43] |
| Frequenz | täglich nachts (Vorschlag); optional mehrfach täglich |
| Ziel | DMS-Eigenschaften E-23 „Zahlstatus" (bezahlt/teilbezahlt/offen) und „Zahldatum" am archivierten Beleg (DMS-API). smart-invoice-Belege sind nach Abschluss nicht per API änderbar, die DMS-Eigenschaften schon. |
| Nicht gefunden | Kein Abgleich möglich (z. B. Rechnungsnummer in DATEV abweichend erfasst) → Eintrag in einer Klärliste für Trios; kein Überschreiben |
| Optional | früher Status „ausgeführt" aus multicash-Statusberichten (pain.002), falls Livos dies nutzt [O, OP-24] |
| Nutzen | durchgängige Statuskette „Eingang → Freigabe → Übergeben → Bezahlt" in Suche und Akte; Grundlage der KPIs Skontoquote und Durchlaufzeit bis Zahlung (Kapitel 16) |

MDIS prüft in Phase 0, ob eine bestehende BeSync-Anbindung an DATEVconnect mit Zahlstatus-Abfrage in der Livos-Gateway-Umgebung wiederverwendet werden kann.

## 15.4 BIM4You (S-08, S-09, S-10)

### 15.4.1 Ausgangslage

BIM4You (BIB GmbH) führt Bau-Budget, Vergabeeinheiten, Verträge und Nachträge. Es hat ein eigenes Rechnungseingangsbuch, einen Prüf- und Freigabe-Workflow (Vier-Augen, optional dritte Prüfstufe ab Betragsgrenze), Zahlungsfreigaben mit Abzügen und Sicherheits- bzw. Gewährleistungseinbehalten sowie eine § 48-Prüfung (BIM4You Jahresrelease 2022–2026). Eine öffentliche REST-API ist **nicht dokumentiert**. Belegt sind dateibasierte Wege: E-Rechnungsimport (XRechnung/ZUGFeRD) in das Rechnungseingangsbuch, Scanordner, eine DMS-Anbindung über Austauschordner und Barcode sowie ein DATEV-Buchungsstapel-Export (Zusatzlizenzen). Die Anbindung an d.velop braucht deshalb BeSync [A] (AE-11, Katalog 5.3 = A).

### 15.4.2 Hinweg (S-08)

| Element | Festlegung |
|---|---|
| Auslöser | WF-02: Schrittverbindung „Bauprüfung" nach der Sachlichen Prüfung. Bedingung: Kreditor-Kennzeichen „Bauleistender" oder Objekt = Bauprojekt oder Belegart Abschlags-/Schlussrechnung (E-14) |
| Technik d.velop-Seite | smart-invoice-Export an die Integration „BIM4You" als **asynchroner Transfer** über die Abhol-API. BeSync holt den Beleg ab und meldet erst nach der BIM4You-Entscheidung Erfolg oder Fehler zurück. Das Zeitfenster ist standardmäßig 2 Tage und bis **28 Tage** einstellbar; d.velop empfiehlt, es so kurz wie möglich zu halten (smart invoice API-Handbuch). In dieser Zeit steht der Beleg im Zustand „aktiver Belegdatentransfer" ohne Benutzeraktion. |
| Datenobjekt | Mandant (E-01), Kreditor-Nr. (E-05) und Konsolidierungsnummer (E-07), Rechnungsnummer, Rechnungs- und Leistungsdatum, Netto/Steuer/Brutto, Belegart, Projekt/Objekt-ID (E-03), Vergabeeinheit/Gewerk (E-18), Vertrags-/Auftragsnummer (E-19), Positionen, Link auf das Dokument, Beleg-ID |
| Übergabe an BIM4You | bevorzugt als E-Rechnung (XRechnung/ZUGFeRD) mit BIM4You-Vertragsnummer im Feld „Contract Number". BIM4You ordnet die Rechnung dann automatisch der Vergabeeinheit zu. Bei Papier- oder PDF-Rechnungen: PDF plus Metadaten über den Scan- bzw. Austauschordner. Welcher Weg bei Livos lizenziert ist, klärt Livos mit der BIB GmbH [O, OP-06]. |
| Schlüssel | **Beleg-ID** der d.velop-Rechnung als **Barcode** im BIM4You-Rechnungseingangsbuch. Über die BIM4You-Variable für die DMS-URL entsteht daraus ein Link zurück auf den d.velop-Beleg. **Vertragsnummer** (BIM4You) für die Zuordnung zur Vergabeeinheit. Mandant und mandantenbezogene Kreditorennummer wie in DATEV. |

### 15.4.3 Rückweg (S-09)

| Element | Festlegung |
|---|---|
| Auslöser | Freigabe (letzte Prüfstufe) oder Storno in BIM4You |
| Technik | BeSync fragt den Status regelmäßig ab (Polling, Vorschlag alle 15 Minuten), weil BIM4You keine Webhooks dokumentiert. Quelle: Export bzw. Übergabeordner (z. B. Zahlungsfreigabe-PDF über einen Infoserver-Job). Ein direkter Lesezugriff auf die BIM4You-Datenbank nur mit Freigabe der BIB GmbH [O]. |
| Datenobjekt | Freigabestatus BIM4You mit Datum und Freigeber, geprüfter Betrag, Einbehalte und Abzüge (Art, Betrag), Nachlass, Kostenaufteilung, Prüfbericht bzw. Zahlungsfreigabe-PDF |
| Schreiben in d.velop | DMS-API: Eigenschaften E-22 (Sicherheitseinbehalt, geprüfter Betrag BIM4You, Freigabestatus BIM4You) am Rechnungsdokument; Prüfbericht als Dokument der Kategorie K-08 in der Vorgangs- und Objektakte |
| Weiterlauf des Workflows | BeSync meldet den Transfer als **erfolgreich**, der Beleg läuft zur Fachlichen Freigabe und Zahlungsfreigabe in d.velop. Bei Ablehnung oder Storno meldet BeSync einen **Fehler mit Klartext** (Deutsch/Englisch); der Beleg geht an den Fehlerschritt „Klärung Bau". |
| Zahlbetrag | Den Zahlbetrag (E-12) im smart-invoice-Beleg setzt die Rechnungsprüfung auf Basis des BIM4You-Ergebnisses. Ein API-Schreibzugriff auf laufende Belege ist nicht dokumentiert (L4, OP-07). |

**Webhook-Variante als Rückfall:** Wird statt der Abhol-API ein Webhook-Export genutzt, muss BeSync innerhalb von **30 Sekunden** quittieren, sonst läuft der Beleg in den Fehlerschritt (smart invoice API-Handbuch). Der Beleg wartet dann in einem Schritt „Warten auf BIM4You" und wird von der Buchhaltung manuell fortgesetzt. Diese Variante ist robuster gegen lange Prüfzeiten über 28 Tage, erfordert aber einen manuellen Handgriff.

**Fehlerschritt:** Für WF-02 wird ein eigener Fehlerschritt „Klärung Bau" mit Zuständigkeit R-02 und Eskalation konfiguriert. Dorthin laufen Belege bei Transferfehler, Ablehnung in BIM4You, Überschreitung des Zeitfensters und Storno.

### 15.4.4 Stammdaten BIM4You (S-10)

Projekte, Vergabeeinheiten/Lose und Verträge kommen nächtlich als `custom_entities` (Kopffelder) bzw. `other_dimensions` (Positionsfelder, hierarchisch) in den smart-invoice-Bucket. Damit sind sie in der Kontierung auswählbar und für KI-Kontierungsvorschläge nutzbar. Die Objekt-ID (E-03) ist mit der BIM4You-Projekt-ID im Objektstamm der Lieferanten-App verknüpft (AE-28).

### 15.4.5 Abgrenzungen und offene Punkte

| Thema | Festlegung |
|---|---|
| Keine Doppelübergabe DATEV | Nur d.velop übergibt Eingangsrechnungen nach DATEV (S-01). Der BIM4You-DATEV-Export bleibt für Eingangsrechnungen deaktiviert (L3). |
| Sonderbuchungsinfos (ARAP/PARP, Rückstellungen, Anzahlungen) | Folgeprojekt. Quelle, Format und Buchungskanal klären Livos, Trios und BIB GmbH [O, OP-28]. |
| Umlageinformationen | Bedeutung offen (Kostenaufteilung auf Einheiten oder Umlagefähigkeit) [O, OP-18]. |
| Führendes System je Rechnungstyp Bau | Empfehlung: d.velop führt Beleg und Workflow, BIM4You führt Budget und Prüfergebnis; mit Livos zu bestätigen [O, OP-06]. |
| Referenzmuster | Ein Immobilien- und Wohnungsbauunternehmen hat DocuWare, BIM4You und DATEV mit eigenen Schnittstellen gekoppelt: Erkennung im DMS → Belegprüfung → fachliche Prüfung in BIM4You → Prüfprotokoll löst den nächsten DMS-Schritt aus → Buchung in DATEV (DocuWare Referenzbericht Krieger + Schramm). Das Muster entspricht dem Livos-Zielbild. Eine Referenz mit d.velop ist nicht bekannt. |
| Betrieb BIM4You bei Livos | On-Premises oder gehostet, Version, Erreichbarkeit für BeSync: Livos-IT [O, OP-42]. |

## 15.5 BeSync und Lieferanten-App (S-04, S-05, S-11, S-12, S-15, S-16)

### 15.5.1 Architektur

BeSync ist die Middleware-Plattform von MDIS. Livos nutzt sie bereits für die Lieferanten- bzw. Stammdaten-App (Workshop 22.09.2026, 00:40:09). BeSync unterstützt REST, SOAP, SQL, Dateien (CSV, JSON, XML) und Webhooks sowie Monitoring und Alarmierung (MDIS Middleware). Im Livos-DMS übernimmt BeSync vier Rollen:

| Rolle | Schnittstellen | Muster |
|---|---|---|
| Stammdatendrehscheibe | S-04, S-05, S-10 | nächtlicher Delta-Batch + Einzelanlage aus Benutzeraktion |
| Prozessbrücke | S-06, S-08, S-09, S-11 | Ereignis aus smart invoice (Export/Webhook) → Verarbeitung → Rückmeldung per DMS-API oder Transfer-Status |
| Ereignisprotokoll | S-12 | Webhook je Schrittwechsel + nächtliche API-Abfrage → MS-SQL-Staging |
| Werkzeuge | S-15, S-16 | anlassbezogene Skripte (Export, Import) |

Aufbau in Schichten: (1) Eingangsadapter (Webhook-Endpunkte mit Signaturprüfung, Poller für DATEV und BIM4You), (2) Warteschlange mit Wiederholung und Ablage für nicht zustellbare Nachrichten, (3) Verarbeitungslogik je Schnittstelle, (4) Ausgangsadapter (d.velop-APIs, Mailversand, Dateiablage), (5) Protokoll- und Staging-Datenbank (MS SQL), (6) Überwachung und Alarmierung.

### 15.5.2 Lieferanten-App und Stammdaten (S-04, S-05)

| Datenfluss | Inhalt | Ziel in d.velop | Technik |
|---|---|---|---|
| Gesellschaftsstamm → smart-invoice-Mandanten | Mandanten-ID, Name **exakt wie auf Rechnungen**, Anschrift, Konzernstruktur (`parent_id`) | smart invoice `companies` | Stammdaten-API (Batch, asynchron mit Job-Status) |
| Gesellschafts- und Objektstamm → DMS | Mandant, Mandantenname, Objekt-ID, Objektbezeichnung, Segment, Verwaltungsart | Datasets/Wertemengen, Restriction Sets `RS_Mandant`/`RS_Objekt` | DmsConfig-/DMS-API |
| Konsolidierungsnummer → Beleg | Konsolidierungsnummer zu (Mandant, Kreditor-Nr.) | DMS-Eigenschaft E-07 | DMS-Webhook (Eigenschaften prüfen/aktualisieren) oder dynamische Wertemenge |
| Kreditor-Mapping ← DATEV | Kreditorennummern je Mandant (70000er/80000er) | Mapping-Tabelle in der Lieferanten-App | DATEVconnect lesend (S-05) |
| Anlage-Anforderung → Trios | fehlender Kreditor mit Stammdaten und Beleg-Referenz | Aufgabe/E-Mail an Trios; Anlage in DATEV; Sync am Folgetag (S-02) | S-05 |

Die fachliche Pflege liegt bei R-12 in der Lieferanten-App (M-16). Das Kreditorobjekt in smart invoice hat kein freies Feld für die Konsolidierungsnummer. Deshalb trägt die DMS-Eigenschaft E-07 sie am Beleg (AE-09). Eine neue Gesellschaft entsteht in einem Durchlauf: Dataset-Wert, Gruppe, Restriction-Set-Zuordnung und smart-invoice-Mandant per API; die REB-Berechtigung setzt ggf. R-12 manuell (AE-18).

### 15.5.3 Technische Benutzer und API-Keys

| Technischer Benutzer (Vorschlag) | Schnittstellen | Rechte (minimal) |
|---|---|---|
| `svc_besync_stamm` | S-04, S-10 | smart-invoice-Stammdaten schreiben (nur Mandanten und ergänzende Entitäten); DmsConfig (Datasets, Restriction Sets) – erfordert Mandanten-Administrator |
| `svc_besync_prozess` | S-06, S-08, S-09, S-11 | Transfers abholen/zurückmelden; DMS-Eigenschaften E-07, E-22, E-23 schreiben; K-07/K-08 ablegen |
| `svc_besync_report` | S-12 | Lesen: Task-, Process- und DMS-Suche (Rolle „Service user") |
| `svc_besync_export` | S-15 | Recht „Datenexport"; Lesen je Gesellschaft; nur bei Bedarf aktiv |
| `svc_graph_mail` (Entra-App) bzw. d.velop-Messaging-Berechtigung | S-11 | Mail senden aus einem definierten Absenderpostfach; Technik gemäß Festlegung in Phase 0 (OP-25) |
| DATEV-Benutzer (lesend) | S-05, S-06 | DATEVconnect lesen für alle angebundenen Bestände |

Technische Benutzer gehören zur technischen Benutzergruppe ohne interaktive Anmeldung. Sie authentifizieren sich mit **API-Key als Bearer-Token** (d.velop Identity Provider). Schreibende DMS-API-Aufrufe brauchen den `Origin`-Header (d.velop DMS-API). API-Keys liegen im Secret-Store von BeSync, nie im Klartext in Konfigurationsdateien (siehe 15.8.4).

### 15.5.4 Rate-Limits

| Grenze | Wert | Quelle | Maßnahme |
|---|---|---|---|
| DMS-API Änderungen | 600 je Minute und Mandant (Tenant) | d.velop DMS-API | Drosselung in BeSync; Stapel verteilen |
| DMS-API Neuanlagen | 1.600 je Minute und Mandant | d.velop DMS-API | wie oben |
| Überschreitung | HTTP 429 | d.velop DMS-API | Wiederholung mit exponentiellem Backoff |
| smart-invoice-Stammdaten Einzel-PUT | synchron mit Rate-Limit (429), nur im Rahmen einer Anwendungsinteraktion | smart invoice API | Massendaten nur als Batch-Job |
| Webhook-Quittung smart invoice | 30 Sekunden | smart invoice API | sofort quittieren, asynchron verarbeiten |
| Wertemengen-Webhook | konfigurierbarer Timeout, höchstens 3 Versuche | d.velop Administration | schnelle Antwort aus Cache |
| Task-Historie | Standard 30 Tage, höchstens 365 Tage | d.velop Task-API | laufende Extraktion (S-12) |

Beim Livos-Mengengerüst (20–30 Rechnungen am Tag) liegen die laufenden Lasten weit unter den Grenzen. Kritisch sind nur Massenläufe: Erstbefüllung, Nachtragen der Konsolidierungsnummer und Zahlstatus-Nachlauf nach Störungen.

### 15.5.5 Monitoring und Protokollierung

| Überwachungsobjekt | Prüfung | Schwelle (Vorschlag) | Reaktion |
|---|---|---|---|
| Webhook-Endpunkte BeSync | Erreichbarkeit, Antwortzeit | Antwort > 5 s oder Ausfall | Alarm MDIS; Belege im Fehlerschritt prüfen |
| Warteschlange | nicht verarbeitete Nachrichten | älter als 1 h | Alarm MDIS |
| Transfers BIM4You | offene Transfers, Alter | älter als 20 Tage | Hinweis an R-02; vor Ablauf des 28-Tage-Fensters handeln |
| Zahlstatus-Lauf | erfolgreich, Anzahl Treffer/Nichttreffer | Lauf fehlt oder Nichttreffer > 5 % | Klärliste an Trios |
| Stammdatenlauf | erfolgreich, Anzahl Änderungen | Lauf fehlt | Nachlauf |
| Mailversand S-11 | Zustellfehler | jeder Fehler | Aufgabe an R-02 |
| API-Fehler | HTTP 429/5xx | Häufung | Drosselung prüfen |

Jede Nachricht wird mit Zeitstempel, Schnittstelle, Beleg-ID, Mandant, Ergebnis und Fehlertext protokolliert. Das Protokoll wird 12 Monate aufbewahrt (Vorschlag); Protokolle zu buchungsrelevanten Vorgängen wie Zahlstatus und Übergaben entsprechend den Fristen in Kapitel 17.

### 15.5.6 Betrieb durch MDIS

MDIS betreibt BeSync einschließlich Hosting, Updates, Überwachung, Fehlerbehebung und Anpassung an Release-Änderungen von d.velop, DATEV und BIM4You (Kapitel 18). Livos erhält einen monatlichen Betriebsbericht (Verfügbarkeit, Nachrichtenvolumen, Störungen, offene Klärfälle).

### 15.5.7 Abgrenzung: Was BeSync tut und was nicht

| BeSync tut | BeSync tut nicht |
|---|---|
| Gesellschafts- und Objektstamm aus der Lieferanten-App in smart invoice und d.velop documents übertragen (S-04) | DATEV-Kreditoren, Sachkonten oder Steuerschlüssel in den smart-invoice-Bucket schreiben (das macht LDconnect) |
| Konsolidierungsnummer am Beleg setzen (S-04) | Kreditoren in DATEV anlegen (das macht Trios) |
| Anlage-Anforderung für fehlende Kreditoren an Trios stellen (S-05) | Eingangsrechnungen nach DATEV buchen oder übergeben (das macht S-01) |
| Zahlstatus aus DATEV lesen und als DMS-Eigenschaft setzen (S-06) | Zahlungsdateien erzeugen oder Zahlungen auslösen |
| Bau-Rechnungen an BIM4You übergeben und das Ergebnis zurückholen (S-08 bis S-10) | Budget-, VOB- oder Einbehaltslogik rechnen (das macht BIM4You) |
| Rückweisungs-, Kürzungs- und PM-Rückmelde-Mails versenden und ablegen (S-11) | Freigabeentscheidungen treffen oder Workflow-Regeln enthalten (das macht smart invoice) |
| Prozessereignisse für evidanza protokollieren (S-12) | laufende smart-invoice-Belege verändern (L4) |
| Export je Gesellschaft ausführen (S-15), PM-Buchungsdaten einlesen (S-16) | Originaldokumente verändern oder löschen |
| technische Tabellen selbst pflegen (MDIS) | Livos zur Pflege technischer Tabellen verpflichten |

## 15.6 Identität und E-Mail (S-13, S-14)

### 15.6.1 Identitäten (S-13)

| Element | Festlegung | Beleg |
|---|---|---|
| Anmeldung | Single Sign-on über **OpenID Connect** mit Microsoft Entra ID; weitere Identity Provider und AD-Integration ab Edition business | d.velop documents Leistungsbeschreibung Cloud [S] |
| Provisionierung | **SCIM 2.0** an den Endpunkt `…/usermanagement/scim` des Tenants mit dem API-Key des Benutzers „Builtin SCIM 2.0 provisioning user" | d.velop Administration Cloud [S/K] |
| Gruppenmodell | **flache** Gruppen. Entra ID stellt nur direkte Mitglieder zugewiesener Gruppen bereit, keine verschachtelten Gruppen (Microsoft Learn). Rollen-, Gesellschafts- und Objektgruppen nach AE-18 | [K] |
| Deaktivierung | Scope-Verlust in Entra ID deaktiviert bzw. löscht den Benutzer in d.velop; Aufgaben vorher umverteilen | Microsoft Learn; Kapitel 18 |
| Externe | B2B-Gäste sind bereitstellbar; Kernpartner (R-08) erhalten Konten mit 2FA/FIDO2 | [S], OP-03 |
| Technische Benutzer | nicht aus Entra ID, sondern als technische Benutzer im Tenant | [S] |
| Voraussetzung | Livos nutzt Entra ID [O, OP-16] | – |

### 15.6.2 E-Mail-Eingang (S-14)

| Element | Festlegung | Beleg |
|---|---|---|
| Technik | **email import über Microsoft Graph**: App-Registrierung in Entra ID mit den Berechtigungen Mail.ReadWrite und User.ReadBasic.All sowie Client-Secret | d.velop email import [S] |
| Postfächer | `rechnung@…` mit Alias je Gesellschaft (AE-22), `freigabe-hv@…` für WF-03 (AE-12), Postfächer für Post und Verträge (Phase 4) | [K] |
| Importprofile | je Postfach bzw. Alias mit Vorbelegung (z. B. Mandant, Eingangskanal E-25); ob der document reader einen vorbelegten Mandanten übernimmt, wird getestet [O, OP-02] | [K] |
| Kommunikationsweg | direkter Weg inbound → document reader → smart invoice von Beginn an; der alte Weg wird am 01.01.2027 abgeschaltet (d.velop Helpcenter 09/2026) | [S] |
| Grenzen | höchstens 10.000 E-Mails je Monat und Postfach in C1/H/O (d.velop invoices Leistungsbeschreibung 12/2025); Abrufintervall nicht dokumentiert | – |
| Überwachung | Jobübersicht des email import (Neustart möglich); Postfachordner für verarbeitete und nicht verarbeitete Mails | [S] |
| Nicht verfügbar | **IMAP** ist in d.velop nur als „zukünftig" angekündigt; Exchange On-Premises nur über einen eigenen Abrufdienst (EWS). Voraussetzung ist deshalb Microsoft 365 [O, OP-16]. | d.velop email import |

## 15.7 Property Manager (S-16) und ERP/PM-Anbindung perspektivisch (S-17)

### 15.7.1 Grundsatz

Die rund zehn Property Manager wechseln und dürfen nicht zur Nutzung eines Livos-Systems verpflichtet werden. Ihre Hausverwaltungssysteme sind heterogen (u. a. Aareon Wodis, RELion, Karthago, DOMUS, iX-Haus, immoware24). Gemeinsam ist fast allen nur der **DATEV-Export** (Herstellerangaben). Der PM-Kanal bleibt deshalb E-Mail: Eingang über S-14 (`freigabe-hv@…`), Rückmeldung über S-11 (AE-12). Eine Anbindung je PM-System ist nicht wirtschaftlich.

### 15.7.2 PM-Buchungsdaten (S-16, optional, Phase 3)

| Element | Festlegung |
|---|---|
| Quelle | bestehendes Monatspaket der PM an Trios: DATEV-Buchungsstapel (DATEV-Format), ggf. Kreditorenstamm |
| Einlieferung | Upload in einen BeSync-Eingangsordner oder Funktionspostfach [A] |
| Verarbeitung | Parser DATEV-Format; Mapping der 80000er-Kreditoren auf die Konsolidierungsnummer in der Lieferanten-App |
| Nutzung | (1) Vollständigkeitsabgleich: Jede gebuchte PM-Rechnung über dem Schwellwert hat eine Freigabe aus WF-03. (2) Kreditorenabgleich gesellschaftsübergreifend. (3) Kennzahlen im BI |
| Voraussetzung | Format und Lieferweg der PM-Daten klären (Livos, Trios) [O, OP-29] |
| Organisatorische Flankierung | Lieferung im DATEV-Format und Rechnungsweiterleitung als E-Rechnung im Verwaltervertrag vereinbaren (Vorschlag) |

### 15.7.3 ERP- und PM-Stammdatensync (S-17, Folgeprojekt)

d.velop bietet offene REST-APIs für DMS, smart invoice, Aufgaben, Prozesse und Eingang (d.velop API-Übersicht). Eine bidirektionale Stammdatensynchronisation mit einzelnen PM-Systemen oder einem künftigen ERP ist technisch möglich, wird aber erst in einem Folgeprojekt konkretisiert (Katalog 5.4 = S/A). Als Muster dient die Partner-Integration zwischen Haufe X360 und d.velop: Stammdatenabgleich, Belegübergabe, Statusspiegelung und Belegansicht im ERP. Sie zeigt, welche Objekte eine ERP-Kopplung abdecken sollte. Für Livos ist nur das Muster übertragbar, weil DATEV führend bleibt.

## 15.8 Querschnittsthemen

### 15.8.1 Fehlerbehandlung

| Fehlerklasse | Beispiel | Verhalten | Anwendersicht |
|---|---|---|---|
| Technisch vorübergehend | Timeout, HTTP 429, 503, Gateway nicht erreichbar | automatische Wiederholung mit exponentiellem Backoff (Vorschlag: 1, 5, 15, 60 Minuten, danach stündlich bis 24 h) | keine; bei Dauerstörung Hinweis im Betriebsbericht |
| Technisch dauerhaft | ungültiger API-Key, geänderte Schnittstelle | Nachricht in die Fehlerablage; Alarm MDIS | Beleg wartet oder steht im Fehlerschritt |
| Fachlich | Kreditor fehlt, Mandant unbekannt, BIM4You lehnt ab, Zahlstatus nicht zuordenbar | keine Wiederholung; Rückmeldung mit Klartext an den Workflow (Fehlerschritt/Klärfall) oder Klärliste | Aufgabe an R-02 bzw. Trios |
| Zeitüberschreitung Prozess | BIM4You-Transfer nahe 28 Tagen | Vorwarnung, dann Fehlerschritt „Klärung Bau" | Aufgabe an R-02 |

Fehlermeldungen an den Workflow sind in Deutsch formuliert und nennen die nächste Aktion (z. B. „Kreditor 70123 im Mandanten 29098-55003 fehlt – Anlage bei Trios angefordert").

### 15.8.2 Wiederanlauf

| Situation | Vorgehen |
|---|---|
| BeSync-Ausfall | Die smart-invoice-Abhol-API hält Transfers bis zum Ende des Zeitfensters vor; nach Wiederanlauf holt BeSync offene Transfers ab. Webhook-Exporte, die in der Ausfallzeit nicht quittiert wurden, stehen im Fehlerschritt und werden nach Wiederanlauf erneut angestoßen. |
| DATEV/Gateway-Ausfall | S-01: Wiederholung durch LDconnect bzw. erneute Übergabe; S-06: nächster Lauf holt alle Änderungen seit dem letzten erfolgreichen Lauf (Zeitstempel je Mandant). |
| Ausfall des Ereignisprotokolls (S-12) | Nachlauf über nächtliche Abfrage von Task-, Process- und DMS-API, solange die Aufgabenhistorie noch vorhanden ist (30–365 Tage). |
| Stammdatenlauf fehlgeschlagen | Delta-Lauf ab dem letzten erfolgreichen Zeitstempel. |

### 15.8.3 Idempotenz

Jede Verarbeitung ist wiederholbar, ohne doppelte Wirkung. Schlüssel sind die Beleg-ID (d.velop), die Transfer-ID (smart invoice), bei DATEV Mandant + Kreditor + Belegfeld 1, bei BIM4You die Beleg-ID als Barcode. Mails (S-11) tragen eine eindeutige Nachrichten-ID je Beleg und Anlass; ein zweiter Versand wird unterdrückt. Eigenschaften werden nur geschrieben, wenn sich der Wert ändert (auch zur Schonung der Rate-Limits). Stornos werden in beide Richtungen gespiegelt (Workflow-Ende „abgebrochen" in smart invoice bzw. Storno in BIM4You).

### 15.8.4 Sicherheit

| Thema | Festlegung |
|---|---|
| Secrets | API-Keys, Client-Secrets und DATEV-Zugangsdaten im Secret-Store von BeSync; Zugriff nur für den Betriebsprozess; Rotation mindestens jährlich und bei Personalwechsel (Vorschlag) |
| Prinzip minimaler Rechte | ein technischer Benutzer je Schnittstellengruppe (15.5.3) |
| Webhook-Signatur | Prüfung der Signatur `X-Smart-Invoice-Signature` (HMAC-SHA256) mit Zeitstempelprüfung (±5 Minuten) (smart invoice API-Handbuch) |
| Transport | TLS ab Version 1.2; DATEV-Zugriff über das VPN-gesicherte Gateway |
| Datenminimierung | BeSync speichert Belegbilder nur transient (Übergabe BIM4You, Export); im Staging nur Metadaten |
| Protokollierung | Zugriffe technischer Benutzer im d.velop-Plattformprotokoll (180 Tage) und im BeSync-Protokoll |
| Partnerzugang MDIS | nur über den kundenseitig vergebenen, zeitlich begrenzten Supportzugang (Kapitel 17, 18) |

### 15.8.5 Tests

| Teststufe | Inhalt | Umgebung | Verantwortlich |
|---|---|---|---|
| Komponententest | je BeSync-Schnittstelle: Mapping, Fehlerfälle, Idempotenz, Rate-Limit-Verhalten | MDIS-Entwicklung | MDIS |
| Integrationstest | Ende-zu-Ende je Schnittstelle mit Testmandanten: S-01/S-02 gegen DATEV-Testbestand und LDconnect-Testsystem, S-06 mit Testzahlung, S-08/S-09 mit BIM4You-Testprojekt | Test-/Abnahme-Tenant (AE-01), DATEV-Testbestand beim Hoster | MDIS, Trios, Hoster, BIB GmbH |
| Last- und Massentest | Erstbefüllung Stammdaten, 110 Mandanten, Nachlauf Zahlstatus | Test-Tenant | MDIS |
| Störfalltest | Ausfall BeSync, Gateway, BIM4You; Wiederanlauf | Test-Tenant | MDIS |
| Fachliche Abnahme | Testfälle aus den Prozesskapiteln inkl. Abstimmliste d.velop ↔ DATEV | Test-Tenant | Livos, Trios |
| Regressionstest | nach d.velop-Releases und DATEV-Updates (Kapitel 18) | Test-Tenant | MDIS |

### 15.8.6 Verantwortlichkeiten (RACI)

R = durchführend, A = verantwortlich, C = konsultiert, I = informiert.

| Aufgabe | MDIS | Livos | Trios | d.velop | LIONDEER | BIB GmbH | Hoster |
|---|---|---|---|---|---|---|---|
| Bestellung Option DATEV Rechnungswesen, Konfiguration S-01/S-02 | R | A | C | C | C | – | I |
| DATEV-Komponenten (DATEVconnect, Beleganzeige), DATEV-Benutzer, Gateway-Freigabe | C | A | R | – | C | – | R |
| Betrieb LDconnect | I | I | I | C | A/R | – | C |
| Betrieb DATEV-Server und Gateway-Endpunkt | I | I | C | – | C | – | A/R |
| Übernahme Buchungsvorschläge, Buchung, Zahlungsvorschlag, SEPA-Export | I | A | R | – | – | – | – |
| Unterschrift und Ausführung in multicash (S-07) | – | A/R | C | – | – | – | – |
| Entwicklung und Betrieb BeSync-Schnittstellen (S-04–S-06, S-08–S-12, S-15, S-16) | A/R | C | C | I | – | C | C |
| Fachliche Stammdatenpflege Lieferanten-App | C | A/R | C | – | – | – | – |
| Kreditorenanlage in DATEV | I | C | A/R | – | – | – | – |
| BIM4You-Import/-Export freischalten, Lizenzen | C | A | – | – | – | R | – |
| d.velop-Plattform, APIs, Export-Freischaltung | C | A | – | R | – | – | – |
| Entra ID, M365-Postfächer, App-Registrierungen (S-13, S-14) | C | A/R | – | C | – | – | – |
| Monitoring aller Schnittstellen, Betriebsbericht | A/R | I | I | – | C | – | – |
| Fachliche Klärfälle aus Schnittstellen | C | A/R | R | – | – | – | – |
| Integrations- und Regressionstests | A/R | C | R | C | C | C | C |

# 16 Reporting und Controlling

Livos braucht zwei Arten von Transparenz: den **aktuellen Stand** (Wo liegt welche Rechnung, bei wem, seit wann?) und die **historische Auswertung** (Wie lange brauchen Schritte und Personen, wie viel Skonto geht verloren?). Den aktuellen Stand liefert das Rechnungseingangsbuch (REB) von d.velop invoices im Standard [S]. Die historische Auswertung entsteht über das BeSync-Ereignisprotokoll in evidanza [A] (AE-16, Katalog 3.2 = S/A).

## 16.1 Rechnungseingangsbuch: Sichten je Rolle

### 16.1.1 Funktionen des REB (belegt)

| Funktion | Beschreibung | Beleg |
|---|---|---|
| Spalten | u. a. Aktueller Schritt, **Aktueller Schritt seit**, **Zugewiesen** (Benutzer/Gruppen), **Status** (u. a. Clearing-Modus, Eskalationsstufe 1/2), Mandant, Kreditor, Skontobetrag, Skonto- und Nettofälligkeit, Rechnungsdatum, **Rechnungsformat** (E-Rechnung/sonstige) | REB-Handbuch; Helpcenter 08/2025 |
| Standard-Schnellzugriffe | Meine offenen Rechnungen, Rechnungen in Vertretung, Alle offenen Rechnungen (global oder mandantenbezogen berechtigt), Archiv, **An mich eskalierte Rechnungen** | REB-Handbuch; Helpcenter 09/2026 |
| Eigene Schnellzugriffe | Filter mit Operatoren und Verknüpfungen plus Spaltenlayout, als Schnellzugriff gespeichert; Zähler und Kennzeichnung „ungelesen" | Helpcenter 03/2026, 12/2025 |
| Gruppierung | nach Schritt, Mandant und Datumsspalten | REB-Handbuch; Helpcenter 12/2025 |
| CSV-Export | „Sichtbare Spalten" oder „Alle Spalten", filtergetreu; Download 30 Tage verfügbar | Helpcenter 09/2026 |
| Historie | Weg durch den Workflow, Kommentare, Notizen, auch für abgeschlossene Vorgänge | Helpcenter 03/2026 |
| Archivsicht | 6 Monate ab Rechnungsdatum, erweiterbar auf 12 Monate | REB-Handbuch |

Das REB zeigt **keine** historischen Durchlaufzeiten je Benutzer und Schritt und hat keinen BI-Konnektor. Das deckt 16.3 ab.

### 16.1.2 Schnellzugriffe je Rolle (Vorschlag)

Die Schnellzugriffe werden im Prozess-Workshop mit Livos bestätigt (OP-17). Gesellschaftsgruppen und Namen sind Beispiele.

| Rolle | Schnellzugriff (Vorschlag) | Filter | Spalten | Gruppierung |
|---|---|---|---|---|
| R-02 Rechnungseingang/Verteilung | „Verteilung offen" | Schritt = Verteilung | Eingang, Mandant, Kreditor, Brutto, Eingangskanal, Aktueller Schritt seit | Mandant |
| R-02 | „Klärfälle" | Status = Clearing oder Schritt = Klärfall | Mandant, Kreditor, Klärgrund, Aktueller Schritt seit | Klärgrund |
| R-02 | „E-Rechnungen mit Befund" | Rechnungsformat = E-Rechnung, Status Prüfbericht mit Fehler | Kreditor, Rechnungsnummer, Aktueller Schritt | – |
| R-03 Sachliche Prüfer | Meine offenen Rechnungen (Standard) | – | Mandant, Objekt, Kreditor, Brutto, Skontofälligkeit | Mandant |
| R-04 Freigeber | Meine offenen Rechnungen; „Skonto in 5 Tagen" | Skontofälligkeit ≤ heute + 5 | Kreditor, Brutto, Skontobetrag, Skontofälligkeit | – |
| R-05 Zahlungsfreigeber | „Zahlungsfreigabe offen" | Schritt = Zahlungsfreigabe | Mandant, Kreditor, Zahlbetrag, Skonto-/Nettofälligkeit | Mandant |
| R-06 Buchhaltung (Trios) | „Buchhaltung offen"; „Übergabefehler" | Schritt = Buchhaltung; Exportstatus Fehler | Mandant, Kreditor, Brutto, Aktueller Schritt seit | Mandant |
| R-07 Controlling/Management | „Alle offenen – Gruppe Bestand/Privatisierung/Bau" | Mandant ∈ Gesellschaftsgruppe | siehe 16.2 | Mandant, Schritt |
| R-07 | „An mich eskalierte Rechnungen" (Standard) | – | Eskalationsstufe, Zugewiesen | – |
| R-12 Fachadministration | „Liegezeit > 10 Tage" (Beispielwert) | Aktueller Schritt seit < heute − 10 | Zugewiesen, Schritt, Mandant | Zugewiesen |

**Rechte:** Die Sicht „Alle offenen Rechnungen" wird **mandantenbezogen** berechtigt. Ein Controller der Gruppe Bau sieht nur die Mandanten dieser Gruppe (AE-18). Die REB-Berechtigung je Mandant setzt ggf. R-12 bei Anlage einer Gesellschaft manuell.

### 16.1.3 Segment und Gesellschaftsgruppen

Das REB gruppiert nach Mandant, nicht nach Segment. Die Zuordnung Mandant → Segment (E-31) steht im Gesellschaftsstamm. Für Segmentsichten gibt es zwei Wege: (1) je Segment ein eigener Schnellzugriff mit der Liste der Mandanten im Filter [K]; (2) die Segmentauswertung in evidanza über den Gesellschaftsstamm [A]. Weg 1 genügt für die operative Arbeit. Kommt eine Gesellschaft hinzu, passt R-12 den Filter an. Weg 2 ist die Managementsicht.

### 16.1.4 CSV-Export

Der CSV-Export ersetzt das bisherige „ER-Vorerfassungsjournal" als Stichtagsliste (AE-08). Beispiel: Zum Monatsende exportiert R-07 „Alle offenen Rechnungen – alle Spalten" je Gesellschaftsgruppe. Trios nutzt die Liste zur Abgrenzung von Rückstellungen für unverbuchte Rechnungen. Ein API-Aufruf für den CSV-Export ist nicht dokumentiert; der Export wird manuell gestartet [O].

## 16.2 Managementsicht

Die Managementsicht (Maske M-09) ist ein REB-Schnellzugriff für R-07 und die Geschäftsführung.

| Element | Inhalt |
|---|---|
| Filter | alle offenen Rechnungen der berechtigten Mandanten |
| Spalten | Mandant, Kreditor, Brutto, Status, Aktueller Schritt, Aktueller Schritt seit, Zugewiesen, Skontofälligkeit, Nettofälligkeit, Eskalationsstufe, Rechnungsformat |
| Gruppierung | Mandant, darunter Schritt |
| Sortierung | Aktueller Schritt seit (älteste zuerst) |
| Nutzung | wöchentliche Durchsicht; Eskalationen ansprechen; CSV-Export für Monatsbericht |
| Ergänzung | Monatsbericht aus evidanza (16.3) mit Trends, Durchlaufzeiten und Skontoverlust |

**Dashboard-Grenzen.** Die Startseite von d.velop documents bietet vier Standard-Widgets (Suche, Zuletzt bearbeitet, Beobachtet, Favorisiert). Eigene Widgets sind als Verknüpfung, Liste (JSON-Dienst hinter einer URL) oder eingebettete Webseite möglich. Einen Diagramm-Typ oder ein Filterfeld gibt es nicht; die Sichtbarkeit je Gruppe ist keine Sicherheitsfunktion (d.velop documents Anwenderhandbuch Cloud). Kennzahlen-Kacheln auf der Startseite wären deshalb eine Entwicklung. Das Konzept verzichtet darauf: Die Startseite je Rolle (M-10) enthält Verknüpfungen auf die REB-Schnellzugriffe und auf den evidanza-Bericht. **Das Rechnungseingangsbuch ist die Managementsicht** für den aktuellen Stand, evidanza für die Historie.

## 16.3 KPI-Katalog

Quellen: **REB** = Rechnungseingangsbuch (Stichtag, Standard) · **BeSync** = Ereignisprotokoll S-12 (Historie) · **DATEV** = Zahlstatus über S-06. Zielwerte legt Livos nach drei Monaten Echtbetrieb fest (Vorschlag). Frequenz und Empfänger sind Vorschläge.

| Nr. | KPI | Definition | Quelle | Frequenz | Empfänger |
|---|---|---|---|---|---|
| KPI-01 | Belege im Umlauf je Status | Anzahl und Bruttosumme offener Belege je Schritt/Status, je Mandant und Segment | REB (Stichtag), BeSync (Verlauf) | täglich (REB), monatlich (Trend) | R-02, R-07 |
| KPI-02 | Liegezeit aktueller Schritt | Heute minus „Aktueller Schritt seit"; Anteil Belege über Schwelle (Beispiel: > 5 Arbeitstage) | REB | täglich | R-02, R-07, Vorgesetzte |
| KPI-03 | Durchlaufzeit Eingang → Freigabe | Median und 90-%-Wert der Tage vom Eingang bis zum Abschluss der letzten fachlichen Freigabe | BeSync | monatlich | R-07, GF |
| KPI-04 | Durchlaufzeit Eingang → Übergabe DATEV | Tage vom Eingang bis zur Übergabe (S-01) | BeSync | monatlich | R-07, Trios |
| KPI-05 | Durchlaufzeit Eingang → Zahlung | Tage vom Eingang bis zum Zahldatum (E-23) | BeSync + DATEV (S-06) | monatlich | R-07, Treasury |
| KPI-06 | Liegezeit je Bearbeiter und Schritt | Median der Bearbeitungsdauer je Person und Schritt (Aufgabeneingang bis Aktion) | BeSync | monatlich | R-07, Vorgesetzte (Betriebsrat beachten, 16.5) |
| KPI-07 | Skontoquote | Anteil der fristgerecht mit Skonto gezahlten Belege an allen skontofähigen Belegen (Zahldatum ≤ Skontofrist) | BeSync + DATEV | monatlich | R-07, GF |
| KPI-08 | Verlorenes Skonto | Summe der Skontobeträge skontofähiger Belege, die nach Ablauf der Skontofrist gezahlt wurden | BeSync + DATEV | monatlich | R-07, GF |
| KPI-09 | Klärfallquote | Anteil der Belege mit mindestens einem Klärfall (Mandant unbekannt, Kreditor fehlt, IBAN-Abweichung) an allen Eingängen; je Klärgrund | BeSync | monatlich | R-02, R-12 |
| KPI-10 | Dublettenquote | Anteil der als Dublette erkannten Belege; davon mit Begründung angenommen | BeSync (Endpfad, Begründung) | monatlich | R-02 |
| KPI-11 | Automatisierungsquote Erkennung | Anteil der Belege ohne manuelle Korrektur von Mandant und Kreditor in der Verteilung; ergänzend die Statistik „Analyse der Erkennungsqualität" von d.velop invoices | BeSync + d.velop invoices Statistik | monatlich | R-12, MDIS |
| KPI-12 | E-Rechnungsquote | Anteil der Eingänge im Format E-Rechnung (Spalte Rechnungsformat bzw. E-25) | REB, BeSync | monatlich | R-07, R-12 (Lieferantenkommunikation) |
| KPI-13 | Rückweisungsquote nach Grund | Anteil abgelehnter Belege an allen Eingängen, je Rückweisungsgrund (E-26) | BeSync | monatlich | R-02, R-07 |
| KPI-14 | Kürzungsvolumen | Summe (Brutto − Zahlbetrag) und Anzahl gekürzter Belege je Kürzungsgrund (E-13), Mandant, Kreditor | BeSync | monatlich | R-07, Asset Management |
| KPI-15 | PM-Freigaben offen | Anzahl und Alter offener Belege in WF-03, je Property Manager und Objekt | REB | wöchentlich | Asset Management |
| KPI-16 | Eskalationen | Anzahl Belege mit Eskalationsstufe 1/2, je Mandant und Schritt | REB, BeSync | wöchentlich | R-07 |
| KPI-17 | Offene Bau-Prüfungen | Anzahl und Alter offener BIM4You-Transfers (ab Phase 3) | BeSync | wöchentlich | Projektleitung Bau |

**Hinweis zur Datenlage:** KPI-05, KPI-07 und KPI-08 setzen S-06 voraus und sind daher erst ab Phase 3 verfügbar. KPI-06 setzt voraus, dass der handelnde Benutzer je Schrittwechsel ermittelbar ist. Im Export-Ereignis steht er nicht auf Kopfebene; Ersatz sind Aufgabenhistorie (Task-API) und die Eigenschaft Workflowbeteiligte (E-32) [O, OP-26, Test T31]. KPI-09 und KPI-11 setzen voraus, dass Klärgründe und Korrekturen als Schritt oder Eigenschaft erfasst werden (Kapitel 9).

## 16.4 evidanza-Anbindung (S-12)

### 16.4.1 Architektur

evidanza ist bei Livos als BI-Werkzeug im Einsatz und arbeitet auf Microsoft SQL Server; über data.SYNAPSE bindet es SQL- und REST-Quellen an (evidanza Produktseiten). Einen fertigen d.velop-Konnektor gibt es nicht. Die Anbindung läuft deshalb über eine Staging-Schicht in BeSync.

| Stufe | Inhalt | Technik |
|---|---|---|
| 1 Ereignisprotokoll in Echtzeit | An allen relevanten Schrittverbindungen in smart invoice ist ein Export an BeSync konfiguriert. Jeder Export enthält Beleg-ID, Mandant, Schritt von/nach, Zeitpunkt, Belegdaten und Positionen. BeSync quittiert sofort (≤ 30 s) und schreibt einen Datensatz. | smart-invoice-Export (Webhook), BeSync-Warteschlange |
| 2 Nächtliche Ergänzung | Abfrage der Aufgabenhistorie (Eingang, Abschluss, Bearbeiter), Prozessinstanzen (Start, Ende, Status) und DMS-Eigenschaften (Zahlstatus, Rückweisungs- und Kürzungsgrund, Eingangskanal) | Task-API, Process-API, DMS-API mit technischem Benutzer |
| 3 Staging | Tabellen: Fakten „Beleg × Schritt × Zeitpunkt × Bearbeiter"; Dimensionen Mandant/Segment, Kreditor/Konsolidierungsnummer, Objekt, Schritt, Rückweisungs- und Kürzungsgrund; Zahlstatus aus S-06 | MS SQL (BeSync) |
| 4 Berechnung | KPIs aus 16.3 als Sichten in der Staging-Datenbank oder im evidanza-Modell | SQL, evidanza |
| 5 Bericht | Monatsbericht, Drilldown Segment → Gesellschaft → Kreditor/Beleg | evidanza |

### 16.4.2 Aufbewahrung der Aufgabenhistorie

Die d.velop-Plattform hält Aufgabendetails standardmäßig **30 Tage**, konfigurierbar bis **365 Tage** (d.velop Task-API). Das process-studio-Prozessprotokoll ist ebenfalls auf 30 Tage bis 1 Jahr begrenzt. Deshalb gilt:

- Das Ereignisprotokoll startet **mit dem Go-live von Phase 1**, auch wenn evidanza-Berichte erst in Phase 2 folgen. Sonst gehen die Daten der ersten Monate verloren.
- Die Aufbewahrung der Aufgabendetails wird auf 365 Tage gesetzt (Vorschlag), um Nachläufe nach Störungen zu ermöglichen.
- Die Staging-Datenbank ist die Langzeitquelle für Durchlaufzeiten. Der GoBD-Nachweis der Freigaben bleibt davon unberührt; er liegt im Workflowprotokoll im DMS (Kapitel 17).

### 16.4.3 Risiken und Gegenmaßnahmen

| Risiko | Gegenmaßnahme |
|---|---|
| Ein nicht quittierter Webhook-Export schickt den Beleg in den Fehlerschritt | BeSync-Endpunkt hochverfügbar, sofortige Quittung; Export nur an Verbindungen, an denen ein Fehlerschritt tragbar ist; sonst nur nächtliche Abfrage |
| Viele Exporte je Workflow – Zulässigkeit und Performance nicht dokumentiert | mit d.velop klären; im Test-Tenant messen [O, OP-26] |
| Handelnder Benutzer nicht im Export | Ergänzung aus Aufgabenhistorie (Stufe 2) [O, OP-26] |
| Lizenzierte evidanza-Konnektoren bei Livos unbekannt | im Projektstart mit Livos und evidanza klären [O, OP-27] |

## 16.5 Datenschutz bei personenbezogenen Kennzahlen

KPI-06 (Liegezeit je Bearbeiter) ist eine Leistungs- und Verhaltensauswertung. Sie wurde im Workshop ausdrücklich gewünscht (Workshop 22.09.2026, 00:35:18). Vor der Einführung klärt Livos die Zulässigkeit mit dem Datenschutzbeauftragten und, falls vorhanden, mit dem Betriebsrat. Vorschlag: Auswertung je Person nur für die direkte Führungskraft, im Monatsbericht nur je Schritt und Team.

# 17 Compliance, Sicherheit und Datenschutz

Dieses Kapitel beschreibt, wie das Livos-DMS die steuer- und handelsrechtlichen Ordnungsvorschriften (GoBD), die Aufbewahrungspflichten, die E-Rechnungspflichten, den Datenzugriff der Finanzverwaltung, den Export je Gesellschaft sowie Datenschutz und Informationssicherheit umsetzt. Rechtliche Aussagen geben den Stand 09/2026 wieder. Fristen und steuerliche Einordnungen bestätigt die Steuerberatung von Livos.

Legende Belegstatus: **[S]** Standard belegt · **[K]** Konfiguration · **[A]** Anpassung/Entwicklung · **[O]** offen.

## 17.1 GoBD-Anforderungen und Umsetzung

### 17.1.1 Anforderungen

Die GoBD verlangen unter anderem: Eine Aufzeichnung darf nicht so verändert werden, dass der ursprüngliche Inhalt nicht mehr feststellbar ist; Änderungen und Löschungen sind zu protokollieren; auch die Änderungshistorie darf nicht nachträglich veränderbar sein (§ 146 Abs. 4 AO; GoBD Rz. 58–59, 110–111). Eingehende elektronische Belege sind in dem Format aufzubewahren, in dem sie empfangen wurden. Bei E-Rechnungen genügt der strukturierte Teil; der Bildteil nur, wenn er zusätzliche steuerrelevante Informationen enthält. Durch OCR gewonnene Informationen sind nach Verifikation und Korrektur ebenfalls aufzubewahren (GoBD, 2. Änderung, BMF-Schreiben vom 14.07.2025).

### 17.1.2 Umsetzung im Livos-DMS

| Anforderung | Umsetzung | Status |
|---|---|---|
| Unveränderbarkeit des Originals | Das Original bleibt unverändert (P5). Kürzungen, Korrekturen und Anmerkungen nur als Workflow-Daten (Zahlbetrag, Kürzungsgrund) oder Annotation; Annotationen werden getrennt vom Original gespeichert. Keine „lokale Bearbeitung" von Rechnungen (AE-14). | [S] + Organisation |
| Versionierung | Jede Freigabe mit Änderung erzeugt eine neue Version; Versionsübersicht; Status Bearbeitung → Freigabe → Archiv, Vorversion wird automatisch „Archiv" (d.velop documents Funktionsbeschreibung 10/2025) | [S] |
| Schutz vor Versionslöschung | Das Löschen der aktuellen Version macht die Vorversion wieder aktuell. Deshalb Löschrecht auf Versionen nur für Administration; Löschsperre für Kategorien im Status Freigabe/Archiv; die Löschsperre überstimmt alle Löschrechte, ihre Rücknahme erfordert eine Begründung (DmsConfig API) | [K] |
| Aktivitätenprotokoll | Protokoll aller Änderungen an Datei und Eigenschaften je Dokument und Akte, filterbar; protokolliert werden u. a. Import, Bearbeitung, Notizen, Eigenschafts- und Statusänderungen, Aufbewahrungsdauer, Verknüpfen und Lösen | [S]; Aufbewahrungsdauer des Protokolls über die volle Belegfrist bestätigt d.velop [O, OP-32] |
| Belegprotokoll smart invoice | Workflowprotokoll als DMS-Dokument (Kategorie „Workflowprotokoll ERV") mit Eigenschaften der Rechnung und Bearbeitungsschritten; Historie je Vorgang im REB (d.velop invoices Leistungsbeschreibung 12/2025) | [S] |
| Protokolle anderer Workflows | process-studio-Prozessprotokolle sind nur 30 Tage bis 1 Jahr verfügbar → Option „Export in Repository" für alle Workflows (WF-06, WF-09, WF-10) aktivieren | [K] |
| Lesbarkeit | Original + automatisch erzeugte **PDF/A-Rendition** als abhängiges Dokument | [S] |
| E-Rechnung | **XML ist das Original** und wird im Empfangsformat abgelegt; die PDF-Visualisierung ist Lesehilfe. Bei XRechnung liegt der Validierungsbericht als Anhang im DMS | [S] |
| OCR-/Erkennungsdaten | Nach Verifikation im Workflow als Eigenschaften und Workflowdaten am Beleg gespeichert | [S] |
| Zugriffsschutz | Berechtigungen je Kategorie und Gesellschaft (Kapitel 13); „DENIED" gewinnt | [K] |
| Festschreibung Buchung | erfolgt in DATEV (führendes FiBu-System); das DMS hält den Beleglink (Dokumentenlink im Buchungssatz, S-01) | [S] (DATEV) |

## 17.2 Aufbewahrungsfristen

### 17.2.1 Rechtsrahmen

| Unterlagenart | Kategorien (Kapitel 7) | Frist | Rechtsgrundlage | Fristbeginn |
|---|---|---|---|---|
| Buchungsbelege: Eingangsrechnungen, Gutschriften, E-Rechnungs-XML, Zahlungsbelege, Belege zur Buchung | K-01, K-02 (soweit Buchungsbeleg), K-08 | **8 Jahre** (seit 01.01.2025, Viertes Bürokratieentlastungsgesetz – BEG IV) | § 147 Abs. 1 Nr. 4, Abs. 3 AO; § 257 Abs. 1 Nr. 4, Abs. 4 HGB; § 14b Abs. 1 UStG | Schluss des Kalenderjahres der Entstehung |
| Bücher, Jahresabschlüsse, Arbeitsanweisungen und Organisationsunterlagen (Verfahrensdokumentation, Workflowdefinitionen, Freigabematrix-Stände) | K-15 Organisationsunterlage | **10 Jahre** | § 147 Abs. 1 Nr. 1, Abs. 3 AO; § 257 Abs. 1 Nr. 1 HGB | Schluss des Kalenderjahres |
| Empfangene Handels- und Geschäftsbriefe, Kopien abgesandter Briefe | K-07, K-09 | **6 Jahre** | § 147 Abs. 1 Nr. 2, 3 AO; § 257 Abs. 1 Nr. 2, 3 HGB | Schluss des Kalenderjahres des Empfangs/Versands |
| Verträge | K-05, K-14 | Vertragsende + Frist (steuerlich 6 bzw. 8 Jahre, zivilrechtlich ggf. länger) | § 147 AO; zivilrechtliche Fristen je Vertragsart | Vertragsende |
| Workflowprotokolle zu Belegen | „Workflowprotokoll ERV" | wie der zugehörige Beleg (8 Jahre, Vorschlag) | GoBD | wie Beleg |
| PM-Freigaberechnungen (WF-03) | K-01 mit Eingangskanal „PM-Freigabe" | offen; bei Livos kein Buchungsbeleg, vorsorglich wie K-01 (8 Jahre) bis zur Festlegung | Festlegung mit der Steuerberatung (OP-46) | Schluss des Kalenderjahres |

**Ablaufhemmung.** Die Aufbewahrungsfrist läuft nicht ab, soweit und solange die Unterlagen für Steuern von Bedeutung sind, deren Festsetzungsfrist noch nicht abgelaufen ist (§ 147 Abs. 3 S. 5 AO). Außersteuerliche kürzere Fristen verkürzen die steuerliche Frist nicht. Längere zivilrechtliche Interessen (Bauverträge mit Gewährleistung, Grundstücksverträge, Darlehen) legt die Livos-Rechtsabteilung je Vertragsart fest [O].

### 17.2.2 Umsetzung in d.velop (Cloud)

| Element | Festlegung | Status |
|---|---|---|
| Frist je Kategorie | Frist in Jahren oder Monaten, bezogen auf eine Datumseigenschaft der Kategorie (DmsConfig API) | [S] |
| Bezugsdatum | Eigenschaft E-29 „Aufbewahrungsbeginn" = 31.12. des Belegjahres (bzw. Vertragsende), automatisch berechnet | [K] |
| Löschsperre | aktiv für alle aufbewahrungspflichtigen Kategorien | [K] |
| Automatisches Löschen | **zunächst aus.** Die aktuelle Funktionsbeschreibung beschreibt das automatische Löschen als konfigurierbar; eine ältere Leistungsbeschreibung formuliert es als Automatik. Die Abschaltbarkeit bestätigt d.velop [O, OP-15]. | [K]/[O] |
| Löschlauf | jährlich (Vorschlag: im zweiten Quartal): Kandidatenliste je Kategorie und Gesellschaft → Prüfung Ablaufhemmung durch Steuer/Recht → Freigabe → Löschung → Löschprotokoll als Organisationsunterlage (K-15) ablegen (process studio, WF-09-Muster) | [K]/[A] |
| Legal Hold | Eine Legal-Hold-Funktion ist nicht dokumentiert. Workaround: Bezugsdatum E-29 für betroffene Dokumente nach vorn schieben (Änderung wird im Aktivitätenprotokoll protokolliert). Ob die Frist dann neu berechnet wird, bestätigt d.velop [O, OP-15]. | [O] |
| Papierkorb/Backup | Gelöschte Daten werden noch 90 Tage vorgehalten, Backups 30 Tage (d.velop Sicherheitsbeschreibung) | [S] |

Die finalen Fristen je Kategorie bestätigt die Steuerberatung (Trios) vor Go-live.

## 17.3 Verfahrensdokumentation

| Element | Inhalt |
|---|---|
| Pflicht | Für jedes DV-System ist eine Verfahrensdokumentation zu führen. Sie beschreibt den Weg von der Entstehung der Information über Indizierung, Verarbeitung, Speicherung, Wiederfinden, maschinelle Auswertbarkeit, Schutz gegen Verlust und Verfälschung bis zur Reproduktion (GoBD Rz. 151–154). |
| Bestandteile | allgemeine Beschreibung, Anwenderdokumentation, technische Systemdokumentation, Betriebsdokumentation |
| Livos-Gliederung (Vorschlag) | (1) Gesamtsystem und Verantwortlichkeiten, (2) Eingangskanäle und Scan (inkl. ersetzendes Scannen, falls Papier vernichtet wird), (3) Rechnungsprozess WF-01 bis WF-05 mit Freigabematrix, (4) Schnittstellen S-01 bis S-17, (5) Verträge und Post, (6) Berechtigungen und Rezertifizierung, (7) Aufbewahrung, Löschung, Legal Hold, (8) Datenzugriff Finanzverwaltung und Export, (9) Betrieb, Datensicherung, Notfall, (10) internes Kontrollsystem |
| Verantwortung | Livos als Steuerpflichtiger ist verantwortlich. MDIS erstellt den Entwurf für die DMS- und BeSync-Teile, Trios ergänzt die DATEV-Teile, d.velop liefert Plattformbeschreibung und Testate. |
| Vorlage | Im d.velop Store gibt es eine Cloud-App „GoBD-Verfahrensdokumentation" (comdatis digital consulting) mit einer Vorlage für ausgewählte Funktionen der d.velop cloud; kostenpflichtige Option. Alternativ MDIS-Vorlage. |
| Pflege | versioniert im DMS (Kategorie K-15 „Organisationsunterlage", 10 Jahre, läuft nicht ab, solange die erklärten Unterlagen aufzubewahren sind); Aktualisierung bei jeder Prozess- oder Schnittstellenänderung (Kapitel 18) |
| Zeitpunkt | Entwurf bis Go-live Phase 1; Fortschreibung je Phase |

## 17.4 Testate und Zertifikate

Ein Softwaretestat bescheinigt, dass eine Software GoBD-konform eingesetzt werden **kann**. Es ersetzt weder die Verfahrensdokumentation noch die ordnungsmäßige Anwendung bei Livos.

| Nachweis | Gegenstand | Befund | Maßnahme |
|---|---|---|---|
| ISO/IEC 27001:2022 | Informationssicherheits-Managementsystem der d.velop AG | belegt (d.velop Zertifikatsseite) | Zertifikat zur Projektakte |
| TISAX AL2 | Informationssicherheit bei hohem Schutzbedarf der d.velop AG | belegt | Zertifikat zur Projektakte |
| ISO 9001 | Qualitätsmanagement d.velop AG | belegt | – |
| IDW PS 880 | Softwareprüfung „d.velop documents" und „d.velop postbox" | belegt; ausgewiesen für d.velop documents (on-premises) und d.velop postbox (cloud). **Ob der Prüfbericht die Cloud-Betriebsform von d.velop documents und d.velop invoices abdeckt, ist nicht belegt.** | Prüfbericht mit Umfang für die Cloud anfordern [O, OP-14] |
| BSI C5, ISO 27017/27018 | Rechenzentrumsbetreiber (AWS bzw. T Cloud) | für die Infrastrukturanbieter belegt | – |
| BSI C5 / IDW PS 951 für d.velop selbst | Cloud-Dienst bzw. dienstleistungsbezogenes IKS der d.velop | **nicht gefunden** | bei d.velop anfragen [O, OP-14] |

## 17.5 Datenschutz

| Thema | Festlegung | Status |
|---|---|---|
| Auftragsverarbeitung | Auftragsverarbeitungsvertrag (AVV) mit d.velop einschließlich der Festlegungen zu Unterauftragsverarbeitern; AVV mit MDIS für Betrieb von BeSync und Support; mit LIONDEER und Riecken für die DATEV-Anbindung (Rollen im Projekt klären) | [O] |
| Hosting | Betriebsform C1: Multi-Tenant-Cloud bei AWS mit Standort Frankfurt (AE-01). Die aktuelle Leistungsbeschreibung enthält keinen Abschnitt „Datenstandort" mehr; die Standortzusage wird im AVV geprüft | [S]/[O] |
| Sicherheit Plattform | Verschlüsselung at rest (AES-256-GCM), Transport TLS ≥ 1.2, Mandantenisolation, tägliche Backups (RPO 24 h, Vorhaltung 30 Tage), Wiederanlaufziel 48 h (d.velop Sicherheitsbeschreibung) | [S] |
| KI-Funktionen | Erkennung, KI-Kontierung und KI-Klassifizierung laufen in der d.velop-Plattform. Für **d.velop pilot** übermittelt d.velop Dokumente und Eingaben verschlüsselt an den jeweiligen KI-Anbieter; Anbieter und Region nennt die aktuelle Funktionsbeschreibung nicht, sondern verweist auf den AVV. Laut d.velop werden Eingaben nicht zum Training genutzt. **LLM-Anbieter und -Region für pilot und die KI-Funktionen klärt Livos vor der Freischaltung mit d.velop** [O, OP-19]. | [O] |
| Löschkonzept | Die Aufbewahrungspflicht geht der DSGVO-Löschung vor: Art. 17 Abs. 3 lit. b DSGVO (rechtliche Verpflichtung) und lit. e (Rechtsansprüche). Nach Fristablauf wird im regulären Löschlauf gelöscht (17.2.2). Personenbezogene Nicht-Belege (z. B. Mieterpost, Bewerbungen) erhalten eigene Kategorien mit kürzeren Fristen. Livos erstellt ein Löschkonzept je Kategorie (Frist, Bezugsdatum, Verantwortlicher, Freigabe). | [K] |
| Betroffenenrechte | Auskunft über Volltext- und Eigenschaftssuche; Schwärzen als Werkzeug für Herausgaben | [S] |
| Personenbezogene Kennzahlen | Liegezeit je Bearbeiter nur nach Abstimmung mit DSB/Betriebsrat (Kapitel 16.5) | [O] |
| Verzeichnis von Verarbeitungstätigkeiten | Livos ergänzt die Verarbeitungen „Rechnungseingang", „Vertragsverwaltung", „Postverteilung", „Reporting" | Organisation |

## 17.6 E-Rechnungspflichten

| Pflicht | Inhalt | Umsetzung |
|---|---|---|
| Empfang | Seit 01.01.2025 müssen inländische Unternehmen E-Rechnungen empfangen können; ein E-Mail-Postfach genügt (BMF-FAQ E-Rechnung). Peppol ist nicht erforderlich. | Empfang über die Rechnungspostfächer (S-14) [S] |
| Formate | XRechnung und ZUGFeRD ab 2.0.1 erfüllen die Anforderungen, **nicht** die Profile MINIMUM und BASIC-WL (BMF-FAQ). d.velop invoices liest ZUGFeRD 2.x, XRechnung 3.0 und Factur-X aus und visualisiert sie. | [S] |
| Validierung | d.velop validiert ausschließlich XRechnungen (KoSIT-Validator, Prüfbericht als Anhang). Eine Profilprüfung für ZUGFeRD ist nicht dokumentiert → Prüfung über BeSync oder Regel [A] (Katalog 2.4). | [S]/[A] |
| Übergang Aussteller | Umsätze bis 31.12.2026: Papier oder sonstiges Format zulässig. Umsätze 2027: nur noch bei Vorjahresumsatz des Ausstellers bis 800.000 € (bzw. EDI). Ab 2028: E-Rechnung Pflicht (§ 27 Abs. 38 UStG). | Anteil E-Rechnungen steigt 2027 deutlich; Messung über KPI-12 |
| Hybride Rechnung | Das XML ist führend | Prüfung auf XML-Basis |
| Fehlerbehandlung | Formale Fehler (Format, Geschäftsregeln) → Rückweisung und Neuanforderung; Leistungskürzung → Zahlbetrag, Rechnung bleibt formal gültig (AE-14; BMF-Schreiben 15.10.2025) | WF-05 |
| Aufbewahrung | XML im Original, 8 Jahre | 17.2 |
| Ausstellerpflicht Livos | Die Pflicht zur Ausstellung von E-Rechnungen gilt nicht für nach § 4 Nr. 8 bis 29 UStG steuerfreie Umsätze (z. B. steuerfreie Wohnraumvermietung). Für steuerpflichtige Umsätze der Gesellschaften klärt Livos die Ausgangsseite mit der Steuerberatung; sie ist nicht Gegenstand dieses Konzepts. | [O] |
| Technischer Stichtag d.velop | Der alte Kommunikationsweg in d.velop invoices wird am 01.01.2027 abgeschaltet; die Validierungsberichte setzen den neuen Weg voraus | Aufbau direkt auf dem neuen Weg (AE-22) |

## 17.7 Datenzugriff der Finanzverwaltung (Z1, Z2, Z3)

Das Zugriffsrecht nach § 147 Abs. 6 AO ist auf den Rahmen der jeweiligen Außenprüfung beschränkt. Buchungsdaten kommen weiterhin aus DATEV. Das DMS liefert die Belege; der Dokumentenlink im DATEV-Buchungssatz und die Gesellschaft (E-01) am Beleg verbinden beide Welten.

| Zugriffsart | Inhalt | Umsetzung im Livos-DMS | Status |
|---|---|---|---|
| **Z1** unmittelbarer Zugriff | Einsicht in die gespeicherten Daten und Nutzung des Systems | Prüferrolle **R-14**: befristeter Benutzer mit Nur-Lese-Recht, eingeschränkt über `RS_Mandant` auf die geprüften Gesellschaften; Zeitraumfilter über gespeicherte Suchen; Benutzer wird nach Prüfungsende deaktiviert. Lizenzbedarf für den temporären Prüfer klärt MDIS mit d.velop [O, OP-45]. | [K] |
| **Z2** mittelbarer Zugriff | Livos wertet nach Vorgaben aus und stellt das Ergebnis maschinell auswertbar bereit oder ermöglicht Nur-Lese-Zugriff (GoBD 2. Änderung) | vorbereitete **Suchvorlagen** (Beispiele: „Eingangsrechnungen Gesellschaft X, Jahr Y", „Gutschriften Gesellschaft X", „Rechnungen § 13b Gesellschaft X") mit Export „Eigenschaften exportieren" (CSV/Excel); REB-CSV-Export | [K] |
| **Z3** Datenüberlassung | Daten inkl. Meta-, Stamm- und Bewegungsdaten, Verknüpfungen und elektronischer Dokumente in maschinell auswertbarem Format | **repo export-API** (Originale aller Versionen + JSON-Metadaten inkl. Verknüpfungen und Aktivitäten) über das Verfahren aus 17.8, gefiltert auf Gesellschaft und Zeitraum | [A] |

Ein Prüfungsleitfaden (Ansprechpartner, Anlage des Prüfers, Suchvorlagen, Exportverfahren) wird Teil der Verfahrensdokumentation.

## 17.8 Export je Gesellschaft bei Verkauf (AE-25, Katalog 1.6)

### 17.8.1 Anforderung und Bewertung

Livos fordert, dass alle Protokolle und Unterlagen einer Gesellschaft, z. B. bei deren Verkauf, exportiert und revisionssicher weitergegeben werden können. Revisionssicherheit und Protokollierung sind Standard [S]. Das Exportpaket je Gesellschaft ist eine Anpassung [A]: Die Export-Schnittstelle von d.velop kennt keinen Filter nach Gesellschaft (Katalog 1.6 = S/A). Das Verfahren ist skriptbar und wiederholbar, aber kein Knopfdruck.

### 17.8.2 Werkzeug: repo export-API

| Merkmal | Befund (d.velop documents repo export, Handbuch) |
|---|---|
| Inhalt | eine Datei je Dokumentversion, abhängige Dateien (PDF-Rendition), Metadaten im JSON-Importformat mit allgemeinen, erweiterten und Systemeigenschaften, Versionsinformationen, Notizen, Verknüpfungen und Aktivitäten |
| Delta | Delta-Export möglich; Stammdatenkonfiguration (Eigenschaften, Kategorien) exportierbar |
| Filter | nur Änderungszeitraum, Kategorie und Dokument-IDs (höchstens 100 je Aufruf) |
| Freischaltung | in der Cloud je Tenant über den d.velop-Support |
| Recht | Benutzer braucht das Recht „Datenexport" |
| Weiterverwendung | Das Ausgabeformat passt zum Importformat von „d.velop cloud migration"; ein Käufer mit d.velop cloud kann das Paket importieren |

### 17.8.3 Paketinhalt

| Bestandteil | Quelle | Format |
|---|---|---|
| Alle Dokumente der Gesellschaft (alle Kategorien, alle Versionen) | repo export-API | Originalformat (inkl. E-Rechnungs-XML) + PDF/A |
| Metadaten, Notizen, Verknüpfungen, Aktivitäten | repo export-API | JSON |
| Aktenstruktur (Gesellschafts-, Objekt-, Kreditoren-, Vorgangs-, Vertragsakten) | repo export-API (Akten als Objekte mit Verknüpfungen) | JSON |
| Workflowprotokolle smart invoice und process studio | DMS (Kategorie „Workflowprotokoll ERV", exportierte Prozessprotokolle) | PDF/Dokument + JSON |
| Rechnungsdaten (Kopf, Positionen, Kontierung, Zahlbetrag, Zahlstatus) | Eigenschaften + REB-Export + BeSync-Staging | CSV/JSON |
| Eigenschafts- und Kategoriedefinitionen | repo export-API (Konfiguration) | JSON |
| Verfahrensdokumentation (Stand im Exportzeitraum) | DMS | PDF |
| Übergabeprotokoll | BeSync-Exportskript | PDF + Prüfsummenliste |

### 17.8.4 Ablauf

| Nr. | Schritt | Verantwortlich |
|---|---|---|
| 1 | Anlass und Umfang festlegen (Gesellschaft, Zeitraum, Share Deal oder Asset Deal, Behandlung gesellschaftsübergreifender Dokumente) | Livos (GF, Recht, Steuer) |
| 2 | Export-Schnittstelle prüfen bzw. freischalten lassen; Export-Benutzer aktivieren | MDIS, d.velop |
| 3 | Dokument-IDs ermitteln: DMS-Suche über alle Kategorien nach Mandant = Gesellschaft | BeSync-Exportskript |
| 4 | Export in Paketen zu je 100 IDs; Dateien und JSON laden | BeSync-Exportskript |
| 5 | Workflowprotokolle, Rechnungsdaten und Verfahrensdokumentation ergänzen | MDIS |
| 6 | Vollständigkeitsprüfung: Anzahl Dokumente und Versionen je Kategorie gegen Suche; Prüfsummen (Hash) je Datei | MDIS; Abnahme Livos |
| 7 | Mehrgesellschaftsdokumente (Mehrfachwert Mandant) juristisch prüfen, ggf. schwärzen oder ausnehmen | Livos Recht |
| 8 | Übergabe (Datenträger oder Plattform) mit Übergabeprotokoll | Livos |
| 9 | Nach Übergabe: Dokumente der Gesellschaft sperren (Berechtigung), **nicht löschen**; Aufbewahrungspflichten beim Veräußerer klären | Livos, MDIS |

### 17.8.5 Voraussetzungen

| Voraussetzung | Grund |
|---|---|
| Mandant (E-01) ist Pflicht auf **allen** Kategorien, einschließlich Akten, Postdokumenten und Workflowprotokollen (P1) | Ohne Schlüssel keine vollständige Suche |
| Akten nie gesellschaftsübergreifend als Ablageort; gesellschaftsübergreifende Sichten nur über gespeicherte Suchen (AE-19) | saubere Trennung |
| Freischaltung der Export-Schnittstelle und Kostenfreiheit vertraglich mit d.velop sichern | Verfügbarkeit über die Vertragslaufzeit |
| Probeexport einmal jährlich für eine Pilotgesellschaft (Vorschlag) | Verfahren bleibt funktionsfähig |
| Rechtliche Klärung Share Deal/Asset Deal und Umfang der Kopien beim Konzern | Umfang des Pakets |

Bei einem Systemwechsel genügt es nach Ablauf des fünften Kalenderjahres nach der Umstellung, die Daten auf einem maschinell lesbaren und auswertbaren Datenträger vorzuhalten (§ 147 Abs. 6 S. 5 AO). Bis dahin muss auch der Käufer Z1/Z2 ermöglichen können. Das spricht für ein importfähiges Paket (Originale + JSON) statt reiner PDF-Sammlungen.

### 17.8.6 Aufwand

Einmalig: Entwicklung und Test des BeSync-Exportskripts und des Runbooks (gering bis mittel). Je Anlass: Ausführung, Vollständigkeitsprüfung und Übergabe (gering, abhängig von der Dokumentmenge) sowie die rechtliche Prüfung durch Livos. Die Konditionen enthält das Angebot.

## 17.9 Informationssicherheit

| Maßnahme | Festlegung | Status |
|---|---|---|
| Single Sign-on | OIDC mit Microsoft Entra ID; Bedingter Zugriff und Passwortrichtlinien gelten aus Entra ID (S-13) | [S/K] |
| Mehrfaktor-Anmeldung | über Entra ID für interne Benutzer; für externe Konten (R-08) 2FA (TOTP) oder FIDO2 in d.velop verpflichtend | [S] |
| Rollen und Rechte | Rollen R-01 bis R-15 und Gruppenmodell nach Kapitel 13; Prinzip minimaler Rechte; Löschrechte nur Administration | [K] |
| Rezertifizierung | halbjährlich (Vorschlag): Gesellschafts- und Rollengruppen durch die Gesellschaftsverantwortlichen bestätigen; externe Konten und Prüferzugänge quartalsweise; Ergebnis als Organisationsunterlage (K-15) ablegen | Organisation |
| Ein- und Austritt | Provisionierung und Deprovisionierung über Entra ID/SCIM; offene Aufgaben vorher umverteilen (Kapitel 18) | [S] |
| Technische Benutzer und Secrets BeSync | ein technischer Benutzer je Schnittstellengruppe, API-Keys im Secret-Store, Rotation, Signaturprüfung der Webhooks (Kapitel 15.8.4) | [A] |
| Partner-/Supportzugang | nur kundenseitig vergeben, zeitlich begrenzt (Support höchstens 7 Tage, benannte Consultants höchstens 12 Monate), Zugriffe werden protokolliert (d.velop Administration Cloud) | [S] |
| Protokollierung | Plattform-Audit-Trail sicherheitsrelevanter Ereignisse (Lese- und Schreibzugriffe, Anmeldungen, Rollen- und Konfigurationsänderungen) 180 Tage; fachliches Aktivitätenprotokoll je Dokument; BeSync-Protokoll | [S]/[A] |
| Teilen mit Externen | Teilen-Links nur befristet (höchstens 180 Tage) und nur für freigegebene Kategorien | [K] |
| Datensicherung | durch d.velop (tägliche Backups, 30 Tage); Exit-Fähigkeit über repo export-API | [S] |
| Notfall | Ausfall d.velop: Rechnungen bleiben im Postfach und werden nachverarbeitet; Ausfall BeSync: Kapitel 15.8.2 | Organisation |

# 18 Betrieb, Organisation und Change

Dieses Kapitel legt fest, wer das Livos-DMS nach dem Go-live betreibt, wie Störungen und Änderungen bearbeitet werden, wie Stammdaten gepflegt werden und wie Livos, Trios, Property Manager und Lieferanten auf die Umstellung vorbereitet werden. Dauern, Rhythmen und Schwellen sind Vorschläge und werden im Projekt mit Livos festgelegt.

## 18.1 Betriebsmodell

| Ebene | Betreiber | Leistung |
|---|---|---|
| Plattform (d.velop documents, d.velop invoices, smart invoice, process studio, contracts, pilot) | **d.velop** (SaaS, Betriebsform C1) | Hosting, Verfügbarkeit, Datensicherung, Sicherheitsupdates, Releases, Herstellersupport |
| DATEV-Konnektor LDconnect | **LIONDEER** | Betrieb des Konnektors, Herstellersupport |
| DATEV-Server, DATEVconnect, Gateway-Endpunkt | **Hoster** / DATEV-Systembetreiber | Betrieb DATEV, Freigaben im Gateway |
| BeSync und Lieferanten-App | **MDIS** | Hosting, Betrieb, Überwachung, Fehlerbehebung, Anpassung aller BeSync-Schnittstellen (Kapitel 15) |
| Anwendungsbetreuung d.velop | **MDIS** | Konfiguration (Kategorien, Workflows, Importprofile, Rechte), Tenant-Administration (R-15), Second-Level-Support, Release-Tests, Weiterentwicklung |
| Fachadministration | **Livos Key-User/Fachadmin (R-12)** | Stammdatenpflege in der Lieferanten-App, Freigabematrix, Gruppenzuordnung, Vertretung für Dritte, First-Level-Support |
| Buchhaltung und DATEV-Stammdaten | **Trios** | Buchung, Kreditorenanlage, Zahlungsvorschlag, Klärung Übergabefehler |
| Identitäten und Postfächer | **Livos IT** | Entra ID, SCIM, M365-Postfächer und Aliase |

Leitprinzip: Livos pflegt fachliche Daten, keine technischen Tabellen (P3). Alles Technische rund um BeSync liegt bei MDIS.

**Key-User-Modell (Vorschlag):** ein zentraler Fachadministrator bei Livos (Vertretung geregelt) plus je Segment (Bestand, Privatisierung, Bau) ein Key-User aus dem Fachbereich sowie ein Key-User bei Trios. Key-User sind erste Ansprechpartner, testen Releases fachlich und schulen neue Kollegen.

## 18.2 Support-Prozess

| Level | Wer | Aufgaben | Kanal |
|---|---|---|---|
| Level 1 | Livos Key-User/Fachadmin (R-12); bei Trios der Trios-Key-User | Anwenderfragen, Bedienung, Vertretungen setzen, Aufgaben umverteilen, Stammdatenfragen, Klärfälle, Erstbewertung von Störungen | intern (Teams/E-Mail), Wissensartikel |
| Level 2 | MDIS Anwendungsbetreuung und BeSync-Betrieb | Konfigurationsfehler, Workflowprobleme, Schnittstellenstörungen, Rechte, Datenkorrekturen, Analyse und Weitergabe an Hersteller | MDIS-Ticketsystem, Supportzugang d.velop (kundenseitig freigegeben) |
| Level 3 | d.velop, LIONDEER, BIB GmbH, Hoster/DATEV | Produktfehler, Plattformstörungen, Konnektorfehler, DATEV-seitige Probleme | Herstellerportale; Einsteuerung durch MDIS |

**Prioritäten (Vorschlag):**

| Priorität | Beispiel | Reaktion MDIS | Ziel Wiederherstellung |
|---|---|---|---|
| 1 kritisch | kein Rechnungseingang, keine DATEV-Übergabe für alle Mandanten, Anmeldung für alle gestört | 1 Stunde (Geschäftszeit) | 1 Arbeitstag bzw. Umgehung |
| 2 hoch | Schnittstelle einer Gesellschaftsgruppe gestört, Zahlstatus-Lauf fehlt | 4 Stunden | 2 Arbeitstage |
| 3 normal | Einzelfehler, Rechtefrage, Anpassung einer Sicht | 1 Arbeitstag | nach Absprache |
| 4 Änderung | neue Gesellschaft, neuer Workflowschritt, neuer Bericht | Planung im Change-Prozess (18.3; Change-Board, Kapitel 19.7.2) | Release-Termin |

Die verbindlichen Service-Level regelt der Betriebsvertrag zwischen Livos und MDIS. Die Plattform-SLA gibt d.velop vor.

## 18.3 Release-Management

| Thema | Festlegung |
|---|---|
| Rhythmus d.velop | d.velop entwickelt die Cloud laufend weiter und fasst Neuerungen quartalsweise zusammen (z. B. „Current 2026.Q3"); Neuerungen und Ankündigungen erscheinen im d.velop-Helpcenter. Ob Livos Cloud-Updates zeitlich beeinflussen kann, ist nicht dokumentiert [O, OP-44]. |
| Vorschau-Funktionen | Funktionen im Vorschaustatus (z. B. „Vier-Augen ab Betrag") werden nur nach Freigabe durch d.velop und nach Test aktiviert (AE-05, OP-09). |
| Beobachtung | MDIS wertet Release Notes und Ankündigungen monatlich aus und bewertet die Wirkung auf Livos (Beispiel: Abschaltung des alten Kommunikationswegs zum 01.01.2027). |
| Test-Tenant | ein Test-/Abnahme-Tenant mit produktionsgleicher Konfiguration (AE-01); Lizenzierung klärt MDIS mit d.velop [O, OP-20]. Konfigurationsänderungen gehen immer zuerst in den Test-Tenant. |
| Regressionstest | nach jedem Quartalsrelease und bei angekündigten Änderungen: Kerntestfälle WF-01 bis WF-05, Schnittstellen S-01, S-04, S-06, S-11, S-12, Rechte-Stichproben (Kapitel 15.8.5). Fachliche Bestätigung durch Key-User. |
| Umsystem-Releases | DATEV-Updates beim Hoster, LDconnect-Versionen und BIM4You-Jahresrelease werden wie d.velop-Releases behandelt: Ankündigung, Test, Freigabe. |
| Eigene Änderungen | Bündelung in geplanten Releases (Vorschlag: monatlich), Dokumentation im Änderungsprotokoll und in der Verfahrensdokumentation (Kapitel 17.3). |

## 18.4 Monitoring

| Objekt | Was wird überwacht | Werkzeug | Rhythmus | Zuständig |
|---|---|---|---|---|
| Fehlerschritte smart invoice | Belege im Fehlerschritt oder mit „Technisches Problem" | REB-Schnellzugriff „Übergabefehler"/Fehlerschritt; smart-invoice-Administration | täglich | MDIS, Trios |
| Transfers | offene Transfers (BIM4You), Alter im Verhältnis zum 28-Tage-Fenster | BeSync-Überwachung | laufend, Bericht täglich | MDIS |
| Webhooks | Erreichbarkeit und Antwortzeit der BeSync-Endpunkte (Quittung ≤ 30 s) | BeSync-Überwachung mit Alarm | laufend | MDIS |
| LDconnect-Sync | Erfolg des täglichen Stammdatenabrufs, Übergabefehler | LDconnect-Protokoll, Klärfälle „Kreditor fehlt" | täglich | MDIS, LIONDEER |
| Zahlstatus-Lauf (S-06) | Erfolg, Treffer/Nichttreffer | BeSync | täglich | MDIS; Klärliste an Trios |
| E-Mail-Eingang | Jobübersicht email import, nicht verarbeitete Mails | d.velop email import | täglich | MDIS, Level 1 |
| Workflows process studio | fehlerhafte Instanzen | process studio Überwachung | täglich | MDIS |
| Mengen und Limits | Ausführungskontingent process studio, Rechnungsvolumen je Edition, Bucket-Limits, Speicher | d.velop Administration, BeSync | monatlich | MDIS |
| Rechte | Rezertifizierung (Kapitel 17.9) | Gruppenberichte | halbjährlich | Livos |

MDIS liefert monatlich einen Betriebsbericht (Verfügbarkeit, Störungen, Volumen, Klärfälle, Kontingente, anstehende Releases).

## 18.5 Stammdatenpflege-Prozesse

| Prozess | Auslöser | Ablauf | Verantwortlich | Werkzeug |
|---|---|---|---|---|
| Neue Gesellschaft | Gründung, Erwerb | Gesellschaftsstamm in der Lieferanten-App (Mandanten-ID, Name exakt wie auf Rechnungen, Anschrift, Segment, Verwaltungsart) → BeSync legt Dataset-Wert, Gruppe, Restriction-Set-Zuordnung und smart-invoice-Mandant an → Trios richtet DATEV-Mandant und LDconnect-Anbindung ein → Freigabematrix-Zeilen → REB-Berechtigung → Alias-Postfach (optional) | R-12, Trios, MDIS, Livos IT | M-16, M-17 |
| Gesellschaft verkauft/aufgelöst | Verkauf, Liquidation | Export (Kapitel 17.8) → Rechte sperren → Mandant in smart invoice deaktivieren → Alias abschalten | Livos, MDIS | – |
| Neues Objekt | Ankauf, Projektstart | Objektstamm in der Lieferanten-App (Objekt-ID, Mandant, Verwaltungsart, PM, Bauprojekt ja/nein, BIM4You-Projekt-ID) → Dataset/`RS_Objekt` → Objektakte | R-12 | M-16 |
| Neuer Kreditor | Klärfall „Kreditor fehlt" | Anlage-Anforderung aus der Lieferanten-App an Trios → Anlage in DATEV → Stammdatenabruf am Folgetag → Beleg läuft weiter; Konsolidierungsnummer zuordnen | R-02, R-12, Trios | M-05, M-16 |
| Bankverbindung ändert sich | Lieferantenmitteilung | **Nur** nach Rückbestätigung beim Lieferanten über eine bekannte Kontaktadresse (Betrugsprävention); Änderung in DATEV durch Trios; Sync am Folgetag | Trios, R-02 | DATEV |
| Freigabematrix | Organisationsänderung, neue Wertgrenzen | Antrag durch Gesellschaftsverantwortliche → Pflege durch R-12 → Vier-Augen-Kontrolle → Ablage des Matrixstands als Organisationsunterlage (K-15) | R-12 | M-17 |
| Benutzer und Rollen | Ein-/Austritt, Wechsel | Entra ID-Gruppen (Livos IT) → SCIM; offene Aufgaben vor Austritt umverteilen | Livos IT, R-12 | Entra ID |
| Property Manager | PM-Wechsel | Objektstamm (PM, Rückmeldeadresse) aktualisieren; neuen PM informieren (18.6) | R-12, Asset Management | M-16 |
| Wertelisten | neue Rückweisungs-/Kürzungsgründe | Antrag → Freigabe Fachbereich → Pflege durch R-12 in der smart-invoice-Administration; MDIS passt ggf. die Mailvorlagen (S-11) an | R-12, MDIS | smart invoice Administration |

## 18.6 Change-Management

### 18.6.1 Kommunikation intern

| Zeitpunkt | Zielgruppe | Inhalt | Kanal |
|---|---|---|---|
| Projektstart | Geschäftsführung, Führungskräfte | Ziele, Nutzen, Zeitplan, Rollen | Management-Runde |
| 8 Wochen vor Go-live je Phase | alle betroffenen Anwender | Was ändert sich, ab wann, Schulungstermine | E-Mail, Intranet, Teamrunden |
| 2 Wochen vor Go-live | Anwender, Trios | Stichtag, Übergangsregeln (Altbelege, Papierwege), Ansprechpartner | E-Mail, Kurzanleitung |
| Hypercare (4 Wochen nach Go-live) | alle | tägliche Sprechstunde, FAQ | Teams |
| laufend | Key-User | Release-Neuerungen, Tipps | Key-User-Runde monatlich |

### 18.6.2 Lieferantenanschreiben

Das Lieferantenanschreiben ist eine Kernmaßnahme für die Mandantenerkennung (AE-23) und die E-Rechnungsquote.

| Inhalt | Zweck |
|---|---|
| Neue Rechnungsadresse `rechnung@…` bzw. Alias je Gesellschaft (Beispiel: eine Adresse je Gesellschaft oder Gesellschaftsgruppe) | automatischer Eingang, Vorbelegung Mandant |
| Exakte Gesellschaftsbezeichnung und Anschrift als Rechnungsempfänger (§ 14 Abs. 4 Nr. 1 UStG) | Mandantenerkennung über Name und Anschrift |
| Bitte um E-Rechnung (XRechnung oder ZUGFeRD ab 2.0.1, nicht MINIMUM/BASIC-WL) | E-Rechnungsquote, Validierung |
| Käuferreferenz (BT-10) mit der Livos-Gesellschaftsnummer bei E-Rechnungen | eindeutige Zuordnung (Wirkung im Test klären, OP-02) |
| Auftrags-/Vertragsnummer auf der Rechnung, bei Bau die BIM4You-Vertragsnummer | Vorgangsakte, BIM4You-Zuordnung |
| Eine Rechnung je PDF, keine Sammel-PDFs; Anlagen als eigene Dateien | Trennung und Erkennung |
| Hinweis auf Rückweisung bei fehlenden Pflichtangaben mit Standardgründen | Erwartungsmanagement (WF-05) |
| Bankverbindungsänderungen nur schriftlich mit Rückbestätigung | Betrugsprävention |

**Vorgehen (Vorschlag):** Versand über die Lieferanten-App als Serienmail an die Top-Lieferanten (nach Volumen) acht Wochen vor Go-live, an alle übrigen vier Wochen vor Go-live. Rückläufer und Adressänderungen pflegt R-12. Die E-Rechnungsquote (KPI-12) und die Klärfallquote Mandant (KPI-09) zeigen die Wirkung; gezielte Nachfass-Aktionen bei Lieferanten mit vielen Klärfällen.

### 18.6.3 Information der Property Manager

| Inhalt | Details |
|---|---|
| Neuer Einreichungsweg | Rechnungen über dem Schwellwert per E-Mail an `freigabe-hv@…` (Alias) statt bisherigem Weg |
| Was der PM mitschickt | Rechnung als PDF oder E-Rechnung; im Betreff oder in der Mail Objekt-ID und Gesellschaft (Beispielformat vorgeben) |
| Rückmeldung | Freigabe oder Ablehnung mit Begründung per E-Mail aus d.velop/BeSync (S-11); keine Systemanmeldung nötig |
| Schwellwerte und Fristen | je Objekt bzw. Verwaltervertrag (Livos Asset Management) |
| Optional | monatliche Buchungsdaten im DATEV-Format (S-16), Rechnungsweiterleitung als E-Rechnung |
| Form | Anschreiben durch Asset Management, Einseiter mit Beispielen; Aufnahme in den Verwaltervertrag bei Neuabschluss (Vorschlag) |

## 18.7 Schulungskonzept

Grundsatz: rollenbezogen, kurz, am echten Beleg. Key-User werden zuerst geschult und schulen mit. Dauer als Vorschlag.

| Zielgruppe | Inhalt | Format | Dauer (Vorschlag) |
|---|---|---|---|
| Key-User/Fachadmin (R-12) | Gesamtprozess, Administration smart invoice (Freigabematrix, Wertelisten), Lieferanten-App, Vertretung für Dritte, REB-Schnellzugriffe, Level-1-Support, Testvorgehen | Präsenz- oder Onlineworkshop, Übungen im Test-Tenant | 2 Tage + 0,5 Tag Vertiefung vor Go-live |
| Rechnungseingang/Verteilung (R-02) | Eingangskanäle, Verteilung, Klärfälle, Dubletten, IBAN-Hinweise, Rückweisung mit Grund, Stapel, REB | Onlineschulung + begleitete Echtarbeit in der Hypercare | 1 Tag |
| Sachliche Prüfer (R-03) | Aufgabenliste, Prüfen und Kontieren, Kostenstellen-Split, Zahlbetrag und Kürzungsgrund, Nachweise anhängen, Rückfrage, Vertretung, mobile App | Online, 1 Termin + Kurzanleitung | 2 Stunden |
| Freigeber (R-04) und Zahlungsfreigeber (R-05) | Freigeben/Ablehnen, Historie, Skontoampel, Eskalationen, Vertretung, mobile App; R-05 zusätzlich Zusammenspiel mit multicash | Online oder Einzeleinweisung, Kurzanleitung | 1 Stunde |
| Buchhaltung Trios (R-06) | Buchhaltungsschritt, Kontrolle, DATEV-Übergabe, Übergabefehler, Kreditor-Anlage-Anforderungen, Zahlstatus-Klärliste, Belegaufruf aus DATEV | Workshop mit Test-DATEV-Bestand | 0,5 Tag |
| Controlling/Management (R-07) | REB-Managementsicht, CSV-Export, evidanza-Bericht, KPIs | Online | 1,5 Stunden |
| Asset Management (PM-Freigabe) | WF-03, Maske M-13, Rückmeldetexte, Schwellwerte | Online | 1 Stunde |
| Poststelle/Scan (R-01) (Phase 4) | Scan, Trennblätter, Stapelprüfung, Postklassifizierung, Verteilung | Präsenz am Arbeitsplatz | 0,5 Tag |
| Vertragsmanager (R-11) (Phase 4) | d.velop contracts, Fristen, Vertragsakte, Vertragsfreigabe, d.velop pilot | Online + Übung | 0,5 Tag |
| Externe Kernpartner (R-08) | Anmeldung mit 2FA, Aufgaben, Freigeben/Ablehnen | Kurzanleitung + Video | 30 Minuten |
| Alle DMS-Nutzer | Suche, gespeicherte Suchen, Akten, Ablage, Outlook-Integration, Aufgaben am Dokument | E-Learning/Video + Kurzanleitung | 1 Stunde |
| MDIS-Betriebsteam | Livos-Konfiguration, Betriebshandbuch, Monitoring | interne Übergabe Projekt → Betrieb | 1 Tag |

Nach drei Monaten Echtbetrieb folgt eine Auffrischung für R-02, R-03 und R-04 auf Basis der häufigsten Tickets und Klärfälle.

## 18.8 Dokumentation und Handbücher

| Dokument | Inhalt | Zielgruppe | Ersteller | Ablage |
|---|---|---|---|---|
| Kurzanleitungen je Rolle | 1–2 Seiten je Rolle mit den häufigsten Aktionen | Anwender | MDIS, Key-User | DMS + Startseiten-Widget |
| Anwenderhandbuch Livos | Prozesse WF-01 bis WF-10 aus Anwendersicht, Livos-spezifische Regeln | Anwender, Key-User | MDIS | DMS |
| Administrationshandbuch | Konfiguration (Kategorien, Eigenschaften, Workflows, Freigabematrix, Rechte, Importprofile), Stammdatenprozesse (18.5) | Key-User, MDIS | MDIS | DMS |
| Betriebshandbuch | Betriebsmodell, Support, Monitoring, Wiederanlauf, Release-Tests, Kontakte der Hersteller | MDIS, Livos IT | MDIS | DMS |
| Schnittstellendokumentation | S-01 bis S-17: Mapping, Auslöser, Fehlerbilder, technische Benutzer (ohne Secrets) | MDIS, Livos IT | MDIS | DMS |
| Verfahrensdokumentation | nach Kapitel 17.3 | Livos, Prüfer | Livos (verantwortlich), MDIS, Trios | DMS (K-15 Organisationsunterlage) |
| Export-Runbook | Kapitel 17.8 | MDIS, Livos | MDIS | DMS |
| FAQ/Wissensartikel | aus Tickets der Hypercare | Anwender | Key-User | DMS |

Alle Dokumente sind versioniert im DMS abgelegt. Änderungen am System ziehen eine Aktualisierung der betroffenen Dokumente nach sich (Teil der Definition „erledigt" jeder Änderung).

## 18.9 Kennzahlen für den Betrieb

| Nr. | Kennzahl | Definition | Quelle | Ziel (Vorschlag) |
|---|---|---|---|---|
| B-01 | Verfügbarkeit BeSync-Schnittstellen | Anteil der Zeit, in der die Webhook-Endpunkte erreichbar sind | BeSync-Überwachung | ≥ 99,5 % in der Geschäftszeit |
| B-02 | Belege im Fehlerschritt | Anzahl Belege in Fehlerschritten, Alter | REB | 0 älter als 1 Arbeitstag |
| B-03 | Schnittstellenfehlerquote | fehlgeschlagene Nachrichten je Schnittstelle / alle Nachrichten | BeSync | < 1 % |
| B-04 | Stammdatenaktualität | Tage seit letztem erfolgreichen LDconnect- und BeSync-Stammdatenlauf | Protokolle | ≤ 1 |
| B-05 | Zahlstatus-Trefferquote | zugeordnete Posten / abgefragte Belege | BeSync | ≥ 95 % |
| B-06 | Ticketvolumen und Lösungszeit | Tickets je Level und Priorität, mittlere Lösungszeit | Ticketsystem | Trend fallend nach Hypercare |
| B-07 | Klärfälle „Kreditor fehlt" | Anzahl und Dauer bis Auflösung | BeSync | Dauer ≤ 2 Arbeitstage |
| B-08 | Kontingentnutzung | process-studio-Ausführungen, Rechnungsvolumen je Edition, Bucket-Limits | d.velop Administration | < 80 % des Kontingents |
| B-09 | Release-Tests | Anteil der Releases mit abgeschlossenem Regressionstest vor Produktivwirkung | Änderungsprotokoll | 100 % |
| B-10 | Rezertifizierung | Anteil fristgerecht bestätigter Gruppen | Rezertifizierungsprotokoll | 100 % |

Die fachlichen Prozesskennzahlen (Durchlaufzeiten, Skontoquote, Klärfall- und Rückweisungsquoten) stehen in Kapitel 16.3.

# 19 Einführungsvorgehen und Roadmap

Dieses Kapitel beschreibt, wie Livos die Lösung schrittweise einführt. Es legt Phasen, Pilotgesellschaften, Migration, Test und Abnahme, Go-live, Hypercare und die Projektorganisation fest. Alle Dauern und Zeitangaben sind **Vorschläge** von MDIS. Sie gelten ab Beauftragung und werden in Phase 0 mit Livos, Trios und d.velop verbindlich geplant.

Grundlage ist Designprinzip **P8 (schrittweise Einführung)**: Zuerst kommt der Rechnungseingang mit dem größten Hebel, danach folgen PM-Freigabe, Bau/BIM4You, Verträge und Post.

## 19.1 Vorgehensmodell

MDIS führt die Lösung **iterativ in Stufen** ein. Jede Phase endet mit einem Qualitätstor (QG), an dem Livos abnimmt und über den Start der nächsten Phase entscheidet. Innerhalb einer Phase arbeitet das Team in kurzen Konfigurationszyklen von zwei Wochen (Vorschlag). Am Ende jedes Zyklus zeigt MDIS das Ergebnis im Test-Tenant und nimmt Rückmeldungen der Key-User auf.

| Element | Ausgestaltung | Begründung |
|---|---|---|
| Standard vor Konfiguration vor Entwicklung | Jede Anforderung wird zuerst gegen den d.velop-Standard geprüft (smart invoice, documents, contracts). BeSync kommt nur dort zum Einsatz, wo der Standard endet (P2, P3). | Geringerer Betriebsaufwand, Release-Sicherheit, Livos pflegt keine technischen Middleware-Tabellen |
| Zwei Umgebungen | Ein **Test-/Abnahme-Tenant** und ein **produktiver Tenant** (AE-01). Konfiguration entsteht im Test-Tenant, wird dort abgenommen und dann übertragen (DmsConfig-Paket, Test T23). | process studio hat keinen Testmodus; der Demo-Tenant ist ein geteilter Fremd-Tenant und für Tests ungeeignet |
| Pilot vor Rollout | Phase 1 startet produktiv mit 3–5 Pilotgesellschaften (Kap. 19.3). Der Rollout auf alle Gesellschaften folgt erst nach der Pilotabnahme. | Mandantenerkennung, DATEV-Übergabe und Freigabematrix werden unter Echtbedingungen geprüft, bevor über 100 Gesellschaften folgen |
| Wellen im Rollout | Gesellschaften werden in Wellen zugeschaltet (Vorschlag: 20–30 Gesellschaften je Welle). Neue Gesellschaft = Stammdatensatz + Gruppe + Restriction-Set-Zuordnung + smart-invoice-Mandant (AE-18). | Steuerbarer Supportaufwand; Lieferantenanschreiben je Welle |
| Qualitätstore | QG-0 bis QG-5 am Ende jeder Phase, mit Abnahmeprotokoll und Entscheidung des Lenkungsausschusses | Klare Entscheidungspunkte für Livos und Trios |
| Entscheidungen früh | Offene Architekturentscheidungen (Status O) und Entscheidungsbedarfe ED-01 ff. (Kap. 20.2) werden in Phase 0 entschieden oder mit Termin versehen. | Späte Entscheidungen zu DATEV-Übergabe oder Bau-Prozess verursachen Umbau |
| As-built-Dokumentation | Jede Konfigurationsstufe wird als As-built-Protokoll dokumentiert (Inventur, angelegt, geändert, Abweichungen). | Grundlage für Verfahrensdokumentation (Kap. 17) und Betrieb (Kap. 18) |

**Qualitätstore (Vorschlag):**

| QG | Zeitpunkt | Prüfgegenstand | Entscheider |
|---|---|---|---|
| QG-0 | Ende Phase 0 | Feinkonzept freigegeben, Entscheidungen ED getroffen oder terminiert, Plattformtests T01–T23 ausgewertet, Lizenzen und DATEV-Komponenten beauftragt | Lenkungsausschuss |
| QG-1a | vor Pilot-Go-live | Abnahmetest Phase 1 bestanden, Go-live-Checkliste (Kap. 19.6) erfüllt | Projektleitung Livos + MDIS, Trios |
| QG-1b | Ende Pilot | Pilotkennzahlen erreicht (Kap. 19.5), Freigabe Rollout | Lenkungsausschuss |
| QG-2 | Ende Phase 2 | alle Gesellschaften produktiv, WF-03/WF-05, Reporting und Exportverfahren je Gesellschaft abgenommen | Lenkungsausschuss |
| QG-3 | Ende Phase 3 | Bau-Prozess mit BIM4You, Zahlstatus, FSB abgenommen | Lenkungsausschuss |
| QG-4 | Ende Phase 4 | Verträge und Post produktiv | Lenkungsausschuss |
| QG-5 | je Optimierungspaket | Nutzen nachgewiesen, Übergabe in den Regelbetrieb | Projektleitung |

## 19.2 Phasenplan

### 19.2.1 Übersicht

| Phase | Inhalt | Workflows / Schnittstellen (IDs) | Voraussetzungen | Ergebnis / Abnahme | Dauer (Vorschlag) |
|---|---|---|---|---|---|
| **0 Klärung & Setup** | Prozess-Workshop (2–3 h) und Detailworkshops; Entscheidungen zu AE mit Status O; Plattformtests; Lizenz- und Mengengerüst; Test-Tenant; Beauftragung DATEV-Komponenten und Gateway; KI-PoC Kreditorenkonsolidierung in der Lieferanten-App | – (Vorbereitung für WF-01, WF-04, S-01, S-02, S-13, S-14) | Beauftragung; Benennung Projektleitung und Key-User Livos; Ansprechpartner Trios und DATEV-Hoster | Freigegebenes Feinkonzept Phase 1; Entscheidungsprotokoll ED-01 ff.; Testbericht T01–T23 (Kap. 20.4); Mengengerüst; Bestellungen; Pilotgesellschaften benannt (QG-0) | 4–6 Wochen |
| **1 MVP Rechnungseingang** | Standard-Eingangsrechnung mit Verteilung, Prüfung, Freigabematrix, Zahlungsfreigabe, Buchhaltung und DATEV-Übergabe; Klärfälle Mandant/Kreditor; Aufgaben am Dokument; Rechte, Aktenplan, Aufbewahrung; Protokollierung der Schrittwechsel; Pilot mit 3–5 Gesellschaften; Lieferantenanschreiben | WF-01, WF-04, WF-08; S-01, S-02, S-13, S-14, S-12 (nur Protokollierung) (S-03 optional, S-07 unverändert im Bestand) | DATEV-Anbindung (LDconnect, DATEVconnect, Riecken-Gateway) betriebsbereit; M365 und Entra ID (OP-16); Mandanten-ID-Format mit Trios abgestimmt | Abnahmetest bestanden (QG-1a); Pilotbetrieb mindestens 4 Wochen mit Zielwerten (QG-1b) | 8–10 Wochen Aufbau + 4–6 Wochen Pilot |
| **2 Rollout & PM-Freigabe** | Rollout auf alle Gesellschaften in Wellen; PM-Freigabeprozess; Rückweisung und Kürzungsmitteilung an Lieferanten; Lieferanten-App an d.velop und DATEV angebunden; Reporting über evidanza; Exportverfahren je Gesellschaft | WF-03, WF-05; S-04, S-05, S-11, S-12 (Auswertungen), S-15 | Pilotabnahme QG-1b; Schwellwerte und Scope PM-Freigabe entschieden (OP-17); Postfach `freigabe-hv@…`; evidanza-Zugang (OP-27) | Alle Gesellschaften produktiv; WF-03 und WF-05 abgenommen; Durchlaufzeiten je Schritt und Benutzer in evidanza (QG-2) | 8–12 Wochen (abhängig von der Wellenzahl) |
| **3 Bau, Zahlstatus, FSB** | Bau-Eingangsrechnung mit asynchronem BIM4You-Schritt; Rückmeldung „bezahlt" aus DATEV; Freistellungsbescheinigungen § 48b; externe Ad-hoc-Freigabe; optional PM-Buchungsdaten ins BI | WF-02, WF-10; S-06, S-08, S-09, S-10, optional S-16; AE-15 | Entscheidung führendes System je Bau-Rechnungstyp (ED-03); Schnittstellenklärung mit BIB GmbH (OP-06); Rückkanal smart invoice geklärt (OP-07); OPOS-Zugriff über DATEVconnect (OP-04) | Bau-Rechnungen laufen mit BIM4You-Ergebnis durch; Zahlstatus am Beleg; FSB-Hinweis aktiv (QG-3) | 10–14 Wochen |
| **4 Verträge, Post, DMS-Ausbau** | Vertragsmanagement mit d.velop contracts und Vertragsfreigabe; Postverteilung mit KI-Klassifizierung und mail dispatcher; Ausbau Akten, Outlook-Integration, mobile App; d.velop pilot für Fragen an Verträge | WF-06, WF-07; AE-20, AE-21 | Entscheidungen Scan intern oder Dienstleister (OP-13) und contracts-Freigabeworkflow (OP-12); Aktenstruktur Verträge/Post von Livos; Migrationsumfang Altverträge (Kap. 19.4) | Verträge mit Fristenüberwachung produktiv; Post wird klassifiziert und verteilt (QG-4) | 10–12 Wochen |
| **5 Optimierung** | KI-Nutzung ausbauen (Kontierungsvorschläge auswerten, d.velop pilot, MDIS X.One für übergreifende Analysen); weitere Freigaben ohne Rechnung; perspektivische ERP-/PM-Anbindung; Übernahme von Vorschau-Features nach d.velop-Freigabe | WF-09; S-17; AE-27 | Stabiler Regelbetrieb; Kennzahlen aus Phase 2 und 3 liegen vor | Je Optimierungspaket ein Nutzennachweis (QG-5) | fortlaufend, je Paket 4–8 Wochen |

Die Phasen 3 und 4 können sich überschneiden, wenn Livos das wünscht. Beide Phasen nutzen unterschiedliche Fachbereiche (Bau/Controlling gegenüber Vertragsverantwortlichen und Poststelle). Sie teilen aber MDIS-Ressourcen für BeSync und Berechtigungen.

### 19.2.2 Phase 0 – Klärung und Setup

| Arbeitspaket | Inhalt | Ergebnis | Beteiligte |
|---|---|---|---|
| Prozess-Workshop | 2–3 h, End-to-End-Durchgang Rechnungseingang, PM-Freigabe, Stammdaten, Zahlung | Gemeinsames Prozessbild, Liste Detailthemen | Livos (Projektleitung, Buchhaltung, Asset Management, Controlling), Trios, MDIS |
| Detailworkshops (je 2–4 h, Vorschlag) | (1) Freigabematrix und Wertgrenzen je Gesellschaft; (2) Kreditoren und Lieferanten-App; (3) DATEV-Übergabe und Zahlung mit Trios; (4) Rollen, Rechte, Aktenplan; (5) PM-Freigabe; (6) Bau und BIM4You (Vorklärung) | Feinkonzept je Thema, Entscheidungsvorlagen | wie oben, zusätzlich GF für Freigabegrenzen |
| Entscheidungen | Offene AE: AE-08 (DATEV-Übergabe ein- oder zweistufig), Alternative zu AE-09 (wer schreibt in den Bucket), AE-11 (führendes System je Bau-Rechnungstyp); weitere ED aus Kap. 20.2 | Entscheidungsprotokoll | Lenkungsausschuss |
| Plattformtests | Tests T01–T23 und Zusatztests T24 ff. im Test-Tenant (Kap. 20.4) | Testbericht; Anpassung des Feinkonzepts | MDIS, d.velop |
| Lizenz- und Mengengerüst | Anzahl Buchhaltungsuser, Freigabeuser, DMS-Vollnutzer, contracts-Nutzer; Rechnungsvolumen; Zulässigkeit Dritter (OP-03); Test-Tenant (OP-20) | Mengengerüst und Bestellung | Livos, MDIS, d.velop |
| Test-Tenant | Bereitstellung, Anbindung Entra ID (SCIM, OIDC), Testpostfächer | Arbeitsfähige Testumgebung | MDIS, Livos-IT, d.velop |
| DATEV-Komponenten | Beauftragung Option DATEV Rechnungswesen (LDconnect), DATEVconnect, Riecken-Gateway beim Hoster; ggf. Beleganzeige Drittanbieter und DUO (OP-04) | Bestellungen, Termin für technische Einrichtung | Livos, Trios, Hoster, d.velop, LIONDEER |
| Lieferanten-App | Datenmodell Konsolidierungsnummer und Kreditor-Mapping je Mandant (AE-09); **KI-PoC Kreditorenkonsolidierung** mit MDIS X.One auf DATEV-Kreditorenexporten | Konsolidierungsvorschlag, Qualitätsbericht Kreditorenstamm | MDIS, Livos (Stammdatenpflege), Trios (Export) |
| Mandantenerkennung vorab | Erkennungstest mit einer Stichprobe echter Livos-Rechnungen, besonders Gesellschaften mit gemeinsamer Anschrift (OP-02, AE-23) | Gemessene Trefferquote, Entscheidung Alias-Postfächer | MDIS, Livos |

Die DATEV-Anbindung hat die längste Vorlaufzeit, weil Hoster, Trios, DATEV-Komponenten und Gateway zusammenkommen müssen. MDIS empfiehlt, sie **in der ersten Woche** von Phase 0 anzustoßen.

### 19.2.3 Phase 1 – MVP Rechnungseingang

| Baustein | Umfang in Phase 1 | Referenz |
|---|---|---|
| Eingangskanäle | Zentrale Rechnungsadresse und Alias je Pilotgesellschaft; Scan; E-Rechnung (ZUGFeRD, XRechnung, Factur-X); **neuer Kommunikationsweg inbound → document reader → smart invoice** von Beginn an, weil d.velop den alten Weg zum 01.01.2027 abschaltet (d.velop invoices Help Center 09/2026) | AE-22, S-14 |
| Workflow | WF-01 mit Verteilung, Sachlicher Prüfung und Kontierung, Fachlicher Freigabe (Freigabematrix), Zahlungsfreigabe, Buchhaltung (Trios) | AE-04, AE-05, AE-06 |
| Klärfälle | WF-04: Mandant unbekannt (Clearing, Klärfall-Mandant), Kreditor fehlt; Dublette mit Begründungspflicht | AE-09, AE-23 |
| Kreditor-Anlage | Übergangsweise: Anlage-Anforderung an Trios per standardisierter E-Mail; automatisiert ab Phase 2 (S-05) | AE-09 |
| DATEV | Buchungsvorschlag und Beleglink ereignisgesteuert; Stammdaten täglich | S-01, S-02, AE-07 |
| Identitäten | Entra ID per SCIM, SSO per OIDC | S-13, AE-18 |
| Stammdaten Gesellschaften/Objekte | Erstbefüllung der Pilotgesellschaften per einmaligem Import; automatische Pflege aus der Lieferanten-App ab Phase 2 (S-04) | AE-28 |
| Rechte und Akten | Restriction Sets je Gesellschaft, Rollengruppen, Aktenplan (Gesellschafts-, Objekt-, Kreditoren-, Vorgangsakte), Aufbewahrung je Kategorie mit Löschsperre | AE-18, AE-19, AE-24 |
| Eskalation und Vertretung | Standardeskalation je Schritt und vor Fälligkeit; Vertretung inkl. Setzen durch Administrator | AE-17 |
| Rückweisung | Übergangslösung: Ablehnen mit Pflichtgrund und manuelles Teilen per E-Mail; automatische Lieferantenmail ab Phase 2 (WF-05) | AE-13 |
| Kürzung | Zahlbetrag mit Kürzungsgrund; Verarbeitung in DATEV mit Trios festgelegt (OP-05) | AE-14 |
| Aufgaben am Dokument | Ad-hoc-Aufgaben und Wiedervorlagen | WF-08 |
| Ereignisprotokoll | Protokollierung jedes Schrittwechsels in die Staging-Schicht ab Pilot-Go-live; Auswertungen in evidanza folgen in Phase 2 | S-12, AE-16 |
| Bau im Pilot | Eine Bau-Gesellschaft läuft über WF-01 **ohne BIM4You-Automatik**: Die Prüfung in BIM4You erfolgt wie heute; das Ergebnis trägt der Prüfer als Zahlbetrag mit Kürzungsgrund ein. | WF-02 (Vorstufe) |
| Lieferantenanschreiben | Schreiben an die Lieferanten der Pilotgesellschaften: exakte Gesellschaftsbezeichnung, Rechnungsadresse bzw. Alias, Käuferreferenz (BT-10) bei E-Rechnungen, bevorzugte Formate | AE-23 |
| Schulung | Key-User-Schulung, rollenbezogene Kurzschulungen für Prüfer und Freigeber (Kap. 18) | – |

### 19.2.4 Phase 2 – Rollout, PM-Freigabe, Rückweisung, Reporting

| Baustein | Umfang | Referenz |
|---|---|---|
| Rollout | Alle Gesellschaften in Wellen; je Welle Stammdaten, Gruppen, Freigabematrix-Zeilen, Alias-Postfach, Lieferantenanschreiben | AE-03, AE-18 |
| PM-Freigabe | Postfach `freigabe-hv@…`, Freigabe durch Asset Management ohne Buchung und Zahlung, Rückmeldung an den Property Manager per E-Mail | WF-03, AE-12, S-11 |
| Rückweisung und Kürzungsmitteilung | Vorlagen-Mail an den Lieferanten mit einem der 5 Standardgründe, Ablage der gesendeten Mail in der Kreditorenakte | WF-05, AE-13, S-11 |
| Lieferanten-App | Konsolidierungsnummer an den Beleg, Gesellschafts- und Objektstamm nach d.velop, Kreditor-Anlage-Anforderung an Trios | S-04, S-05 |
| Reporting | Auswertung der seit Phase 1 protokollierten Schrittwechsel in evidanza (Durchlauf- und Liegezeiten je Schritt und Benutzer) | S-12, AE-16 |
| Export je Gesellschaft | Exportverfahren (BeSync-Skript) für Gesellschaftsverkauf und Betriebsprüfung (Z3), erster Probeexport | S-15, AE-25 |
| Externe Kernpartner | Projektsteuerer und Architekten als Freigabeuser, soweit lizenzrechtlich zulässig (OP-03) | AE-26, R-08 |

Die Protokollierung (S-12) läuft bereits **ab dem Pilot-Go-live in Phase 1**, weil die Plattform die Aufgabenhistorie nur 30 bis 365 Tage hält (AE-16). Später erfasste Daten lassen sich nicht rückwirkend ergänzen.

### 19.2.5 Phase 3 – Bau/BIM4You, Zahlstatus, FSB

| Baustein | Umfang | Referenz |
|---|---|---|
| Bau-Eingangsrechnung | Erkennung Bau, asynchroner Transfer an BIM4You, Rückmeldung von Prüfergebnis, Einbehalt und Freigabestatus, Prüfbericht in der Akte | WF-02, AE-11, S-08, S-09 |
| BIM4You-Stammdaten | Projekte, Vergabeeinheiten, Verträge als Custom Entities | S-10 |
| Zahlstatus | „bezahlt" und Zahldatum aus DATEV-OPOS als DMS-Eigenschaft am archivierten Beleg | S-06, AE-10 |
| Freistellungsbescheinigung | FSB-Status je Kreditor und Gesellschaft, Hinweis bzw. Klärfall bei fehlender oder abgelaufener FSB, Vorschlag Einbehalt 15 % | AE-15 |
| Externe Ad-hoc-Freigabe | Externe Benutzeraufgabe (process studio) mit zeitlich begrenztem Teilen-Link, Kopplung an smart invoice | WF-10, AE-26 |
| Optional | Monatliche PM-Buchungsdaten ins BI für Vollständigkeits- und Kreditorenabgleich; Option frühe DATEV-Übergabe mit Postensperre, falls ED-01 so entschieden | S-16, AE-08 |

### 19.2.6 Phase 4 – Verträge, Post, DMS-Ausbau

| Baustein | Umfang | Referenz |
|---|---|---|
| Verträge | d.velop contracts mit Vertragsakte, Fristen, Hierarchien; fachliche Vertragsfreigabe; Migration aktiver Verträge (Kap. 19.4) | WF-06, AE-20 |
| Post | Scan (intern oder Dienstleister), E-Mail-Funktionspostfächer, KI-Trennung und -Klassifizierung, Verteilung über mail dispatcher, Umleitung von Rechnungen in WF-01 und von Verträgen in contracts | WF-07, AE-21 |
| DMS-Ausbau | Weitere Kategorien und Akten, Outlook-Integration, d.velop mobile, gespeicherte Suchen je Rolle | Kap. 12 |
| KI an Verträgen | d.velop pilot für Fragen an Vertragsinhalte (z. B. „Ist Skonto vereinbart?"); Tokengrenze vorher im PoC prüfen (OP-19) | AE-20, AE-27 |

### 19.2.7 Phase 5 – Optimierung

| Paket (Beispiele) | Inhalt | Referenz |
|---|---|---|
| KI-Auswertung | Trefferquote der KI-Kontierungsvorschläge messen und Kontierungsvorlagen nachschärfen | AE-27 |
| Freigaben ohne Rechnung | z. B. Ausbuchungen auf Mietkonten | WF-09 |
| ERP-/PM-Anbindung | Stammdatensynchronisation mit PM-Systemen über die d.velop-REST-API | S-17 |
| Vorschau-Features | Vier-Augen ab Betrag X aus dem Standard übernehmen, sobald d.velop es freigibt (OP-09) | AE-05 |
| MDIS X.One | Übergreifende Analysen über BeSync-Daten (Lieferanten, Durchlaufzeiten, Kürzungen) | AE-27 |

## 19.3 Kriterien für Pilotgesellschaften

Der Pilot soll die kritischen Fälle unter Echtbedingungen zeigen, aber überschaubar bleiben. MDIS empfiehlt **3–5 Gesellschaften**. Livos wählt sie in Phase 0 nach den folgenden Kriterien aus.

| Nr. | Kriterium | Warum | Pflicht / Soll |
|---|---|---|---|
| PK-1 | Mindestens eine Gesellschaft mit **nennenswertem Rechnungsvolumen** im Bestandssegment, eigenverwaltet | Belastbare Kennzahlen, Routine im Workflow | Pflicht |
| PK-2 | Mindestens ein **Paar von Gesellschaften mit gemeinsamer Anschrift** | Härtetest der Mandantenerkennung über Name und Anschrift (AE-23) | Pflicht |
| PK-3 | Eine **Bau-Gesellschaft** mit Abschlagsrechnungen und § 13b-Fällen, **ohne BIM4You-Automatik** | Prüft Belegart, Reverse Charge, Zahlbetrag und Kürzung; bereitet WF-02 vor | Pflicht |
| PK-4 | Gesellschaften mit unterschiedlichen Freigabegrenzen oder Freigebern | Prüft die Freigabematrix mit Spalte Mandant (AE-05) | Soll |
| PK-5 | Alle Pilotgesellschaften sind DATEV-Mandanten auf dem über das Gateway erreichbaren DATEV-System | DATEV-Übergabe und Stammdatensync ohne Sonderwege | Pflicht |
| PK-6 | Engagierte Key-User und Freigeber, die im Pilotzeitraum verfügbar sind (kein Urlaubsschwerpunkt, kein Jahresabschluss) | Schnelle Rückmeldung, Akzeptanz | Pflicht |
| PK-7 | Keine Gesellschaft mit laufendem Verkauf oder Umstrukturierung | Stabile Stammdaten, kein Exportdruck im Pilot | Soll |
| PK-8 | Möglichst ein Kreditor, der mehrere Pilotgesellschaften beliefert | Prüft Kreditor-Mapping je Mandant und Konsolidierungsnummer (AE-09) | Soll |
| PK-9 | Keine PM-verwalteten Objekte als Schwerpunkt | WF-03 folgt in Phase 2; PM-Rechnungen im Pilot vermeiden | Soll |

In der Demo-Instanz bildeten die fiktiven Gesellschaften NORD und BAUP das Anschriftspaar (PK-2), SUED die Gesellschaft mit Abschlagsrechnungen und § 13b (PK-3). Die Pilotauswahl erfolgt aber ausschließlich mit echten Livos-Gesellschaften.

**Pilotdauer und Abschluss (Vorschlag):** mindestens 4 Wochen produktiver Betrieb und ein vollständiger Zahllauf-Zyklus in DATEV und multicash. Der Pilot endet mit QG-1b und den Abnahmekriterien in Kap. 19.5.3.

## 19.4 Migration und Altdaten

### 19.4.1 Offene Rechnungen im Umlauf zum Stichtag

Zum Go-live einer Gesellschaft gibt es Rechnungen, die im bisherigen Verfahren noch nicht abgeschlossen sind. Für sie gilt ein **Stichtag je Gesellschaft bzw. Welle**. Wichtigste Regel: Eine Rechnung darf **nie doppelt nach DATEV** übergeben werden (P4).

| Option | Beschreibung | Vorteile | Nachteile |
|---|---|---|---|
| A – Auslaufen | Alle vor dem Stichtag eingegangenen Rechnungen laufen im alten Verfahren zu Ende. Nur neue Eingänge laufen in d.velop. | Kein Risiko der Doppelübergabe; einfach | Zwei Verfahren parallel für einige Wochen; keine vollständige Transparenz im REB |
| B – Vollständig nachschleusen | Alle offenen Rechnungen werden in d.velop importiert und durchlaufen WF-01 vollständig. | Volle Transparenz ab Stichtag | Doppelte Arbeit bei bereits geprüften Rechnungen; Risiko Doppelübergabe bei bereits gebuchten Belegen |
| **C – Hybrid (Empfehlung)** | Rechnungen **ohne** fachliche Freigabe zum Stichtag werden in d.velop importiert und laufen WF-01. Rechnungen **mit** Freigabe oder bereits in DATEV gebucht laufen im alten Verfahren zu Ende. Ihre Belege werden nach Abschluss ins Archiv übernommen, als Altbeleg gekennzeichnet und **ohne DATEV-Übergabe** abgelegt. | Keine Doppelarbeit, keine Doppelübergabe; Archiv vollständig | Klare Stichtagsliste nötig; Kennzeichnung „Altbeleg" konfigurieren [K, O: Umsetzung am Workflowende im Test prüfen] |

**Vorgehen bei Option C (Vorschlag):**

| Schritt | Zeitpunkt | Verantwortlich |
|---|---|---|
| Stichtagsliste offener Rechnungen je Gesellschaft (Kreditor, Rechnungsnummer, Betrag, Status) erstellen | 1 Woche vor Stichtag | Livos Buchhaltung, Trios |
| Postfach und Scanweg auf d.velop umstellen, altes Postfach mit Weiterleitung versehen | Stichtag | Livos-IT, MDIS |
| Nicht freigegebene Rechnungen in d.velop importieren; die Duplikatsprüfung (Zeitfenster 18 Monate) zeigt Doppeleingänge an | Stichtag bis +5 Arbeitstage | Livos Rechnungseingang (R-02) |
| Abgleich Stichtagsliste gegen REB und DATEV | +10 Arbeitstage | Livos Buchhaltung, Trios |
| Altbelege nach Abschluss ins Archiv übernehmen (Kategorie Eingangsrechnung, Kennzeichen Altbeleg) | laufend bis Abschluss | Livos, MDIS |

### 19.4.2 Altbestand Verträge

Für Verträge (Phase 4) gibt es drei Optionen. Die Entscheidung trifft Livos in Phase 3 (ED-16, Kap. 20.2).

| Option | Beschreibung | Aufwand | Empfehlung |
|---|---|---|---|
| V1 – Aktive Verträge mit Metadaten | Alle laufenden Verträge werden gescannt bzw. importiert und in d.velop contracts mit Vertragspartner, Beginn, Ende, Kündigungsfrist und Verlängerung erfasst. Beendete Verträge bleiben im Altbestand. | mittel | **Empfohlen**: Fristenüberwachung wirkt sofort für alle relevanten Verträge |
| V2 – Vollmigration | Aktive und beendete Verträge werden migriert, beendete nur mit Grundmetadaten. | hoch | nur bei konkretem Bedarf (z. B. Gewährleistung, Verkauf) |
| V3 – Anlassbezogen | Verträge werden erst bei Bedarf (Nachtrag, Kündigung, Prüfung) erfasst. | gering | nicht empfohlen: Fristen bleiben lückenhaft |

Für V1 schlägt MDIS eine Priorisierung vor: zuerst Verträge mit Kündigungsfristen in den nächsten 12 Monaten, dann Rahmen- und Bauverträge, dann den Rest. Die Metadaten können KI-gestützt vorbelegt werden (d.velop pilot bzw. document reader). Eine Person prüft jeden Datensatz (P7).

### 19.4.3 Weitere Altdaten

| Datenbestand | Vorgehen (Vorschlag) | Offen |
|---|---|---|
| Gesellschaften und Objekte | Erstbefüllung aus dem Stamm der Lieferanten-App bzw. einer Livos-Liste; Schreibweise exakt wie auf Rechnungen, UTF-8 | Liste DATEV-Mandanten mit Berater- und Mandantennummer (OP-21) |
| Kreditoren | Kein manueller Import: LDconnect liefert den DATEV-Kreditorenstamm je Mandant (S-02); Konsolidierungsnummern aus dem KI-PoC | Mengengerüst je Mandant (OP-21) |
| Archivierte Rechnungen früherer Jahre | Verbleiben im bisherigen Ablageort, solange die Aufbewahrungsfrist läuft; Übernahme nur auf Wunsch, als eigenes Paket | Bestehendes Archiv/DMS bei Livos (OP-37) |
| Sonstige Dokumente (Post, Akten) | Keine Pauschalmigration; Übernahme je Aktenart nach Livos-Vorgabe in Phase 4 | Aktenstruktur (OP-17) |

Große Dateien lädt MDIS in Paketen über die DMS-API. Die API begrenzt den Upload auf 100 MB je Anfrage (empfohlen 25 MB).

## 19.5 Test- und Abnahmekonzept

### 19.5.1 Testarten

| Testart | Ziel | Umgebung | Durchführung | Phase |
|---|---|---|---|---|
| Plattformtest | Annahmen zur Cloud-Plattform bestätigen (Rechte, Aktenbildung, Aufbewahrung, Identitäten) | Test-Tenant | MDIS | 0 |
| Konfigurationstest | Jede Konfiguration (Kategorie, Eigenschaft, Workflowschritt, Freigabematrix, Eskalation) einzeln prüfen | Test-Tenant | MDIS | je Zyklus |
| Schnittstellentest | S-xx mit Testdaten und Fehlerfällen (Zeitüberschreitung, fehlender Stammsatz, doppelte Übergabe) | Test-Tenant + DATEV-Testmandant | MDIS, Trios, LIONDEER | 1–4 |
| Berechtigungstest | Sichtbarkeit je Rolle und Gesellschaft positiv und negativ prüfen | Test-Tenant | MDIS, Livos Key-User | 1, 2 |
| Erkennungstest | Trefferquote Mandant, Kreditor und Pflichtfelder mit **echten, anonymisierten Livos-Belegen** messen | Test-Tenant | MDIS, Livos | 0, 1 |
| End-to-End-Fachtest | Beleg vom Eingang bis „bezahlt" mit allen Rollen | Test-Tenant | Livos Key-User, Trios | 1–4 |
| Abnahmetest (UAT) | Abnahme der Phase anhand des Testfallkatalogs | Test-Tenant | Livos | je Phase |
| Regressionstest | Kerntestfälle nach d.velop-Releases und nach BeSync-Änderungen | Test-Tenant | MDIS | Betrieb |

### 19.5.2 Testfälle

Grundlage sind die Testdaten der Demo-Instanz. Sie sind fiktiv, bilden aber typische Livos-Fälle ab. Vor dem Abnahmetest ersetzt Livos sie durch echte Belege, jeweils mindestens drei je Fall (Vorschlag). Die Beleg-Nummern verweisen auf das Demo-Testset.

| TF | Testfall | Demo-Beleg (Beispiel) | Erwartetes Ergebnis | Referenz |
|---|---|---|---|---|
| TF-01 | Standardrechnung unter Freigabegrenze | Beleg 02 (1.190 € brutto) | Einstufige Freigabe, Zahlungsfreigabe, Buchungsvorschlag in DATEV mit Beleglink | WF-01, S-01 |
| TF-02 | Rechnung über Freigabegrenze | Beleg 01 (12.400 € netto) | Zweite Freigabestufe über Wertgrenzen-Verbindung auf Nettobetrag; Prüfer ≠ Freigeber | AE-05 |
| TF-03 | **Gleiche Anschrift** zweier Gesellschaften | Beleg 04 (Empfänger mit Anschrift einer anderen Gesellschaft) | Richtiger Mandant über Namen oder Alias-Vorbelegung; sonst Klärfall, kein falscher Mandant | AE-23, WF-04 |
| TF-04 | **Unbekannte Gesellschaft** | Beleg 08 (Gesellschaft nicht angelegt) | Klärfall-Mandant, Zuordnung durch R-02, Protokoll | WF-04 |
| TF-05 | Kreditor fehlt | neuer Lieferant | Klärfall „Kreditor fehlt", Anlage-Anforderung an Trios, Weiterlauf nach Sync am Folgetag | WF-04, S-05 |
| TF-06 | **§ 13b Reverse Charge** | Beleg 06 (USt 0, Hinweis Steuerschuldnerschaft) | Kennzeichen Reverse Charge = Ja; passender Steuerschlüssel im Buchungsvorschlag; Hinweis, wenn der Empfänger nicht als Bauleistender gekennzeichnet ist | E-20, AE-28 |
| TF-07 | **Abschlagsrechnung kumuliert** | Beleg 07 (2. Abschlag, kumuliert, mit Sicherheitseinbehalt) | Belegart Abschlag; Verknüpfung mit Auftrag in der Vorgangsakte; frühere Abschläge sichtbar; ab Phase 3 Prüfung in BIM4You | E-14, E-19, WF-02 |
| TF-08 | **Kürzung** positionsweise | Beleg 01 (eine Position kürzen) | Zahlbetrag < Brutto, Kürzungsgrund Pflicht, Original unverändert, Protokoll; DATEV-Verarbeitung wie mit Trios vereinbart | AE-14, OP-05 |
| TF-09 | **Dublette** über zwei Kanäle | Beleg 09 bzw. 10 (gleiche Rechnung wie 02 bzw. 01) | Duplikatswarnung; Ablehnung ohne Lieferantenmail oder Annahme nur mit Begründung | T-27 |
| TF-10 | **XRechnung** | Beleg 09 (UBL, XRechnung 3.0) | Import, Visualisierung, Validierungsbericht, XML als Original archiviert | Katalog 2.4 |
| TF-11 | **ZUGFeRD / Factur-X** | Beleg 10 (EN16931, kein PDF/A-3, eine Sammelposition) | Import; Abweichung XML ↔ PDF sichtbar; Profilprüfung gemäß Lösung zu OP-41 (Kap. 20.3), Test T37 | Katalog 2.4, RI-13 |
| TF-12 | IBAN-Abweichung | Beleg 09/10 (IBAN weicht vom Stamm ab) | Hinweis an Prüfer; keine stille Übernahme | T-16, T25 |
| TF-13 | Kostenstellensplit | Beleg 03 (55 % / 45 %) | Aufteilung über Positionen bzw. Kontierungsvorlage | Katalog 2.8, T27 |
| TF-14 | Skonto und Eskalation | Beleg 01 (2 % Skonto) | Dynamische Eskalation vor Skontoablauf, Eskalationsbenachrichtigung | AE-17, T26 |
| TF-15 | Rückweisung an Lieferanten | beliebiger Beleg | Pflichtgrund, Vorlagen-Mail an Kreditoren-Adresse, Mail in Kreditorenakte | WF-05 |
| TF-16 | Vertretung bei Krankheit | Freigabeaufgabe | Administrator setzt Abwesenheit, Vertreter sieht persönlich zugestellte Aufgaben | AE-17 |
| TF-17 | Mandantentrennung | Benutzer einer Gesellschaft | Keine Sicht auf Belege anderer Gesellschaften in Suche, Akte und REB | AE-18, T02 |
| TF-18 | PM-Freigabe | Rechnung eines Property Managers | Freigabe ohne Buchung und Zahlung, Rückmeldemail an PM | WF-03 |
| TF-19 | Zahlstatus | gebuchte und bezahlte Rechnung | „bezahlt" und Zahldatum am Beleg am Folgetag | S-06 |
| TF-20 | Export je Gesellschaft | Testgesellschaft | Originale und Metadaten vollständig, keine fremden Dokumente | S-15 |

Die Demo-Testdaten enthalten bewusste und unbeabsichtigte Unstimmigkeiten, zum Beispiel ungültige IBANs in den E-Rechnungen und einen Sicherheitseinbehalt, der zu keiner Bemessungsgrundlage passt. Sie eignen sich deshalb gut als Negativtests für IBAN-Prüfung und BIM4You-Abgleich.

### 19.5.3 Abnahmekriterien

| Kriterium | Messgröße | Zielwert (Vorschlag) |
|---|---|---|
| Funktionsumfang | Alle Testfälle der Phase bestanden | 100 % der Pflichttestfälle |
| Fehlerfreiheit | Offene Fehler nach Fehlerklasse | 0 × Klasse 1 (Blocker), 0 × Klasse 2 (wesentlich); Klasse 3 mit Termin |
| Mandantenerkennung | Anteil der Belege mit korrektem Mandanten ohne manuellen Eingriff | Zielwert mit Livos nach Erkennungstest in Phase 0 festlegen; **0 Belege mit falschem Mandanten** ohne Klärfall |
| DATEV-Übergabe | Übergebene Buchungsvorschläge ohne Fehler bzw. Doppelübergabe | 100 % korrekt, 0 Doppelübergaben |
| Rechte | Positiv- und Negativtests je Rolle und Gesellschaft | 100 % bestanden |
| Durchlauf | Belege im Pilot, die ohne Workaround durchlaufen | ≥ 95 % |
| Dokumentation | As-built-Protokoll, Rollen- und Berechtigungsmatrix, Betriebshandbuch-Beitrag | vollständig |
| Schulung | Geschulte Anwender je Rolle | 100 % der Pilotanwender |

**Fehlerklassen:** Klasse 1 verhindert den Betrieb oder gefährdet Buchung, Zahlung oder Rechtetrennung. Klasse 2 beeinträchtigt einen Kernprozess, ein Workaround existiert. Klasse 3 betrifft Komfort oder Darstellung.

## 19.6 Go-live und Hypercare

### 19.6.1 Go-live-Checkliste (Vorschlag)

| Nr. | Punkt | Verantwortlich |
|---|---|---|
| GL-1 | Abnahmetest bestanden, Abnahmeprotokoll unterschrieben | Livos |
| GL-2 | Konfiguration vom Test- in den Produktiv-Tenant übertragen und gegen As-built geprüft | MDIS |
| GL-3 | Stammdaten der Gesellschaften der Welle vollständig (Mandanten-ID, Name exakt, Anschrift, Freigabematrix, Gruppen) | Livos, MDIS |
| GL-4 | DATEV-Stammdatensync gelaufen, Probe-Übergabe an einen DATEV-Testmandanten erfolgreich | MDIS, Trios |
| GL-5 | Postfächer und Aliasse aktiv, Mailimport getestet, Graph-Berechtigung auf die Postfächer eingeschränkt | Livos-IT, MDIS |
| GL-6 | Anwender angelegt (SCIM), Rollen zugeordnet, Vertretungen hinterlegt | Livos-IT, R-12 |
| GL-7 | Schulungen durchgeführt, Kurzanleitungen verteilt | MDIS, Key-User |
| GL-8 | Lieferantenanschreiben versendet (mindestens 2 Wochen vor Stichtag, Vorschlag) | Livos |
| GL-9 | Stichtagsliste offener Rechnungen erstellt (Kap. 19.4.1) | Livos, Trios |
| GL-10 | Supportweg und Eskalation (MDIS, d.velop) kommuniziert, BeSync-Monitoring aktiv | MDIS |
| GL-11 | Rückfallplan abgestimmt: Rechnungen können übergangsweise im alten Verfahren bearbeitet werden, Postfach-Weiterleitung umkehrbar | Livos, MDIS |

**Zeitpunkt:** MDIS empfiehlt, Go-live-Termine nicht in die letzten zwei Wochen eines Monats und nicht in die Jahresabschlussphase zu legen. Trios braucht dann stabile Abläufe für Monatsabschluss und Rückstellungen.

### 19.6.2 Hypercare

| Element | Ausgestaltung (Vorschlag) |
|---|---|
| Dauer | 4 Wochen nach jedem Go-live (Pilot und jede Rollout-Welle); 2 Wochen für kleinere Folgewellen |
| Tägliche Abstimmung | 15 Minuten in den ersten zwei Wochen: Klärfälle, Fehler, Rückfragen der Anwender |
| Beobachtete Kennzahlen | Anteil Klärfälle Mandant/Kreditor, Erkennungsquote, Belege je Schritt mit Alter > 3 Tage, DATEV-Übergabefehler, Mailimport-Rückstände, BeSync-Fehler |
| Vor-Ort- oder Remote-Begleitung | Key-User-Sprechstunde, Floor-Support für Rechnungseingang und Freigeber in den ersten Tagen |
| Nachsteuerung | Schnelle Anpassungen an Freigabematrix, Eskalationsfristen, Kontierungsvorlagen und Erkennung nach Change-Verfahren (Kap. 18) |
| Abschluss | Hypercare-Bericht, Übergabe in den Regelbetrieb und Support (Kap. 18) |

## 19.7 Projektorganisation

### 19.7.1 Rollen

| Organisation | Rolle | Aufgaben |
|---|---|---|
| Livos | Auftraggeber / Sponsor (Geschäftsführung) | Budget, Grundsatzentscheidungen, Vorsitz Lenkungsausschuss |
| Livos | Projektleitung (André Töpper) | Steuerung auf Kundenseite, Entscheidungsvorlagen, Abnahmen, Ressourcen |
| Livos | Key-User je Bereich (Rechnungseingang, Asset Management, Controlling, Bau, Verträge, Poststelle) | Fachanforderungen, Tests, Schulung der Kollegen, Ansprechpartner im Betrieb |
| Livos | Fachadministration (R-12) | Pflege Lieferanten-App, Freigabematrix, Gruppen, Vertretungen |
| Livos | IT | M365, Entra ID, Postfächer, Scan-Infrastruktur, Sicherheitsfreigaben |
| Livos | Datenschutz, Steuerberatung | AVV, Aufbewahrungsfristen, Verfahrensdokumentation |
| MDIS | Projektleitung | Gesamtplanung, Qualitätstore, Risiko- und Änderungsmanagement |
| MDIS | Lösungsarchitekt d.velop | Konfiguration smart invoice, documents, contracts, Rechte, Akten |
| MDIS | BeSync-Entwicklung und -Betrieb | Schnittstellen S-04 bis S-17, Lieferanten-App, Monitoring |
| MDIS | BI-Beratung | Staging-Schicht und evidanza-Auswertungen |
| MDIS | Schulung / Change | Schulungskonzept, Kurzanleitungen, Kommunikation |
| Trios | Buchhaltungsdienstleister | DATEV-Übergabe, Kreditorenanlage, Buchungslogik, Tests, Verarbeitung Zahlbetrag |
| DATEV-Hoster | Betreiber der DATEV-Umgebung | Freigabe und Betrieb von DATEVconnect und Riecken-Gateway |
| d.velop | Hersteller | Tenants, Lizenzen, Support, Klärung Produktfragen (Kap. 20.3) |
| LIONDEER | Hersteller LDconnect | Einrichtung und Support der DATEV-Schnittstelle |
| BIB GmbH | Hersteller BIM4You | Schnittstellenformate, Import und Export (Phase 3) |
| Omikron | Hersteller multicash | Importprofil für SEPA-Dateien (bei Bedarf) |

### 19.7.2 Gremien

| Gremium | Teilnehmer | Rhythmus (Vorschlag) | Aufgaben |
|---|---|---|---|
| Lenkungsausschuss | Livos GF (Vorsitz), Livos Projektleitung, MDIS Geschäftsleitung und Projektleitung; Trios bei Bedarf | monatlich und an jedem Qualitätstor | Entscheidungen ED, Abnahmen der Qualitätstore, Budget, Eskalation |
| Projektteam (Jour fixe) | Projektleitungen Livos und MDIS, Key-User nach Thema | wöchentlich | Fortschritt, Risiken, offene Punkte, Planung der Zyklen |
| Fach-Arbeitsgruppen | Key-User, MDIS-Berater, Trios | nach Bedarf in Phase 0–4 | Detailkonzept, Tests |
| Schnittstellenrunde | MDIS, Trios, Hoster, LIONDEER, bei Bau BIB GmbH | 14-täglich in Phase 0–3 | DATEV-, BIM4You- und Zahlungsflüsse |
| Change-Board | Fachadministration Livos, MDIS | ab Go-live monatlich | Änderungswünsche, Release-Themen, Priorisierung |

## 19.8 Grobe Zeitleiste

Die Zeitleiste ist ein **Vorschlag**. Monat 1 (M1) beginnt mit der Beauftragung. Die tatsächliche Planung hängt vor allem von der Bereitstellung der DATEV-Anbindung beim Hoster, von den Entscheidungen in Phase 0 und von der Verfügbarkeit der Livos-Key-User ab.

| Phase / Meilenstein | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 | M10 | M11 | M12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Phase 0 Klärung & Setup | ■ | ■ | | | | | | | | | | |
| DATEV-Komponenten und Gateway bereitstellen | ■ | ■ | ■ | | | | | | | | | |
| Phase 1 Aufbau MVP | | ■ | ■ | ■ | | | | | | | | |
| Pilotbetrieb (QG-1b) | | | | ■ | ■ | | | | | | | |
| Phase 2 Rollout, WF-03, WF-05, Reporting | | | | | ■ | ■ | ■ | | | | | |
| Phase 3 Bau/BIM4You, Zahlstatus, FSB | | | | | | | ■ | ■ | ■ | ■ | | |
| Phase 4 Verträge und Post | | | | | | | | | ■ | ■ | ■ | |
| Phase 5 Optimierung | | | | | | | | | | | ■ | ■ |

| Meilenstein | Monat (Vorschlag) |
|---|---|
| QG-0 Feinkonzept und Entscheidungen | Ende M2 |
| Pilot-Go-live (QG-1a) | Anfang M4 |
| Freigabe Rollout (QG-1b) | Ende M4 / Anfang M5 |
| Alle Gesellschaften produktiv (QG-2) | Ende M7 |
| Bau-Prozess mit BIM4You produktiv (QG-3) | Ende M10 |
| Verträge und Post produktiv (QG-4) | Ende M11 |

Beginnt das Projekt im vierten Quartal 2026, fällt der Pilot-Go-live in das erste Quartal 2027. Dann liegt der Jahresabschluss 2026 in der Aufbauphase. MDIS empfiehlt, den Pilotstart mit Trios so zu legen, dass Jahresabschlussarbeiten und Pilot sich möglichst wenig überschneiden.

# 20 Risiken, Entscheidungsbedarfe und offene Punkte

Dieses Kapitel fasst zusammen, was vor und während der Einführung zu klären, zu entscheiden oder zu testen ist. Es besteht aus vier Teilen: Risikoregister (20.1), Entscheidungsbedarfe für Livos (20.2), offene Punkte mit Klärungsweg (20.3) und Testplan für die Plattform (20.4). Das Projektteam führt alle Listen im Jour fixe fort (Kap. 19.7).

## 20.1 Risikoregister

**Bewertung:** W = Eintrittswahrscheinlichkeit, A = Auswirkung, jeweils **h** (hoch), **m** (mittel), **g** (gering). Die Bewertung ist eine Einschätzung von MDIS zum Konzeptstand 09/2026 und wird an jedem Qualitätstor aktualisiert.

| ID | Risiko | Ursache | Folge | W | A | Maßnahme | Verantwortlich |
|---|---|---|---|---|---|---|---|
| RI-01 | Mandantenerkennung ordnet Rechnungen falsch oder gar nicht zu | smart invoice erkennt den Empfänger über Name und Anschrift; viele Livos-Gesellschaften teilen eine Verwaltungsanschrift (AE-23) | Manueller Aufwand je Beleg, Fehlbuchung im falschen DATEV-Mandanten | h | h | Maßnahmenbündel AE-23: Lieferantenanschreiben, Alias-Postfach je Gesellschaft, Mandantenname exakt wie auf Rechnungen, Käuferreferenz (BT-10), Klärfall; Erkennungstest mit echten Belegen in Phase 0 (T28–T30); Pilot mit Anschriftspaar | MDIS, Livos |
| RI-02 | DATEV-Anbindung beim Hoster verzögert sich oder ist nicht möglich | DATEV läuft bei einem externen Hoster; LDconnect braucht DATEVconnect und das Riecken-Datengateway; Betreiber und Lizenznehmer sind ungeklärt (OP-04) | Kein produktiver Rechnungsfluss nach DATEV; Verschiebung von Phase 1 | m | h | Beauftragung in Woche 1 von Phase 0; Schnittstellenrunde mit Hoster, Trios und LIONDEER; Rückfall: Buchungsvorschläge vorübergehend per Export an Trios [O] | Livos, MDIS |
| RI-03 | Neue Kreditoren stehen erst am Folgetag zur Verfügung | LDconnect synchronisiert DATEV-Stammdaten täglich (AE-07); Kreditoren legt nur Trios in DATEV an | Rechnungen neuer Lieferanten liegen mindestens einen Tag im Klärfall; Skontoverlust möglich | h | m | Klärfall „Kreditor fehlt" mit Frist; Anlage-Anforderung aus der Lieferanten-App (S-05); Servicezeit mit Trios vereinbaren; untertägigen Sync bei LIONDEER klären (OP-22) | Trios, MDIS |
| RI-04 | Dritte dürfen lizenzrechtlich nicht als Freigabe- oder Buchhaltungsuser arbeiten | Nutzungsbedingungen für externe Personen (Trios, Projektsteuerer, PM) nicht eindeutig (OP-03) | Höhere Lizenzkosten oder anderer Weg für Externe | m | m | Schriftliche Bestätigung durch d.velop in Phase 0; Alternative externe Benutzeraufgabe (WF-10) | MDIS, d.velop |
| RI-05 | BIM4You lässt sich nicht wie geplant anbinden | Keine veröffentlichte API; Anbindung nur über Import, Austauschordner oder Datenbank (AE-11) | WF-02 nur teilautomatisiert; Doppelerfassung im Bau | h | m | Frühe Klärung mit BIB GmbH (OP-06, OP-42); datei- und importbasierter Entwurf; Pilot-Bau ohne Automatik in Phase 1 | MDIS, Livos |
| RI-06 | Kein Schreib-Rückkanal in laufende smart-invoice-Belege | Schreibzugriff per API auf laufende Belege (z. B. Zahlbetrag nach BIM4You) ist nicht belegt (OP-07) | BIM4You-Ergebnis muss manuell als Zahlbetrag übernommen werden | h | m | Anfrage bei d.velop; Ergebnis als DMS-Eigenschaft und Prüfbericht am Beleg, Übernahme durch den Prüfer mit Pflichtfeld; Test T34 | MDIS, d.velop |
| RI-07 | Service-Limits des smart-invoice-Buckets werden erreicht | Kreditoren und Sachkonten werden je Mandant angelegt; Limit 100.000 Kreditoren, 1.000 Mandanten, 50.000 Sachkonten je Bucket (AE-03); Rechenbeispiel 110 Mandanten × 500 Sachkonten = 55.000 (Kapitel 6.6) | Stammdatensync bricht ab, neue Gesellschaften nicht anlegbar | m | h | Mengengerüst je Mandant ermitteln (OP-21); nur genutzte Konten übertragen bzw. Sachkonten ohne Mandantenbezug (OP-22); Erhöhung vertraglich vereinbaren; mehrere Buckets nur als letzte Option (OP-04) | MDIS, Trios |
| RI-08 | Kontingent für process-studio-Ausführungen reicht nicht | Edition business enthält 1.000 Ausführungen je Monat; unklar, ob smart invoice mitzählt (OP-11) | Zusatzkosten oder Einschränkung bei WF-06, WF-09, WF-10 | m | m | Klärung mit d.velop; Mengenschätzung je Prozess; Rechnungsworkflows in smart invoice (AE-04) | MDIS |
| RI-09 | Vorschau-Features sind nicht verfügbar oder ändern sich | Vier-Augen ab Betrag und mehrere Buckets sind Vorschau-Funktionen (OP-09) | Konzept verliert Funktion | m | m | Nur Standardwege einplanen (Wertgrenzen-Verbindung, ein Bucket); Vorschau-Features erst nach Freigabe (Phase 5) | MDIS |
| RI-10 | Property Manager nutzen den Freigabeweg nicht | PM dürfen nicht zu einem System verpflichtet werden (K.-o.-Randbedingung) | Freigaben laufen weiter außerhalb, Transparenz fehlt | m | m | Reiner E-Mail-Kanal ohne Konto (WF-03); Information der PM durch Livos Asset Management; monatlicher Vollständigkeitsabgleich optional (S-16) | Livos Asset Management |
| RI-11 | Livos lehnt Middleware-Anteile ab | Livos ist bei Middleware-Eigenbau vorsichtig und will keine technischen Tabellen pflegen (P3) | Anforderungen mit [A] bleiben offen | m | h | BeSync nur, wo der Standard endet; jede Leistung im Schnittstellenkatalog mit Zweck und Betrieb durch MDIS; fachliche Pflege nur in der Lieferanten-App | MDIS |
| RI-12 | Schlechte Datenqualität im Kreditorenstamm | Gleiche Lieferanten mit verschiedenen Nummern je Gesellschaft, 70000er und 80000er-Kreise ohne Konsolidierung, abweichende Schreibweisen | Falsche Kreditorenerkennung, fehlerhafte Lieferantensicht | h | m | KI-PoC Konsolidierung in Phase 0; Mapping in der Lieferanten-App; Schreibweisen-Regeln (UTF-8, eine führende Quelle) | MDIS, Livos, Trios |
| RI-13 | Fehlerhafte ZUGFeRD-Rechnungen werden nicht erkannt | d.velop validiert nur XRechnung; ZUGFeRD-Profile MINIMUM und BASIC-WL gelten nicht als E-Rechnung | Vorsteuerrisiko, unzulässige Rechnungen im Umlauf | m | m | Profilprüfung ergänzen (OP-41, Test T37); Rückweisungsgrund „formaler E-Rechnungsfehler" | MDIS |
| RI-14 | Aufbewahrung und Löschung arbeiten nicht wie gefordert | Automatische Löschung nach Frist; Legal Hold und Ablaufhemmung nicht dokumentiert (OP-15); Aktivitätenprotokoll mit unklarer Dauer (OP-32) | Vorzeitige Löschung, Nachweislücke bei Prüfung | g | h | Automatisches Löschen zunächst aus, jährlicher freigegebener Löschlauf (AE-24); Test T17/T18; Fristen mit Steuerberatung | MDIS, Livos |
| RI-15 | Abhängigkeit von Trios | Trios bucht, legt Kreditoren an und verarbeitet Zahlbetrag und Zahlungsvorschlag | Engpass bei Tests, Kreditoranlage und Go-live | m | h | Trios von Phase 0 an im Projektteam; Servicezeiten vereinbaren; Schnittstellenrunde | Livos |
| RI-16 | Geringe Akzeptanz oder unzureichende Schulung | ~80 Anwender intern und extern, wechselnde Rollen, neue Arbeitsweise (Aufgabenliste statt E-Mail) | Liegezeiten, Umgehungswege | m | m | Rollenbezogene Kurzschulungen, Key-User, Hypercare, abschaltbare E-Mail-Benachrichtigung (Kap. 18, 19.6) | MDIS, Livos |
| RI-17 | Mandantentrennung in den Rechten greift nicht wie geplant | Kernannahme: Restriction Set zieht Werte aus allen Gruppen eines Benutzers (AE-18) | Sicht auf fremde Gesellschaften oder zu restriktive Rechte | m | h | Tests T02–T09 in Phase 0; Negativtests vor jedem Go-live | MDIS |
| RI-18 | Gekürzter Zahlbetrag wird in DATEV nicht berücksichtigt | LDconnect überträgt den Bruttobetrag (AE-14, OP-05) | Überzahlung im Zahllauf | m | h | Verfahren mit Trios festlegen (z. B. Differenzbuchung oder Zahlungsvorschlag anpassen); Test T24; bis dahin Kürzungsgrund im Buchungstext | Trios, MDIS |
| RI-19 | Prozesshistorie für Reporting geht verloren | Aufgabenhistorie wird nur 30–365 Tage gehalten (AE-16) | Keine historischen Durchlaufzeiten | m | m | S-12-Protokollierung ab Pilot-Go-live (Phase 1); laufender Abzug in die Staging-Schicht | MDIS |
| RI-20 | Mailimport nicht nutzbar oder zu weit berechtigt | email import produktiv nur mit M365/Graph; Graph-Berechtigung wirkt ohne Einschränkung auf jedes Postfach (OP-16, OP-36) | Kein automatischer Eingang; Sicherheitsbedenken | g | h | M365 und Entra ID in Phase 0 bestätigen; Berechtigung per Richtlinie auf die Rechnungspostfächer beschränken | Livos-IT |
| RI-21 | Cloud-Releases ändern Verhalten oder schalten Wege ab | d.velop entwickelt die Cloud laufend weiter; Beispiel: alter Kommunikationsweg in d.velop invoices endet am 01.01.2027 | Nacharbeit, Störungen | m | m | Neuen Kommunikationsweg von Beginn an; Release Notes beobachten; Regressionstests (Kap. 19.5) | MDIS |
| RI-22 | Vertretung erreicht nicht alle Aufgaben | Vertreter sehen nur Aufgaben, die dem Abwesenden persönlich zugestellt sind (AE-17) | Liegezeiten bei Krankheit | m | m | Aufgaben an Personen oder Gruppen mit mehreren Mitgliedern; Test T32; Eskalation als Sicherheitsnetz | MDIS, Livos |
| RI-23 | Key-User sind nicht ausreichend verfügbar | Projekt läuft neben dem Tagesgeschäft und dem Jahresabschluss | Verzögerte Tests und Entscheidungen | m | m | Kapazität je Phase im Lenkungsausschuss zusagen; Termine außerhalb Abschlussphasen | Livos |

## 20.2 Entscheidungsbedarfe Livos

Die folgenden Entscheidungen trifft Livos, teils gemeinsam mit Trios. Grundlage sind die Architekturentscheidungen mit Status O, die zu bestätigenden Empfehlungen (Status E) mit großer Tragweite und die Themen aus OP-17.

| ID | Frage | Optionen | Empfehlung MDIS | Bis wann / Phase |
|---|---|---|---|---|
| ED-01 | Wie wird nach DATEV übergeben? (AE-08) | (a) einstufig nach Zahlungsfreigabe; (b) zweistufig: Vorerfassung bei Verteilung, Verbuchung nach Freigabe | (a); Transparenz über offene Rechnungen im REB; (b) nur als Option in Phase 3 mit Postensperre [A] | QG-0 (mit Trios) |
| ED-02 | Welches System schreibt Stammdaten in den smart-invoice-Bucket? (AE-09) | (a) nur LDconnect (DATEV-Stammdaten), Konsolidierungsnummer als DMS-Eigenschaft; (b) BeSync schreibt, LDconnect nur Buchung | (a): ein Schreiber je Bucket, keine Konflikte | QG-0 |
| ED-03 | Welches System führt je Bau-Rechnungstyp? (AE-11) | (a) d.velop führt, BIM4You prüft, nur d.velop übergibt an DATEV; (b) BIM4You führt und übergibt an DATEV, d.velop archiviert | (a); BIM4You-DATEV-Export für Eingangsrechnungen deaktivieren | Phase 0 Vorklärung, spätestens Start Phase 3 |
| ED-04 | Format der Mandanten-ID (AE-03) | (a) DATEV-Mandantennummer; (b) Beraternummer-Mandantennummer; (c) eigener Schlüssel | (a) oder (b) nach Abstimmung mit Trios; eindeutig und DATEV-kompatibel | QG-0 |
| ED-05 | Freigabegrenzen und Stufen je Gesellschaft (AE-05, OP-17) | Grenzen je Gesellschaft, Kostenobjekt und Stufe; Bemessung netto oder brutto | Netto (Standardbedingung); Matrix je Mandant mit wenigen Standardprofilen | Phase 0 |
| ED-06 | Rollenbesetzung (OP-17) | Personen je Rolle R-01 bis R-15 und Gesellschaft; Personen- oder Gruppenaufgaben | Freigaben möglichst an Personen, Gruppen mit mindestens zwei Mitgliedern | Phase 0 (Pilot), Phase 2 (Rollout) |
| ED-07 | Aktenstruktur (OP-17) | Ebenen und Aktenarten gemäß AE-19 oder Livos-eigene Ordnerstruktur | Max. 4 Ebenen (AE-19); Livos liefert die fachliche Ordnerstruktur | Phase 0 |
| ED-08 | Rückweisungs- und Kürzungsgründe (OP-17) | Vorschlagslisten aus Kap. 9 übernehmen oder anpassen | 5 Rückweisungs- und 7 Kürzungsgründe wie vorgeschlagen, Formulierung der Mailvorlagen durch Livos | Phase 1 |
| ED-09 | Umfang der PM-Freigabe (OP-17) | (a) nur Rechnungen über Schwellwert; (b) alle PM-Rechnungen zur Kenntnis; (c) zusätzlich monatliche PM-Buchungsdaten ins BI | (a) ab Phase 2, (c) optional in Phase 3 | Phase 1 |
| ED-10 | Belegbild in DATEV (S-03) | (a) Beleglink (Beleganzeige Drittanbieter); (b) zusätzlich Belegbild über DATEV Unternehmen online | (a); (b) nur, wenn Trios oder Prüfer das Bild in DATEV benötigen | QG-0 |
| ED-11 | Fälligkeit aus Rechnung oder Stammdaten | (a) Rechnung; (b) Zahlungsbedingung im Kreditorenstamm; (c) Rechnung mit Hinweis bei Abweichung | (c); manuelle Änderung mit Protokoll | Phase 1 |
| ED-12 | Wer führt den Buchhaltungsschritt aus? | (a) nur Trios bzw. Steuerberatung; (b) Trios und Livos-Buchhaltung | (a) für Buchung, Livos mit Leserecht; Zahlungsauslösung **nicht** mit dem Buchen koppeln (AE-10) | Phase 0 |
| ED-13 | Zahlungsgovernance | Wer erstellt den Zahlungsvorschlag in DATEV, wer unterschreibt in multicash, welcher Zahlrhythmus? | Zahlungsfreigabe in d.velop, Unterschrift nach Unterschriftsklassen in multicash (AE-10) | QG-0 |
| ED-14 | Umgang mit offenen Rechnungen zum Stichtag | Option A, B oder C (Kap. 19.4.1) | C (Hybrid) | Phase 1 |
| ED-15 | Pilotgesellschaften | Auswahl nach Kriterien PK-1 bis PK-9 (Kap. 19.3) | 3–5 Gesellschaften inkl. Anschriftspaar und Bau-Gesellschaft | QG-0 |
| ED-16 | Altbestand Verträge | V1, V2 oder V3 (Kap. 19.4.2) | V1 (aktive Verträge mit Metadaten) | Phase 3 |
| ED-17 | Papierpost: zentraler Scan oder Scandienstleister (AE-21, OP-13) | (a) interner Scan mit inbound scan; (b) Dienstleister per Postfach oder API | nach Volumen und Standorten; Entscheidung mit Kostenvergleich | Phase 3 |
| ED-18 | Werkzeug für Vertragsverwaltung und -freigabe (AE-20) | (a) d.velop contracts + process studio; (b) alphaflow Contracts | (a), vorbehaltlich OP-12 | Phase 3 |
| ED-19 | Aufbewahrungsfristen und Löschverfahren (AE-24) | Fristen je Kategorie; automatische Löschung oder jährlicher Löschlauf | 8/10/6 Jahre je Kategorie, Löschlauf jährlich mit Freigabe; Bestätigung durch Steuerberatung | Phase 1 |
| ED-20 | Betriebsform (AE-01) | (a) Cloud C1 (AWS Frankfurt); (b) T Cloud (C2) | (a), weil nur dort KI-Kontierung, KI-Postklassifizierung und die DATEV-Optionen verfügbar sind | QG-0 |

## 20.3 Offene Punkte

### 20.3.1 Offene Punkte OP-01 bis OP-20

Prioritäten: **P1** blockiert Konzeptfreigabe oder Phase 1; **P2** vor der betroffenen Phase klären; **P3** vor Umsetzung des jeweiligen Bausteins.

| ID | Thema | Klärung mit | Prio | Klärungsweg | Phase |
|---|---|---|---|---|---|
| OP-01 | Betriebsform der Zielumgebung (C1 AWS) und der Demo-Instanz | d.velop | P1 | Schriftliche Bestätigung d.velop; Prüfung in der Tenant-Verwaltung | 0 |
| OP-02 | Mandantenerkennung: Test mit echten Livos-Belegen (gleiche Anschriften), Alias-Vorbelegung, BT-10 | Livos, Test | P1 | Erkennungstest T28–T30 im Test-Tenant mit anonymisierten Belegen | 0 |
| OP-03 | Lizenzrecht: Dritte (Trios, Projektsteuerer, PM) als Buchhaltungs-/Freigabeuser zulässig? Mischlizenz invoices/platform edition | d.velop | P1 | Schriftliche Anfrage an d.velop Vertrieb; Aufnahme ins Angebot | 0 |
| OP-04 | DATEV-Betrieb: wer betreibt und lizenziert DATEV, Riecken-Gateway, DATEVconnect, Beleganzeige Drittanbieter, Konditionen Option DATEV und LDconnect > 75 Mandanten | Trios, Hoster, d.velop, LIONDEER | P1 | Schnittstellenrunde; Name des Hosters und Hosting-Modell erheben | 0 |
| OP-05 | DATEV-Übergabe ein- vs. zweistufig; Verarbeitung Zahlbetrag/Kürzung in DATEV und Zahlungsvorschlag | Trios | P1 | Workshop DATEV/Zahlung; Test T24 | 0 |
| OP-06 | Führendes System je Bau-Rechnungstyp; BIM4You-Import (PDF/ZUGFeRD), Export Prüfergebnis | Livos, BIB GmbH | P1 | Workshop Bau; Anfrage BIB GmbH; ED-03 | 0 / 3 |
| OP-07 | Schreibzugriff auf laufende smart-invoice-Belege per API (Zahlbetrag nach BIM4You) | d.velop | P2 | Anfrage Technology Partner Management | vor 3 |
| OP-08 | Restriction Set über alle Gruppen (T03), Aktenbildung Mehrfachregel (T13), Verhalten leerer Erkennungsfelder | Test-Tenant | P1 | Tests T03, T05, T13 | 0 |
| OP-09 | Vier-Augen-Vorschau-Feature: Status und allgemeine Verfügbarkeit | d.velop | P2 | Anfrage d.velop Support; bis dahin Wertgrenzen-Verbindung | 1 / 5 |
| OP-10 | Eskalations-Mailkanal, IBAN-Abweichungswarnung, Zahlbetrag-Feld in Maske schaltbar, Kontierungsvorlagen mit %-Schlüssel | Test | P2 | Tests T24–T27 | 0 / 1 |
| OP-11 | process-studio-Kontingent (1.000 Ausführungen/Monat in business): zählt smart invoice mit? | d.velop | P2 | Anfrage d.velop; Mengenschätzung | vor 3 |
| OP-12 | d.velop contracts: Standard-Freigabeworkflow? Handbuch; alternativ alphaflow | d.velop | P3 | Handbuch über Partnerzugang; Demo | vor 4 |
| OP-13 | Post: Scan intern vs. Dienstleister; mail dispatcher Cloud-Lizenz | Livos, d.velop | P3 | Volumenerhebung; Anfrage d.velop; ED-17 | vor 4 |
| OP-14 | IDW PS 880 / C5 für Cloud, Verfahrensdokumentation | d.velop | P2 | Prüfbericht und Testat anfordern | 1 |
| OP-15 | Legal Hold / Ablaufhemmung technisch | d.velop | P3 | Anfrage d.velop; Test T17 | vor 2 |
| OP-16 | Livos: M365 als Mailsystem? Entra ID? | Livos | P1 | Abfrage Livos-IT | 0 |
| OP-17 | Livos: Aktenstruktur, Freigabegrenzen, Rollenbesetzung, Rückweisungs-/Kürzungsgründe, Scope PM-Freigabe | Livos (Prozess-Workshop) | P1 | Prozess- und Detailworkshops; ED-05 bis ED-09 | 0 |
| OP-18 | Umlageinformationen aus BIM4You: Bedeutung und Format | Livos | P3 | Workshop Bau | vor 3 |
| OP-19 | d.velop pilot: Tokengrenze bei langen Verträgen, LLM-Region/AVV | d.velop | P3 | PoC mit einem echten Vertrag (T35); AVV anfordern | vor 4 |
| OP-20 | Test-Tenant-Lizenzierung | d.velop | P2 | Anfrage d.velop Vertrieb | 0 |

### 20.3.2 Ergänzende offene Punkte OP-21 ff.

Die folgenden Punkte stammen aus der Detailanalyse zu DATEV, Rechnungsdetails, Verträgen/Archiv, Umsystemen, Cloud-Administration und aus den Kapiteln 13 bis 18. Sie sind nicht in OP-01 bis OP-20 enthalten.

| ID | Thema | Klärung mit | Prio | Klärungsweg | Phase |
|---|---|---|---|---|---|
| OP-21 | DATEV-Mandantenliste mit Berater- und Mandantennummer; liegen alle Mandanten auf einem DATEV-System? Anzahl Kreditoren, Sachkonten, KOST1/KOST2 je Mandant; einheitlicher Kontenrahmen? | Livos, Trios | P1 | Export aus DATEV durch Trios | 0 |
| OP-22 | LDconnect: Stammdatensync untertägig oder auf Anforderung; nur genutzte Sachkonten; Postensperre und Belegfeld 2 übertragbar; Verhalten bei Schnittstellenfehlern | LIONDEER, d.velop | P1 | Handbuch LDconnect über Partnerzugang; Anfrage LIONDEER | 0 |
| OP-23 | Zahlungsgovernance: wer erstellt den Zahlungsvorschlag, wer ist unterschriftsberechtigt, Zahlrhythmus | Livos, Trios | P1 | Workshop DATEV/Zahlung; ED-13 | 0 |
| OP-24 | multicash: Produkt und Version, Importweg für SEPA-Dateien, Statusrückmeldung (pain.002), Weg der Kontoauszüge nach DATEV | Livos, Omikron | P2 | Abfrage Livos-Treasury; Anfrage Omikron | vor 3 |
| OP-25 | Versand von E-Mails an externe Adressen aus d.velop (Messaging-Aktion, Anhänge) – würde BeSync-Anteil in S-11 verringern | d.velop | P2 | Release Notes beobachten; Anfrage d.velop | vor 2 |
| OP-26 | Export-Ereignisse: enthalten sie den handelnden Benutzer? Sind viele Integrations-Exporte je Workflow zulässig (Performance)? Werteliste `Workflowstatus` | d.velop | P2 | API-Test T31; Anfrage d.velop | vor 2 |
| OP-27 | evidanza: lizenzierte Konnektoren (SQL, REST), bestehendes Datenmodell bei Livos | Livos, MDIS | P2 | Bestandsaufnahme BI | vor 2 |
| OP-28 | Sonderbuchungsinformationen (ARAP/PARP, Rückstellungen, Anzahlungen): Quelle, Format, Buchungskanal | Livos, Trios | P3 | Workshop Bau/Buchhaltung | vor 3 |
| OP-29 | PM-Buchungsdaten: Format (z. B. DATEV-Buchungsstapel), eingesetzte PM-Systeme, Lieferweg über Trios | Livos, Trios | P3 | Abfrage bei Asset Management und Trios | vor 3 |
| OP-30 | Steuerliche Einordnung je Gesellschaft: Bauleistender i. S. v. § 13b UStG, Freigrenzen Bauabzugsteuer nach § 48 EStG, § 17 UStG bei Kürzungen und Einbehalten | Trios, Steuerberatung | P2 | Liste je Gesellschaft; Übernahme in den Gesellschaftsstamm (AE-28) | 1 |
| OP-31 | FSB-Prüfung: Registrierung im EIBE-Portal, Prüfintervall, Nachweisführung | Livos Steuer | P3 | Abstimmung mit Steuerabteilung | vor 3 |
| OP-32 | Aufbewahrungsdauer und Export des Aktivitätenprotokolls in der Cloud; Leseprotokoll | d.velop | P2 | Anfrage d.velop; Test T18 | 1 |
| OP-33 | Datenrückgabe bei Vertragsende (Format, Kosten, Fristen); Freischaltung und Grenzen der repo export-API | d.velop | P2 | Vertragsprüfung; Anfrage d.velop | vor 3 |
| OP-34 | Gesellschaftsübergreifende Dokumente beim Verkauf einer Gesellschaft; Aufbewahrungspflichten bei Share Deal und Asset Deal | Livos Recht, Steuerberatung | P3 | Rechtliche Prüfung | vor 3 |
| OP-35 | Datenstandort (Deutschland/EU), AVV und TOM der d.velop-Cloud | d.velop, Livos Datenschutz | P2 | AVV und TOM anfordern | 0 |
| OP-36 | Mailimport: Abrufintervall, Einschränkung der Graph-Berechtigung auf die Rechnungspostfächer | d.velop, Livos-IT | P2 | Messung T33; Richtlinie in M365 | 1 |
| OP-37 | Bestehendes Archiv oder DMS bei Livos: Umfang, Formate, Übernahmebedarf | Livos | P3 | Bestandsaufnahme | vor 1 |
| OP-38 | Freigabe in der mobilen App (d.velop mobile) für smart-invoice-Aufgaben | Test | P3 | Test T36 | 2 |
| OP-39 | Externe Zugänge: Passwortschutz oder MFA für Freigabe- und Formularlinks, Entra-ID-B2B-Gäste statt Cloud-Konten | d.velop, Livos-IT | P3 | Anfrage d.velop; Test | vor 3 |
| OP-40 | Obergrenzen für Permissions, Restriction Sets, Datasets und Gruppen; delegierte Pflege von Restriction Sets durch Fachadministration | d.velop | P2 | Schriftliche Anfrage; Test T19 | 0 |
| OP-41 | ZUGFeRD-Profilprüfung (MINIMUM/BASIC-WL erkennen und zurückweisen) | d.velop | P2 | Anfrage d.velop; Test T37 | 1 |
| OP-42 | BIM4You bei Livos: Betriebsform, Version, Erreichbarkeit für BeSync, lizenzierte Module (E-Rechnungsimport, DATEV-Connector) | Livos-IT, BIB GmbH | P2 | Bestandsaufnahme; Anfrage BIB GmbH | vor 3 |
| OP-43 | Zahlstatus-Rückmeldung (S-06): Verifikation der OPOS-Ressource in DATEVconnect; Abgleichsschlüssel Beleg ↔ offener Posten (Mandant, Kreditor, Belegfeld 1, Betrag, ggf. Dokumentenlink); Erfassungsregel für Belegfeld 1 bei Trios | Trios, DATEV, MDIS | P2 | DATEV Developer Portal; Abstimmung mit Trios; Test T40 | vor 3 |
| OP-44 | Einfluss von Livos auf den Zeitpunkt von Cloud-Updates (Release-Verschiebung, Vorankündigungsfristen) | d.velop | P3 | Anfrage d.velop; Aufnahme in den Vertrag | 1 |
| OP-45 | Lizenz und Zugang für temporäre Betriebsprüfer (R-14, Z1): Lizenzart, Befristung, Kosten | d.velop | P3 | Anfrage d.velop | vor 2 |
| OP-46 | Aufbewahrungsfrist für PM-Freigaberechnungen (WF-03), die bei Livos keine Buchungsbelege sind | Livos, Steuerberatung | P2 | Abstimmung mit der Steuerberatung; Übernahme in Kapitel 7.7 | vor 2 |

## 20.4 Testplan Plattform

### 20.4.1 Tests T01–T23 (Struktur, Rechte, Administration)

Die Tests laufen im **Test-Tenant**. Im geteilten Demo-Tenant sind nur lesende Prüfungen zulässig (T01, T12).

| ID | Test | Erwartung / Zweck | Bezug | Phase |
|---|---|---|---|---|
| T01 | Menüpfade für Berechtigungen, Restriction Sets, Strukturregeln und Aufbewahrung in der Cloud-Oberfläche finden und dokumentieren | Menüpfade für Konfiguration und Betriebshandbuch | AE-18, AE-19, AE-24 | 0 |
| T02 | Permission auf Kategorie Eingangsrechnung mit Filter auf Restriction Set; Testbenutzer in einer Gesellschaftsgruppe | Benutzer sieht nur Belege seiner Gesellschaft (Suche, Akte, REB) | AE-18 | 0 |
| T03 | Permission an Rollengruppe, Werte nur über Gesellschaftsgruppe | Bestätigt die Kernannahme: Restriction Set zieht Werte aus allen Gruppen | AE-18, OP-08 | 0 |
| T04 | Mehrfachwert Mandant (z. B. Rahmenvertrag für zwei Gesellschaften) | Sichtbarkeit für beide Gesellschaftsgruppen | AE-18 | 0 |
| T05 | Dokument ohne Mandant | Klären, wer es sieht (Risiko: niemand oder alle) | P1, OP-08 | 0 |
| T06 | Zuordnung mit leerer Werteliste | Bestätigt, ob eine leere Liste alle Werte erlaubt | AE-18 | 0 |
| T07 | Benutzer in zwei Gruppen, eine davon mit DENIED | DENIED setzt sich gruppenübergreifend durch | AE-18 | 0 |
| T08 | Exakt- gegenüber Teilstring-Vergleich (z. B. 100 gegenüber 1001), Platzhalter | Entscheidet über feste Schlüssellänge der Mandanten-ID | AE-03 | 0 |
| T09 | Verschachtelte oder globale Gruppe als Set-Zuordnung | Vererbung wirksam? Grundlage für Verbundgruppen | AE-18 | 0 |
| T10 | Gruppenmitgliedschaft ändern | Zeit bis zur Wirksamkeit, Neuanmeldung nötig? | S-13 | 0 |
| T11 | Recht Schreiben ohne Löschen; Verknüpfen, Export, Eigenschaftsänderung | Rechtearten der Cloud-Oberfläche | AE-18 | 0 |
| T12 | Bestehende Rechteprofile lesend prüfen | Exakte Syntax der Einschränkungen dokumentieren | AE-18 | 0 |
| T13 | Strukturregeln: Rechnung in Kreditorenakte **und** Objektakte; automatische Aktenanlage; leeres Erkennungsfeld | Mehrfachablage automatisch? | AE-19, OP-08 | 0 |
| T14 | Viele Währungs- und Mehrfach-Eigenschaften in einer Kategorie; Grenze 89 Eigenschaften | Gelten Typkontingente in der Cloud? | Kap. 7 | 0 |
| T15 | Zwei Gruppen mit gleichem 8-Zeichen-Präfix und unterschiedlichen Rechten | Namensschema der Gruppen absichern | AE-18 | 0 |
| T16 | Eigenschaft oder Kategorie umbenennen; Datentyp oder Mehrfachwert nachträglich ändern | Wirkung auf Zuordnungen, Suchen, smart invoice | Kap. 7 | 0 |
| T17 | Test-Kategorie mit kurzer Frist ab Datumseigenschaft und Löschsperre | Automatische Löschung abschaltbar? Protokoll? | AE-24, OP-15 | 0 |
| T18 | Aktivitätenprotokoll: Lesen/Download protokolliert, Export, Aufbewahrungsdauer | Anforderungen der Betriebsprüfung | Kap. 17, OP-32 | 0 |
| T19 | Dataset mit 150 Werten; dynamische Wertemenge über 100 Einträge | Bedienbarkeit bei über 100 Gesellschaften | AE-28, OP-40 | 0 |
| T20 | REB-Workflowberechtigung für mehrere Mandanten oder mit Platzhalter | Aufwand für Geschäftsführung und Verbünde | AE-16, AE-18 | 0 |
| T21 | Bearbeiterfindung über Regel „Gruppe Freigeber je Mandantennummer" | Eine Regel für alle Gesellschaften | AE-05 | 0 |
| T22 | Entra-Enterprise-App: SCIM-Bereitstellung und OIDC-Anmeldung; Deaktivierung; B2B-Gast | Identitätskonzept | S-13, OP-39 | 0 |
| T23 | Konfigurationspaket vom Test- in den Produktiv-Tenant übertragen | Transport- und Change-Verfahren | Kap. 18, 19.1 | 0 |

### 20.4.2 Zusatztests T24 ff. (Rechnungsverarbeitung, Schnittstellen, KI)

| ID | Test | Erwartung / Zweck | Bezug | Phase |
|---|---|---|---|---|
| T24 | Zahlbetrag (Kopf und Position) in der Prüfmaske sichtbar und änderbar schalten; Verarbeitung des Zahlbetrags im DATEV-Buchungsvorschlag und Zahlungsvorschlag | Kürzung ohne Überzahlung | AE-14, OP-05, RI-18 | 0 |
| T25 | IBAN auf der Rechnung weicht vom Kreditorenstamm ab | Sichtbarer Hinweis in der Maske; erkannte IBAN im Export verfügbar | T-16, OP-10 | 0 |
| T26 | Eskalation je Schritt und vor Skonto-/Nettofälligkeit | Benachrichtigung per E-Mail; Übernahme oder Umleitung der Aufgabe durch die Leitung | AE-17, OP-10 | 0 |
| T27 | Kontierungsvorlage mit prozentualer Aufteilung (z. B. 55/45); kreditorenunabhängige Vorlage je Gesellschaft | Standardschlüssel je Gesellschaft (Katalog 2.8) | OP-10 | 0 |
| T28 | Alias-Postfach je Gesellschaft mit Vorbelegung des Mandanten über Importprofil | document reader übernimmt den vorbelegten Mandanten | AE-22, AE-23, OP-02 | 0 |
| T29 | Mandantenerkennung mit echten Livos-Belegen, getrennt nach Gesellschaften mit eigener und mit gemeinsamer Anschrift | Gemessene Trefferquote; Zielwert für die Abnahme (Kap. 19.5.3) | AE-23, OP-02 | 0 / 1 |
| T30 | E-Rechnung mit Käuferreferenz (BT-10) | Wird BT-10 zur Mandantenermittlung genutzt oder per Regel auswertbar? | AE-23, OP-02 | 0 |
| T31 | Export-Ereignis an einer Schrittverbindung auswerten | Enthält Benutzer, Zeitstempel, Schritt; Grundlage S-12 | AE-16, OP-26 | 1 |
| T32 | Vertretung bei Gruppen- und Personenaufgaben; Abwesenheit durch Administrator setzen | Welche Aufgaben sieht der Vertreter? | AE-17, RI-22 | 0 |
| T33 | Abrufintervall des Mailimports messen | Zusagefähige Eingangszeiten | S-14, OP-36 | 1 |
| T34 | Asynchroner Transfer an einer Schrittverbindung mit langer Wartezeit (bis 28 Tage) und Rückmeldung per API | Tragfähigkeit von WF-02 | AE-11, OP-07 | vor 3 |
| T35 | d.velop pilot mit einem langen Livos-Vertrag (z. B. 20 Seiten) | Antwortqualität, Tokengrenze | AE-20, OP-19 | vor 4 |
| T36 | Freigabe einer smart-invoice-Aufgabe in d.velop mobile | Mobile Freigabe möglich (Katalog 1.3) | OP-38 | 2 |
| T37 | ZUGFeRD-Rechnung im Profil MINIMUM bzw. BASIC-WL | Erkennung und Rückweisung als formaler Fehler | RI-13, OP-41 | 1 |
| T38 | Altbeleg aus der Stichtagsmigration ohne DATEV-Übergabe abschließen | Keine Doppelübergabe | Kap. 19.4.1 | 1 |
| T39 | DATEV-Probeübergabe an einen Testmandanten über das Riecken-Gateway, inklusive Fehlerfall | Buchungsvorschlag mit Beleglink, Fehlermeldung bei fehlendem Kreditor | S-01, OP-04 | 1 |
| T40 | OPOS-Abfrage über DATEVconnect und Setzen „bezahlt" am archivierten Beleg | Zahlstatus-Rückmeldung (S-06) technisch möglich | AE-10, OP-04, OP-43 | vor 3 |
| T41 | Zahlungsfreigabe durch dieselbe Person wie die letzte fachliche Freigabe | Wird durch Bedingung oder Gruppentrennung verhindert | AE-05, AE-06 | 0 |

Ergebnisse dokumentiert MDIS in einem Testbericht. Jeder Test erhält einen Status: bestanden, nicht bestanden oder mit Einschränkung. Ein nicht bestandener Test führt zu einer Konzeptanpassung oder einem neuen Risiko im Register (Kap. 20.1).

# 21 Anhang

## 21.1 Glossar

Das Glossar erklärt die Fachbegriffe, Produktnamen und Abkürzungen dieses Konzepts. Es ist nach Themen gegliedert, innerhalb der Themen alphabetisch.

### 21.1.1 d.velop-Produkte und -Begriffe

| Begriff | Erläuterung |
|---|---|
| Aktenbildung / Strukturregel | Regel in d.velop documents, die Dokumente anhand von Eigenschaftswerten automatisch Akten zuordnet und Akten bei Bedarf anlegt. Ein Dokument kann mehreren Akten zugeordnet sein (Mehrfachablage). |
| Aktivitäten | Änderungsprotokoll eines Dokuments in d.velop documents (Cloud): Eigenschaftsänderungen, Versionen, Verknüpfungen. |
| Bucket (Stammdatenbucket) | Stammdatenbereich von smart invoice, der Mandanten, Kreditoren, Sachkonten und weitere Stammdaten aufnimmt. Grenzen je Bucket: 1.000 Mandanten, 100.000 Kreditoren, 50.000 Sachkonten, 100 Workflowdefinitionen. d.velop empfiehlt einen Bucket je Tenant. |
| Buchhaltungsuser | Lizenzrolle in d.velop invoices für Benutzer, die Belege erfassen, verteilen und buchhalterisch bearbeiten. Die Anzahl ist je Paket begrenzt (Medium: 10). |
| C1 / C2 (Betriebsform) | C1: d.velop Cloud im Multi-Tenant-Betrieb auf AWS (Frankfurt). C2: Betrieb in der T Cloud Public. Der Funktionsumfang unterscheidet sich, z. B. bei KI-Funktionen. |
| Clearing / Klärfall | Arbeitsschritt für Belege, die nicht automatisch weiterlaufen können, z. B. bei unbekanntem Mandanten, fehlendem Kreditor oder Dublettenverdacht. |
| Custom Entity | Frei definierbare Stammdatenart in smart invoice, z. B. für Kürzungsgründe oder BIM4You-Vergabeeinheiten. |
| d.velop contracts | Cloud-Anwendung für Vertragsmanagement auf Basis von d.velop documents: Vertragsakte, Laufzeit- und Fristenberechnung, Fristenkalender, Vertragshierarchien. |
| d.velop documents | Dokumentenmanagementsystem (DMS) von d.velop; in der Cloud als platform edition in den Editionen basic, business und ultimate. |
| d.velop invoices | Produktpaket für die Eingangsrechnungsverarbeitung; umfasst Erkennung, smart invoice, Rechnungseingangsbuch; Lizenz nach Rechnungsvolumen und Buchhaltungsusern. |
| d.velop mobile | App für iOS und Android zum Zugriff auf Dokumente und Aufgaben (ab Edition business). |
| d.velop pilot | KI-Assistent von d.velop für Fragen an Dokumente, z. B. an Vertragsinhalte (ab Edition business). |
| d.velop sign | Dienst für elektronische Signaturen. |
| DmsConfig API | Programmierschnittstelle zur Konfiguration von d.velop-documents-Repositories in der Cloud (Kategorien, Eigenschaften, Berechtigungen, Pakete). |
| document reader | Erkennungsdienst von d.velop, der Rechnungsdaten und Dokumentinhalte per OCR und KI ausliest. |
| eInvoice converter | Dienst, der E-Rechnungen (XRechnung, ZUGFeRD) einliest, visualisiert und XRechnungen validiert. |
| email import | Dienst zum automatischen Abruf von E-Mails und Anhängen aus Microsoft-365-Postfächern über Microsoft Graph. |
| Freigabematrix | Tabelle in smart invoice, die Freigeber abhängig von Mandant, Kostenobjekt, Betrag und Stufe bestimmt. |
| Freigabeuser | Lizenzrolle in d.velop invoices für Prüfer und Freigeber; in beliebiger Anzahl enthalten (Zulässigkeit für Dritte: OP-03). |
| inbound (scan, e-mail) | Eingangsdienste von d.velop für Scan, E-Mail und Upload, inklusive Stapelverarbeitung. |
| Kategorie | Cloud-Begriff für Dokumentart oder Aktenart in d.velop documents. |
| Kontierungsvorlage | Vorlage in smart invoice, die Sachkonto und Kostenstellen für wiederkehrende Rechnungen vorbelegt. |
| Mandant (smart invoice) | Buchungskreis in smart invoice; im Konzept entspricht ein Mandant einer Livos-Gesellschaft bzw. einem DATEV-Mandanten. Nicht zu verwechseln mit dem Cloud-Tenant. |
| mail dispatcher | d.velop-Anwendung zur Verteilung von Posteingang an Gruppen mit Erinnerung und Eskalation. |
| Permission | Berechtigungseintrag in d.velop documents (Cloud): Kategorie × Rechtestufe (Lesen, Schreiben, Löschen) mit ALLOWED, INHERITED oder DENIED. |
| platform edition | Lizenzmodell von d.velop documents in der Cloud mit den Editionen basic, business und ultimate, abgerechnet pro Benutzer und Monat. |
| process studio | Werkzeug von d.velop zur Modellierung und Ausführung von BPMN-Prozessen mit Formularen (d.velop forms), Aufgaben und externen Benutzeraufgaben. |
| Rechnungseingangsbuch (REB) | Übersicht aller Rechnungen in d.velop invoices mit Status, aktuellem Schritt, Zuständigkeit, Schnellzugriffen und CSV-Export. |
| repo export-API | Programmierschnittstelle zum Export von Dokumenten (Originale aller Versionen) und JSON-Metadaten aus einem Cloud-Repository. |
| Restriction Set | Werteliste je Gruppe (z. B. Mandanten-IDs), die eine Permission auf bestimmte Eigenschaftswerte einschränkt. Grundlage der Mandantentrennung. |
| smart invoice | Workflow-Komponente von d.velop invoices: Verteilung, Prüfung, Kontierung, Freigabe, Buchhaltung, Freigabematrix, Eskalation. |
| Tenant | Eigenständige Instanz der d.velop Cloud. Livos erhält einen produktiven und einen Test-Tenant. |
| Transfer (asynchron) | Mechanismus in smart invoice, bei dem ein Beleg an ein Fremdsystem übergeben wird und auf dessen Rückmeldung wartet. |
| Wertemenge / Dataset | Liste zulässiger Werte für eine Eigenschaft (statisch oder aus Stammdaten befüllt). |
| Wertgrenzen-Verbindung | Bedingte Verbindung zwischen Workflowschritten, z. B. zweite Freigabe ab einem Nettobetrag (Beträge in Cent). |
| Webhook | Automatischer Aufruf einer externen Adresse bei einem Ereignis, z. B. an einer Schrittverbindung in smart invoice. |

### 21.1.2 DATEV, Finanzbuchhaltung und Zahlung

| Begriff | Erläuterung |
|---|---|
| Beleganzeige Drittanbieter | DATEV-Funktion, mit der ein Beleglink aus einem Fremd-DMS in der Buchung geöffnet wird. |
| Beraternummer / Mandantennummer | Identifikation des DATEV-Nutzers (Kanzlei oder Unternehmen) bzw. des Mandanten (Gesellschaft) in DATEV. |
| Buchungsvorschlag | Vorbereitete Buchung, die in DATEV geprüft und übernommen wird. |
| DATEV Unternehmen online (DUO) | Cloud-Plattform von DATEV für den Belegaustausch zwischen Unternehmen und Kanzlei. |
| DATEVasp / SmartIT / PARTNERasp | Hosting-Angebote für DATEV-Arbeitsplätze durch DATEV bzw. Partner. |
| DATEVconnect | Programmierschnittstelle zu DATEV-Anwendungen, z. B. für Buchungsvorschläge und offene Posten (`accounts-payable`). |
| EBICS | Electronic Banking Internet Communication Standard; Verfahren zur Übertragung von Zahlungsdateien an Banken. |
| EXTF | DATEV-Format für Buchungsstapel und Stammdaten (Kopfkennung „EXTF"). |
| KOST1 / KOST2 | Kostenstellen- bzw. Kostenträgerfelder in DATEV. |
| Kreditor | Lieferantenkonto in der Buchhaltung; bei Livos je Gesellschaft mit eigener Nummer (70000er-Kreis intern, 80000er-Kreis aus Hausverwaltungen). |
| LDconnect | DATEV-Konnektor von LIONDEER; von d.velop als Option „DATEV Rechnungswesen" vertrieben. Überträgt Buchungsvorschläge und synchronisiert Stammdaten. |
| multicash | Zahlungsverkehrssoftware von Omikron; führt SEPA-Zahlungen mit Unterschriftsklassen über EBICS aus. |
| OPOS | Offene-Posten-Verwaltung in DATEV; zeigt, ob eine Rechnung bezahlt ist. |
| pain.001 / pain.002 | SEPA-XML-Nachrichten für Überweisungsaufträge bzw. Statusrückmeldungen der Bank. |
| Postensperre | Kennzeichen in DATEV, das einen offenen Posten von Zahlungsvorschlägen ausschließt. |
| Riecken Cloud Gateway | Datengateway der Firma Riecken, über das Cloud-Anwendungen DATEVconnect in gehosteten DATEV-Umgebungen erreichen. |
| Sachkonto | Konto der Finanzbuchhaltung für die Kontierung (z. B. Aufwand, Anlagen). |
| SEPA | Einheitlicher Euro-Zahlungsverkehrsraum; Zahlungsdateien im XML-Format. |
| Skonto | Preisnachlass bei Zahlung innerhalb einer Frist. |
| Zahlungsvorschlag | DATEV-Funktion, die fällige offene Posten zur Zahlung zusammenstellt und eine SEPA-Datei erzeugt. |

### 21.1.3 Recht, Steuern und E-Rechnung

| Begriff | Erläuterung |
|---|---|
| § 13b UStG | Steuerschuldnerschaft des Leistungsempfängers (Reverse Charge). Bei Bauleistungen schuldet der Empfänger die Umsatzsteuer, wenn er selbst nachhaltig Bauleistungen erbringt. |
| § 146 Abs. 4 AO | Verbot, Buchungen und Aufzeichnungen so zu verändern, dass der ursprüngliche Inhalt nicht mehr feststellbar ist. |
| § 147 AO | Aufbewahrungspflichten und Datenzugriff der Finanzverwaltung (Z1–Z3); Abs. 3 S. 5 regelt die Ablaufhemmung. |
| § 48 / § 48b EStG | Bauabzugsteuer von 15 % auf Bauleistungen (§ 48); Befreiung durch Freistellungsbescheinigung (§ 48b). |
| Abschlagsrechnung / Schlussrechnung | Teilrechnung nach Leistungsstand bzw. abschließende Rechnung nach Fertigstellung; bei VOB-Verträgen oft kumuliert. |
| Ablaufhemmung | Die Aufbewahrungsfrist endet nicht, solange die Unterlagen für eine noch nicht abgelaufene Festsetzungsfrist von Bedeutung sind. |
| BEG IV | Viertes Bürokratieentlastungsgesetz (BGBl. 2024 I Nr. 323). Verkürzt die Aufbewahrungsfrist für Buchungsbelege von 10 auf 8 Jahre. |
| BT-10 (Käuferreferenz) | Feld „Buyer reference" der europäischen Norm EN 16931; in XRechnung Pflicht. Kann eine Gesellschaft eindeutig kennzeichnen. |
| EIBE | Elektronische Abfrage von Freistellungsbescheinigungen beim Bundeszentralamt für Steuern (BZSt), Webportal ohne Schnittstelle. |
| E-Rechnung | Rechnung in einem strukturierten elektronischen Format nach EN 16931 (z. B. XRechnung, ZUGFeRD ab Profil EN16931); das XML ist das Original. |
| Factur-X | Französisch-deutsches Hybridformat, technisch identisch mit ZUGFeRD 2.x. |
| Freistellungsbescheinigung (FSB) | Bescheinigung des Finanzamts nach § 48b EStG; befreit den Auftraggeber vom Einbehalt der Bauabzugsteuer. |
| GoBD | Grundsätze zur ordnungsmäßigen Führung und Aufbewahrung von Büchern, Aufzeichnungen und Unterlagen in elektronischer Form sowie zum Datenzugriff (BMF-Schreiben 28.11.2019, geändert 2024 und 2025). |
| IDW PS 880 | Prüfungsstandard des Instituts der Wirtschaftsprüfer für die Prüfung von Softwareprodukten. |
| Legal Hold | Sperre von Dokumenten gegen Löschung, z. B. wegen laufender Prüfung oder Rechtsstreit. |
| Peppol | Europäisches Netzwerk zum Austausch von E-Rechnungen über zertifizierte Zugangspunkte; für Livos nicht erforderlich. |
| Sicherheitseinbehalt | Einbehalt eines Teils des Rechnungsbetrags als Sicherheit für Vertragserfüllung oder Gewährleistung (VOB/B § 17). |
| Verfahrensdokumentation | Nach GoBD geforderte Beschreibung des DV-gestützten Verfahrens (Organisation, Technik, Kontrollen). |
| VOB/B | Vergabe- und Vertragsordnung für Bauleistungen, Teil B; regelt u. a. Abschlagszahlungen (§ 16) und Sicherheitsleistung (§ 17). |
| XRechnung | Deutscher Standard für E-Rechnungen auf Basis EN 16931 (reines XML); aktuelle Version 3.0. |
| Z1 / Z2 / Z3 | Formen des Datenzugriffs der Finanzverwaltung: Z1 unmittelbarer Nur-Lese-Zugriff, Z2 mittelbarer Zugriff (Auswertung durch das Unternehmen nach Vorgabe), Z3 Datenträgerüberlassung. |
| ZUGFeRD | Deutsches Hybridformat: PDF/A-3 mit eingebettetem XML. Die Profile MINIMUM und BASIC-WL gelten nicht als E-Rechnung. |

### 21.1.4 Identität, Sicherheit und Technik

| Begriff | Erläuterung |
|---|---|
| 2FA / FIDO2 | Zwei-Faktor-Anmeldung bzw. Standard für hardwaregestützte Anmeldung. |
| AVV / TOM | Auftragsverarbeitungsvertrag und technisch-organisatorische Maßnahmen nach DSGVO. |
| C5 | Cloud Computing Compliance Criteria Catalogue des BSI; Testat für Cloud-Dienste. |
| Microsoft Entra ID | Identitätsdienst von Microsoft (früher Azure Active Directory); bei Livos Quelle für Benutzer und Gruppen (OP-16). |
| Microsoft Graph | Programmierschnittstelle zu Microsoft 365; genutzt für den E-Mail-Import und, je nach Festlegung in Phase 0 (OP-25), für den E-Mail-Versand durch BeSync. |
| Microsoft 365 (M365) | Office- und Mailplattform von Microsoft; Voraussetzung für den E-Mail-Import von d.velop. |
| OIDC | OpenID Connect; Standard für Single Sign-on (SSO). |
| SCIM | System for Cross-domain Identity Management; Standard zur automatischen Übertragung von Benutzern und Gruppen. |
| SSO | Single Sign-on; einmalige Anmeldung für mehrere Anwendungen. |
| Staging-Schicht | Zwischendatenbank (MS SQL), in der BeSync Prozessereignisse für Auswertungen sammelt. |

### 21.1.5 Livos, MDIS und Projektbegriffe

| Begriff | Erläuterung |
|---|---|
| Asset Management | Livos-interne Einheit, die u. a. Rechnungen der Property Manager oberhalb eines Schwellwerts freigibt. |
| BeSync | Middleware-Plattform von MDIS. Im Konzept für Schnittstellen und Automatisierungen, die der d.velop-Standard nicht abdeckt; betrieben von MDIS. |
| BIM4You | Software für Bau-Budgetcontrolling und Bauprojektsteuerung der BIB GmbH (u. a. Budgetabgleich, VOB-Prüfung, Einbehalte). |
| evidanza | BI-, Reporting- und Planungssoftware, bei Livos im Einsatz. |
| Gesellschaft | Rechtliche Einheit der LIVOS Gruppe; im Konzept gleichbedeutend mit Mandant. |
| Hypercare | Verstärkte Betreuung in den ersten Wochen nach einem Go-live. |
| Konsolidierungsnummer | Gesellschaftsübergreifende Lieferantennummer in der Lieferanten-App; verbindet die DATEV-Kreditorennummern eines Lieferanten in allen Gesellschaften. |
| Lieferanten-App | Bestehende MDIS-App auf BeSync zur Pflege von Lieferanten- und Stammdaten; führt Lieferantenidentität und Kreditor-Mapping. |
| Mandanten-ID | Schlüssel der Gesellschaft auf jedem Dokument (Eigenschaft „Mandant"); Vorschlag: DATEV-Mandantennummer. |
| MVP | Minimum Viable Product; erster produktiv nutzbarer Umfang (Phase 1). |
| Objekt | Immobilie oder Bauvorhaben mit global eindeutiger Objekt-ID. |
| PoC | Proof of Concept; Machbarkeitsnachweis. |
| Property Manager (PM) / Hausverwaltung (HV) | Externe Verwalter, die Objekte für Livos bewirtschaften und ihre Rechnungen überwiegend selbst buchen und zahlen. |
| Qualitätstor (QG) | Entscheidungspunkt am Ende einer Projektphase. |
| Segment | Geschäftsbereich einer Gesellschaft: Bestand, Privatisierung oder Bau. |
| Trios | Externer Buchhaltungsdienstleister von Livos; bucht in DATEV. |
| Umlageinformationen | Begriff aus der Zielarchitektur (Rückfluss aus BIM4You); Bedeutung offen (OP-18). |
| Vergabeeinheit / Los / Gewerk | Einheiten der Bauvergabe; Grundlage für die Zuordnung von Bau-Rechnungen in BIM4You. |
| X.One | KI-Plattform von MDIS; im Konzept für die Kreditorenkonsolidierung (PoC) und übergreifende Analysen. |

## 21.2 Quellenverzeichnis

Die Quellen wurden bis zum 26.09.2026 abgerufen. Vertragsdokumente von d.velop (Leistungs- und Funktionsbeschreibungen) haben Vorrang vor Produktseiten. Vor Angebotsabgabe sind die jeweils gültigen Fassungen neu zu prüfen. Einige Handbücher (u. a. DATEV-Anbindung, Cloud-Administration) sind nur mit Partnerzugang erreichbar und hier nicht aufgeführt.

### 21.2.1 Livos-Unterlagen und Workshop

| Nr. | Quelle |
|---|---|
| Q-01 | Livos: Leistungskatalog Rechnungsmanagement (29 Anforderungen), Stand Juli 2026 |
| Q-02 | MDIS: Livos DMS Business-Architektur (Zielarchitektur, 5 Folien) |
| Q-03 | MDIS: Agenda Demo-Workshop Livos mit offenen Fragen |
| Q-04 | MDIS: Architektur und Konfiguration der Demo-Instanz, Testdaten (fiktive Gesellschaften und Belege) |
| Q-05 | Demo-Workshop mit Livos am 22.09.2026 (Protokollierung, zitiert als „Workshop 22.09.2026") |

### 21.2.2 d.velop

| Nr. | Quelle | URL |
|---|---|---|
| Q-10 | Leistungsbeschreibung d.velop invoices, Version 2025-12-15 | https://my.d-velop.cloud/center/a/dvelopinvoicesmedium/legal/sow?language=de |
| Q-11 | d.velop smart invoice Cloud: Administrieren (Stand 06/2026) | https://help.d-velop.de/docs/api/documentations/de/smart-invoice-cloud/cloud/pdf |
| Q-12 | d.velop smart invoice: Arbeiten mit Eskalationen | https://help.d-velop.de/docs/de/pub/smart-invoice-cloud/cloud/konfigurieren-von-dvelop-smart-invoice/arbeiten-mit-eskalationen |
| Q-13 | d.velop smart invoice-API (Cloud) | https://help.d-velop.de/docs/api/documentations/de/smart-invoice-developer/cloud/pdf |
| Q-14 | d.velop invoices – Rechnungseingangsbuch: Anwenden | https://help.d-velop.de/docs/api/documentations/de/invoice-monitor/cloud/pdf |
| Q-15 | d.velop eInvoice converter: Administrieren | https://help.d-velop.de/docs/api/documentations/de/einvoice-converter/cloud/pdf |
| Q-16 | d.velop inbound scan: Administrieren | https://help.d-velop.de/docs/api/documentations/de/inbound-scan-admin-cloud/cloud/pdf |
| Q-17 | d.velop invoices Help Center: Umstellung des Kommunikationswegs (09/2026) | https://help.d-velop.de/invoices/de/articles/cmtiz5gdg4oxt06vyxjrm9kfk |
| Q-18 | d.velop invoices Help Center: CSV-Export im REB (09/2026) | https://help.d-velop.de/invoices/de/articles/cms7m6f3dyddy07w4mmm35kqn |
| Q-19 | d.velop invoices Help Center: Schnellzugriff eskalierte Rechnungen (09/2026) | https://help.d-velop.de/invoices/de/articles/cmtvssd4zeoct07uoaijon9b8 |
| Q-20 | Leistungsbeschreibung d.velop documents platform edition (2025-10-16) | https://s3.eu-central-1.amazonaws.com/mediamanager.cloudcenter.service.d-velop.cloud/fe5f22d4-0b44-46d7-aed1-30067e47fe7a |
| Q-21 | Funktionsbeschreibung d.velop documents (2025-11-28) | https://s3.eu-central-1.amazonaws.com/mediamanager.cloudcenter.service.d-velop.cloud/00fdd0bf-d698-4e3d-8a46-34c864678fdc |
| Q-22 | Leistungsbeschreibung d.velop documents (Cloud), 2025-02-18 | https://s3.eu-central-1.amazonaws.com/mediamanager.cloudcenter.service.d-velop.cloud/71677a83-7cdb-4097-bfc1-bec37f37bc07 |
| Q-23 | Leistungsbeschreibung d.velop cloud platform (2026-07-28) | https://s3.eu-central-1.amazonaws.com/mediamanager.cloudcenter.service.d-velop.cloud/42f5a2ba-b16d-4e0c-be37-3f0d6d6f6bee |
| Q-24 | d.velop documents: Anwenden (Cloud) | https://help.d-velop.de/docs/api/documentations/de/documents/cloud/pdf |
| Q-25 | DmsConfig API | https://help.d-velop.de/dev/api/openapi/dmsconfig |
| Q-26 | d.velop usermanagement: Administrieren (Cloud) | https://help.d-velop.de/docs/api/documentations/de/usermanagement-cloud-on-premises/cloud/pdf |
| Q-27 | d.velop usermanagement API (SCIM 2.0) | https://help.d-velop.de/dev/api/openapi/usermanagement |
| Q-28 | d.velop contracts: Administrieren (Cloud) | https://help.d-velop.de/docs/api/documentations/de/contracts-admin-cloud/cloud/pdf |
| Q-29 | d.velop contracts – Produktseite und Preise & Pläne | https://www.d-velop.de/software/vertragsmanagement |
| Q-30 | d.velop process studio: Anwenden 2026.q2 | https://help.d-velop.de/docs/api/documentations/de/process-studio-user/2026.q2/pdf |
| Q-31 | Funktionsbeschreibung d.velop process studio (2025-10-29) | https://my.d-velop.cloud/center/a/processstudiobusiness/legal/funktionsbeschreibung?language=de |
| Q-32 | d.velop mail dispatcher: Administrieren (Cloud) | https://help.d-velop.de/docs/api/documentations/de/mail-dispatcher-admin/cloud/pdf |
| Q-33 | d.velop documents repo export-API (Cloud) | https://help.d-velop.de/docs/api/documentations/de/documents-repo-export-developer/cloud/pdf |
| Q-34 | Funktionsbeschreibung d.velop pilot (2026-09-11) | https://my.d-velop.cloud/center/a/inboundgpt/legal/sow?language=de |
| Q-35 | d.velop pilot: Administrieren 1.0.0 | https://help.d-velop.de/docs/api/documentations/de/pilot-admin/1.0.0/pdf |
| Q-36 | d.velop Zertifizierungen | https://www.d-velop.com/certifications |
| Q-37 | d.velop userprofile: Konfigurieren des Abwesenheitsstatus | https://help.d-velop.de/docs/de/pub/userprofile/latest/erste-schritte/konfigurieren-des-abwesenheitsstatus |
| Q-38 | d.velop DMSApp API | https://help.d-velop.de/dev/api/openapi/dms-app |
| Q-39 | d.velop API-Übersicht | https://help.d-velop.de/dev/documentation |

### 21.2.3 DATEV-Anbindung, Zahlung und Drittanbieter

| Nr. | Quelle | URL |
|---|---|---|
| Q-40 | Leistungsschein LDconnect für DATEV Rechnungswesen (Cloud), Stand 11/2025 | https://s3.eu-central-1.amazonaws.com/mediamanager.cloudcenter.service.d-velop.cloud/82f418b4-8a85-4687-a9ff-53f938f690a3 |
| Q-41 | d.velop Store: LDconnect für DATEV Rechnungswesen | https://www.d-velop.de/store/liondeer-ldconnect-datev-rechnungswesen |
| Q-42 | Leistungsbeschreibung d.velop invoices for DATEV Unternehmen Online (2023-07-05) | https://s3.eu-central-1.amazonaws.com/mediamanager.cloudcenter.service.d-velop.cloud/be5e4349-ebfa-4fe2-ae4f-9608677d53b3 |
| Q-43 | Riecken Cloud Gateway: Produkt | https://cloudgateway.riecken.io/produkt.html |
| Q-44 | DATEV: Einsatz Cloud Gateway for DATEVconnect in DATEVasp | https://www.datev.de/content/dam/markenassets/themen-und-produktgruppen/mydatev/pdf/datevasp_smartit/einsatz_cloud_gateway_for_datevconnect_in_datevasp.pdf |
| Q-45 | DATEV Shop: DATEVconnect | https://www.datev.de/web/de/shop/produkt-details/datevconnect-95280 |
| Q-46 | DATEV Developer: DATEV-Format Buchungsstapel | https://developer.datev.de/de/file-format/details/datev-format/format-description/booking-batch |
| Q-47 | DATEV Hilfe 1036491: SEPA-Zahlungsaufträge exportieren und importieren | https://apps.datev.de/help-center/documents/1036491 |
| Q-48 | multicash (Omikron): Produktseite multicash classic | https://www.multicash.com/loesungen/unternehmen/multicash/ |
| Q-49 | BIB GmbH: Neues in BIM4You 2026 | https://bibdata.bib-gmbh.de/info/Neues_in_BIM4You_2026.pdf |
| Q-50 | DocuWare Case Study Krieger + Schramm (DMS, BIM4You, DATEV) | https://start.docuware.com/de/case-studies/krieger-schramm |
| Q-51 | evidanza: Standardlösung DATEV | https://evidanza.de/produkte/standardloesungen/datev/ |
| Q-52 | MDIS: MDIS One / BeSync | https://mdis-consulting.de/loesungen/mdis-one/ |
| Q-53 | Microsoft Learn: Anwendungsbereitstellung in Microsoft Entra ID (SCIM) | https://learn.microsoft.com/de-de/entra/identity/app-provisioning/how-provisioning-works |

### 21.2.4 Recht und Verwaltung

| Nr. | Quelle | URL |
|---|---|---|
| Q-60 | § 14 UStG | https://www.gesetze-im-internet.de/ustg_1980/__14.html |
| Q-61 | § 13b UStG | https://www.gesetze-im-internet.de/ustg_1980/__13b.html |
| Q-62 | § 48 EStG | https://www.gesetze-im-internet.de/estg/__48.html |
| Q-63 | § 48b EStG | https://www.gesetze-im-internet.de/estg/__48b.html |
| Q-64 | § 146 AO | https://www.gesetze-im-internet.de/ao_1977/__146.html |
| Q-65 | § 147 AO | https://www.gesetze-im-internet.de/ao_1977/__147.html |
| Q-66 | § 257 HGB | https://www.gesetze-im-internet.de/hgb/__257.html |
| Q-67 | GoBD 1. Änderung, BMF-Schreiben 11.03.2024 | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Weitere_Steuerthemen/Abgabenordnung/AO-Anwendungserlass/2024-03-11-aenderung-gobd.pdf?__blob=publicationFile&v=4 |
| Q-68 | GoBD 2. Änderung, BMF-Schreiben 14.07.2025 | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Weitere_Steuerthemen/Abgabenordnung/2025-07-14-GoBD-2-aenderung.pdf?__blob=publicationFile&v=4 |
| Q-69 | BMF: FAQ E-Rechnung (Stand März 2026) | https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html |
| Q-70 | BZSt: Bauabzugsteuer und Freistellungsbescheinigungen | https://www.bzst.de/DE/Unternehmen/Bauleistungen/bauleistungen.html |
| Q-71 | EIBE-Portal (Abfrage Freistellungsbescheinigungen) | https://eibe.bff-online.de/eibe/index.xhtml |
| Q-72 | VOB/B § 17 Sicherheitsleistung | https://dejure.org/gesetze/VOB-B/17.html |
| Q-73 | BDO: Verkürzung der Aufbewahrungsfristen durch BEG IV | https://www.bdo.de/de-de/insights/accounting-it/hgb/verkuerzung-der-aufbewahrungsfristen-257-abs-4-hgb-durch-das-4-buerokratieentlastungsgesetz |
| Q-74 | Art. 17 DSGVO | https://dsgvo-gesetz.de/art-17-dsgvo/ |

## 21.3 Workshop-Anforderungsliste

Die Liste enthält alle fachlichen Anforderungen, die im Demo-Workshop am 22.09.2026 geäußert wurden, in Kurzform. Die Themen zum Angebot selbst (T-42 bis T-45) sind nicht enthalten. Die Spalte „Status" nutzt die Kürzel aus Kap. 1: **[S]** Standard, **[K]** Konfiguration, **[A]** Anpassung (meist BeSync), **[O]** offen bzw. zu verifizieren.

| ID | Anforderung (Kurzform) | Katalog | Lösung / Verweis | Status |
|---|---|---|---|---|
| T-01 | Anhänge aus einem definierten Postfach automatisch importieren und verarbeiten | 2.1 | Zentrales Rechnungspostfach und Alias je Gesellschaft über email import (Kap. 9; AE-22; S-14) | [S] |
| T-02 | Klären, welches System die Lieferantennummer führt; gleiche Lieferanten haben je Gesellschaft verschiedene Kreditorennummern | 1.1, 2.2, 5.1 | Drei Nummernkreise: Konsolidierungsnummer in der Lieferanten-App, DATEV-Kreditor je Mandant, HV-Kreditor (Kap. 8; AE-09) | [K] / [A] |
| T-03 | Neue Kreditoren verarbeiten, ohne dass Livos in DATEV anlegt | 5.1 | Klärfall „Kreditor fehlt", Anlage-Anforderung an Trios, Sync am Folgetag (WF-04; S-05; AE-09) | [A] |
| T-04 | Initialaufwand für das Kreditoren-Mapping über mehr als 100 Gesellschaften gering halten | 5.4 | KI-gestützte Erstkonsolidierung mit MDIS X.One als PoC in Phase 0 (Kap. 8, 19.2.2; AE-09) | [A] |
| T-05 | Eindeutiger Schlüssel aus DATEV-Mandantennummer und Kreditorennummer | 5.1, 5.4 | Mapping-Schlüssel „DATEV-Mandantennr + Kreditorennr" in der Lieferanten-App (AE-09; AE-03) | [K] |
| T-06 | Stammdatenabgleich in beide Richtungen; neue Kreditoren aus DATEV kommen mit Nummer zurück | 5.1, 5.4 | DATEV-Stammdaten täglich in den Bucket (S-02); Rückführung in die Lieferanten-App (S-05) | [K] / [A] |
| T-07 | Property Manager werden nicht zur Nutzung eines Erfassungssystems verpflichtet | 4.1 | Rahmenbedingung RB-2: PM-Freigabe per E-Mail-Postfach ohne Konto; Rückmeldung per E-Mail (Kap. 3.7, 11; WF-03; AE-12) | – (Rahmenbedingung) |
| T-08 | Stammdatenabgleich muss trotz externem DATEV-Hosting funktionieren | 5.1 | LDconnect mit DATEVconnect und Riecken-Datengateway (AE-07); Klärung mit Hoster (OP-04) | [K] / [O] |
| T-09 | Alle Rechnungen außerhalb der Verwalter in d.velop erfassen, prüfen, freigeben und dem Zahllauf übergeben | 1.4, 5.5 | Standard-Eingangsrechnung mit Zahlungsfreigabe vor DATEV-Übergabe; Zahllauf über DATEV und multicash (WF-01; AE-06; AE-10) | [S] / [K] |
| T-10 | Transparente, konsolidierte Kreditorensicht über Livos und Hausverwaltungen | 5.4, 4.1 | Konsolidierungsnummer am Beleg, gespeicherte Suche über alle Gesellschaften; optional PM-Buchungsdaten ins BI (AE-09; AE-19; S-16) | [A] |
| T-11 | Prozess für Rechnungen mit unbekannter Kreditornummer | 2.3 | Klärfall im Schritt Verteilung mit Zuständigkeit R-02 (WF-04) | [K] |
| T-12 | Neue Lieferanten werden der später in DATEV angelegten Kreditornummer automatisch zugeordnet | 5.1, 5.4 | Täglicher Sync und automatisches Mapping in der Lieferanten-App; Beleg läuft danach weiter (S-02; S-05) | [K] / [A] |
| T-13 | Von Hausverwaltungen gebuchte Rechnungen über einer Größenordnung durch Asset Management freigeben, ohne Buchung und Zahlung | 4.1 | Eigener Freigabeworkflow mit eigenem Postfach, Endstatus „Freigegeben"/„Abgelehnt" (Kap. 11; WF-03) | [K] / [A] |
| T-14 | Auch für HV-Rechnungen: sehen, wo die Rechnung liegt; Vollständigkeit; Einsicht durch Vertreter | 3.2, 3.4, 4.1 | Rechnungseingangsbuch mit Status und aktuellem Schritt, Vertretung (AE-16; AE-17) | [S] |
| T-15 | Nachvollziehen, ob ein Wert aus dem Dokument oder aus den Stammdaten stammt (z. B. IBAN) | 2.2 | Erkannte Belegwerte und Stammdaten in der Verteilungsmaske gegenüberstellen (Kap. 14, M-02); Verhalten im Test prüfen (T25) | [S] / [O] |
| T-16 | IBAN der Rechnung mit Stammdaten abgleichen, Hinweis bei Abweichung | 2.6 | IBAN-Hinweis in der Maske; Negativtest mit abweichender IBAN (Kap. 9; T25) | [S] / [O] |
| T-17 | E-Mail-Benachrichtigungen abschaltbar; Arbeit nur über die Aufgabenliste | 3.1 | Aufgabenliste und REB-Schnellzugriffe als Arbeitsmittel; Benachrichtigungen je Benutzer abschaltbar (Kap. 10.6) | [S] |
| T-18 | Fälligkeit wahlweise aus der Rechnung oder aus den Stammdaten, manuell änderbar | 2.2, 1.8 | Fälligkeit aus der Zahlungsbedingung, Hinweis bei Abweichung vom Beleg; Regel je Entscheidung ED-11; Änderung mit Protokoll (Kap. 9) | [S] |
| T-19 | Mandant automatisch aus dem Beleg erkennen und der Mandantennummer zuordnen | 2.2, 1.1, 5.1 | Erkennung über Name und Anschrift plus Maßnahmenbündel (Alias, BT-10, Lieferantenanschreiben, Klärfall); Test mit echten Belegen (AE-23; T28–T30) | [K] (Vorbehalt) |
| T-20 | Weitere Dokumente als Nachweis an die Rechnung anhängen | 1.7 | Anlagen am Beleg, Kategorie Rechnungsanlage/Nachweis, Mehrfachablage in Akten (Kap. 7, 12; K-02) | [S] |
| T-21 | Option: Buchungsschritt nur für die Steuerberatung bzw. Trios | 1.5 | Buchhaltungsschritt nur für Gruppe Buchhaltung (R-06); Entscheidung ED-12 (Kap. 13) | [K] |
| T-22 | Option: Zahlung mit dem Buchen automatisch auslösen | 5.5 | Automatische Zahlung beim Buchen nicht empfohlen; stattdessen Zahlungsfreigabe in d.velop vor der DATEV-Übergabe, Ausführung mit Unterschrift in multicash (AE-06; AE-10; ED-13) | [S] / [A] |
| T-23 | Durchlauf- und Liegezeiten je Schritt und Benutzer auswerten | 3.2 | Aktueller Stand im REB; Historie über Protokoll aller Schrittwechsel in evidanza (Kap. 16; AE-16; S-12) | [S] / [A] |
| T-24 | Auswertungen in evidanza auf Basis der d.velop-Daten | 3.2, 5.4 | Staging-Schicht und evidanza-Modell (Kap. 16; S-12) | [A] |
| T-25 | Zeitvorgaben je Prüfer und Schritt, danach Eskalation | 3.3 | Statische und fälligkeitsabhängige Eskalation, zwei Stufen, Empfänger je Mandant (Kap. 10; AE-17; T26) | [S] / [K] |
| T-26 | Rückweisung mit vorgefertigter, anpassbarer E-Mail an den Lieferanten, ca. 5 Standardgründe, Adresse automatisch | nahe 2.6 | Ablehnen mit Pflichtgrund, Vorlagen-Mail an die Kreditorenadresse, Ablage in der Kreditorenakte (Kap. 9; WF-05; AE-13; S-11) | [K] / [A] |
| T-27 | Dubletten aus Doppeleingang ohne Lieferantenmail ablehnen | 2.6 | Duplikatsprüfung, interne Ablehnung, Annahme nur mit Begründung (Kap. 9; AE-13) | [S] |
| T-28 | Freigaben auch für Vorgänge ohne Rechnung, z. B. Ausbuchungen auf Mietkonten | 6.1, 1.4 | Freigabeprozesse in process studio (WF-09, Phase 5) | [K] |
| T-29 | Rechnungen kürzen, z. B. wegen mangelhafter Leistung | 1.8 | Zahlbetrag mit Pflicht-Kürzungsgrund und Notiz; Original bleibt unverändert (Kap. 9; AE-14) | [K] |
| T-30 | Positionsweise Kürzung mit automatischer Neuberechnung; Original bleibt erhalten | 1.8, 1.6 | Zahlbetrag auf Positionsebene mit Neuberechnung; Verarbeitung in DATEV mit Trios klären (AE-14; OP-05; T24) | [K] / [O] |
| T-31 | Bei Abschlagsrechnungen die bereits akzeptierten Beträge früherer Abschläge sehen | 5.2 | Vorgangsakte je Auftrag mit allen Abschlägen und Zahlbeträgen; ab Phase 3 Prüfergebnis aus BIM4You (AE-19; K-13; WF-02) | [K] / [A] |
| T-32 | Kumulierte Abschlagsrechnungen automatisch gegen geleistete Zahlungen prüfen | 5.2, 5.3 | Prüfung in BIM4You, Ergebnis und Einbehalt zurück an den Beleg (AE-11; S-08; S-09) | [A] |
| T-33 | E-Rechnung: Rückgabe und Neuanforderung statt Streichungen | 2.4 | Formale Fehler: Rückweisung mit Grund; Leistungskürzung: Zahlbetrag, Rechnung bleibt gültig (AE-14; WF-05) | [K] / [A] |
| T-34 | Bei Bau-Rechnungen prüfen, ob eine Freistellungsbescheinigung vorliegt (am Kreditor hinterlegt) | 2.7, 2.6 | FSB in der Kreditorenakte, FSB-Status je Kreditor und Gesellschaft, Hinweis bzw. Klärfall mit Einbehaltsvorschlag (AE-15, Phase 3) | [A] |
| T-35 | Standardfunktionen vor Middleware; keine eigenen Middleware-Tabellen bei Livos | übergreifend | Designprinzipien P2 und P3; BeSync nur mit klarer Abgrenzung und Betrieb durch MDIS (Kap. 5; Kap. 15) | Leitprinzip |
| T-36 | Kategorie, Gesellschaft, Kreditor und Objekt auch bei sonstigen Dokumenten automatisch erkennen | 6.1, 2.2 | KI-Trennung und -Klassifizierung im Posteingang; Metadaten-Vorschläge im Test prüfen (Kap. 12; WF-07; AE-21) | [S] / [O] |
| T-37 | Mehrstufige Aktenhierarchie mit mehr als zwei Ebenen | 6.1 | Aktenplan mit bis zu 4 Ebenen: Gesellschaft, Objekt, Vorgang bzw. Kreditor (Kap. 7; AE-19) | [K] |
| T-38 | Unterschiedliche Rechnungsworkflows | 1.4 | Workflows je Prozesstyp (WF-01 bis WF-04), Gesellschaftsunterschiede über die Freigabematrix (AE-04; AE-05) | [K] |
| T-39 | Vertretung, bei Krankheit auch durch Administrator oder Vorgesetzte aktivierbar | 3.4 | Abwesenheit im Benutzerprofil, durch Administrator für Dritte setzbar; Einschränkung bei Gruppenaufgaben (Kap. 10; AE-17; T32) | [S] |
| T-40 | Transparentes Lizenzmodell: Abrechnung nach Aktenanzahl oder Dokumentgröße? | Lizenz | Weder noch: d.velop documents pro Benutzer und Monat, d.velop invoices nach Rechnungsvolumen und Buchhaltungsusern; Speicher je Tenant enthalten (Kap. 5; AE-02) | [S] |
| T-41 | KI-gestützte Fragen an Verträge, z. B. „Ist Skonto vereinbart?" | Umfeld 6.1 | d.velop pilot (ab Edition business); Test mit langem Vertrag (AE-20; AE-27; T35) | [S] / [O] |
| T-46 | KI-Plattform auch für die bestehende App und die Middleware nutzen | 5.4 | MDIS X.One für Kreditorenkonsolidierung und Analysen über BeSync-Daten (AE-27) | [A] |
