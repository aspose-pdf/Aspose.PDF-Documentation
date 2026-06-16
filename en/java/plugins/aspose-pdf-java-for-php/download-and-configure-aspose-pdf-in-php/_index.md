---
title: Download and Configure Aspose.PDF in PHP
linktitle: Download and Configure Aspose.PDF in PHP
type: docs
weight: 10
url: /java/download-and-configure-aspose-pdf-in-php/
description: Learn how to download and configure Aspose.PDF in PHP for easy integration and PDF manipulation within your PHP projects.
lastmod: "2026-06-09"
---
## Download Required Libraries

Download the required libraries mentioned below. These are the required for executing Aspose.PDF Java for PHP examples.

- **Aspose:** [Aspose.PDF for Java Component](https://downloads.aspose.com/pdf/java)
- PHP/Java Bridge

## Download Examples from Social Coding Sites

Following releases of running examples are available to download on below mentioned social coding sites:

### GitHub

- **Aspose.PDF Java for PHP Examples**
  - [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)

## How to configure the source code on Linux Platform

Please follow these simple stepsВ in order to open and extend the source code while using:

## 1. Install Tomcat Server

To install Tomcat server, issue following command on the Linux console.В This will successfully install the Tomcat server.

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}

## 2. Download and Configure PHP/JavaBridge

In order to download the PHP/JavaBridge binaries, issue the following command on the Linux console.

{{< highlight actionscript3 >}}

  wget http://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

Unzip the PHP/JavaBridge binaries by issuing the following command on the Linux console.

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

This will extractВ **JavaBridge.war**В file. Copy it to the tomcat88В **webapps**В folder by issuing the following command on the Linux console.

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war

{{< /highlight >}}

By copying, tomcat8 will automatically create a new folder "**JavaBridge**" inВ **webapps**. Once the folder is created, make sure your tomcat8 is running and then checkВ  http://localhost:8080/JavaBridge В in the browser, it should open a default page of JavaBridge.

If any error message appears then installВ  **FastCGI**В by issuing the following command on Linux console.

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi

{{< /highlight >}}

After installing php5.5 CGI, restart the tomcat8 server and checkВ  http://localhost:8080/JavaBridge В again in the browser.

IfВ **JAVA_HOME**В error is displayed, then open /etc/default/tomcat8 file and uncomment the line that sets the JAVA_HOME. CheckВ http://localhost:8080/JavaBridge В in the browser again, it should come with PHP/JavaBridge Examples page.

## 3. Configure Aspose.PDF Java for PHP Examples

Clone, PHP examples by issuing the following commands inside webapps/JavaBridge folder.

{{< highlight actionscript3 >}}

$ git init&nbsp;

$ git clone [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]

{{< /highlight >}}

## How to configure the source code on Windows

Please follow below simple steps to configure PHP/Java Bridge on Windows Platform

1. Install PHP5 and configure as you normally do
2. Install JRE 6 (Java Runtime Environment) if you donвЂ™t already have it. You can check this in C:\Program Files etc. You can download it here . I am using JRE 6 as It is compatible with PHP Java Bridge (PJB).

3. Install Apache Tomcat 8.0. You can download it here

4. Download JavaBridge.war.
5. Copy this file to tomcat webapps directory.
(ex: C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps )

6. Restart tomcat apache service.

7. Go to  http://localhost:8080/JavaBridge/test.php  to check if php works. You can find other examples in there

8. Copy your [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) jar file to C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib

9. Clone [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) examples inside C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\ folder.

10. Copy folder C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java to your Aspose.PDF Java for PHP examples folder.

11. Restart apache tomcat service and start using examples.
