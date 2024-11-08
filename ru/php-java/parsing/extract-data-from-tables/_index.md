---
title: Извлечение данных таблицы из PDF 
linktitle: Извлечение данных таблицы
type: docs
weight: 40
url: /ru/php-java/extract-data-from-table-in-pdf/
description: Узнайте, как извлечь табличные данные из PDF с помощью Aspose.PDF для PHP
lastmod: "2021-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Программное извлечение таблиц из PDF

Извлечение таблиц из PDF не является тривиальной задачей, потому что таблица может быть создана различными способами.

Aspose.PDF для PHP через Java имеет инструмент, который упрощает извлечение таблиц. Чтобы извлечь данные таблицы, выполните следующие шаги:

1. Откройте PDF документ - создайте объект [Document](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/Document);
1. Создайте объект TableAbsorber [TableAbsorber](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/tableabsorber), чтобы извлечь таблицы из документа.
1. Переберите каждую страницу документа.

1. Решите, какие страницы будут анализироваться, и примените [visit](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TableAbsorber#visit-com.aspose.pdf.Page-) к нужным страницам. Табличные данные будут сканироваться, и результат будет сохранен в списке [AbsorbedTable](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedTable). Мы можем получить этот список через метод [getTableList](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TableAbsorber#getTableList--).

1. Чтобы получить данные, итерируйте через `TableList` и обрабатывайте список [поглощенных строк](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedRow) и список поглощенных ячеек. Мы можем получить доступ к первому списку, вызвав метод [getTableList](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TableAbsorber#getTableList--), и ко второму, вызвав метод [getCellList](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedRow#getCellList--).

1. Каждый [AbsorbedCell](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedCell) содержит [TextFragmentCollections](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TextFragmentCollection). Вы можете обработать это для своих целей.

Следующий пример показывает извлечение таблицы со всех страниц:

```php

$document = new Document($inputFile);
$tableAbsorber = new TableAbsorber();

for ($pageIndex = 1; $pageIndex <= java_values($pages->size()); $pageIndex++) {
    $page = $pages->get_Item($pageIndex);
    $tableAbsorber->visit($page);
    $tableList = $tableAbsorber->getTableList();
    $tableIterator = $tableList->iterator();

    while (java_values($tableIterator->hasNext())) {
        $table = $tableIterator->next();
        $tableRowList = $table->getRowList();
        $tableRowListIterator = $tableRowList->iterator();

        while (java_values($tableRowListIterator->hasNext())) {
            $row = $tableRowListIterator->next();
            $cellList = $row->getCellList();
            $cellListIterator = $cellList->iterator();

            // Перебираем каждую ячейку в строке.
            while (java_values($cellListIterator->hasNext())) {
                $cell = $cellListIterator->next();
                $fragmentList = $cell->getTextFragments();

                // Перебираем каждый текстовый фрагмент в ячейке.
                for ($fragmentIndex = 1; $fragmentIndex <= java_values($fragmentList->size()); $fragmentIndex++) {
                    $fragment = $fragmentList->get_Item($fragmentIndex);
                    $segments = $fragment->getSegments();

                    // Перебираем каждый сегмент в текстовом фрагменте.
                    for ($segmentIndex = 1; $segmentIndex <= java_values($segments->size()); $segmentIndex++) {
                        $segment = $segments->get_Item($segmentIndex);
                        $responseData .= $segment->getText();
                    }
                }
                $responseData .= "|";
            }
            $responseData .= PHP_EOL;
        }
    }
}

// Сохраните данные таблицы в выходной файл.
file_put_contents($outputFile, $responseData);

// Закрыть PDF документ.
$document->close();
```


## Извлечение данных таблицы из PDF и сохранение их в CSV файл

Следующий пример показывает, как извлечь таблицу и сохранить ее как CSV файл.
Чтобы узнать, как преобразовать PDF в электронную таблицу Excel, пожалуйста, обратитесь к статье [Преобразование PDF в Excel](/pdf/ru/php-java/convert-pdf-to-excel/).

```php

    // Загрузите входной PDF документ, используя класс Document.
    $document = new Document($inputFile);

    // Создайте экземпляр класса ExcelSaveOptions, чтобы указать параметры сохранения.
    $saveOption = new ExcelSaveOptions();

    // Установите формат вывода в CSV.
    $saveOption->setFormat(ExcelSaveOptions_ExcelFormat::$CSV);

    // Сохраните PDF документ как файл Excel, используя указанные параметры сохранения.
    $document->save($outputFile, $saveOption);
```