---
title: PDF 파일에서 주석 수정하기 (파사드)
type: docs
weight: 50
url: /ko/java/modify-annotations/
description: 이 섹션에서는 Aspose.PDF Facades를 사용하여 PDF 파일의 주석을 XFDF로 수정하는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[modifyAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#modifyAnnotations-int-int-com.aspose.pdf.Annotation-) 메소드는 주석의 기본 속성, 즉 주제, 수정 날짜, 작성자, 주석 색상 및 열린 플래그를 변경할 수 있게 해줍니다. 또한 ModifyAnnotations 메소드를 사용하여 작성자를 직접 설정할 수 있습니다. 이 클래스는 주석을 삭제하는 두 가지 오버로드된 메소드도 제공합니다. 첫 번째 메소드인 DeleteAnnotations는 PDF 파일에서 모든 주석을 삭제합니다.

예를 들어, 다음 코드에서 [modifyAnnotationsAuthor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#modifyAnnotationsAuthor-int-int-java.lang.String-java.lang.String-)를 사용하여 주석의 작성자를 변경하는 것을 고려하십시오.

```java
 public static void ModifyAnnotationsAuthor() {
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
        annotationEditor.modifyAnnotationsAuthor(1, 2, "Aspose User", "Aspose.PDF user");
        annotationEditor.save(_dataDir + "ModifyAnnotationsAuthor.pdf");
    }
```

두 번째 메서드는 지정된 유형의 모든 주석을 삭제할 수 있습니다.

```java
    public static void ModifyAnnotations() {
        Document document = new Document(_dataDir + "sample_cats_dogs.pdf");
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(document);

        // 주석 속성을 수정하기 위해 Annotation 유형의 새 객체를 만듭니다.
        DefaultAppearance defaultAppearance = new DefaultAppearance();
        FreeTextAnnotation annotation = new FreeTextAnnotation(document.getPages().get_Item(1),
                new Rectangle(1, 1, 1, 1), defaultAppearance);

        annotation.setTitle("Aspose.PDF 데모 사용자");
        annotation.setSubject("기술 기사");

        // PDF 파일의 주석을 수정합니다.
        annotationEditor.modifyAnnotations(1, 1, annotation);
        annotationEditor.save(_dataDir + "ModifyAnnotations.pdf");
    }
```


## 참조

비교하고 자신에게 맞는 주석 작업 방법을 찾아보세요. [PDF 주석](/pdf/ko/java/annotations/) 섹션을 배워봅시다.