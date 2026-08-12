---
title: التكامل مع جاسبرسيرفر
linktitle: التكامل مع جاسبرسيرفر
type: docs
weight: 30
url: /ar/jasperreports/integration-with-jasperserver/
description: تعرف على كيفية دمج Aspose.PDF مع JasperServer. قم بتصدير تقارير الخادم بسهولة إلى تنسيقات PDF عالية الجودة.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

يتم وصف دمج Aspose.PDF for JasperReports مع JasperServer أدناه.

{{% /alert %}}

في الخطوات التالية <InstallDir> يرمز إلى دليل تثبيت JasperServer.

{{% alert color="primary" %}}

1. Add the following new exporter properties to the

**<InstallDir>\Apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml** ملف.

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

2. حدد موقع العنصر <util:map id=”exporterConfigMap> في ملف

**<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml** file and add the following lines:

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

3. انسخ جميع صور GIF من المجلد \lib الخاص بـ **Aspose-pdf-jasperreports.zip** إلى <InstallDir>\Apache-tomcat\webapps\jasperserver\images\.
4. انسخ **Aspose-pdf-jasperreports.jar** من المجلد \lib في **Aspose.PDF.JasperReports.zip** إلى <InstallDir>\Apache-tomcat\webapps\jasperserver\WEB-INF\lib\.
5. أضف الأسطر التالية إلى الملف **<InstallDir>\Apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml**.

   قد تحتوي هذه الحبة على إعدادات تكوين مختلفة مخصصة لتكوين التصدير. على سبيل المثال، يمكنك استخدام ميزة تعيين الخطوط JasperReports أو تحديد موقع ملف ترخيص Aspose.Cells for JasperReports.
  
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

6. قم بتشغيل JasperServer وافتح أي تقرير لعرضه. إذا تم تنفيذ الخطوات السابقة بشكل صحيح، فسترى أيقونة للتصدير عبر Aspose.PDF for JasperReports في قائمة التنسيقات المتاحة.

   **تم دمج Aspose.PDF for JasperReports**

![Integration with JasperServer](integration-with-jasperserver_1.png)

{{% /alert %}}


