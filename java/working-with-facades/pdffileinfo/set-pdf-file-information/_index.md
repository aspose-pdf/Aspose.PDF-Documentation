---
title: Set PDF file information - facades
type: docs
weight: 20
url: /java/set-pdf-information/
description: This section explains how to set PDF file information  with Aspose.PDF Facades using PdfFileInfo Class.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[PdfFileInfo](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo) class allows you to set file specific information of a PDF document. You need to create an object of [PdfFileInfo](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo) class and then set different file specific properties like Author, Title, Keyword, and Creator etc. Finally, save the updated PDF file using [saveNewInfo(..)](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo#saveNewInfo-java.io.OutputStream-) method of the [PdfFileInfo](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo) object.

The following code snippet shows you how to set PDF file information.

```java
 public static void SetPdfInfo()
    {
        PdfFileInfo fileInfo = new PdfFileInfo(_dataDir + "sample.pdf");
        // Set PDF information
        fileInfo.setAuthor("Aspose");
        fileInfo.setTitle ("Hello World!");
        fileInfo.setKeywords("Peace and Development");
        fileInfo.setCreator ("Aspose");
        
        // Save updated file
        fileInfo.saveNewInfo(_dataDir + "SetfileInfo_out.pdf");
    }
```

## Set Meta Info

[setMetaInfo](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo#setMetaInfo-java.lang.String-java.lang.String-) method allows you to add any information. In our example, we added a field. Check next code snippet:

```java
   public static void SetMetaInfo()
    {
        // Create instance of PdffileInfo object
        PdfFileInfo fInfo = new PdfFileInfo(_dataDir + "sample.pdf");
       
        // Set new customer attribute as meta info
        fInfo.setMetaInfo("Reviewer", "Aspose.PDF user");

        // Save updated file
        fInfo.saveNewInfo(_dataDir + "SetMetaInfo_out.pdf");

    }
```