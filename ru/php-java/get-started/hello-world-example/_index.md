---
title: Пример Hello World PHP через Java
linktitle: Пример Hello World
type: docs
weight: 40
url: ru/php-java/hello-world-example/
description: Эта страница показывает, как использовать простое программирование для создания PDF-документа с текстом - Hello World с использованием Aspose.PDF для PHP через Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Пример Hello World

Пример «Hello World» обычно используется для демонстрации основных возможностей языка программирования или программного обеспечения с простым вариантом использования.

Aspose.PDF для PHP через Java API позволяет разработчикам создавать, читать, редактировать и обрабатывать PDF-файлы в своих Java-приложениях. Он поддерживает чтение и конвертацию различных типов файлов в формат PDF и обратно. Эта статья Hello World показывает, как создать PDF-файл с использованием Aspose.PDF для PHP через Java API. После [установки Aspose.PDF для PHP через Java](/pdf/php-java/installation/) в вашей среде вы можете выполнить приведенный ниже пример кода, чтобы увидеть, как работает API Aspose.PDF.

Приведенный ниже фрагмент кода выполняет следующие шаги:


1. Создайте объект [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document)
1. Добавьте [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/page) к объекту документа
1. Создайте объект [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment)
1. Добавьте TextFragment в коллекцию [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) страницы
1. Сохраните полученный PDF-документ

Следующий фрагмент кода - это программа Hello World, демонстрирующая работу Aspose.PDF для PHP через Java API.

```php
    $document = new Document();    
    $page = $document->getPages()->add();
    $textFragment = new TextFragment("Hello World!");    
    $page->getParagraphs()->add($textFragment);
    $document->save($outputFile);
```