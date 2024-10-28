---
title: 주석 추출 (파사드)
type: docs
weight: 30
url: /java/extract-annotation/
description: 이 섹션에서는 Aspose.PDF Facades를 사용하여 PDF 파일에서 XFDF로 주석을 추출하는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[extractAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#extractAnnotations-int-int-int:A-0) 메서드는 PDF 파일에서 주석을 추출할 수 있게 해줍니다. 주석을 추출하기 위해서는 [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Facade#bindPdf-com.aspose.pdf.IDocument-) 메서드를 사용하여 PDF 파일을 바인딩해야 합니다. 그 후, PDF 파일에서 추출하고자 하는 주석 유형의 열거를 생성해야 합니다. 마지막으로, PdfAnnotationEditor 객체의 Save 메서드를 사용하여 업데이트된 PDF 파일을 저장합니다. 다음 코드 스니펫은 PDF 파일에서 주석을 추출하는 방법을 보여줍니다.

```java
  public static void ExtractAnnotation() {
        var document = new Document(_dataDir + "sample_cats_dogs.pdf");
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(document);

        // 주석 추출
        var annotationTypes = new int[] { AnnotationType.FreeText, AnnotationType.Text };
        var annotations = annotationEditor.extractAnnotations(1, 2, annotationTypes);
        for (var annotation : annotations) {
            System.out.println(annotation.getContents());
        }
```