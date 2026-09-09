---
title: Java에서 PDF에 페이지 번호 추가
linktitle: 페이지 번호 추가
type: docs
weight: 30
url: /java/add-page-number/
description: Java로 PDF 문서에 페이지 번호 스탬프를 추가하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 파일에 페이지 번호 스탬프 추가
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 페이지 번호 스탬프를 추가하는 방법을 설명합니다. 사용자 정의 글꼴 스타일을 사용한 표준 페이지 번호 매기기와 구성 가능한 시작 번호를 사용한 로마 숫자 번호 매기기를 다룹니다.
---
## 페이지 번호 스탬프 추가


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/) 개체를 만듭니다.

1. 
필요한 스탬프 배치 및 번호 매기기 옵션을 구성합니다.

1. 
[FontRepository](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontrepository/), [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/) 등 필요한 텍스트 서식 옵션을 설정합니다.
1. 구성된 [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/)를 대상 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)에 추가합니다.

1. 
업데이트된 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 저장합니다.

```java
public static void addPageNumStamp(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageNumberStamp pageNumberStamp = new PageNumberStamp();
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setFormat("Page # of " + document.getPages().size());
        pageNumberStamp.setBottomMargin(10);
        pageNumberStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(1);
        pageNumberStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize(14.0f);
        pageNumberStamp.getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        pageNumberStamp.getTextState().setForegroundColor(Color.getBlueViolet());

        document.getPages().get_Item(1).addStamp(pageNumberStamp);
        document.save(outputFile.toString());
    }
}
```
