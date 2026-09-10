---
title: Aspose.PDF Java pour PHP
linktitle: Aspose.PDF Java pour PHP
type: docs
weight: 50
url: /java/aspose-pdf-java-for-php/
description: Découvrez comment intégrer Aspose.PDF pour Java dans des projets PHP. Débloquez la fonctionnalité PDF avancée pour vos applications Web.
lastmod: "2026-06-09"
---
## 
Introduction à Aspose.PDF Java pour PHP


### 
Pont PHP/Java

Le pont PHP/Java est une implémentation d'un [protocole réseau] de streaming basé sur XML (http://php-java-bridge.sourceforge.net/pjb/PROTOCOL.TXT), qui peut être utilisé pour connecter un moteur de script natif, par exemple PHP, Scheme ou Python, avec une machine virtuelle Java. Il est jusqu'à 50 fois plus rapide que le RPC local via SOAP et nécessite moins de ressources côté serveur Web. Il est [plus rapide] (http://php-java-bridge.sourceforge.net/pjb/FAQ.html#performance) et plus fiable que la communication directe via l'interface native Java, et il ne nécessite aucun composant supplémentaire pour appeler des procédures Java à partir de PHP ou des procédures PHP à partir de Java.



En savoir plus sur [sourceforge.net] (http://php-java-bridge.sourceforge.net/pjb/)


### 
Aspose.PDF pour Java



Aspose.PDF pour Java est un composant de création de documents PDF qui permet à vos applications Java de lire, écrire et manipuler des documents PDF sans utiliser Adobe Acrobat.



Aspose.PDF pour Java est un composant à prix abordable qui offre une incroyable richesse de fonctionnalités, notamment : des options de compression PDF, la création et la manipulation de tableaux, la prise en charge de graphiques, des fonctions d'image, une fonctionnalité étendue de liens hypertexte, des contrôles de sécurité étendus et une gestion des polices personnalisées.

Aspose.PDF pour Java vous permet de créer des fichiers PDF directement via les modèles API et XML fournis. L'utilisation d'Aspose.PDF pour Java vous permettra également d'ajouter des fonctionnalités PDF à vos applications en un rien de temps.


### 
Aspose.PDF Java pour PHP



Le projet Aspose.PDF pour PHP montre comment différentes tâches peuvent être effectuées à l'aide des API Java Aspose.PDF en PHP. Ce projet vise à fournir des exemples utiles aux développeurs PHP qui souhaitent utiliser Aspose.PDF pour Java dans leurs projets PHP en utilisant [PHP/Java Bridge] (http://php-java-bridge.sourceforge.net/pjb/).


## 
Configuration système requise et plates-formes prises en charge


### 
Configuration système requise

Voici la configuration système requise pour utiliser Aspose.PDF pour PHP via Java :


- 
Tomcat Server 8.0 ou supérieur installé.

- 
PHP/JavaBridge est configuré.

- 
FastCGI est installé.

- 
Composant Aspose.PDF téléchargé.

### Plateformes prises en charge



Voici les plates-formes prises en charge :


- 
PHP 5.3 ou supérieur

- 
Java 1.8 ou supérieur


## 
Téléchargements et configuration

### Télécharger les bibliothèques requises



Téléchargez les bibliothèques requises mentionnées ci-dessous. Ce sont les éléments requis pour l’exécution des exemples Aspose.PDF Java pour PHP.


- 
**Aspose :** [Aspose.PDF pour le composant Java] (https://downloads.aspose.com/pdf/java)

- 
Pont PHP/Java


### 
Téléchargez des exemples à partir de sites de codage social

Les versions suivantes d'exemples en cours d'exécution sont disponibles en téléchargement sur les sites de codage social mentionnés ci-dessous :


### 
GitHub


- 
Aspose.PDF Java pour exemples PHP

  - 
[Aspose.PDF Java pour PHP] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)


### 
Comment configurer le code source sur la plateforme Linux

Veuillez suivre ces étapes simples afin d'ouvrir et d'étendre le code source tout en utilisant :


### 
1. Installez le serveur Tomcat



Pour installer le serveur Tomcat, exécutez la commande suivante sur la console Linux. Cela installera avec succès le serveur Tomcat.


{{< highlight actionscript3 >}}

 
sudo apt-get install tomcat8


{{< /highlight >}}

### 
2. Téléchargez et configurez PHP/JavaBridge

Afin de télécharger les binaires PHP/JavaBridge, exécutez la commande suivante sur la console Linux.


{{< highlight actionscript3 >}}

  
wget http://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip


{{< /highlight >}}


Décompressez les binaires PHP/JavaBridge en exécutant la commande suivante sur la console Linux.


{{< highlight actionscript3 >}}

  
décompresser -d php-java-bridge_6.2.1_documentation.zip


{{< /highlight >}}


Cela extraira le fichier**JavaBridge.war**Â. Copiez-le dans le dossier tomcat88В **webapps**В en exécutant la commande suivante sur la console Linux.

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war


{{< /highlight >}}


En copiant, Tomcat8 créera automatiquement un nouveau dossier "**JavaBridge**" dans**webapps**.



Si un message d'erreur apparaît, installez **FastCGI**В en exécutant la commande suivante sur la console Linux.


{{< highlight actionscript3 >}}

  
sudo apt-get install php55-cgi


{{< /highlight >}}


Si une erreur **JAVA_HOME**В s'affiche, ouvrez le fichier /etc/default/tomcat8 et décommentez la ligne qui définit JAVA_HOME.

### 3. Configurez Aspose.PDF Java pour les exemples PHP



Clonez des exemples PHP en exécutant les commandes suivantes dans le dossier webapps/JavaBridge.


{{< highlight actionscript3 >}}


$ git init&nbsp;



$ git clone [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]


{{< /highlight >}}

### 
Comment configurer le code source sur la plateforme Windows

Veuillez suivre les étapes simples ci-dessous pour configurer PHP/Java Bridge sur la plate-forme Windows


1. 
Installez PHP5 et configurez comme vous le faites habituellement

2. 
Installez JRE 6 (Java Runtime Environment) si vous ne l'avez pas déjà. Vous pouvez le vérifier dans C:\Program Fichiers etc. Vous pouvez le télécharger ici . J'utilise JRE 6 car il est compatible avec PHP Java Bridge (PJB).


3. 
Installez Apache Tomcat 8.0. Vous pouvez le télécharger ici


4. 
Téléchargez [JavaBridge.war] (https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/JavaBridgeTemplate621.war/download). Copiez ce fichier dans le répertoire Tomcat Webapps.
(ex : C:\Program Fichiers\Apache Software Foundation\Tomcat 8.0\webapps )


5. 
Redémarrez le service Apache de Tomcat.


6. 
Accédez à http://localhost:8080/JavaBridge/test.php pour vérifier si php fonctionne. Vous pouvez y trouver d'autres exemples


7. 
Copiez votre fichier jar [Aspose.PDF Java] (https://downloads.aspose.com/pdf/java) dans C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib


8. 
Clonez des exemples [Aspose.PDF Java pour PHP] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) dans le dossier C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\.

9. Copiez le dossier C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java dans votre dossier d'exemples Aspose.PDF Java pour PHP.


10. 
Redémarrez le service Apache Tomcat et commencez à utiliser des exemples.


## 
Soutenir, étendre et contribuer


### 
Assistance



Dès les premiers jours d’Aspose, nous savions qu’offrir à nos clients de bons produits ne suffirait pas. Nous devions également offrir un bon service. Nous sommes nous-mêmes développeurs et comprenons à quel point il est frustrant lorsqu'un problème technique ou une bizarrerie dans le logiciel vous empêche de faire ce que vous devez faire. Nous sommes là pour résoudre les problèmes, pas pour les créer.

C'est pourquoi nous offrons une assistance gratuite. Quiconque utilise notre produit, qu'il l'ait acheté ou qu'il utilise une évaluation, mérite toute notre attention et notre respect.



Vous pouvez enregistrer tous les problèmes ou suggestions liés à Aspose.Cells Java pour PHP en utilisant l'une des plates-formes suivantes :


- 
[Github] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)


### 
Prolongez et contribuez



Aspose.PDF Java pour PHP est open source et son code source est disponible sur les principaux sites Web de codage social répertoriés ci-dessous. Les développeurs sont encouragés à télécharger le code source et à contribuer en suggérant ou en ajoutant de nouvelles fonctionnalités ou en améliorant celles existantes, afin que d'autres puissent également en bénéficier.

### Code source



Vous pouvez obtenir le dernier code source à partir de l'un des emplacements suivants


- 
[Github] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)
