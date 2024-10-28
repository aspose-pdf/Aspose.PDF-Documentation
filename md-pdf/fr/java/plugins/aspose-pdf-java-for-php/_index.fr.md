---
title: Aspose.PDF Java pour PHP
type: docs
weight: 50
url: /java/aspose-pdf-java-for-php/
lastmod: "2021-06-05"
---

## Introduction à Aspose.PDF Java pour PHP

### PHP / Java Bridge

Le PHP/Java Bridge est une implémentation d'un [protocole réseau](http://php-java-bridge.sourceforge.net/pjb/PROTOCOL.TXT) basé sur XML et streaming, qui peut être utilisé pour connecter un moteur de script natif, par exemple PHP, Scheme ou Python, avec une machine virtuelle Java. Il est jusqu'à 50 fois plus rapide que l'RPC local via SOAP, nécessite moins de ressources côté serveur web. Il est [plus rapide](http://php-java-bridge.sourceforge.net/pjb/FAQ.html#performance) et plus fiable que la communication directe via l'interface native Java, et il ne nécessite aucun composant supplémentaire pour invoquer des procédures Java depuis PHP ou des procédures PHP depuis Java.

Lisez plus sur [sourceforge.net](http://php-java-bridge.sourceforge.net/pjb/)

### Aspose.PDF pour Java

Aspose.PDF pour Java est un composant de création de documents PDF qui permet à vos applications Java de lire, écrire et manipuler des documents PDF sans utiliser Adobe Acrobat.

Aspose.PDF for Java est un composant à prix abordable qui offre une incroyable richesse de fonctionnalités, notamment : des options de compression PDF, la création et la manipulation de tableaux, le support des graphiques, des fonctions d'image, une fonctionnalité de liens hypertextes étendue, des contrôles de sécurité avancés et une gestion personnalisée des polices.

Aspose.PDF for Java vous permet de créer des fichiers PDF directement via l'API fournie et les modèles XML. Utiliser Aspose.PDF for Java vous permettra également d'ajouter des capacités PDF à vos applications en un rien de temps.

### Aspose.PDF Java pour PHP

Le projet Aspose.PDF pour PHP montre comment différentes tâches peuvent être effectuées en utilisant les API Aspose.PDF Java en PHP. Ce projet vise à fournir des exemples utiles pour les développeurs PHP qui souhaitent utiliser Aspose.PDF for Java dans leurs projets PHP en utilisant [PHP/Java Bridge](http://php-java-bridge.sourceforge.net/pjb/).

## Configuration système requise et plateformes prises en charge

### Configuration système requise

Voici les exigences système pour utiliser Aspose.PDF for PHP via Java :

- Serveur Tomcat 8.0 ou supérieur installé.
- PHP/JavaBridge est configuré.
- FastCGI est installé.
- Composant Aspose.PDF téléchargé.

### Plates-formes prises en charge

Les plates-formes suivantes sont prises en charge :

- PHP 5.3 ou supérieur
- Java 1.8 ou supérieur

## Téléchargements et Configuration

### Télécharger les Bibliothèques Nécessaires

Téléchargez les bibliothèques nécessaires mentionnées ci-dessous. Celles-ci sont requises pour exécuter des exemples d'Aspose.PDF Java pour PHP.

- **Aspose :** [Composant Aspose.PDF pour Java](https://downloads.aspose.com/pdf/java)
- PHP/Java Bridge

### Télécharger des Exemples depuis les Sites de Codage Social

Les versions suivantes d'exemples en cours d'exécution sont disponibles en téléchargement sur les sites de codage social mentionnés ci-dessous :

### GitHub

- Exemples Aspose.PDF Java pour PHP
  - [Aspose.PDF Java pour PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)

### Comment configurer le code source sur la plate-forme Linux

Veuillez suivre ces étapes simples pour ouvrir et étendre le code source tout en utilisant :

### 1. Installer le Serveur Tomcat

Pour installer le serveur Tomcat, exécutez la commande suivante sur la console Linux. Cela installera avec succès le serveur Tomcat.

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}

### 2. Télécharger et configurer PHP/JavaBridge

Afin de télécharger les binaires de PHP/JavaBridge, exécutez la commande suivante sur la console Linux.

{{< highlight actionscript3 >}}

  wget http://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

Décompressez les binaires de PHP/JavaBridge en exécutant la commande suivante sur la console Linux.

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}


Cela va extraire le fichier **JavaBridge.war**. Copiez-le dans le dossier **webapps** de tomcat88 en exécutant la commande suivante sur la console Linux.

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war

{{< /highlight >}}

En copiant, tomcat8 créera automatiquement un nouveau dossier "**JavaBridge**" dans **webapps**.


Si un message d'erreur apparaît, installez **FastCGI** en exécutant la commande suivante sur la console Linux.

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi

{{< /highlight >}}


Si une erreur **JAVA_HOME** s'affiche, ouvrez alors le fichier /etc/default/tomcat8 et décommentez la ligne qui définit le JAVA_HOME.

### 3. Configurer Aspose.PDF Java pour les exemples PHP

Clonez, les exemples PHP en exécutant les commandes suivantes à l'intérieur du dossier webapps/JavaBridge.

{{< highlight actionscript3 >}}

$ git init&nbsp;

$ git clone [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]

{{< /highlight >}}

### Comment configurer le code source sur la plateforme Windows

Veuillez suivre les étapes simples ci-dessous pour configurer le pont PHP/Java sur la plateforme Windows

1. Installez PHP5 et configurez-le comme vous le faites normalement
2. Installez JRE 6 (Java Runtime Environment) si vous ne l'avez pas déjà. Vous pouvez vérifier cela dans C:\Program Files etc. Vous pouvez le télécharger ici. J'utilise JRE 6 car il est compatible avec PHP Java Bridge (PJB).

3. Installez Apache Tomcat 8.0. Vous pouvez le télécharger ici

4. Téléchargez [JavaBridge.war](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/JavaBridgeTemplate621.war/download). Copiez ce fichier dans le répertoire webapps de tomcat. (ex: C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps )

5. Redémarrez le service apache tomcat.

6. Allez à http://localhost:8080/JavaBridge/test.php pour vérifier si php fonctionne. Vous pouvez y trouver d'autres exemples.

7. Copiez votre fichier jar [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) dans C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib

8. Clonez les exemples [Aspose.PDF Java pour PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) à l'intérieur du dossier C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\.

9. Copiez le dossier C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java dans votre dossier d'exemples Aspose.PDF Java pour PHP.

10. Redémarrez le service apache tomcat et commencez à utiliser les exemples.


## Support, Étendre et Contribuer

### Support

Dès les premiers jours d'Aspose, nous savions que donner à nos clients de bons produits ne suffirait pas. Nous devions également offrir un bon service. Nous sommes nous-mêmes développeurs et comprenons à quel point il est frustrant lorsqu'un problème technique ou une bizarrerie dans le logiciel vous empêche de faire ce que vous devez faire. Nous sommes ici pour résoudre des problèmes, pas pour en créer.

C'est pourquoi nous offrons un support gratuit. Toute personne utilisant notre produit, qu'elle l'ait acheté ou qu'elle utilise une version d'évaluation, mérite toute notre attention et notre respect.

Vous pouvez enregistrer tout problème ou suggestion lié à Aspose.Cells Java pour PHP en utilisant l'une des plateformes suivantes :

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)

### Extend and Contribute

Aspose.PDF Java pour PHP est open source et son code source est disponible sur les principaux sites de codage social listés ci-dessous.
 Les développeurs sont encouragés à télécharger le code source et à contribuer en suggérant ou en ajoutant de nouvelles fonctionnalités ou en améliorant celles existantes, afin que d'autres puissent également en bénéficier.

### Code Source

Vous pouvez obtenir le dernier code source à partir de l'un des emplacements suivants

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)