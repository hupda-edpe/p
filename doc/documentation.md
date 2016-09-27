# Event Driven Process Engine

## Inhalt

[toc]

| | ![Unicorn Logo](img/unicorn.png) | EDPE | ![ProcessMaker Logo](img/pm.png) |
| :--- | --- | --- | --- |
| Engine | Esper | Django | Zend |
| Language | Java | Python | PHP |
| LOC | N.a.N. | ~500 | > 10000 |

## Kontext und Motivation
### Posed Questions
> * In welchen Bereich ordnet sich das Projekt ein? (Where?)
> * Wer sind potenzielle Nutzer? (Who?)
> * Wieso ist es überhaupt interessant sich damit zu beschäftigen? (Why?)

### Welche Bereiche sind betroffen?
#### CEP
CEP means taking a stream of data, called events, analyzing it and looking for patterns - the complex events. Obviously, hat requires a certain minimum amount of data. 

The kind of data is neither specified nor limited. It can range from weather data, to service calls, text messages, stock market, traffic, and so on. An event can also be a delta, meaning a change in value. 

Therefore there is not really any conclusion as to who might be using complex event processing besides the fact that they need to produce rather large amounts of data. Which isn't really a problem when you consider that everyone can produce huge amounts of log data. From that basis everyone can start drawing conclusions as to how to tune, improve or alter their system(s), workflows or strategy.

Analysis however can be done without having complex event *processing*. The need for some sort of real time analysis requires the processing of the stream while it happens as oppesed to after the fact. 

CEP allows for multiple sources of data. 

#### BPM
Management of Business Processes. Aims at improving processes. (Because reasons.) That's why Wikipedia says it's a "process optimization process".

#### EventDriven-BPM
Theoretically this kind of project could be used for all kinds of appications. The only two requirements are somewhat large amounts of data (which any sensor can produce) and a recurring process that can be modeled in BPMN. Seeing the amount of work that is required, it is probably not going to be used by your garden-variety home-automation hobbiest, but it would be possible. 

More realistically businesses will usese this kind of software to further automate their behavior and integrate data driven processes or decisions. Future appilcations might even hold the possibility of Event Driven Process Modeling. 

### Wieso ist es interessant sich damit zu beschäftigen?
BPM beschäftigt sich mit einzelnen Prozessen eines "Business". CEP schafft es zusammenhänge zwischen vielen (zu vielen für Menschen?) Daten automatisiert herzustellen. Das zusammenspiel der Beiden, ermöglicht ein ganzheitlicheres Bild auf Business abläufe und zusammenhänge zwischen diesen aufzuzeigen. Dies erfordert (noch) selbstverständlich Menschliches eingreifen. 

Insbesondere 

## Problemstellung
### Posed Questions
> Welches Problem löst Ihr in Eurem Projekt? Hier bitte auch die zugeordnete Process-Engine mit einbauen, sprich das Problem für Eure Engine "instanziieren".

* Wir verbinden zwei Softwares miteinander.
* Wir verbinden sie via REST APIs
* 


### Aufgabenstellung
*Aus den Intro-Slides*

> Primary goal: Extend an existing execution engine for BPMN models
> 
> * Import of extended process models from the process repository
> * Sending produced events to a CEP engine
> * Receiving and reacting on events matched by a CEP engine


## Verlauf des Projektes
### Posed Questions
> * Plan vs. Wirklichkeit
> * Sackgassen
> * untersuchte Lösungsansätze

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