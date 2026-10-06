---
title: Trabalhar com tabelas em Tagged PDFs em Java
linktitle: Trabalhar com tabela em Tagged PDFs
type: docs
weight: 40
url: /pt/java/working-with-table-in-tagged-pdfs/
description: Aprenda a trabalhar com tabelas acessíveis em PDFs marcados em Java com Aspose.PDF, incluindo estrutura da tabela, mesclagem de células, estilização, configurações de linhas e posicionamento.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
Tagged table APIs permitem criar estruturas de tabela acessíveis com cabeçalhos explícitos, linhas de corpo, rodapés e semântica por célula.

## Criar uma tabela marcada

Use este exemplo quando precisar de uma tabela acessível básica com cabeçalho, corpo, rodapé e metadados de resumo da tabela.

1. Crie um novo Tagged PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e adicione um [TableElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/tableelement/).
1. Configure a borda da tabela e preencha o conteúdo com o método auxiliar compartilhado.
1. Defina o atributo de resumo da tabela e salve o documento.

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

## Estilizar uma tabela marcada

Este exemplo aplica formatação ao nível da tabela, como cores, bordas, dimensionamento de colunas, linhas repetidas e alinhamento.

1. Crie um novo Tagged PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e adicione um elemento de tabela.
1. Configure as configurações visuais e de layout da tabela.
1. Preencha a tabela e salve o documento.

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

## Estilizar linhas de tabela marcadas

Use este exemplo quando cada linha deve ter seus próprios metadados, bordas, configurações de altura e padrões de célula.

1. Crie um novo Tagged PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e adicione seções de tabela para cabeçalho, corpo e rodapé.
1. Crie linhas e configure as configurações em nível de linha, como borda, preenchimento, altura e comportamento da página.
1. Preencha as linhas com células e salve o documento.

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

## Estilizar células de tabela marcadas

Este exemplo usa o método auxiliar compartilhado para criar uma tabela com formatação a nível de célula e células mescladas.

1. Crie um novo Tagged PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Adicione um elemento de tabela e preencha‑o através do método auxiliar com a estilização de célula habilitada.
1. Salve o documento.

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

## Ajustar posição da tabela marcada

Use este exemplo quando uma tabela marcada deve ser posicionada explicitamente na página.

1. Crie um novo Tagged PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e adicione um elemento de tabela.
1. Configure [PositionSettings](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure/positionsettings/) para a tabela.
1. Aplique as configurações de posição, preencha a tabela e salve o documento.

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

## Preencher uma tabela marcada com conteúdo estruturado

Este método auxiliar cria as linhas de cabeçalho, corpo e rodapé de uma tabela e, opcionalmente, aplica estilos de célula e mesclagens.

1. Crie as seções de cabeçalho, corpo e rodapé da tabela.
1. Preencha as linhas de cabeçalho, corpo e rodapé com elementos de célula acessíveis.
1. Opcionalmente, configure células estilizadas, células mescladas e valores de estado de texto.

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
