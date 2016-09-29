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
...oder kurz *CEP*. Dabei wir ein Fluss an Daten beziehungsweise Ereignissen (Events) aus einer oder mehreren Quellenzusammengeführt und in Echtzeit analysiert. Echtzeit deswegen, weil genau das es von herkömmlicher Analyse der Daten, nach dem aggregieren, abgrenzt. <br>
Wissen, dass aus der Kombination mehrerer Ereignisse gewonnen wird, sind Komplexe Ereignisse. Ereignisse sind nicht weiter spezifiziert oder limitiert und können von Wetter-Daten über Börsentrends bis zu Netzwerk-Logs reichen. <br>
Bei der Analyse können sowohl die konkreten Werte, als auch der Unterschied zwischen ihnen (Delta) eine Rolle spielen. <br> 
Um Zusammenhänge und mögliche Schlüsse verlässlicher aufdecken, respektive treffen zu können, ist eine kritische Menge an Daten von Nöten. Ein kontinuerlicher Strom an zusammenhängenden Daten wird daher als Voraussetzung angenommen. <span style="color: red">#bullshit</span>

Es lassen sich alleinig aus der Beschreibung von CEP keine Rückschlüsse auf potentielle Nutzer oder Andendungsbereiche ziehen, denn relativ große Mengen an Daten, lassen sich, mindestens durch logs, heutzutage sehr leicht produzieren oder aggregieren. Ausgehend davon ist es theoretisch allen Menschen möglich, ihre Daten durch eine CEP zu schleusen und Schlüsse über ihr System, ihre Prozesse oder Strategien zu ziehen. 

#### Process Execution
Als Process Execution Engine bezeichnet man Software, die darauf abzielt Geschäftsprozesse zu unterstützen und Teile davon gegebenen Falls zu automatisieren.
Um diese Geschäftsprozesse zu modellieren wird BPMN benutzt.
BPMN ist ... (wird auch im Bereich "Problemstellung" erklärt).
Man möchte außerdem Analysen über die Prozesse führen um sie dann eventuell besser zu modellieren und umzustrukturieren.

Process Execution Engines können zum Beispiel benutzt werden, um eine Bestellung in einem Onlineshop oder eine Supportanfrage zu unterstützen und umzusetzen. Tolles Beispiel von Prof. Weidlich: Zalando (TODO: hier nochmal beschreiben).
Für Supportmitarbeiter kann das dann wie ein Ticketsystem aussehen, bei dem Anfragen automatisch verteilt und weitergeleitet werden.

#### EventDriven-BPM
Theoretically this kind of project could be used for all kinds of appications. The only two requirements are somewhat large amounts of data (which any sensor can produce) and a recurring process that can be modeled in BPMN. Seeing the amount of work that is required, it is probably not going to be used by your garden-variety home-automation hobbiest, but it would be possible. 

More realistically businesses will usese this kind of software to further automate their behavior and integrate data driven processes or decisions. Future appilcations might even hold the possibility of Event Driven Process Modeling. 
Zum Beispiel kann bei einer Bestellung bei Zalando auf einen Event Stream für Verkehrsdaten innerhalb des Business Process zugegriffen werden und anhand der Auswertung entschieden werden, an welches Lager die Bestellung weitergeleitet wird.
Umgekehrt können auch die Lieferfahreuge wiederum Events für die CEP Engine produzieren, die dann bessere Einsicht in die Verkehrslage ermöglichen.

### Wieso ist es interessant sich damit zu beschäftigen?
BPM beschäftigt sich mit einzelnen Prozessen eines "Business". CEP schafft es zusammenhänge zwischen vielen (zu vielen für Menschen?) Daten automatisiert herzustellen. Das zusammenspiel der Beiden, ermöglicht ein ganzheitlicheres Bild auf Business abläufe und zusammenhänge zwischen diesen aufzuzeigen. Dies erfordert (noch) selbstverständlich Menschliches eingreifen. 

Insbesondere 

## Problemstellung
### Fragestellung
> Welches Problem löst Ihr in Eurem Projekt? Hier bitte auch die zugeordnete Process-Engine mit einbauen, sprich das Problem für Eure Engine "instanziieren".

Auf einfachster Ebene gesprochen, verbindet die entwickelte Software zwei Anwendungen. Auf der einen Seite eine CEP-Engine, auf der anderen eine BPM-Software. Beides sind Open-Source Projekte. Die CEP-Engine, Unicorn, entwickelt vom Hasso-Plattner-Institut in Potsdam wurde in Java geschrieben und läuft auf einem Apache Tomcat Server. ProcessMaker, entwickelt durch ProcessMaker Inc., ist hauptsächlich in PHP geschrieben. Ein Server für ProcessMaker ist nicht vorgegeben, doch Apache HTTP Server wird empfohlen und in der Dokumentation verwendet. Durch die Server Architektur bringen beide Komponenten REST-APIs mit sich, sodass eine Middleware die naheliegendste Entscheidung war. 

Schon von der Teminologie her bringen sowohl Complex Events als auch BPMN *events* mit. In Unicorn können Queries erstellt werden, die auf eine Abfolge von eingehenden Events reagieren. Ein solches, aus mehreren Granulaten bestehendes, Event nennt man Komplexes Event. Die Daten der einzelnen Events und den Typ und die ID des Komplexen Events, können dann an einen vorbestimmten Ort (z.B. via REST-API) übergeben werden. Events in BPMN repräsentieren Dinge, die sich Ereignen, wie zum Beispiel, das Eingehen einer Bestellung. BPMN Events teilen sich in drei Typen auf: Start, Stopp und Intermediate. Events können dabei jeweils fangend (Catching) oder werfend (Throwing) sein. Darüber hinaus gibt es weitere Klassifizierungen, die aber hier keine weitere Rolle spielen sollen. 

Das Ziel war, die Events beider Anwendungen zu verknüpfen und insbesondere für die BPMN-Seite Schnittstellen für jeden Typen, sowohl Catching als auch Throwing zu haben. Die schlussendliche Funktionalität sollte beinhalten, ein Complexes Event an ProcessMaker zu senden (und dadurch einen Prozess zu starten, zu beenden oder zwischendurch zu beeinflussen) und von ProcessMaker aus ein Event an Unicorn zu senden und es in den Event-Fluss einzugliedern. 

Eines der größeren Probleme im Verlauf des Projekts war, dass die API von ProcessMaker keine Möglichkeit zur Manipulation von Events bereitstellt. Das nächstebeste was BPMN bietet und durch die API von ProcessMaker zu erreichen ist, sind Aktivitäten (Activity). (Diskussion im Abschnitt "Verlauf des Projekts".) Aktivitäten in BPMN stellen zu erledigende Aufgaben dar und sind daher semantisch nicht ganz akurat auf Komplexe Events abzubilden. Aktivitäten sind in ProcessMaker konkreten Nutzern oder Nutzergruppen des Systems zugeordnet und müssen entlang des Prozessablaufs geroutet werden. Sowohl das Abarbeiten als auch das routen sind via der API verfügbar. 

Das neue Ziel war weiterhin Komplexe Events von Unicorn an ProcessMaker und zurück zu senden, in ProcessMaker aber Aktivitäten zu nutzen um das Verhalten von Events nach außen zu simulieren. Eingehende Events lassen sich von der Middleware auffangen, an den Aktivitäten Endpoint pushen und von der Middleware automatisch weiter routen. Werfende Events zu simulieren ist nicht ohne weiteres möglich, nicht zuletzt, weil die API keine Callbacks ermöglicht. Aber eine geroutete Aktivität landet in der Inbox des zuständigen Nutzers und diese ist wiederum per API abzufragen. Somit polled die Middleware die Inbox eines designierten Unicorn-Nutzers und pushed gegebenenfalls ein Event in den Datenfluss von Unicron. 


## Verlauf des Projektes

### Planung
Die Planung zu Anfang war sehr vage. Es gab keine festgelegte Programmiersprache, keine Architektur, kein Klassendiagrammm, .... 

Das macht es schwer von der Planung abzuweichen. Vieles war try-and-error und *Python* war eine schnelle Lösung um auszuprobieren. Als es dann die basis funktionalität in Python gab, wurde das Framework (Django) als neuer untergrund gewählt und das Haus darauf umgezogen. 

Was das Endprodukt können sollte, hatten wir in der ursprünglichen Planung aufgelistet und es zwischen drin, nachdem die Möglichkeiten der ProcessMaker API feststanden, erweitert. 
Ab dann waren es die Endpoints der API die in einer eigenen Wrapper Klasse aufrufbar gemacht wurden und auf komplexere Funktionen erweitert. Von vornerein geplant war der Wrapper als Modell allerdings nicht. 

Das ein Unicorn Wrapper entstand, war ebenfalls nicht teil des initialen Plans, aber ergibt in anbetracht der Tatsache, dass unsere Lösung eine eigenständige Middleware ist, Sinn. 


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

### Prototyp
Dann haben wir erst mal einen Prototyp mit Python gebaut.
### Django Middleware
Und dann die Django Middleware.

### Obstacles
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

### Workflow
* Different OSes (Linux / OS X)
* Differnt editors (Sublime / Atom)
* Same container software (Docker)
* Repo / Versioning: GitHub
* Inner-Team communication: 
	* Mostly Threema
	* Sometimes Mail
	* Meetups - usually before meetings

## Architektur und Scope
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

## Vorführung an einem Beispiel

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