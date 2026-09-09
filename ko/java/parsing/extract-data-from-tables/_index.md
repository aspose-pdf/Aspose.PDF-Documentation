---
title: Java를 사용하여 PDF의 테이블에서 데이터 추출
linktitle: 테이블에서 데이터 추출
type: docs
weight: 40
url: /java/extract-data-from-table-in-pdf/
description: Aspose.PDF for Java를 사용하여 PDF 파일에서 테이블 데이터를 추출하고 추가 처리를 위해 감지된 테이블을 내보내는 방법을 알아보세요.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 통해 PDF의 테이블에서 데이터를 추출하는 방법
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서에서 테이블 데이터를 추출하고 처리하는 방법을 설명합니다. `TableAbsorber`으로 페이지를 스캔하고, 감지된 테이블에서 행과 셀을 읽고, 특정 주석이 달린 영역으로 추출을 제한하고, 결과를 Excel로 내보내는 방법을 보여줍니다.
---
## PDF에서 테이블 추출



`TableAbsorber`을 사용하여 각 페이지에서 테이블을 찾고 행, 셀, 텍스트 조각 및 텍스트 세그먼트를 반복합니다.


1. 
[문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
테이블은 페이지별로 감지되므로 문서 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 개체를 반복합니다.

1. 
각 페이지에 대해 [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/)를 생성하고 `visit(page)`을 호출하여 감지된 테이블 목록을 채웁니다.
1. 감지된 [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedtable/), [AbsorbedRow](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedrow/), [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedcell/), [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) 및 `TextSegment` 개체를 반복합니다.

1. 
조각 콘텐츠에서 추출된 행 텍스트를 작성하고 테이블 데이터를 인쇄합니다.


```java
public static void extractTablesFromPdf(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            TableAbsorber absorber = new TableAbsorber();
            absorber.visit(page);

            for (AbsorbedTable table : absorber.getTableList()) {
                System.out.println("Table");
                for (AbsorbedRow row : table.getRowList()) {
                    StringBuilder rowText = new StringBuilder();
                    for (AbsorbedCell cell : row.getCellList()) {
                        if (rowText.length() > 0) {
                            rowText.append("|");
                        }
                        StringBuilder cellText = new StringBuilder();
                        for (TextFragment fragment : cell.getTextFragments()) {
                            StringBuilder fragmentText = new StringBuilder();
                            for (TextSegment segment : fragment.getSegments()) {
                                fragmentText.append(segment.getText());
                            }
                            if (cellText.length() > 0) {
                                cellText.append("|");
                            }
                            cellText.append(fragmentText);
                        }
                        rowText.append(cellText);
                    }
                    System.out.println(rowText);
                }
            }
        }
    }
}
```

## 
특정 표시된 영역에서 테이블 추출



이 예에서는 정사각형 주석을 찾고, 해당 직사각형을 감지된 각 테이블과 비교하고, 표시된 영역 내부의 테이블만 출력합니다.


1. 
[문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.
1. 대상 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)을 가져오고 추출 영역을 표시하는 사각형 [주석](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/)을 찾습니다.

1. 
[TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/)를 만들고 `visit(page)`을 호출하여 해당 페이지의 테이블을 감지합니다.

1. 
감지된 각 [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedtable/) [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/)을 주석 직사각형 경계와 비교합니다.

1. 
일치하는 [AbsorbedRow](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedrow/) 및 [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedcell/) 개체를 반복하고 행 텍스트를 재구성합니다.

1. 
표시된 영역에 대한 테이블 데이터만 인쇄합니다.

```java
public static void extractTableFromSpecificArea(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        Annotation squareAnnotation = null;
        for (Annotation annotation : page.getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Square) {
                squareAnnotation = annotation;
                break;
            }
        }

        if (squareAnnotation == null) {
            System.out.println("No square annotation found.");
            return;
        }

        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(page);

        for (AbsorbedTable table : absorber.getTableList()) {
            Rectangle tableRect = table.getRectangle();
            Rectangle annotationRect = squareAnnotation.getRect();

            boolean isInRegion = annotationRect.getLLX() < tableRect.getLLX()
                    && annotationRect.getLLY() < tableRect.getLLY()
                    && annotationRect.getURX() > tableRect.getURX()
                    && annotationRect.getURY() > tableRect.getURY();

            if (isInRegion) {
                for (AbsorbedRow row : table.getRowList()) {
                    StringBuilder rowText = new StringBuilder();
                    for (AbsorbedCell cell : row.getCellList()) {
                        if (rowText.length() > 0) {
                            rowText.append("|");
                        }
                        StringBuilder cellText = new StringBuilder();
                        for (TextFragment fragment : cell.getTextFragments()) {
                            StringBuilder fragmentText = new StringBuilder();
                            for (TextSegment segment : fragment.getSegments()) {
                                fragmentText.append(segment.getText());
                            }
                            if (cellText.length() > 0) {
                                cellText.append("|");
                            }
                            cellText.append(fragmentText);
                        }
                        rowText.append(cellText);
                    }
                    System.out.println(rowText);
                }
            }
        }
    }
}
```

## 테이블을 Excel로 내보내기


1. 
[문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
내보내기를 위해 [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/)를 만듭니다.

1. 
Excel 출력 형식을 `XLSX`으로 설정하면 감지된 테이블 레이아웃이 Excel 통합 문서로 작성됩니다.

1. 
문서를 Excel 형식으로 내보내려면 `document.save(outputFile.toString(), excelSave)`으로 전화하세요.

```java
public static void exportTablesToExcel(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions excelSave = new ExcelSaveOptions();
        excelSave.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        document.save(outputFile.toString(), excelSave);
    }
}
```
