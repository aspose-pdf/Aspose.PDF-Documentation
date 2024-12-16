---
title: C#을 사용하여 도형 주석 추가
linktitle: 도형 주석
type: docs
weight: 30
url: /ko/net/figures-annotation/
description: 이 글은 Aspose.PDF for .NET을 사용하여 PDF 문서에서 도형 주석을 추가, 가져오기 및 삭제하는 방법을 설명합니다.
lastmod: "2023-09-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "C#을 사용하여 도형 주석 추가",
    "alternativeHeadline": "PDF에서 도형 주석 추가 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, c#, 도형 주석, 다각형 주석, 선 주석, 사각형 주석, 원 주석",
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
    "url": "/net/figures-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/figures-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "이 글은 Aspose.PDF for .NET을 사용하여 PDF 문서에서 도형 주석을 추가, 가져오기 및 삭제하는 방법을 설명합니다."
}
</script>

PDF 문서 관리 앱은 문서에 주석을 달기 위한 다양한 도구를 제공합니다. PDF의 내부 구조에서 볼 때, 이러한 도구들은 주석입니다. 다음과 같은 종류의 그리기 도구를 지원합니다.

* 선 주석 - 선과 화살표를 그리는 도구
* 사각형 주석 - 사각형과 직사각형을 그리기 위한 도구
* 원 주석 - 타원과 원을 그리기 위한 도구
* 자유 텍스트 주석 - 콜아웃 코멘트를 위한 도구
* 다각형 주석 - 다각형과 구름 모양을 그리기 위한 도구
* 폴리라인 주석 - 연결된 선을 그리기 위한 도구

## 페이지에 도형과 그림 추가하기

주석을 추가하는 접근 방식은 모든 주석에 대해 일반적입니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

1. [문서](https://reference.aspose.com/pdf/net/aspose.pdf/document)를 통해 PDF 파일을 불러오거나 새로 만듭니다.
1. 새 주석을 생성하고 매개변수를 설정합니다(새로운 사각형, 새로운 포인트, 제목, 색상, 너비 등).
1. 원본과 링크 팝업 주석을 연결합니다.
1. 페이지에 주석을 추가합니다.

## 선이나 화살표 추가하기

선 주석의 목적은 페이지에 직선이나 화살표를 표시하는 것입니다.
선을 생성하려면 새 LineAnnotation 객체가 필요합니다.
LineAnnotation 클래스의 생성자는 네 가지 매개변수를 받습니다:

* 주석이 추가될 페이지,
* 주석의 경계를 정의하는 사각형,
* 선의 시작과 끝을 정의하는 두 점.

또한 몇 가지 속성을 초기화할 필요가 있습니다:

* `Title` - 보통 이 주석을 만든 사용자의 이름입니다.
* `Subject` - 어떤 문자열도 될 수 있지만 일반적으로 주석의 이름입니다.

선을 스타일링하려면 색상, 너비, 시작 스타일, 종료 스타일을 설정해야 합니다.
선을 스타일링하기 위해서는 색상, 너비, 시작 스타일 및 종료 스타일을 설정해야 합니다.

다음 코드 스니펫은 PDF 파일에 선 주석을 추가하는 방법을 보여줍니다:

```csharp
// PDF 파일 로드
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments.pdf"));

// 선 주석 생성
var lineAnnotation = new LineAnnotation(
    document.Pages[1],
    new Rectangle(550, 93, 562, 439),
    new Point(556, 99), new Point(556, 443))
{
    Title = "John Smith",
    Color = Color.Red,
    Width = 3,
    StartingStyle = LineEnding.OpenArrow,
    EndingStyle = LineEnding.OpenArrow,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 124, 1021, 266))
};

// 페이지에 주석 추가
document.Pages[1].Annotations.Add(lineAnnotation);
document.Save(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
```

## 사각형 또는 원 추가

[Square](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/squareannotation) 및 [Circle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/circleannotation) 주석은 페이지에 사각형 또는 타원을 표시합니다.
[Square](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/squareannotation) 및 [Circle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/circleannotation) 주석은 페이지에 사각형이나 타원을 표시합니다.

### 원 주석 추가하기

새로운 원이나 타원 주석을 그리려면 새 CircleAnnotation 객체를 생성해야 합니다. `CircleAnnotation` 클래스의 생성자는 두 개의 매개변수를 받습니다:

* 주석이 추가될 페이지,
* 주석의 경계를 정의하는 사각형

또한 `CircleAnnotation` 객체의 몇 가지 속성을 설정할 수 있습니다. 예를 들어 제목, 색상, 내부 색상, 불투명도 등이 있습니다. 이러한 속성은 PDF 뷰어에서 주석의 모양과 동작을 제어합니다. 여기서 그리고 Square에서 `InteriorColor` 색상은 채우기 색상이고 `Color`는 테두리 색상입니다.

### 사각형 주석 추가하기

사각형을 그리는 것은 원을 그리는 것과 같습니다.
사각형을 그리는 것은 원을 그리는 것과 같습니다.

```csharp
var dataDir = "<path-to-file>";
// PDF 파일을 불러옵니다
Document document = new Document(System.IO.Path.Combine(dataDir, "appartments.pdf"));

// 원형 주석 생성
var circleAnnotation = new CircleAnnotation(document.Pages[1], new Rectangle(270, 160, 483, 383))
{
    Title = "John Smith",
    Subject = "Circle",
    Color = Color.Red,
    InteriorColor = Color.MistyRose,
    Opacity = 0.5,        
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 316, 1021, 459))
};

// 사각형 주석 생성
var squareAnnotation = new SquareAnnotation(document.Pages[1], new Rectangle(67, 317, 261, 459))
{
    Title = "John Smith",
    Subject = "Rectangle",
    Color = Color.Blue,
    InteriorColor = Color.BlueViolet,
    Opacity = 0.25,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 196, 1021, 338))
};

// 페이지에 주석 추가
document.Pages[1].Annotations.Add(circleAnnotation);
document.Pages[1].Annotations.Add(squareAnnotation);
document.Save(System.IO.Path.Combine(dataDir, "appartments_mod.pdf"));
```
예를 들어, PDF 문서에 사각형 및 원형 주석을 추가한 결과는 다음과 같습니다:

![Circle and Square Annotation demo](circle_demo.png)

## 다각형 및 폴리라인 주석 추가

Poly- 도구를 사용하면 문서에 임의의 면수를 가진 도형 및 윤곽을 생성할 수 있습니다.

**다각형 주석**은 페이지에 다각형을 나타냅니다. 직선으로 연결된 임의의 수의 꼭짓점을 가질 수 있습니다.
**폴리라인 주석**도 다각형과 유사하지만, 첫 번째 꼭짓점과 마지막 꼭짓점이 암시적으로 연결되지 않는 것이 유일한 차이점입니다.

### 다각형 주석 추가

PolygonAnnotation은 다각형 주석을 담당합니다. PolygonAnnotation 클래스의 생성자는 세 가지 매개 변수를 사용합니다:

* 주석이 추가될 페이지,
* 주석의 경계를 정의하는 직사각형,
* 다각형의 꼭짓점을 정의하는 점 배열.

`Color` 및 `InteriorColor`는 각각 테두리 및 채우기 색상에 사용됩니다.

### 폴리라인 주석 추가
### 폴리라인 주석 추가

PolygonAnnotation은 다각형 주석을 담당합니다. PolygonAnnotation 클래스의 생성자는 세 가지 매개변수를 사용합니다:

* 주석이 추가될 페이지,
* 주석의 경계를 정의하는 사각형,
* 다각형의 꼭짓점을 정의하는 점 배열.

PolygonAnnotation 대신 이 모양을 채울 수 없으므로 `InteriorColor`를 사용할 필요가 없습니다.

다음 코드 스니펫은 PDF 파일에 다각형 및 폴리라인 주석을 추가하는 방법을 보여줍니다:

```csharp
// PDF 파일 로드
Document document = new Document(System.IO.Path.Combine(dataDir, "appartments.pdf"));

// 다각형 주석 생성
var polygonAnnotation = new PolygonAnnotation(document.Pages[1],
    new Rectangle(270, 193, 571, 383),
    new Point[] {
        new Point(274, 381),
        new Point(555, 381),
        new Point(555, 304),
        new Point(570, 304),
        new Point(570, 195),
        new Point(274, 195)})
{
    Title = "John Smith",
    Color = Color.Blue,
    InteriorColor = Color.BlueViolet,
    Opacity = 0.25,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 196, 1021, 338))
};

// 폴리라인 주석 생성
var polylineAnnotation = new PolylineAnnotation(document.Pages[1],
    new Rectangle(270, 193, 571, 383),
    new Point[] {
        new Point(545,150),
        new Point(545,190),
        new Point(667,190),
        new Point(667,110),
        new Point(626,111)
        })
{
    Title = "John Smith",
    Color = Color.Red,
    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 196, 1021, 338))
};

// 페이지에 주석 추가
document.Pages[1].Annotations.Add(polygonAnnotation);
document.Pages[1].Annotations.Add(polylineAnnotation);
document.Save(System.IO.Path.Combine(dataDir, "appartments_mod.pdf"));
```
## 도형 가져오기

모든 주석은 `Annotations` 컬렉션에 저장됩니다. 모든 주석은 `AnnotationType` 속성을 통해 자신의 유형을 나타낼 수 있습니다. 따라서 원하는 주석을 필터링하기 위한 LINQ 쿼리를 만들 수 있습니다.

### 선 주석 가져오기

아래 예제는 PDF 문서의 첫 페이지에서 모든 선 주석을 가져오는 방법을 설명합니다.

```csharp
// PDF 파일을 불러옵니다
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var lineAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Line)
    .Cast<LineAnnotation>();
foreach (var la in lineAnnotations)
{
    Console.WriteLine($"[{la.Starting.X},{la.Starting.Y}]-[{la.Ending.X},{la.Ending.Y}]");
}   
```

### 원 주석 가져오기

아래 예제는 PDF 문서의 첫 페이지에서 모든 원 주석을 가져오는 방법을 설명합니다.

```csharp
// PDF 파일을 불러옵니다
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var circleAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Line)
    .Cast<CircleAnnotation>();
foreach (var ca in circleAnnotations)
{
    Console.WriteLine($"[{ca.Rect}]");
}   
```
### 사각형 주석 가져오기

아래 예제는 PDF 문서 첫 페이지의 모든 사각형 주석을 얻는 방법을 설명합니다.

```csharp
// PDF 파일 로드
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var squareAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Square)
    .Cast<SquareAnnotation>();
foreach (var sq in squareAnnotations)
{
    Console.WriteLine($"[{sq.Rect}]");
}
```

### 폴리라인 주석 가져오기

아래 예제는 PDF 문서 첫 페이지의 모든 폴리라인 주석을 얻는 방법을 설명합니다.

```csharp
// PDF 파일 로드
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var polyAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.PolyLine)
    .Cast<PolylineAnnotation>();
foreach (var pa in polyAnnotations)
{
    Console.WriteLine($"[{pa.Rect}]");
}
```

### 다각형 주석 가져오기
아래 예시는 PDF 문서의 첫 페이지에서 모든 폴리곤 주석을 가져오는 방법을 설명합니다.

```csharp
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var polyAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Polygon)
    .Cast<PolygonAnnotation>();
foreach (var pa in polyAnnotations)
{
    Console.WriteLine($"[{pa.Rect}]");
} 
```

## 도형 삭제

PDF에서 주석을 삭제하는 방법은 매우 간단합니다:

* 삭제할 주석 선택 (몇몇 컬렉션 만들기)
* foreach 루프를 사용하여 컬렉션을 반복하고 Delete 메소드를 사용하여 주석 컬렉션에서 각 주석을 삭제합니다.

### 선 주석 삭제

```csharp
// PDF 파일을 로드합니다
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var lineAnnotations = document.Pages[1].Annotations
    .Where(a => a.AnnotationType == AnnotationType.Line)
    .Cast<LineAnnotation>();

foreach (var la in lineAnnotations)
{
    document.Pages[1].Annotations.Delete(la);
}
```
### 원 및 사각형 주석 삭제

```csharp
// PDF 파일 로드
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var figures = document.Pages[1].Annotations
    .Where(a =>
        a.AnnotationType == AnnotationType.Circle
        || a.AnnotationType == AnnotationType.Square);

foreach (var fig in figures)
{
    document.Pages[1].Annotations.Delete(fig);
}
document.Save(System.IO.Path.Combine(_dataDir, "Appartments_del.pdf"));
```

### 다각형 및 폴리라인 주석 삭제

PDF 파일에서 다각형 및 폴리라인 주석을 삭제하는 방법을 보여주는 코드 스니펫입니다.

```csharp
// PDF 파일 로드
Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
var polyAnnotations = document.Pages[1].Annotations
                .Where(a => a.AnnotationType == AnnotationType.PolyLine
                || a.AnnotationType == AnnotationType.Polygon);

foreach (var pa in polyAnnotations)
{
    document.Pages[1].Annotations.Delete(pa);
}
document.Save(System.IO.Path.Combine(_dataDir, "Appartments_del.pdf"));
```
## PDF 파일에 잉크 주석 추가하기

잉크 주석은 하나 이상의 분리된 경로로 구성된 자유형 "낙서"를 나타냅니다. 열면 관련 노트의 텍스트가 포함된 팝업 창이 표시됩니다.

[InkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/inkannotation)은 하나 이상의 분리된 점으로 구성된 자유형 낙서를 나타냅니다. 다음 코드 스니펫을 사용하여 PDF 문서에 InkAnnotation을 추가해 보세요.

```csharp
// PDF 파일 로드
Document document = new Document(System.IO.Path.Combine(_dataDir, "appartments.pdf"));
Page page = document.Pages[1];

Rectangle arect = new Rectangle(156.574, 521.316, 541.168, 575.703);

IList<Point[]> inkList = new List<Point[]>();
Point[] arrpt = new[]
{
    new Point(209.727,542.263),
    new Point(209.727,541.94),
    new Point(209.727,541.616)
};
inkList.Add(arrpt);

InkAnnotation ia = new InkAnnotation(page, arect, inkList)
{
    Title = "John Smith",
    Subject = "Pencil",
    Color = Color.LightBlue,
    CapStyle = CapStyle.Rounded,
    Opacity = 0.5
};
Border border = new Border(ia)
{
    Width = 25
};
ia.Border = border;
page.Annotations.Add(ia);

// 출력 파일 저장
document.Save(System.IO.Path.Combine(_dataDir, "appartments_mod.pdf"));
```
### InkAnnotation의 선 너비 설정

[InkAnnottion](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/inkannotation)의 너비는 LineInfo와 Border 객체를 사용하여 변경할 수 있습니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인해주세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

Document doc = new Document();
doc.Pages.Add();
IList<Point[]> inkList = new List<Point[]>();
LineInfo lineInfo = new LineInfo();
lineInfo.VerticeCoordinate = new float[] { 55, 55, 70, 70, 70, 90, 150, 60 };
lineInfo.Visibility = true;
lineInfo.LineColor = System.Drawing.Color.Red;
lineInfo.LineWidth = 2;
int length = lineInfo.VerticeCoordinate.Length / 2;
Aspose.Pdf.Point[] gesture = new Aspose.Pdf.Point[length];
for (int i = 0; i < length; i++)
{
   gesture[i] = new Aspose.Pdf.Point(lineInfo.VerticeCoordinate[2 * i], lineInfo.VerticeCoordinate[2 * i + 1]);
}

inkList.Add(gesture);
InkAnnotation a1 = new InkAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), inkList);
a1.Subject = "Test";
a1.Title = "Title";
a1.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
Border border = new Border(a1);
border.Width = 3;
border.Effect = BorderEffect.Cloudy;
border.Dash = new Dash(1, 1);
border.Style = BorderStyle.Solid;
doc.Pages[1].Annotations.Add(a1);

dataDir = dataDir + "lnkAnnotationLineWidth_out.pdf";
// 출력 파일 저장
doc.Save(dataDir);
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
### 원 주석 삭제하기

다음 코드 조각은 PDF 파일에서 원 주석을 삭제하는 방법을 보여줍니다.

```csharp
public static void DeleteCircleAnnotation()
{
    // PDF 파일을 불러옵니다
    Document document = new Document(System.IO.Path.Combine(dataDir, "Appartments_mod.pdf"));
    var circleAnnotations = document.Pages[1].Annotations
        .Where(a => a.AnnotationType == AnnotationType.Circle)
        .Cast<CircleAnnotation>();

    foreach (var ca in circleAnnotations)
    {
        document.Pages[1].Annotations.Delete(ca);
    }
    document.Save(System.IO.Path.Combine(dataDir, "Appartments_del.pdf"));
}
```
