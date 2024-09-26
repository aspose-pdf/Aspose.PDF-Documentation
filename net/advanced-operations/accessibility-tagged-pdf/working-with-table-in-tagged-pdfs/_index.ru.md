---
title: Работа с таблицей в тегированных PDF
linktitle: Работа с таблицей в тегированных PDF
type: docs
weight: 40
url: /net/working-with-table-in-tagged-pdfs/
description: Эта статья объясняет, как работать с таблицами в тегированных PDF документах с помощью Aspose.PDF для .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Работа с таблицей в тегированных PDF",
    "alternativeHeadline": "Манипулирование таблицами в тегированных PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "таблица, pdf, стилизация элементов таблицы, создание таблицы",
    "wordcount": "302",
    "proficiencyLevel":"Начальный",
    "publisher": {
        "@type": "Organization",
        "name": "Команда документации Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/working-with-table-in-tagged-pdfs/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-table-in-tagged-pdfs/"
    },
    "dateModified": "2022-02-04",
    "description": "Эта статья объясняет, как работать с таблицами в тегированных PDF документах с помощью Aspose.PDF для .NET."
}
</script>

## Создание таблицы в тегированном PDF

Aspose.PDF для .NET позволяет создавать таблицы в тегированных PDF документах.
Aspose.PDF для .NET позволяет создавать таблицы в тегированных PDF документах.

Следующий пример кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

Следующий пример кода показывает, как создать таблицу в тегированном PDF документе:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Создание документа
Document document = new Document();
ITaggedContent taggedContent = document.TaggedContent;

taggedContent.SetTitle("Пример таблицы");
taggedContent.SetLanguage("en-US");

// Получение корневого структурного элемента
StructureElement rootElement = taggedContent.RootElement;


TableElement tableElement = taggedContent.CreateTableElement();
rootElement.AppendChild(tableElement);

tableElement.Border = new BorderInfo(BorderSide.All, 1.2F, Color.DarkBlue);

TableTHeadElement tableTHeadElement = tableElement.CreateTHead();
TableTBodyElement tableTBodyElement = tableElement.CreateTBody();
TableTFootElement tableTFootElement = tableElement.CreateTFoot();
int rowCount = 50;
int colCount = 4;
int rowIndex;
int colIndex;

TableTRElement headTrElement = tableTHeadElement.CreateTR();
headTrElement.AlternativeText = "Заголовочная строка";

headTrElement.BackgroundColor = Color.LightGray;

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTHElement thElement = headTrElement.CreateTH();
    thElement.SetText(String.Format("Заголовок {0}", colIndex));

    thElement.BackgroundColor = Color.GreenYellow;
    thElement.Border = new BorderInfo(BorderSide.All, 4.0F, Color.Gray);

    thElement.IsNoBorder = true;
    thElement.Margin = new MarginInfo(16.0, 2.0, 8.0, 2.0);

    thElement.Alignment = HorizontalAlignment.Right;
}

for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
{
    TableTRElement trElement = tableTBodyElement.CreateTR();
    trElement.AlternativeText = String.Format("Строка {0}", rowIndex);

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

        TableTDElement tdElement = trElement.CreateTD();
        tdElement.SetText(String.Format("Ячейка [{0}, {1}]", rowIndex, colIndex));


        tdElement.BackgroundColor = Color.Yellow;
        tdElement.Border = new BorderInfo(BorderSide.All, 4.0F, Color.Gray);

        tdElement.IsNoBorder = false;
        tdElement.Margin = new MarginInfo(8.0, 2.0, 8.0, 2.0);

        tdElement.Alignment = HorizontalAlignment.Center;

        TextState cellTextState = new TextState();
        cellTextState.ForegroundColor = Color.DarkBlue;
        cellTextState.FontSize = 7.5F;
        cellTextState.FontStyle = FontStyles.Bold;
        cellTextState.Font = FontRepository.FindFont("Arial");
        tdElement.DefaultCellTextState = cellTextState;

        tdElement.IsWordWrapped = true;
        tdElement.VerticalAlignment = VerticalAlignment.Center;

        tdElement.ColSpan = colSpan;
        tdElement.RowSpan = rowSpan;
    }
}

TableTRElement footTrElement = tableTFootElement.CreateTR();
footTrElement.AlternativeText = "Нижняя строка";

footTrElement.BackgroundColor = Color.LightSeaGreen;

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTDElement tdElement = footTrElement.CreateTD();
    tdElement.SetText(String.Format("Ножка {0}", colIndex));

    tdElement.Alignment = HorizontalAlignment.Center;
    tdElement.StructureTextState.FontSize = 7F;
    tdElement.StructureTextState.FontStyle = FontStyles.Bold;
}


StructureAttributes tableAttributes = tableElement.Attributes.GetAttributes(AttributeOwnerStandard.Table);
StructureAttribute summaryAttribute = new StructureAttribute(AttributeKey.Summary);
summaryAttribute.SetStringValue("Сводный текст для таблицы");
tableAttributes.SetAttribute(summaryAttribute);


// Сохранение тегированного PDF документа
document.Save(dataDir + "CreateTableElement.pdf");

// Проверка соответствия PDF/UA
document = new Document(dataDir + "CreateTableElement.pdf");
bool isPdfUaCompliance = document.Validate(dataDir + "table.xml", PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("Соответствие PDF/UA: {0}", isPdfUaCompliance));
```
## Оформление элемента таблицы

Aspose.PDF для .NET позволяет стилизовать таблицу в тегированном PDF-документе. Чтобы стилизовать таблицу, вы можете создать таблицу с помощью метода [CreateTableElement()](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/methods/createtableelement) интерфейса [ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent) и установить стиль таблицы с использованием свойств класса [TableElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement). Ниже приведен список свойств, которые вы можете использовать для стилизации таблицы:

- [BackgroundColor](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/backgroundcolor)
- [Border](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/border)
- [Alignment](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/alignment)
- [CornerStyle](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/cornerstyle)
- [Стиль угла](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/cornerstyle)
- [Разделенный](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/broken)
- [Настройка колонок](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/columnadjustment)
- [Ширины колонок](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/columnwidths)
- [Граница ячейки по умолчанию](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/defaultcellborder)
- [Отступ в ячейке по умолчанию](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/defaultcellpadding)
- [Текстовое состояние ячейки по умолчанию](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/defaultcelltextstate)
- [Ширина колонки по умолчанию](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/defaultcolumnwidth)
- [Разделен ли](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/isbroken)
- [IsBroken](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/isbroken)
- [IsBordersIncluded](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/isbordersincluded)
- [Left](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/left)
- [Top](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/top)

Следующий фрагмент кода показывает, как стилизовать таблицу в документе Tagged PDF:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Создание документа
Document document = new Document();
ITaggedContent taggedContent = document.TaggedContent;

taggedContent.SetTitle("Пример стиля таблицы");
taggedContent.SetLanguage("en-US");

// Получить корневой структурный элемент
StructureElement rootElement = taggedContent.RootElement;

// Создание структурного элемента таблицы
TableElement tableElement = taggedContent.CreateTableElement();
rootElement.AppendChild(tableElement);

tableElement.BackgroundColor = Color.Beige;
tableElement.Border = new BorderInfo(BorderSide.All, 0.80F, Color.Gray);
tableElement.Alignment = HorizontalAlignment.Center;
tableElement.Broken = TableBroken.Vertical;
tableElement.ColumnAdjustment = ColumnAdjustment.AutoFitToWindow;
tableElement.ColumnWidths = "80 80 80 80 80";
tableElement.DefaultCellBorder = new BorderInfo(BorderSide.All, 0.50F, Color.DarkBlue);
tableElement.DefaultCellPadding = new MarginInfo(16.0, 2.0, 8.0, 2.0);
tableElement.DefaultCellTextState.ForegroundColor = Color.DarkCyan;
tableElement.DefaultCellTextState.FontSize = 8F;
tableElement.DefaultColumnWidth = "70";

tableElement.IsBroken = false;
tableElement.IsBordersIncluded = true;

tableElement.Left = 0F;
tableElement.Top = 40F;

tableElement.RepeatingColumnsCount = 2;
tableElement.RepeatingRowsCount = 3;
TextState rowStyle = new TextState();
rowStyle.BackgroundColor = Color.LightCoral;
tableElement.RepeatingRowsStyle = rowStyle;

TableTHeadElement tableTHeadElement = tableElement.CreateTHead();
TableTBodyElement tableTBodyElement = tableElement.CreateTBody();
TableTFootElement tableTFootElement = tableElement.CreateTFoot();
int rowCount = 10;
int colCount = 5;
int rowIndex;
int colIndex;

TableTRElement headTrElement = tableTHeadElement.CreateTR();
headTrElement.AlternativeText = "Заголовочная строка";

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTHElement thElement = headTrElement.CreateTH();
    thElement.SetText(String.Format("Заголовок {0}", colIndex));
}

for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
{
    TableTRElement trElement = tableTBodyElement.CreateTR();
    trElement.AlternativeText = String.Format("Строка {0}", rowIndex);

    for (colIndex = 0; colIndex < colCount; colIndex++)
    {
        TableTDElement tdElement = trElement.CreateTD();
        tdElement.SetText(String.Format("Ячейка [{0}, {1}]", rowIndex, colIndex));
    }
}

TableTRElement footTrElement = tableTFootElement.CreateTR();
footTrElement.AlternativeText = "Нижняя строка";

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTDElement tdElement = footTrElement.CreateTD();
    tdElement.SetText(String.Format("Нижний {0}", colIndex));
}

// Сохранить документ Tagged Pdf
document.Save(dataDir + "StyleTableElement.pdf");

// Проверка соответствия PDF/UA
document = new Document(dataDir + "StyleTableElement.pdf");
bool isPdfUaCompliance = document.Validate(dataDir + "StyleTableElement.xml", PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("Соответствие PDF/UA: {0}", isPdfUaCompliance));
```
## Стилизация строки таблицы

Aspose.PDF для .NET позволяет стилизовать строку таблицы в тегированном PDF-документе. Для стилизации строки таблицы можно использовать свойства класса [TableTRElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tabletrelement). Ниже приведен список свойств, которые можно использовать для стилизации строки таблицы:

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

Следующий фрагмент кода показывает, как стилизовать строку таблицы в тегированном PDF-документе:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Создание документа
Document document = new Document();
ITaggedContent taggedContent = document.TaggedContent;

taggedContent.SetTitle("Пример стиля строки таблицы");
taggedContent.SetLanguage("en-US");

// Получение корневого структурного элемента
StructureElement rootElement = taggedContent.RootElement;

// Создание структурного элемента таблицы
TableElement tableElement = taggedContent.CreateTableElement();
rootElement.AppendChild(tableElement);

TableTHeadElement tableTHeadElement = tableElement.CreateTHead();
TableTBodyElement tableTBodyElement = tableElement.CreateTBody();
TableTFootElement tableTFootElement = tableElement.CreateTFoot();
int rowCount = 7;
int colCount = 3;
int rowIndex;
int colIndex;

TableTRElement headTrElement = tableTHeadElement.CreateTR();
headTrElement.AlternativeText = "Заголовочная строка";

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTHElement thElement = headTrElement.CreateTH();
    thElement.SetText(String.Format("Заголовок {0}", colIndex));
}

for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
{
    TableTRElement trElement = tableTBodyElement.CreateTR();
    trElement.AlternativeText = String.Format("Строка {0}", rowIndex);

    trElement.BackgroundColor = Color.LightGoldenrodYellow;
    trElement.Border = new BorderInfo(BorderSide.All, 0.75F, Color.DarkGray);

    trElement.DefaultCellBorder = new BorderInfo(BorderSide.All, 0.50F, Color.Blue);
    trElement.MinRowHeight = 100.0;
    trElement.FixedRowHeight = 120.0;
    trElement.IsInNewPage = (rowIndex % 3 == 1);
    trElement.IsRowBroken = true;

    TextState cellTextState = new TextState();
    cellTextState.ForegroundColor = Color.Red;
    trElement.DefaultCellTextState = cellTextState;

    trElement.DefaultCellPadding = new MarginInfo(16.0, 2.0, 8.0, 2.0);
    trElement.VerticalAlignment = VerticalAlignment.Bottom;

    for (colIndex = 0; colIndex < colCount; colIndex++)
    {
        TableTDElement tdElement = trElement.CreateTD();
        tdElement.SetText(String.Format("Ячейка [{0}, {1}]", rowIndex, colIndex));
    }
}

TableTRElement footTrElement = tableTFootElement.CreateTR();
footTrElement.AlternativeText = "Нижняя строка";

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTDElement tdElement = footTrElement.CreateTD();
    tdElement.SetText(String.Format("Низ {0}", colIndex));
}

// Сохранение тегированного PDF-документа
document.Save(dataDir + "StyleTableRow.pdf");

// Проверка соответствия PDF/UA
document = new Document(dataDir + "StyleTableRow.pdf");
bool isPdfUaCompliance = document.Validate(dataDir + "StyleTableRow.xml", PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("Соответствие PDF/UA: {0}", isPdfUaCompliance));
```
## Стилизация ячейки таблицы

Aspose.PDF для .NET позволяет стилизовать ячейку таблицы в тегированном PDF документе. Для стилизации ячейки таблицы можно использовать свойства класса [TableCellElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement). Ниже приведен список свойств, которые можно использовать для стилизации ячейки таблицы:

- [BackgroundColor](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/backgroundcolor)
- [Border](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/border)
- [IsNoBorder](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/isnoborder)
- [Margin](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/margin)
- [Alignment](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/alignment)
- [DefaultCellTextState](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/defaultcelltextstate)
- [DefaultCellTextState](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/defaultcelltextstate)
- [IsWordWrapped](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/iswordwrapped)
- [VerticalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/verticalalignment)
- [ColSpan](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/colspan)
- [RowSpan](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/rowspan)

Следующий фрагмент кода показывает, как оформить ячейку таблицы в документе Tagged PDF:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Создание документа
Document document = new Document();
ITaggedContent taggedContent = document.TaggedContent;

taggedContent.SetTitle("Пример стиля ячейки таблицы");
taggedContent.SetLanguage("en-US");

// Получить корневой структурный элемент
StructureElement rootElement = taggedContent.RootElement;

// Создать структурный элемент таблицы
TableElement tableElement = taggedContent.CreateTableElement();
rootElement.AppendChild(tableElement);

TableTHeadElement tableTHeadElement = tableElement.CreateTHead();
TableTBodyElement tableTBodyElement = tableElement.CreateTBody();
TableTFootElement tableTFootElement = tableElement.CreateTFoot();
int rowCount = 4;
int colCount = 4;
int rowIndex;
int colIndex;

TableTRElement headTrElement = tableTHeadElement.CreateTR();
headTrElement.AlternativeText = "Заголовочная строка";

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTHElement thElement = headTrElement.CreateTH();
    thElement.SetText(String.Format("Заголовок {0}", colIndex));

    thElement.BackgroundColor = Color.GreenYellow;
    thElement.Border = new BorderInfo(BorderSide.All, 4.0F, Color.Gray);

    thElement.IsNoBorder = true;
    thElement.Margin = new MarginInfo(16.0, 2.0, 8.0, 2.0);

    thElement.Alignment = HorizontalAlignment.Right;
}

for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
{
    TableTRElement trElement = tableTBodyElement.CreateTR();
    trElement.AlternativeText = String.Format("Строка {0}", rowIndex);

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

        TableTDElement tdElement = trElement.CreateTD();
        tdElement.SetText(String.Format("Ячейка [{0}, {1}]", rowIndex, colIndex));

        tdElement.BackgroundColor = Color.Yellow;
        tdElement.Border = new BorderInfo(BorderSide.All, 4.0F, Color.Gray);

        tdElement.IsNoBorder = false;
        tdElement.Margin = new MarginInfo(8.0, 2.0, 8.0, 2.0);

        tdElement.Alignment = HorizontalAlignment.Center;

        TextState cellTextState = new TextState();
        cellTextState.ForegroundColor = Color.DarkBlue;
        cellTextState.FontSize = 7.5F;
        cellTextState.FontStyle = FontStyles.Bold;
        cellTextState.Font = FontRepository.FindFont("Arial");
        tdElement.DefaultCellTextState = cellTextState;

        tdElement.IsWordWrapped = true;
        tdElement.VerticalAlignment = VerticalAlignment.Center;

        tdElement.ColSpan = colSpan;
        tdElement.RowSpan = rowSpan;
    }
}

TableTRElement footTrElement = tableTFootElement.CreateTR();
footTrElement.AlternativeText = "Заключительная строка";

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTDElement tdElement = footTrElement.CreateTD();
    tdElement.SetText(String.Format("Нижняя часть {0}", colIndex));
}

// Сохранить документ Tagged Pdf
document.Save(dataDir + "StyleTableCell.pdf");

// Проверка соответствия PDF/UA
document = new Document(dataDir + "StyleTableCell.pdf");
bool isPdfUaCompliance = document.Validate(dataDir + "StyleTableCell.xml", PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("Соответствие PDF/UA: {0}", isPdfUaCompliance));
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF для библиотеки .NET",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "продажи",
                "areaServed": "США",
                "availableLanguage": "английский"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "Великобритания",
                "availableLanguage": "английский"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "Австралия",
                "availableLanguage": "английский"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Библиотека для манипуляции PDF для .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```

