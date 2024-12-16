---
title: 기존 PDF에서 테이블 조작
linktitle: 테이블 조작
type: docs
weight: 30
url: /ko/java/manipulate-tables-in-existing-pdf/
description: 기존 PDF 파일에서 테이블을 조작하고 Aspose.PDF for Java로 PDF 문서에서 오래된 테이블을 새 테이블로 교체합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 기존 PDF에서 테이블 조작

Aspose.PDF for Java에서 지원하는 초기 기능 중 하나는 테이블 작업 기능이며, 처음부터 생성된 PDF 파일이나 기존 PDF 파일에 테이블을 추가하는 데 뛰어난 지원을 제공합니다.
 당신은 또한 데이터베이스(DOM)와 테이블을 통합하여 데이터베이스 내용에 기반한 동적 테이블을 생성할 수 있는 기능을 얻습니다. 이 새로운 릴리스에서, 우리는 PDF 문서의 페이지에 이미 존재하는 간단한 테이블을 검색하고 구문 분석하는 새로운 기능을 구현했습니다. **Aspose.PDF.Text.TableAbsorber**라는 새로운 클래스가 이러한 기능을 제공합니다. TableAbsorber의 사용법은 기존의 TextFragmentAbsorber 클래스와 매우 유사합니다.

다음 코드 스니펫은 특정 테이블 셀의 내용을 업데이트하는 단계를 보여줍니다.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleManipulate {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ManipulateTables() {

        // 기존 PDF 파일 로드
        Document pdfDocument = new Document(_dataDir + "input.pdf");
        // 테이블을 찾기 위한 TableAbsorber 객체 생성
        TableAbsorber absorber = new TableAbsorber();

        // 첫 번째 페이지를 흡수기로 방문
        absorber.visit(pdfDocument.getPages().get_Item(1));

        // 페이지의 첫 번째 테이블, 그들의 첫 번째 셀 및 그 안의 텍스트 조각에 접근
        TextFragment fragment = absorber.getTableList().get(0).getRowList().get(0).getCellList().get(0)
                .getTextFragments().get_Item(1);

        // 셀의 첫 번째 텍스트 조각의 텍스트 변경
        fragment.setText("hi world");

        pdfDocument.save(_dataDir + "ManipulateTable_out.pdf");
    }
```

## PDF 문서에서 오래된 테이블을 새로운 테이블로 교체하기

특정 테이블을 찾아서 원하는 테이블로 교체해야 하는 경우, [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber) 클래스의 Replace() 메서드를 사용할 수 있습니다.

다음 예제는 PDF 문서 내의 테이블을 교체하는 기능을 보여줍니다:

```java
public static void ReplaceOldTableWithNew() {

        // 기존 PDF 문서 로드
        Document pdfDocument = new Document(_dataDir + "Table_input2.pdf");

        // 테이블을 찾기 위한 TableAbsorber 객체 생성
        TableAbsorber absorber = new TableAbsorber();

        Page page = pdfDocument.getPages().get_Item(1);

        // 첫 페이지를 흡수기로 방문
        absorber.visit(page);

        // 페이지에서 첫 번째 테이블 가져오기
        AbsorbedTable table = absorber.getTableList().get(0);

        // 새로운 테이블 생성
        Table newTable = new Table();
        newTable.setColumnWidths("100 100 100");
        newTable.setDefaultCellBorder (new BorderInfo(BorderSide.All, 1F));

        Row row = newTable.getRows().add();
        row.getCells().add("Col 1");
        row.getCells().add("Col 2");
        row.getCells().add("Col 3");

        // 테이블을 새로운 테이블로 교체
        absorber.replace(page, table, newTable);

        // 문서 저장
        pdfDocument.save(_dataDir + "TableReplaced_out.pdf");
        
    }

}
```