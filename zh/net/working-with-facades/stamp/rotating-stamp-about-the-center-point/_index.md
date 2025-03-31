---
title: 关于中心点旋转印章
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /zh/net/rotating-stamp-about-the-center-point/
description: 本节解释如何使用印章类围绕中心点旋转印章。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Rotating stamp about the center point",
    "alternativeHeadline": "Rotate Stamps Precisely Around Their Center Point",
    "abstract": "Aspose.PDF for .NET中的功能允许用户在PDF文件中精确地围绕其中心点旋转印章。利用印章类，开发人员可以轻松设置从0到360度的旋转值，增强文档中水印位置的灵活性和自定义。这一功能非常适合创建具有个性化印章方向的视觉动态PDF。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "339",
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
    "url": "/net/rotating-stamp-about-the-center-point/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/rotating-stamp-about-the-center-point/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一节以获取高级用户和开发人员的信息。"
}
</script>

{{% alert color="primary" %}}

[Aspose.Pdf.Facades命名空间](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades) 在 [Aspose.PDF for .NET](/pdf/zh/net/) 中允许您在现有PDF文件中添加印章。有时，用户确实需要旋转印章。在本文中，我们将看到如何围绕其中心点旋转印章。

{{% /alert %}}

## 实现细节

[印章](https://reference.aspose.com/pdf/zh/net/aspose.pdf/stamp) 类允许您在PDF文件中添加水印。您可以使用 [BindImage](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades.stamp/bindimage/methods/1) 方法指定要作为印章添加的图像。[SetOrigin](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/stamp/methods/setorigin) 方法允许您设置添加的印章的原点；该原点是印章的左下角坐标。您还可以使用 [SetImageSize](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/stamp/methods/setimagesize) 方法设置图像的大小。

现在，我们来看一下如何围绕印章的中心旋转印章。[印章](https://reference.aspose.com/pdf/zh/net/aspose.pdf/stamp) 类提供了一个名为 Rotation 的属性。该属性设置或获取印章内容的旋转角度，范围从0到360。我们可以指定从0到360的任何旋转值。通过指定旋转值，我们可以围绕其中心点旋转印章。如果一个印章是印章类型的对象，则可以指定旋转值为 aStamp.Rotation = 90。在这种情况下，印章将围绕印章内容的中心旋转90度。以下代码片段向您展示了如何围绕中心点旋转印章：


```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddRotatingStampToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();  

    // Create PdfFileInfo object to get height and width of the pages
    using (var fileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "RotatingStamp.pdf"))
    {
        // Create Stamp object
        var aStamp = new Aspose.Pdf.Facades.Stamp();

        // Bind image file with the Stamp object
        aStamp.BindImage(dataDir + "RotatingStamp.jpg");

        // Specify whether the stamp will be added as a background or not
        aStamp.IsBackground = false;

        // Specifies at which pages to add the watermark
        aStamp.Pages = new int[] { 1 };

        // Specifies the watermark rotation - rotate at 90 degrees
        aStamp.Rotation = 90;

        // Specifies the position of stamp - lower left corner of the stamp
        aStamp.SetOrigin(fileInfo.GetPageWidth(1) / 2, fileInfo.GetPageHeight(1) / 2);

        // Set the size of the watermark
        aStamp.SetImageSize(100, 100);

        // Open PDF document
        using (var document = new Aspose.Pdf.Document(dataDir + "RotatingStamp_out.pdf"))
        {
            // Create PdfFileStamp class to bind input and output files
            using (var stamper = new Aspose.Pdf.Facades.PdfFileStamp(document))
            {
                // Add the stamp in the PDF file
                stamper.AddStamp(aStamp);
            }
        }
    }
}
```