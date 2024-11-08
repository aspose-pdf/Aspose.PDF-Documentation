---
title: 이미지 배치 작업하기
linktitle: 이미지 배치 작업하기
type: docs
weight: 50
url: /ko/net/working-with-image-placement/
description: 이 섹션은 C# 라이브러리를 사용하여 PDF 파일에서 이미지 배치 작업의 기능에 대해 설명합니다.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "이미지 배치 작업하기",
    "alternativeHeadline": "PDF 파일에서 이미지의 위치를 얻는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "PDF, C#, PDF에서 이미지 배치",
    "wordcount": "302",
    "proficiencyLevel":"초보자",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/working-with-image-placement/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-image-placement/"
    },
    "dateModified": "2022-02-04",
    "description": "이 섹션은 C# 라이브러리를 사용하여 PDF 파일에서 이미지 배치 작업의 기능에 대해 설명합니다."
}
</script>
Aspose.PDF for .NET 7.0.0 버전이 출시되면서, PDF 문서에서 이미지의 해상도와 위치를 얻는 기능을 제공하는 [ImagePlacement](https://reference.aspose.com/pdf/net/aspose.pdf/imageplacement), [ImagePlacementAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf/imageplacementabsorber), [ImagePlacementCollection](https://reference.aspose.com/pdf/net/aspose.pdf/imageplacementcollection) 같은 클래스를 도입했습니다.

- ImagePlacementAbsorber는 ImagePlacement 객체 컬렉션으로 이미지 사용 검색을 수행합니다.
- ImagePlacement은 실제 이미지 배치 값을 반환하는 Resolution 및 Rectangle 멤버를 제공합니다.

다음 코드 스니펫은 새로운 그래픽 [Aspose.Drawing](/pdf/ko/net/drawing/) 인터페이스와 함께 작동합니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// 소스 PDF 문서를 로드합니다.
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir+ "ImagePlacement.pdf");
ImagePlacementAbsorber abs = new ImagePlacementAbsorber();

// 첫 페이지의 내용을 로드합니다.
doc.Pages[1].Accept(abs);
foreach (ImagePlacement imagePlacement in abs.ImagePlacements)
{
    // 이미지 속성을 가져옵니다.
    Console.Out.WriteLine("image width:" + imagePlacement.Rectangle.Width);
    Console.Out.WriteLine("image height:" + imagePlacement.Rectangle.Height);
    Console.Out.WriteLine("image LLX:" + imagePlacement.Rectangle.LLX);
    Console.Out.WriteLine("image LLY:" + imagePlacement.Rectangle.LLY);
    Console.Out.WriteLine("image horizontal resolution:" + imagePlacement.Resolution.X);
    Console.Out.WriteLine("image vertical resolution:" + imagePlacement.Resolution.Y);

    // 실제 크기의 이미지를 검색합니다.
    Bitmap scaledImage;
    using (MemoryStream imageStream = new MemoryStream())
    {
        // 리소스에서 이미지를 검색합니다.
        imagePlacement.Image.Save(imageStream, System.Drawing.Imaging.ImageFormat.Png);
        Bitmap resourceImage = (Bitmap)Bitmap.FromStream(imageStream);
        // 실제 크기의 비트맵을 생성합니다.
        scaledImage = new Bitmap(resourceImage, (int)imagePlacement.Rectangle.Width, (int)imagePlacement.Rectangle.Height);
    }
}
```
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
                "contactType": "영업",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "영업",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "영업",
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
    "applicationCategory": ".NET을 위한 PDF 조작 라이브러리",
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
```

