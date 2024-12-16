---
title: Добавить страницы в PDF
linktitle: Добавить страницы
type: docs
weight: 10
url: /ru/php-java/add-pages/
description: Эта статья обучает, как вставить (добавить) страницу в нужное место в PDF файле. Узнайте, как перемещать, удалять (удалять) страницы из PDF файла с использованием PHP.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Добавление или вставка страницы в PDF файл

Aspose.PDF для PHP через Java позволяет вставлять страницу в PDF документ в любом месте файла, а также добавлять страницы в конец PDF файла. Вам нужно передать место, куда вы хотите вставить пустую страницу, в метод вставки.
Этот раздел показывает, как добавлять страницы в PDF с помощью Aspose.PDF для PHP через Java.

### Вставка пустой страницы в PDF файл в нужное место

Следующий фрагмент кода показывает, как вставить пустую страницу в PDF файл:

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) с входным PDF файлом.
2. Добавьте страницу и вставьте её в PDF.

1. Сохраните выходной PDF, используя метод Save.

Следующий фрагмент кода показывает, как вставить страницу в PDF-файл.

```php

    // Открыть документ
    $document = new Document($inputFile);

    // Добавить страницу
    $document->getPages()->add();

    // Вставить пустую страницу в PDF
    $document->getPages()->insert(2);

    // Сохранить выходной документ
    $document->save($outputFile);
    $document->close();
```

В примере выше мы добавили пустую страницу с параметрами по умолчанию. Если вам нужно сделать размер страницы таким же, как у другой страницы в документе, следует добавить несколько строк кода:

```php

    // Открыть документ
    $document = new Document($inputFile);

    // Добавить страницу
    $page1 = $document->getPages()->add();

    // Вставить пустую страницу в PDF
    $page2 = $document->getPages()->insert(2);

    // скопировать параметры страницы с первой страницы
    $page2->setCropBox($page1->getCropBox());
    $page2->setMediaBox($page1->getMediaBox());
    $page2->setTrimBox($page1->getTrimBox());
    $page2->setArtBox($page1->getArtBox());
    $page2->setBleedBox($page1->getBleedBox());
    
    // Сохранить выходной документ
    $document->save($outputFile);
    $document->close();
```


### Добавить пустую страницу в конец файла PDF

Иногда требуется, чтобы документ заканчивался пустой страницей. Эта тема объясняет, как вставить пустую страницу в конец PDF-документа.

Чтобы вставить пустую страницу в конец PDF-файла:

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) с входным PDF-файлом.
1. Добавьте страницу и вставьте её в PDF.
1. Сохраните выходной PDF, используя метод save.

Следующий фрагмент кода показывает, как вставить пустую страницу в конец PDF-файла.

```php

    // Открыть документ
    $document = new Document($inputFile);

    // Добавить страницу
    $document->getPages()->add();

    // Вставить пустую страницу в PDF
    $document->getPages()->insert(2);

    // Сохранить выходной документ
    $document->save($outputFile);
    $document->close();
```