---
title: Java에서 PDF에 원 모양 추가
linktitle: 서클 추가
type: docs
weight: 20
url: /java/add-circle/
description: Java에서 PDF 파일에 원 모양을 그리고 채우는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 파일에 원 모양 그리기
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서에 원 모양을 추가하는 방법을 보여줍니다. 원 외곽선 그리기, 원을 색상으로 채우기, 원 모양 안에 텍스트 배치 등을 다룹니다.
---
## 
원 윤곽선 추가


1. 
새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만듭니다.

1. 
문서에 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 추가하세요.

1. 
[그래프](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 컨테이너를 생성하여 페이지에 추가하세요.

1. 
[원](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) 모양을 만들고 해당 형상을 구성합니다.

1. 
[그래프](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 컨테이너에 [원](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/)을 추가합니다.

1. 
[색상](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/) 등 예제에서 요구하는 도형 속성을 설정합니다.

1. 
출력된 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 저장합니다.


```java
public static void addCircle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 200.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Circle circle = new Circle(100, 100, 40);
        circle.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().addItem(circle);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```

## 
텍스트로 채워진 원 추가


1. 
새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만듭니다.

1. 
문서에 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 추가하세요.

1. 
[그래프](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 컨테이너를 생성하여 페이지에 추가하세요.

1. 
[원](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) 모양을 만들고 해당 형상을 구성합니다.

1. 
[그래프](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 컨테이너에 [원](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/)을 추가합니다.

1. 
[Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/), [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) 등 예제에서 요구하는 도형 속성을 설정합니다.

1. 
출력된 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 저장합니다.

```java
public static void addCircleFilled(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 200.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Circle circle = new Circle(100, 100, 40);
        circle.getGraphInfo().setColor(Color.getGreenYellow());
        circle.getGraphInfo().setFillColor(Color.getGreen());
        circle.setText(new TextFragment("Circle"));
        graph.getShapes().addItem(circle);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```
