---
title: FAQ 
linktitle: FAQ
type: docs
weight: 140
url: /net/faq/
description: Here you can find answers to Frequently Asked Questions for Aspose.PDF for .NET library.
lastmod: "2024-11-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## What formats does Aspose.PDF for .NET support?
Aspose.PDF for .NET supports popular file formats such as PDF, TXT, HTML, PCL, XML, XPS, EPUB, TEX, and image formats. For more details, please visit the page [Supported File Formats](https://docs.aspose.com/pdf/net/supported-file-formats/)

## What AI features Aspose.PDF for .NET support?

## How many files can I combine to PDF at once?
You can merge an unlimited number of files into PDF at once.

```csharp
// Create a new PDF document
Document mergedDoc = new Document();

// List of files to merge
string[] pdfFiles = { "file1.pdf", "file2.pdf", "file3.pdf" };

foreach (string file in pdfFiles)
{
    Document tempDoc = new Document(file);
    mergedDoc.Pages.Add(tempDoc.Pages);
}

// Save the merged PDF document
mergedDoc.Save("merged_output.pdf");
```

or

```csharp
using (Document mergedDocuments = Document.MergeDocuments("input1.pdf", "input2.pdf", `"input3.pdf"))
{
     mergedDocuments.Save("merged_output.pdf");
}
```

## How to insert Image into PDF?
To insert an image into a PDF using Aspose.PDF for .NET, you can use the following code:

```csharp
// Load or create a new PDF document
Document pdfDoc = new Document("input.pdf");

// Access the page where the image will be added
Page page = pdfDoc.Pages[1];

// Load the image
Image image = new Image
{
    File = "image.jpg",
    FixWidth = 100,
    FixHeight = 100
};

// Define the image position
page.Paragraphs.Add(image);

// Save the PDF document
pdfDoc.Save("output.pdf");
```

## How to edit the text in PDF?
To edit the text in a PDF using Aspose.PDF for .NET, you can follow these steps:

```csharp
// Load or create a new PDF document
Document pdfDoc = new Document("input.pdf");

// Access the page where the image will be added
Page page = pdfDoc.Pages[1];

// Load the image
Image image = new Image
{
    File = "image.jpg",
    FixWidth = 100,
    FixHeight = 100
};

// Define the image position
page.Paragraphs.Add(image);

// Save the PDF document
pdfDoc.Save("output.pdf");
```

## How to add page numbers to PDF file?
To add page numbers to a PDF using Aspose.PDF for .NET, you can use the following code:

```csharp
// Create a new PDF document
Document doc = new Document();

// Add pages to the document
for (int i = 0; i < 5; i++)
{
    Page page = doc.Pages.Add();
    page.Paragraphs.Add($"This is page {i + 1}.");
}

// Add page numbers to the document
for (int i = 0; i < doc.Pages.Count; i++)
{
    Page page = doc.Pages[i];
    Paragraph paragraph = page.Paragraphs.Add($"Page {i + 1} of {doc.Pages.Count}");
    paragraph.Format.Alignment = ParagraphAlignment.Right;
    paragraph.Format.FontSize = 10;
    paragraph.Format.VerticalAlignment = VerticalAlignment.Bottom;
    paragraph.Format.LineSpacing = 1;
}

// Save the PDF document
doc.Save("output.pdf");
```

## How to create a background for PDF Documents?
To create a background for a PDF document using Aspose.PDF for .NET, you can use the following code:

```csharp
// Load the PDF document
Document pdfDoc = new Document("input.pdf");

// Create an image and set it as a background
foreach (Page page in pdfDoc.Pages)
{
    ImageStamp backgroundImage = new ImageStamp("background.jpg")
    {
        Opacity = 0.5,
        Background = true
    };
    page.AddStamp(backgroundImage);
}

// Save the PDF with background image
pdfDoc.Save("output_with_image_background.pdf");
```

## How to secure PDF document?
To secure a PDF document using Aspose.PDF for .NET, you can apply password protection and set permissions. Here's an example:

```csharp
// Load the PDF document
Document pdfDoc = new Document("input.pdf");

// Set encryption and password options
pdfDoc.Encrypt("user_password", "owner_password", Permissions.PrintDocument | Permissions.FillIn, CryptoAlgorithm.AESx128);

// Save the secured PDF document
pdfDoc.Save("secured_output.pdf");
```

- Specify the permissions using the `Security.Permissions` property

With these password and permissions settings, the PDF document will be secured and users will need to provide the correct passwords to access and use the document.

## How to add bold text in highlighted annotation on a PDF page?
To add bold text in a highlighted annotation:
- Use the `TextAnnotation` class to create the highlight annotation.
- Set the annotation’s `RichText` property with the HTML string that specifies the text style (e.g., `<b>` tag for bold).

```csharp
// Initialize PDF Document
Document pdfDoc = new Document("input.pdf");
Page page = pdfDoc.Pages[1];

// Create a highlight annotation
TextAnnotation highlight = new TextAnnotation(page, new Rectangle(100, 600, 200, 650))
{
    Title = "Highlight Annotation",
    RichText = "<b>This is bold text in a highlighted annotation</b>",
    Color = Color.Yellow,
    Opacity = 0.5
};

// Add annotation to the page
page.Annotations.Add(highlight);

// Save document
pdfDoc.Save("output.pdf");
```

## How to use GoToRemoteAction and XYZExplicitDestination to create a hyperlink to another PDF file, inheriting the current document's zoom level?
To create a hyperlink to another PDF file that preserves the current zoom level:
- Use `GoToRemoteAction` for linking to an external PDF.
- Apply `XYZExplicitDestination` to inherit the zoom level from the current document.

```csharp
// Initialize PDF Document
Document pdfDoc = new Document("input.pdf");

// Create GoToRemoteAction with XYZExplicitDestination
GoToRemoteAction remoteAction = new GoToRemoteAction("target.pdf", new XYZExplicitDestination(1, 100, 100, 1));

// Add link annotation with remote action
LinkAnnotation link = new LinkAnnotation(pdfDoc.Pages[1], new Rectangle(100, 600, 200, 650))
{
    Action = remoteAction
};
pdfDoc.Pages[1].Annotations.Add(link);

// Save document
pdfDoc.Save("output.pdf");
```

## How to validate a tagged PDF?
- This method verifies compliance with PDF/UA standards.
- Validation results are typically saved to a log file.

```csharp
// Load the tagged PDF document
Document pdfDoc = new Document("tagged.pdf");

// Validate for PDF/UA compliance
pdfDoc.Validate("validation-log.xml", PdfFormat.PDF_UA_1);
```

## How to implement regex search for TextFragemntAbsorber?
To use regex with the `TextFragmentAbsorber` class in Aspose.PDF for .NET, you can follow this example:

```csharp
// Create a new PDF document
Document doc = new Document("input.pdf");

// Create a TextFragmentAbsorber with a regex pattern
TextFragmentAbsorber absorber = new TextFragmentAbsorber(@"\b\w+\b", new TextSearchOptions(true));

// Process the PDF document
absorber.Visit(doc);

// Loop through matched fragments
foreach (TextFragment fragment in asorber.TextFragments)
{
    // Example: Change text color of matched fragments
    fragment.TextState.ForegroundColor = Color.Red;
    
    // Example: Modify the matched text if needed
    fragment.Text = "[REDACTED]";  // Replace with custom text
}
```

The key points are:
- Pass a regular expression pattern to the `TextFragmentAbsorber` constructor
- The pattern `@"\b\w+\b"` will match whole words
- Call the `Visit()` method to process the PDF document
- Access the extracted `TextFragments` objects from the `TextFragments` property

## How to make a valid PDF/A document unless the missing font or its substitution is provided?
To create a valid PDF/A document in Aspose.PDF for .NET, you need to ensure that all required fonts are embedded or substituted. Here's an example:

- Set the `DefaultFontName` property to define a substitute font.
- Use `Convert` to ensure the document meets PDF/A standards.

```csharp
// Load the document
Document pdfDoc = new Document("input.pdf");

// Set default font for substitution
pdfDoc.FontUtilities.DefaultFontName = "Arial";

// Convert to PDF/A
pdfDoc.Convert("conversion-log.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

// Save as PDF/A
pdfDoc.Save("output-pdfa.pdf");
```

## Does Aspose.PDF for .NET support Linux?
Yes, Aspose.PDF for .NET supports running on Linux environments. You can use the .NET Core version or later, which is cross-platform and can be used on Windows, macOS, and Linux.

## Does Aspose.PDF for .NET support .NET 2.0, 3.5, and 4.0 frameworks?
Yes, Aspose.PDF for .NET supports the following .NET frameworks:

- .NET 2.0
- .NET 3.5
- .NET 4.0
- .NET Standard 2.0 (which is compatible with .NET Core 2.0 and later)

You can use Aspose.PDF for .NET with any of these frameworks in your project. The library provides a consistent API across the different .NET versions, making it easy to migrate your code between frameworks as needed.

## Where are your .NET Examples?
You can check all of them on [GitHub](https://github.com/aspose-pdf).