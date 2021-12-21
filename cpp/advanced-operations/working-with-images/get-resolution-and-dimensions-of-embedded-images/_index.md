---
title: Get Resolution and Dimensions of Embedded Images
linktitle: Get Resolution and Dimensions
type: docs
weight: 40
url: /cpp/get-resolution-and-dimensions-of-embedded-images/
description: This section shows details in getting resolution and dimensions of Embedded Images
lastmod: "2021-12-18"
---

This topic explains how to use the operator classes in the Aspose.PDF namespace which provide the capability to get resolution and dimension information about images without having to extract them.

There are different ways of achieving this. This article explains how to use an `arraylist` and [image placement classes](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement).

1. First, load the source PDF file (with images).
1. Then create an ArrayList object to hold the names of any images in the document.
1. Get the images using the Page.Resources.Images property.
1. Create a stack object to hold the image’s graphics state and use it to keep track of different image states.
1. Create a ConcatenateMatrix object which defines current transformation. It also supports scaling, rotating, and skewing any content. It concatenates the new matrix with previous one. Please note that we cannot define the transformation from scratch but only modify the existing transformation.
1. Because we can modify the matrix with ConcatenateMatrix, we may also need to revert back to the original image state. Use [GSave operator ](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_save/) and [GRestore operator](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_restore/). These operators are paired so they should be called together. For example, if you do some graphics work with complex transformations and finally return transformations back to initial state, the approach will be something like this:

The following code snippet shows you how to get an image’s dimensions and resolution without extracting the image from the PDF document.

```cpp
void WorkingWithImages::GetResolutionAndDimensionsOfEmbeddedImages()
{
	String _dataDir("C:\\Samples\\");
	// Load the source PDF file
	auto document = MakeObject<Document>(_dataDir + u"ImageInformation.pdf");

	// Define the default resolution for image
	int defaultResolution = 72;
	auto graphicsState = MakeObject<System::Collections::Generic::Stack<System::SmartPtr<object>>>();
	// Define array list object which will hold image names
	auto imageNames = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->get_Names();

	// Insert an object to stack
	graphicsState->Push(System::DynamicCast<object>(MakeObject<System::Drawing::Drawing2D::Matrix>(1, 0, 0, 1, 0, 0)));

	// Get all the operators on first page of document
	for (auto op : document->get_Pages()->idx_get(1)->get_Contents())
	{
		// Use GSave/GRestore operators to revert the transformations back to previously set
		auto opSaveState = System::DynamicCast<Aspose::Pdf::Operators::GSave>(op);
		auto opRestoreState = System::DynamicCast<Aspose::Pdf::Operators::GRestore>(op);

		// Instantiate ConcatenateMatrix object as it defines current transformation matrix.
		auto opCtm = System::DynamicCast<Aspose::Pdf::Operators::ConcatenateMatrix>(op);

		// Create Do operator which draws objects from resources. It draws Form objects and Image objects
		auto opDo = System::DynamicCast<Aspose::Pdf::Operators::Do>(op);

		if (opSaveState != nullptr)
		{
			// Save previous state and push current state to the top of the stack
			graphicsState->Push(System::DynamicCast<System::Drawing::Drawing2D::Matrix>(graphicsState->Peek())->Clone());
		}
		else if (opRestoreState != nullptr)
		{
			// Throw away current state and restore previous one
			graphicsState->Pop();
		}
		else if (opCtm != nullptr)
		{
			auto cm = MakeObject<System::Drawing::Drawing2D::Matrix>(
				(float)opCtm->get_Matrix()->get_A(),
				(float)opCtm->get_Matrix()->get_B(),
				(float)opCtm->get_Matrix()->get_C(),
				(float)opCtm->get_Matrix()->get_D(),
				(float)opCtm->get_Matrix()->get_E(),
				(float)opCtm->get_Matrix()->get_F());

			// Multiply current matrix with the state matrix
			System::DynamicCast<System::Drawing::Drawing2D::Matrix>(graphicsState->Peek())->Multiply(cm);
			continue;
		}
		else if (opDo != nullptr)
		{
			// In case this is an image drawing operator
			if (imageNames->Contains(opDo->get_Name()))
			{
				auto lastCTM = System::DynamicCast<System::Drawing::Drawing2D::Matrix>(graphicsState->Peek());
				// Create XImage object to hold images of first pdf page
				auto image = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->idx_get(opDo->get_Name());

				// Get image dimensions
				double scaledWidth = Math::Sqrt(Math::Pow(lastCTM->get_Elements()->idx_get(0), 2) + Math::Pow(lastCTM->get_Elements()->idx_get(1), 2));
				double scaledHeight = Math::Sqrt(Math::Pow(lastCTM->get_Elements()->idx_get(2), 2) + Math::Pow(lastCTM->get_Elements()->idx_get(3), 2));
				// Get Height and Width information of image
				double originalWidth = image->get_Width();
				double originalHeight = image->get_Height();

				// Compute resolution based on above information
				double resHorizontal = originalWidth * defaultResolution / scaledWidth;
				double resVertical = originalHeight * defaultResolution / scaledHeight;

				// Display Dimension and Resolution information of each image
				Console::Write(_dataDir);
				Console::Write(u" image {0} ({1:.##}:{2:.##}): res {3:.##} x {4:.##}",
					opDo->get_Name(), scaledWidth, scaledHeight, resHorizontal, resVertical);
			}
		}
	}
}
```
