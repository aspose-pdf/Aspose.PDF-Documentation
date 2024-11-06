---
title: 기존 PDF에서 표 제거
linktitle: 표 제거
type: docs
weight: 50
url: ko/cpp/remove-tables-from-existing-pdf/
description: 이 섹션에서는 PDF 문서에서 표를 제거하는 방법을 설명합니다.
lastmod: "2021-11-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for C++를 사용하면 PDF 문서를 처음부터 생성할 때 테이블을 삽입하고 생성할 수 있으며, 기존 PDF 문서에 테이블 객체를 추가할 수도 있습니다. 그러나 기존 테이블 셀의 내용을 업데이트할 수 있는 [기존 PDF에서 테이블 조작](https://docs.aspose.com/pdf/cpp/manipulate-tables-in-existing-pdf/)이 필요한 경우가 있을 수 있습니다. 또한 기존 PDF 문서에서 테이블 객체를 제거해야 하는 경우도 있을 수 있습니다.

테이블을 제거하기 위해서는 기존 PDF에서 테이블을 가져오기 위해 [TableAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.absorbed_table) 클래스를 사용한 다음 'Remove' 메서드를 호출해야 합니다.

## PDF 문서에서 표 제거

새로운 기능을 추가했습니다. i.e. [Remove](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber#ace39006d8f44c9cb776ee26281a1cbb3) 기존 TableAbsorber 클래스에 추가하여 PDF 문서에서 테이블을 제거합니다. 흡수기가 페이지에서 테이블을 성공적으로 찾으면 이를 제거할 수 있게 됩니다. PDF 문서에서 테이블을 제거하는 방법을 보여주는 다음 코드 스니펫을 확인하십시오:

>Headers:

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/TableAbsorber.h>
```

>Samples:

```cpp
using namespace System;
using namespace Aspose::Pdf;

void RemoveTable() {

    String _dataDir("C:\\Samples\\");

    // 원본 PDF 문서 로드
    auto document = MakeObject<Document>(_dataDir + u"Table_input.pdf");

    // 테이블을 찾기 위한 TableAbsorber 객체 생성
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // 첫 번째 페이지를 흡수기로 방문
    absorber->Visit(document->get_Pages()->idx_get(1));

    // 페이지에서 첫 번째 테이블 가져오기
    auto table = absorber->get_TableList()->idx_get(0);

    // 테이블 제거
    absorber->Remove(table);

    // PDF 저장
    document->Save(_dataDir + u"Table_out.pdf");
}
```
## PDF 문서에서 여러 테이블 제거하기

일부 작업은 하나의 pdf 문서에서 여러 테이블과 함께 작업하는 것과 관련이 있습니다. 그리고 여러 테이블을 삭제해야 할 것입니다. PDF 문서에서 여러 테이블을 제거하려면 다음 코드 조각을 사용하십시오:

```cpp
void RemoveMultipleTables() {

    String _dataDir("C:\\Samples\\");

    // 기존 PDF 문서 로드
    auto document = MakeObject<Document>(_dataDir + u"Table_input2.pdf");

    // 테이블을 찾기 위한 TableAbsorber 객체 생성
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // 흡수기로 첫 페이지 방문
    absorber->Visit(document->get_Pages()->idx_get(1));

    // 테이블 컬렉션의 복사본 가져오기
    auto tables = absorber->get_TableList();


    // 컬렉션의 복사본을 반복하여 테이블 제거
    for(auto table : tables)
    absorber->Remove(table);

    // 문서 저장
    document->Save(_dataDir + u"Table2_out.pdf");
}
```

{{% alert color="primary" %}}

테이블을 제거하거나 교체하면 TableList 컬렉션이 변경된다는 점을 유의하십시오. 따라서 루프에서 테이블을 제거/교체할 경우 TableList 컬렉션의 복사가 필수적입니다.

{{% /alert %}}