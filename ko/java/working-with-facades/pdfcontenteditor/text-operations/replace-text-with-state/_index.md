---
title: 텍스트를 상태로 바꾸기
linktitle: 텍스트를 상태로 바꾸기
type: docs
weight: 20
url: /java/replace-text-with-state/
description: Aspose.PDF의 PdfContentEditor 파사드를 사용하여 Java에서 텍스트를 사용자 정의 형식으로 바꾸는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: PDF 텍스트를 Java의 사용자 정의 형식으로 바꾸기
Abstract: 이 문서에서는 PDF를 바인딩하고, 사용자 정의 TextState를 구성하고, 일치하는 모든 텍스트 항목을 바꾸고, Aspose.PDF for Java의 PdfContentEditor 파사드를 사용하여 업데이트된 문서를 저장하는 방법을 보여줍니다.
---
## 
텍스트를 사용자 정의 텍스트 상태로 바꾸기


1. 
소스 PDF를 `PdfContentEditor` 파사드에 바인딩합니다.

2. 
필요한 색상과 글꼴 크기로 `TextState`을 만들고 구성합니다.

3. 
대체 텍스트 범위를 `ReplaceAll`으로 설정합니다.

4. 
검색 텍스트, 대체 텍스트 및 구성된 `TextState`을 사용하여 `replaceText(...)`을 호출합니다.

5. 
업데이트된 PDF 문서를 저장합니다.

```java
public static void replaceTextWithState(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        TextState textState = new TextState();
        textState.setForegroundColor(com.aspose.pdf.Color.getBlue());
        textState.setFontSize(14);
        editor.getReplaceTextStrategy().setReplaceScope(ReplaceTextStrategy.Scope.ReplaceAll);
        editor.replaceText("software", "SOFTWARE", textState);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
