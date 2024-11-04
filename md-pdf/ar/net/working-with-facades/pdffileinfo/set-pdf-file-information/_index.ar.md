---
title: تعيين معلومات ملف PDF
type: docs
weight: 40
url: /net/set-pdf-file-information/
description: يوضح هذا القسم كيفية تعيين معلومات ملف PDF باستخدام Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

تسمح لك فئة [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) بتعيين معلومات محددة لملف PDF. تحتاج إلى إنشاء كائن من فئة [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) ثم تعيين خصائص مختلفة محددة للملف مثل المؤلف، العنوان، الكلمة الرئيسية، والمبدع إلخ. وأخيراً، احفظ ملف PDF المحدث باستخدام طريقة [SaveNewInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileinfo/savenewinfo/methods/1) لكائن [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo).

يوضح لك مقطع الشيفرة التالي كيفية تعيين معلومات ملف PDF.

```csharp
 public static void SetPdfInfo()
        {
            PdfFileInfo fileInfo = new PdfFileInfo(_dataDir + "sample.pdf")
            {
                // تعيين معلومات PDF
                Author = "Aspose",
                Title = "Hello World!",
                Keywords = "Peace and Development",
                Creator = "Aspose"
            };
            // حفظ الملف المحدث
            fileInfo.SaveNewInfo(_dataDir + "SetFileInfo_out.pdf");
        }
```
```

## إعداد معلومات التعريف

طريقة [SetMetaInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/methods/setmetainfo) تتيح لك إضافة أي معلومات. في مثالنا، أضفنا حقلًا. تحقق من المقتطف البرمجي التالي:

```csharp
 public static void SetMetaInfo()
        {
            // إنشاء مثيل لكائن PdfFileInfo
            Aspose.Pdf.Facades.PdfFileInfo fInfo = new Aspose.Pdf.Facades.PdfFileInfo(_dataDir + "sample.pdf");

            // تعيين سمة العميل الجديدة كمعلومات تعريف
            fInfo.SetMetaInfo("Reviewer", "Aspose.PDF user");

            // حفظ الملف المحدث
            fInfo.SaveNewInfo(_dataDir + "SetMetaInfo_out.pdf");
```