---
title: Convert DICOM to PDF 
linktitle: Convert DICOM to PDF
type: docs
weight: 250
url: /androidjava/convert-dicom-to-pdf/
lastmod: "2021-06-05"
description: Convert medical images saved in DICOM format to a PDF file using Aspose.PDF for Android via Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> is a standard for handling, storing, printing, and transmitting information in medical imaging. It includes a file format definition and a network communications protocol.

Aspsoe.PDF for Java allows you to convert DICOM files to PDF format, check next code snippet:

1. Load image into stream
1. Initialize [`Document object`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)
1. Load sample DICOM image file
1. Save output PDF document

```java
//    Convert DICOM to PDF
    public void convertDICOMtoPDF () {
        // Initialize document object
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/bmode.dcm");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Load sample BMP image file
        image.setImageStream(inputStream);
        image.setFileType(ImageFileType.Dicom);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "DICOM-to-PDF.pdf");

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
