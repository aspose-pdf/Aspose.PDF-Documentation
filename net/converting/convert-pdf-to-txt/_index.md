---
title: Convert PDF to TXT
type: docs
weight: 260
url: /net/convert-pdf-to-txt/
---
# Convert PDF to TXT

## Convert whole PDF document to text file

You can convert PDF document to .TXT file using `Visit` method of `TextAbsorber` class.

The following code snippet explains how to extract the texts from the all pages.

```csharp
public static void ConvertPDFDoctoTXT()
{
    // Open document
    Document pdfDocument = new Document(_dataDir + "demo.pdf");
    TextAbsorber ta = new TextAbsorber();
    ta.Visit(pdfDocument);
    // Save the extracted text in text file
    File.WriteAllText(_dataDir + "input_Text_Extracted_out.txt",ta.Text);
}
```

## Convert PDF page to text file

You can convert PDF document to .TXT file using `Visit` method of `TextAbsorber` class.

The following code snippet explains how to extract the texts from the all pages.

```csharp
public static void ConvertPDFPagestoTXT()
{
    // Open document
    Document pdfDocument = new Document(_dataDir + "demo.pdf");
    var pages = new int[];
    TextAbsorber ta = new TextAbsorber();

    ta.Visit(pdfDocument);
    // Save the extracted text in text file
    File.WriteAllText(_dataDir + "input_Text_Extracted_out.txt",ta.Text);
}
```
