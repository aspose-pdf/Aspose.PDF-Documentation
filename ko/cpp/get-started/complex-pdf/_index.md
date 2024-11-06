---
title: 복잡한 PDF 만들기
linktitle: 복잡한 PDF 만들기
type: docs
weight: 60
url: ko/cpp/complex-pdf-example/
description: Aspose.PDF for C++를 사용하면 하나의 문서에 이미지, 텍스트 조각 및 테이블을 포함하는 더 복잡한 문서를 만들 수 있습니다.
lastmod: "2021-11-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

[Hello, World](/pdf/cpp/hello-world-example/) 예제는 C++와 Aspose.PDF를 사용하여 PDF 문서를 만드는 간단한 단계를 보여주었습니다. 이 기사에서는 C++와 Aspose.PDF for C++를 사용하여 더 복잡한 문서를 만드는 방법을 살펴보겠습니다. 예를 들어, 승객 페리 서비스를 운영하는 가상의 회사의 문서를 살펴보겠습니다.
우리의 문서에는 이미지, 두 개의 텍스트 조각 (헤더 및 단락), 그리고 테이블이 포함될 것입니다. 이러한 문서를 만들기 위해 DOM 기반 접근 방식을 사용할 것입니다. [DOM API의 기본](/pdf/cpp/basics-of-dom-api/) 섹션에서 더 많은 정보를 읽을 수 있습니다.

문서를 처음부터 만들려면 특정 단계를 따라야 합니다:

1. 
[String Class](https://reference.aspose.com/pdf/cpp/class/system.string)를 경로 이름과 파일 이름에 대해 생성합니다.
1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 객체를 인스턴스화합니다. 이 단계에서는 메타데이터는 있지만 페이지가 없는 빈 PDF 문서를 만듭니다.
1. 문서 객체에 [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)를 추가합니다. 이제 문서에 한 페이지가 추가됩니다.
1. 페이지에 [Image](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image)를 추가합니다.
1. 헤더를 위한 [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/)를 생성합니다. 헤더에는 Arial 폰트를 사용하고, 글꼴 크기는 24pt, 중앙 정렬을 사용합니다.
1. 페이지 [Paragraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#ac5c48bedc9fe8a7e0800a1d9b2c28170)에 헤더를 추가합니다.
1.
``` 
[TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/)를 설명을 위해 생성합니다. 설명을 위해 Arial 폰트를 사용하고 글꼴 크기 24pt와 중앙 정렬을 사용합니다.
1. (설명)을 페이지 단락에 추가합니다.
1. 표를 생성하고, 표 속성을 추가합니다.
1. (표)를 페이지 [Paragraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#ac5c48bedc9fe8a7e0800a1d9b2c28170)에 추가합니다.
1. 문서를 "Complex.pdf"로 저장합니다.

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
    auto header = MakeObject<TextFragment>(u"2020년 가을 새로운 페리 노선");
    auto textFragementState = header->get_TextState();
    textFragementState->set_Font(FontRepository::FindFont(u"Arial"));
    textFragementState->set_FontSize(24);
    header->set_HorizontalAlignment(HorizontalAlignment::Center);
    auto position = MakeObject<Aspose::Pdf::Text::Position>(130, 720);
    header->set_Position(position);
    page->get_Paragraphs()->Add(header);

    // Add description
    String descriptionText(u"방문객은 온라인으로 티켓을 구매해야 하며, 티켓은 하루에 5,000장으로 제한됩니다. 페리 서비스는 절반 용량으로 운영되며, 일정이 축소되었습니다. 줄을 서야 할 수 있습니다.");
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
    headerRow->get_Cells()->Add(u"출발 도시");
    headerRow->get_Cells()->Add(u"출발 섬");

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
```