---
title: Import and Export Data in JSON
type: docs
weight: 80
url: /net/import-export-json/
description: This section explains how to import and Export Data in JSON
lastmod: "2024-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import and Export Data in JSON",
    "alternativeHeadline": "Enhance PDF Form Management with JSON Import/Export",
    "abstract": "The new feature enables seamless import and export of PDF form data using JSON format, providing a straightforward way to manipulate form fields across documents. Users can utilize various methods, including FileStream and MemoryStream, to manage data efficiently, ensuring flexibility whether working with full documents or specific fields. This functionality enhances data processing workflows, making PDF form management simpler and more effective",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Import Data, Export Data, JSON format, Form fields, Aspose.PDF library, FieldSerializationResult, ExportFieldsToJsonOptions, FileStream, MemoryStream, Specific field export/import",
    "wordcount": "1255",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/import-export-json/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-export-json/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Import and Export Data from Forms in JSON

Manipulating form fields within PDF documents can be crucial when handling data input and output operations in various applications. The Aspose.PDF library offers robust functionality for exporting and importing form fields in JSON format. Below, we explore several code snippets demonstrating how to perform these tasks using different approaches.

Since 24.7 it's possible to add Import and Export Data from Forms in JSON Format:

### Export form fields to and from the JSON file

This approach exports all the form fields from an existing PDF document into a JSON file and imports them into a new PDF document.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void ExportAllFieldsToJson(string inputPdfPath, string outputJsonPath, string outputPdfPath)
{
    // Create ExportFieldsToJsonOptions with indentation
    var options = new Aspose.Pdf.ExportFieldsToJsonOptions { WriteIndented = true };

    // Load the document
    using (var document = new Aspose.Pdf.Document(inputPdfPath))
    {
        // Export fields to JSON
        var exportResult = document.Form.ExportToJson(outputJsonPath, options);

        // Optionally, save the document with fields to a new PDF
        document.Save(outputPdfPath);
    }
}
```

### Import form fields from the JSON file and insert their to created Pdf document

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void ImportFieldsFromJsonAndInsertToPdf(string inputPdfPath, string outputJsonPath, string outputPdfPath)
{
    // Load the document
    using (var document = new Aspose.Pdf.Document(inputPdfPath))
    {
        // Create a new document to import fields into
        var newDocument = new Aspose.Pdf.Document();

        // Add a new page to the new document
        var page = newDocument.Pages.Add();

        // Import fields from JSON
        var importResult = newDocument.Form.ImportFromJson(outputJsonPath);

        // Save the new document with imported fields
        newDocument.Save(outputPdfPath);
    }
}
```

### Export form fields to and from the JSON file using FileStream

This snippet export fields to Json file utilizes 'FileStream' to manage the file input and output.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void ExportFieldsToJson(string inputPdfPath, string outputJsonPath, string outputPdfPath)
{
    // Create ExportFieldsToJsonOptions with indentation
    var options = new Aspose.Pdf.ExportFieldsToJsonOptions { WriteIndented = true };

    // Load the document
    using (var document = new Aspose.Pdf.Document(inputPdfPath))
    {
        // Create a FileStream to write the JSON output
        using (var fileStream = File.Create(outputJsonPath))
        {
            // Export fields to JSON using the FileStream
            var exportResult = document.Form.ExportToJson(fileStream, options);
        }
    }
}
```

### Import form fields from the JSON file using FileStream and insert theres to created Pdf document

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void ImportFieldsFromJsonToCreatedPdt(string inputPdfPath, string outputJsonPath, string outputPdfPath)
{
    // Load the document
    using (var document = new Aspose.Pdf.Document(inputPdfPath))
    {
        // Create a new document to import fields into
        var newDocument = new Aspose.Pdf.Document();

        // Add a new page to the new document
        var page = newDocument.Pages.Add();

        // Open the JSON file for reading
        using (var fileStream = File.OpenRead(outputJsonPath))
        {
            // Import fields from JSON using the FileStream
            var importResult = newDocument.Form.ImportFromJson(fileStream);
        }

        // Save the new document with imported fields
        newDocument.Save(outputPdfPath);
    }
}
```

### Export form fields in JSON format using MemoryStream

In some scenarios, you might prefer to work with data in memory rather than with files on disk. This approach uses 'MemoryStream' to handle the export and import processes entirely in memory.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void ExportFieldsToJsonUsingMemoryStream(string inputPdfPath, string outputPdfPath)
{
    // Create a MemoryStream to hold the JSON data
    using (var memoryStream = new MemoryStream())
    {
        // Load the document
        using (var document = new Aspose.Pdf.Document(inputPdfPath))
        {
            // Export fields to JSON and write to the MemoryStream
            var exportResult = document.Form.ExportToJson(memoryStream);
        }

        // Optionally, you can save the MemoryStream content to a file
        File.WriteAllBytes(outputPdfPath, memoryStream.ToArray());
    }
}
```

### Import form fields in JSON format using MemoryStream

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void ImportFieldsFromJsonUsingMemoryStream(string inputPdfPath, string outputPdfPath)
{
    // Load the document
    using (var document = new Aspose.Pdf.Document(inputPdfPath))
    {
        // Create a new document to import fields into
        var newDocument = new Aspose.Pdf.Document();

        // Add a new page to the new document
        var page = newDocument.Pages.Add();

        // Create a MemoryStream to hold the JSON data
        using (var memoryStream = new MemoryStream())
        {
            // Export fields from the original document to the MemoryStream
            document.Form.ExportToJson(memoryStream);

            // Reset the MemoryStream position to the beginning
            memoryStream.Position = 0;

            // Import fields from the MemoryStream into the new document
            var importResult = newDocument.Form.ImportFromJson(memoryStream);
        }

        // Save the new document with imported fields
        newDocument.Save(outputPdfPath);
    }
}
```

### Export the specified field to and from the JSON file

Sometimes, you may need to export or import only a specific field rather than all the fields in the document.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void ExportFieldToJson(string inputPdfPath, string outputJsonPath, string outputPdfPath)
{
    // Create ExportFieldsToJsonOptions with indentation
    var options = new Aspose.Pdf.ExportFieldsToJsonOptions { WriteIndented = true };

    // Load the document
    using (var document = new Aspose.Pdf.Document(inputPdfPath))
    {
        // Get the specific field (WidgetAnnotation) from the form
        if (document.Form[1] is Aspose.Pdf.Annotations.WidgetAnnotation field)
        {
            // Export the field to JSON
            var exportResult = field.ExportToJson(outputJsonPath, options);
        }
    }
}
```

### Import the specified field to and from the JSON file

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void ImportFieldFromJson(string inputPdfPath, string outputJsonPath, string outputPdfPath)
{
    // Load the document
    using (var document = new Aspose.Pdf.Document(inputPdfPath))
    {
        // Create a new document to import fields into
        var newDocument = new Aspose.Pdf.Document();

        // Add a new page to the new document
        var page = newDocument.Pages.Add();

        // Import fields from JSON
        var importResult = newDocument.Form.ImportFromJson(outputJsonPath);

        // Save the new document with imported fields
        newDocument.Save(outputPdfPath);
    }
}
```

### Export the specified field to and from the JSON file using FileStream

This example is similar to the one above but uses 'FileStream' to handle the export and import operations for a specific field.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void ExportFieldToJson(string inputPdfPath, string outputJsonPath, string outputPdfPath)
{
    // Create ExportFieldsToJsonOptions with indentation
    var options = new Aspose.Pdf.ExportFieldsToJsonOptions { WriteIndented = true };

    // Load the document
    using (var document = new Aspose.Pdf.Document(inputPdfPath))
    {
        // Get the specific field (WidgetAnnotation) from the form
        if (document.Form[1] is Aspose.Pdf.Annotations.WidgetAnnotation field)
        {
            // Create a FileStream to write the JSON output
            using (var fileStream = File.Create(outputJsonPath))
            {
                // Export the field to JSON using the FileStream
                var exportResult = field.ExportToJson(fileStream, options);
            }
        }
    }
}
```

### Import the specified field to and from the JSON file using FileStream

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void ImportFieldFromJson(string inputPdfPath, string outputJsonPath, string outputPdfPath)
{
    // Create a new document to import fields into
    using (var newDocument = new Aspose.Pdf.Document())
    {
        // Add a new page to the new document
        var page = newDocument.Pages.Add();

        // Open the JSON file for reading
        using (var fileStream = File.OpenRead(outputJsonPath))
        {
            // Import fields from JSON using the FileStream
            var importResult = newDocument.Form.ImportFromJson(fileStream);
        }

        // Save the new document with imported fields
        newDocument.Save(outputPdfPath);
    }
}
```

### Export the specified field in JSON format using MemoryStream

This code snippet demonstrates how to export a specific form field from a PDF document into JSON format using a 'MemoryStream' and then import it into a new PDF document. 

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void ExportFieldToJsonUsingMemoryStream(string inputPdfPath, string outputPdfPath)
{
    // Create a MemoryStream to hold the JSON data
    using (var memoryStream = new MemoryStream())
    {
        // Load the document
        using (var document = new Aspose.Pdf.Document(inputPdfPath))
        {
            // Get the specific field (WidgetAnnotation) from the form
            if (document.Form[1] is Aspose.Pdf.Annotations.WidgetAnnotation field)
            {
                // Export the field to JSON and write to the MemoryStream
                var exportResult = field.ExportToJson(memoryStream);
            }
        }

        // Optionally, you can save the MemoryStream content to a file
        File.WriteAllBytes(outputPdfPath, memoryStream.ToArray());
    }
}
```

### Import the specified field in JSON format using MemoryStream

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void ImportFieldFromJsonUsingMemoryStream(string inputPdfPath, string outputPdfPath)
{
    // Load the document
    using (var document = new Aspose.Pdf.Document(inputPdfPath))
    {
        // Create a new document to import fields into
        var newDocument = new Aspose.Pdf.Document();

        // Add a new page to the new document
        var page = newDocument.Pages.Add();

        // Create a MemoryStream to hold the JSON data
        using (var memoryStream = new MemoryStream())
        {
            // Export fields from the original document to the MemoryStream
            document.Form.ExportToJson(memoryStream);

            // Reset the MemoryStream position to the beginning
            memoryStream.Position = 0;

            // Import fields from the MemoryStream into the new document
            var importResult = newDocument.Form.ImportFromJson(memoryStream);
        }

        // Save the new document with imported fields
        newDocument.Save(outputPdfPath);
    }
}
```

### Export value from the specified field to the JSON file using FileStream

This code snippet shows how to export the value of a specific form field from a PDF document into a JSON file using FileStream.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void ExportFieldValueToJson(string inputPdfPath, string outputJsonPath, string outputPdfPath)
{
    // Load the document
    using (var document = new Aspose.Pdf.Document(inputPdfPath))
    {
        // Get the specific field from the form
        if (document.Form.Fields[1] is Aspose.Pdf.Forms.Field field)
        {
            // Create a FileStream to write the JSON output
            using (var fileStream = File.Create(outputJsonPath))
            {
                // Export the field value to JSON using the FileStream
                field.ExportValueToJson(fileStream);
            }
        }
    }
}
```

### Import value to the specified field from the JSON file using FileStream

This code snippet demonstrates how to import a value from a JSON file into a specific form field in a PDF document using FileStream.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void ImportFieldValueFromJson(string inputPdfPath, string outputJsonPath, string outputPdfPath)
{
    // Load the document
    using (var document = new Aspose.Pdf.Document(inputPdfPath))
    {
        // Get the specific field from the form
        if (document.Form.Fields[1] is Aspose.Pdf.Forms.Field field)
        {
            // Open the JSON file for reading
            using (var fileStream = File.OpenRead(outputJsonPath))
            {
                // Import the field value from JSON using the FileStream
                field.ImportValueFromJson(fileStream);
            }
        }

        // Save the document with the updated field value
        document.Save(outputPdfPath);
    }
}
```

### Import value of another field to the specified field from the JSON file using FileStream

This code snippet demonstrates how to import a value of another field to the specified field from the JSON file using FileStream and Aspose.PDF.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void ImportFieldValueFromJson(string inputPdfPath, string outputJsonPath, string outputPdfPath, string fullNameOfOtherFieldInJson)
{
    // Load the document
    using (var document = new Aspose.Pdf.Document(inputPdfPath))
    {
        // Get the specific field from the form
        if (document.Form.Fields[1] is Aspose.Pdf.Forms.Field field)
        {
            // Open the JSON file for reading
            using (var fileStream = File.OpenRead(outputJsonPath))
            {
                // Import the field value from JSON using the FileStream and the full name of the other field in JSON
                field.ImportValueFromJson(fileStream, fullNameOfOtherFieldInJson);
            }
        }

        // Save the document with the updated field value
        document.Save(outputPdfPath);
    }
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
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void ExportFieldsToJsonWithOptions()
{
    // Explicit dataDir initialization
    string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Load the document
    var document = new Aspose.Pdf.Document(Path.Combine(dataDir, "Forms", "Sample.pdf"));

    // Create ExportFieldsToJsonOptions with specific settings
    var options = new Aspose.Pdf.ExportFieldsToJsonOptions
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
}
```                

