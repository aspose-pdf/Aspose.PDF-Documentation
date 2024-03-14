---
title: Table Generator
type: docs
weight: 130
url: /net/plugins/tablegenerator/
description: Allows adding/inserting a table on the specified page number of the PDF document.
lastmod: "2024-01-24"
draft: false
---

Do you need to create dynamic and visually appealing tables in your PDF documents using .NET? Aspose.PDF for .NET provides a powerful TableGenerator class that simplifies the process. In this chapter, we'll walk through the steps to generate tables in a PDF document using Aspose.PDF Table Generator, from creating a demo document to generating tables with the TableGenerator class.
Let's dive in and learn how to generate tables step by step.

## Prerequisites

You will need the following:

* Visual Studio 2019 or later
* Aspose.PDF for .NET 24.3 or later
* A sample PDF file

## Creating a Demo Document

Before we dive into generating tables, let's create a demo document with empty pages where our tables will be inserted. The `CreateDemoDocument` method in the `TableDemo` class handles this task. Here's how to create a demo document:

* Create a new PDF document.
* Add empty pages to the document.
* Save the document to the specified file.

```cs
// <summary>
// Creates a demo document with empty pages.
//
// Parameters:
// - fileName: The path and name of the output file.
// </summary>
internal static void CreateDemoDocument(string fileName)
{
    // Create a new PDF document.
    var document = new Aspose.Pdf.Document();

    // Add four empty pages to the document.
    for (int i = 0; i < 2; i++)
    {
        document.Pages.Add();
    }

    // Save the document to the specified file.
    document.Save(fileName);
}
```

## Generating Tables

Once we have our demo document ready, we can start generating tables using the `TableGenerator` class. The following snippet demonstrates how to generate tables with various content types and formatting options. Here's how to generate tables:

* Create a new instance of the `TableGenerator` class.
* Create table options and specify input and output file data sources.
* Add tables with rows and cells to the options, specifying content and formatting.
* Process the table generation using the `Process` method and get the result container.

### Creating Tables

To create a table using Aspose.PDF, follow these steps:

```cs
// Create a new instance of the TableGenerator class.
var generator = new TableGenerator();

// Create table options and add demo tables.
var options = new TableOptions();

// Add input and output file data sources to the options.
options.AddInput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));
options.AddOutput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));

// Add the first table to the options.
options
    .InsertPageAfter(1)
    .AddTable()
```

In the code above, we create an instance of `TableOptions` and specify input and output file data sources for the PDF document. We then add a table to the options using the `AddTable` method.

### Adding Content to Tables

Once the table is created, you can populate it with rows and cells containing various types of content, such as text, HTML, images, etc. Here's how to add content to a table:

```csharp
options
    .AddTable()
        .AddRow()
            .AddCell()
                .AddParagraph(new HtmlFragment("<h1>Header 1</h1>")) // Add HTML content to the cell.
            .AddCell()
                .AddParagraph(new HtmlFragment("<h2>Header 2</h2>"))
            .AddCell()
                .AddParagraph(new HtmlFragment("<h3>Header 3</h3>"));
```

In this example, we add a row to the table and populate it with cells containing HTML fragments representing headers.

Useful methods:

* **InsertPageAfter**: Inserts a page after the specified page number.
* **InsertPageBefore**: Inserts a page after the specified page number.
* **AddTable**: Adds a table to the document.
* **AddRow**: Adds a row to the table.
* **AddCell**: Adds cells to the row.
* **AddParagraph**: Adds content to the cell.

You can add the following types of content as paragraph:

* **HtmlFragment** - a content based on HTML markup
* **TeXFragment** - a content based on TeX/LaTeX markup
* **TextFragment** - a simple text content
* **Image** - graphics

## Perform table generation

After adding the content, we can start creating the table.

```cs
// Process the table generation and get the result container.
var resultContainer = generator.Process(options);

// Print the number of results in the result collection.            
Console.WriteLine(resultContainer.ResultCollection.Count);
```

The `Process` method performs table generation. This method also can be wrapped with try-catch to handle errors.

Below you can see the full code of example:

```cs
using Aspose.Pdf;
using Aspose.Pdf.Plugins;
using Aspose.Pdf.Text;

namespace AsposePluginsNet8.Documentation
{
    // <summary>
    // Represents a class that demonstrates the usage of table generation in Aspose.Pdf.
    // </summary>
    internal static class TableDemo
    {
        // <summary>
        // Runs the table generation demo.
        // </summary>
        internal static void Run()
        {
            // Create a demo document and generate tables.
            CreateDemoDocument(@"C:\Samples\Results\table-generator-demo.pdf");
            CreateDemoTable();
        }

        // <summary>
        // Creates a demo document with four empty pages.
        //
        // Parameters:
        // - fileName: The path and name of the output file.
        // </summary>
        internal static void CreateDemoDocument(string fileName)
        {
            // Create a new PDF document.
            var document = new Aspose.Pdf.Document();

            // Add four empty pages to the document.
            for (int i = 0; i < 2; i++)
            {
                document.Pages.Add();
            }

            // Save the document to the specified file.
            document.Save(fileName);
        }

        // <summary>
        // Generates tables using the TableGenerator class.
        // </summary>
        internal static void CreateDemoTable()
        {
            // Create a new instance of the TableGenerator class.
            var generator = new TableGenerator();

            // Create table options and add demo tables.
            var options = new TableOptions();

            // Add input and output file data sources to the options.
            options.AddInput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));
            options.AddOutput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));

            // Add the first table to the options.
            options
                .InsertPageAfter(1)
                .AddTable()
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new HtmlFragment("<h1>Header 1</h1>"))
                        .AddCell()
                            .AddParagraph(new HtmlFragment("<h2>Header 2</h2>"))
                        .AddCell()
                            .AddParagraph(new HtmlFragment("<h3>Header 3</h3>"))
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new TeXFragment("{\\small The equation $E=mc^2$, discovered in 1905 by Albert Einstein.}", true))
                        .AddCell()
                            .AddParagraph(new TextFragment("Cell 2 2"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Cell 2 3"))
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new TextFragment("Cell 3 1a"))
                            .AddParagraph(new TextFragment("Cell 3 1b"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Cell 3 2"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Cell 3 3"));

            // Add the second table to the options.
            options
                .InsertPageBefore(2)
                .AddTable()
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new TextFragment("Header 1 1"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Header 1 2"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Header 1 3"))
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new Image()
                            {
                                File = @"C:\Samples\logo.png",
                                FixWidth = 75,
                                FixHeight = 75,
                            })
                        .AddCell()
                            .AddParagraph(new Image()
                            {
                                File = @"C:\Samples\sample.svg",
                                FileType = ImageFileType.Svg,
                                FixWidth = 75,
                                FixHeight = 75
                            })
                        .AddCell()
                            .AddParagraph(new Image()
                            {
                                ImageStream = File.OpenRead(@"C:\Samples\Conversion\Demo.dcm"),
                                FileType = ImageFileType.Dicom,
                                FixWidth = 75,
                                FixHeight = 75
                            });

            // Process the table generation and get the result container.
            var resultContainer = generator.Process(options);

            // Print the number of results in the result collection.
            Console.WriteLine(resultContainer.ResultCollection.Count);
        }
    }
}
```
