---
title: Extract and Save an Attachment 
linktitle: Extract and Save an Attachment
type: docs
weight: 20
url: /androidjava/extract-and-save-an-attachment/
description: Aspose.PDF for Java allows you to get all attachments from a PDF document. Also, you can get an individual attachment from your document.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Get Attachments From PDF Document

With Aspose.PDF, it is possible to get all attachments from a PDF document. This is useful either when you want to save the documents separately from the PDF, or if you need to strip a PDF of attachments.

The following code snippets show how to get all the attachments from a PDF document.

```java
   public static void GetAttachmentsFromPDFDocument() {
// Open document
Document pdfDocument = new Document(_dataDir+"input.pdf");
  // Get particular embedded file
  FileSpecification fileSpecification = pdfDocument.getEmbeddedFiles().get_Item(1);
  // Get the file properties
  System.out.printf("Name: - " + fileSpecification.getName());
  System.out.printf("\nDescription: - " + fileSpecification.getDescription());
  System.out.printf("\nMime Type: - " + fileSpecification.getMIMEType());
  // Get attachment form PDF file
  try {
   InputStream input = fileSpecification.getContents();
   File file = new File(fileSpecification.getName());
   // Create path for file from pdf
   file.getParentFile().mkdirs();
   // Create and extract file from pdf
   java.io.FileOutputStream output = new java.io.FileOutputStream(fileSpecification.getName(), true);
   byte[] buffer = new byte[4096];
   int n = 0;
   while (-1 != (n = input.read(buffer)))
    output.write(buffer, 0, n);
   // Close InputStream object
   input.close();
   output.close();
  } catch (IOException e) {
   e.printStackTrace();
  }
  // Close Document object
  pdfDocument.dispose();
        
    }

```

## Get Attachment Information

As mentioned in [Get Attachments from a PDF Document](/pdf/java/get-attachments-from-a-pdf-document/), attachment information is held in the [FileSpecification](https://apireference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) object, gathered with other attachments in the [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Document) object's EmbeddedFiles collection.

The [FileSpecification](https://apireference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) object provides methods that get information about the attachment, for example:

- getName() – gets the file name.
- [getDescription()](https://apireference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification#getDescription--) – gets the file description.
- getMIMEType() – gets the file's MIME type.
- getParams() – information about the file parameters, for example CheckSum, CreationDate, ModDate and Size.

To get these parameters, first make sure that the getParams() method does not return null.

Either loop through all of the attachments in the EmbeddedFiles collection using for loop, or get an individual attachment by specifying its index value. The following code snippet shows how to get information about a specific attachment.

```java
    public static void GetAttachmentInformation() {
  // Open document
  Document pdfDocument = new Document(_dataDir+"input.pdf");
  // Get particular embedded file
  FileSpecification fileSpecification = pdfDocument.getEmbeddedFiles().get_Item(1);
  // Get the file properties
  System.out.println("Name:-" + fileSpecification.getName());
  System.out.println("Description:- " + fileSpecification.getDescription());
  System.out.println("Mime Type:-" + fileSpecification.getMIMEType());
  // Check if parameter object contains the parameters
  if (fileSpecification.getParams() != null) {
   System.out.println("CheckSum:- " + fileSpecification.getParams().getCheckSum());
   System.out.println("Creation Date:- " + fileSpecification.getParams().getCreationDate());
   System.out.println("Modification Date:- " + fileSpecification.getParams().getModDate());
   System.out.println("Size:- " + fileSpecification.getParams().getSize());
  } 
```
