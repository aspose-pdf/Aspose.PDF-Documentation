---
title: PNG converter
type: docs
weight: 110
url: /net/plugins/png/
description: Convert PDF to PNG Images with Aspose.PDF PNG Plugin
lastmod: "2024-01-24"
---

If you're looking to [convert PDF documents into PNG images](https://products.aspose.org/pdf/net/png-converter/) using .NET, Aspose.PDF for .NET provides a robust solution. In this article, we'll walk through the essential steps to create an object, add a data source, and run the process method using the Aspose.PDF library.

## Prerequisites

You will need the following:

* Visual Studio 2019 or later
* Aspose.PDF for .NET 24.1 or later
* A sample PDF file

## Code Walkthrough

The code below demonstrates a PNG conversion demo using the Aspose.PDF PNG Plugin:

```csharp
using Aspose.Pdf.Plugins;

//....

// Create a new instance of the PngOptions class.
var convertorOptions = new PngOptions();

// Add the input and output paths to the PngOptions.
convertorOptions.AddInput(new FileDataSource(Path.Combine(@"C:\Samples\", "sample.pdf")));
convertorOptions.AddOutput(new FileDataSource(Path.Combine(@"C:\Samples\", "images")));

// Set the output resolution to 300 DPI.
convertorOptions.OutputResolution = 300;

// Create a new instance of the Png class.
Png converter = new ();

// Process the PNG conversion and get the result container.
ResultContainer resultContainer = converter.Process(convertorOptions);

// Print the result to the console.
foreach (FileResult operationResult in resultContainer.ResultCollection.Cast<FileResult>())
{
      Console.WriteLine(operationResult.Data.ToString());
}
```

Let's break down the key steps:

1. **Create an Object (PngOptions and Png)**

   The code starts by creating an instance of the `PngOptions` class to configure the PNG conversion. Additionally, an instance of the `Png` class is created for further processing.

2. **Add Data Source**

   The input PDF file path is added to the `PngOptions` using the `AddInput` method. Similarly, the output path for the PNG images is added using the `AddOutput` method.

3. **Set Output Resolution**

   The code sets the output resolution to 300 DPI using the `OutputResolution` property of the `PngOptions` class.

4. **Run Process Method**

   The PNG conversion is initiated by calling the `Process` method on the `Png` class, passing the configured `PngOptions`. The result is stored in the `resultContainer`.

5. **Handle Result**

   The code prints the result to the console, showcasing the converted file path(s).
