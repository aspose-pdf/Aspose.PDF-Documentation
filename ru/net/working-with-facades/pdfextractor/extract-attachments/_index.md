---
title: Извлечение вложений из PDF файла
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ru/net/extract-attachments/
description: Узнайте, как извлекать и управлять вложениями в PDF документах на .NET с помощью Aspose.PDF для лучшей обработки документов.
lastmod: "2021-06-05"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Attachments from PDF File",
    "alternativeHeadline": "Effortlessly Extract and Manage PDF Attachments",
    "abstract": "Новая функциональность извлечения вложений в Aspose.PDF for .NET позволяет разработчикам легко извлекать и управлять файловыми вложениями в PDF документах. Используя класс PdfExtractor, пользователи могут извлекать вложения и получать важную информацию, такую как имена вложений и детали, что улучшает возможности обработки документов.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "208",
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
    "url": "/net/extract-attachments/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-attachments/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

Одна из основных категорий под возможностями извлечения пространства имен [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades) — это извлечение вложений. Эта категория предоставляет набор методов, которые не только помогают извлекать вложения, но и предоставляют методы, которые могут дать вам информацию, связанную с вложениями, т.е. методы [GetAttachmentInfo](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdfextractor/methods/getattachmentinfo) и [GetAttachName](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdfextractor/methods/getattachnames) предоставляют информацию о вложении и имя вложения соответственно. Для извлечения и получения вложений мы используем методы [ExtractAttachment](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdfextractor/methods/extractattachment) и [GetAttachment](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdfextractor/methods/getattachment).

Следующий фрагмент кода показывает, как использовать методы PdfExtractor:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractAttachments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

    // Create the extractor
    using (var pdfExtractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        pdfExtractor.BindPdf(dataDir + "GetAlltheAttachments.pdf");

        // Extract attachments
        pdfExtractor.ExtractAttachment();

        // Get attachment names
        if (pdfExtractor.GetAttachNames().Count > 0)
        {
            Console.WriteLine("Extracting and storing...");

            // Get extracted attachments
            pdfExtractor.GetAttachment(dataDir + "GetAlltheAttachments_out.pdf");
        }
    }
}
```