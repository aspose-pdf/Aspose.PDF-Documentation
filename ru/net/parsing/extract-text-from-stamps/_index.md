---
title: Извлечение текста из штампов с помощью C#
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /ru/net/extract-text-from-stamps/
description: Узнайте, как использовать специальную функцию Aspose.PDF for .NET — извлечение текста из аннотаций штампов
lastmod: "2021-01-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Text From Stamps using C#",
    "alternativeHeadline": "Extract Text from PDF Stamp Annotations with Ease",
    "abstract": "Откройте для себя мощные возможности извлечения текста из Aspose.PDF для .NET, разработанные специально для извлечения текста из штамповых аннотаций в PDF-документах. Эта новая функция упрощает процесс, позволяя разработчикам легко получать доступ к тексту внутри штамповых аннотаций и управлять им с помощью кратких фрагментов кода, повышая производительность и эффективность задач управления PDF",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "168",
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
    "url": "/net/extract-text-from-stamps/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-text-from-stamps/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и лёгкие задачи, но и справляться с более сложными целями. Ознакомьтесь со следующим разделом для опытных пользователей и разработчиков."
}
</script>

## Извлечение текста из аннотаций штампов

Aspose.PDF для NET позволяет извлекать текст из аннотаций штампов. Для извлечения текста из аннотаций штампов в PDF можно выполнить следующие действия.

1. Создайте объект класса `Document`.
1. Получите нужную `Annotation` из списка аннотаций страницы.
1. Определите новый объект класса `TextAbsorber`.
1. Используйте метод TextAbsorber `visit`, чтобы получить текст.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractStampText.pdf"))
    {
        Aspose.Pdf.Annotations.Annotation item = document.Pages[1].Annotations[1];
        if (item is Aspose.Pdf.Annotations.StampAnnotation annot)
        {
            var absorber = new Aspose.Pdf.Text.TextAbsorber();
            Aspose.Pdf.XForm appearance = annot.Appearance["N"];
            absorber.Visit(appearance);
            Console.WriteLine(absorber.Text);
        }
    }
}
```