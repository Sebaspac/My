# 22 — Audit-Bericht Konsolidierung Livos-DMS-Gesamtkonzept (K01, K03–K21)

Stand: 26.09.2026 · Grundlage: 20_LEITPLANKEN.md (Zählung §5 korrigiert: S 10, S/K 3, S/A 4, K 6, K/A 2, A 3, N/A 1 = 29), 21_AUDIT_NOTIZEN.md · K02 (Lead) nicht bearbeitet, nur gegengelesen.

## 1. Befunde und Korrekturen

| ID | Kapitel | Befund | Korrektur |
|---|---|---|---|
| AB-01 | K04, K02 | Zählung Katalogbewertung gegen Leitplanken-§5 geprüft: K04 4.3.1/4.3.2 und K02 bereits korrekt (10/3/4/6/2/3/1 = 29; Must 7/3/3/6/1/1/0). | ja (nichts zu ändern) |
| AB-02 | K05, K06, K08, K09, K11–K13, K15–K17 | Katalogbewertungen außerhalb K04 gegen §5 geprüft (1.1, 1.5, 1.6, 2.2, 2.7, 2.8, 3.2, 3.4, 4.2, 4.3, 5.1–5.5, 6.1): alle identisch. | ja (nichts zu ändern) |
| AB-03 | K07, K13, K17, K18 | Kategorie „Organisationsunterlage" nur in K13/K17/K18 ohne ID. Als **K-15** in K07 aufgenommen (Kategorienkatalog, Zuordnungsmatrix, Aktenplan/Regel S10, Aufbewahrung 10 Jahre nach § 147 Abs. 1 Nr. 1 AO / § 257 Abs. 1 Nr. 1 HGB); K13 Berechtigungsmatrix um Spalte K-15 ergänzt (Mengengerüst 15 Kategorien); K17/K18 auf „K-15" umgestellt. | ja |
| AB-04 | K03, K04, K05, K15, K19, K02 | Phase S-06 (Zahlstatus) uneinheitlich (K03/K04/K15: 2; K05/K19/K02: 3). Einheitlich **Phase 3** (Voraussetzung OPOS-Zugriff OP-04/OP-43, T40 „vor 3"). K03, K04, K15 angepasst; K16 ergänzt: KPI-05/07/08 erst ab Phase 3. | ja |
| AB-05 | K03, K04, K19, K20 | S-12: Protokollierung **ab Phase 1 (Pilot-Go-live)**, evidanza-Berichte **Phase 2**. K19 Phasenübersicht und Phase-1-Tabelle ergänzt, Hinweis 19.2.4 und RI-19 („ab erstem Rollout-Schritt") korrigiert; K03/K04 präzisiert. | ja |
| AB-06 | K03, K04, K15, K19 | S-15 (Export je Gesellschaft): K15 Phase 1/2, K19 Phase 3, K04 „bei Bedarf". Einheitlich: Voraussetzung P1 ab Phase 1, **Exportskript Phase 2** (Katalog 1.6 ist Must). K19 (Übersicht, 19.2.4/19.2.5, QG-2) und K03/K04 angepasst. | ja |
| AB-07 | K03, K08, K15, K19 | Zusätzlicher Phasenkonflikt S-04/S-05: K03/K15 Phase 1, K19 Phase 2 (Phase 1 nur Erstimport bzw. E-Mail-Anforderung an Trios). An K19 angeglichen: Phase 1 Erstbefüllung/manuelle Anforderung, Phase 2 Automatik. K08 („konsolidierte Sicht ab Go-live") präzisiert. | ja (fachlich bestätigen, siehe 2.) |
| AB-08 | K05, K09, K14, K15, K21 | Mailversand S-11 uneinheitlich („Microsoft Graph"). Überall „Microsoft Graph oder d.velop-Messaging-API (Festlegung in Phase 0, OP-25)"; technischer Benutzer in K15 15.5.3 und Glossar angepasst. | ja |
| AB-09 | K20, K13, K15, K17, K18 | Offene Punkte ohne ID aus K13–K18 aufgenommen: **OP-43** Zahlstatus-Abgleichsschlüssel/OPOS-Ressource, **OP-44** Einfluss auf Cloud-Updates, **OP-45** Lizenz temporärer Betriebsprüfer R-14, **OP-46** Aufbewahrung PM-Freigaberechnungen. Bereits vorhanden: Auslöser-Benutzer (OP-26), Aktivitätenprotokoll (OP-32), Belegfeld 2 (OP-22). Quellstellen mit OP-Nummer verlinkt. | ja |
| AB-10 | K13 | Ungültige Verweise „O-13" (Lizenz Betriebsprüfer) → OP-45. | ja |
| AB-11 | K09, K10 | Ungültige Verweise „OP O-12" → OP-41, „OP O-07" → OP-26. | ja |
| AB-12 | K10, K09, K20 | Vorschlag „Zahlungsfreigeber ≠ letzter fachlicher Freigeber" ohne Test → neuer Test **T41**, in K09/K10 referenziert. | ja |
| AB-13 | K11, K13, K14 | Widerspruch externe Ad-hoc-Freigabe: K11 „nur Stellungnahme", K13 R-10 und K14 M-19 „Einzelfreigabe/setzt die Freigabe". An K11 angeglichen (Stellungnahme, verbindliche Freigabe intern; OP-39 referenziert). Abweichung vom Leitplanken-Wortlaut R-10 „Einzelfreigabe" – begründet durch fehlende Authentifizierung am Formular. | ja |
| AB-14 | K21, K04, K10, K12 | T-Status K21 vs. K04/Fachkapitel: T-15 einheitlich [S]/[O]; T-17 auf [S] (K10: abschaltbar, Standard); T-36 einheitlich [S]/[O] (K12: KI-Klassifizierung Standard, Metadaten offen; K04 angepasst). Weitere Einzelabweichungen in K21 an K04 angeglichen: T-07, T-08, T-09, T-18, T-22, T-26, T-29, T-30, T-31, T-37. | ja |
| AB-15 | K06, K15, K20 | Bucket-Limit Sachkonten (55.000 > 50.000) uneinheitlich dargestellt (K15: mehrere Buckets als gleichwertige Option; K20 RI-07 W = g). Einheitlich: Mengengerüst (OP-21) → nur genutzte Konten/Sachkonten ohne Mandantenbezug (OP-22) → Erhöhung → mehrere Buckets nur als letzte Option (OP-04). RI-07 auf W = m. | ja |
| AB-16 | K06, K08, K15 | LDconnect-Funktionsfragen (untertägiger Sync, Filter, Fehlerverhalten) auf OP-04 statt OP-22 verwiesen; korrigiert. Dynamische Wertemengen/REB-Mehrfachmandant auf OP-40/T19 bzw. T20 statt OP-08. | ja |
| AB-17 | K08, K13, K14, K15 | „Nur LDconnect schreibt in den Bucket": K14 M-16 und K13 13.9.1 widersprachen K08 8.7/K15 L2 (BeSync schreibt Mandanten und ergänzende Entitäten). Einheitlich: DATEV-Stammdaten nur LDconnect; BeSync nur Mandanten, Custom Entities, DMS-Eigenschaften. | ja (Präzisierung ggü. Leitplanken-Wortlaut AE-09, bitte bestätigen) |
| AB-18 | K09, K13, K10 | Gruppennamen uneinheitlich (`SI_Clearing` vs. `SI_Clearing_Zentral`; `SI_Zahlungsfreigabe_<Nr>` vs. `SI_Zahlung_<Verbund>`; `SI_Freigabe…` vs. `SI_Freigeber…`). Vereinheitlicht auf `SI_Clearing_Zentral`, `SI_Zahlung_<MandantNr>` (bzw. je Verbund), `SI_Freigeber_<MandantNr>`. | ja |
| AB-19 | K10, K13 | Beispiel-Mandanten-IDs uneinheitlich (10001, 1001 vs. 10010 in K06/K07/K08). Auf fünfstelliges Schema (10010, 10020, 10050) umgestellt; Test-Beispiel T08 (`100` gegen `1001`) bewusst belassen. | ja |
| AB-20 | K09 | WF-04/WF-05 „keine eigenständigen Workflowdefinitionen" widersprach AE-04/K06. Umformuliert: fachlich eigene Prozesse mit ID, technisch als Schritt/Pfad in WF-01 bis WF-03, eigene Definition für Klärfall möglich. WF-04 = Klärfall durchgängig geprüft. | ja |
| AB-21 | K09 | Pilot-Bau: K09 „WF-02 ohne Transfer" vs. K19/Leitplanken „WF-01 ohne BIM4You-Automatik". An K19 angeglichen. | ja |
| AB-22 | K12, K07 | Aufbewahrung FSB/Bescheinigung: K12 P-07 „6 Jahre" vs. K07 K-06 „8 Jahre". Auf 8 Jahre angeglichen; Hinweis zu K-09-Fristen (6 Jahre bis zur Feinaufteilung). | ja |
| AB-23 | K07, K11, K17 | Aufbewahrung PM-Freigaberechnungen (keine Buchungsbelege) offen: Hinweis in K07, Zeile in K17 17.2.1, Verweis in K11; vorsorglich Frist wie K-01 bis Festlegung (OP-46). | ja |
| AB-24 | K18, K08, K07 | Pflege Rückweisungs-/Kürzungsgründe: K18 „Pflege durch MDIS" vs. K07/K08 „Fachadministration". Auf R-12 angeglichen (MDIS nur Mailvorlagen). | ja |
| AB-25 | K11 | Interne Verweise im Kundendokument: „Leitplanken Kap. 5", „Option D der Umsystem-Recherche", „Umsystem-Recherche". Ersetzt durch Kapitel 4.2, S-16, OP-29. | ja |
| AB-26 | K09, K10, K12 | MDIS-interne Korrekturen eigener Workshop-/Demo-Aussagen („im Workshop genannte lokale Bearbeitung", „Demo-Dokumentation sprach von brutto", „Workshop-Aussage … wird präzisiert"). Neutral umformuliert. | ja |
| AB-27 | K08, K15, K20 | Konditions-/Vertriebshinweise: „kostenloser PoC", „MDIS verfügt aus einem anderen Projekt …", „aus den Recherchen", „Sekundärquelle". Neutralisiert. Preise: keine im Konzept gefunden (nur „Konditionen im Angebot"). | ja |
| AB-28 | alle | Terminologie §0.7 geprüft („Develop", „Smart Invoice", „dvelop" u. ä.): keine Abweichung. Personennamen: nur André Töpper. Interne Dateipfade: keine. | ja (nichts zu ändern) |
| AB-29 | K11 | Quellenstand „process studio Handbuch 2026.q3" widerspricht Quellenverzeichnis Q-30 (2026.q2). Korrigiert. | ja |
| AB-30 | K18 | Verweis „Change-Prozess (18.6)" zeigt auf Change-Management/Kommunikation. Korrigiert auf 18.3 bzw. Change-Board (19.7.2). | ja |
| AB-31 | alle | Querverweise „Kapitel/Kap. x.y" automatisiert gegen die Überschriften geprüft: alle Ziele existieren. | ja (nichts zu ändern) |
| AB-32 | alle | Überschriftenebenen `# N`, `## N.M`, `### N.M.K` konsistent (K14 mit Abschnitt 14.0 zulässig). | ja (nichts zu ändern) |
| AB-33 | K01 | ID-Systematik ohne RI, ED, KPI und ohne Unterscheidung Workshop-Anforderung (T-xx) vs. Plattformtest (Txx). Ergänzt. | ja |
| AB-34 | K04, K05, K12, K13, K16 | Fehlende OP-Verweise bei [O]-Aussagen ergänzt (OP-38 mobile Freigabe, OP-40 Obergrenzen, OP-26/OP-27 evidanza, OP-24 multicash, OP-28, OP-29, OP-42). | ja |
| AB-35 | Leitplanken §4.2 | Leitplanken-Katalog K kennt nur K-01 bis K-14; K-15 ist neu. | nein (Leitplanken/FAZIT durch Lead nachziehen) |
| AB-36 | draw.io | Audit-Notiz 12 (Roadmap 18 vs. 12 Monate, KPI-Nummern, Matrix p18) betrifft die draw.io-Datei; sie liegt nicht im Arbeitsverzeichnis. Zusätzlich nachzuziehen: K-15, S-06 Phase 3, S-12/S-15 Phasen, M-19 „Stellungnahme". | nein (Datei nicht verfügbar) |
| AB-37 | K12 | Unter-IDs OP-12.1 bis OP-12.8 für contracts-Fragen: keine Doppelbelegung, aber abweichendes ID-Format. | nein (vertretbar; bei Bedarf in OP-12 zusammenfassen) |

## 2. Verbleibende Punkte mit fachlichem Entscheidungsbedarf

| Nr. | Thema | Stand im Konzept | Entscheidung durch |
|---|---|---|---|
| 1 | Phase S-04/S-05 (Lieferanten-App-Automatik) | Phase 1 manuell/Erstimport, Automatik Phase 2 (nach K19). Alternative: Automatik bereits Phase 1 (höheres Pilotrisiko, frühere Konsolidierungssicht). | Lead / Livos |
| 2 | Phase S-15 (Exportskript) | Phase 2 gesetzt (Audit-Notiz); vorher war Phase 3 in K19. Bei Ressourcenengpass in Phase 2 zurück nach Phase 3 mit „vorziehen bei Verkaufsanlass". | Lead |
| 3 | Bucket-Schreibregel AE-09 | Konzept präzisiert: „je Objekttyp ein Schreiber" (BeSync schreibt Mandanten/Custom Entities). Leitplanken-Wortlaut „nur LDconnect schreibt" anpassen. | Lead |
| 4 | Externe Ad-hoc-Freigabe (R-10, WF-10, Katalog 4.2) | Nur Stellungnahme, verbindliche Freigabe intern. Bewertung 4.2 = K/A bleibt; Livos sollte bestätigen, dass dies die Anforderung „Freigabe per Link ohne Lizenz" erfüllt. | Livos |
| 5 | Aufbewahrung PM-Freigaberechnungen | vorsorglich 8 Jahre bis Festlegung (OP-46). | Livos, Steuerberatung |
| 6 | K-15 Mandantenzuordnung gruppenweiter Organisationsunterlagen | Vorschlag Obergesellschaft als Mandant. | Livos |
| 7 | Mail-Technik S-11 | Graph oder d.velop-Messaging-API, Festlegung Phase 0 (OP-25). | MDIS / d.velop |
| 8 | RI-07 Bucket-Limits | W auf „m" angehoben; tatsächliche Mengen erst nach OP-21. | MDIS, Trios |
