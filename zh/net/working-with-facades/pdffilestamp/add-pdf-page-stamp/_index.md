---
title: 添加 PDF 页面印章
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /zh/net/add-pdf-page-stamp/
description: 了解如何在 .NET 中向 PDF 页面添加印章，包括文本和图像，用于水印或品牌标识，使用 Aspose.PDF。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add PDF Page Stamp",
    "alternativeHeadline": "Enhance PDFs with Custom Stamps and Page Numbers",
    "abstract": "介绍 PDF 页面印章功能，允许用户轻松地在 PDF 文档的所有或特定页面上添加自定义印章，使用 PdfFileStamp 类。此功能通过启用旋转、背景和自定义编号样式等各种属性来增强文档个性化，使您的 PDF 文件不仅独特而且专业。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1309",
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
    "url": "/net/add-pdf-page-stamp/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-pdf-page-stamp/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

## 在 PDF 文件的所有页面上添加 PDF 页面印章

[PdfFileStamp](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffilestamp) 类允许您在 PDF 文件的所有页面上添加 PDF 页面印章。为了添加 PDF 页面印章，您首先需要创建 [PdfFileStamp](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffilestamp) 和 [Stamp](https://reference.aspose.com/pdf/zh/net/aspose.pdf/stamp) 类的对象。您还需要使用 [Stamp](https://reference.aspose.com/pdf/zh/net/aspose.pdf/stamp) 类的 [PdfFileStamp](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffilestamp) 方法创建 PDF 页面印章。您还可以使用 [Stamp](https://reference.aspose.com/pdf/zh/net/aspose.pdf/stamp) 对象设置其他属性，如原点、旋转、背景等。然后，您可以使用 [PdfFileStamp](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffilestamp) 类的 [AddStamp](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) 方法将印章添加到 PDF 文件中。最后，使用 [PdfFileStamp](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffilestamp) 类的 [Close](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/facade/methods/close) 方法保存输出 PDF 文件。以下代码片段演示了如何在 PDF 文件的所有页面上添加 PDF 页面印章。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPageStampOnAllPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "SourcePDF.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        // Bind PDF document
        stamp.BindPdf(dataDir + "AddPageStampOnAllPages.pdf", 1);
        stamp.SetOrigin(20, 20);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "PageStampOnAllPages_out.pdf");
    }
}
```

## 在 PDF 文件的特定页面上添加 PDF 页面印章

[PdfFileStamp](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffilestamp) 类允许您在 PDF 文件的特定页面上添加 PDF 页面印章。为了添加 PDF 页面印章，您首先需要创建 [PdfFileStamp](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffilestamp) 和 [Stamp](https://reference.aspose.com/pdf/zh/net/aspose.pdf/stamp) 类的对象。您还需要使用 [Stamp](https://reference.aspose.com/pdf/zh/net/aspose.pdf/stamp) 类的 [BindPdf](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades.facade/bindpdf/methods/3) 方法创建 PDF 页面印章。您还可以使用 [Stamp](https://reference.aspose.com/pdf/zh/net/aspose.pdf/stamp) 对象设置其他属性，如原点、旋转、背景等。由于您想在 PDF 文件的特定页面上添加 PDF 页面印章，您还需要设置 [Stamp](https://reference.aspose.com/pdf/zh/net/aspose.pdf/stamp) 类的 [Pages](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/stamp/properties/pages) 属性。此属性需要一个整数数组，包含您想要添加印章的页面编号。然后，您可以使用 [PdfFileStamp](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffilestamp) 类的 [AddStamp](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) 方法将印章添加到 PDF 文件中。最后，使用 [PdfFileStamp](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffilestamp) 类的 [Close](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/facade/methods/close) 方法保存输出 PDF 文件。以下代码片段演示了如何在 PDF 文件的特定页面上添加 PDF 页面印章。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPageStampOnCertainPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "SourcePDF.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        // Bind PDF document
        stamp.BindPdf(dataDir + "PageStampOnCertainPages.pdf", 1);
        stamp.SetOrigin(20, 20);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;
        stamp.Pages = new[] { 1, 3 };  // Apply stamp to specific pages (1 and 3)

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "PageStampOnCertainPages_out.pdf");
    }
}
```

## 在 PDF 文件中添加页码

[PdfFileStamp](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffilestamp) 类允许您在 PDF 文件中添加页码。为了添加页码，您首先需要创建 [PdfFileStamp](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffilestamp) 类的对象。如果您想以“第 X 页，共 N 页”的形式显示页码，其中 X 是当前页码，N 是 PDF 文件中的总页数，则您首先需要使用 [PdfFileInfo](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffileinfo) 类的 [NumberOfpages](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffileinfo/properties/numberofpages) 属性获取页数。为了获取当前页码，您可以在文本中使用 **#** 符号。您可以使用 [FormattedText](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/formattedtext) 类格式化页码文本。如果您想从特定数字开始页码编号，则可以设置 [StartingNumber](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffilestamp/properties/startingnumber) 属性。一旦您准备好在文件中添加页码，您需要调用 [PdfFileStamp](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffilestamp) 类的 [AddPageNumber](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades.pdffilestamp/addpagenumber/methods/7) 方法。最后，使用 [PdfFileStamp](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/facade/methods/close) 类的 [Close](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/facade/methods/close) 方法保存输出 PDF 文件。以下代码片段演示了如何在 PDF 文件中添加页码。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPageNumberInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "StampPDF.pdf");

        // Get total number of pages
        int totalPages = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "StampPDF.pdf").NumberOfPages;

        // Create formatted text for page number
        var formattedText = new Aspose.Pdf.Facades.FormattedText($"Page # of {totalPages}",
            System.Drawing.Color.AntiqueWhite,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.TimesBoldItalic,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            false, 12);

        // Set starting number for first page; you might want to start from 2 or more
        fileStamp.StartingNumber = 1;
        // Add page number in upper right corner
        fileStamp.AddPageNumber(formattedText, (int)PageNumPosition.PosUpperRight);

        // Save PDF document
        fileStamp.Save(dataDir + "AddPageNumber_out.pdf");
    }
}

// Add PDF Page Numbers
public enum PageNumPosition
{
    PosBottomMiddle, PosBottomRight, PosUpperRight, PosSidesRight, PosUpperMiddle, PosBottomLeft, PosSidesLeft, PosUpperLeft
}
```

### 自定义编号样式

PdfFileStamp 类提供了将页码信息作为印章对象添加到 PDF 文档中的功能。在此版本之前，该类仅支持 1,2,3,4 作为页码样式。然而，一些客户要求在 PDF 文档中放置页码印章时使用自定义编号样式。为了满足这一要求，引入了 [NumberingStyle](https://reference.aspose.com/pdf/zh/net/aspose.pdf/numberingstyle) 属性，该属性接受来自 [NumberingStyle](https://reference.aspose.com/pdf/zh/net/aspose.pdf/numberingstyle) 枚举的值。以下是该枚举中提供的值。

- 小写字母。
- 大写字母。
- 阿拉伯数字。
- 小写罗马数字。
- 大写罗马数字。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddCustomPageNumberInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "StampPDF.pdf");

        // Get total number of pages
        int totalPages = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "StampPDF.pdf").NumberOfPages;

        // Create formatted text for page number
        var formattedText = new Aspose.Pdf.Facades.FormattedText($"Page # of {totalPages}",
            System.Drawing.Color.AntiqueWhite,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.TimesBoldItalic,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            false, 12);

        // Specify numbering style as Numerals Roman UpperCase
        fileStamp.NumberingStyle = Aspose.Pdf.NumberingStyle.NumeralsRomanUppercase;

        // Set starting number for first page; you might want to start from 2 or more
        fileStamp.StartingNumber = 1;

        // Add page number in upper right corner
        fileStamp.AddPageNumber(formattedText, (int)PageNumPosition.PosUpperRight);

        // Save PDF document
        fileStamp.Save(dataDir + "AddCustomPageNumber_out.pdf");
    }
}

// Add PDF Page Numbers
public enum PageNumPosition
{
    PosBottomMiddle, PosBottomRight, PosUpperRight, PosSidesRight, PosUpperMiddle, PosBottomLeft, PosSidesLeft, PosUpperLeft
}
```