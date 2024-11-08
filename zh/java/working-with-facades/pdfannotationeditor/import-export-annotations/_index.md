---
title: 使用 com.aspose.pdf.facades 将注释导入和导出为 XFDF 格式
type: docs
weight: 20
url: /zh/java/import-export-annotations/
description: 本节解释如何使用 Aspose.PDF Facades 将 PDF 文件中的注释导出和导入到 XFDF。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

XFDF 代表 XML Forms Data Format。它是一种基于 XML 的文件格式。此文件格式用于表示 PDF 表单中包含的表单数据或注释。XFDF 可用于许多不同的目的，但在我们的例子中，它可以用于发送或接收表单数据或注释到其他计算机或服务器等，或者用于存档表单数据或注释。在本文中，我们将看到 Aspose.Pdf.Facades 如何考虑这一概念，以及我们如何将注释数据导入和导出到 XFDF 文件。

[PDFAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) 类包含两个方法，用于处理注释到 XFDF 文件的导入和导出。
 [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#exportAnnotationsToXfdf-java.io.OutputStream-) 方法提供了将 PDF 文档中的注释导出到 XFDF 文件的功能，而 [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#importAnnotationFromXfdf-java.io.InputStream-) 方法允许您从现有的 XFDF 文件中导入注释。为了导入或导出注释，我们需要指定注释类型。我们可以以枚举的形式指定这些类型，然后将此枚举作为参数传递给这些方法中的任何一个。

以下代码片段向您展示了如何将注释导入到 XFDF 文件：

```java
public static void ImportAnnotation() {
        String[] sources = new String[] { _dataDir + "sample_cats_dogs.pdf" };
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(_dataDir + "sample.pdf");
        annotationEditor.importAnnotations(sources);
        annotationEditor.save(_dataDir + "sample_demo.pdf");
    }
```

下一个代码片段描述了如何将注释导入/导出到XFDF文件：

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

这样，指定类型的注释将仅被导入或导出到XFDF文件。

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