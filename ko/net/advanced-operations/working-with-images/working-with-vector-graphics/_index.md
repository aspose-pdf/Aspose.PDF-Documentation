---
title: 벡터 그래픽 작업
linktitle: 벡터 그래픽 작업
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 120
url: /ko/net/working-with-vector-graphics/
description: 이 문서에서는 C#을 사용하여 GraphicsAbsorber 도구로 작업하는 기능을 설명합니다.
lastmod: "2024-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Vector Graphics in PDF",
    "alternativeHeadline": "Programmatically manipulate PDF vector graphics",
    "abstract": "새로운 GraphicsAbsorber 클래스를 사용하여 PDF 문서에서 벡터 그래픽을 프로그래밍 방식으로 조작합니다. Aspose.PDF for .NET C# 라이브러리는 그래픽 요소에 대한 정밀한 제어를 가능하게 하여 그래픽을 이동, 제거 및 추가하는 등의 작업을 통해 PDF 비주얼을 향상시킵니다. 이 도구는 최적의 성능을 위해 개별 및 대량 조작 방법을 제공합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "GraphicsAbsorber, Vector Graphics, PDF Manipulation, C# library, Aspose.PDF, Move Graphics, Remove Graphics, Add Graphics, PDF Vector Graphics",
    "wordcount": "967",
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
    "url": "/net/working-with-vector-graphics/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-vector-graphics/"
    },
    "dateModified": "2024-11-26",
    "description": "이 섹션에서는 C# 라이브러리를 사용하여 GraphicsAbsorber PDF 파일로 작업하는 기능을 설명합니다."
}
</script>

이 장에서는 PDF 문서 내에서 벡터 그래픽과 상호작용하기 위해 강력한 `GraphicsAbsorber` 클래스를 사용하는 방법을 살펴보겠습니다. 그래픽을 이동, 제거 또는 추가해야 하는 경우 이 가이드는 이러한 작업을 효과적으로 수행하는 방법을 보여줍니다. 시작해 보겠습니다!

## 소개<a name="introduction"></a>

벡터 그래픽은 이미지, 도형 및 기타 그래픽 요소를 나타내는 데 사용되는 많은 PDF 문서의 중요한 구성 요소입니다. Aspose.PDF는 개발자가 이러한 그래픽에 프로그래밍 방식으로 접근하고 조작할 수 있도록 하는 `GraphicsAbsorber` 클래스를 제공합니다. `GraphicsAbsorber`의 `Visit` 메서드를 사용하면 지정된 페이지에서 벡터 그래픽을 추출하고 이동, 제거 또는 다른 페이지로 복사하는 등의 다양한 작업을 수행할 수 있습니다.

## 1. `GraphicsAbsorber`로 그래픽 추출하기<a name="extracting-graphics"></a>

벡터 그래픽 작업의 첫 번째 단계는 PDF 문서에서 그래픽을 추출하는 것입니다. 다음은 `GraphicsAbsorber` 클래스를 사용하여 이를 수행하는 방법입니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UsingGraphicsAbsorber()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Sample-Document-01.pdf"))
    {
        // Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Select the first page of the document
            var page = document.Pages[1];

            // Use the `Visit` method to extract graphics from the page
            graphicsAbsorber.Visit(page);

            // Display information about the extracted elements
            foreach (var element in graphicsAbsorber.Elements)
            {
                Console.WriteLine($"Page Number: {element.SourcePage.Number}");
                Console.WriteLine($"Position: ({element.Position.X}, {element.Position.Y})");
                Console.WriteLine($"Number of Operators: {element.Operators.Count}");
            }
        }
    }
}

```

### 설명:

1. **문서 객체 생성**: 대상 PDF 파일의 경로로 새 `Document` 객체를 인스턴스화합니다.
2. **`GraphicsAbsorber` 인스턴스 생성**: 이 클래스는 지정된 페이지에서 모든 그래픽 요소를 캡처합니다.
3. **방문 메서드**: 첫 번째 페이지에서 `Visit` 메서드를 호출하여 `GraphicsAbsorber`가 벡터 그래픽을 흡수하도록 합니다.
4. **추출된 요소 반복**: 코드는 각 추출된 요소를 반복하며 페이지 번호, 위치 및 관련 드로잉 연산자의 수와 같은 정보를 출력합니다.

## 2. 그래픽 이동하기<a name="moving-graphics"></a>

그래픽을 추출한 후에는 동일한 페이지에서 다른 위치로 이동할 수 있습니다. 다음은 이를 달성하는 방법입니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MoveGraphics()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "MoveGraphics.pdf"))
    {
        // Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the first page of the document
            var page = document.Pages[1];

            // Use the `Visit` method to extract graphics from the page
            graphicsAbsorber.Visit(page);

            // Temporarily suspend updates to improve performance
            graphicsAbsorber.SuppressUpdate();

            // Move graphics by shifting their X and Y coordinates
            foreach (var element in graphicsAbsorber.Elements)
            {
                var position = element.Position;
                element.Position = new Aspose.Pdf.Point(position.X + 150, position.Y - 10);
            }

            // Resume updates and apply changes
            graphicsAbsorber.ResumeUpdate();

            // Save PDF document
            document.Save(dataDir + "MoveGraphics_out.pdf");
        }
    }
}
```

### 주요 사항:

- **SuppressUpdate**: 이 메서드는 여러 변경을 수행할 때 성능을 개선하기 위해 업데이트를 일시적으로 중단합니다.
- **ResumeUpdate**: 이 메서드는 업데이트를 재개하고 그래픽의 위치에 대한 변경 사항을 적용합니다.
- **요소 위치 지정**: 각 그래픽의 위치는 `X` 및 `Y` 좌표를 변경하여 조정됩니다.

## 3. 그래픽 제거하기<a name="removing-graphics"></a>

특정 그래픽을 페이지에서 제거해야 하는 경우가 있습니다. Aspose.PDF는 이를 수행하기 위한 두 가지 방법을 제공합니다:

### 방법 1: 사각형 경계 사용

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveGraphicsMethod1()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RemoveGraphics.pdf"))
    {
        // Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the first page of the document
            var page = document.Pages[1];

            // Extract graphic elements from the page
            graphicsAbsorber.Visit(page);

            // Define the rectangle within which graphics will be removed
            var rectangle = new Aspose.Pdf.Rectangle(70, 248, 170, 252);

            // Temporarily suppress updates for better performance
            graphicsAbsorber.SuppressUpdate();

            // Iterate through the extracted graphic elements and remove those inside the rectangle
            foreach (var element in graphicsAbsorber.Elements)
            {
                if (rectangle.Contains(element.Position))
                {
                    element.Remove(); // Remove the graphic element
                }
            }

            // Resume updates and apply changes
            graphicsAbsorber.ResumeUpdate();

            // Save PDF document
            document.Save(dataDir + "RemoveGraphics_out.pdf");
        }
    }
}
```

### 방법 2: 제거된 요소의 컬렉션 사용

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveGraphicsMethod2()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RemoveGraphics.pdf"))
    {
        // Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the first page of the document
            var page = document.Pages[1];

            // Define the rectangle within which graphics will be removed
            var rectangle = new Aspose.Pdf.Rectangle(70, 248, 170, 252);

            // Extract graphic elements from the page
            graphicsAbsorber.Visit(page);

            // Create a collection to store the removed elements
            var removedElementsCollection = new Aspose.Pdf.Vector.GraphicElementCollection();

            // Iterate through the extracted elements and add those inside the rectangle to the collection
            foreach (var item in graphicsAbsorber.Elements.Where(el => rectangle.Contains(el.Position)))
            {
                removedElementsCollection.Add(item);
            }

            // Temporarily suppress updates for better performance
            page.Contents.SuppressUpdate();

            // Delete the graphics elements from the page
            page.DeleteGraphics(removedElementsCollection);

            // Resume updates and apply changes
            page.Contents.ResumeUpdate();

            // Save PDF document
            document.Save(dataDir + "RemoveGraphics_out.pdf");
        }
    }
}
```

### 설명:

- **사각형 경계**: 제거할 그래픽을 지정하기 위해 사각형 영역을 정의합니다.
- **업데이트 중단 및 재개**: 중간 렌더링 없이 효율적으로 제거할 수 있도록 합니다.

## 4. 다른 페이지에 그래픽 추가하기<a name="adding-graphics"></a>

한 페이지에서 흡수된 그래픽은 동일한 문서 내의 다른 페이지에 추가할 수 있습니다. 이를 달성하는 두 가지 방법은 다음과 같습니다:

### 방법 1: 개별적으로 그래픽 추가하기

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddToAnotherPageMethod1()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddToAnotherPage.pdf"))
    {
        // Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the pages from the document
            var page1 = document.Pages[1];
            var page2 = document.Pages[2];

            // Extract graphics from the first page
            graphicsAbsorber.Visit(page1);

            // Temporarily suppress updates for better performance
            page2.Contents.SuppressUpdate();

            // Add each graphic element to the second page
            foreach (var element in graphicsAbsorber.Elements)
            {
                element.AddOnPage(page2); // Add each graphic element to the second page
            }

            // Resume updates and apply changes
            page2.Contents.ResumeUpdate();

            // Save PDF document
            document.Save(dataDir + "AddToAnotherPage_out.pdf");
        }
    }
}
```

### 방법 2: 컬렉션으로 그래픽 추가하기

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddToAnotherPageMethod2()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddToAnotherPage.pdf"))
    {
        // Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the pages from the document
            var page1 = document.Pages[1];
            var page2 = document.Pages[2];

            // Extract graphics from the first page
            graphicsAbsorber.Visit(page1);

            // Temporarily suppress updates for better performance
            page2.Contents.SuppressUpdate();

            // Add all graphics elements to the second page at once
            page2.AddGraphics(graphicsAbsorber.Elements);

            // Resume updates and apply changes
            page2.Contents.ResumeUpdate();

            // Save PDF document
            document.Save(dataDir + "AddToAnotherPage_out.pdf");
        }
    }
}
```

### 주요 사항:

- **SuppressUpdate 및 ResumeUpdate**: 이러한 메서드는 대량 변경을 수행할 때 성능을 유지하는 데 도움이 됩니다.
- **AddOnPage 대 AddGraphics**: 개별 추가에는 `AddOnPage`를 사용하고 대량 추가에는 `AddGraphics`를 사용합니다.

## 결론

이 장에서는 Aspose.PDF를 사용하여 PDF 문서 내에서 벡터 그래픽을 추출, 이동, 제거 및 추가하는 방법을 살펴보았습니다. 이러한 기술을 마스터하면 PDF의 시각적 표현을 크게 향상시키고 동적이고 시각적으로 매력적인 문서를 만들 수 있습니다.

코드 예제를 실험하고 특정 사용 사례에 맞게 조정해 보세요. 즐거운 코딩 되세요!

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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
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