title: التكامل مع JasperServer

type: docs

weight: 30

url: ar/jasperreports/integration-with-jasperserver/

lastmod: "2021-06-05"

---

{{% alert color="primary" %}}

يتم وصف تكامل Aspose.PDF لـ JasperReports مع JasperServer أدناه.

{{% /alert %}}

في الخطوات التالية <InstallDir> تمثل دليل تثبيت JasperServer.

{{% alert color="primary" %}}

1. أضف خصائص المصدّر الجديدة التالية إلى ملف **<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml**.

{{% /alert %}}

```

 <bean id="AsposePdfExporter" class="com.aspose.pdf.jr3_7_0.jasperreports.AsposeServerPdfExporter" parent="baseReportExporter">

   <property name="exportParameters" ref="AsposeExportParameters"/>

   <property name="setResponseContentLength" value="true"/>

</bean>

<bean id="AsposePdfExporterConfiguration" class="com.jaspersoft.jasperserver.war.action.ExporterConfigurationBean">

   <property name="descriptionKey" value="Pdf - PDF عبر Aspose.PDF لـ JasperReports"/>
```

```
<property name="iconSrc" value="/images/pdf.gif"/>

<property name="parameterDialogName" value="dlg"/>

<property name="exportParameters" ref="AsposeExportParameters"/>

<property name="currentExporter" ref="AsposePdfExporter"/>

</bean>
```

{{% alert color="primary" %}}

2. حدد العنصر <util:map id=”exporterConfigMap> في الملف **<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml** وأضف الأسطر التالية:

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


3. انسخ جميع صور GIF من مجلد \lib في **Aspose-pdf-jasperreports.zip** إلى <InstallDir>\apache-tomcat\webapps\jasperserver\images\.

4. انسخ **Aspose-pdf-jasperreports.jar** من المجلد \lib في **Aspose.PDF.JasperReports.zip** إلى <InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\lib\.

5. أضف السطور التالية إلى ملف **<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml**.



   قد يحتوي هذا الكائن على إعدادات تهيئة مختلفة تهدف إلى تهيئة التصدير. على سبيل المثال، يمكنك استخدام ميزة تعيين الخطوط في JasperReports أو تحديد موقع ملف ترخيص Aspose.Cells لـ JasperReports.

  

{{% /alert %}}



<bean id="AsposeExportParameters" class="com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExportParametersBean">

<property name="localizedFontMap" ref="localePdfFontMap"/>



<!-- قم بإلغاء التعليق لتطبيق ترخيص. تحقق من مسار الترخيص.

<property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/


jasperserver/WEB-INF/Aspose.PDF.JasperReports.lic"/>
```


-->

</bean>



{{% alert color="primary" %}}



6. قم بتشغيل JasperServer وافتح أي تقرير لعرضه. إذا تم تنفيذ الخطوات السابقة بشكل صحيح، سترى أيقونة للتصدير عبر Aspose.PDF لـ JasperReports في قائمة التنسيقات المتاحة.



   **تم دمج Aspose.PDF لـ JasperReports**



![todo:image_alt_text](integration-with-jasperserver_1.png)



{{% /alert %}}
```