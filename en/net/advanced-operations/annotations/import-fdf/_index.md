---
title: Import FDF format annotations to PDF via C#
linktitle: Import FDF format annotations to PDF
type: docs
weight: 50
url: /net/import-fdf/
description: Use existing Form.ImportFdf() or add PdfAnnotationEditor.ImportAnnotationsFromFdf() methods for import FDF format annotations to PDF with Aspose.PDF for .NET.
lastmod: "2024-09-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

{{% alert color="primary" %}}

FDF (Forms Data Format) is a file format that stores and transmits form data and annotations in PDF documents. It is a lightweight PDF version that contains only the form field values or comments, without the full content of the original PDF file. FDF files are often used when submitting form data to a server, or when exchanging annotations without needing to send the entire PDF file. They can be imported back into a PDF to fill in form fields or apply comments.

{{% /alert %}}

[PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/) class contains method to work with import of annotations from FDF file. [PdfAnnotationEditor.ImportAnnotationsFromFdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/importannotationsfromfdf/) method provides the functionality to import annotations from a FDF document to PDF file.

Also, [Class Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/) include the [Form.ImportFdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/importfdf/) method - imports the content of the fields from the FDF file and put them into the new PDF.

The following code snippet shows you how to Import FDF format annotations to PDF with Form.ImportFdf() method:

```csharp
var fdfPath = Params.InputPath + "test.fdf";
var templatePath = Params.InputPath + "Empty.pdf";
var outputPath = Params.OutputPath + "test_form.pdf";

using (var form = new Aspose.Pdf.Facades.Form(templatePath))
{
    using (var fdfInputStream = new FileStream(fdfPath, FileMode.Open))
    {
        form.ImportFdf(fdfInputStream);
    }

    form.Save(outputPath);
}
```

The next code snippet shows how to import FDF format annotations to PDF with PdfAnnotationEditor.ImportAnnotationsFromFdf() method:

```csharp
var fdfPath = Params.InputPath + "test.fdf";
var templatePath = Params.InputPath + "Empty.pdf";
var outputPath = Params.OutputPath + "test_annEditor.pdf";

var editor = new PdfAnnotationEditor();
editor.BindPdf(new Document(templatePath));
editor.ImportAnnotationsFromFdf(fdfPath);
editor.Save(outputPath);
```
