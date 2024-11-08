---
title: Télécharger et Configurer Aspose.PDF en PHP
type: docs
weight: 10
url: /fr/java/download-and-configure-aspose-pdf-in-php/
lastmod: "2021-06-05"
---

## Télécharger les Bibliothèques Nécessaires

Téléchargez les bibliothèques nécessaires mentionnées ci-dessous. Elles sont requises pour exécuter les exemples d'Aspose.PDF Java pour PHP.

- **Aspose :** [Composant Aspose.PDF pour Java](https://downloads.aspose.com/pdf/java)
- PHP/Java Bridge

## Télécharger des Exemples depuis des Sites de Codage Social

Les versions suivantes d'exemples en cours d'exécution sont disponibles pour téléchargement sur les sites de codage social mentionnés ci-dessous :

### GitHub

- **Exemples Aspose.PDF Java pour PHP**
  - [Aspose.PDF Java pour PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)

## Comment configurer le code source sur la Plateforme Linux

Veuillez suivre ces étapes simples afin d'ouvrir et d'étendre le code source tout en utilisant :

## 1. Installer le Serveur Tomcat

Pour installer le serveur Tomcat, exécutez la commande suivante sur la console Linux. Cela installera avec succès le serveur Tomcat.

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}

## 2. Télécharger et configurer PHP/JavaBridge

Afin de télécharger les binaires de PHP/JavaBridge, exécutez la commande suivante sur la console Linux.

{{< highlight actionscript3 >}}

  wget http://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}


Décompressez les binaires de PHP/JavaBridge en exécutant la commande suivante sur la console Linux.

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}


Cela extraira le fichier **JavaBridge.war**. Copiez-le dans le dossier **webapps** de tomcat88 en exécutant la commande suivante sur la console Linux.

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war

{{< /highlight >}}


En copiant, tomcat8 créera automatiquement un nouveau dossier "**JavaBridge**" dans **webapps**.
 Une fois le dossier créé, assurez-vous que votre tomcat8 est en cours d'exécution, puis vérifiez http://localhost:8080/JavaBridge dans le navigateur, cela devrait ouvrir une page par défaut de JavaBridge.

Si un message d'erreur apparaît, installez **FastCGI** en exécutant la commande suivante dans la console Linux.

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi

{{< /highlight >}}

Après avoir installé php5.5 CGI, redémarrez le serveur tomcat8 et vérifiez à nouveau http://localhost:8080/JavaBridge dans le navigateur.

Si l'erreur **JAVA_HOME** s'affiche, ouvrez le fichier /etc/default/tomcat8 et décommentez la ligne qui définit le JAVA_HOME. Vérifiez à nouveau http://localhost:8080/JavaBridge dans le navigateur, cela devrait afficher la page des exemples PHP/JavaBridge.

## 3. Configurer Aspose.PDF Java pour les exemples PHP

Clonez les exemples PHP en exécutant les commandes suivantes à l'intérieur du dossier webapps/JavaBridge.

{{< highlight actionscript3 >}}

$ git init&nbsp;

$ git clone [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]
{{< /highlight >}}

## Comment configurer le code source sur Windows

Veuillez suivre les étapes simples ci-dessous pour configurer PHP/Java Bridge sur la plateforme Windows

1. Installez PHP5 et configurez-le comme vous le faites normalement.
2. Installez JRE 6 (Java Runtime Environment) si vous ne l'avez pas déjà. Vous pouvez vérifier cela dans C:\Program Files, etc. Vous pouvez le télécharger ici. J'utilise JRE 6 car il est compatible avec PHP Java Bridge (PJB).

3. Installez Apache Tomcat 8.0. Vous pouvez le télécharger ici.

4. Téléchargez JavaBridge.war.
5. Copiez ce fichier dans le répertoire webapps de tomcat.
(ex : C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps)

6. Redémarrez le service apache tomcat.

7. Allez à http://localhost:8080/JavaBridge/test.php pour vérifier si PHP fonctionne. Vous pouvez y trouver d'autres exemples.

8. Copiez votre fichier jar [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) dans C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib

9. Clonez les exemples [Aspose.PDF Java pour PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) dans le dossier C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\.

10. Copiez le dossier C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java dans votre dossier d'exemples Aspose.PDF Java pour PHP.

11. Redémarrez le service apache tomcat et commencez à utiliser les exemples.