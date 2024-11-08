---
title: Объединение PDF программно
linktitle: Объединение файлов PDF
type: docs
weight: 50
url: /ru/php-java/merge-pdf-documents/
description: Эта страница объясняет, как объединить PDF-документы в один PDF файл с использованием PHP.
lastmod: "2024-06-05"
---

Теперь объединение PDF файлов является одной из самых востребованных задач.
Эта статья показывает, как объединить несколько PDF файлов в один PDF документ с использованием Aspose.PDF для PHP через Java. Пример написан на Java, но API может быть использован и в других языках программирования. PDF файлы объединяются таким образом, что первый присоединяется в конец другого документа.

## Объединение файлов PDF с использованием PHP

{{% alert color="primary" %}}

Вы можете объединить файлы PDF, используя Aspose.PDF и получить результаты онлайн по этой ссылке: [Merger](https://products.aspose.app/pdf/merger)

{{% /alert %}}

Для объединения двух PDF файлов:

1. Создайте два объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document), каждый из которых содержит один из входных PDF файлов.

1. Затем вызовите метод Add коллекции [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection) для объекта Document, к которому вы хотите добавить другой PDF-файл.
1. Передайте коллекцию PageCollection второго объекта Document в метод Add первой коллекции PageCollection.
1. Наконец, сохраните выходной PDF-файл, используя метод Save.

Следующий фрагмент кода показывает, как объединять PDF-файлы с использованием PHP.

```php
    // Открыть первый документ
    $document1 = new Document($inputFile1);
    
    // Открыть второй документ
    $document2 = new Document($inputFile2);

    // Добавить страницы второго документа к первому
    $document1->getPages()->add($document2->getPages());

    // Сохранить объединенный выходной файл
    $document1->save($outputFile);
    $document1->close();
    $document2->close();
```