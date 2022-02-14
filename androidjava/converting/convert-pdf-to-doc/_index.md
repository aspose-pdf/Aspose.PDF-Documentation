---
title: Convert PDF to DOC 
linktitle: Convert PDF to DOC
type: docs
weight: 70
url: /androidjava/convert-pdf-to-doc/
lastmod: "2021-06-05"
description: Convert PDF file to DOC format with ease and full control with Aspose.PDF for Android via Java. Learn more how to tune up Microsoft Word Doc file to PDF conversion.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

One of the most popular feature is PDF to Microsoft Word DOC conversion, which makes the content easy to manipulate. Aspose.PDF for Android via Java allows you to convert PDF files to DOC.

**Aspose.PDF for Android via Java** can create PDF documents from scratch and is a great toolkit for updating, editing and manipulating existing PDF documents. An important feature is the ability to convert pages and entire PDF documents to images. Another popular feature is PDF to Microsoft Word DOC conversion, which makes the content easy to manipulate. (Most users can’t edit PDF documents but can easily work with tables, text, and images in Microsoft Word.)

To make things simple and understandable, Aspose.PDF for Android via Java provides a two-line code for transforming a source PDF file into a DOC file.

{{% alert color="primary" %}}

Try online. You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/conversion/pdf-to-doc](https://products.aspose.app/pdf/conversion/pdf-to-doc)

{{% /alert %}}

The following code snippet shows the process of converting a PDF file into DOC format.

```java
 public void convertPDFtoDOC() {
        // Open the source PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File docFileName = new File(fileStorage, "PDF-to-Word.doc");

        try {
            // Save the file into MS document format
            document.save(docFileName.toString(), SaveFormat.Doc);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

