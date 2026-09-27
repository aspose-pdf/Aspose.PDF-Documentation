---
title: 텍스트를 상태로 바꾸기
linktitle: 텍스트를 상태로 바꾸기
type: docs
weight: 20
url: /ko/java/replace-text-with-state/
description: Aspose.PDF의 PdfContentEditor 파사드를 사용하여 Java에서 텍스트를 사용자 정의 형식으로 바꾸는 방법을 알아보세요.
lastmod: "2026-09-24"
TechArticle: true
AlternativeHeadline: PDF 텍스트를 Java의 사용자 정의 형식으로 바꾸기
Abstract: 이 문서에서는 PDF를 바인딩하고, 사용자 정의 TextState를 구성하고, 일치하는 모든 텍스트 항목을 바꾸고, Aspose.PDF for Java의 PdfContentEditor 파사드를 사용하여 업데이트된 문서를 저장하는 방법을 보여줍니다.
---
## 텍스트를 사용자 정의 텍스트 상태로 바꾸기

1. 소스 PDF를 `PdfContentEditor` 파사드에 바인딩하세요.
2. 필요한 색상과 글꼴 크기로 `TextState`를 만들고 구성하세요.
3. 대체 텍스트 범위를 `ReplaceAll`으로 설정하세요.
4. 검색 텍스트, 대체 텍스트 및 구성된 `TextState`를 사용하여 `replaceText(...)`를 호출하세요.
5. 업데이트된 PDF 문서를 저장하세요.

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
