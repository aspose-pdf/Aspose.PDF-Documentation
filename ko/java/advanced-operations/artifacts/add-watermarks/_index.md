---
title: Java에서 PDF에 워터마크 추가
linktitle: 워터마크 추가
type: docs
weight: 30
url: /ko/java/add-watermarks/
description: Java에서 PDF 페이지에 스타일 텍스트 워터마크 아티팩트를 추가합니다.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java에서 워터마크 추가
Abstract: Java에서 PDF 페이지에 스타일 텍스트 워터마크 아티팩트를 추가합니다.
---
워터마크 아티팩트를 사용하면 페이지에 지속적인 시각 표식을 삽입할 수 있지만 메인 문서 콘텐츠와 혼합되지 않습니다.

## 워터마크 아티팩트 추가

페이지에 사용자 지정 회전, 불투명도 및 배경 위치와 함께 중앙 정렬 텍스트 워터마크가 표시되어야 할 때 이 예제를 사용하십시오.

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)로 원본 PDF를 여세요.
1. [WatermarkArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/watermarkartifact/) 개체를 만들고 텍스트 상태와 배치 옵션을 설정하세요.
1. 페이지에 워터마크를 추가하고 출력 파일을 저장하세요.

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

## 관련 항목

- [워터마크 세부 정보 추출](/pdf/ko/java/extract-watermarks/)
- [워터마크 제거](/pdf/ko/java/remove-watermarks/)
- [Java에서 PDF 아티팩트 작업](/pdf/ko/java/artifacts/)
