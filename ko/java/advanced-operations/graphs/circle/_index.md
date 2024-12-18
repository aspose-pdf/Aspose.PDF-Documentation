---
title: PDF 파일에 원 객체 추가
linktitle: 원 추가
type: docs
weight: 20
url: /ko/java/add-circle/
description: 이 기사는 Aspose.PDF for Java를 사용하여 PDF에 원 객체를 생성하는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 원 객체 추가

막대 그래프처럼 원 그래프는 여러 개의 개별 범주에 데이터를 표시하는 데 사용될 수 있습니다. 그러나 막대 그래프와 달리 원 그래프는 전체를 구성하는 모든 범주의 데이터가 있을 때만 사용할 수 있습니다. 그러므로 Aspose.PDF for Java를 사용하여 [원](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Circle) 객체를 추가하는 방법을 살펴보겠습니다.

아래 단계를 따르세요:

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 인스턴스 생성

1. 특정 치수로 [Drawing object](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/package-frame) 생성

1. Drawing 객체에 [Border](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph#setBorder-com.aspose.pdf.BorderInfo-) 설정

1. 페이지의 문단 컬렉션에 [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph) 객체 추가

1. PDF 파일 저장

```java
public static void ExampleCircle() {
        // Document 인스턴스 생성
        Document pdfDocument = new Document();
        // PDF 파일의 페이지 컬렉션에 페이지 추가
        Page page = pdfDocument.getPages().add();

        // 특정 크기로 Drawing 객체 생성
        Graph graph = new Graph(400, 200);
        // Drawing 객체에 경계 설정
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Circle circle = new Circle(100,100,40);

        circle.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().add(circle);

        // 페이지의 문단 컬렉션에 Graph 객체 추가
        page.getParagraphs().add(graph);

        // PDF 파일 저장
        pdfDocument.save(_dataDir + "DrawingCircle1_out.pdf");
    }
```


우리의 그려진 원은 다음과 같이 보일 것입니다:

![Drawing Circle](drawing_circle.png)

## 채워진 원 객체 생성

이 예제는 색으로 채워진 Circle 객체를 추가하는 방법을 보여줍니다.

```java

    public static void ExampleFilledCircle() {
        // Document 인스턴스 생성
        Document pdfDocument = new Document();
        // PDF 파일의 페이지 컬렉션에 페이지 추가
        Page page = pdfDocument.getPages().add();

        // 특정 크기의 Drawing 객체 생성
        Graph graph = new Graph(400, 200);
        // Drawing 객체에 테두리 설정
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Circle circle = new Circle(100,100,40);
        circle.getGraphInfo().setColor(Color.getGreenYellow());       
        circle.getGraphInfo().setFillColor(Color.getGreenYellow());

        graph.getShapes().add(circle);

        // 페이지의 단락 컬렉션에 Graph 객체 추가
        page.getParagraphs().add(graph);

        // PDF 파일 저장
        pdfDocument.save(_dataDir + "DrawingCircle2_out.pdf");
    }
```


Let's see the result of adding a filled Circle:

![채워진 원](filled_circle.png)