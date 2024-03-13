---
title: Using Aspose.PDF Table Generator (.NET version)
type: docs
weight: 130
url: /net/plugins/tablegenerator/
description: Allows adding/inserting a table on the specified page number of the PDF document.
lastmod: "2024-01-24"
draft: false
---

# Generating Tables in PDF Documents with Aspose.PDF for .NET

Do you need to create dynamic and visually appealing tables in your PDF documents using .NET? Aspose.PDF for .NET provides a powerful TableGenerator class that simplifies the process. In this guide, we'll walk through the steps to generate tables in a PDF document using Aspose.PDF, from creating a demo document to generating tables with the TableGenerator class.

## Prerequisites

Before we begin, make sure you have the Aspose.PDF for .NET library installed on your system. If you haven't installed it yet, use the following NuGet command:

```bash
Install-Package Aspose.Pdf
```

Additionally, familiarize yourself with the `TableOptions` class and its functionalities. Detailed information can be found in the [Aspose.PDF documentation](https://reference.aspose.com/pdf/net/aspose.pdf/TableOptions/).

Now, let's dive into the code and explore how to create a demo document and generate tables.

## Code Walkthrough

The provided code showcases a TableDemo class with methods to create a demo document and generate tables. Let's break down the essential steps:

### 1. Create a Demo Document

The `CreateDemoDocument` method creates a new PDF document with four empty pages. This is achieved by adding empty pages to the document using the `Pages.Add` method.

```csharp
internal static void CreateDemoDocument(string fileName)
{
    // Create a new PDF document.
    var document = new Aspose.Pdf.Document();

    // Add four empty pages to the document.
    for (int i = 0; i < 4; i++)
    {
        document.Pages.Add();
    }

    // Save the document to the specified file.
    document.Save(fileName);
}
```

### 2. Generate Tables

The `TableGeneratorDemo` method demonstrates the generation of tables using the `TableGenerator` class. It creates an instance of `TableGenerator`, defines table options, and adds demo tables to the document.

```csharp
internal static void TableGeneratorDemo()
{
    // Create a new instance of the TableGenerator class.
    var generator = new TableGenerator();

    // Create table options and add demo tables.
    var options = new TableOptions()
        .AddDemoTable(1)
        .AddDemoTable(3);

    // Add input and output file data sources to the options.
    options.AddInput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));
    options.AddOutput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));

    // Process the table generation and get the result container.
    var resultContainer = generator.Process(options);

    // Print the number of results in the result collection.
    Console.WriteLine(resultContainer.ResultCollection.Count);
}
```

### 3. Helper Class for Demo Tables

The `Helper` class provides an extension method `AddDemoTable` to simplify the process of adding demo tables to the `TableOptions`. It allows you to specify the page number where the table should be inserted.

```csharp
internal static class Helper
{
    // Adds a demo table to the TableOptions.
    public static TableOptions AddDemoTable(this TableOptions tableOptions, int pageNumber)
    {
        return tableOptions
            .InsertPageAfter(pageNumber)
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
                        .AddParagraph(new TextFragment("Cell 1 1"))
                    .AddCell()
                        .AddParagraph(new TextFragment("Cell 1 2"))
                    .AddCell()
                        .AddParagraph(new TextFragment("Cell 1 3"))
                .AddRow()
                    .AddCell()
                        .AddParagraph(new TextFragment("Cell 1 1"))
                    .AddCell()
                        .AddParagraph(new TextFragment("Cell 1 3"));
    }
}
```

## Conclusion

Congratulations! You've learned how to create a demo document and generate tables in a PDF document using Aspose.PDF for .NET. Feel free to integrate these methods into your projects, customize the table content, and explore additional features provided by the Aspose.PDF library.

For more in-depth information and options, refer to the [Aspose.PDF documentation](https://docs.aspose.com/pdf/net/). 


# Creating Dynamic Tables in PDF Documents with Aspose.PDF for .NET

Are you looking to enhance your PDF documents with dynamic and visually appealing tables? With Aspose.PDF for .NET and the `Helper` class, you can effortlessly create tables with custom content. In this guide, we'll explore the `AddDemoTable` method provided by the `Helper` class, allowing you to insert a demo table into your PDF using the `TableOptions` class.

## Prerequisites

Before you begin, ensure you have the Aspose.PDF for .NET library installed on your system. If you haven't installed it yet, use the following NuGet command:

```bash
Install-Package Aspose.Pdf
```

Additionally, familiarize yourself with the `TableOptions` class and its functionalities. Detailed information can be found in the [Aspose.PDF documentation](https://reference.aspose.com/pdf/net/aspose.pdf/TableOptions/).

Now, let's delve into the code and explore how to use the `AddDemoTable` method to create dynamic tables.

## Code Walkthrough

The provided code showcases the `Helper` class with the `AddDemoTable` method. Let's break down the key steps:

```csharp
internal static class Helper
{
    // Adds a demo table to the TableOptions.
    public static TableOptions AddDemoTable(this TableOptions tableOptions, int pageNumber)
    {
        return tableOptions
            .InsertPageAfter(pageNumber)
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
                        .AddParagraph(new TextFragment("Cell 1 1"))
                    .AddCell()
                        .AddParagraph(new TextFragment("Cell 1 2"))
                    .AddCell()
                        .AddParagraph(new TextFragment("Cell 1 3"))
                .AddRow()
                    .AddCell()
                        .AddParagraph(new TextFragment("Cell 1 1"))
                    .AddCell()
                        .AddParagraph(new TextFragment("Cell 1 3"));
    }
}
```

### 1. AddDemoTable Method

The `AddDemoTable` method is an extension method for `TableOptions` that simplifies the process of adding a demo table. It takes the `TableOptions` instance and the page number where the table should be inserted as parameters.

- **InsertPageAfter**: Inserts a page after the specified page number.
- **AddTable**: Adds a table to the document.
- **AddRow**: Adds a row to the table.
- **AddCell**: Adds cells to the row.
- **AddParagraph**: Adds text to the cell.

### 2. Utilizing AddDemoTable

To use the `AddDemoTable` method, include it in your code as follows:

```csharp
// Create an instance of TableOptions
var tableOptions = new TableOptions();

// Add a demo table to the options on page 1
tableOptions.AddDemoTable(1);
```

This will insert a demo table into your PDF document on the specified page, complete with headers and cells.

## Conclusion

Congratulations! You've learned how to dynamically create tables in your PDF documents using the `AddDemoTable` method provided by the `Helper` class. Feel free to customize the content and structure of the table to suit your specific requirements. For further exploration of features and options, refer to the [Aspose.PDF documentation](https://docs.aspose.com/pdf/net/).

