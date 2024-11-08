---
title: PDF 파일에 선 객체 추가
linktitle: 선 추가
type: docs
weight: 40
url: /ko/cpp/add-line/
description: 이 문서에서는 Aspose.PDF for C++를 사용하여 PDF에 선 객체를 추가하는 방법을 설명합니다.
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 선 객체 추가

Aspose.PDF for C++는 PDF 문서에 그래프 객체(예: 그래프, 선, 직사각형 등)를 추가하는 기능을 지원합니다. 또한 선 요소에 대한 대시 패턴, 색상 및 기타 서식을 지정할 수 있는 [Line](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.line/) 객체를 추가할 수 있는 이점도 제공합니다.

다음 단계를 따르세요:

1. 새 PDF [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) 생성

1. PDF 파일의 페이지 컬렉션에 [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page/) 추가

1. [Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph/) 인스턴스 생성

1. 페이지 인스턴스의 단락 컬렉션에 그래프 객체 추가

1. [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) 인스턴스를 생성합니다.

1. 선 너비를 설정합니다.

1. [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) 객체를 Graph 객체의 도형 컬렉션에 추가합니다.

1. PDF 파일을 저장합니다.

다음 코드 조각은 색으로 채워진 [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) 객체를 추가하는 방법을 보여줍니다.

```cpp

void AddLineObjectToPDF()
{

String _dataDir("C:\\Samples\\");

// 문서 인스턴스를 생성합니다.

auto document = MakeObject<Document>();


// PDF 파일의 페이지 컬렉션에 페이지를 추가합니다.

auto page = document->get_Pages()->Add();


// 그래프 인스턴스를 생성합니다.

auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(100, 400);


// 페이지 인스턴스의 단락 컬렉션에 그래프 객체를 추가합니다.

page->get_Paragraphs()->Add(graph);


// 사각형 인스턴스를 생성합니다.

auto line = MakeObject<Aspose::Pdf::Drawing::Line>(new float[] { 100, 100, 200, 100 });



// 그래프 객체의 채우기 색상을 지정합니다.

line->get_GraphInfo()->set_DashArray (MakeArray<int>({ 0, 1, 0 }));

line->get_GraphInfo()->set_DashPhase (1);



// 그래프 객체의 도형 컬렉션에 사각형 객체를 추가합니다.

graph->get_Shapes()->Add(line);



// PDF 파일을 저장합니다.

document->Save(_dataDir + u"AddLineObject_out.pdf");
}

```
![Add Line](add_line.png)

## PDF 문서에 점선 추가하는 방법

```cpp
void DashLengthInBlackAndDashLengthInWhite()
{

String _dataDir("C:\\Samples\\");

// Document 인스턴스 생성

auto document = MakeObject<Document>();


// PDF 파일의 페이지 컬렉션에 페이지 추가

auto page = document->get_Pages()->Add();


// 특정 크기로 Drawing 객체 생성

auto canvas = MakeObject<Aspose::Pdf::Drawing::Graph>(100, 400);

// 페이지 인스턴스의 단락 컬렉션에 Drawing 객체 추가

page->get_Paragraphs()->Add(canvas);



// Line 객체 생성

auto line = MakeObject<Aspose::Pdf::Drawing::Line>(MakeArray<float>({ 100, 100, 200, 100 }));

// Line 객체에 색상 설정

line->get_GraphInfo()->set_Color (Aspose::Pdf::Color::get_Red());

// Line 객체에 대시 배열 지정

line->get_GraphInfo()->set_DashArray(MakeArray<int>({ 0, 1, 0 }));

// Line 인스턴스의 대시 위상 설정

line->get_GraphInfo()->set_DashPhase(1);

// Drawing 객체의 도형 컬렉션에 Line 추가

canvas->get_Shapes()->Add(line);


// PDF 파일 저장

document->Save(_dataDir + u"DashLength_out.pdf");
}
```

결과를 확인해 봅시다:

![Dashed Line](dash_line.png)

## 페이지 가로로 선 그리기

라인 객체를 사용하여 왼쪽-아래에서 오른쪽-위 모서리 및 왼쪽-위 모서리에서 오른쪽-아래 모서리로 시작하는 십자가를 그릴 수도 있습니다.

이 요구 사항을 충족하기 위해 다음 코드 조각을 확인하십시오.

```cpp
void ExampleLineAcrossPage() {

    // 문서 인스턴스 생성
    String _dataDir("C:\\Samples\\");
    // 문서 인스턴스 생성
    auto document = MakeObject<Document>();
   
    // PDF 파일의 페이지 컬렉션에 페이지 추가
    auto page = document->get_Pages()->Add();
    // 페이지 여백을 모든 면에 대해 0으로 설정
    page->get_PageInfo()->get_Margin()->set_Left(0);
    page->get_PageInfo()->get_Margin()->set_Right(0);
    page->get_PageInfo()->get_Margin()->set_Bottom(0);
    page->get_PageInfo()->get_Margin()->set_Top(0);

    // 페이지 치수와 동일한 너비와 높이의 그래프 객체 생성
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(
        page->get_PageInfo()->get_Width(), 
        page->get_PageInfo()->get_Height());

    // 페이지의 왼쪽-아래에서 오른쪽-위 모서리로 시작하는 첫 번째 라인 객체 생성
    auto line = MakeObject<Aspose::Pdf::Drawing::Line>(
        MakeArray<double>({ 
                      page->get_Rect()->get_LLX(), 0, 
                      page->get_PageInfo()->get_Width(),
                      page->get_Rect()->get_URY() }));

    // 그래프 객체의 도형 컬렉션에 선 추가
    graph->get_Shapes()->Add(line);
    // 페이지의 왼쪽-위 모서리에서 오른쪽-아래 모서리로 선 그리기
    auto line2 = MakeObject<Aspose::Pdf::Drawing::Line>( MakeArray<double>({0, 
        page->get_Rect()->get_URY(), page->get_PageInfo()->get_Width(), page->get_Rect()->get_LLX() }));

    // 그래프 객체의 도형 컬렉션에 선 추가
    graph->get_Shapes()->Add(line2);
    // 페이지의 단락 컬렉션에 그래프 객체 추가
    page->get_Paragraphs()->Add(graph);

    // PDF 파일 저장
    document->Save(_dataDir + u"DrawingLine_out.pdf");
}
```

```
![선 그리기](draw_line.png)
```