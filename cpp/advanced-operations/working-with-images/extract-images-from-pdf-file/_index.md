---
title: Extract Images from PDF File using C++
linktitle: Extract Images
type: docs
weight: 30
url: /cpp/extract-images-from-pdf-file/
description: This section shows how to extract images from PDF file using C++ library.
lastmod: "2021-12-18"
---

You may use Aspose.PDF for C++ to extract all images from your PDF documents into separate files that can be reused in other programs.

Images are held in each page’s Resources  collection’s Images collection. To extract a particular page, then get the image from the Images collection using the particular index of the image.

The image’s index returns an [XImage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image) object. This object provides a Save method which can be used to save the extracted image.

The following code snippet shows how to extract images from a PDF file.

```cpp
void WorkingWithImages::ExtractImages()
{
    String _dataDir("C:\\Samples\\");

    // Open document
    auto document = MakeObject<Document>(_dataDir + u"ExtractImages.pdf");

    // Extract a particular image
    auto xImage = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->idx_get(1);

    auto outputImage = System::IO::File::OpenWrite(_dataDir + u"output.jpg");

    // Save output image
    xImage->Save(outputImage, System::Drawing::Imaging::ImageFormat::get_Jpeg());
    outputImage->Close();

    // Save updated PDF file
    document->Save(_dataDir + u"ExtractImages_out.pdf");
}
```
