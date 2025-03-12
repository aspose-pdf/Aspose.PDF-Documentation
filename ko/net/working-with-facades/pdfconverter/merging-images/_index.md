---
title: 이미지 병합
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ko/net/merge-images/
description: Aspose.PDF를 사용하여 .NET에서 이미지를 단일 PDF 문서로 병합하는 방법을 알아보세요.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Merge images",
    "alternativeHeadline": "Merge Images with Flexible Formats and Arrangements",
    "abstract": "Aspose.PDF for .NET은 사용자가 이미지를 원활하게 병합할 수 있는 강력한 새로운 기능을 소개합니다. 이 기능은 수직, 수평 또는 중앙 정렬과 같은 다양한 형식과 스타일로 이미지를 결합할 수 있으며, 최종 출력을 매우 다재다능한 TIFF 형식으로 저장할 수 있는 옵션도 제공합니다. 문서 프레젠테이션을 향상시키기에 이상적이며, 이 기능은 간단한 코드 통합을 사용하여 병합된 이미지 파일을 생성하는 과정을 단순화합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "482",
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
    "url": "/net/merge-images/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/merge-images/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

Aspose.PDF 21.4는 이미지를 결합할 수 있습니다. [Merge Images](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/mergeimages) 메서드는 특정 폴더의 내용을 확인하고 그 안의 지정된 유형의 파일로 작업합니다. 이미지를 병합할 때 'inputImagesStreams', 이미지 형식 및 이미지 병합 모드(예: 수직)를 지정합니다. 그런 다음 결과를 FileOutputStream에 저장합니다.

다음 코드 스니펫을 따라 작업을 해결하세요:

## 이미지 병합

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MergeImages01()
{
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();  // Updated to use dynamic path
    // Get all image files matching the pattern "MergeImages*.jpg"
    var fileStreams = Directory.GetFiles(dataDir, "MergeImages*.jpg")
                                .OrderBy(f => f)
                                .Select(f => File.OpenRead(f))
                                .Cast<Stream>()
                                .ToList();

    using (Stream inputStream = Aspose.Pdf.Facades.PdfConverter.MergeImages(fileStreams, Aspose.Pdf.Drawing.ImageFormat.Jpeg, ImageMergeMode.Vertical, 1, 1))
    using (FileStream outputStream = new FileStream(dataDir + "MergeImages_out.jpg", FileMode.Create))
    {
        // Copy merged images to the output file
        inputStream.CopyTo(outputStream);
    }
}
```

두 번째 예제는 이전 예제와 동일하게 작동하지만 병합된 이미지는 수평으로 저장됩니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MergeImages02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Get all image files matching the pattern "MergeImages*.jpg"
    var fileStreams = Directory.GetFiles(dataDir, "MergeImages*.jpg")
                            .OrderBy(f => f)
                            .Select(f => File.OpenRead(f))
                            .Cast<Stream>()
                            .ToList();

    using (Stream inputStream =
            Aspose.Pdf.Facades.PdfConverter.MergeImages(fileStreams, Aspose.Pdf.Drawing.ImageFormat.Jpeg, ImageMergeMode.Horizontal, 1, 1))
    using (FileStream outputStream = new FileStream(dataDir + "MergeImages02_out.jpg", FileMode.Create))
    {
        // Copy merged images to the output file
        inputStream.CopyTo(outputStream);
    }
}
```

세 번째 예제에서는 이미지를 중앙에 배치하여 병합합니다. 두 개는 수평으로, 두 개는 수직으로 배치합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MergeImages03()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Get all image files matching the pattern "MergeImages*.jpg"
    var fileStreams = Directory.GetFiles(dataDir, "MergeImages*.jpg")
                            .OrderBy(f => f)
                            .Select(f => File.OpenRead(f))
                            .Cast<Stream>()
                            .ToList();

    using (Stream inputStream =
            Aspose.Pdf.Facades.PdfConverter.MergeImages(fileStreams, Aspose.Pdf.Drawing.ImageFormat.Jpeg, ImageMergeMode.Center, 2, 2))
    using (FileStream outputStream = new FileStream(dataDir + "MergeImages03_out.jpg", FileMode.Create))
    {
        // Copy merged images to the output file
        inputStream.CopyTo(outputStream);
    }
}
```

또한, Aspose.PDF for Java는 이미지를 결합하고 [MergeImagesAsTiff Method](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#saveAsTIFF-java.io.OutputStream-)를 사용하여 TIFF 형식으로 저장할 수 있는 기회를 제공합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MergeImages04()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Get all image files matching the pattern "MergeImages*.jpg"
    var fileStreams = Directory.GetFiles(dataDir, "MergeImages*.jpg")
                            .OrderBy(f => f)
                            .Select(f => File.OpenRead(f))
                            .Cast<Stream>()
                            .ToList();

    using (Stream inputStream =
            Aspose.Pdf.Facades.PdfConverter.MergeImagesAsTiff(fileStreams))
    using (FileStream outputStream = new FileStream(dataDir + "MergeImages_out.tiff", FileMode.Create))
    {
        // Copy merged images to the output file
        inputStream.CopyTo(outputStream);
    }
}
```

병합된 이미지를 PDF 페이지의 하나의 이미지로 저장하려면 imageStream에 배치하고 addImage 메서드를 사용하여 페이지에 결과를 배치합니다. 이때 이미지를 배치할 좌표를 지정합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MergeImages05()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Get all image files matching the pattern "MergeImages*.jpg"
    var fileStreams = Directory.GetFiles(dataDir, "MergeImages*.jpg")
                                .OrderBy(f => f)
                                .Select(f => File.OpenRead(f))
                                .Cast<Stream>()
                                .ToList();

    using (Stream inputStream =
            Aspose.Pdf.Facades.PdfConverter.MergeImages(fileStreams, Aspose.Pdf.Drawing.ImageFormat.Jpeg, ImageMergeMode.Vertical, 1, 1))
    using (MemoryStream outputStream = new MemoryStream())  // Output to MemoryStream
    {
        // Copy merged images to the MemoryStream
        inputStream.CopyTo(outputStream);

        // Create PDF document
        using (var document = new Aspose.Pdf.Document())
        {
            // Add page
            var page = document.Pages.Add();

            // Add the image from the MemoryStream to the page
            page.AddImage(outputStream, new Aspose.Pdf.Rectangle(10, 120, 400, 720));

            // Save PDF document
            document.Save(dataDir + "MergeImages_out.pdf");
        }
    }
}
```