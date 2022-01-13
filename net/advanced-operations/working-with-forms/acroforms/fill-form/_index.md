---
title: Fill AcroForm
linktitle: Fill AcroForm
type: docs
weight: 20
url: /net/fill-form/
description: Fill form in your PDF file with Aspose.PDF for .NET
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Fill Form Field in a PDF Document

To fill a form field, get the field from the Document object’s Form collection. then set the field value using the field’s Value property.

This example selects a TextBoxField and sets its value using the Value property.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Open document
Document pdfDocument = new Document(dataDir + "FillFormField.pdf");

// Get a field
TextBoxField textBoxField = pdfDocument.Form["textbox1"] as TextBoxField;

// Modify field value
textBoxField.Value = "Value to be filled in the field";
dataDir = dataDir + "FillFormField_out.pdf";
// Save updated document
pdfDocument.Save(dataDir);
```

