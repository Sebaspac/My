# 15 – Web-Recherche: Struktur, Berechtigungen und Administration in der d.velop **Cloud**

Stand: 26.09.2026 · Arbeitspaket 15 · Anlass: Audit-Befund „Struktur- und Rechte-Mechanismen nur für On-Premises (d.3 admin) belegt" (vgl. [04a §3.3, §4, §9 G03/G04/G10/G13/G16/G17, §10 R-01/R-02/R-07/R-10]; [03 §5.3 G6/G9/G19/G24, §7 Nr. 20])
Methode: Öffentliche d.velop-Quellen (help.d-velop.de inkl. Such-Index, Entwicklerportal/OpenAPI, Vertragsunterlagen im d.velop cloud center, d.velop store, KB-Titel), Microsoft Learn. Keine Anmeldung am Service-Portal. Lokale Kopien aller ausgewerteten Dokumente: `SP/work/_web15/` (u. a. `dmsconfig.yaml`, `fb_documents_mycloud.txt`, `lb_documents_cloud_2025-02-18.txt`, `um_cloud.txt`, `smart-invoice-cloud.txt`, `smart-invoice-developer.txt`, `contracts-admin-cloud.txt`, `custom-logics-admin.txt`).

---

## 0. Kurzfazit (Antwort auf den Audit-Befund)

1. **Der zentrale Cloud-Beleg ist die öffentliche „DmsConfig API"** (OpenAPI, Version v1). Sie ist laut eigener Beschreibung „designed for configuring d.velop documents repositories in the cloud" und „exclusively available in the cloud environment" [Q01]. Sie beschreibt das Cloud-Objektmodell vollständig: Kategorien, Eigenschaften, Wertemengen (Datasets), **Berechtigungen (Permissions) mit Einschränkungen**, **Restriction Sets** (dynamische, gruppenabhängige Wertelisten), **Strukturregeln (automatische Aktenbildung)**, **Aufbewahrung und Löschschutz je Kategorie**, Webhooks und Pakete. Damit sind die Kernmechanismen für die Cloud **belegt**, auch wenn das Cloud-Admin-Handbuch „d.velop cloud: Administrieren" nur nach Login lesbar ist [Q26].
2. **Rechte in der Cloud:** Eine *Berechtigung* gilt für **genau eine Kategorie** und kann über weitere Eigenschaftswerte eingeschränkt werden. Sie wird **Gruppen (oder Apps)** mit den getrennten Rechten **Lesen / Schreiben (inkl. Anlegen) / Löschen** zugeordnet, jeweils `ALLOWED | INHERITED | DENIED`. `DENIED` setzt sich immer durch [Q01 PermissionDto, PermissionRestrictionDto, PermissionAssignmentDto]. Die Funktions- und die Leistungsbeschreibung bestätigen das als „Rollen- und Attributbasierte Berechtigungsverwaltung" [Q02 §4.1.6; Q03].
3. **Das Cloud-Äquivalent zu `@D3GROUP`/`@D3SET`** sind die Platzhalter `@CURRENT_USER`, `@CURRENT_USER_EMAIL`, `@CURRENT_USER_IN_GROUP` und `@Filter([Filter-ID])`. Letzterer verweist auf ein **Restriction Set**. Dort erhält jede Gruppe eine Werteliste, z. B. Gesellschafts-IDs. Ein Benutzer ist berechtigt, wenn der Eigenschaftswert in der Liste liegt, die sich aus seinen Gruppenmitgliedschaften ergibt [Q01 Tag „Restriction Sets"]. Damit lassen sich >100 Gesellschaften mit **einer Berechtigung je Kategorie und Rechtestufe** abbilden. Eine Berechtigung je Gesellschaft ist nicht nötig. Achtung: **„An empty array allows all values"** [Q01 RestrictionSetAssignmentDto].
4. **Die On-Prem-Grenzen aus 04a sind in der Cloud weitgehend gegenstandslos.** Eigenschaften, Kategorien und Gruppen werden über IDs (GUID) referenziert. Es gibt **kein Kürzel und keine DB-Position** im Cloud-Objektmodell [Q01 CategoryDto/PropertyDto; 03 §5.3 G6]. Rechte greifen über die Eigenschafts-ID, nicht über eine gemeinsame DB-Position. Die **8-Zeichen-Gruppenregel** ist für die Cloud nirgends belegt. Rechte werden an Gruppen-IDs vergeben. Ob die Regel intern dennoch gilt, ist per Test zu prüfen (T15).
5. **Aktenbildung in der Cloud ist belegt:** Strukturregeln bestehen aus übergeordneter Kategorie, untergeordneter Kategorie, Erkennungseigenschaften (gleichnamig oder als Paar Eltern-/Kind-Eigenschaft) und Vererbung. Dazu kommen die Optionen „Geschwisterakten erzeugen" und „bei Änderung neu zuordnen" [Q01 StructureRuleDto]. Akten werden „automatisch anhand ihrer Dokumenteigenschaften … erstellt, wenn diese noch nicht vorhanden sind". Eine Akte kann in mehreren Akten liegen [Q02 §4.1.2; Q03].
6. **Aufbewahrung in der Cloud ist eine Kategorie-Einstellung:** Frist in Jahren oder Monaten (0 = unbegrenzt), Beginn ab „zuletzt bearbeitet" oder ab einer Datumseigenschaft. Dazu kommt `preventDeletion`: Freigegebene und archivierte Elemente dürfen dann nicht gelöscht werden, und das übersteuert alle Löschrechte. Nach Fristablauf wird trotzdem gelöscht [Q01 CategoryRetentionDto/CategoryProtectionDto; Q02; Q03]. **Legal Hold ist nicht dokumentiert.** Der d.ecs storage manager ist eine On-Prem-Komponente und für die Cloud nicht einschlägig [Q23].
7. **Benutzer und Gruppen:** Die Pflege erfolgt unter *Konfiguration > Dokumentenmanagement > Benutzerkonten- und Gruppenverwaltung > Benutzerkonten und Gruppen* [Q04] bzw. *…> Verwaltung > Benutzerkonten- und Gruppenverwaltung* [Q13]. Es gibt globale Gruppen, Gruppentypen und **SCIM 2.0** (`https://<Tenant>/usermanagement/scim`) [Q04; Q05]. SSO läuft über **OpenID Connect**, dazu kommen AD-Integration (ADFS/LDAP) und weitere OIDC-Provider. **SSO, AD-Integration, Business Objects/Custom Logics und die API gibt es erst ab Edition *business*** [Q03 Editionstabelle]. Microsoft Entra ID wird von d.velop ausdrücklich als möglicher Identitätsanbieter genannt [Q13].
8. **Delegierte Administration** für das DMS ist in der Cloud **nicht belegt**. Die DmsConfig API verlangt **Tenant-Administratoren** [Q01]. Es gibt nur fachliche Teil-Delegationen, z. B. smart-invoice-Berechtigungen, Business-Objects-Rechte je Modell und Supportzugänge [Q07; Q12; Q14].
9. **smart invoice** ist mandantenfähig: Rechnungseingangsbuch global oder **je Mandantennummer und Gruppe**, Clearing-Gruppen je Mandant, Freigabematrix mit Spalte Mandant, Urkel-Bearbeiterfindung über `voucher.company.nr` [Q07]. Die Mandanten-Stammdaten kommen über die Bucket-API [Q08]. Die Verbindung zum DMS läuft über „Zuordnungen": Mandant Nummer, Mandant Name und Workflowbeteiligte sind Pflicht [Q07].

**Konsequenz:** Die Empfehlung aus [04a §3.5] (Option A: ein Repository, Pflichteigenschaft „Gesellschaft", dynamische Rechte) bleibt **richtig**. In der Cloud wird sie aber **nicht** mit Dokumentklassen, `@D3GROUP` und DB-Positionen umgesetzt, sondern mit **Permissions + Restriction Sets + Strukturregeln**. Menüpfade der Cloud-UI für „Berechtigungen" und „Strukturen" sind öffentlich **nicht** dokumentiert und am System zu verifizieren (T01).

### 0.1 Kennzeichnung

- **F-C** = Fakt, belegt durch eine Cloud-Quelle (URL). **F-O** = Fakt, nur On-Prem-Quelle. **F-M** = Fakt aus einer Nicht-d.velop-Quelle (Microsoft).
- **A** = Annahme/Ableitung (nicht als Produkteigenschaft zusagen). **T** = auf der Demo- bzw. Test-Instanz zu prüfen (Testfall in §11). **O** = offen, nicht belegt.
- Zitierweise `[Qnn]` → Quellenverzeichnis (Anhang). Interne Bezüge: `[04a §x]`, `[03 §x]`, `[TR hh:mm:ss Sprecher]`.

---

## 1. On-Prem-Baustein → Cloud-Äquivalent (erledigt Rechercheauftrag R-01 aus 04a)

| On-Prem-Baustein (d.3 admin) [04a] | Cloud-Äquivalent | Beleg / Status | Quelle |
|---|---|---|---|
| Dokumentart / Aktenart mit Kürzel (max. 5, unveränderlich) | **Kategorie** `type = DOCUMENT_TYPE \| DOSSIER_TYPE`, mehrsprachiger Name, **kein Kürzel-Feld** | F-C | Q01 CategoryDto; 03 §1.1 |
| Erweiterte Eigenschaft auf DB-Position 1–89 | **Eigenschaft** (ID, Name, Datentyp, `isMultiValue`, optional Wertemenge, RegEx, Min/Max); **keine Position**. Reihenfolge und Maskenverhalten je Kategorie (`propertyRefs`) | F-C (Position fehlt im Modell). Typgrenzen (z. B. max. 10 Währungsfelder) in der Cloud nicht dokumentiert → **T14** | Q01 PropertyDto, CategoryPropertyRefDto; 03 §5.3 G6, G9 |
| Wertemenge (manuell/DB/Hook/dynamisch) | **Dataset** `STRING/CURRENCY/NUMERIC/DATE/URI (dynamisch)`; System-Datasets `USERS`, `EXISTING_VALUES`; dynamische Wertemengen aus Stammdaten über **custom logics + business objects** | F-C | Q01 DataSetDto, Tag DataSets; Q11; Q02 |
| Dokumentklasse + Berechtigungsprofil | **Permission**: `restrictions` (genau **eine** `CATEGORY` + beliebige Eigenschafts-Filter) + `assignments` (Gruppe/App → read/write/delete) | F-C | Q01 PermissionDto |
| Dokumentartunabhängige Klasse (Restriktion auf DB-Position) | **entfällt**. Einschränkung per Eigenschafts-ID je Berechtigung. Eine Berechtigung gilt aber nur für **eine** Kategorie → je Kategorie eine Berechtigung | F-C (eine Kategorie je Permission: „may occur only once") | Q01 PermissionRestrictionDto |
| `@D3USER` / `@D3USER_EMAIL` | `@CURRENT_USER` (ID) / `@CURRENT_USER_EMAIL` | F-C | Q01 |
| `@D3GROUP` (Eigenschaft enthält Gruppenname) | `@CURRENT_USER_IN_GROUP` = „ID of a group or application in which the logged on user is a member". Vergleich gegen die **Gruppen-ID**, nicht den Namen | F-C; Vergleichssemantik (Gleichheit, Mehrfachwert) → **T02/T04** | Q01 |
| `@D3SET` + d.3 restriction set manager | **Restriction Set** + `@Filter([Filter-ID])`; Zuordnung je Gruppe (`GROUP`) oder für alle (`NO_ASSIGNMENT`) mit Werteliste; leere Liste = alle Werte | F-C | Q01 Tag „Restriction Sets", RestrictionSetAssignmentDto |
| Rechte Lesen/Schreiben/Statustransfer/Verknüpfen/Aktivitäten/Export | **nur read / write / delete** in der API. Status, Verknüpfen, Aktivitäten, Export nicht als eigene Rechte modelliert | F-C (API); ob die UI mehr kennt → **O/T11** | Q01 PermissionAssignmentDto |
| Explizites Verweigern | `DENIED` „will always apply" (je Gruppe/App); Wirkung über mehrere Gruppen eines Benutzers → **T07** | F-C | Q01 |
| Aktenbildung (folder scheme: Erkennung, Vererbung) | **Strukturregel** `parent`, `child`, `recognition[]`, `inheritance[]`, `createSiblingDossiers`, `changeParent` | F-C | Q01 StructureRuleDto |
| Lebensdauer je Dokumentart, storage manager Retention | **Kategorie `retention`** (`period`, `unit`, `basedOn`) + **`protection.preventDeletion`** | F-C | Q01 CategoryRetentionDto, CategoryProtectionDto; Q02; Q03 |
| Hooks (JPL/Groovy), `@D3HOOK` | **Webhooks je Ereignis** (u. a. `validateimport`, `validateupdateproperties`, `predelete`, `prereleasedocument`), einschränkbar auf Kategorien | F-C | Q01 Events/WebHookDto |
| Benutzer/Gruppen in d.3 admin, IdP-Sync stündlich | **d.velop usermanagement** (UMA) + d.ecs identity provider; **SCIM 2.0**; globale Gruppen; Gruppentypen | F-C; Sync-Intervall bei SCIM bestimmt der Sender (Entra) | Q04; Q05; Q20 |
| Sub-Administration | **nicht dokumentiert**; DmsConfig nur für Tenant-Administratoren | O | Q01 (403-Hinweis) |
| Transport (d.3 admin Transportsystem) | **Packages** („metadata …, structures, authorizations, and webhooks") per API installierbar; custom logics mit Paketverwaltung; usermanagement-Backup „nicht als Transportsystem" | F-C (Install); Export-Weg der DMS-Konfiguration → **O/T23** | Q01 Tag Packages; Q11 §1.7; Q04 §1.3.1 |
| Repository-ID (Speicher-Pool) | kein Cloud-Pendant dokumentiert; Speicher je Mandant: 100/1.000/2.000 GB (basic/business/ultimate) | F-C | Q03 Editionstabelle |

---

## 2. Frage 1 – Berechtigungen in d.velop documents (Cloud)

### 2.1 Modell (F-C)

- Die Funktions- und die Leistungsbeschreibung sagen: „Über die Eigenschaften der Kategorie kann der Kunde unter anderem Zugriffsberechtigungen und die automatische Aktenbildung steuern." Weiter: „In d.velop documents kann der Kunde für Dokumente und Akten Zugriffsberechtigungen auf Ebene der Kategorie vergeben. Die zu berechtigenden Objekte können anhand von weiteren Eigenschaften der Kategorie weiter eingeschränkt/gefiltert werden. Diese Berechtigungsprofile können Benutzergruppen zugeordnet werden" [Q02 §2, §4.1.6; Q03 §2, §4.1.6].
- DmsConfig-Tag „Permissions": „Within a repository, you can assign different permissions for the categories you have created … to limit the visibility and access options of different user groups and applications" [Q01].
- **PermissionDto** [Q01]:
  - `name` ist Pflicht und eindeutig („a permission with the name already exists" → 400).
  - `restrictions[]` ist Pflicht: „There must be at least one object with the key category".
  - `assignments[]` sind die Gruppen und Apps mit ihren Rechten.
- **PermissionRestrictionDto** [Q01]:
  - `key` = `CATEGORY` („may occur only once") **oder die ID einer Objekteigenschaft**. Das Beispiel nennt auch `OWNER`.
  - `value` = Kategorie-ID oder ein Filtertext.
  - **Operatoren:** Bereich `|-`, `*` (beliebig viele Zeichen), `?` (genau ein Zeichen), `@CURRENT_USER`, `@CURRENT_USER_EMAIL`, `@CURRENT_USER_IN_GROUP` sowie „Dynamically via a filter set with `@Filter([Filter-ID])`".
- **Systemeigenschaften**, die in Berechtigungen nutzbar sind: `DOCUMENT_ID`, `CATEGORY`, `FILE_EXTENSION`, `FILE_NAME`, `STATUS`, `EDITOR`, `OWNER` („you can use these properties to assign permissions") [Q01 Tag Properties]. Damit sind z. B. „nur eigene Dokumente" oder „nur Status Freigabe" möglich.

### 2.2 Rechtearten (F-C)

| Recht | Bedeutung laut API | Werte | Regeln |
|---|---|---|---|
| `read` | „Authorizes … to read objects" | `ALLOWED` / `INHERITED` (Standard) / `DENIED` | `read = DENIED` erzwingt `write = DENIED` und `delete = DENIED` |
| `write` | „… to **edit or create** objects" | dto. | `write = ALLOWED` setzt `read = ALLOWED` voraus |
| `delete` | „… to delete objects" | dto. | `delete = ALLOWED` setzt `read = ALLOWED` voraus |

Auswertung [Q01 PermissionAssignmentDto]:
- `INHERITED`: „Right is not granted. If several permissions for the group or application pertain to an object, the others will apply. Otherwise as DENIED."
- `DENIED`: „If several permissions … pertain to an object, DENIED will always apply."

→ **Lesen, Bearbeiten und Löschen sind getrennt vergebbar (F-C).** Eigene Rechte für Statuswechsel, Verknüpfen, Export oder Aktivitäten-Lesen, wie es sie On-Prem gibt [04a §4.2], kennt die Cloud-API **nicht** (O).

Das smart-invoice-Cloud-Handbuch fordert für den API-Benutzer „die Berechtigung **Attributänderung in Freigabe**" [Q07 §1.2.2]. Das ist ein On-Prem-Begriff. Ob die Cloud-UI dieses Recht anbietet oder ob `write` es abdeckt, ist **O → T11**.

### 2.3 Dynamische Rechte aus Eigenschaftswerten (F-C)

- **Restriction Sets** [Q01 Tag]: „A restriction set allows you to dynamically grant a user authorization for a document. Authorization is granted by calculating a list of values. This list results from the user's group membership. If a restriction set is assigned to a property within a permission, the user receives the configured authorization if the value is contained in the calculated list."
- **Zuordnung** (`RestrictionSetAssignmentDto`): `type = GROUP` (mit Gruppen-ID) oder `NO_ASSIGNMENT` („assigned to all groups"). Dazu `values[]`. **„Attention: An empty array allows all values."**
- **Verwaltung per API:**
  - Werte ersetzen (`PUT …/values`) oder anhängen (`PATCH …/values`).
  - Je Gruppe nur **eine** Zuordnung je Set (409 „An assignment with this group already exists").
  - Ein Set lässt sich nicht löschen, solange eine Berechtigung es verwendet (409) [Q01].
- **Referenzmuster aus dem Standard:** Das smart-invoice-Onboarding legt Berechtigungsprofile an, z. B. „ERV - Eingangsrechnung/-gutschrift **[ALL]** / **[Group]** / **[User]**" (Lesen und Schreiben bzw. Lesen für dv_-Gruppen). Dazu kommen die Mehrfacheigenschaften „Workflowbeteiligte" und „WorkflowbeteiligteIDs" [Q07 §1.2.21]. Die Leserechte werden „anhand der Liste der Workflowbeteiligten" gewährt [Q07 §1.2.2].
  - **A:** [User] bzw. [Group] nutzen `@CURRENT_USER` bzw. `@CURRENT_USER_IN_GROUP` gegen `WorkflowbeteiligteIDs`. Dafür spricht, dass beide Platzhalter IDs liefern. Prüfbar ohne Änderung: bestehende Profile im Demo-Tenant **nur ansehen** (T12).

### 2.4 Menüpfad (Stand der Belege)

| Zweck | Pfad | Status |
|---|---|---|
| Struktur (Wertemengen/Eigenschaften/Kategorien) | Konfiguration > Dokumentenmanagement > Verwaltung > Dokumenten- und Aktenstrukturen (Register Wertemengen · Eigenschaften · Kategorien; lt. custom logics mit Einstieg „Übersicht") | F-C [03 §1.1; Q11 §1.5.1] |
| Benutzer/Gruppen | Konfiguration > Dokumentenmanagement > (Verwaltung >) Benutzerkonten- und Gruppenverwaltung > Benutzerkonten und Gruppen | F-C [Q04; Q13] |
| API-Schlüssel, technische Benutzergruppe, Benutzerkontenprovider | Konfiguration > Infrastruktur und Sicherheit > Anmeldung > API-Schlüssel / Benutzerkontenprovider | F-C [Q13] |
| **Berechtigungen, Restriction Sets, Strukturregeln (DMS)** | **nicht öffentlich dokumentiert.** Die Schulung „d.velop documents administrieren (Cloud)" behandelt „Berechtigungen" und „Strukturen und Aktenpläne" im „d.velop webadmin" [Q21]. **A:** Die Punkte liegen neben „Dokumenten- und Aktenstrukturen" unter *Dokumentenmanagement > Verwaltung*. | **T01** |
| smart-invoice-Rechte | smart invoice-Administration > Settings > Berechtigung (Globale Rechnungsliste / Workflowberechtigungen) | F-C [Q07 §1.2.25] |

### 2.5 Grenzen (belegt vs. offen)

- **Belegt (F-C) [Q01]:**
  - Eine Kategorie je Berechtigung.
  - Berechtigungsname eindeutig; Restriction-Set-Name eindeutig.
  - Eine Zuordnung je Gruppe und Set.
  - Leere Werteliste = alle Werte.
  - Eine Kategorie ist nur löschbar, wenn **keiner Berechtigung** zugeordnet.
  - DmsConfig-Anfragen „only sequential"; Konfiguration nur durch Tenant-Administratoren.
- **Globale Gruppen:** „können die Leistung des Identitätsmanagements negativ beeinflussen … nur dann, wenn es wirklich erforderlich ist". Die Umstellung auf global ist **nicht umkehrbar** [Q04 §1.2.2].
- **Nicht dokumentiert (O):** maximale Anzahl Berechtigungen, Gruppen, Restriction Sets, Werte je Zuordnung; Wirkung verschachtelter/globaler Gruppen in Restriction Sets; Latenz nach Gruppenänderung. → Schriftliche Anfrage an d.velop + T09/T10.

### 2.6 Umsetzung der Livos-Anforderungen – Kurzantwort

Details in §10.

| Anforderung | Cloud-Mechanismus | Status |
|---|---|---|
| >100 Gesellschaften, strikte Trennung | Pflicht-Eigenschaft „Mandant" (Gesellschafts-ID) + Restriction Set `RS_Mandant` (Gruppe → IDs) + je Kategorie eine Berechtigung mit `Mandant = @Filter(RS_Mandant)` | Mechanismus F-C; Verhalten T02–T08 |
| Zentrale Buchhaltung (auch externer Dienstleister „Trios") | Berechtigung je Kategorie **ohne** Mandant-Filter für Gruppe Buchhaltung, oder Zuordnung im Set mit leerer Liste (= alle). smart invoice: „Globale Rechnungsliste" | F-C [Q01; Q07] |
| Projektleiter nur ein Objekt | Eigenschaft „Objekt-ID" + `RS_Objekt` (Objektgruppe → Objekt-ID) + Berechtigung `Objekt = @Filter(RS_Objekt)` (nur Lesen) | Mechanismus F-C; T02 analog |
| Geschäftsführung nur eigene Gesellschaften | GF-Gruppe je Gesellschaftsverbund mit Werteliste der eigenen Gesellschaften in `RS_Mandant`; Leserecht | F-C |
| Lesen/Bearbeiten/Löschen getrennt | `read`/`write`/`delete` | F-C |

---

## 3. Frage 2 – Aktenbildung in der Cloud

**Belegt (F-C):**
- „Der Kunde kann in d.velop documents (hierarchische) Aktenstrukturen konfigurieren. … Akten können Dokumente oder weitere Akten enthalten. **Eine Akte kann in einer oder mehreren Akten enthalten sein.** Akten können manuell angelegt … oder so konfiguriert werden, dass durch eingehende Dokumente **automatisch anhand ihrer Dokumenteigenschaften passende Akten erstellt werden, wenn diese noch nicht vorhanden sind**. Akten können Eigenschaften … an eingehende Dokumente vererben." [Q02 §4.1.2; Q03 §4.1.2]. Die Leistungsbeschreibung (Cloud): „Durch die Definition von Regeln lassen sich eingehende Dokumente automatisch in Akten einsortieren und neue Akten automatisch erzeugen." [Q03 §1]
- **StructureRuleDto** [Q01]:
  - `parent` (Kategorie-ID der übergeordneten Akte) und `child` (Kategorie-ID des Dokuments bzw. der Akte). Voraussetzung: „at least two available categories".
  - `recognition[]` (Pflicht): „If these properties are the same in a parent element and a child element, they are linked". Entweder `propertyId` (in beiden Kategorien vorhanden) oder das Paar `parentId`/`childId` bei unterschiedlichen Eigenschaften. „Different properties can be combined."
  - `inheritance[]`: `propertyId`, `type = FROM_PARENT_TO_CHILD | FROM_CHILD_TO_PARENT`, `overwrite`, `overwriteSrcEmpty`. Die Eigenschaft muss in beiden Kategorien existieren und darf nicht zugleich Erkennungseigenschaft sein.
  - `createSiblingDossiers`: „All child dossiers with the same parent dossier are also created automatically when the selected child dossier is created."
  - `changeParent`: „Apply rule to all subordinate objects when changing."
- **Mehrfachablage:** belegt durch „Eine Akte kann in einer oder mehreren Akten enthalten sein" [Q02] und das manuelle Verknüpfen („Zum Verknüpfen markieren" → „Markierte Elemente verknüpfen") [Q16 §1.9.32]. Im Demo-Termin wurde gezeigt, dass ein Dokument in mehreren Akten liegt („Folder Content") [03 §1.2; TR 00:55:02, 01:06:18 Sebastian Pachon].
- **Aktenansicht:** Es werden zunächst die „ersten 100 Elemente" geladen, umstellbar [Q16 §1.4.12].
- **Referenzmuster d.velop contracts (Cloud):** Kategorien „Vertragsakte" (übergeordnet) und „Vertragsdokumente". „Die Eigenschaft Vertrags-ID (intern) dient als verknüpfendes Element. Die weiteren Eigenschaften werden hierarchisch von der Vertragsakte auf die Vertragsdokumente übertragen." [Q10 §1.4.2]

**Annahmen / Tests:**
- **A:** Für eine Mehrfachablage „automatisch" (Rechnung → Kreditorenakte **und** Objektakte) braucht man **zwei Strukturregeln** mit gleichem `child` und verschiedenem `parent`. Das Schema schließt das nicht aus. Die 400-Meldung „structure rule already exists" deutet auf Eindeutigkeit je Paar parent/child. → **T13**
- **O:** Verhalten bei **leerer Erkennungseigenschaft**. On-Prem entsteht dann keine Akte [04a S16]; für die Cloud nicht dokumentiert → T13.
- **O:** Wo in der Cloud-UI die Regeln gepflegt werden (T01). Im Termin wurde eine Zuordnung „welche Dokumentarten in welche Aktenart dürfen" gezeigt [03 §4.3; TR 00:55:02–00:56:45]. **A:** Das ist die UI-Sicht der Strukturregeln.
- **O:** Eine Obergrenze der Aktenebenen ist nicht dokumentiert. Empfehlung im Termin: 4–5 Ebenen [TR 00:57:14 Sebastian Pachon].

---

## 4. Frage 3 – Strukturverwaltung in der Cloud

| Thema | Beleg (F-C) | Quelle | Offen / Test |
|---|---|---|---|
| Datentypen | `STRING` (Text), `CURRENCY` (Währung), `NUMERIC` (Zahl), `DATE`, `DATETIME`. **Kein Boolean** | Q01 PropertyDto; 03 §5.3 G1 | – |
| Mehrfachwerte | `isMultiValue` | Q01 | Wert-Obergrenze je Mehrfachfeld (On-Prem 100/2.000) → O |
| Validierung | `validationRegEx` (POSIX basic, nur STRING); `minValue`/`maxValue` (nur NUMERIC/CURRENCY). **Keine Eindeutigkeitsprüfung** (Unique) im Modell → Webhook `validateimport`/`validateupdateproperties` | Q01 | – |
| Wertemengen statisch | Dataset mit `values[]` (Typ passend zur Eigenschaft); per API pflegbar (`PUT /objectmanagement/datasets/{id}`) | Q01 | Obergrenze Einträge → O/T19 |
| Wertemengen dynamisch | System-Datasets `USERS`, `EXISTING_VALUES`; Typ `URI: Dynamic`; **custom logics**: „Vordefinierte Werte > custom logics Dataset", Datenquelle = business-objects-Modell, abhängige Wertemengen, Attributierung (Kopf-, Positions-, Bezugsdaten); nur Cloud, **Freischaltung auf Anfrage** | Q01; Q11 §1.2–1.6; Q12 | – |
| Grenze dynamische Wertemengen | „Für Vorschlagswerte von Dokumenteigenschaften gilt dabei ein Limit von maximal **100 Einträgen pro Wertemenge**." | Q02 §4.1.4 | Bei >100 Gesellschaften: Suche per Tippen statt Vollliste? → T19 |
| Stammdaten-Quotas (business objects) | 500.000 Datensätze/Mandant, 1 GB/Mandant, 100.000 Datensätze bzw. 200 MB je Stammdatentyp, 5 Modelle/Mandant, 10 Stammdatentypen/Modell, 60 Eigenschaften/Stammdatentyp | Q12 (Quotas) | – |
| Pflichtfelder | je Kategorie: `propertyRefs[].required` | Q01 | – |
| Masken-/Suchverhalten je Kategorie | `showInImport`, `showInSearch`, `showInFacets`, `showInResult` | Q01 | – |
| Titel | `titleRefs[]` (Eigenschaften inkl. `FILE_NAME`, je mit Trennzeichen `delimiter`); „Der Titel wird … automatisch gebildet" | Q01; Q02 („der Titel dynamisch erzeugt") | – |
| Kategorie-Kürzel/Schlüssel | **kein Kürzel-Feld**; Identifikation per ID, Name mehrsprachig | Q01 CategoryDto; 03 §5.3 G6 | – |
| Umbenennen | `PUT` auf Kategorie, Eigenschaft und Dataset (Name ist Teil des DTO) | Q01 | Wirkung auf Suchvorlagen/Zuordnungen → T16 |
| Datentyp/„Anzahl der Werte" ändern | Für d.velop-contracts-Eigenschaften: „Datentyp nachträglich nicht mehr ändern" / „Anzahl nachträglich nicht mehr ändern" | Q10 §1.4.1 (contracts-Konfiguration) | Für DMS-Eigenschaften nicht dokumentiert → **A:** ebenso nicht änderbar; T16 |
| Löschen | Kategorie nur, wenn **keiner Berechtigung** zugeordnet und nicht `readOnly`; Eigenschaft nur, wenn **keiner Kategorie** zugeordnet; Dataset nur, wenn **keiner Eigenschaft** zugeordnet | Q01 DELETE-Beschreibungen | Kategorie mit vorhandenen Dokumenten → O |
| Namenseindeutigkeit | 400 „already exists" bei Kategorie, Eigenschaft, Dataset | Q01; 03 §5.3 G7 | – |
| Mehrsprachigkeit | Namen als Sprach-Schlüssel-Paare (de, en, hr, cs, da, nl, fr, it, pl, sr, es, sk, zh-CN) | Q01 info | – |
| Ereignis-Webhooks | presearch, postsearch, validateimport, preimport, postimport, prenewversion, postnewversion, validateupdateproperties, preupdateproperties, postupdateproperties, predelete, postdelete, prelink, postlink, pretransfer, posttransfer, pregenerateddocument, postgenerateddocument, prereleasedocument, postreleasedocument; `timeout` Standard 300 ms, `retry` bis 3× | Q01 Events/WebHookDto | – |

**Sind die On-Prem-Grenzen in der Cloud relevant?**

- **DB-Position:** Im Cloud-Modell gibt es keine Position [Q01; 03 §5.3 G6]. Rechte-Einschränkungen verwenden die **Eigenschafts-ID** [Q01]. Die On-Prem-Vorgabe „Gesellschaft überall auf derselben DB-Position" [04a §2.3 Nr. 1] **entfällt (F-C)**.
  - **Restrisiko (A):** Intern kann ein d.3-Repository mit Typ-Kontingenten liegen. Die Demo-Folie nennt „max. 89 Eigenschaften je Kategorie" [03 §5.3 G9]. Ob pro Typ nur 10 Währungs- oder Mehrfachfelder möglich sind, ist unbekannt → **T14**.
- **Kategorie-Kürzel (5 Zeichen, unveränderlich):** **entfällt (F-C)**, weil es im Modell kein Kürzel gibt.
- **8-Zeichen-Regel für Gruppennamen:** nur On-Prem belegt [04a §2.2]. In der Cloud werden Gruppen per ID referenziert [Q01 `subject` = „ID of an application or group from the identity provider app"]. **A:** nicht relevant → **T15**.

---

## 5. Frage 4 – Benutzer und Gruppen in der Cloud

| Thema | Beleg | Quelle | Status |
|---|---|---|---|
| Benutzerverwaltung | Benutzer anlegen, bearbeiten, (de)aktivieren, löschen: „geht die eindeutige ID … verloren". Gruppen, Gruppentypen (Standard: Hidden, Distribution, Authorization), **globale Gruppen** (enthalten Gruppen aus usermanagement und IdP-Providern). Sicherung und Wiederherstellung der Benutzer/Gruppen, „nicht als Transportsystem" | Q04 §1.2–1.3; Q02/Q03 „Integrierte Benutzerverwaltung (mit Massenimport)" | F-C |
| Adminrecht | „Teil der administrativen Gruppe des Usermanagement-Providers" oder BuiltInAdmin-Provider. Gruppe „**Administrative group for the tenant**". DmsConfig: „Only tenant administrators …" | Q04 §1.2; Q25; Q01 | F-C |
| **SCIM** | SCIM 2.0: `https://<Basisadresse>/usermanagement/scim`, API-Schlüssel des Benutzers „Builtin SCIM 2.0 provisioning user", Bearer-Token; Gruppentypen per SCIM-Erweiterung. API: `/usermanagement/scim/users` und `/groups` (GET/POST/PUT/PATCH/DELETE). identityprovider: SCIM 1.1 lesend | Q04 §1.2.10–1.2.11; Q05; Q06 | F-C |
| **Microsoft Entra ID** | Leistungsbeschreibung Cloud: SSO „via OpenId Connect"; „Active Directory (AD)-Integration (via ADFS, LDAP) (mit Filterfunktion)"; „Authentifizierung über weitere Identity Provider (via OpenID Connect)". Diese drei Funktionen **nur in business/ultimate**. d.velop-Handbuch: „Grundsätzlich können Sie jedoch auch andere Identitätsanbieter verwenden, z.B. Entra ID." KB-Artikel (Titel): „Wie konfiguriere ich die Anmeldung an d.velop documents mithilfe von OpenID Connect und einem Azure AD?" und „Wie kann ich Benutzer und Gruppen aus Azure Active Directory für den d.velop cloud-Mandanten bereitstellen?". Laut Suchauszug per SCIM (Tenant-URL `<Tenant>/usermanagement/scim`, API-Schlüssel des SCIM-Provisioning-Benutzers; Profilbilder werden nicht übertragen) | Q03 §4.1.6 + Editionstabelle; Q13; Q19 | F-C (OIDC, SCIM); KB-Inhalt nur als Suchauszug → Volltext mit Portal-Login verifizieren |
| Entra-Provisioning (Microsoft-Seite) | Nur **direkte** Mitglieder zugewiesener Gruppen („kann Benutzer in verschachtelten Gruppen [nicht] lesen oder bereitstellen … nur … direkte Mitglieder"). Inkrementelle Zyklen im App-spezifischen Intervall. Deaktivieren/Löschen bei Scope-Verlust. B2B-Gäste bereitstellbar | Q20 | F-M → Gruppenmodell **flach** halten |
| 2FA / FIDO2 | TOTP-2FA (alle Editionen); FIDO2-Anmeldung | Q03; Q16 §1.9.28 | F-C |
| Technische Benutzer | „technische Benutzergruppe" (kein interaktiver Login, nur API-Schlüssel) unter *Infrastruktur und Sicherheit > Anmeldung > Benutzerkontenprovider* | Q13 | F-C |
| Externe | „Einfaches Teilen von Dokumenten mit Externen" ohne Lizenz (Link mit max. Gültigkeit; nur lesen/herunterladen oder neue Versionen hochladen) – **nur business/ultimate**. Widget-Option „Freigeben für externe Anwendende" | Q03; Q17 | F-C. Lizenzart „externe Anwendende" → O |
| Delegierte Administration | Für DMS-Konfiguration **nicht belegt**. Fachliche Teil-Delegation: smart invoice Settings > Berechtigung [Q07]; business objects: Rechte „auf Benutzer- und Gruppenebene für die Modellkonfiguration, die Datenanlieferung und die Abfrage" [Q12]; Supportzugang „Anwendenden erlauben, Supportzugriff zu gewähren" [Q14]; contracts: Berechtigungsmatrix je Organisation × Vertragstyp [Q10] | Q07; Q10; Q12; Q14 | O (DMS) |
| Partner-/Supportzugang (MDIS) | *Infrastruktur und Sicherheit > Supportzugang*: zeitlich begrenzt (Support ≤ 7 Tage, spezifische Personen z. B. Consultants ≤ 12 Monate), nur kundenseitig vergebbar, externe Zugriffe werden protokolliert | Q14 | F-C |

---

## 6. Frage 5 – Aufbewahrung und Löschung in der Cloud

- **Aufbewahrungsfrist je Kategorie (F-C):**
  - „In d.velop documents können für Kategorien Aufbewahrungsfristen festgelegt werden, die abhängig von einer vom Kunden gewählten Datumseigenschaft der Kategorie sind." [Q02; Q03]
  - `CategoryRetentionDto`: `period` („0 means unlimited"), `unit` = `YEARS | MONTHS`, `basedOn` = `LAST_EDITED` (Standard) oder eine Datumseigenschaft der Kategorie. „Changes to the retention period will also affect existing documents with a time delay." [Q01]
- **Löschung nach Ablauf:**
  - Leistungsbeschreibung Cloud (2025-02-18): „Nach Ablauf der Aufbewahrungsfrist werden die Dokumente bzw. Akten dieser Kategorie **automatisch gelöscht**." [Q03]
  - Funktionsbeschreibung (2025-11-28): „Es kann konfiguriert werden, dass die Dokumente nach Ablauf … automatisch gelöscht werden." [Q02]
  - → **A:** Die automatische Löschung ist in neueren Ständen abschaltbar → T17 / Frage an d.velop.
- **Löschsperre:** `protection.preventDeletion`: „Prevents deletion of items in the status Release and Archive. The property **overrules all Delete rights**. If you specified a retention period …, the items are still deleted after the period expires." Wer die Sperre zurücknimmt (true → false), muss einen Grund angeben (`preventDeletionChangeReason`) [Q01]. In der Oberfläche heißen die Einstellungen (d.3one-Handbuch) „**Freigegebene Elemente dürfen nicht gelöscht werden**" und „**Aufbewahrungsdauer festlegen**" [Q18]. Übertragbarkeit auf die Cloud-UI: A.
- **Protokoll:** „Änderungen an der Definition einer Kategorie bei der Aufbewahrungsdauer und Löschsperre werden ebenfalls protokolliert." [Q02; Q03; Q18]
- **Löschprozess:**
  - Das Recht `delete` ist getrennt vergebbar [Q01].
  - Massenlöschung „unter Berücksichtigung der jeweiligen Berechtigungen … inklusive aller zugehörigen Versionen" [Q02 §4.1.2 Massenbearbeitung].
  - Das Löschen der aktuellen Version stellt die Vorgängerversion her. Eine Bearbeitungsversion ist danach nicht wiederherstellbar [Q02; Q03].
  - Webhooks `predelete`/`postdelete` stehen zur Verfügung [Q01].
  - Migration: `dateRetention` je Dokument darf nicht in der Vergangenheit liegen [Q22].
- **storage manager:** d.ecs storage manager ist eine On-Prem-Komponente. Auch das Modul „cloud storage" legt nur On-Prem-Dokumente im d.velop cloud storage ab [Q23]. **Für den Cloud-Tenant ist er nicht einschlägig (F-O/A).**
- **Legal Hold: nicht dokumentiert (O).**
  - **A (Workaround, zu prüfen):** Frist auf einer eigenen Datumseigenschaft „Aufbewahrungsbeginn" aufsetzen. Für gesperrte Fälle wird das Datum hochgesetzt; die Änderung ist in den Aktivitäten nachvollziehbar.
  - Oder die Kategorie-Frist auf 0 setzen und die Löschung über einen gesteuerten Prozess führen.
  - Beides braucht eine d.velop-Bestätigung.
- **GoBD-Hinweis (A, fachlich zu bestätigen):** `basedOn` rechnet ab dem Datumswert. Steuerliche Fristen beginnen mit Ablauf des Kalenderjahres. Empfehlung: eine berechnete Eigenschaft „Aufbewahrungsbeginn = 31.12. des Belegjahres" als `basedOn`. Die Dauer je Belegart (z. B. Buchungsbelege, Handelsbriefe, Verträge) legt die Steuerberatung bzw. Trios fest.
- **Weitere Produkte (nur Existenz belegt):** d.velop records management (API mit z.d.A.-Prozess) [Q27] und d.velop disposition management (Handbücher nur mit Login) sind eher für Aktenpläne der öffentlichen Verwaltung und Aussonderung gedacht. Relevanz für Livos: gering (A).

---

## 7. Frage 6 – Aktivitäten, Änderungsprotokoll, Versionierung

- **Aktivitäten (F-C):**
  - „An einer Akte oder einem Dokument können sämtliche Änderungen an der Datei oder den Eigenschaften in Form eines Protokolls nachvollzogen und nach Zeitraum und Schlagwörtern gefiltert werden." [Q02; Q03]
  - Anwendersicht: Liste neuste zuerst, Filter nach Zeiträumen, Inhalten oder Tätigkeitsbereichen, Standard- und erweiterte Ansicht, persönliche Aktivitäten als eigenes Feature [Q16 §1.9.7, §1.9.20–21].
  - Protokolliert werden Import, erneutes Bearbeiten, Notizen/Markierungen, Änderungen an Eigenschaften, Status und **Aufbewahrungsdauer** sowie Verknüpfen und Lösen [Q18].
  - Die Aktivitätenprotokollierung ist in allen drei Editionen enthalten [Q03].
- **Offen (O):** Aufbewahrungsdauer der Aktivitäten, Export, Leseprotokoll (Wer hat was angesehen/heruntergeladen?), Manipulationsschutz. Supportzugriffe werden protokolliert (z. B. „per Amazon CloudWatch") [Q14].
- **Versionierung (F-C):**
  - „Dokumente werden automatisch bei Freigabe neuer Dokumentenstände versioniert. Jede Freigabe mit Änderung erzeugt eine neue Version." Versionsübersicht vorhanden [Q02; Q03].
  - Status: Bearbeitung, (Prüfung,) Freigabe, Archiv. Beim Freigeben wird die bisherige Freigabeversion zu Archiv [Q02; Q03; Q10 Glossar].
  - Check-in/Check-out „kann vom Kunden selbst konfiguriert werden" [Q02].
  - Versionen per API abrufbar (`/o2m/{id}/v`) [Q24].
- **Webhooks für eigenen Audit oder Plausibilisierung:** `prereleasedocument`/`postreleasedocument`, `preupdateproperties`/`postupdateproperties`, `prelink`/`postlink`, `predelete`/`postdelete` [Q01].

---

## 8. Frage 7 – Suche, gespeicherte Suchen, Dashboard

- **Suche (F-C):**
  - Volltext (inkl. OCR), Facetten und Filter, Recherche in Aktenstrukturen [Q02; Q03].
  - Je Kategorie steuerbar, welche Eigenschaften in Suche, Facetten, Ergebnisliste und Ablage erscheinen [Q01 `showIn…`].
  - API-Suche: Standardseitengröße 25 [Q24].
- **Suchvorlagen (F-C):**
  - In persönlicher Ordnerstruktur, **per Link teilbar**, beobachtbar mit E-Mail-Benachrichtigung („nur in der Business Edition") [Q02; Q16 §1.5.1, §1.5.9–1.5.10].
  - Eine zentrale Zuweisung von Suchvorlagen an Rollen ist **nicht** dokumentiert (O; vgl. 04a S23).
- **Dashboard (F-C):**
  - Vier Standard-Widgets: Suche, Zuletzt bearbeitet, Beobachtet, Favorisiert. „Zuletzt bearbeitet" zählt keine Statuswechsel [Q16 §1.9.13].
  - Eigene Widgets unter *Konfiguration > Erscheinungsbild > Startseite > Widgets erstellen*: Verknüpfungs-Widget (Ziel-URL, Symbol Pflicht, data-URL max. 10.000 Zeichen, empfohlen 48×48), **Listen-Widget** (URL auf Listeninhalt), **Erweitertes Widget** (Webseite), Option „Freigeben für externe Anwendende"; Sichtbarkeit je Benutzer/Gruppe [Q17].
  - Eine Obergrenze für die Anzahl der Widgets ist nicht dokumentiert (O). Sichtbarkeit ist keine Sicherheitsfunktion [04a R17].
- **Rechnungseingangsbuch:** Schnellzugriffe und eigene Schnellzugriffe, Gruppierung nach Schritt oder **Mandant**. Archiv 6 Monate, erweiterbar auf 12 (Admin-Handbuch: „bis zu 365 Tagen") [Q09; Q07 §1.2.25].

---

## 9. Frage 8 – smart invoice: Mandanten

| Thema | Beleg (F-C) | Quelle |
|---|---|---|
| Mandanten-Stammdaten | `POST /smartinvoice/api/v1/buckets/:bucket_id/companies/batch`; Felder: `id` (Pflicht, String 255, sichtbar), `name` (Pflicht; „für die automatische Mandantenermittlung … ein wichtiges Kriterium … so angegeben …, wie er auf den Rechnungen zu finden ist"), `address` (wichtig für die Ermittlung), `city`, `zip_code`, `local_currency` (ISO 4217), `country` (ISO 3166-1 alpha-2). `parent_id` kommt **nur im Beispiel** vor und ist in der Feldtabelle nicht beschrieben → Semantik O. Einzelaktualisierung `PUT …/companies` (synchron, Rate-Limit) | Q08 |
| Kreditoren je Mandant | `company_id` Pflicht; Kreditor-`id` „muss je company_id eindeutig sein"; `vat_id` „wichtig für die automatische Erkennung"; `registration_id` = Steuernummer | Q08 |
| Buckets | „beliebig viele Datensammlungen (Buckets)"; d.velop empfiehlt **einen** Stammdatenbucket. Mehrere Buckets mit document-reader-Sync nur als Vorschau-Feature | Q07 §1.2.11, §1.2.22 |
| Mandant ↔ DMS | smart invoice greift über ein Quellsystem auf documents zu. Pflichtzuordnung (Konfiguration „Zuordnungen", Quelle „smart invoice - invoice"): **Mandant Nummer, Mandant Name, Workflowbeteiligte** + „Erstellt am". Das Onboarding legt die DMS-Eigenschaften **„Mandant" (Text)** und **„Mandantenname" (Text)** an und prüft nicht auf Dubletten (Namenszusatz „(1)") | Q07 §1.2.2, §1.2.21 |
| Rechte im DMS für Rechnungen | Leserechte für Workflowbeteiligte über die Mehrfacheigenschaft **Workflowbeteiligte**; Berechtigungsprofile [ALL]/[Group]/[User]. Vertretung wird bei Öffnen der Aufgabe den Workflowbeteiligten hinzugefügt (kurzzeitige Rechte-Latenz möglich) | Q07 §1.2.2, §1.2.21 |
| Rechnungseingangsbuch je Mandant | *Settings > Berechtigung*: „**Globale Rechnungsliste**" je Gruppe, oder *Workflowberechtigungen* > Neue Berechtigung > Gruppe + **Mandantennummer** (Beispiel `Buchhaltung_M001` → `M001`) | Q07 §1.2.25; Q09 |
| Clearing je Mandant | „Berechtigen individueller Gruppen für jeden Mandanten" (Mandanten-ID → Gruppe) | Q07 §1.2.10 |
| Freigabematrix | 2 feste Spalten (Bearbeiter, Freigabegrenze) + bis 20 Spalten, z. B. **Mandant**; Grenze gilt je **Kostenobjekt**; **Groß-/Kleinschreibung** relevant; Zeilen per API (`…/approval_matrices/:matrix_id/rows/batch`, Benutzer/Gruppe `type = idp \| aad`) | Q07 §1.2.5; Q08 |
| Bearbeiterfindung/Start je Mandant | Urkel: `voucher.company.nr`, `company.name`; Beispiel `/^Freigeber_#{voucher.company.nr}$/ =~ "Freigeber_23"`. Workflow-Startbedingung je Mandantennummer | Q07 §1.2.1, §1.2.19 |

**Ableitung (A):**
- Ein Namensschema `Freigeber_<MandantNr>`, `Pruefer_<MandantNr>` usw. erlaubt **eine** Bearbeiterfindungs-Regel für alle Gesellschaften (`group.name` gegen den Regex). Zu testen (T21).
- Die Workflowberechtigung im Rechnungseingangsbuch ist je Eintrag **eine** Mandantennummer (Beispiel). Mehrere oder Platzhalter sind nicht dokumentiert → T20.

---

## 10. Empfohlenes Berechtigungs- und Strukturmodell für Livos in der Cloud (belegt vs. Annahme)

### 10.1 Leitentscheidungen

| # | Entscheidung | Begründung | Status |
|---|---|---|---|
| E1 | **1 Tenant, 1 Repository** für alle Gesellschaften, dazu ein separater Test-/Abnahme-Tenant | Tenant trennt Kunden, nicht Gesellschaften [04a §3.1]. Rechte sind datensatzgenau per Eigenschaft steuerbar [Q01] | F-C (Mechanik) / A (Architektur) |
| E2 | **Edition mindestens *business*** | SSO (OIDC), AD-Integration, weitere IdP, API, Business Objects/Custom Logics, process studio, externes Teilen, PDF zusammenführen fehlen in *basic* [Q03 Editionstabelle] | F-C |
| E3 | **Gesellschafts-Schlüssel = smart-invoice-Mandanten-ID** in der vorhandenen DMS-Eigenschaft **„Mandant"**. Keine zweite Eigenschaft „Gesellschaft (Livos)". Anzeige über „Mandantenname" | Onboarding-Eigenschaft existiert, Zuordnung ist Pflicht [Q07]. Ein einheitlicher Schlüssel für DMS-Rechte, Aktenbildung und smart invoice [04a §3.4] | F-C (Eigenschaften) / A (Wiederverwendung) |
| E4 | **Rechte = Permission je Kategorie × Rechtestufe**. Gesellschaftsbezug über **Restriction Set** `RS_Mandant`, Objektbezug über `RS_Objekt` | Anzahl Berechtigungen unabhängig von der Anzahl Gesellschaften [Q01] | F-C (Mechanik) |
| E5 | **Identitäten aus Entra ID per SCIM**, flache Gruppen (keine Verschachtelung), SSO per OIDC | Q03; Q04; Q13; Q20 (nur direkte Mitglieder) | F-C/F-M; KB-Details T22 |
| E6 | **Eine führende Stammdatenquelle** (MDIS-Stammdaten-App): speist smart-invoice-Bucket (Mandanten, Kreditoren), DMS-Dataset „Mandant" bzw. business objects, Restriction-Set-Werte und Gruppen-Anlage | APIs belegt [Q01; Q05; Q08; Q12] | F-C (APIs) / A (Architektur) |

### 10.2 Eigenschaften (Kern, rechte- und aktenrelevant)

| Eigenschaft | Typ | Wertemenge | Pflicht | Rolle | Status |
|---|---|---|---|---|---|
| **Mandant** (Gesellschafts-ID) | Text | Dataset „Gesellschaften". Statisch per API gepflegt (`PUT datasets`), oder dynamisch per custom logics (Limit 100 Vorschläge [Q02]) | **ja, in allen Kategorien** | Rechteträger, Aktenschlüssel, smart-invoice-Zuordnung | F-C / T19 |
| Mandantenname | Text | – (Attributierung aus Stammdaten oder smart-invoice-Zuordnung) | nein | Titel/Anzeige | F-C [Q07; Q11] |
| **Objekt-ID** | Text | Dataset/dynamisch; **global eindeutig** (z. B. mit Gesellschaftspräfix) | in objektbezogenen Kategorien | Rechteträger PL, Aktenschlüssel | A |
| Kreditor-Nr / Kreditorname | Text | aus smart-invoice-Bucket bzw. business objects | ER: ja | Aktenschlüssel (mit Mandant) | F-C (Felder) |
| Konsolidierungsnummer Lieferant | Text | aus MDIS-App | nein | mandantenübergreifende Suche | A [TR 00:09:16–00:11:39 Thomas Gross] |
| Workflowbeteiligte / WorkflowbeteiligteIDs | Text, Mehrfach | – (von smart invoice gefüllt) | – | Leserecht Workflowbeteiligte | F-C [Q07] |
| Aufbewahrungsbeginn | Datum | – (berechnet: 31.12. des Belegjahres) | in aufbewahrungspflichtigen Kategorien | `retention.basedOn` | A |

### 10.3 Gruppenmodell (Entra ID → SCIM → usermanagement)

| Gruppenart | Beispiel | Zweck | Anzahl (Livos) | Status |
|---|---|---|---|---|
| Rollengruppen DMS | `DMS_R_Lesen`, `DMS_R_Sachbearbeitung`, `DMS_R_Buchhaltung`, `DMS_R_GF`, `DMS_R_PL`, `DMS_R_HV_Extern`, `DMS_R_Fachadmin` | Träger der **Permissions** (welche Kategorie, welches Recht) | ~7–10 | A |
| Gesellschaftsgruppen | `DMS_G_<MandantNr>` (Gruppentyp z. B. „Hidden") | nur **Werteträger** im `RS_Mandant` | ~100–150 | A (Gruppentyp: F-C [Q04]) |
| Gesellschaftsverbünde (GF) | `DMS_GF_<Verbund>` | Werteliste der eigenen Gesellschaften in `RS_Mandant` | nach Bedarf | A |
| Objektgruppen | `DMS_O_<ObjektID>` | Werteträger in `RS_Objekt` (nur wo PL-Zugriff nötig) | nach Bedarf | A |
| smart invoice | `dv_*` aus dem Onboarding; `Freigeber_<MandantNr>` usw. für Urkel-Bearbeiterfindung; `Buchhaltung_<MandantNr>` für das Rechnungseingangsbuch | Workflow-Rollen | nach Bedarf | F-C (dv_, Muster) / A (Schema) |
| Technisch | „Technical User Group", Service-Benutzer für MDIS-Middleware (API-Schlüssel) | Integration, Pflege von Datasets und Restriction Sets | 1–3 | F-C [Q13]. DmsConfig erfordert Tenant-Admin → Admin-API-Schlüssel sichern [Q01] |

**Kernannahme A1 (entscheidend, T03):** Die Werteliste eines Restriction Sets ergibt sich aus **allen** Gruppen des Benutzers, nicht nur aus der Gruppe, der die Permission zugeordnet ist. Wortlaut: „This list results from the user's group membership" [Q01]. Dann funktioniert das **orthogonale Modell** (Rolle × Gesellschaft).
- Ein Sachbearbeiter in `DMS_R_Sachbearbeitung` + `DMS_G_1001` bearbeitet nur Belege von 1001.
- **Grenze des orthogonalen Modells:** Jemand, der in Gesellschaft A bearbeiten und in B nur lesen soll, bekäme Bearbeitungsrecht auch in B. **Lösung:** je Rechtestufe ein eigenes Set (`RS_Mandant_Lesen`, `RS_Mandant_Bearbeiten`) mit eigenen Zuordnungen.
- Trifft A1 nicht zu: kombinierte Gruppen `DMS_<Rolle>_<MandantNr>` (bei 100+ Gesellschaften × Rollen deutlich mehr Gruppen), weiterhin automatisierbar.

### 10.4 Restriction Sets

| Set | Zuordnung (Gruppe → Werte) | Bemerkung | Status |
|---|---|---|---|
| `RS_Mandant` | `DMS_G_1001 → [1001]` … ; `DMS_GF_Nord → [1001,1002,1005]` | neue Gesellschaft = 1 Zuordnung (API `POST …/assignments`) | F-C |
| | **nicht** für die Zentralbuchhaltung verwenden | Leere Liste = **alle Werte** [Q01]. Besser eine eigene Permission ohne Mandant-Filter (siehe 10.5), damit „alle" bewusst und sichtbar vergeben wird | F-C / A |
| `RS_Objekt` | `DMS_O_4711 → [4711]` | Projektleiter nur für ein Objekt | F-C |
| Governance | Middleware prüft: keine leeren Wertelisten, keine `NO_ASSIGNMENT`-Zuordnung, Vier-Augen-Freigabe von Rechteänderungen, Änderungsprotokoll | Delegation an Fachverantwortliche ist in der Cloud nicht dokumentiert [Q01] | A |

### 10.5 Berechtigungsmatrix (je Kategorie K; Beispiel)

| Permission | Restrictions | Zuordnung (read/write/delete) | Zweck | Status |
|---|---|---|---|---|
| `K – Mandant – Lesen` | `CATEGORY=K`; `Mandant=@Filter(RS_Mandant)` | `DMS_R_Lesen`: ALLOWED/INHERITED/INHERITED; `DMS_R_GF`: ALLOWED/–/– | Strikte Trennung, GF nur eigene | F-C |
| `K – Mandant – Bearbeiten` | dto. | `DMS_R_Sachbearbeitung`: ALLOWED/ALLOWED/INHERITED | Sachbearbeitung je Gesellschaft | F-C |
| `K – Alle – Buchhaltung` | `CATEGORY=K` | `DMS_R_Buchhaltung`: ALLOWED/ALLOWED/INHERITED | Zentrale Buchhaltung / Trios | F-C |
| `K – Objekt – PL` | `CATEGORY=K`; `Objekt-ID=@Filter(RS_Objekt)` | `DMS_R_PL`: ALLOWED/–/– | Projektleiter nur Objekt | F-C |
| `ER – Workflowbeteiligte [User]/[Group]` | `CATEGORY=ER`; `WorkflowbeteiligteIDs=@CURRENT_USER` bzw. `@CURRENT_USER_IN_GROUP` | alle Workflowteilnehmer: Lesen | Rechnungssicht für Prüfer/Freigeber (**bewusste Ausnahme** von der Gesellschaftstrennung) | F-C (Muster [Q07]) / A (exakte Restriction, T12) |
| `K – Löschen` | `CATEGORY=K` | `DMS_R_Fachadmin`: ALLOWED/ALLOWED/ALLOWED | Löschen nur Fachadmin; zusätzlich `preventDeletion` | F-C |
| `K – vertraulich – Sperre` (optional) | `CATEGORY=K`; `Vertraulichkeit=hoch` | Gruppen ohne Zugriff: DENIED | harte Sperre | F-C; Wirkung über Gruppen T07 |

**Mengengerüst (A):** ~10–12 Kategorien × 4–6 Permissions ≈ **50–70 Permissions**, **unabhängig von der Zahl der Gesellschaften**. Eine neue Gesellschaft braucht:
- 1 Dataset-Wert,
- 1 Entra-Gruppe (SCIM),
- 1 Restriction-Set-Zuordnung,
- 1 smart-invoice-Mandant (Bucket),
- ggf. Workflowberechtigung im Rechnungseingangsbuch (T20).

Das ist per API vollständig automatisierbar, bis auf die Rechnungseingangsbuch-Berechtigung (API nicht dokumentiert → O).

**Vertretung (A, Governance):** Eine Vertretung übernimmt fremde Aufgaben und wird zu den Workflowbeteiligten hinzugefügt [Q07]. Sie bekommt damit Leserecht auf die betroffene Rechnung, auch über die Gesellschaftsgrenze hinweg. Regel: Vertretungen möglichst innerhalb derselben Gesellschaftsgruppe.

### 10.6 Aktenplan über Strukturregeln

| Regel | parent → child | Erkennung (`recognition`) | Vererbung | Status |
|---|---|---|---|---|
| S1 | Gesellschaftsakte → Kreditorenakte | `Mandant` | Mandantenname (FROM_PARENT_TO_CHILD) | F-C (Mechanik) |
| S2 | Gesellschaftsakte → Objektakte | `Mandant` | Mandantenname | F-C |
| S3 | Kreditorenakte → Eingangsrechnung | `Mandant` + `Kreditor-Nr` | Kreditorname, Konsolidierungsnr. | F-C |
| S4 | Objektakte → Eingangsrechnung | `Mandant` + `Objekt-ID` | Objektbezeichnung | **A:** 2. Regel für dasselbe child → Mehrfachablage (T13) |
| S5 | Objektakte → Vertragsakte → Vertragsdokument | `Objekt-ID` bzw. `Vertrags-ID` | Vertragsdaten (Muster d.velop contracts [Q10]) | F-C (Muster) |
| S6 | Kreditorenakte → Freistellungsbescheinigung/Nachweis | `Mandant` + `Kreditor-Nr` | – | F-C |

**Grundsätze:**
- `Mandant` gehört in **jede** Erkennungskombination, weil Kreditor- und Objektnummern je Gesellschaft kollidieren können [04a S16].
- Erkennungsfelder sind Pflichtfelder. Das Verhalten bei leeren Werten ist in der Cloud offen (T13).
- Akten sind eigene Kategorien. Sie brauchen **eigene Permissions** nach demselben Muster.
- Livos liefert die „Folder Structure" [TR 00:57:22].
- Das smart-invoice-Onboarding bringt eine „Kreditorenvorgangsakte" mit [Q07]. Wiederverwenden oder bewusst ersetzen (A).

### 10.7 Aufbewahrung je Kategorie

| Kategorie (Beispiel) | `retention` | `preventDeletion` | Status |
|---|---|---|---|
| Eingangsrechnung, Buchungsbelege | Frist gemäß steuerlicher Vorgabe (Dauer durch Steuerberatung festlegen), `basedOn = Aufbewahrungsbeginn` | true | Mechanik F-C / Dauer A |
| Verträge | `basedOn = Vertragsende` (+ Frist) | true | F-C / A |
| Korrespondenz | Frist gemäß Vorgabe für Handels- und Geschäftsbriefe | true | F-C / A |
| Workflowprotokoll ERV | wie Eingangsrechnung | true | A |

Automatische Löschung nach Fristende: einschaltbar bzw. Standard, Stand der Dokumente uneinheitlich [Q02 vs. Q03] → T17. Legal Hold: O (siehe §6).

---

## 11. Offene Punkte / Test auf der Demo-Instanz

**Rahmen:** `mdisconsulting.d-velop.cloud` ist ein **produktiv genutzter** Tenant: 102 bzw. 226 Belege, aktiver Workflow, si_-Gruppen. Es gelten die „vier Verbote" [03 §5.1]. Deshalb:
- **Lesende Prüfungen** (T01, T12) sofort möglich.
- **Schreibende Tests** nur mit „Livos_"-Testobjekten und ausdrücklicher Freigabe (Aufgabe 3). Besser in einem **eigenen Test-Tenant** („free for 30 days" = Umfang ultimate [Q03 §4.2.1]).

| ID | Test | Erwartung / Zweck | Bezug |
|---|---|---|---|
| T01 | UI-Pfade finden: Berechtigungen, Restriction Sets („Filtermengen"?), Strukturregeln, Aufbewahrung/Löschsperre an der Kategorie. Screenshot | Menüpfade für das Konzept | §2.4, §3, §6 |
| T02 | Permission `CATEGORY=Livos Eingangsrechnung` + `Mandant=@Filter(RS_Test)`; Testbenutzer U2 in `G_1001` | U2 sieht nur 1001-Belege (Suche, Akte, Rechnungseingangsbuch) | §2.3 |
| T03 | Orthogonalität: Permission an Rollengruppe, Werte nur über Gesellschaftsgruppe | bestätigt/widerlegt **A1** | §10.3 |
| T04 | Mehrfachwert „Mandant" = [1001, 1002] (z. B. Rahmenvertrag) | Sichtbar für G_1002? | §2.3 |
| T05 | Dokument ohne Mandant (leer) | Wer sieht es? (Risiko: niemand oder alle) | §2.5 |
| T06 | Zuordnung mit leerer Werteliste; Typ `NO_ASSIGNMENT` | bestätigt „empty array allows all values" | §10.4 |
| T07 | Benutzer in zwei Gruppen, eine mit DENIED | Setzt sich DENIED gruppenübergreifend durch? | §2.2 |
| T08 | Exakt- vs. Teilstring-Vergleich (`100` vs. `1001`); Platzhalter `*`/`?` im Set-Wert | feste Schlüssellänge nötig? | §2.1 |
| T09 | Globale Gruppe / verschachtelte Gruppe als Set-Zuordnung | Wirkt Vererbung? | §2.5; Q04 |
| T10 | Gruppenmitgliedschaft ändern → Zeit bis Wirksamkeit; Neuanmeldung nötig? | Onboarding/Offboarding-Latenz | §5 |
| T11 | Recht write ohne delete; Statuswechsel, Verknüpfen, Export ohne Zusatzrechte? „Attributänderung in Freigabe" vorhanden? | Rechtearten der UI | §2.2 |
| T12 | **Nur lesen:** vorhandene Profile „ERV - … [User]/[Group]/[ALL]" öffnen | exakte Restriction (Platzhalter, Eigenschaft) dokumentieren | §2.3 |
| T13 | Strukturregeln: ER → Kreditorenakte **und** Objektakte (2 Regeln); automatische Aktenanlage; leeres Erkennungsfeld; `createSiblingDossiers`; Vererbung | Mehrfachablage automatisch? | §3, §10.6 |
| T14 | 11 Währungs- und 11 Mehrfach-Eigenschaften in einer Kategorie; >89 Eigenschaften | Gelten Typ-Kontingente in der Cloud? | §4 |
| T15 | Zwei Gruppen mit gleichem 8-Zeichen-Präfix (`LIVOS_NORD_BUCH`/`LIVOS_NORD_FREI`) mit unterschiedlichen Rechten | 8-Zeichen-Regel irrelevant? | §4 |
| T16 | Eigenschaft/Kategorie umbenennen; Datentyp bzw. Mehrfach nachträglich ändern | Wirkung auf Zuordnungen, Suchvorlagen, smart invoice | §4 |
| T17 | Test-Kategorie: Frist 1 Monat `basedOn` Datumseigenschaft, `preventDeletion`; Aktivitäten prüfen; Löschzeitpunkt beobachten | Automatik abschaltbar? Protokoll? | §6 |
| T18 | Aktivitäten: Lesen/Download protokolliert? Export? Aufbewahrungsdauer? | Prüferanforderungen | §7 |
| T19 | Dataset mit 150 Werten (statisch); dynamische Wertemenge >100 | Bedienbarkeit der Auswahl | §4 |
| T20 | Rechnungseingangsbuch: Workflowberechtigung mit mehreren Mandanten oder Platzhalter | Aufwand für GF/Verbünde | §9 |
| T21 | Urkel-Bearbeiterfindung `group.name =~ /^Freigeber_#{voucher.company.nr}$/` | eine Regel für alle Gesellschaften | §9 |
| T22 | (Test-Tenant) Entra-Enterprise-App: SCIM-Provisioning + OIDC-SSO; Gruppen-IDs, Deaktivierung, B2B-Gast | Identitätskonzept | §5 |
| T23 | DmsConfig-Package-Installation Test → Prod; Export-Weg der Konfiguration | Transport-/Change-Konzept | §1 |

**Schriftlich bei d.velop anzufragen:**
1. Zugang zum Handbuch „d.velop cloud: Administrieren" (Login) bzw. zur Cloud-UI-Dokumentation für Berechtigungen, Filtermengen und Strukturen [Q26].
2. Obergrenzen: Permissions, Restriction Sets, Zuordnungen, Werte je Zuordnung, Gruppen, Dataset-Einträge, Eigenschaften je Kategorie/Typ.
3. Legal Hold; Abschaltbarkeit der automatischen Löschung; Aufbewahrungsdauer und Export der Aktivitäten; Leseprotokoll.
4. Delegierte Administration (Pflege von Restriction Sets durch Fachverantwortliche ohne Tenant-Admin-Recht).
5. Semantik `parent_id` bei smart-invoice-Mandanten; API für Workflowberechtigungen im Rechnungseingangsbuch.
6. Freischaltung custom logics / business objects; Edition und Lizenz (business vs. ultimate, externe Anwendende).
7. Volltext der KB-Artikel 000001933 / 000001740 / 000001900 (Entra OIDC, SCIM, LDAP in der Cloud) [Q19].

---

## 12. Korrekturbedarf in 04a / 03 (aus dieser Recherche)

| Stelle | Bisher | Neu (Beleg) |
|---|---|---|
| 04a §3.2/§3.3/§3.5, R-01, R-02 | Dokumentklassen, `@D3GROUP`, dokumentartunabhängige Klasse; Cloud offen | Cloud: Permissions + Restriction Sets + Platzhalter [Q01]; Option A bleibt, andere Technik |
| 04a §2.3 Nr. 1–2, G03, G04, G13 | DB-Positionsplan, Kürzel, gleiche Position für „Gesellschaft" | in der Cloud **nicht** anwendbar (kein Positions-/Kürzelfeld; Restriktion per Eigenschafts-ID) [Q01]; Typ-Kontingente T14 |
| 04a G10 / §2.2 | 8-Zeichen-Gruppenregel | nur On-Prem; Cloud referenziert Gruppen-IDs [Q01] → T15 |
| 04a S16, G17, R-10 | Aktenbildung nur On-Prem belegt | Cloud belegt: Strukturregeln [Q01], Funktions- und Leistungsbeschreibung [Q02; Q03] |
| 04a R16, R-07 | Entra-SSO/SCIM nicht belegt | OIDC-SSO, AD (ADFS/LDAP), weitere OIDC-IdP (ab business) [Q03]; SCIM 2.0 [Q04; Q05]; Entra als IdP genannt [Q13] |
| 04a G16, R11 | Sub-Administration Cloud nicht belegt | weiterhin nicht belegt; DmsConfig nur Tenant-Admins [Q01] |
| 04a S19, §6, R-05/R-06 | Retention über storage manager | Cloud: Kategorie-`retention` + `preventDeletion` [Q01; Q02; Q03]; storage manager = On-Prem [Q23] |
| 04a G09 | Obergrenze Wertemenge nicht dokumentiert | dynamische Vorschlagswerte max. 100 je Wertemenge [Q02]; statisch O |
| 04a R15 | Lizenztypen nicht belegt | Editionsmatrix basic/business/ultimate inkl. Speicher 100/1.000/2.000 GB [Q03] |
| 04a R-15 | d.velop contract ohne Beleg | **d.velop contracts (Cloud)** belegt; Rechte je Organisation × Vertragstyp (Lesen/Schreiben/Löschen) [Q10] |
| 03 §1.3 | Cloud-Menüpfad Aufbewahrung offen | Einstellung liegt an der Kategorie [Q01]; UI-Pfad T01 |
| 03 §5.3 G19, §7 Nr. 20 | Cloud-Berechtigungsoberfläche ungeprüft | Mechanik belegt [Q01]; UI weiterhin T01 |

---

## Anhang: Quellenverzeichnis

| ID | Quelle | URL | Lokale Kopie (SP/work/…) |
|---|---|---|---|
| Q01 | **DmsConfig API** (OpenAPI 3.0.1, „configuring d.velop documents repositories in the cloud") | https://help.d-velop.de/dev/api/openapi/dmsconfig · Übersicht: https://help.d-velop.de/dev/documentation/dmsconfig | _web15/dmsconfig.yaml |
| Q02 | Funktionsbeschreibung d.velop documents, Version D010522543/2025-11-28 | https://my.d-velop.cloud/center/a/dvelop-documentsfreefor30days/legal/funktionsbeschreibungdvelopdocuments?language=de · Spiegel: https://s3.eu-central-1.amazonaws.com/mediamanager.cloudcenter.service.d-velop.cloud/00fdd0bf-d698-4e3d-8a46-34c864678fdc | _web15/fb_documents_mycloud.txt |
| Q03 | Leistungsbeschreibung d.velop documents (Cloud), Version 2025-02-18, inkl. Editionstabelle S. 11–12 | https://s3.eu-central-1.amazonaws.com/mediamanager.cloudcenter.service.d-velop.cloud/71677a83-7cdb-4097-bfc1-bec37f37bc07 | _web15/lb_documents_cloud_2025-02-18.txt, lb_p11.png, lb_p12.png |
| Q04 | d.velop usermanagement: Administrieren (cloud) | https://help.d-velop.de/docs/api/documentations/de/usermanagement-cloud-on-premises/cloud/pdf · https://help.d-velop.de/docs/de/pub/usermanagement-cloud-on-premises/cloud/verwalten-von-benutzern-und-gruppen/automatisiertes-verwalten-von-benutzern-und-gruppen | _web15/um_cloud.txt |
| Q05 | d.velop usermanagement API (SCIM 2.0) | https://help.d-velop.de/dev/api/openapi/usermanagement | _web15/oa_usermanagement.yaml |
| Q06 | Identityprovider API (SCIM 1.1, OIDC-Callback) | https://help.d-velop.de/dev/api/openapi/identityprovider | _web15/oa_identityprovider.yaml |
| Q07 | d.velop smart invoice Cloud: Administrieren | https://help.d-velop.de/docs/api/documentations/de/smart-invoice-cloud/cloud/pdf · …/docs/de/pub/smart-invoice-cloud/cloud/konfigurieren-von-dvelop-smart-invoice/interagieren-mit-dvelop-documents · …/wissenswertes-zum-onboarding · …/wissenswertes-zu-berechtigungen | _web15/smart-invoice-cloud.txt |
| Q08 | d.velop smart invoice-API (developer, cloud) | https://help.d-velop.de/docs/api/documentations/de/smart-invoice-developer/cloud/pdf | _web15/smart-invoice-developer.txt |
| Q09 | d.velop invoices – Rechnungseingangsbuch: Anwenden (cloud) | https://help.d-velop.de/docs/api/documentations/de/invoice-monitor/cloud/pdf | _web15/invoice-monitor.txt |
| Q10 | d.velop contracts: Administrieren (cloud) | https://help.d-velop.de/docs/api/documentations/de/contracts-admin-cloud/cloud/pdf · …/docs/de/pub/contracts-admin-cloud/cloud/betrieb-und-verwaltung/verwalten-von-berechtigungen | _web15/contracts-admin-cloud.txt |
| Q11 | d.velop custom logics: Administrieren (cloud) | https://help.d-velop.de/docs/api/documentations/de/custom-logics-admin/cloud/pdf · …/docs/de/pub/custom-logics-admin/cloud/wertemengen/erstellen-einer-dynamischen-wertemenge | _web15/custom-logics-admin.txt |
| Q12 | d.velop business objects: Administrieren (cloud) – Berechtigungen, Quotas, Bereitstellung | https://help.d-velop.de/docs/de/pub/business-objects-admin/cloud/konfigurieren-der-berechtigungen · …/basisinformationen/quotas · …/bereitstellung-von-dvelop-business-objects · API: https://help.d-velop.de/dev/api/openapi/businessobjects | _web15/oa_businessobjects.yaml |
| Q13 | d.velop connect for Microsoft Dynamics 365 (cloud) – Verwenden von technischen Benutzern (Menüpfade, Entra ID als IdP) | https://help.d-velop.de/docs/de/pub/connect-dynamics-365/cloud/tipps-und-tricks/verwenden-von-technischen-benutzern | _web15/connect-dynamics-365.txt |
| Q14 | d.velop tenant access: Administrieren (cloud) | https://help.d-velop.de/docs/api/documentations/de/tenant-access-admin/cloud/pdf | _web15/tenant-access-admin.txt |
| Q15 | d.ecs open id provider app: Administrieren (cloud) | https://help.d-velop.de/docs/api/documentations/de/open-id-provider-app/cloud/pdf | _web15/openid-provider-app.txt |
| Q16 | d.velop documents: Anwenden (cloud) | https://help.d-velop.de/docs/api/documentations/de/documents/cloud/pdf | _web13/documents.txt |
| Q17 | d.ecs dashboard: Administrieren (cloud) | https://help.d-velop.de/docs/api/documentations/de/dashboard-admin/cloud/pdf | _web15/dashboard-admin_cloud.txt |
| Q18 | d.3one: Administrieren – „Welche Aktivitäten werden zu einem Element protokolliert?" (On-Prem-Webclient; UI-Begriffe) | https://help.d-velop.de/docs/de/pub/one/2026.q3/troubleshooting-und-faq/welche-aktivitaten-werden-zu-einem-element-protokolliert | – |
| Q19 | d.velop Knowledge Base (nur Titel/Suchauszug; Seite lädt ohne Login/JS nicht): 000001933 (OIDC + Azure AD), 000001740 (Benutzer/Gruppen aus Azure AD bereitstellen), 000001900 (LDAP-Provider in der d.velop-Cloud), 000001455 (OIDC-Werte Azure AD) | https://kb.d-velop.de/s/article/000001933?language=de · https://kb.d-velop.de/s/article/000001740?language=de · https://kb.d-velop.de/s/article/000001900 · https://kb.d-velop.de/s/article/000001455?language=de | – |
| Q20 | Microsoft Learn: Grundlegendes zur Anwendungsbereitstellung in Microsoft Entra ID (SCIM, verschachtelte Gruppen, B2B, Zyklen) | https://learn.microsoft.com/de-de/entra/identity/app-provisioning/how-provisioning-works | – |
| Q21 | d.velop Schulung „d.velop documents administrieren (Cloud)" (Inhalte: Eigenschaften/Wertemengen, Kategorien, Berechtigungen, Strukturen und Aktenpläne; „d.velop webadmin") | https://store.d-velop.com/de/d.velop-documents-Cloud-administration/R0000340 | – |
| Q22 | d.velop cloud migration: Administrieren (cloud) | https://help.d-velop.de/docs/api/documentations/de/cloud-migration-admin/cloud/pdf | _web13/cloud-migration-admin.txt |
| Q23 | d.ecs storage manager: Administrieren (On-Prem; Modul „cloud storage") | https://help.d-velop.de/docs/de/pub/storage-manager/latest | _web13/storage-manager.txt |
| Q24 | d.velop DMSApp API | https://help.d-velop.de/dev/api/openapi/dms-app | _web15/oa_dms-app.yaml |
| Q25 | d.velop mail dispatcher: Administrieren (Hinweis „Administrative group for the tenant") | https://help.d-velop.de/docs/api/documentations/de/mail-dispatcher-admin/cloud/pdf | _web15/mail-dispatcher-admin.txt |
| Q26 | Handbuch „d.velop cloud: Administrieren" (nur mit Login; Seitentitel im Such-Index: Cloudberechtigungen, Cloudmandanten, Verwaltung, „Was ist eine Wertemenge?" usw.) | https://help.d-velop.de/docs/de/pub/cloud/cloud (Login) · PDF-Endpunkt liefert 401 | – |
| Q27 | Records Management Public API (z.d.A.-Prozess) | https://help.d-velop.de/dev/api/openapi/dvelop-records-management | _web15/oa_dvelop-records-management.yaml |

Hinweis zur Aktualität: Die Funktionsbeschreibung (2025-11-28) und die Leistungsbeschreibung (2025-02-18) sind die zum Abrufzeitpunkt verlinkten Fassungen. Vor Angebotsabgabe die gültige Fassung im d.velop cloud center bzw. store neu ziehen.
