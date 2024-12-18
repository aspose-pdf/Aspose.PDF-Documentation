---
title: إنشاء PDF/3-A متوافق مع PDF وإرفاق فاتورة ZUGFeRD في C#
linktitle: إرفاق ZUGFeRD بـ PDF
type: docs
weight: 10
url: /ar/net/attach-zugferd/
description: تعرف على كيفية توليد مستند PDF مع ZUGFeRD في Aspose.PDF لـ .NET
lastmod: "2023-11-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## إرفاق ZUGFeRD بـ PDF

الشفرة البرمجية التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

نوصي باتباع الخطوات التالية لإرفاق ZUGFeRD بـ PDF:

* تحديد متغير المسار الذي يشير إلى مجلد حيث توجد ملفات PDF الإدخال والإخراج.
* إنشاء كائن المستند بتحميل ملف PDF موجود (مثلاً "ZUGFeRD-test.pdf") من المسار.
* إنشاء كائن [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification/) بتوفير المسار ووصف ملف آخر يُدعى "factur-x.xml"، والذي يحتوي على بيانات فواتير مطابقة لمعيار ZUGFeRD.
* إضافة خصائص إلى كائن مواصفات الملف، مثل الوصف، نوع MIME، وعلاقة AF.
* أضف خصائص إلى كائن مواصفات الملف، مثل الوصف، نوع MIME، وعلاقة AF.
* أضف كائن مواصفات الملف إلى مجموعة الملفات المدمجة في المستند. يجب تحديد اسم الملف وفقًا لمعيار ZUGFeRD، مثل "factur-x.xml".
* تحويل المستند إلى تنسيق PDF/A-3U، وهو جزء من PDF يضمن الحفظ طويل الأمد للوثائق الإلكترونية. يسمح PDF/A-3U بتضمين ملفات بأي تنسيق في مستندات PDF.
* حفظ المستند المحول كملف PDF جديد (على سبيل المثال، "ZUGFeRD-res.pdf").

```cs
var path = @"C:\Samples\ZUGFeRD\";

var document = new Aspose.Pdf.Document(Path.Combine(path,"ZUGFeRD-test.pdf"));
// Setup new file to be added as attachment
var description = "بيانات فاتورة وفقًا لمعيار ZUGFeRD";
var fileSpecification = new Aspose.Pdf.FileSpecification(Path.Combine(path, "factur-x.xml"), description)
{
    Description = "Zugferd",
    MIMEType = "text/xml",
    AFRelationship = Aspose.Pdf.AFRelationship.Alternative
};
// Add attachment to document's attachment collection
document.EmbeddedFiles.Add(fileSpecification);
document.Convert(new MemoryStream(), Aspose.Pdf.PdfFormat.PDF_A_3U, Aspose.Pdf.ConvertErrorAction.Delete);
document.Save(Path.Combine(path, "ZUGFeRD-res.pdf"));
```
الطريقة convert تأخذ stream، تنسيق PDF، وإجراء خطأ التحويل كمعاملات. يمكن استخدام معامل الstream لحفظ سجل التحويل. معامل إجراء خطأ التحويل يحدد ما يجب القيام به إذا حدثت أي أخطاء أثناء التحويل. في هذه الحالة، يتم ضبطه على "Delete"، وهذا يعني أن أي عناصر غير متوافقة مع تنسيق PDF/A-3U سيتم حذفها من الوثيقة.
