---
title: Извлечение Аннотаций (фасады)
type: docs
weight: 30
url: /ru/java/extract-annotation/
description: Этот раздел объясняет, как извлечь аннотации из PDF файла в XFDF с помощью Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[extractAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#extractAnnotations-int-int-int:A-0) метод позволяет извлекать аннотации из PDF файла. Для того чтобы извлечь аннотации, вам нужно создать объект [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) и привязать PDF файл, используя метод [BindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Facade#bindPdf-com.aspose.pdf.IDocument-). После этого вам нужно создать перечисление типов аннотаций, которые вы хотите извлечь из PDF файла. И, наконец, сохраните обновленный PDF файл, используя метод Save объекта PdfAnnotationEditor. Следующий фрагмент кода показывает, как извлечь аннотации из PDF файла.

```java
  public static void ExtractAnnotation() {
        var document = new Document(_dataDir + "sample_cats_dogs.pdf");
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(document);

        // Извлечение аннотаций
        var annotationTypes = new int[] { AnnotationType.FreeText, AnnotationType.Text };
        var annotations = annotationEditor.extractAnnotations(1, 2, annotationTypes);
        for (var annotation : annotations) {
            System.out.println(annotation.getContents());
        }
```