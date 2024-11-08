---
title: 导入和导出注释到XFDF格式使用Aspose.PDF for C++
linktitle: 导入和导出注释到XFDF格式
type: docs
weight: 40
url: /zh/cpp/import-export-xfdf/
description: 您可以使用C++和Aspose.PDF for C++库导入和导出注释为XFDF格式。
lastmod: "2021-12-02"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

XFDF是一种与PDF阅读器兼容的文件格式。XFDF文件使用XML格式存储数据，如表单编码和注释，这些数据可以保存并导入/导出到PDF并查看。

XFDF可以用于更多不同的任务，但在我们的情况下，它可以用于向其他计算机或服务器等发送或接收表单数据或注释，或者用于存档表单数据或注释。

{{% /alert %}}

**Aspose.PDF for C++** 是一个功能丰富的组件，用于编辑PDF文档。 As we know XFDF is an important aspect of PDF forms manipulation, Aspose.Pdf.Facades namespace in Aspose.PDF for C++ has considered this very well, and have provided methods to import and export annotations data to XFDF files.

我们知道，XFDF 是 PDF 表单操作的重要方面，Aspose.Pdf.Facades 命名空间在 Aspose.PDF for C++ 中对此进行了很好的考虑，并提供了将注释数据导入和导出到 XFDF 文件的方法。

[PDFAnnotationEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor/) class contains two methods to work with import and export of annotations to XFDF file.

[PDFAnnotationEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor/) 类包含两个方法，用于处理注释到 XFDF 文件的导入和导出。 [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor#a533c7c17dfd25a2a192617492bbb561c) 方法提供了将注释从 PDF 文档导出到 XFDF 文件的功能，而 [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor#a17902042e1b48f5a85c0cfb8c428af0a) 方法允许您从现有的 XFDF 文件中导入注释。为了导入或导出注释，我们需要指定注释类型。我们可以以枚举的形式指定这些类型，然后将此枚举作为参数传递给这些方法中的任何一个。

以下代码片段向您展示了如何将注释导出到 XFDF 文件：

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Facades;

void AnnotationImportExport::ExportAnnotationXFDF() {

    String _dataDir("C:\\Samples\\");

    // Create PdfAnnotationEditor object
    auto annotationEditor = MakeObject<PdfAnnotationEditor>();

    // Bind PDF document to the Annotation Editor
    annotationEditor->BindPdf(_dataDir + u"AnnotationDemo1.pdf");

    // Export annotations
    auto fileStream = System::IO::File::OpenWrite(_dataDir +u"exportannotations.xfdf");
    auto annotType = MakeArray<AnnotationType>({ AnnotationType::Line, AnnotationType::Square });
    annotationEditor->ExportAnnotationsXfdf(fileStream, 1, 1, annotType);
    fileStream->Flush();
    fileStream->Close();
}
```
下一个代码片段描述了如何将注释导入到XFDF文件中：

```cpp
void AnnotationImportExport::ImportAnnotationXFDF() {

    // 创建PdfAnnotationEditor对象
    auto annotationEditor = MakeObject<PdfAnnotationEditor>();

    // 创建一个新的PDF文档
    auto document = new Document();
    document->get_Pages()->Add();

    annotationEditor->BindPdf(document);

    String _dataDir("C:\\Samples\\");
    String exportFileName = _dataDir + u"exportannotations.xfdf";

    if (!System::IO::File::Exists(exportFileName))
        ExportAnnotationXFDF();

    // 导入注释
    annotationEditor->ImportAnnotationsFromXfdf(exportFileName);

    // 保存输出PDF
    document->Save(_dataDir + u"AnnotationDemo2.pdf");
}
```

## 另一种一次性导出/导入注释的方法

在下面的代码中，ImportAnnotations方法允许直接从另一个PDF文档导入注释。

```cpp
void AnnotationImportExport::ImportAnnotationFromPDF() {

    // 创建PdfAnnotationEditor对象
    auto annotationEditor = MakeObject<PdfAnnotationEditor>();

    // 创建一个新的PDF文档
    auto document = new Document();
    document->get_Pages()->Add();

    annotationEditor->BindPdf(document);
    String _dataDir("C:\\Samples\\");
    String exportFileName = _dataDir + u"exportannotations.xfdf";

    if (!System::IO::File::Exists(exportFileName))
        ExportAnnotationXFDF();

    // 注释编辑器允许从多个PDF文档导入注释，
    // 但在此示例中，我们仅使用一个。
    auto fileStreams = MakeArray<String>({ _dataDir + u"AnnotationDemo1.pdf" });
    annotationEditor->ImportAnnotations(fileStreams);

    // 保存输出PDF
    document->Save(_dataDir + u"AnnotationDemo3.pdf");
}
```