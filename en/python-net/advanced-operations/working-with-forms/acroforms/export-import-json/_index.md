---
title: Import and Export Form Data 
type: docs
weight: 80
url: /python-net/import-export-json/
description: This section explains how to import and Export Form Data.
lastmod: "2025-08-05"
TechArticle: true
AlternativeHeadline: 
Abstract: 
---

## Import Form Data from an XML file

Next example demonstrates how to import form data from an XML file into an existing PDF form using Aspose.PDF for Python. By binding a PDF form, loading XML data, and saving the updated file, you can quickly populate interactive form fields without manually editing each page. This method is ideal for automating bulk form filling, processing large datasets, and ensuring data consistency across multiple documents.

Use the following steps:

1. Create Form Object.
1. Bind the PDF Form.
1. Load XML Data.
1. Import XML into PDF.
1. Save Updated PDF.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    # Construct full file paths using the working directory
    path_infile = path.join(self.workdir_path, infile)
    path_datafile = path.join(self.workdir_path, datafile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create a Form object from Aspose.PDF
    form = ap.facades.Form()
    
    # Bind the input PDF form
    form.bind_pdf(path_infile)

    # Import XML data into the form
    with FileIO(path_datafile, "r") as f:
        form.import_xml(f)

    # Save the form with imported data to a new PDF file
    form.save(path_outfile)
```

## Export Form field Data from a PDF document to an XML file

Python library shows how to export form field data from a PDF document to an XML file using Aspose.PDF for Python. By binding a PDF form and saving its field values in XML format, you can easily store, process, or reuse the form data in other applications or workflows. This approach is ideal for data backup, analysis, and integration with external systems.

Use the following steps:

1. Create Form Object
1. Bind the PDF Form
1. Export Form Data
1. Save Field Values to XML

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap
    
    # Combine the working directory path with the input PDF file name
    path_infile = path.join(self.workdir_path, infile)

    # Combine the working directory path with the output XML file name
    path_outfile = path.join(self.workdir_path, datafile)

    # Create a Form object to work with PDF form fields
    form = ap.facades.Form()

    # Bind the PDF document containing the form
    form.bind_pdf(path_infile)

    # Open the XML file in write mode to store exported form data
    with FileIO(path_outfile, "w") as f:
        # Export form field data from the PDF to the XML file
        form.export_xml(f)
```

## Import Form field Data from an FDF

The 'import_data_from_fdf' method imports form field data from an FDF (Forms Data Format) file into an existing PDF form and saves the updated document. This approach is useful for pre-filling or updating PDF forms programmatically without modifying the structure of the document.

Use the following steps:

1. Create Form Object.
1. Bind the input PDF.
1. Import the form data with import_fdf().
1. Save the PDF with the imported data to the specified output file path.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_datafile = path.join(self.workdir_path, datafile)
    path_outfile = path.join(self.workdir_path, outfile)

    form = ap.facades.Form()
    form.bind_pdf(path_infile)

    with FileIO(path_datafile, "r") as f:
        form.import_fdf(f)
        form.save(path_outfile)
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
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(Path.Combine(dataDir, "Forms", "Sample.pdf")))
    {
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
                case Aspose.Pdf.FieldSerializationStatus.Success:
                    Console.WriteLine("Success");
                    break;
                case Aspose.Pdf.FieldSerializationStatus.Warning:
                    foreach (var messages in result.WarningMessages)
                    {
                        Console.WriteLine(messages);
                    }
                    break;
                case Aspose.Pdf.FieldSerializationStatus.Error:
                    foreach (var messages in result.ErrorMessages)
                    {
                        Console.WriteLine(messages);
                    }
                    break;
            }
        }
    }
}
```                

