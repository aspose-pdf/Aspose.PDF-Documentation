---
title: Get and Set Page Properties using Python
linktitle: Get and Set Page Properties
type: docs
weight: 90
url: /python-net/get-and-set-page-properties/
description: This section shows how to get the number of pages in a PDF file, get information about PDF page properties such as color and set page properties.
lastmod: "2025-02-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to Get and Set page properties using Python
Abstract: This article discusses the capabilities of Aspose.PDF for Python via .NET, focusing on reading and setting page properties in PDF files using Python. The article covers various functionalities including determining the number of pages in a PDF, accessing and modifying page properties, and handling color information. To get the number of pages, the `Document` class and `PageCollection` collection are used, with code snippets demonstrating how to retrieve the page count, even without saving the document. The article explains different page properties such as MediaBox, BleedBox, TrimBox, ArtBox, and CropBox, and provides code examples for accessing these properties. Additionally, it covers retrieving a specific page from a PDF and saving it as a separate document, as well as determining the color type of each page. The examples throughout are implemented in Python, illustrating practical applications of these features.
---

Aspose.PDF for Python via .NET lets you read and set properties of pages in a PDF file in your Python applications. This section shows how to get the number of pages in a PDF file, get information about PDF page properties such as color and set page properties. The examples given are in Python.

## Get Number of Pages in a PDF File

When working with documents, you often want to know how many pages they contain. With Aspose.PDF this takes no more than two lines of code.

To get the number of pages in a PDF file:

1. Open the PDF file using the [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class.
1. Then use the [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) collection's Count property (from the Document object) to get the total number of pages in the document.

The following code snippet shows how to get the number of pages of a PDF file.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Get page count
    print("Page Count:", str(len(document.pages)))
```

### Get page count without saving the document

Sometimes we generate the PDF files on the fly and during PDF file creation, we may come across the requirement (creating Table Of Contents etc.) to get page count of PDF file without saving the file over system or stream. So in order to cater to this requirement, a method [process_paragraphs()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) has been introduced in Document class. Please take a look over the following code snippet which shows the steps to get page count without saving the document.

```python

    import aspose.pdf as ap

    # Instantiate Document instance
    document = ap.Document()
    # Add page to pages collection of PDF file
    page = document.pages.add()
    # Create loop instance
    for i in range(0, 300):
        # Add TextFragment to paragraphs collection of page object
        page.paragraphs.add(ap.text.TextFragment("Pages count test"))
    # Process the paragraphs in PDF file to get accurate page count
    document.process_paragraphs()
    # Print number of pages in document
    print("Number of pages in document =", str(len(document.pages)))
```

## Get Page Properties

Each page in a PDF file has a number of properties, such as the width, height, bleed-, crop- and trimbox. Aspose.PDF allows you to access these properties.

### **Understanding Page Properties: the Difference between Artbox, BleedBox, CropBox, MediaBox, TrimBox and Rect property**

- **Media box**: The media box is the largest page box. It corresponds to the page size (for example A4, A5, US Letter, etc.) selected when the document was printed to PostScript or PDF. In other words, the media box determines the physical size of the media on which the PDF document is displayed or printed.
- **Bleed box**: If the document has bleed, the PDF will also have a bleed box. Bleed is the amount of color (or artwork) that extends beyond the edge of a page. It is used to make sure that when the document is printed and cut to size (“trimmed”), the ink will go all the way to the edge of the page. Even if the page is mistrimmed - cut slightly off the trim marks - no white edges will appear on the page.
- **Trim box**: The trim box indicates the final size of a document after printing and trimming.
- **Art box**: The art box is the box drawn around the actual contents of the pages in your documents. This page box is used when importing PDF documents in other applications.
- **Crop box**: The crop box is the “page” size at which your PDF document is displayed in Adobe Acrobat. In normal view, only the contents of the crop box are displayed in Adobe Acrobat.
  For detailed descriptions of these properties, read the Adobe.Pdf specification, particularly 10.10.1 Page Boundaries.
- **Page.Rect**: the intersection (commonly visible rectangle) of the MediaBox and DropBox. The picture below illustrates these properties.

For further details, please visit [this page](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### **Accessing Page Properties**

The [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) class provides all the properties related to a particular PDF page. All the pages of the PDF files are contained in the of the [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) object's [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) collection.

From there, it is possible to access either individual Page objects using their index, or loop through the collection, using a foreach loop, to get all pages. Once an individual page is accessed, we can get its properties. The following code snippet shows how to get page properties.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Get particular page
    page = document.pages[1]
    # Get page properties
    print(
        "ArtBox : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.art_box.height,
            page.art_box.width,
            page.art_box.llx,
            page.art_box.lly,
            page.art_box.urx,
            page.art_box.ury,
        )
    )
    print(
        "BleedBox : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.bleed_box.height,
            page.bleed_box.width,
            page.bleed_box.llx,
            page.bleed_box.lly,
            page.bleed_box.urx,
            page.bleed_box.ury,
        )
    )
    print(
        "CropBox : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.crop_box.height,
            page.crop_box.width,
            page.crop_box.llx,
            page.crop_box.lly,
            page.crop_box.urx,
            page.crop_box.ury,
        )
    )
    print(
        "MediaBox : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.media_box.height,
            page.media_box.width,
            page.media_box.llx,
            page.media_box.lly,
            page.media_box.urx,
            page.media_box.ury,
        )
    )
    print(
        "TrimBox : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.trim_box.height,
            page.trim_box.width,
            page.trim_box.llx,
            page.trim_box.lly,
            page.trim_box.urx,
            page.trim_box.ury,
        )
    )
    print(
        "Rect : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.rect.height,
            page.rect.width,
            page.rect.llx,
            page.rect.lly,
            page.rect.urx,
            page.rect.ury,
        )
    )
    print("Page Number :", page.number)
    print("Rotate :", page.rotate)
```

## Get a Particular Page of the PDF File

Aspose.PDF for Python allows you to [split a PDF into individual pages](/pdf/python-net/split-pdf-document/) and save them as PDF files. Getting a specified page in a PDF file and saving it as a new PDF is a very similar operation: open the source document, access the page, create a new document and add the page to this.

The [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document) object's [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection) holds the pages in the PDF file. To get a particular page from this collection:

1. Specify the page index using the Pages property.
1. Create a new [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) object.
1. Add the [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) object to the new Document object.
1. Save the output using [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method.

The following code snippet shows how to get a particular page from a PDF file and save it as a new file.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Get particular page
    page = document.pages[2]

    # Save the page as PDF file
    new_document = ap.Document()
    new_document.pages.add(page)
    new_document.save(output_pdf)
```

## Determine Page Color

The [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) class provides the properties related to a particular page in a PDF document, including what type of colour - RGB, black and white, grayscale or undefined - the page uses.

All the pages of the PDF files are contained by the [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) collection. The [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) property specifies the color of elements on page. To get or determine the color information for particular PDF page, use the [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) object's [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) property.

The following code snippet shows how to iterate through individual page of PDF file to get color information.

```python

    import aspose.pdf as ap

    # Open source PDF file
    document = ap.Document(input_pdf)
    # Iterate through all the page of PDF file
    for page_n in range(0, len(document.pages)):
        page_number = page_n + 1
        # Get the color type information for particular PDF page
        page_color_type = document.pages[page_number].color_type
        if page_color_type == ap.ColorType.BLACK_AND_WHITE:
            print("Page # " + str(page_number) + " is Black and white.")

        if page_color_type == ap.ColorType.GRAYSCALE:
            print("Page # " + str(page_number) + " is Gray Scale.")

        if page_color_type == ap.ColorType.RGB:
            print("Page # " + str(page_number) + " is RGB.")

        if page_color_type == ap.ColorType.UNDEFINED:
            print("Page # " + str(page_number) + " Color is undefined.")
```

