# Livos – DMS auf Basis d.velop: Zusammenfassung und Fazit

**Kunde:** Livos Gruppe · **Erstellt von:** MDIS Consulting · **Stand:** 26.09.2026 · **Version:** 0.9 (Entwurf zur Abstimmung)
**Begleitdokumente:** „Livos – DMS-Gesamtkonzept d.velop" (Dokument 2) · „Livos – DMS-Konzept d.velop.drawio" (Dokument 3, alle Sichten und Masken)

> Das Dokument hat zwei Teile. **Teil A** ist für Livos bestimmt. **Teil B** ist ein interner MDIS-Teil (Angebot, Korrekturen, Risiken) und wird **nicht** an Livos weitergegeben.

---

# Teil A – Zusammenfassung für Livos

## A1 Worum es geht

Livos will das Rechnungsmanagement und die Dokumentenablage von über 100 Gesellschaften (Bestand, Privatisierung, Bau) auf eine gemeinsame, webbasierte Lösung stellen. Rund 80 interne und externe Anwender, 20–30 Eingangsrechnungen am Tag (5.000–8.000 im Jahr). Die Grundlage sind der Leistungskatalog vom Juli 2026 (29 Anforderungen), der Demo-Workshop vom 22.09.2026 auf der d.velop-Instanz von MDIS und die MDIS-Zielarchitektur (Eingangsrechnungen, Verträge, Post in d.velop; DATEV als Finanzbuchhaltung; BIM4You für das Bau-Budgetcontrolling).

Für das Konzept wurden alle Unterlagen, das Workshop-Transkript und die aktuelle d.velop-Produktdokumentation (Stand 09/2026) in mehreren Prüfschleifen ausgewertet. Jede Aussage zur Lösung ist nach Standard, Konfiguration, Anpassung oder „offen" eingestuft.

## A2 Die zehn Kernaussagen

1. **d.velop deckt den Rechnungsprozess von Livos im Kern mit Standard und Konfiguration ab.** Erfassung aus E-Mail, Scan und E-Rechnung, KI-Erkennung, Dublettenprüfung, sachliche Prüfung, mehrstufige Freigabe mit Wertgrenzen je Gesellschaft, Eskalation, Vertretung, Rechnungseingangsbuch und revisionssichere Ablage sind Produktfunktionen von d.velop invoices und d.velop documents.
2. **Über 100 Gesellschaften laufen in einer Umgebung.** Ein Cloud-Tenant, jede Gesellschaft als eigener Mandant. Rechte, Akten, Freigabewege und DATEV-Übergabe hängen an diesem Mandantenschlüssel. Eine neue Gesellschaft lässt sich in wenigen, automatisierbaren Schritten aufnehmen. Die Mandantenzahl treibt die Lizenzkosten nicht.
3. **Gesellschaftsindividuelle Freigaben entstehen über Regeln, nicht über Kopien.** Eine Freigabematrix legt je Gesellschaft, Kostenobjekt und Betrag fest, wer prüft und freigibt. So bleiben die Workflows wartbar.
4. **Die automatische Zuordnung zur richtigen Gesellschaft ist der kritischste Punkt.** d.velop erkennt den Rechnungsempfänger über Name und Anschrift. Bei Gesellschaften mit gemeinsamer Verwaltungsanschrift reicht das allein nicht. Wir sichern das mit einem Maßnahmenbündel ab: eigene E-Mail-Adresse je Gesellschaft, Lieferantenanschreiben (exakte Gesellschaftsbezeichnung, Käuferreferenz in E-Rechnungen), Klärfallprozess. Vor dem Go-live testen wir das mit echten Livos-Belegen.
5. **DATEV bleibt führend für Buchung und Kreditorenkonten.** Freigegebene Rechnungen gehen ereignisgesteuert, also mehrmals täglich, als Buchungsvorschlag mit Beleglink nach DATEV. Die Stammdaten kommen täglich aus DATEV zurück. Weil DATEV bei einem externen Dienstleister läuft, ist ein Datengateway nötig. Das klären wir früh mit Trios und dem Hoster.
6. **Kreditoren bekommen eine eindeutige Identität über alle Gesellschaften.** Die bestehende Lieferanten-App führt eine gesellschaftsübergreifende Lieferantennummer und verknüpft sie mit den DATEV-Kreditorennummern (intern 70000er) und den Kreditoren der Hausverwaltungen (80000er). Neue Kreditoren legt Livos nicht selbst in DATEV an; die Anlage läuft über einen geregelten Anforderungsweg an Trios.
7. **Zahlungen werden in d.velop freigegeben und in DATEV und multicash ausgeführt.** Die Zahlungsfreigabe liegt vor der DATEV-Übergabe. Der Zahllauf erfolgt über den DATEV-Zahlungsvorschlag und multicash (Omikron) mit Unterschrift der berechtigten Personen. Der Status „bezahlt" wird an den Beleg in d.velop zurückgemeldet.
8. **Rechnungen der Property Manager werden transparent, ohne dass die Hausverwaltungen ein neues System nutzen müssen.** Rechnungen über dem Schwellwert kommen per E-Mail in ein eigenes Freigabepostfach, werden vom Asset Management freigegeben und per E-Mail zurückgemeldet. Keine Buchung, keine Zahlung in d.velop, aber vollständige Nachvollziehbarkeit.
9. **Bau-Spezifika bleiben dort, wo sie fachlich hingehören.** Kumulierte Abschlagsprüfung nach VOB, Einbehalte und Budgetabgleich leistet BIM4You. d.velop steuert den Beleg, übergibt Bau-Rechnungen zur Prüfung an BIM4You und übernimmt das Ergebnis. Nur d.velop übergibt Eingangsrechnungen an DATEV, damit nichts doppelt gebucht wird.
10. **Verträge, Post und allgemeine Ablage folgen auf derselben Plattform.** d.velop contracts für Vertragsakten und Fristen, KI-gestützte Postklassifizierung und -verteilung, Fragen an Dokumente mit d.velop pilot. Dieselben Akten, dieselben Rechte, dieselbe Suche.

## A3 Die Lösung auf einen Blick

| Baustein | Aufgabe | Einstufung |
|---|---|---|
| d.velop invoices (smart invoice, document reader, Rechnungseingangsbuch) | Eingang, Erkennung, Prüfung, Freigabe, Zahlungsfreigabe, Übergabe | Standard + Konfiguration |
| d.velop documents (Cloud, Edition business) | Ablage, Akten, Suche, Rechte, Aufbewahrung, mobile App, Outlook, d.velop pilot | Standard + Konfiguration |
| Option DATEV Rechnungswesen (LDconnect) + Datengateway | Buchungsvorschlag mit Beleglink nach DATEV, Stammdaten aus DATEV | Konfiguration (Zusatzoption) |
| d.velop contracts, process studio, mail dispatcher | Verträge, Sonderprozesse, Postverteilung | Standard + Konfiguration (spätere Phase) |
| MDIS BeSync und Lieferanten-App | Lieferantenidentität, Rückweisungs- und Rückmeldemails, Zahlstatus aus DATEV, BIM4You-Anbindung, Prozessdaten für evidanza, Export je Gesellschaft | Anpassung, von MDIS betrieben |
| DATEV / Trios, multicash (Omikron), BIM4You | Buchung, Zahlungsausführung, Bau-Budgetcontrolling | Umsysteme, bleiben führend |

Der Rechnungsprozess im Überblick: **Eingang → Erkennung und Vorprüfung → Verteilung (ggf. Klärfall) → sachliche Prüfung und Kontierung → (Bau: Prüfung in BIM4You) → fachliche Freigabe nach Matrix → Zahlungsfreigabe → Buchhaltung und DATEV-Übergabe → Zahlung über multicash → Rückmeldung „bezahlt".**

## A4 Abdeckung des Leistungskatalogs

| Einstufung | Anzahl | Katalogpunkte |
|---|---|---|
| Standard (S) | 10 | 1.2, 1.3, 1.7, 1.8, 2.1, 2.4, 2.5, 3.1, 4.3, 6.1 |
| Standard mit Konfigurationsanteil (S/K) | 3 | 2.8, 3.3, 3.4 |
| Standard mit Anpassungsanteil (S/A) | 4 | 1.6, 2.6, 3.2, 5.4 |
| Konfiguration (K) | 6 | 1.1, 1.4, 1.5, 2.2, 2.3, 5.1 |
| Konfiguration mit Anpassungsanteil (K/A) | 2 | 4.1, 4.2 |
| Anpassung (A) | 3 | 2.7, 5.3, 5.5 |
| In d.velop nicht, über BIM4You abgedeckt (N/A) | 1 | 5.2 |

**Alle 21 Must-Have-Anforderungen sind abgedeckt**, keine davon mit „Nein". Fünf Must-Haves enthalten einen Anpassungsanteil, den MDIS über BeSync liefert: Export je Gesellschaft (1.6), Prüfung der Freistellungsbescheinigung (2.6), historische Durchlaufzeiten für das Controlling (3.2), Rückmeldung an Property Manager (4.1) und die Zahlstatus-Rückmeldung im Omikron-Prozess (5.5).

## A5 Was Standard ist – und was MDIS ergänzt

Der Grundsatz lautet: **Standard vor Konfiguration vor Entwicklung.** MDIS ergänzt nur dort, wo der d.velop-Standard endet, und betreibt diese Ergänzungen selbst. Livos pflegt keine technischen Tabellen, sondern nur die fachlichen Lieferantendaten in der bereits vorhandenen Lieferanten-App.

| BeSync-Leistung | Warum nötig | Phase |
|---|---|---|
| Lieferanten-Konsolidierungsnummer an Belegen, Kreditor-Anlageanforderung an Trios | gesellschaftsübergreifende Lieferantensicht, Livos legt keine DATEV-Kreditoren an | 1–2 |
| Rückweisungs- und Kürzungsmails an Lieferanten, Rückmeldung an Property Manager | d.velop versendet keine E-Mails an externe Adressen aus dem Workflow | 2 |
| Prozessereignisse an evidanza | historische Liege- und Durchlaufzeiten je Schritt und Bearbeiter | 1–2 |
| BIM4You-Anbindung (Hin- und Rückweg) | BIM4You bietet keine veröffentlichte Programmierschnittstelle | 3 |
| Zahlstatus „bezahlt" aus DATEV | Standard meldet den Zahlstatus nicht zurück | 3 |
| Prüfung Freistellungsbescheinigung § 48b | kein Standardfeld, keine BZSt-Schnittstelle | 3 |
| Exportpaket je Gesellschaft (z.B. bei Verkauf) | Export-Schnittstelle filtert nicht nach Gesellschaft | bei Bedarf |

## A6 Kritische Punkte und wie wir sie absichern

| Thema | Absicherung |
|---|---|
| Gesellschaftszuordnung bei gemeinsamer Anschrift | Alias-Postfach je Gesellschaft, Lieferantenanschreiben, Klärfall, Test mit echten Belegen vor Go-live |
| DATEV beim externen Hoster | Datengateway und DATEV-Komponenten in Phase 0 mit Trios und Hoster beauftragen; neue Kreditoren sind erst am Folgetag in d.velop verfügbar |
| Einzelne Funktionen sind bei d.velop noch Vorschau oder ungeprüft (z.B. „zweite Freigabe ab Betrag X", IBAN-Warnung, Mailkanal der Eskalation) | Standard-Ersatzlösungen im Konzept; Tests in einer eigenen Testumgebung in Phase 0 |
| Rückmeldung aus BIM4You in laufende Belege | Ergebnis kommt als Belegeigenschaft und Prüfbericht; der Zahlbetrag wird in d.velop gesetzt; technische Rückfrage an d.velop läuft |
| Kürzungen | Die Rechnung bleibt unverändert (GoBD). Gekürzt wird über Zahlbetrag und Kürzungsgrund; die Verarbeitung in DATEV stimmen wir mit Trios ab |
| Lizenzrechtliche Einordnung externer Nutzer (Trios, Projektsteuerer) | Klärung mit d.velop vor Angebotsabschluss |

## A7 Entscheidungen, die Livos treffen sollte

1. Betriebsform d.velop Cloud (Empfehlung: AWS-Rechenzentrum Frankfurt, wegen KI-Kontierung und DATEV-Optionen).
2. DATEV-Übergabe einstufig nach der Zahlungsfreigabe (Empfehlung) oder zusätzlich eine frühe Vorerfassung.
3. Führendes System für Bau-Rechnungen: d.velop übergibt an DATEV, BIM4You prüft (Empfehlung).
4. Freigabegrenzen, Freigabeketten und Rollenbesetzung je Gesellschaft bzw. Gesellschaftsverbund.
5. Umfang des Freigabeprozesses für Property-Manager-Rechnungen und die Schwellwerte je Hausverwaltung.
6. Aktenstruktur (Livos liefert die fachliche Ordnerstruktur; Vorschlag: Gesellschaft → Objekt → Vorgang/Vertrag, dazu Kreditorenakte).
7. Standardgründe für Rückweisungen und Kürzungen.
8. Posteingang: zentraler Scan bei Livos oder Scandienstleister.

## A8 Vorgehen und nächste Schritte

| Phase | Inhalt (Vorschlag) |
|---|---|
| 0 Klärung und Setup | Prozess-Workshop (2–3 Stunden) und Detailworkshops, Entscheidungen A7, Testumgebung, DATEV-Komponenten und Gateway, KI-gestützte Lieferantenkonsolidierung als Proof of Concept |
| 1 Rechnungseingang (Pilot) | Standard-Rechnungsprozess mit 3–5 Pilotgesellschaften, DATEV-Anbindung, Klärfälle |
| 2 Rollout | alle Gesellschaften, Property-Manager-Freigabe, Rückweisungsmails, Controlling-Daten für evidanza |
| 3 Bau und Zahlung | BIM4You-Anbindung, Zahlstatus, Freistellungsbescheinigung, externe Ad-hoc-Freigaben |
| 4 Verträge und Post | d.velop contracts, Postverteilung, Ausbau der Ablage |
| 5 Optimierung | KI-Funktionen, weitere Freigabeprozesse (z.B. Ausbuchungen auf Mietkonten), perspektivische ERP-/PM-Anbindung |

Die Einzelheiten stehen in Kapitel 19 des Konzepts; alle Zeitangaben sind Vorschläge.

## A9 Fazit

d.velop ist für Livos eine tragfähige Plattform: Der Rechnungsprozess mit über 100 Gesellschaften lässt sich weitgehend mit Standard und Konfiguration abbilden. DATEV, multicash und BIM4You bleiben in ihren Rollen führend. Die Lücken des Standards sind klar benannt, begrenzt und werden von MDIS über die bei Livos bereits eingesetzte BeSync-Plattform geschlossen. Entscheidend für den Erfolg sind drei Dinge: eine belastbare Gesellschaftszuordnung, eine saubere Kreditoren-Stammdatenbasis und eine früh geklärte DATEV-Anbindung beim Hoster. Alle drei gehen wir in Phase 0 an, bevor der erste produktive Beleg läuft.

---

# Teil B – Intern MDIS (nicht an Livos weitergeben)

## B1 Korrekturbedarf an Aussagen aus dem Workshop vom 22.09.2026

| Aussage im Termin | Richtigstellung | Umgang |
|---|---|---|
| Kürzungen: Rechnung „lokal bearbeiten", Positionen in der Rechnung ändern [00:41:47–00:44:32] | Nicht GoBD-konform (§ 146 Abs. 4 AO; bei E-Rechnung ist das XML das Original). Kürzung über Zahlbetrag (Kopf/Position) + Kürzungsgrund, Rechnung unverändert. „Lokale Umgebung" ist für eine Cloud-Lösung ein Widerspruch zu Katalog 1.2 | Im Konzept korrekt dargestellt (AE-14); im nächsten Termin aktiv ansprechen |
| Durchlaufzeiten/Liegezeiten: „kann d.velop nicht abdecken" [00:36:13] | Zu pessimistisch: Rechnungseingangsbuch zeigt „Aktueller Schritt seit", „Zugewiesen", Status; CSV-Export. Nur historische Auswertung je Benutzer braucht BeSync/evidanza | Katalog 3.2 = S/A |
| KI-Fragen an Verträge: „nicht über d.velop direkt" [01:09:07] | d.velop pilot kann Fragen zu Dokumenten beantworten (ab Edition business); Tokengrenze bei langen Dokumenten testen | Positiv korrigieren |
| Mandantenerkennung: „Das ist korrekt" [00:31:41] | Erkennung nur über Name + Anschrift; bei gemeinsamer Anschrift riskant | Katalog 2.2 = K mit Vorbehalt, Test mit echten Belegen |
| E-Mail aus d.velop: mal ja, mal nein [00:22:19 / 00:40:42 / 00:47:29] | Kein Versand an externe Adressen aus smart invoice/process studio; Lösung über BeSync (klein) | Einheitlich kommunizieren |
| Freistellungsbescheinigung: „geht alles über d.velop" [00:48:57] | Nur manuell im Standard; automatische Prüfung = BeSync | Katalog 2.7 = A |
| Kumulierte Abschläge: „alles möglich" [00:46:22] | Nicht in d.velop; fachlich in BIM4You | Katalog 5.2 = N (d.velop) / A (über BIM4You) |
| Lizenz nach Akten/Dokumentgröße? [01:08:13] | Nicht nach Akten: invoices nach Rechnungsvolumen + Buchhaltungsuser (Freigabeuser beliebig), documents je Benutzer, Speicher je Tenant | Im Angebot transparent darstellen |
| Omikron wurde im Termin nicht angesprochen | Zielprozess: DATEV-Zahlungsvorschlag → multicash; Rückmeldung über BeSync | Im Angebot als A ausweisen |

## B2 Vor dem Versand des Leistungskatalogs

- Spalte F auf die neue Bewertung (Konzept Kapitel 4) umstellen. Wesentliche Änderungen gegenüber dem bisherigen Stand: 1.4 S→K, 1.5 S→K, 2.2 S→K, 5.1 S→K, 3.2 S→S/A, 1.6 S→S/A, 2.6 S→S/A, 2.7 N→A, 4.1 N→K/A, 4.2 leer→K/A, 5.3 leer→A, 5.4 leer→S/A, 5.5 leer→A, 5.2 N→N/A (BIM4You).
- **Blatt „Tabelle1" (interne MDIS-Hypothesen) vor Versand löschen.**
- Livos hatte den ausgefüllten Katalog zum Termin noch nicht erhalten [01:11:36] – mit dem Angebot senden.

## B3 Lizenz- und Kostenindikation für das Angebot (Listenpreise, AWS-Cloud, Stand 09/2026, ohne Rabatte, zur Orientierung)

| Baustein | Listenpreis | Indikation Livos |
|---|---|---|
| d.velop invoices Medium (750 Rechnungen/Monat, 10 Buchhaltungsuser, Freigabeuser beliebig) | 680 €/Monat; Mehrmenge 0,69 €/Rechnung; weiterer Buchhaltungsuser 17 €/Monat | ca. 8.160 €/Jahr (Alternative Small + Mehrmenge 5.460–7.530 €/Jahr) |
| Option DATEV Rechnungswesen | Preis nicht öffentlich | bei d.velop anfragen |
| LDconnect DATEV ReWe Enterprise (75 Mandanten, 3.000 Rechnungen/Monat) | 1.035 €/Monat + 3,45 €/Mandant/Monat darüber | ca. 1.155 €/Monat bei ~110 Mandanten; ob in der d.velop-Option enthalten: klären |
| DATEV Beleganzeige Drittanbieter | einmalig 1.575 € + Staffel | über Steuerberater/Trios |
| DATEVasp Zusatzmodul Anbindung Drittanbieter | 30,75 €/Monat | falls DATEVasp |
| d.velop documents platform edition business | 39 €/Benutzer/Monat | 20 Vollnutzer ≈ 9.360 €/Jahr; alle 80 ≈ 37.440 €/Jahr |
| d.velop contracts | 9 € (lesend) / 29 € (voll) je Benutzer/Monat | Phase 4 |
| d.velop pilot | in business/ultimate enthalten (Kontingente) | – |

Zusätzlich: Einführungsleistung MDIS, BeSync-Entwicklung und -Betrieb (A-Anteile, siehe A5), Testumgebung (Lizenzierung bei d.velop klären).

## B4 Rückfragen an d.velop (vor Angebotsabgabe)

1. Dürfen Dritte (Trios, Projektsteuerer, Property Manager) als Buchhaltungs- bzw. Freigabeuser lizenziert werden?
2. Preis Option DATEV Rechnungswesen; ist LDconnect enthalten; Kosten ab 75 Mandanten.
3. Betriebsform der Demo-Instanz; Verfügbarkeit aller Funktionen in C1.
4. Status Vorschau-Feature „Vier-Augen ab Betrag X"; Schreibzugriff per API auf laufende smart-invoice-Belege (Zahlbetrag nach BIM4You).
5. Zählt smart invoice auf das process-studio-Kontingent (1.000 Ausführungen/Monat in business)?
6. IDW PS 880 / C5 für die Cloud; Lizenzierung eines Test-Tenants; Freischaltung repo export-API.

## B5 Risiken für MDIS

- **Middleware-Skepsis bei Livos** [00:40:13, 00:49:28]: BeSync-Anteile klein, klar abgegrenzt und als von MDIS betriebene Leistung verkaufen – nicht als Pflegeaufgabe für Livos.
- **Wettbewerb:** Livos vergleicht Anbieter; Wettbewerber (z.B. DocuWare) holen OPOS/Zahlstatus aus DATEV im Standard und haben eine BIM4You-Referenz. Unser Vorteil: bestehende BeSync-/BI-Integration und Stammdaten-App bei Livos, KI-Kreditorenkonsolidierung.
- **Terminzusagen:** Angebot „diese Woche" zugesagt; Prozess-Workshop und KI-PoC angeboten, aber nicht terminiert – aktiv nachfassen.
- **Datenschutz im Kundenordner:** Der Ordner „Livos" enthält den Haufe-X360-Snapshot „Mocca_V14_108.zip" (Demo-Firma, keine Livos-Daten) mit Passwort- und Tokenfeldern sowie Login-Protokoll. Nicht an Livos weitergeben, aus dem Kundenordner entfernen. Er wurde bewusst nicht in dieses Repository übernommen.

## B6 Wie dieses Ergebnis entstanden ist

Sechs Extraktionsanalysen (Transkript, Anforderungen, Demo-Aufbau, d.velop-Recherche A/B, ERP-Snapshot), sechs Web-Recherchen (DATEV/Zahlung, Externe/Lizenz/KI, Rechnungsdetails/Bau, Verträge/Post/Archiv, Umsysteme/API, Cloud-Berechtigungen), Audit mit Stichproben gegen die Primärquellen, verbindliche Leitplanken (29 Architekturentscheidungen, ID-Kataloge), Konzepterstellung in sechs Teilen, Konsolidierungsaudit. Offene Punkte sind im Konzept (Kapitel 20) mit Klärungsweg erfasst.
