---
title: Извлечение абзаца из PDF
linktitle: Извлечение абзаца
type: docs
weight: 20
url: /php-java/extract-paragraph-from-pdf/
description: В этой статье описывается, как использовать ParagraphAbsorber - специальный инструмент в Aspose.PDF для извлечения текста из PDF-документов.
lastmod: "2024-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Извлечение текста из PDF-документа в форме абзацев

Мы можем получить текст из PDF-документа, ищя определенный текст (используя "обычный текст" или "регулярные выражения") с одной страницы или всего документа, или мы можем получить полный текст одной страницы, диапазона страниц или полного документа. Однако в некоторых случаях вам требуется извлечь абзацы из PDF-документа или текст в форме абзацев. Мы реализовали функциональность для поиска секций и абзацев в тексте страниц PDF-документа. Мы представили класс ParagraphAbsorber (как TextFragmentAbsorber и TextAbsorber), который может быть использован для извлечения абзацев из PDF-документов.

### Итерация по коллекции абзацев и получение их текста

```php

// Открыть существующий PDF файл
$document = new Document($inputFile);
// Создать экземпляр ParagraphAbsorber
$absorber = new ParagraphAbsorber();
$absorber->visit($document);
$responseData = "";

foreach ($absorber->getPageMarkups() as $markup) {
    $i = 1;

    foreach ($markup->getSections() as $section) {
        $j = 1;

        foreach ($section->getParagraphs() as $paragraph) {
            $paragraphText = "\r\n";

            foreach ($paragraph->getLines() as $line) {
                foreach ($line as $fragment) {
                    $paragraphText = $paragraphText . $fragment->getText();
                }
                $paragraphText = $paragraphText . "\r\n";
            }
            $paragraphText = $paragraphText . "\r\n";

            $responseData = $responseData . "Параграф " . $j++ . " секции " . $i++ . " на странице" . ":" . markup->getNumber();
            $responseData = $responseData . $paragraphText;
            $j++;
        }
        $i++;
    }
}

// Сохранить извлеченный текст в выходной файл.
file_put_contents($outputFile, $responseData);
```