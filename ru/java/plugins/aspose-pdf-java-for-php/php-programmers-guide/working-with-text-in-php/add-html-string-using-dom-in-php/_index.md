---
title: Добавьте строку HTML, используя DOM в PHP
linktitle: Добавьте строку HTML, используя DOM в PHP
type: docs
weight: 10
url: /java/add-html-string-using-dom-in-php/
description: Узнайте, как добавить HTML-содержимое в PDF-документ с помощью DOM в PHP с помощью Aspose.PDF для создания расширенных документов.
lastmod: "2026-06-09"
---
## Aspose.PDF — Добавить HTML

Чтобы добавить строку HTML в документ PDF с помощью **Aspose.PDF Java для PHP**, просто вызовите модуль **AddHtml**.

PHP-код

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

**Загрузить рабочий код**

Загрузите **Добавьте HTML (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddHtml.php)
