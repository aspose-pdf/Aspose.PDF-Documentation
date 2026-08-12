---
title: Integración con JasperServer
linktitle: Integración con JasperServer
type: docs
weight: 30
url: /es/jasperreports/integration-with-jasperserver/
description: Aprenda cómo integrar Aspose.PDF con JasperServer. Exporte fácilmente informes del servidor a formatos PDF de alta calidad.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

A continuación se describe la integración de Aspose.PDF for JasperReportscon JasperServer.

{{% /alert %}}

En los siguientes pasos <InstallDir> representa el directorio de instalación de JasperServer.

{{% alert color="primary" %}}

1. Agregue las siguientes nuevas propiedades de exportador al

**<InstallDir>Archivo \apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml**.

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

2. Localice el <util:map id=”exporterConfigMap> elemento en el 

**<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml** y agregue las siguientes líneas:

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

3. Copie todas las imágenes GIF de la carpeta \lib de **Aspose-pdf-jasperreports.zip** a <InstallDir>\apache-tomcat\webapps\jasperserver\images\.
4. Copie **Aspose-pdf-jasperreports.jar** de la carpeta \lib en **Aspose.PDF.JasperReports.zip** a <InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\lib\.
5. Agregue las siguientes líneas al **<InstallDir>Archivo \apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml**.

   Este bean puede contener varios ajustes de configuración destinados a configurar la exportación. Por ejemplo, puede utilizar la función de asignación de fuentes de JasperReports o especificar la ubicación del archivo de licencia Aspose.Cells para JasperReports.
  
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

6. Ejecute JasperServer y abra cualquier informe para verlo. Si los pasos anteriores se realizaron correctamente, verá un ícono para exportar a través de Aspose.PDF for JasperReportsen la lista de formatos disponibles.

   **Aspose.PDF for JasperReportsestá integrado**

![Integración con JasperServer](integration-with-jasperserver_1.png)

{{% /alert %}}



