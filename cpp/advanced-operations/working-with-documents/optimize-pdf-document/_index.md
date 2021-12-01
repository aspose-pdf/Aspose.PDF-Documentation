---
title: Optimize PDF using C++
linktitle: Optimize PDF
type: docs
weight: 30
url: /cpp/optimize-pdf/
description: Optimize PDF file, shrink all images, reduce size PDF, unembed fonts, enable reusing page content, remove or flatten annotations with C++.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

First of all, any PDF optimization you do is for the user. In PDFs, user optimization is largely about reducing the size of your PDFs in order to increase their loading speed. This is the most popular task.
We can use several techniques to optimize PDF, but the most essential:

- Optimize page content for online browsing
- Shrink or compress all images
- Enable reusing page content
- Merge duplicate streams
- Unembed fonts
- Remove unused objects
- Remove flattening form fields
- Remove or flatten annotations

## Optimize PDF Document for the Web

When you are faced with the task of optimizing the content of your PDF document for better ranking in search engines, Aspose.PDF for C++ has a solution.

1. Open the input document in an [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document) object.
1. Use the [Optimize](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document#a04d95824c334f5e543c13f69a19d9cda) method.
1. Save the optimized document using the Save method.

The following code snippet shows how to optimize a PDF document for the web.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
//Optimize PDF Document for the Web
void OptimizeForWeb() {
    // String for path name
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String outfilename("OptimizeDocument_out.pdf");

    // Open document
    auto document = MakeObject<Document>();

    // Make some operations (add pages, images, etc) 
    // ...

    // Optimize for web
    document->Optimize();

    // Save output document
    document->Save(_dataDir + outfilename);
}
```

## Reduce Size PDF

The [OptimizeResources()](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document#aea33aac69a42423efb82bcdb359f2ec6) method allows you to reduce the document size by weeding out the unnecessary information. By default, this method works as follows:

- Resources that are not used on the document pages are removed
- Equal resources are joined into one object
- Unused objects are deleted

The snippet below is an example. Note, though, that this method cannot guarantee document shrinking.

```cpp
void ReduceSizePDF() {

    // String for path name
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String outfilename("ShrinkDocument_out.pdf");

    // Open document
    auto document = MakeObject<Document>();
    // Make some operations (add pages, images, etc) 
    // ...

    // Optimize PDF document. Note, though, that this method cannot guarantee document shrinking 
    document->OptimizeResources();

    // Save output document
    document->Save(_dataDir + outfilename);
}
```

## Optimization Strategy Management

We can also customize the optimization strategy. Currently, the [OptimizeResources()](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document#aea33aac69a42423efb82bcdb359f2ec6) method uses 5 techniques. These techniques can be applied using the OptimizeResources() method with the [OptimizationOptions](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document.optimization_options/) parameter.

### Shrinking or Compressing All Images

To optimize images in your PDF document, we will use [Aspose.Pdf.Optimization](https://apireference.aspose.com/pdf/cpp/namespace/aspose.pdf.optimization).
To solve the problem with image optimization, we have the following options: reduce image quality and/or change their resolution. In any case, [ImageCompressionOptions](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options/) should be applied. In the following example, we shrink images by reducing [ImageQuality](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#a92ee855b042a6b310984b4966ea7154e) to 50.

```cpp
void CompressImage() {
    // String for path name
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Initialize OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Set CompressImages option
    optimizationOptions->get_ImageCompressionOptions()->set_CompressImages(true);
    // Set ImageQuality option
    optimizationOptions->get_ImageCompressionOptions()->set_ImageQuality(50);

    // Optimize PDF document using OptimizationOptions
    document->OptimizeResources(optimizationOptions); 
    // Save updated document
    document->Save(_dataDir + outfilename);
}
```

To set the image at a lower resolution, set [ResizeImages](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#a0e5aad7e140ee380c09ebbb8a5238ff6) to true and [MaxResolution](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#a05a4d1ace23ef074b3dc203cb213755e) to the corresponding value.

```cpp
void ResizeImagesWithLowerResolution() {
    // String for path name
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String infilename("ResizeImage.pdf");
    String outfilename("ResizeImages_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Initialize OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Set CompressImages option
    optimizationOptions->get_ImageCompressionOptions()->set_CompressImages(true);
    // Set ImageQuality option
    optimizationOptions->get_ImageCompressionOptions()->set_ImageQuality(75);

    // Set ResizeImage option
    optimizationOptions->get_ImageCompressionOptions()->set_ResizeImages(true);
    // Set MaxResolution option
    optimizationOptions->get_ImageCompressionOptions()->set_MaxResolution(300);

    // Optimize PDF document using OptimizationOptions
    document->OptimizeResources(optimizationOptions);
    // Save updated document
    document->Save(_dataDir + outfilename);
}
```

Aspose.PDF for C++ also offers you control over the runtime setting. Today, we can use two algorithms - Standard and Fast. To control the execution time we should set a [Version](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#aa2f1d93725ce56f8fabe692152bbf3a4) property.

The following snippet demonstrates the Fast algorithm:

```cpp
void ResizeImagesWithLowerResolutionFast() {
    auto time = System::DateTime::get_Now().get_Ticks();
    // String for path name
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String infilename("ResizeImage.pdf");
    String outfilename("ResizeImages_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Initialize OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Set CompressImages option
    optimizationOptions->get_ImageCompressionOptions()->set_CompressImages(true);
    // Set ImageQuality option
    optimizationOptions->get_ImageCompressionOptions()->set_ImageQuality(75);

    // Set ResizeImage option
    optimizationOptions->get_ImageCompressionOptions()->set_ResizeImages(true);
    // Set Imagae Compression Version to fast
    optimizationOptions->get_ImageCompressionOptions()->set_Version (Aspose::Pdf::Optimization::ImageCompressionVersion::Fast);

    // Optimize PDF document using OptimizationOptions
    document->OptimizeResources(optimizationOptions);
    // Save updated document
    document->Save(_dataDir + outfilename);
    std::cout << "Ticks: " << System::DateTime::get_Now().get_Ticks() - time << std::endl;
}
```

### Removing Unused Objects

Sometimes you may need to remove some unused objects from your PDF document that are not referenced on the pages.This may happen, for example, when a page is removed from the document page tree but the page object itself isn’t removed. Removing these objects doesn’t make the document invalid but rather shrinks it. Check next code snippet:

```cpp
void RemovingUnusedObject() { 
    // String for path name
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Initialize OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Set RemoveUsedObject option
    optimizationOptions->set_RemoveUnusedObjects(true);

    // Optimize PDF document using OptimizationOptions
    document->OptimizeResources(optimizationOptions);

    // Save updated document
    document->Save(_dataDir + outfilename); 
}
```

### Removing Unused Streams

Sometimes the document contains the unused resource streams. These streams are not “unused objects” because they are referenced from a page resource dictionary. Thus, they are not removed with a “remove unused objects” method. But these streams are never used with the page contents. This may happen in cases when an image has been removed from the page but not from the page resources. Also, this situation often occurs when pages are extracted from the document and document pages have “common” resources, that is, the same Resources object. Page contents are analyzed in order to determine if a resource stream is used or not. Unused streams are removed. It sometimes decreases the document size. The use of this technique is similar to the previous step:

```cpp
void RemovingUnusedStreams() { 
    // String for path name
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Open document
    auto document = MakeObject<Document>();

    // Initialize OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Set RemoveUsedStreams option
    optimizationOptions->set_RemoveUnusedStreams(true);

    // Optimize PDF document using OptimizationOptions
    document->OptimizeResources(optimizationOptions);

    // Save updated document
    document->Save(_dataDir + outfilename); 
}
```

### Linking Duplicate Streams

Some documents can contain several duplicate resource streams (like images, for instance). This may happen, say when a document is concatenated with itself. The output document contains two independent copies of the same resource stream. We analyze all resource streams and compare them. If streams are duplicated, they are merged, that is, only one copy is left. The references are changed appropriately, and the copies of the object are removed. In some cases, it helps to decrease the document size.

```cpp
void LinkingDuplicateStreams() { 
    // String for path name
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Initialize OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Set LinkDuplcateStreams option
    optimizationOptions->set_LinkDuplcateStreams(true);

    // Optimize PDF document using OptimizationOptions
    document->OptimizeResources(optimizationOptions);

    // Save updated document
    document->Save(_dataDir + outfilename); 
}
```

Additionally, we can use [AllowReusePageContent](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.optimization_options#aedaab36eaf8ed5059a2b1e11275bf6d8) settings. If this property is set to true, the page content will be reused when optimizing the document for identical pages.

```cpp
void AllowReusePageContent() { 
    // String for path name
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Initialize OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Set AllowReusePageContent option
    optimizationOptions->set_AllowReusePageContent(true);

    // Optimize PDF document using OptimizationOptions
    document->OptimizeResources(optimizationOptions);

    // Save updated document
    document->Save(_dataDir + outfilename); 
}
```

### Unembedding Fonts

When you create a PDF version of your personal design file, a copy of all necessary fonts is added to the PDF file itself. It is embedding. Regardless of where this PDF is opened, whether it is on your computer, a friend’s computer, or your print provider’s computer, all of the correct fonts will be there and will render properly.

But, if the document uses embedded fonts, it means that all font data is stored in the document. The advantage is that the document is viewable regardless of whether the font is installed on the user’s machine or not. But embedding fonts makes the document larger. The unembed fonts method removes all embedded fonts. Thus, the document size decreases but the document itself may become unreadable if the correct font is not installed.

```cpp
void UnembedFonts() {
    // String for path name
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir+infilename);

    // Initialize OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Set AllowReusePageContent option
    optimizationOptions->set_UnembedFonts(true);

    // Optimize PDF document using OptimizationOptions
    document->OptimizeResources(optimizationOptions);

    // Save updated document
    document->Save(_dataDir + outfilename);
}
```

The optimization resources apply these methods to the document. If any of these methods are applied, the document size will most probably decrease. If none of these methods is applied, the document size will not change which is obvious.

## Additional Ways to Reduce the PDF Document Size

### Removing or Flattening Annotations

The presence of annotations in your PDF document increases its size naturally.
Annotations can be deleted when they are unnecessary. When they are needed but do not require additional editing, they can be flattened. Both of these techniques will reduce the file size.

```cpp
void FlatteningAnnotation() {
    // String for path name
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String infilename("OptimizeDocument.pdf");
    // String for output file name
    String outfilename("OptimizeDocument_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Flatten annotations
    for(auto page : document->get_Pages())
    {
        for(auto annotation : page->get_Annotations())
        {
        annotation->Flatten();
        }
    }
    // Save updated document
    document->Save(_dataDir + outfilename);
}
```

### Removing Form Fields

Removing forms from your PDF will also optimize your document.
If the PDF document contains AcroForms, we can try to reduce the file size by flattening form fields.

```cpp
void FlatteningFormFields() {
    // String for path name
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String infilename("OptimizeFormField.pdf");
    // String for output file name
    String outfilename("OptimizeFormField_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Flatten form fields
    // Flatten Forms
    if (document->get_Form()->get_Fields()->get_Count() > 0)
    {
        for(auto item : document->get_Form()->get_Fields())
        {
            item->Flatten();
        }
    }
    // Save updated document
    document->Save(_dataDir + outfilename);
}
```

### Convert a PDF from RGB colorspace to grayscale

A PDF file comprises Text, Image, Attachment, Annotations, Graphs, and other objects. You may come across a requirement to convert a PDF from RGB colorspace to grayscale so that it would be faster while printing those PDF files. Also, when the file is converted to grayscale, the document size is reduced too, but it can just as well cause a decrease in the document quality. This feature is currently supported by the Pre-Flight feature of Adobe Acrobat, but when talking about Office automation, Aspose.PDF is an ultimate solution to provide such leverages for document manipulations. In order to accomplish this requirement, the following code snippet can be used.

```cpp
void ConvertPDFfromColorspaceToGrayscale() {
    // String for path name
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String infilename("OptimizeDocument.pdf");
    // String for output file name
    String outfilename("Test-gray_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto strategy = MakeObject<Aspose::Pdf::RgbToDeviceGrayConversionStrategy>();
    for (int idxPage = 1; idxPage <= document->get_Pages()->get_Count(); idxPage++)
    {
        // Get instance of particular page inside PDF
        auto page = document->get_Pages()->idx_get(idxPage);
        // Convert the RGB colorspace image to GrayScale colorspace
        strategy->Convert(page);
    }
    // Save resultant file
    document->Save(_dataDir + outfilename); 
}
```

### FlateDecode Compression

Aspose.PDF for C++ provides support of FlateDecode compression for PDF Optimisation functionality.
To optimize image using FlateDecode Compression set optimization options to Flate.
The following code snippet below shows how to use the option in Optimization to store images with **FlateDecode** compression:

```cpp
void FlatDecodeCompression() {
 // String for path name
 String _dataDir("C:\\Samples\\");

 // String for input file name
 String infilename("FlateDecodeCompression.pdf");
 // String for output file name
 String outfilename("FlateDecodeCompression_out.pdf");

 // Open document
 auto document = MakeObject<Document>(_dataDir + infilename);

 // Initialize OptimizationOptions
 auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

 // To optimize image using FlateDecode Compression set optimization options to Flate
 optimizationOptions->get_ImageCompressionOptions()->set_Encoding(Aspose::Pdf::Optimization::ImageEncoding::Flate);

 // Optimize PDF document using OptimizationOptions
 document->OptimizeResources(optimizationOptions);

 // Save updated document
 document->Save(_dataDir + outfilename);
}
```

### **Store Image in XImageCollection**

Aspose.PDF for C++ provides the ability to store new images into [XImageCollection](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.x_image_collection) with FlateDecode compression. To enable this option you can use **ImageFilterType.Flate** flag.
The following code snippet shows how to use this functionality:

```cpp
void StoreImageInXImageCollection() {

 // String for path name
 String _dataDir("C:\\Samples\\");

 // String for output file name
 String outfilename("FlateDecodeCompression_out.pdf");

 // Open document
 auto document = MakeObject<Document>();
 
 auto page = document->get_Pages()->Add();
 
 auto imageStream = System::IO::File::OpenRead(_dataDir + u"aspose-logo.jpg");
 
 page->get_Resources()->get_Images()->Add(imageStream, Aspose::Pdf::ImageFilterType::Flate);
 
 auto ximage = page->get_Resources()->get_Images()->idx_get(page->get_Resources()->get_Images()->get_Count());

 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());

 // Set coordinates
 int lowerLeftX = 0;
 int lowerLeftY = 0;
 int upperRightX = 600;
 int upperRightY = 600;
 
 auto rectangle = MakeObject<Rectangle>(lowerLeftX, lowerLeftY, upperRightX, upperRightY);

 auto matrix = MakeObject<Matrix>(new double[] {rectangle->get_URX() - rectangle->get_LLX(), 0, 0, rectangle->get_URY() - rectangle->get_LLY(), rectangle->get_LLX(), rectangle->get_LLY()});
 // Using ConcatenateMatrix (concatenate matrix) operator: defines how image must be placed
 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(matrix));
 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));
 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

 document->Save(_dataDir + outfilename);
}
```
