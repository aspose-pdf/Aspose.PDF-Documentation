---
title: Render PDFs and merge images in C++
linktitle: PdfConverter Class
type: docs
weight: 70
url: /cpp/pdfconverter-class/
description: Render PDF pages as JPEG images and combine input images into JPEG, TIFF, or PDF output using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Render PDF Pages and Combine Images in C++
Abstract: Use PdfConverter to render PDF pages, configure resolution and page selection, and substitute fonts during conversion. Image examples create horizontal, vertical, and centered compositions, a multipage TIFF, and a PDF containing merged images.
---

Use [PdfConverter](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfconverter/) to render PDF pages as JPEG images and combine input images into JPEG, TIFF, or PDF output.

Conversion functions write numbered JPEG files to outputFolder. Image-merging functions sort files matching MergeImages*.jpg in inputDirectory and fail if none exist. The TIFF variant uses Document and TiffDevice rather than MergeImagesAsTiff, matching the supplied compatibility workaround.

The snippets are independent example functions with their SDK includes and example namespaces. Configure the Aspose.PDF for C++ SDK, supply the input resources referenced by the sample, and choose writable output paths. The examples retain the source field names, page indexes, coordinates, and options.

## Render PDF pages as JPEG images

Render the PDF and write each page image to a numbered JPEG file.

1. Create [PdfConverter](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfconverter/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Prepare page rendering with [PdfConverter::DoConvert()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfconverter/doconvert/).
1. Check for another image with [PdfConverter::HasNextImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfconverter/hasnextimage/).
1. Write each image with [PdfConverter::GetNextImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfconverter/getnextimage/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfConverter.h>
#include <Aspose.PDF.Cpp/Presentation/IndependentImpl/ImageFormat.h>
#include <drawing/imaging/image_format.h>
#include <system/io/directory.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/string.h>

namespace Facades::Examples::PDF_Converter
{
	using namespace System;
	using namespace Aspose::Pdf;
	using Aspose::Pdf::Facades::PdfConverter;

	void ConvertPdfPagesToImages01(String inputFile, String outputFolder)
	{
		auto converter = MakeObject<PdfConverter>();
		converter->BindPdf(inputFile);

		converter->DoConvert();
		System::IO::Directory::CreateDirectory_(outputFolder);
		int imageNumber = 1;
		while (converter->HasNextImage())
		{
			String outputFile = outputFolder + u"/" + String::Format(u"{0}_out.jpg", imageNumber);
			converter->GetNextImage(outputFile, System::Drawing::Imaging::ImageFormat::get_Jpeg());
			++imageNumber;
		}
	}
} // namespace Facades::Examples::PDF_Converter
```

## Render pages with resolution and CropBox settings

Render from page 2 at 600 DPI using CropBox coordinates and Production form presentation.

1. Create [PdfConverter](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfconverter/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Set coordinate type through [PdfConverter](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfconverter/) using the example values.
1. Set resolution through [PdfConverter](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfconverter/) using the example values.
1. Set form presentation mode through [PdfConverter](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfconverter/) using the example values.
1. Set start page through [PdfConverter](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfconverter/) using the example values.
1. Prepare page rendering with [PdfConverter::DoConvert()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfconverter/doconvert/).
1. Check for another image with [PdfConverter::HasNextImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfconverter/hasnextimage/).
1. Write each image with [PdfConverter::GetNextImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfconverter/getnextimage/).

```cpp
#include <Aspose.PDF.Cpp/Devices/FormPresentationMode.h>
#include <Aspose.PDF.Cpp/Devices/Resolution.h>
#include <Aspose.PDF.Cpp/Facades/PdfConverter.h>
#include <Aspose.PDF.Cpp/PageCoordinateType.h>
#include <Aspose.PDF.Cpp/Presentation/IndependentImpl/ImageFormat.h>
#include <drawing/imaging/image_format.h>
#include <system/io/directory.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/string.h>

namespace Facades::Examples::PDF_Converter
{
using namespace System;
using namespace Aspose::Pdf;
using Aspose::Pdf::Facades::PdfConverter;

void ConvertPdfPagesToImages02(String inputFile, String outputFolder)
{
    auto converter = MakeObject<PdfConverter>();
    converter->BindPdf(inputFile);
    converter->set_CoordinateType(PageCoordinateType::CropBox);
    converter->set_Resolution(MakeObject<Devices::Resolution>(600));
    converter->set_FormPresentationMode(Devices::FormPresentationMode::Production);
    converter->set_StartPage(2);
    converter->DoConvert();
    System::IO::Directory::CreateDirectory_(outputFolder);
    int imageNumber = 1;
    while (converter->HasNextImage())
    {
        String outputFile = outputFolder + u"/" + String::Format(u"{0}_out.jpg", imageNumber);
        converter->GetNextImage(outputFile, System::Drawing::Imaging::ImageFormat::get_Jpeg());
        ++imageNumber;
    }
}
} // namespace Facades::Examples::PDF_Converter
```

## Convert with font substitution

Temporarily substitute Helvetica with Arial during rendering. Remove the substitution after conversion and in the exception path.

1. Create [PdfConverter](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfconverter/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Prepare page rendering with [PdfConverter::DoConvert()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfconverter/doconvert/).
1. Check for another image with [PdfConverter::HasNextImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfconverter/hasnextimage/).
1. Write each image with [PdfConverter::GetNextImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfconverter/getnextimage/).

```cpp
#include <Aspose.PDF.Cpp/CommonData/Text/Fonts/FontSubstitutions/FontSubstitutionCollection.h>
#include <Aspose.PDF.Cpp/CommonData/Text/Fonts/FontSubstitutions/SimpleFontSubstitution.h>
#include <Aspose.PDF.Cpp/Facades/PdfConverter.h>
#include <Aspose.PDF.Cpp/Presentation/IndependentImpl/ImageFormat.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <drawing/imaging/image_format.h>
#include <system/io/directory.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/string.h>

namespace Facades::Examples::PDF_Converter
{
using namespace System;
using namespace Aspose::Pdf;
using Aspose::Pdf::Facades::PdfConverter;

void ConvertWithFontSubstitution(String inputFile, String outputFolder)
{
    auto substitutions = Aspose::Pdf::Text::FontRepository::get_Substitutions();
    auto substitution = MakeObject<Aspose::Pdf::Text::SimpleFontSubstitution>(u"Helvetica", u"Arial");
    substitutions->Add(substitution);
    try
    {
        auto converter = MakeObject<PdfConverter>();
        converter->BindPdf(inputFile);

        converter->DoConvert();
        System::IO::Directory::CreateDirectory_(outputFolder);
        int imageNumber = 1;
        while (converter->HasNextImage())
        {
            String outputFile = outputFolder + u"/" + String::Format(u"{0}_out.jpg", imageNumber);
            converter->GetNextImage(outputFile, System::Drawing::Imaging::ImageFormat::get_Jpeg());
            ++imageNumber;
        }
    }
    catch (...)
    {
        substitutions->Remove(substitution);
        throw;
    }
    substitutions->Remove(substitution);
}
} // namespace Facades::Examples::PDF_Converter
```

## Merge images vertically

Sort matching JPEG inputs and combine them vertically into a JPEG output.

1. Combine the prepared image streams with [PdfConverter::MergeImages()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfconverter/mergeimages/).

```cpp
#include <Aspose.PDF.Cpp/Facades/ImageMergeMode.h>
#include <Aspose.PDF.Cpp/Facades/PdfConverter.h>
#include <Aspose.PDF.Cpp/Presentation/IndependentImpl/ImageFormat.h>
#include <algorithm>
#include <stdexcept>
#include <system/collections/list.h>
#include <system/io/directory.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/io/memory_stream.h>
#include <system/string.h>

namespace Facades::Examples::PDF_Converter
{
using namespace System;
using namespace Aspose::Pdf;
using Aspose::Pdf::Facades::PdfConverter;

void MergeImages01(String inputDirectory, String outputFile)
{
    auto imageFiles = System::IO::Directory::GetFiles(inputDirectory, u"MergeImages*.jpg");
    std::sort(imageFiles->begin(), imageFiles->end());
    if (imageFiles->get_Length() == 0)
    {
        throw std::runtime_error("No images matching MergeImages*.jpg");
    }
    auto streams = MakeObject<System::Collections::Generic::List<SharedPtr<System::IO::Stream>>>();
    for (const auto &imageFile : imageFiles)
    {
        auto bytes = System::IO::File::ReadAllBytes(imageFile);
        streams->Add(MakeObject<System::IO::MemoryStream>(bytes));
    }
    auto mergedImage = PdfConverter::MergeImages(streams, Aspose::Pdf::Drawing::ImageFormat::Jpeg,
                                                 Aspose::Pdf::Facades::ImageMergeMode::Vertical, 1, 1);
    auto output = System::IO::File::Create(outputFile);
    mergedImage->CopyTo(output);
    output->Close();
}
} // namespace Facades::Examples::PDF_Converter
```

## Merge images horizontally

Sort matching JPEG inputs and combine them horizontally into a JPEG output.

1. Combine the prepared image streams with [PdfConverter::MergeImages()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfconverter/mergeimages/).

```cpp
#include <Aspose.PDF.Cpp/Facades/ImageMergeMode.h>
#include <Aspose.PDF.Cpp/Facades/PdfConverter.h>
#include <Aspose.PDF.Cpp/Presentation/IndependentImpl/ImageFormat.h>
#include <algorithm>
#include <stdexcept>
#include <system/collections/list.h>
#include <system/io/directory.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/io/memory_stream.h>
#include <system/string.h>

namespace Facades::Examples::PDF_Converter
{
using namespace System;
using namespace Aspose::Pdf;
using Aspose::Pdf::Facades::PdfConverter;

void MergeImages02(String inputDirectory, String outputFile)
{
    auto imageFiles = System::IO::Directory::GetFiles(inputDirectory, u"MergeImages*.jpg");
    std::sort(imageFiles->begin(), imageFiles->end());
    if (imageFiles->get_Length() == 0)
    {
        throw std::runtime_error("No images matching MergeImages*.jpg");
    }
    auto streams = MakeObject<System::Collections::Generic::List<SharedPtr<System::IO::Stream>>>();
    for (const auto &imageFile : imageFiles)
    {
        auto bytes = System::IO::File::ReadAllBytes(imageFile);
        streams->Add(MakeObject<System::IO::MemoryStream>(bytes));
    }
    auto mergedImage = PdfConverter::MergeImages(streams, Aspose::Pdf::Drawing::ImageFormat::Jpeg,
                                                 Aspose::Pdf::Facades::ImageMergeMode::Horizontal, 1, 1);
    auto output = System::IO::File::Create(outputFile);
    mergedImage->CopyTo(output);
    output->Close();
}
} // namespace Facades::Examples::PDF_Converter
```

## Merge images with Center mode

Combine matching JPEG inputs using Center mode and the supplied 2 by 2 spacing arguments.

1. Combine the prepared image streams with [PdfConverter::MergeImages()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfconverter/mergeimages/).

```cpp
#include <Aspose.PDF.Cpp/Facades/ImageMergeMode.h>
#include <Aspose.PDF.Cpp/Facades/PdfConverter.h>
#include <Aspose.PDF.Cpp/Presentation/IndependentImpl/ImageFormat.h>
#include <algorithm>
#include <stdexcept>
#include <system/collections/list.h>
#include <system/io/directory.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/io/memory_stream.h>
#include <system/string.h>

namespace Facades::Examples::PDF_Converter
{
using namespace System;
using namespace Aspose::Pdf;
using Aspose::Pdf::Facades::PdfConverter;

void MergeImages03(String inputDirectory, String outputFile)
{
    auto imageFiles = System::IO::Directory::GetFiles(inputDirectory, u"MergeImages*.jpg");
    std::sort(imageFiles->begin(), imageFiles->end());
    if (imageFiles->get_Length() == 0)
    {
        throw std::runtime_error("No images matching MergeImages*.jpg");
    }
    auto streams = MakeObject<System::Collections::Generic::List<SharedPtr<System::IO::Stream>>>();
    for (const auto &imageFile : imageFiles)
    {
        auto bytes = System::IO::File::ReadAllBytes(imageFile);
        streams->Add(MakeObject<System::IO::MemoryStream>(bytes));
    }
    auto mergedImage = PdfConverter::MergeImages(streams, Aspose::Pdf::Drawing::ImageFormat::Jpeg,
                                                 Aspose::Pdf::Facades::ImageMergeMode::Center, 2, 2);
    auto output = System::IO::File::Create(outputFile);
    mergedImage->CopyTo(output);
    output->Close();
}
} // namespace Facades::Examples::PDF_Converter
```

## Create a multipage TIFF from images

Create one PDF page for each input image and render the temporary document to a 24-bit multipage TIFF at 72 DPI.

1. Collect and sort the matching input images.
1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and add one page containing each input image.
1. Configure [TiffSettings](https://reference.aspose.com/pdf/cpp/aspose.pdf.devices/tiffsettings/) for 24-bit output and a resolution of 72 DPI.
1. Write the multipage TIFF with [TiffDevice::Process()](https://reference.aspose.com/pdf/cpp/aspose.pdf.devices/tiffdevice/process/) and close the output stream.

```cpp
#include <Aspose.PDF.Cpp/Devices/ColorDepth.h>
#include <Aspose.PDF.Cpp/Devices/Resolution.h>
#include <Aspose.PDF.Cpp/Devices/TiffDevice.h>
#include <Aspose.PDF.Cpp/Devices/TiffSettings.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/PdfConverter.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <algorithm>
#include <drawing/bitmap.h>
#include <stdexcept>
#include <system/collections/list.h>
#include <system/io/directory.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/io/memory_stream.h>
#include <system/string.h>

namespace Facades::Examples::PDF_Converter
{
using namespace System;
using namespace Aspose::Pdf;
using Aspose::Pdf::Facades::PdfConverter;

void MergeImages04(String inputDirectory, String outputFile)
{
    auto imageFiles = System::IO::Directory::GetFiles(inputDirectory, u"MergeImages*.jpg");
    std::sort(imageFiles->begin(), imageFiles->end());
    if (imageFiles->get_Length() == 0)
    {
        throw std::runtime_error("No images matching MergeImages*.jpg");
    }
    auto streams = MakeObject<System::Collections::Generic::List<SharedPtr<System::IO::Stream>>>();
    for (const auto &imageFile : imageFiles)
    {
        auto bytes = System::IO::File::ReadAllBytes(imageFile);
        streams->Add(MakeObject<System::IO::MemoryStream>(bytes));
    }
    // C++ 26.9 cannot use MergeImagesAsTiff because its drawing runtime
    // lacks frame enumeration. Render one image per TIFF frame instead.
    auto document = MakeObject<Document>();
    for (auto stream : streams)
    {
        auto bitmap = MakeObject<System::Drawing::Bitmap>(stream);
        int width = bitmap->get_Width();
        int height = bitmap->get_Height();
        stream->set_Position(0);
        auto page = document->get_Pages()->Add();
        page->SetPageSize(width, height);
        page->AddImage(stream, MakeObject<Rectangle>(0, 0, width, height));
    }
    auto settings = MakeObject<Devices::TiffSettings>();
    settings->set_Depth(Devices::ColorDepth::Format24bpp);
    auto device = MakeObject<Devices::TiffDevice>(MakeObject<Devices::Resolution>(72), settings);
    auto output = System::IO::File::Create(outputFile);
    device->Process(document, 1, document->get_Pages()->get_Count(), output);
    output->Close();
}
} // namespace Facades::Examples::PDF_Converter
```

## Place merged images in a PDF

Merge input images vertically, place the merged image on a new PDF page, and save the PDF.

1. Create or open the [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and prepare its pages as shown.
1. Combine the prepared image streams with [PdfConverter::MergeImages()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfconverter/mergeimages/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/ImageMergeMode.h>
#include <Aspose.PDF.Cpp/Facades/PdfConverter.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Presentation/IndependentImpl/ImageFormat.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <algorithm>
#include <stdexcept>
#include <system/collections/list.h>
#include <system/io/directory.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/io/memory_stream.h>
#include <system/string.h>

namespace Facades::Examples::PDF_Converter
{
using namespace System;
using namespace Aspose::Pdf;
using Aspose::Pdf::Facades::PdfConverter;

void MergeImages05(String inputDirectory, String outputFile)
{
    auto imageFiles = System::IO::Directory::GetFiles(inputDirectory, u"MergeImages*.jpg");
    std::sort(imageFiles->begin(), imageFiles->end());
    if (imageFiles->get_Length() == 0)
    {
        throw std::runtime_error("No images matching MergeImages*.jpg");
    }
    auto streams = MakeObject<System::Collections::Generic::List<SharedPtr<System::IO::Stream>>>();
    for (const auto &imageFile : imageFiles)
    {
        auto bytes = System::IO::File::ReadAllBytes(imageFile);
        streams->Add(MakeObject<System::IO::MemoryStream>(bytes));
    }
    auto mergedImage = PdfConverter::MergeImages(streams, Aspose::Pdf::Drawing::ImageFormat::Jpeg,
                                                 Aspose::Pdf::Facades::ImageMergeMode::Vertical, 1, 1);
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    page->AddImage(mergedImage, MakeObject<Rectangle>(10, 120, 400, 720));
    document->Save(outputFile);
}
} // namespace Facades::Examples::PDF_Converter
```
