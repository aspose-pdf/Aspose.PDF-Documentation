---
title:  Extract data from AcroForm using Aspose.PDF for .NET
linktitle:  Extract data from AcroForm
type: docs
weight: 50
url: /net/extract-data-from-acroform/
description: Aspose.PDF makes it easy to extract form field data from PDF files. Learn how to extract data from AcroForms and save it into JSON, XML, or FDF format.
lastmod: "2020-12-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extract form fields from PDF document

As well as enabling you to generate form fields and fill form fields, Aspose.PDF for .NET makes it easy to extract form field data or information about form fields from PDF files.

In the sample code below we demonstrate how to iterate through each page in a PDF to extract information about all of the AcroForm in the PDF as well as the form field values. This sample code presumes that you don’t know the name of the form fields in advance.

```csharp
public static void ExtractFormFields()
{
    var document = new Aspose.Pdf.Document(Path.Combine(_dataDir, "StudentInfoFormElectronic.pdf"));
    // Get values from all fields
    foreach (Field formField in document.Form)
    {
        Console.WriteLine("Field Name : {0} ", formField.PartialName);
        Console.WriteLine("Value : {0} ", formField.Value);
    }
}
```

If you do know the name of the form fields that you wish to extract values from then you can use indexer in Documents.Form collection to quickly retrieve this data. Look at the bottom of this article for a sample code on how to use that function.

## Retrieve form field value by title

The form field's Value property allows you to get the value of a particular field. To get the value, get the form field from the Document object’s Form collection. This example selects a TextBoxField and retrieves its value using the Value property.

## Extract form fields from PDF document to JSON

```csharp
public static void ExtractFormFieldsToJson()
{
    var document = new Aspose.Pdf.Document(Path.Combine(_dataDir, "StudentInfoFormElectronic.pdf"));
    var formData = document.Form.Cast<Field>().Select(f => new { Name = f.PartialName, f.Value });
    string jsonString = JsonSerializer.Serialize(formData);
    Console.WriteLine(jsonString);
}
```

## Extract Data to XML from a PDF File

Form class allows you to export data to an XML file from the PDF file using ExportXml method. In order to export data to XML, you need to create an object of Form class and then call the ExportXml method using the FileStream object. Finally, you can close FileStream object and dispose Form object. The following code snippet shows you how to export data to XML file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

// Open document
Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
form.BindPdf(dataDir + "input.pdf");
// Create xml file.
System.IO.FileStream xmlOutputStream = new FileStream( dataDir + "input.xml", FileMode.Create);
// Export data
form.ExportXml(xmlOutputStream);
// Close file stream
xmlOutputStream.Close();

// Close the document
form.Dispose();
```

## Export Data to FDF from a PDF File

Form class allows you to export data to an FDF file from the PDF file using ExportFdf method. In order to export data to FDF, you need to create an object of Form class and then call the ExportFdf method using the FileStream object. Finally, you can save the PDF file using Save method of the Form class. The following code snippet shows you how to export data to FDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
// Open Document
form.BindPdf(dataDir + "input.pdf");

// Create fdf file.
System.IO.FileStream fdfOutputStream = new FileStream(dataDir + "student.fdf", FileMode.Create);

// Export data
form.ExportFdf(fdfOutputStream);

// Close file stream
fdfOutputStream.Close();

// Save updated document
form.Save(dataDir + "ExportDataToPdf_out.pdf");
```

## Export Data to XFDF from a PDF File

Form class allows you to export data to an XFDF file from the PDF file using ExportXfdf method. In order to export data to XFDF, you need to create an object of Form class and then call the ExportXfdf method using the FileStream object. Finally, you can save the PDF file using Save method of the Form class. The following code snippet shows you how to export data to XFDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
// Open Document
form.BindPdf(dataDir + "input.pdf");

// Create xfdf file.
System.IO.FileStream xfdfOutputStream = new FileStream("student1.xfdf", FileMode.Create);

// Export data
form.ExportXfdf(xfdfOutputStream);

// Close file stream
xfdfOutputStream.Close();

// Save updated document
form.Save(dataDir + "ExportDataToXFDF_out.pdf");
```
