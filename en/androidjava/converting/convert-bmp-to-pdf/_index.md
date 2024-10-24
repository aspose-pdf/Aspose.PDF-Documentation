---
title: Convert BMP to PDF 
linktitle: Convert BMP to PDF
type: docs
weight: 220
url: /androidjava/convert-bmp-to-pdf/
lastmod: "2021-06-05"
description: You may easily convert BMP bitmap files to PDF used to store digital bitmap images separately from the display device using Aspose.PDF. for Android via Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

BMP images are Files having extension .BMP represent Bitmap Image files that are used to store bitmap digital images. These images are independent of graphics adapter and are also called device independent bitmap (DIB) file format.
You can convert BMP to PDF with Aspose.PDF for Java API. Therefore, you can follow the following steps to convert BMP images:

1. Initialize a new Document
1. Load sample BMP image file
1. Finally, save the output PDF file

So the following code snippet follows these steps and shows how to convert BMP to PDF using Java:

```java
public void convertBMPtoPDF () {
        // Initialize document object
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/sample.bmp");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Load sample BMP image file
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "BMP-to-PDF.pdf");

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
