---
title: PDF에 테이블 생성 또는 추가
linktitle: 테이블 생성 또는 추가
type: docs
weight: 10
url: ko/java/add-table-in-existing-pdf-document/
description: PDF 문서에 테이블을 생성하거나 추가하는 방법, 셀 스타일 적용, 페이지에서 테이블 나누기 및 행과 열 사용자 정의 등을 배우세요.
lastmod: "2021-12-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 테이블 생성

Aspose.PDF 네임스페이스에는 PDF 문서를 처음부터 생성할 때 테이블을 생성하는 기능을 제공하는 [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table), [Cell](https://reference.aspose.com/pdf/java/com.aspose.pdf/cell), 및 [Row](https://reference.aspose.com/pdf/java/com.aspose.pdf/row)라는 클래스가 포함되어 있습니다.

테이블은 Table 클래스의 객체를 생성하여 만들 수 있습니다.

```java
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
```

### 기존 PDF 문서에 테이블 추가

Java용 Aspose.PDF로 기존 PDF 파일에 테이블을 추가하려면 다음 단계를 따르세요:

1. 소스 파일을 로드합니다.

1. 테이블을 초기화하고 열과 행을 설정합니다.
1. 테이블 설정을 설정합니다 (테두리를 설정했습니다).
1. 테이블을 채웁니다.
1. 페이지에 테이블을 추가합니다.
1. 파일을 저장합니다.

다음 코드 스니펫은 기존 PDF 파일에 텍스트를 추가하는 방법을 보여줍니다.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleAddTable {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void CreateTable() {
        Document doc = new Document(_dataDir + "input.pdf");
        // 테이블의 새 인스턴스를 초기화합니다
        Table table = new Table();
        // 테이블 테두리 색상을 연회색으로 설정합니다
        table.setBorder(new BorderInfo(BorderSide.All, .5f, Color.getLightGray()));
        // 테이블 셀의 테두리를 설정합니다
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, .5f, Color.getLightGray()));
        // 10개의 행을 추가하기 위한 루프를 생성합니다
        for (int row_count = 1; row_count < 10; row_count++) {
            // 테이블에 행을 추가합니다
            Row row = table.getRows().add();
            // 테이블 셀을 추가합니다
            row.getCells().add("열 (" + row_count + ", 1)");
            row.getCells().add("열 (" + row_count + ", 2)");
            row.getCells().add("열 (" + row_count + ", 3)");
        }
        // 입력 문서의 첫 번째 페이지에 테이블 객체를 추가합니다
        doc.getPages().get_Item(1).getParagraphs().add(table);
        // 테이블 객체를 포함하는 업데이트된 문서를 저장합니다
        doc.save(_dataDir + "document_with_table.pdf");
    }
```


### Aspose.PDF 테이블에서 ColSpan 및 RowSpan 사용 (Java)

Aspose.PDF for Java는 테이블의 열을 병합하기 위한 [setColSpan](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell#setColSpan-int-) 메서드와 행을 병합하기 위한 [setRowSpan](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell#setRowSpan-int-) 메서드를 제공합니다.

우리는 [Cell](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell) 객체에 [setColSpan](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell#setColSpan-int-) 또는 [setRowSpan](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell#setRowSpan-int-) 메서드를 사용하여 테이블 셀을 생성합니다. 필요한 속성을 적용한 후 생성된 셀을 테이블에 추가할 수 있습니다.

```java
public static void AddTable_RowColSpan() {
        // 소스 PDF 문서 로드
        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();

        // 테이블의 새 인스턴스를 초기화
        Table table = new Table();
        // 테이블 테두리 색상을 연회색으로 설정
        table.setBorder(new BorderInfo(BorderSide.All, .5f, Color.getBlack()));
        // 테이블 셀의 테두리 설정
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, .5f, Color.getBlack()));
        // 테이블에 첫 번째 행 추가
        Row row1 = table.getRows().add();
        for (int cellCount = 1; cellCount < 5; cellCount++) {
            // 테이블 셀 추가
            row1.getCells().add("Test 1 " + cellCount);
        }

        // 테이블에 두 번째 행 추가
        Row row2 = table.getRows().add();
        row2.getCells().add("Test 2 1");
        Cell cell = row2.getCells().add("Test 2 2");
        cell.setColSpan(2);
        row2.getCells().add("Test 2 4");

        // 테이블에 세 번째 행 추가
        Row row3 = table.getRows().add();
        row3.getCells().add("Test 3 1");
        row3.getCells().add("Test 3 2");
        row3.getCells().add("Test 3 3");
        row3.getCells().add("Test 3 4");

        // 테이블에 네 번째 행 추가
        Row row4 = table.getRows().add();
        row3.getCells().add("Test 4 1");
        cell = row3.getCells().add("Test 4 2");
        cell.setRowSpan(2);
        row3.getCells().add("Test 4 3");
        row3.getCells().add("Test 4 4");

        // 테이블에 다섯 번째 행 추가
        row4 = table.getRows().add();
        row4.getCells().add("Test 5 1");
        row4.getCells().add("Test 5 3");
        row4.getCells().add("Test 5 4");

        // 입력 문서의 첫 번째 페이지에 테이블 객체 추가
        page.getParagraphs().add(table);

        // 테이블 객체가 포함된 업데이트된 문서 저장
        pdfDocument.save(_dataDir + "document_with_table_out.pdf");
    }
```


코드 실행 결과는 다음 이미지에 묘사된 표입니다:

![ColSpan and RowSpan demo](colspan_rowspan.png)

## 경계, 여백 및 패딩 작업

Aspose.PDF for Java는 개발자가 PDF 문서에서 표를 생성할 수 있도록 합니다. Aspose.PDF의 문서 객체 모델에 따르면, 표는 단락 수준의 요소입니다.

또한 테이블에 대한 테두리 스타일, 여백 및 셀 패딩을 설정하는 기능도 지원합니다. 기술적 세부 사항으로 들어가기 전에, 아래 다이어그램에 제시된 테두리, 여백 및 패딩의 개념을 이해하는 것이 중요합니다:

![Borders, margins and padding](set-border-style-margins-and-padding-of-table_1.png)

위 그림에서 볼 수 있듯이 테이블, 행 및 셀의 테두리가 겹칩니다. Aspose.PDF를 사용하여 테이블은 여백을 가질 수 있으며 셀은 패딩을 가질 수 있습니다. 셀 여백을 설정하려면 셀 패딩을 설정해야 합니다.

## 테두리

[Table.setBorder](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table#setBorder-com.aspose.pdf.BorderInfo-), [Row.setBorder](https://reference.aspose.com/pdf/java/com.aspose.pdf/Row#setBorder-com.aspose.pdf.BorderInfo-) 및 [Cell.setBorder](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell#setBorder-com.aspose.pdf.BorderInfo-) 메서드를 사용하여 Table, [Row](https://reference.aspose.com/pdf/java/com.aspose.pdf/row) 및 [Cell](https://reference.aspose.com/pdf/java/com.aspose.pdf/cell) 객체의 테두리를 설정하십시오.
 셀 테두리는 [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table) 또는 [Row](https://reference.aspose.com/pdf/java/com.aspose.pdf/row) 클래스 [DefaultCellBorder](https://reference.aspose.com/pdf/java/com.aspose.pdf/Row#setDefaultCellBorder-com.aspose.pdf.BorderInfo-) 메서드를 사용하여 설정할 수 있습니다. 위에서 논의한 모든 테두리 관련 속성은 생성자를 호출하여 생성된 Row 클래스의 인스턴스에 할당됩니다. Row 클래스는 테두리를 사용자 지정하는 데 필요한 거의 모든 매개변수를 받는 많은 오버로드를 가지고 있습니다.

## 여백 또는 패딩

셀 패딩은 Table 클래스 [DefaultCellPadding](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table#setDefaultCellPadding-com.aspose.pdf.MarginInfo-) 메서드를 사용하여 관리할 수 있습니다. 모든 패딩 관련 속성은 사용자 정의 여백을 만들기 위해 `Left`, `Right`, `Top` 및 `Bottom` 매개변수에 대한 정보를 가져오는 [MarginInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/MarginInfo) 클래스의 인스턴스로 할당됩니다.

다음 예제에서는 셀 테두리의 너비를 0.1 포인트로 설정하고, 테이블 테두리의 너비를 1 포인트로 설정하며 셀 패딩을 5 포인트로 설정합니다.

![PDF 테이블의 여백 및 테두리](margin-border.png)

```java
public static void MargingPadding() {
        // 빈 생성자를 호출하여 Document 객체를 생성합니다.
        Document doc = new Document();
        Page page = doc.getPages().add();
        // 테이블 객체를 인스턴스화합니다.
        Table tab1 = new Table();
        // 원하는 섹션의 단락 컬렉션에 테이블을 추가합니다.
        page.getParagraphs().add(tab1);
        // 테이블의 열 너비를 설정합니다.
        tab1.setColumnWidths ("50 50 50");
        // BorderInfo 객체를 사용하여 기본 셀 테두리를 설정합니다.
        tab1.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.1F));
        // 다른 맞춤형 BorderInfo 객체를 사용하여 테이블 테두리를 설정합니다.
        tab1.setBorder (new BorderInfo(BorderSide.All, 1F));

        // MarginInfo 객체를 생성하고 왼쪽, 아래쪽, 오른쪽 및 위쪽 여백을 설정합니다.
        MarginInfo margin = new MarginInfo();
        margin.setTop (5f);
        margin.setLeft (5f);
        margin.setRight (5f);
        margin.setBottom (5f);

        // MarginInfo 객체에 기본 셀 패딩을 설정합니다.
        tab1.setDefaultCellPadding(margin);

        // 테이블에 행을 만들고 행에 셀을 만듭니다.
        Row row1 = tab1.getRows().add();
        row1.getCells().add("col1");
        row1.getCells().add("col2");
        row1.getCells().add();

        TextFragment mytext = new TextFragment("col3 with large text string");

        row1.getCells().get_Item(2).getParagraphs().add(mytext);
        row1.getCells().get_Item(2).setWordWrapped(false);

        Row row2 = tab1.getRows().add();
        row2.getCells().add("item1");
        row2.getCells().add("item2");
        row2.getCells().add("item3");

        // PDF 저장
        doc.save(_dataDir + "MarginsOrPadding_out.pdf");
    }
}
```

테이블을 둥근 모서리로 만들려면 [BorderInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/BorderInfo) 클래스의 `RoundedBorderRadius` 값을 사용하고 테이블 모서리 스타일을 둥글게 설정하십시오.

```java
    public static void RoundedBorderRadius() {
        Document doc = new Document();
        Page page = doc.getPages().add();

        // 테이블 객체를 인스턴스화합니다.
        Table tab1 = new Table();

        // 원하는 섹션의 단락 컬렉션에 테이블을 추가합니다.
        page.getParagraphs().add(tab1);

        GraphInfo graph = new GraphInfo();
        graph.setColor(Color.getRed());
        // 빈 BorderInfo 객체를 생성합니다.
        BorderInfo bInfo = new BorderInfo(BorderSide.All, graph);
        // 반지름이 15인 둥근 테두리를 설정합니다.
        bInfo.setRoundedBorderRadius(15);
        // 테이블 모서리 스타일을 둥글게 설정합니다.
        tab1.setCornerStyle(BorderCornerStyle.Round);
        // 테이블 테두리 정보를 설정합니다.
        tab1.setBorder(bInfo);
        // 테이블에 행을 생성하고 행에 셀을 추가합니다.
        Row row1 = tab1.getRows().add();
        row1.getCells().add("col1");
        row1.getCells().add("col2");
        row1.getCells().add();

        TextFragment mytext = new TextFragment("col3 with large text string");

        row1.getCells().get_Item(2).getParagraphs().add(mytext);
        row1.getCells().get_Item(2).setWordWrapped(false);

        Row row2 = tab1.getRows().add();
        row2.getCells().add("item1");
        row2.getCells().add("item2");
        row2.getCells().add("item3");

        // PDF를 저장합니다.
        doc.save(_dataDir + "BorderRadius_out.pdf");
    }
```


### ColumnAdjustmentType 열거형의 AutoFitToWindow 속성

```java
 public static void AutoFitToWindowProperty() {
        // 빈 생성자를 호출하여 Pdf 객체를 인스턴스화합니다
        Document doc = new Document();
        // Pdf 객체에 섹션을 생성합니다
        Page sec1 = doc.getPages().add();

        // 테이블 객체를 인스턴스화합니다
        Table tab1 = new Table();
        // 원하는 섹션의 단락 컬렉션에 테이블을 추가합니다
        sec1.getParagraphs().add(tab1);

        // 테이블의 열 너비를 설정합니다
        tab1.setColumnWidths("50 50 50");
        tab1.setColumnAdjustment(ColumnAdjustment.AutoFitToWindow);

        // BorderInfo 객체를 사용하여 기본 셀 테두리를 설정합니다
        tab1.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.1F));

        // 다른 맞춤형 BorderInfo 객체를 사용하여 테이블 테두리를 설정합니다
        tab1.setBorder(new BorderInfo(BorderSide.All, 1F));

        // MarginInfo 객체를 생성하고 왼쪽, 아래, 오른쪽, 위쪽 여백을 설정합니다
        MarginInfo margin = new MarginInfo();
        margin.setTop(5f);
        margin.setLeft(5f);
        margin.setRight(5f);
        margin.setBottom(5f);

        // MarginInfo 객체에 기본 셀 패딩을 설정합니다
        tab1.setDefaultCellPadding(margin);

        // 테이블에 행을 생성한 다음 행에 셀을 만듭니다
        Row row1 = tab1.getRows().add();
        row1.getCells().add("col1");
        row1.getCells().add("col2");
        row1.getCells().add("col3");
        Row row2 = tab1.getRows().add();
        row2.getCells().add("item1");
        row2.getCells().add("item2");
        row2.getCells().add("item3");

        // 테이블 객체를 포함하는 업데이트된 문서를 저장합니다
        doc.save(_dataDir + "AutoFitToWindow_out.pdf");
    }
```


### 테이블 너비 가져오기

때때로 테이블 너비를 동적으로 가져와야 할 때가 있습니다. Aspose.PDF.Table 클래스에는 이를 위한 [GetWidth](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table#getWidth--) 메서드가 있습니다. 예를 들어, 테이블 열 너비를 명시적으로 설정하지 않고 [ColumnAdjustment](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColumnAdjustment)를 AutoFitToContent로 설정한 경우, 다음과 같이 테이블 너비를 가져올 수 있습니다.

```java
public static void GetTableWidth() {
        // 새 문서 생성
        Document doc = new Document();
        // 문서에 페이지 추가
        Page page = doc.getPages().add();

        // 새 테이블 초기화
        Table table = new Table();

        // 원하는 섹션의 문단 컬렉션에 테이블 추가
        page.getParagraphs().add(table);
        table.setColumnAdjustment(ColumnAdjustment.AutoFitToContent);

        // 테이블에 행 추가
        Row row = table.getRows().add();
        // 테이블에 셀 추가
        row.getCells().add("셀 1 텍스트");
        row.getCells().add("셀 2 텍스트");
        // 테이블 너비 가져오기
        System.out.println(table.getWidth());
    }
```


## 테이블 셀에 SVG 객체 추가하기

Aspose.PDF for Java는 PDF 파일에 테이블 셀을 추가하는 기능을 지원합니다. 테이블을 생성하는 동안, 셀에 텍스트나 이미지를 추가할 수 있습니다. 또한, API는 SVG 파일을 PDF 형식으로 변환하는 기능도 제공합니다. 이러한 기능을 조합하여 SVG 이미지를 로드하고 테이블 셀에 추가할 수 있습니다.

다음 코드 스니펫은 테이블 인스턴스를 생성하고 테이블 셀 안에 SVG 이미지를 추가하는 단계를 보여줍니다.

```java
 public static void AddSVGObjectToTableCell() {
        // Document 객체 인스턴스화
        Document doc = new Document();
        // 이미지 인스턴스 생성
        com.aspose.pdf.Image img = new com.aspose.pdf.Image();
        // 이미지 유형을 SVG로 설정
        img.setFileType (com.aspose.pdf.ImageFileType.Svg);
        // 원본 파일 경로
        img.setFile (_dataDir + "SVGToPDF.svg");
        // 이미지 인스턴스의 너비 설정
        img.setFixWidth (50);
        // 이미지 인스턴스의 높이 설정
        img.setFixHeight (50);
        // 테이블 인스턴스 생성
        com.aspose.pdf.Table table = new com.aspose.pdf.Table();
        // 테이블 셀의 너비 설정
        table.setColumnWidths ("100 100");
        // 행 객체 생성 및 테이블 인스턴스에 추가
        com.aspose.pdf.Row row = table.getRows().add();
        // 셀 객체 생성 및 행 인스턴스에 추가
        com.aspose.pdf.Cell cell = row.getCells().add();
        // 셀 객체의 단락 컬렉션에 텍스트 조각 추가
        cell.getParagraphs().add(new TextFragment("First cell"));
        // 행 객체에 또 다른 셀 추가
        cell = row.getCells().add();
        // 최근에 추가된 셀 인스턴스의 단락 컬렉션에 SVG 이미지 추가
        cell.getParagraphs().add(img);
        // 페이지 객체 생성 및 문서 인스턴스의 페이지 컬렉션에 추가
        Page page = doc.getPages().add();
        // 페이지 객체의 단락 컬렉션에 테이블 추가
        page.getParagraphs().add(table);
        // PDF 파일 저장
        doc.save(_dataDir + "AddSVGObject_out.pdf");
    }
```


## 테이블 내에 HTML 태그 추가

Aspose.PDF for Java를 사용하면 PDF 파일의 단락에 새로운 HTML 조각을 추가할 수 있습니다.

{{% alert color="primary" %}}

테이블 요소 내에서 HTML 태그를 사용할 경우, API가 HTML 태그를 처리하고 출력 PDF 문서에 렌더링해야 하므로 문서 생성 시간이 증가한다는 점을 유의하세요.

{{% /alert %}}

```java
  public static void AddHTMLFragmentToTableCell() {
        Document doc = new Document(_dataDir + "input.pdf");
        // 테이블의 새 인스턴스를 초기화합니다.
        Table table = new Table();
        // 테이블 테두리 색상을 LightGray로 설정합니다.
        table.setBorder(new BorderInfo(BorderSide.All, .5f, Color.getLightGray()));
        // 테이블 셀의 테두리를 설정합니다.
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, .5f, Color.getLightGray()));
        // 10개의 행을 추가하는 루프를 만듭니다.
        for (int row_count = 1; row_count < 10; row_count++) {
            Cell cell;
            // 테이블에 행을 추가합니다.
            Row row = table.getRows().add();
            // 테이블 셀을 추가합니다.
            cell = row.getCells().add();
            cell.getParagraphs().add(new HtmlFragment("Column <strong>(" + row_count + ", 1)</strong>"));

            cell = row.getCells().add();
            cell.getParagraphs().add(new HtmlFragment("Column <span style='color:red'>(" + row_count + ", 2)</span>"));

            cell = row.getCells().add();
            cell.getParagraphs().add(new HtmlFragment("Column <span style='text-decoration: underline'>(" + row_count + ", 3)</span>"));
        }
        // 입력 문서의 첫 번째 페이지에 테이블 객체를 추가합니다.
        doc.getPages().get_Item(1).getParagraphs().add(table);
        // 테이블 객체가 포함된 업데이트된 문서를 저장합니다.
        doc.save(_dataDir + "AddHTMLObject_out.pdf");
    }

}
```


## 테이블 행 사이에 페이지 나누기 삽입

기본 동작으로, PDF 파일 내에 테이블을 생성할 때, 테이블이 하단 여백에 도달하면 다음 페이지로 흐릅니다. 그러나 테이블에 특정 행 수가 추가될 때 강제로 페이지 나누기를 삽입해야 할 필요가 있을 수 있습니다. 다음 코드 스니펫은 테이블에 10개의 행이 추가될 때 페이지 나누기를 삽입하는 단계를 보여줍니다.

```java
    public static void InsertPageBreak() {
        // Document 인스턴스 생성
        Document doc = new Document();
        // PDF 파일의 페이지 컬렉션에 페이지 추가
        Page page = doc.getPages().add();
        // Table 인스턴스 생성
        Table tab = new Table();
        // 테이블의 테두리 스타일 설정
        tab.setBorder (new BorderInfo(BorderSide.All, Color.getRed()));
        // 테이블의 기본 테두리 스타일을 빨간색으로 설정
        tab.setDefaultCellBorder (new BorderInfo(BorderSide.All, Color.getRed()));
        // 테이블 열 너비 지정
        tab.setColumnWidths ("100 100");
        // 테이블에 200개의 행을 추가하는 루프 생성
        for (int counter = 0; counter <= 200; counter++) {
            Row row = new Row();
            tab.getRows().add(row);
            Cell cell1 = new Cell();
            cell1.getParagraphs().add(new TextFragment("Cell " + counter + ", 0"));
            row.getCells().add(cell1);
            Cell cell2 = new Cell();
            cell2.getParagraphs().add(new TextFragment("Cell " + counter + ", 1"));
            row.getCells().add(cell2);
            // 10개의 행이 추가되면, 새로운 페이지에 새 행을 렌더링
            if (counter % 10 == 0 && counter != 0)
                row.setInNewPage(true);
        }
        // 테이블을 PDF 파일의 단락 컬렉션에 추가
        page.getParagraphs().add(tab);

        // PDF 문서 저장
        doc.save(_dataDir + "InsertPageBreak_out.pdf");
    }
```


## 스팬된 셀 테두리 숨기기

셀을 테이블에 추가할 때, 스팬된 셀 테두리는 다른 행으로 넘어갈 때 나타날 수 있습니다. 이러한 스팬된 테두리는 다음 코드 샘플과 같이 숨길 수 있습니다.

```java
Document doc = new Document();
com.aspose.pdf.Page page = doc.getPages().add();

// 내부 테이블에 중첩될 테이블 객체를 생성합니다. 동일한 페이지 내에서 깨질 것입니다.
com.aspose.pdf.Table mytable = new com.aspose.pdf.Table();
mytable.setBroken(TableBroken.Vertical);
mytable.setDefaultCellBorder(new BorderInfo(BorderSide.All));
mytable.setRepeatingColumnsCount(2);
page.getParagraphs().add(mytable);

// 헤더 행 추가
com.aspose.pdf.Row row = mytable.getRows().add();
Cell cell = row.getCells().add("header 1");
cell.setColSpan(2);
cell.setBackgroundColor(Color.getLightGray());
Cell header3 = row.getCells().add("header 3");
Cell cell2 = row.getCells().add("header 4");
cell2.setColSpan(2);
cell2.setBackgroundColor(Color.getLightBlue());
row.getCells().add("header 6");
Cell cell3 = row.getCells().add("header 7");
cell3.setColSpan(2);
cell3.setBackgroundColor(Color.getLightGreen());
Cell cell4 = row.getCells().add("header 9");
cell4.setColSpan(3);
cell4.setBackgroundColor(Color.getLightCoral());
row.getCells().add("header 12");
row.getCells().add("header 13");
row.getCells().add("header 14");
row.getCells().add("header 15");
row.getCells().add("header 16");
row.getCells().add("header 17");

for (int rowCounter = 0; rowCounter < 1; rowCounter++)
{
  // 테이블에 행을 생성한 후 행에 셀을 추가합니다.
  com.aspose.pdf.Row row1 = mytable.getRows().add();
  row1.getCells().add("col "+rowCounter+", 1");
  row1.getCells().add("col "+rowCounter+", 2");
  row1.getCells().add("col "+rowCounter+", 3");
  row1.getCells().add("col "+rowCounter+", 4");
  row1.getCells().add("col "+rowCounter+", 5");
  row1.getCells().add("col "+rowCounter+", 6");
  row1.getCells().add("col "+rowCounter+", 7");
  row1.getCells().add("col "+rowCounter+", 8");
  row1.getCells().add("col "+rowCounter+", 9");
  row1.getCells().add("col "+rowCounter+", 10");
  row1.getCells().add("col "+rowCounter+", 11");
  row1.getCells().add("col "+rowCounter+", 12");
  row1.getCells().add("col "+rowCounter+", 13");
  row1.getCells().add("col "+rowCounter+", 14");
  row1.getCells().add("col "+rowCounter+", 15");
  row1.getCells().add("col "+rowCounter+", 16");
  row1.getCells().add("col "+rowCounter+", 17");
}
doc.save(dataDir + "3_out.pdf");
```