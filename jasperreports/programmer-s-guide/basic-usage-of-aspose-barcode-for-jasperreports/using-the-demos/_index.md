---
title: Using the Demos
type: docs
weight: 60
url: /jasperreports/using-the-demos/
---

{{% alert color="primary" %}} 

Aspose.BarCode for JasperReports includes a few demos to help you get started rendering barcodes in JasperReports.

{{% /alert %}} 
### **How to Use Demos**
To build and run Aspose.BarCode for JasperReports demos, perform the following steps: 

1. Download JasperReports from <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579>. Make sure to download the entire archived project with the source code and demos, not just a single JAR.
1. Unpack the archived project to a location on your hard disk, for example C:\.
1. Copy all demo folders from the **\demo** folder of the **aspose.barcode.jasperreports.zip** file to **<InstallDir>\jasperreports\demo\samples**, where <InstallDir> is the location you have unpacked JasperReports to. This step is required because the demo build scripts rely on JasperReports’ folder structure; otherwise you need to modify the build scripts.
1. Copy **aspose.barcode.jasperreports.jar** from the **\lib** folder of the **aspose.barcode.jasperreports.zip** file to **<InstallDir>\jasperreports\lib**.
1. Download the ANT tool from <http://ant.apache.org/bindownload.cgi>.
1. Unpack the ANT tool and set up environment variables as described in the tool’s manual.
1. Change the current directory to one of the Aspose.BarCode for JasperReports demos, for example **<InstallDir>\demo\samples\bc.SimpleReport** and run the following commands in the command line: 
   1. ant build – to compile the Java source files and produce the .jasper file.
   1. ant run –- export the report in PDF format.
1. Open one of the resulting PDF documents to view it in Adobe Pdf viewer or other software.
