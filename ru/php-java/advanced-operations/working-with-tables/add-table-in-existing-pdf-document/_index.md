---
title: Создание или Добавление Таблицы в PDF
linktitle: Создание или Добавление Таблицы
type: docs
weight: 10
url: ru/php-java/add-table-in-existing-pdf-document/
description: Узнайте, как создать или добавить таблицу в PDF-документ, применить стиль ячеек, разделить таблицу на страницы и настроить строки и столбцы и т.д.
lastmod: "2024-05-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Добавление Таблицы в Существующий PDF Документ

Чтобы добавить таблицу в существующий PDF файл с помощью Aspose.PDF для PHP, выполните следующие шаги:

1. Загрузите исходный файл.
1. Инициализируйте таблицу
1. Установите цвет границы таблицы как LightGray
1. Установите границу для ячеек таблицы
1. Создайте цикл для добавления 10 строк
1. Добавьте объект таблицы на первую страницу входного документа
1. Сохраните файл.

Следующие фрагменты кода показывают, как добавить текст в существующий PDF файл.

```php

    // Открыть документ
    $document = new Document($inputFile);        
    // Инициализирует новый экземпляр таблицы
    $table = new Table();
    $colors= new Color();
    // Установить цвет границы таблицы как LightGray
    $borderSide = new BorderSide();
    $borderInfo = new BorderInfo($borderSide->All, 0.5, $colors->getLightGray());
    $table->setBorder($borderInfo);
    // установить границу для ячеек таблицы
    $table->setDefaultCellBorder($borderInfo);
    // создать цикл для добавления 10 строк
    for ($row_count = 1; $row_count < 10; $row_count++) {
        // добавить строку в таблицу
        $row = $table->getRows()->add();
        // добавить ячейки в таблицу
        $row->getCells()->add("Column (" . $row_count . ", 1)");
        $row->getCells()->add("Column (" . $row_count . ", 2)");
        $row->getCells()->add("Column (" . $row_count . ", 3)");
    }
    // Добавить объект таблицы на первую страницу входного документа
    $document->getPages()->add()->getParagraphs()->add($table);

    // Сохранить итоговый PDF документ.    
    $document->save($outputFile);
    $document->close();
```