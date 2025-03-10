---
title: 管理页眉和页脚
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /zh/net/manage-header-and-footer/
description: 探索如何在 .NET 中使用 Aspose.PDF 操作 PDF 文件中的页眉和页脚，以改善文档结构。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manage Header and Footer",
    "alternativeHeadline": "Enhance PDFs with Custom Headers and Footers",
    "abstract": "Aspose.PDF for .NET 中的管理页眉和页脚功能允许用户轻松地在 PDF 文档中添加、定制和格式化页眉和页脚，使用 PdfFileStamp 类。此功能支持文本和图像的包含，提供文档呈现的灵活性，同时确保专业的格式。用户可以将此功能无缝集成到他们的应用程序中，以增强 PDF 文件的视觉吸引力和组织性。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1007",
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
    "url": "/net/manage-header-and-footer/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manage-header-and-footer/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

## 在 PDF 文件中添加页眉

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 类允许您在 PDF 文件中添加页眉。为了添加页眉，您首先需要创建 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 类的对象。您可以使用 [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) 类格式化页眉文本。一旦您准备好在文件中添加页眉，您需要调用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 类的 [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) 方法。您还需要在 [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) 方法中至少指定顶部边距。最后，使用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 类的 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) 方法保存输出的 PDF 文件。以下代码片段向您展示如何在 PDF 文件中添加页眉。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHeader()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create formatted text for the header
        var formattedText = new Aspose.Pdf.Facades.FormattedText(
            "Aspose - Your File Format Experts!",
            System.Drawing.Color.Yellow,
            System.Drawing.Color.Black,
            Aspose.Pdf.Facades.FontStyle.Courier,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            false,
            14);

        // Add header
        fileStamp.AddHeader(formattedText, 10);

        // Save PDF document
        fileStamp.Save(dataDir + "AddHeader_out.pdf");
    }
}
```

## 在 PDF 文件中添加页脚

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 类允许您在 PDF 文件中添加页脚。为了添加页脚，您首先需要创建 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 类的对象。您可以使用 [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) 类格式化页脚文本。一旦您准备好在文件中添加页脚，您需要调用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 类的 [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) 方法。您还需要在 [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) 方法中至少指定底部边距。最后，使用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 类的 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) 方法保存输出的 PDF 文件。以下代码片段向您展示如何在 PDF 文件中添加页脚。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFooter()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create formatted text for the footer
        var formattedText = new Aspose.Pdf.Facades.FormattedText(
            "Aspose - Your File Format Experts!",
            System.Drawing.Color.Blue,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.Courier,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            false,
            14);

        // Add footer
        fileStamp.AddFooter(formattedText, 10);

        // Save PDF document
        fileStamp.Save(dataDir + "AddFooter_out.pdf");
    }
}
```

## 在现有 PDF 文件的页眉中添加图像

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 类允许您在 PDF 文件的页眉中添加图像。为了在页眉中添加图像，您首先需要创建 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 类的对象。之后，您需要调用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 类的 [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) 方法。您可以将图像传递给 [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/addheader/methods/4) 方法。最后，使用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 类的 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) 方法保存输出的 PDF 文件。以下代码片段向您展示如何在 PDF 文件的页眉中添加图像。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageHeader()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Add Header
        using (var fs = new FileStream(dataDir + "ImageHeader.png", FileMode.Open))
        {
            fileStamp.AddHeader(fs, 10);  // Add image header with position offset

            // Save PDF document
            fileStamp.Save(dataDir + "AddImageHeader_out.pdf");
        }
    }
}
```

## 在现有 PDF 文件的页脚中添加图像

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 类允许您在 PDF 文件的页脚中添加图像。为了在页脚中添加图像，您首先需要创建 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 类的对象。之后，您需要调用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 类的 [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) 方法。您可以将图像传递给 [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) 方法。最后，使用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 类的 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) 方法保存输出的 PDF 文件。以下代码片段向您展示如何在 PDF 文件的页脚中添加图像。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageFooter()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Add footer
        using (var fs = new FileStream(dataDir + "ImageFooter.png", FileMode.Open))
        {
            fileStamp.AddFooter(fs, 10);  // Add image footer with position offset

            // Save PDF document
            fileStamp.Save(dataDir + "AddImageFooter_out.pdf");
        }
    }
}
```