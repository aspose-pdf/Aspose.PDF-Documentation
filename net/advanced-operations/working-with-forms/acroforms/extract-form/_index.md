---
title: Extract AcroForm
linktitle: Extract AcroForm
type: docs
weight: 30
url: /net/extract-form/
description: Extract form from your PDF document with Aspose.PDF for .NET library. Get value from an individual field of PDF file.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extract data from form

### Get Values from all the Fields of PDF Document

To get values from all the fields in a PDF document, you need to navigate through all the form fields and then get the value using the Value property. Get each field from the Form collection, in the base field type called Field and access its Value property.

The following code snippets show how to get the values of all the fields from a PDF document.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Open document
Document pdfDocument = new Document(dataDir + "GetValuesFromAllFields.pdf");

// Get values from all fields
foreach (Field formField in pdfDocument.Form)
{
    Console.WriteLine("Field Name : {0} ", formField.PartialName);
    Console.WriteLine("Value : {0} ", formField.Value);
}
```

### Get Value from an Individual Field of PDF Document

The form field’s Value property allows you to get the value of a particular field. To get the value, get the form field from the Document object’s Form collection. This example selects a [TextBoxField](https://apireference.aspose.com/pdf/net/aspose.pdf.forms/textboxfield) and retrieves its value using the Value property.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Open document
Document pdfDocument = new Document(dataDir + "GetValueFromField.pdf");

// Get a field
TextBoxField textBoxField = pdfDocument.Form["textbox1"] as TextBoxField;

// Get field value
Console.WriteLine("PartialName : {0} ", textBoxField.PartialName);
Console.WriteLine("Value : {0} ", textBoxField.Value);
```

To get the submit button’s URL, use the following lines of code.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Open document
Document pdfDocument = new Document(dataDir + "GetValueFromField.pdf");
SubmitFormAction act = pdfDocument.Form[1].OnActivated as SubmitFormAction;
if(act != null)
Console.WriteLine(act.Url.Name);
```

### Get Form Fields from a Specific Region of PDF File

Sometimes, you might know where in a document a form field is, but not have it’s name. For example, if all you have to go from is a schematic of a printed form. With Aspose.PDF for .NET, this is not a problem. You can find out which fields are in a given region of a PDF file. To get form fields from a specific region of a PDF file:

1. Open the PDF file using the [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) object.
1. Get the form from the document’s Forms collection.
1. Specify the rectangular region and pass it to the Form object’s GetFieldsInRect method. A Fields collection is returned.
1. Use this to manipulate the fields.

The following code snippet shows how to get form fields in a specific rectangular region of a PDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Open pdf file
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "GetFieldsFromRegion.pdf");

// Create rectangle object to get fields in that area
Aspose.Pdf.Rectangle rectangle = new Aspose.Pdf.Rectangle(35, 30, 500, 500);

// Get the PDF form
Aspose.Pdf.Forms.Form form = doc.Form;

// Get fields in the rectangular area
Aspose.Pdf.Forms.Field[] fields = form.GetFieldsInRect(rectangle);

// Display Field names and values
foreach (Field field in fields)
{
    // Display image placement properties for all placements
    Console.Out.WriteLine("Field Name: " + field.FullName + "-" + "Field Value: " + field.Value);
}
```
