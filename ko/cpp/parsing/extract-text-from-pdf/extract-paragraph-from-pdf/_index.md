---
title: PDF에서 단락 추출 
linktitle: PDF에서 단락 추출
type: docs
weight: 20
url: /ko/cpp/extract-paragraph-from-pdf/
description: 이 문서에서는 PDF 문서에서 텍스트를 추출하기 위해 Aspose.PDF의 특별한 도구인 ParagraphAbsorber를 사용하는 방법을 설명합니다.
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 단락 형태로 PDF 문서에서 텍스트 추출

특정 텍스트("일반 텍스트" 또는 "정규 표현식" 사용)를 단일 페이지 또는 전체 문서에서 검색하여 PDF 문서에서 텍스트를 얻을 수 있으며, 단일 페이지, 페이지 범위 또는 전체 문서의 전체 텍스트를 얻을 수 있습니다. 그러나 어떤 경우에는 PDF 문서에서 문단을 추출하거나 문단 형태로 텍스트를 추출해야 합니다. 우리는 PDF 문서 페이지의 텍스트에서 섹션과 문단을 검색하는 기능을 구현했습니다. 우리는 PDF 문서에서 문단을 추출하는 데 사용할 수 있는 ParagraphAbsorber 클래스를 도입했습니다. 다음 두 가지 방법으로 ParagraphAbsorber를 사용할 수 있습니다:

```cpp
static void DrawRectangleOnPage(System::SmartPtr<Rectangle> rectangle, System::SmartPtr<Page> page);
static void DrawPolygonOnPage(System::ArrayPtr<System::SmartPtr<Point>> polygon, System::SmartPtr<Page> page);
void Parsing::ExtractParagraph()
{
    // 문서 디렉토리 경로입니다.
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름을 위한 문자열
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