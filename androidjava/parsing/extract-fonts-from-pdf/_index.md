---
title: Extract fonts from PDF using Java
linktitle: Extract fonts
type: docs
weight: 30
url: /android-via-java/extract-fonts-from-pdf/
description: How to extract font from PDF using Aspose.PDF for Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
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
