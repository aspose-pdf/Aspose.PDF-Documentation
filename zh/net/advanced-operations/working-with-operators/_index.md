---
title: 使用操作符
linktitle: 使用操作符
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 90
url: /zh/net/working-with-operators/
description: 本主题解释了如何与 Aspose.PDF 一起使用操作符。操作符类为 PDF 操作提供了很好的功能。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Operators",
    "alternativeHeadline": "Empowered PDF Manipulation with Operators Integration",
    "abstract": "操作符功能在 Aspose.PDF for .NET 中增强了 PDF 操作能力，允许用户利用特定的操作符类进行添加图像和移除图形等任务。此功能简化了在 PDF 中定义图形元素及其状态的过程，为开发人员提供了强大的工具，以便进行精细的文档编辑和处理",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "operators, Aspose.PDF, PDF manipulation, GSave operator, ConcatenateMatrix operator, Do operator, GRestore operator, graphics state, remove graphics",
    "wordcount": "1233",
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
    "url": "/net/working-with-operators/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-operators/"
    },
    "dateModified": "2024-11-26",
    "description": "本主题解释了如何与 Aspose.PDF 一起使用操作符。操作符类为 PDF 操作提供了很好的功能。"
}
</script>

## PDF 操作符及其使用简介

操作符是一个 PDF 关键字，指定要执行的某些操作，例如在页面上绘制图形形状。操作符关键字通过缺少初始斜杠字符 (2Fh) 与命名对象区分。操作符仅在内容流内有意义。

内容流是一个 PDF 流对象，其数据由描述要在页面上绘制的图形元素的指令组成。有关 PDF 操作符的更多详细信息，请参见 [PDF 规范](https://opensource.adobe.com/dc-acrobat-sdk-docs/)。

### 实现细节

本主题解释了如何与 Aspose.PDF 一起使用操作符。所选示例将图像添加到 PDF 文件中以说明该概念。要在 PDF 文件中添加图像，需要不同的操作符。此示例使用 [GSave](https://reference.aspose.com/pdf/net/aspose.pdf.ioperatorselector/visit/methods/28)、[ConcatenateMatrix](https://reference.aspose.com/pdf/net/aspose.pdf.ioperatorselector/visit/methods/10)、[Do](https://reference.aspose.com/pdf/net/aspose.pdf.ioperatorselector/visit/methods/14) 和 [GRestore](https://reference.aspose.com/pdf/net/aspose.pdf.ioperatorselector/visit/methods/26)。

- **GSave** 操作符保存 PDF 的当前图形状态。
- **ConcatenateMatrix**（连接矩阵）操作符用于定义图像在 PDF 页面上的放置方式。
- **Do** 操作符在页面上绘制图像。
- **GRestore** 操作符恢复图形状态。

要在 PDF 文件中添加图像：

1. 创建一个 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 对象并打开输入 PDF 文档。
1. 获取要添加图像的特定页面。
1. 将图像添加到页面的资源集合中。
1. 使用操作符将图像放置在页面上：
   - 首先，使用 GSave 操作符保存当前图形状态。
   - 然后使用 ConcatenateMatrix 操作符指定图像要放置的位置。
   - 使用 Do 操作符在页面上绘制图像。
1. 最后，使用 GRestore 操作符保存更新后的图形状态。

以下代码片段还可以与 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库一起使用。

以下代码片段演示了如何使用 PDF 操作符。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageUsingPDFOperators()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFOperators.pdf"))
    {
        // Set coordinates for the image placement
        int lowerLeftX = 100;
        int lowerLeftY = 100;
        int upperRightX = 200;
        int upperRightY = 200;

        // Get the page where the image needs to be added
        var page = document.Pages[1];

        // Load the image into a file stream
        using (var imageStream = new FileStream(dataDir + "PDFOperators.jpg", FileMode.Open))
        {
            // Add the image to the page's Resources collection
            page.Resources.Images.Add(imageStream);
        }

        // Save the current graphics state using the GSave operator
        page.Contents.Add(new Aspose.Pdf.Operators.GSave());

        // Create a rectangle and matrix for positioning the image
        var rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        var matrix = new Aspose.Pdf.Matrix(new double[]
        {
            rectangle.URX - rectangle.LLX, 0,
            0, rectangle.URY - rectangle.LLY,
            rectangle.LLX, rectangle.LLY
        });

        // Define how the image must be placed using the ConcatenateMatrix operator
        page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));

        // Get the image from the Resources collection
        var ximage = page.Resources.Images[page.Resources.Images.Count];

        // Draw the image using the Do operator
        page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));

        // Restore the graphics state using the GRestore operator
        page.Contents.Add(new Aspose.Pdf.Operators.GRestore());

        // Save PDF document
        document.Save(dataDir + "PDFOperators_out.pdf");
    }
}
```

## 使用操作符在页面上绘制 XForm

本主题演示了如何使用 GSave/GRestore 操作符、ConcatenateMatrix 操作符来定位 xForm，以及使用 Do 操作符在页面上绘制 xForm。

下面的代码使用 GSave/GRestore 操作符对 PDF 文件的现有内容进行包装。这种方法有助于在现有内容的末尾获取初始图形状态。如果没有这种方法，可能会在现有操作符链的末尾留下不必要的变换。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DrawXFormOnPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DrawXFormOnPage.pdf"))
    {
        var pageContents = document.Pages[1].Contents;

        // Wrap existing contents with GSave/GRestore operators to preserve graphics state
        pageContents.Insert(1, new Aspose.Pdf.Operators.GSave());
        pageContents.Add(new Aspose.Pdf.Operators.GRestore());

        // Add GSave operator to start new graphics state
        pageContents.Add(new Aspose.Pdf.Operators.GSave());

        // Create an XForm
        var form = Aspose.Pdf.XForm.CreateNewForm(document.Pages[1], document);
        document.Pages[1].Resources.Forms.Add(form);

        form.Contents.Add(new Aspose.Pdf.Operators.GSave());
        // Define image width and height
        form.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(200, 0, 0, 200, 0, 0));

        // Load image into stream
        using (var imageStream = new FileStream(dataDir + "aspose-logo.jpg", FileMode.Open))
        {
            // Add the image to the XForm's resources
            form.Resources.Images.Add(imageStream);
        }

        var ximage = form.Resources.Images[form.Resources.Images.Count];
        // Draw the image on the XForm
        form.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));
        form.Contents.Add(new Aspose.Pdf.Operators.GRestore());

        // Place and draw the XForm at two different coordinates

        // Draw the XForm at (100, 500)
        pageContents.Add(new Aspose.Pdf.Operators.GSave());
        pageContents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 100, 500));
        pageContents.Add(new Aspose.Pdf.Operators.Do(form.Name));
        pageContents.Add(new Aspose.Pdf.Operators.GRestore());

        // Draw the XForm at (100, 300)
        pageContents.Add(new Aspose.Pdf.Operators.GSave());
        pageContents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 100, 300));
        pageContents.Add(new Aspose.Pdf.Operators.Do(form.Name));
        pageContents.Add(new Aspose.Pdf.Operators.GRestore());

        // Restore graphics state
        pageContents.Add(new Aspose.Pdf.Operators.GRestore());

        // Save PDF document
        document.Save(dataDir + "DrawXFormOnPage_out.pdf");
    }
}
```

## 使用操作符类移除图形对象

操作符类为 PDF 操作提供了很好的功能。当 PDF 文件包含无法使用 [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 类的 [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteimage) 方法移除的图形时，可以使用操作符类来移除它们。

以下代码片段演示了如何移除图形。请注意，如果 PDF 文件包含图形的文本标签，它们可能会在 PDF 文件中保留，因此请搜索图形操作符以找到删除此类图像的替代方法。

```csharp
  // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
  private static void RemoveGraphicsObjects()
  {
      // The path to the documents directory
      var dataDir = RunExamples.GetDataDir_AsposePdf();

      // Open PDF document
      using (var document = new Aspose.Pdf.Document(dataDir + "RemoveGraphicsObjects.pdf"))
      {
          // Get the specific page (page 2 in this case)
          var page = document.Pages[2];

          // Get the operator collection from the page contents
          var oc = page.Contents;

          // Define the path-painting operators to be removed
          var operators = new Aspose.Pdf.Operator[]
          {
              new Aspose.Pdf.Operators.Stroke(),
              new Aspose.Pdf.Operators.ClosePathStroke(),
              new Aspose.Pdf.Operators.Fill()
          };

          // Delete the specified operators from the page contents
          oc.Delete(operators);

          // Save PDF document
          document.Save(dataDir + "NoGraphics_out.pdf");
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