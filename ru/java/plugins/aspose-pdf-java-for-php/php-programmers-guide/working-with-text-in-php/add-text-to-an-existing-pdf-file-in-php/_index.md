---
title: Добавить текст в существующий PDF файл на PHP
type: docs
weight: 20
url: ru/java/add-text-to-an-existing-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Добавление текста

Чтобы добавить текстовую строку в PDF документ с использованием **Aspose.PDF Java for PHP**, просто вызовите модуль **AddText**.

PHP Код

```php

# Создать объект Document
$doc = new Document($dataDir . 'input1.pdf');

# получить конкретную страницу
$pdf_page = $doc->getPages()->get_Item(1);

# создать текстовый фрагмент
$text_fragment = new TextFragment("основной текст");
$text_fragment->setPosition(new Position(100, 600));

$font_repository = new FontRepository();
$color = new Color();

# установить свойства текста
$text_fragment->getTextState()->setFont($font_repository->findFont("Verdana"));
$text_fragment->getTextState()->setFontSize(14);

# создать объект TextBuilder
$text_builder = new TextBuilder($pdf_page);

# добавить текстовый фрагмент на страницу PDF
$text_builder->appendText($text_fragment);

# Сохранить PDF файл
$doc->save($dataDir . "Text_Added.pdf");

print "Текст успешно добавлен" . PHP_EOL;

```


**Скачать Выполняемый Код**

Скачайте **Добавить текст (Aspose.PDF)** с любого из нижеупомянутых социальных сайтов для разработчиков:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddText.php)