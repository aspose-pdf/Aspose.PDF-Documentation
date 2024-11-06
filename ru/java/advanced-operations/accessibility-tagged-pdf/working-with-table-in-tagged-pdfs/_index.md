---
title: Работа с таблицей в Tagged PDF
linktitle: Работа с таблицей в Tagged PDF
type: docs
weight: 40
url: ru/java/working-with-table-in-tagged-pdfs/
description: В этой статье объясняется, как работать с таблицей в документе Tagged PDF с помощью Aspose.PDF для Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Эта функция поддерживается в версии 19.6 или выше.

{{% /alert %}}

## Создание таблицы в Tagged PDF

Aspose.PDF для Java позволяет создавать таблицы в документах Tagged PDF.
 Для работы с таблицами API предоставляет класс [TableElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableElement). In order to create a table, you can use [createTableElement()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent#createTableElement--) method of [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent) interface.

Чтобы создать таблицу, вы можете использовать метод [createTableElement()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent#createTableElement--) интерфейса [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). Кроме того, вы можете использовать методы [createTHead()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableElement#createTHead--), [createTBody()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableElement#createTBody--) и [createTFoot()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableElement#createTFoot--) класса TableElement для создания заголовка таблицы, тела таблицы и нижнего колонтитула таблицы соответственно. Для создания строки таблицы вы можете использовать метод [createTR()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableRowCollectionElement#createTR--) класса [TableRowCollectionElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableRowCollectionElement). Следующий фрагмент кода показывает, как создать таблицу в документе Tagged PDF:

```java
// Для полноценных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Путь к каталогу документов.
String path = Utils.getDataDir() + "TaggedPDFs\\";

// Создать документ
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("Пример таблицы");
taggedContent.setLanguage("en-US");

// Получить корневой элемент структуры
StructureElement rootElement = taggedContent.getRootElement();

TableElement tableElement = taggedContent.createTableElement();
rootElement.appendChild(tableElement);

tableElement.setBorder(new BorderInfo(BorderSide.All, 1.2F, Color.getDarkBlue()));

TableTHeadElement tableTHeadElement = tableElement.createTHead();
TableTBodyElement tableTBodyElement = tableElement.createTBody();
TableTFootElement tableTFootElement = tableElement.createTFoot();
int rowCount = 50;
int colCount = 4;
int rowIndex;
int colIndex;

TableTRElement headTrElement = tableTHeadElement.createTR();
headTrElement.setAlternativeText("Строка заголовка");

headTrElement.setBackgroundColor(Color.getLightGray());

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTHElement thElement = headTrElement.createTH();
    thElement.setText(String.format("Заголовок %s", colIndex));

    thElement.setBackgroundColor(Color.getGreenYellow());
    thElement.setBorder(new BorderInfo(BorderSide.All, 4.0F, Color.getLightGray()));

    thElement.setMargin(new MarginInfo(16.0, 2.0, 8.0, 2.0));

    thElement.setAlignment(HorizontalAlignment.Right);
}

for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
{
    TableTRElement trElement = tableTBodyElement.createTR();
    trElement.setAlternativeText(String.format("Строка %s", rowIndex));

    for (colIndex = 0; colIndex < colCount; colIndex++)
    {
        int colSpan = 1;
        int rowSpan = 1;

        if (colIndex == 1 && rowIndex == 1)
        {
            colSpan = 2;
            rowSpan = 2;
        }
        else if (colIndex == 2 && (rowIndex == 1 || rowIndex == 2))
        {
            continue;
        }
        else if (rowIndex == 2 && (colIndex == 1 || colIndex == 2))
        {
            continue;
        }

        TableTDElement tdElement = trElement.createTD();
        tdElement.setText(String.format("Ячейка [%s, %s]", rowIndex, colIndex));


        tdElement.setBackgroundColor(Color.getYellow());
        tdElement.setBorder(new BorderInfo(BorderSide.All, 4.0F, Color.getGray()));


        tdElement.setMargin(new MarginInfo(8.0, 2.0, 8.0, 2.0));

        tdElement.setAlignment(HorizontalAlignment.Center);

        TextState cellTextState = new TextState();
        cellTextState.setForegroundColor(Color.getDarkBlue());
        cellTextState.setFontSize(7.5F);
        cellTextState.setFontStyle(FontStyles.Bold);
        cellTextState.setFont(FontRepository.findFont("Arial"));
        tdElement.setDefaultCellTextState(cellTextState);

        tdElement.isWordWrapped();
        tdElement.setVerticalAlignment(VerticalAlignment.Center);

        tdElement.setColSpan(colSpan);
        tdElement.setRowSpan(rowSpan);
    }
}

TableTRElement footTrElement = tableTFootElement.createTR();
footTrElement.setAlternativeText("Строка нижнего колонтитула");

footTrElement.setBackgroundColor(Color.getLightSeaGreen());

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTDElement tdElement = footTrElement.createTD();
    tdElement.setText(String.format("Нижний колонтитул %s", colIndex));

    tdElement.setAlignment(HorizontalAlignment.Center);
    tdElement.getStructureTextState().setFontSize(7F);
    tdElement.getStructureTextState().setFontStyle(FontStyles.Bold);
}

StructureAttributes tableAttributes = tableElement.getAttributes().getAttributes(AttributeOwnerStandard.Table);
StructureAttribute summaryAttribute = new StructureAttribute(AttributeKey.Summary);
summaryAttribute.setStringValue("Резюме для таблицы");
tableAttributes.setAttribute(summaryAttribute);

// Сохранить документ Tagged PDF
document.save(path + "CreateTableElement.pdf");
```

## Стиль элемента таблицы

Aspose.PDF для Java позволяет стилизовать таблицу в документе Tagged PDF. Чтобы стилизовать таблицу, вы можете создать таблицу, используя метод [createTableElement()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent#createTableElement--) интерфейса [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). и задать стиль таблицы, используя свойства класса [TableElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableElement). Ниже приведен список свойств, которые вы можете использовать для стилизации таблицы:

- BackgroundColor
- Border
- Alignment
- CornerStyle
- Broken
- ColumnAdjustment
- ColumnWidths
- DefaultCellBorder
- DefaultCellPadding
- DefaultCellTextState
- DefaultColumnWidth
- IsBroken
- IsBordersIncluded
- Left
- Top

Следующий фрагмент кода показывает, как стилизовать таблицу в документе Tagged PDF:

```java
// Для полноценных примеров и файлов данных, пожалуйста, посетите https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Путь к директории с документами.
String path = Utils.getDataDir() + "TaggedPDFs\\";

// Создаем документ
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("Пример стиля таблицы");
taggedContent.setLanguage("en-US");

// Получаем корневой элемент структуры
StructureElement rootElement = taggedContent.getRootElement();

// Создаем элемент структуры таблицы
TableElement tableElement = taggedContent.createTableElement();
rootElement.appendChild(tableElement);

tableElement.setBackgroundColor(Color.getBeige());
tableElement.setBorder(new BorderInfo(BorderSide.All, 0.80F, Color.getGray()));
tableElement.setAlignment(HorizontalAlignment.Center);
tableElement.setBroken(TableBroken.Vertical);
tableElement.setColumnAdjustment(ColumnAdjustment.AutoFitToWindow);
tableElement.setColumnWidths("80 80 80 80 80");
tableElement.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.50F, Color.getDarkBlue()));
tableElement.setDefaultCellPadding(new MarginInfo(16.0, 2.0, 8.0, 2.0));
tableElement.getDefaultCellTextState().setForegroundColor(Color.getDarkCyan());
tableElement.getDefaultCellTextState().setFontSize(8F);
tableElement.setDefaultColumnWidth("70");

tableElement.setBroken(false);
tableElement.setBordersIncluded(true);

tableElement.setLeft(0F);
tableElement.setTop(40F);

tableElement.setRepeatingColumnsCount(2);
tableElement.setRepeatingRowsCount(3);
TextState rowStyle = new TextState();
rowStyle.setBackgroundColor(Color.getLightCoral());
tableElement.setRepeatingRowsStyle(rowStyle);

TableTHeadElement tableTHeadElement = tableElement.createTHead();
TableTBodyElement tableTBodyElement = tableElement.createTBody();
TableTFootElement tableTFootElement = tableElement.createTFoot();
int rowCount = 10;
int colCount = 5;
int rowIndex;
int colIndex;

TableTRElement headTrElement = tableTHeadElement.createTR();
headTrElement.setAlternativeText("Head Row");

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTHElement thElement = headTrElement.createTH();
    thElement.setText(String.format("Head %s", colIndex));
}

for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
{
    TableTRElement trElement = tableTBodyElement.createTR();
    trElement.setAlternativeText(String.format("Row %s", rowIndex));

    for (colIndex = 0; colIndex < colCount; colIndex++)
    {
        TableTDElement tdElement = trElement.createTD();
        tdElement.setText(String.format("Cell [%s, %s]", rowIndex, colIndex));
    }
}

TableTRElement footTrElement = tableTFootElement.createTR();
footTrElement.setAlternativeText("Foot Row");

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTDElement tdElement = footTrElement.createTD();
    tdElement.setText(String.format("Foot %s", colIndex));
}

// Сохраняем документ Tagged Pdf
document.save(path + "StyleTableElement.pdf");
```


## Стиль строки таблицы

Aspose.PDF для Java позволяет стилизовать строку таблицы в документе Tagged PDF. Для того чтобы стилизовать строку таблицы, вы можете использовать свойства класса [TableTRElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableTRElement). Ниже приведен список свойств, которые вы можете использовать для стилизации строки таблицы:

- BackgroundColor
- Border
- DefaultCellBorder
- MinRowHeight
- FixedRowHeight
- IsInNewPage
- IsRowBroken
- DefaultCellTextState
- DefaultCellPadding
- VerticalAlignment

Следующий фрагмент кода показывает, как стилизовать строку таблицы в документе Tagged PDF:

```java
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Путь к каталогу документов.
String path = Utils.getDataDir() + "TaggedPDFs\\";

// Создать документ
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("Пример стиля строки таблицы");
taggedContent.setLanguage("en-US");

// Получить корневой элемент структуры
StructureElement rootElement = taggedContent.getRootElement();


// Создать элемент структуры таблицы
TableElement tableElement = taggedContent.createTableElement();
rootElement.appendChild(tableElement);


TableTHeadElement tableTHeadElement = tableElement.createTHead();
TableTBodyElement tableTBodyElement = tableElement.createTBody();
TableTFootElement tableTFootElement = tableElement.createTFoot();
int rowCount = 7;
int colCount = 3;
int rowIndex;
int colIndex;

TableTRElement headTrElement = tableTHeadElement.createTR();
headTrElement.setAlternativeText("Заголовок строки");

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTHElement thElement = headTrElement.createTH();
    thElement.setText(String.format("Заголовок %s", colIndex));
}

for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
{
    TableTRElement trElement = tableTBodyElement.createTR();
    trElement.setAlternativeText(String.format("Строка %s", rowIndex));

    trElement.setBackgroundColor(Color.getLightSeaGreen());
    trElement.setBorder(new BorderInfo(BorderSide.All, 0.75F, Color.getDarkGray()));

    trElement.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.50F, Color.getBlue()));
    trElement.setMinRowHeight(100.0);
    trElement.setFixedRowHeight(120.0);
    trElement.setRowBroken(true);

    TextState cellTextState = new TextState();
    cellTextState.setForegroundColor(Color.getRed());
    trElement.setDefaultCellTextState(cellTextState);

    trElement.setDefaultCellPadding(new MarginInfo(16.0, 2.0, 8.0, 2.0));
    trElement.setVerticalAlignment(VerticalAlignment.Bottom);

    for (colIndex = 0; colIndex < colCount; colIndex++)
    {
        TableTDElement tdElement = trElement.createTD();
        tdElement.setText(String.format("Ячейка [{0}, {1}]", rowIndex, colIndex));
    }
}

TableTRElement footTrElement = tableTFootElement.createTR();
footTrElement.setAlternativeText("Подвал строки");

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTDElement tdElement = footTrElement.createTD();
    tdElement.setText(String.format("Подвал %s", colIndex));
}



// Сохранить документ Tagged Pdf
document.save(path + "StyleTableRow.pdf");
```


## Стиль Ячейки Таблицы

Aspose.PDF для Java позволяет стилизовать ячейку таблицы в документе Tagged PDF. Для того чтобы стилизовать ячейку таблицы, вы можете использовать свойства класса [TableCellElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableCellElement). Ниже приведен список свойств, которые вы можете использовать для стилизации ячейки таблицы:

- BackgroundColor
- Border
- IsNoBorder
- Margin
- Alignment
- DefaultCellTextState
- IsWordWrapped
- VerticalAlignment
- ColSpan
- RowSpan

Следующий фрагмент кода показывает, как стилизовать ячейку таблицы в документе Tagged PDF. Вы также можете проверить соответствие созданного документа стандарту **PDF/UA**. Фрагмент кода ниже показывает, как использовать эту функциональность.

```java
// Для получения полных примеров и файлов данных, пожалуйста, посетите https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Путь к директории документов.
String path = Utils.getDataDir() + "TaggedPDFs\\";

// Создать документ
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("Пример стиля ячейки таблицы");
taggedContent.setLanguage("en-US");

// Получить корневой элемент структуры
StructureElement rootElement = taggedContent.getRootElement();

// Создать элемент структуры таблицы
TableElement tableElement = taggedContent.createTableElement();
rootElement.appendChild(tableElement);

TableTHeadElement tableTHeadElement = tableElement.createTHead();
TableTBodyElement tableTBodyElement = tableElement.createTBody();
TableTFootElement tableTFootElement = tableElement.createTFoot();
int rowCount = 4;
int colCount = 4;
int rowIndex;
int colIndex;

TableTRElement headTrElement = tableTHeadElement.createTR();
headTrElement.setAlternativeText("Заголовочная строка");

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTHElement thElement = headTrElement.createTH();
    thElement.setText(String.format("Заголовок %s", colIndex));

    thElement.setBackgroundColor(Color.getGreenYellow());
    thElement.setBorder(new BorderInfo(BorderSide.All, 4.0F, Color.getGray()));

    thElement.setNoBorder(false);
    thElement.setMargin(new MarginInfo(16.0, 2.0, 8.0, 2.0));

    thElement.setAlignment(HorizontalAlignment.Right);
}

for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
{
    TableTRElement trElement = tableTBodyElement.createTR();
    trElement.setAlternativeText(String.format("Строка %s", rowIndex));

    for (colIndex = 0; colIndex < colCount; colIndex++)
    {
        int colSpan = 1;
        int rowSpan = 1;

        if (colIndex == 1 && rowIndex == 1)
        {
            colSpan = 2;
            rowSpan = 2;
        }
        else if (colIndex == 2 && (rowIndex == 1 || rowIndex == 2))
        {
            continue;
        }
        else if (rowIndex == 2 && (colIndex == 1 || colIndex == 2))
        {
            continue;
        }

        TableTDElement tdElement = trElement.createTD();
        tdElement.setText(String.format("Ячейка [%s, %s]", rowIndex, colIndex));

        tdElement.setBackgroundColor(Color.getYellow());
        tdElement.setBorder(new BorderInfo(BorderSide.All, 4.0F, Color.getGray()));

        tdElement.setNoBorder(false);
        tdElement.setMargin(new MarginInfo(8.0, 2.0, 8.0, 2.0));

        tdElement.setAlignment(HorizontalAlignment.Center);

        TextState cellTextState = new TextState();
        cellTextState.setForegroundColor(Color.getDarkBlue());
        cellTextState.setFontSize(7.5F);
        cellTextState.setFontStyle(FontStyles.Bold);
        cellTextState.setFont(FontRepository.findFont("Arial"));
        tdElement.setDefaultCellTextState(cellTextState);

        tdElement.setWordWrapped(false);
        tdElement.setVerticalAlignment(VerticalAlignment.Center);

        tdElement.setColSpan(colSpan);
        tdElement.setRowSpan(rowSpan);
    }
}

TableTRElement footTrElement = tableTFootElement.createTR();
footTrElement.setAlternativeText("Подвальная строка");

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTDElement tdElement = footTrElement.createTD();
    tdElement.setText(String.format("Подвал %s", colIndex));
}

// Сохранить документ Tagged Pdf
document.save(path + "StyleTableCell.pdf");
```