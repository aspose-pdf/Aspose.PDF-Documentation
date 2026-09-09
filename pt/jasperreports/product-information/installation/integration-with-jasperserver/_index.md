---
title: Integração com JasperServer
linktitle: Integração com JasperServer
type: docs
weight: 30
url: /pt/jasperreports/integration-with-jasperserver/
description: Aprenda como integrar Aspose.PDF com JasperServer. Exporte facilmente relatórios do servidor para formatos PDF de alta qualidade.
lastmod: "2026-09-09"
---

{{% alert color="primary" %}}

A integração do Aspose.PDF for JasperReports com JasperServer é descrita abaixo.

{{% /alert %}}

Nas etapas seguintes <InstallDir> significa o diretório de instalação do JasperServer.

{{% alert color="primary" %}}

1. Adicione as seguintes novas propriedades do exportador ao

**<InstallDir>arquivo \apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml**

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

2. Localizar o <util:map id=”exporterConfigMap> elemento no 

**<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml** arquivo e adicione as linhas a seguir:

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

3. Copie todas as imagens GIF da pasta \lib do **Aspose-pdf-jasperreports.zip** para <InstallDir>\apache-tomcat\webapps\jasperserver\images\.
4. Copie **Aspose-pdf-jasperreports.jar** da pasta \lib no **Aspose.PDF.JasperReports.zip** para <InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\lib\.
5. Adicione as linhas a seguir ao **<InstallDir>\\apache-tomcat\\webapps\\jasperserver\\WEB-INF\\applicationContext.xml** arquivo.

Este bean pode conter várias configurações destinadas a configurar a exportação. Por exemplo, você pode usar o recurso de mapeamento de fontes do JasperReports ou especificar a localização do arquivo de licença do Aspose.Cells for JasperReports.
  
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

6. Execute o JasperServer e abra qualquer relatório para visualizar. Se as etapas anteriores foram realizadas corretamente, você verá um ícone para exportação via Aspose.PDF for JasperReports na lista de formatos disponíveis.

   **Aspose.PDF for JasperReports está integrado**

![Integração com JasperServer](integration-with-jasperserver_1.png)

{{% /alert %}}
