---
title: Crop PDF Pages programmatically C++
linktitle: Crop Pages
type: docs
weight: 80
url: /cpp/crop-pages/
description: You may get page properties, such as the width, height, bleed-, crop- and trimbox using Aspose.PDF for C++.
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Get Page Properties

Each page in a PDF file has a number of properties, such as the width, height, bleed-, crop- and trimbox. Aspose.PDF allows you to access these properties.

- **Media box**: The media box is the largest page box. It corresponds to the page size (for example A4, A5, US Letter, etc.) selected when the document was printed to PostScript or PDF. In other words, the media box determines the physical size of the media on which the PDF document is displayed or printed.
- **Bleed box**: If the document has bleed, the PDF will also have a bleed box. Bleed is the amount of color (or artwork) that extends beyond the edge of a page. It is used to make sure that when the document is printed and cut to size ("trimmed"), the ink will go all the way to the edge of the page. Even if the page is mistrimmed - cut slightly off the trim marks - no white edges will appear on the page.
- **Trim box**: The trim box indicates the final size of a document after printing and trimming.
- **Art box**: The art box is the box drawn around the actual contents of the pages in your documents. This page box is used when importing PDF documents in other applications.
- **Crop box**: The crop box is the "page" size at which your PDF document is displayed in Adobe Acrobat. In normal view, only the contents of the crop box are displayed in Adobe Acrobat. For detailed descriptions of these properties, read the Adobe.Pdf specification, particularly 10.10.1 Page Boundaries.
- **Page.Rect**: the intersection (commonly visible rectangle) of the MediaBox and DropBox. The picture below illustrates these properties.
For further details, please visit [this page](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

The snippet below show how to crop the page:

```cpp
void CropPagesPDF()
{	
	String _dataDir("C:\\Samples\\");
	String inputFileName("crop_page.pdf");
	String outputFileName("crop_page_out.pdf");

	// Open source document
	auto document = MakeObject<Document>(_dataDir + inputFileName);

	Console::WriteLine(document->get_Pages()->idx_get(1)->get_CropBox());
	Console::WriteLine(document->get_Pages()->idx_get(1)->get_TrimBox());
	Console::WriteLine(document->get_Pages()->idx_get(1)->get_ArtBox());
	Console::WriteLine(document->get_Pages()->idx_get(1)->get_BleedBox());
	Console::WriteLine(document->get_Pages()->idx_get(1)->get_MediaBox());

	// Create new Box Rectagle
	auto newBox = MakeObject<Rectangle>(200, 220, 2170, 1520);
	document->get_Pages()->idx_get(1)->set_CropBox(newBox);
	document->get_Pages()->idx_get(1)->set_TrimBox(newBox);
	document->get_Pages()->idx_get(1)->set_ArtBox (newBox);
	document->get_Pages()->idx_get(1)->set_BleedBox (newBox);

	// Save updated document
	document->Save(_dataDir + outputFileName);
}
```

In this example we used a sample file [here](crop_page.pdf). Initially our page looks like shown on the Figure 1.
![Figure 1. Cropped Page](crop_page.png)

After the change, the page will look like Figure 2.
![Figure 2. Cropped Page](crop_page2.png)
