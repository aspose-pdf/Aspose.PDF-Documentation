---
title: Удаление страниц PDF программно 
linktitle: Удаление страниц PDF
type: docs
weight: 40
url: /java/delete-pages/
description: Вы можете удалить страницы из вашего PDF-файла, используя Java-библиотеку.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Вы можете удалить страницы из PDF-файла, используя Aspose.PDF для Java. Чтобы удалить конкретную страницу из [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection), просто вызовите метод delete() и укажите индекс конкретной страницы, которую хотите удалить. Затем вызовите метод save, чтобы сохранить обновленный PDF-файл.

## Удаление страницы из PDF-файла

1. Вызовите метод Delete и укажите индекс страницы
1. Вызовите метод Save, чтобы сохранить обновленный PDF-файл

Следующий фрагмент кода показывает, как удалить конкретную страницу из PDF-файла с использованием Java.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleDeletePage {

  private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

  public static void DeletePageFromPDFFile() {

    // Открыть документ
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Удалить конкретную страницу
    pdfDocument.getPages().delete(2);

    _dataDir = _dataDir + "DeleteParticularPage_out.pdf";
    // Сохранить обновленный PDF
    pdfDocument.save(_dataDir);    

  }
```