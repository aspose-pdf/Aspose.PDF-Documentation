---
title: Convert PDF to DOC 
linktitle: Convert PDF to DOC
type: docs
weight: 70
url: /java/convert-pdf-to-doc/
lastmod: "2021-02-04"
description: Convert PDF file to DOC format with ease and full control with Aspose.PDF for Java. Learn more how to tune up Microsoft Word Doc file to PDF conversion.
aliases:
    - /net/convert-pdf-to-doc/
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

One of the most popular feature is PDF to Microsoft Word DOC conversion, which makes the content easy to manipulate. Aspose.PDF for Java allows you to convert PDF files to DOC.

**Aspose.PDF for Java** can create PDF documents from scratch and is a great toolkit for updating, editing and manipulating existing PDF documents. An important feature is the ability to convert pages and entire PDF documents to images. Another popular feature is PDF to Microsoft Word DOC conversion, which makes the content easy to manipulate. (Most users can’t edit PDF documents but can easily work with tables, text, and images in Microsoft Word.)

To make things simple and understandable, Aspose.PDF for Java provides a two-line code for transforming a source PDF file into a DOC file. 

{{% alert color="primary" %}}

Try online. You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/conversion/pdf-to-doc](https://products.aspose.app/pdf/conversion/pdf-to-doc)

{{% /alert %}}

The following code snippet shows the process of converting a PDF file into DOC format.

```java
    public static void main(String[] args) throws IOException {
        ConvertPDFtoWord();
        ConvertPDFtoWordDocAdvanced();
    }

    public static void ConvertPDFtoWord() {
        // Open the source PDF document
        Document pdfDocument = new Document(_dataDir + "PDFToDOC.pdf");
        // Save the file into MS document format
        pdfDocument.save(_dataDir + "PDFToDOC_out.doc", SaveFormat.Doc);

    }
```

## Using the DocSaveOptions Class 

The [DocSaveOptions class](https://apireference.aspose.com/pdf/java/com.aspose.pdf/DocSaveOptions) provides numerous properties that improve the process of converting PDF files to DOC format. Among these properties, Mode enables you to specify the recognition mode for PDF content. You can specify any value from the RecognitionMode enumeration for this property. Each of these values has specific benefits and limitations:

- [Textbox](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) mode is fast and good for preserving a PDF file’s original look, but the editability of the resulting document could be limited. Every visually grouped block of text in the original PDF is converted into a textbox in the output document. This achieves a maximal resemblance to the original so the output document looks good, but it consists entirely of textboxes and it could make editing in Microsoft Word hard.

- Flow is full recognition mode, where the engine performs grouping and multi-level analysis to restore the original document as per the author’s intent while producing an easily editable document. The limitation is that the output document might look different from the original.

- The RelativeHorizontalProximity property can be used to control the relative proximity between textual elements and means that distance is normed by the font size. Larger fonts may have bigger distances between syllables and still be considered a single whole. It is specified as a percentage of the font size, for example, 1 = 100%. This means that two characters of 12pt that are placed 12 pt apart are proximal.

- RecognitionBullets is used to switch on bullet recognition during conversion.

```java
    public static void ConvertPDFtoWordDocAdvanced()
    {
        Path pdfFile = Paths.get(_dataDir.toString(), "PDF-to-DOC.pdf");
        Path docFile = Paths.get(_dataDir.toString(), "PDF-to-DOC.doc");
        Document pdfDocument = new Document(pdfFile.toString());        
        DocSaveOptions saveOptions = new DocSaveOptions();
        
        // Specify the output format as DOC
        saveOptions.setFormat(DocSaveOptions.DocFormat.Doc);
        // Set the recognition mode as Flow
        saveOptions.setMode(DocSaveOptions.RecognitionMode.Flow);
        
        // Set the Horizontal proximity as 2.5
        saveOptions.setRelativeHorizontalProximity(2.5f);
        
        // Enable the value to recognize bullets during conversion process
        saveOptions.setRecognizeBullets(true);

        pdfDocument.save(docFile.toString(), saveOptions);
    }
```