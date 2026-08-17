---
title: Java의 PDF에서 양식 삭제
linktitle: 양식 삭제
type: docs
weight: 70
url: /java/remove-form/
description: 전체 정리 및 대상 삭제를 포함하여 Java용 Aspose.PDF를 사용하여 PDF 페이지에서 양식 개체를 제거합니다.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 페이지에서 양식 리소스 제거
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서에서 양식 리소스를 제거하는 방법을 설명합니다. 페이지 양식 컬렉션을 필터링한 후 페이지에서 모든 양식을 지우고 선택한 입력기 양식 리소스만 삭제하는 방법을 다룹니다.
---

이 예에서는 필드 값만 변경하는 대신 페이지에서 양식 리소스를 제거합니다.


## 
페이지에서 모든 양식 리소스 제거



선택한 페이지의 모든 양식 리소스를 한 번의 작업으로 제거해야 하는 경우 이 예를 사용합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
대상 페이지의 [XFormCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/xformcollection/)에 접근합니다.

1. 
컬렉션을 지우고 업데이트된 문서를 저장합니다.


```java
public static void removeAllForms(Path inputFile, int pageNum, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        XFormCollection forms = document.getPages().get_Item(pageNum).getResources().getForms();
        forms.clear();
        document.save(outputFile.toString());
    }
}
```

## 
특정 양식 리소스 제거



Typewriter 양식과 같이 선택된 양식 리소스만 삭제해야 하는 경우 이 예를 사용합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
대상 페이지의 [XFormCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/xformcollection/)에 접근합니다.

1. 
제거하려는 [XForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/) 리소스를 필터링하고 컬렉션에서 삭제합니다.

1. 
업데이트된 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 저장합니다.

```java
public static void removeSpecifiedForm(Path inputFile, int pageNum, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        XFormCollection forms = document.getPages().get_Item(pageNum).getResources().getForms();
        List<String> formNames = new ArrayList<>();
        for (XForm form : forms) {
            if ("Typewriter".equals(form.getIT()) && "Form".equals(form.getSubtype())) {
                formNames.add(forms.getFormName(form));
            }
        }
        for (String formName : formNames) {
            forms.delete(formName);
        }
        document.save(outputFile.toString());
    }
}
```
