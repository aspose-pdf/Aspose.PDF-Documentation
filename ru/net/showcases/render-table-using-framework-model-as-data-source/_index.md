---
title: Отображение таблицы с использованием Entity Framework
linktitle: Отображение таблицы с использованием Entity Framework
type: docs
weight: 40
url: /ru/net/render-table-using-entity-framework-model-as-data-source/
description: В этой статье показано, как отобразить таблицу, используя модель Entity Framework в качестве источника данных с помощью Aspose.PDF для .NET.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Есть ряд задач, когда по каким-то причинам удобнее экспортировать данные из баз данных в документ PDF, не используя недавно популярную схему конвертации HTML в PDF.

В этой статье показано, как генерировать документ PDF с использованием Aspose.PDF для .NET.

## Основы создания PDF с Aspose.PDF

Одним из самых важных классов в Aspose.PDF является [класс Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Этот класс является движком для рендеринга PDF. Для представления структуры PDF библиотека Aspose.PDF использует модель Документ-Страница, где:

* Document - содержит свойства документа PDF, включая коллекцию страниц;
* Документ - содержит свойства PDF-документа, включая коллекцию страниц;
* Страница - содержит свойства конкретной страницы и различные коллекции элементов, связанных с этой страницей.

Следовательно, чтобы создать PDF-документ с помощью Aspose.PDF, вам следует выполнить следующие шаги:

1. Создать объект Document;
1. Добавить страницу (объект Page) в объект Document;
1. Создать объекты, которые размещаются на странице (например, текстовый фрагмент, таблица и т.д.)
1. Добавить созданные элементы в соответствующую коллекцию на странице (в нашем случае это будет коллекция параграфов);
1. Сохранить документ в формате PDF.

```csharp
// Шаг 1
var document = new Document
{
    PageInfo = new PageInfo { Margin = new MarginInfo(28, 28, 28, 42) }
};

// Шаг 2
var pdfPage = document.Pages.Add();

// Шаг 3
var textFragment = new TextFragment(reportTitle);
// ..........................................

var table = new Table
{
    // .................................
};

// Шаг 4
pdfPage.Paragraphs.Add(textFragment);
pdfPage.Paragraphs.Add(table);

// Шаг 5
using (var streamOut = new MemoryStream())
{
    document.Save(streamOut);
    return new FileContentResult(streamOut.ToArray(), "application/pdf")
    {
        FileDownloadName = "tenants.pdf"
    };
}
```
Самая распространенная проблема - это вывод данных в табличной форме. [Класс Table](https://reference.aspose.com/pdf/net/aspose.pdf/table) используется для обработки таблиц. Этот класс дает нам возможность создавать таблицы и размещать их в документе, используя [Строки](https://reference.aspose.com/pdf/net/aspose.pdf/rows) и [Ячейки](https://reference.aspose.com/pdf/net/aspose.pdf/cell). Таким образом, чтобы создать таблицу, вам нужно добавить необходимое количество строк и заполнить их соответствующим количеством ячеек.

Следующий пример создает таблицу 4x10.

```csharp
var table = new Table
    {
        // Установка автоматической ширины столбцов таблицы
        ColumnWidths = "25% 25% 25% 25%",
        // Установка отступов ячейки
        DefaultCellPadding = new MarginInfo(10, 5, 10, 5), // Слева Снизу Справа Сверху
        // Установка цвета границы таблицы в Зеленый
        Border = new BorderInfo(BorderSide.All, .5f, Color.Green),
        // Установка границ для ячеек таблицы в Черный
        DefaultCellBorder = new BorderInfo(BorderSide.All, .2f, Color.Green),
    };
    for (var rowCount = 0; rowCount < 10; rowCount++)
    {
        // Добавление строки в таблицу
        var row = table.Rows.Add();
        // Добавление ячеек в таблицу
        for (int i = 0; i < 4; i++)
        {
            row.Cells.Add($"Cell ({i+1}, {rowCount +1})");
        }
    }
    // Добавление объекта таблицы на первую страницу входного документа
    document.Pages[1].Paragraphs.Add(table);
```
При инициализации объекта Table были использованы минимальные настройки внешнего вида:

* [ColumnWidths](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/columnwidths) - ширина столбцов (по умолчанию);
* [DefaultCellPadding](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellpadding) - стандартные поля ячейки таблицы;
* [Border](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/border) - атрибуты рамки таблицы (стиль, толщина, цвет);
* [DefaultCellBorder](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellborder) - атрибуты рамки ячейки (стиль, толщина, цвет).

В результате получаем таблицу 4x10 с равной шириной столбцов.

![Table 4x10](http://aspose-html-doc.azurewebsites.net/docs/images/img001.jpg)

## Экспорт данных из объектов ADO.NET

Класс Table предоставляет методы для взаимодействия с источниками данных ADO.NET - [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1) и [ImportDataView](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/importdataview).
Класс Table предоставляет методы для взаимодействия с источниками данных ADO.NET - [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1) и [ImportDataView](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/importdataview).
Учитывая, что эти объекты не очень удобны для работы в шаблоне MVC, мы ограничимся кратким примером. В этом примере (строка 50) вызывается метод ImportDataTable и получает в качестве параметров экземпляр DataTable и дополнительные настройки, такие как флаг заголовка и начальная позиция (строки/столбцы) для вывода данных.

```csharp
// Создать новый документ PDF
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
    DefaultCellPadding = new MarginInfo(10, 5, 10, 5), // Лево Низ Право Верх
    // Установить цвет границы таблицы в зеленый
    Border = new BorderInfo(BorderSide.All, .5f, Color.Green),
    // Установить границы для ячеек таблицы в черный цвет
    DefaultCellBorder = new BorderInfo(BorderSide.All, .2f, Color.Green),
};

var configuration = new ConfigurationBuilder()
    .SetBasePath(Directory.GetCurrentDirectory())
    .AddJsonFile("config.json", false)
    .Build();

var connectionString = configuration.GetSection("connectionString").Value;

if (string.IsNullOrEmpty(connectionString))
    throw new ArgumentException("Отсутствует строка подключения в config.json");

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
## Экспорт данных из Entity Framework

Более актуально для современного .NET является импорт данных из ORM-фреймворков. В этом случае хорошей идеей будет расширение класса Table методами расширения для импорта данных из простого списка или из сгруппированных данных. Давайте приведем пример для одного из самых популярных ORM - Entity Framework.

```csharp
public static class PdfHelper
    {
        public static void ImportEntityList<TSource>(this Pdf.Table table, IList<TSource> data)
        {
            var headRow = table.Rows.Add();

            var props = typeof(TSource).GetProperties(BindingFlags.Public | BindingFlags.Instance);
            foreach (var prop in props)
            {
                headRow.Cells.Add(prop.GetCustomAttribute(typeof(DisplayAttribute)) is DisplayAttribute dd ? dd.Name : prop.Name);
            }

            foreach (var item in data)
            {
                // Добавить строку в таблицу
                var row = table.Rows.Add();
                // Добавить ячейки таблицы
                foreach (var t in props)
                {
                    var dataItem = t.GetValue(item, null);
                    if (t.GetCustomAttribute(typeof(DataTypeAttribute)) is DataTypeAttribute dataType)
                        switch (dataType.DataType)
                        {

                            case DataType.Currency:
                                row.Cells.Add(string.Format("{0:C}", dataItem));
                                break;
                            case DataType.Date:
                                var dateTime = (DateTime)dataItem;
                                if (t.GetCustomAttribute(typeof(DisplayFormatAttribute)) is DisplayFormatAttribute df)
                                {
                                    row.Cells.Add(string.IsNullOrEmpty(df.DataFormatString)
                                        ? dateTime.ToShortDateString()
                                        : string.Format(df.DataFormatString, dateTime));
                                }
                                break;
                            default:
                                row.Cells.Add(dataItem.ToString());
                                break;
                        }
                    else
                    {
                        row.Cells.Add(dataItem.ToString());
                    }
                }
            }
        }
        public static void ImportGroupedData<TKey,TValue>(this Pdf.Table table, IEnumerable<Models.GroupViewModel<TKey, TValue>> groupedData)
        {
            var headRow = table.Rows.Add();           
            var props = typeof(TValue).GetProperties(BindingFlags.Public | BindingFlags.Instance);
            foreach (var prop in props)
            {
               headRow.Cells.Add(prop.GetCustomAttribute(typeof(DisplayAttribute)) is DisplayAttribute dd ? dd.Name : prop.Name);               
            }

            foreach (var group in groupedData)
            {
                // Добавить строку группы в таблицу
                var row = table.Rows.Add();
                var cell = row.Cells.Add(group.Key.ToString());
                cell.ColSpan = props.Length;
                cell.BackgroundColor = Pdf.Color.DarkGray;
                cell.DefaultCellTextState.ForegroundColor = Pdf.Color.White;

                foreach (var item in group.Values)
                {
                    // Добавить строку данных в таблицу
                    var dataRow = table.Rows.Add();
                    // Добавить ячейки
                    foreach (var t in props)
                    {
                        var dataItem = t.GetValue(item, null);

                        if (t.GetCustomAttribute(typeof(DataTypeAttribute)) is DataTypeAttribute dataType)
                            switch (dataType.DataType)
                            {
                                case DataType.Currency:
                                    dataRow.Cells.Add(string.Format("{0:C}", dataItem));
                                    break;
                                case DataType.Date:
                                    var dateTime = (DateTime)dataItem;
                                    if (t.GetCustomAttribute(typeof(DisplayFormatAttribute)) is DisplayFormatAttribute df)
                                    {
                                        dataRow.Cells.Add(string.IsNullOrEmpty(df.DataFormatString)
                                            ? dateTime.ToShortDateString()
                                            : string.Format(df.DataFormatString, dateTime));
                                    }
                                    break;
                                default:
                                    dataRow.Cells.Add(dataItem.ToString());
                                    break;
                            }
                        else
                        {
                            dataRow.Cells.Add(dataItem.ToString());
                        }
                    }
                }
            }
        }
    }
```
Атрибуты Data Annotations часто используются для описания моделей и помогают нам создавать таблицу. Поэтому был выбран следующий алгоритм генерации таблицы для ImportEntityList:

* строки 12-18: создаются строка заголовка и ячейки заголовка в соответствии с правилом "Если присутствует атрибут DisplayAttribute, то берется его значение, иначе берется имя свойства"
* строки 50-53: создаются строки данных и ячейки данных в соответствии с правилом "Если определен атрибут DataTypeAttribute, то мы проверяем, нужно ли делать дополнительные настройки дизайна для него, и иначе просто конвертируем данные в строку и добавляем в ячейку;"

В этом примере были сделаны дополнительные настройки для DataType.Currency (строки 32-34) и DataType.Date (строки 35-43), но вы можете добавить другие, если это необходимо.
Алгоритм метода ImportGroupedData почти такой же, как и предыдущий. Дополнительно используется класс GroupViewModel для хранения сгруппированных данных.

```csharp
using System.Collections.Generic;
    public class GroupViewModel<K,T>
    {
        public K Key;
        public IEnumerable<T> Values;
    }
```
Поскольку мы обрабатываем группы, сначала мы генерируем строку для ключевого значения (строки 66-71), а после этого - строки этой группы.
