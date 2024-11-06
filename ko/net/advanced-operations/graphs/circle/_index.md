---
title: PDF 파일에 원 객체 추가
linktitle: 원 추가
type: docs
weight: 20
url: ko/net/add-circle/
description: 이 문서는 Aspose.PDF for .NET을 사용하여 PDF에 원 객체를 생성하는 방법을 설명합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF 파일에 원 객체 추가",
    "alternativeHeadline": "PDF 파일에서 원 객체 생성 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "PDF, C#, PDF 내 원",
    "wordcount": "302",
    "proficiencyLevel":"초급",
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
    "url": "/net/add-circle/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-circle/"
    },
    "dateModified": "2022-02-04",
    "description": "이 문서는 Aspose.PDF for .NET을 사용하여 PDF에 원 객체를 생성하는 방법을 설명합니다."
}
</script>
다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리에서도 작동합니다.

## 원 객체 추가

막대 그래프와 마찬가지로 원 그래프는 여러 개별 카테고리의 데이터를 표시하는 데 사용할 수 있습니다. 그러나 원 그래프는 전체를 구성하는 모든 카테고리에 대한 데이터가 있을 때만 사용할 수 있습니다. 그러므로 Aspose.PDF for .NET을 사용하여 [원](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/circle) 객체를 추가하는 방법을 살펴보겠습니다.

아래 단계를 따르세요:

1. [문서](https://reference.aspose.com/pdf/net/aspose.pdf/document) 인스턴스 생성

1. 특정 치수로 [그리기 객체](https://reference.aspose.com/pdf/net/aspose.pdf.drawing) 생성

1. 그리기 객체에 [테두리](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border) 설정

1. 페이지의 단락 컬렉션에 [그래프](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) 객체 추가

1. PDF 파일 저장

```csharp
        public static void Circle()
        {
            // 문서 인스턴스 생성
            var document = new Document();

            // PDF 파일의 페이지 컬렉션에 페이지 추가
            var page = document.Pages.Add();

            // 특정 치수로 그리기 객체 생성
            var graph = new Aspose.Pdf.Drawing.Graph(400, 200);
            // 그리기 객체에 테두리 설정
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var circle = new Circle(100, 100, 40);

            circle.GraphInfo.Color = Color.GreenYellow;
            graph.Shapes.Add(circle);

            // 페이지의 단락 컬렉션에 그래프 객체 추가
            page.Paragraphs.Add(graph);

            // PDF 파일 저장
            document.Save(_dataDir + "DrawingCircle1_out.pdf");
        }
```
우리가 그린 원은 다음과 같습니다:

![원 그리기](drawing_circle.png)

## 채워진 원 객체 생성

이 예제는 색으로 채워진 원 객체를 추가하는 방법을 보여줍니다.

```csharp
        public static void CircleFilled()
        {
            // 문서 인스턴스 생성
            var document = new Document();

            // PDF 파일의 페이지 컬렉션에 페이지 추가
            var page = document.Pages.Add();

            // 특정 치수의 드로잉 객체 생성
            var graph = new Aspose.Pdf.Drawing.Graph(400, 200);

            // 드로잉 객체에 테두리 설정
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var circle = new Circle(100, 100, 40);
            circle.GraphInfo.Color = Color.GreenYellow;
            circle.GraphInfo.FillColor = Color.Green;
            circle.Text = new TextFragment("원");

            graph.Shapes.Add(circle);

            // 페이지의 문단 컬렉션에 그래프 객체 추가
            page.Paragraphs.Add(graph);

            // PDF 파일 저장
            document.Save(_dataDir + "DrawingCircle2_out.pdf");
        }
```
충전된 원을 추가한 결과를 확인해 보겠습니다:

![Filled Circle](filled_circle.png)

