---
title: Манипуляции с таблицами в существующем PDF
linktitle: Манипуляции с таблицами
type: docs
weight: 40
url: /ru/cpp/manipulate-tables-in-existing-pdf/
description: Этот раздел охватывает различные методы изменения таблиц с использованием Aspose.PDF для C++
lastmod: "2021-11-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Манипуляции с таблицами в существующем PDF

Aspose.PDF для C++ позволяет быстро и эффективно работать с таблицами, а именно, создавать их с нуля или добавлять в существующие PDF документы.

Вы также получаете возможность интегрировать таблицу с базой данных (DOM) для создания динамических таблиц на основе содержимого базы данных.

Класс [Aspose.PDF.Text.TableAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.absorbed_table) позволяет искать и анализировать простые таблицы, которые уже существуют на странице PDF документа. Следующий фрагмент кода показывает шаги по обновлению содержимого в конкретной ячейке таблицы.

>Заголовки:

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
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>

#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>

#include <Aspose.PDF.Cpp/Color.h>

#include <Aspose.PDF.Cpp/Table/Table.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/TableAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedTable.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedRow.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedCell.h>
```

>Примеры:

```cpp
using namespace System;
using namespace Aspose::Pdf;

#include "Table-Manipulate.h"

void ManipulateTables() {

    String _dataDir("C:\\Samples\\");

    // Загрузить существующий PDF файл
    auto document = MakeObject<Document>(_dataDir + u"input.pdf");

    // Создать объект TableAbsorber для поиска таблиц
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // Обойти первую страницу с абсорбером
    absorber->Visit(document->get_Pages()->idx_get(1));

    // Получить доступ к первой таблице на странице, ее первой ячейке и фрагментам текста в ней
    auto fragment = absorber->get_TableList()->idx_get(0)->get_RowList()->idx_get(0)->get_CellList()->idx_get(0)->get_TextFragments()->idx_get(1);

    // Изменить текст первого текстового фрагмента в ячейке
    fragment->set_Text(u"hi world");
    document->Save(_dataDir + u"ManipulateTable_out.pdf");
}
```

## Заменить старую таблицу на новую в PDF документе

Если вам нужно найти конкретную таблицу и заменить ее на нужную, вы можете использовать метод Replace() класса [TableAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.absorbed_table) для этого.

Следующий пример демонстрирует функциональность замены таблицы в PDF документе:

```cpp
void ReplaceOldTable() {
    String _dataDir("C:\\Samples\\");

    // Загрузить существующий PDF файл
    auto document = MakeObject<Document>(_dataDir + u"Table_input2.pdf");

    // Создать объект TableAbsorber для поиска таблиц
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // Посетить первую страницу с поглотителем
    absorber->Visit(document->get_Pages()->idx_get(1));

    // Получить первую таблицу на странице
    auto table = absorber->get_TableList()->idx_get(0);

    // Создать новую таблицу
    auto newTable = MakeObject<Table>();
    newTable->set_ColumnWidths(u"100 100 100");
    newTable->set_DefaultCellBorder (MakeObject<BorderInfo>(BorderSide::All, 1.0F));

    auto row = newTable->get_Rows()->Add();
    row->get_Cells()->Add(u"Col 1");
    row->get_Cells()->Add(u"Col 2");
    row->get_Cells()->Add(u"Col 3");

    // Заменить таблицу новой
    absorber->Replace(document->get_Pages()->idx_get(1), table, newTable);

    // Сохранить документ
    document->Save(_dataDir + u"TableReplaced_out.pdf");
}
```