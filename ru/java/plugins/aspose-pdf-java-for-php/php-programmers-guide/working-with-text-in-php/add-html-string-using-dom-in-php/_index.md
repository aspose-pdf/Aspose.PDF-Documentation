---
title: Добавить строку HTML с использованием DOM в PHP
linktitle: Добавить строку HTML с использованием DOM в PHP
type: docs
weight: 10
url: /ru/java/add-html-string-using-dom-in-php/
description: Изучите, как добавить HTML‑контент в PDF‑документ с помощью DOM в PHP с Aspose.PDF для создания богато оформленных документов.
lastmod: "2026-08-19"
---
## Aspose.PDF — Добавить HTML

Чтобы добавить строку HTML в PDF‑документ, используя **Aspose.PDF Java for PHP**, просто вызовите модуль **AddHtml**.

PHP‑код

```php
# Instantiate Document object
$doc = new Document();

# Add a page to pages collection of PDF file
$page = $doc->getPages()->add();

# Instantiate HtmlFragment with HTML contents
$title = new HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>");

# set MarginInfo for margin details
$margin = new MarginInfo();
$margin->setBottom(10);
$margin->setTop(200);

# Set margin information
$title->setMargin($margin);

# Add HTML Fragment to paragraphs collection of page
$page->getParagraphs()->add($title);

# Save PDF file
$doc->save($dataDir . "html.output.pdf");

print "HTML added successfully" . PHP_EOL;

```

**Загрузить исполняемый код**

СкачатьВ **Add HTML (Aspose.PDF)**В из любого из приведённых ниже сайтов для совместного программирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddHtml.php)


