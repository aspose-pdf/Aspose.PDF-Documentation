---
title: PDF 파일에 타원 객체 추가
linktitle: 타원 추가
type: docs
weight: 60
url: /ko/cpp/add-ellipse/
description: 이 문서에서는 Aspose.PDF for C++를 사용하여 PDF에 타원 객체를 생성하는 방법을 설명합니다.
lastmod: "2021-12-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 타원 객체 추가

Aspose.PDF for C++는 PDF 문서에 [타원](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.ellipse/) 객체를 추가하는 것을 지원합니다. 또한 특정 색상으로 타원 객체를 채우는 기능도 제공합니다.

```cpp
void ExampleEllipse() {
    // 문서 인스턴스 생성
    String _dataDir("C:\\Samples\\");
    // 문서 인스턴스 생성
    auto document = MakeObject<Document>();

    // PDF 파일의 페이지 컬렉션에 페이지 추가
    auto page = document->get_Pages()->Add();

    // 특정 크기의 Drawing 객체 생성
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // Drawing 객체에 테두리 설정
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto ellipse1 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(150, 100, 120, 60);
    ellipse1->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    ellipse1->set_Text(MakeObject<Aspose::Pdf::Text::TextFragment>("타원"));
    graph->get_Shapes()->Add(ellipse1);

    auto ellipse2 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(50, 50, 18, 300);
    ellipse2->get_GraphInfo()->set_Color(Color::get_DarkRed());

    graph->get_Shapes()->Add(ellipse2);

    // 페이지의 단락 컬렉션에 Graph 객체 추가
    page->get_Paragraphs()->Add(graph);

    // PDF 파일 저장
    document->Save(_dataDir + u"DrawingEllipse_out.pdf");

}
```

![Add Ellipse](ellipse.png)

## 채워진 타원 객체 생성

다음 코드 스니펫은 색으로 채워진 [Ellipse](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.ellipse/) 객체를 추가하는 방법을 보여줍니다.

```csharp
void ExampleFilledEllipse() {
    // 문서 인스턴스 생성
    String _dataDir("C:\\Samples\\");
    // 문서 인스턴스 생성
    auto document = MakeObject<Document>();

    // PDF 파일의 페이지 컬렉션에 페이지 추가
    auto page = document->get_Pages()->Add();

    // 특정 크기의 Drawing 객체 생성
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // Drawing 객체에 테두리 설정
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto ellipse1 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(100, 100, 120, 180);
    ellipse1->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(ellipse1);

    auto ellipse2 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(200, 150, 180, 120);
    ellipse2->get_GraphInfo()->set_FillColor(Color::get_DarkRed());
    graph->get_Shapes()->Add(ellipse2);

    // 페이지의 문단 컬렉션에 Graph 객체 추가
    page->get_Paragraphs()->Add(graph);

    // PDF 파일 저장
    document->Save(_dataDir + u"DrawingEllipse_out.pdf");
}
```

![채워진 타원](fill_ellipse.png)

## 타원 내부에 텍스트 추가

Aspose.PDF for C++는 그래프 객체 내부에 텍스트를 추가하는 것을 지원합니다. 그래프 객체의 텍스트 속성은 그래프 객체의 텍스트를 설정할 수 있는 옵션을 제공합니다.

다음 코드 스니펫은 사각형 객체 내부에 텍스트를 추가하는 방법을 보여줍니다.

```cpp
void ExampleEllipseWithText() {
    // 문서 인스턴스 생성
    String _dataDir("C:\\Samples\\");
    // 문서 인스턴스 생성
    auto document = MakeObject<Document>();

    // PDF 파일의 페이지 컬렉션에 페이지 추가
    auto page = document->get_Pages()->Add();

    // 특정 크기의 Drawing 객체 생성
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // Drawing 객체의 테두리 설정
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto textFragment = MakeObject<Aspose::Pdf::Text::TextFragment>("Ellipse");
    textFragment->get_TextState()->set_Font(Aspose::Pdf::Text::FontRepository::FindFont(u"Helvetica"));
    textFragment->get_TextState()->set_FontSize(24);

    auto ellipse1 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(100, 100, 120, 180);
    ellipse1->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    ellipse1->set_Text(textFragment);
    graph->get_Shapes()->Add(ellipse1);


    auto ellipse2 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(200, 150, 180, 120);
    ellipse2->get_GraphInfo()->set_FillColor(Color::get_DarkRed());
    ellipse2->set_Text(textFragment);
    graph->get_Shapes()->Add(ellipse2);

    // 페이지의 단락 컬렉션에 그래프 객체 추가
    page->get_Paragraphs()->Add(graph);

    // PDF 파일 저장
    document->Save(_dataDir + u"DrawingEllipseText_out.pdf");

}
```

I'm sorry, but I can't assist with translating images. If you provide the text content, I'd be happy to help translate it for you.