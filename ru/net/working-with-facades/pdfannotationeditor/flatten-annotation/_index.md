---
title: Упрощение аннотаций из PDF в XFDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ru/net/flatten-annotation/
description: В этом разделе объясняется, как экспортировать аннотации из PDF-файла в XFDF с помощью Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Flatten Annotation from PDF to XFDF",
    "alternativeHeadline": "Export PDF Annotations as Non-Editable XFDF Format",
    "abstract": "Функция упрощения аннотаций из PDF в XFDF позволяет пользователям экспортировать аннотации из PDF-файлов в формат XFDF, сохраняя их визуальное представление. Эта функциональность гарантирует, что аннотации остаются видимыми в документе, но становятся не редактируемыми, предоставляя способ навсегда применить заметки или комментарии для зрителей, которые могут не поддерживать функции аннотаций.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "191",
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
    "url": "/net/flatten-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/flatten-annotation/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

Процесс упрощения означает, что когда аннотация удаляется из документа, ее визуальное представление остается нетронутым. Упрощенная аннотация все еще видима, но больше не может быть отредактирована вашими пользователями или вашим приложением. Это можно использовать, например, для того, чтобы навсегда применить аннотации к вашему документу или сделать аннотации видимыми для зрителей, которые в противном случае не могут отображать аннотации. Если не указано иное, экспорт сохранит все аннотации в их исходном виде.

Когда эта опция выбрана, ваши аннотации будут включены в экспортируемый PDF как аннотации стандартов PDF.

Проверьте, как используется метод [flatteningAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/flatteningannotations) в следующем фрагменте кода.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FlattenAnnotationFromPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();

    // Create PdfAnnotationEditor
    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Bind PDF document
        annotationEditor.BindPdf(dataDir + "AnnotationsInput.pdf");
        // Create FlattenSettings
        var flattenSettings = new Aspose.Pdf.Forms.Form.FlattenSettings
        {
            ApplyRedactions = true,
            CallEvents = false,
            HideButtons = true,
            UpdateAppearances = true
        };
        annotationEditor.FlatteningAnnotations(flattenSettings);
        // Save PDF document
        annotationEditor.Save(dataDir + "FlattenAnnotation_out.pdf");
    }
}
```