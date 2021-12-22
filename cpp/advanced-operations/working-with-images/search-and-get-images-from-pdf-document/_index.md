---
title: Search and Get Images from PDF Document using C++
linktitle: Search and Get Images
type: docs
weight: 60
url: /cpp/search-and-get-images-from-pdf-document/
description: This section explain how to search and get images from PDF document with Aspose.PDF library.
lastmod: "2021-12-18"
---

The ImagePlacementAbsorber allows you to search among images on all pages in a PDF document.

To search a whole document for images:

1. Call the [Pages](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) collection’s [Accept](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#ae71a2782e747936e3c14b7ded5c6dc3f) method. The Accept method takes an [ImagePlacementAbsorber](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement_absorber/) object as a parameter. This returns a collection of ImagePlacement objects.
1. Loop through the ImagePlacements objects and get their properties (Image, dimensions, resolution and so on).

The following code snippet shows how to search a document for all its images.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void SearchAndGetImagesFromPDFDocument() {

    String _dataDir("C:\\Samples\\");

    // Open document
    auto document = MakeObject<Document>(_dataDir + u"SearchAndGetImages.pdf");

    // Create ImagePlacementAbsorber object to perform image placement search
    auto abs = MakeObject<ImagePlacementAbsorber>();

    // Accept the absorber for all the pages
    document->get_Pages()->Accept(abs);

    // Loop through all ImagePlacements, get image and ImagePlacement Properties
    for(auto imagePlacement : abs->get_ImagePlacements())
    {
        // Get the image using ImagePlacement object
        auto image = imagePlacement->get_Image();

        // Display image placement properties for all placements
        Console::WriteLine(u"image width: {0}", imagePlacement->get_Rectangle()->get_Width());
        Console::WriteLine(u"image height:{0}", imagePlacement->get_Rectangle()->get_Height());
        Console::WriteLine(u"image LLX:{0}", imagePlacement->get_Rectangle()->get_LLX());
        Console::WriteLine(u"image LLY:{0}", imagePlacement->get_Rectangle()->get_LLY());
        Console::WriteLine(u"image horizontal resolution:{0}", imagePlacement->get_Resolution()->get_X());
        Console::WriteLine(u"image vertical resolution:{0}", imagePlacement->get_Resolution()->get_Y());
    }
}
```

