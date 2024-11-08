---
title: Перемещение страниц PDF
linktitle: Перемещение страниц PDF
type: docs
weight: 20
url: /ru/php-java/move-pages/
description: Попробуйте переместить страницы в нужное место или в конец файла PDF с помощью Aspose.PDF для PHP через Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Перемещение страницы из одного PDF документа в другой

Эта тема объясняет, как переместить страницу из одного PDF документа в конец другого документа с использованием PHP. Чтобы переместить страницу, мы должны:

1. Создать объект класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) с исходным файлом PDF
1. Создать объект класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) с файлом назначения PDF
1. Добавить страницу в выходной документ. Сохраните выходной файл
1. Удалить страницу из входного документа. Сохраните измененный входной документ
1. Закрыть документы
1. Сохранить и закрыть выходной документ

Следующий фрагмент кода показывает, как переместить одну страницу.

```php

    // Открыть документ
    $document = new Document($inputFile1);
    $dstDocument = new Document($outputFile);
    
    $page = $document->getPages()->get_Item(2);
    $dstDocument->getPages()->add($page);

    // Сохранить выходной файл
    $dstDocument->save($srcFileName);
    $document->getPages()->delete(2);
    $document->save($dstFileName);
    $document->close();
    $dstDocument->close();
  
    // Сохранить выходной документ
    $document->save($outputFile);
    $document->close();
```


## Перемещение группы страниц из одного PDF документа в другой

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) с исходным PDF файлом.
1. Создайте объект класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) с целевым PDF файлом.
1. Определите страницы, которые нужно скопировать из входного документа в выходной документ.
1. Выполните цикл по массиву:
    1. Получите страницу по указанному индексу из входного документа.
    1. Добавьте страницу в целевой документ.
1. Сохраните выходной PDF, используя метод Save.
1. Удалите страницу в исходном документе, используя массив.
1. Сохраните исходный PDF, используя метод Save.

Следующий фрагмент кода показывает, как вставить пустую страницу в конец PDF файла.

```php

    // Открыть документ
    $document = new Document($inputFile1);
    $dstDocument = new Document($outputFile);
    
    $pages = [1, 3 ];
    foreach ($pages as $pageIndex) {
      $page = $document->getPages()->get_Item($pageIndex);
      $dstDocument->getPages()->add(page);
    }
    // Сохранить выходные файлы
    $dstDocument->save($srcFileName);
    $document->getPages()->delete($pages);

    $document->save(dstFileName);

    $document->close();
    $dstDocument->close();  
```


## Перемещение страницы в новое местоположение в текущем PDF-документе

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) с исходным PDF-файлом.
1. Получите страницу из коллекции [pageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection).
1. Добавьте страницу в новое местоположение.
1. Удалите страницу на индексе 2.
1. Сохраните выходной PDF, используя метод save.

```php

    // Открыть документ
    $document = new Document($inputFile);
        
    $pageCollection = $document->getPages();
    
    $page = $pageCollection->get_Item(2);
    $pageCollection->add(page);
    $pageCollection->delete(2);

    // Сохранить выходной файл
    $document->save($outputFile);
    $document->close();      
```