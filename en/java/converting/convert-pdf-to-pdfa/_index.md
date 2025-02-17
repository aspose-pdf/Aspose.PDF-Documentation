---
title: Convert PDF to PDF/A formats 
linktitle: Convert PDF to PDF/A formats
type: docs
weight: 100
url: /java/convert-pdf-to-pdfa/
lastmod: "2025-02-17"
description: Learn how to convert PDF files to PDF/A format for long-term archiving and compliance with document preservation standards using Aspose.PDF in Java.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true 
AlternativeHeadline: How to convert PDF files to PDF/A format using Aspose.PDF for Java
Abstract: The article outlines the process of converting PDF files to various PDF/A compliance formats using Aspose.PDF for Java, emphasizing the necessity of validating the PDF before conversion, which is done following Adobe Preflight standards. The article provides code snippets for converting PDFs to PDF/A-1b, PDF/A-3b, PDF/A-3a, PDF/A-2a, and PDF/A-3U formats. It describes the validation process, which involves generating an XML file to log validation results, and offers functionality to specify actions for elements that cannot be converted. Additionally, it explains how to attach XML files to PDF/A-3 compliant documents and highlights the importance of reconverting post-attachment to ensure proper metadata handling. The article also mentions an online tool for converting PDFs to PDF/A-1A, offering users a chance to explore the functionality and quality of the conversion process.
SoftwareApplication: java
---

**Aspose.PDF for Java** allows you to convert a PDF file to a PDF/A compliant PDF file. Before doing so, the file must be validated. This article explains how.

Please note we follow Adobe Preflight for validating PDF/A conformance. All tools on the market have their own "representation" of PDF/A conformance. Please check this article on [PDF/A validation tools](http://wiki.opf-labs.org/display/SPR/PDFA+Validation+tools+give+different+results) for reference. We chose Adobe products for verifying how Aspose.PDF produces PDF files because Adobe is at the center of everything connected to PDF.

Before converting the PDF to a PDF/A compliant file, validate the PDF using the validate method. The validation result is stored in an XML file and then this result is also passed to the convert method. You can also specify the action for the elements which can not be converted using the [ConvertErrorAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction) enumeration.

## PDF to PDF/A_1b Conversion

The following code snippet shows how to convert PDF files to PDF/A-1b compliant PDF.

```java
// Open document
Document document = new Document(DATA_DIR + "PDFToPDFA.pdf");

// Convert to PDF/A compliant document
// During conversion process, the validation is also performed
document.convert(DATA_DIR + "log.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

// Save output document
document.save(DATA_DIR + "PDFToPDFA_out.pdf");
document.close();
```

To perform validation only, use the following line of code:

```java
// Open document
Document document = new Document(DATA_DIR + "ValidatePDFAStandard.pdf");

// Validate PDF for PDF/A-1a
if (document.validate(DATA_DIR + "validation-result-A1A.xml", PdfFormat.PDF_A_1B)) {
    System.out.println("Valid");
} else {
    System.out.println("Non valid");
}
document.close();
```

## PDF to PDF/A_3b Conversion

From [Aspose.PDF for Java 9.3.0](https://downloads.aspose.com/pdf/java), the API also supports converting PDF files to PDF/A_3b format.

```java
// Open document
Document document = new Document(DATA_DIR + "PDFToPDFA.pdf");

// Convert to PDF/A compliant document
// During conversion process, the validation is also performed
document.convert(DATA_DIR + "log.xml", PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);

// Save output document
document.save(DATA_DIR + "PDFToPDFA_out.pdf");
document.close();
```

## PDF to PDF/A_3a Conversion

From [Aspose.PDF for Java 10.6.0](https://downloads.aspose.com/pdf/java), the API also supports converting PDF files to PDF/A_3a format.

```java
// Open document
Document document = new Document(DATA_DIR + "PDFToPDFA.pdf");

// Convert to PDF/A compliant document
// During conversion process, the validation is also performed
document.convert("file.log", PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);

// Save output document
document.save(DATA_DIR + "PDFToPDFA_out.pdf");
document.close();
```

## PDF to PDF/A_2a Conversion

Starting release of [Aspose.PDF for Java 10.2.0](https://downloads.aspose.com/pdf/java), the API offers the feature to convert PDF files to PDF/A3 format.

```java
    public static void ConvertPDFtoPDFa2a() {
        // Open document
        Document pdfDocument = new Document(_dataDir + "PDFToPDFA.pdf");

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        pdfDocument.convert("file.log", PdfFormat.PDF_A_2A, ConvertErrorAction.Delete);

        // Save output document
        pdfDocument.save(_dataDir + "PDFToPDFA_out.pdf");
    }
```

## PDF to PDF/A_3U Conversion

Starting release of Aspose.PDF for Java 17.2.0, the API offers the feature to convert PDF files to PDF/A_3U format.

```java
    public static void ConvertPDFtoPDFa3u() {
        // Open document
        Document pdfDocument = new Document(_dataDir + "PDFToPDFA.pdf");

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        pdfDocument.convert("file.log", PdfFormat.PDF_A_3U, ConvertErrorAction.Delete);

        // Save output document
        pdfDocument.save(_dataDir + "PDFToPDFA_out.pdf");
    }
```

## Create PDF/A-3 and attach XML file

Aspose.PDF for Java offers the feature to convert PDF files to PDF/A format and it also supports the capabilities of adding files as an attachment to PDF document. In case you have a requirement to attach files to PDF/A compliance format, then we recommend using PDF_A_3A value from com.aspose.pdf.PdfFormat enumeration, the PDF/A_3a is the format that provides the feature to attach any file format as an attachment to PDF/A compliant file. However, once the file is attached, you should convert it into Pdf-3a format again, in order to fix metadata. Please take a look over the following code snippet.

```java
    public static void ConvertPDFtoPDFa3u_attachXML() {
        Document doc = new Document();
        // add page to PDF file
        doc.getPages().add();
        // load XML file
        FileSpecification fileSpecification = new FileSpecification(_dataDir + "attachment.xml", "Sample xml file");
        // Add attachment to document's attachment collection
        doc.getEmbeddedFiles().add(fileSpecification);
        // perform PDF/A_3a conversion
        doc.convert(_dataDir + "log.xml", PdfFormat.PDF_A_3A/* or PDF_A_3B */, ConvertErrorAction.Delete);
        // save final PDF file
        doc.save(_dataDir + "attached_PDFA_3A.pdf");
    }
```

{{% alert color="primary" %}}
**Try to convert PDF to PDF/A online**

Aspose.PDF for Java presents you online free application ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to PDF/A with Free App](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}
