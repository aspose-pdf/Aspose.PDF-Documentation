---
title: 뷰어 기본 설정 변경
linktitle: 뷰어 기본 설정 변경
type: docs
weight: 20
url: /java/change-viewer-preferences/
description: Aspose.PDF의 PdfContentEditor 파사드를 사용하여 Java에서 PDF 문서의 뷰어 기본 설정을 변경하는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java에서 PDF 뷰어 기본 설정 변경
Abstract: 이 문서에서는 PDF를 바인딩하고, 현재 뷰어 기본 설정 값을 수정하고, Aspose.PDF for Java의 PdfContentEditor 파사드를 사용하여 업데이트된 문서를 저장하는 방법을 보여줍니다.
---
## 시청자 환경설정 변경


1. 
소스 PDF를 `PdfContentEditor` 파사드에 바인딩합니다.

2. 
현재 시청자 선호도 값을 읽습니다.

3. 
이를 원하는 추가 플래그와 결합하고 결과를 `changeViewerPreference(...)`에 전달합니다.

4. 
업데이트된 PDF 문서를 저장합니다.

```java
public static void changeViewerPreferences(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.changeViewerPreference(editor.getViewerPreference() | 1);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
