---
title: Добавить текст в существующий PDF‑файл в PHP
linktitle: Добавить текст в существующий PDF‑файл в PHP
type: docs
weight: 20
url: /ru/java/add-text-to-an-existing-pdf-file-in-php/
description: Узнайте, как добавить новый текст в существующий PDF‑документ в PHP с помощью Aspose.PDF для улучшения содержимого.
lastmod: "2026-08-19"
---
## Aspose.PDF - Добавить текст

Чтобы добавить строку текста в документ PDF, используя **Aspose.PDF Java for PHP**, просто вызовите модуль **AddText**.

PHP‑код

```php

# Instantiate Document object
$doc = new Document($dataDir . 'input1.pdf');

# get particular page
$pdf_page = $doc->getPages()->get_Item(1);

# create text fragment
$text_fragment = new TextFragment("main text");
$text_fragment->setPosition(new Position(100, 600));

$font_repository = new FontRepository();
$color = new Color();

# set text properties
$text_fragment->getTextState()->setFont($font_repository->findFont("Verdana"));
$text_fragment->getTextState()->setFontSize(14);

# create TextBuilder object
$text_builder = new TextBuilder($pdf_page);

# append the text fragment to the PDF page
$text_builder->appendText($text_fragment);

# Save PDF file
$doc->save($dataDir . "Text_Added.pdf");

print "Text added successfully" . PHP_EOL;

```

**Скачать выполняемый код**

Загрузить **Add Text (Aspose.PDF)** из любого из указанных ниже сайтов для совместного программирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddText.php)


