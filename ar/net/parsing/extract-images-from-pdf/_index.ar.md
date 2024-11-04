---
title: استخراج الصور من PDF C#
linktitle: استخراج الصور من PDF
type: docs
weight: 20
url: /net/extract-images-from-the-pdf-file/
description: كيفية استخراج جزء من الصورة من PDF باستخدام Aspose.PDF لـ .NET في C#
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

الصور موجودة في مجموعة [الموارد](https://reference.aspose.com/pdf/net/aspose.pdf/resources) لكل صفحة داخل مجموعة [الصور](https://reference.aspose.com/pdf/net/aspose.pdf/resources/properties/images). لاستخراج صفحة معينة، ثم الحصول على الصورة من مجموعة الصور باستخدام الفهرس المحدد للصورة.

فهرس الصورة يعيد كائن [XImage](https://reference.aspose.com/pdf/net/aspose.pdf/ximage). هذا الكائن يوفر طريقة حفظ يمكن استخدامها لحفظ الصورة المستخرجة. يوضح الجزء التالي من الكود كيفية استخراج الصور من ملف PDF.

الجزء التالي من الكود يعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

 ```csharp
 // للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 ```

// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// فتح المستند
Document pdfDocument = new Document(dataDir+ "ExtractImages.pdf");

// استخراج صورة معينة
XImage xImage = pdfDocument.Pages[1].Resources.Images[1];

FileStream outputImage = new FileStream(dataDir + "output.jpg", FileMode.Create);

// حفظ الصورة الناتجة
xImage.Save(outputImage, ImageFormat.Jpeg);
outputImage.Close();

dataDir = dataDir + "ExtractImages_out.pdf";

// حفظ ملف PDF المحدث
pdfDocument.Save(dataDir);
```

