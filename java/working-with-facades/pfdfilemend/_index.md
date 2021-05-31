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

## <ins>**Add Text in an Existing PDF File (facades)**
You can use addText method of the [PdfFileMend](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfFileMend) class to add text in an existing PDF file. Before that, you need to create a [PdfFileMend](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfFileMend) object and bind an input file using bindPdf mehtod. After this create a [FormattedText](http://www.aspose.com/api/java/pdf/com.aspose.pdf.facades/classes/FormattedText) object, which contains the text and the formatting information. Then you need to save the updated PDF file using save method after adding formatted text to PDF file using addText method. The following code snippet shows you how to add text in the PDF file.



{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Text-AddTextInAnExistingPDFFile-.java" >}}