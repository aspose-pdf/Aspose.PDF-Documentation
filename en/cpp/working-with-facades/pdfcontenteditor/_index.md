---
title: Edit PDF content and actions in C++
linktitle: PdfContentEditor Class
type: docs
weight: 50
url: /cpp/pdfcontenteditor-class/
description: Replace text and images, manage attachments and stamps, create annotations, and configure document actions and viewer preferences using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Modify PDF Content, Stamps, and Actions in C++
Abstract: Use PdfContentEditor to replace text and images and manage attachments, stamps, annotations, and document actions. The examples also inspect viewer preferences and create a sample stamp for inspection workflows.
---

Use [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/) to replace text and images, manage attachments and stamps, create annotations, and configure document actions and viewer preferences.

Several examples require existing images or stamps on page 1. CreateStampSample produces a PDF with a stamp that can be used by the stamp inspection examples. Viewer action and media activation are separate from creating the PDF objects.

The snippets are independent example functions with their SDK includes and example namespaces. Configure the Aspose.PDF for C++ SDK, supply the input resources referenced by the sample, and choose writable output paths. The examples retain the source field names, page indexes, coordinates, and options.

## Add attachment

Attach the supplied file stream using its filename and a sample description.

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Attach the file with [PdfContentEditor::AddDocumentAttachment()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/adddocumentattachment/).
1. Save the resulting PDF with [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/io/path.h>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
	using namespace System;
	using namespace Aspose::Pdf;
	using namespace Aspose::Pdf::Facades;

	void AddAttachment(String inputFile, String attachmentFile, String outputFile)
	{
		auto editor = MakeObject<PdfContentEditor>();
		auto attachmentStream = System::IO::File::OpenRead(attachmentFile);

		editor->BindPdf(inputFile);
		editor->AddDocumentAttachment(attachmentStream, System::IO::Path::GetFileName(attachmentFile),
			u"Sample attachment.");
		editor->Save(outputFile);
	}
} // namespace Facades::Examples::PDF_ContentEditor
```

## Add document action

Assign an alert script to the document-open additional action.

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Set the document action with [PdfContentEditor::AddDocumentAdditionalAction()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/adddocumentadditionalaction/).
1. Save the resulting PDF with [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void AddDocumentAction(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfContentEditor>();

    editor->BindPdf(inputFile);
    editor->AddDocumentAdditionalAction(PdfContentEditor::DocumentOpen,
                                        u"app.alert('Document opened with PdfContentEditor action');");
    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_ContentEditor
```

## Add line annotation

Create a red line annotation on page 1 with the specified endpoints, border, and line-ending settings.

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Create the line annotation with [PdfContentEditor::CreateLine()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/createline/).
1. Save the resulting PDF with [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <drawing/color.h>
#include <drawing/rectangle.h>
#include <system/array.h>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using Rectangle = System::Drawing::Rectangle;
using DrawingColor = System::Drawing::Color;

void AddLineAnnotation(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfContentEditor>();

    editor->BindPdf(inputFile);
    editor->CreateLine(Rectangle(100, 100, 200, 200), u"This is line annotation", 100, 100, 200, 200, 1, 1,
                       DrawingColor::get_Red(), u"Solid", MakeArray<int32_t>({3, 2}), MakeArray<String>({u"Square"}));
    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_ContentEditor
```

## Add movie annotation

Create a movie annotation on page 1 using movieFile and the supplied display rectangle.

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Create the movie annotation with [PdfContentEditor::CreateMovie()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/createmovie/).
1. Save the resulting PDF with [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <drawing/rectangle.h>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using Rectangle = System::Drawing::Rectangle;

void AddMovieAnnotation(String inputFile, String movieFile, String outputFile)
{
    auto editor = MakeObject<PdfContentEditor>();

    editor->BindPdf(inputFile);
    editor->CreateMovie(Rectangle(80, 500, 220, 120), movieFile, 1);
    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_ContentEditor
```

## Add polygon annotation

Create a page 1 polygon annotation using the LineInfo vertex array.

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Create the polygon annotation with [PdfContentEditor::CreatePolygon()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/createpolygon/).
1. Save the resulting PDF with [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/LineInfo.h>
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <drawing/rectangle.h>
#include <system/array.h>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using Rectangle = System::Drawing::Rectangle;

void AddPolygonAnnotation(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfContentEditor>();

    editor->BindPdf(inputFile);
    auto lineInfo = MakeObject<LineInfo>();
    lineInfo->set_BorderStyle(0);
    lineInfo->set_VerticeCoordinate(MakeArray<float>({100, 200, 150, 260, 220, 220, 200, 160}));
    editor->CreatePolygon(lineInfo, 1, Rectangle(90, 150, 150, 120), u"This is polygon annotation");
    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_ContentEditor
```

## Add rubber stamp

Create a green Approved rubber-stamp annotation on page 1.

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Create the rubber-stamp annotation with [PdfContentEditor::CreateRubberStamp()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/createrubberstamp/).
1. Save the resulting PDF with [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <drawing/color.h>
#include <drawing/rectangle.h>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using Rectangle = System::Drawing::Rectangle;
using DrawingColor = System::Drawing::Color;

void AddRubberStamp(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfContentEditor>();

    editor->BindPdf(inputFile);
    editor->CreateRubberStamp(1, Rectangle(120, 450, 180, 60), u"Approved", u"Approved by reviewer",
                              DrawingColor::get_Green());
    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_ContentEditor
```

## Add text annotation

Create an open text annotation titled Text Annotation on page 1.

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Create the text annotation with [PdfContentEditor::CreateText()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/createtext/).
1. Save the resulting PDF with [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <drawing/rectangle.h>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using Rectangle = System::Drawing::Rectangle;

void AddTextAnnotation(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfContentEditor>();

    editor->BindPdf(inputFile);
    editor->CreateText(Rectangle(100, 400, 50, 50), u"Text Annotation", u"This is a text annotation", true, u"Insert",
                       1);
    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_ContentEditor
```

## Bind from stream and save

Bind the editor to a PDF input stream and save it to outputFile.

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Save the resulting PDF with [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void BindFromStreamAndSave(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfContentEditor>();
    auto inputStream = System::IO::File::OpenRead(inputFile);

    editor->BindPdf(inputStream);
    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_ContentEditor
```

## Change stamp position

Move stamp index 0 on page 1 to (200, 200).

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Move the stamp by index with [PdfContentEditor::MoveStamp()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/movestamp/).
1. Save the resulting PDF with [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void ChangeStampPosition(String inputFile, String outputFile)
{
    auto pdfContentEditor = MakeObject<PdfContentEditor>();

    pdfContentEditor->BindPdf(inputFile);

    int pageId = 1;
    int stampIndex = 0;
    double x = 200;
    double y = 200;

    pdfContentEditor->MoveStamp(pageId, stampIndex, x, y);

    pdfContentEditor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_ContentEditor
```

## Change viewer preferences

Read the existing viewer-preference flags and set the additional bit represented by 1.

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Set the viewer flags with [PdfContentEditor::ChangeViewerPreference()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/changeviewerpreference/).
1. Read the viewer flags with [PdfContentEditor::GetViewerPreference()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/getviewerpreference/).
1. Save the resulting PDF with [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void ChangeViewerPreferences(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfContentEditor>();

    editor->BindPdf(inputFile);
    editor->ChangeViewerPreference(editor->GetViewerPreference() | 1);
    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_ContentEditor
```

## Create stamp sample

Write a sample PNG image, create a one-page PDF, and apply an image stamp with ID 1.

1. Create [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/).
1. Create or open the [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and prepare its pages as shown.
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Bind the stamp image with [Stamp::BindImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/bindimage/).
1. Set stamp id through [Stamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/) using the example values.
1. Set page number through [Stamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/) using the example values.
1. Set stamp placement with [Stamp::SetOrigin()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/stamp/setorigin/).
1. Apply the configured stamp with [PdfFileStamp::AddStamp()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/addstamp/).
1. Save the resulting PDF with [PdfFileStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilestamp/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/PdfFileStamp.h>
#include <Aspose.PDF.Cpp/Facades/Stamp.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Presentation/IndependentImpl/ImageFormat.h>
#include <drawing/bitmap.h>
#include <drawing/color.h>
#include <drawing/graphics.h>
#include <drawing/image.h>
#include <drawing/imaging/image_format.h>
#include <drawing/solid_brush.h>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
	using namespace System;
	using namespace Aspose::Pdf;
	using namespace Aspose::Pdf::Facades;

	void CreateStampSample(String imageFile, String outputFile)
	{
		auto image = MakeObject<System::Drawing::Bitmap>(120, 60);
		auto graphics = System::Drawing::Graphics::FromImage(image);
		graphics->Clear(System::Drawing::Color::get_White());
		graphics->FillRectangle(MakeObject<System::Drawing::SolidBrush>(System::Drawing::Color::get_Blue()), 10, 10, 100,
			40);
		image->Save(imageFile, System::Drawing::Imaging::ImageFormat::get_Png());
		auto document = MakeObject<Aspose::Pdf::Document>();
		document->get_Pages()->Add();
		auto stamper = MakeObject<Aspose::Pdf::Facades::PdfFileStamp>();
		stamper->BindPdf(document);
		auto stamp = MakeObject<Aspose::Pdf::Facades::Stamp>();
		stamp->BindImage(imageFile);
		stamp->set_StampId(1);
		stamp->set_PageNumber(1);
		stamp->SetOrigin(100, 400);
		stamper->AddStamp(stamp);
		stamper->Save(outputFile);
	}
} // namespace Facades::Examples::PDF_ContentEditor
```

## Delete image

Delete image index 1 from page 1.

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Delete the images with [PdfContentEditor::DeleteImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/deleteimage/).
1. Save the resulting PDF with [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <system/array.h>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void DeleteImage(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfContentEditor>();

    editor->BindPdf(inputFile);
    editor->DeleteImage(1, MakeArray<int32_t>({1}));

    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_ContentEditor
```

## Delete images

Call DeleteImage() without arguments to remove images from the bound PDF.

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Delete the images with [PdfContentEditor::DeleteImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/deleteimage/).
1. Save the resulting PDF with [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void DeleteImages(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfContentEditor>();

    editor->BindPdf(inputFile);
    editor->DeleteImage();
    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_ContentEditor
```

## Extract image from stamp

Read page 1 stamps and save the first stamp image as PNG. Throw an error if no stamps are found.

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Read page stamp information with [PdfContentEditor::GetStamps()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/getstamps/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <Aspose.PDF.Cpp/Facades/StampInfo.h>
#include <Aspose.PDF.Cpp/Presentation/IndependentImpl/ImageFormat.h>
#include <drawing/image.h>
#include <drawing/imaging/image_format.h>
#include <stdexcept>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void ExtractImageFromStamp(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfContentEditor>();
    editor->BindPdf(inputFile);
    auto infos = editor->GetStamps(1);
    if (infos->get_Length() == 0)
        throw std::runtime_error("No stamps found");
    infos->idx_get(0)->get_Image()->Save(outputFile, System::Drawing::Imaging::ImageFormat::get_Png());
}
} // namespace Facades::Examples::PDF_ContentEditor
```

## Get viewer preferences

Print the current viewer-preference flags.

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Read the viewer flags with [PdfContentEditor::GetViewerPreference()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/getviewerpreference/).
1. Print the results or diagnostic messages shown in the example.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <iostream>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void GetViewerPreferences(String inputFile)
{
    auto editor = MakeObject<PdfContentEditor>();

    editor->BindPdf(inputFile);
    std::cout << "Current viewer preference: " << editor->GetViewerPreference() << std::endl;
}
} // namespace Facades::Examples::PDF_ContentEditor
```

## List stamps

Print the number of stamps returned for page 1.

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Read page stamp information with [PdfContentEditor::GetStamps()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/getstamps/).
1. Print the results or diagnostic messages shown in the example.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <Aspose.PDF.Cpp/Facades/StampInfo.h>
#include <drawing/image.h>
#include <iostream>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void ListStamps(String inputFile)
{
    auto editor = MakeObject<PdfContentEditor>();

    editor->BindPdf(inputFile);
    auto stamps = editor->GetStamps(1);
    std::cout << "Stamps on page 1: " << stamps->get_Length() << std::endl;
}
} // namespace Facades::Examples::PDF_ContentEditor
```

## Move stamp by id

Move stamp ID 1 on page 1 to (200, 200).

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Move the stamp by identifier with [PdfContentEditor::MoveStampById()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/movestampbyid/).
1. Save the resulting PDF with [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void MoveStampById(String inputFile, String outputFile)
{
    auto pdfContentEditor = MakeObject<PdfContentEditor>();

    pdfContentEditor->BindPdf(inputFile);

    int pageId = 1;
    int stampId = 1;
    double x = 200;
    double y = 200;

    pdfContentEditor->MoveStampById(pageId, stampId, x, y);

    pdfContentEditor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_ContentEditor
```

## Remove attachments

Delete document attachments.

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Remove document attachments with [PdfContentEditor::DeleteAttachments()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/deleteattachments/).
1. Save the resulting PDF with [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void RemoveAttachments(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfContentEditor>();

    editor->BindPdf(inputFile);
    editor->DeleteAttachments();
    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_ContentEditor
```

## Remove open action

Remove the document-open action.

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Remove the open action with [PdfContentEditor::RemoveDocumentOpenAction()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/removedocumentopenaction/).
1. Save the resulting PDF with [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void RemoveOpenAction(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfContentEditor>();

    editor->BindPdf(inputFile);
    editor->RemoveDocumentOpenAction();
    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_ContentEditor
```

## Replace image

Replace image index 1 on page 1 with imageFile.

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Replace the selected image with [PdfContentEditor::ReplaceImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/replaceimage/).
1. Save the resulting PDF with [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void ReplaceImage(String inputFile, String imageFile, String outputFile)
{
    auto editor = MakeObject<PdfContentEditor>();

    editor->BindPdf(inputFile);
    editor->ReplaceImage(1, 1, imageFile);
    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_ContentEditor
```

## Replace text simple

Set ReplaceAll scope and replace 33 with XXXIII followed by a space.

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Replace matching text with [PdfContentEditor::ReplaceText()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/replacetext/).
1. Save the resulting PDF with [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <Aspose.PDF.Cpp/Facades/ReplaceTextStrategy.h>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void ReplaceTextSimple(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfContentEditor>();

    editor->BindPdf(inputFile);
    editor->get_ReplaceTextStrategy()->set_ReplaceScope(ReplaceTextStrategy::Scope::ReplaceAll);
    editor->ReplaceText(u"33", u"XXXIII ");
    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_ContentEditor
```

## Replace text with state

Replace software with SOFTWARE using blue, 14-point text and ReplaceAll scope.

1. Create [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Replace matching text with [PdfContentEditor::ReplaceText()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/replacetext/).
1. Save the resulting PDF with [PdfContentEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfcontenteditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Facades/PdfContentEditor.h>
#include <Aspose.PDF.Cpp/Facades/ReplaceTextStrategy.h>
#include <Aspose.PDF.Cpp/Text/TextState.h>
#include <system/string.h>

namespace Facades::Examples::PDF_ContentEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using namespace Aspose::Pdf::Text;
using PdfColor = Aspose::Pdf::Color;

void ReplaceTextWithState(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfContentEditor>();

    editor->BindPdf(inputFile);
    auto textState = MakeObject<TextState>();
    textState->set_ForegroundColor(PdfColor::get_Blue());
    textState->set_FontSize(14);
    editor->get_ReplaceTextStrategy()->set_ReplaceScope(ReplaceTextStrategy::Scope::ReplaceAll);
    editor->ReplaceText(u"software", u"SOFTWARE", textState);
    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_ContentEditor
```
