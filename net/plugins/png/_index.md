---
title: Using Aspose.PDF PNG plugin (.NET version)
type: docs
weight: 110
url: /net/plugins/png/
description: Convert PDF to PNG Images with Aspose.PDF PNG Plugin
lastmod: "2024-01-24"
---

If you're looking to convert PDF documents into PNG images using .NET, Aspose.PDF for .NET provides a robust solution. In this guide, we'll walk through the essential steps to create an object, add a data source, and run the process method using the Aspose.PDF library.

## Prerequisites

Before we begin, ensure you have the Aspose.PDF for .NET library installed on your system. If you haven't installed it yet, you can do so via NuGet using the following command:

```bash
Install-Package Aspose.Pdf
```

Additionally, familiarize yourself with the `PngOptions` class and its properties. You can find detailed information about this class in the [Aspose.PDF documentation](https://reference.aspose.com/pdf/net/aspose.pdf/PngOptions/). Note that the `OutputResolution` property represents the image resolution, measured in DPI.

Now, let's explore the provided code and understand how to convert a PDF to PNG images.

## Code Walkthrough

The code below demonstrates a PNG conversion demo using the Aspose.PDF PNG Plugin:

```csharp
using Aspose.Pdf.Plugins;

namespace AsposePluginsNet8.Landings
{
    // Contains methods to convert a PDF document to PNG images.
    internal static class PngDemo
    {
        // Runs the PNG conversion demo.
        internal static void Run()
        {
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
        }
    }
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
