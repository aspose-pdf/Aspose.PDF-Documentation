---
title: العثور على ما إذا كان ملف PDF يحتوي على صور أو نص
linktitle: تحقق من وجود النصوص والصور
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ar/net/find-whether-pdf-file-contains-images-or-text-only/
description: يشرح هذا الموضوع كيفية العثور على ما إذا كان ملف PDF يحتوي على صور أو نص فقط باستخدام فئة PdfExtractor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Find whether PDF contains images or text",
    "alternativeHeadline": "Determine PDF Content: Text, Images, or Both",
    "abstract": "اكتشف الوظيفة التي تتيح للمستخدمين تحديد ما إذا كان ملف PDF يحتوي على نصوص، صور، أو كليهما، باستخدام فئة PdfExtractor. تسهل هذه الميزة عملية تحليل محتوى PDF، مما يوفر مخرجات واضحة حول وجود النصوص والصور داخل الملف. مع بضع أسطر من التعليمات البرمجية، يمكن للمستخدمين تصنيف مستندات PDF الخاصة بهم بناءً على نوع المحتوى",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "265",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/find-whether-pdf-file-contains-images-or-text-only/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/find-whether-pdf-file-contains-images-or-text-only/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF تنفيذ المهام البسيطة والسلسة ولكن أيضًا التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## الخلفية

يمكن أن يحتوي ملف PDF على نصوص وصور. في بعض الأحيان، قد يحتاج المستخدم إلى معرفة ما إذا كان ملف PDF يحتوي على نصوص فقط، أو يحتوي على صور فقط. يمكننا أيضًا معرفة ما إذا كان يحتوي على كليهما أو لا شيء.

{{% alert color="primary" %}}

تظهر لك مقتطفات التعليمات البرمجية التالية كيفية تلبية هذا المتطلب.

{{% /alert %}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckIfPdfContainsTextOrImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Instantiate a memoryStream object to hold the extracted text from Document
    using (var ms = new MemoryStream())
    {
        // Create the PdfExtractor
        using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
        {
            // Bind PDF document
            extractor.BindPdf(dataDir + "FilledForm.pdf");
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
            {
                Console.WriteLine("PDF contains text only");
            }
            else if (!containsText && containsImage)
            {
                Console.WriteLine("PDF contains image only");
            }
            else if (containsText && containsImage)
            {
                Console.WriteLine("PDF contains both text and image");
            }
            else if (!containsText && !containsImage)
            {
                Console.WriteLine("PDF contains neither text or nor image");
            }
        }
    }
}
```