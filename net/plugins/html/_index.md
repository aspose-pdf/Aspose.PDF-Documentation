---
title: Using Aspose.PDF HTML plugin (.NET version)
type: docs
weight: 60
url: /net/plugins/html/
description: How to Convert PDF Files to and from HTML Files using Aspose.PDF PdfHtml Plugin
lastmod: "2024-01-24"
draft: false
---


Aspose.PDF is a powerful and versatile library that allows you to work with PDF documents in various ways. One of the features of Aspose.PDF is the ability to use plugins that extend its functionality and provide more capabilities. In this article, we will show you how to use the PdfHtml plugin, which can convert PDF files to and from HTML files.

## Prerequisites

To follow this tutorial, you will need the following:

* Visual Studio 2019 or later
* Aspose.PDF for .NET 21.1 or later
* A sample PDF file and a sample HTML file

You can download the Aspose.PDF and Aspose.PDF.Plugins libraries from the official website or install them using the NuGet Package Manager in Visual Studio.

## Steps

The basic steps to convert PDF files to and from HTML files using the PdfHtml plugin are:

1. Create an object of the PdfHtml class
2. Create an object of the PdfToHtmlOptions or HtmlToPdfOptions class, depending on the direction of the conversion
3. Add the input and output data sources to the options object
4. Run the Process method of the PdfHtml object

Let's see how to implement these steps in C# code for each direction of the conversion.

### Step 1: Create an object of the PdfHtml class

The PdfHtml class is the main class that provides the functionality of converting PDF files to and from HTML files. To use it, you need to create an instance of it using the default constructor:

```cs
// Create an instance of the PdfHtml plugin
var plugin = new PdfHtml();
```

### Step 2: Create an object of the PdfToHtmlOptions or HtmlToPdfOptions class, depending on the direction of the conversion

The PdfToHtmlOptions and HtmlToPdfOptions classes are helper classes that allow you to specify various options and parameters for the conversion process, such as the output format, the page range, the encoding, the fonts, etc. To use these classes, you need to create an instance of the appropriate class using the default constructor or passing some parameters. For example, to convert a PDF file to an HTML file with embedded resources, you can use the following code:

```cs
// Create a new instance of the PdfToHtmlOptions class
var options = new PdfToHtmlOptions(PdfToHtmlOptions.SaveDataType.FileWithEmbeddedResources);
```

To convert an HTML file to a PDF file with default settings, you can use the following code:

```cs
// Create a new instance of the HtmlToPdfOptions class
var options = new HtmlToPdfOptions();
```
You can also set other options, such as the output format, the page range, the encoding, the fonts, etc. using the properties of the options classes. For example, to convert a PDF file to an HTML file with UTF-8 encoding and Arial font, you can use the following code:

```cs
// Create a new instance of the PdfToHtmlOptions class
var options = new PdfToHtmlOptions(PdfToHtmlOptions.SaveDataType.FileWithEmbeddedResources);

// Set the encoding to UTF-8
options.Encoding = Encoding.UTF8;

// Set the font to Arial
options.Font = "Arial";
```

### Step 3: Add the input and output data sources to the options object

The input and output data sources are the PDF or HTML files that you want to convert and save. They can be either file paths or streams. To add them to the options object, you need to use the AddInput and AddOutput methods of the options class. For example, to convert a PDF file named sample.pdf in the C:\Samples folder to an HTML file named sample.html in the same folder, you can use the following code:

```cs
// Specify the input and output file paths
var inputPath = Path.Combine(@"C:\Samples\", "sample.pdf");
var outputPath = Path.Combine(@"C:\Samples\", "sample.html");

// Add the input and output file paths to the options
options.AddInput(new FileDataSource(inputPath));
options.AddOutput(new FileDataSource(outputPath));
```

### Step 4: Run the Process method of the PdfHtml object

The final step is to run the Process method of the PdfHtml object, passing the options object as a parameter. This method will perform the conversion and return a ResultContainer object, which contains the results of the conversion, such as the status, the messages, the output data sources, etc. You can access the results using the properties and methods of the ResultContainer class. For example, to get the first result from the result collection and print it to the console, you can use the following code:

```cs
// Process the conversion and get the result container
var resultContainer = plugin.Process(options);

// Get the first result from the result collection
var result = resultContainer.ResultCollection[0];

// Print the result to the console
Console.WriteLine(result);
```

The result will contain information such as the input and output file paths, the status, the message, the exception, etc. For example, if the conversion is successful, the result might look like this:

Input: C:\Samples\sample.pdf
Output: C:\Samples\sample.html
Status: Success
Message: Conversion completed successfully
Exception: null

If the conversion fails, the result might look like this:

Input: C:\Samples\sample.pdf
Output: C:\Samples\sample.html
Status: Failure
Message: An error occurred while converting the file
Exception: System.IO.FileNotFoundException: Could not find file 'C:\Samples\sample.pdf'
