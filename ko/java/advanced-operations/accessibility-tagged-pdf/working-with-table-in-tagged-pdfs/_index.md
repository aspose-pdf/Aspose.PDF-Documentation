---
title: Java에서 태그가 있는 PDF의 표 작업
linktitle: 태그가 있는 PDF의 표 작업
type: docs
weight: 40
url: /java/working-with-table-in-tagged-pdfs/
description: 테이블 구조, 셀 범위, 스타일 지정, 행 설정 및 위치 지정을 포함하여 Aspose.PDF를 사용하여 Java에서 태그가 지정된 PDF의 액세스 가능한 테이블로 작업하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

태그가 있는 테이블 API를 사용하면 명시적인 머리글, 본문 행, 바닥글 및 셀별 의미 체계를 사용하여 액세스 가능한 테이블 구조를 만들 수 있습니다.


## 
태그가 지정된 테이블 만들기



머리글, 본문, 바닥글 및 테이블 요약 메타데이터가 포함된 기본 액세스 가능 테이블이 필요한 경우 이 예를 사용하십시오.


1. 
새 태그가 있는 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만들고 [TableElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/tableelement/)를 추가합니다.

1. 
테이블 테두리를 구성하고 공유 도우미 메서드로 콘텐츠를 채웁니다.

1. 
테이블 요약 속성을 설정하고 문서를 저장합니다.


```java
public static void createTable(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Example table");
        taggedContent.setLanguage("en-US");

        TableElement tableElement = taggedContent.createTableElement();
        taggedContent.getRootElement().appendChild(tableElement, true);
        tableElement.setBorder(new BorderInfo(BorderSide.All, 1.2f, Color.getDarkBlue()));

        fillTable(tableElement, 50, 4, true);

        StructureAttributes tableAttributes = tableElement.getAttributes().getAttributes(AttributeOwnerStandard.Table);
        StructureAttribute summaryAttribute = new StructureAttribute(AttributeKey.Summary);
        summaryAttribute.setStringValue("The summary text for table");
        tableAttributes.setAttribute(summaryAttribute);

        document.save(outputFile.toString());
    }
}
```

## 
태그가 지정된 테이블 스타일 지정



이 예에서는 색상, 테두리, 열 크기 조정, 반복 행 및 정렬과 같은 테이블 수준 서식을 적용합니다.


1. 
새 태그가 있는 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만들고 테이블 요소를 추가합니다.

1. 
테이블 수준 시각적 개체 및 레이아웃 설정을 구성합니다.

1. 
테이블을 채우고 문서를 저장합니다.


```java
public static void styleTable(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Example table style");
        taggedContent.setLanguage("en-US");

        TableElement tableElement = taggedContent.createTableElement();
        taggedContent.getRootElement().appendChild(tableElement, true);

        tableElement.setBackgroundColor(Color.getBeige());
        tableElement.setBorder(new BorderInfo(BorderSide.All, 0.80f, Color.getGray()));
        tableElement.setAlignment(HorizontalAlignment.Center);
        tableElement.setBroken(TableBroken.Vertical);
        tableElement.setColumnAdjustment(ColumnAdjustment.AutoFitToWindow);
        tableElement.setColumnWidths("80 80 80 80 80");
        tableElement.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.50f, Color.getDarkBlue()));
        tableElement.setDefaultCellPadding(new MarginInfo(16.0, 2.0, 8.0, 2.0));
        tableElement.getDefaultCellTextState().setForegroundColor(Color.getDarkCyan());
        tableElement.getDefaultCellTextState().setFontSize(8.0f);
        tableElement.setDefaultColumnWidth("70");
        tableElement.setBordersIncluded(true);
        tableElement.setLeft(0.0f);
        tableElement.setTop(40.0f);
        tableElement.setRepeatingColumnsCount(2);
        tableElement.setRepeatingRowsCount(3);

        TextState rowStyle = new TextState();
        rowStyle.setBackgroundColor(Color.getLightCoral());
        tableElement.setRepeatingRowsStyle(rowStyle);

        fillTable(tableElement, 10, 5, false);
        document.save(outputFile.toString());
    }
}
```

## 
태그가 지정된 테이블 행 스타일 지정



각 행에 고유한 메타데이터, 테두리, 높이 설정 및 셀 기본값이 있어야 하는 경우 이 예를 사용합니다.


1. 
새 태그가 있는 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만들고 머리, 몸, 발에 대한 테이블 섹션을 추가합니다.

1. 
행을 만들고 테두리, 안쪽 여백, 높이, 페이지 동작 등 행 수준 설정을 구성합니다.

1. 
행을 셀로 채우고 문서를 저장합니다.


```java
public static void styleTableRow(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Example table style");
        taggedContent.setLanguage("en-US");

        TableElement tableElement = taggedContent.createTableElement();
        taggedContent.getRootElement().appendChild(tableElement, true);
        TableTHeadElement tableTHeadElement = tableElement.createTHead();
        TableTBodyElement tableTBodyElement = tableElement.createTBody();
        TableTFootElement tableTFootElement = tableElement.createTFoot();

        TableTRElement headTrElement = tableTHeadElement.createTR();
        headTrElement.setAlternativeText("Head Row");
        for (int colIndex = 0; colIndex < 3; colIndex++) {
            headTrElement.createTH().setText("Head " + colIndex);
        }

        for (int rowIndex = 0; rowIndex < 7; rowIndex++) {
            TableTRElement trElement = tableTBodyElement.createTR();
            trElement.setAlternativeText("Row " + rowIndex);
            trElement.setBackgroundColor(Color.getLightGoldenrodYellow());
            trElement.setBorder(new BorderInfo(BorderSide.All, 0.75f, Color.getDarkGray()));
            trElement.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.50f, Color.getBlue()));
            trElement.setMinRowHeight(100.0);
            trElement.setFixedRowHeight(120.0);
            trElement.setInNewPage(rowIndex % 3 == 1);
            trElement.setRowBroken(true);

            TextState cellTextState = new TextState();
            cellTextState.setForegroundColor(Color.getRed());
            trElement.setDefaultCellTextState(cellTextState);
            trElement.setDefaultCellPadding(new MarginInfo(16.0, 2.0, 8.0, 2.0));
            trElement.setVerticalAlignment(VerticalAlignment.Bottom);

            for (int colIndex = 0; colIndex < 3; colIndex++) {
                trElement.createTD().setText("Cell [" + rowIndex + ", " + colIndex + "]");
            }
        }

        TableTRElement footTrElement = tableTFootElement.createTR();
        footTrElement.setAlternativeText("Foot Row");
        for (int colIndex = 0; colIndex < 3; colIndex++) {
            footTrElement.createTD().setText("Foot " + colIndex);
        }

        document.save(outputFile.toString());
    }
}
```

## 
스타일 태그가 지정된 표 셀



이 예에서는 공유 도우미 메서드를 사용하여 셀 수준 서식 및 병합된 셀이 포함된 테이블을 만듭니다.


1. 
새 태그가 있는 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만듭니다.

1. 
테이블 요소를 추가하고 셀 스타일 지정이 활성화된 도우미 메서드를 통해 요소를 채웁니다.

1. 
문서를 저장합니다.


```java
public static void styleTableCell(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Example table cell style");
        taggedContent.setLanguage("en-US");

        TableElement tableElement = taggedContent.createTableElement();
        taggedContent.getRootElement().appendChild(tableElement, true);
        fillTable(tableElement, 4, 4, true);

        document.save(outputFile.toString());
    }
}
```

## 
태그가 지정된 테이블 위치 조정



태그가 지정된 테이블을 페이지에 명시적으로 배치해야 하는 경우 이 예를 사용하세요.


1. 
새 태그가 있는 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만들고 테이블 요소를 추가합니다.

1. 
테이블에 대한 [PositionSettings](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure/positionsettings/)를 구성합니다.

1. 
위치 설정을 적용하고 테이블을 채운 다음 문서를 저장합니다.


```java
public static void adjustTablePosition(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Example table position");
        taggedContent.setLanguage("en-US");

        TableElement tableElement = taggedContent.createTableElement();
        taggedContent.getRootElement().appendChild(tableElement, true);

        PositionSettings positionSettings = new PositionSettings();
        positionSettings.setHorizontalAlignment(HorizontalAlignment.None);
        positionSettings.setMargin(new MarginInfo(20, 0, 0, 0));
        positionSettings.setVerticalAlignment(VerticalAlignment.None);
        positionSettings.setFirstParagraphInColumn(false);
        positionSettings.setKeptWithNext(false);
        positionSettings.setInNewPage(false);
        positionSettings.setInLineParagraph(false);
        tableElement.adjustPosition(positionSettings);

        fillTable(tableElement, 4, 4, true);
        document.save(outputFile.toString());
    }
}
```

## 
구조화된 콘텐츠로 태그가 지정된 테이블 채우기



이 도우미 메서드는 테이블의 머리글, 본문, 바닥글 행을 만들고 선택적으로 셀 스타일과 범위를 적용합니다.


1. 
테이블 머리 부분, 몸체 부분, 바닥 부분을 만듭니다.

1. 
머리글, 본문, 바닥글 행을 액세스 가능한 셀 요소로 채웁니다.

1. 
필요에 따라 스타일이 지정된 셀, 병합된 셀 및 텍스트 상태 값을 구성합니다.

```java
private static void fillTable(TableElement tableElement, int rowCount, int colCount, boolean styleCells) {
    TableTHeadElement tableTHeadElement = tableElement.createTHead();
    TableTBodyElement tableTBodyElement = tableElement.createTBody();
    TableTFootElement tableTFootElement = tableElement.createTFoot();

    TableTRElement headTrElement = tableTHeadElement.createTR();
    headTrElement.setAlternativeText("Head Row");
    headTrElement.setBackgroundColor(Color.getLightGray());

    for (int columnIndex = 0; columnIndex < colCount; columnIndex++) {
        TableTHElement thElement = headTrElement.createTH();
        thElement.setText("Head " + columnIndex);
        thElement.setBackgroundColor(Color.getGreenYellow());
        thElement.setBorder(new BorderInfo(BorderSide.All, 4.0f, Color.getGray()));
        thElement.setNoBorder(true);
        thElement.setMargin(new MarginInfo(16.0, 2.0, 8.0, 2.0));
        thElement.setAlignment(HorizontalAlignment.Right);
    }

    for (int rowIndex = 0; rowIndex < rowCount; rowIndex++) {
        TableTRElement trElement = tableTBodyElement.createTR();
        trElement.setAlternativeText("Row " + rowIndex);

        for (int columnIndex = 0; columnIndex < colCount; columnIndex++) {
            int colSpan = 1;
            int rowSpan = 1;

            if (styleCells && columnIndex == 1 && rowIndex == 1) {
                colSpan = 2;
                rowSpan = 2;
            } else if (styleCells && ((rowIndex == 1 && columnIndex == 2)
                    || (rowIndex == 2 && (columnIndex == 1 || columnIndex == 2)))) {
                continue;
            }

            TableTDElement tdElement = trElement.createTD();
            tdElement.setText("Cell [" + rowIndex + ", " + columnIndex + "]");
            tdElement.setBackgroundColor(Color.getYellow());
            tdElement.setBorder(new BorderInfo(BorderSide.All, 4.0f, Color.getGray()));
            tdElement.setNoBorder(false);
            tdElement.setMargin(new MarginInfo(8.0, 2.0, 8.0, 2.0));
            tdElement.setAlignment(HorizontalAlignment.Center);

            TextState cellTextState = new TextState();
            cellTextState.setForegroundColor(Color.getDarkBlue());
            cellTextState.setFontSize(7.5f);
            cellTextState.setFontStyle(FontStyles.Bold);
            cellTextState.setFont(FontRepository.findFont("Arial"));
            tdElement.setDefaultCellTextState(cellTextState);

            tdElement.setWordWrapped(true);
            tdElement.setVerticalAlignment(VerticalAlignment.Center);
            tdElement.setColSpan(colSpan);
            tdElement.setRowSpan(rowSpan);
        }
    }

    TableTRElement footTrElement = tableTFootElement.createTR();
    footTrElement.setAlternativeText("Foot Row");
    footTrElement.setBackgroundColor(Color.getLightSeaGreen());

    for (int columnIndex = 0; columnIndex < colCount; columnIndex++) {
        TableTDElement tdElement = footTrElement.createTD();
        tdElement.setText("Foot " + columnIndex);
        tdElement.setAlignment(HorizontalAlignment.Center);
        tdElement.getStructureTextState().setFontSize(com.aspose.pdf.Nullable.of(7.0f));
        tdElement.getStructureTextState().setFontStyle(com.aspose.pdf.Nullable.of(FontStyles.Bold));
    }
}
```
