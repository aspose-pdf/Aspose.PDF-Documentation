---
title: Form Exporter
type: docs
weight: 50
url: /net/plugins/formexpoter/
description: How to Export Form Field Values to CSV Files using Aspose.PDF Form Exporter Plugin
lastmod: "2024-01-24"
draft: false
---

In this article, we will show you how to use the [Form Exporter plugin](https://products.aspose.org/pdf/net/form-exporter/), which can export form field values from PDF files to CSV files.

## Prerequisites

You will need the following:

* Visual Studio 2019 or later
* Aspose.PDF for .NET 21.1 or later
* A sample PDF file that contains some form fields

You can download the Aspose.PDF for .NET library from the official website or install them using the NuGet Package Manager in Visual Studio.

## Steps

The basic steps to export form field values to CSV files using the FormExporter plugin are:

1. Create an object of the `FormExporter` class
1. Create an object of the `FormExporterValuesToCsvOptions` class and specify the predicate and the delimiter
1. Add the input and output data sources to the options object
1. Run the `Process` method of the `FormExporter` object

Let's see how to implement these steps in C# code.

### Step 1: Create an object of the FormExporter class

The FormExporter class is the main class that provides the functionality of exporting form field values to CSV files. To use it, you need to create an instance of it using the default constructor:

```cs
// Create an instance of the FormExporter plugin
var plugin = new FormExporter();
```

### Step 2: Create an object of the FormExporterValuesToCsvOptions class and specify the predicate and the delimiter

The FormExporterValuesToCsvOptions class is a helper class that allows you to specify various options and parameters for the export process, such as the predicate and the delimiter. The predicate is a function that selects the form fields that you want to export based on some criteria, such as the field type, the page index, the field name, etc. The delimiter is a character that separates the values in the CSV file. To use this class, you need to create an instance of it and pass the predicate and the delimiter as parameters. For example, to export only the textbox fields on the second page of the PDF file, and use a semicolon as the delimiter, you can use the following code:

```cs
// Create options for exporting form field values to CSV
var options = new FormExporterValuesToCsvOptions(
(field) => { return field is TextBoxField && field.PageIndex == 2; }, ';');
```

### Step 3: Add the input and output data sources to the options object

The input and output data sources are the PDF files that you want to export from and the CSV file that you want to save. They can be either file paths or streams. To add them to the options object, you need to use the AddInput and AddOutput methods of the options class. For example, to export from four PDF files named `inputFileNameWithFields-1.pdf`, `inputFileNameWithFields-2.pdf`, `inputFileNameWithFields-3.pdf`, and `inputFileNameWithFields-4`.pdf in the current folder, and save to a CSV file named outputFileName.csv in the same folder, you can use the following code:

```cs
// Add input and output files to the options
options.AddInput(new FileDataSource("inputFileNameWithFields-1.pdf"));
options.AddInput(new FileDataSource("inputFileNameWithFields-2.pdf"));
options.AddInput(new FileDataSource("inputFileNameWithFields-3.pdf"));
options.AddInput(new FileDataSource("inputFileNameWithFields-4.pdf"));
options.AddOutput(new FileDataSource("outputFileName.csv"));

```

### Step 4: Run the Process method of the FormExporter object

The final step is to run the Process method of the FormExporter object, passing the options object as a parameter. This method will perform the export process and return a ResultContainer object, which contains the results of the process, such as the status, the messages, the output data sources, etc. You can access the results using the properties and methods of the ResultContainer class. For example, to get the first result from the result collection and print it to the console, you can use the following code:

```cs
// Process the form field values using the plugin
var resultContainer = plugin.Process(options);
var result = resultContainer.ResultCollection[0];
Console.WriteLine(result);

```

The result will contain information such as the input and output file paths.