---
title: Java를 통해 PDF로 양식 게시
linktitle: 양식 게시
type: docs
weight: 75
url: /java/posting-form/
description: Aspose.PDF for Java를 사용하여 PDF AcroForms에 제출 버튼과 제출 작업을 추가합니다.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 파일에 제출 버튼 및 양식 게시 작업 추가
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 양식에 제출 기능을 추가하는 방법을 보여줍니다. FormEditor를 사용하여 제출 버튼을 생성하고 제출 URL 및 플래그를 더 효과적으로 제어하기 위해 SubmitFormAction을 사용하는 사용자 정의 버튼 필드를 구축하는 방법을 다룹니다.
---

Java용 Aspose.PDF는 파사드 기반 및 DOM 기반 제출 버튼 생성을 모두 지원합니다.


## 
FormEditor로 제출 버튼 추가


1. 
소스 PDF 문서에 대한 [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/) Facade를 만듭니다.

1. 
[FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/) 파사드를 통해 구성된 제출 버튼 개체를 추가합니다.

1. 
업데이트된 PDF 문서를 저장합니다.


```java
public static void addSubmitButton(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    editor.bindPdf(inputFile.toString());
    try {
        editor.addSubmitBtn("submitbutton", 1, "Submit", "http://localhost/testing/show",
                100, 450, 150, 475);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```

## 
제출 작업을 수동으로 추가


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[SubmitFormAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/submitformaction/) 및 URL [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/)을 생성합니다.

1. 
대상 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)에 [ButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/)를 생성하고 제출 작업을 할당합니다.

1. 
업데이트된 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 저장합니다.

```java
public static void addSubmitAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        SubmitFormAction submitAction = new SubmitFormAction();
        submitAction.setUrl(new FileSpecification("http://localhost:3000/submit"));
        submitAction.setFlags(SubmitFormAction.EXPORT_FORMAT | SubmitFormAction.SUBMIT_COORDINATES);

        ButtonField submitButton = new ButtonField(document.getPages().get_Item(1), new Rectangle(10, 10, 100, 40));
        submitButton.setPartialName("SubmitButton");
        submitButton.setValue("Submit");
        submitButton.getPdfActions().add(submitAction);

        document.getForm().add(submitButton, 1);
        document.save(outputFile.toString());
    }
}
```
