---
title: استخراج المرفقات من ملف PDF
type: docs
weight: 10
url: /ar/net/extract-attachments/
description: يوضح هذا القسم كيفية استخراج المرفقات من ملفات pdf باستخدام فئة PdfExtractor.
lastmod: "2021-06-05"
---

إحدى الفئات الرئيسية تحت قدرات الاستخراج في مساحة الأسماء [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) هي استخراج المرفقات.
``` 
هذه الفئة توفر مجموعة من الأساليب، التي لا تساعد فقط في استخراج المرفقات بل توفر أيضًا الأساليب التي يمكن أن تعطيك المعلومات المتعلقة بالمرفقات مثل [GetAttachmentInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachmentinfo) و [GetAttachName](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachnames) توفر معلومات المرفقات واسم المرفق على التوالي. من أجل استخراج ثم الحصول على المرفقات نستخدم طرق [ExtractAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractattachment) و [GetAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachment).

يعرض مقطع الشيفرة التالي كيفية استخدام أساليب PdfExtractor:

```csharp
public static void ExtractAttachments()
{
    PdfExtractor pdfExtractor = new PdfExtractor();
    pdfExtractor.BindPdf(_dataDir + "sample-attach.pdf");

    // Extract attachments
    pdfExtractor.ExtractAttachment();

    // Get attachment names
    if (pdfExtractor.GetAttachNames().Count > 0)
    {
         Console.WriteLine("Extracting and storing...");
         // Get extracted attachments
         pdfExtractor.GetAttachment(_dataDir);
    }
}
```
```