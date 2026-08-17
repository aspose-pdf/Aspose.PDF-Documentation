---
title: AcroForm 수정
linktitle: AcroForm 수정
type: docs
weight: 45
url: /java/modifying-form/
description: 텍스트 지우기, 제한 설정, 필드 스타일 지정 및 필드 제거를 포함하여 Java용 Aspose.PDF를 사용하여 PDF 문서의 AcroForm 필드를 수정합니다.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 양식 필드 수정 및 사용자 정의
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 AcroForm 콘텐츠를 수정하는 방법을 설명합니다. 입력기 양식 리소스에서 텍스트 지우기, 텍스트 필드 길이 제한 설정 및 읽기, 양식 필드 글꼴 모양 변경, 이름으로 특정 필드 삭제 등을 다룹니다.
---

양식 유지 관리에는 필드 수준 편집과 양식 관련 페이지 리소스 정리가 모두 포함되는 경우가 많습니다.


## 
포함된 양식 리소스의 텍스트 지우기



양식 개체 자체를 제거하지 않고 Typewriter 양식 콘텐츠를 비워야 하는 경우 이 예를 사용합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
페이지 양식 리소스를 반복하고 타자기 양식을 찾습니다.

1. 
흡수된 텍스트 조각을 지우고 문서를 저장합니다.


```java
public static void clearTextInForm(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (XForm form : document.getPages().get_Item(1).getResources().getForms()) {
            if ("Typewriter".equals(form.getIT()) && "Form".equals(form.getSubtype())) {
                TextFragmentAbsorber absorber = new TextFragmentAbsorber();
                absorber.visit(form);

                for (TextFragment fragment : absorber.getTextFragments()) {
                    fragment.setText("");
                }
            }
        }
        document.save(outputFile.toString());
    }
}
```

## 
텍스트 필드 길이 제한 설정



텍스트 필드에 제한된 수의 문자만 허용해야 하는 경우 이 예를 사용하십시오.


1. 
[FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/) Facade를 생성하고 소스 PDF를 바인딩합니다.

1. 
대상 필드의 최대 길이를 설정합니다.

1. 
업데이트된 문서를 저장합니다.


```java
public static void setFieldLimit(Path inputFile, Path outputFile) {
    FormEditor form = new FormEditor();
    form.bindPdf(inputFile.toString());
    try {
        form.setFieldLimit("First Name", 15);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## 
텍스트 필드 길이 제한 가져오기



텍스트 필드의 현재 최대 길이를 검사해야 할 때 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
양식 컬렉션에서 대상 필드에 액세스합니다.

1. 
[TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/)에서 제한값을 읽어 출력합니다.


```java
public static void getFieldLimit(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Field field = document.getForm().getFields()[0];
        if (field instanceof TextBoxField textBoxField) {
            System.out.println("Limit: " + textBoxField.getMaxLen());
        }
    }
}
```

## 
양식 필드 글꼴 변경



기존 텍스트 필드가 다른 글꼴이나 모양을 사용해야 하는 경우 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
대상 [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/)에 액세스하고 새로운 기본 모양을 설정합니다.

1. 
업데이트된 PDF를 저장합니다.


```java
public static void setFormFieldFont(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Field field = document.getForm().getFields()[0];
        if (field instanceof TextBoxField textBoxField) {
            textBoxField.setDefaultAppearance(new DefaultAppearance(
                    FontRepository.findFont("Calibri"), 10, com.aspose.pdf.Color.getBlack().toRgb()));
        }

        document.save(outputFile.toString());
    }
}
```

## 
이름으로 양식 필드 삭제



AcroForm에서 특정 필드를 제거해야 하는 경우 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
이름으로 양식에서 대상 필드를 삭제합니다.

1. 
업데이트된 문서를 저장합니다.

```java
public static void deleteFormField(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getForm().delete("First Name");
        document.save(outputFile.toString());
    }
}
```
