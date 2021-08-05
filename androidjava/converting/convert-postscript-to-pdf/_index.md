---
title: Convert PostScript to PDF 
linktitle: Convert PostScript to PDF
type: docs
weight: 370
url: /androidjava/convert-postscript-to-pdf/
lastmod: "2021-06-05"
description: Conversion PostScript to PDF format is possible with Java library. Aspose.PDF allows you to use PsLoadOptions class for this task.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Java** support features converting PostScript files to PDF format. One of the features from Aspose.PDF is that you can set a set of font folders to be used during conversion.

In order to convert a PostScript file to PDF format, Aspose.PDF for Java offers [PsLoadOptions](https://apireference.aspose.com/pdf/java/com.aspose.pdf/PsLoadOptions) class which is used to initialize the LoadOptions object. Later this object can be passed as an argument to Document object constructor, which will help PDF Rendering Engine to determine the format of source document.

Following code snippet can be used to convert a PostScript file into PDF format:

```java
public static void ConvertPostScriptToPDF_Simple() 
        // Initialize document object

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo.pdf").toString();
        String psDocumentFileName = Paths.get(_dataDir.toString(), "demo.ps").toString();
        PsLoadOptions options = new PsLoadOptions();

        // Create Document object
        Document document = new Document(psDocumentFileName, options);

        // Save output PDF document
        document.save(pdfDocumentFileName);
    }
```
Additionally, you can set a set of font folders that will be used during conversion:

```java
public static void ConvertPostscriptToPDFAvdanced() {
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo.pdf").toString();
        String psDocumentFileName = Paths.get(_dataDir.toString(), "demo.ps").toString();
        PsLoadOptions options = new PsLoadOptions();
        
        options.setFontsFolders(new String[] { "c:\tmp\fonts1", "c:\tmp\fonts2" });

        // Create Document object
        Document document = new Document(psDocumentFileName, options);

        // Save output PDF document
        document.save(pdfDocumentFileName);
    }
}
```