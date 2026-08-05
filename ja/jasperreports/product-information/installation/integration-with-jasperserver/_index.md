---
title: JasperServer との統合
linktitle: Integration with JasperServer
type: docs
weight: 30
url: /ja/jasperreports/integration-with-jasperserver/
description: Aspose.PDF を JasperServer と統合する方法を学びます。サーバー レポートを高品質の PDF 形式で簡単にエクスポートします。
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.PDF for JasperReports と JasperServer の統合については、以下で説明します。

{{% /alert %}}

次の手順の <InstallDir> は、JasperServer インストール ディレクトリを表します。

{{% alert color="primary" %}}

1. 次の新しいエクスポータ プロパティを

**<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml** ファイル。

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

2. <util:map id=”exporterConfigMap> 要素を見つけます。

**<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml** ファイルに次の行を追加します。

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

3. **Aspose-pdf-jasperreports.zip** の \lib フォルダーからすべての GIF 画像を <InstallDir>\apache-tomcat\webapps\jasperserver\images\ にコピーします。
4. **Aspose-pdf-jasperreports.jar** を **Aspose.PDF.JasperReports.zip** の \lib フォルダーから <InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\lib\ にコピーします。
5. **<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml** ファイルに次の行を追加します。

   この Bean には、エクスポートを構成するためのさまざまな構成設定が含まれる場合があります。たとえば、JasperReports フォント マッピング機能を使用したり、Aspose.Cells for JasperReports ライセンス ファイルの場所を指定したりできます。
  
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

6. JasperServer を実行し、表示するレポートを開いてください。前の手順が適切に実行された場合は、使用可能な形式のリストに、JasperReports 用の Aspose.PDF 経由でエクスポートするためのアイコンが表示されます。

   **JasperReports 用の Aspose.PDF が統合されました**

![Integration with JasperServer](integration-with-jasperserver_1.png)

{{% /alert %}}

