---
title: Java에서 PDF에 호 모양 추가
linktitle: 호 추가
type: docs
weight: 10
url: /java/add-arc/
description: Java에서 PDF 파일에 호 모양을 그리고 채우는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 파일에 호 모양 그리기
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서에 호 모양을 추가하는 방법을 보여줍니다. 다양한 색상으로 윤곽선이 있는 여러 개의 호를 그리는 방법과 호를 닫는 선과 결합하여 채워진 호 세그먼트를 만드는 방법을 다룹니다.
---

Aspose.PDF for Java는 벡터 그래픽을 렌더링하기 위해 `Arc` 및 `Line`과 같은 모양 개체와 함께 `Graph`을 사용합니다.


## 
호 윤곽선 추가


1. 
새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만듭니다.

1. 
문서에 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 추가하세요.

1. 
[그래프](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 컨테이너를 생성하여 페이지에 추가하세요.

1. 
[Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) 형상을 생성하고 해당 형상을 구성합니다.

1. 
[그래프](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 컨테이너에 [호](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/)를 추가합니다.

1. 
[색상](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/) 등 예제에서 요구하는 도형 속성을 설정합니다.

1. 
출력된 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 저장합니다.


```java
public static void addArc(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 400.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Arc arc1 = new Arc(100, 100, 95, 0, 90);
        arc1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().addItem(arc1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```


전체 예제에서는 반경, 각도 및 색상이 다른 세 개의 호를 동일한 그래프에 추가합니다.


## 
채워진 호 세그먼트 추가


1. 
새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만듭니다.

1. 
문서에 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 추가하세요.

1. 
[그래프](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 컨테이너를 생성하여 페이지에 추가합니다.

1. 
[Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) 모양을 생성하고 좌표를 구성합니다.

1. 
[Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) 형상을 생성하고 해당 형상을 구성합니다.

1. 
[그래프](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 컨테이너에 [선](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/)과 [호](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/)를 추가합니다.

1. 
출력된 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 저장합니다.

```java
public static void addArcFilled(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 400.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Arc arc = new Arc(100, 100, 95, 0, 90);
        arc.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().addItem(arc);

        Line line = new Line(new float[]{195, 100, 100, 100, 100, 195});
        line.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().addItem(line);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```
