---
title: Import and Export Annotations to XFDF format using Aspose.PDF for C++
linktitle: Import and Export Annotations to XFDF format
type: docs
weight: 40
url: /cpp/import-export-xfdf/
description: You may import and export annotation with XFDF format with C++ and Aspose.PDF for C++ library.
lastmod: "2021-12-02"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

XFDF is a file format compatible with  PDF readers. XFDF files used XML format to store data such as form encoding and annotations, which can be saved and imported/exported to PDF and viewed.

XFDF can be used for many more different tasks, but in our case, it can be used either to send or receive form data or annotations to other computers or servers, etc., or it can be used to archive form data or annotations.

{{% /alert %}}

**Aspose.PDF for C++** is a feature rich component when it comes to editing the PDF documents. As we know XFDF is an important aspect of PDF forms manipulation, Aspose.Pdf.Facades namespace in Aspose.PDF for C++ has considered this very well, and have provided methods to import and export annotations data to XFDF files.

[PDFAnnotationEditor](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor/) class contains two methods to work with import and export of annotations to XFDF file. [ExportAnnotationsXfdf](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor#a533c7c17dfd25a2a192617492bbb561c) method provides the functionality to export annotations from a PDF document to XFDF file, while [ImportAnnotationFromXfdf](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor#a17902042e1b48f5a85c0cfb8c428af0a) method allows you to import annotations from an existing XFDF file. In order to import or export annotations we need to specify the annotation types. We can specify these types in the form of an enumeration and then pass this enumeration as an argument to any of these methods.

The following code snippet shows you how to export annotations to an XFDF file:

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

The next code snippet describes how import annotations to an XFDF file:

```cpp
void AnnotationImportExport::ImportAnnotationXFDF() {

    // Create PdfAnnotationEditor object
    auto annotationEditor = MakeObject<PdfAnnotationEditor>();

    // Create a new PDF document
    auto document = new Document();
    document->get_Pages()->Add();

    annotationEditor->BindPdf(document);

    String _dataDir("C:\\Samples\\");
    String exportFileName = _dataDir + u"exportannotations.xfdf";

    if (!System::IO::File::Exists(exportFileName))
        ExportAnnotationXFDF();

    // Import annotation
    annotationEditor->ImportAnnotationsFromXfdf(exportFileName);

    // Save output PDF
    document->Save(_dataDir + u"AnnotationDemo2.pdf");
}
```

## Yet another way to export/import annotations at once

In the code below an ImportAnnotations method allows import annotations directly from another PDF doc.

```cpp
void AnnotationImportExport::ImportAnnotationFromPDF() {

    // Create PdfAnnotationEditor object
    auto annotationEditor = MakeObject<PdfAnnotationEditor>();

    // Create a new PDF document
    auto document = new Document();
    document->get_Pages()->Add();

    annotationEditor->BindPdf(document);
    String _dataDir("C:\\Samples\\");
    String exportFileName = _dataDir + u"exportannotations.xfdf";

    if (!System::IO::File::Exists(exportFileName))
        ExportAnnotationXFDF();

    // Annotation Editor allows import annotations from several PDF documents,
    // but in this example, we use only one.
    auto fileStreams = MakeArray<String>({ _dataDir + u"AnnotationDemo1.pdf" });
    annotationEditor->ImportAnnotations(fileStreams);

    // Save output PDF
    document->Save(_dataDir + u"AnnotationDemo3.pdf");
}
```
