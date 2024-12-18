---
title: Convert JPG to PDF 
linktitle: Convert JPG to PDF 
type: docs
weight: 190
url: /androidjava/convert-jpg-to-pdf/
lastmod: "2021-06-05"
description: Learn how to easily convert a JPG images to PDF file. Also, you can convert an image to PDF with the same height and width of the page.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

No need to wonder how to convert JPG to PDF, because Apose.PDF for Android via Java library has best decision.

You can very easy convert a JPG images to PDF with Aspose.PDF for Android via Java by following steps:

1. Initialize object of [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) class
1. Load JPG image and add to paragraph
1. Save output PDF

The code snippet below shows how to convert JPG Image to PDF:

```java
public void convertJPEGtoPDF () {
        // Initialize document object
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/sample.jpg");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Load sample JPEG image file
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "JPEG-to-PDF.pdf");

        // Save output document
        try {
            document.save(pdfFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```