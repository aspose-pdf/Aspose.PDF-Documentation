---
title: Импорт и экспорт аннотаций в формат XFDF с использованием com.aspose.pdf.facades
type: docs
weight: 20
url: ru/java/import-export-annotations/
description: Этот раздел объясняет, как экспортировать и импортировать аннотации из PDF-файла в XFDF с помощью Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

XFDF означает XML Forms Data Format. Это файловый формат на основе XML. Этот формат файла используется для представления данных формы или аннотаций, содержащихся в PDF-форме. XFDF может использоваться для многих различных целей, но в нашем случае он может использоваться для отправки или получения данных формы или аннотаций на другие компьютеры или серверы и т. д., или он может использоваться для архивирования данных формы или аннотаций. В этой статье мы рассмотрим, как Aspose.Pdf.Facades учел этот концепт и как мы можем импортировать и экспортировать данные аннотаций в файл XFDF.

Класс [PDFAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) содержит два метода для работы с импортом и экспортом аннотаций в файл XFDF.
 [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#exportAnnotationsToXfdf-java.io.OutputStream-) метод предоставляет функциональность для экспорта аннотаций из PDF-документа в файл XFDF, в то время как метод [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#importAnnotationFromXfdf-java.io.InputStream-) позволяет импортировать аннотации из существующего файла XFDF. Для того чтобы импортировать или экспортировать аннотации, нам нужно указать типы аннотаций. Мы можем указать эти типы в виде перечисления, а затем передать это перечисление в качестве аргумента любому из этих методов.

Следующий фрагмент кода показывает, как импортировать аннотации в файл XFDF:

```java
public static void ImportAnnotation() {
        String[] sources = new String[] { _dataDir + "sample_cats_dogs.pdf" };
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(_dataDir + "sample.pdf");
        annotationEditor.importAnnotations(sources);
        annotationEditor.save(_dataDir + "sample_demo.pdf");
    }
```

Следующий фрагмент кода описывает, как импортировать/экспортировать аннотации в файл XFDF:

```java
    public static void ImportExportXFDF01() {
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
        OutputStream xmlOutputStream;
        try {
            xmlOutputStream = new FileOutputStream(_dataDir + "sample.xfdf");
            annotationEditor.exportAnnotationsToXfdf(xmlOutputStream);
            xmlOutputStream.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        Document document = new Document();
        document.getPages().add();
        annotationEditor.bindPdf(document);
        annotationEditor.importAnnotationsFromXfdf(_dataDir + "sample.xfdf");
        annotationEditor.save(_dataDir + "ImportedAnnotation.pdf");
    }
```

Таким образом, аннотации указанных типов будут импортироваться или экспортироваться только в файл XFDF.

```java
    public static void ImportExportXFDF02() {
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
        OutputStream xmlOutputStream;

        try {
            xmlOutputStream = new FileOutputStream(_dataDir + "sample.xfdf");
            int[] annotationTypes = new int[] { AnnotationType.FreeText, AnnotationType.Text };
            annotationEditor.exportAnnotationsXfdf(xmlOutputStream, 2, 2, annotationTypes);
            xmlOutputStream.close();
        } catch (IOException e) {            
            e.printStackTrace();
        }

        Document document = new Document(_dataDir + "sample.pdf");
        document.getPages().add();
        annotationEditor.bindPdf(document);
        annotationEditor.importAnnotationsFromXfdf(_dataDir + "sample.xfdf");
        annotationEditor.save(_dataDir + "ImportedAnnotation.pdf");
    }
```