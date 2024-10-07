---
title: 导入和导出注释到XFDF
type: docs
weight: 20
url: /net/import-export-annotations/
description: 本节解释如何使用Aspose.PDF Facades将PDF文件中的注释导入和导出到XFDF。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

XFDF代表XML Forms Data Format。它是一种基于XML的文件格式。此文件格式用于表示PDF表单中包含的表单数据或注释。XFDF可以用于许多不同的目的，但在我们的例子中，它可以用于在计算机或服务器之间发送或接收表单数据或注释，也可以用于存档表单数据或注释。在本文中，我们将看到Aspose.Pdf.Facades如何考虑到这个概念，以及我们如何将注释数据导入和导出到XFDF文件。

## 导入和导出注释到XFDF

[Aspose.PDF for .NET](/pdf/net/)是一个功能丰富的组件，当涉及到编辑PDF文档时。 ```
As we know XFDF is an important aspect of PDF forms manipulation, [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) in [Aspose.PDF for .NET](/pdf/net/) has considered this very well, and have provided methods to import and export annotations data to XFDF files.

[PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) class contains two methods to work with import and export of annotations to XFDF file.
```

```
正如我们所知，XFDF 是 PDF 表单操作的重要方面，[Aspose.Pdf.Facades 命名空间](https://reference.aspose.com/pdf/net/aspose.pdf.facades) 在 [Aspose.PDF for .NET](/pdf/net/) 中对此进行了充分考虑，并提供了将注释数据导入和导出到 XFDF 文件的方法。

[PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) 类包含两个用于处理注释到 XFDF 文件的导入和导出的方法。
``` [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/exportannotationsxfdf/index) 方法提供了将PDF文档中的注释导出到XFDF文件的功能，而 [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/importannotationfromxfdf/index) 方法允许您从现有的XFDF文件中导入注释。为了导入或导出注释，我们需要指定注释类型。我们可以通过枚举的形式指定这些类型，然后将此枚举作为参数传递给任何这些方法。这样，只有指定类型的注释才会被导入或导出到XFDF文件中。

以下代码片段向您展示了如何将注释导入XFDF文件：

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
下一个代码片段描述了如何将注释导入/导出到XFDF文件：

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

这样，只有指定类型的注释才会被导入或导出到XFDF文件。

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