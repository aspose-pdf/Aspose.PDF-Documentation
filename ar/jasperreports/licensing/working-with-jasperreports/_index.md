---
title: العمل مع جاسبر ريبورتس
linktitle: العمل مع جاسبر ريبورتس
type: docs
weight: 10
url: /ar/jasperreports/working-with-jasperreports/
description: إتقان العمل مع JasperReports باستخدام Aspose.PDF. قم بإنشاء وتصدير تقارير مفصلة بتنسيق PDF مع ميزات متقدمة.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

يتوفر Aspose.PDF for JasperReports للتقييم المجاني وغير المحدود من صفحة التنزيل. التقييم والإصدارات المرخّصة للمنتج هي نفس التنزيل.

عندما تكون راضيًا عن الإصدار التقييمي، [قم بشراء ترخيص](https://purchase.aspose.com/buy?ppId=98899). تأكد من أنك تفهم شروط الترخيص وتوافق عليها.

{{% /alert %}}

الترخيص متاح للتنزيل من صفحة الطلب بعد دفع الطلب. الترخيص عبارة عن نص واضح وملف XML موقّع رقميًا. يحتوي الترخيص على معلومات مثل اسم العميل والمنتج الذي تم شراؤه ونوع الترخيص. لا تقم بتعديل محتوى ملف الترخيص: فهذا يبطل الترخيص.

هناك عدة طرق لتفعيل الترخيص:

- [اتصل بـ setLicense](/pdf/jasperreports/working-with-jasperreports/#call-setlicense).
- [قم بتعيين معلمة المصدر في الكود](/pdf/jasperreports/working-with-jasperreports/#set-the-licensefile-exporter-parameter-in-the-code).
- [قم بتعيين معلمة المصدر في **applicationContext.xml**](/pdf/jasperreports/working-with-jasperserver/).

يتم استخدام الأولين مع JasperReports، والأخير مع JasperServer.

## اتصل بـ setLicense

يتم استخدام هذه الطريقة مع JasperReports.

1. Download the license to your computer and copy it to the appropriate folder (for example your application's folder or JasperReports\lib).
2. أضف الكود التالي إلى مشروعك:

```java
import com.aspose.pdf.jr3_7_0.jasperreports.*;
try
{ 
    // create a stream object containing the license file
   FileInputStream fstream = new FileInputStream("C:\\Aspose.PDF.JasperReports.lic");  

    // Set the license through the stream object
 
   License license = new License();
   license.setLicense(fstream);
}
catch(Exception ex)
{
   System.out.println(ex.toString());
}

```

## قم بتعيين معلمة مُصدر ملف الترخيص في الكود

يتم استخدام هذه الطريقة مع JasperReports.

1. قم بتنزيل الترخيص على جهاز الكمبيوتر الخاص بك وانسخه إلى المجلد المناسب (على سبيل المثال، مجلد التطبيق الخاص بك أو JasperReports\lib).
2. أضف الكود التالي إلى مشروعك:

```java

import com.aspose.pdf.jr3_7_0.jasperreports.*;

com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter exporter = new com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter();
exporter.setParameter(PdfExporterParameter.LICENSE, "Aspose.PDF.JasperReports.lic");
exporter.exportReport();

```



