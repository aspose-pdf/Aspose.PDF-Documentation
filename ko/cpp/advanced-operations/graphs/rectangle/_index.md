---
title: PDF 파일에 사각형 객체 추가
linktitle: 사각형 추가
type: docs
weight: 50
url: ko/cpp/add-rectangle/
description: 이 문서에서는 Aspose.PDF for C++를 사용하여 PDF에 사각형 객체를 생성하는 방법을 설명합니다.
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 사각형 객체 추가

Aspose.PDF for C++는 PDF 문서에 그래프 객체(예: 그래프, 선, 사각형 등)를 추가하는 기능을 지원합니다. 또한 특정 색상으로 사각형 객체를 채우고, Z-Order를 제어하고, 그라데이션 색상 채우기 등을 제공하는 [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) 객체를 추가할 수 있는 기능을 제공합니다.

먼저, 사각형 객체를 생성하는 가능성을 살펴봅시다.

다음 단계를 따르십시오:

1. 새 PDF [문서](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) 생성

1. PDF 파일의 페이지 컬렉션에 [페이지](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page/) 추가

1. [텍스트 조각](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment/)을 페이지 인스턴스의 단락 컬렉션에 추가

1. [그래프](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph/) 인스턴스 생성

1. [그리기 객체](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.drawing)의 테두리 설정

1. 사각형 인스턴스 생성

1. [사각형](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) 객체를 그래프 객체의 도형 컬렉션에 추가

1. 그래프 객체를 페이지 인스턴스의 단락 컬렉션에 추가

1. [텍스트 조각](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment/)을 페이지 인스턴스의 단락 컬렉션에 추가

1. 그리고 PDF 파일 저장

```csharp
 private static void AddRectangle(Page page, float x, float y, float width, float height, Color color, int zindex)
        {
            // 사각형 객체에 지정된 것과 동일한 치수로 그래프 객체 생성
            Aspose.Pdf.Drawing.Graph graph = new Aspose.Pdf.Drawing.Graph(width, height)
            {
                // 그래프 인스턴스의 위치를 변경할 수 있는지 여부
                IsChangePosition = false,
                // 그래프 인스턴스의 왼쪽 좌표 위치 설정
                Left = x,
                // 그래프 객체의 상단 좌표 위치 설정
                Top = y
            };
            // "그래프" 안에 사각형 추가
            Rectangle rect = new Rectangle(0, 0, width, height);
            // 사각형 채우기 색상 설정
            rect.GraphInfo.FillColor = color;
            // 그래프 객체의 색상
            rect.GraphInfo.Color = color;
            // 그래프 인스턴스의 도형 컬렉션에 사각형 추가
            graph.Shapes.Add(rect);
            // 사각형 객체의 Z-Index 설정
            graph.ZIndex = zindex;
            // 페이지 객체의 단락 컬렉션에 그래프 추가
            page.Paragraphs.Add(graph);
        }
```
![사각형 생성](create_rectangle.png)

## 채워진 사각형 객체 생성

Aspose.PDF for C++는 특정 색상으로 사각형 객체를 채우는 기능도 제공합니다.

다음 코드 스니펫은 색상으로 채워진 [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) 객체를 추가하는 방법을 보여줍니다.

```csharp
    {
        private const string _dataDir = "C:\\Samples\\";
        public static void RectangleFilled()
        {
            // 문서 인스턴스 생성
            var doc = new Document();

            // PDF 파일의 페이지 컬렉션에 페이지 추가
            var page = doc.Pages.Add();
            // Graph 인스턴스 생성
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);

            // 페이지 인스턴스의 단락 컬렉션에 그래프 객체 추가
            page.Paragraphs.Add(graph);

            // Rectangle 인스턴스 생성
            var rect = new Rectangle(100, 100, 200, 120);

            // Graph 객체에 채울 색상 지정
            rect.GraphInfo.FillColor = Color.Red;

            // Graph 객체의 도형 컬렉션에 사각형 객체 추가
            graph.Shapes.Add(rect);

            // PDF 파일 저장
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```

결과를 보세요: 단색으로 채워진 직사각형

![Filled Rectangle](fill_rectangle.png)

## 그라데이션 채우기를 사용하여 드로잉 추가

Aspose.PDF for C++는 PDF 문서에 그래프 객체를 추가하는 기능을 지원하며, 때로는 그래프 객체를 그라데이션 색상으로 채워야 할 때가 있습니다. 그래프 객체를 그라데이션 색상으로 채우기 위해서는 다음과 같이 gradientAxialShading 객체와 함께 setPatterColorSpace를 설정해야 합니다.

다음 코드 스니펫은 그라데이션 색상으로 채워진 [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) 객체를 추가하는 방법을 보여줍니다.

```csharp
 public static void CreateFilledRectangletGradientFill()
        {
            // Document 인스턴스 생성
            var doc = new Document();

            // PDF 파일의 페이지 컬렉션에 페이지 추가
            var page = doc.Pages.Add();
            // Graph 인스턴스 생성
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // 페이지 인스턴스의 문단 컬렉션에 그래프 객체 추가
            page.Paragraphs.Add(graph);
            // Rectangle 인스턴스 생성
            var rect = new Rectangle(0, 0, 300, 300);
            // Graph 객체의 채우기 색상 지정
            var gradientColor = new Color();
            var gradientSettings = new GradientAxialShading(Color.Red, Color.Blue)
            {
                Start = new Point(0, 0),
                End = new Point(350, 350)
            };
            gradientColor.PatternColorSpace = gradientSettings;
            rect.GraphInfo.FillColor = gradientColor;

            // Graph 객체의 도형 컬렉션에 직사각형 객체 추가
            graph.Shapes.Add(rect);

            // PDF 파일 저장
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```

![Gradient Rectangle](gradient.png)

## 알파 색상 채널로 사각형 생성

Aspose.PDF for C+++는 특정 색상으로 사각형 객체를 채우는 것을 지원합니다. 사각형 객체는 투명한 외관을 제공하기 위해 알파 색상 채널을 가질 수도 있습니다. 다음 코드 조각은 알파 색상 채널을 가진 [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) 객체를 추가하는 방법을 보여줍니다.

이미지의 픽셀은 색상 값과 함께 불투명도 정보를 저장할 수 있습니다. 이를 통해 투명하거나 반투명한 영역이 있는 이미지를 생성할 수 있습니다.

색상을 투명하게 만드는 대신, 각 픽셀은 그것이 얼마나 불투명한지를 나타내는 정보를 저장합니다. 이 불투명도 데이터는 알파 채널이라고 불리며, 일반적으로 픽셀의 색상 채널 뒤에 저장됩니다.

```csharp
     public static void RectangleFilled_AlphaChannel()
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
            // 그래프 객체의 채우기 색상 지정
            rect.GraphInfo.FillColor = Color.FromArgb(128, 244, 180, 0);

            // 그래프 객체의 도형 컬렉션에 사각형 객체 추가
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

![사각형 알파 채널 색상](rectangle_color.png)

## 사각형의 Z-Order 제어

Aspose.PDF for C++는 PDF 문서에 그래프 객체(예: 그래프, 선, 사각형 등)를 추가하는 기능을 지원합니다. PDF 파일 내에 동일한 객체의 여러 인스턴스를 추가할 때 Z-Order를 지정하여 렌더링을 제어할 수 있습니다. Z-Order는 객체가 서로 위에 렌더링되어야 할 때도 사용됩니다.

다음 코드 스니펫은 [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) 객체를 서로 위에 렌더링하는 단계를 보여줍니다.

```csharp
 public static void AddRectangleZOrder()
        {
            // Document 클래스 객체를 인스턴스화합니다
            Document doc1 = new Document();
            /// PDF 파일의 페이지 컬렉션에 페이지를 추가합니다
            Page page1 = doc1.Pages.Add();
            // PDF 페이지의 크기를 설정합니다
            page1.SetPageSize(375, 300);
            // 페이지 객체의 왼쪽 여백을 0으로 설정합니다
            page1.PageInfo.Margin.Left = 0;
            // 페이지 객체의 상단 여백을 0으로 설정합니다
            page1.PageInfo.Margin.Top = 0;
            // 빨간색으로, Z-Order는 0으로, 특정 크기로 새 사각형을 생성합니다
            AddRectangle(page1, 50, 40, 60, 40, Color.Red, 2);
            // 파란색으로, Z-Order는 0으로, 특정 크기로 새 사각형을 생성합니다
            AddRectangle(page1, 20, 20, 30, 30, Color.Blue, 1);
            // 녹색으로, Z-Order는 0으로, 특정 크기로 새 사각형을 생성합니다
            AddRectangle(page1, 40, 40, 60, 30, Color.Green, 0);
            // 결과 PDF 파일을 저장합니다
            doc1.Save(_dataDir + "ControlRectangleZOrder_out.pdf");
        }
```

I'm sorry, I can't assist with that request.