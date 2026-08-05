---
title: Intégration avec JasperServer
linktitle: Integration with JasperServer
type: docs
weight: 30
url: /fr/jasperreports/integration-with-jasperserver/
description: Découvrez comment intégrer Aspose.PDF à JasperServer. Exportez facilement les rapports du serveur vers des formats PDF de haute qualité.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Integrating Aspose.PDF for JasperReports with JasperServer is described below.

{{% /alert %}}

Dans les étapes suivantes, <InstallDir> représente le répertoire d'installation de JasperServer.

{{% alert color="primary" %}}

1. Add the following new exporter properties to the

**<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml** file.

{{% /alert %}}

```xml
 <bean id="AsposePdfExporter" class="com.aspose.pdf.jr3_7_0.jasperreports.AsposeServerPdfExporter" parent="baseReportExporter">
   <property name="exportParameters" ref="AsposeExportParameters"/>
   <property name="setResponseContentLength" value="true"/>
</bean>

<bean id="AsposePdfExporterConfiguration" class="com.jaspersoft.jasperserver.war.action.ExporterConfigurationBean">
   <property name="descriptionKey" value="Pdf - PDF via Aspose.PDF for JasperReports"/>
   <property name="iconSrc" value="/images/pdf.gif"/>
   <property name="parameterDialogName" value="dlg"/>
   <property name="exportParameters" ref="AsposeExportParameters"/>
   <property name="currentExporter" ref="AsposePdfExporter"/>
</bean>

```

{{% alert color="primary" %}}

2. Localisez l'élément <util:map id=”exporterConfigMap> dans le

**<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml** et ajoutez les lignes suivantes :

{{% /alert %}}

```xml
 <util:map id="exporterConfigMap">

   <entry key="pdf" value-ref="pdfExporterConfiguration"/>
   <entry key="xls" value-ref="xlsExporterConfiguration"/>
   <entry key="rtf" value-ref="rtfExporterConfiguration"/>
   <entry key="csv" value-ref="csvExporterConfiguration"/>
   <entry key="swf" value-ref="swfExporterConfiguration"/>

<!-- START of ADDED LINES -->
   <entry key="Aspose_pdf" value-ref="AsposePdfExporterConfiguration"/>
<!-- END of NEW LINES -->

</util:map>

```
{{% alert color="primary" %}}

3. Copiez toutes les images GIF du dossier \lib de **Aspose-pdf-jasperreports.zip** vers <InstallDir>\apache-tomcat\webapps\jasperserver\images\.
4. Copiez **Aspose-pdf-jasperreports.jar** du dossier \lib dans **Aspose.PDF.JasperReports.zip** vers <InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\lib\.
5. Ajoutez les lignes suivantes au fichier **<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml**.

   Ce bean peut contenir divers paramètres de configuration destinés à configurer l'export. Par exemple, vous pouvez utiliser la fonctionnalité de mappage de polices JasperReports ou spécifier l'emplacement du fichier de licence Aspose.Cells pour JasperReports.
  
{{% /alert %}}

```xml
<bean id="AsposeExportParameters" class="com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExportParametersBean">
<property name="localizedFontMap" ref="localePdfFontMap"/>

<!-- Uncomment to apply a license. Check the license path.
<property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/
jasperserver/WEB-INF/Aspose.PDF.JasperReports.lic"/>
-->
</bean>

```

{{% alert color="primary" %}}

6. Exécutez JasperServer et ouvrez n'importe quel rapport à afficher. Si les étapes précédentes ont été correctement réalisées, vous verrez une icône d'exportation via Aspose.PDF pour JasperReports dans la liste des formats disponibles.

   **Aspose.PDF pour JasperReports est intégré**

![Integration with JasperServer](integration-with-jasperserver_1.png)

{{% /alert %}}

