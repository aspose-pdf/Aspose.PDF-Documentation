---
title: Working with Facades
type: docs
weight: 112
url: /java/working-with-facades/
description: This section explains how to work with Aspose.PDF Facades - a toolset for popular operations with PDF.
lastmod: "2021-05-28"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## <ins>**Get PDF file information - facades**
In order to get information specific to PDF file, you need to create an object of [PdfFileInfo](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfFileInfo) class. After that, you can get values of the individual properties like Subject, Title, Keywords and Creator etc.

The following code snippet shows you how to get PDF file information.



{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Document-GetPDFFilenformation-.java" >}}
## <ins>**Set PDF file information - facades**
[PdfFileInfo](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfFileInfo) class allows you to set file specific information of a PDF document. You need to create an object of [PdfFileInfo](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfFileInfo) class and then set different file specific properties like Author, Title, Keyword, and Creator etc. Finally, save the updated PDF file using [saveNewInfo(..)](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfFileInfo#saveNewInfo-java.io.OutputStream-) method of the [PdfFileInfo](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfFileInfo) object.

The following code snippet shows you how to set PDF file information.



{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Document-SetPDFFileInformation-.java" >}}