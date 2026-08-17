---
title: Java에서 PDF에 텍스트 스탬프 추가
linktitle: PDF 파일의 텍스트 스탬프
type: docs
weight: 20
url: /java/text-stamps-in-the-pdf-file/
description: Java로 PDF 문서에 텍스트 스탬프를 추가하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 파일에 텍스트 스탬프 추가
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 파일에 텍스트 스탬프를 추가하는 방법을 설명합니다. 배경 텍스트 스탬프 생성, 위치 지정, 회전 및 글꼴, 크기, 스타일 및 색상 사용자 정의를 다룹니다.
---

PDF 페이지에 눈에 보이는 레이블이나 워터마크를 추가해야 하는 경우 텍스트 스탬프를 사용하세요.


## 
텍스트 스탬프 추가



페이지에 사용자 정의 스타일을 사용하여 회전된 텍스트 스탬프를 표시해야 하는 경우 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstamp/)를 생성하고 배치 및 텍스트 모양을 구성합니다.

1. 
대상 페이지에 스탬프를 추가하고 문서를 저장합니다.

```java
public static void addTextStamp(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextStamp textStamp = new TextStamp("Sample Stamp");
        textStamp.setBackground(true);
        textStamp.setXIndent(100);
        textStamp.setYIndent(100);
        textStamp.setRotate(Rotation.on90);
        textStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        textStamp.getTextState().setFontSize(14.0f);
        textStamp.getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        textStamp.getTextState().setForegroundColor(Color.getDarkGreen());
        document.getPages().get_Item(1).addStamp(textStamp);
        document.save(outputFile.toString());
    }
}
```
