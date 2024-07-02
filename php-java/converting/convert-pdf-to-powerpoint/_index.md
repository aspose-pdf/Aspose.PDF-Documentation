---
title: Convert PDF to Microsoft PowerPoint 
linktitle: Convert PDF to PowerPoint
type: docs
weight: 30
url: /php-java/convert-pdf-to-powerpoint/
lastmod: "2024-05-20"
description: Aspose.PDF allows you to convert PDF to PowerPoint format using PHP. One way there is a possibility to convert PDF to PPTX with Slides as Images.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF for PHP** lets you track the progress of PDF to PPTX conversion.
We have an API named Aspose.Slides which offers the feature to create as well as manipulate PPT/PPTX presentations. This API also provides the feature to convert PPT/PPTX files to PDF format. In Aspose.PDF for PHP, we have introduced a feature to transform PDF documents into PPTX format. During this conversion, the individual pages of the PDF file are converted to separate slides in the PPTX file.

During PDF to PPTX conversion, the text is rendered as Text where you can select/update it, instead of its rendered as an image. Please note that in order to convert PDF files to PPTX format, Aspose.PDF provides a class named PptxSaveOptions. An object of the [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) class is passed as a second argument to the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..) method.

Check next code snippet to resolve your tasks with conversion PDF to PowerPoint format:

```php
// Load the input PDF document
$document = new Document($inputFile);

// Create an instance of PptxSaveOptions
$saveOption = new PptxSaveOptions();

// Save the PDF document as a PPTX file
$document->save($outputFile, $saveOption);
```

## Convert PDF to PPTX with Slides as Images

In case if you need to convert a searchable PDF to PPTX as images instead of selectable text, Aspose.PDF provides such a feature via [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) class. To achieve this, set property SlidesAsImages  of [PptxSaveOptios](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) class to 'true' as shown in the following code sample.

The following code snippet shows the process for converting PDF files into PPTX format Slides as Images. 

```php
// Load the input PDF document
$document = new Document($inputFile);

// Create an instance of PptxSaveOptions
$saveOption = new PptxSaveOptions();
$saveOption->setSlidesAsImages(true);

// Save the PDF document as a PPTX file
$document->save($outputFile, $saveOption);

    public static void ConvertPDFtoPPTX_SlideAsImages() {
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "PDFToPPTX.pdf").toString();
        String pptxDocumentFileName = Paths.get(_dataDir.toString(), "PDFToPPTX_out.pptx").toString();

        // Load PDF document
        Document doc = new Document(pdfDocumentFileName);
        // Instantiate PptxSaveOptions instance
        PptxSaveOptions pptx_save = new PptxSaveOptions();
        // Save the output in PPTX format
        pptx_save.setSlidesAsImages(true);

        doc.save(pptxDocumentFileName, pptx_save);
    }
```

{{% alert color="success" %}}
**Try to convert PDF to PowerPoint online**

Aspose.PDF for PHP presents you online free application ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to PPTX with Free App](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}
