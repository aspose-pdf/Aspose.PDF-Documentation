---
title: PDF 파일에 호 객체 추가
linktitle: 호 추가
type: docs
weight: 10
url: ko/net/add-arc/
description: 이 문서는 Aspose.PDF for .NET을 사용하여 PDF에 호 객체를 생성하는 방법을 설명합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF 파일에 호 객체 추가",
    "alternativeHeadline": "PDF 파일에서 호 생성 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "PDF, C#, PDF 내 호",
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
    "url": "/net/add-arc/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-arc/"
    },
    "dateModified": "2022-02-04",
    "description": "이 문서는 Aspose.PDF for .NET을 사용하여 PDF에 호 객체를 생성하는 방법을 설명합니다."
}
</script>

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

## Arc 객체 추가

Aspose.PDF for .NET은 PDF 문서에 그래프 객체(예: 그래프, 선, 사각형 등)를 추가하는 기능을 지원합니다. 또한 특정 색상으로 아크 객체를 채우는 기능을 제공합니다.

아래 단계를 따르세요:

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 인스턴스 생성

1. 특정 크기로 [Drawing object](https://reference.aspose.com/pdf/net/aspose.pdf.drawing) 생성

1. Drawing 객체에 [Border](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border) 설정

1. 페이지의 단락 컬렉션에 [Graph](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) 객체 추가

1. PDF 파일 저장

다음 코드 스니펫은 [Arc](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/arc) 객체를 추가하는 방법을 보여줍니다.

```csharp
 public static void Arc()
        {
            // Document 인스턴스 생성
            var document = new Document();

            // PDF 파일의 페이지 컬렉션에 페이지 추가
            var page = document.Pages.Add();

            // 특정 크기로 Drawing 객체 생성
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // Drawing 객체에 대한 테두리 설정
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var arc1 = new Arc(100, 100, 95, 0, 90);
            arc1.GraphInfo.Color = Color.GreenYellow;
            graph.Shapes.Add(arc1);

            var arc2 = new Arc(100, 100, 90, 70, 180);
            arc2.GraphInfo.Color = Color.DarkBlue;
            graph.Shapes.Add(arc2);

            var arc3 = new Arc(100, 100, 85, 120, 210);
            arc3.GraphInfo.Color = Color.Red;
            graph.Shapes.Add(arc3);

            // 페이지의 단락 컬렉션에 Graph 객체 추가
            page.Paragraphs.Add(graph);

            // PDF 파일 저장
            document.Save(_dataDir + "DrawingArc_out.pdf");

        }
```
## 채워진 호 객체 생성

다음 예제는 색상과 특정 치수로 채워진 호 객체를 추가하는 방법을 보여줍니다.

```csharp
        public static void ArcFilled()
        {
            // 문서 인스턴스 생성
            var document = new Document();

            // PDF 파일의 페이지 컬렉션에 페이지 추가
            var page = document.Pages.Add();

            // 특정 치수를 가진 Drawing 객체 생성
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // Drawing 객체에 테두리 설정
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var arc = new Arc(100, 100, 95, 0, 90);
            arc.GraphInfo.FillColor = Color.GreenYellow;
            graph.Shapes.Add(arc);

            var line = new Line(new float[] { 195, 100, 100, 100, 100, 195 });
            line.GraphInfo.FillColor = Color.GreenYellow;
            graph.Shapes.Add(line);

            // 페이지의 단락 컬렉션에 그래프 객체 추가
            page.Paragraphs.Add(graph);

            // PDF 파일 저장
            document.Save(_dataDir + "ExampleFilledArc_out.pdf");

        }
```
채워진 아크의 결과를 보겠습니다:

![Filled Arc](filled_arc.png)

