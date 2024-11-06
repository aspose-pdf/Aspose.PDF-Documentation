---
title: PDF 파일에 호 객체 추가
linktitle: 호 추가
type: docs
weight: 10
url: ko/cpp/add-arc/
description: 이 문서는 Aspose.PDF for C++를 사용하여 PDF에 호 객체를 생성하는 방법을 설명합니다.
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 호 객체 추가

Aspose.PDF for C++는 그래프 객체(예: 그래프, 선, 사각형 등)를 PDF 문서에 추가하는 기능을 지원합니다. 또한 특정 색상으로 [호](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.arc) 객체를 채우는 기능도 제공합니다.

아래의 단계를 따르세요:

1. [문서](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 인스턴스 생성

1. 특정 크기의 [드로잉 객체](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.drawing) 생성

1. 드로잉 객체의 [테두리](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph#ab63dde9501441515b915fd68f66a01bd) 설정

1. [Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph) 객체를 페이지의 단락 컬렉션에 추가

1. PDF 파일 저장

다음 코드 스니펫은 [Arc](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.arc/) 객체를 추가하는 방법을 보여줍니다.

```cpp
void ExampleArc() {
    // Document 인스턴스 생성
    String _dataDir("C:\\Samples\\");
    // Document 인스턴스 생성
    auto document = MakeObject<Document>();

    // PDF 파일의 페이지 컬렉션에 페이지 추가
    auto page = document->get_Pages()->Add();

    // 특정 크기의 Drawing 객체 생성
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // Drawing 객체에 테두리 설정
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto arc1 = MakeObject<Aspose::Pdf::Drawing::Arc>(100, 100, 95, 0, 90);
    arc1->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    graph->get_Shapes()->Add(arc1);

    auto arc2 = MakeObject<Aspose::Pdf::Drawing::Arc>(100, 100, 90, 70, 180);
    arc2->get_GraphInfo()->set_Color(Color::get_DarkBlue());
    graph->get_Shapes()->Add(arc2);

    auto arc3 = MakeObject<Aspose::Pdf::Drawing::Arc>(100, 100, 85, 120, 210);
    arc3->get_GraphInfo()->set_Color(Color::get_Red());
    graph->get_Shapes()->Add(arc3);

    // Graph 객체를 페이지의 단락 컬렉션에 추가
    page->get_Paragraphs()->Add(graph);

    // PDF 파일 저장
    document->Save(_dataDir + u"DrawingArc_out.pdf");

}
```
## 채워진 호 객체 만들기

다음 예제는 색상과 특정 치수로 채워진 호 객체를 추가하는 방법을 보여줍니다.

```cpp
void ExampleFilledArc() {

    // Document 인스턴스 생성
    String _dataDir("C:\\Samples\\");
    // Document 인스턴스 생성
    auto document = MakeObject<Document>();

    // PDF 파일의 페이지 컬렉션에 페이지 추가
    auto page = document->get_Pages()->Add();

    // 특정 치수로 Drawing 객체 생성
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // Drawing 객체에 경계 설정
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto arc = MakeObject<Aspose::Pdf::Drawing::Arc>(100, 100, 95, 0, 90);
    arc->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(arc);

    auto line = MakeObject<Aspose::Pdf::Drawing::Line>(MakeArray<double>({ 195, 100, 100, 100, 100, 195 }));
    line->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(line);

    // 페이지의 단락 컬렉션에 Graph 객체 추가
    page->get_Paragraphs()->Add(graph);

    // PDF 파일 저장
    document->Save(_dataDir + u"DrawingArc_out.pdf");

}
```

```
Let's see the result of adding a filled Arс:

![Filled Arc](filled_arc.png)
```

결과를 확인해봅시다:

![채워진 호](filled_arc.png)