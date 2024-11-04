---
title: Манипулирование таблицами в существующем PDF
linktitle: Манипулирование таблицами
type: docs
weight: 30
url: /java/manipulate-tables-in-existing-pdf/
description: Манипулирование таблицами в существующем PDF файле и замена старой таблицы на новую в PDF документе с помощью Aspose.PDF для Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Манипулирование таблицами в существующем PDF

Одна из самых ранних функций, поддерживаемых Aspose.PDF для Java, — это его возможности работы с таблицами, и он обеспечивает отличную поддержку для добавления таблиц в PDF файлы, создаваемые с нуля или в любые существующие PDF файлы.
 You also get the capability to Integrate Table with Database (DOM) to create dynamic tables based on database contents. In this new release, we have implemented new feature of searching and parsing simple tables that already exist on page of PDF document. A new class named **Aspose.PDF.Text.TableAbsorber** provides these capabilities. The usage of TableAbsorber is very much similar to existing TextFragmentAbsorber class.

Вы также получаете возможность интегрировать таблицы с базой данных (DOM) для создания динамических таблиц на основе содержимого базы данных. В этом новом выпуске мы реализовали новую функцию поиска и анализа простых таблиц, которые уже существуют на странице PDF документа. Новый класс с именем **Aspose.PDF.Text.TableAbsorber** предоставляет эти возможности. Использование TableAbsorber очень похоже на существующий класс TextFragmentAbsorber.

The following code snippet shows the steps to update contents in particular table cell.

Следующий фрагмент кода показывает шаги для обновления содержимого в конкретной ячейке таблицы.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleManipulate {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ManipulateTables() {

        // Load existing PDF file
        // Загрузить существующий PDF файл
        Document pdfDocument = new Document(_dataDir + "input.pdf");
        // Create TableAbsorber object to find tables
        // Создать объект TableAbsorber для поиска таблиц
        TableAbsorber absorber = new TableAbsorber();

        // Visit first page with absorber
        // Посетить первую страницу с абсорбером
        absorber.visit(pdfDocument.getPages().get_Item(1));

        // Get access to first table on page, their first cell and text fragments in it
        // Получить доступ к первой таблице на странице, её первой ячейке и текстовым фрагментам в ней
        TextFragment fragment = absorber.getTableList().get(0).getRowList().get(0).getCellList().get(0)
                .getTextFragments().get_Item(1);

        // Change text of the first text fragment in the cell
        // Изменить текст первого текстового фрагмента в ячейке
        fragment.setText("hi world");

        pdfDocument.save(_dataDir + "ManipulateTable_out.pdf");
    }
```

## Заменить старую таблицу на новую в PDF документе

В случае, если вам нужно найти конкретную таблицу и заменить ее на нужную, вы можете использовать метод Replace() класса [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber) для этого.

Следующий пример демонстрирует функциональность замены таблицы внутри PDF документа:

```java
public static void ReplaceOldTableWithNew() {

        // Загрузить существующий PDF документ
        Document pdfDocument = new Document(_dataDir + "Table_input2.pdf");

        // Создать объект TableAbsorber для поиска таблиц
        TableAbsorber absorber = new TableAbsorber();

        Page page = pdfDocument.getPages().get_Item(1);

        // Посетить первую страницу с поглотителем
        absorber.visit(page);

        // Получить первую таблицу на странице
        AbsorbedTable table = absorber.getTableList().get(0);

        // Создать новую таблицу
        Table newTable = new Table();
        newTable.setColumnWidths("100 100 100");
        newTable.setDefaultCellBorder (new BorderInfo(BorderSide.All, 1F));

        Row row = newTable.getRows().add();
        row.getCells().add("Колонка 1");
        row.getCells().add("Колонка 2");
        row.getCells().add("Колонка 3");

        // Заменить таблицу на новую
        absorber.replace(page, table, newTable);

        // Сохранить документ
        pdfDocument.save(_dataDir + "TableReplaced_out.pdf");
        
    }

}
```