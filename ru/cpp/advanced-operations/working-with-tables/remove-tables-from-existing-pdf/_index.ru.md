---
title: Удалить таблицы из существующего PDF
linktitle: Удалить таблицы
type: docs
weight: 50
url: /cpp/remove-tables-from-existing-pdf/
description: Этот раздел описывает, как удалить таблицу из PDF документа.
lastmod: "2021-11-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF для C++ позволяет вставлять и создавать таблицы внутри PDF документа, когда он создается с нуля, или вы также можете добавить объект таблицы в любой существующий PDF документ. Но у вас может возникнуть необходимость [манипулировать таблицами в существующем PDF](https://docs.aspose.com/pdf/cpp/manipulate-tables-in-existing-pdf/), где вы можете обновить содержимое в существующих ячейках таблицы. Также у вас может возникнуть необходимость удалить объекты таблицы из существующих PDF документов.

Для удаления таблиц нам необходимо использовать класс [TableAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.absorbed_table), чтобы получить таблицы в существующем PDF, и затем вызвать метод 'Remove'.

## Удалить таблицу из PDF документа

Мы добавили новую функцию, т.е. [Убрать](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber#ace39006d8f44c9cb776ee26281a1cbb3) в существующий класс TableAbsorber, чтобы удалить таблицу из PDF документа. Как только абсорбер успешно находит таблицы на странице, он становится способным их удалять. Пожалуйста, ознакомьтесь с следующим примером кода, показывающим, как удалить таблицу из PDF документа:

>Headers:

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/TableAbsorber.h>
```

>Samples:

```cpp
using namespace System;
using namespace Aspose::Pdf;

void RemoveTable() {

    String _dataDir("C:\\Samples\\");

    // Загрузить исходный PDF документ
    auto document = MakeObject<Document>(_dataDir + u"Table_input.pdf");

    // Создать объект TableAbsorber для поиска таблиц
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // Посетить первую страницу с абсорбером
    absorber->Visit(document->get_Pages()->idx_get(1));

    // Получить первую таблицу на странице
    auto table = absorber->get_TableList()->idx_get(0);

    // Удалить таблицу
    absorber->Remove(table);

    // Сохранить PDF
    document->Save(_dataDir + u"Table_out.pdf");
}
```
## Удаление нескольких таблиц из PDF документа

Некоторые задачи будут связаны с работой с несколькими таблицами в одном PDF документе. И вам нужно будет удалить из него несколько таблиц. Чтобы удалить несколько таблиц из PDF документа, используйте следующий фрагмент кода:

```cpp
void RemoveMultipleTables() {

    String _dataDir("C:\\Samples\\");

    // Загрузить существующий PDF документ
    auto document = MakeObject<Document>(_dataDir + u"Table_input2.pdf");

    // Создать объект TableAbsorber для поиска таблиц
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // Посетить первую страницу с поглотителем
    absorber->Visit(document->get_Pages()->idx_get(1));

    // Получить копию коллекции таблиц
    auto tables = absorber->get_TableList();


    // Перебрать копию коллекции и удалить таблицы
    for(auto table : tables)
    absorber->Remove(table);

    // Сохранить документ
    document->Save(_dataDir + u"Table2_out.pdf");
}
```

{{% alert color="primary" %}}

Пожалуйста, учитывайте, что удаление или замена таблицы изменяет коллекцию TableList. Therefore, in case removing/replacing tables in a loop the copying of TableList collection is essential.

{{% /alert %}}