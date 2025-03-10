---
title: 获取图像的分辨率和尺寸
linktitle: 获取分辨率和尺寸
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /zh/net/get-resolution-and-dimensions-of-embedded-images/
description: 学习如何使用 Aspose.PDF 在 .NET 中检索 PDF 中嵌入图像的分辨率和尺寸。
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get Resolution and Dimensions of Images",
    "alternativeHeadline": "Extract Image Resolution and Dimensions Efficiently",
    "abstract": "发现如何高效地获取 PDF 文档中嵌入图像的分辨率和尺寸，使用 Aspose.PDF 库。此功能允许开发人员直接访问图像属性，而无需提取，从而简化 PDF 文件中图像操作的过程，同时增强对图像数据的功能和控制。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Get Resolution, Dimensions of Images, Embedded Images, Aspose.PDF.Drawing, ArrayList, Image Placement Classes, ConcatenateMatrix, XImage, PDF Manipulation Library, Image Resolution Computation",
    "wordcount": "827",
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
    "url": "/net/get-resolution-and-dimensions-of-embedded-images/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-resolution-and-dimensions-of-embedded-images/"
    },
    "dateModified": "2024-11-26",
    "description": "本节显示获取嵌入图像的分辨率和尺寸的详细信息"
}
</script>

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

本主题解释了如何使用 Aspose.PDF 命名空间中的操作符类，这些类提供了获取图像的分辨率和尺寸信息的能力，而无需提取它们。

实现这一点有不同的方法。本文解释了如何使用 `arraylist` 和 [图像放置类](https://reference.aspose.com/pdf/net/aspose.pdf/imageplacement)。

1. 首先，加载源 PDF 文件（包含图像）。
1. 然后创建一个 ArrayList 对象来保存文档中任何图像的名称。
1. 使用 Page.Resources.Images 属性获取图像。
1. 创建一个堆栈对象来保存图像的图形状态，并使用它来跟踪不同的图像状态。
1. 创建一个 ConcatenateMatrix 对象，定义当前变换。它还支持缩放、旋转和倾斜任何内容。它将新矩阵与之前的矩阵连接。请注意，我们不能从头定义变换，只能修改现有的变换。
1. 因为我们可以使用 ConcatenateMatrix 修改矩阵，我们可能还需要恢复到原始图像状态。使用 GSave 和 GRestore 操作符。这些操作符是成对的，因此应一起调用。例如，如果您使用复杂的变换进行一些图形工作，最后将变换返回到初始状态，方法将类似于：

```csharp
// Draw some text
GSave

ConcatenateMatrix  // rotate contents after the operator

// Some graphics work

ConcatenateMatrix // scale (with previous rotation) contents after the operator

// Some other graphics work

GRestore

// Draw some text
```

结果，文本以常规形式绘制，但在文本操作符之间执行了一些变换。为了显示图像或绘制形状对象和图像，我们需要使用 Do 操作符。

我们还有一个名为 XImage 的类，它提供两个属性，Width 和 Height，可用于获取图像尺寸。

1. 执行一些计算以计算图像分辨率。
1. 在命令提示符中显示信息以及图像名称。

以下代码片段向您展示如何在不从 PDF 文档中提取图像的情况下获取图像的尺寸和分辨率。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImageInformationFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImageInformation.pdf"))
    {
        // Define the default resolution for image
        int defaultResolution = 72;
        var graphicsState = new Stack();

        // Define list which will hold image names
        var imageNames = new List<string>(document.Pages[1].Resources.Images.Names);

        // Insert an object to stack
        graphicsState.Push(new System.Drawing.Drawing2D.Matrix(1, 0, 0, 1, 0, 0));

        // Get all the operators on first page of document
        foreach (var op in document.Pages[1].Contents)
        {
            // Use GSave/GRestore operators to revert the transformations back to previously set
            var opSaveState = op as Aspose.Pdf.Operators.GSave;
            var opRestoreState = op as Aspose.Pdf.Operators.GRestore;
            var opCtm = op as Aspose.Pdf.Operators.ConcatenateMatrix;
            var opDo = op as Aspose.Pdf.Operators.Do;

            if (opSaveState != null)
            {
                // Save previous state and push current state to the top of the stack
                graphicsState.Push(((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Clone());
            }
            else if (opRestoreState != null)
            {
                // Throw away current state and restore previous one
                graphicsState.Pop();
            }
            else if (opCtm != null)
            {
                var cm = new System.Drawing.Drawing2D.Matrix(
                   (float)opCtm.Matrix.A,
                   (float)opCtm.Matrix.B,
                   (float)opCtm.Matrix.C,
                   (float)opCtm.Matrix.D,
                   (float)opCtm.Matrix.E,
                   (float)opCtm.Matrix.F);

                // Multiply current matrix with the state matrix
                ((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Multiply(cm);

                continue;
            }
            else if (opDo != null)
            {
                // In case this is an image drawing operator
                if (imageNames.Contains(opDo.Name))
                {
                    var lastCTM = (System.Drawing.Drawing2D.Matrix)graphicsState.Peek();
                    // Create XImage object to hold images of first pdf page
                    var image = document.Pages[1].Resources.Images[opDo.Name];

                    // Get image dimensions
                    double scaledWidth = Math.Sqrt(Math.Pow(lastCTM.Elements[0], 2) + Math.Pow(lastCTM.Elements[1], 2));
                    double scaledHeight = Math.Sqrt(Math.Pow(lastCTM.Elements[2], 2) + Math.Pow(lastCTM.Elements[3], 2));
                    // Get Height and Width information of image
                    double originalWidth = image.Width;
                    double originalHeight = image.Height;

                    // Compute resolution based on above information
                    double resHorizontal = originalWidth * defaultResolution / scaledWidth;
                    double resVertical = originalHeight * defaultResolution / scaledHeight;

                    // Display Dimension and Resolution information of each image
                    Console.Out.WriteLine(
                            string.Format(dataDir + "image {0} ({1:.##}:{2:.##}): res {3:.##} x {4:.##}",
                                         opDo.Name, scaledWidth, scaledHeight, resHorizontal,
                                         resVertical));
                }
            }
        }
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