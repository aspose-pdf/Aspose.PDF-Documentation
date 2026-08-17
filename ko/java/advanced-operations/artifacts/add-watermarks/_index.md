---
title: Java에서 PDF에 워터마크 추가
linktitle: 워터마크 추가
type: docs
weight: 30
url: /java/add-watermarks/
description: Java용 Aspose.PDF를 사용하여 PDF 파일에서 워터마크 아티팩트를 추가, 추출 및 삭제하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF에 워터마크를 추가하는 방법
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서에서 워터마크 아티팩트를 추가, 검사 및 제거하는 방법을 설명합니다. 정렬, 회전, 불투명도 및 배경 설정을 사용하여 텍스트 워터마크 생성, 페이지의 워터마크 아티팩트 검사 및 삭제를 다룹니다.
---

워터마크 아티팩트를 사용하면 기본 문서 콘텐츠에 혼합하지 않고도 페이지에 지속적인 시각적 표시를 배치할 수 있습니다.


## 
PDF에서 워터마크 아티팩트 추출



기존 워터마크 아티팩트를 검사하고 텍스트나 위치를 읽어야 할 때 이 예를 사용하세요.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
대상 페이지의 아티팩트 컬렉션을 반복합니다.

1. 
워터마크 페이지 매김 아티팩트를 필터링하고 해당 텍스트와 직사각형을 인쇄합니다.


```java
public static void extractWatermarkFromPdf(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Artifact artifact : document.getPages().get_Item(1).getArtifacts()) {
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                System.out.println(artifact.getText() + " " + artifact.getRectangle());
            }
        }
    }
}
```

## 
워터마크 아티팩트 추가



페이지가 사용자 정의 회전, 불투명도 및 배경 배치와 함께 중앙에 텍스트 워터마크를 표시해야 하는 경우 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[WatermarkArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/watermarkartifact/)를 생성하고 텍스트 상태 및 배치 설정을 구성합니다.

1. 
페이지에 워터마크를 추가하고 출력 파일을 저장합니다.


```java
public static void addWatermarkArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextState textState = new TextState();
        textState.setFontSize(72);
        textState.setForegroundColor(Color.getBlueViolet());
        textState.setFontStyle(FontStyles.Bold);
        textState.setFont(FontRepository.findFont("Arial"));

        WatermarkArtifact watermark = new WatermarkArtifact();
        watermark.setTextAndState("WATERMARK", textState);
        watermark.setArtifactHorizontalAlignment(HorizontalAlignment.Center);
        watermark.setArtifactVerticalAlignment(VerticalAlignment.Center);
        watermark.setRotation(60);
        watermark.setOpacity(0.2);
        watermark.setBackground(true);

        document.getPages().get_Item(1).getArtifacts().add(watermark);
        document.save(outputFile.toString());
    }
}
```

## 
워터마크 아티팩트 삭제



페이지에서 기존 워터마크 아티팩트를 제거해야 하는 경우 이 접근 방식을 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
페이지 아티팩트 컬렉션을 역순으로 반복합니다.

1. 
하위 유형이 워터마크인 페이지 매김 아티팩트를 삭제한 다음 문서를 저장합니다.

```java
public static void deleteWatermarkArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```
