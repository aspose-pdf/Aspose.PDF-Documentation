---
title: Удаление таблиц из существующего PDF
linktitle: Удаление таблиц
type: docs
weight: 40
url: ru/java/remove-tables-from-existing-pdf/
description: Aspose.PDF для Java позволяет удалять таблицу и несколько таблиц из вашего PDF документа.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Aspose.PDF для Java предлагает возможности для вставки/создания таблиц внутри PDF документа, когда он создается с нуля, или вы также можете добавить объект таблицы в любой существующий PDF документ. Однако у вас может возникнуть необходимость [Манипулировать таблицами в существующем PDF](https://docs.aspose.com/pdf/java/manipulate-tables-in-existing-pdf/), где вы можете обновлять содержимое в существующих ячейках таблицы. Однако у вас может возникнуть требование удалить объекты таблиц из существующего PDF документа.

{{% /alert %}}

Чтобы удалить таблицы, нам нужно использовать класс [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber), чтобы получить доступ к таблицам в существующем PDF, а затем вызвать метод [Remove](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#remove-com.aspose.pdf.AbsorbedTable-).

## Удаление таблицы из PDF документа

Мы добавили новую функцию, т.е. Remove(), в существующий класс [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber) для удаления таблицы из PDF документа. Как только абсорбер успешно находит таблицы на странице, он становится способным их удалять. Пожалуйста, ознакомьтесь с следующим фрагментом кода, показывающим, как удалить таблицу из PDF документа:

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleRemoveTable {
    
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void RemoveTable() {
        // Загрузить существующий PDF документ
        Document pdfDocument = new Document(_dataDir + "Table_input.pdf");

        // Создать объект TableAbsorber для поиска таблиц
        TableAbsorber absorber = new TableAbsorber();

        // Обойти первую страницу с помощью абсорбера
        absorber.visit(pdfDocument.getPages().get_Item(1));

        // Получить первую таблицу на странице
        AbsorbedTable table = absorber.getTableList().get(0);

        // Удалить таблицу
        absorber.remove(table);

        // Сохранить PDF
        pdfDocument.save(_dataDir + "Table_out.pdf");
    }  
```


## Удаление нескольких таблиц из PDF документа

Иногда PDF документ может содержать более одной таблицы, и может возникнуть необходимость удалить из него несколько таблиц. Чтобы удалить несколько таблиц из PDF документа, используйте следующий фрагмент кода:

```java
    public static void RemoveMultipleTable() {
        // Загрузить существующий PDF документ
        Document pdfDocument = new Document(_dataDir + "Table_input2.pdf");

        // Создать объект TableAbsorber для поиска таблиц
        TableAbsorber absorber = new TableAbsorber();

        // Посетить вторую страницу с абсорбером
        absorber.visit(pdfDocument.getPages().get_Item(2));

        // Перебрать копию коллекции и удалить таблицы
        for (AbsorbedTable table : absorber.getTableList())
            absorber.remove(table);

        // Сохранить документ
        pdfDocument.save(_dataDir + "Table2_out.pdf");
    }
}
```