---
title: Convert PDF to DOCX 
linktitle: Convert PDF to DOCX
type: docs
weight: 80
url: /java/convert-pdf-to-docx/
lastmod: "2021-06-05"
description: Convert PDF file to DOCX format with ease and full control with Aspose.PDF for Java. 
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Convert PDF to DOCX

{{% alert color="primary" %}}

Try online. You can check the quality of Aspose.PDF conversion and view the results online at this  link [products.aspose.app/pdf/conversion/pdf-to-docx](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

The DocFormat enumeration also provides the option to choose DOCX as the output format for Word documents. To render the source PDF file to DOCX format, use the code snippet specified below. 

## How to convert PDF to DOCX

For quick conversion use Save() method with SaveFormat.DocX options:

```java
    public static void ConvertPDFtoWord_DOCX_Format() {
        // Open the source PDF document
        Document pdfDocument = new Document(_dataDir + "PDFToDOC.pdf");
        // Save the resultant DOC file
        pdfDocument.save(_dataDir + "saveOptionsOutput_out.doc", SaveFormat.DocX);
    }
```
The [DocSaveOptions](https://apireference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions) class has a property named Format which provides the capability to specify the format of the resultant document, that is, DOC or DOCX. In order to convert a PDF file to DOCX format, please pass the Docx value from the DocSaveOptions.DocFormat enumeration.

Please take a look over the following code snippet which provides the capability to convert PDF file to DOCX format with Java.

```java
    public static void ConvertPDFtoWord_Advanced_DOCX_Format()
    {        
        // Open the source PDF document
        Document pdfDocument = new Document(_dataDir + "PDFToDOC.pdf");
    
        // Instantiate DocSaveOptions object
        DocSaveOptions saveOptions = new DocSaveOptions();
        // Specify the output format as DOCX
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        // Set other DocSaveOptions params
        // ....
        
        // Save document in docx format
        pdfDocument.save("ConvertToDOCX_out.docx", saveOptions);
    }
}
```




