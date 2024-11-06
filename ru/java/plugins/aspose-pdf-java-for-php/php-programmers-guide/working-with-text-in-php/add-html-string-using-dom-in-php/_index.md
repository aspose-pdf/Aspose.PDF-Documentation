---
title: Добавить строку HTML с использованием DOM в PHP
type: docs
weight: 10
url: ru/java/add-html-string-using-dom-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Добавить HTML

Чтобы добавить HTML строку в Pdf документ, используя **Aspose.PDF Java для PHP**, просто вызовите модуль **AddHtml**.

PHP Код

```php
# Создать объект Document
$doc = new Document();

# Добавить страницу в коллекцию страниц PDF файла
$page = $doc->getPages()->add();

# Создать HtmlFragment с HTML содержимым
$title = new HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>");

# установить MarginInfo для деталей полей
$margin = new MarginInfo();
$margin->setBottom(10);
$margin->setTop(200);

# Установить информацию о полях
$title->setMargin($margin);

# Добавить HTML Фрагмент в коллекцию абзацев страницы
$page->getParagraphs()->add($title);

# Сохранить PDF файл
$doc->save($dataDir . "html.output.pdf");

print "HTML успешно добавлен" . PHP_EOL;

```

**Загрузить работающий код**

Скачайте **Add HTML (Aspose.PDF)** с любого из указанных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddHtml.php)