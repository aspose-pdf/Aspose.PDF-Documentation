---
title: C#를 사용하여 도형 주석 추가
linktitle: 도형 주석
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ko/net/figures-annotation/
description: 이 문서에서는 PDF 문서에서 도형 주석을 추가, 가져오기 및 삭제하는 방법을 설명합니다.
lastmod: "2023-09-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Figures Annotations using C#",
    "alternativeHeadline": "Enhance PDF Documents with Comprehensive Figure Annotations",
    "abstract": "Aspose.PDF for .NET의 새로운 도형 주석 기능을 소개합니다. 이 기능은 사용자가 PDF 문서에 선, 사각형, 원, 다각형 및 폴리라인을 포함한 다양한 유형의 주석을 원활하게 추가, 검색 및 삭제할 수 있도록 합니다. 이 기능은 문서의 상호작용을 향상시켜 PDF 파일 내에서 명확한 커뮤니케이션과 시각적 마크업을 가능하게 합니다. C#을 사용하는 개발자를 위해 맞춤화된 이 강력한 주석 도구 세트를 통해 PDF 편집 작업을 최적화하세요.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, figures annotations, line annotation, square annotation, circle annotation, polygon annotation, polyline annotation, free text annotation, ink annotation, Aspose.PDF for .NET",
    "wordcount": "2125",
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
    "url": "/net/figures-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/figures-annotation/"
    },
    "dateModified": "2024-11-25",
    "description": "이 문서에서는 PDF 문서에서 도형 주석을 추가, 가져오기 및 삭제하는 방법을 설명합니다."
}
</script>

PDF 문서 관리 앱은 문서에 주석을 달기 위한 다양한 도구를 제공합니다. PDF의 내부 구조 관점에서 이러한 도구는 주석입니다. 우리는 다음과 같은 종류의 드로잉 도구를 지원합니다.

* 선 주석 - 선과 화살표를 그리기 위한 도구.
* 사각형 주석 - 사각형과 직사각형을 그리기 위한 도구.
* 원 주석 - 타원과 원을 그리기 위한 도구.
* 자유 텍스트 주석 - 주석을 위한 콜아웃.
* 다각형 주석 - 다각형과 구름을 그리기 위한 도구.
* 폴리라인 주석 - 연결된 선을 그리기 위한 도구.

## 페이지에 도형 및 도형 추가하기

주석을 추가하는 접근 방식은 모든 경우에 일반적입니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

1. PDF 파일을 로드하거나 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)를 사용하여 새로 만듭니다.
1. 새 주석을 만들고 매개변수(새 Rectangle, 새 Point, 제목, 색상, 너비 등)를 설정합니다.
1. 새 [PopupAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/popupannotation/methods/index)를 만듭니다.
1. 팝업 주석을 원본 주석과 연결합니다.
1. 페이지에 주석을 추가합니다.

## 선 또는 화살표 추가하기

선 주석의 목적은 페이지에 간단한 선이나 화살표를 표시하는 것입니다.
선을 만들기 위해서는 새로운 LineAnnotation 객체가 필요합니다.  
LineAnnotation 클래스의 생성자는 네 개의 매개변수를 받습니다:

* 주석이 추가될 페이지.
* 주석의 경계를 정의하는 사각형.
* 선의 시작과 끝을 정의하는 두 점.

또한 몇 가지 속성을 초기화해야 합니다:

* `Title` - 일반적으로 이 주석을 작성한 사용자의 이름입니다.
* `Subject` - 임의의 문자열일 수 있지만 일반적으로 주석의 이름입니다.

선을 스타일링하기 위해 색상, 너비, 시작 스타일 및 종료 스타일을 설정해야 합니다. 이러한 속성은 PDF 뷰어에서 주석이 어떻게 보이고 동작하는지를 제어합니다. 예를 들어, `StartingStyle` 및 `EndingStyle` 속성은 선의 끝에 그려질 모양(예: 열린 화살표, 닫힌 화살표, 원 등)을 결정합니다.

다음 코드 스니펫은 PDF 파일에 선 주석을 추가하는 방법을 보여줍니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddLineAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments.pdf"))
    {
        // Create Line Annotation
        var lineAnnotation = new Aspose.Pdf.Annotations.LineAnnotation(
            document.Pages[1],
            new Aspose.Pdf.Rectangle(550, 93, 562, 439),
            new Aspose.Pdf.Point(556, 99), new Aspose.Pdf.Point(556, 443))
        {
            Title = "John Smith",
            Color = Aspose.Pdf.Color.Red,
            Width = 3,
            StartingStyle = Aspose.Pdf.Annotations.LineEnding.OpenArrow,
            EndingStyle = Aspose.Pdf.Annotations.LineEnding.OpenArrow,
            Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(842, 124, 1021, 266))
        };

        // Add annotation to the page
        document.Pages[1].Annotations.Add(lineAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddLineAnnotation_out.pdf");
    }
}
```

## 사각형 또는 원 추가하기

[사각형](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/squareannotation) 및 [원](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/circleannotation) 주석은 페이지에 사각형 또는 타원을 표시합니다. 열면 관련 메모의 텍스트가 포함된 팝업 창이 표시됩니다. 사각형 주석은 원 주석(Aspose. Pdf. Annotations. CircleAnnotation 클래스의 인스턴스)과 모양을 제외하고 유사합니다.

### 원 주석 추가하기

새로운 원 또는 타원 주석을 그리기 위해서는 새로운 CircleAnnotation 객체를 생성해야 합니다. `CircleAnnotation` 클래스의 생성자는 두 개의 매개변수를 받습니다:

* 주석이 추가될 페이지.
* 주석의 경계를 정의하는 사각형.

또한 `CircleAnnotation` 객체의 제목, 색상, 내부 색상, 불투명도와 같은 몇 가지 속성을 설정할 수 있습니다. 이러한 속성은 PDF 뷰어에서 주석이 어떻게 보이고 동작하는지를 제어합니다. 여기서 및 이후의 사각형에서 `InteriorColor` 색상은 채우기 색상이고 `Color`는 테두리 색상입니다.

### 사각형 주석 추가하기

사각형을 그리는 것은 원을 그리는 것과 동일합니다. 다음 코드 스니펫은 PDF 페이지에 원 및 사각형 주석을 추가하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddCircleAndSquareAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "appartments.pdf"))
    {
        // Create Circle Annotation
        var circleAnnotation = new Aspose.Pdf.Annotations.CircleAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(270, 160, 483, 383))
        {
            Title = "John Smith",
            Subject = "Circle",
            Color = Aspose.Pdf.Color.Red,
            InteriorColor = Aspose.Pdf.Color.MistyRose,
            Opacity = 0.5,
            Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(842, 316, 1021, 459))
        };

        // Create Square Annotation
        var squareAnnotation = new Aspose.Pdf.Annotations.SquareAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(67, 317, 261, 459))
        {
            Title = "John Smith",
            Subject = "Rectangle",
            Color = Aspose.Pdf.Color.Blue,
            InteriorColor = Aspose.Pdf.Color.BlueViolet,
            Opacity = 0.25,
            Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(842, 196, 1021, 338))
        };

        // Add annotations to the page
        document.Pages[1].Annotations.Add(circleAnnotation);
        document.Pages[1].Annotations.Add(squareAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddCircleAndSquareAnnotations_out.pdf");
    }
}
```

예를 들어, PDF 문서에 사각형 및 원 주석을 추가한 결과는 다음과 같습니다:

## 다각형 및 폴리라인 주석 추가하기

폴리 도구를 사용하면 문서에서 임의의 수의 변을 가진 도형과 윤곽선을 만들 수 있습니다.

**다각형 주석**은 페이지에 다각형을 나타냅니다. 그들은 직선으로 연결된 임의의 수의 정점을 가질 수 있습니다.
**폴리라인 주석**은 다각형과 유사하지만 첫 번째와 마지막 정점이 암묵적으로 연결되지 않는다는 점이 다릅니다.

### 다각형 주석 추가하기

PolygonAnnotation은 다각형 주석을 담당합니다. PolygonAnnotation 클래스의 생성자는 세 개의 매개변수를 받습니다:

* 주석이 추가될 페이지.
* 주석의 경계를 정의하는 사각형.
* 다각형의 정점을 정의하는 점 배열.

`Color`와 `InteriorColor`는 각각 테두리와 채우기 색상에 사용됩니다.

### 폴리라인 주석 추가하기

PolygonAnnotation은 다각형 주석을 담당합니다. PolygonAnnotation 클래스의 생성자는 세 개의 매개변수를 받습니다:

* 주석이 추가될 페이지.
* 주석의 경계를 정의하는 사각형.
* 다각형의 정점을 정의하는 점 배열.

`PolygonAnnotation` 대신 이 도형을 채울 수 없으므로 `InteriorColor`를 사용할 필요가 없습니다.

다음 코드 스니펫은 PDF 파일에 다각형 및 폴리라인 주석을 추가하는 방법을 보여줍니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPolygonAndPolylineAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "appartments.pdf"))
    {
        // Create Polygon Annotation
        var polygonAnnotation = new Aspose.Pdf.Annotations.PolygonAnnotation(
            document.Pages[1],
            new Aspose.Pdf.Rectangle(270, 193, 571, 383),
            new Aspose.Pdf.Point[] {
                new Aspose.Pdf.Point(274, 381),
                new Aspose.Pdf.Point(555, 381),
                new Aspose.Pdf.Point(555, 304),
                new Aspose.Pdf.Point(570, 304),
                new Aspose.Pdf.Point(570, 195),
                new Aspose.Pdf.Point(274, 195)
            })
        {
            Title = "John Smith",
            Color = Aspose.Pdf.Color.Blue,
            InteriorColor = Aspose.Pdf.Color.BlueViolet,
            Opacity = 0.25,
            Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(842, 196, 1021, 338))
        };

        // Create Polyline Annotation
        var polylineAnnotation = new Aspose.Pdf.Annotations.PolylineAnnotation(
            document.Pages[1],
            new Aspose.Pdf.Rectangle(270, 193, 571, 383),
            new Aspose.Pdf.Point[] {
                new Aspose.Pdf.Point(545, 150),
                new Aspose.Pdf.Point(545, 190),
                new Aspose.Pdf.Point(667, 190),
                new Aspose.Pdf.Point(667, 110),
                new Aspose.Pdf.Point(626, 111)
            })
        {
            Title = "John Smith",
            Color = Aspose.Pdf.Color.Red,
            Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(842, 196, 1021, 338))
        };

        // Add annotations to the page
        document.Pages[1].Annotations.Add(polygonAnnotation);
        document.Pages[1].Annotations.Add(polylineAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddPolygonAndPolylineAnnotations_out.pdf");
    }
}
```

## 도형 가져오기

모든 주석은 `Annotations` 컬렉션에 저장됩니다. 모든 주석은 `AnnotationType` 속성을 통해 자신의 유형을 소개할 수 있습니다. 따라서 원하는 주석을 필터링하기 위해 LINQ 쿼리를 만들 수 있습니다.

### 선 주석 가져오기

아래 예제는 PDF 문서의 첫 페이지에서 모든 선 주석을 얻는 방법을 설명합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReadLineAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all line annotations from the first page
        var lineAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Line)
            .Cast<Aspose.Pdf.Annotations.LineAnnotation>();

        // Iterate through each line annotation and print its coordinates
        foreach (var la in lineAnnotations)
        {
            Console.WriteLine($"[{la.Starting.X},{la.Starting.Y}]-[{la.Ending.X},{la.Ending.Y}]");
        }
    }
}
```

### 원 주석 가져오기

아래 예제는 PDF 문서의 첫 페이지에서 모든 폴리라인 주석을 얻는 방법을 설명합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReadCircleAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all circle annotations from the first page
        var circleAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Circle)
            .Cast<Aspose.Pdf.Annotations.CircleAnnotation>();

        // Iterate through each circle annotation and print its rectangle
        foreach (var ca in circleAnnotations)
        {
            Console.WriteLine($"[{ca.Rect}]");
        }
    }
}
```

### 사각형 주석 가져오기

아래 예제는 PDF 문서의 첫 페이지에서 모든 폴리라인 주석을 얻는 방법을 설명합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReadSquareAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all square annotations from the first page
        var squareAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Square)
            .Cast<Aspose.Pdf.Annotations.SquareAnnotation>();

        // Iterate through each square annotation and print its rectangle
        foreach (var sq in squareAnnotations)
        {
            Console.WriteLine($"[{sq.Rect}]");
        }
    }
}
```

### 폴리라인 주석 가져오기

아래 예제는 PDF 문서의 첫 페이지에서 모든 폴리라인 주석을 얻는 방법을 설명합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReadPolylineAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all polyline annotations from the first page
        var polyAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.PolyLine)
            .Cast<Aspose.Pdf.Annotations.PolylineAnnotation>();

        // Iterate through each polyline annotation and print its rectangle
        foreach (var pa in polyAnnotations)
        {
            Console.WriteLine($"[{pa.Rect}]");
        }
    }
}
```

### 다각형 주석 가져오기

아래 예제는 PDF 문서의 첫 페이지에서 모든 다각형 주석을 얻는 방법을 설명합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReadPolygonAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all polygon annotations from the first page
        var polyAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Polygon)
            .Cast<Aspose.Pdf.Annotations.PolygonAnnotation>();

        // Iterate through each polygon annotation and print its rectangle
        foreach (var pa in polyAnnotations)
        {
            Console.WriteLine($"[{pa.Rect}]");
        }
    }
}
```

## 도형 삭제하기

PDF에서 주석을 제거하는 접근 방식은 매우 간단합니다:

* 삭제할 주석을 선택합니다(컬렉션을 만듭니다).
* foreach 루프를 사용하여 컬렉션을 반복하고 Delete 메서드를 사용하여 각 주석을 주석 컬렉션에서 삭제합니다.

### 선 주석 삭제하기

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteLineAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all line annotations from the first page
        var lineAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Line)
            .Cast<Aspose.Pdf.Annotations.LineAnnotation>();

        // Iterate through each line annotation and delete it
        foreach (var la in lineAnnotations)
        {
            document.Pages[1].Annotations.Delete(la);
        }

        // Save PDF document
        document.Save(dataDir + "DeleteLineAnnotations_out.pdf");
    }
}
```

### 원 및 사각형 주석 삭제하기

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteCircleAndSquareAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all circle and square annotations from the first page
        var figures = document.Pages[1].Annotations
            .Where(a =>
                a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Circle
                || a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Square);

        // Iterate through each figure annotation and delete it
        foreach (var fig in figures)
        {
            document.Pages[1].Annotations.Delete(fig);
        }

        // Save PDF document
        document.Save(dataDir + "DeleteCircleAndSquareAnnotations_out.pdf");
    }
}
```

### 다각형 및 폴리라인 주석 삭제하기

다음 코드 스니펫은 PDF 파일에서 다각형 및 폴리라인 주석을 삭제하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeletePolylineAndPolygonAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        // Get all polyline and polygon annotations from the first page
        var polyAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.PolyLine
                        || a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Polygon);

        // Iterate through each polyline or polygon annotation and delete it
        foreach (var pa in polyAnnotations)
        {
            document.Pages[1].Annotations.Delete(pa);
        }

        // Save PDF document
        document.Save(dataDir + DeletePolylineAndPolygonAnnotations_out.pdf");
    }
}
```

## PDF 파일에 잉크 주석 추가하는 방법

잉크 주석은 하나 이상의 분리된 경로로 구성된 자유형 "낙서"를 나타냅니다. 열면 관련 메모의 텍스트가 포함된 팝업 창이 표시됩니다.

[InkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/inkannotation)는 하나 이상의 분리된 점으로 구성된 자유형 낙서를 나타냅니다. PDF 문서에 InkAnnotation을 추가하기 위해 다음 코드 스니펫을 사용해 보세요.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddInkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "appartments.pdf"))
    {
        // Get first page
        var page = document.Pages[1];

        // Define the rectangle for the ink annotation
        var arect = new Aspose.Pdf.Rectangle(156.574, 521.316, 541.168, 575.703);

        // Create a list of ink paths
        IList<Aspose.Pdf.Point[]> inkList = new List<Aspose.Pdf.Point[]>();
        var arrpt = new[]
        {
            new Aspose.Pdf.Point(209.727, 542.263),
            new Aspose.Pdf.Point(209.727, 541.94),
            new Aspose.Pdf.Point(209.727, 541.616)
        };
        inkList.Add(arrpt);

        // Create the ink annotation
        var ia = new Aspose.Pdf.Annotations.InkAnnotation(page, arect, inkList)
        {
            Title = "John Smith",
            Subject = "Pencil",
            Color = Aspose.Pdf.Color.LightBlue,
            CapStyle = Aspose.Pdf.Annotations.CapStyle.Rounded,
            Opacity = 0.5
        };

        // Set the border for the annotation
        var border = new Aspose.Pdf.Annotations.Border(ia)
        {
            Width = 25
        };
        ia.Border = border;

        // Add the annotation to the page
        page.Annotations.Add(ia);

        // Save PDF document
        document.Save(dataDir + "AddInkAnnotation_out.pdf");
    }
}
```

### InkAnnotation의 선 너비 설정하기

[InkAnnottion](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/inkannotation)의 너비는 LineInfo 및 Border 객체를 사용하여 변경할 수 있습니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddInkAnnotationWithLineWidth()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create a list of ink paths
        IList<Aspose.Pdf.Point[]> inkList = new List<Aspose.Pdf.Point[]>();

        // Define line information
        var lineInfo = new Aspose.Pdf.Facades.LineInfo
        {
            VerticeCoordinate = new float[] { 55, 55, 70, 70, 70, 90, 150, 60 },
            Visibility = true,
            LineColor = System.Drawing.Color.Red,
            LineWidth = 2
        };

        // Convert line coordinates to Aspose.Pdf.Point array
        int length = lineInfo.VerticeCoordinate.Length / 2;
        var gesture = new Aspose.Pdf.Point[length];
        for (int i = 0; i < length; i++)
        {
            gesture[i] = new Aspose.Pdf.Point(lineInfo.VerticeCoordinate[2 * i], lineInfo.VerticeCoordinate[2 * i + 1]);
        }

        // Add the gesture to the ink list
        inkList.Add(gesture);

        // Create the ink annotation
        var a1 = new Aspose.Pdf.Annotations.InkAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), inkList)
        {
            Subject = "Test",
            Title = "Title",
            Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green)
        };

        // Set the border for the annotation
        var border = new Aspose.Pdf.Annotations.Border(a1)
        {
            Width = 3,
            Effect = Aspose.Pdf.Annotations.BorderEffect.Cloudy,
            Dash = new Aspose.Pdf.Annotations.Dash(1, 1),
            Style = Aspose.Pdf.Annotations.BorderStyle.Solid
        };
        a1.Border = border;

        // Add the annotation to the page
        page.Annotations.Add(a1);

        // Save PDF document
        document.Save(dataDir + "lnkAnnotationLineWidth_out.pdf");
    }
}
```

### 원 주석 삭제하기

다음 코드 스니펫은 PDF 파일에서 원 주석을 삭제하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteCircleAnnotation()
{
	// The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
	
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments_mod.pdf"))
    {
        var circleAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == AnnotationType.Circle)
            .Cast<Aspose.Pdf.Annotations.CircleAnnotation>();

        foreach (var ca in circleAnnotations)
        {
            document.Pages[1].Annotations.Delete(ca);
        }

        // Save PDF document
        document.Save(dataDir + "DeleteCircleAnnotation_out.pdf");
    }
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