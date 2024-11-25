---
title: Import and Export Data in JSON
type: docs
weight: 70
url: /net/import-export-json/
description: This section explains how to import and Export Data in JSON
lastmod: "2024-06-05"
draft: false
---

## Import and Export Data from Forms in JSON

Manipulating form fields within PDF documents can be crucial when handling data input and output operations in various applications. The Aspose.PDF library offers robust functionality for exporting and importing form fields in JSON format. Below, we explore several code snippets demonstrating how to perform these tasks using different approaches.

Since 24.7 it's possible to add Import and Export Data from Forms in JSON Format:

### Export form fields to and from the JSON file

This approach exports all the form fields from an existing PDF document into a JSON file and imports them into a new PDF document.

```cs
string inputPdfPath = "documentWithFields.pdf";
string outputJsonPath = "exportingFields.json";
string outputPdfPath = "newDocumentWithFields.pdf";
ExportFieldsToJsonOptions options = new ExportFieldsToJsonOptions();
options.WriteIndented = true;
using (Document document = new Document(inputPdfPath))
{
    IEnumerable<FieldSerializationResult> exportResult = document.Form.ExportToJson(outputJsonPath, options);
}
```

### Import form fields to and from the JSON file

```cs
string inputPdfPath = "documentWithFields.pdf";
string outputJsonPath = "exportingFields.json";
string outputPdfPath = "newDocumentWithFields.pdf";
using (Document document = new Document(inputPdfPath))
{
    Page page = newDocument.Pages.Add();
    IEnumerable<FieldSerializationResult> importResult = newDocument.Form.ImportFromJson(outputJsonPath);
    newDocument.Save(outputPdfPath);
}
```

### Export form fields to and from the JSON file using FileStream

This snippet performs the same operations as the previous one but utilizes 'FileStream' to manage the file input and output.

```cs
string inputPdfPath = "documentWithFields.pdf";
string outputJsonPath = "exportingFields.json";
string outputPdfPath = "newDocumentWithFields.pdf";
ExportFieldsToJsonOptions options = new ExportFieldsToJsonOptions();
options.WriteIndented = true;
using (Document document = new Document(inputPdfPath))
{
    using (FileStream fileStream = File.Create(outputJsonPath))
    {
        IEnumerable<FieldSerializationResult> exportResult = document.Form.ExportToJson(fileStream, options);
    }
}
```

### Import form fields to and from the JSON file using FileStream

```cs
string inputPdfPath = "documentWithFields.pdf";
string outputJsonPath = "exportingFields.json";
string outputPdfPath = "newDocumentWithFields.pdf";
using (Document document = new Document(inputPdfPath))
{
    Page page = newDocument.Pages.Add();
    using (FileStream fileStream = File.OpenRead(outputJsonPath))
    {
        IEnumerable<FieldSerializationResult> importResult = newDocument.Form.ImportFromJson(fileStream);
    }
    newDocument.Save(outputPdfPath);
}
```

### Export form fields in JSON format using MemoryStream

In some scenarios, you might prefer to work with data in memory rather than with files on disk. This approach uses 'MemoryStream' to handle the export and import processes entirely in memory.

```cs
string inputPdfPath = "documentWithFields.pdf";
string outputPdfPath = "newDocumentWithFields.pdf";
using (MemoryStream memoryStream = new MemoryStream())
{
    using (Document document = new Document(inputPdfPath))
    {
        IEnumerable<FieldSerializationResult> exportResult = document.Form.ExportToJson(memoryStream);
    }
}
```

### Import form fields in JSON format using MemoryStream

```cs
string inputPdfPath = "documentWithFields.pdf";
string outputPdfPath = "newDocumentWithFields.pdf";
using (Document document = new Document(inputPdfPath))
{
    Page page = newDocument.Pages.Add();
    IEnumerable<FieldSerializationResult> importResult = newDocument.Form.ImportFromJson(memoryStream);
    newDocument.Save(outputPdfPath);
}
```

### Export the specified field to and from the JSON file

Sometimes, you may need to export or import only a specific field rather than all the fields in the document.

```cs
string inputPdfPath = "documentWithFields.pdf";
string outputJsonPath = "exportingField.json";
string outputPdfPath = "newDocumentWithField.pdf";
ExportFieldsToJsonOptions options = new ExportFieldsToJsonOptions();
options.WriteIndented = true;
using (Document document = new Document(inputPdfPath))
{
    WidgetAnnotation field = document.Form[1];
    IEnumerable<FieldSerializationResult> exportResult = field.ExportToJson(outputJsonPath, options);
}
```

### Import the specified field to and from the JSON file

```cs
string inputPdfPath = "documentWithFields.pdf";
string outputJsonPath = "exportingField.json";
string outputPdfPath = "newDocumentWithField.pdf";
using (Document document = new Document(inputPdfPath))
{
    Page page = newDocument.Pages.Add();
    IEnumerable<FieldSerializationResult> importResult = newDocument.Form.ImportFromJson(outputJsonPath);
    newDocument.Save(outputPdfPath);
}
```

### Export the specified field to and from the JSON file using FileStream

This example is similar to the one above but uses 'FileStream' to handle the export and import operations for a specific field.

```cs
string inputPdfPath = "documentWithFields.pdf";
string outputJsonPath = "exportingField.json";
string outputPdfPath = "newDocumentWithField.pdf";
ExportFieldsToJsonOptions options = new ExportFieldsToJsonOptions();
options.WriteIndented = true;
using (Document document = new Document(inputPdfPath))
{
    WidgetAnnotation field = document.Form[1];
    using (FileStream fileStream = File.Create(outputJsonPath))
    {
        IEnumerable<FieldSerializationResult> exportResult = field.ExportToJson(fileStream, options);
    }
}
```

### Import the specified field to and from the JSON file using FileStream

```cs
string inputPdfPath = "documentWithFields.pdf";
string outputJsonPath = "exportingField.json";
string outputPdfPath = "newDocumentWithField.pdf";
using (Document newDocument = new Document())
{
    Page page = newDocument.Pages.Add();
    using (FileStream fileStream = File.OpenRead(outputJsonPath))
    {
        IEnumerable<FieldSerializationResult> importResult = newDocument.Form.ImportFromJson(fileStream);
    }
    newDocument.Save(outputPdfPath);
}
```

### Export the specified field in JSON format using MemoryStream

This code snippet demonstrates how to export a specific form field from a PDF document into JSON format using a 'MemoryStream' and then import it into a new PDF document. 

```cs
string inputPdfPath = "documentWithFields.pdf";
string outputPdfPath = "newDocumentWithField.pdf";
using (MemoryStream memoryStream = new MemoryStream())
{
    using (Document document = new Document(inputPdfPath))
    {
        WidgetAnnotation field = document.Form[1];
        IEnumerable<FieldSerializationResult> exportResult = field.ExportToJson(memoryStream);
    }
}
```

### Import the specified field in JSON format using MemoryStream

```cs
string inputPdfPath = "documentWithFields.pdf";
string outputPdfPath = "newDocumentWithField.pdf";    
using (Document newDocument = new Document())
{
    Page page = newDocument.Pages.Add();
    IEnumerable<FieldSerializationResult> importResult = newDocument.Form.ImportFromJson(memoryStream);
    newDocument.Save(outputPdfPath);
}
```

### Export value from the specified field to the JSON file using FileStream

This code snippet shows how to export the value of a specific form field from a PDF document into a JSON file using FileStream.

```cs
string inputPdfPath = "documentWithFields.pdf";
string outputJsonPath = "fieldsValue.json";
string outputPdfPath = "documentWithImportingFieldsValues.pdf";
using (Document document = new Document(inputPdfPath))
{
    Field field = document.Form.Fields[1];
    using (FileStream fileStream = File.Create(outputJsonPath))
    {
        field.ExportValueToJson(fileStream);
    }
}
```

### Import value to the specified field from the JSON file using FileStream

This code snippet demonstrates how to import a value from a JSON file into a specific form field in a PDF document using FileStream.

```cs
string inputPdfPath = "documentWithFields.pdf";
string outputJsonPath = "fieldsValue.json";
string outputPdfPath = "documentWithImportingFieldsValues.pdf";
using (Document document = new Document(inputPdfPath))
{
    Field field = document.Form.Fields[1];
    using (FileStream fileStream = File.OpenRead(outputJsonPath))
    {
        field.ImportValueFromJson(fileStream);
    }
    document.Save(outputPdfPath);
}
```

### Import value of another field to the specified field from the JSON file using FileStream

This code snippet demonstrates how to import a value of another field to the specified field from the JSON file using FileStream and Aspose.PDF.

```cs
string inputPdfPath = "documentWithFields.pdf";
string outputJsonPath = "fieldsValues.json";
string outputPdfPath = "documentWithImportingFieldsValues.pdf";
using (Document document = new Document(inputPdfPath))
{
    Field field = document.Form.Fields[1];
    string fullNameOfOtherFieldInJson = "fullName.OfOtherField.InJson";
    using (FileStream fileStream = File.OpenRead(outputJsonPath))
    {
        field.ImportValueFromJson(fileStream, fullNameOfOtherFieldInJson);
    }
    document.Save(outputPdfPath);
}
```

## Error handling 

This example demonstrates how to export form fields from a PDF to a JSON file using Aspose.PDF, including handling different statuses for each field during the export process.

Let's break down this Aspose.PDF example step by step:

1. Loading the Document. We load a PDF document named "Sample.pdf" from a specified directory.
1. Setting Export Options. Here, we create an instance of ExportFieldsToJsonOptions with two settings:
    * `ExportPasswordValue` : This includes password fields in the export.
    * `WriteIndented` : This formats the JSON output to be indented for readability
1. Export form fields to JSON. We export the form fields from the PDF file to a JSON file called "export.json" using the specified parameters.
1. Processing Export Results:
    This loop iterates through the export results and prints the status of each field:

    * Success: Indicates the field was successfully exported.
    * Warning: Prints any warning messages related to the field.
    * Error: Prints any error messages related to the field.


```cs
var document = new Document(Path.Combine(dataDir, "Forms", "Sample.pdf"));

var options
    = new ExportFieldsToJsonOptions
    {
        ExportPasswordValue = true,
        WriteIndented = true,
    };

var exportResults = document.Form.ExportToJson(File.OpenWrite("export.json"), options);

foreach (var result in exportResults)
{
    Console.Write($"{result.FieldFullName} ");
    switch (result.FieldSerializationStatus)
    {
        case FieldSerializationStatus.Success:
            Console.WriteLine("Success");
            break;
        case FieldSerializationStatus.Warning:
            foreach (var messages in result.WarningMessages)
            {
                Console.WriteLine(messages);
            }
            break;
        case FieldSerializationStatus.Error:
            foreach (var messages in result.ErrorMessages)
            {
                Console.WriteLine(messages);
            }
            break;
    }
}
```                

