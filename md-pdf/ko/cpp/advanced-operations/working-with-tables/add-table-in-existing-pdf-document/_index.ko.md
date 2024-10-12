---
title: PDF에 테이블 생성 또는 추가
linktitle: 테이블 생성 또는 추가
type: docs
weight: 10
url: /cpp/add-table-in-existing-pdf-document/
description: Aspose.PDF for C++는 PDF 테이블을 생성, 읽기 및 편집하는 데 사용되는 라이브러리입니다. 이 라이브러리를 사용하여 C++로 PDF 페이지에 테이블을 페이지 매김할 수 있습니다.
lastmod: "2021-11-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## C++를 사용하여 테이블 생성

PDF 문서를 작업할 때 테이블은 중요합니다. 테이블은 체계적인 방식으로 정보를 표시하는 훌륭한 기능을 제공합니다.

PDF 문서의 테이블은 데이터를 체계적인 방식으로 행과 열로 구성합니다. Aspose.PDF for C++ API를 사용하면 C++ 응용 프로그램에서 PDF 문서에 테이블을 추가하고, 행과 열을 추가할 수 있습니다. [Table](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table/) 클래스는 문서에 테이블을 추가하는 데 사용됩니다. 다음 단계는 C++를 사용하여 PDF 문서에 테이블을 추가하는 방법입니다.

### 기존 PDF 문서에 테이블 추가

Aspose.PDF for C++를 사용하여 기존 PDF 파일에 테이블을 추가하려면 다음 단계를 따르십시오:

1. 소스 파일을 불러옵니다.
1. 테이블을 초기화하고 열과 행을 설정합니다.
1. 테이블 설정을 설정합니다 (우리는 경계를 설정했습니다).
1. 테이블을 채웁니다.
1. 페이지에 테이블을 추가합니다.
1. 파일을 저장합니다.

다음 코드 스니펫은 기존 PDF 파일에 텍스트를 추가하는 방법을 보여줍니다.

>헤더

```cpp
#include <system/date_time.h>
#include <system/io/file.h>
#include <system/console.h>
#include <data/data_table.h>
#include <data/data_column_collection.h>
#include <system/type_info.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/PageInfo.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/Generator/GraphInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderCornerStyle.h>
#include <Aspose.PDF.Cpp/Generator/ColumnAdjustment.h>
#include <Aspose.PDF.Cpp/Generator/ImageFileType.h>
#include <Aspose.PDF.Cpp/Generator/Image.h>
#include <Aspose.PDF.Cpp/Generator/HtmlFragment.h>

#include <Aspose.PDF.Cpp/Text/TextFragment.h>

#include <Aspose.PDF.Cpp/Color.h>

#include <Aspose.PDF.Cpp/Table/Table.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
```

>Sample

```cpp
using namespace System;
using namespace Aspose::Pdf;

void AddingTableInExistingPDFDocument() {
    
    String _dataDir("C:\\Samples\\");
    
    // 소스 PDF 문서 로드
    auto document = MakeObject<Document>(_dataDir + u"AddTable.pdf");
    
    // Table의 새 인스턴스 초기화
    auto table = MakeObject<Table>();
    
    // 테이블 테두리 색상을 LightGray로 설정
    table->set_Border(MakeObject<Aspose::Pdf::BorderInfo>(
        Aspose::Pdf::BorderSide::All, .5f, 
        Aspose::Pdf::Color::get_LightGray()));
    // 테이블 셀의 테두리 설정
    table->set_DefaultCellBorder (MakeObject<Aspose::Pdf::BorderInfo>(
        Aspose::Pdf::BorderSide::All, .5f, 
        Aspose::Pdf::Color::get_LightGray()));

    // 10개의 행을 추가하는 루프 생성
    for (int row_count = 1; row_count < 10; row_count++)
    {
        // 테이블에 행 추가
        auto row = table->get_Rows()->Add();
        // 테이블 셀 추가
        row->get_Cells()->Add(String::Format(u"열 ({0}, 1)", row_count));
        row->get_Cells()->Add(String::Format(u"열 ({0}, 2)", row_count));
        row->get_Cells()->Add(String::Format(u"열 ({0}, 3)", row_count));
    }

    // 입력 문서의 첫 번째 페이지에 테이블 객체 추가
    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(table);
    
    // 테이블 객체가 포함된 업데이트된 문서 저장
    document->Save(_dataDir + u"document_with_table_out.pdf");
}
```

### ColSpan and RowSpan in Tables

Aspose.PDF for C++는 테이블의 열을 병합하기 위한 [ColSpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell#ae79c581d2245258699c98617e78c01d1) 속성과 행을 병합하기 위한 [RowSpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell#a4eb7337d118314e6c2180670fb32721a) 속성을 제공합니다.

우리는 [Cell](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell) 객체에 [ColSpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell#ae79c581d2245258699c98617e78c01d1) 또는 [RowSpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell#a4eb7337d118314e6c2180670fb32721a) 속성을 사용하여 테이블 셀을 생성합니다. 필요한 속성을 적용한 후 생성된 셀을 테이블에 추가할 수 있습니다.

```cpp
void AddTable_RowColSpan()
{
    String _dataDir("C:\\Samples\\");

    // 소스 PDF 문서 로드
    auto document = MakeObject<Document>();
    document->get_Pages()->Add();

    // 테이블의 새 인스턴스 초기화
    auto table = MakeObject<Table>();
    // 테이블 테두리 색상을 LightGray로 설정
    table->set_Border(MakeObject<Aspose::Pdf::BorderInfo>(
        Aspose::Pdf::BorderSide::All, .5f, 
        Color::get_Black()));
        // 테이블 셀의 테두리 설정
    table->set_DefaultCellBorder(
        MakeObject<Aspose::Pdf::BorderInfo>(
            Aspose::Pdf::BorderSide::All, .5f, 
            Color::get_Black()));
    

    // 테이블에 첫 번째 행 추가
    auto row1 = table->get_Rows()->Add();
    for (int cellCount = 1; cellCount < 5; cellCount++)
    {
        // 테이블 셀 추가
        row1->get_Cells()->Add(String::Format(u"Test 1 {0}", cellCount));
    }

    // 테이블에 두 번째 행 추가
    auto row2 = table->get_Rows()->Add();
    row2->get_Cells()->Add(u"Test 2 1");
    auto cell = row2->get_Cells()->Add(u"Test 2 2");
    cell->set_ColSpan(2);
    row2->get_Cells()->Add(u"Test 2 4");

    // 테이블에 세 번째 행 추가
    auto row3 = table->get_Rows()->Add();
    row3->get_Cells()->Add(u"Test 3 1");
    row3->get_Cells()->Add(u"Test 3 2");
    row3->get_Cells()->Add(u"Test 3 3");
    row3->get_Cells()->Add(u"Test 3 4");

    // 테이블에 네 번째 행 추가
    auto row4 = table->get_Rows()->Add();
    row4->get_Cells()->Add(u"Test 4 1");
    cell = row4->get_Cells()->Add(u"Test 4 2");
    cell->set_RowSpan (2);
    row4->get_Cells()->Add(u"Test 4 3");
    row4->get_Cells()->Add(u"Test 4 4");


    // 테이블에 다섯 번째 행 추가
    auto row5 = table->get_Rows()->Add();
    row5->get_Cells()->Add(u"Test 5 1");
    row5->get_Cells()->Add(u"Test 5 3");
    row5->get_Cells()->Add(u"Test 5 4");

    // 입력 문서의 첫 번째 페이지에 테이블 객체 추가
    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(table);

    // 테이블 객체가 포함된 업데이트된 문서 저장
    document->Save(_dataDir + u"document_with_table_out.pdf");
}
```

코드 실행 결과는 다음 이미지에 묘사된 표입니다:

![ColSpan and RowSpan demo](colspan_rowspan.png)

## 테두리, 여백 및 패딩 작업

또한 테이블의 테두리, 여백 및 셀 패딩 설정 기능도 지원한다는 점에 유의하십시오. 먼저 아래 다이어그램에 제시된 테두리, 여백 및 패딩의 개념을 이해해 봅시다:

![Borders, margins and padding](set-border-style-margins-and-padding-of-table_1.png)

그림을 자세히 확인하십시오. 테이블, 행 및 셀의 테두리가 겹쳐져 있음을 보여줍니다. Aspose.PDF for C++를 사용하여 테이블에 여백을 설정하고 셀을 들여쓰기할 수 있습니다. 셀 여백을 설정하려면 셀 패딩을 설정해야 합니다.

## 테두리

Table, [Row](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.row) 및 [Cell](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell) 객체의 테두리를 설정하려면 Table.Border, Row.Border 및 Cell.Border 속성을 사용하십시오. 셀 테두리는 [Table](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table) 또는 Row 클래스의 DefaultCellBorder 속성을 사용하여 설정할 수도 있습니다. 위에서 논의한 모든 테두리 관련 속성은 생성자를 호출하여 생성된 Row 클래스의 인스턴스에 할당됩니다. Row 클래스는 테두리를 사용자 정의하는 데 필요한 거의 모든 매개변수를 수용하는 많은 오버로드를 가지고 있습니다.

## 여백 또는 패딩

셀 패딩은 Table 클래스의 [DefaultCellPadding](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table#ac64196de6dfed7550c3278892ed9dbe0) 속성을 사용하여 관리할 수 있습니다. 모든 패딩 관련 속성은 `Left`, `Right`, `Top` 및 `Bottom` 매개변수에 대한 정보를 수집하여 사용자 정의 여백을 만드는 [MarginInfo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.margin_info/) 클래스의 인스턴스에 할당됩니다.

![PDF 테이블에서의 여백과 테두리](margin-border.png)

```cpp
void AddTable_MergingPadding() {

    String _dataDir("C:\\Samples\\");

    // 빈 생성자를 호출하여 Document 객체를 인스턴스화합니다.
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    // 테이블 객체를 인스턴스화합니다.
    auto tab1 = MakeObject<Table>();
    // 원하는 섹션의 단락 컬렉션에 테이블을 추가합니다.
    page->get_Paragraphs()->Add(tab1);
    // 테이블의 열 너비를 설정합니다.
    tab1->set_ColumnWidths (u"50 50 50");
    // BorderInfo 객체를 사용하여 기본 셀 테두리를 설정합니다.
    tab1->set_DefaultCellBorder (
        MakeObject<Aspose::Pdf::BorderInfo>(
            Aspose::Pdf::BorderSide::All, 0.1F));
    // 다른 맞춤화된 BorderInfo 객체를 사용하여 테이블 테두리를 설정합니다.
    tab1->set_Border (
        MakeObject<Aspose::Pdf::BorderInfo>(
            Aspose::Pdf::BorderSide::All, 1.0F));

    // MarginInfo 객체를 생성하고 왼쪽, 아래, 오른쪽 및 위쪽 여백을 설정합니다.
    auto margin = MakeObject<MarginInfo>();
    margin->set_Top (5.0f);
    margin->set_Left (5.0f);
    margin->set_Right (5.0f);
    margin->set_Bottom (5.0f);

    // MarginInfo 객체에 기본 셀 패딩을 설정합니다.
    tab1->set_DefaultCellPadding (margin);
    // 테이블에서 행을 생성하고 행에서 셀을 생성합니다.
    auto row1 = tab1->get_Rows()->Add();
    row1->get_Cells()->Add(u"col1");
    row1->get_Cells()->Add(u"col2");
    row1->get_Cells()->Add();

    auto mytext = MakeObject<Aspose::Pdf::Text::TextFragment>(u"col3 with large text string");
        
    row1->get_Cells()->idx_get(2)->get_Paragraphs()->Add(mytext);
    row1->get_Cells()->idx_get(2)->set_IsWordWrapped(false);
    

    auto row2 = tab1->get_Rows()->Add();
    row2->get_Cells()->Add(u"item1");
    row2->get_Cells()->Add(u"item2");
    row2->get_Cells()->Add(u"item3");
    
    // PDF를 저장합니다.
    document->Save(_dataDir + u"MarginsOrPadding_out.pdf");
}
```
테이블을 둥근 모서리로 만들기 위해 [BorderInfo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.border_info) 클래스의 [RoundedBorderRadius](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.border_info#a6a2bed69dd034fba9ce439dcbe1fd3de) 값을 사용하고 테이블 모서리 스타일을 둥글게 설정하십시오.

```cpp
void AddTable_RoundedBorderRadius()
{
    // 문서 디렉토리 경로.
    String _dataDir("C:\\Samples\\");

    auto tab1 = MakeObject<Aspose::Pdf::Table>();

    auto graph = MakeObject<GraphInfo>();
    graph->set_Color(Color::get_Red());
    // 빈 BorderInfo 객체 생성
    auto bInfo = MakeObject<BorderInfo>(BorderSide::All, graph);

    // 반경이 15인 둥근 테두리를 설정합니다.
    bInfo->set_RoundedBorderRadius(15);
    // 테이블 모서리 스타일을 둥글게 설정합니다.
    tab1->set_CornerStyle (Aspose::Pdf::BorderCornerStyle::Round);
    // 테이블 테두리 정보를 설정합니다.
    tab1->set_Border(bInfo);
}
```

### ColumnAdjustmentType 열거형의 AutoFitToWindow 속성

```cpp
void AddTable_AutoFitToWindow() {
    
    // 문서 디렉터리 경로입니다.
    String _dataDir("C:\\Samples\\");

    // 빈 생성자를 호출하여 Pdf 객체를 인스턴스화합니다.
    auto document = MakeObject<Document>();

    // Pdf 객체에 섹션을 만듭니다.
    auto sec1 = document->get_Pages()->Add();

    // 테이블 객체를 인스턴스화합니다.
    auto tab1 = MakeObject<Aspose::Pdf::Table>();
    // 원하는 섹션의 단락 컬렉션에 테이블을 추가합니다.
    sec1->get_Paragraphs()->Add(tab1);

    // 테이블의 열 너비를 설정합니다.
    tab1->set_ColumnWidths (u"50 50 50");
    tab1->set_ColumnAdjustment (ColumnAdjustment::AutoFitToWindow);

    // BorderInfo 객체를 사용하여 기본 셀 테두리를 설정합니다.
    tab1->set_DefaultCellBorder(MakeObject<BorderInfo>(Aspose::Pdf::BorderSide::All, 0.1F));

    // 다른 사용자 정의 BorderInfo 객체를 사용하여 테이블 테두리를 설정합니다.
    tab1->set_Border (MakeObject<BorderInfo>(Aspose::Pdf::BorderSide::All, 1.0F));

    // MarginInfo 객체를 생성하고 왼쪽, 아래쪽, 오른쪽 및 위쪽 마진을 설정합니다.
    auto margin = MakeObject<MarginInfo>();
    margin->set_Top(5.0f);
    margin->set_Left(5.0f);
    margin->set_Right(5.0f);
    margin->set_Bottom(5.0f);

    // MarginInfo 객체에 기본 셀 패딩을 설정합니다.
    tab1->set_DefaultCellPadding(margin);

    // 테이블에 행을 만들고 행에 셀을 추가합니다.
    auto row1 = tab1->get_Rows()->Add();
    row1->get_Cells()->Add(u"col1");
    row1->get_Cells()->Add(u"col2");
    row1->get_Cells()->Add(u"col3");

    auto row2 = tab1->get_Rows()->Add();
    row2->get_Cells()->Add(u"item1");
    row2->get_Cells()->Add(u"item2");
    row2->get_Cells()->Add(u"item3");
    
    // 테이블 객체를 포함한 업데이트된 문서를 저장합니다.
    document->Save(_dataDir + u"AutoFitToWindow_out.pdf");
}
```

### 테이블 너비 가져오기

테이블의 너비를 동적으로 가져와야 하는 작업이 있습니다. [Aspose.PDF.Table](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table) 클래스에는 이러한 목적을 위한 [GetWidth] 메서드가 있습니다 (https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table#a3361cc8d4af87eec2e3da616c474ac1c). 예를 들어, 테이블 열의 너비를 명시적으로 설정하지 않았고, [ColumnAdjustment] (https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#afc01382935026dd569c96d77d09dc3a4)를 AutoFitToContent로 설정하지 않았습니다. 이 경우, 다음 테이블 너비를 가져올 수 있습니다.

```cpp
void GetTableWidth() {
    // 새 문서 생성
    auto document = MakeObject<Document>();
    
    // 문서에 페이지 추가
    auto page = document->get_Pages()->Add();

    // 새 테이블 초기화
    auto table = MakeObject<Table>();
    table->set_ColumnAdjustment(ColumnAdjustment::AutoFitToContent);
    
    // 테이블에 행 추가
    auto row = table->get_Rows()->Add();

    // 테이블에 셀 추가
    auto cell = row->get_Cells()->Add(u"셀 1 텍스트");
    cell = row->get_Cells()->Add(u"셀 2 텍스트");
    // 테이블 너비 가져오기
    Console::WriteLine(table->GetWidth());
}
```

## 테이블 셀에 SVG 이미지 추가

Aspose.PDF for C++를 사용하면 PDF 파일에 테이블 셀을 추가할 수 있습니다. 테이블을 생성할 때 셀에 텍스트나 이미지를 추가할 수 있습니다. 또한, 이 API는 SVG 파일을 PDF로 변환하는 기능도 제공합니다. 이러한 기능을 결합하여 SVG 이미지를 로드하고 테이블 셀에 추가할 수 있습니다.

다음 코드 스니펫은 테이블을 인스턴스화하고 테이블 셀에 SVG 이미지를 추가하는 단계를 보여줍니다.

```cpp
void InsertSVGObject() 
{
    String _dataDir("C:\\Samples\\");

    // Document 객체 인스턴스화
    auto document = MakeObject<Document>();
    // 이미지 인스턴스 생성
    auto img = MakeObject<Aspose::Pdf::Image>();

    // 이미지 유형을 SVG로 설정
    img->set_FileType(Aspose::Pdf::ImageFileType::Svg);
    // 소스 파일 경로
    img->set_File (_dataDir + u"SVGToPDF.svg");
    // 이미지 인스턴스의 너비 설정
    img->set_FixWidth (50);
    // 이미지 인스턴스의 높이 설정
    img->set_FixHeight(50);
    // 테이블 인스턴스 생성
    auto table = MakeObject<Aspose::Pdf::Table>();
    // 테이블 셀의 너비 설정
    table->set_ColumnWidths (u"100 100");
    // 행 객체 생성 및 테이블 인스턴스에 추가
    auto row = table->get_Rows()->Add();
    // 셀 객체 생성 및 행 인스턴스에 추가
    auto cell = row->get_Cells()->Add();
    // 텍스트 조각을 셀 객체의 단락 컬렉션에 추가
    cell->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"First cell"));
    // 행 객체에 다른 셀 추가
    cell = row->get_Cells()->Add();
    // 최근 추가된 셀 인스턴스의 단락 컬렉션에 SVG 이미지 추가
    cell->get_Paragraphs()->Add(img);
    // 페이지 객체 생성 및 문서 인스턴스의 페이지 컬렉션에 추가
    auto page = document->get_Pages()->Add();
    // 페이지 객체의 단락 컬렉션에 테이블 추가
    page->get_Paragraphs()->Add(table);    
    // PDF 파일 저장
    document->Save(_dataDir + u"AddSVGObject_out.pdf");
}
```

## 테이블 안에 HTML 태그 사용하기

일부 작업에서는 데이터베이스 내용을 일부 HTML 태그와 함께 가져와서 테이블 객체에 내용을 가져와야 합니다. 내용을 가져올 때 HTML 태그는 PDF 문서 안에 표시되어야 합니다.

다음 코드 스니펫에서는 테이블 테두리 색상을 설정하고 테이블 셀의 테두리를 설정할 수 있습니다. 그런 다음 10개의 행을 추가하는 루프를 생성합니다. 입력 문서의 첫 페이지에 테이블 객체를 추가하고 업데이트된 문서를 저장합니다.

```cpp
void AddHTMLFragmentToTableCell() {
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"input.pdf");    
    // 테이블의 새 인스턴스를 초기화합니다.
    auto table = MakeObject<Table>();
    // 테이블 테두리 색상을 연회색으로 설정합니다.
    table->set_Border(new BorderInfo(BorderSide::All, .5f, Color::get_LightGray()));
    // 테이블 셀의 테두리를 설정합니다.
    table->set_DefaultCellBorder(new BorderInfo(BorderSide::All, .5f, Color::get_LightGray()));
    // 10개의 행을 추가하는 루프를 생성합니다.       
    for (int row_count = 1; row_count < 10; row_count++) {
        SmartPtr<Cell> cell;
        // 테이블에 행을 추가합니다.
        auto row = table->get_Rows()->Add();
        // 테이블 셀을 추가합니다.
        cell = row->get_Cells()->Add();
        cell->get_Paragraphs()->Add(new HtmlFragment(String::Format(u"Column <strong>({0}, 1)</strong>", row_count)));

        cell = row->get_Cells()->Add();
        cell->get_Paragraphs()->Add(new HtmlFragment(String::Format(u"Column <span style='color:red'>({0}, 2)</span>",row_count)));

        cell = row->get_Cells()->Add();
        cell->get_Paragraphs()->Add(new HtmlFragment(String::Format(u"Column <span style='text-decoration: underline'>([0}, 3)</span>", row_count)));
    }
    // 입력 문서의 첫 페이지에 테이블 객체를 추가합니다.
    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(table);
    // 테이블 객체를 포함하는 업데이트된 문서를 저장합니다.
    document->Save(_dataDir + u"AddHTMLObject_out.pdf");
}
```

## 테이블 행 사이에 페이지 나누기 삽입

일반적으로 PDF 내에서 테이블을 생성할 때, 테이블이 하단 여백에 도달하면 다음 페이지로 흐릅니다. 하지만 특정 행 수가 테이블에 추가될 때 페이지 나누기를 강제로 삽입해야 하는 요구사항이 있을 수 있습니다. 다음 코드 스니펫은 테이블에 10개의 행을 추가하면서 페이지 나누기를 삽입하는 단계를 보여줍니다.

다음 코드 스니펫은 테이블에 10개의 행이 추가될 때 페이지 나누기를 삽입하는 단계를 보여줍니다.

```cpp
void InsertPageBreak() {
    String _dataDir("C:\\Samples\\");

    // Document 인스턴스를 인스턴스화
    auto document = MakeObject<Document>();
    
    // PDF 파일의 페이지 컬렉션에 페이지 추가
    auto page = document->get_Pages()->Add();

    // 테이블 인스턴스 생성
    auto tab = MakeObject<Table>();

    // 테이블에 대한 테두리 스타일 설정
    tab->set_Border(MakeObject<BorderInfo>(BorderSide::All, Color::get_Red()));
    // 테두리 색상을 빨간색으로 하여 테이블에 기본 테두리 스타일 설정
    tab->set_DefaultCellBorder(MakeObject<BorderInfo>(BorderSide::All, Color::get_Red()));
    // 테이블 열 너비 지정
    tab->set_ColumnWidths(u"100 100");

    // 테이블에 200개의 행을 추가하기 위한 루프 생성
    for (int counter = 0; counter <= 200; counter++) {
        auto row = MakeObject<Row>();
        tab->get_Rows()->Add(row);
        auto cell1 = MakeObject<Cell>();
        cell1->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(String::Format(u"Cell {0}, 0", counter)));
        row->get_Cells()->Add(cell1);

        auto cell2 = new Cell();
        cell2->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(String::Format(u"Cell {0}, 1", counter)));
        row->get_Cells()->Add(cell2);
        // 10개의 행이 추가되면 새 페이지에 새 행 렌더링
        if (counter % 10 == 0 && counter != 0)
            row->set_IsInNewPage(true);
    }
    // PDF 파일의 단락 컬렉션에 테이블 추가
    page->get_Paragraphs()->Add(tab);

    // PDF 문서 저장
    document->Save(_dataDir + u"InsertPageBreak_out.pdf");
}
```

## 새 페이지에 테이블 렌더링

기본적으로 단락은 페이지 객체의 Paragraphs 컬렉션에 추가됩니다. 그러나 페이지에서 이전에 추가된 단락 수준 객체 바로 뒤에 테이블을 렌더링하는 대신 새 페이지에 테이블을 렌더링하는 것도 가능합니다.

### 샘플: C++를 사용하여 새 페이지에 테이블 렌더링하는 방법

새 페이지에 테이블을 렌더링하려면 [BaseParagraph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.base_paragraph) 클래스의 [IsInNewPage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.base_paragraph#a614946048d22afb9dce4cd42346c7561) 속성을 사용하십시오. 다음 코드 스니펫은 그 방법을 보여줍니다.

```cpp
void RenderTableOnNewPage()
{
    auto document = MakeObject<Document>();
    auto pageInfo = document->get_PageInfo();
    auto marginInfo = pageInfo->get_Margin();

    marginInfo->set_Left (37);
    marginInfo->set_Right (37);
    marginInfo->set_Top (37);
    marginInfo->set_Bottom (37);

    pageInfo->set_IsLandscape(true);

    auto table = MakeObject<Aspose::Pdf::Table>();
    table->set_ColumnWidths(u"50 100");
    // 페이지 추가됨.
    auto curPage = document->get_Pages()->Add();
    for (int i = 1; i <= 120; i++)
    {
        auto row = table->get_Rows()->Add();
        row->set_FixedRowHeight(15);
        auto cell1 = row->get_Cells()->Add();
        cell1->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"Content 1"));
        auto cell2 = row->get_Cells()->Add();
        cell2->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"HHHHH"));
    }
    auto paragraphs = curPage->get_Paragraphs();
    paragraphs->Add(table);

    //-------------------------------------

    auto document = MakeObject<Document>();
    auto table1 = MakeObject<Aspose::Pdf::Table>();
    table1->set_ColumnWidths(u"100 100");

    String _dataDir("C:\\Samples\\");

    for (int i = 1; i <= 10; i++)
    {
        auto row = table1->get_Rows()->Add();
        auto cell1 = row->get_Cells()->Add();
        cell1->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"LAAAAAAA"));
        auto cell2 = row->get_Cells()->Add();
        cell2->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"LAAGGGGGG"));
    }
    
    table1->set_IsInNewPage (true);
    // 테이블 1을 다음 페이지에 유지하고 싶습니다...
    paragraphs->Add(table1);
    
    document->Save(_dataDir + u"IsNewPageProperty_Test_out.pdf");
}
```