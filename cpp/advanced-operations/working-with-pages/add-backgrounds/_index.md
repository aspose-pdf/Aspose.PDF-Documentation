---
title: Add background to PDF with C++
linktitle: Add backgrounds
type: docs
weight: 110
url: /cpp/add-backgrounds/
descriptions: Add background image to the your PDF file with C++. Use the BackgroundArtifact object.
lastmod: "2021-12-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Adding a background to PDF files helps to improve the overall readability of the document. The content in the PDF is more engaging and readers will take notice if you have a good appearance of the document. The background can also be used to highlight the highlights of the PDF.

Background images can be used to add a watermark, or other subtle design, to documents. In Aspose.PDF for С++, each PDF document is a collection of pages and each page contains a collection of artifacts. The [BackgroundArtifact](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.background_artifact) class can be used to add a background image to a page object.

The following code snippet shows how to add a background image to PDF pages using the BackgroundArtifact object with C++.

```cpp
void WorkingWithPages::AddBackgrounds()
{
	String _dataDir("C:\\Samples\\");

	// Create a new Document object
	auto document = MakeObject<Document>();

	// Add a new page to document object
	auto page = document->get_Pages()->Add();

	// Create Background Artifact object
	auto background = MakeObject<BackgroundArtifact>();

	// Specify the image for backgroundartifact object
	background->set_BackgroundImage(System::IO::File::OpenRead(_dataDir + u"background.png"));

	// Add backgroundartifact to artifacts collection of page
	page->get_Artifacts()->Add(background);

	// Save the document
	document->Save(_dataDir + u"ImageAsBackground_out.pdf");
}
```
