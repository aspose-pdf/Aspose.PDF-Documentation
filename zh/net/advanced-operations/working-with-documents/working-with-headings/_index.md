---
title: 在 PDF 中使用标题
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
url: /zh/net/working-with-headings/
weight: 70
description: 使用 C# 在 PDF 文档中创建标题编号。Aspose.PDF for .NET 提供不同类型的编号样式。
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
    "abstract": "使用 Aspose.PDF for .NET 自定义标题编号来增强您的 PDF 文档。此新功能允许您应用各种预定义的编号样式，例如罗马数字和字母列表，以有效组织您的标题，提高文档的可读性和结构。通过将此多功能功能集成到您的 C# 应用程序中，简化您的 PDF 创建过程。",
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
    "description": "使用 C# 在 PDF 文档中创建标题编号。Aspose.PDF for .NET 提供不同类型的编号样式。"
}
</script>

## 在标题中应用编号样式

标题是任何文档的重要部分。作者总是试图使标题对读者更加突出和有意义。如果文档中有多个标题，作者有几种选择来组织这些标题。组织标题的最常见方法之一是以编号样式书写标题。

[Aspose.PDF for .NET](/pdf/zh/net/) 提供许多预定义的编号样式。这些预定义的编号样式存储在一个枚举中，NumberingStyle。NumberingStyle 枚举的预定义值及其描述如下：

|**标题类型**|**描述**|
| :- | :- |
|NumeralsArabic|阿拉伯类型，例如，1,1.1,...|
|NumeralsRomanUppercase|罗马大写类型，例如，I,I.II,...|
|NumeralsRomanLowercase|罗马小写类型，例如，i,i.ii,...|
|LettersUppercase|英语大写类型，例如，A,A.B,...|
|LettersLowercase|英语小写类型，例如，a,a.b,...|
**Aspose.Pdf.Heading** 类的 **Style** 属性用于设置标题的编号样式。

|**图：预定义编号样式**|
| :- |
获取上图所示输出的源代码如下所示。

下一个代码片段也与 [Aspose.Drawing](/pdf/zh/net/drawing/) 库一起使用。

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