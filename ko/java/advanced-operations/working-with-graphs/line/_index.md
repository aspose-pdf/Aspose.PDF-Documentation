---
title: Java에서 PDF에 선 모양 추가
linktitle: 라인 추가
type: docs
weight: 40
url: /java/add-line/
description: Java에서 PDF 파일에 선 모양과 스타일 선을 그리는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 파일에 선 모양 그리기
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서에 선 모양을 추가하는 방법을 보여줍니다. 좌표 배열에서 선 만들기, 점선 스타일 및 색상 적용, 전체 페이지 영역에 선 그리기 등을 다룹니다.
---
## 
점선 추가


1. 
새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만듭니다.

1. 
문서에 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 추가하세요.

1. 
[그래프](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 컨테이너를 생성하여 페이지에 추가합니다.

1. 
[Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) 모양을 생성하고 좌표를 구성합니다.

1. 
[그래프](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 컨테이너에 [선](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/)을 추가합니다.

1. 
출력된 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 저장합니다.


```java
public static void addLine(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(100.0, 400.0);
        page.getParagraphs().add(graph);

        Line line = new Line(new float[]{100, 100, 200, 100});
        line.getGraphInfo().setDashArray(new int[]{0, 1, 0});
        line.getGraphInfo().setDashPhase(1);
        graph.getShapes().addItem(line);

        document.save(outputFile.toString());
    }
}
```

## 
색상이 있는 점선이나 점선을 추가하세요.



`addDottedDashedLine`은 동일한 좌표와 대시 설정을 사용하지만 `Color.getRed()`도 적용됩니다.


## 
페이지 전체에 선을 그립니다.


1. 
새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만듭니다.

1. 
문서에 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 추가하세요.

1. 
[그래프](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 컨테이너를 생성하여 페이지에 추가합니다.

1. 
[Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) 모양을 생성하고 좌표를 구성합니다.

1. 
[그래프](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 컨테이너에 [선](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/)을 추가합니다.

1. 
출력된 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 저장합니다.

```java
public static void drawLineAcrossPage(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getPageInfo().getMargin().setLeft(0);
        page.getPageInfo().getMargin().setRight(0);
        page.getPageInfo().getMargin().setBottom(0);
        page.getPageInfo().getMargin().setTop(0);

        Graph graph = new Graph(page.getPageInfo().getWidth(), page.getPageInfo().getHeight());
        Line line = new Line(new float[]{
                (float) page.getRect().getLLX(),
                0,
                (float) page.getPageInfo().getWidth(),
                (float) page.getRect().getURY()
        });
        graph.getShapes().addItem(line);
        page.getParagraphs().add(graph);

        document.save(outputFile.toString());
    }
}
```
