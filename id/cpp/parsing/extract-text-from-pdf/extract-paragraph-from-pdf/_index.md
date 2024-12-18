---
title: Extract Paragraph from PDF 
linktitle: Extract Paragraph from PDF
type: docs
weight: 20
url: /id/cpp/extract-paragraph-from-pdf/
description: Artikel ini menjelaskan cara menggunakan ParagraphAbsorber - alat khusus di Aspose.PDF untuk mengekstrak teks dari dokumen PDF.
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Mengekstrak Teks dari dokumen PDF dalam bentuk Paragraf

Kita dapat mendapatkan teks dari dokumen PDF dengan mencari teks tertentu (menggunakan "plain text" atau "regular expressions") dari satu halaman atau seluruh dokumen, atau kita dapat mendapatkan teks lengkap dari satu halaman, rentang halaman, atau dokumen lengkap. Namun, dalam beberapa kasus, Anda perlu mengekstrak paragraf dari dokumen PDF atau teks dalam bentuk Paragraf. Kami telah mengimplementasikan fungsi untuk mencari bagian dan paragraf dalam teks halaman dokumen PDF. Kami telah memperkenalkan Kelas ParagraphAbsorber (seperti TextFragmentAbsorber dan TextAbsorber), yang dapat digunakan untuk mengekstrak paragraf dari dokumen PDF. Ada dua cara berikut yang dapat Anda gunakan dengan ParagraphAbsorber:

```cpp
static void DrawRectangleOnPage(System::SmartPtr<Rectangle> rectangle, System::SmartPtr<Page> page);
static void DrawPolygonOnPage(System::ArrayPtr<System::SmartPtr<Point>> polygon, System::SmartPtr<Page> page);
void Parsing::ExtractParagraph()
{
    // Jalur ke direktori dokumen.
    std::clog << __func__ << ": Mulai" << std::endl;
    // String untuk nama jalur
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