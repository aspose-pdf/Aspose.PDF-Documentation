---
title: ToC Generator
type: docs
weight: 150
url: /net/plugins/tocgenerator/
description: Creates table of content with Aspose.PDF ToC Generator for .NET 
lastmod: "2024-01-24"
draft: false
---

Do you want to enhance your PDF documents by adding a Table of Contents (TOC) dynamically? Aspose.PDF for .NET provides a powerful `TocGenerator` class that allows you to generate TOCs with ease. In this guide, we'll walk through the basic steps to create a TOC in a PDF document using Aspose.PDF, covering the creation of a `TocGenerator` object, adding input/output paths, and running the TOC generation process.

## Prerequisites

You will need the following:

* Visual Studio 2019 or later
* Aspose.PDF for .NET 24.1 or later
* A sample PDF file

Additionally, familiarize yourself with the `TocOptions` class and its functionalities. Detailed information can be found in the [Aspose.PDF API Reference](https://reference.aspose.com/pdf/net/aspose.pdf/TocOptions/).

Now, let's dive into the code and explore how to generate a Table of Contents for your PDF document.

## Code Walkthrough

We will use `TocGeneratorDemo` class with a `Run` method do demonstrate how to create ToC. Let's break down the key steps:

```csharp
using Aspose.Pdf.Plugins;

namespace AsposePluginsNet8.Documentation
{
    internal static class TocGeneratorDemo
    {
        private const string PathForSamples = @"C:\Samples\";

        // Runs the TOC generation demo.
        internal static void Run()
        {
            // Create a new instance of the TocGenerator class.
            TocGenerator generator = new();

            // Create a new instance of the TocOptions class.
            TocOptions options = new();
            // Add the input and output paths to the TocOptions.
            options.AddInput(new FileDataSource(Path.Combine(PathForSamples, "sample.pdf")));
            options.AddOutput(new FileDataSource(Path.Combine(PathForSamples, "sample_toc.pdf")));

            // Process the TOC generation and get the result container.
            var resultContainer = generator.Process(options);

            // Get the result from the result container.
            var result = resultContainer.ResultCollection[0];

            // Print the result to the console.
            Console.WriteLine(result);
        }
    }
}
```

### 1. Create a TocGenerator Object

The code begins by creating a new instance of the `TocGenerator` class. This class provides methods to generate TOCs for PDF documents.

```csharp
TocGenerator generator = new();
```

### 2. Create TocOptions

Next, a new instance of the `TocOptions` class is created to configure the TOC generation process. Input and output file paths are added to the options.

```csharp
TocOptions options = new();
options.AddInput(new FileDataSource(Path.Combine(PathForSamples, "sample.pdf")));
options.AddOutput(new FileDataSource(Path.Combine(PathForSamples, "sample_toc.pdf")));
```

### 3. Run TOC Generation Process

The `Process` method is then called on the `TocGenerator` object, passing the configured options. The result container holds the generated TOC, and it is printed to the console.

```csharp
var resultContainer = generator.Process(options);
var result = resultContainer.ResultCollection[0];
Console.WriteLine(result);
```
