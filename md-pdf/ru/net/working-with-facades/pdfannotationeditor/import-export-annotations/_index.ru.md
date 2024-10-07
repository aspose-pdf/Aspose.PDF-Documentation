---
title: Import and Export Annotations to XFDF 
type: docs
weight: 20
url: /net/import-export-annotations/
description: Этот раздел объясняет, как импортировать и экспортировать аннотации из PDF файла в XFDF с помощью Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

XFDF означает XML Forms Data Format. Это формат файла на основе XML. Этот формат файла используется для представления данных формы или аннотаций, содержащихся в PDF-форме. XFDF может использоваться для множества различных целей, но в нашем случае он может использоваться для отправки или получения данных формы или аннотаций на другие компьютеры или серверы и т. д., или он может использоваться для архивирования данных формы или аннотаций. В этой статье мы рассмотрим, как Aspose.Pdf.Facades учел эту концепцию и как мы можем импортировать и экспортировать данные аннотаций в файл XFDF.

## Импорт и экспорт аннотаций в XFDF

[Aspose.PDF for .NET](/pdf/net/) — это компонент, богатый функциями, когда дело касается редактирования PDF-документов. As we know XFDF is an important aspect of PDF forms manipulation, [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) in [Aspose.PDF for .NET](/pdf/net/) has considered this very well, and have provided methods to import and export annotations data to XFDF files.

Как мы знаем, XFDF является важным аспектом манипуляции с формами PDF, [пространство имен Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) в [Aspose.PDF для .NET](/pdf/net/) хорошо это учло и предоставило методы для импорта и экспорта данных аннотаций в файлы XFDF.

[PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) class contains two methods to work with import and export of annotations to XFDF file.

Класс [PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) содержит два метода для работы с импортом и экспортом аннотаций в файл XFDF. [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/exportannotationsxfdf/index) метод предоставляет возможность экспортировать аннотации из PDF документа в XFDF файл, в то время как метод [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/importannotationfromxfdf/index) позволяет импортировать аннотации из существующего XFDF файла. Для импорта или экспорта аннотаций нам нужно указать типы аннотаций. Мы можем указать эти типы в виде перечисления и затем передать это перечисление в качестве аргумента в любой из этих методов. Таким образом, аннотации указанных типов будут импортированы или экспортированы в XFDF файл.

Следующий фрагмент кода показывает, как импортировать аннотации в XFDF файл:

```csharp
public static void ImportAnnotation()
        {
            var sources = new string[] { _dataDir + "sample_cats_dogs.pdf" };
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample.pdf");
            annotationEditor.ImportAnnotations(sources);
            annotationEditor.Save(_dataDir + "sample_demo.pdf");
        }
```
Следующий фрагмент кода описывает, как импортировать/экспортировать аннотации в файл XFDF:

```csharp
public static void ImportExportXFDF01()
        {
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample_cats_dogs.pdf");
            System.IO.FileStream xmlOutputStream = System.IO.File.OpenWrite(_dataDir + "sample.xfdf");
            annotationEditor.ExportAnnotationsToXfdf(xmlOutputStream);
            xmlOutputStream.Close();
            var document = new Document();
            document.Pages.Add();
            annotationEditor.BindPdf(document);
            annotationEditor.ImportAnnotationsFromXfdf(System.IO.File.OpenRead(_dataDir + "sample.xfdf"));
            annotationEditor.Save(_dataDir + "ImportedAnnotation.pdf");
        }
```

Таким образом, аннотации указанных типов будут импортироваться или экспортироваться только в файл XFDF.

```csharp
   public static void ImportExportXFDF02()
        {
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample_cats_dogs.pdf");
            System.IO.FileStream xmlOutputStream = System.IO.File.OpenWrite(_dataDir + "sample.xfdf");
            var annotationTypes = new[] { AnnotationType.FreeText, AnnotationType.Text };
            annotationEditor.ExportAnnotationsXfdf(xmlOutputStream, 2, 2, annotationTypes);
            xmlOutputStream.Close();

            var document = new Document(_dataDir + "sample.pdf");
            document.Pages.Add();
            annotationEditor.BindPdf(document);
            annotationEditor.ImportAnnotationsFromXfdf(System.IO.File.OpenRead(_dataDir + "sample.xfdf"));
            annotationEditor.Save(_dataDir + "ImportedAnnotation.pdf");
        }
```