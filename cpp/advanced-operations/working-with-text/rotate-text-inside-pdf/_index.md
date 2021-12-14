---
title: Rotate Text Inside PDF using C++
linktitle: Rotate Text Inside PDF
type: docs
weight: 50
url: /cpp/rotate-text-inside-pdf/
description: Learn different ways to rotate text to PDF. Aspose.PDF allows you to rotate text to any angle, rotate text fragment or a whole paragraph.
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Rotate Text Inside PDF using Rotation Property

By using the Rotation property of [TextFragment](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/) class, you can rotate text at various angles. The text rotation can be used in different scenarios of document generation. You can specify the rotation angle in degrees to rotate the text as per your requirement. Please check the following different scenarios, in which you can implement text rotation.

## Implement Rotation using TextFragment and TextBuilder

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ImplementRotationUsingTextFragmentAndTextBuilder() {

	String _dataDir("C:\\Samples\\");

	// Initialize document object
	auto document = MakeObject<Document>();
	// Get particular page
	auto page = document->get_Pages()->Add();
	// Create text fragment
	auto textFragment1 = MakeObject<TextFragment>("main text");
	textFragment1->set_Position(MakeObject<Position>(100, 600));

	// Set text properties
	textFragment1->get_TextState()->set_FontSize(12);
	textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

	// Create rotated text fragment
	auto textFragment2 = MakeObject<TextFragment>("rotated text");
	textFragment2->set_Position(MakeObject<Position>(200, 600));
	// Set text properties
	textFragment2->get_TextState()->set_FontSize(12);
	textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
	textFragment2->get_TextState()->set_Rotation(45);

	// Create rotated text fragment
	auto textFragment3 = MakeObject<TextFragment>("rotated text");
	textFragment3->set_Position(MakeObject<Position>(300, 600));

	// Set text properties
	textFragment3->get_TextState()->set_FontSize(12);
	textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
	textFragment3->get_TextState()->set_Rotation(90);

	// create TextBuilder object
	auto textBuilder = MakeObject<TextBuilder>(page);
	// Append the text fragment to the PDF page
	textBuilder->AppendText(textFragment1);
	textBuilder->AppendText(textFragment2);
	textBuilder->AppendText(textFragment3);

	// Save document
	document->Save(_dataDir + u"TextFragmentTests_Rotated1_out.pdf");
}
```

## Implement Rotation using TextParagraph and TextBuilder (Rotated Fragments)

```cpp
void ImplementRotationUsingTextParagraphAndTextBuilder_RotatedFragments() {

	String _dataDir("C:\\Samples\\");

	// Initialize document object
	auto document = MakeObject<Document>();
	// Get particular page
	auto page = document->get_Pages()->Add();
	auto paragraph = MakeObject<TextParagraph>();
	paragraph->set_Position(MakeObject<Position>(200, 600));

	// Create text fragment
	auto textFragment1 = MakeObject<TextFragment>("rotated text");
	// Set text properties
	textFragment1->get_TextState()->set_FontSize(12);
	textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
	// Set rotation
	textFragment1->get_TextState()->set_Rotation(45);

	// Create text fragment
	auto textFragment2 = MakeObject<TextFragment>("main text");
	// Set text properties
	textFragment2->get_TextState()->set_FontSize(12);
	textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

	// Create text fragment
	auto textFragment3 = MakeObject<TextFragment>("another rotated text");
	// Set text properties
	textFragment3->get_TextState()->set_FontSize(12);
	textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
	// Set rotation
	textFragment3->get_TextState()->set_Rotation(-45);

	// Append the text fragments to the paragraph
	paragraph->AppendLine(textFragment1);
	paragraph->AppendLine(textFragment2);
	paragraph->AppendLine(textFragment3);
	// Create TextBuilder object
	auto textBuilder = MakeObject<TextBuilder>(page);
	// Append the text paragraph to the PDF page
	textBuilder->AppendParagraph(paragraph);
	// Save document
	document->Save(_dataDir + u"TextFragmentTests_Rotated2_out.pdf");

}
```

## Implement Rotation using TextFragment and Page.Paragraphs

```cpp
void ImplementRotationUsingTextFragmentAndPageParagraphs() {

	String _dataDir("C:\\Samples\\");

	// Initialize document object
	auto document = MakeObject<Document>();
	// Get particular page
	auto page = document->get_Pages()->Add();
	// Create text fragment
	auto textFragment1 = MakeObject<TextFragment>("main text");
	// Set text properties
	textFragment1->get_TextState()->set_FontSize(12);
	textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

	// Create text fragment
	auto textFragment2 = MakeObject<TextFragment>("rotated text");

	// Set text properties
	textFragment2->get_TextState()->set_FontSize(12);
	textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

	// Set rotation
	textFragment2->get_TextState()->set_Rotation(315);

	// Create text fragment
	auto textFragment3 = MakeObject<TextFragment>("rotated text");
	// Set text properties
	textFragment3->get_TextState()->set_FontSize(12);
	textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

	// Set rotation
	textFragment3->get_TextState()->set_Rotation(270);
	page->get_Paragraphs()->Add(textFragment1);
	page->get_Paragraphs()->Add(textFragment2);
	page->get_Paragraphs()->Add(textFragment3);

	// Save document
	document->Save(_dataDir + u"TextFragmentTests_Rotated3_out.pdf");
}
```

## Implement Rotation using TextParagraph and TextBuilder (Whole Paragraph Rotated)

```cpp
void ImplementRotationUsingTextParagraphAndTextBuilder() {

	String _dataDir("C:\\Samples\\");

	// Initialize document object
	auto document = MakeObject<Document>();
	// Get particular page
	auto page = document->get_Pages()->Add();
	for (int i = 0; i < 4; i++) {
		auto paragraph = MakeObject<TextParagraph>();
		paragraph->set_Position(MakeObject<Position>(200, 600));
		// Specify rotation
		paragraph->set_Rotation(i * 90 + 45);
		// Create text fragment
		auto textFragment1 = MakeObject<TextFragment>("Paragraph Text");
		// Create text fragment
		textFragment1->get_TextState()->set_FontSize(12);
		textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
		textFragment1->get_TextState()->set_BackgroundColor(Color::get_LightGray());
		textFragment1->get_TextState()->set_ForegroundColor(Color::get_Blue());

		// Create text fragment
		auto textFragment2 = MakeObject<TextFragment>("Second line of text");
		// Set text properties
		textFragment2->get_TextState()->set_FontSize(12);
		textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
		textFragment2->get_TextState()->set_BackgroundColor(Color::get_LightGray());
		textFragment2->get_TextState()->set_ForegroundColor(Color::get_Blue());

		// Create text fragment
		auto textFragment3 = MakeObject<TextFragment>("And some more text...");
		// Set text properties
		textFragment3->get_TextState()->set_FontSize(12);
		textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
		textFragment3->get_TextState()->set_BackgroundColor(Color::get_LightGray());
		textFragment3->get_TextState()->set_ForegroundColor(Color::get_Blue());
		textFragment3->get_TextState()->set_Underline(true);

		paragraph->AppendLine(textFragment1);
		paragraph->AppendLine(textFragment2);
		paragraph->AppendLine(textFragment3);
		// Create TextBuilder object
		auto textBuilder = MakeObject<TextBuilder>(page);
		// Append the text fragment to the PDF page
		textBuilder->AppendParagraph(paragraph);
	}
	// Save document
	document->Save(_dataDir + u"TextFragmentTests_Rotated4_out.pdf");
}
```
