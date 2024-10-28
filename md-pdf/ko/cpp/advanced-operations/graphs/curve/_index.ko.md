---
title: PDF 파일에 곡선 객체 추가
linktitle: 곡선 추가
type: docs
weight: 30
url: /cpp/add-curve/
description: 이 문서는 Aspose.PDF for C++를 사용하여 PDF에 곡선 객체를 생성하는 방법을 설명합니다.
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 곡선 객체 추가

그래프 [Curve](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.curve/)는 각각 세 개의 다른 점에서 만나는 사영선의 연결된 합집합입니다.

베지어 곡선은 컴퓨터 그래픽에서 매끄러운 곡선을 모델링하는 데 널리 사용됩니다. 곡선은 제어점의 볼록 껍질 내에 완전히 포함되어 있으며, 이 점들은 그래픽으로 표시되어 곡선을 직관적으로 조작하는 데 사용될 수 있습니다.
전체 곡선은 주어진 네 점(그들의 볼록 껍질)의 꼭짓점인 사변형 내에 포함되어 있습니다.

이 문서에서는 PDF 문서에서 생성할 수 있는 간단한 그래프 곡선 및 채워진 곡선에 대해 조사합니다.

다음 단계를 따르세요:

1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 인스턴스 생성

1. 특정 크기로 [Drawing object](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.drawing) 생성

1. Drawing 객체에 [Border](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph#ab63dde9501441515b915fd68f66a01bd) 설정

1. 페이지의 단락 컬렉션에 [Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph) 객체 추가

1. PDF 파일 저장

```cpp
void ExampleCurve() {

    // Document 인스턴스 생성
    String _dataDir("C:\\Samples\\");
    // Document 인스턴스 생성
    auto document = MakeObject<Document>();

    // PDF 파일의 페이지 컬렉션에 페이지 추가
    auto page = document->get_Pages()->Add();

    // 특정 크기로 Drawing 객체 생성
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 200);
    
    // Drawing 객체에 테두리 설정
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto curve1 = MakeObject<Aspose::Pdf::Drawing::Curve>(MakeArray<double> ({ 10, 10, 50, 60, 70, 10, 100, 120}));
    curve1->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    graph->get_Shapes()->Add(curve1);

    // 페이지의 단락 컬렉션에 Graph 객체 추가
    page->get_Paragraphs()->Add(graph);

    // PDF 파일 저장
    document->Save(_dataDir + u"DrawingCurve1_out.pdf");
}
```
다음 그림은 코드 스니펫을 실행한 결과를 보여줍니다:

![Drawing Curve](drawing_curve.png)

## 색으로 채워진 곡선 객체 생성

이 예제는 색으로 채워진 Curve 객체를 추가하는 방법을 보여줍니다.

```cpp
void ExampleFilledCurve() {

    // Document 인스턴스 생성
    String _dataDir("C:\\Samples\\");
    // Document 인스턴스 생성
    auto document = MakeObject<Document>();

    // PDF 파일의 페이지 컬렉션에 페이지 추가
    auto page = document->get_Pages()->Add();

    // 특정 크기의 Drawing 객체 생성
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 200);
    
    // Drawing 객체에 테두리 설정
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto curve1 = MakeObject<Aspose::Pdf::Drawing::Curve>(MakeArray<double>({ 10, 10, 50, 60, 70, 10, 100, 120}));
    curve1->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(curve1);

    // 페이지의 단락 컬렉션에 Graph 객체 추가
    page->get_Paragraphs()->Add(graph);

    // PDF 파일 저장
    document->Save(_dataDir + u"DrawingCurve2_out.pdf");
}
```

Look at the result of adding a filled Curve:

![채워진 곡선](filled_curve.png)