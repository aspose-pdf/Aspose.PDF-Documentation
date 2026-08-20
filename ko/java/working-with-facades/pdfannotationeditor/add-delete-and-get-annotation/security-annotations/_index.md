---
title: Java를 사용한 보안 주석
linktitle: 보안 주석
type: docs
weight: 60
url: /java/pdfannotationeditor-class/security-annotations/
description: 교정할 텍스트를 표시하고, 교정 주석을 적용하고, Java를 사용하여 PDF 파일에서 선택한 페이지 영역을 교정하는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: 보안 주석을 사용하여 Java에서 중요한 PDF 콘텐츠를 수정합니다.
Abstract: 이 문서에서는 Java를 사용하여 PDF 문서에서 편집 주석 작업을 수행하는 방법을 설명합니다. 교정 주석으로 일치하는 텍스트 표시, 교정 영구 적용, 감지된 이미지 배치 직사각형을 기반으로 선택한 영역 교정을 다룹니다.
---
## 교정할 텍스트 표시


1. 
PDF를 로드하고 수정해야 할 텍스트를 모든 페이지에서 검색하세요.

2. 
일치하는 각 텍스트 조각에 대해 `RedactionAnnotation`을 만들고 모양을 구성합니다.

3. 
해당 페이지에 교정 주석을 추가하고 문서를 저장합니다.

```java
public static void markTextRedaction(Path inputFile, Path outputFile, String searchTerm) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(searchTerm);
        TextSearchOptions textSearchOptions = new TextSearchOptions(true);
        textFragmentAbsorber.setTextSearchOptions(textSearchOptions);
        document.getPages().accept(textFragmentAbsorber);

        for (TextFragment textFragment : textFragmentAbsorber.getTextFragments()) {
            Page page = textFragment.getPage();
            Rectangle annotationRectangle = textFragment.getRectangle();
            RedactionAnnotation annotation = new RedactionAnnotation(page, annotationRectangle);
            annotation.setFillColor(Color.getGray());
            annotation.setBorderColor(Color.getRed());
            annotation.setColor(Color.getWhite());
            annotation.setOverlayText("REDACTED");
            annotation.setTextAlignment(HorizontalAlignment.Center);
            annotation.setRepeat(true);
            page.getAnnotations().add(annotation, true);
        }

        document.save(outputFile.toString());
    }
}
```
