---
title: Convert PDF to PowerPoint 
linktitle: Convert PDF to PowerPoint
type: docs
weight: 110
url: /androidjava/convert-pdf-to-powerpoint/
description: Aspose.PDF allows you to convert PDF to PowerPoint format. One way there is a possibility to convert PDF to PPTX with Slides as Images. 
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

We have an API named Aspose.Slides which offers the feature to create as well as manipulate PPT/PPTX presentations. This API also provides the feature to convert PPT/PPTX files to PDF format. In Aspose.PDF for Java, we have introduced a feature to transform PDF documents into PPTX format. During this conversion, the individual pages of the PDF file are converted to separate slides in the PPTX file.

{{% alert color="primary" %}}

Try online. You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/conversion/pdf-to-pptx](https://products.aspose.app/pdf/conversion/pdf-to-pptx)

{{% /alert %}}

During PDF to PPTX conversion, the text is rendered as Text where you can select/update it, instead of its rendered as an image. Please note that in order to convert PDF files to PPTX format, Aspose.PDF provides a class named PptxSaveOptions. An object of the [PptxSaveOptions](https://apireference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) class is passed as a second argument to the [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..) method.

Check next code snippet to resolve your tasks with conversion PDF to PowerPoint format:

```java
 public void convertPDFtoPowerPoint() {
        // Load PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        PptxSaveOptions pptxSaveOptions = new PptxSaveOptions();


        // Save the output in PPTX
        File xlsFileName = new File(fileStorage, "PDF-to-Powerpoint.pptx");
        try {
            // Save the file into PPTX format
            document.save(xlsFileName.toString(), pptxSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```
