---
title: Set Viewer Preference of an existing PDF File - facades
type: docs
weight: 20
url: /java/set-viewer-preference/
description: This section explains how to set viewer Preference with Aspose.PDF Facades using PdfViewer Class.
lastmod: "2021-06-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

The [ViewerPreference](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/ViewerPreference) class represents display modes of PDF files; for example, positioning the document window in the center of the screen, hiding viewer application’s menu bar etc. [changeViewerPreference(..)](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfContentEditor#changeViewerPreference-int-) method in [PdfContentEditor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfContentEditor) class allows you to change the viewer preference. In order to do that, you need to create an object of [PdfContentEditor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfContentEditor) class and bind the input PDF file using [bindPdf(..)](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/Facade#bindPdf-com.aspose.pdf.IDocument-) method. Ater that, you can call [changeViewerPreference(..)](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfContentEditor#changeViewerPreference-int-) method to set any preferences. Finally, you have to save the updated PDF file using [save(..)](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/SaveableFacade#save-java.io.OutputStream-) method.

The following code snippet shows you how to change viewer preference in an existing PDF file.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Document-SetViewerPreferenceOfAnExistingPDFFile-.java" >}}