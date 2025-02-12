---
title: Extract fonts from PDF 
linktitle: Extract fonts
type: docs
weight: 30
url: /java/extract-fonts-from-pdf/
description: How to extract font from PDF using Aspose.PDF for Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to extract fonts from a PDF document using Aspose.PDF for Java
Abstract: The article provides a method to extract all fonts from a PDF document using the `Document.IDocumentFontUtilities.getAllFonts()` method from the `Document` class in Java. The process involves loading the PDF document and retrieving its fonts, which are then saved using their respective font names. The code snippet demonstrates the implementation of this process, illustrating the steps to load the document, extract fonts, and save them to a specified location. This approach is useful for users needing to access or utilize fonts embedded within PDF files.
SoftwareApplication: java
---

In case you want to get all fonts from a PDF document, you can use `Document.IDocumentFontUtilities.getAllFonts()` method provided in Document class.
Please check following code snippet in order to get all fonts from an existing PDF document:

```java
public static void Extract_Fonts() throws FileNotFoundException
{
    // The path to the documents directory.
    String filePath = "<... enter file name ...>";
    
    // Load PDF document
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);
    com.aspose.pdf.Font[] fonts = pdfDocument.getFontUtilities().getAllFonts();

    for (com.aspose.pdf.Font font : fonts)
    {
        font.save(new FileOutputStream(font.getFontName()));
    }
}
```
