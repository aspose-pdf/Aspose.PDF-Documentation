---
title: PDF 파일에 원 객체 추가
linktitle: 원 추가
type: docs
weight: 20
url: /ko/cpp/add-circle/
description: 이 문서에서는 Aspose.PDF for C++를 사용하여 PDF에 원 객체를 생성하는 방법을 설명합니다.
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 원 객체 추가

막대 그래프처럼 원 그래프는 여러 개의 별도 카테고리의 데이터를 표시하는 데 사용할 수 있습니다. 하지만 막대 그래프와 달리, 원 그래프는 전체를 구성하는 모든 카테고리에 대한 데이터가 있을 때만 사용할 수 있습니다. 이제 Aspose.PDF for C++로 [원](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.circle/) 객체를 추가하는 방법을 살펴보겠습니다.

다음 단계를 따르세요:

1. [문서](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 인스턴스 생성

1. 특정 크기로 [그리기 객체](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.drawing) 생성

1. [그리기](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph#ab63dde9501441515b915fd68f66a01bd) 객체에 대한 테두리 설정

1. 페이지의 단락 컬렉션에 [그래프](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph) 객체 추가

1. PDF 파일 저장

```cpp
void ExampleCircle() {

    // 문서 인스턴스 생성
    String _dataDir("C:\\Samples\\");
    // 문서 인스턴스 생성
    auto document = MakeObject<Document>();

    // PDF 파일의 페이지 컬렉션에 페이지 추가
    auto page = document->get_Pages()->Add();

    // 특정 크기로 그리기 객체 생성
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 200);
    // 그리기 객체에 테두리 설정
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto circle = MakeObject<Aspose::Pdf::Drawing::Circle>(100, 100, 40);

    circle->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    graph->get_Shapes()->Add(circle);

    // 페이지의 단락 컬렉션에 그래프 객체 추가
    page->get_Paragraphs()->Add(graph);

    // PDF 파일 저장
    document->Save(_dataDir + u"DrawingCircle1_out.pdf");
}
```
우리의 그려진 원은 다음과 같이 보일 것입니다:

![원 그리기](drawing_circle.png)

## 채워진 원 객체 생성

이 예제는 색으로 채워진 Circle 객체를 추가하는 방법을 보여줍니다.

```cpp
void ExampleFilledCircle() {
    // Document 인스턴스 생성
    String _dataDir("C:\\Samples\\");
    // Document 인스턴스 생성
    auto document = MakeObject<Document>();

    // 페이지를 PDF 파일의 페이지 컬렉션에 추가
    auto page = document->get_Pages()->Add();

    // 특정 치수로 Drawing 객체 생성
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 200);
    
    // Drawing 객체에 경계 설정
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto circle = MakeObject<Aspose::Pdf::Drawing::Circle>(100, 100, 40);
    circle->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    circle->get_GraphInfo()->set_FillColor(Color::get_Green());

    circle->set_Text(MakeObject<Aspose::Pdf::Text::TextFragment>(u"Circle"));

    graph->get_Shapes()->Add(circle);

    // 페이지의 문단 컬렉션에 Graph 객체 추가
    page->get_Paragraphs()->Add(graph);

    // PDF 파일 저장
    document->Save(_dataDir + u"DrawingCircle2_out.pdf");
}
```

```
Let's see the result of adding a filled Circle:

![채워진 원](filled_circle.png)
```