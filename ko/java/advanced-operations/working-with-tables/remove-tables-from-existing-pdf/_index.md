---
title: 기존 PDF에서 테이블 제거
linktitle: 테이블 제거
type: docs
weight: 40
url: /ko/java/remove-tables-from-existing-pdf/
description: Aspose.PDF for Java는 PDF 문서에서 테이블 및 여러 테이블을 제거할 수 있습니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Aspose.PDF for Java는 PDF 문서를 처음부터 생성할 때 내부에 테이블을 삽입/생성하는 기능을 제공하며, 기존 PDF 문서에 테이블 객체를 추가할 수도 있습니다. 그러나 기존 PDF에서 [테이블 조작하기](https://docs.aspose.com/pdf/java/manipulate-tables-in-existing-pdf/)라는 요구 사항이 있을 수 있으며, 여기서 기존 테이블 셀의 내용을 업데이트할 수 있습니다. 그러나 기존 PDF 문서에서 테이블 객체를 제거해야 하는 요구 사항에 직면할 수 있습니다.

{{% /alert %}}

테이블을 제거하기 위해서는 [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber) 클래스를 사용하여 기존 PDF의 테이블을 확보한 다음 [Remove](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#remove-com.aspose.pdf.AbsorbedTable-) 메서드를 호출해야 합니다.

## PDF 문서에서 테이블 제거

우리는 PDF 문서에서 테이블을 제거하기 위해 기존 [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber) 클래스에 새로운 함수인 Remove()를 추가했습니다. 흡수기가 페이지에서 테이블을 성공적으로 찾으면, 그것들을 제거할 수 있게 됩니다. PDF 문서에서 테이블을 제거하는 방법을 보여주는 다음 코드 스니펫을 확인하십시오:

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleRemoveTable {
    
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void RemoveTable() {
        // 기존 PDF 문서 로드
        Document pdfDocument = new Document(_dataDir + "Table_input.pdf");

        // 테이블을 찾기 위한 TableAbsorber 객체 생성
        TableAbsorber absorber = new TableAbsorber();

        // 흡수기로 첫 페이지 방문
        absorber.visit(pdfDocument.getPages().get_Item(1));

        // 페이지의 첫 번째 테이블 가져오기
        AbsorbedTable table = absorber.getTableList().get(0);

        // 테이블 제거
        absorber.remove(table);

        // PDF 저장
        pdfDocument.save(_dataDir + "Table_out.pdf");
    }  
```


## PDF 문서에서 여러 테이블 제거하기

때때로 PDF 문서에는 하나 이상의 테이블이 포함되어 있을 수 있으며, 여러 테이블을 제거해야 하는 요구 사항이 발생할 수 있습니다. PDF 문서에서 여러 테이블을 제거하려면 다음 코드 스니펫을 사용하십시오:

```java
    public static void RemoveMultipleTable() {
        // 기존 PDF 문서 로드
        Document pdfDocument = new Document(_dataDir + "Table_input2.pdf");

        // 테이블을 찾기 위한 TableAbsorber 객체 생성
        TableAbsorber absorber = new TableAbsorber();

        // 두 번째 페이지를 흡수기로 방문
        absorber.visit(pdfDocument.getPages().get_Item(2));

        // 컬렉션의 복사를 통해 반복하고 테이블 제거
        for (AbsorbedTable table : absorber.getTableList())
            absorber.remove(table);

        // 문서 저장
        pdfDocument.save(_dataDir + "Table2_out.pdf");
    }
}
```