---
title: التكامل مع جاسبر ريبورتس
linktitle: التكامل مع جاسبر ريبورتس
type: docs
weight: 20
url: /ar/jasperreports/integration-with-jasperreports/
description: اكتشف كيفية دمج Aspose.PDF مع JasperReports. قم بتصدير التقارير بسلاسة إلى ملفات PDF احترافية مع وظائف محسنة.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

لاستخدام Aspose.PDF لـ JasperReports في التطبيق الخاص بك، انسخ **aspose.pdf.jasperreports.jar** من المجلد \lib في **Aspose.PDF.JasperReports.zip** إلى دليل JasperReports\lib، أو إلى مجلد مكتبة التطبيق الخاص بك. بعد ذلك، يمكنك الوصول إلى المصدرين برمجيا.

{{% /alert %}}

يوضح المثال التالي الكود النموذجي المطلوب لتصدير تقرير إلى تنسيق PDF باستخدام Aspose.PDF لـ JasperReports. يمكن العثور على المزيد من الأمثلة في التقارير التجريبية المضمنة في تنزيل المنتج.

```java
import com.aspose.pdf.jr3_7_0.jasperreports.*;

com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter exporter = new com.aspose.pdf. jr3_7_0.jasperreports.JrPdfExporter();

File sourceFile = new File(fileName);

JasperPrint jasperPrint = (JasperPrint)JRLoader.loadObject(sourceFile);

exporter.setParameter(JRExporterParameter.JASPER_PRINT, jasperPrint);

File destFile = new File(sourceFile.getParent(), jasperPrint.getName() + ".pdf");

exporter.setParameter(JRExporterParameter.OUTPUT_FILE_NAME, destFile.toString());

exporter.exportReport();
```

تم اختبار مقتطف الكود أعلاه باستخدام JasperReports 3.5.2. إذا كنت تستخدم JasperReports 3.1.0، فيرجى محاولة استخدام import com.aspose.pdf.jr3_1_0.jasperreports.; واستبدل إصدار المنتج في بقية الكود أيضًا.


