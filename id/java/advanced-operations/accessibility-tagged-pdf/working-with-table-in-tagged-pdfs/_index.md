---
title: Bekerja dengan Tabel dalam PDF Berlabel
linktitle: Bekerja dengan Tabel dalam PDF Berlabel
type: docs
weight: 40
url: id/java/working-with-table-in-tagged-pdfs/
description: Artikel ini menjelaskan cara bekerja dengan tabel dalam dokumen PDF Berlabel menggunakan Aspose.PDF untuk Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Fitur ini didukung oleh versi 19.6 atau lebih baru.

{{% /alert %}}

## Membuat Tabel dalam PDF Berlabel

Aspose.PDF untuk Java memungkinkan pembuatan tabel dalam dokumen PDF Berlabel.
 For bekerja dengan tabel, API menyediakan kelas [TableElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableElement). In order to create a table, you can use [createTableElement()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent#createTableElement--) method of [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent) interface.

Untuk membuat tabel, Anda dapat menggunakan metode [createTableElement()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent#createTableElement--) dari antarmuka [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). Lebih lanjut, Anda dapat menggunakan metode [createTHead()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableElement#createTHead--), [createTBody()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableElement#createTBody--), dan [createTFoot()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableElement#createTFoot--) dari kelas TableElement untuk membuat Table Head, Table Body, dan Table Foot masing-masing. Untuk membuat baris tabel, Anda dapat menggunakan metode [createTR()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableRowCollectionElement#createTR--) dari kelas [TableRowCollectionElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableRowCollectionElement). Cuplikan kode berikut menunjukkan cara membuat tabel dalam dokumen PDF Berlabel:

```java
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Jalur ke direktori dokumen.
String path = Utils.getDataDir() + "TaggedPDFs\\";

// Buat dokumen
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("Contoh tabel");
taggedContent.setLanguage("en-US");

// Dapatkan elemen struktur akar
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
headTrElement.setAlternativeText("Baris Kepala");

headTrElement.setBackgroundColor(Color.getLightGray());

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTHElement thElement = headTrElement.createTH();
    thElement.setText(String.format("Kepala %s", colIndex));

    thElement.setBackgroundColor(Color.getGreenYellow());
    thElement.setBorder(new BorderInfo(BorderSide.All, 4.0F, Color.getLightGray()));

    thElement.setMargin(new MarginInfo(16.0, 2.0, 8.0, 2.0));

    thElement.setAlignment(HorizontalAlignment.Right);
}

for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
{
    TableTRElement trElement = tableTBodyElement.createTR();
    trElement.setAlternativeText(String.format("Baris %s", rowIndex));

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
        tdElement.setText(String.format("Sel [%s, %s]", rowIndex, colIndex));

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
footTrElement.setAlternativeText("Baris Kaki");

footTrElement.setBackgroundColor(Color.getLightSeaGreen());

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTDElement tdElement = footTrElement.createTD();
    tdElement.setText(String.format("Kaki %s", colIndex));

    tdElement.setAlignment(HorizontalAlignment.Center);
    tdElement.getStructureTextState().setFontSize(7F);
    tdElement.getStructureTextState().setFontStyle(FontStyles.Bold);
}

StructureAttributes tableAttributes = tableElement.getAttributes().getAttributes(AttributeOwnerStandard.Table);
StructureAttribute summaryAttribute = new StructureAttribute(AttributeKey.Summary);
summaryAttribute.setStringValue("Teks ringkasan untuk tabel");
tableAttributes.setAttribute(summaryAttribute);

// Simpan Dokumen Pdf Berlabel
document.save(path + "CreateTableElement.pdf");
```

## Elemen Tabel Gaya

Aspose.PDF untuk Java memungkinkan penataan tabel dalam dokumen PDF Berpenanda. Untuk menata tabel, Anda dapat membuat tabel menggunakan metode [createTableElement()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent#createTableElement--) dari antarmuka [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). dan mengatur gaya tabel menggunakan properti kelas [TableElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableElement). Berikut adalah daftar properti yang dapat Anda gunakan untuk menata tabel:

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

Cuplikan kode berikut menunjukkan cara menata tabel dalam dokumen PDF Berpenanda:

```java
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Jalur ke direktori dokumen.
String path = Utils.getDataDir() + "TaggedPDFs\\";

// Buat dokumen
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("Contoh gaya tabel");
taggedContent.setLanguage("en-US");

// Dapatkan elemen struktur akar
StructureElement rootElement = taggedContent.getRootElement();


// Buat elemen struktur tabel
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
headTrElement.setAlternativeText("Baris Kepala");

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTHElement thElement = headTrElement.createTH();
    thElement.setText(String.format("Kepala %s", colIndex));
}

for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
{
    TableTRElement trElement = tableTBodyElement.createTR();
    trElement.setAlternativeText(String.format("Baris %s", rowIndex));

    for (colIndex = 0; colIndex < colCount; colIndex++)
    {
        TableTDElement tdElement = trElement.createTD();
        tdElement.setText(String.format("Sel [%s, %s]", rowIndex, colIndex));
    }
}

TableTRElement footTrElement = tableTFootElement.createTR();
footTrElement.setAlternativeText("Baris Kaki");

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTDElement tdElement = footTrElement.createTD();
    tdElement.setText(String.format("Kaki %s", colIndex));
}

// Simpan Dokumen Pdf Berpenanda
document.save(path + "StyleTableElement.pdf");
```


## Gaya Baris Tabel

Aspose.PDF untuk Java memungkinkan pengaturan gaya baris tabel dalam dokumen PDF Berlabel. Untuk mengatur gaya baris tabel, Anda dapat menggunakan properti dari kelas [TableTRElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableTRElement). Berikut adalah daftar properti yang dapat Anda gunakan untuk mengatur gaya baris tabel:

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

Cuplikan kode berikut menunjukkan cara mengatur gaya baris tabel dalam dokumen PDF Berlabel:

```java
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Jalur ke direktori dokumen.
String path = Utils.getDataDir() + "TaggedPDFs\\";

// Buat dokumen
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("Contoh gaya baris tabel");
taggedContent.setLanguage("en-US");

// Dapatkan elemen struktur root
StructureElement rootElement = taggedContent.getRootElement();

// Buat elemen struktur tabel
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
headTrElement.setAlternativeText("Baris Kepala");

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTHElement thElement = headTrElement.createTH();
    thElement.setText(String.format("Kepala %s", colIndex));
}

for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
{
    TableTRElement trElement = tableTBodyElement.createTR();
    trElement.setAlternativeText(String.format("Baris %s", rowIndex));

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
        tdElement.setText(String.format("Sel [{0}, {1}]", rowIndex, colIndex));
    }
}

TableTRElement footTrElement = tableTFootElement.createTR();
footTrElement.setAlternativeText("Baris Kaki");

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTDElement tdElement = footTrElement.createTD();
    tdElement.setText(String.format("Kaki %s", colIndex));
}

// Simpan Dokumen Pdf Berlabel
document.save(path + "StyleTableRow.pdf");
```


## Gaya Sel Tabel

Aspose.PDF untuk Java memungkinkan penggayaan sel tabel dalam dokumen PDF Ter-Tag. Untuk menggaya sel tabel, Anda dapat menggunakan properti dari kelas [TableCellElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableCellElement). Berikut adalah daftar properti yang dapat Anda gunakan untuk menggaya sel tabel:

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

Cuplikan kode berikut menunjukkan cara menggaya sel tabel dalam dokumen PDF Ter-Tag. Anda juga dapat memverifikasi kepatuhan **PDF/UA** dari dokumen yang dibuat. Cuplikan kode di bawah ini menunjukkan cara menggunakan fungsionalitas ini.

```java
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Jalur ke direktori dokumen.
String path = Utils.getDataDir() + "TaggedPDFs\\";

// Buat dokumen
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("Contoh gaya sel tabel");
taggedContent.setLanguage("en-US");

// Dapatkan elemen struktur root
StructureElement rootElement = taggedContent.getRootElement();

// Buat elemen struktur tabel
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
headTrElement.setAlternativeText("Baris Kepala");

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTHElement thElement = headTrElement.createTH();
    thElement.setText(String.format("Kepala %s", colIndex));

    thElement.setBackgroundColor(Color.getGreenYellow());
    thElement.setBorder(new BorderInfo(BorderSide.All, 4.0F, Color.getGray()));

    thElement.setNoBorder(false);
    thElement.setMargin(new MarginInfo(16.0, 2.0, 8.0, 2.0));

    thElement.setAlignment(HorizontalAlignment.Right);
}

for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
{
    TableTRElement trElement = tableTBodyElement.createTR();
    trElement.setAlternativeText(String.format("Baris %s", rowIndex));

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
        tdElement.setText(String.format("Sel [%s, %s]", rowIndex, colIndex));

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
footTrElement.setAlternativeText("Baris Kaki");

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTDElement tdElement = footTrElement.createTD();
    tdElement.setText(String.format("Kaki %s", colIndex));
}

// Simpan Dokumen Pdf Ter-Tag
document.save(path + "StyleTableCell.pdf");
```