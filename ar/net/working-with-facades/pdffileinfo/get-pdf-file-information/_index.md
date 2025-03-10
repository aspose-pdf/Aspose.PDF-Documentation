---
title: الحصول على معلومات ملف PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ar/net/get-pdf-file-information/
description: يشرح هذا القسم كيفية الحصول على معلومات ملف PDF باستخدام Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get PDF file information",
    "alternativeHeadline": "Retrieve Detailed Information from PDF Files",
    "abstract": "افتح بيانات التعريف الأساسية لملف PDF مع الميزة الجديدة التي تستخدم فئة PdfFileInfo من Aspose.PDF for .NET Facades. تتيح هذه الوظيفة للمطورين الوصول بسهولة إلى التفاصيل المهمة المتعلقة بالملف مثل الموضوع، العنوان، الكلمات الرئيسية، والمبدع، مما يعزز عمليات إدارة وتحليل الوثائق. قم بتبسيط تفاعلات PDF الخاصة بك من خلال الاستفادة من هذه الأداة القوية لاسترجاع معلومات الملف الشاملة",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "285",
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
    "url": "/net/get-pdf-file-information/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-pdf-file-information/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسريعة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

لكي تحصل على معلومات محددة عن ملف PDF، تحتاج إلى إنشاء كائن من فئة [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo). بعد ذلك، يمكنك الحصول على قيم الخصائص الفردية مثل الموضوع، العنوان، الكلمات الرئيسية، والمبدع، إلخ.

تظهر لك الشيفرة البرمجية التالية كيفية الحصول على معلومات ملف PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetPdfInfo()
{
    // Define the directory for input files
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var fileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "sample.pdf"))
    {
        // Get and display PDF information
        Console.WriteLine("Subject: {0}", fileInfo.Subject);
        Console.WriteLine("Title: {0}", fileInfo.Title);
        Console.WriteLine("Keywords: {0}", fileInfo.Keywords);
        Console.WriteLine("Creator: {0}", fileInfo.Creator);
        Console.WriteLine("Creation Date: {0}", fileInfo.CreationDate);
        Console.WriteLine("Modification Date: {0}", fileInfo.ModDate);

        // Check if the file is a valid PDF and if it is encrypted
        Console.WriteLine("Is Valid PDF: {0}", fileInfo.IsPdfFile);
        Console.WriteLine("Is Encrypted: {0}", fileInfo.IsEncrypted);

        // Get dimensions of the first page
        Console.WriteLine("Page width: {0}", fileInfo.GetPageWidth(1));
        Console.WriteLine("Page height: {0}", fileInfo.GetPageHeight(1));
    }
}
```

## الحصول على معلومات التعريف

لكي نحصل على المعلومات، نستخدم خاصية [Header](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/properties/header). باستخدام 'Hashtable' نحصل على جميع القيم الممكنة.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetMetaInfo()
{
    // Define the directory for input files
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of PdfFileInfo object
    using (var fileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "SetMetaInfo_out.pdf"))
    {
        // Retrieve all existing custom attributes
        var hashTable = new System.Collections.Hashtable(fileInfo.Header);

        // Enumerate and display all custom attributes
        var enumerator = hashTable.GetEnumerator();
        while (enumerator.MoveNext())
        {
            string output = $"{enumerator.Key} {enumerator.Value}";
            Console.WriteLine(output);
        }

        // Retrieve and display a specific custom attribute
        Console.WriteLine("Reviewer: " + fileInfo.GetMetaInfo("Reviewer"));
    }
}
```