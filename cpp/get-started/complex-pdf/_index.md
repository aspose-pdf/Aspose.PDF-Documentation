---
title: Creating a complex PDF using Aspose.PDF
linktitle: Creating a complex PDF
type: docs
weight: 30
url: /cpp/complex-pdf-example/
description: Aspose.PDF for NET allows you to create more complex documents that contain images, text fragments, and tables in one document.
lastmod: "2021-11-01"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

The [Hello, World](/pdf/cpp/hello-world-example/) example showed simple steps to create a PDF document using C# and Aspose.PDF. In this article, we will take a look at creating a more complex document with C# and Aspose.PDF for .NET. As an example, we'll take a document from a fictitious company that operates passenger ferry services.
Our document will contain a image, two text fragments (header and paragraph), and a table. To build such a document, we will use DOM-base approach. You can read more in section [Basics of DOM API](/pdf/cpp/basics-of-dom-api/).

If we create a document from scratch we need to follow certain steps:

1. Instantiate a [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document) object. In this step we will create an empty PDF document with some metadata but without pages.
1. Add a [Page](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.page) to the document object. So, now our document will have one page.
1. Add a [Image](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.image) to the Page.
1. Create a [TextFragment](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment) for header. For the header we will use Arial font with font size 24pt and center alignment.
1. Add header to the page [Paragraphs](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.paragraphs).
1. Create a [TextFragment](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment) for description. For the description we will use Arial font with font size 24pt and center alignment.
1. Add (description) to the page Paragraphs.
1. Create a table, add table properties.
1. Add (table) to the page [Paragraphs](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.paragraphs).
1. Save a document "Complex.pdf".

```cpp
void ExampleComplex()
{
    String outputFileName;

    // String for path name.
    String _dataDir("C:\\Samples\\");

    // String for file name.
    String filename("Complex.pdf");

    // Initialize document object
    auto document = MakeObject<Document>();
    // Add page
    auto page = document->get_Pages()->Add();

    // Add image
    String imageFileName = _dataDir + String(u"logo.png");

    // Add image to Images collection of Page Resources
    auto rectangle = MakeObject<Rectangle>(20, 730, 120, 830);
    page->AddImage(imageFileName, rectangle);

    // Add Header
    auto header = MakeObject<TextFragment>(u"New ferry routes in Fall 2020");
    auto textFragementState = header->get_TextState();
    textFragementState->set_Font(FontRepository::FindFont(u"Arial"));
    textFragementState->set_FontSize(24);
    header->set_HorizontalAlignment(HorizontalAlignment::Center);
    auto position = MakeObject<Aspose::Pdf::Text::Position>(130, 720);
    header->set_Position(position);
    page->get_Paragraphs()->Add(header);

    // Add description
    String descriptionText(u"Visitors must buy tickets online and tickets are limited to 5,000 per day. Ferry service is operating at half capacity and on a reduced schedule. Expect lineups.");
    auto description = MakeObject<TextFragment>(descriptionText);
    description->get_TextState()->set_Font(FontRepository::FindFont(u"Times New Roman"));
    description->get_TextState()->set_FontSize(14);
    description->set_HorizontalAlignment(HorizontalAlignment::Left);
    page->get_Paragraphs()->Add(description);

    // Add table
    auto table = MakeObject<Table>();
    table->set_ColumnWidths(u"200");

    table->set_Border(MakeObject<BorderInfo>(Aspose::Pdf::BorderSide::Box, 1.0f, Aspose::Pdf::Color::get_DarkSlateGray()));
    table->set_DefaultCellBorder(MakeObject<BorderInfo>(Aspose::Pdf::BorderSide::Box, .5f, Aspose::Pdf::Color::get_Black()));
    table->get_Margin()->set_Bottom(10);
    table->get_DefaultCellTextState()->set_Font(FontRepository::FindFont(u"Helvetica"));

    auto headerRow = table->get_Rows()->Add();
    headerRow->get_Cells()->Add(u"Departs City");
    headerRow->get_Cells()->Add(u"Departs Island");

    for (auto headerRowCell : headerRow->get_Cells())
    {
        headerRowCell->set_BackgroundColor(Color::get_Gray());
        headerRowCell->get_DefaultCellTextState()->set_ForegroundColor(Color::get_WhiteSmoke());
    }

    String arrivals[10] = { u"6:00",u"6:45", u"7:00", u"7:45", u"8:00", u"8:45", u"9:00", u"9:45", u"10:00", u"10:45" };
    String departures[10] = { u"7:00", u"7:45", u"8:00", u"8:45", u"9:00", u"9:45", u"10:00", u"10:45", u"11:00", u"11:45" };

    for (int i = 0; i < 10; i++)
    {
        auto dataRow = table->get_Rows()->Add();
        dataRow->get_Cells()->Add(arrivals[i]);
        dataRow->get_Cells()->Add(departures[i]);
    }

    page->get_Paragraphs()->Add(table);

    // Save updated PDF
    outputFileName = _dataDir + filename;

    document->Save(outputFileName);
}
```
