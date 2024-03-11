---
title: Using Aspose.PDF Text Extractor (.NET version)
type: docs
weight: 130
url: /net/plugins/textextractor/
description: Extracts text content from the PDF document.
lastmod: "2024-01-24"
draft: false
---

# Extracting Text from PDF Documents using Aspose.PDF for .NET

Do you have a PDF document from which you need to extract text programmatically? With Aspose.PDF for .NET, you can easily achieve this task using the TextExtractor class. In this guide, we'll walk through the basic steps to create a text extraction application in .NET, covering the creation of a TextExtractor object, adding a data source, and running the text extraction process.

## Prerequisites

Before we start, ensure you have the Aspose.PDF for .NET library installed on your system. If you haven't installed it yet, use the following NuGet command:

```bash
Install-Package Aspose.Pdf
```

Additionally, familiarize yourself with the `TextExtractorOptions` class and its functionalities. Detailed information can be found in the [Aspose.PDF documentation](https://reference.aspose.com/pdf/net/aspose.pdf/TextExtractorOptions/).

Now, let's delve into the code and explore how to extract text from a PDF document.

## Code Walkthrough

The provided code showcases a `TextExtractorDemo` class with a `Run` method. Let's break down the key steps:

```csharp
using Aspose.Pdf.Plugins;

namespace AsposePluginsNet8.Documentation
{
    internal static class TextExtractorDemo
    {
        // Runs the text extraction demo.
        internal static void Run()
        {
            // Create a new instance of TextExtractor.
            using TextExtractor extractor = new();

            // Create a FileDataSource for the input PDF file.
            FileDataSource fileSource = new(Path.Combine(@"C:\Samples\", "sample.pdf"));

            // Create TextExtractorOptions.
            TextExtractorOptions textExtractorOptions = new();
            textExtractorOptions.AddInput(fileSource);

            // Process the text extraction.
            var resultContainer = extractor.Process(textExtractorOptions);
            var results = resultContainer.ResultCollection;

            // Print the extracted text.
            Console.WriteLine(results[0]);
        }
    }
}
```

### 1. Create a TextExtractor Object

The code begins by creating a new instance of the `TextExtractor` class. This class provides methods to extract text from PDF documents.

```csharp
using TextExtractor extractor = new();
```

### 2. Add a Data Source

Next, a `FileDataSource` is created for the input PDF file. This is the file from which text will be extracted.

```csharp
FileDataSource fileSource = new(Path.Combine(@"C:\Samples\", "sample.pdf"));
```

### 3. Create TextExtractorOptions

A `TextExtractorOptions` object is created to configure the text extraction process. The input file source is added to the options.

```csharp
TextExtractorOptions textExtractorOptions = new();
textExtractorOptions.AddInput(fileSource);
```

### 4. Run Text Extraction Process

The `Process` method is then called on the `TextExtractor` object, passing the configured options. The result container holds the extracted text, and it is printed to the console.

```csharp
var resultContainer = extractor.Process(textExtractorOptions);
var results = resultContainer.ResultCollection;
Console.WriteLine(results[0]);
```

