---
title: Удаление Аннотаций (фасады)
type: docs
weight: 10
url: /ru/java/delete-annotations/
description: Этот раздел объясняет, как удалить аннотации с помощью Aspose.PDF Facades, используя класс PdfAnnotationEditor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Вы можете использовать класс [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) для удаления аннотаций, по указанному типу аннотации, из существующего PDF файла.
 Вам необходимо создать объект [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) и связать входной PDF файл, используя метод bindPdf. После этого вызовите метод [deleteAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#deleteAnnotation-java.lang.String-), с строковым параметром, чтобы удалить все аннотации из файла; строковый параметр представляет тип аннотации, которую нужно удалить. Наконец, используйте метод save, чтобы сохранить обновленный PDF файл.

Следующий фрагмент кода показывает, как удалить аннотацию по указанному типу аннотации.

```java
public static void DeleteAnnotation() {
        // Открыть документ
        Scanner consoleScanner = new Scanner(System.in);
        Document document = new Document(_dataDir + "sample_cats_dogs.pdf");
        int index;
        for (index = 1; index <= document.getPages().get_Item(1).getAnnotations().size(); index++) {
            System.out.println(index + ". " + document.getPages().get_Item(1).getAnnotations().get_Item(index).getName()
                    + " " + document.getPages().get_Item(1).getAnnotations().get_Item(index).toString());
        }
        System.out.print("Пожалуйста, введите номер:");
        index = consoleScanner.nextInt();

        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(document);
        annotationEditor.deleteAnnotation(document.getPages().get_Item(1).getAnnotations().get_Item(1).getName());

        // Сохранить обновленный PDF
        annotationEditor.save(_dataDir + "DeleteAnnotation.pdf");
        consoleScanner.close();
    }
    ```
[PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) позволяет удалять все аннотации из существующего PDF файла.

Во-первых, создайте [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) и свяжите входной PDF файл с помощью метода BindPdf.

После этого вызовите метод [deleteAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#deleteAnnotation-java.lang.String-), чтобы удалить все аннотации из файла, а затем используйте метод Save, чтобы сохранить обновленный PDF файл. Следующий фрагмент кода показывает, как удалить все аннотации из PDF файла.

```java
public static void DeleteAllAnnotations() {
    // Открыть документ
    PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
    annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
    // Удалить все аннотации
    annotationEditor.deleteAnnotations();
    // Сохранить обновленный PDF
    annotationEditor.save(_dataDir + "DeleteAllAnnotations_out.pdf");
}
```