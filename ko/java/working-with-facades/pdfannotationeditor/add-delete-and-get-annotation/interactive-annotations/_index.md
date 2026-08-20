---
title: Java를 사용한 대화형 주석
linktitle: 대화형 주석
type: docs
weight: 30
url: /java/pdfannotationeditor-class/interactive-annotations/
description: Java를 사용하여 PDF 문서에서 링크 주석을 추가, 검사 및 삭제하는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java에서 대화형 PDF 주석 작업
Abstract: 이 문서에서는 Java를 사용하여 PDF 파일의 대화형 링크 주석을 사용하는 방법을 설명합니다. 텍스트 찾기, 일치하는 텍스트 영역 위에 링크 주석 생성, 기존 링크 주석 읽기 및 삭제에 대해 다룹니다.
---
## 링크 주석 추가


1. 
원본 PDF 문서를 로드하고 첫 번째 페이지에서 대상 텍스트를 검색합니다.

2. 
일치하는 텍스트 직사각형을 사용하여 `LinkAnnotation`을 만들고 대상 URI를 할당합니다.

3. 
페이지에 주석을 추가하고 업데이트된 PDF를 저장합니다.

```java
public static void linkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("file");
        document.getPages().get_Item(1).accept(textFragmentAbsorber);

        TextFragment phoneNumberFragment = textFragmentAbsorber.getTextFragments().get_Item(1);

        LinkAnnotation linkAnnotation = new LinkAnnotation(
                document.getPages().get_Item(1), phoneNumberFragment.getRectangle());
        linkAnnotation.setAction(new GoToURIAction("www.aspose.com"));

        document.getPages().get_Item(1).getAnnotations().add(linkAnnotation);
        document.save(outputFile.toString());
    }
}
```
