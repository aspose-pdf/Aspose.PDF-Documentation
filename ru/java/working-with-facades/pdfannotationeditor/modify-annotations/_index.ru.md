---
title: Изменение аннотаций в вашем PDF файле (facades)
type: docs
weight: 50
url: /java/modify-annotations/
description: Этот раздел объясняет, как изменить аннотации из PDF файла в XFDF с помощью Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[modifyAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#modifyAnnotations-int-int-com.aspose.pdf.Annotation-) метод позволяет изменить основные атрибуты аннотации, такие как Тема, Дата изменения, Автор, Цвет аннотации и Флаг открытия. Вы также можете установить Автора напрямую, используя метод ModifyAnnotations. Этот класс также предоставляет два перегруженных метода для удаления аннотаций. Первый метод, называемый DeleteAnnotations, удаляет все аннотации из PDF файла.

Например, в следующем коде, рассмотрите изменение автора в нашей аннотации, используя [modifyAnnotationsAuthor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#modifyAnnotationsAuthor-int-int-java.lang.String-java.lang.String-).

```java
 public static void ModifyAnnotationsAuthor() {
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
        annotationEditor.modifyAnnotationsAuthor(1, 2, "Aspose User", "Aspose.PDF user");
        annotationEditor.save(_dataDir + "ModifyAnnotationsAuthor.pdf");
    }
```

Второй метод позволяет удалить все аннотации заданного типа.

```java
    public static void ModifyAnnotations() {
        Document document = new Document(_dataDir + "sample_cats_dogs.pdf");
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(document);

        // Создать новый объект типа Annotation для изменения атрибутов аннотации
        DefaultAppearance defaultAppearance = new DefaultAppearance();
        FreeTextAnnotation annotation = new FreeTextAnnotation(document.getPages().get_Item(1),
                new Rectangle(1, 1, 1, 1), defaultAppearance);

        annotation.setTitle("Aspose.PDF Demo User");
        annotation.setSubject("Technical Article");

        // Изменить аннотации в PDF файле
        annotationEditor.modifyAnnotations(1, 1, annotation);
        annotationEditor.save(_dataDir + "ModifyAnnotations.pdf");
    }
```


## См. также

Попробуйте сравнить и найти способ работы с аннотациями, который вам подходит. Давайте изучим раздел [Аннотации PDF](/pdf/java/annotations/).