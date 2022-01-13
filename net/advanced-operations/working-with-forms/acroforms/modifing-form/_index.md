---
title: Modifing AcroForm
linktitle: Modifing AcroForm
type: docs
weight: 40
url: /net/modifing-form/
description: Modifing form in your PDF file with Aspose.PDF for .NET library. You can Add or remove fields in existing form, getand set fieldlimit and etc.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Get or Set Field Limit

The FormEditor class SetFieldLimit(field, limit) method allows you to set a field limit, the maximum number of characters that can be entered into a field.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Adding Field with limit
FormEditor form = new FormEditor();

form.BindPdf( dataDir + "input.pdf");
form.SetFieldLimit("textbox1", 15);
dataDir = dataDir + "SetFieldLimit_out.pdf";
form.Save(dataDir);
```

Similarly, Aspose.PDF has a method that gets the field limit using the DOM approach. The following code snippet shows the steps.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
// Getting maximum field limit using DOM
Document doc = new Document(dataDir + "FieldLimit.pdf");
Console.WriteLine("Limit: " + (doc.Form["textbox1"] as TextBoxField).MaxLen);
```

You can also get the same value using the *Aspose.PDF.Facades* namespace using the following code snippet.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
// Getting maximum field limit using Facades
Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
form.BindPdf(dataDir + "FieldLimit.pdf");
Console.WriteLine("Limit: " + form.GetFieldLimit("textbox1"));
```

## Set Custom Font for the Form Field

Form fields in Adobe PDF files can be configured to use specific default fonts. In the early versions of Aspose.PDF, only the 14 default fonts were supported. Later releases allowed developers to apply any font. To set and update the default font used for form fields, use the DefaultAppearance(Font font, double size, Color color) class. This class can be found under the Aspose.PDF.InteractiveFeatures namespace. To use this object, use the Field class DefaultAppearance property.

The following code snippet shows how to set the default font for PDF form fields.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Open document
Document pdfDocument = new Document(dataDir + "FormFieldFont14.pdf");

// Get particular form field from document
Aspose.Pdf.Forms.Field field = pdfDocument.Form["textbox1"] as Aspose.Pdf.Forms.Field;

// Create font object
Aspose.Pdf.Text.Font font = FontRepository.FindFont("ComicSansMS");

// Set the font information for form field
// Field.DefaultAppearance = new Aspose.Pdf.Forms.in.DefaultAppearance(font, 10, System.Drawing.Color.Black);

dataDir = dataDir + "FormFieldFont14_out.pdf";
// Save updated document
pdfDocument.Save(dataDir);
```

## Add/remove fields in existing form

All the form fields are contained in the Document object’s Form collection. This collection provides different methods that manage form fields, including the Delete method. If you want to delete a particular field, pass the field name as a parameter to the Delete method and then save the updated PDF document. The following code snippet shows how to delete a particular field from a PDF document.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Open document
Document pdfDocument = new Document(dataDir + "DeleteFormField.pdf");

// Delete a particular field by name
pdfDocument.Form.Delete("textbox1");
dataDir = dataDir + "DeleteFormField_out.pdf";
// Save modified document
pdfDocument.Save(dataDir);
```
