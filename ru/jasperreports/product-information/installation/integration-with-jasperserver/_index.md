---

title: Интеграция с JasperServer

type: docs

weight: 30

url: ru/jasperreports/integration-with-jasperserver/

lastmod: "2021-06-05"

---

{{% alert color="primary" %}}

Интеграция Aspose.PDF для JasperReports с JasperServer описана ниже.

{{% /alert %}}

В следующих шагах <InstallDir> обозначает каталог установки JasperServer.

{{% alert color="primary" %}}

1. Добавьте следующие новые свойства экспортера в файл **<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml**.

{{% /alert %}}

```
<bean id="AsposePdfExporter" class="com.aspose.pdf.jr3_7_0.jasperreports.AsposeServerPdfExporter" parent="baseReportExporter">

   <property name="exportParameters" ref="AsposeExportParameters"/>

   <property name="setResponseContentLength" value="true"/>

</bean>

<bean id="AsposePdfExporterConfiguration" class="com.jaspersoft.jasperserver.war.action.ExporterConfigurationBean">

   <property name="descriptionKey" value="Pdf - PDF через Aspose.PDF для JasperReports"/>
```


<property name="iconSrc" value="/images/pdf.gif"/>

<property name="parameterDialogName" value="dlg"/>

<property name="exportParameters" ref="AsposeExportParameters"/>

<property name="currentExporter" ref="AsposePdfExporter"/>

</bean>
```

{{% alert color="primary" %}}

2. Найдите элемент <util:map id=”exporterConfigMap> в файле **<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml** и добавьте следующие строки:

{{% /alert %}}


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

3. Скопируйте все GIF-изображения из папки \lib **Aspose-pdf-jasperreports.zip** в <InstallDir>\apache-tomcat\webapps\jasperserver\images\.

4. Скопируйте **Aspose-pdf-jasperreports.jar** из папки \lib в **Aspose.PDF.JasperReports.zip** в <InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\lib\.

5. Добавьте следующие строки в файл **<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml**.



   Этот bean может содержать различные настройки конфигурации, предназначенные для настройки экспорта. Например, вы можете использовать функцию сопоставления шрифтов JasperReports или указать местоположение файла лицензии Aspose.Cells для JasperReports.

  

{{% /alert %}}



```

<bean id="AsposeExportParameters" class="com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExportParametersBean">

<property name="localizedFontMap" ref="localePdfFontMap"/>



<!-- Уберите комментарий, чтобы применить лицензию. Проверьте путь к лицензии.

<property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/


jasperserver/WEB-INF/Aspose.PDF.JasperReports.lic"/>

-->

</bean>



```

{{% alert color="primary" %}}



6. Запустите JasperServer и откройте любой отчет для просмотра. Если предыдущие шаги были выполнены правильно, вы увидите значок для экспорта через Aspose.PDF for JasperReports в списке доступных форматов.



   **Aspose.PDF для JasperReports интегрирован**



![todo:image_alt_text](integration-with-jasperserver_1.png)



{{% /alert %}}