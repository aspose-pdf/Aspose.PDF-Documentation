---
title: Java를 통해 PDF에서 글꼴 추출
linktitle: PDF에서 글꼴 추출
type: docs
weight: 30
url: /java/extract-fonts-from-pdf/
description: Java용 Aspose.PDF를 사용하여 PDF 문서에 사용된 글꼴을 검사하고 추출하세요.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF에서 글꼴을 추출하는 방법
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서에 사용된 글꼴을 검사하는 방법을 설명합니다. PDF를 열고 `getFontUtilities().getAllFonts()`을 호출하고 결과 글꼴 개체를 반복하여 이름을 읽는 방법을 보여줍니다.
---
문서 입력 체계를 감사하거나, 포함된 리소스를 검사하거나, 변환 또는 보관 작업 흐름 전에 글꼴 사용을 확인해야 하는 경우 글꼴 추출을 사용하세요.


1. 
[문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
문서에서 참조하는 모든 [글꼴](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) 리소스를 수집하려면 `document.getFontUtilities().getAllFonts()`에 전화하세요.

1. 
추출된 [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) 개체를 반복하고 글꼴 메타데이터에서 각 글꼴 이름을 읽습니다.

1. 
문서 서체를 감사하거나 내보낼 수 있도록 글꼴 이름을 인쇄합니다.

```java
public static void extractFonts(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Font[] fonts = document.getFontUtilities().getAllFonts();
        for (Font font : fonts) {
            System.out.println(font.getFontName());
        }
    }
}
```
