---
title: Программное разделение PDF
linktitle: Разделение PDF файлов
type: docs
weight: 60
url: /php-java/split-document/
description: Эта тема показывает, как разделить страницы PDF на отдельные PDF файлы в ваших PHP приложениях.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Вы можете разделить PDF файлы с помощью Aspose.PDF и получить результаты онлайн по этой ссылке: [products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter)

{{% /alert %}}

Эта тема показывает, как разделить страницы PDF с помощью Aspose.PDF для PHP через Java на отдельные PDF файлы в ваших PHP приложениях. Чтобы разделить страницы PDF на файлы с одной страницей с использованием PHP, вы можете следовать следующим шагам:

1. Переберите страницы документа PDF через коллекцию [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection) объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. Для каждой итерации создайте новый объект Document и добавьте отдельный объект [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) в пустой документ.
1. Сохраните новый PDF, используя метод Save.

Следующий фрагмент кода PHP показывает, как разделить страницы PDF на отдельные PDF-файлы.

```php

    // Открыть документ
    $document = new Document($inputFile);
    $pages = $document->getPages();
    $pagesSize = java_values($pages->size());
       
    // Перебрать все страницы
    for ($pageCount = 1; $pageCount <= $pagesSize; $pageCount++) {
        $page = $pages->get_Item($pageCount);
        $newDocument = new Document();
        $newDocument->getPages()->add($page);
        $newDocument->save($outputFile . "page_" . $pageCount . ".pdf");
        $newDocument->close();
    }
    $document->close();
```