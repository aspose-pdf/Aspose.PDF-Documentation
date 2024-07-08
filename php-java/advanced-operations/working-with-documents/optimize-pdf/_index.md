---
title: Optimize, Compress or Reduce PDF Size in PHP
linktitle: Optimize PDF Document
type: docs
weight: 40
url: /php-java/optimize-pdf/
description: Optimize PDF file, shrink all images, reduce size PDF, Unembed fonts, Remove unused objects using PHP.
lastmod: "2024-06-05"
---

A PDF document can sometimes contain additional data. Reducing the size of a PDF file will help you optimize network transfer and storage. This is especially handy for publishing on web pages, sharing on social networks, sending by e-mail, or archiving in storage. We can use several techniques to optimize PDF:

- Optimize page content for online browsing
- Shrink or compress all images
- Enable reusing page content
- Merge duplicate streams
- Unembed fonts
- Remove unused objects
- Remove flattening form fields
- Remove or flatten annotations

## Optimize PDF Document for the Web

Optimization or linearization refers to the process of making a PDF file suitable for online browsing using a web browser. Aspose.PDF supports this process.

To optimize a PDF for web display:

1. Open the input document in a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object.
1. Use the [optimize()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#optimize--) method.
1. Save the optimized document using the save(..) method.

The following code snippet shows how to optimize a PDF document for the web.

```php

    // Open document
    $document = new Document($inputFile);

    // Optimize for web
    $document->optimize();

    // Save the updated document
    $document->save($outputFile);
    $document->close();
```

## Reduce PDF File Size

This topic explains the steps to optimize/reduce the PDF file size. Aspose.PDF API provides the [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.optimization/class-use/OptimizationOptions) class that gives the flexibility to optimize output PDF by removing unnecessary objects and compressing PDF files having images. Both these options are elaborated in the following sections.

### Remove Unnecessary Objects

We can optimize the size of PDF documents by removing duplicate and unused objects. The following code snippet shows how.

```php

    // Open document
    $document = new Document($inputFile);
    
    // Optimize PDF document. Note, though, that this method cannot guarantee
    // document shrinking
    $document->optimizeResources();

    // Save the updated document
    $document->save($outputFile);
    $document->close();

```

## Shrinking or Compressing All Images

If the source PDF file contains images, consider compressing the images and setting their quality. In order to enable image compression, pass true as an argument to the setCompressImages(..) method. All the images in a document will be re-compressed. The compression is defined by the setImageQuality(..) method, which is the value of the quality in percent. 100% is unchanged quality and image size. To decrease image size, pass an argument of less than 100 to the setImageQuality(..) method.

```php

    // Open document
    $document = new Document($inputFile);
    
    // Initialize OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    // Set CompressImages option
    $optimizationOptions->getImageCompressionOptions()->setCompressImages(true);

    // Set ImageQuality option
    $optimizationOptions->getImageCompressionOptions()->setImageQuality(50);

    // Optimize PDF document using OptimizationOptions
    $document->optimizeResources($optimizationOptions);

    // Save the updated document
    $document->save($outputFile);
    $document->close();
```

Another way is to resize the images with a lower resolution. In this case, we should set ResizeImages to true and MaxResolution to the appropriate value.

```php

    // Open document
    $document = new Document($inputFile);
    
    // Initialize OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    // Set CompressImages option
    $optimizationOptions->getImageCompressionOptions()->setCompressImages(true);
    
    // Set ImageQuality option
    $optimizationOptions->getImageCompressionOptions()->setImageQuality(75);

    // Set ResizeImage option
    $optimizationOptions->getImageCompressionOptions()->setResizeImages(true);

    // Set MaxResolution option
    $optimizationOptions->getImageCompressionOptions()->setMaxResolution(300);

    // Save the updated document
    $document->save($outputFile);
    $document->close();
```

Another important issue is the execution time. But again, we can manage this setting too. Currently, we can use two algorithms - Standard and Fast. To control the execution time we should set a Version property. The following snippet demonstrates the Fast algorithm:

```php
    // Open document
    $document = new Document($inputFile);
    
    // Initialize OptimizationOptions
    $optimizationOptions = new optimization_OptimizationOptions();

    // Set CompressImages option
    $optimizationOptions->getImageCompressionOptions()->setCompressImages(true);

    // Set ImageQuality option
    $optimizationOptions->getImageCompressionOptions()->setImageQuality(75);
    $optimization_ImageCompressionVersion = new optimization_ImageCompressionVersion();

    // Set Image Compression Version to fast
    $optimizationOptions->getImageCompressionOptions()->setVersion($optimization_ImageCompressionVersion->Fast);

    // Optimize PDF document using OptimizationOptions
    $document->optimizeResources($optimizationOptions);

    // Save the updated document
    $document->save($outputFile);
    $document->close();
```

## Removing Unused Objects

A PDF document sometimes contains the PDF objects that are not referenced from any other object in the document. This may happen, for example, when a page is removed from the document page tree but the page object itself isn't removed. Removing these objects doesn't make the document invalid but rather shrinks it.

```php

    // Open document
    $document = new Document($inputFile);
    
    // Initialize OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setRemoveUnusedObjects(true);

    // Optimize PDF document using OptimizationOptions
    $document->optimizeResources($optimizationOptions);

    // Save the updated document
    $document->save($outputFile);
    $document->close();
```

## Removing Unused Streams

Sometimes a document contains unused resource streams. These streams are not “unused objects” because they are referenced from a page's resource dictionary. This may happen in cases where an image has been removed from the page but not from the page resources. Also, this situation often occurs when pages are extracted from the document and document pages have “common” resources, that is, the same Resources object. Page contents are analyzed in order to determine if a resource stream is used or not. Unused streams are removed. Sometimes this decreases the document size.

```php

    // Open document
    $document = new Document($inputFile);
    
    // Initialize OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setRemoveUnusedStreams(true);

    // Optimize PDF document using OptimizationOptions
    $document->optimizeResources($optimizationOptions);

    // Save the updated document
    $document->save($outputFile);
    $document->close();
```

## Linking Duplicate Streams

Sometimes a document contains several identical resource streams (for example images). This may happen for example when a document is concatenated with itself. The output document contains two independent copies of the same resource stream. We analyze all resource streams and compare them. If streams are duplicated they are merged, that is, only one copy is left, references are changed appropriately and copies of the object are removed. Sometimes this decreases the document size.

```php
    // Open document
    $document = new Document($inputFile);
    
    // Initialize OptimizationOptions
    $optimizationOptions = new OptimizationOptions();
    
    $optimizationOptions->setLinkDuplcateStreams(true);
    
    // Optimize PDF document using OptimizationOptions
    $document->optimizeResources($optimizationOptions);

    // Save the updated document
    $document->save($outputFile);
    $document->close();
```

Additionally, we can use AllowReusePageContent settings. If this property is set to true, the page content will be reused when optimizing the document for identical pages.

```php
    // Open document
    $document = new Document($inputFile);
    
    // Initialize OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setAllowReusePageContent(true);

    // Optimize PDF document using OptimizationOptions
    $document->optimizeResources($optimizationOptions);

    // Save the updated document
    $document->save($outputFile);
    $document->close();
```

## Unembedding Fonts

If the document uses embedded fonts it means that all font data is placed in the document. The advantage is that the document is viewable regardless of whether the font is installed on the user's machine or not. But embedding fonts makes the document larger. The unembed fonts method removes all embedded fonts. This decreases the document size but the document may become unreadable if the correct font is not installed.

```php

    // Open document
    $document = new Document($inputFile);
    
    // Initialize OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setUnembedFonts(true);

    // Optimize PDF document using OptimizationOptions
    $document->optimizeResources($optimizationOptions);

    // Save the updated document
    $document->save($outputFile);
    $document->close();
```

## Removing or Flattening Annotations

Annotations can be deleted when they are unnecessary. When they are needed but do not require additional editing, they can be flattened. Both of these techniques will reduce the file size.

```php

    // Open document
    $document = new Document($inputFile);
    $pages = $document->getPages();

    for ($i=1; $i < $pages->size() ; $i++) { 
        $page = $pages->get_Item($i);
        $annotations = $page->getAnnotations();
        for ($idx=0; $idx < $annotations->size(); $idx++) { 
            $annotation = $annotations->get_Item($idx);
            $annotation->flatten();
        }
    }
     
    // Save the updated document
    $document->save($outputFile);
    $document->close();
```

## Removing Form Fields

If the PDF document contains AcroForms, we can try to reduce the file size by flattening form fields.

```php

    // Open document
    $document = new Document($inputFile);
    
    // Flatten Forms
    $fields = $document->getForm()->getFields();
    foreach ($fields as $field) {
        $field->flatten();
    }            

    // Save the updated document
    $document->save($outputFile);
    $document->close();
```

## Convert a PDF from RGB colorspace to grayscale

A PDF file is comprised of Text, Image, Attachment, Annotations, Graphs and other objects. You may come across a requirement to convert a PDF from RGB colorspace to Grayscale so that it would be faster while printing those PDF files. Also when the file is converted to Grayscale, the size of the document is also reduced but with this change, the quality of the document may drop. Currently, this feature is supported by the Pre-Flight feature of Adobe Acrobat, but when talking about Office automation, Aspose.PDF is an ultimate solution to provide such leverages for document manipulation.

In order to accomplish this requirement, the following code snippet can be used.

```php

    // Open document
    $document = new Document($inputFile);
    
    $strategy = new RgbToDeviceGrayConversionStrategy();
    for ($idxPage = 1; $idxPage <= $document->getPages()->size(); $idxPage++) {
        $page = $document->getPages()->get_Item($idxPage);
        $strategy->convert($page);
    }          

    // Save the updated document
    $document->save($outputFile);
    $document->close();
```

## FlateDecode Compression

Aspose.PDF for PHP via Java provides support of FlateDecode compression for PDF Optimisation functionality. The following code snippet below shows how to use the option in Optimization to store images with FlateDecode compression:

```php

    // Open document
    $document = new Document($inputFile);

    // Initialize OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setUnembedFonts(true);

    // Optimize PDF document using OptimizationOptions
    $optimizationOptions->getImageCompressionOptions()->setEncoding(optimization_ImageEncoding::$Flate);

    // Save the updated document
    $document->save($outputFile);
    $document->close();
```

## Store Image in XImageCollection

Aspose.PDF for PHP via Java provides the ability to store new images into [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/XImageCollection) with FlateDecode compression. To enable this option you can use ImageFilterType.Flate flag. The following code snippet shows how to use this functionality:

```php
    // Open document
    $document = new Document($inputFile);

    // Initialize Document
    $page = $document->getPages()->get_Item(1);

    // Load image into stream
    $imageStream = new java("java.io.FileInputStream",$inputFile);
    $imageFilterType = new ImageFilterType();
    $page->getResources()->getImages()->add($imageStream, $imageFilterType->Flate);
    $idx = $page->getResources()->getImages()->size();
    $ximage = $page->getResources()->getImages()->get_Item($idx);
    $page->getContents()->add(new operators_GSave());

    // Set coordinates
    $lowerLeftX = 0;
    $lowerLeftY = 0;
    $upperRightX = 600;
    $upperRightY = 600;
    $rectangle = new Rectangle($lowerLeftX, $lowerLeftY, $upperRightX, $upperRightY);
    $matrixData = [
        $rectangle->getURX() - $rectangle->getLLX(), 0, 
        0, $rectangle->getURY() - $rectangle->getLLY(), 
        $rectangle->getLLX(), $rectangle->getLLY()];
    $matrix = new Matrix($matrixData);

    // Using ConcatenateMatrix (concatenate matrix) operator: defines how image must be placed
    $page->getContents()->add(new operators_ConcatenateMatrix($matrix));
    $page->getContents()->add(new operators_Do($ximage->getName()));
    $page->getContents()->add(new operators_GRestore());

    // Save the updated document
    $document->save($outputFile);
    $document->close();
```
