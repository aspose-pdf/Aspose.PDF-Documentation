---

title: Working with JasperReports

type: docs

weight: 10

url: ar/jasperreports/working-with-jasperreports/

lastmod: "2021-06-05"

---

{{% alert color="primary" %}}

Aspose.Words for JasperReports متاح للتقييم المجاني وغير المحدود من صفحة التحميل. الإصدار التجريبي والإصدار المرخص من المنتج هو نفس التحميل.

عندما تكون راضيًا عن الإصدار التجريبي، [قم بشراء ترخيص](http://www.aspose.com/purchase/default.aspx). تأكد من أنك تفهم وتوافق على شروط الترخيص.

{{% /alert %}}

الترخيص متاح للتحميل من صفحة الطلب بعد دفع الطلب. الترخيص هو ملف XML موقع رقميًا وواضح النص. يحتوي الترخيص على معلومات مثل اسم العميل، المنتج المشتري ونوع الترخيص. لا تقم بتعديل محتوى ملف الترخيص: يؤدي ذلك إلى إبطال الترخيص.

هناك عدة طرق لتفعيل الترخيص:

- [استدعاء setLicense](/pdf/jasperreports/working-with-jasperreports/#call-setlicense).

- [تعيين مُعَامِل المصدِّر في الكود](/pdf/jasperreports/working-with-jasperreports/#set-the-licensefile-exporter-parameter-in-the-code).

- [تعيين معلمة المُصدّر في **applicationContext.xml**](/pdf/jasperreports/working-with-jasperserver/).



الأولان يُستخدمان مع JasperReports، والأخير مع JasperServer.

#### **استدعاء setLicense**

<ins> **تُستخدم هذه الطريقة مع JasperReports.**



1. قم بتنزيل الترخيص على جهاز الكمبيوتر الخاص بك ونسخه إلى المجلد المناسب (على سبيل المثال مجلد التطبيق الخاص بك أو JasperReports\lib).

2. أضف الكود التالي إلى مشروعك:



```

import com.aspose.pdf.jr3_7_0.jasperreports.*;

try

{ 

    // إنشاء كائن تدفق يحتوي على ملف الترخيص

   FileInputStream fstream = new FileInputStream("C:\\Aspose.PDF.JasperReports.lic");  



    // تعيين الترخيص من خلال كائن التدفق

 

   License license = new License();

   license.setLicense(fstream);

}

catch(Exception ex)

{

   System.out.println(ex.toString());

}



```



#### **تعيين معلمة Exporter licenseFile في الكود**



<ins> **تُستخدم هذه الطريقة مع JasperReports.**



1. Download the license to your computer and copy it to the appropriate folder (for example your application's folder or JasperReports\lib).

قم بتنزيل الترخيص على جهاز الكمبيوتر الخاص بك وانسخه إلى المجلد المناسب (على سبيل المثال مجلد التطبيق الخاص بك أو JasperReports\lib).

2. Add the following code to your project:

2. أضف الكود التالي إلى مشروعك:

```

import com.aspose.pdf.jr3_7_0.jasperreports.*;

import com.aspose.pdf.jr3_7_0.jasperreports.*;

com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter exporter = new com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter();

com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter exporter = new com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter();

exporter.setParameter(PdfExporterParameter.LICENSE, "Aspose.PDF.JasperReports.lic");

exporter.setParameter(PdfExporterParameter.LICENSE, "Aspose.PDF.JasperReports.lic");

exporter.exportReport();

exporter.exportReport();

```