---
title: اكتشف ما إذا كان ملف PDF يحتوي على صور أو نص
linktitle: تحقق من وجود النص والصور
type: docs
weight: 40
url: ar/net/find-whether-pdf-file-contains-images-or-text-only/
description: يشرح هذا الموضوع كيفية معرفة ما إذا كان ملف PDF يحتوي على صور أو نص فقط باستخدام فئة PdfExtractor.
lastmod: "2021-06-05"
draft: false
---

## الخلفية

يمكن أن يحتوي ملف PDF على كل من النصوص والصور. في بعض الأحيان، قد يحتاج المستخدم إلى معرفة ما إذا كان ملف PDF يحتوي على نص فقط، أو يحتوي على صور فقط. يمكننا أيضًا معرفة ما إذا كان يحتوي على كليهما أو لا يحتوي على أي منهما.

{{% alert color="primary" %}}

يوضح لك مقتطف الشيفرة التالي كيفية تحقيق هذا المتطلب.

{{% /alert %}}

```csharp
 public static void CheckIfPdfContainsTextOrImages()
{
    // Instantiate a memoryStream object to hold the extracted text from Document
    MemoryStream ms = new MemoryStream();
    // Instantiate PdfExtractor object
    PdfExtractor extractor = new PdfExtractor();

    // Bind the input PDF document to extractor
    extractor.BindPdf(_dataDir + "FilledForm.pdf");
    // Extract text from the input PDF document
    extractor.ExtractText();
    // Save the extracted text to a text file
    extractor.GetText(ms);
    // Check if the MemoryStream length is greater than or equal to 1

    bool containsText = ms.Length >= 1;

    // Extract images from the input PDF document
    extractor.ExtractImage();

    // Calling HasNextImage method in while loop. When images will finish, loop will exit
    bool containsImage = extractor.HasNextImage();

    // Now find out whether this PDF is text only or image only

    if (containsText && !containsImage)
        Console.WriteLine("PDF يحتوي على نص فقط");
    else if (!containsText && containsImage)
        Console.WriteLine("PDF يحتوي على صور فقط");
    else if (containsText && containsImage)
        Console.WriteLine("PDF يحتوي على نص وصورة");
    else if (!containsText && !containsImage)
        Console.WriteLine("PDF لا يحتوي على نص ولا صورة");
}
```