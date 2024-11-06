---
title: PDF에서 폰트 추출
linktitle: 폰트 추출
type: docs
weight: 30
url: ko/java/extract-fonts-from-pdf/
description: Aspose.PDF for Java를 사용하여 PDF에서 폰트를 추출하는 방법
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF 문서에서 모든 폰트를 얻고자 하는 경우, Document 클래스에서 제공하는 `Document.IDocumentFontUtilities.getAllFonts()` 메서드를 사용할 수 있습니다. 기존 PDF 문서에서 모든 폰트를 얻기 위한 다음 코드 스니펫을 확인하십시오:

```java
public static void Extract_Fonts() throws FileNotFoundException
{
    // 문서 디렉토리 경로.
    String filePath = "<... enter file name ...>";
    
    // PDF 문서 로드
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);
    com.aspose.pdf.Font[] fonts = pdfDocument.getFontUtilities().getAllFonts();

    for (com.aspose.pdf.Font font : fonts)
    {
        font.save(new FileOutputStream(font.getFontName()));
    }
}
```