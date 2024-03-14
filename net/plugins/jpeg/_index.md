---
title: JPEG Converter
type: docs
weight: 90
url: /net/plugins/jpeg/
description: How to Convert PDF Pages to JPEG Images using Aspose.PDF JPEG Converter
lastmod: "2024-01-24"
draft: false
---

In this article, we will show you how to use the JPEG Converter, which can convert PDF pages to JPEG images and save them as separate files.

## Prerequisites

You will need the following:

* Visual Studio 2019 or later
* Aspose.PDF for .NET 24.1 or later
* A sample PDF file that contains some pages

You can download the Aspose.PDF for .NET library from the official website or install them using the NuGet Package Manager in Visual Studio.

## Steps

The basic steps to convert PDF pages to JPEG images using the JPEG Converter are:

1. Create an object of the Jpeg class
1. Create an object of the JpegOptions class and add the input and output file paths
1. Run the Process method of the Jpeg object and get the result container
1. Print the paths of the converted JPEG images

Let's see how to implement these steps in C# code.

### Step 1: Create an object of the Jpeg class

The Jpeg class is the main class that provides the functionality of converting PDF pages to JPEG images. To use it, you need to create an instance of it using the default constructor:

```cs
// Create a new instance of Jpeg
var converter = new Jpeg();
```

### Step 2: Create an object of the JpegOptions class and add the input and output file paths

The JpegOptions class is a helper class that allows you to specify various options and parameters for the conversion process, such as the output resolution, the page range, the image quality, etc. To use this class, you need to create an instance of it using the default constructor and add the input and output file paths using the AddInput and AddOutput methods. The input and output file paths can be either strings or FileDataSource objects. For example, to convert a PDF file named sample.pdf in the C:\Samples folder to JPEG images in the same folder, you can use the following code:

```cs
// Specify the input and output file paths
var inputPath = Path.Combine(@"C:\Samples\", "sample.pdf");
var outputPath = Path.Combine(@"C:\Samples\", "images");

// Create an instance of the JpegOptions class
var converterOptions = new JpegOptions();

// Add the input and output file paths to the options
converterOptions.AddInput(new FileDataSource(inputPath));
converterOptions.AddOutput(new FileDataSource(outputPath));
```

You can also set other options, such as the output resolution, the page range, the image quality, etc. using the properties of the JpegOptions class. For example, to convert only the first page of the PDF file to a JPEG image with 300 dpi resolution, you can use the following code:

```cs
// Set the output resolution to 300 dpi
converterOptions.OutputResolution = 300;

// Set the page range to the first page
converterOptions.PageRange = new PageRange(1);
```

### Step 3: Run the Process method of the Jpeg object and get the result container

The final step is to run the Process method of the Jpeg object, passing the converterOptions object as a parameter. This method will perform the conversion and return a ResultContainer object, which contains the results of the conversion, such as the status, the messages, the output file paths, etc. You can access the results using the properties and methods of the ResultContainer class. For example, to get the result container and print the status of the conversion, you can use the following code:

```cs
// Process the conversion and get the result container
ResultContainer resultContainer = converter.Process(converterOptions);

// Print the status of the conversion
Console.WriteLine(resultContainer.Status);
```

The status of the conversion can be either Success or Failure, depending on whether the conversion was completed successfully or not.

### Step 4: Print the paths of the converted JPEG images

The result container contains a collection of results, one for each output file path. Each result contains information such as the input and output file paths, the status, the message, the exception, etc. You can access the results using the ResultCollection property and the indexer of the result container. For example, to print the paths of the converted JPEG images, you can use the following code:

```cs
// Print the paths of the converted JPEG images
foreach (FileResult operationResult in resultContainer.ResultCollection.Cast<FileResult>())
{
  Console.WriteLine(operationResult.Data.ToString());
}
```

The output file paths will have the format of {outputPath}{pageNumber}.jpg, where {outputPath} is the output directory and {pageNumber} is the page number of the PDF file. For example, if the output directory is C:\Samples\images and the PDF file has three pages, the output file paths will be:

```text
C:\Samples\images\1.jpg
C:\Samples\images\2.jpg
C:\Samples\images\3.jpg
```
