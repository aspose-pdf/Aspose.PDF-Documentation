---
title: Работа с заголовками в PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
url: /ru/net/working-with-headings/
weight: 70
description: Создайте нумерацию заголовков в вашем PDF-документе на C#. Aspose.PDF for .NET предлагает различные виды стилей нумерации.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Headings in PDF",
    "alternativeHeadline": "Enhance PDF Headings with Custom Numbering Styles",
    "abstract": "Улучшите свои PDF-документы с помощью настраиваемой нумерации заголовков с помощью Aspose.PDF для .NET. Эта новая функция позволяет применять различные предустановленные стили нумерации, такие как римские цифры и алфавитные списки, для эффективной организации заголовков, улучшая читаемость и структуру документа. Оптимизируйте процесс создания PDF-файлов, интегрировав эту универсальную функцию в свои приложения на C#",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF, C#, headings in PDF, numbering style, Aspose.PDF for .NET, pre-defined numbering styles, NumberingStyle enumeration, document generation, Heading class, pdf document manipulation",
    "wordcount": "453",
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
    "url": "/net/working-with-headings/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-headings/"
    },
    "dateModified": "2024-11-25",
    "description": "Создайте нумерацию в заголовке вашего PDF-документа с помощью C#. Aspose.PDF для .NET предлагает различные стили нумерации"
}
</script>

## Применение стиля нумерации в заголовке

Заголовки являются важными частями любого документа. Авторы всегда стараются сделать заголовки более заметными и значимыми для читателей. Если в документе несколько заголовков, у автора есть несколько способов их упорядочить. Один из наиболее распространённых подходов к упорядочиванию заголовков — это написание заголовков со стилем нумерации.

[Aspose.PDF for .NET](/pdf/net/) предлагает множество предустановленных стилей нумерации. Эти предустановленные стили хранятся в перечислении NumberingStyle. Предустановленные значения перечисления NumberingStyle и их описания приведены ниже:

|Типы заголовков|Описание|
|:--:| :--:|
|Арабские цифры| Арабский тип, например, 1,1.1,...|
|Римские цифры (прописные)| Римский верхний тип, например, I,I.II, ...|
|Римские цифры (строчные)| Римский нижний тип, например, i,i.ii, ...|
|Буквы (прописные)| Английский верхний тип, например, A,A.B, ...|
|Буквы (строчные)| Английский нижний тип, например, a,a.b, ...|

Свойство **Style** класса **Aspose.Pdf.Heading** используется для установки стилей нумерации заголовков.

|Рисунок: Предустановленные стили нумерации|
|:---|

Исходный код для получения вывода, показанного на рисунке выше, приведён ниже в примере.
Следующий фрагмент кода также работает с библиотекой [Aspose.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ApplyNumberStyleToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        document.PageInfo.Width = 612.0;
        document.PageInfo.Height = 792.0;
        document.PageInfo.Margin = new Aspose.Pdf.MarginInfo();
        document.PageInfo.Margin.Left = 72;
        document.PageInfo.Margin.Right = 72;
        document.PageInfo.Margin.Top = 72;
        document.PageInfo.Margin.Bottom = 72;

        // Add page
        var pdfPage = document.Pages.Add();
        pdfPage.PageInfo.Width = 612.0;
        pdfPage.PageInfo.Height = 792.0;
        pdfPage.PageInfo.Margin = new Aspose.Pdf.MarginInfo();
        pdfPage.PageInfo.Margin.Left = 72;
        pdfPage.PageInfo.Margin.Right = 72;
        pdfPage.PageInfo.Margin.Top = 72;
        pdfPage.PageInfo.Margin.Bottom = 72;

        // Create a floating box with the same margin as the page
        var floatBox = new Aspose.Pdf.FloatingBox();
        floatBox.Margin = pdfPage.PageInfo.Margin;

        // Add the floating box to the page
        pdfPage.Paragraphs.Add(floatBox);

        // Add headings with numbering styles
        var heading = new Aspose.Pdf.Heading(1);
        heading.IsInList = true;
        heading.StartNumber = 1;
        heading.Text = "List 1";
        heading.Style = Aspose.Pdf.NumberingStyle.NumeralsRomanLowercase;
        heading.IsAutoSequence = true;
        floatBox.Paragraphs.Add(heading);

        var heading2 = new Aspose.Pdf.Heading(1);
        heading2.IsInList = true;
        heading2.StartNumber = 13;
        heading2.Text = "List 2";
        heading2.Style = Aspose.Pdf.NumberingStyle.NumeralsRomanLowercase;
        heading2.IsAutoSequence = true;
        floatBox.Paragraphs.Add(heading2);

        var heading3 = new Aspose.Pdf.Heading(2);
        heading3.IsInList = true;
        heading3.StartNumber = 1;
        heading3.Text = "the value, as of the effective date of the plan, of property to be distributed under the plan on account of each allowed";
        heading3.Style = Aspose.Pdf.NumberingStyle.LettersLowercase;
        heading3.IsAutoSequence = true;
        floatBox.Paragraphs.Add(heading3);

        // Save PDF document
        document.Save(dataDir + "ApplyNumberStyle_out.pdf");
    }
}
```

<!-- 8081537722 -->
<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "Программное приложение",
    "название": "Библиотека Aspose.PDF for .NET",
    "изображение": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "издательство": {
        "@type": "Организация",
        "название": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "логотип": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternativeName": "Aspose",
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
    "предложения": {
        "@type": "Предложение",
        "цена": "1199",
        "валюта цены": "USD"
    },
    "категория приложения": "Библиотека управления PDF-файлами для .NET",
    "URL загрузки": "https://www.nuget.org/packages/Aspose.PDF/",
    "операционная система": "Windows, MacOS, Linux",
    "снимок экрана": 
<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>