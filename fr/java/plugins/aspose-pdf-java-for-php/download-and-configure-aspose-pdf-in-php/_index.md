---
title: Téléchargez et configurez Aspose.PDF en PHP
linktitle: Téléchargez et configurez Aspose.PDF en PHP
type: docs
weight: 10
url: /java/download-and-configure-aspose-pdf-in-php/
description: Découvrez comment télécharger et configurer Aspose.PDF en PHP pour une intégration et une manipulation PDF faciles dans vos projets PHP.
lastmod: "2026-06-09"
---
## 
Télécharger les bibliothèques requises



Téléchargez les bibliothèques requises mentionnées ci-dessous. Ce sont les éléments requis pour l’exécution des exemples Aspose.PDF Java pour PHP.

- **Aspose :** [Aspose.PDF pour le composant Java] (https://downloads.aspose.com/pdf/java)

- 
Pont PHP/Java


## 
Téléchargez des exemples à partir de sites de codage social



Les versions suivantes d'exemples en cours d'exécution sont disponibles en téléchargement sur les sites de codage social mentionnés ci-dessous :


### 
GitHub

- **Aspose.PDF Java pour exemples PHP**

  - 
[Aspose.PDF Java pour PHP] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)


## 
Comment configurer le code source sur la plateforme Linux



Veuillez suivre ces étapes simples afin d'ouvrir et d'étendre le code source tout en utilisant :


## 
1. Installez le serveur Tomcat

Pour installer le serveur Tomcat, exécutez la commande suivante sur la console Linux. Cela installera avec succès le serveur Tomcat.


{{< highlight actionscript3 >}}

 
sudo apt-get install tomcat8


{{< /highlight >}}

## 
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


En copiant, Tomcat8 créera automatiquement un nouveau dossier "**JavaBridge**" dans**webapps**. Une fois le dossier créé, assurez-vous que votre Tomcat8 est en cours d'exécution, puis cochez http://localhost:8080/JavaBridge dans le navigateur, il devrait ouvrir une page par défaut de JavaBridge.

Si un message d'erreur apparaît, installez **FastCGI**В en exécutant la commande suivante sur la console Linux.


{{< highlight actionscript3 >}}

  
sudo apt-get install php55-cgi


{{< /highlight >}}


Après avoir installé php5.5 CGI, redémarrez le serveur Tomcat8 et cochez à nouveau http://localhost:8080/JavaBridge Â dans le navigateur.



Si une erreur **JAVA_HOME**В s'affiche, ouvrez le fichier /etc/default/tomcat8 et décommentez la ligne qui définit JAVA_HOME. Cochez à nouveau http://localhost:8080/JavaBridge В dans le navigateur, il devrait contenir la page d'exemples PHP/JavaBridge.


## 
3. Configurez Aspose.PDF Java pour les exemples PHP

Clonez des exemples PHP en exécutant les commandes suivantes dans le dossier webapps/JavaBridge.


{{< highlight actionscript3 >}}


$ git init&nbsp;



$ git clone [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]


{{< /highlight >}}

## 
Comment configurer le code source sous Windows



Veuillez suivre les étapes simples ci-dessous pour configurer PHP/Java Bridge sur la plate-forme Windows

1. Installez PHP5 et configurez comme vous le faites habituellement

2. 
Installez JRE 6 (Java Runtime Environment) si vous ne l'avez pas déjà. Vous pouvez le vérifier dans C:\Program Fichiers etc. Vous pouvez le télécharger ici . J'utilise JRE 6 car il est compatible avec PHP Java Bridge (PJB).


3. 
Installez Apache Tomcat 8.0. Vous pouvez le télécharger ici


4. 
Téléchargez JavaBridge.war.

5. 
Copiez ce fichier dans le répertoire Tomcat Webapps.
(ex : C:\Program Fichiers\Apache Software Foundation\Tomcat 8.0\webapps )


6. 
Redémarrez le service Apache de Tomcat.


7. 
Accédez à http://localhost:8080/JavaBridge/test.php pour vérifier si php fonctionne. Vous pouvez y trouver d'autres exemples


8. 
Copiez votre fichier jar [Aspose.PDF Java] (https://downloads.aspose.com/pdf/java) dans C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib


9. 
Clonez des exemples [Aspose.PDF Java pour PHP] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) dans le dossier C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\.

10. Copiez le dossier C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java dans votre dossier d'exemples Aspose.PDF Java pour PHP.


11. 
Redémarrez le service Apache Tomcat et commencez à utiliser des exemples.
