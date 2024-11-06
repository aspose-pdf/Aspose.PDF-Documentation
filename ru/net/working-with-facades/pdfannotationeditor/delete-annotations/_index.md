---
title: Удалить аннотации (фасады)
type: docs
weight: 10
url: ru/net/delete-annotations/
description: Этот раздел объясняет, как удалить аннотации с использованием Aspose.PDF Facades и класса PdfAnnotationEditor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Удалить все аннотации из существующего PDF файла

[PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) позволяет удалить все аннотации из существующего PDF файла. Первым делом создайте объект [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) и свяжите входной PDF-файл, используя метод [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). После этого вызовите метод [DeleteAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/deleteannotations) для удаления всех аннотаций из файла, а затем используйте метод [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) для сохранения обновленного PDF-файла. Следующий фрагмент кода показывает, как удалить все аннотации из PDF-файла.

```csharp
   public static void DeleteAllAnnotations()
        {
            // Открыть документ
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample_cats_dogs.pdf");
            // Удалить все аннотации
            annotationEditor.DeleteAnnotations();
            // Сохранить обновленный PDF
        }   
    
```
## Удаление всех аннотаций по указанному типу

Вы можете использовать класс [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) для удаления всех аннотаций указанного типа из существующего PDF-файла. Для этого вам нужно создать объект [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) и привязать входной PDF-файл, используя метод [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). После этого вызовите метод [DeleteAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/deleteannotations) с параметром-строкой, чтобы удалить все аннотации из файла; строковый параметр представляет тип аннотации, который нужно удалить. Наконец, используйте метод [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save), чтобы сохранить обновленный PDF-файл. В следующем фрагменте кода показано, как удалить все аннотации по указанному типу аннотации.

```csharp
    public static void DeleteAnnotation()
        {
            // Открыть документ
            var document = new Document(_dataDir + "sample_cats_dogs.pdf");
            int index;
            for (index = 1; index <= document.Pages[1].Annotations.Count; index++)
            {
                System.Console.WriteLine($"{index}. {document.Pages[1].Annotations[index].Name} {document.Pages[1].Annotations[index].AnnotationType}");
            }
            System.Console.Write("Пожалуйста, введите номер:");
            index = int.Parse(System.Console.ReadLine());

            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(document);
            annotationEditor.DeleteAnnotation(document.Pages[1].Annotations[index].Name);

            // Сохранить обновленный PDF
            annotationEditor.Save(_dataDir + "DeleteAnnotation.pdf");
        }
```