---
title: Добавить номер страницы в PDF 
linktitle: Добавить номер страницы
type: docs
weight: 100
url: /php-java/add-page-number/
description: Aspose.PDF для PHP через Java позволяет добавить штамп номера страницы в ваш PDF файл, используя класс PageNumber Stamp.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Все документы должны иметь номера страниц. Номер страницы облегчает читателю поиск различных частей документа.
**Aspose.PDF для PHP через Java** позволяет добавить номера страниц с помощью PageNumberStamp.

{{% alert color="primary" %}}

Попробуйте онлайн. Вы можете проверить качество конвертации Aspose.PDF и просмотреть результаты онлайн по этой ссылке [products.aspose.app/pdf/page-number](https://products.aspose.app/pdf/page-number)

{{% /alert %}}

Вы можете использовать класс [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) для добавления штампа номера страницы в PDF документ.
 [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) класс предоставляет методы для создания штампа на основе номера страницы, такие как формат, поля, выравнивание, начальный номер и т.д. Чтобы добавить штамп с номером страницы, необходимо создать объект [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) и объект [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) с необходимыми текстовыми свойствами. После этого можно вызвать метод [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) класса [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page), чтобы добавить штамп в PDF файл. Также можно установить атрибуты шрифта для штампа номера страницы.

Следующий фрагмент кода показывает, как добавить номера страниц в PDF файл.

```php

    // Открыть документ
    $document = new Document($inputFile);

    // Создать штамп номера страницы
    $pageNumberStamp = new PageNumberStamp();

    // Является ли штамп фоновым
    $Center = (new HorizontalAlignment())->getCenter();
    $pageNumberStamp->setBackground(false);
    $pageNumberStamp->setFormat("Page # of " . $document->getPages()->size());
    $pageNumberStamp->setBottomMargin(10);
    $pageNumberStamp->setHorizontalAlignment($Center);
    $pageNumberStamp->setStartingNumber(1);

    $fontRepository = new FontRepository();
    // Установить текстовые свойства
    $pageNumberStamp->getTextState()->setFont($fontRepository->findFont("Arial"));
    $pageNumberStamp->getTextState()->setFontSize(14.0);
    $pageNumberStamp->getTextState()->setFontStyle(FontStyles::$Bold);
    $pageNumberStamp->getTextState()->setForegroundColor((new Color())->getAqua());

    // Добавить штамп на конкретную страницу
    $document->getPages()->get_Item(1)->addStamp($pageNumberStamp);

    // Сохранить выходной документ
    $document->save($outputFile);
    $document->close();
```