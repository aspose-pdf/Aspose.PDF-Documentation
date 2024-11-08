---
title: Создание сложного PDF
linktitle: Создание сложного PDF
type: docs
weight: 60
url: /ru/php-java/complex-pdf-example/
description: Aspose.PDF для PHP через Java позволяет создавать более сложные документы, содержащие изображения, текстовые фрагменты и таблицы в одном документе.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Пример [Hello, World](/pdf/ru/php-java/hello-world-example/) показал простые шаги создания PDF-документа с использованием Aspose.PDF. В этой статье мы рассмотрим создание более сложного документа с Aspose.PDF для PHP через Java. В качестве примера мы возьмем документ от вымышленной компании, которая занимается пассажирскими паромными перевозками.

Если мы создаем документ с нуля, нам нужно следовать определенным шагам:

1. Создайте объект [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document). На этом этапе мы создадим пустой PDF-документ с некоторыми метаданными, но без страниц.

1. Добавьте [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page) в объект документа. Теперь наш документ будет иметь одну страницу.
1. Добавьте [Image](https://reference.aspose.com/pdf/java/com.aspose.pdf/image). Это сложная операция, основанная на низкоуровневых действиях с операторами PDF.
    - Загрузите изображение из потока
    - Добавьте изображение в коллекцию Images ресурсов страницы
    - Использование оператора GSave: этот оператор сохраняет текущее состояние графики.
    - Создайте объект [Matrix](https://reference.aspose.com/pdf/java/com.aspose.pdf/matrix/).
    - Использование оператора ConcatenateMatrix: определяет, как изображение должно быть размещено.
    - Использование оператора Do: этот оператор рисует изображение.
    - Использование оператора GRestore: этот оператор восстанавливает состояние графики.
1. Создайте [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) для заголовка. Для заголовка мы будем использовать шрифт Arial с размером 24pt и выравниванием по центру.

1. Добавьте заголовок на страницу [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--).
1. Создайте [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) для описания. Для описания мы будем использовать шрифт Arial размером 24pt и выравнивание по центру.
1. Добавьте (описание) к абзацам страницы.
1. Создайте таблицу, добавьте свойства таблицы.
1. Добавьте (таблицу) к абзацам страницы [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--).
1. Сохраните документ "Complex.pdf".

```php

    $document = new Document();
    //Добавить страницу
    $page = $document->getPages()->add();
    // -------------------------------------------------------------
    // Добавить изображение
    $imageFileName = $dataDir . DIRECTORY_SEPARATOR . 'logo.png';
    $page->AddImage($imageFileName, new Rectangle(20, 730, 120, 830));

    // -------------------------------------------------------------
    // Добавить заголовок
    $fontRepository = new FontRepository();
    $fontArial = $fontRepository->findFont("Arial");

    $header = new TextFragment("Новые паромные маршруты осенью 2020 года");
    $header->getTextState()->setFont($fontArial);
    $header->getTextState()->setFontSize(24);
    $header->setHorizontalAlignment(2);
    $header->setPosition(new Position(130, 720));
    $page->getParagraphs()->add($header);

    // Добавить описание
    $descriptionText = "Посетители должны покупать билеты онлайн, и количество билетов ограничено до 5000 в день. Паромное сообщение работает с половинной вместимостью и по сокращенному расписанию. Ожидайте очередей.";
    $description = new TextFragment($descriptionText);
    $description->getTextState()->setFont($fontRepository->findFont("Times New Roman"));
    $description->getTextState()->setFontSize(14);
    $header->setHorizontalAlignment(1);
    $page->getParagraphs()->add($description);

    // Добавить таблицу
    $table = new Table();
    $table->setColumnWidths("200");

    $colors = new Color();
    $darkSlateGrayColor = $colors->getDarkSlateGray();
    $blackColor = $colors->getBlack();
    $grayColor = $colors->getGray();
    $whiteSmokeColor = $colors->getWhiteSmoke();

    $table->setBorder(new BorderInfo(BorderSide::$Box, 1.0, $darkSlateGrayColor));
    $table->setDefaultCellBorder(new BorderInfo(BorderSide::$Box, 0.5, $blackColor));
    $table->getMargin()->setBottom(10);
    $table->getDefaultCellTextState()->setFont($fontRepository->findFont("Helvetica"));

    $headerRow = $table->getRows()->add();

    $headerRowCell = $headerRow->getCells()->add("Отправление из города");
    $headerRowCell->setBackgroundColor($grayColor);
    $headerRowCell->getDefaultCellTextState()->setForegroundColor($whiteSmokeColor);

    $headerRowCell = $headerRow->getCells()->add("Отправление с острова");
    $headerRowCell->setBackgroundColor($grayColor);
    $headerRowCell->getDefaultCellTextState()->setForegroundColor($whiteSmokeColor);

    $timenow = new DateTime('06:00');

    for ($i = 0; $i < 10; $i++) {
        $dataRow = $table->getRows()->add();
        $cell = $dataRow->getCells()->add($timenow->format('H:i'));
        $timenow->add(new DateInterval('PT30M'));
        $dataRow->getCells()->add($timenow->format('H:i'));
    }

    $page->getParagraphs()->add($table);

    $document->save($outputFile);
```