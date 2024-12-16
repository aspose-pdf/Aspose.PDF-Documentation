title: JasperServerとの統合

type: docs

weight: 30

url: /ja/jasperreports/integration-with-jasperserver/

lastmod: "2021-06-05"

---

{{% alert color="primary" %}}

Aspose.PDF for JasperReportsとJasperServerの統合について以下に説明します。

{{% /alert %}}

以下のステップで <InstallDir> はJasperServerのインストールディレクトリを表します。

{{% alert color="primary" %}}

1. 以下の新しいエクスポーターのプロパティを **<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml** ファイルに追加します。

{{% /alert %}}

```

<bean id="AsposePdfExporter" class="com.aspose.pdf.jr3_7_0.jasperreports.AsposeServerPdfExporter" parent="baseReportExporter">

   <property name="exportParameters" ref="AsposeExportParameters"/>

   <property name="setResponseContentLength" value="true"/>

</bean>

<bean id="AsposePdfExporterConfiguration" class="com.jaspersoft.jasperserver.war.action.ExporterConfigurationBean">

   <property name="descriptionKey" value="Pdf - PDF via Aspose.PDF for JasperReports"/>
```

```
<property name="iconSrc" value="/images/pdf.gif"/>

<property name="parameterDialogName" value="dlg"/>

<property name="exportParameters" ref="AsposeExportParameters"/>

<property name="currentExporter" ref="AsposePdfExporter"/>

</bean>
```

{{% alert color="primary" %}}

2. **<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml** ファイル内の <util:map id=”exporterConfigMap> 要素を見つけて、次の行を追加してください:

{{% /alert %}}

```
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

3. **Aspose-pdf-jasperreports.zip** の \lib フォルダからすべての GIF 画像を <InstallDir>\apache-tomcat\webapps\jasperserver\images\ にコピーします。

4. **Aspose.PDF.JasperReports.zip** の \lib フォルダから **Aspose-pdf-jasperreports.jar** を <InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\lib\ にコピーします。

5. 次の行を **<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml** ファイルに追加します。



   このビーンには、エクスポートを構成するためのさまざまな設定が含まれている場合があります。例えば、JasperReports のフォントマッピング機能を使用したり、Aspose.Cells for JasperReports ライセンスファイルの場所を指定したりできます。

  

{{% /alert %}}



```

<bean id="AsposeExportParameters" class="com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExportParametersBean">

<property name="localizedFontMap" ref="localePdfFontMap"/>



<!-- ライセンスを適用するにはコメントを外します。ライセンスパスを確認してください。

<property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/


jasperserver/WEB-INF/Aspose.PDF.JasperReports.lic"/>

```
</bean>
```

{{% alert color="primary" %}}

6. JasperServerを実行し、任意のレポートを開いて表示します。前のステップが正しく実行された場合、使用可能な形式のリストにAspose.PDF for JasperReportsによるエクスポート用のアイコンが表示されます。

   **Aspose.PDF for JasperReportsが統合されています**

![todo:image_alt_text](integration-with-jasperserver_1.png)

{{% /alert %}}