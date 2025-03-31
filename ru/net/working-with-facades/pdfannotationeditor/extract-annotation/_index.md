---
title: Извлечение аннотаций из PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ru/net/extract-annotation/
description: Этот раздел объясняет, как извлечь аннотации из PDF-файла в XFDF с помощью Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Annotations from PDF",
    "alternativeHeadline": "Effortlessly Extract PDF Annotations to XFDF Format",
    "abstract": "Раскройте потенциал ваших PDF-документов с новой функцией извлечения аннотаций, которая позволяет бесшовно извлекать аннотации в формат XFDF с использованием Aspose.PDF for .NET. Эта функциональность позволяет легко извлекать конкретные типы аннотаций, повышая эффективность управления документами и сотрудничества. Узнайте, как оптимизировать ваши рабочие процессы PDF, извлекая и сохраняя важные данные аннотаций без усилий.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "254",
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
    "url": "/net/extract-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-annotation/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но также справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

[ExtractAnnotations](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades.pdfannotationeditor/extractannotations/methods/1) метод позволяет извлекать аннотации из PDF-файла. Для извлечения аннотаций вам необходимо создать объект [PdfAnnotationEditor](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdfannotationeditor) и связать PDF-файл с помощью метода [BindPdf](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades.facade/bindpdf/methods/3). После этого вам нужно создать перечисление типов аннотаций, которые вы хотите извлечь из PDF-файла.

Затем вы можете использовать метод [ExtractAnnotations](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades.pdfannotationeditor/extractannotations/methods/1) для извлечения аннотаций в ArrayList. После этого вы можете пройтись по этому списку и получить отдельные аннотации. И, наконец, сохраните обновленный PDF-файл, используя метод [Save](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document/methods/save) объекта [PdfAnnotationEditor](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdfannotationeditor). Следующий фрагмент кода показывает, как извлечь аннотации из PDF-файла.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AnnotationsInput.pdf"))
    {
        using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
        {
            // Bind PDF document
            annotationEditor.BindPdf(document);
            // Extract annotations
            var annotationTypes = new[] { Aspose.Pdf.Annotations.AnnotationType.FreeText, Aspose.Pdf.Annotations.AnnotationType.Text };
            var annotations = annotationEditor.ExtractAnnotations(1, 2, annotationTypes);
            foreach (var annotation in annotations)
            {
                Console.WriteLine(annotation.Contents);
            }
        }
    }
}
```