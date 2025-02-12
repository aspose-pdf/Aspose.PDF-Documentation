---
title: Disable Files Compression when Adding as Embedded Resources
linktitle: Disable Files Compression
type: docs
weight: 40
url: /java/disable-files-compression-when-adding-as-embedded-resources/
description: This article explains how to disable files compression when Adding as Embedded Resources
lastmod: "2021-06-05"
TechArticle: true 
AlternativeHeadline: How to disable files compression when Adding as Embedded Resources Aspose.PDF Java 
Abstract: The article introduces an update to the `FileSpecification` class in the Aspose.PDF Java API, which now allows developers to disable compression for attachments added to PDF documents. By default, attachments are compressed using the `FileEncoding.Zip` method. However, with the new `setEncoding(..)` method, developers can choose to disable compression by setting the encoding to `FileEncoding.None`. This enhancement provides greater flexibility in handling file attachments. The article includes a code snippet demonstrating how to add an uncompressed attachment to a PDF, illustrating the use of this new capability.
SoftwareApplication: java
---

The [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) class allows developers to add attachments to PDF documents. By default, attachments are compressed. We have updated the API to allow developers to disable compression when adding files as embedded resource. This gives developers more control over how files are processed.

To allow developers to control file compression the [setEncoding(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification#setEncoding-int-) method has been added to the [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) class. This property determines which encoding will be used for file compression. The method accepts a value from the [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding) enumerator. The possible values are [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).None and [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).Zip.

If Encoding is set to [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).None, then attachment is not compressed. The default encoding is [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).Zip.

The following code snippet shows how to add an attachment to a PDF document.

```java
    public static void DisableFilesCompressionWhenAddingAsEmbeddedResources() throws IOException{
  // get reference of source/input file
  java.nio.file.Path path = java.nio.file.Paths.get(_dataDir+"input.pdf");
  // read all the contents from source file into ByteArray
  byte[] data = java.nio.file.Files.readAllBytes(path);
  // create an instance of Stream object from ByteArray contents
  InputStream is = new ByteArrayInputStream(data);
  // Instantiate Document object from stream instance
  Document pdfDocument = new Document(is);
  // setup new file to be added as attachment
  FileSpecification fileSpecification = new FileSpecification("test.txt", "Sample text file");
  // Specify Encoding property setting it to FileEncoding.None
  fileSpecification.setEncoding(FileEncoding.None);
  // add attachment to document's attachment collection
  pdfDocument.getEmbeddedFiles().add(fileSpecification);
  // save new output
  pdfDocument.save("output.pdf");
    }
```
