---
title: Перемещение страниц PDF
linktitle: Перемещение страниц
type: docs
weight: 20
url: /ru/java/move-pages/
description: Попробуйте переместить страницы в нужное место или в конец PDF файла, используя Aspose.PDF для Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Перемещение страницы из одного PDF документа в другой

Эта тема объясняет, как переместить страницу из одного PDF документа в конец другого документа, используя Java.
Чтобы переместить страницу, необходимо:

1. Создать объект класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) с исходным PDF файлом.
1. Создать объект класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) с целевым PDF файлом.
1. Получить страницу из коллекции [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection).
1. Добавить страницу в целевой документ.
1. Сохранить выходной PDF, используя метод Save.
1. Удалить страницу в исходном документе.
1. Сохранить исходный PDF, используя метод Save.

Следующий фрагмент кода показывает, как переместить одну страницу.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleMovePDFPages {

  private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

  public static void MovePage() {
    String srcFileName = _dataDir + "<enter file name>";
    String dstFileName = _dataDir + "<enter file name>";
    Document srcDocument = new Document();
    Document dstDocument = new Document();
    Page page = srcDocument.getPages().get_Item(2);
    dstDocument.getPages().add(page);
    // Сохранить выходной файл
    dstDocument.save(srcFileName);
    srcDocument.getPages().delete(2);
    srcDocument.save(dstFileName);
  }
```

## Перемещение группы страниц из одного PDF документа в другой

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) с исходным PDF файлом.
1. Создайте объект класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) с целевым PDF файлом.
1. Определите массив с номерами страниц, которые необходимо переместить.

1. Запустите цикл по массиву:
    1. Получите страницу из коллекции [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection).
    1. Добавьте страницу в целевой документ.
1. Сохраните выходной PDF, используя метод Save.
1. Удалите страницу в исходном документе, используя массив.
1. Сохраните исходный PDF, используя метод Save.

Следующий фрагмент кода показывает, как вставить пустую страницу в конец PDF файла.

```java
  public static void MoveBunchPages() {
    String srcFileName = _dataDir + "<enter file name>";
    String dstFileName = _dataDir + "<enter file name>";
    Document srcDocument = new Document(srcFileName);
    Document dstDocument = new Document();

    Integer[] pages = { 1, 3 };
    for (int pageIndex : pages) {
      Page page = srcDocument.getPages().get_Item(pageIndex);
      dstDocument.getPages().add(page);
    }
    // Сохраните выходные файлы
    dstDocument.save(srcFileName);
    srcDocument.getPages().delete(pages);

    srcDocument.save(dstFileName);
  }
```

## Перемещение страницы в новое местоположение в текущем PDF документе

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) с исходным PDF файлом.
1. Получите страницу из коллекции [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection).
1. Добавьте страницу в новое место (например, в конец).
1. Удалите страницу в предыдущем месте.
1. Сохраните итоговый PDF, используя метод Save.

```java
  public static void MovePagesInOnePDF() {
    String srcFileName = _dataDir + "<enter file name>";
    String dstFileName = _dataDir + "<enter file name>";

    Document srcDocument = new Document(srcFileName);
    Page page = srcDocument.getPages().get_Item(2);
    srcDocument.getPages().add(page);
    srcDocument.getPages().delete(2);

    // Сохраните выходной файл
    srcDocument.save(dstFileName);
  }
}
```