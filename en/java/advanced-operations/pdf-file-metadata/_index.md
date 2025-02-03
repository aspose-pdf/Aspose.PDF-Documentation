---
title: Working with PDF File Metadata 
linktitle: PDF File Metadata
type: docs
weight: 140
url: /java/pdf-file-metadata/
description: Discover how to manage and extract metadata from PDF files in Java using Aspose.PDF to handle document properties.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Guide on handling PDF file metadata using Aspose.PDF for Java
Abstract: The article provides a comprehensive guide on handling PDF file metadata using Aspose.PDF for Java. It covers methods to retrieve and set both file-specific information and XMP metadata. The guide begins by explaining how to access and display PDF file information such as author, creation date, and title using the `DocumentInfo` class. It then details how to modify these properties and save the updated document, while noting limitations on altering certain fields like "Producer" and "Creator". The article also demonstrates retrieving and setting XMP metadata, including creating custom metadata namespaces with prefixes. Code snippets are provided throughout to illustrate the practical application of these processes.
SoftwareApplication: java
---

## Get PDF File Information

To get file-specific information about a PDF file, first get the [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocumentInfo) object using the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) class  [getInfo()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getInfo--). Once the [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocumentInfo) object is retrieved, you can get the values of the individual properties.

The following code snippet shows you how to set PDF file information.

```java
public class ExampleMetadata {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Metadata/";

    public static void GetPDFFileInformation() {
        // Create a new PDF document
        Document pdfDocument = new Document(_dataDir + "sample.pdf");
        // Get document information
        DocumentInfo docInfo = pdfDocument.getInfo();
        // Show document information
        System.out.println("Author: " + docInfo.getAuthor());
        System.out.println("Creation Date: " + docInfo.getCreationDate());
        System.out.println("Keywords: " + docInfo.getKeywords());
        System.out.println("Modify Date: " + docInfo.getModDate());
        System.out.println("Subject: " + docInfo.getSubject());
        System.out.println("Title: " + docInfo.getTitle());
    }
```

## Set PDF File Information

Aspose.PDF for Java allows you to set file-specific information for a PDF, information like author, creation date, subject, and title.

To set this information:

1. Create a [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocumentInfo) object.
1. Set the values of the properties.
1. Save the updated document using the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) class' [save()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save-com.aspose.ms.System.IO.FileStream-) method.

{{% alert color="primary" %}}

Please note that you cannot set values against the **Producer** and **Creator** fields, because Aspose.PDF for Java x.x.x will be displayed against these fields.

{{% /alert %}}

The following code snippet shows you how to set PDF file information.

```java
 public static void SetPDFFileInformation() {
        // Open document
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // Specify document information
        DocumentInfo docInfo = new DocumentInfo(pdfDocument);

        docInfo.setAuthor("Aspose");
        docInfo.setCreationDate(new java.util.Date());
        docInfo.setKeywords("Aspose.Pdf, DOM, API");
        docInfo.setModDate(new java.util.Date());
        docInfo.setSubject("PDF Information");
        docInfo.setTitle("Setting PDF Document Information");

        // Save output document
        pdfDocument.save(_dataDir + "SetFileInfo_out.pdf");
    }
```

## Get XMP Metadata from PDF File

Aspose.PDF for Java allows you to access a PDF file's XMP metadata.

To get a PDF file's metadata,

1. Create a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object and open the input PDF file.
1. Use the [getMetadata()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getMetadata--) property to get the metadata.

The following code snippet shows you how to get metadata from the PDF file.

```java
   public static void GetXMPMetadata() {

        // Open document
        Document pdfDocument = new Document(_dataDir + "SetXMPMetadata.pdf");

        System.out.println("xmp:CreateDate: " + pdfDocument.getMetadata().get_Item("xmp:CreateDate"));
        System.out.println("xmp:Nickname: " + pdfDocument.getMetadata().get_Item("xmp:Nickname"));
        System.out.println("xmp:CustomProperty: " + pdfDocument.getMetadata().get_Item("xmp:CustomProperty"));

    }
```

## Set XMP Metadata in a PDF File

Aspose.PDF for Java allows you to set metadata in a PDF file. To set metadata:

1. Create a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object.
1. Set metadata values using the [getMetadata()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getMetadata--) property.
1. Save the updated document using the [save()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save-com.aspose.ms.System.IO.FileStream-) method of the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object.

The following code snippet shows you how to set metadata in a PDF file.

```java
    public static void SetXMPMetadata() {

        // Open document
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // Set properties
        pdfDocument.getMetadata().set_Item("xmp:CreateDate", new XmpValue(new java.util.Date()));
        pdfDocument.getMetadata().set_Item("xmp:Nickname", new XmpValue("Nickname"));
        pdfDocument.getMetadata().set_Item("xmp:CustomProperty", new XmpValue("Custom Value"));

        // Save document
        pdfDocument.save(_dataDir + "SetXMPMetadata.pdf");
    }
```

## Insert Metadata with Prefix

Some developers need to create a new metadata namespace with a prefix. The following code snippet shows how to insert metadata with prefix.

```java
    public static void InsertMetadataWithPrefix() {
        // Open document
        Document pdfDocument = new Document(_dataDir + "SetXMPMetadata.pdf");
        pdfDocument.getMetadata().registerNamespaceUri("adc", "http://tempuri.org/adc/1.0");
        pdfDocument.getMetadata().set_Item("adc:format", new XmpValue("application/pdf"));
        pdfDocument.getMetadata().set_Item("adc:title", new XmpValue("alternative title"));        
        // Save document
        pdfDocument.save(_dataDir + "SetPrefixMetadata_out.pdf");
    }
}
```
