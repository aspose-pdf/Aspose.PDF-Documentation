---
title: 텍스트 단순 교체
linktitle: 텍스트 단순 교체
type: docs
weight: 10
url: /java/replace-text-simple/
description: Aspose.PDF의 PdfContentEditor 파사드를 사용하여 Java에서 PDF 문서 전체의 텍스트를 바꾸는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java에서 PDF의 텍스트 바꾸기
Abstract: 이 문서에서는 PDF를 바인딩하고, 텍스트 바꾸기 범위를 구성하고, 일치하는 모든 텍스트 항목을 바꾸고, Aspose.PDF for Java의 PdfContentEditor 파사드를 사용하여 업데이트된 문서를 저장하는 방법을 보여줍니다.
---
## 
문서 전체에서 텍스트 바꾸기


1. 
소스 PDF를 `PdfContentEditor` 파사드에 바인딩합니다.

2. 
대체 텍스트 범위를 `ReplaceAll`으로 설정합니다.

3. 
검색어와 대체문자를 가지고 `replaceText(...)`로 전화주세요.

4. 
업데이트된 PDF 문서를 저장합니다.

```java
public static void replaceTextSimple(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.getReplaceTextStrategy().setReplaceScope(ReplaceTextStrategy.Scope.ReplaceAll);
        editor.replaceText("33", "XXXIII ");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
