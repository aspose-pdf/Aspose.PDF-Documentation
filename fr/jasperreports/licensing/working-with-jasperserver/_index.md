---
title: Travailler avec JasperServer
linktitle: Working with JasperServer
type: docs
weight: 20
description: Explore how to efficiently work with JasperServer using Aspose.PDF. Export reports to professional PDFs with ease.
lastmod: "2026-08-31"
---

## <ins>Définissez le paramètre LicenseFile Exporter dans applicationContext.xml

{{% alert color="primary" %}}

Cette méthode est utilisée avec JasperServer.

{{% /alert %}}

1. Téléchargez la licence sur votre ordinateur et copiez-la dans ```<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF``` folder, where  ```<InstallDir>``` représente le répertoire d'installation de JasperServer.
2. Localisez le fichier ```<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml``` et ajoutez les lignes suivantes :

```xml
 <bean id="AsposeExportParameters" class="com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExportParametersBean">
    <property name="licenseFile" value="C:/jasperserver-pro-3.7.1/apache-tomcat/webapps/jasperserver-pro/WEB-INF/Aspose.Total.JasperReports.lic"/>
</bean>
```

{{% alert color="primary" %}}
Note: Please note that installation path should not contain any spaces, for example C:/Program Files/JasperServer… as that causes problems when accessing the license file.
{{% /alert %}}

## Vérifiez que la licence fonctionne

Export any report to PDF format and check if the report contains an evaluation message. If there is no evaluation message, then the license is working properly.

Aspose.PDF for JasperReports injecte un filigrane lorsque vous travaillez en mode évaluation

![Integration with JasperServer_1](working-with-jasperserver_1.png)

Aspose.PDF for JasperReports injects a watermark when working in evaluation mode

![Integration with JasperServer_2](working-with-jasperserver_2.png)

