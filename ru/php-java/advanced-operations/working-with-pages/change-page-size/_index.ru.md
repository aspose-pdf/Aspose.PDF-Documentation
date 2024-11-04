---
title: Изменение размера страницы PDF программно
linktitle: Изменение размера страницы PDF
type: docs
weight: 50
url: /php-java/change-page-size/
description: Измените размер страницы в вашем PDF-файле с помощью PHP.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Изменение размера страницы PDF

Aspose.PDF для PHP через Java позволяет изменять размер страницы PDF с помощью простых строк кода в ваших Java-приложениях. Эта тема объясняет, как обновить/изменить размеры страницы существующего PDF-файла.

Класс [Page](https://reference.aspose.com/pdf//java/com.aspose.pdf/page) содержит метод SetPageSize(...), который позволяет установить размер страницы. Пример кода ниже обновляет размеры страницы за несколько простых шагов:

1. Загрузите исходный PDF-файл.
1. Получите страницы в объект [pageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection).
1. Получите заданную страницу.
1. Вызовите метод setPageSize(..), чтобы обновить её размеры.

1. Вызовите метод save(..) класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) для создания PDF-файла с обновленными размерами страниц.

Следующий фрагмент кода показывает, как изменить размеры страницы PDF на размер A4.

```php

    // Открыть документ
    $document = new Document($inputFile);
      
    // Получить коллекцию страниц
    $pageCollection = $document->getPages();

    // Получить конкретную страницу
    $page = $pageCollection->get_Item(1);

    // Установить размер страницы как A4 (11.7 x 8.3 дюймов) и в Aspose.Pdf, 1 дюйм = 72 точки
    // Так что размеры A4 в точках будут (842.4, 597.6)
    $page.setPageSize(597.6, 842.4);

    // Сохранить выходной документ
    $document->save($outputFile);
    $document->close();
```

## Получить размер страницы PDF

Вы можете прочитать размер страницы PDF существующего PDF-файла, используя Aspose.PDF для PHP через Java. Следующий пример кода показывает, как прочитать размеры страницы PDF, используя PHP.

```php

    // Открыть документ
    $document = new Document($inputFile);
      
    // Добавить пустую страницу в PDF-документ
    $page = $document->getPages()->size() > 0 
        ? $document->getPages()->get_Item(1) 
        : $document->getPages()->add();
    
    // Получить информацию о высоте и ширине страницы
    $responseData = $page->getPageRect(true)->getWidth() . ":" . $page->getPageRect(true)->getHeight();
    
    // Повернуть страницу на угол 90 градусов
    $rotation = new Rotation();
    $page->setRotate($rotation->getOn90());

    // Получить информацию о высоте и ширине страницы
    $responseData = $responseData . $page->getPageRect(true)->getWidth() . ":" . $page->getPageRect(true)->getHeight();
    
    // Сохранить выходной документ
    $document->save($outputFile);
    $document->close();
```