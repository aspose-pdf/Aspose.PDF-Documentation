---
title: 기존 PDF에서 테이블 조작
linktitle: 테이블 조작
type: docs
weight: 40
url: /ko/cpp/manipulate-tables-in-existing-pdf/
description: 이 섹션은 Aspose.PDF for C++를 사용하여 테이블을 수정하는 다양한 방법을 다룹니다.
lastmod: "2021-11-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 기존 PDF에서 테이블 조작

Aspose.PDF for C++를 사용하면 테이블을 신속하고 효율적으로 작업할 수 있으며, 즉 처음부터 생성하거나 기존 PDF 문서에 추가할 수 있습니다.

또한 데이터베이스(DOM)와 테이블을 통합하여 데이터베이스의 내용을 기반으로 동적인 테이블을 생성할 수 있는 기능을 제공합니다.

[Aspose.PDF.Text.TableAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.absorbed_table) 클래스는 PDF 문서 페이지에 이미 존재하는 간단한 테이블을 검색하고 구문 분석할 수 있도록 해줍니다. 다음 코드 스니펫은 테이블의 특정 셀의 내용을 업데이트하는 단계를 보여줍니다.

>헤더:

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
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>

#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>

#include <Aspose.PDF.Cpp/Color.h>

#include <Aspose.PDF.Cpp/Table/Table.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/TableAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedTable.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedRow.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedCell.h>
```

>샘플:

```cpp
using namespace System;
using namespace Aspose::Pdf;

#include "Table-Manipulate.h"

void ManipulateTables() {

    String _dataDir("C:\\Samples\\");

    // 기존 PDF 파일 로드
    auto document = MakeObject<Document>(_dataDir + u"input.pdf");

    // 테이블을 찾기 위한 TableAbsorber 객체 생성
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // 첫 페이지를 흡수기로 방문
    absorber->Visit(document->get_Pages()->idx_get(1));

    // 페이지의 첫 번째 테이블, 첫 번째 셀 및 그 안의 텍스트 조각에 접근
    auto fragment = absorber->get_TableList()->idx_get(0)->get_RowList()->idx_get(0)->get_CellList()->idx_get(0)->get_TextFragments()->idx_get(1);

    // 셀의 첫 번째 텍스트 조각의 텍스트 변경
    fragment->set_Text(u"hi world");
    document->Save(_dataDir + u"ManipulateTable_out.pdf");
}
```

## PDF 문서에서 오래된 테이블을 새로운 테이블로 교체하기

특정 테이블을 찾아 원하는 테이블로 교체해야 하는 경우, [TableAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.absorbed_table) 클래스의 Replace() 메서드를 사용하여 이를 수행할 수 있습니다.

다음 예제는 PDF 문서 내의 테이블을 교체하는 기능을 보여줍니다:

```cpp
void ReplaceOldTable() {
    String _dataDir("C:\\Samples\\");

    // 기존 PDF 파일 로드
    auto document = MakeObject<Document>(_dataDir + u"Table_input2.pdf");

    // 테이블을 찾기 위한 TableAbsorber 객체 생성
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // 첫 번째 페이지를 absorber로 방문
    absorber->Visit(document->get_Pages()->idx_get(1));

    // 페이지에서 첫 번째 테이블 가져오기
    auto table = absorber->get_TableList()->idx_get(0);

    // 새 테이블 생성
    auto newTable = MakeObject<Table>();
    newTable->set_ColumnWidths(u"100 100 100");
    newTable->set_DefaultCellBorder (MakeObject<BorderInfo>(BorderSide::All, 1.0F));

    auto row = newTable->get_Rows()->Add();
    row->get_Cells()->Add(u"Col 1");
    row->get_Cells()->Add(u"Col 2");
    row->get_Cells()->Add(u"Col 3");

    // 기존 테이블을 새로운 테이블로 교체
    absorber->Replace(document->get_Pages()->idx_get(1), table, newTable);

    // 문서 저장
    document->Save(_dataDir + u"TableReplaced_out.pdf");
}
```