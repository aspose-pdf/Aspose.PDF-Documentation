---
title: Создание или Добавление Таблицы в PDF с использованием C#
linktitle: Создание или Добавление Таблицы
type: docs
weight: 10
url: /ru/net/add-table-in-existing-pdf-document/
description: Aspose.PDF для .NET - это библиотека, используемая для создания, чтения и редактирования таблиц PDF. Ознакомьтесь с другими расширенными функциями в этой теме.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/add-and-extract-a-table/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Создание или Добавление Таблицы в PDF с использованием C#",
    "alternativeHeadline": "Как добавить таблицу в PDF с помощью .NET",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, создание таблицы в pdf, добавление таблицы",
    "wordcount": "302",
    "proficiencyLevel":"Начинающий",
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
                "contactType": "продажи",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/add-table-in-existing-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-table-in-existing-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF для .NET - это библиотека, используемая для создания, чтения и редактирования таблиц PDF. Ознакомьтесь с другими расширенными функциями в этой теме."
}
</script>
## Создание таблицы с использованием C\#

Таблицы важны при работе с PDF-документами. Они предоставляют отличные возможности для систематического отображения информации. Пространство имен Aspose.PDF содержит классы с именами [Table](https://reference.aspose.com/pdf/net/aspose.pdf/table), [Cell](https://reference.aspose.com/pdf/net/aspose.pdf/cell), и [Row](https://reference.aspose.com/pdf/net/aspose.pdf/row), которые предоставляют функционал для создания таблиц при генерации PDF-документов с нуля.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

Таблица может быть создана путем создания объекта класса Table.

```csharp
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
```

### Добавление таблицы в существующий PDF-документ

Чтобы добавить таблицу в существующий PDF-файл с Aspose.PDF для .NET, выполните следующие шаги:

1. Загрузите исходный файл.
1. Инициализируйте таблицу и установите ее колонки и строки.
1. Установите настройки таблицы (мы установили границы).
1. Заполните таблицу.
1. Добавьте таблицу на страницу.
1.
Следующие фрагменты кода показывают, как добавить текст в существующий PDF-файл.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Загрузка исходного PDF документа
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir+ "AddTable.pdf");
// Инициализация нового экземпляра таблицы
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
// Установка цвета границы таблицы как светло-серый
table.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// Установка границ для ячеек таблицы
table.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// Создание цикла для добавления 10 строк
for (int row_count = 1; row_count < 10; row_count++)
{
    // Добавление строки в таблицу
    Aspose.Pdf.Row row = table.Rows.Add();
    // Добавление ячеек в таблицу
    row.Cells.Add("Колонка (" + row_count + ", 1)");
    row.Cells.Add("Колонка (" + row_count + ", 2)");
    row.Cells.Add("Колонка (" + row_count + ", 3)");
}
// Добавление объекта таблицы на первую страницу входного документа
doc.Pages[1].Paragraphs.Add(table);
dataDir = dataDir + "document_with_table_out.pdf";
// Сохранение обновленного документа, содержащего объект таблицы
doc.Save(dataDir);
```
### Объединение столбцов и строк в таблицах

Aspose.PDF для .NET предоставляет свойство [ColSpan](https://reference.aspose.com/pdf/net/aspose.pdf/cell/properties/colspan), чтобы объединить столбцы в таблице, и свойство [RowSpan](https://reference.aspose.com/pdf/net/aspose.pdf/cell/properties/rowspan), чтобы объединить строки.

Мы используем свойство `ColSpan` или `RowSpan` для объекта `Cell`, который создает ячейку таблицы. После применения необходимых свойств созданная ячейка может быть добавлена в таблицу.

```csharp
public static void AddTable_RowColSpan()
{
    // Загрузить исходный PDF документ
    Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document();
    pdfDocument.Pages.Add();

    // Инициализирует новый экземпляр таблицы
    Aspose.Pdf.Table table = new Aspose.Pdf.Table
    {
        // Установить цвет границы таблицы как LightGray
        Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Color.Black),
        // Установить границы для ячеек таблицы
        DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Color.Black)
    };

    // Добавить первую строку в таблицу
    Aspose.Pdf.Row row1 = table.Rows.Add();
    for (int cellCount = 1; cellCount <5; cellCount++)
    {
        // Добавить ячейки таблицы
        row1.Cells.Add($"Test 1 {cellCount}");
    }

    // Добавить вторую строку в таблицу
    Aspose.Pdf.Row row2 = table.Rows.Add();
    row2.Cells.Add($"Test 2 1");
    var cell = row2.Cells.Add($"Test 2 2");
    cell.ColSpan = 2;
    row2.Cells.Add($"Test 2 4");

    // Добавить третью строку в таблицу
    Aspose.Pdf.Row row3 = table.Rows.Add();
    row3.Cells.Add("Test 3 1");
    row3.Cells.Add("Test 3 2");
    row3.Cells.Add("Test 3 3");
    row3.Cells.Add("Test 3 4");

    // Добавить четвертую строку в таблицу
    Aspose.Pdf.Row row4 = table.Rows.Add();
    row4.Cells.Add("Test 4 1");
    cell = row4.Cells.Add("Test 4 2");
    cell.RowSpan = 2;
    row4.Cells.Add("Test 4 3");
    row4.Cells.Add("Test 4 4");

    // Добавить пятую строку в таблицу
    row4 = table.Rows.Add();
    row4.Cells.Add("Test 5 1");
    row4.Cells.Add("Test 5 3");
    row4.Cells.Add("Test 5 4");

    // Добавить объект таблицы на первую страницу входного документа
    pdfDocument.Pages[1].Paragraphs.Add(table);

    // Сохранить обновленный документ, содержащий объект таблицы
    doc.Save(Path.Combine(_dataDir, "document_with_table_out.pdf"));
}
```
Результат выполнения кода ниже представляет собой таблицу, изображенную на следующем рисунке:

![ColSpan and RowSpan demo](colspan_rowspan.png)

## Работа с границами, отступами и полями

Обратите внимание, что также поддерживается функция установки стиля границ, отступов и внутренних отступов ячеек таблицы. Прежде чем переходить к более техническим деталям, важно понять концепции границ, отступов и внутренних отступов, которые представлены ниже на диаграмме:

![Borders, margins and padding](set-border-style-margins-and-padding-of-table_1.png)

На приведенной выше рисунке вы можете видеть, что границы таблицы, строки и ячейки перекрываются. Используя Aspose.PDF, таблица может иметь отступы, а ячейки могут иметь внутренние отступы. Для установки отступов ячеек необходимо установить внутренние отступы.

### Границы

Для установки границ объектов [Table](https://reference.aspose.com/pdf/net/aspose.pdf/table), [Row](https://reference.aspose.com/pdf/net/aspose.pdf/row) и [Cell](https://reference.aspose.com/pdf/net/aspose.pdf/cell) используйте свойства Table.Border, Row.Border и Cell.Border.
Чтобы установить границы для объектов Table, [Row](https://reference.aspose.com/pdf/net/aspose.pdf/row) и [Cell](https://reference.aspose.com/pdf/net/aspose.pdf/cell), используйте свойства Table.Border, Row.Border и Cell.Border.

### Отступы

Управление отступами ячеек можно осуществлять с помощью свойства [DefaultCellPadding](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellpadding) класса Table. Все свойства, связанные с отступами, назначаются экземпляру класса [MarginInfo](https://reference.aspose.com/pdf/net/aspose.pdf/margininfo), который принимает информацию о параметрах `Left`, `Right`, `Top` и `Bottom` для создания пользовательских отступов.

В следующем примере ширина границы ячейки установлена в 0.1 пункт, ширина границы таблицы - 1 пункт, а отступ ячейки - 5 пунктов.

![Отступы и границы в таблице PDF](margin-border.png)

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Создание объекта документа путем вызова его пустого конструктора
Document doc = new Document();
Page page = doc.Pages.Add();
// Создание объекта таблицы
Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();
// Добавление таблицы в коллекцию параграфов нужного раздела
page.Paragraphs.Add(tab1);
// Установка ширин колонок таблицы
tab1.ColumnWidths = "50 50 50";
// Установка границы по умолчанию для ячеек с использованием объекта BorderInfo
tab1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);
// Установка границы таблицы с использованием другого настроенного объекта BorderInfo
tab1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
// Создание объекта MarginInfo и установка его отступов слева, снизу, справа и сверху
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 5f;
margin.Left = 5f;
margin.Right = 5f;
margin.Bottom = 5f;
// Установка отступа по умолчанию для ячеек в объект MarginInfo
tab1.DefaultCellPadding = margin;
// Создание строк в таблице, а затем ячеек в строках
Aspose.Pdf.Row row1 = tab1.Rows.Add();
row1.Cells.Add("col1");
row1.Cells.Add("col2");
row1.Cells.Add();
TextFragment mytext = new TextFragment("col3 с длинной строкой текста");
// row1.Cells.Add("col3 с длинной строкой текста для размещения в ячейке");
row1.Cells[2].Paragraphs.Add(mytext);
row1.Cells[2].IsWordWrapped = false;
// row1.Cells[2].Paragraphs[0].FixedWidth= 80;
Aspose.Pdf.Row row2 = tab1.Rows.Add();
row2.Cells.Add("item1");
row2.Cells.Add("item2");
row2.Cells.Add("item3");
dataDir = dataDir + "MarginsOrPadding_out.pdf";
// Сохранение PDF
doc.Save(dataDir);
```
Чтобы создать таблицу со скругленными углами, используйте значение `RoundedBorderRadius` класса BorderInfo и установите стиль углов таблицы в виде скругления.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();
Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();

GraphInfo graph = new GraphInfo();
graph.Color = Aspose.Pdf.Color.Red;
// Создание пустого объекта BorderInfo
BorderInfo bInfo = new BorderInfo(BorderSide.All, graph);
// Установка границы с закругленным радиусом 15
bInfo.RoundedBorderRadius = 15;
// Установка стиля углов таблицы как скругленные.
tab1.CornerStyle = Aspose.Pdf.BorderCornerStyle.Round;
// Установка информации о границе таблицы
tab1.Border = bInfo;
```

## Применение различных настроек автоматической подгонки к таблице

При создании таблицы с использованием визуального агента, такого как Microsoft Word, вы часто сталкиваетесь с использованием одного из вариантов AutoFit для автоматического размера таблицы до желаемой ширины.
При создании таблицы с помощью визуального агента, такого как Microsoft Word, вы часто будете использовать один из вариантов AutoFit для автоматической настройки размера таблицы до желаемой ширины.

По умолчанию Aspose.Pdf вставляет новую таблицу с использованием `ColumnAdjustment` со значением `Customized`. Таблица будет подстраиваться под доступную ширину на странице. Чтобы изменить поведение размера такой таблицы или существующей таблицы, вы можете вызвать метод Table.autoFit(int). Этот метод принимает перечисление AutoFitBehavior, которое определяет, какой тип автоматической подгонки применяется к таблице.

Как и в Microsoft Word, метод автоподгонки на самом деле является ярлыком, который применяет различные свойства к таблице одновременно. Эти свойства на самом деле определяют наблюдаемое поведение таблицы. Мы обсудим эти свойства для каждой опции автоподгонки. Мы будем использовать следующую таблицу и применять различные настройки автоподгонки в качестве демонстрации:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Создание объекта Pdf путем вызова его пустого конструктора
Document doc = new Document();
// Создание раздела в объекте Pdf
Page sec1 = doc.Pages.Add();

// Создание объекта таблицы
Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();
// Добавление таблицы в коллекцию абзацев желаемого раздела
sec1.Paragraphs.Add(tab1);

// Установка ширины столбцов таблицы
tab1.ColumnWidths = "50 50 50";
tab1.ColumnAdjustment = ColumnAdjustment.AutoFitToWindow;

// Установка стандартной границы ячейки с использованием объекта BorderInfo
tab1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);

// Установка границы таблицы с использованием другого настроенного объекта BorderInfo
tab1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
// Создание объекта MarginInfo и установка его левого, нижнего, правого и верхнего отступов
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 5f;
margin.Left = 5f;
margin.Right = 5f;
margin.Bottom = 5f;

// Установка стандартного отступа ячейки для объекта MarginInfo
tab1.DefaultCellPadding = margin;

// Создание строк в таблице, а затем ячеек в строках
Aspose.Pdf.Row row1 = tab1.Rows.Add();
row1.Cells.Add("col1");
row1.Cells.Add("col2");
row1.Cells.Add("col3");
Aspose.Pdf.Row row2 = tab1.Rows.Add();
row2.Cells.Add("item1");
row2.Cells.Add("item2");
row2.Cells.Add("item3");

dataDir = dataDir + "AutoFitToWindow_out.pdf";
// Сохранение обновленного документа, содержащего объект таблицы
doc.Save(dataDir);
```
### Получить ширину таблицы

Иногда требуется динамически получить ширину таблицы. Класс Aspose.PDF.Table имеет метод [GetWidth](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/getwidth) для этой цели. Например, вы не установили ширину столбцов таблицы явно и установили [ColumnAdjustment](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/columnadjustment) в AutoFitToContent. В этом случае вы можете получить ширину таблицы следующим образом.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Создать новый документ
Document doc = new Document();
// Добавить страницу в документ
Page page = doc.Pages.Add();
// Инициализировать новую таблицу
Table table = new Table
{
    ColumnAdjustment = ColumnAdjustment.AutoFitToContent
};
// Добавить строку в таблицу
Row row = table.Rows.Add();
// Добавить ячейку в таблицу
Cell cell = row.Cells.Add("Текст ячейки 1");
cell = row.Cells.Add("Текст ячейки 2");
// Получить ширину таблицы
Console.WriteLine(table.GetWidth());
```

## Добавить изображение SVG в ячейку таблицы
## Добавление изображения SVG в ячейку таблицы

Aspose.PDF для .NET поддерживает возможность добавления ячейки таблицы в файл PDF. При создании таблицы можно добавлять в ячейки текст или изображения. Кроме того, API также предлагает возможность конвертации файлов SVG в формат PDF. Используя комбинацию этих функций, можно загрузить изображение SVG и добавить его в ячейку таблицы.

Следующий фрагмент кода показывает шаги создания экземпляра таблицы и добавления изображения SVG в ячейку таблицы.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Создание объекта документа
Document doc = new Document();
// Создание экземпляра изображения
Aspose.Pdf.Image img = new Aspose.Pdf.Image();
// Установка типа изображения как SVG
img.FileType = Aspose.Pdf.ImageFileType.Svg;
// Путь к исходному файлу
img.File = dataDir + "SVGToPDF.svg";
// Установка ширины для экземпляра изображения
img.FixWidth = 50;
// Установка высоты для экземпляра изображения
img.FixHeight = 50;
// Создание экземпляра таблицы
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
// Установка ширины для ячеек таблицы
table.ColumnWidths = "100 100";
// Создание объекта строки и добавление его в экземпляр таблицы
Aspose.Pdf.Row row = table.Rows.Add();
// Создание объекта ячейки и добавление его в экземпляр строки
Aspose.Pdf.Cell cell = row.Cells.Add();
// Добавление текстового фрагмента в коллекцию параграфов объекта ячейки
cell.Paragraphs.Add(new TextFragment("Первая ячейка"));
// Добавление другой ячейки в объект строки
cell = row.Cells.Add();
// Добавление изображения SVG в коллекцию параграфов недавно добавленного экземпляра ячейки
cell.Paragraphs.Add(img);
// Создание объекта страницы и добавление его в коллекцию страниц объекта документа
Page page = doc.Pages.Add();
// Добавление таблицы в коллекцию параграфов объекта страницы
page.Paragraphs.Add(table);

dataDir = dataDir + "AddSVGObject_out.pdf";
// Сохранение файла PDF
doc.Save(dataDir);
```
## Использование HTML-тегов внутри таблицы

Иногда может возникнуть потребность импортировать содержимое базы данных, содержащее HTML-теги, а затем импортировать содержимое в объект Table. При импортировании содержимого HTML-теги должны соответствующим образом отображаться в документе PDF. Мы усовершенствовали метод ImprotDataTable(), чтобы достичь такой потребности следующим образом:

{{% alert color="primary" %}}

Пожалуйста, учтите, что использование HTML-тегов внутри элемента таблицы увеличивает время генерации документа, так как API необходимо соответственно обработать HTML-теги и отобразить их в выходном документе PDF.

{{% /alert %}}

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

DataTable dt = new DataTable("Employee");
dt.Columns.Add("data", System.Type.GetType("System.String"));

DataRow dr = dt.NewRow();
dr[0] = "<li>Отделение экстренной медицины: 3400 Spruce Street Ground Silverstein Bldg Philadelphia PA 19104-4206</li>";
dt.Rows.Add(dr);
dr = dt.NewRow();
dr[0] = "<li>Служба наблюдения за медициной Penn: 3400 Spruce Street Ground Floor Donner Philadelphia PA 19104-4206</li>";
dt.Rows.Add(dr);
dr = dt.NewRow();
dr[0] = "<li>UPHS/Presbyterian - Отдел экстренной медицины: 51 N. 39th Street . Philadelphia PA 19104-2640</li>";
dt.Rows.Add(dr);

Document doc = new Document();
doc.Pages.Add();
// Инициализирует новый экземпляр таблицы
Aspose.Pdf.Table tableProvider = new Aspose.Pdf.Table();
// Устанавливает ширину столбцов таблицы
tableProvider.ColumnWidths = "400 50 ";
// Устанавливает цвет границы таблицы в LightGray
tableProvider.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.5F, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// Устанавливает границу для ячеек таблицы
tableProvider.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.5F, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 2.5F;
margin.Left = 2.5F;
margin.Bottom = 1.0F;
tableProvider.DefaultCellPadding = margin;

tableProvider.ImportDataTable(dt, false, 0, 0, 3, 1, true);

doc.Pages[1].Paragraphs.Add(tableProvider);
doc.Save(dataDir + "HTMLInsideTableCell_out.pdf");
```
## Вставка разрыва страницы между строками таблицы

По умолчанию при создании таблицы внутри файла PDF таблица переходит на следующие страницы, когда достигает нижнего поля таблицы. Однако у нас может возникнуть требование принудительно вставить разрыв страницы, когда добавляется определенное количество строк в таблицу. Следующий фрагмент кода показывает шаги для вставки разрыва страницы после добавления 10 строк в таблицу.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Создание экземпляра документа
Document doc = new Document();
// Добавление страницы в коллекцию страниц PDF файла
doc.Pages.Add();
// Создание экземпляра таблицы
Aspose.Pdf.Table tab = new Aspose.Pdf.Table();
// Установка стиля границы для таблицы
tab.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Red);
// Установка стиля границы по умолчанию для таблицы с цветом границы красный
tab.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Red);
// Указание ширины столбцов таблицы
tab.ColumnWidths = "100 100";
// Создание цикла для добавления 200 строк в таблицу
for (int counter = 0; counter <= 200; counter++)
{
    Aspose.Pdf.Row row = new Aspose.Pdf.Row();
    tab.Rows.Add(row);
    Aspose.Pdf.Cell cell1 = new Aspose.Pdf.Cell();
    cell1.Paragraphs.Add(new TextFragment("Ячейка " + counter + ", 0"));
    row.Cells.Add(cell1); Aspose.Pdf.Cell cell2 = new Aspose.Pdf.Cell();
    cell2.Paragraphs.Add(new TextFragment("Ячейка " + counter + ", 1"));
    row.Cells.Add(cell2);
    // При добавлении 10 строк, новая строка рендерится на новой странице
    if (counter % 10 == 0 && counter != 0) row.IsInNewPage = true;
}
// Добавление таблицы в коллекцию абзацев PDF файла
doc.Pages[1].Paragraphs.Add(tab);

dataDir = dataDir + "InsertPageBreak_out.pdf";
// Сохранение PDF документа
doc.Save(dataDir);
```
## Отрисовка таблицы на новой странице

По умолчанию абзацы добавляются в коллекцию Paragraphs объекта Page. Однако возможно отрисовать таблицу на новой странице вместо добавления её сразу после предыдущего объекта абзаца на странице.

### Пример: Как отрисовать таблицу на новой странице используя C#

Для отрисовки таблицы на новой странице используйте свойство [IsInNewPage](https://reference.aspose.com/pdf/net/aspose.pdf/baseparagraph/properties/isinnewpage) в классе BaseParagraph. Следующий код показывает как это сделать.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

Document doc = new Document();
PageInfo pageInfo = doc.PageInfo;
Aspose.Pdf.MarginInfo marginInfo = pageInfo.Margin;

marginInfo.Left = 37;
marginInfo.Right = 37;
marginInfo.Top = 37;
marginInfo.Bottom = 37;

pageInfo.IsLandscape = true;

Aspose.Pdf.Table table = new Aspose.Pdf.Table();
table.ColumnWidths = "50 100";
// Добавлена страница.
Page curPage = doc.Pages.Add();
for (int i = 1; i <= 120; i++)
{
    Aspose.Pdf.Row row = table.Rows.Add();
    row.FixedRowHeight = 15;
    Aspose.Pdf.Cell cell1 = row.Cells.Add();
    cell1.Paragraphs.Add(new TextFragment("Content 1"));
    Aspose.Pdf.Cell cell2 = row.Cells.Add();
    cell2.Paragraphs.Add(new TextFragment("HHHHH"));
}
Aspose.Pdf.Paragraphs paragraphs = curPage.Paragraphs;
paragraphs.Add(table);
/********************************************/
Aspose.Pdf.Table table1 = new Aspose.Pdf.Table();
table.ColumnWidths = "100 100";
for (int i = 1; i <= 10; i++)
{
    Aspose.Pdf.Row row = table1.Rows.Add();
    Aspose.Pdf.Cell cell1 = row.Cells.Add();
    cell1.Paragraphs.Add(new TextFragment("LAAAAAAA"));
    Aspose.Pdf.Cell cell2 = row.Cells.Add();
    cell2.Paragraphs.Add(new TextFragment("LAAGGGGGG"));
}
table1.IsInNewPage = true;
// Я хочу, чтобы таблица 1 была на следующей странице, пожалуйста...
paragraphs.Add(table1);
dataDir = dataDir + "IsNewPageProperty_Test_out.pdf";
doc.Save(dataDir);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Библиотека Aspose.PDF для .NET",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Организация",
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
                "@type": "Контактная точка",
                "telephone": "+1 903 306 1676",
                "contactType": "продажи",
                "areaServed": "США",
                "availableLanguage": "английский"
            },
            {
                "@type": "Контактная точка",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "Великобритания",
                "availableLanguage": "английский"
            },
            {
                "@type": "Контактная точка",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "Австралия",
                "availableLanguage": "английский"
            }
        ]
    },
    "offers": {
        "@type": "Предложение",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Библиотека для манипулирования PDF для .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "Совокупный рейтинг",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```

