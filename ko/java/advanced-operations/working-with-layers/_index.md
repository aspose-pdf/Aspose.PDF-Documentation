---
title: Java를 사용하여 PDF 레이어 작업
linktitle: PDF 레이어 작업
type: docs
weight: 50
url: /java/working-with-pdf-layers/
description: Java에서 PDF 레이어를 추가, 잠금, 추출, 병합 및 병합하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java로 PDF 레이어 관리
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 선택적 콘텐츠 그룹이라고도 하는 PDF 레이어로 작업하는 방법을 설명합니다. 페이지에 레이어를 추가하고, 기존 레이어를 잠그고, 레이어 콘텐츠를 파일이나 스트림으로 추출하고, 레이어된 콘텐츠를 병합하고, 레이어를 하나로 병합하는 방법을 알아보세요.
---

Java용 Aspose.PDF는 각 페이지의 `Layer` API를 통해 PDF 레이어를 노출합니다. 선택적 콘텐츠 그룹을 생성하고, 해당 동작을 수정하고, 필요할 때 해당 콘텐츠를 내보내거나 평면화할 수 있습니다.


## 
PDF 페이지에 레이어 추가


1. 
새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만듭니다.

1. 
문서에 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 추가하세요.

1. 
페이지에서 필수 [레이어](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/) 개체를 생성하고 구성합니다.

1. 
출력된 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 저장합니다.


```java
public static void addLayers(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Layer layer = new Layer("oc1", "Red Line");
        layer.getContents().add(new SetRGBColorStroke(1, 0, 0));
        layer.getContents().add(new MoveTo(500, 700));
        layer.getContents().add(new LineTo(400, 700));
        layer.getContents().add(new Stroke());
        page.getLayers().add(layer);

        document.save(outputFile.toString());
    }
}
```


전체 예제에서는 빨간색, 녹색, 파란색 선 콘텐츠가 포함된 세 개의 개별 레이어를 만듭니다.


## 
레이어 잠그기


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
대상 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)에 액세스하고 해당 [레이어](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/) 컬렉션을 가져옵니다.

1. 
대상 [레이어](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/)를 잠급니다.

1. 
업데이트된 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 저장합니다.

```java
public static void lockLayer(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        if (!page.getLayers().isEmpty()) {
            Layer layer = page.getLayers().getFirst();
            layer.lock();
            document.save(outputFile.toString());
        }
    }
}
```
