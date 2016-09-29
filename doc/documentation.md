# Event Driven Process Engine
*Gruppe Processmaker*<br>
*Lukas Rosentreter, Alexander Senger*

## Inhalt

<!--
	[toc]
-->


## Kontext und Motivation
### Posed Questions
> * In welchen Bereich ordnet sich das Projekt ein? (Where?)
> * Wer sind potenzielle Nutzer? (Who?)
> * Wieso ist es überhaupt interessant sich damit zu beschäftigen? (Why?)

### Welche Bereiche sind betroffen?
#### Complex Event Proccessing
...oder kurz *CEP*. Dabei wir ein Fluss an Daten beziehungsweise Ereignissen (Events) aus einer oder mehreren Quellen zusammengeführt und in Echtzeit analysiert. Echtzeit deswegen, weil genau das es von herkömmlicher Analyse der Daten, nach dem aggregieren, abgrenzt. <br>
Wissen, dass aus der Kombination mehrerer Ereignisse gewonnen wird, sind Komplexe Ereignisse. Ereignisse sind nicht weiter spezifiziert oder limitiert und können von Wetter-Daten über Börsentrends bis zu Netzwerk-Logs reichen. <br>
Bei der Analyse spielen sowohl die konkreten Werte, als auch der Unterschied zwischen ihnen (Delta) eine Rolle. <br> 
Um Zusammenhänge und mögliche Schlüsse verlässlicher aufdecken, respektive treffen zu können, ist eine kritische Menge an Daten von Nöten. Ein kontinuerlicher Strom an zusammenhängenden Daten wird daher als Voraussetzung angenommen. 

Es lassen sich alleinig aus der Beschreibung von CEP keine Rückschlüsse auf potentielle Nutzer oder Andendungsbereiche ziehen, denn relativ große Mengen an Daten, lassen sich, mindestens durch logs, heutzutage sehr leicht produzieren oder aggregieren. Ausgehend davon ist es theoretisch allen Menschen möglich, ihre Daten durch eine CEP zu schleusen und Schlüsse über ihr System, ihre Prozesse oder Strategien zu ziehen. 

#### Process Execution
Als Process Execution Engine bezeichnet man Software, die darauf abzielt (Geschäfts-) Prozesse zu unterstützen und Teile davon gegebenen Falls zu automatisieren. Diese Prozesse sind im Vorfeld modelliert und bilden in der Regel häufig auftretende Abläufe ab. Zur Modellierung wird eine besondere Sprache verwendet, in unserem Fall *Business Process Model and Notation* (BPMN). Alternativ gibt es weitere Sprachen, wie z.B. *Business Process Execution Language* (BPEL). Ein Prozess selber kann unter anderem verschiedene Ereignisse und Aktivitäten beinhalten, sowie Schnittstellen nach außen. Ob diese zu Menschen oder Maschienen sind, Daten senden oder empfangen spielt dabei keine Rolle. 
Die Engine hilft dabei, die vorhandenen Prozesse aus- und durchzuführen, aber auch zu analysieren und Möglichkeiten zur Verbesserung aufzuzeigen.

Process Execution Engines können zum Beispiel benutzt werden, um eine Bestellung in einem Onlineshop oder eine Supportanfrage zu unterstützen und umzusetzen. Ein Prozess kann dabei wie folgt modelliert sein.

> **TO DO**
> 
> Bild!

Ein Kunde legt in einem Webshop ein Produkt in den Warenkorb und klickt auf "Jetzt bestellen". Der Prozess beginnt damit, zu überprüfen ob der Warenkorb nicht leer ist. Ist die Bedingung erfüllt geht es weiter zur Kasse. Der Shop bietet mehrere Zahlungsmöglichkeiten und der Kunde wählt seine aus. Der Prozess wartet nun, bis er bestätigung der Zahlung hat. Ob diese sofort (Kreditkarte) erfolgt oder erst einige Tage später (Kauf auf Rechnung) ist dabei egal. In dem Moment in dem die Besätigung erfolgt, wird geprüft ob und wenn ja in welchem Lager die Waren verfügbar sind. Angenommen die Waren sind alle im gleichen Lager vorrätig, bekommt ein Mitarbeiter eine Liste in welchem Regal welches Produkt liegt und kann anfangen das Paket zu packen. Sobald der aufgedruckte Barcode auf dem Paket gescanned wurde, bekommt der Kunde eine E-Mail mit der Versandbenachrichtigung. Bei Ankunft des Pakets wird der Barcode erneut gescanned und der Prozess mit der Unterschrift des Kunden abgeschlossen. 

~~Für Supportmitarbeiter kann das dann wie ein Ticketsystem aussehen, bei dem Anfragen automatisch verteilt und weitergeleitet werden.~~

#### EventDriven-BPM
Durch die sehr offenen use cases der beiden betroffenen Bereiche, ergeben sich auch in der Schnittstelle der beiden noch eine Unzahl verschiedener Anwendungen. Laut Theorie wäre es auch dem Hobby-Tüftler für seine Heim-Automation möglich Event-Driven-Process-Models zu verwenden, jedoch scheint der Aufwand kaum in irgendeiner Relation zum nutzen zu stehen. Wesentlich wahrscheinlicher ist die Anwendung ab kleinen bis mittelständischen Unternehmen oder auch Start-Ups. Der Hautpaufwand für Unternehmen, die noch keine Prozess-Modelle nutzen besteht dann darin, die Abläufe des Tagesgeschäft in solche zu übersetzen. Start-Ups hingegen haben die Möglichkeit, gleich von Beginn, ihre Geschäfte Event-Driven anzulegen. In beiden Fällen gibt es den Unternehmen - ob etabliert oder nicht - die Möglichkeit ihre Prozesse zu analysieren, anzupassen und zu optimieren. <br>
Zum Beispiel kann bei einer Bestellung bei Zalando auf einen Event Stream für Verkehrsdaten innerhalb des Business Process zugegriffen werden und anhand der Auswertung entschieden werden, an welches Lager die Bestellung weitergeleitet wird.
Umgekehrt können auch die Lieferfahreuge wiederum Events für die CEP Engine produzieren, die dann bessere Einsicht in die Verkehrslage ermöglichen.

### Wieso ist es interessant sich damit zu beschäftigen?
> **TO DO**
> 
> * feritg machen...
> * "Future appilcations might even hold the possibility of Event Driven Process Modeling."


BPM beschäftigt sich mit einzelnen Prozessen eines "Business". CEP schafft es zusammenhänge zwischen vielen (zu vielen für Menschen?) Daten automatisiert herzustellen. Das Zusammenspiel der Beiden, ermöglicht ein ganzheitlicheres Bild auf Businessabläufe und Zusammenhänge zwischen diesen aufzuzeigen. Dies erfordert (noch) selbstverständlich Menschliches eingreifen. 

Insbesondere ...

## Problemstellung
### Fragestellung
> Welches Problem löst Ihr in Eurem Projekt? Hier bitte auch die zugeordnete Process-Engine mit einbauen, sprich das Problem für Eure Engine "instanziieren".

Auf einfachster Ebene gesprochen, verbindet die entwickelte Software zwei Anwendungen. Auf der einen Seite eine CEP-Engine, auf der anderen eine BPM-Software. Beides sind Open-Source Projekte. Die CEP-Engine, Unicorn, entwickelt vom Hasso-Plattner-Institut in Potsdam wurde in Java geschrieben und läuft auf einem Apache Tomcat Server. ProcessMaker, entwickelt durch ProcessMaker Inc., ist hauptsächlich in PHP geschrieben. Ein Server für ProcessMaker ist nicht vorgegeben, doch Apache HTTP Server wird empfohlen und in der Dokumentation verwendet. Durch die Server Architektur bringen beide Komponenten REST-APIs mit sich, sodass eine Middleware die naheliegendste Entscheidung war. 

Schon von der Teminologie her bringen sowohl Complex Events als auch BPMN *events* mit. In Unicorn können Queries erstellt werden, die auf eine Abfolge von eingehenden Events reagieren. Ein solches, aus mehreren Granulaten bestehendes, Event nennt man Komplexes Event. Die Daten der einzelnen Events und den Typ und die ID des Komplexen Events, können dann an einen vorbestimmten Ort (z.B. via REST-API) übergeben werden. Events in BPMN repräsentieren Dinge, die sich Ereignen, wie zum Beispiel, das Eingehen einer Bestellung. BPMN Events teilen sich in drei Typen auf: Start, Stopp und Intermediate. Events können dabei jeweils fangend (Catching) oder werfend (Throwing) sein. Darüber hinaus gibt es weitere Klassifizierungen, die aber hier keine weitere Rolle spielen sollen. 

Das Ziel war, die Events beider Anwendungen zu verknüpfen und insbesondere für die BPMN-Seite Schnittstellen für jeden Typen, sowohl Catching als auch Throwing zu haben. Die schlussendliche Funktionalität sollte beinhalten, ein Complexes Event an ProcessMaker zu senden (und dadurch einen Prozess zu starten, zu beenden oder zwischendurch zu beeinflussen) und von ProcessMaker aus ein Event an Unicorn zu senden und es in den Event-Fluss einzugliedern. 

### Diesen Absatz würde ich aus Problemstellung nehmen und wo anders einordnen, ggf. inhaltlich auseinanderziehen

Das neue Ziel war weiterhin Komplexe Events von Unicorn an ProcessMaker und zurück zu senden, in ProcessMaker aber Aktivitäten zu nutzen um das Verhalten von Events nach außen zu simulieren. Eingehende Events lassen sich von der Middleware auffangen, an den Aktivitäten Endpoint pushen und von der Middleware automatisch weiter routen. Werfende Events zu simulieren ist nicht ohne weiteres möglich, nicht zuletzt, weil die API keine Callbacks ermöglicht. Aber eine geroutete Aktivität landet in der Inbox des zuständigen Nutzers und diese ist wiederum per API abzufragen. Somit polled die Middleware die Inbox eines designierten Unicorn-Nutzers und pushed gegebenenfalls ein Event in den Datenfluss von Unicron. 


## Verlauf des Projektes

### Planung
Die Milestones waren den gesamten Verlauf des Projekts über sehr grob gehalten. Nicht zuletzt, da wir als einziges Projekt Management Tool GitHub hatten und mit den dortigen Werkzeugen *Wiki* und *Issues* gearbeitet haben. So gab es zu Beginn einen Sechsschrittigen Plan im Wiki, der wie folt aussah.

> 1. **Setting up the two parallel systems** *Until 15.05.*
> 	* Create (Docker) Image, preferably Debian
>	* Install Dependencies and Unicorn & Processmaker
>	* Setup coding environment
> 2. **Identifying Interfaces of the two systems** *Until 22.05.*
> 	* Make familiar with interface documentation
> 	* Simple tryout with small scripts and examples
> 3. **Normalising the data and rudimentary communication between systems** *Until 31.05.*
> 4. Eliminating the kinks, testing, debugging
> 5. Sophisticating the communication and broadening of the possibilities
> 6. Further Testing, Debugging
> 
> <div style="text-align: right; font-style: italic;"><a href="https://github.com/hupda-edpe/p/wiki/Project">https://github.com/hupda-edpe/p/wiki/Project</a></div>

Enstanden ist dieser Plan vorwiegend aus den bereitgestellten Folien mit der Aufgabenstellung und dem generellen Grundgerüßt, das für fast jedes Setup von Applikationen notwendig ist. Während des Projekts wurde lediglich drei bis vier Male mit der konkreten Planung gearbeitet, aber die einzelnen Schritte und die Abfolge dieser, stimmten mit der Realität überein. Im Verlaufe der einzelnen Phasen, sind diese nach Bedarf präzisiert und arbeitsteilig abgearbeitet worden. <br>
Auffällig ist, das in der Planung keine Entscheidungen beziehungsweise konkreten Aussagen zum Endgültigen Produkt sind (z.B. Middleware oder die Nutzung von APIs). Architektur und Scope wären zu Beginn sicherlich auch mit relativer Genauigkeit vorhersehbar gewesen, schien aber zweitrangig gegenüber dem vergleichsweise hohen Setup-Aufwand der beiden bestehenden Software Projekte. Erst nach erfolgreichem zum-laufen-bringen von Unicorn und ProcessMaker ging es um die effizienteste Variante, wie diese zu verknüpfen sind.<br>
Diese herangehensweise ist prototypisch für viele weitere Planungs-Entscheidungen des Projekts. So kamen weitere Wiki-Seiten dazu, die sowohl den theoretischen Ablauf für das arbeiten mit Aktivitäten, als auch den API-spezifischen Ablauf dokumentierten. Je weiter das Projekt fortschritt, desto klarer wurde die Aufgabenteilung im Team und die eigentliche Planung und Dokumentation trat in den Hintergrund, sodass gegen Ende des Projektes durch direkte Kommunikation die anstehenden Aufgaben leicht abgearbeitet werden konnten. 


### Workflow
* Different OSes (Linux / OS X)
* Differnt editors (Sublime / Atom)
* Same container software (Docker)
* Repo / Versioning: GitHub
* Inner-Team communication: 
	* Mostly Threema
	* Sometimes Mail
	* Meetups - usually before meetings

### Setup
#### Setting up containers (in general):

* Time consuming
* Made initial debugging harder (Error could be on multile levels)
	* Container config
	* Software (ProcessMaker / Unicorn)
	* Our own code

#### Setting up the PM Container:

* Required a LAMP stack, which is easily done with Docker Compose
	* A Linux image with Apache and PHP is readily available from Docker Hub
	* A MySQL image is also readly available
* Installing libraries, dependencies and requirements from ProcesMaker was a bit tricky and required a lot of Stackoverflow reading. 
* The installation guide of ProcessMaker luckily is thourough, even though it misses a couple of requirements. 
* Another big issue was the shared folder between host and image, due to usage rights. The Apache Server required `www-data` as owner whereas docker only allows the user with `uid 1000` to read/write host files. Setting the `uid` of `www-data` to `1000` solved the problem.

#### Setting up the Unicorn Container:

* At first: Didn't do it ourselves. We copies the Dockerfile from the `shared` repo.
* Later modified it, due to issues on OS X
	* Simplifying the script didn't work due to unknown reasons
	* Solution: Compiling the code and deploying the readily compiled `.war`
	* For further development a more flexible solution should be implemented
	* Precompiling turned out to be smart, since the repository was removed from GitHub

### Kommunikation mit ProcessMaker

Es stellte sich die Frage, wie wir mit ProcessMaker interagieren.

#### BPMN in PM
EventTypes und Events sind in Unicorn mittels BPMN definiert.
Auch die Prozesse, einschließlich Tasks und Events sind in ProcessMaker mit BPMN modelliert.
Es lag daher nahe, EventTypen zu modellieren, die für den Austausch zwischen Unicorn und PM gedacht sind. Es war zudem ein Bestreben diese BPMN Erweiterungen zwischen den drei Projektgruppen auszutauschen, so dass eine Interkompatiblität entsteht.
Der Versuche eigene BPMN Erweiterungen in ProcessMaker einzuspeisen schlug allerdings in ganzer Linie fehl. Tatsächlich war es nicht mal möglich standardkonforme Modelle zu importieren, lediglich eigens aus ProcessMaker exportierte Prozesse ließen sich wieder importieren.

#### Events
Nachdem dieser erste Ansatz keine Früchte trug, stellte sich dennoch die Frage  mittels ProcessMaker Events die Kommunikation mit Unicorn zu steuern.
Auch hier wurden wir enttäuscht, da es uns nicht einmal gelang Events aus zwei verschiedenen Prozessen innerhalb von ProcessMaker zu verbinden. An die REST-API waren Events nicht angebunden.

Da Events auch seitens ProcessMaker über einen Pull-Mechanismus implementiert waren, den man eigenständig von außen z.B. mit einem Cronjob auslösen musste, wäre man möglicherweise über diesen Ansatz zu einer Lösung gekommen.
Dieser Weg schien aber in erster Linie aus Trial and Error und Reverse Engineering zu bestehen und so ließen sich Zeitrahmen und Arbeitsumfang nicht abschätzen. Daher haben wir uns für die vielversprechendere Lösung über Tasks entschieden.

#### Tasks
Die REST-API für Tasks war gut dokumentiert und bot uns alle nötigen Möglichkeiten der Interaktion. Die Vermutung, dass die ProcessMaker eigene Weboberfläche selber über diese API mit der Execution Engine kommuniziert, ist sogar naheliegend.
Leider war dies nicht der syntaktisch korrekte Ansatz, aber der einzige, der im Rahmen dieses Semesterprojektes als machbar wirkte.

TODO: Vorigen und folgenden Absatz zusammenführen.

Aktivitäten in BPMN stellen zu erledigende Aufgaben dar und sind daher semantisch nicht ganz akurat auf Komplexe Events abzubilden. Aktivitäten sind in ProcessMaker konkreten Nutzern oder Nutzergruppen des Systems zugeordnet und müssen entlang des Prozessablaufs geroutet werden. Sowohl das Abarbeiten als auch das routen sind via der API verfügbar. 

### Prototyp für ProcessMaker
Da der generelle Ansatz zur Kommunikation mit ProcessMaker bereits eine Hürde war, haben wir uns dann dazu entschieden zunächst einen Prototyp zu implementieren um damit die Möglichkeiten der API auszuloten und zu testen. Desweiteren diente dies auch dazu unseren Zwischenstand und das bis dahin gesammelte Wissen über unsere spezifische Process Execution Engine den anderen Gruppen vorzustellen und zu demonstrieren.

Um flexibel und interaktiv zu sein haben wir als Programmiersprache für den Prototyp Python gewählt.
Das stellte sich als eine gute Wahl heraus, da wir so zügig zu einem funktionierenden Ergebnis gekommen sind.
Außerdem haben wir damit einen guten Grundstein für die eigentliche Middleware, die das Ziel des Projektes war, gelegt.

### Django Middleware
Bis zu diesem Zeitpunkt war lediglich die Seite richtung ProcessMaker abgedeckt.
Da man beim Registrieren von EventQueries in Unicorn einen HTTP Endpoint als Callback angeben musste, war klar, dass wir irgendeine Form von HTTP Server anbieten mussten.
Wir wollten Teile vom Prototyp wiederverwenden und uns nicht damit aufhalten, ein Callback-Interface für Unicorn selber zu implementieren, also haben wir uns dafür entschieden einen Django-Server aufzusetzen.
Das hatte außerdem den Vorteil, dass man die Middleware selber leicht über eine Weboberfläche bedienen konnte.

### Obstacles
### TODO: Dieser Abschnitt eventuell eher unter Reflektion?
* ProcessMaker
	* Buggy community Version, especially MySQL errors.
		* Login DB didn't install
		* Query for registering OAuth Apps threw an error
		* Wrong DB connector listed in system requirements
	* Different nameing conventions
	* Events only accessible through Cron Jobs
		* Not a problem per se but much more difficult due to containerized setup
			* Requires a lot of scripting, for automated setup
		* Solution: We ended up using the so called Tasks due to them being available through the API
	* API
		* Even though it is quite powerful and well documented, it took some time to figure out that some keys are named doffernt but actially mean the same. 
* Unicorn 
	* The given Docker config wouldn't run on OS X (Compilation: Yes, Deployment: No)
	* Poorly Documented
	* Source and Doc removed from GitHub during the end of the Project. Good thing, local Backups exist. ;-)
* External Circumstances
	* No severe issues. 
	* Good communication => Lightweight and instant
	* Few resources timewise
		* Absence from inter-team meeting
			* turned out not to be too bad. The Teams didn't intersect too much
		* In the beginning we could sometimes only manage to have 1 team member present. 


## Architektur des ProcessMaker-Unicorn-Connectors


Ab dann waren es die Endpoints der API die in einer eigenen Wrapper Klasse aufrufbar gemacht wurden und auf komplexere Funktionen erweitert. Von vornerein geplant war der Wrapper als Modell allerdings nicht. 

Das ein Unicorn Wrapper entstand, war ebenfalls nicht teil des initialen Plans, aber ergibt in anbetracht der Tatsache, dass unsere Lösung eine eigenständige Middleware ist, Sinn. 


### Posed Questions
> * Tragweite des Produkts
> * umgesetzte Funktionen
> * Grenzen...

### Architektur
* Middelware. 
* Server der beide APIs verbindet
* Fasaden (Wrapper) zu beiden Seiten hin.

Besser wäre: Beide Engines so modifiezieren, dass sie direkt miteinander reden. (Push/Pull) Bzw. Eine Software so zu erweitern, dass sie mit der anderen reden kann. 

### Setup
Using container was a good solution, especially in the beginning the circumstances weren't clear. (see Workflow). Containers offer several advantages:

* Easy (re)installs for all team members
* Quick way to purge the system and start over
* No system requirements, version incompatablities, ... 
* Easyly transferable due to small file size (compared to VMs)
* No IDE required.

## Reflektion
### Posed Questions
> * Wie nutzbar ist das Produkt?
> * Was müsste getan werden, um es "richtig nutzbar" zu machen?
> * Was würde man wohl als nächstes verbessern/erweitern?
> * Wie viel der Lösung ist spezifisch für Eure Engine?

### Wie nutzbar ist das Produkt?
* Ok. Könnte ausgereifter sein. (Django + Weboberfläche vielleicht keine optimale Lösung)
* Solider 1. Prototyp.

### Verbesserungsvorschläge (zur Nutzbarkeit)
* Würde so nicht in Produktion genommen werden. 
* Nicht zuletzt wegen APIs bräuchte man mehr Sicherheit. 
* Ebenso müsste mehr Automatisiert werden. 
* Die Middleware ist auch nicht auf evtl. große Datendurchsätze getestet. (ProcessMaker auch nicht.) Evtl. müsste die Middleware sogar als Buffer wirken. 
* Config zusammenführen. Bisher wird an vielen verschiedenen Stellen immer wieder das gleiche eingefügt. Hierzu eine einheitliche Konfigurationsdatei im root Verzeichnis schafft ein einheitlicheres feel eines SW-Produktes. 

### Engine-Spezifisches
Durch den implementieren REST basieren Wrapper für ProcessMaker, ließe sich, mit vergleichsweise geringem Aufwand, jede andere REST fähige Software anbinden. Dann allerdings ebenso via Tasks und nicht Events. Je nach eingesetzter Engine, der Mächtigkeit der dort implementieren Events und deren Erreichbarkeit via API, varriert der Aufwand sehr stark. 

## Dokumentierter Code

### Readme
### Howto
```sh
cd processmaker
docker-compose up --build

cd ../unicorn
docker-compose up --build

cd ../connector
docker-compose up --build

```
### Manual

# Bullshit und Anhang
| | ![Unicorn Logo](img/unicorn.png) | EDPE | ![ProcessMaker Logo](img/pm.png) |
| :--- | --- | --- | --- |
| Engine | Esper | Django | Zend |
| Language | Java | Python | PHP |
| LOC | N.a.N. | ~500 | > 10000 |
