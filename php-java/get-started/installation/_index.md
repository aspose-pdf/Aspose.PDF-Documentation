---
title: Install Aspose.PDF for PHP via Java
linktitle: Installation
type: docs
weight: 20
url: /php-java/installation/
description: This section shows a product description and instructions for installing Aspose.PDF for PHP via Java on your own, as well as using NuGet.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for PHP via Java is composed of two separate components: the script wrapper (aspose.pdf.php) and Aspose.PDF for Java. These components interact through the PHP/Java Bridge, with each requiring its own environment and execution process.

## Installation

1. Install Tomcat on any location such as \java\apache-tomcat-9.0.24.
1. Copy JavaBridge.war to webapps folder of Tomcat such as \java\apache-tomcat-9.0.24\webapps.
1. Copy aspose-pdf-xx.x.jar to lib folder such as \java\apache-tomcat-9.0.24\lib.
1. Run \bin\startup.bat, JavaBridge.war will be deployed to \java\apache-tomcat-9.0.24\webapps\JavaBridge.
1. Test http://localhost:8080/JavaBridge/test.php to ensure that PHP works fine.
1. Copy aspose.pdf.php and example.php to \java\apache-tomcat-9.0.24\webapps\JavaBridge.
1. Open http://localhost:8080/JavaBridge/example.php or create your own PHP file as follows.
You will find the Jar and PHP library in vendor/aspose/pdf folder.