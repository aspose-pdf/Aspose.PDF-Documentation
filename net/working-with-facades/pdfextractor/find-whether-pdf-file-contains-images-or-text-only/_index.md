---
title: Find whether PDF contains images or text
linktitle: Check presence text and images
type: docs
weight: 40
url: /net/find-whether-pdf-file-contains-images-or-text-only/
description: This topic explain how to find whether PDF file contains images or text only with PdfExtractor Class.
lastmod: "2021-06-05"
draft: false
---

## Background

A PDF file can contain both text and images. Sometimes, a user might need to find out whether a PDF file contains only text, or it contains only images. We can also find whether it contain both or none.

{{% alert color="primary" %}}

Following code snippet shows you how to fulfill this requirement.

{{% /alert %}}

```csharp
public static void CheckIfPdfContainsTextOrImages()
{
    // Instantiate a memoryStream object to hold the extracted text from Document
    MemoryStream ms = new MemoryStream();
    // Instantiate PdfExtractor object
    PdfExtractor extractor = new PdfExtractor();

    // Bind the input PDF document to extractor
    extractor.BindPdf(_dataDir + "FilledForm.pdf");
    // Extract text from the input PDF document
    extractor.ExtractText();
    // Save the extracted text to a text file
    extractor.GetText(ms);
    // Check if the MemoryStream length is greater than or equal to 1

    bool containsText = ms.Length >= 1;

    // Extract images from the input PDF document
    extractor.ExtractImage();

    // Calling HasNextImage method in while loop. When images will finish, loop will exit
    bool containsImage = extractor.HasNextImage();

    // Now find out whether this PDF is text only or image only

    if (containsText && !containsImage)
    {
        Console.WriteLine("PDF contains text only");
    }
    else if (!containsText && containsImage)
    {
        Console.WriteLine("PDF contains image only");
    }
    else if (containsText && containsImage)
    {
        Console.WriteLine("PDF contains both text and image");
    }
    else if (!containsText && !containsImage)
    {
        Console.WriteLine("PDF contains neither text or nor image");
    }
}
```
