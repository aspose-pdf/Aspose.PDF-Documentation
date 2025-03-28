---
title: Optimize, Compress or Reduce PDF Size in Python
linktitle: Optimize PDF
type: docs
weight: 30
url: /python-net/optimize-pdf/
description: Learn how to optimize PDF documents in Python for improved web performance and reduced file size using Aspose.PDF.
lastmod: "2025-02-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Compress PDF pages using Python
Abstract: This article provides a comprehensive guide on optimizing PDF files to reduce their size and enhance performance across various platforms, such as web pages, emails, and storage systems. The optimization techniques include reducing image sizes, removing unused resources, and unembedding fonts. Specific methods for optimizing PDFs for the web and reducing overall file size are discussed, utilizing the `Optimize` and `OptimizeResources` methods in Aspose.PDF for Python. Customization of optimization strategies is possible via `OptimizationOptions`, allowing for targeted actions like compressing images, removing unused objects and streams, linking duplicate streams, and unembedding fonts. Additional strategies cover flattening annotations, removing form fields, and converting PDF files from RGB to grayscale to further decrease size. The article also highlights the use of FlateDecode compression for image optimization, ensuring effective PDF file management while maintaining quality and functionality.
---

A PDF document may sometimes contain additional data. Reducing the size of a PDF file will help you optimize network transfer and storage. This is especially handy for publishing on web pages, sharing on social networks, sending by e-mail, or archiving in storage. We can use several techniques to optimize PDF:

- Optimize page content for online browsing
- Shrink or compress all images
- Enable reusing page content
- Merge duplicate streams
- Unembed fonts
- Remove unused objects
- Remove flattening form fields
- Remove or flatten annotations

{{% alert color="primary" %}}

 Detailed explanation of optimization methods can be found in the Optimization Methods Overview page.

{{% /alert %}}

## Optimize PDF Document for the Web

Optimization, or linearization for Web, refers to the process of making a PDF file suitable for online browsing using a web browser. To optimize a file for web display:

1. Open the input document in an [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) object.
1. Use the [Optimize](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method.
1. Save the optimized document using the [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method.

The following code snippet shows how to optimize a PDF document for the web.

```python

    import aspose.pdf as ap

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    document.optimize()
    document.save(path_outfile)
```

## Reduce Size PDF

The [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method allows you to reduce the document size by weeding out the unnecessary information. By default, this method works as follows:

- Resources that are not used on the document pages are removed
- Equal resources are joined into one object
- Unused objects are deleted

The snippet below is an example. Note, though, that this method cannot guarantee document shrinking.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Optimize PDF document. Note, though, that this method cannot guarantee document shrinking
    document.optimize_resources()
    # Save updated document
    document.save(output_pdf)
```

## Optimization Strategy Management

We can also customize the optimization strategy. Currently, the [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method uses 5 techniques. These techniques can be applied using the OptimizeResources() method with the [OptimizationOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/optimizationoptions/) parameter.

### Shrinking or Compressing All Images

We have two ways to work with images: reduce image quality and/or change their resolution. In any case, [ImageCompressionOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/imagecompressionoptions/) should be applied. In the following example, we shrink images by reducing ImageQuality to 50.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Initialize OptimizationOptions
    optimizeOptions = ap.optimization.OptimizationOptions()
    # Set CompressImages option
    optimizeOptions.image_compression_options.compress_images = True
    # Set ImageQuality option
    optimizeOptions.image_compression_options.image_quality = 50
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
```

### Removing Unused Objects

A PDF document sometimes contains the PDF objects that are not referenced from any other object in the document. This may happen, for example, when a page is removed from the document page tree but the page object itself isn’t removed. Removing these objects doesn’t make the document invalid but rather shrinks it.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Set RemoveUsedObject option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_objects = True

    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
```

### Removing Unused Streams

Sometimes the document contains the unused resource streams. These streams are not “unused objects” because they are referenced from a page resource dictionary. Thus, they are not removed with a “remove unused objects” method. But these streams are never used with the page contents. This may happen in cases when an image has been removed from the page but not from the page resources. Also, this situation often occurs when pages are extracted from the document and document pages have “common” resources, that is, the same Resources object. Page contents are analyzed in order to determine if a resource stream is used or not. Unused streams are removed. It sometimes decreases the document size. The use of this technique is similar to the previous step:

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Set RemoveUsedStreams option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_streams = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
```

### Linking Duplicate Streams

Some documents can contain several identical resource streams (like images, for instance). This may happen, say when a document is concatenated with itself. The output document contains two independent copies of the same resource stream. We analyze all resource streams and compare them. If streams are duplicated, they are merged, that is, only one copy is left. The references are changed appropriately, and the copies of the object are removed. In some cases, it helps to decrease the document size.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Set LinkDuplicateStreams option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.link_duplcate_streams = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
```

### Unembedding Fonts

If the document uses embedded fonts, it means that all font data is stored in the document. The advantage is that the document is viewable regardless of whether the font is installed on the user's machine or not. But embedding fonts makes the document larger. The unembed fonts method removes all embedded fonts. Thus, the document size decreases but the document itself may become unreadable if the correct font is not installed.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Set UnembedFonts  option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.unembed_fonts = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
    file_stats_1 = os.stat(input_pdf)
    file_stats_2 = os.stat(output_pdf)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

The optimization resources apply these methods to the document. If any of these methods are applied, the document size will most probably decrease. If none of these methods is applied, the document size will not change which is obvious.

## Additional Ways to Reduce the PDF Document Size

### Removing or Flattening Annotations

Annotations can be deleted when they are unnecessary. When they are needed but do not require additional editing, they can be flattened. Both of these techniques will reduce the file size.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Flatten annotations
    for page in document.pages:
        for annotation in page.annotations:
            annotation.flatten()

    # Save updated document
    document.save(output_pdf)
```

### Removing Form Fields

If the PDF document contains AcroForms, we can try to reduce the file size by flattening form fields.

```python

    import aspose.pdf as ap

    # Load source PDF form
    doc = ap.Document(input_pdf)

    # Flatten Forms
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # Save the updated document
    doc.save(output_pdf)
```

### Convert a PDF from RGB colorspace to grayscale

A PDF file comprises Text, Image, Attachment, Annotations, Graphs, and other objects. You may come across a requirement to convert a PDF from RGB colorspace to grayscale so that it would be faster while printing those PDF files. Also, when the file is converted to grayscale, the document size is reduced too, but it can just as well cause a decrease in the document quality. This feature is currently supported by the Pre-Flight feature of Adobe Acrobat, but when talking about Office automation, Aspose.PDF is an ultimate solution to provide such leverages for document manipulations. In order to accomplish this requirement, the following code snippet can be used.

```python

    import aspose.pdf as ap

    # Load source PDF file
    document = ap.Document(input_pdf)
    strategy = ap.RgbToDeviceGrayConversionStrategy()
    for page in document.pages:
        # Convert the RGB colorspace image to GrayScale colorspace
        strategy.convert(page)

    # Save resultant file
    document.save(output_pdf)
```

### FlateDecode Compression

Aspose.PDF for Python via .NET provides support of FlateDecode compression for PDF Optimisation functionality. The following code snippet below shows how to use the option in Optimization to store images with **FlateDecode** compression:

```python

    import aspose.pdf as ap

    # Open Document
    doc = ap.Document(input_pdf)
    # Initialize OptimizationOptions
    optimizationOptions = ap.optimization.OptimizationOptions()
    # To optimise image using FlateDecode Compression set optimization options to Flate
    optimizationOptions.image_compression_options.encoding = ap.optimization.ImageEncoding.FLATE
    # Set Optimization Options
    doc.optimize_resources(optimizationOptions)
    # Save Document
    doc.save(output_pdf)
```

