---
title: استخراج الخطوط من PDF C#
linktitle: استخراج الخطوط من PDF
type: docs
weight: 30
url: /ar/net/extract-fonts-from-pdf/
description: استخدم مكتبة Aspose.PDF for. NET لاستخراج جميع الخطوط المضمنة من مستند PDF الخاص بك.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

في حالة رغبتك في الحصول على جميع الخطوط من مستند PDF، يمكنك استخدام الطريقة FontUtilities.GetAllFonts() المتوفرة في فئة Document. يرجى التحقق من الشفرة البرمجية التالية للحصول على جميع الخطوط من مستند PDF موجود:

الشفرة البرمجية التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
Document doc = new Document(dataDir + "input.pdf");
Aspose.Pdf.Text.Font[] fonts = doc.FontUtilities.GetAllFonts();
foreach (Aspose.Pdf.Text.Font font in fonts)
{
    Console.WriteLine(font.FontName);
}
```

