---
title: Convert various Images formats to PDF 
linktitle: Convert Images to PDF
type: docs
weight: 60
url: /php-java/convert-images-format-to-pdf/
lastmod: "2024-05-20"
description: This topic show you how to Aspose.PDF for PHP library allows to convert various images formats to PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF for PHP**  allows you to convert different formats of images to PDF files. Our library demonstrates code snippets for converting the most popular image formats, such as - BMP, CGM, DICOM, JPG, PNG, SVG and TIFF formats.

## Convert BMP to PDF

Convert BMP files to PDF document using **Aspose.PDF for PHP** library.

<abbr title="Bitmap Image File">BMP</abbr> images are Files having extension .BMP represent Bitmap Image files that are used to store bitmap digital images. These images are independent of graphics adapter and are also called device independent bitmap (DIB) file format.
You can convert BMP to PDF with Aspose.PDF for PHP API. Therefore, you can follow the following steps to convert BMP images:

1. Create a new Document object
1. Add a new page to the document
1. Set the margins of the page to 0 (if needed)
1. Create a new Image object and set the input BMP file
1. Add the image to the page
1. Save the document to the output PDF file

So the following code snippet follows these steps and shows how to convert BMP to PDF using PHP:

```php
// Create a new Document object
$document = new Document();

// Add a new page to the document
$page = $document->getPages()->add();

// Set the margins of the page to 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// Create a new Image object and set the input BMP file
$image = new Image();
$image->setFile($inputFile);

// Add the image to the page
$page->getParagraphs()->add($image);

// Save the document to the output PDF file
$document->save($outputFile);
```

## Convert CGM to PDF

<abbr title="Computer Graphics Metafile">CGM</abbr> is an ISO standard that provides a vector-based 2D image file format for the storage and retrieval of graphics information. CGM is a device-independent format. CGM is a vector graphics format that supports three different encoding methods: binary (best for program read speed), character-based (produces the smallest file size and allows for faster data transfers) or cleartext encoding (allows users to read and modify the file with a text editor)

The following code snippet shows you how to convert CGM files to PDF format using Aspose.PDF for PHP.

1. Create an instance of [CgmLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/cgmloadoptions/) to specify any specific options for loading the CGM file
1. Create an instance of [Document](https://reference.aspose.com/page/java/com.aspose.page/Document) class with mention source filename and options.
1. Save the document with the desired file name.

```php
$options = new CgmLoadOptions();

// Create a Document object and load the CGM file using the specified options
$document = new Document($inputFile, $options);

// Save the document as a PDF file
$document->save($outputFile);
```

## Convert DICOM to PDF

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> is a standard for handling, storing, printing, and transmitting information in medical imaging. It includes a file format definition and a network communications protocol.

Aspsoe.PDF for PHP allows you to convert DICOM files to PDF format, check next code snippet:

1. Create a new Document object
1. Add a new page to the document
1. Set the margins of the page to 0 (if needed)
1. Create a new Image object and set the input BMP file
1. Set the DICOM file as the source file for the image
1. Set the file type of the image to DICOM
1. Add the image to the page
1. Save the document to the output PDF file

```php
// Create a new Document object
$document = new Document();

// Add a new page to the document
$page = $document->getPages()->add();

// Set the margins of the page to 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// Create a new Image object
$image = new Image();

// Set the DICOM file as the source file for the image
$image->setFile($inputFile);

// Set the file type of the image to DICOM
$image->setFileType(ImageFileType::$Dicom);

// Add the image to the page
$page->getParagraphs()->add($image);

// Save the document as a PDF file
$document->save($outputFile);
```

{{% alert color="success" %}}
**Try to convert DICOM to PDF online**

Aspose presents you online free application ["DICOM to PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion DICOM to PDF using Free App](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## Convert EMF to PDF

Enhanced metafile format (<abbr title="Enhanced metafile format">EMF</abbr>) stores graphical images device-independently. Metafiles of EMF comprises of variable-length records in chronological order that can render the stored image after parsing on any output device.

We have several approaches to convert EMF into PDF.

## Using Image class

A PDF document comprises pages and each page contains one or more paragraph objects. A paragraph can be a text, image, table, floating box, graph, heading, form field or an attachment.
To convert an image file into PDF format, enclose it in a paragraph.

It is possible to convert images at a physical location on the local hard
drive, found at a web URL or in a Stream instance.

To add an image:

1. Create an object of the com.aspose.pdf.Image class.
1. Add the image to a [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/paragraphs) collection of page instance.
1. Specify the path or source of Image.
    - If an image is at a location on the hard drive, specify the path location using the [Image.setFile(…)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image) method.
    - If an image is placed in a FileInputStream, pass the object holding the image to the [Image.setImageStream(…)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image) method.

The following code snippet shows how to load an image object, set the page margin, place the image on page and save the output as PDF.

```php
$inputFile = "sample.emf";

// Create a new Document object
$document = new Document();

// Add a new page to the document
$page = $document->getPages()->add();

// Set the margins of the page to 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// Create a new Image object and set the input file
$image = new Image();
$image->setFile($inputFile);

// Add the image to the page
$page->getParagraphs()->add($image);

// Save the document as a PDF file
$document->save($outputFile);
```

## Convert JPG to PDF

No need to wonder how to convert JPG to PDF, because Apose.PDF for PHP library has best decision.

You can very easy convert a JPG images to PDF with Aspose.PDF for PHP by following steps:

1. Initialize object of [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) class
1. Add a new page to the document
1. Set the margins of the page to 0
1. Create a new Image object and set the input file
1. Save output PDF

The code snippet below shows how to convert JPG Image to PDF using PHP:

```php
$inputFile = "sample.jpg";

// Create a new Document object
$document = new Document();

// Add a new page to the document
$page = $document->getPages()->add();

// Set the margins of the page to 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// Create a new Image object and set the input file
$image = new Image();
$image->setFile($inputFile);

// Add the image to the page
$page->getParagraphs()->add($image);

// Save the document as a PDF file
$document->save($outputFile);
```

{{% alert color="success" %}}
**Try to convert JPG to PDF online**

Aspose presents you online free application ["JPG to PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion JPG to PDF using Free App](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## Convert PNG to PDF

**Aspose.PDF for PHP** support feature to convert PNG images to PDF format. Check the next code snippet for realizing you task.

<abbr title="Portable Network Graphics">PNG</abbr> refers to a type of raster image file format that use loseless compression, that makes it popular among its users.

You can convert PNG to PDF image using the below steps:

1. Initialize object of [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) class
1. Add a new page to the document
1. Set the margins of the page to 0
1. Create a new Image object and set the input file
1. Save output PDF

Moreover, the code snippet below shows how to convert PNG to PDF in your PHP applications:

```php
$inputFile = "sample.png";

// Create a new Document object
$document = new Document();

// Add a new page to the document
$page = $document->getPages()->add();

// Set the margins of the page to 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// Create a new Image object and set the input file
$image = new Image();
$image->setFile($inputFile);

// Add the image to the page
$page->getParagraphs()->add($image);

// Save the document as a PDF file
$document->save($outputFile);
```

{{% alert color="success" %}}
**Try to convert PNG to PDF online**

Aspose presents you online free application ["PNG to PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PNG to PDF using Free App](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## Convert SVG to PDF

Scalable Vector Graphics (SVG) is a family of specifications of an XML-based file format for two-dimensional vector graphics, both static and dynamic (interactive or animated). The SVG specification is an open standard that has been under development by the World Wide Web Consortium (W3C) since 1999.

SVG images and their behaviors are defined in XML text files. This means that they can be searched, indexed, scripted and, if required, compressed. As XML files, SVG images can be created and edited with any text editor, but it is often more convenient to create them with drawing programs such as Inkscape

## How to convert SVG file to PDF format

To convert SVG files to PDF, use the class named [SvgLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgloadoptions) which is used to initialize the [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions) object. Later, this object is passed as an argument during the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) object initialization and helps the PDF rendering engine to determine the input format of the source document.

The following code snippet shows the process of converting SVG file into PDF format.

```php
// Create a new SvgLoadOptions object
$loadOption = new SvgLoadOptions();

// Create a new Document object and load the SVG file
$document = new Document($inputFile, $loadOption);

// Save the document as a PDF file
$document->save($outputFile);
```

{{% alert color="success" %}}
**Try to convert SVG format to PDF online**

Aspose.PDF for PHP presents you online free application ["SVG to PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion SVG to PDF with Free App](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

## Convert TIFF to PDF

**Aspose.PDF for PHP** file format supported, be it a single frame or multi-frame <abbr title="Tag Image File Format">TIFF</abbr> image. It means that you can convert the TIFF image to PDF in your Java applications.

TIFF or TIF, Tagged Image File Format, represents raster images that are meant for usage on a variety of devices that comply with this file format standard. TIFF image can contain several frames with different images. Aspose.PDF file format is also supported, be it a single frame or multi-frame TIFF image. So you can convert the TIFF image to PDF in your Java applications. Therefore, we will consider an example of converting multi-page TIFF image to multi-page PDF document with below steps:

1. Create a new Document object
1. Add a new page to the document
1. Set the margins of the page to 0
1. Create a new Image object
1. Set the file path of the input TIFF image
1. Add the image to the page
1. Save the document as a PDF file

Moreover, the following code snippet shows how to convert multi-page or multi-frame TIFF image to PDF:

```php
// Create a new Document object
$document = new Document();

// Add a new page to the document
$page = $document->getPages()->add();

// Set the margins of the page to 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// Create a new Image object
$image = new Image();

// Set the file path of the input TIFF image
$image->setFile($inputFile);

// Add the image to the page
$page->getParagraphs()->add($image);

// Save the document as a PDF file
$document->save($outputFile);
```
