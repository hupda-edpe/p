<!--
Use Marp https://yhatt.github.io/marp/ to compile.

$theme: default
$size: 4:3
-->

# ProcessMaker
Lukas Rosentreter, Alexander Senger

---
# Inhalt

* Motivation
<!--
	* <small><small>Einordnung</small></small>
	* <small><small>Nutzer</small></small>
--> 
* Projekt
<!--
	* <small><small>Vorbereitung und Planung</small></small>
	* <small><small>Workflow</small></small>
	* <small><small>Schwierigkeiten</small></small>
-->
* Lösung
<!--
	* <small><small>Architektur</small></small>
	* <small><small>Prinzip</small></small>
	* <small><small>Funktionsweise</small></small>
	* <small><small>Umfang</small></small>
	* <small><small>Grenzen</small></small>
-->
* Reflektion
<!--
	* <small><small>Nutzbarkeit</small></small>
	* <small><small>Verbesserungen</small></small>
	* <small><small>Flexibilität</small></small>
-->

---
# Motivation
## Einordnung

---
# Einordnung

* (Wirtschafts-) Informatik
* Event Driven Software

---
# Motivation
## Nutzer

---
# Nutzer
* Datenaggregaten
* Modellierbare (Geschäfts-) Abläufe


---
# Projekt
## Vorbereitung & Planung

---
# Vorbereitung & Planung
1. Schritt: Grober Funktionsumfang
2. Schritt: Anpassung auf PM API

---
# Vorbereitung & Planung

## 1. Schritt

> A Model is triggered because of a sequence of Events.
>  <small> &dash; aus Wiki "Project"</small>

## 2. Schritt
> 1. Get a List of all Projects
> 2. Get a List of all Starting Tasks in the Project
> 3. Start a new Case
> 4. Route Case
>
> <small>&dash; aus Wiki "PM API: Start a Case"</small>

---
# Projekt
## Workflow

---
# Workflow
* Linux / OS X
* Texteditor, keine IDE
* Docker
* GitHub
* Threema

---
# Projekt
## Docker

---
# Docker
**Gute Wahl!**

* Verschiedene OS
* Schnelles Neustarten
* Keine Versions oder Abhängigkeiten Probleme
* Kleine Dateien (vgl. VMs)
* Keine IDE notwendig

---
# Projekt
## Schwierigkeiten

---
# Schwierigkeiten
## ProcessMaker

* Viele Bugs in Community Edition
	* Falscher MySQL Connector in den Requirements
	* Einige Tabellen nicht installiert
	* Queries (z.B. für OAuth registration) falsch zusammengesetzt.
	* ...
* Inkonsistente Namensgebung

---
# Schwierigkeiten
## ProcessMaker

* Events nicht über API erreichbar
	* Cron Jobs. Hoher Konfigurationsaufwand.
	* Tasks (Aktivitäten) sind über API erreichbar.

---
# Schwierigkeiten
## Unicorn
* Der "shared" Docker lief nicht auf OS X
	* Vorkompiliert und manuell Deployed
* Quellcode verschwand

---
# Schwierigkeiten
## Extern

* Zwischenzeitlich wenig Zeit
	* Abwesenheit beim inter-team Treffen
	* Bei Veranstaltungen nur einer anwesend
* Keine weiteren, schwerwiegenden

---
# Lösung
## Architektur

---
# Architektur

* Middleware
* Wrapper / Fassaden
* Django Server (Python)
* 3 separate Container
	* Unicorn
	* ProcessMaker
	* Connector

---
# Lösung
## Prinzip

---
# Prinzip

* Polling von ProcessMaker Daten
* Push von Unicorn an Connector
* Mapping von Events zu Tasks im Connector

---
# Lösung
## Funktionsweise

* ...


---
# Lösung
## Umfang

---
# Umfang

---
# Lösung
## Grenzen

---
# Grenzen

---
# Reflektion
## Nutzbarkeit

---
# Nutzbarkeit

* Solider 1. Prototyp
* Im Betriebsalltag so nicht einsetzbar
* Gut um zu testen, ob ED-BMP gut für einen ist

---
# Reflektion
## Verbesserungen

---
# Verbesserungen

* Sicherheit
* Automation
* Tests
	* insb. große Datenmengen
* Zusammengeführte Konfiguration

---
# Reflektion
## Flexibilität

---
# Flexibilität

* REST-basiert
	* Alle REST Engines möglich
* Middleware + Wrapper
	* Leicht zu implementieren
* Tasks nicht Events
	* Abhängig von Engine
