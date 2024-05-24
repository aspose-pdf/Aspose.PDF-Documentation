---
title: Splitter
type: docs
weight: 120
url: /net/plugins/splitter/
description: Divides PDF document into separate pages
lastmod: "2024-01-24"
draft: false
---

Do you have a large PDF document that you'd like to break down into smaller, more manageable files? With [Aspose.PDF Splitter for .NET](https://products.aspose.org/pdf/net/splitter/), you can easily achieve this task. In this article, we'll explore the process of splitting a PDF document into multiple files using the Aspose.PDF plugin. Let's dive into the code and walk through the steps.

## Prerequisites

You will need the following:

* Visual Studio 2019 or later
* Aspose.PDF for .NET 24.1 or later
* A sample PDF file

Additionally, familiarize yourself with the `SplitOptions` class and its properties. You can find detailed information about this class in the [API Reference](https://reference.aspose.com/pdf/net/aspose.pdf/SplitOptions/). Note that each output `FileDataSource` represents a single page in the split PDF files.

Now, let's explore the provided code and understand how to split a PDF document.

## Code Walkthrough

The code below demonstrates a PDF splitting demo using the Aspose.PDF.Plugins:

```csharp
using Aspose.Pdf.Plugins;
// ...........

// Set the input path of the PDF document to be split.
using var inputStream = File.OpenRead(Path.Combine(@"C:\Samples\", "sample.pdf"));

// Create a new instance of Splitter.
var splitter = new Splitter();

// Create options for splitting the document.
var options = new SplitOptions();

// Add input and output data sources to the options.
options.AddInput(new StreamDataSource(inputStream));

var document = new Aspose.Pdf.Document(inputStream);

for (int i = 1; i <= document.Pages.Count; i++)
{
   var pageNum = string.Format("{0,3}", i.ToString("D3"));
   options.AddOutput(new FileDataSource(Path.Combine(@"C:\Samples\", $"splitter_{pageNum}.pdf")));
}

// Process the options to split the document.
var result = splitter.Process(options);
Console.WriteLine(result);
```

Let's break down the key steps:

1. **Set the Input PDF**

   The code starts by specifying the input PDF document's path to be split. This is done using the `File.OpenRead` method.

2. **Create an Object (Splitter and SplitOptions)**

   The code creates an instance of the `Splitter` class to handle the splitting process. Additionally, an instance of the `SplitOptions` class is created to configure the splitting operation.

3. **Add Data Source (Input and Output)**

   The input PDF document is added to the `SplitOptions` as an input data source using the `AddInput` method. For each page in the document, an output file path is added as an output data source using the `AddOutput` method.

4. **Run Process Method**

   The splitting process is initiated by calling the `Process` method on the `Splitter` class, passing the configured `SplitOptions`. The result of the operation is stored in the `result` variable.

5. **Handle Result**

   The code prints the result to the console, providing information about the splitting process.
