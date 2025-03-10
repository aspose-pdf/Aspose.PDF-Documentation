---
title: 添加文本和图像印章
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /zh/net/add-text-and-image-stamp/
description: 本节解释如何使用 PdfFileStamp 类通过 Aspose.PDF Facades 添加文本和图像印章。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Text and Image Stamp",
    "alternativeHeadline": "Add Custom Text and Image Stamps in PDFs",
    "abstract": "添加文本和图像印章的功能使用户能够无缝地在 PDF 文档的所有或特定页面上应用自定义文本和图像印章。此功能增强了文档个性化，允许对印章属性（如位置、旋转和质量）进行详细控制，最终改善 PDF 文件的展示和品牌形象。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1435",
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
    "url": "/net/add-text-and-image-stamp/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-text-and-image-stamp/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一节以获取高级用户和开发人员的信息。"
}
</script>

## 在 PDF 文件的所有页面上添加文本印章

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 类允许您在 PDF 文件的所有页面上添加文本印章。为了添加文本印章，您首先需要创建 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 和 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 类的对象。您还需要使用 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 类的 [BindLogo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) 方法创建文本印章。您还可以使用 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 对象设置其他属性，如原点、旋转、背景等。然后，您可以使用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 类的 [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) 方法将印章添加到 PDF 文件中。最后，使用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 类的 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) 方法保存输出的 PDF 文件。以下代码片段演示了如何在 PDF 文件的所有页面上添加文本印章。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextStampOnAllPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindLogo(new Aspose.Pdf.Facades.FormattedText("Hello World!",
            System.Drawing.Color.Blue,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.Helvetica,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            true,
            14));

        stamp.SetOrigin(10, 400);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddTextStampOnAllPages_out.pdf");
    }
}
```

## 在 PDF 文件的特定页面上添加文本印章

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 类允许您在 PDF 文件的特定页面上添加文本印章。为了添加文本印章，您首先需要创建 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 和 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 类的对象。您还需要使用 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 类的 [BindLogo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) 方法创建文本印章。您还可以使用 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 对象设置其他属性，如原点、旋转、背景等。由于您想在 PDF 文件的特定页面上添加文本印章，您还需要设置 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 类的 [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) 属性。该属性需要一个整数数组，包含您想要添加印章的页面编号。然后，您可以使用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 类的 [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) 方法将印章添加到 PDF 文件中。最后，使用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 类的 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) 方法保存输出的 PDF 文件。以下代码片段演示了如何在 PDF 文件的特定页面上添加文本印章。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextStampOnParticularPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindLogo(new Aspose.Pdf.Facades.FormattedText("Hello World!",
            System.Drawing.Color.Blue,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.Helvetica,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            true,
            14));
        stamp.SetOrigin(10, 400);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Set particular pages (page 2)
        stamp.Pages = new[] { 2 };

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddTextStampOnParticularPages_out.pdf");
    }
}
```

## 在 PDF 文件的所有页面上添加图像印章

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 类允许您在 PDF 文件的所有页面上添加图像印章。为了添加图像印章，您首先需要创建 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 和 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 类的对象。您还需要使用 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 类的 [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) 方法创建图像印章。您还可以使用 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 对象设置其他属性，如原点、旋转、背景等。然后，您可以使用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 类的 [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) 方法将印章添加到 PDF 文件中。最后，使用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 类的 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) 方法保存输出的 PDF 文件。以下代码片段演示了如何在 PDF 文件的所有页面上添加图像印章。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageStampOnAllPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindImage(dataDir + "StampImage.png");
        stamp.SetOrigin(10, 200);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Set particular pages (page 2)
        stamp.Pages = new[] { 2 };

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddImageStampOnAllPages_out.pdf");
    }
}
```

### 添加印章时控制图像质量

在将图像作为印章对象添加时，您还可以控制图像的质量。为了实现这一要求，[Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 类添加了 Quality 属性。它表示图像的质量百分比（有效值为 0..100）。

## 在 PDF 文件的特定页面上添加图像印章

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 类允许您在 PDF 文件的特定页面上添加图像印章。为了添加图像印章，您首先需要创建 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 和 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 类的对象。您还需要使用 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 类的 [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) 方法创建图像印章。您还可以使用 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 对象设置其他属性，如原点、旋转、背景等。由于您想在 PDF 文件的特定页面上添加图像印章，您还需要设置 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 类的 [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) 属性。该属性需要一个整数数组，包含您想要添加印章的页面编号。然后，您可以使用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 类的 [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) 方法将印章添加到 PDF 文件中。最后，使用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 类的 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) 方法保存输出的 PDF 文件。以下代码片段演示了如何在 PDF 文件的特定页面上添加图像印章。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageStampOnParticularPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindImage(dataDir + "StampImage.png");
        stamp.SetOrigin(10, 200);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddImageStampOnParticularPages_out.pdf");
    }
}
```