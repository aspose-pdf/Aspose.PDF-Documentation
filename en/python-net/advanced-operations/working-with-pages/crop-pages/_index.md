---
title: Crop PDF Pages programmatically Python
linktitle: Crop Pages
type: docs
weight: 70
url: /python-net/crop-pages/
description: You may get page properties, such as the width, height, bleed-, crop- and trimbox using Aspose.PDF for Python via .NET.
lastmod: "2025-02-27"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to crop PDF Pages programmatically Python
Abstract: This article, authored and published by the Aspose.PDF Doc Team, provides a beginner-level guide on how to programmatically crop PDF pages using Python through the Aspose.PDF for Python via .NET library. It explains the various properties of a PDF page, such as media box, bleed box, trim box, art box, and crop box, which define the dimensions and boundaries of the page content. The article includes a code snippet demonstrating how to adjust these properties to crop a PDF page effectively. It also provides visual examples showing the effects of cropping on a sample PDF page. Additionally, the article highlights the features of the Aspose.PDF library, including compatibility with multiple operating systems and its availability for download, along with pricing and contact information for the publisher.
---

## Get Page Properties

Each page in a PDF file has a number of properties, such as the width, height, bleed-, crop- and trimbox. Aspose.PDF for Python allows you to access these properties.

- **media_box**: The media box is the largest page box. It corresponds to the page size (for example A4, A5, US Letter, etc.) selected when the document was printed to PostScript or PDF. In other words, the media box determines the physical size of the media on which the PDF document is displayed or printed.
- **bleed_box**: If the document has bleed, the PDF will also have a bleed box. Bleed is the amount of color (or artwork) that extends beyond the edge of a page. It is used to make sure that when the document is printed and cut to size ("trimmed"), the ink will go all the way to the edge of the page. Even if the page is mistrimmed - cut slightly off the trim marks - no white edges will appear on the page.
- **trim_box**: The trim box indicates the final size of a document after printing and trimming.
- **art_box**: The art box is the box drawn around the actual contents of the pages in your documents. This page box is used when importing PDF documents in other applications.
- **crop_box**: The crop box is the "page" size at which your PDF document is displayed in Adobe Acrobat. In normal view, only the contents of the crop box are displayed in Adobe Acrobat. For detailed descriptions of these properties, read the Adobe.Pdf specification, particularly 10.10.1 Page Boundaries.

The snippet below show how to crop the page:

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)

    # Create new Box Rectagle
    new_box = ap.Rectangle(200, 220, 2170, 1520, True)
    document.pages[1].crop_box = new_box
    document.pages[1].trim_box = new_box
    document.pages[1].art_box = new_box
    document.pages[1].bleed_box = new_box

    document.save(output_pdf)
```

In this example we used a sample file [here](crop_page.pdf). Initially our page looks like shown on the Figure 1.
![Figure 1. Cropped Page](crop_page.png)

After the change, the page will look like Figure 2.
![Figure 2. Cropped Page](crop_page2.png)

