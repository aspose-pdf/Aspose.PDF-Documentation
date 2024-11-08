---
title: PDF 파일에 호 객체 추가
linktitle: 호 추가
type: docs
weight: 10
url: /ko/java/add-arc/
description: 이 문서는 Aspose.PDF for Java를 사용하여 PDF에 호 객체를 생성하는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 호 객체 추가

Aspose.PDF for Java는 PDF 문서에 그래프 객체(예: 그래프, 선, 사각형 등)를 추가하는 기능을 지원합니다. 또한 특정 색상으로 호 객체를 채우는 기능도 제공합니다.

다음 단계를 따르세요:

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 인스턴스 생성

1. 특정 크기로 [Drawing object](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/package-frame) 생성

1. Drawing 객체에 대한 [Border](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph#setBorder-com.aspose.pdf.BorderInfo-) 설정

1. 페이지의 단락 컬렉션에 [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph) 객체 추가

1. PDF 파일 저장


다음 코드 조각은 [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Arc) 객체를 추가하는 방법을 보여줍니다.

```java
    public static void ExampleArc() {
        // Document 인스턴스 생성
        Document pdfDocument = new Document();
        // PDF 파일의 페이지 컬렉션에 페이지 추가
        Page page = pdfDocument.getPages().add();

        // 특정 크기로 Drawing 객체 생성
        Graph graph = new Graph(400, 400);
        // Drawing 객체에 경계 설정
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Arc arc1 = new Arc(100, 100, 95, 0, 90);
        arc1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().add(arc1);

        Arc arc2 = new Arc(100, 100, 90, 70, 180);
        arc2.getGraphInfo().setColor(Color.getDarkBlue());
        graph.getShapes().add(arc2);

        Arc arc3 = new Arc(100, 100, 85, 120, 210);
        arc3.getGraphInfo().setColor(Color.getRed());
        graph.getShapes().add(arc3);

        // 페이지의 단락 컬렉션에 Graph 객체 추가
        page.getParagraphs().add(graph);

        // PDF 파일 저장
        pdfDocument.save(_dataDir + "DrawingArc_out.pdf");

    }
```


## 채워진 호 객체 생성

다음 예시는 색상과 특정 치수로 채워진 호 객체를 추가하는 방법을 보여줍니다.

```java
    public static void ExampleFilledArc() {
        // 문서 인스턴스 생성
        Document pdfDocument = new Document();
        // PDF 파일의 페이지 컬렉션에 페이지 추가
        Page page = pdfDocument.getPages().add();

        // 특정 치수로 Drawing 객체 생성
        Graph graph = new Graph(400, 400);
        // Drawing 객체에 테두리 설정
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Arc arc = new Arc(100, 100, 95, 0, 90);
        arc.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().add(arc);

        Line line = new Line(new float[] { 195, 100, 100, 100, 100, 195 });
        line.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().add(line);

        // 페이지의 단락 컬렉션에 Graph 객체 추가
        page.getParagraphs().add(graph);

        // PDF 파일 저장
        pdfDocument.save(_dataDir + "DrawingArc_out.pdf");

    }
```


Let's see the result of adding a filled Arс:

![채워진 호](filled_arc.png)