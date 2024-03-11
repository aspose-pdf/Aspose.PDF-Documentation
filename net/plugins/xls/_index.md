---
title: Using Aspose.PDF Excel plugin (.NET version)
type: docs
weight: 150
url: /net/plugins/excel/
description: How to Convert PDF to Excel using Aspose.Pdf Plugins
lastmod: "2024-01-24"
draft: false
---

{{% alert color="primary" %}}

Aspose.PDF is a powerful and versatile library that allows you to work with PDF documents in various ways. One of the features of Aspose.PDF is the ability to use plugins that extend its functionality and provide more capabilities. In this article, we will show you how to use the PdfExcel plugin, which can convert PDF files to Excel format with high fidelity and accuracy.

{{% /alert %}}

## Prerequisites

To follow this tutorial, you will need the following:

* Visual Studio 2019 or later
* Aspose.PDF for .NET 24.1 or later
* A sample PDF file that you want to convert to Excel format

You can download the Aspose.Pdf and Aspose.Pdf.Plugins libraries from the official website or install them using the NuGet Package Manager in Visual Studio.

## Steps

The basic steps to convert a PDF file to Excel format using the PdfExcel plugin are:

1. Create an object of the PdfExcel class
1. Add the input and output data sources to the PdfToExcelOptions object
1. Run the Process method of the PdfExcel object

Let's see how to implement these steps in C# code.

### Step 1: Create an object of the PdfExcel class

The PdfExcel class is the main class that provides the functionality of converting PDF to Excel. To use it, you need to create an instance of it using the default constructor:

```csharp
// Create an instance of the PdfExcel plugin
var plugin = new PdfExcel();
```

### Step 2: Add the input and output data sources to the PdfToExcelOptions object

The PdfToExcelOptions class is a helper class that allows you to specify various options and parameters for the conversion process.  To use it, you need to create an instance of it and add the input and output data sources using the `AddInput` and `AddOutput` methods. The data sources can be either file paths or streams. For example, to convert a PDF file named `sample.pdf` in the `C:\Samples` folder to an Excel file named `sample.xlsx` in the same folder, you can use the following code:

```csharp
// Specify the input and output file paths
var inputPath = Path.Combine(@"C:\Samples\", "sample.pdf");
var outputPath = Path.Combine(@"C:\Samples\", "sample.xlsx");

// Create an instance of the PdfToExcelOptions class
var options = new PdfToExcelOptions();

// Add the input and output file paths to the options
options.AddInput(new FileDataSource(inputPath));
options.AddOutput(new FileDataSource(outputPath));
```

You can also set other options, such as the output format, the page range, the worksheet name, etc. using the properties of the PdfToExcelOptions class. For example, to convert the PDF file to the XLSX format, insert a blank column at the first position, and name the worksheet as "MySheet", you can use the following code:

```csharp
// Set the output format to XLSX
options.Format = PdfToExcelOptions.ExcelFormat.XLSX;

// Insert a blank column at the first position
options.InsertBlankColumnAtFirst = true;
```

### Step 3: Run the Process method of the PdfExcel object

The final step is to run the Process method of the PdfExcel object, passing the PdfToExcelOptions object as a parameter. This method will perform the conversion and return a ResultContainer object, which contains the results of the conversion, such as the status, the messages, the output data sources, etc. You can access the results using the properties and methods of the ResultContainer class. For example, to get the first result from the result collection and print it to the console, you can use the following code:

```csharp
// Process the PDF to Excel conversion using the plugin and options
var resultContainer = plugin.Process(options);

// Get the first result from the result collection
var result = resultContainer.ResultCollection[0];

// Print the result
Console.WriteLine(result);
```

The result will contain information such as the input and output file paths, the status, the message, the exception, etc. For example, if the conversion is successful, the result might look like this:

```text
Input: C:\Samples\sample.pdf
Output: C:\Samples\sample.xlsx
Status: Success
Message: Conversion completed successfully
Exception: null
```

If the conversion fails, the result might look like this:

```text
Input: C:\Samples\sample.pdf
Output: C:\Samples\sample.xlsx
Status: Failure
Message: An error occurred while converting the PDF file
Exception: System.IO.FileNotFoundException: Could not find file 'C:\Samples\sample.pdf'
```
