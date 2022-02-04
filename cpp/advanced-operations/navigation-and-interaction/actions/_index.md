---
title: Working with Actions in PDF 
linktitle: Actions
type: docs
weight: 20
url: /cpp/actions/
description: This section explains how to add actions to the document and form fields programmatically with C++. 
lastmod: "2022-01-25"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Add Hyperlink in a PDF File

PDF documents are a great way to share information. They are easy to read, edit and distribute. However, creating links in a PDF document can be challenging. Let's show you how.

It is possible to add hyperlinks to PDF files, either to allow readers to navigate to another part of the PDF, or to external content.

For example, you may want to add a clickable table of contents to your ebooks, cite outside resources for your article, or quickly navigate the reader to a different page on the website to get more information on a subject.

To create hyperlinks with a few clicks, follow these simple steps:

1. Create a [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document) Class object.
1. Get the [Page](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.page) Class you want to add the link to.
1. Create a [LinkAnnotation](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) object using the Page and [Rectangle](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle/) objects. The rectangle object is used to specify the location on the page where the link should be added.
1. Set the Action property to the [GoToURIAction](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_u_r_i_action) object which specifies the location of the remote URI.
1. To display a hyperlink text, add a text string on a location similar to where the [LinkAnnotation](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation) object is placed.
1. To add a free text:

- Instantiate an [FreeTextAnnotation](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.free_text_annotation) object. It also accepts Page and Rectangle objects as argument, so it is possible to provide same values as specified against the LinkAnnotation constructor.
- Using the [FreeTextAnnotation](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.free_text_annotation) object’s Contents property, specify the string that should be displayed in the output PDF.
- Optionally, set the border width of both the [LinkAnnotation](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) and FreeTextAnnotation objects to 0 so that they do not appear in the PDF document.
- Once the [LinkAnnotation](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) and [FreeTextAnnotation](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.free_text_annotation) objects have been defined, add these links to the [Page](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.page) object’s Annotations collection.
- Finally, save the updated PDF using the [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document) object's Save method.

The following code snippet shows you how to add a hyperlink to a PDF file.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddHyperlinkInPDFFile() {
	String _dataDir("C:\\Samples\\");
	// Open document
	auto document = MakeObject<Document>(_dataDir + u"AddHyperlink.pdf");
	// Create link
	auto page = document->get_Pages()->idx_get(1);
	// Create Link annotation object
	auto link = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, MakeObject<Rectangle>(100, 100, 300, 300));
	// Create border object for LinkAnnotation
	auto border = MakeObject<Aspose::Pdf::Annotations::Border>(link);
	// Set the border width value as 0
	border->set_Width(0);
	// Set the border for LinkAnnotation
	link->set_Border(border);
	// Specify the link type as remote URI
	link->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToURIAction>("www.aspose.com"));
	// Add link annotation to annotations collection of first page of PDF file
	page->get_Annotations()->Add(link);

	// Create Free Text annotation
	auto textAnnotation = MakeObject<Aspose::Pdf::Annotations::FreeTextAnnotation>(
		page,
		MakeObject<Rectangle>(100, 100, 300, 300),
		MakeObject<Aspose::Pdf::Annotations::DefaultAppearance>(
			FontRepository::FindFont(u"TimesNewRoman"), 10, Color::get_Blue()));

	// String to be added as Free text
	textAnnotation->set_Contents(u"Link to Aspose website");
	// Set the border for Free Text Annotation
	textAnnotation->set_Border(border);
	// Add FreeText annotation to annotations collection of first page of Document
	page->get_Annotations()->Add(textAnnotation);

	// Save updated document
	document->Save(_dataDir + u"AddHyperlink_out.pdf");

}
```

## Create Hyperlink to pages in same PDF

Aspose.PDF for C++ provides a great feature to PDF creation as well as its manipulation. It also offers the feature to add links to PDF pages and a link can either direct to pages in another PDF file, a web URL, link to launch an Application or even link to pages in same PDF file. In order to add local hyperlinks (links to pages in same PDF file), a class named [LocalHyperlink](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.local_hyperlink) is added to Aspose.PDF namespace and this class has a property named TargetPageNumber, which is used to specify the target/destination page for hyperlink.

In order to add the local hyperlink, we need to create a TextFragment so that link can be associated with the TextFragment. The [TextFragment](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment) class has a property named Hyperlink which is used to associate LocalHyperlink instance. The following code snippet shows the steps to accomplish this requirement.

```cpp
void CreateHyperlinkToPagesInSamePDF() {
	String _dataDir("C:\\Samples\\");

	// Create Document instance
	auto document = MakeObject<Document>();

	// Add page to pages collection of PDF file
	auto page = document->get_Pages()->Add();

	// Create Text Fragment instance
	auto text = MakeObject<TextFragment>(u"link page number test to page 2");

	// Create local hyperlink instance
	auto link = MakeObject<LocalHyperlink>();

	// Set target page for link instance
	link->set_TargetPageNumber(2);

	// Set TextFragment hyperlink
	text->set_Hyperlink(link);

	// Add text to paragraphs collection of Page
	page->get_Paragraphs()->Add(text);

	// Create new TextFragment instance
	text = new TextFragment(u"link page number test to page 1");

	// TextFragment should be added over new page
	text->set_IsInNewPage(true);

	// Create another local hyperlink instance
	link = new LocalHyperlink();

	// Set Target page for second hyperlink
	link->set_TargetPageNumber(1);

	// Set link for second TextFragment
	text->set_Hyperlink(link);

	// Add text to paragraphs collection of page object
	page->get_Paragraphs()->Add(text);

	// Save updated document
	document->Save(_dataDir + u"CreateLocalHyperlink_out.pdf");
}
```

## Get PDF Hyperlink Destination (URL)

Links are represented as annotations in a PDF file and they can be added, updated or deleted. Aspose.PDF for C++ also supports getting the destination (URL) of the hyperlink in PDF file.

To get a link’s URL:

1. Create a [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document) object.
1. Get the [Page](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.page) you want to extract links from.
1. Use the [AnnotationSelector](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) class to extract all the [LinkAnnotation](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation) objects from the specified page.
1. Pass the [AnnotationSelector](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) object to the [Page](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.page) object’s Accept method.
1. Get all the selected link annotations into an IList object using the [AnnotationSelector](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) object’s Selected property.
1. Finally, extract the LinkAnnotation Action as GoToURIAction.

The following code snippet shows how to get hyperlink destinations (URL) from a PDF file.

```cpp
void GetPDFHyperlinkDestination() {
	String _dataDir("C:\\Samples\\");

	auto document = new Document(_dataDir + u"Aspose-app-list.pdf");
	// Extract actions
	auto page = document->get_Pages()->idx_get(1);

	auto selector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
		MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial()));
	page->Accept(selector);

	auto list = selector->get_Selected();
	// Iterate through individual item inside list
	if (list->get_Count() == 0)
		Console::WriteLine(u"No Hyperlinks found...");
	else {
		// Loop through all the bookmarks
		for (auto annot : list) {
			auto la = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(annot);
			if (la != nullptr) {
				auto action = System::DynamicCast<Aspose::Pdf::Annotations::GoToURIAction>(la->get_Action());
				// Print the destination URL
				Console::WriteLine(u"Destination: " + action->get_URI());
			}
		}
	} // end else
}
```

## Get Hyperlink Text

A hyperlink has two parts: the text that shows in the document, and the destination URL. In some cases, it’s the text rather than the URL we need.

Text and annotations/actions in a PDF file are represented by different entities. Text on a page is just a set of words and characters, while annotations bring some interactivity such as that inherent in a hyperlink.

To find the URL content, you need to work with both annotation and text. The [Annotation](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation) object does not have itself have the text but sits under the text on the page. So to get the text, the Annotation gives the URL’s bounds, while the Text object gives the URL contents. Please see the following code snippet.

```cpp
  void GetHyperlinkText() {
	String _dataDir("C:\\Samples\\");
	auto document = MakeObject<Document>(_dataDir + u"aspose-app-list.pdf");
	// Extract actions
	auto page = document->get_Pages()->idx_get(1);

	for (auto annot : page->get_Annotations()) {
		auto la = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(annot);
		if (la != nullptr) {
			// Print the URL of each Link Annotation
			auto action = System::DynamicCast<Aspose::Pdf::Annotations::GoToURIAction>(la->get_Action());
			Console::WriteLine(u"URI: " + action->get_URI());

			auto absorber = MakeObject<TextAbsorber>();
			absorber->get_TextSearchOptions()->set_LimitToPageBounds(true);
			absorber->get_TextSearchOptions()->set_Rectangle(annot->get_Rect());
			page->Accept(absorber);
			String extractedText = absorber->get_Text();
			// Print the text associated with hyperlink
			Console::WriteLine(extractedText);
		}
	}
}
```

## Remove Document Open Action from a PDF File

[How to Specify PDF Page when Viewing Document](#how-to-specify-pdf-page-when-viewing-document) explained how to tell a document to open on a different page than the first. When concatenating several documents, and one or more has a GoTo action set, you probably want to remove them. For example, if combining two documents and the second one has a GoTo action that takes you to the second page, the output document will open on the second page of the second document instead of the first page of the combined document. To avoid this behavior, remove the open action command.

To remove an open action:

1. Set the [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document) object’s [OpenAction](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document#a24b876bb6bee957feac48ac8031dc28e) property to null.
1. Save the updated PDF using the Document object’s Save  method.

The following code snippet shows how to remove a document open action from the PDF file.

```cpp
void RemoveDocumentOpenActionFromPDFFile()
{
	String _dataDir("C:\\Samples\\");
	// Open document
	auto document = new Document(_dataDir + u"RemoveOpenAction.pdf");
	// Remove document open action
	document->set_OpenAction(nullptr);

	// Save updated document
	document->Save(_dataDir + u"RemoveOpenAction_out.pdf");
}
```

## How to Specify PDF Page when Viewing Document {#how-to-specify-pdf-page-when-viewing-document}

When viewing PDF files in a PDF viewer such as Adobe Reader, the files usually open on the first page. However, it is possible to set the file to open on a different page.

The 'XYZExplicitDestination' class allows you to specify a page in a PDF file that you want to open. When passing the GoToAction object value to the [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document) class OpenAction property, the document opens at the page specified against the XYZExplicitDestination object. The following code snippet shows how to specify a page as the document open action.

```cpp
void HowToSpecifyPDFPageWhenViewingDocument()
{
	String _dataDir("C:\\Samples\\");
	// Load the PDF file
	auto document = new Document(_dataDir + u"SpecifyPageWhenViewing.pdf");
	// Get the instance of second page of document
	auto page2 = document->get_Pages()->idx_get(2);
	// Create the variable to set the zoom factor of target page
	double zoom = 1;
	// Create GoToAction instance
	auto action = MakeObject<Aspose::Pdf::Annotations::GoToAction>(page2);
	// Go to 2 page
	action->set_Destination(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(page2, 0, page2->get_Rect()->get_Height(), zoom));
	// Set the document open action
	document->set_OpenAction(action);
	// Save updated document
	document->Save(_dataDir + u"goto2page_out.pdf");
}
```
