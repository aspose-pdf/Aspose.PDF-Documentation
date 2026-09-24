---
title: 与 JasperServer 集成
linktitle: 与 JasperServer 集成
type: docs
weight: 30
url: /zh/jasperreports/integration-with-jasperserver/
description: 了解如何将 Aspose.PDF 与 JasperServer 集成。轻松将服务器报告导出为高质量的 PDF 格式。
lastmod: "2026-08-31"
---

{{% alert color="primary" %}}

下面描述了将 Aspose.PDF for JasperReports 与 JasperServer 集成。

{{% /alert %}}

在以下步骤中 <InstallDir> 代表 JasperServer 安装目录。

{{% alert color="primary" %}}

1. 将以下新的导出器属性添加到

**<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml** 文件。

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

2. 找到 <util:map id=”exporterConfigMap> 中的元素 

**<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml** 文件并添加以下行：

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

3. 将 **Aspose-pdf-jasperreports.zip** 的 \lib 文件夹中的所有 GIF 图像复制到 <InstallDir>\apache-tomcat\webapps\jasperserver\images\。
4. 将 **Aspose.PDF.JasperReports.zip** 中的 \lib 文件夹中的 **Aspose-pdf-jasperreports.jar** 复制到 <InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\lib\。
5. 将以下行添加到 **<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml** 文件。

   该 bean 可能包含旨在配置导出的各种配置设置。例如，您可以使用 JasperReports 字体映射功能或指定 Aspose.Cells for JasperReports 许可证文件的位置。
  
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

6. 运行 JasperServer 并打开任何报告进行查看。如果正确执行了前面的步骤，您将在可用格式列表中看到一个用于通过 Aspose.PDF for JasperReports 导出的图标。

   **集成了 JasperReports 的 Aspose.PDF**

![与 JasperServer 集成](integration-with-jasperserver_1.png)

{{% /alert %}}

