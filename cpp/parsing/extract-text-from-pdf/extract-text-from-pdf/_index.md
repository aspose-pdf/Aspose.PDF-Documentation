---
title: Extract text from PDF C++
linktitle: Extract text from PDF
type: docs
weight: 10
url: /cpp/extract-text-from-all-pdf/
description: This article describes various ways to extract text from PDF documents using Aspose.PDF in C++. From entire pages, from a specific part, based on columns, etc.
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extract Text From All the Pages of a PDF Document

Extracting text from a PDF document is a common requirement. In this example, you’ll see how Aspose.PDF for C++ allows extracting text from all the pages of a PDF document. You need to create an object of the [TextAbsorber](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) class. After that, open the PDF using [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document) class and call the 'Accept' method of the [Pages](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.page)collection. The  [TextAbsorber](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) class absorbs the text from the document and returns in 'Text' property. The following code snippet shows you how to extract text from all pages of PDF document.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ExtractTextFromAllThePages() {

	std::clog << __func__ << ": Start" << std::endl;
	// String for path name
	String _dataDir("C:\\Samples\\Parsing\\");

	// String for file name
	String infilename("sample-4pages.pdf");
	String outfilename("extracted-text.txt");

	// Open document
	auto document = MakeObject<Document>(_dataDir + infilename);

	// Create TextAbsorber object to extract text
	auto textAbsorber = MakeObject<TextAbsorber>();
	// Accept the absorber for all the pages
	document->get_Pages()->Accept(textAbsorber);
	// Get the extracted text
	auto extractedText = textAbsorber->get_Text();

	System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
	std::clog << __func__ << ": Finish" << std::endl;
}
```

Call the **Accept** method on a particular page of the Document object. The Index is the particular page number from where text needs to be extracted.

```cpp
void ExtractTextFromParticularPage() {

	std::clog << __func__ << ": Start" << std::endl;
	// String for path name
	String _dataDir("C:\\Samples\\Parsing\\");

	// String for file name
	String infilename("sample-4pages.pdf");
	String outfilename("extracted-text.txt");

	// Open document
	auto document = MakeObject<Document>(_dataDir + infilename);

	// Create TextAbsorber object to extract text
	auto textAbsorber = MakeObject<TextAbsorber>();
	// Accept the absorber for all the pages
	document->get_Pages()->idx_get(1)->Accept(textAbsorber);
	// Get the extracted text
	auto extractedText = textAbsorber->get_Text();

	System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
	std::clog << __func__ << ": Finish" << std::endl;
}
```

## Extract Text from Pages using Text Device

You can use the [TextDevice](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.devices.text_device/)class to extract text from a PDF file TextDevice uses TextAbsorber in its implementation, thus, in fact, they do the same thing but TextDevice just implemented to unify the "Device" approach to extract anything from the page ImageDevice, PageDevice, etc. TextAbsorber may extract text from Page, entire PDF or XForm, this TextAbsorber is more universal

### Extract text from all pages

The following steps and code snippet shows you how to extract text from a PDF using the text device.

1. Create an object of Document class with input PDF file specified
1. Create an object of TextDevice class
1. Use object of TextExtractOptions class to specify extraction options
1. Use the Process method of TextDevice class to convert contents to the text
1. Save the text to the output file

```cpp
void ExtractTextUsingTextDevice() {

	std::clog << __func__ << ": Start" << std::endl;
	// String for path name
	String _dataDir("C:\\Samples\\Parsing\\");

	// String for file name
	String infilename("sample-4pages.pdf");
	String outfilename("extracted-text.txt");

	// Open document
	auto document = MakeObject<Document>(_dataDir + infilename);

	auto builder = MakeObject<System::Text::StringBuilder>();
	// String to hold extracted text
	String extractedText;

	for (auto page : document->get_Pages()) {
		auto textStream = MakeObject<System::IO::MemoryStream>();
		// Create text device
		auto textDevice = MakeObject<Aspose::Pdf::Devices::TextDevice>();

		// Set text extraction options - set text extraction mode (Raw or Pure)
		auto textExtOptions = MakeObject<TextExtractionOptions>(TextExtractionOptions::TextFormattingMode::Pure);

		textDevice->set_ExtractionOptions(textExtOptions);

		// Convert a particular page and save text to the stream
		textDevice->Process(page, textStream);

		// Close memory stream
		textStream->Close();

		// Get text from memory stream
		extractedText = System::Text::Encoding::get_Unicode()->GetString(textStream->ToArray());
		builder->Append(extractedText);

	}
	// Save the extracted text in text file
	System::IO::File::WriteAllText(_dataDir + outfilename, builder->ToString());
	std::clog << __func__ << ": Finish" << std::endl;
}
```

## Extract Text from a particular page region

[TextAbsorber](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) class provides the capability to extract text from a particular or all pages of a PDF document. This class returns the extracted text in the 'Text' property. However, if we have the requirement to extract text from a particular page region, we can use the **Rectangle** property of [TextSearchOptions](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_search_options/) The Rectangle property takes a Rectangle object as a value and using this property, we can specify the region of the page from which we need to extract the text.

The **Accept** method of a page is called to extract the text. Create objects of [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document/) and [TextAbsorber](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) classes. Call 'Accept' method on the individual page, as **Page** Index, of the [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document/) object. The **Index** is the particular page number from where text needs to be extracted. You can get text from the 'Text' property of the [TextAbsorber](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) class. The following code snippet shows you how to extract text from an individual page.

```cpp
void ExtractTextFromParticularPageRegion() {

	std::clog << __func__ << ": Start" << std::endl;
	// String for path name
	String _dataDir("C:\\Samples\\Parsing\\");

	// String for file name
	String infilename("sample-4pages.pdf");
	String outfilename("extracted-text.txt");

	// Open document
	auto document = MakeObject<Document>(_dataDir + infilename);

	// Create TextAbsorber object to extract text
	auto textAbsorber = MakeObject<TextAbsorber>();
	textAbsorber->get_TextSearchOptions()->set_LimitToPageBounds(true);
	textAbsorber->get_TextSearchOptions()->set_Rectangle(MakeObject<Rectangle>(100, 200, 250, 350));

	// Accept the absorber for all the pages
	document->get_Pages()->idx_get(1)->Accept(textAbsorber);
	// Get the extracted text
	auto extractedText = textAbsorber->get_Text();

	System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
	std::clog << __func__ << ": Finish" << std::endl;

}
```

## Extract text based on columns

PDF is a very popular format, and for good reason: with PDF, you can be practically sure that your document will display and print the same way on different computers.

However, PDF documents suffer from the disadvantage that they usually lack information about what content is in paragraphs, tables, figures, header/footer information, and so on.

Aspose.PDf for C++ - it is an easy-to-use utility, that allows you to extract text based on columns.

```cpp
void ExtractTextBasedOnColumns() {

	std::clog << __func__ << ": Start" << std::endl;
	// String for path name
	String _dataDir("C:\\Samples\\Parsing\\");

	// String for file name
	String infilename("sample-4pages.pdf");
	String outfilename("extracted-text.txt");

	// Open document
	auto document = MakeObject<Document>(_dataDir + infilename);

	// Create TextAbsorber object to extract text
	auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>();


	// Accept the absorber for all the pages
	document->get_Pages()->Accept(textFragmentAbsorber);

	auto tfc = textFragmentAbsorber->get_TextFragments();
	for (auto tf : tfc)
	{
		// Need to reduce font size at least for 70%
		auto size = tf->get_TextState()->get_FontSize() * 0.7f;
		tf->get_TextState()->set_FontSize(size);
	}
	auto stream = MakeObject<System::IO::MemoryStream>();
	document->Save(stream);
	document = MakeObject<Document>(stream);
	auto textAbsorber = MakeObject<TextAbsorber>();
	document->get_Pages()->Accept(textAbsorber);
	String extractedText = textAbsorber->get_Text();

	System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
	std::clog << __func__ << ": Finish" << std::endl;
}
```

### Second approach - Using ScaleFactor

In this new release, we also have introduced several improvements in TextAbsorber and in the internal text formatting mechanism. So now during the text extraction using ‘Pure’ mode, you may specify the [ScaleFactor](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_extraction_options#a4f9a173765d483b493c31e416f8b035a) option and it can be another approach to extract text from a multi-column PDF document besides the above-stated approach. This scale factor may be set to adjust the grid which is used for the internal text formatting mechanism during text extraction. Specifying the ScaleFactor values between 1 and 0.1 (including 0.1) has the same effect as font reduction.

Specifying the ScaleFactor values between 0.1 and -0.1 is treated as zero value, but it makes the algorithm to calculate scale factor needed during extracting text automatically. The calculation is based on average glyph width of the most popular font on the page, but we cannot guarantee that in extracted text no string of column reaches the start of the next column. Please note that if ScaleFactor value is not specified, the default value of 1.0 will be used. It means no scaling will be carried out. If the specified ScaleFactor value is more than 10 or less than -0.1, the default value of 1.0 will be used.

We propose the usage of auto-scaling (ScaleFactor = 0) when processing a large number of PDF files for text content extraction. Or manually set redundant reducing of grid width ( about ScaleFactor = 0.5). However, you must not determine whether scaling is necessary for concrete documents or not. If You set redundant reducing of grid width for the document (that doesn't need in it), the extracted text content will remain fully adequate. Please take a look at the following code snippet.

```cpp
void ExtractTextUsingScaleFactor() {

	std::clog << __func__ << ": Start" << std::endl;
	// String for path name
	String _dataDir("C:\\Samples\\Parsing\\");

	// String for file name
	String infilename("sample-4pages.pdf");
	String outfilename("extracted-text.txt");

	// Open document
	auto document = MakeObject<Document>(_dataDir + infilename);

	auto textAbsorber = MakeObject<TextAbsorber>();
	textAbsorber->set_ExtractionOptions(MakeObject<TextExtractionOptions>(TextExtractionOptions::TextFormattingMode::Pure));
	// Setting scale factor to 0.5 is enough to split columns in the majority of documents
	// Setting of zero allows to algorithm choose scale factor automatically
	textAbsorber->get_ExtractionOptions()->set_ScaleFactor(0.5); /* 0; */
	document->get_Pages()->Accept(textAbsorber);
	String extractedText = textAbsorber->get_Text();

	System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
	std::clog << __func__ << ": Finish" << std::endl;
}
```

## Extract Highlighted Text from PDF Document

In various scenarios of text extraction from a PDF document, you can come up with a requirement to extract only highlighted text from PDF document. In order to implement the functionality, we have added TextMarkupAnnotation.GetMarkedText() and TextMarkupAnnotation.GetMarkedTextFragments() methods in API. You can extract highlighted text from PDF document by filtering TextMarkupAnnotation and using the mentioned methods. The following code snippet shows how you can extract highlighted text from PDF document.

```cpp
void ExtractHighlightedText() {

	std::clog << __func__ << ": Start" << std::endl;
	// String for path name
	String _dataDir("C:\\Samples\\Parsing\\");

	// String for file name
	String infilename("sample-highlight.pdf");
	String outfilename("extracted-text.txt");

	// Open document
	auto document = MakeObject<Document>(_dataDir + infilename);

	// Loop through all the annotations
	for (auto annotation : document->get_Pages()->idx_get(1)->get_Annotations())
	{
		// Filter TextMarkupAnnotation
		if (annotation->get_AnnotationType() == Aspose::Pdf::Annotations::AnnotationType::Highlight)
		{
			auto highlightedAnnotation = System::DynamicCast<Aspose::Pdf::Annotations::HighlightAnnotation>(annotation);

			// Retrieve highlighted text fragments
			auto collection = highlightedAnnotation->GetMarkedTextFragments();
			for (auto tf : collection)
			{
				// Display highlighted text
				String s = tf->get_Text();
				std::cout << s << std::endl;
			}
		}
	}
}
```

## Access Text Fragment and Segment Elements from XML

Sometimes we need access to TextFragement or TextSegment items when processing PDF documents generated from XML. Aspose.PDF for C++ provides access to such items by name. The code snippet below shows how to use this functionality.

```cpp
void AccessTextFragmentandSegmentElementsXML()
{
	std::clog << __func__ << ": Start" << std::endl;
	// String for path name
	String _dataDir("C:\\Samples\\Parsing\\");

	// String for file name
	String infilename("sample-doc.xml");
	String outfilename("sample-doc.pdf");

	auto document = MakeObject<Document>();
	document->BindXml(_dataDir + infilename);

	System::SharedPtr<Page> page = System::DynamicCast<Aspose::Pdf::Page>(document->GetObjectById(u"mainSection"));
	// Make some operations with page
	// ...

	System::SharedPtr<TextSegment> segment = System::DynamicCast<Aspose::Pdf::Text::TextSegment>(document->GetObjectById(u"product_description"));
	// Make some operations with segment
	// ...
	document->Save(_dataDir + outfilename);

	std::clog << __func__ << ": Finish" << std::endl;
}
```
