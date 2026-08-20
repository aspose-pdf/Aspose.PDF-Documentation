---
title: Java에서 PDF에 곡선 모양 추가
linktitle: 곡선 추가
type: docs
weight: 30
url: /java/add-curve/
description: Java에서 PDF 파일의 곡선 모양을 그리고 채우는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 파일에 곡선 모양 그리기
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서에 곡선 모양을 추가하는 방법을 보여줍니다. 좌표 배열에서 곡선을 만들고 그래프 컨테이너 내부에 획 색상이나 채우기 색상을 적용하는 방법을 다룹니다.
---
Aspose.PDF for Java의 곡선은 `Curve`에 전달된 부동 좌표 배열로 정의됩니다.


## 
곡선 윤곽선 추가


1. 
새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만듭니다.

1. 
문서에 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 추가하세요.

1. 
[그래프](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 컨테이너를 생성하여 페이지에 추가하세요.
1. [곡선](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/curve/) 모양을 생성하고 제어점을 구성합니다.

1. 
[그래프](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) 컨테이너에 [곡선](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/curve/)을 추가합니다.

1. 
[색상](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/) 등 예제에서 요구하는 도형 속성을 설정합니다.

1. 
출력된 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 저장합니다.

```java
public static void addCurve(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 200.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Curve curve1 = new Curve(new float[]{10, 10, 50, 60, 70, 10, 100, 120});
        curve1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().addItem(curve1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```
