---
title: PDF 페이지 자르기 프로그래밍 C#
linktitle: 페이지 자르기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /ko/net/crop-pages/
description: Aspose.PDF for .NET를 사용하여 너비, 높이, 여백, 자르기 및 트림 박스와 같은 페이지 속성을 가져올 수 있습니다.
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
    "abstract": "Aspose.PDF for .NET는 개발자가 PDF의 다양한 페이지 속성에 프로그래밍 방식으로 접근하고 조작할 수 있는 강력한 새로운 기능을 소개합니다. 여기에는 미디어 박스, 여백 박스, 트림 박스, 아트 박스 및 자르기 박스가 포함됩니다. 이 기능은 PDF 레이아웃을 사용자 정의하는 프로세스를 간소화하여 문서 프레젠테이션의 정확성을 보장하고 인쇄 품질을 향상시키며 흰색 가장자리를 최소화합니다. 사용하기 쉬운 코드 스니펫을 통해 사용자는 이러한 기능을 애플리케이션에 원활하게 통합하여 PDF 관리 및 조작을 개선할 수 있습니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1079",
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
    "description": "Aspose.PDF for .NET를 사용하여 너비, 높이, 여백, 자르기 및 트림 박스와 같은 페이지 속성을 가져올 수 있습니다."
}
</script>

## 페이지 속성 가져오기

PDF 파일의 각 페이지는 너비, 높이, 여백, 자르기 및 트림 박스와 같은 여러 속성을 가지고 있습니다. Aspose.PDF를 사용하면 이러한 속성에 접근할 수 있습니다.

- **미디어 박스**: 미디어 박스는 가장 큰 페이지 박스입니다. 이는 문서가 PostScript 또는 PDF로 인쇄될 때 선택된 페이지 크기(예: A4, A5, US Letter 등)에 해당합니다. 즉, 미디어 박스는 PDF 문서가 표시되거나 인쇄되는 매체의 물리적 크기를 결정합니다.
- **여백 박스**: 문서에 여백이 있는 경우 PDF에도 여백 박스가 있습니다. 여백은 페이지의 가장자리를 넘어 확장되는 색상(또는 아트워크)의 양입니다. 이는 문서가 인쇄되고 크기에 맞게 잘릴 때("트림") 잉크가 페이지의 가장자리까지 가도록 보장하는 데 사용됩니다. 페이지가 잘못 잘리더라도 - 트림 마크에서 약간 벗어나 잘리더라도 - 페이지에 흰색 가장자가 나타나지 않습니다.
- **트림 박스**: 트림 박스는 인쇄 및 트림 후 문서의 최종 크기를 나타냅니다.
- **아트 박스**: 아트 박스는 문서의 페이지에 실제 내용 주위에 그려진 박스입니다. 이 페이지 박스는 다른 애플리케이션에서 PDF 문서를 가져올 때 사용됩니다.
- **자르기 박스**: 자르기 박스는 PDF 문서가 Adobe Acrobat에서 표시되는 "페이지" 크기입니다. 일반 보기에서는 Adobe Acrobat에서 자르기 박스의 내용만 표시됩니다. 이러한 속성에 대한 자세한 설명은 Adobe.Pdf 사양, 특히 10.10.1 페이지 경계를 참조하십시오.
- **Page.Rect**: 미디어 박스와 드롭 박스의 교차점(일반적으로 보이는 사각형)입니다. 아래 그림은 이러한 속성을 설명합니다.
자세한 내용은 [이 페이지](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html)를 방문하십시오.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

아래 스니펫은 페이지를 자르는 방법을 보여줍니다:

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

이 예제에서는 샘플 파일을 [여기](crop_page.pdf)에서 사용했습니다. 처음에 우리의 페이지는 그림 1과 같이 보입니다.

변경 후 페이지는 그림 2와 같이 보일 것입니다.

### 페이지 주위의 흰색 공간 자르기

예를 들어, 비트맵을 로드할 수 있는 그래픽 라이브러리를 사용하여 페이지 주위의 흰색 공간을 자를 수 있습니다:

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
        var device = new Aspose.Pdf.Devices.PngDevice(new Aspose.Pdf.Devices.Resolution(300));

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
    var device = new Aspose.Pdf.Devices.PngDevice(new Aspose.Pdf.Devices.Resolution(300));

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