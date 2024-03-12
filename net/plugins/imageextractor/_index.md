---
title: Using Aspose.PDF ImageExtractor plugin (.NET version)
type: docs
weight: 80
url: /net/plugins/imageextractor/
description: Extracting Images from PDFs Made Easy with ImageExtractor Plugin
lastmod: "2024-01-24"
draft: false
---

## Introduction

If you've ever needed to extract images from a PDF file using .NET, Aspose.PDF for .NET provides a powerful and straightforward solution. In this guide, we'll walk through the basic steps to create an object, add a data source, and run the process method using the Aspose.PDF library.

## Prerequisites

You will need the following:

* Visual Studio 2019 or later
* Aspose.PDF for .NET 21.1 or later
* A sample PDF file

You can download the Aspose.PDF for .NET library from the official website or install them using the NuGet Package Manager in Visual Studio.
Now, let's dive into the code and learn how to use the ImageExtractor plugin.

## Steps

The provided code demonstrates the usage of the `ImageExtractor` plugin to extract images from a PDF file. Let's break down the steps:

### 1. Create an Object (ImageExtractor)

The first step involves creating an instance of the `ImageExtractor` plugin. This is achieved using the following code:

```csharp
using var plugin = new ImageExtractor();
```

Here, the `using` statement ensures proper disposal of resources when the operation is complete.

### 2. Add Data Source

Next, an instance of the `ImageExtractorOptions` class is created to configure the image extraction process. The input file path is added to the options using the `AddInput` method:

```csharp
var imageExtractorOptions = new ImageExtractorOptions();
imageExtractorOptions.AddInput(new FileDataSource(Path.Combine(@"C:\Samples\", "sample.pdf")));
```

Make sure to replace `"C:\Samples\"` and `"sample.pdf"` with the appropriate path and filename of your PDF file.

### 3. Run Process Method

The final step is to process the image extraction using the plugin and options:

```csharp
var resultContainer = plugin.Process(imageExtractorOptions);
```

The result is stored in the `resultContainer`, which contains the extracted image(s).

### 4. Handle Extracted Image(s)

After running the process, you can retrieve the extracted image(s) from the result container. The code below demonstrates saving the first extracted image to a temporary location:

```csharp
var imageExtracted = resultContainer.ResultCollection[0].ToStream();
var someTemporaryPlace = File.OpenWrite("C:\\tmp\\tmp.jpg");
imageExtracted.CopyTo(someTemporaryPlace);
```

Ensure you customize the destination path and filename according to your preferences.

You can copy full example below:

```cs
using Aspose.Pdf.Plugins;

namespace AsposePluginsNet8.Documentation;

internal static class ImageExtractorDemo
{
    // <summary>
    // Demonstrates the usage of the ImageExtractor plugin to extract images from a PDF file.
    // </summary>
    internal static void Run()
    {
        // Create an instance of the ImageExtractor plugin.
        using var plugin = new ImageExtractor();

        // Create an instance of the ImageExtractorOptions class.
        var imageExtractorOptions = new ImageExtractorOptions();

        // Add the input file path to the options.
        imageExtractorOptions.AddInput(new FileDataSource(Path.Combine(@"C:\Samples\", "sample.pdf")));

        // Process the image extraction using the plugin and options.
        var resultContainer = plugin.Process(imageExtractorOptions);

        // Get the extracted image from the result container.
        var imageExtracted = resultContainer.ResultCollection[0].ToStream();
        var someTemporaryPlace = File.OpenWrite(Path.Combine(@"C:\Samples\","tmp.jpg"));
        imageExtracted.CopyTo(someTemporaryPlace);
    }
}
```
