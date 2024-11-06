---
title: PDF 파일에 곡선 객체 추가
linktitle: 곡선 추가
type: docs
weight: 30
url: ko/net/add-curve/
description: 이 글은 Aspose.PDF for .NET을 사용하여 PDF에 곡선 객체를 만드는 방법을 설명합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF 파일에 곡선 객체 추가",
    "alternativeHeadline": "PDF 파일에서 곡선 객체 생성 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "PDF, .net, PDF 내 곡선",
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
    "url": "/net/add-curve/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-curve/"
    },
    "dateModified": "2022-02-04",
    "description": "이 글은 Aspose.PDF for .NET을 사용하여 PDF에 곡선 객체를 만드는 방법을 설명합니다."
}
</script>
다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리에서도 작동합니다.

## 곡선 객체 추가

그래프 [Curve](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/curve)는 각 선이 보통의 이중 점에서 세 개의 다른 선과 만나는 사영선들의 연결된 합집합입니다.

Aspose.PDF for .NET은 그래프에서 Bézier 곡선을 사용하는 방법을 보여줍니다.
Bézier 곡선은 컴퓨터 그래픽에서 부드러운 곡선을 모델링하는 데 널리 사용됩니다. 곡선은 제어점의 볼록 껍질에 완전히 포함되며, 점들은 그래픽으로 표시되어 곡선을 직관적으로 조작하는 데 사용될 수 있습니다.
전체 곡선은 주어진 네 점(그들의 볼록 껍질)의 사각형의 모서리에 포함됩니다.

이 글에서는 PDF 문서에서 만들 수 있는 단순 그래프 곡선과 채워진 곡선을 조사할 것입니다.

아래 단계를 따르세요:

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 인스턴스 생성

changefreq: "monthly"
type: docs
1. [테두리](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border)를 그래픽 객체에 설정하세요.

1. 페이지의 단락 컬렉션에 [그래프](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) 객체를 추가하세요.

1. PDF 파일을 저장하세요.

```csharp
 public static void ExampleCurve()
        {
            // 문서 인스턴스 생성
            var document = new Document();

            // 페이지를 PDF 파일의 페이지 컬렉션에 추가
            var page = document.Pages.Add();

            // 특정 치수를 가진 그래픽 객체 생성
            var graph = new Aspose.Pdf.Drawing.Graph(400, 200);

            // 그래픽 객체에 테두리 설정
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120 });
            curve1.GraphInfo.Color = Color.GreenYellow;
            graph.Shapes.Add(curve1);

            // 페이지의 단락 컬렉션에 그래프 객체 추가
            page.Paragraphs.Add(graph);

            // PDF 파일 저장
            document.Save(_dataDir + "DrawingCurve1_out.pdf");
        }
```
다음 그림은 코드 스니펫을 실행한 결과를 보여줍니다:

![Drawing Curve](drawing_curve.png)

## 채워진 곡선 객체 생성

이 예제는 색상으로 채워진 곡선 객체를 추가하는 방법을 보여줍니다.

```csharp
      public static void CurveFilled()
        {
            // 문서 인스턴스 생성
            var document = new Document();

            // PDF 파일의 페이지 컬렉션에 페이지 추가
            var page = document.Pages.Add();

            // 특정 차원으로 Drawing 객체 생성
            var graph = new Aspose.Pdf.Drawing.Graph(400, 200);

            // Drawing 객체에 테두리 설정
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120 });
            curve1.GraphInfo.FillColor = Color.GreenYellow;
            graph.Shapes.Add(curve1);

            // 페이지의 단락 컬렉션에 Graph 객체 추가
            page.Paragraphs.Add(graph);

            // PDF 파일 저장
            document.Save(_dataDir + "DrawingCurve2_out.pdf");
        }
```
충전된 곡선 추가 결과를 확인하세요:

![Filled Curve](filled_curve.png)

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
                "contactType": "판매",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "판매",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "판매",
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

