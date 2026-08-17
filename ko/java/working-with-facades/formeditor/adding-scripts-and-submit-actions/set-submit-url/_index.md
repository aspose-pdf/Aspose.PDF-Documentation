---
title: 제출 URL 설정
linktitle: 제출 URL 설정
type: docs
weight: 30
url: /java/set-submit-url/
description: Aspose.PDF의 FormEditor 파사드를 사용하여 Java에서 PDF 양식 버튼의 제출 URL을 설정하는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java에서 PDF 양식 제출 URL 구성
Abstract: 이 문서에서는 기존 PDF를 바인딩하고, 제출 URL을 설정하고, 버튼 필드에 대한 제출 플래그를 설정하고, Java용 Aspose.PDF에서 FormEditor 파사드를 사용하여 업데이트된 문서를 저장하는 방법을 보여줍니다.
---
## 
제출 URL 설정


1. 
소스 PDF를 `FormEditor` 파사드에 바인딩합니다.

2. 
버튼 필드는 `setSubmitUrl(...)`으로 전화하세요.

3. 
제출 형식에 제출 플래그를 적용합니다.

4. 
업데이트된 문서를 저장합니다.

```java
public static void setSubmitUrl(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setSubmitUrl("Script_Demo_Button", "http://www.example.com/submit");
        editor.setSubmitFlag("Script_Demo_Button", SubmitFormFlag.Xfdf);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
