---
title: Отображение таблицы из источника данных
linktitle: Отображение таблицы из источника данных
type: docs
weight: 30
url: /ru/net/render-table-from-the-data-source/
description: На этой странице объясняется, как можно отобразить таблицу из источника данных с использованием библиотеки Aspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF позволяет создавать таблицу с DataSource из DataSet, DataTable, массивов и объектов IEnumerable с использованием класса PdfLightTable

Класс [Table](https://reference.aspose.com/pdf/net/aspose.pdf/table) используется для обработки таблиц. Этот класс дает нам возможность создавать таблицы и размещать их в документе, используя [Rows](https://reference.aspose.com/pdf/net/aspose.pdf/rows) и [Cells](https://reference.aspose.com/pdf/net/aspose.pdf/cell). Таким образом, для создания таблицы необходимо добавить нужное количество строк и заполнить их соответствующим количеством ячеек.

Следующий пример создает таблицу размером 4x10.

```csharp
var table = new Table
    {
        // Установить автоматическую ширину столбцов таблицы
        ColumnWidths = "25% 25% 25% 25%",
        // Установить отступы в ячейках
        DefaultCellPadding = new MarginInfo(10, 5, 10, 5), // Left Bottom Right Top
        // Установить цвет рамки таблицы как Зеленый
        Border = new BorderInfo(BorderSide.All, .5f, Color.Green),
        // Установить рамку для ячеек таблицы как Черный
        DefaultCellBorder = new BorderInfo(BorderSide.All, .2f, Color.Green),
    };
    for (var rowCount = 0; rowCount < 10; rowCount++)
    {
        // Добавить строку в таблицу
        var row = table.Rows.Add();
        // Добавить ячейки в таблицу
        for (int i = 0; i < 4; i++)
        {
            row.Cells.Add($"Cell ({i+1}, {rowCount +1})");
        }
    }
    // Добавить объект таблицы на первую страницу входного документа
    document.Pages[1].Paragraphs.Add(table);
```
При инициализации объекта Table были использованы минимальные настройки оформления:

* [ColumnWidths](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/columnwidths) - ширина столбцов (по умолчанию);
* [DefaultCellPadding](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellpadding) - стандартные поля для ячейки таблицы;
* [Border](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/border) - атрибуты рамки таблицы (стиль, толщина, цвет);
* [DefaultCellBorder](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellborder) - атрибуты рамки ячейки (стиль, толщина, цвет).

## Экспорт данных из массива объектов

Класс Table предоставляет методы для взаимодействия с источниками данных ADO.NET - [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1) и [ImportDataView](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/importdataview).

Учитывая, что эти объекты не очень удобны для работы в шаблоне MVC, мы ограничимся кратким примером. В этом примере (строка 50) вызывается метод ImportDataTable, который получает в качестве параметров экземпляр DataTable и дополнительные настройки, такие как флаг заголовка и начальная позиция (строки/столбцы) для вывода данных.

```csharp
// Создать новый PDF документ
var document = new Document
{
    PageInfo = new PageInfo { Margin = new MarginInfo(28, 28, 28, 42) }
};

var pdfPage = document.Pages.Add();

// Инициализирует новый экземпляр TextFragment для заголовка отчета
var textFragment = new TextFragment(reportTitle1);
Table table = new Table
{
    // Установить ширину столбцов таблицы
    ColumnWidths = "25% 25% 25% 25%",
    // Установить отступы в ячейках
    DefaultCellPadding = new MarginInfo(10, 5, 10, 5), // Левый Нижний Правый Верхний
    // Установить цвет границы таблицы в зеленый
    Border = new BorderInfo(BorderSide.All, .5f, Color.Green),
    // Установить границы для ячеек таблицы в черный
    DefaultCellBorder = new BorderInfo(BorderSide.All, .2f, Color.Green),
};

var configuration = new ConfigurationBuilder()
    .SetBasePath(Directory.GetCurrentDirectory())
    .AddJsonFile("config.json", false)
    .Build();

var connectionString = configuration.GetSection("connectionString").Value;

if (string.IsNullOrEmpty(connectionString))
    throw new ArgumentException("Нет строки подключения в config.json");

var resultTable = new DataTable();

using (var conn = new SqlConnection(connectionString))
{
    const string sql = "SELECT * FROM Tennats";
    using (var cmd = new SqlCommand(sql, conn))
    {
        using (var adapter = new SqlDataAdapter(cmd))
        {
            adapter.Fill(resultTable);
        }
    }
}

table.ImportDataTable(resultTable,true,1,1);

// Добавить объект таблицы на первую страницу входного документа
document.Pages[1].Paragraphs.Add(table);
using (var streamOut = new MemoryStream())
{
    document.Save(streamOut);
    return new FileContentResult(streamOut.ToArray(), "application/pdf")
    {
        FileDownloadName = "demotable2.pdf"
    };
}
```

