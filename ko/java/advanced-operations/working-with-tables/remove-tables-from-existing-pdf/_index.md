---
title: 기존 PDF 문서에서 표 제거
linktitle: 테이블 제거
description: Java의 기존 PDF 문서에서 하나 이상의 테이블을 제거하는 방법을 알아보세요.
lastmod: "2026-06-09"
type: docs
weight: 50
url: /java/removing-tables/
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 파일에서 하나 이상의 테이블 삭제
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 기존 PDF 문서에서 테이블을 제거하는 방법을 설명합니다. 테이블 찾기를 위한 TableAbsorber를 소개하고 단일 테이블을 삭제하거나 페이지에서 감지된 모든 테이블을 제거하는 방법을 보여줍니다.
---
기존 PDF에서 감지된 테이블을 하나 이상 삭제해야 하는 경우 `TableAbsorber`을 사용하세요.


## 
감지된 테이블 1개 제거



페이지에서 일치하는 첫 번째 테이블만 삭제해야 하는 경우 이 예를 사용하세요.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/)로 대상 페이지를 방문하세요.
1. 처음 감지된 테이블을 제거하고 문서를 저장합니다.


```java
public static void removeOneTable(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));
        absorber.remove(absorber.getTableList().get(0));
        document.save(outputFile.toString());
    }
}
```

## 
페이지에서 감지된 모든 테이블을 제거합니다.



페이지에서 일치하는 모든 테이블을 제거해야 하는 경우 이 예를 사용하세요.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/)로 대상 페이지를 방문하고 감지된 테이블을 목록에 복사합니다.
1. 감지된 각 테이블을 제거하고 업데이트된 PDF를 저장합니다.

```java
public static void removeAllTables(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));
        List<AbsorbedTable> tables = new ArrayList<>(absorber.getTableList());
        for (AbsorbedTable table : tables) {
            absorber.remove(table);
        }
        document.save(outputFile.toString());
    }
}
```
