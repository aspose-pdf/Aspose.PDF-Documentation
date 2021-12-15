---
title: Extract Paragraph from PDF using C++
linktitle: Extract Paragraph from PDF
type: docs
weight: 20
url: /cpp/extract-paragraph-from-pdf/
description: This article describes how to use ParagraphAbsorber - a special tool in Aspose.PDF to extract text from PDF documents.
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extract Text from PDF document in Paragraphs form

We can get text from a PDF document by searching a particular text (using "plain text" or "regular expressions") from a single page or whole document, or we can get the complete text of a single page, range of pages or complete document. However, in some cases, you require to extract paragraphs from a PDF document or text in the form of Paragraphs. We have implemented functionality for searching sections and paragraphs in the text of PDF document pages. We have introduced ParagraphAbsorber Class (like TextFragmentAbsorber and TextAbsorber), which can be used to extract paragraphs from PDF documents. There are two following ways in which you can use ParagraphAbsorber:

```cpp
static void DrawRectangleOnPage(System::SmartPtr<Rectangle> rectangle, System::SmartPtr<Page> page);
static void DrawPolygonOnPage(System::ArrayPtr<System::SmartPtr<Point>> polygon, System::SmartPtr<Page> page);
void Parsing::ExtractParagraph()
{
    // The path to the documents directory.
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Parsing\\");

    auto doc = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = doc->get_Pages()->idx_get(1);

    auto absorber = MakeObject<ParagraphAbsorber>();
    absorber->Visit(page);

    auto markup = absorber->get_PageMarkups()->idx_get(0);

    for(auto &section : markup->get_Sections())
    {
        DrawRectangleOnPage(section->get_Rectangle(), page);
        for(auto &paragraph : section->get_Paragraphs())
        {
        DrawPolygonOnPage(paragraph->get_Points(), page);
        }
    }

    doc->Save(_dataDir + u"output_out.pdf");
}

void DrawRectangleOnPage(System::SmartPtr<Rectangle> rectangle, System::SmartPtr<Page> page)
{
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(1, 0, 0, 1, 0, 0));
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::SetRGBColorStroke>(0, 1, 0));
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::SetLineWidth>(2));
    page->get_Contents()->Add(
        MakeObject<Aspose::Pdf::Operators::Re>(
        rectangle->get_LLX(),
        rectangle->get_LLY(),
        rectangle->get_Width(),
        rectangle->get_Height()));
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ClosePathStroke>());
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());
}

void DrawPolygonOnPage(System::ArrayPtr<System::SmartPtr<Point>> polygon, System::SmartPtr<Page> page)
{
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(1, 0, 0, 1, 0, 0));
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::SetRGBColorStroke>(0, 0, 1));
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::SetLineWidth>(1));
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::MoveTo>(polygon->idx_get(0)->get_X(), polygon[0]->get_Y()));
    for (int i = 1; i < polygon->get_Length(); i++)
    {
        page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::LineTo>(polygon->idx_get(i)->get_X(), polygon[i]->get_Y()));
    }
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::LineTo>(polygon->idx_get(0)->get_X(), polygon[0]->get_Y()));
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ClosePathStroke>());
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());
}
```


