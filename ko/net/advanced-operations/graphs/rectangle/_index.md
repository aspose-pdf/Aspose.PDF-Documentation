---
title: PDF 파일에 사각형 객체 추가
linktitle: 사각형 추가
type: docs
weight: 50
url: /ko/net/add-rectangle/
description: 이 글은 Aspose.PDF for .NET을 사용하여 PDF에 사각형 객체를 생성하는 방법을 설명합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF 파일에 사각형 객체 추가",
    "alternativeHeadline": "PDF 파일에서 사각형 객체 생성 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "pdf, c#, pdf내 사각형",
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
    "url": "/net/add-rectangle/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-rectangle/"
    },
    "dateModified": "2022-02-04",
    "description": "이 글은 Aspose.PDF for .NET을 사용하여 PDF에 사각형 객체를 생성하는 방법을 설명합니다."
}
</script>
다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

## 사각형 객체 추가

Aspose.PDF for .NET은 PDF 문서에 그래프 객체(예: 그래프, 선, 사각형 등)를 추가하는 기능을 지원합니다. 또한 [사각형](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) 객체를 추가할 때 특정 색상으로 사각형 객체를 채우고, Z-순서를 제어하며, 그라디언트 색상을 채우는 기능도 제공합니다.

먼저 사각형 객체를 생성하는 가능성을 살펴봅시다.

아래 단계를 따르세요:

1. 새 PDF [문서](https://reference.aspose.com/pdf/net/aspose.pdf/document)를 생성합니다

1. PDF 파일의 페이지 컬렉션에 [페이지](https://reference.aspose.com/pdf/net/aspose.pdf/page)를 추가합니다

1. 페이지 인스턴스의 단락 컬렉션에 [텍스트 조각](https://reference.aspose.com/pdf/net/aspose.pdf/texfragment)을 추가합니다

1. [그래프](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) 인스턴스를 생성합니다

1.
1. 사각형 인스턴스 생성

1. [사각형](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) 객체를 그래프 객체의 도형 컬렉션에 추가

1. 그래프 객체를 페이지 인스턴스의 단락 컬렉션에 추가

1. [텍스트 조각](https://reference.aspose.com/pdf/net/aspose.pdf/texfragment)을 페이지 인스턴스의 단락 컬렉션에 추가

1. PDF 파일 저장

```csharp
 private static void AddRectangle(Page page, float x, float y, float width, float height, Color color, int zindex)
        {
            // 사각형 객체의 지정된 크기와 동일한 크기의 그래프 객체 생성
            Aspose.Pdf.Drawing.Graph graph = new Aspose.Pdf.Drawing.Graph(width, height)
            {
                // 그래프 인스턴스의 위치 변경 가능 여부
                IsChangePosition = false,
                // 그래프 인스턴스의 왼쪽 좌표 위치 설정
                Left = x,
                // 그래프 객체의 상단 좌표 위치 설정
                Top = y
            };
            // "graph" 안에 사각형 추가
            Rectangle rect = new Rectangle(0, 0, width, height);
            // 사각형 채우기 색상 설정
            rect.GraphInfo.FillColor = color;
            // 그래프 객체의 색상
            rect.GraphInfo.Color = color;
            // 그래프 인스턴스의 도형 컬렉션에 사각형 추가
            graph.Shapes.Add(rect);
            // 사각형 객체의 Z-인덱스 설정
            graph.ZIndex = zindex;
            // 페이지 객체의 단락 컬렉션에 그래프 추가
            page.Paragraphs.Add(graph);
        }
```
## 채워진 사각형 객체 생성

Aspose.PDF for .NET은 특정 색상으로 사각형 객체를 채울 수 있는 기능을 제공합니다.

다음 코드 조각은 색상으로 채워진 [사각형](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) 객체를 추가하는 방법을 보여줍니다.

```csharp
    {
        private const string _dataDir = "C:\\Samples\\";
        public static void RectangleFilled()
        {
            // 문서 인스턴스 생성
            var doc = new Document();

            // PDF 파일의 페이지 컬렉션에 페이지 추가
            var page = doc.Pages.Add();
            // 그래프 인스턴스 생성
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);

            // 페이지 인스턴스의 단락 컬렉션에 그래프 객체 추가
            page.Paragraphs.Add(graph);

            // 사각형 인스턴스 생성
            var rect = new Rectangle(100, 100, 200, 120);

            // 그래프 객체에 채우기 색상 지정
            rect.GraphInfo.FillColor = Color.Red;

            // 그래프 객체의 형태 컬렉션에 사각형 객체 추가
            graph.Shapes.Add(rect);

            // PDF 파일 저장
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```
사각형이 단색으로 채워진 결과를 보세요:

![Filled Rectangle](fill_rectangle.png)

## 그라데이션 채우기로 그리기 추가

Aspose.PDF for .NET은 PDF 문서에 그래프 객체를 추가하는 기능을 지원하며 때때로 그라프 객체를 그라데이션 색상으로 채울 필요가 있습니다. 그라프 객체를 그라데이션 색상으로 채우려면 다음과 같이 gradientAxialShading 객체로 setPatterColorSpace를 설정해야 합니다.

다음 코드 조각은 그라데이션 색상으로 채워진 [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) 객체를 추가하는 방법을 보여줍니다.

```csharp
 public static void CreateFilledRectangletGradientFill()
        {
            // 문서 인스턴스 생성
            var doc = new Document();

            // PDF 파일의 페이지 컬렉션에 페이지 추가
            var page = doc.Pages.Add();
            // 그래프 인스턴스 생성
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // 페이지 인스턴스의 단락 컬렉션에 그래프 객체 추가
            page.Paragraphs.Add(graph);
            // 사각형 인스턴스 생성
            var rect = new Rectangle(0, 0, 300, 300);
            // 그래프 객체에 채우기 색상 지정
            var gradientColor = new Color();
            var gradientSettings = new GradientAxialShading(Color.Red, Color.Blue)
            {
                Start = new Point(0, 0),
                End = new Point(350, 350)
            };
            gradientColor.PatternColorSpace = gradientSettings;
            rect.GraphInfo.FillColor = gradientColor;

            // 그래프 객체의 형태 컬렉션에 사각형 객체 추가
            graph.Shapes.Add(rect);

            // PDF 파일 저장
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```
![그라디언트 사각형](gradient.png)

## 알파 색상 채널을 가진 사각형 생성

Aspose.PDF for .NET은 특정 색상으로 사각형 객체를 채울 수 있습니다. 사각형 객체는 투명한 외관을 제공하기 위해 알파 색상 채널을 가질 수도 있습니다. 다음 코드 스니펫은 알파 색상 채널을 가진 [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) 객체를 추가하는 방법을 보여줍니다.

이미지의 픽셀은 색상 값과 함께 불투명도에 대한 정보를 저장할 수 있습니다. 이를 통해 투명하거나 반투명 영역을 가진 이미지를 생성할 수 있습니다.

색상을 투명하게 만드는 대신, 각 픽셀은 그 불투명도에 대한 정보를 저장합니다. 이 불투명도 데이터를 알파 채널이라고 하며, 일반적으로 픽셀의 색상 채널 다음에 저장됩니다.

```csharp
     public static void RectangleFilled_AlphaChannel()
        {
            // Document 인스턴스 생성
            var doc = new Document();

            // PDF 파일의 페이지 컬렉션에 페이지 추가
            var page = doc.Pages.Add();
            // Graph 인스턴스 생성
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);
            // 페이지 인스턴스의 단락 컬렉션에 그래프 객체 추가
            page.Paragraphs.Add(graph);
            // Rectangle 인스턴스 생성
            var rect = new Rectangle(100, 100, 200, 120);
            // Graph 객체에 채우기 색상 지정
            rect.GraphInfo.FillColor = Color.FromArgb(128, 244, 180, 0);

            // Graph 객체의 도형 컬렉션에 사각형 객체 추가
            graph.Shapes.Add(rect);

            // 두 번째 사각형 객체 생성
            var rect1 = new Rectangle(200, 150, 200, 100);
            rect1.GraphInfo.FillColor = Color.FromArgb(160, 120, 0, 120);
            graph.Shapes.Add(rect1);

            // 페이지 객체의 단락 컬렉션에 그래프 인스턴스 추가
            page.Paragraphs.Add(graph);

            // PDF 파일 저장
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```
![Rectangle Alpha Channel Color](rectangle_color.png)

## 사각형의 Z-순서 제어

Aspose.PDF for .NET은 PDF 문서에 그래프 객체(예: 그래프, 선, 사각형 등)를 추가하는 기능을 지원합니다. PDF 파일 내에 동일 객체의 인스턴스를 여러 개 추가할 때, Z-순서를 지정하여 렌더링을 제어할 수 있습니다. Z-순서는 객체를 서로 위에 렌더링할 필요가 있을 때도 사용됩니다.

다음 코드 조각은 서로 위에 [사각형](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) 객체를 렌더링하는 단계를 보여줍니다.

```csharp
 public static void AddRectangleZOrder()
        {
            // Document 클래스 객체 인스턴스화
            Document doc1 = new Document();
            /// PDF 파일의 페이지 컬렉션에 페이지 추가
            Page page1 = doc1.Pages.Add();
            // PDF 페이지의 크기 설정
            page1.SetPageSize(375, 300);
            // 페이지 객체의 왼쪽 여백을 0으로 설정
            page1.PageInfo.Margin.Left = 0;
            // 페이지 객체의 상단 여백을 0으로 설정
            page1.PageInfo.Margin.Top = 0;
            // 색상이 빨간색이고 Z-순서가 0이며 특정 치수의 새 사각형 생성
            AddRectangle(page1, 50, 40, 60, 40, Color.Red, 2);
            // 색상이 파란색이고 Z-순서가 0이며 특정 치수의 새 사각형 생성
            AddRectangle(page1, 20, 20, 30, 30, Color.Blue, 1);
            // 색상이 초록색이고 Z-순서가 0이며 특정 치수의 새 사각형 생성
            AddRectangle(page1, 40, 40, 60, 30, Color.Green, 0);
            // 결과 PDF 파일 저장
            doc1.Save(_dataDir + "ControlRectangleZOrder_out.pdf");
        }
```
![Z 순서 제어](control.png)

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
                "availableLanguage": "영어"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "영업",
                "areaServed": "GB",
                "availableLanguage": "영어"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "영업",
                "areaServed": "AU",
                "availableLanguage": "영어"
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


