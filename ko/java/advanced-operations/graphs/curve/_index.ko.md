---
title: PDF 파일에 곡선 객체 추가
linktitle: 곡선 추가
type: docs
weight: 30
url: /java/add-curve/
description: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF에 곡선 객체를 생성하는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 곡선 객체 추가

그래프 [Curve](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Curve)는 투영선의 연결된 결합체로, 각 선은 보통의 이중 점에서 다른 세 개의 선과 만납니다.

Aspose.PDF for Java는 그래프에서 베지어 곡선을 사용하는 방법을 보여줍니다.
베지어 곡선은 컴퓨터 그래픽에서 매끄러운 곡선을 모델링하는 데 널리 사용됩니다. 곡선은 제어점의 볼록 껍질 내에 완전히 포함되며, 점은 그래픽으로 표시되고 직관적으로 곡선을 조작하는 데 사용될 수 있습니다.
전체 곡선은 주어진 네 개의 점(그들의 볼록 껍질)의 꼭지점인 사각형에 포함됩니다.

이 문서에서는 PDF 문서에서 생성할 수 있는 단순 그래프 곡선과 채워진 곡선을 조사할 것입니다.

아래의 단계를 따르세요:

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 인스턴스를 생성합니다.

1. 특정 크기를 가진 [Drawing object](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/package-frame)를 생성합니다.

1. Drawing 객체에 대해 [Border](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph#setBorder-com.aspose.pdf.BorderInfo-)를 설정합니다.

1. 페이지의 단락 컬렉션에 [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph) 객체를 추가합니다.

1. PDF 파일을 저장합니다.

```java
    public static void ExampleCurve() {
        // Document 인스턴스를 생성합니다
        Document pdfDocument = new Document();
        // PDF 파일의 페이지 컬렉션에 페이지를 추가합니다
        Page page = pdfDocument.getPages().add();

        // 특정 크기를 가진 Drawing 객체를 생성합니다
        Graph graph = new Graph(400, 200);
        // Drawing 객체에 대해 테두리를 설정합니다
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Curve curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120});

        curve1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().add(curve1);

        // 페이지의 단락 컬렉션에 Graph 객체를 추가합니다
        page.getParagraphs().add(graph);

        // PDF 파일을 저장합니다
        pdfDocument.save(_dataDir + "DrawingCurve1_out.pdf");
    }
```


다음 그림은 코드 스니펫을 실행한 결과를 보여줍니다:

![Drawing Curve](drawing_curve.png)

## 채워진 곡선 객체 생성

이 예제는 색으로 채워진 Curve 객체를 추가하는 방법을 보여줍니다.

```java
    public static void ExampleFilledCurve() {
        // Document 인스턴스 생성
        Document pdfDocument = new Document();
        // PDF 파일의 페이지 컬렉션에 페이지 추가
        Page page = pdfDocument.getPages().add();

        // 특정 크기의 Drawing 객체 생성
        Graph graph = new Graph(400, 200);
        // Drawing 객체에 테두리 설정
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Curve curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120});
        curve1.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().add(curve1);

        // 페이지의 단락 컬렉션에 Graph 객체 추가
        page.getParagraphs().add(graph);

        // PDF 파일 저장
        pdfDocument.save(_dataDir + "DrawingCurve2_out.pdf");
    }
```


결과를 확인해 보세요: 채워진 곡선 추가하기

![Filled Curve](filled_curve.png)