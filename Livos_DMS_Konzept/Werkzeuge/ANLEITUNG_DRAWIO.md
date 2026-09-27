# Anleitung für draw.io-Seitenautoren (Livos DMS-Konzept)

Verzeichnis: SP/drawio (SP = /tmp/claude-0/-home-user-My/9b9087bc-2d0b-5088-b7bc-148ecd5c6c69/scratchpad)

## Werkzeuge
- `dio.py` – Bibliothek. Lies sie komplett (Stile in `S`/`E`, Klassen `Doc`/`Page`, Bausteine `lanes`, `ui_window`, `ui_field(s)`, `ui_section`, `ui_buttons`, `ui_tabs`, `ui_viewer`, `ui_table`, `ann`, `legend_box`, `status_legend`, `p.header`, `p.table`, `p.box`, `p.edge`, `p.line`).
- `render.py datei.drawio outdir [seitenindex…]` – rendert Seiten als PNG (draw.io-Viewer, headless). **Jede Seite rendern und mit dem Read-Tool ansehen**, Überlappungen/abgeschnittene Texte korrigieren, bis es sauber aussieht.

## Deine Lieferung
Eine Datei `pages_<X>.py` mit Funktion `build(doc)`, die deine Seiten in der vorgegebenen Reihenfolge mit `doc.page(name, pid)` anlegt. Seiten-IDs (`pid`) exakt wie vorgegeben (z.B. "p08"), weil die Übersichtsseite darauf verlinkt. Zum Testen: kleines Skript, das nur deine Seiten in `test_<X>.drawio` schreibt und rendert.

## Gestaltungsregeln
1. Format A3 quer (1654 × 1169). Jede Seite beginnt mit `p.header(titel, untertitel)`. Inhalte zwischen y=110 und y=1120.
2. Farben ausschließlich über die Stile aus `dio.py`. Bedeutung: `dvelop` = d.velop Standard, `dvelop_l` = d.velop Konfiguration, `mdis`/`task_mdis` = MDIS BeSync (Anpassung), `ext`/`task_ext` = Umsystem/extern, `open`/`task_open` = offen. Auf Seiten mit Status-Farben `status_legend(p, x, y)` platzieren.
3. Prozesse als Swimlanes (`lanes`) mit BPMN-nahen Elementen: `start`, `end`, `task`, `gateway` (Text max. 3 Wörter, Frage), `doc`, `db`. Kanten `flow` (Sequenz), `data` (Datenfluss), `msg` (Nachricht extern). Beschriftungen kurz.
4. IDs aus den Leitplanken (AE-, R-, K-, E-, WF-, S-, M-, OP-) in Beschriftungen verwenden, damit Konzept und Diagramm verknüpft sind (z.B. „S-01 Buchungsvorschlag").
5. Masken: `ui_window` + `ui_section`/`ui_fields` links (Belegdaten), `ui_viewer` rechts (Belegvorschau), Schaltflächen unten. Feldarten: `req` Pflicht, `ai` KI-erkannt, `ro` schreibgeschützt, `select` Auswahl, `input` frei. Rechts oder unten nummerierte Annotationen (`ann`) mit Erklärungen (Regel, Quelle, [S]/[K]/[A]). Fiktive Beispieldaten aus den Demo-Testdaten verwenden (Livos Objektgesellschaft Nord mbH, Musterbau GmbH, RE-2026-1041, 14.756,00 €, BV Hafenstraße 22 …).
6. Keine Texte außerhalb der Boxen überlaufen lassen: Boxgrößen großzügig wählen; lange Texte in `text`-Boxen mit ausreichender Höhe.
7. Deutsch, Fachbegriffe wie im Konzept. Keine Preise, keine internen MDIS-Hinweise.
