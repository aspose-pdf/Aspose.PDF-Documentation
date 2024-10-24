---
title: Get and Set Page Properties
type: docs
weight: 20
url: /cpp/get-and-set-page-properties/
description: You can get and set page properties from your PDF file using C++ library.
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for C++** lets you read and set properties of pages in a PDF file in your C++ applications. This section shows how to get the number of pages in a PDF file, get information about PDF page properties such as color and set page properties, get a particular page of the PDF file and etc.

## Get Number of Pages in a PDF File

When working with documents, you often want to know how many pages they contain. With Aspose.PDF this takes no more than two lines of code.

To get the number of pages in a PDF file:

1. Open the PDF file using the [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) class.
1. Then use the [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) collection's Count property (from the Document object) to get the total number of pages in the document.

The following code snippet shows how to get the number of pages of a PDF file.

```cpp
void GetNumberOfPages() {
    // Open document
    String _dataDir("C:\\Samples\\");
    String srcFileName("GetNumberofPages.pdf");

    auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);

    // Get page count
    std::cout << "Page Count : " << srcDocument->get_Pages()->get_Count() << std::endl;
}
```

### Get page count without saving the document

Sometimes we generate the PDF files on the fly and during PDF file creation, we may come across the requirement (creating Table Of Contents etc.) to get page count of PDF file without saving the file over system or stream. So in order to cater to this requirement, a method [ProcessParagraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a1773e7b6a887eaddd602073e29939a6f) has been introduced in Document class. Please take a look over the following code snippet which shows the steps to get page count without saving the document.

```cpp
void GetPageCountWithoutSavingTheDocument() {
    // Instantiate Document instance
    auto document = MakeObject<Document>();

    // Add page to pages collection of PDF file
    auto page = document->get_Pages()->Add();
    // Create loop instance
    for (int i = 0; i < 300; i++)
        // Add TextFragment to paragraphs collection of page object
        page->get_Paragraphs()->Add(MakeObject<TextFragment>(u"Pages count test"));
    // Process the paragraphs in PDF file to get accurate page count
    document->ProcessParagraphs();
    // Print number of pages in document
    std::cout << "Number of pages in document = " << document->get_Pages()->get_Count();
}
```

## Get Page Properties

### Accessing Page Properties

The [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) class provides all the properties related to a particular PDF page. All the pages of the PDF files are contained in the of the [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) object's [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) collection.

From there, it is possible to access either individual Page objects using their index, or loop through the collection, using a foreach loop, to get all pages. Once an individual page is accessed, we can get its properties. The following code snippet shows how to get page properties.

```cpp
void AccessingPageProperties() {

    String _dataDir("C:\\Samples\\");
    String pdfDocument("GetProperties.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + pdfDocument);

    // Get particular page
    auto pdfPage = document->get_Pages()->idx_get(1);
    // Get page properties
    Console::WriteLine(u"ArtBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_ArtBox()->get_Height(), pdfPage->get_ArtBox()->get_Width(),
        pdfPage->get_ArtBox()->get_LLX(), pdfPage->get_ArtBox()->get_LLY(),
        pdfPage->get_ArtBox()->get_URX(), pdfPage->get_ArtBox()->get_URY());

    Console::WriteLine(u"->get_BleedBox() : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_BleedBox()->get_Height(), pdfPage->get_BleedBox()->get_Width(),
        pdfPage->get_BleedBox()->get_LLX(), pdfPage->get_BleedBox()->get_LLY(),
        pdfPage->get_BleedBox()->get_URX(), pdfPage->get_BleedBox()->get_URY());

    Console::WriteLine(u"get_CropBox() : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_CropBox()->get_Height(), pdfPage->get_CropBox()->get_Width(),
        pdfPage->get_CropBox()->get_LLX(), pdfPage->get_CropBox()->get_LLY(),
        pdfPage->get_CropBox()->get_URX(), pdfPage->get_CropBox()->get_URY());

    Console::WriteLine(u"get_MediaBox() : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_MediaBox()->get_Height(), pdfPage->get_MediaBox()->get_Width(),
        pdfPage->get_MediaBox()->get_LLX(), pdfPage->get_MediaBox()->get_LLY(),
        pdfPage->get_MediaBox()->get_URX(), pdfPage->get_MediaBox()->get_URY());

    Console::WriteLine(u"get_TrimBox() : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_TrimBox()->get_Height(), pdfPage->get_TrimBox()->get_Width(),
        pdfPage->get_TrimBox()->get_LLX(), pdfPage->get_TrimBox()->get_LLY(),
        pdfPage->get_TrimBox()->get_URX(), pdfPage->get_TrimBox()->get_URY());

    Console::WriteLine(u"Rect : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_Rect()->get_Height(), pdfPage->get_Rect()->get_Width(),
        pdfPage->get_Rect()->get_LLX(), pdfPage->get_Rect()->get_LLY(),
        pdfPage->get_Rect()->get_URX(), pdfPage->get_Rect()->get_URY());

    Console::WriteLine(u"Page Number : {0}", pdfPage->get_Number());
    Console::WriteLine(u"Rotate : {0}", pdfPage->get_Rotate());
}
```

