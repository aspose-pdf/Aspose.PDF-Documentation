---
title: العمل مع جاسبرسيرفر
linktitle: العمل مع جاسبرسيرفر
type: docs
weight: 20
description: اكتشف كيفية العمل بكفاءة مع JasperServer باستخدام Aspose.PDF. تصدير التقارير إلى ملفات PDF احترافية بسهولة.
lastmod: "2026-08-31"
---

## <ins>قم بتعيين معلمة مُصدِّر ملف الترخيص في applicationContext.xml</ins>

{{% alert color="primary" %}}

يتم استخدام هذه الطريقة مع JasperServer.

{{% /alert %}}

1. قم بتنزيل الترخيص على جهاز الكمبيوتر الخاص بك وانسخه إلى ```<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF``` folder, where  ```<InstallDir>``` وهو اختصار لدليل تثبيت JasperServer.
2. حدد موقع الملف ```<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml``` وأضف الأسطر التالية:

```xml
 <bean id="AsposeExportParameters" class="comcom.aspose.pdf.jr3_7_0.jasperreports.JrPdfExportParametersBean">
    <property name="licenseFile" value="C:/jasperserver-pro-3.7.1/apache-tomcat/webapps/jasperserver-pro/WEB-  
    INF/Aspose.Total.JasperReports.lic"/>
</bean>
```

{{% alert color="primary" %}}
ملاحظة: يرجى ملاحظة أن مسار التثبيت يجب ألا يحتوي على أي مسافات، على سبيل المثال C:/Program Files/JasperServer... لأن ذلك يسبب مشاكل عند الوصول إلى ملف الترخيص.
{{% /alert %}}

## التحقق من أن الترخيص يعمل

قم بتصدير أي تقرير إلى تنسيق PDF وتحقق مما إذا كان التقرير يحتوي على رسالة تقييم. إذا لم تكن هناك رسالة تقييم، فهذا يعني أن الترخيص يعمل بشكل صحيح.

يقوم Aspose.PDF for JasperReports بإدخال علامة مائية عند العمل في وضع التقييم

![Integration with JasperServer_1](working-with-jasperserver_1.png)

يقوم Aspose.PDF for JasperReports بإدخال علامة مائية عند العمل في وضع التقييم

![Integration with JasperServer_2](working-with-jasperserver_2.png)


