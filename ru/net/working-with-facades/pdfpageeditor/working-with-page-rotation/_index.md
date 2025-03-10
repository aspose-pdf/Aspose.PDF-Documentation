---
title: Работа с поворотом страниц
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ru/net/working-with-page-rotation/
description: В этом разделе объясняется, как работать с поворотом страниц с помощью класса PdfPageEditor.
lastmod: "2021-07-07"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Page Rotation",
    "alternativeHeadline": "Effortlessly Rotate PDF Pages with PdfPageEditor",
    "abstract": "Откройте для себя мощную функцию поворота страниц в классе PdfPageEditor, позволяющую точно манипулировать страницами документа с помощью настраиваемых углов поворота. С возможностью указания индивидуальных поворотов страниц или применения единообразного поворота к выбранным страницам, эта функциональность улучшает возможности редактирования PDF, предлагая большую гибкость и контроль для пользователей.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "202",
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
    "url": "/net/working-with-page-rotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-page-rotation/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

{{% alert color="primary" %}}

[PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) класс предоставляет возможность поворачивать страницу.

{{% /alert %}}

## Поворот страницы с использованием PageRotations

Чтобы повернуть страницы в документе, мы можем использовать [PageRotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/pagerotations).
`PageRotations` содержит номер страницы и угол поворота, ключ представляет номер страницы, значение ключа представляет угол поворота в градусах.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void RotatePages1()
 {
    // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     using (var editor = new Aspose.Pdf.Facades.PdfPageEditor())
     {
         // Bind PDF document
         editor.BindPdf(dataDir + "sample.pdf");

         // Specify the page rotation dictionary
         editor.PageRotations = new System.Collections.Generic.Dictionary<int, int>
         {
             { 1, 90 },
             { 2, 180 },
             { 3, 270 }
         };

         // Save PDF document
         editor.Save(dataDir + "sample-rotate-a.pdf");
     }
 }
```

## Поворот страницы с использованием Rotation

Мы также можем использовать [Rotation](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/rotation) свойство. Поворот должен быть 0, 90, 180 или 270

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RotatePages2()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    using (var editor = new Aspose.Pdf.Facades.PdfPageEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "sample.pdf");

        // Specify the pages to rotate and the rotation angle
        editor.ProcessPages = new int[] { 1, 3 };
        editor.Rotation = 90;

        // Save PDF document
        editor.Save(dataDir + "sample-rotate-a.pdf");
    }
}
```