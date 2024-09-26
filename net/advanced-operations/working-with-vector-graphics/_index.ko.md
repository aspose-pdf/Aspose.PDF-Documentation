---
title: 벡터 그래픽 작업하기
linktitle: 벡터 그래픽 작업하기
type: docs
weight: 120
url: /net/working-with-vector-graphics/
description: 이 글은 C#을 사용하여 GraphicsAbsorber 도구로 작업하는 기능을 설명합니다.
lastmod: "2024-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "GraphicsAbsorber 사용하기",
    "alternativeHeadline": "PDF 파일에서 이미지의 위치를 얻는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, c#, pdf에서 GraphicsAbsorber",
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
    "url": "/net/working-with-vector-graphics/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-vector-graphics/"
    },
    "dateModified": "2022-02-04",
    "description": "이 섹션에서는 C# 라이브러리를 사용하여 GraphicsAbsorber PDF 파일로 작업하는 기능을 설명합니다."
}
</script>
이 장에서는 `GraphicsAbsorber` 클래스를 사용하여 PDF 문서 내의 벡터 그래픽과 상호 작용하는 방법을 살펴보겠습니다. 그래픽을 이동, 제거 또는 추가해야 하는 경우 이 가이드는 이러한 작업을 효과적으로 수행하는 방법을 보여줄 것입니다. 시작해봅시다!

## 소개<a name="introduction"></a>

벡터 그래픽은 많은 PDF 문서에서 중요한 구성 요소로 사용되며, 이미지, 도형 및 기타 그래픽 요소를 나타냅니다. Aspose.PDF는 `GraphicsAbsorber` 클래스를 제공하여 개발자가 이러한 그래픽에 프로그래밍 방식으로 접근하고 조작할 수 있도록 합니다. `GraphicsAbsorber`의 `Visit` 메소드를 사용하면 지정된 페이지에서 벡터 그래픽을 추출하고 이동, 제거 또는 다른 페이지로 복사하는 등 다양한 작업을 수행할 수 있습니다.

## 1. `GraphicsAbsorber`를 사용하여 그래픽 추출하기<a name="extracting-graphics"></a>

벡터 그래픽을 작업하기 위한 첫 번째 단계는 PDF 문서에서 그래픽을 추출하는 것입니다. 다음은 `GraphicsAbsorber` 클래스를 사용하여 이를 수행하는 방법입니다:

```csharp
public static void UsingGraphicsAbsorber()
{
    // Step 1: Document 객체 생성.
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");

    // Step 2: GraphicsAbsorber 인스턴스 생성.
    var graphicsAbsorber = new GraphicsAbsorber();

    // 문서의 첫 페이지를 선택합니다.
    var page = document.Pages[1];

    // Step 3: `Visit` 메소드를 사용하여 페이지에서 그래픽 추출.
    graphicsAbsorber.Visit(page);

    // 추출된 요소에 대한 정보 표시.
    foreach (var element in graphicsAbsorber.Elements)
    {
        Console.WriteLine($"페이지 번호: {element.SourcePage.Number}");
        Console.WriteLine($"위치: ({element.Position.X}, {element.Position.Y})");
        Console.WriteLine($"연산자 수: {element.Operators.Count}");
    }
}
```
### 설명:

1. **문서 객체 생성**: 새로운 `Document` 객체가 타깃 PDF 파일 경로와 함께 인스턴스화됩니다.
2. **`GraphicsAbsorber` 인스턴스 생성**: 이 클래스는 지정된 페이지에서 모든 그래픽 요소를 캡처합니다.
3. **방문 방법**: `Visit` 메소드가 첫 페이지에서 호출되어 `GraphicsAbsorber`가 벡터 그래픽을 흡수하도록 합니다.
4. **추출된 요소 반복**: 코드는 추출된 각 요소를 반복하면서 페이지 번호, 위치 및 그리기 연산자 수와 같은 정보를 출력합니다.

## 2. 그래픽 이동<a name="moving-graphics"></a>

그래픽을 추출한 후에는 동일한 페이지의 다른 위치로 이동할 수 있습니다. 다음은 이를 달성하는 방법입니다:

```csharp
public static void MoveGraphics()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page = document.Pages[1];
    graphicsAbsorber.Visit(page);

    // 성능 향상을 위해 업데이트를 일시적으로 중단합니다.
    graphicsAbsorber.SuppressUpdate();

    foreach (var element in graphicsAbsorber.Elements)
    {
        var position = element.Position;
        // X 및 Y 좌표를 이동하여 그래픽을 이동합니다.
        element.Position = new Point(position.X + 150, position.Y - 10);
    }

    // 업데이트를 재개하고 변경 사항을 적용합니다.
    graphicsAbsorber.ResumeUpdate();
    document.Save("test.pdf");
}
```
### 핵심 포인트:

- **SuppressUpdate**: 이 메소드는 여러 변경 사항을 수행할 때 성능을 향상시키기 위해 일시적으로 업데이트를 중단합니다.
- **ResumeUpdate**: 이 메소드는 업데이트를 재개하고 그래픽 위치에 대한 변경 사항을 적용합니다.
- **Element Positioning**: 각 그래픽의 위치는 `X` 및 `Y` 좌표를 변경하여 조정됩니다.

## 3. 그래픽 제거<a name="removing-graphics"></a>

특정 그래픽을 페이지에서 제거하고 싶은 시나리오가 있을 수 있습니다. Aspose.PDF는 이를 수행할 수 있는 두 가지 방법을 제공합니다:

### 방법 1: 사각형 경계 사용

```csharp
public static void RemoveGraphicsMethod1()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page = document.Pages[1];
    graphicsAbsorber.Visit(page);
    var rectangle = new Rectangle(70, 248, 170, 252);

    graphicsAbsorber.SuppressUpdate();
    foreach (var element in graphicsAbsorber.Elements)
    {
        // 그래픽의 위치가 사각형 내에 있는지 확인합니다.
        if (rectangle.Contains(element.Position))
        {
            element.Remove(); // 그래픽 요소를 제거합니다.
        }
    }
    graphicsAbsorber.ResumeUpdate();
    document.Save("test.pdf");
}
```
### 방법 2: 제거된 요소들의 모음 사용하기

```csharp
public static void RemoveGraphicsMethod2()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page = document.Pages[1];
    var rectangle = new Rectangle(70, 248, 170, 252);

    graphicsAbsorber.Visit(page);
    var removedElementsCollection = new GraphicElementCollection();
    foreach (var item in graphicsAbsorber.Elements.Where(el => rectangle.Contains(el.Position)))
    {
        removedElementsCollection.Add(item);
    }

    page.Contents.SuppressUpdate();
    page.DeleteGraphics(removedElementsCollection);
    page.Contents.ResumeUpdate();
    document.Save("test.pdf");
}
```

### 설명:

- **사각형 경계**: 제거할 그래픽을 지정하기 위해 사각형 영역을 정의합니다.
- **업데이트 억제 및 재개**: 중간 렌더링 없이 효율적인 제거를 보장합니다.

## 4. 다른 페이지에 그래픽 추가하기<a name="adding-graphics"></a>

한 페이지에서 흡수된 그래픽은 동일한 문서의 다른 페이지에 추가될 수 있습니다.
한 페이지에서 흡수된 그래픽은 동일한 문서의 다른 페이지에 추가될 수 있습니다.

### 방법 1: 그래픽 개별 추가

```csharp
public static void AddToAnotherPageMethod1()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page1 = document.Pages[1];
    var page2 = document.Pages[2];

    graphicsAbsorber.Visit(page1);
    page2.Contents.SuppressUpdate();
    foreach (var element in graphicsAbsorber.Elements)
    {
        element.AddOnPage(page2); // 두 번째 페이지에 각 그래픽 요소를 추가합니다.
    }
    page2.Contents.ResumeUpdate();
    document.Save("test.pdf");
}
```

### 방법 2: 그래픽을 컬렉션으로 추가

```csharp
public static void AddToAnotherPageMethod2()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page1 = document.Pages[1];
    var page2 = document.Pages[2];

    graphicsAbsorber.Visit(page1);
    page2.Contents.SuppressUpdate();
    page2.AddGraphics(graphicsAbsorber.Elements); // 한 번에 모든 그래픽을 추가합니다.
    page2.Contents.ResumeUpdate();
    document.Save("test.pdf");
}
```
### 핵심 포인트:

- **SuppressUpdate 및 ResumeUpdate**: 이 메소드들은 대량 변경을 진행할 때 성능을 유지하는 데 도움이 됩니다.
- **AddOnPage 대 AddGraphics**: 개별 추가는 `AddOnPage`를 사용하고 대량 추가는 `AddGraphics`를 사용하세요.

## 결론

이 장에서는 Aspose.PDF를 사용하여 PDF 문서 내에서 벡터 그래픽을 추출, 이동, 제거 및 추가하는 방법을 탐구했습니다. 이 기술을 마스터함으로써, PDF의 시각적 프레젠테이션을 크게 향상시키고 동적이며 시각적으로 매력적인 문서를 생성할 수 있습니다.

코드 예제를 실험해 보고 특정 사용 사례에 맞게 조정하세요. 코딩을 즐기세요!

