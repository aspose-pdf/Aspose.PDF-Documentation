---
title: Installer Aspose.PDF pour PHP via Java
linktitle: Installation
type: docs
weight: 20
url: fr/php-java/installation/
description: Cette section montre une description du produit et des instructions pour installer Aspose.PDF pour PHP via Java par vous-même, ainsi qu'en utilisant NuGet.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF pour PHP via Java est composé de deux composants distincts : le wrapper de script (aspose.pdf.php) et Aspose.PDF pour Java. Ces composants interagissent à travers le pont PHP/Java, chacun nécessitant son propre environnement et processus d'exécution.

## Installation

1. Installez Tomcat à n'importe quel emplacement tel que \java\apache-tomcat-9.0.24.
1. Copiez JavaBridge.war dans le dossier webapps de Tomcat tel que \java\apache-tomcat-9.0.24\webapps.
1. Copiez aspose-pdf-xx.x.jar dans le dossier lib tel que \java\apache-tomcat-9.0.24\lib.
1. Exécutez \bin\startup.bat, JavaBridge.war sera déployé dans \java\apache-tomcat-9.0.24\webapps\JavaBridge.

1. Testez http://localhost:8080/JavaBridge/test.php pour vous assurer que PHP fonctionne correctement.
1. Copiez aspose.pdf.php et example.php dans \java\apache-tomcat-9.0.24\webapps\JavaBridge.
1. Ouvrez http://localhost:8080/JavaBridge/example.php ou créez votre propre fichier PHP comme suit.

Vous trouverez la bibliothèque Jar et PHP dans le dossier vendor/aspose/pdf.