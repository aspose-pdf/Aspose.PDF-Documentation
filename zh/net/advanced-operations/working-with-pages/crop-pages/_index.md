---
title: 以编程方式裁剪 PDF 页面 C#
linktitle: 裁剪页面
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /zh/net/crop-pages/
description: 您可以使用 Aspose.PDF for .NET 获取页面属性，例如宽度、高度、出血框、裁剪框和修整框。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Crop PDF Pages programmatically C#",
    "alternativeHeadline": "Crop PDF Pages Easily with Aspose.PDF for .NET",
    "abstract": "Aspose.PDF for .NET 引入了一项强大的新功能，允许开发人员以编程方式访问和操作 PDF 的各种页面属性，包括媒体框、出血框、修整框、艺术框和裁剪框。此功能简化了自定义 PDF 布局的过程，确保文档呈现的精确性，并提高打印质量，同时最小化白边。通过易于使用的代码片段，用户可以将这些功能无缝集成到他们的应用程序中，从而改善 PDF 管理和操作。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "911",
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
    "url": "/net/crop-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/crop-pages/"
    },
    "dateModified": "2025-04-10",
    "description": "您可以使用 Aspose.PDF for .NET 获取页面属性，例如宽度、高度、出血框、裁剪框和修整框。"
}
</script>

## 获取页面属性

每个 PDF 文件中的页面都有多个属性，例如宽度、高度、出血框、裁剪框和修整框。Aspose.PDF 允许您访问这些属性。

- **媒体框**：媒体框是最大的页面框。它对应于在将文档打印为 PostScript 或 PDF 时选择的页面大小（例如 A4、A5、美国信纸等）。换句话说，媒体框决定了 PDF 文档显示或打印的介质的物理大小。
- **出血框**：如果文档有出血，PDF 也将有一个出血框。出血是指超出页面边缘的颜色（或艺术作品）量。它用于确保在文档打印并裁剪到大小（“修整”）时，墨水会一直延伸到页面边缘。即使页面被错误裁剪 - 稍微偏离修整标记 - 页面上也不会出现白边。
- **修整框**：修整框指的是文档在打印和修整后最终的大小。
- **艺术框**：艺术框是围绕文档中实际内容绘制的框。此页面框在将 PDF 文档导入其他应用程序时使用。
- **裁剪框**：裁剪框是您的 PDF 文档在 Adobe Acrobat 中显示的“页面”大小。在正常视图中，只有裁剪框的内容会在 Adobe Acrobat 中显示。有关这些属性的详细描述，请阅读 Adobe.Pdf 规范，特别是 10.10.1 页面边界。
- **Page.Rect**：媒体框和出血框的交集（通常可见的矩形）。下图说明了这些属性。
有关更多详细信息，请访问 [此页面](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html)。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

下面的代码片段展示了如何裁剪页面：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CropPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "CropPageInput.pdf"))
    {
        Console.WriteLine(document.Pages[1].CropBox);
        Console.WriteLine(document.Pages[1].TrimBox);
        Console.WriteLine(document.Pages[1].ArtBox);
        Console.WriteLine(document.Pages[1].BleedBox);
        Console.WriteLine(document.Pages[1].MediaBox);
        // Create new Box rectangle
        var newBox = new Rectangle(200, 220, 2170, 1520);
        document.Pages[1].CropBox = newBox;
        document.Pages[1].TrimBox = newBox;
        document.Pages[1].ArtBox = newBox;
        document.Pages[1].BleedBox = newBox;
        // Save PDF document
        document.Save(dataDir + "CropPage_out.pdf");  
    }
}
```

在此示例中，我们使用了一个示例文件 [这里](crop_page.pdf)。最初我们的页面看起来如图 1 所示。

更改后，页面将看起来像图 2。

### 修整页面周围的白边

例如，您可以使用任何可以加载位图的图形库修整页面周围的白边：

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void TrimWhiteSpaceAroundPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TrimWhiteSpaceAroundPage.pdf"))
    {
        var device = new Aspose.Pdf.Devices.PngDevice(new Resolution(300));

        using (var imageStr = new MemoryStream())
        {
            // Convert page to PNG image
            device.Process(document.Pages[1], imageStr);
            using (var pageBitmap = new Bitmap(imageStr))
            {
                document.Pages[1].CropBox = GetNewCropBox(pageBitmap, document.Pages[1].CropBox);
            }
        }
        // Save PDF document
        document.Save(dataDir + "TrimWhiteSpaceAroundPage_out.pdf");
    }
}

// Determine white areas with System.Drawing
private static Aspose.Pdf.Rectangle GetNewCropBox(Bitmap pageBitmap, Aspose.Pdf.Rectangle prevCropBox)
{
    var imageBitmapData = pageBitmap.LockBits(new Rectangle(0, 0, pageBitmap.Width, pageBitmap.Height),
                            ImageLockMode.ReadOnly, PixelFormat.Format32bppRgb);

    int toHeight = pageBitmap.Height;
    int toWidth = pageBitmap.Width;

    int? leftNonWhite = null;
    int? rightNonWhite = null;
    int? topNonWhite = null;
    int? bottomNonWhite = null;

    var imageRowBytes = new byte[imageBitmapData.Stride];
    for (int y = 0; y < toHeight; y++)
    {

        // Copy the row data to byte array
        if (IntPtr.Size == 4)
        {
            Marshal.Copy(new IntPtr(imageBitmapData.Scan0.ToInt32() + y * imageBitmapData.Stride), imageRowBytes, 0, imageBitmapData.Stride);
        }
        else
        {
            Marshal.Copy(new IntPtr(imageBitmapData.Scan0.ToInt64() + y * imageBitmapData.Stride), imageRowBytes, 0, imageBitmapData.Stride);
        }

        int? leftNonWhite_row = null;
        int? rightNonWhite_row = null;

        for (int x = 0; x < toWidth; x++)
        {
            if (imageRowBytes[x * 4] != 255
                || imageRowBytes[x * 4 + 1] != 255
                || imageRowBytes[x * 4 + 2] != 255)
            {
                if (leftNonWhite_row == null)
                {
                    leftNonWhite_row = x;
                }

                rightNonWhite_row = x;
            }
        }

        if (leftNonWhite_row != null || rightNonWhite_row != null)
        {
            if (topNonWhite == null)
            {
                topNonWhite = y;
            }

            bottomNonWhite = y;
        }

        if (leftNonWhite_row != null
            && (leftNonWhite == null || leftNonWhite > leftNonWhite_row))
        {
            leftNonWhite = leftNonWhite_row;
        }
        if (rightNonWhite_row != null
            && (rightNonWhite == null || rightNonWhite < rightNonWhite_row))
        {
            rightNonWhite = rightNonWhite_row;
        }
    }

    leftNonWhite = leftNonWhite ?? 0;
    rightNonWhite = rightNonWhite ?? toWidth;
    topNonWhite = topNonWhite ?? 0;
    bottomNonWhite = bottomNonWhite ?? toHeight;

    double xCoef = prevCropBox.Width / toWidth;
    double yCoef = prevCropBox.Height / toHeight;

    pageBitmap.UnlockBits(imageBitmapData);
    
    // Create crop box with correction to previous crop box
    return
        new Aspose.Pdf.Rectangle(
            leftNonWhite.Value * xCoef + prevCropBox.LLX,
            (toHeight * yCoef + prevCropBox.LLY) - bottomNonWhite.Value * yCoef,
            rightNonWhite.Value * xCoef + prevCropBox.LLX,
            (toHeight * yCoef + prevCropBox.LLY) - topNonWhite.Value * yCoef
        );
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void TrimWhiteSpaceAroundPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "TrimWhiteSpaceAroundPage.pdf");
    var device = new Aspose.Pdf.Devices.PngDevice(new Resolution(300));

    using var imageStr = new MemoryStream();

    // Convert page to PNG image
    device.Process(document.Pages[1], imageStr);
    using var pageBitmap = new Bitmap(imageStr);
    document.Pages[1].CropBox = GetNewCropBox(pageBitmap, document.Pages[1].CropBox);

    // Save PDF document
    document.Save(dataDir + "TrimWhiteSpaceAroundPage_out.pdf");
}

// Determine white areas with System.Drawing
private static Aspose.Pdf.Rectangle GetNewCropBox(Bitmap pageBitmap, Aspose.Pdf.Rectangle prevCropBox)
{
    var imageBitmapData = pageBitmap.LockBits(new Rectangle(0, 0, pageBitmap.Width, pageBitmap.Height),
                            ImageLockMode.ReadOnly, PixelFormat.Format32bppRgb);

    int toHeight = pageBitmap.Height;
    int toWidth = pageBitmap.Width;

    int? leftNonWhite = null;
    int? rightNonWhite = null;
    int? topNonWhite = null;
    int? bottomNonWhite = null;

    var imageRowBytes = new byte[imageBitmapData.Stride];
    for (int y = 0; y < toHeight; y++)
    {

        // Copy the row data to byte array
        if (IntPtr.Size == 4)
        {
            Marshal.Copy(new IntPtr(imageBitmapData.Scan0.ToInt32() + y * imageBitmapData.Stride), imageRowBytes, 0, imageBitmapData.Stride);
        }
        else
        {
            Marshal.Copy(new IntPtr(imageBitmapData.Scan0.ToInt64() + y * imageBitmapData.Stride), imageRowBytes, 0, imageBitmapData.Stride);
        }

        int? leftNonWhite_row = null;
        int? rightNonWhite_row = null;

        for (int x = 0; x < toWidth; x++)
        {
            if (imageRowBytes[x * 4] != 255
                || imageRowBytes[x * 4 + 1] != 255
                || imageRowBytes[x * 4 + 2] != 255)
            {
                if (leftNonWhite_row == null)
                {
                    leftNonWhite_row = x;
                }

                rightNonWhite_row = x;
            }
        }

        if (leftNonWhite_row != null || rightNonWhite_row != null)
        {
            if (topNonWhite == null)
            {
                topNonWhite = y;
            }

            bottomNonWhite = y;
        }

        if (leftNonWhite_row != null
            && (leftNonWhite == null || leftNonWhite > leftNonWhite_row))
        {
            leftNonWhite = leftNonWhite_row;
        }
        if (rightNonWhite_row != null
            && (rightNonWhite == null || rightNonWhite < rightNonWhite_row))
        {
            rightNonWhite = rightNonWhite_row;
        }
    }

    leftNonWhite = leftNonWhite ?? 0;
    rightNonWhite = rightNonWhite ?? toWidth;
    topNonWhite = topNonWhite ?? 0;
    bottomNonWhite = bottomNonWhite ?? toHeight;

    double xCoef = prevCropBox.Width / toWidth;
    double yCoef = prevCropBox.Height / toHeight;

    pageBitmap.UnlockBits(imageBitmapData);
    
    // Create crop box with correction to previous crop box
    return
        new Aspose.Pdf.Rectangle(
            leftNonWhite.Value * xCoef + prevCropBox.LLX,
            (toHeight * yCoef + prevCropBox.LLY) - bottomNonWhite.Value * yCoef,
            rightNonWhite.Value * xCoef + prevCropBox.LLX,
            (toHeight * yCoef + prevCropBox.LLY) - topNonWhite.Value * yCoef
        );
}
```
{{< /tab >}}
{{< /tabs >}}

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