---
title: Java에서 PDF에 타원 모양 추가
linktitle: 타원 추가
type: docs
weight: 60
url: /java/add-ellipse/
description: Java에서 PDF 파일의 타원 모양을 그리고 채우고 레이블을 지정하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 파일에 타원 모양 그리기
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서에 타원 모양을 추가하는 방법을 보여줍니다. 윤곽선이 있는 타원, 채워진 타원, 타원 모양 안에 텍스트 조각 배치 등을 다룹니다.
---
## 타원 윤곽선 추가


1. 
새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만듭니다.

1. 
문서에 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 추가하세요.

1. 
[그래프](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 컨테이너를 생성하여 페이지에 추가하세요.

1. 
[타원](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) 모양을 만들고 해당 형상을 구성합니다.
1. [그래프](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 컨테이너에 [타원](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/)을 추가합니다.

1. 
[Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/), [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) 등 예제에서 요구하는 도형 속성을 설정합니다.

1. 
출력된 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 저장합니다.


```java
public static void addEllipse(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 400.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Ellipse ellipse1 = new Ellipse(150, 100, 120, 60);
        ellipse1.getGraphInfo().setColor(Color.getGreenYellow());
        ellipse1.setText(new TextFragment("Ellipse"));
        graph.getShapes().addItem(ellipse1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```


전체 예제에서는 동일한 그래프에 두 개의 서로 다른 윤곽선 타원을 추가합니다.


## 
채워진 타원 추가

`createEllipseFilled`은 `Color.getGreenYellow()` 및 `Color.getDarkRed()`으로 두 개의 타원을 채웁니다.


## 
타원 안에 텍스트 추가


1. 
새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만듭니다.

1. 
문서에 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 추가하세요.

1. 
[TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/)를 만들고 필요한 텍스트 서식 옵션을 설정하세요.
1. [그래프](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 컨테이너를 생성하여 페이지에 추가합니다.

1. 
[타원](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) 모양을 만들고 해당 형상을 구성합니다.

1. 
[그래프](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 컨테이너에 [타원](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/)을 추가합니다.

1. 
출력된 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 저장합니다.

```java
public static void addTextInsideEllipse(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 400.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        TextFragment textFragment = new TextFragment("Ellipse");
        textFragment.getTextState().setFont(FontRepository.findFont("Helvetica"));
        textFragment.getTextState().setFontSize(24);

        Ellipse ellipse1 = new Ellipse(100, 100, 120, 180);
        ellipse1.getGraphInfo().setFillColor(Color.getGreenYellow());
        ellipse1.setText(textFragment);
        graph.getShapes().addItem(ellipse1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```
