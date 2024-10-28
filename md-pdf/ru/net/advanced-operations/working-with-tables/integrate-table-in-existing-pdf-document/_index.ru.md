---
title: Интеграция таблицы с источниками данных PDF
linktitle: Интеграция таблицы
type: docs
weight: 30
url: /net/integrate-table/
description: Эта статья показывает, как интегрировать таблицы PDF. Интеграция таблицы с базой данных и определение, разделится ли таблица на текущей странице.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Интеграция таблицы с источниками данных PDF",
    "alternativeHeadline": "Как интегрировать таблицу с источниками данных PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, интеграция таблицы",
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
    "url": "/net/integrate-table/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/integrate-table/"
    },
    "dateModified": "2022-02-04",
    "description": "Эта статья показывает, как интегрировать таблицы PDF. Интеграция таблицы с базой данных и определение, разделится ли таблица на текущей странице."
}
</script>
Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Интеграция таблицы с базой данных

Базы данных созданы для хранения и управления данными. Распространенной практикой среди программистов является заполнение различных объектов данными из баз данных. В этой статье обсуждается добавление данных из базы данных в таблицу. Возможно заполнить объект [Table](https://reference.aspose.com/pdf/net/aspose.pdf/table) данными из любого источника данных с помощью Aspose.PDF для .NET. И это не только возможно, но и очень просто.

[Aspose.PDF для .NET](https://docs.aspose.com/pdf/net/) позволяет разработчикам импортировать данные из:

- Массива объектов
- DataTable
- DataView

Эта тема предоставляет информацию о получении данных из DataTable или DataView.

Все разработчики, работающие на платформе .NET, должны быть знакомы с основными концепциями ADO.NET, введенными .NET Framework.
Все разработчики, работающие на платформе .NET, должны быть знакомы с базовыми концепциями ADO.NET, введенными .NET Framework.

Методы ImportDataTable(..) и ImportDataView(..) класса Table используются для импорта данных из баз данных.

Пример ниже демонстрирует использование метода ImportDataTable. В этом примере объект DataTable создается с нуля, и записи добавляются программно, вместо того чтобы заполнять DataTable данными из баз данных. Разработчики также могут заполнять DataTable из базы данных по своему желанию.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

DataTable dt = new DataTable("Employee");
dt.Columns.Add("Employee_ID", typeof(Int32));
dt.Columns.Add("Employee_Name", typeof(string));
dt.Columns.Add("Gender", typeof(string));
// Добавляем 2 строки в объект DataTable программно
DataRow dr = dt.NewRow();
dr[0] = 1;
dr[1] = "John Smith";
dr[2] = "Male";
dt.Rows.Add(dr);
dr = dt.NewRow();
dr[0] = 2;
dr[1] = "Mary Miller";
dr[2] = "Female";
dt.Rows.Add(dr);
// Создаем экземпляр документа
Document doc = new Document();
doc.Pages.Add();
// Инициализируем новый экземпляр таблицы
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
// Устанавливаем ширину столбцов таблицы
table.ColumnWidths = "40 100 100 100";
// Устанавливаем цвет границы таблицы как LightGray
table.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// Устанавливаем границы для ячеек таблицы
table.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
table.ImportDataTable(dt, true, 0, 1, 3, 3);

// Добавляем объект таблицы на первую страницу входного документа
doc.Pages[1].Paragraphs.Add(table);
dataDir = dataDir + "DataIntegrated_out.pdf";
// Сохраняем обновленный документ, содержащий объект таблицы
doc.Save(dataDir);
```

## Как определить, разорвется ли таблица на текущей странице

Таблицы по умолчанию добавляются с верхней левой позиции, и если таблица достигает конца страницы, она автоматически разрывается. Вы можете программно получить информацию о том, поместится ли таблица на текущей странице или разорвется внизу страницы. Для этого сначала вам нужно получить информацию о размере документа, затем вам нужно получить информацию о верхнем и нижнем полях страницы, информацию о верхнем поле таблицы и высоте таблицы. Если вы добавите верхнее поле страницы + нижнее поле страницы + верхнее поле таблицы + высоту таблицы и вычтете это из высоты документа, вы можете получить количество оставшегося пространства над документом. В зависимости от конкретной высоты строки (которую вы указали), вы можете рассчитать, могут ли все строки таблицы разместиться в оставшемся пространстве над страницей или нет. Пожалуйста, посмотрите следующий фрагмент кода. В следующем коде средняя высота строки составляет 23.002 пункта.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Создайте объект класса PDF
Document pdf = new Document();
// Добавьте раздел в коллекцию разделов PDF документа
Aspose.Pdf.Page page = pdf.Pages.Add();
// Создайте объект таблицы
Aspose.Pdf.Table table1 = new Aspose.Pdf.Table();
table1.Margin.Top = 300;
// Добавьте таблицу в коллекцию параграфов нужного раздела
page.Paragraphs.Add(table1);
// Установите ширину колонок таблицы
table1.ColumnWidths = "100 100 100";
// Установите границу ячейки по умолчанию, используя объект BorderInfo
table1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);
// Установите границу таблицы, используя другой настроенный объект BorderInfo
table1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
// Создайте объект MarginInfo и установите его левые, нижние, правые и верхние поля
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 5f;
margin.Left = 5f;
margin.Right = 5f;
margin.Bottom = 5f;
// Установите отступы ячеек по умолчанию для объекта MarginInfo
table1.DefaultCellPadding = margin;
// Если увеличить счетчик до 17, таблица разорвется
// Потому что она больше не поместится на этой странице
for (int RowCounter = 0; RowCounter <= 16; RowCounter++)
{
    // Создайте строки в таблице, а затем ячейки в строках
    Aspose.Pdf.Row row1 = table1.Rows.Add();
    row1.Cells.Add("col " + RowCounter.ToString() + ", 1");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 2");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 3");
}
// Получите информацию о высоте страницы
float PageHeight = (float)pdf.PageInfo.Height;
// Получите общую информацию о высоте верхнего и нижнего поля страницы,
// верхнем поле таблицы и высоте таблицы.
float TotalObjectsHeight = (float)page.PageInfo.Margin.Top + (float)page.PageInfo.Margin.Bottom + (float)table1.Margin.Top + (float)table1.GetHeight();

// Отобразите информацию о высоте страницы, высоте таблицы, верхнем поле таблицы и верхнем
// и нижнем поле страницы
Console.WriteLine("Высота документа PDF = " + pdf.PageInfo.Height.ToString() + "\nИнформация о верхнем поле = " + page.PageInfo.Margin.Top.ToString() + "\nИнформация о нижнем поле = " + page.PageInfo.Margin.Bottom.ToString() + "\n\nИнформация о верхнем поле таблицы = " + table1.Margin.Top.ToString() + "\nСредняя высота строки = " + table1.Rows[0].MinRowHeight.ToString() + " \nВысота таблицы " + table1.GetHeight().ToString() + "\n ----------------------------------------" + "\nОбщая высота страницы =" + PageHeight.ToString() + "\nСуммарная высота включая таблицу =" + TotalObjectsHeight.ToString());

// Проверьте, если вычесть сумму верхнего поля страницы + нижнего поля страницы
// + верхнего поля таблицы и высоты таблицы из высоты страницы, и это меньше
// чем 10 (средняя высота строки может быть больше 10)
if ((PageHeight - TotalObjectsHeight) <= 10)
    // Если значение меньше 10, то отобразите сообщение.
    // Которое показывает, что другая строка не может быть размещена, и если мы добавим новую
    // строку, таблица разорвется. Это зависит от значения высоты строки.
    Console.WriteLine("Высота страницы - Высота объектов < 10, так что таблица разорвется");

dataDir = dataDir + "DetermineTableBreak_out.pdf";
// Сохраните документ PDF
pdf.Save(dataDir);
```
## Добавление повторяющихся столбцов в таблицу

В классе Aspose.Pdf.Table вы можете установить RepeatingRowsCount, который будет повторять строки, если таблица слишком длинная по вертикали и переходит на следующую страницу. Однако в некоторых случаях таблицы слишком широки, чтобы поместиться на одной странице и должны быть продолжены на следующей странице. Чтобы решить эту задачу, мы реализовали свойство RepeatingColumnsCount в классе Aspose.Pdf.Table. Установка этого свойства приведет к тому, что таблица будет разбиваться на следующую страницу по столбцам и повторять заданное количество столбцов в начале следующей страницы. Следующий фрагмент кода показывает использование свойства RepeatingColumnsCount:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

string outFile = dataDir + "AddRepeatingColumn_out.pdf";
// Создание нового документа
Document doc = new Document();
Aspose.Pdf.Page page = doc.Pages.Add();

// Создание внешней таблицы, которая занимает всю страницу
Aspose.Pdf.Table outerTable = new Aspose.Pdf.Table();
outerTable.ColumnWidths = "100%";
outerTable.HorizontalAlignment = HorizontalAlignment.Left;

// Создание объекта таблицы, который будет вложен в outerTable и будет разрываться внутри той же страницы
Aspose.Pdf.Table mytable = new Aspose.Pdf.Table();
mytable.Broken = TableBroken.VerticalInSamePage;
mytable.ColumnAdjustment = ColumnAdjustment.AutoFitToContent;

// Добавление outerTable в абзацы страницы
// Добавление mytable в outerTable
page.Paragraphs.Add(outerTable);
var bodyRow = outerTable.Rows.Add();
var bodyCell = bodyRow.Cells.Add();
bodyCell.Paragraphs.Add(mytable);
mytable.RepeatingColumnsCount = 5;
page.Paragraphs.Add(mytable);

// Добавление заголовочной строки
Aspose.Pdf.Row row = mytable.Rows.Add();
row.Cells.Add("header 1");
row.Cells.Add("header 2");
row.Cells.Add("header 3");
row.Cells.Add("header 4");
row.Cells.Add("header 5");
row.Cells.Add("header 6");
row.Cells.Add("header 7");
row.Cells.Add("header 11");
row.Cells.Add("header 12");
row.Cells.Add("header 13");
row.Cells.Add("header 14");
row.Cells.Add("header 15");
row.Cells.Add("header 16");
row.Cells.Add("header 17");

for (int RowCounter = 0; RowCounter <= 5; RowCounter++)

{
    // Создание строк в таблице, затем ячеек в строках
    Aspose.Pdf.Row row1 = mytable.Rows.Add();
    row1.Cells.Add("col " + RowCounter.ToString() + ", 1");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 2");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 3");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 4");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 5");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 6");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 7");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 11");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 12");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 13");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 14");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 15");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 16");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 17");
}
doc.Save(outFile);
```
## Интеграция таблицы с источником Entity Framework

Более актуально для современного .NET является импорт данных из ORM-фреймворков. В этом случае хорошей идеей будет расширение класса Table методами расширения для импорта данных из простого списка или из группированных данных. Давайте приведем пример для одного из самых популярных ORM - Entity Framework.

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
Атрибуты Data Annotations часто используются для описания моделей и помогают нам создать таблицу. Поэтому для ImportEntityList был выбран следующий алгоритм генерации таблицы:

- строки 12-18: создать строку заголовка и добавить ячейки заголовка согласно правилу "Если присутствует DisplayAttribute, то брать его значение, иначе брать имя свойства"
- строки 50-53: создать строки данных и добавить ячейки строк согласно правилу "Если определен атрибут DataTypeAttribute, то проверяем, нужно ли делать дополнительные настройки дизайна для него, и в противном случае просто конвертировать данные в строку и добавить в ячейку;"

В этом примере были сделаны дополнительные настройки для DataType.Currency (строки 32-34) и DataType.Date (строки 35-43), но вы можете добавить другие, если это необходимо.
Алгоритм метода ImportGroupedData почти такой же, как у предыдущего. Дополнительно используется класс GroupViewModel для хранения группированных данных.

```csharp
using System.Collections.Generic;
    public class GroupViewModel<K,T>
    {
        public K Key;
        public IEnumerable<T> Values;
    }
```
Поскольку мы обрабатываем группы, сначала мы генерируем строку для ключевого значения (строки 66-71), а затем - строки этой группы.

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Библиотека Aspose.PDF для .NET",
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
                "availableLanguage": "англ."
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "Великобритания",
                "availableLanguage": "англ."
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "Австралия",
                "availableLanguage": "англ."
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Библиотека для работы с PDF в .NET",
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

