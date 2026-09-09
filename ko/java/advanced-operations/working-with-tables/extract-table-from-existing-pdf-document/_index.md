---
title: Java의 PDF에서 테이블 추출
linktitle: 테이블 추출
type: docs
weight: 20
url: /java/extracting-table/
description: Java의 기존 PDF 문서에서 테이블 데이터를 추출하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 파일에서 테이블 데이터 추출
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서에서 테이블을 추출하는 방법을 설명합니다. TableAbsorber를 사용하여 페이지별로 테이블을 감지하고, 행과 셀을 반복하고, 다운스트림 처리를 위해 셀 텍스트를 수집하는 방법을 보여줍니다.
---
기존 PDF에서 테이블 구조를 감지하고 해당 내용을 읽어야 하는 경우 `TableAbsorber`을 사용하세요.


## 
감지된 테이블에서 텍스트 추출



각 페이지에서 테이블을 찾고 해당 셀 텍스트를 수집해야 할 때 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/)로 각 페이지를 방문해보세요.
1. 흡수된 테이블, 행 및 셀을 반복한 다음 추출된 텍스트를 출력합니다.

```java
public static void extract(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            TableAbsorber absorber = new TableAbsorber();
            absorber.visit(page);
            for (AbsorbedTable table : absorber.getTableList()) {
                System.out.println("Table ----");
                for (AbsorbedRow row : table.getRowList()) {
                    System.out.println("Row:");
                    StringBuilder rowText = new StringBuilder();
                    for (AbsorbedCell cell : row.getCellList()) {
                        StringBuilder cellText = new StringBuilder();
                        for (TextFragment fragment : cell.getTextFragments()) {
                            for (TextSegment segment : fragment.getSegments()) {
                                cellText.append(segment.getText());
                            }
                        }
                        rowText.append(" | ").append(cellText);
                    }
                    System.out.println(rowText);
                }
            }
        }
    }
}
```
