```
---
title: PDF 파일에 선 객체 추가
linktitle: 선 추가
type: docs
weight: 40
url: ko/net/add-line/
description: 이 문서는 Aspose.PDF for .NET을 사용하여 PDF에 선 객체를 생성하는 방법을 설명합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF 파일에 선 객체 추가",
    "alternativeHeadline": "PDF 파일에서 선 객체 생성 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "PDF, C#, PDF 내 선",
    "wordcount": "302",
    "proficiencyLevel":"초급",
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
    "url": "/net/add-line/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-line/"
    },
    "dateModified": "2022-02-04",
    "description": "이 문서는 Aspose.PDF for .NET을 사용하여 PDF에 선 객체를 생성하는 방법을 설명합니다."
}
</script>
```
다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리에서도 작동합니다.

## 선 객체 추가

Aspose.PDF for .NET은 PDF 문서에 그래프 객체(예: 그래프, 선, 사각형 등)를 추가하는 기능을 지원합니다. 또한 [선](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/line) 객체를 추가할 수 있으며 여기에서 대시 패턴, 색상 및 선 요소의 다른 형식을 지정할 수도 있습니다.

아래 단계를 따르세요:

1. 새 PDF [문서](https://reference.aspose.com/pdf/net/aspose.pdf/document)를 생성합니다.

1. PDF 파일의 페이지 컬렉션에 [페이지](https://reference.aspose.com/pdf/net/aspose.pdf/page)를 추가합니다.

1. [그래프](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) 인스턴스를 생성합니다.

1. 페이지 인스턴스의 문단 컬렉션에 그래프 객체를 추가합니다.

1. [사각형](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) 인스턴스를 생성합니다.

1. 선 너비를 설정합니다.
1. PDF 파일을 저장하세요.

다음 코드 스니펫은 색상으로 채워진 [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) 객체를 추가하는 방법을 보여줍니다.

```csharp
        public static void AddLineObjectToPDF()
        {
            // Document 인스턴스 생성
            var document = new Document();

            // PDF 파일의 페이지 컬렉션에 페이지 추가
            var page = document.Pages.Add();

            // Graph 인스턴스 생성
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);

            // 페이지 인스턴스의 단락 컬렉션에 그래프 객체 추가
            page.Paragraphs.Add(graph);

            // Rectangle 인스턴스 생성
            var line = new Line(new float[] { 100, 100, 200, 100 });

            // Graph 객체에 대한 채우기 색상 지정
            line.GraphInfo.DashArray = new int[] { 0, 1, 0 };
            line.GraphInfo.DashPhase = 1;

            // Graph 객체의 모양 컬렉션에 사각형 객체 추가
            graph.Shapes.Add(line);

            // PDF 파일 저장
            document.Save(_dataDir + "AddLineObject_out.pdf");
        }
```
![Add Line](add_line.png)

## PDF 문서에 점선 대시 라인 추가 방법

```csharp
        public static void DashLengthInBlackAndDashLengthInWhite()
        {
            // 문서 인스턴스 생성
            var document = new Document();

            // PDF 파일의 페이지 컬렉션에 페이지 추가
            var page = document.Pages.Add();

            // 특정 크기의 Drawing 객체 생성
            var canvas = new Aspose.Pdf.Drawing.Graph(100, 400);
            // 페이지 인스턴스의 단락 컬렉션에 Drawing 객체 추가
            page.Paragraphs.Add(canvas);

            // Line 객체 생성
            var line = new Line(new float[] { 100, 100, 200, 100 });
            // Line 객체에 색상 설정
            line.GraphInfo.Color = Color.Red;
            // Line 객체에 대시 배열 지정
            line.GraphInfo.DashArray = new int[] { 0, 1, 0 };
            // Line 인스턴스에 대시 위상 설정
            line.GraphInfo.DashPhase = 1;
            // Drawing 객체의 도형 컬렉션에 라인 추가
            canvas.Shapes.Add(line);
            // PDF 파일 저장
            document.Save(_dataDir + "DashLengthInBlackAndDashLengthInWhite_out.pdf");
        }
```
![점선](dash_line.png)

## 페이지를 가로질러 선 그리기

또한 선 객체를 사용하여 왼쪽-아래에서 오른쪽-위로, 왼쪽-위에서 오른쪽-아래로 교차하는 선을 그릴 수 있습니다.

다음 코드 스니펫을 살펴보아 이 요구사항을 완성하세요.

```csharp
   public static void ExampleLineAcrossPage()
        {

            // 문서 인스턴스 생성
            var document = new Document();

            // 페이지를 PDF 파일의 페이지 컬렉션에 추가
            var page = document.Pages.Add();
            // 모든 면의 페이지 마진을 0으로 설정

            page.PageInfo.Margin.Left = 0;
            page.PageInfo.Margin.Right = 0;
            page.PageInfo.Margin.Bottom = 0;
            page.PageInfo.Margin.Top = 0;

            // 페이지 크기와 동일한 너비와 높이를 가진 그래프 객체 생성
            var graph = new Aspose.Pdf.Drawing.Graph(
                (float)page.PageInfo.Width,
                (float)page.PageInfo.Height);

            // 페이지의 왼쪽-아래에서 오른쪽-위 모서리로 시작하는 첫 번째 선 객체 생성
            var line = new Line(
                    new float[]{
                        (float)page.Rect.LLX, 0,
                        (float)page.PageInfo.Width,
                        (float)page.Rect.URY });

            // 선을 그래프 객체의 도형 컬렉션에 추가
            graph.Shapes.Add(line);
            // 페이지의 왼쪽-위 모서리에서 오른쪽-아래 모서리로 선 그리기
            var line2 = new Line(
                new float[]{ 0,
                    (float) page.Rect.URY,
                    (float) page.PageInfo.Width,
                    (float) page.Rect.LLX });

            // 선을 그래프 객체의 도형 컬렉션에 추가
            graph.Shapes.Add(line2);

            // 그래프 객체를 페이지의 단락 컬렉션에 추가
            page.Paragraphs.Add(graph);

            // PDF 파일 저장
            document.Save(_dataDir + "ExampleLineAcrossPage_out.pdf");
        }
```
![Drawing Line](draw_line.png)

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


