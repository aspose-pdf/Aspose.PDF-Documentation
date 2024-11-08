---
title: PDFから段落を抽出 
linktitle: PDFから段落を抽出
type: docs
weight: 20
url: /ja/cpp/extract-paragraph-from-pdf/
description: この記事では、Aspose.PDFの特別なツールであるParagraphAbsorberを使用して、PDFドキュメントからテキストを抽出する方法について説明します。
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 段落形式でPDFドキュメントからテキストを抽出

特定のテキストを検索することによって（「プレーンテキスト」または「正規表現」を使用）、単一のページまたは全体のドキュメントからPDFドキュメントのテキストを取得することができます。また、単一のページ、ページの範囲、または完全なドキュメントの全テキストを取得することもできます。 しかし、場合によっては、PDFドキュメントから段落を抽出したり、段落の形式でテキストを抽出する必要があります。PDFドキュメントのページのテキスト内のセクションや段落を検索する機能を実装しました。PDFドキュメントから段落を抽出するために使用できるParagraphAbsorberクラス（TextFragmentAbsorberやTextAbsorberのようなもの）を導入しました。ParagraphAbsorberを使用するには、次の2つの方法があります：

```cpp
static void DrawRectangleOnPage(System::SmartPtr<Rectangle> rectangle, System::SmartPtr<Page> page);
static void DrawPolygonOnPage(System::ArrayPtr<System::SmartPtr<Point>> polygon, System::SmartPtr<Page> page);
void Parsing::ExtractParagraph()
{
    // ドキュメントディレクトリへのパス。
    std::clog << __func__ << ": Start" << std::endl;
    // パス名の文字列
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