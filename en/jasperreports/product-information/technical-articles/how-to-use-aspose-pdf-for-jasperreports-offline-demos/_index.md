---
title: How to - use Aspose.Pdf for JasperReports offline demos
type: docs
weight: 10
url: /jasperreports/how-to-use-aspose-pdf-for-jasperreports-offline-demos/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.PDF for JasperReports includes a number of demo projects to help you get started exporting reports to PDF formats from your application. The demos are standard JasperReports demos that have been modified to demonstrate how to use new exporters.

{{% /alert %}}
### **Running Aspose.PDF for JasperReports Demos**
To run Aspose.PDF for JasperReports demos:

{{% alert color="primary" %}}

1. Download JasperReports from <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579>. Make sure to download the entire archived project with the source code and demos, not just a single JAR.
2. Unpack the archived project to some location on your hard disk, for example C:\.
3. Copy all demo folders from the \demo folder in **Aspose.PDF.JasperReports.zip** to ```<InstallDir>```\jasperreports\demo\samples, where ```<InstallDir>``` is the location you have unpacked JasperReports to. This step is required because the demo build scripts rely on the JasperReports folder structure, otherwise you have to modify build scripts.
4. Copy the **aspose.pdf.jasperreports.jar** file from the \lib folder in **Aspose.PDF.JasperReports.zip** to ```<InstallDir>```\jasperreports\lib.
5. Download the ANT tool from <http://ant.apache.org/bindownload.cgi>.
6. Unpack the ANT tool and set up environment variables as described in the tool's manual.
7. Change the current directory to ```<InstallDir>```\demo\hsqldb and run the following command line:
   ant runServer
8. Open new command prompt instance and change the current directory to one of the Aspose.PDF for JasperReports demos, for example ```<InstallDir>```\demo\samples\charts.ap.
9. Run the following commands on the command line:
10. ant javac – to compile the Java source files of the test application.
11. ant compile – to compile the XML report design and produce the .jasper file
12. ant fill – to fill the compiled report design with data and produce the .jrprint file
13. Run the following command on the command line:
   ant pdf – to produce a PDF file from the demo report.
14. Open one of the resulting documents to view, for example ```<InstallDir>```\demo\samples\charts.ap\AreaChartReport.pdf in Adobe Reader or another application.

{{% /alert %}}
