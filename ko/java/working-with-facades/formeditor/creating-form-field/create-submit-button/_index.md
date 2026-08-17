---
title: 제출 버튼 생성
linktitle: 제출 버튼 생성
type: docs
weight: 60
url: /java/create-submit-button/
description: Aspose.PDF의 FormEditor 파사드를 사용하여 Java에서 PDF 문서에 제출 버튼을 추가하는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java에서 PDF 제출 버튼 만들기
Abstract: 이 문서에서는 기존 PDF를 바인딩하고, 대상 URL이 포함된 제출 버튼 필드를 추가하고, Java용 Aspose.PDF에서 FormEditor 파사드를 사용하여 수정된 문서를 저장하는 방법을 보여줍니다.
---

양식 데이터를 제출하는 버튼을 만들려면 `FormEditorExamples.createSubmitButton(...)`을 사용하세요.


## 
제출 버튼 만들기


1. 
소스 PDF를 `FormEditor` 파사드에 바인딩합니다.

2. 
버튼 이름, 페이지, 라벨, 대상 URL 및 직사각형을 사용하여 `addSubmitBtn(...)`을 호출하세요.

3. 
업데이트된 문서를 저장합니다.

```java
public static void createSubmitButton(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addSubmitBtn("submitbutton", 1, "Submit", "http://localhost/testing/show", 100, 450, 150, 475);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
