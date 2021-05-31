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


## <ins>**Print PDF file to default printer (facades)**
The [PdfViewer](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfViewer) class allows you to print a PDF file to the default printer. Therefore you need to create a [PdfViewer](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfViewer) object and open the PDF using the openPdfFile(..) method.

Call the printDocument(..) method to print the PDF to the default printer.

The following code snippet shows how to print PDF to the default printer with printer and page Settings.



{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-PDFPrinting-PrintPDFFileToDefaultPrinter-.java" >}}


## <ins>**Set Viewer Preference of an existing PDF File - facades**
The [ViewerPreference](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/ViewerPreference) class represents display modes of PDF files; for example, positioning the document window in the center of the screen, hiding viewer application’s menu bar etc. [changeViewerPreference(..)](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfContentEditor#changeViewerPreference-int-) method in [PdfContentEditor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfContentEditor) class allows you to change the viewer preference. In order to do that, you need to create an object of [PdfContentEditor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfContentEditor) class and bind the input PDF file using [bindPdf(..)](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/Facade#bindPdf-com.aspose.pdf.IDocument-) method. Ater that, you can call [changeViewerPreference(..)](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfContentEditor#changeViewerPreference-int-) method to set any preferences. Finally, you have to save the updated PDF file using [save(..)](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/SaveableFacade#save-java.io.OutputStream-) method.

The following code snippet shows you how to change viewer preference in an existing PDF file.



{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Document-SetViewerPreferenceOfAnExistingPDFFile-.java" >}}