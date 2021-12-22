---
title: Working with Image Placement using C++
linktitle: Working with Image Placement
type: docs
weight: 50
url: /cpp/working-with-image-placement/
description: This section describes the features of working with image placement PDF file using C++ library.
lastmod: "2021-12-18"
---

**Aspose.PDF for C++** suppots the [ImagePlacement](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement), [ImagePlacementAbsorber](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement_absorber) and [ImagePlacementCollection](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement_collection) which provide similar capability as the classes described above to get an image’s resolution and position in a PDF document.

- ImagePlacementAbsorber performs image usage search as the ImagePlacement objects collection.
- ImagePlacement provides the members Resolution and Rectangle that return actual image placement values.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void WorkingWithImagePlacement() {

    String _dataDir("C:\\Samples\\");

    // Load the source PDF document
    auto document = MakeObject<Aspose::Pdf::Document>(_dataDir + u"ImagePlacement.pdf");

    auto abs = MakeObject<ImagePlacementAbsorber>();

    // Load the contents of first page
    document->get_Pages()->idx_get(1)->Accept(abs);
    for(auto imagePlacement : abs->get_ImagePlacements())
    {
        // Get image properties
        Console::WriteLine(u"image width: {0}", imagePlacement->get_Rectangle()->get_Width());
        Console::WriteLine(u"image height:{0}", imagePlacement->get_Rectangle()->get_Height());
        Console::WriteLine(u"image LLX:{0}", imagePlacement->get_Rectangle()->get_LLX());
        Console::WriteLine(u"image LLY:{0}", imagePlacement->get_Rectangle()->get_LLY());
        Console::WriteLine(u"image horizontal resolution:{0}", imagePlacement->get_Resolution()->get_X());
        Console::WriteLine(u"image vertical resolution:{0}", imagePlacement->get_Resolution()->get_Y());

        // Retrieve image with visible dimensions
        auto imageStream = MakeObject<System::IO::MemoryStream>();

        // Retrieve image from resources
        imagePlacement->get_Image()->Save(imageStream, System::Drawing::Imaging::ImageFormat::get_Png());
        auto resourceImage = System::DynamicCast< System::Drawing::Bitmap>(System::Drawing::Bitmap::FromStream(imageStream));

        // Create bitmap with actual dimensions
        auto scaledImage = MakeObject<System::Drawing::Bitmap>(resourceImage, (int)imagePlacement->get_Rectangle()->get_Width(), (int)imagePlacement->get_Rectangle()->get_Height());
        // ...

    }

}
```
