---
title: Добавить страницы в PDF
linktitle: Добавить страницы
type: docs
weight: 10
url: /java/add-pages/
description: Эта статья учит, как вставить (добавить) страницу в нужное место PDF файла. Узнайте, как перемещать, удалять (удалять) страницы из PDF файла с помощью Java библиотеки.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Добавить или вставить страницу в PDF файл

Aspose.PDF для Java позволяет вставить страницу в PDF документ в любом месте файла, а также добавить страницы в конец PDF файла. Вам нужно передать место, куда вы хотите вставить пустую страницу, в метод вставки.
Этот раздел показывает, как добавить страницы в PDF с помощью Aspose.PDF для Java.

### Вставить пустую страницу в PDF файл в нужное место

Следующий фрагмент кода показывает, как вставить пустую страницу в PDF файл:

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) с входным PDF файлом.

1. Вызовите метод Insert коллекции [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection) с указанным индексом.
1. Сохраните выходной PDF, используя метод Save.

Следующий фрагмент кода показывает, как вставить страницу в PDF файл.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleAddPages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void InsertEmptyPageInPDFFileAtDesiredLocation() {
        Document document = new Document();

        // Добавить страницу
        document.getPages().add();

        // Вставить пустую страницу в PDF
        document.getPages().insert(2);

        // Сохранить обновленный PDF
        document.save(_dataDir + "InsertEmptyPage_out.pdf");
    }
```

В приведенном выше примере мы добавили пустую страницу с параметрами по умолчанию. Если вам нужно сделать размер страницы таким же, как и у другой страницы в документе, вам следует добавить
несколько строк кода:

```java
    public static void InsertEmptyPageInPDFFileAtDesiredLocation01() {
        Document document = new Document();

        // Добавить страницу
        Page page1 = document.getPages().add();

        // Вставить пустую страницу в PDF
        Page page2 = document.getPages().insert(2);
        ;
        // скопировать параметры страницы из страницы 1
        page2.setArtBox(page1.getArtBox());
        page2.setBleedBox(page1.getBleedBox());
        page2.setCropBox(page1.getCropBox());
        page2.setMediaBox(page1.getMediaBox());
        page2.setTrimBox(page1.getTrimBox());

        // Сохранить обновленный PDF
        document.save(_dataDir + "InsertEmptyPage_out.pdf");
    }
```


### Добавить пустую страницу в конец PDF файла

Иногда необходимо убедиться, что документ заканчивается на пустой странице. Эта тема объясняет, как вставить пустую страницу в конец PDF документа.

Чтобы вставить пустую страницу в конец PDF файла:

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) с входным PDF файлом.
1. Вызовите метод Add коллекции [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection) без параметров.
1. Сохраните выходной PDF, используя метод Save.

Следующий фрагмент кода показывает, как вставить пустую страницу в конец PDF файла.

```java
public static void AddAnEmptyPageAtTheEndOfAPDFFile() {

        Document document = new Document();
        // Добавить страницу
        document.getPages().add();

        // Вставить пустую страницу в конец PDF файла
        document.getPages().add();

        // Сохранить обновленный PDF
        document.save(_dataDir + "InsertEmptyPageAtEnd_out.pdf");
    }

}
```