---
title: XLS Converter
type: docs
weight: 20
url: /net/plugins/xls/
description: How to Convert PDF to Excel spreadsheets using Aspose.Pdf plugins
lastmod: "2024-01-24"
---

{{% alert color="primary" %}}

In this article, we will show you how to use the PdfXls plugin, which can convert PDF files to Excel format with high fidelity and accuracy.

{{% /alert %}}

## Prerequisites

You will need the following:

* Visual Studio 2019 or later
* Aspose.PDF for .NET 24.1 or later
* A sample PDF file that you want to convert to Excel format

You can download the Aspose.PDF for .NET library from the official website or install them using the NuGet Package Manager in Visual Studio.

## Steps

The basic steps to convert a PDF file to Excel format using the PdfXls plugin are:

1. Create an object of the PdfXls class
1. Add the input and output data sources to the PdfToXlsOptions object
1. Run the Process method of the PdfXls object

Let's see how to implement these steps in C# code.

### Step 1: Create an object of the PdfXls class

The PdfXls class is the main class that provides the functionality of converting PDF to Excel. To use it, you need to create an instance of it using the default constructor:

```csharp
// Create an instance of the PdfXls plugin
var plugin = new PdfXls();
```

### Step 2: Add the input and output data sources to the PdfToXlsOptions object

The PdfToXlsOptions class is a helper class that allows you to specify various options and parameters for the conversion process.  To use it, you need to create an instance of it and add the input and output data sources using the `AddInput` and `AddOutput` methods. The data sources can be either file paths or streams. For example, to convert a PDF file named `sample.pdf` in the `C:\Samples` folder to an Excel file named `sample.xlsx` in the same folder, you can use the following code:

```csharp
// Specify the input and output file paths
var inputPath = Path.Combine(@"C:\Samples\", "sample.pdf");
var outputPath = Path.Combine(@"C:\Samples\", "sample.xlsx");

// Create an instance of the PdfToXlsOptions class
var options = new PdfToXlsOptions();

// Add the input and output file paths to the options
options.AddInput(new FileDataSource(inputPath));
options.AddOutput(new FileDataSource(outputPath));
```

You can also set other options, such as the output format, the page range, the worksheet name, etc. using the properties of the PdfToXlsOptions class. For example, to convert the PDF file to the XLSX format, insert a blank column at the first position, and name the worksheet as "MySheet", you can use the following code:

```csharp
// Set the output format to XLSX
options.Format = PdfToXlsOptions.ExcelFormat.XLSX;

// Insert a blank column at the first position
options.InsertBlankColumnAtFirst = true;
```

### Step 3: Run the Process method of the PdfXls object

The final step is to run the Process method of the PdfXls object, passing the PdfToXlsOptions object as a parameter. This method will perform the conversion and return a ResultContainer object, which contains the results of the conversion, such as the status, the messages, the output data sources, etc. You can access the results using the properties and methods of the ResultContainer class. For example, to get the first result from the result collection and print it to the console, you can use the following code:

```csharp
// Process the PDF to Excel conversion using the plugin and options
var resultContainer = plugin.Process(options);

// Get the first result from the result collection
var result = resultContainer.ResultCollection[0];

// Print the result
Console.WriteLine(result);
```

The result will contain information such as the output file paths.
