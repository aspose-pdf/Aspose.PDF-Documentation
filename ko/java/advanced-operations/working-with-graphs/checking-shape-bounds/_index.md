---
title: Java를 사용하여 PDF 그래프의 모양 경계 확인
linktitle: 모양 경계 확인
type: docs
weight: 70
url: /java/aspose-pdf-drawing-graph-shapes-bounds-check/
description: Java의 PDF 그래프 컬렉션에서 모양 경계의 유효성을 검사하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 파일의 그래프 모양 경계 검증
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 그래프 컬렉션의 모양 경계를 확인하는 방법을 보여줍니다. 엄격한 경계 검사 활성화, 범위를 벗어난 모양 추가 시도, 문서를 저장하는 동안 결과 예외 처리 등을 다룹니다.
---
도형이 그래프 컨테이너 내부에 맞는지 확인해야 하는 경우 `BoundsCheckMode`을 사용하세요.


## 
그래프 모양 경계 검증


1. 
새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만듭니다.

1. 
문서에 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 추가하세요.

1. 
[그래프](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 컨테이너를 생성하여 페이지에 추가하세요.
1. [직사각형](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) 모양을 만들고 해당 형상을 구성합니다.

1. 
엄격한 경계 검사를 활성화하고 `BoundsCheckMode`을 사용하여 그래프 컬렉션에 모양을 추가해 보세요.

1. 
모양이 맞지 않으면 예외를 처리합니다.

1. 
출력된 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 저장합니다.

```java
public static void checkShapeBounds(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(100.0, 100.0);
        graph.setTop(10);
        graph.setLeft(15);
        graph.setBorder(new BorderInfo(BorderSide.Box, 1, Color.getBlack()));
        page.getParagraphs().add(graph);

        Rectangle rectangle = new Rectangle(-1, 0, 50, 50);
        rectangle.getGraphInfo().setFillColor(Color.getTomato());
        try {
            graph.getShapes().updateBoundsCheckMode(BoundsCheckMode.ThrowExceptionIfDoesNotFit);
            graph.getShapes().addItem(rectangle);
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }

        document.save(outputFile.toString());
    }
}
```
