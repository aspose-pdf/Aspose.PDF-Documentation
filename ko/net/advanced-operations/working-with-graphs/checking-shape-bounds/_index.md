---
title: 도형 컬렉션에서 모양 경계 확인
type: docs
weight: 70
url: /ko/net/aspose-pdf-drawing-graph-shapes-bounds-check/
description: 도형이 도형 컬렉션에 삽입될 때 경계를 확인하여 부모 컨테이너 내에 적합한지 확인하는 방법을 알아보세요.
lastmod: "2025-02-28"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Checking Element Bounds in Shapes Collection",
    "alternativeHeadline": "Configurable Bounds Checking for Aspose.PDF Shapes with Exception Mode",
    "abstract": "Aspose.PDF for .NET의 새로운 경계 확인 기능은 `Drawing.Graph.Shapes` 컬렉션에서 요소의 치수를 부모 컨테이너와 자동으로 검증하여 레이아웃 오버플로우를 방지합니다. 요소가 컨테이너 한계를 초과할 때 예외를 발생시켜 삽입 중에 엄격한 크기 제약을 적용하여 정확한 PDF 형식을 보장하고 디자인 정확성을 간소화합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "723",
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
    "url": "/net/aspose-pdf-drawing-graph-shapes-bounds-check/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/aspose-pdf-drawing-graph-shapes-bounds-check/"
    },
    "dateModified": "2025-03-17",
    "description": ""
}
</script>

## 소개
이 문서는 도형 컬렉션에서 경계 확인 기능을 사용하는 방법에 대한 자세한 가이드를 제공합니다. 이 기능은 요소가 부모 컨테이너 내에 적합하도록 보장하며, 구성하여 구성 요소가 맞지 않을 경우 예외를 발생시킬 수 있습니다. 이 기능을 구현하는 단계를 안내하고 완전한 예제를 제공합니다.

## 전제 조건
다음이 필요합니다:
* Visual Studio 2019 이상
* Aspose.PDF for .NET 25.3 이상
* 몇 페이지가 포함된 샘플 PDF 파일

Aspose.PDF for .NET 라이브러리는 공식 웹사이트에서 다운로드하거나 Visual Studio의 NuGet 패키지 관리자를 사용하여 설치할 수 있습니다.

## 단계
작업을 완료하기 위한 단계는 다음과 같습니다:
1. 새 문서를 만들고 페이지를 추가합니다.
2. 지정된 치수로 `Graph` 객체를 만듭니다.
3. 지정된 치수로 `Shape` 객체를 만듭니다.
4. `BoundsCheckMode`를 `ThrowExceptionIfDoesNotFit`로 설정합니다.
5. 도형을 그래프에 추가하려고 시도합니다.

이 단계들을 C# 코드로 구현하는 방법을 살펴보겠습니다.

### 단계 1: 새 문서 만들고 페이지 추가
먼저, 새 PDF 문서를 만들고 페이지를 추가합니다.

```csharp
using (var doc = new Aspose.Pdf.Document())
{
    Aspose.Pdf.Page page = doc.Pages.Add();
}
```

### 단계 2: 지정된 치수로 Graph 객체 만들기
다음으로, 너비와 높이가 100 단위인 `Graph` 객체를 만듭니다. 페이지의 상단에서 10 단위, 왼쪽에서 15 단위 떨어진 위치에 그래프를 배치합니다. 그래프에 검은색 테두리를 추가합니다.

```csharp
var graph = new Aspose.Pdf.Drawing.Graph(100d, 100d)
{
    Top = 10,
    Left = 15,
    Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1F, Aspose.Pdf.Color.Black)
};
page.Paragraphs.Add(graph);
```

### 단계 3: 지정된 치수로 Aspose.Pdf.Drawing.Shape 객체 (예: Aspose.Pdf.Drawing.Rectangle) 만들기
너비와 높이가 50 단위인 사각형 객체를 만듭니다. 사각형을 (-1, 0) 위치에 배치하는데, 이는 그래프의 경계를 벗어납니다.

```csharp
Aspose.Pdf.Drawing.Rectangle rect = new Aspose.Pdf.Drawing.Rectangle(-1, 0, 50, 50)
{
    GraphInfo =
    {
        FillColor = Aspose.Pdf.Color.Tomato
    }
};
```

### 단계 4: BoundsCheckMode를 ThrowExceptionIfDoesNotFit로 설정
사각형이 그래프 내에 맞지 않을 경우 예외가 발생하도록 `BoundsCheckMode`를 `ThrowExceptionIfDoesNotFit`로 설정합니다.

```csharp
graph.Shapes.UpdateBoundsCheckMode(Aspose.Pdf.BoundsCheckMode.ThrowExceptionIfDoesNotFit);
```

### 단계 5: 사각형을 그래프에 추가하려고 시도
사각형을 그래프에 추가하려고 시도합니다. 이는 사각형이 그래프의 치수 내에 맞지 않기 때문에 `Aspose.Pdf.BoundsOutOfRangeException`을 발생시킵니다.

```csharp
graph.Shapes.Add(rect);
```

## 출력
코드를 실행한 후 예상 출력은 다음과 같은 `Aspose.Pdf.BoundsOutOfRangeException`입니다:

```
Bounds not fit. Container dimensions: 100x100
```

## 문제 해결
문제가 발생할 경우, 다음 몇 가지 팁을 참고하세요:
* `BoundsCheckMode`가 올바르게 설정되었는지 확인합니다.
* 요소와 컨테이너의 치수가 정확한지 확인합니다.
* 컨테이너 내에서 요소의 위치를 확인합니다.

## 전체 예제
아래는 모든 단계를 결합한 전체 예제입니다:

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckShapeBounds()
{
    // Create a new document and add a page
    using (var doc = new Aspose.Pdf.Document())
    {
        Aspose.Pdf.Page page = doc.Pages.Add();
        
        // Create a Graph Object with Specified Dimensions
        var graph = new Aspose.Pdf.Drawing.Graph(100d, 100d)
        {
            Top = 10,
            Left = 15,
            Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1F, Aspose.Pdf.Color.Black)
        };
        page.Paragraphs.Add(graph);
        
        // Create a Aspose.Pdf.Drawing.Shape object (for example, Aspose.Pdf.Drawing.Rectangle) with specified dimensions
        Aspose.Pdf.Drawing.Rectangle rect = new Aspose.Pdf.Drawing.Rectangle(-1, 0, 50, 50)
        {
            GraphInfo =
            {
                FillColor = Aspose.Pdf.Color.Tomato
            }
        };
        
        // Set the BoundsCheckMode to ThrowExceptionIfDoesNotFit
        graph.Shapes.UpdateBoundsCheckMode(Aspose.Pdf.BoundsCheckMode.ThrowExceptionIfDoesNotFit);
        
        // Attempt to add the rectangle to the graph
        graph.Shapes.Add(rect);
    }
}```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckShapeBounds()
{
    // Create a new document and add a page
    using var doc = new Aspose.Pdf.Document();
    Aspose.Pdf.Page page = doc.Pages.Add();

    // Create a Graph Object with Specified Dimensions
    var graph = new Aspose.Pdf.Drawing.Graph(100d, 100d)
    {
        Top = 10,
        Left = 15,
        Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1F, Aspose.Pdf.Color.Black)
    };
    page.Paragraphs.Add(graph);

    // Create a Aspose.Pdf.Drawing.Shape object (for example, Aspose.Pdf.Drawing.Rectangle) with specified dimensions
    Aspose.Pdf.Drawing.Rectangle rect = new Aspose.Pdf.Drawing.Rectangle(-1, 0, 50, 50)
    {
        GraphInfo =
        {
            FillColor = Aspose.Pdf.Color.Tomato
        }
    };

    // Set the BoundsCheckMode to ThrowExceptionIfDoesNotFit
    graph.Shapes.UpdateBoundsCheckMode(Aspose.Pdf.BoundsCheckMode.ThrowExceptionIfDoesNotFit);

    // Attempt to add the rectangle to the graph
    graph.Shapes.Add(rect);
}
```
{{< /tab >}}
{{< /tabs >}}

## 결론
도형 컬렉션의 경계 확인 기능은 요소가 부모 컨테이너 내에 적합하도록 보장하는 강력한 도구입니다. `BoundsCheckMode`를 `ThrowExceptionIfDoesNotFit`로 설정하여 PDF 문서에서 레이아웃 문제를 방지할 수 있습니다. 이 기능은 요소의 정확한 위치 지정 및 크기가 중요한 시나리오에서 특히 유용합니다. 자세한 내용은 [공식 문서](https://docs.aspose.com/pdf/net/)를 방문하세요.