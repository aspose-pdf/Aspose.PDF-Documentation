---
title: Изменение аннотаций в вашем PDF
type: docs
weight: 50
url: ru/net/modify-annotations/
description: Этот раздел объясняет, как изменить аннотации из PDF файла в XFDF с помощью Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Метод [ModifyAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/modifyannotations) позволяет изменять основные атрибуты аннотации, такие как Тема, Дата изменения, Автор, Цвет аннотации и Флаг открытия. Вы также можете напрямую установить Автора, используя метод ModifyAnnotations. Этот класс также предоставляет два перегруженных метода для удаления аннотаций. Первый метод, называемый DeleteAnnotations, удаляет все аннотации из PDF файла.  

Например, в следующем коде рассмотрим изменение автора в нашей аннотации с использованием [ModifyAnnotationsAuthor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/modifyannotationsauthor).

```csharp
   public static void ModifyAnnotationsAuthor()
        {
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample_cats_dogs.pdf");
            annotationEditor.ModifyAnnotationsAuthor(1, 2, "Aspose User", "Aspose.PDF user");
            annotationEditor.Save(_dataDir + "ModifyAnnotationsAuthor.pdf");
        }
```

Второй метод позволяет удалить все аннотации указанного типа.

```csharp
   public static void ModifyAnnotations()
        {
            var document = new Document(_dataDir + "sample_cats_dogs.pdf");
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(document);

            // Создать новый объект типа Annotation для изменения атрибутов аннотации
            var defaultAppearance = new Aspose.Pdf.Annotations.DefaultAppearance();
            Aspose.Pdf.Annotations.FreeTextAnnotation annotation = new Aspose.Pdf.Annotations.FreeTextAnnotation(
                document.Pages[1],
                new Aspose.Pdf.Rectangle(1, 1, 1, 1),
                defaultAppearance)
            {

                // Установить новые атрибуты аннотации
                Title = "Пользователь Aspose.PDF Demo",
                Subject = "Техническая статья"
            };
            // Изменить аннотации в PDF файле
            annotationEditor.ModifyAnnotations(1, 1, annotation);
            annotationEditor.Save(_dataDir + "ModifyAnnotations.pdf");
        }
```

## See also

Попробуйте сравнить и найти способ работы с аннотациями, который подходит вам. Давайте изучим раздел [PDF Аннотации](/pdf/net/annotations/).