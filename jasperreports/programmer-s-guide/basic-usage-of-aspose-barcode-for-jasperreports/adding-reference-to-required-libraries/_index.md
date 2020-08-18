---
title: Adding Reference to Required Libraries
type: docs
weight: 10
url: /jasperreports/adding-reference-to-required-libraries/
---

To successfully compile the Java files for rendering barcodes in JasperReports, you need to include the following required .jar files (libraries).

- <JasperReports_Install_Folder>/lib – required .jar files
- <JasperReports_Install_Folder>/dist/jasperreports-3.5.2.jar (file name may differ according to the version installed on your machine)
- <Aspose.BarCode for JasperReports Installation Folder>/Aspose.BarCode.JasperReports.jar

You also need to copy the following two files in the output folder (build/classes) for successful compilation of the java program, which requires Aspose.BarCode for Jasper Reports:

- <Aspose.BarCode for JasperReports Installation Folder>/asposebarcode_beans.xml
- <Aspose.BarCode for JasperReports Installation Folder>/jasperreports_extension.properties

{{% alert color="primary" %}} 

If you are using an IDE, for example Netbeans or Eclipse, you need to modify the project settings to include the JARs listed above. If you are using the javac command for compilation, set the --sourcepath to include the required libraries.

{{% /alert %}} 

If you have any problems with Aspose.BarCode for Jasper Reports, post on the [support forums](http://www.aspose.com/community/forums/aspose.barcode-for-.net-java-and-reporting-services/193/showforum.aspx) and our dedicated support team will help you. 
