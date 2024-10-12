---
title: Создать или Добавить Таблицу в PDF
linktitle: Создать или Добавить Таблицу
type: docs
weight: 10
url: /cpp/add-table-in-existing-pdf-document/
description: Aspose.PDF для C++ - это библиотека, используемая для создания, чтения и редактирования таблиц PDF. С помощью этой библиотеки вы можете разбивать таблицу на страницы PDF, используя C++.
lastmod: "2021-11-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Создание Таблицы с использованием C++

Таблицы важны при работе с PDF-документами. Они предоставляют отличные возможности для отображения информации систематическим образом.

Таблицы в PDF-документе организуют данные в строки и столбцы систематическим образом. API Aspose.PDF для C++ позволяет добавлять таблицы в PDF-документ и добавлять в них строки и столбцы в ваших C++ приложениях. Класс [Table](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table/) используется для добавления таблицы в документ. Следующие шаги можно выполнить, чтобы добавить таблицу в PDF-документ, используя C++.

### Добавление Таблицы в Существующий PDF Документ

Чтобы добавить таблицу в существующий PDF-файл с помощью Aspose.PDF для C++, выполните следующие шаги:

1. Загрузите исходный файл.
1. Инициализируйте таблицу и задайте ее столбцы и строки.
1. Установите настройки таблицы (мы установили границы).
1. Заполните таблицу.
1. Добавьте таблицу на страницу.
1. Сохраните файл.

Следующие фрагменты кода показывают, как добавить текст в существующий PDF файл.

>Заголовки

```cpp
#include <system/date_time.h>
#include <system/io/file.h>
#include <system/console.h>
#include <data/data_table.h>
#include <data/data_column_collection.h>
#include <system/type_info.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/PageInfo.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/Generator/GraphInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderCornerStyle.h>
#include <Aspose.PDF.Cpp/Generator/ColumnAdjustment.h>
#include <Aspose.PDF.Cpp/Generator/ImageFileType.h>
#include <Aspose.PDF.Cpp/Generator/Image.h>
#include <Aspose.PDF.Cpp/Generator/HtmlFragment.h>

#include <Aspose.PDF.Cpp/Text/TextFragment.h>

#include <Aspose.PDF.Cpp/Color.h>

#include <Aspose.PDF.Cpp/Table/Table.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
```

>Sample

```cpp
using namespace System;
using namespace Aspose::Pdf;

void AddingTableInExistingPDFDocument() {
    
    String _dataDir("C:\\Samples\\");
    
    // Загрузить исходный PDF документ
    auto document = MakeObject<Document>(_dataDir + u"AddTable.pdf");
    
    // Инициализирует новый экземпляр Table
    auto table = MakeObject<Table>();
    
    // Установить цвет границы таблицы как LightGray
    table->set_Border(MakeObject<Aspose::Pdf::BorderInfo>(
        Aspose::Pdf::BorderSide::All, .5f, 
        Aspose::Pdf::Color::get_LightGray()));
    // Установить границу для ячеек таблицы
    table->set_DefaultCellBorder (MakeObject<Aspose::Pdf::BorderInfo>(
        Aspose::Pdf::BorderSide::All, .5f, 
        Aspose::Pdf::Color::get_LightGray()));

    // Создать цикл для добавления 10 строк
    for (int row_count = 1; row_count < 10; row_count++)
    {
        // Добавить строку в таблицу
        auto row = table->get_Rows()->Add();
        // Добавить ячейки в таблицу
        row->get_Cells()->Add(String::Format(u"Колонка ({0}, 1)", row_count));
        row->get_Cells()->Add(String::Format(u"Колонка ({0}, 2)", row_count));
        row->get_Cells()->Add(String::Format(u"Колонка ({0}, 3)", row_count));
    }

    // Добавить объект таблицы на первую страницу входного документа
    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(table);
    
    // Сохранить обновленный документ, содержащий объект таблицы
    document->Save(_dataDir + u"document_with_table_out.pdf");
}
```

### ColSpan и RowSpan в таблицах

Aspose.PDF для C++ предоставляет свойство [ColSpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell#ae79c581d2245258699c98617e78c01d1) для объединения столбцов в таблице и свойство [RowSpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell#a4eb7337d118314e6c2180670fb32721a) для объединения строк.

Мы используем свойство [ColSpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell#ae79c581d2245258699c98617e78c01d1) или [RowSpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell#a4eb7337d118314e6c2180670fb32721a) для объекта [Cell](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell), который создает ячейку таблицы. После применения необходимых свойств созданная ячейка может быть добавлена в таблицу.

```cpp
void AddTable_RowColSpan()
{
    String _dataDir("C:\\Samples\\");

    // Загрузите источник PDF документа
    auto document = MakeObject<Document>();
    document->get_Pages()->Add();

    // Инициализируйте новый экземпляр таблицы
    auto table = MakeObject<Table>();
    // Установите цвет границы таблицы как LightGray
    table->set_Border(MakeObject<Aspose::Pdf::BorderInfo>(
        Aspose::Pdf::BorderSide::All, .5f, 
        Color::get_Black()));
        // Установите границу для ячеек таблицы
    table->set_DefaultCellBorder(
        MakeObject<Aspose::Pdf::BorderInfo>(
            Aspose::Pdf::BorderSide::All, .5f, 
            Color::get_Black()));
    

    // Добавьте 1-ю строку в таблицу
    auto row1 = table->get_Rows()->Add();
    for (int cellCount = 1; cellCount < 5; cellCount++)
    {
        // Добавьте ячейки в таблицу
        row1->get_Cells()->Add(String::Format(u"Тест 1 {0}", cellCount));
    }

    // Добавьте 2-ю строку в таблицу
    auto row2 = table->get_Rows()->Add();
    row2->get_Cells()->Add(u"Тест 2 1");
    auto cell = row2->get_Cells()->Add(u"Тест 2 2");
    cell->set_ColSpan(2);
    row2->get_Cells()->Add(u"Тест 2 4");

    // Добавьте 3-ю строку в таблицу
    auto row3 = table->get_Rows()->Add();
    row3->get_Cells()->Add(u"Тест 3 1");
    row3->get_Cells()->Add(u"Тест 3 2");
    row3->get_Cells()->Add(u"Тест 3 3");
    row3->get_Cells()->Add(u"Тест 3 4");

    // Добавьте 4-ю строку в таблицу
    auto row4 = table->get_Rows()->Add();
    row4->get_Cells()->Add(u"Тест 4 1");
    cell = row4->get_Cells()->Add(u"Тест 4 2");
    cell->set_RowSpan (2);
    row4->get_Cells()->Add(u"Тест 4 3");
    row4->get_Cells()->Add(u"Тест 4 4");


    // Добавьте 5-ю строку в таблицу
    auto row5 = table->get_Rows()->Add();
    row5->get_Cells()->Add(u"Тест 5 1");
    row5->get_Cells()->Add(u"Тест 5 3");
    row5->get_Cells()->Add(u"Тест 5 4");

    // Добавьте объект таблицы на первую страницу входного документа
    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(table);

    // Сохраните обновленный документ, содержащий объект таблицы
    document->Save(_dataDir + u"document_with_table_out.pdf");
}
```

Результатом выполнения кода ниже является таблица, изображенная на следующем изображении:

![Демонстрация ColSpan и RowSpan](colspan_rowspan.png)

## Работа с границами, полями и отступами

Обратите внимание, что он также поддерживает функцию установки границ, полей и отступов ячеек для таблиц, давайте сначала поймем концепцию границ, полей и отступов, которые представлены на диаграмме ниже:

![Границы, поля и отступы](set-border-style-margins-and-padding-of-table_1.png)

Проверьте рисунок подробно. Он показывает, что границы таблицы, строк и ячеек перекрываются. Используя Aspose.PDF для C++, таблица может иметь поля, а ячейки могут быть с отступами. Чтобы установить поля ячеек, мы должны установить отступы ячеек.

## Границы

Чтобы установить границы объектов Table, [Row](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.row) и [Cell](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell), используйте свойства Table.Border, Row.Border и Cell.Border. Границы ячеек также могут быть установлены с использованием свойства DefaultCellBorder класса [Table](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table) или Row. Все свойства, связанные с границей, обсужденные выше, назначаются экземпляру класса Row, который создается вызовом его конструктора. Класс Row имеет множество перегрузок, которые принимают почти все параметры, необходимые для настройки границы.

## Поля или отступы

Отступы ячеек можно управлять с помощью свойства класса Table [DefaultCellPadding](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table#ac64196de6dfed7550c3278892ed9dbe0). Все свойства, связанные с отступами, назначаются экземпляру класса [MarginInfo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.margin_info/), который принимает информацию о параметрах `Left`, `Right`, `Top` и `Bottom` для создания пользовательских полей.

![Поля и границы в таблице PDF](margin-border.png)

```cpp
void AddTable_MergingPadding() {

    String _dataDir("C:\\Samples\\");

    // Создание объекта Document вызовом его пустого конструктора
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    // Создание объекта таблицы
    auto tab1 = MakeObject<Table>();
    // Добавление таблицы в коллекцию параграфов нужного раздела
    page->get_Paragraphs()->Add(tab1);
    // Установка ширины столбцов таблицы
    tab1->set_ColumnWidths (u"50 50 50");
    // Установка границы ячеек по умолчанию с использованием объекта BorderInfo
    tab1->set_DefaultCellBorder (
        MakeObject<Aspose::Pdf::BorderInfo>(
            Aspose::Pdf::BorderSide::All, 0.1F));
    // Установка границы таблицы с использованием другого настраиваемого объекта BorderInfo
    tab1->set_Border (
        MakeObject<Aspose::Pdf::BorderInfo>(
            Aspose::Pdf::BorderSide::All, 1.0F));

    // Создание объекта MarginInfo и установка его полей left, bottom, right и top
    auto margin = MakeObject<MarginInfo>();
    margin->set_Top (5.0f);
    margin->set_Left (5.0f);
    margin->set_Right (5.0f);
    margin->set_Bottom (5.0f);

    // Установка отступа ячеек по умолчанию для объекта MarginInfo
    tab1->set_DefaultCellPadding (margin);
    // Создание строк в таблице, а затем ячеек в строках
    auto row1 = tab1->get_Rows()->Add();
    row1->get_Cells()->Add(u"col1");
    row1->get_Cells()->Add(u"col2");
    row1->get_Cells()->Add();

    auto mytext = MakeObject<Aspose::Pdf::Text::TextFragment>(u"col3 with large text string");
        
    row1->get_Cells()->idx_get(2)->get_Paragraphs()->Add(mytext);
    row1->get_Cells()->idx_get(2)->set_IsWordWrapped(false);
    

    auto row2 = tab1->get_Rows()->Add();
    row2->get_Cells()->Add(u"item1");
    row2->get_Cells()->Add(u"item2");
    row2->get_Cells()->Add(u"item3");
    
    // Сохранение PDF
    document->Save(_dataDir + u"MarginsOrPadding_out.pdf");
}
```
Чтобы создать таблицу с закругленными углами, используйте класс [BorderInfo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.border_info) со значением [RoundedBorderRadius](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.border_info#a6a2bed69dd034fba9ce439dcbe1fd3de) и установите стиль углов таблицы на круглый.

```cpp
void AddTable_RoundedBorderRadius()
{
    // Путь к каталогу документов.
    String _dataDir("C:\\Samples\\");

    auto tab1 = MakeObject<Aspose::Pdf::Table>();

    auto graph = MakeObject<GraphInfo>();
    graph->set_Color(Color::get_Red());
    // Создать пустой объект BorderInfo
    auto bInfo = MakeObject<BorderInfo>(BorderSide::All, graph);

    // Установите округлую границу с радиусом 15
    bInfo->set_RoundedBorderRadius(15);
    // Установите стиль углов таблицы как круглый.
    tab1->set_CornerStyle (Aspose::Pdf::BorderCornerStyle::Round);
    // Установите информацию о границе таблицы
    tab1->set_Border(bInfo);
}
```

### Свойство AutoFitToWindow в перечислении ColumnAdjustmentType

```cpp
void AddTable_AutoFitToWindow() {
    
    // Путь к директории с документами.
    String _dataDir("C:\\Samples\\");

    // Создание объекта Pdf, вызвав его пустой конструктор
    auto document = MakeObject<Document>();

    // Создание секции в объекте Pdf
    auto sec1 = document->get_Pages()->Add();

    // Создание объекта таблицы
    auto tab1 = MakeObject<Aspose::Pdf::Table>();
    // Добавление таблицы в коллекцию абзацев нужной секции
    sec1->get_Paragraphs()->Add(tab1);

    // Установка ширины столбцов таблицы
    tab1->set_ColumnWidths (u"50 50 50");
    tab1->set_ColumnAdjustment (ColumnAdjustment::AutoFitToWindow);

    // Установка границ ячеек по умолчанию с использованием объекта BorderInfo
    tab1->set_DefaultCellBorder(MakeObject<BorderInfo>(Aspose::Pdf::BorderSide::All, 0.1F));

    // Установка границы таблицы с использованием другого объекта BorderInfo
    tab1->set_Border (MakeObject<BorderInfo>(Aspose::Pdf::BorderSide::All, 1.0F));

    // Создание объекта MarginInfo и установка его отступов слева, снизу, справа и сверху
    auto margin = MakeObject<MarginInfo>();
    margin->set_Top(5.0f);
    margin->set_Left(5.0f);
    margin->set_Right(5.0f);
    margin->set_Bottom(5.0f);

    // Установка отступов ячеек по умолчанию на объект MarginInfo
    tab1->set_DefaultCellPadding(margin);

    // Создание строк в таблице, а затем ячеек в строках
    auto row1 = tab1->get_Rows()->Add();
    row1->get_Cells()->Add(u"col1");
    row1->get_Cells()->Add(u"col2");
    row1->get_Cells()->Add(u"col3");

    auto row2 = tab1->get_Rows()->Add();
    row2->get_Cells()->Add(u"item1");
    row2->get_Cells()->Add(u"item2");
    row2->get_Cells()->Add(u"item3");
    
    // Сохранение обновленного документа, содержащего объект таблицы
    document->Save(_dataDir + u"AutoFitToWindow_out.pdf");
}
```

### Получение Ширины Таблицы

Существуют задачи, в которых необходимо динамически получить ширину таблицы.
Класс [Aspose.PDF.Table](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table) имеет метод [GetWidth] (https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table#a3361cc8d4af87eec2e3da616c474ac1c) для этой цели. Например, вы не установили явно ширину столбцов таблицы и не установили [ColumnAdjustment] (https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#afc01382935026dd569c96d77d09dc3a4) в AutoFitToContent. В этом случае вы можете получить следующую ширину таблицы.

```cpp
void GetTableWidth() {
    // Создать новый документ
    auto document = MakeObject<Document>();
    
    // Добавить страницу в документ
    auto page = document->get_Pages()->Add();

    // Инициализировать новую таблицу
    auto table = MakeObject<Table>();
    table->set_ColumnAdjustment(ColumnAdjustment::AutoFitToContent);
    
    // Добавить строку в таблицу
    auto row = table->get_Rows()->Add();

    // Добавить ячейку в таблицу
    auto cell = row->get_Cells()->Add(u"Cell 1 text");
    cell = row->get_Cells()->Add(u"Cell 2 text");
    // Получить ширину таблицы
    Console::WriteLine(table->GetWidth());
}
```

## Добавление SVG изображения в ячейку таблицы

Aspose.PDF для C++ позволяет добавлять ячейки таблицы в PDF файл. Когда вы создаете таблицу, вы можете добавлять текст или изображения в ячейки. Кроме того, API также предлагает функцию для преобразования файлов SVG в PDF. Используя комбинацию этих функций, можно загрузить SVG изображение и добавить его в ячейку таблицы.

Следующий фрагмент кода показывает шаги для создания таблицы и добавления SVG изображения в ячейку таблицы.

```cpp
void InsertSVGObject() 
{
    String _dataDir("C:\\Samples\\");

    // Создание объекта документа
    auto document = MakeObject<Document>();
    // Создание экземпляра изображения
    auto img = MakeObject<Aspose::Pdf::Image>();

    // Установить тип изображения как SVG
    img->set_FileType(Aspose::Pdf::ImageFileType::Svg);
    // Путь к исходному файлу
    img->set_File (_dataDir + u"SVGToPDF.svg");
    // Установить ширину для экземпляра изображения
    img->set_FixWidth (50);
    // Установить высоту для экземпляра изображения
    img->set_FixHeight(50);
    // Создание экземпляра таблицы
    auto table = MakeObject<Aspose::Pdf::Table>();
    // Установить ширину для ячеек таблицы
    table->set_ColumnWidths (u"100 100");
    // Создание объекта строки и добавление его в экземпляр таблицы
    auto row = table->get_Rows()->Add();
    // Создание объекта ячейки и добавление его в экземпляр строки
    auto cell = row->get_Cells()->Add();
    // Добавить текстовый фрагмент в коллекцию абзацев объекта ячейки
    cell->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"Первая ячейка"));
    // Добавить еще одну ячейку в объект строки
    cell = row->get_Cells()->Add();
    // Добавить SVG изображение в коллекцию абзацев недавно добавленного экземпляра ячейки
    cell->get_Paragraphs()->Add(img);
    // Создание объекта страницы и добавление его в коллекцию страниц экземпляра документа
    auto page = document->get_Pages()->Add();
    // Добавить таблицу в коллекцию абзацев объекта страницы
    page->get_Paragraphs()->Add(table);    
    // Сохранить PDF файл
    document->Save(_dataDir + u"AddSVGObject_out.pdf");
}
```

## Использование HTML тегов внутри таблицы

Для некоторых задач вам потребуется импортировать содержимое базы данных с некоторыми HTML тегами, а затем импортировать содержимое в объект таблицы. При импорте содержимого HTML теги должны отображаться внутри PDF документа.

В следующем фрагменте кода вы можете установить цвет границы таблицы, установить границы для ячеек таблицы. Затем создайте цикл для добавления 10 строк. Добавьте объект таблицы на первую страницу входного документа и сохраните обновленный документ.

```cpp
void AddHTMLFragmentToTableCell() {
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"input.pdf");    
    // Инициализирует новый экземпляр таблицы
    auto table = MakeObject<Table>();
    // Установите цвет границы таблицы как LightGray
    table->set_Border(new BorderInfo(BorderSide::All, .5f, Color::get_LightGray()));
    // Установите границу для ячеек таблицы
    table->set_DefaultCellBorder(new BorderInfo(BorderSide::All, .5f, Color::get_LightGray()));
    // Создайте цикл для добавления 10 строк       
    for (int row_count = 1; row_count < 10; row_count++) {
        SmartPtr<Cell> cell;
        // Добавьте строку в таблицу
        auto row = table->get_Rows()->Add();
        // Добавьте ячейки в таблицу
        cell = row->get_Cells()->Add();
        cell->get_Paragraphs()->Add(new HtmlFragment(String::Format(u"Столбец <strong>({0}, 1)</strong>", row_count)));

        cell = row->get_Cells()->Add();
        cell->get_Paragraphs()->Add(new HtmlFragment(String::Format(u"Столбец <span style='color:red'>({0}, 2)</span>",row_count)));

        cell = row->get_Cells()->Add();
        cell->get_Paragraphs()->Add(new HtmlFragment(String::Format(u"Столбец <span style='text-decoration: underline'>([0}, 3)</span>", row_count)));
    }
    // Добавьте объект таблицы на первую страницу входного документа
    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(table);
    // Сохраните обновленный документ, содержащий объект таблицы
    document->Save(_dataDir + u"AddHTMLObject_out.pdf");
}
```

## Вставка разрыва страницы между строками таблицы

Как правило, при создании таблицы в формате PDF таблица переходит на последующие страницы, когда достигает нижнего поля таблицы. Но у нас может быть требование вставить разрыв страницы, когда к таблице добавляется определенное количество строк. Следующий фрагмент кода показывает шаги для вставки разрыва страницы при добавлении 10 строк в таблицу.

Следующий фрагмент кода показывает шаги для вставки разрыва страницы, когда добавлено 10 строк в таблицу.

```cpp
void InsertPageBreak() {
    String _dataDir("C:\\Samples\\");

    // Создать экземпляр документа
    auto document = MakeObject<Document>();
    
    // Добавить страницу в коллекцию страниц PDF файла
    auto page = document->get_Pages()->Add();

    // Создать экземпляр таблицы
    auto tab = MakeObject<Table>();

    // Установить стиль границы для таблицы
    tab->set_Border(MakeObject<BorderInfo>(BorderSide::All, Color::get_Red()));
    // Установить стиль границы по умолчанию для таблицы с цветом границы Красный
    tab->set_DefaultCellBorder(MakeObject<BorderInfo>(BorderSide::All, Color::get_Red()));
    // Указать ширину столбцов таблицы
    tab->set_ColumnWidths(u"100 100");

    // Создать цикл для добавления 200 строк в таблицу
    for (int counter = 0; counter <= 200; counter++) {
        auto row = MakeObject<Row>();
        tab->get_Rows()->Add(row);
        auto cell1 = MakeObject<Cell>();
        cell1->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(String::Format(u"Cell {0}, 0", counter)));
        row->get_Cells()->Add(cell1);

        auto cell2 = new Cell();
        cell2->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(String::Format(u"Cell {0}, 1", counter)));
        row->get_Cells()->Add(cell2);
        // Когда добавлено 10 строк, отрисовать новую строку на новой странице
        if (counter % 10 == 0 && counter != 0)
            row->set_IsInNewPage(true);
    }
    // Добавить таблицу в коллекцию параграфов PDF файла
    page->get_Paragraphs()->Add(tab);

    // Сохранить PDF документ
    document->Save(_dataDir + u"InsertPageBreak_out.pdf");
}
```

## Отображение таблицы на новой странице

По умолчанию абзацы добавляются в коллекцию абзацев объекта Page. Однако возможно отобразить таблицу на новой странице, а не непосредственно после ранее добавленного объекта уровня абзаца на странице.

### Пример: Как отобразить таблицу на новой странице с использованием C++

Чтобы отобразить таблицу на новой странице, используйте свойство [IsInNewPage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.base_paragraph#a614946048d22afb9dce4cd42346c7561) в классе [BaseParagraph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.base_paragraph). Следующий фрагмент кода показывает, как это сделать.

```cpp
void RenderTableOnNewPage()
{
    auto document = MakeObject<Document>();
    auto pageInfo = document->get_PageInfo();
    auto marginInfo = pageInfo->get_Margin();

    marginInfo->set_Left (37);
    marginInfo->set_Right (37);
    marginInfo->set_Top (37);
    marginInfo->set_Bottom (37);

    pageInfo->set_IsLandscape(true);

    auto table = MakeObject<Aspose::Pdf::Table>();
    table->set_ColumnWidths(u"50 100");
    // Добавлена страница.
    auto curPage = document->get_Pages()->Add();
    for (int i = 1; i <= 120; i++)
    {
        auto row = table->get_Rows()->Add();
        row->set_FixedRowHeight(15);
        auto cell1 = row->get_Cells()->Add();
        cell1->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"Содержимое 1"));
        auto cell2 = row->get_Cells()->Add();
        cell2->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"HHHHH"));
    }
    auto paragraphs = curPage->get_Paragraphs();
    paragraphs->Add(table);

    //-------------------------------------

    auto document = MakeObject<Document>();
    auto table1 = MakeObject<Aspose::Pdf::Table>();
    table1->set_ColumnWidths(u"100 100");

    String _dataDir("C:\\Samples\\");

    for (int i = 1; i <= 10; i++)
    {
        auto row = table1->get_Rows()->Add();
        auto cell1 = row->get_Cells()->Add();
        cell1->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"LAAAAAAA"));
        auto cell2 = row->get_Cells()->Add();
        cell2->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"LAAGGGGGG"));
    }
    
    table1->set_IsInNewPage (true);
    // Я хочу оставить таблицу 1 на следующей странице, пожалуйста...
    paragraphs->Add(table1);
    
    document->Save(_dataDir + u"IsNewPageProperty_Test_out.pdf");
}
```