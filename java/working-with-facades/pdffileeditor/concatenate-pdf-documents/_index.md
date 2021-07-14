---
title: Concatenate PDF documents
type: docs
weight: 10
url: /java/concatenate-pdf-documents/
description: This section explains how to concatenate PDF documents with Aspose.PDF Facades using PdfFileEditor class.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Concatenate PDF Files Using File Paths (Facades)

concatenate method of [**PdfFileEditor**](http://www.aspose.com/api/java/pdf/com.aspose.pdf.facades/classes/PdfFileEditor) class can be used to concatenate two PDF files. The concatenate method allows you to pass three parameters: first input PDF, second input PDF, and output PDF. The final output PDF contains both the input PDF files.

The following code snippet shows you how to concatenate PDF files using file paths.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Pages-ConcatenatePDFFilesUsingFilePaths-.java" >}}

In some cases, when there are a lot of outlines, users may disable them with setting **CopyOutlines** to false and improve performance of concatenation.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Pages-ConcatenatePDFFilesUsingFilePaths-SettingCopyOutlines.java" >}}

## Concatenate Array of PDF Files Using File Paths (Facades)

If you want to concatenate multiple PDF files, you can use the overload of the concatenate method, which allows you to pass an array of PDF files path. The final output is saved as a merged file created from all the files in the array.

The following code snippet shows you how to concatenate array of PDF files using file paths.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Pages-ConcatenateArrayOfPDFFilesUsingFilePaths-.java" >}}

## Concatenate Array of PDF Files Using Streams (Facades)

{{% alert color="primary" %}}

Concatenating an array of PDF files is not limited to only files residing on the disk. You can also concatenate an array of PDF files from streams. If you want to concatenate multiple PDF files, you can use the appropriate overload of the Concatenate method. First, you need to create an array of input streams and one stream for output PDF and then call the Concatenate method. The output will be saved in the output stream.

{{% /alert %}}

The following code snippet shows you how to concatenate array of PDF files using streams.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Pages-ConcatenateArrayOfPDFFilesUsingStreams-.java" >}}
