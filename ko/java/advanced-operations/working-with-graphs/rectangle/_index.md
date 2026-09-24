---
title: Java에서 PDF에 직사각형 모양 추가
linktitle: 직사각형 추가
type: docs
weight: 50
url: /java/add-rectangle/
description: Java에서 PDF 파일에 직사각형 모양을 그리고 채우는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 파일에 직사각형 모양 그리기
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서에 직사각형 모양을 추가하는 방법을 보여줍니다. 윤곽선이 있는 직사각형, 단색 채우기, 그라데이션 채우기, 알파 투명도 및 겹치는 모양에 대한 Z 순서 제어를 다룹니다.
---
## 직사각형 윤곽선 추가


1. 
새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만듭니다.

1. 
문서에 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 추가하세요.

1. 
[그래프](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 컨테이너를 생성하여 페이지에 추가하세요.

1. 
[직사각형](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) 모양을 만들고 해당 형상을 구성합니다.
1. [그래프](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 컨테이너에 [사각형](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/)을 추가합니다.

1. 
출력된 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 저장합니다.


```java
public static void addRectangle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 300.0);
        page.getParagraphs().add(graph);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getRed()));

        Rectangle rectangle = new Rectangle(20, 20, 350, 250);
        graph.getShapes().addItem(rectangle);

        document.save(outputFile.toString());
    }
}
```

## 
단색 또는 그라데이션 색상으로 직사각형 채우기



직사각형 예는 다음과 같습니다.


- 
`createRectangleFilled` `Color.getRed()`으로 꽉 채우려면
- `GradientAxialShading` 채우기의 경우 `addDrawingWithGradientFill`


## 
알파 투명도 사용



`createRectangleWithAlphaColorChannel`은 `Color.fromArgb(...)`을 사용하여 반투명 색상을 적용하므로 겹치는 직사각형이 계속 표시됩니다.


## 
직사각형의 z 순서 제어


1. 
새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만듭니다.
1. 문서에 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 추가합니다.

1. 
필요한 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 크기를 설정하세요.

1. 
구성된 [직사각형](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) 도형을 필수 z 순서로 대상 페이지에 추가합니다.

1. 
출력된 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 저장합니다.

```java
public static void controlZOrderOfRectangle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.setPageSize(375, 300);
        page.getPageInfo().getMargin().setLeft(0);
        page.getPageInfo().getMargin().setTop(0);

        addRectangleToPage(page, 50, 40, 60, 40, Color.getRed(), 2);
        addRectangleToPage(page, 20, 20, 30, 30, Color.getBlue(), 1);
        addRectangleToPage(page, 40, 40, 60, 30, Color.getGreen(), 0);

        document.save(outputFile.toString());
    }
}
```
