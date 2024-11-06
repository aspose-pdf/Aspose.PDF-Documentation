---
title: C#을 사용한 PDF 스티키 주석
linktitle: 스티키 주석
type: docs
weight: 50
url: ko/net/sticky-annotations/
description: 이 주제는 스티키 주석에 대해 설명하며, 예로써 텍스트에서 워터마크 주석을 보여줍니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "C#을 사용한 PDF 스티키 주석",
    "alternativeHeadline": "PDF에 스티키 주석 추가 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "PDF, C#, 스티키 주석, 워터마크 주석",
    "wordcount": "302",
    "proficiencyLevel":"초보자",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF 문서 팀",
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
    "url": "/net/sticky-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/sticky-annotations/"
    },
    "dateModified": "2022-02-04",
    "description": "이 주제는 스티키 주석에 대해 설명하며, 예로써 텍스트에서 워터마크 주석을 보여줍니다."
}
</script>
다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

## 워터마크 주석 추가

워터마크 주석은 페이지의 고정된 크기와 위치에 인쇄될 그래픽을 나타내는 데 사용해야 합니다. 인쇄 페이지의 치수에 관계없이 말입니다.

[WatermarkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/watermarkannotation)을 사용하여 PDF 페이지의 특정 위치에 워터마크 텍스트를 추가할 수 있습니다. 불투명도 속성을 사용하여 워터마크의 불투명도도 조절할 수 있습니다.

워터마크 주석을 추가하기 위한 다음 코드 스니펫을 확인하세요.

```csharp
 //문서 로드
Aspose.PDF.Document doc = new Aspose.PDF.Document("source.pdf");

//주석 추가를 위한 페이지 객체 로드
Page page = doc.Pages[1];

//주석 생성
WatermarkAnnotation wa = new WatermarkAnnotation(page, new Aspose.PDF.Rectangle(100, 500, 400, 600));

//페이지의 주석 컬렉션에 주석 추가
page.Annotations.Add(wa);

//폰트 설정을 위한 TextState 생성
Aspose.PDF.Text.TextState ts = new Aspose.PDF.Text.TextState();

ts.ForegroundColor = Aspose.PDF.Color.Blue;
ts.Font = FontRepository.FindFont("Times New Roman");

ts.FontSize = 32;

//주석 텍스트의 불투명도 레벨 설정

wa.Opacity = 0.5;
//주석에 텍스트 추가

wa.SetTextAndState(new string[] { "HELLO", "Line 1", "Line 2" }, ts);

//문서 저장
doc.Save("Output.pdf");
```
## PDF 문서에서 단일 이미지 참조를 여러 번 추가하기

때때로 PDF 문서에서 동일한 이미지를 여러 번 사용해야 하는 요구 사항이 있습니다. 새 인스턴스를 추가하면 결과 PDF 문서가 증가합니다. Aspose.PDF for .NET 17.1.0에서는 XImageCollection.Add(XImage)라는 새 메소드를 추가했습니다. 이 메소드는 원본 이미지와 동일한 PDF 객체에 대한 참조를 추가하여 PDF 문서 크기를 최적화합니다.

```csharp
 Aspose.PDF.Rectangle imageRectangle = new Aspose.PDF.Rectangle(0, 0, 30, 15);

using (Aspose.PDF.Document document = new Aspose.PDF.Document("input.pdf"))
{
    using (var imageStream = File.Open("icon.png", FileMode.Open))
    {
        XImage image = null;
        foreach (Page page in document.Pages)
        {
            WatermarkAnnotation annotation = new WatermarkAnnotation(page, page.Rect);
            XForm form = annotation.Appearance["N"];
            form.BBox = page.Rect;
            string name;
            if (image == null)
            {
                name = form.Resources.Images.Add(imageStream);
                image = form.Resources.Images[name];
            }
            else
            {
                name = form.Resources.Images.Add(image);
            }
            form.Contents.Add(new Operator.GSave());
            form.Contents.Add(new Operator.ConcatenateMatrix(new Aspose.PDF.Matrix(imageRectangle.Width, 0, 0, imageRectangle.Height, 0, 0)));
            form.Contents.Add(new Operator.Do(name));
            form.Contents.Add(new Operator.GRestore());
            page.Annotations.Add(annotation, false);
            imageRectangle = new Aspose.PDF.Rectangle(0, 0, imageRectangle.Width * 1.01, imageRectangle.Height * 1.01);
        }
    }
    document.Save("output.pdf");
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
    "applicationCategory": ".NET용 PDF 조작 라이브러리",
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

