---
title: 기존 PDF 문서의 표 조작
linktitle: 테이블 조작
type: docs
weight: 40
url: /java/manipulating-tables/
description: Java를 사용하여 기존 PDF 문서의 테이블을 검사하고 수정하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 기존 PDF 테이블 검사 및 수정
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서에 이미 있는 테이블을 조작하는 방법을 설명합니다. TableAbsorber를 사용하여 테이블 찾기, 셀 내부의 텍스트 업데이트, 감지된 테이블을 새 Table 개체로 바꾸는 방법을 다룹니다.
---

기존 테이블을 찾고 해당 내용을 업데이트해야 하는 경우 `TableAbsorber`을 사용하세요.


## 
표 셀 내부의 텍스트 바꾸기



전체 테이블을 다시 작성하지 않고 감지된 셀의 텍스트를 업데이트해야 하는 경우 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 열고 [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/)가 있는 페이지를 방문하세요.

1. 
대상 테이블과 셀 텍스트 조각이 존재하는지 확인하십시오.

1. 
셀 텍스트를 바꾸고 업데이트된 문서를 저장합니다.


```java
public static void replaceCells(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        if (absorber.getTableList().isEmpty()) {
            throw new IllegalStateException("No tables were found on page 1.");
        }
        if (absorber.getTableList().get(0).getRowList().get(0).getCellList().get(0).getTextFragments().size() == 0) {
            throw new IllegalStateException("The target cell has no text fragments.");
        }

        absorber.getTableList().get(0).getRowList().get(0).getCellList().get(0)
                .getTextFragments().get_Item(1).setText("New Value");
        document.save(outputFile.toString());
    }
}
```

## 
감지된 테이블을 새 테이블로 교체



원래 테이블을 새로 생성된 테이블로 완전히 교체해야 하는 경우 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 열고 페이지에서 테이블을 검색합니다.

1. 
원하는 구조로 새 [테이블](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/)을 생성합니다.

1. 
흡수된 테이블을 교체하고 출력 PDF를 저장합니다.

```java
public static void replaceTable(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        if (absorber.getTableList().isEmpty()) {
            throw new IllegalStateException("No tables were found on page 1.");
        }

        AbsorbedTable oldTable = absorber.getTableList().get(0);
        Table newTable = new Table();
        newTable.setColumnWidths("100 100 100");
        newTable.setDefaultCellBorder(new BorderInfo(BorderSide.All, 1.0f));

        Row row = newTable.getRows().add();
        row.getCells().add("Col 1");
        row.getCells().add("Col 2");
        row.getCells().add("Col 3");
        row = newTable.getRows().add();
        row.getCells().add("Col 12");
        row.getCells().add("Col 22");
        row.getCells().add("Col 32");

        absorber.replace(document.getPages().get_Item(1), oldTable, newTable);
        document.save(outputFile.toString());
    }
}
```
