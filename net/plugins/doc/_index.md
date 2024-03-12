---
title: Using Aspose.PDF DOC Converter (.NET version)
type: docs
weight: 10
url: /net/plugins/doc/
description: Converting PDF to Word Made Simple with PdfDoc Plugin
lastmod: "2024-01-24"
draft: true
---

## Working with Aspose.Pdf.Doc plugin for Microsoft Word Conversion

This chapter guides you through using the Aspose.Pdf plugin for .NET to convert a PDF document to Microsoft Word format (.docx).

Aspose.Pdf provides a powerful set of tools for manipulating and converting PDF files. Here, we'll focus on the `PdfDoc` plugin specifically designed for seamless conversion between PDF and Word formats.

### 1. Setting Up Your Conversion (screenshot of FileDataSource class)

The conversion process involves three main steps: defining input and output files, creating a `PdfDoc` object, and specifying conversion options.

#### 1.1. Defining Data Sources:

- **Input File:** We'll use the `FileDataSource` class to specify the location of the PDF file you want to convert. 
  
```csharp
  FileDataSource inputDataSource = new(Path.Combine(@"C:\Samples\", "sample.pdf"));
```

    - Replace `"C:\Samples\sample.pdf"` with the actual path to your PDF file.

- **Output File:** Similarly, use another `FileDataSource` object to define the location and filename for the resulting Word document.

```csharp
  FileDataSource outputDataSource = new(Path.Combine(@"C:\Samples\", "sample.docx"));
```

  - Replace `"C:\Samples\sample.docx"` with your desired output path and filename.

### 2. Creating the PdfDoc Plugin Object (screenshot of PdfDoc class)

Next, we create an instance of the `PdfDoc` class to perform the conversion.

```csharp
  var plugin = new PdfDoc();
```

This object serves as the engine for the conversion process.

### 3. Configuring Conversion Options (screenshot of PdfToDocOptions class)

The `PdfToDocOptions` class allows you to fine-tune the conversion process. Here's how to set the essential options:

  - **Save Format:** Specify the desired output format for the Word document. In this case, we use `SaveFormat.DocX` to generate a Microsoft Word 2007 or later compatible document (.docx).

  - **Conversion Mode:** Define how the plugin interprets the PDF structure during conversion. We'll use `ConversionMode.EnhancedFlow` to optimize the resulting Word document for layout and formatting. 

Here's the code snippet for configuring options:

```csharp
  PdfToDocOptions options = new()
  {
      SaveFormat = SaveFormat.DocX,
      ConversionMode = ConversionMode.EnhancedFlow
  };
```

**Adding Input and Output:**

Finally, we associate the previously defined data sources with the conversion options using the `AddInput` and `AddOutput` methods: 

```csharp
  options.AddInput(inputDataSource);
  options.AddOutput(outputDataSource);
```

This connects the input PDF and desired output Word document to the conversion process.

### 4. Performing the Conversion

With everything set up, let's initiate the conversion by calling the `Process` method of the `PdfDoc` plugin and passing the configured options:

```csharp
  var resultContainer = plugin.Process(options);
```

This method executes the conversion and returns a `ResultContainer` object containing details about the process.

**Retrieving Results:**

Although not essential for basic conversion, you can access the results through the `ResultCollection` property of the `ResultContainer` object. This might be useful for debugging or tracking specific conversion details.

```csharp
  var result = resultContainer.ResultCollection[0];

  // Print the result (optional for demonstration purposes)
  Console.WriteLine(result);
```

With this final step, your PDF document will be converted to the specified Word format and saved to the defined output location.

This chapter provided a basic overview of using Aspose.Pdf for PDF to Word conversion. Remember to consult the official Aspose.Pdf documentation for more advanced options and functionalities.
