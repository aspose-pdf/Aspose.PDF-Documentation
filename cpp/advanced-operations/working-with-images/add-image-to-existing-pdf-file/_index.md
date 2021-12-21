---
title: Add Image to PDF 
linktitle: Add Image
type: docs
weight: 10
url: /cpp/add-image-to-existing-pdf-file/
description: This section describes how to add image to existing PDF file using C++ library.
lastmod: "2021-12-18"
---

## Add Image in an Existing PDF File

Every PDF page contains Resources and Contents properties. Resources can be images and forms for example, while content is represented by a set of PDF operators. Each operator has its name and argument. This example uses operators to add an image to a PDF file.

To add an image to an existing PDF file:

- Create a [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document/) object and open the input PDF document.
- Get the page you want to add an image to.
- Add the image into the page’s Resources collection.
- Use operators to place the image on the page:
- Use the [GSave operator ](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_save/) to save the current graphical state.
- Use [ConcatenateMatrix operator](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.operators.concatenate_matrix#a40ca09b1fa45560d57a1fd042d3fbe96) to specify where the image is to be placed.
- Use the [Do operator](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.operators.do/) to draw the image on the page.
- Finally, use [GRestore operator](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_restore/) to save the updated graphical state.
- Save the file.
The following code snippet shows how to add the image in a PDF document.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void WorkingWithImages::AddImageToExistingPDF()
{
	String _dataDir("C:\\Samples\\");

	// Open document
	auto document = MakeObject<Document>(_dataDir + u"AddImage.pdf");

	// Set coordinates
	int lowerLeftX = 50;
	int lowerLeftY = 750;
	int upperRightX = 100;
	int upperRightY = 800;

	// Get the page you want to add the image to
	auto page = document->get_Pages()->idx_get(1);

	// Load image into stream
	auto imageStream = System::IO::File::OpenRead(_dataDir + u"logo.png");

	// Add an image to the Images collection of the page resources
	page->get_Resources()->get_Images()->Add(imageStream);

	// Using the GSave operator: this operator saves current graphics state
	page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());

	// Create Rectangle and Matrix objects
	auto rectangle = MakeObject<Rectangle>(lowerLeftX, lowerLeftY, upperRightX, upperRightY);

	auto matrix = MakeObject<Matrix>(
		MakeArray<double>({
			rectangle->get_URX() - rectangle->get_LLX(),
			0,                  0,
			rectangle->get_URY() - rectangle->get_LLY(),
			rectangle->get_LLX(), rectangle->get_LLY() }));

	// Using ConcatenateMatrix (concatenate matrix) operator:
	// defines how image must be placed
	page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(matrix));
	auto ximage = page->get_Resources()->get_Images()->idx_get(page->get_Resources()->get_Images()->get_Count());

	// Using Do operator: this operator draws image
	page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));

	// Using GRestore operator: this operator restores graphics state
	page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

	// Save the new PDF
	document->Save(_dataDir + u"updated_document.pdf");

	// Close image stream
	imageStream->Close();
}
```

## Add Reference of a single Image multiple times in a PDF Document

Sometimes we have a requirement to use same image multiple times in a PDF document. Adding a new instance increases the resultant PDF document. [XImageCollection.Add(XImage)](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.x_image/) method allows to add reference to the same PDF object as original image that optimize the PDF Document size.

```cpp
void WorkingWithImages::AddReferenceOfaSingleImageMultipleTimes() {

	String _dataDir("C:\\Samples\\");
	auto imageRectangle = MakeObject<Rectangle>(0, 0, 30, 15);

	auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

	document->get_Pages()->Add();
	document->get_Pages()->Add();

	auto imageStream = System::IO::File::OpenRead(_dataDir + u"aspose-logo.png");

	SharedPtr<Aspose::Pdf::XImage> image;

	for (auto page : document->get_Pages()) {
		auto annotation = MakeObject<Aspose::Pdf::Annotations::WatermarkAnnotation>(page, page->get_Rect());
		auto form = annotation->get_Appearance()->idx_get(u"N");
		form->set_BBox(page->get_Rect());
		String name;
		if (image != nullptr) {
			name = form->get_Resources()->get_Images()->Add(imageStream);
			image = form->get_Resources()->get_Images()->idx_get(name);
		}
		else {
			form->get_Resources()->get_Images()->AddWithName(image);
		}
		form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
		form->get_Contents()->Add(
			MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(
				MakeObject<Matrix>(imageRectangle->get_Width(), 0, 0, imageRectangle->get_Height(), 0, 0)));

		form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(name));
		form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());
		page->get_Annotations()->Add(annotation, false);
		imageRectangle = MakeObject<Rectangle>(0, 0, imageRectangle->get_Width() * 1.01, imageRectangle->get_Height() * 1.01);
	}
	document->Save(_dataDir + u"AddReferenceOfaSingleImageMultipleTimes_out.pdf");
}
```

## Place image on page and preserve (control) aspect ratio

If we do not know the dimensions of the image there is every chance of getting a distorted image on the page. The following example shows one of the ways to avoid this.

```cpp
void WorkingWithImages::AddingImageAndPreserveAspectRatioIntoPDF() {

	String _dataDir("C:\\Samples\\");

	auto bitmap = System::Drawing::Image::FromFile(_dataDir + u"3410492.jpg");

	int width;
	int height;

	width = bitmap->get_Width();
	height = bitmap->get_Height();

	auto document = MakeObject<Document>();
	auto page = document->get_Pages()->Add();

	int scaledWidth = 400;
	int scaledHeight = scaledWidth * height / width;

	page->AddImage(_dataDir + u"3410492.jpg", new Rectangle(10, 10, scaledWidth, scaledHeight));
	document->Save(_dataDir + u"sample_image.pdf");
}
```

## Identify if image inside PDF is Colored or Black & White

To reduce the size of the image, you need to compress it. Before you can determine the type of compression of an image, you need to know whether it is color or black and white.

The type of compression applied to the image depends on the ColorSpace of the original image, i.e. if the image is in color (RGB) then use JPEG2000 compression, and if it is black and white then use JBIG2 / JBIG2000 compression. 

A PDF file may contain Text, Image, Graph, Attachment, Annotation etc elements and if the source PDF file contains images, we can determine image Color space and apply appropriate compression for image to reduce PDF file size. 

The following code snippet shows the steps to Identify if image inside PDF is Colored or Black & White.

```cpp
void WorkingWithImages::CheckColors() {

	String _dataDir("C:\\Samples\\");
	auto document = MakeObject<Document>(_dataDir + u"test4.pdf");
	try {
		// iterate through all pages of PDF file
		for (auto page : document->get_Pages()) {
			// create Image Placement Absorber instance
			auto abs = MakeObject<ImagePlacementAbsorber>();
			page->Accept(abs);

			for (auto ia : abs->get_ImagePlacements()) {
				/* ColorType */
				auto colorType = ia->get_Image()->GetColorType();
				switch (colorType) {
				case ColorType::Grayscale:
					Console::WriteLine(u"Grayscale Image");
					break;
				case ColorType::Rgb:
					Console::WriteLine(u"Colored Image");
					break;
				}
			}
		}
	}
	catch (Exception ex) {
		Console::WriteLine(u"Error reading file = {0}", document->get_FileName());
	}
}
```

## Control Image Quality

It is possible to control the quality of an image that’s being added to a PDF file. Use the overloaded [Replace](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.x_image_collection#a698b65051b073f0f4b84b1235889bd72) method in the [XImageCollection](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.x_image_collection) class.

The following code snippet demonstrates how to convert all the document images into JPEGs that use 80% quality for compression.

```cpp
void WorkingWithImages::ControlImageQuality() {

	String _dataDir("C:\\Samples\\");

	auto document = MakeObject<Document>(_dataDir + u"sample_with_images.pdf");

	for (auto page : document->get_Pages())
	{
		int idx = 1;
		for (auto image : page->get_Resources()->get_Images())
		{
			auto imageStream = MakeObject<System::IO::MemoryStream>();
			image->Save(imageStream, System::Drawing::Imaging::ImageFormat::get_Jpeg());
			page->get_Resources()->get_Images()->Replace(idx, imageStream, 80);
			idx = idx + 1;
		}
	}

	document->Save(_dataDir + u"sample_with_images_out.pdf");
}
```
