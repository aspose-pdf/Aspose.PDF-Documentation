---
title: Добавить фон в PDF
linktitle: Добавить фоны
type: docs
weight: 110
url: /java/add-backgrounds/
descriptions: Добавьте фоновое изображение в ваш PDF файл с помощью Java. Используйте объект BackgroundArtifact.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Фоновые изображения могут использоваться для добавления водяного знака или другого тонкого дизайна к документам. В Aspose.PDF для Java каждый PDF документ является коллекцией страниц, и каждая страница содержит коллекцию артефактов. Класс [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/BackgroundArtifact) может использоваться для добавления фонового изображения к объекту страницы.

Следующий фрагмент кода показывает, как добавить фоновое изображение к страницам PDF с использованием объекта BackgroundArtifact на Java.

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;

import com.aspose.pdf.BackgroundArtifact;
import com.aspose.pdf.Document;
import com.aspose.pdf.Page;

public class ExampleAddBackground {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void InsertEmptyPageInPDFFileAtDesiredLocation() throws FileNotFoundException {
        // Для полных примеров и файлов данных, пожалуйста, перейдите на
        // https://github.com/aspose-pdf/Aspose.Pdf-for-Java
        String myDir = "";
        // Создайте новый объект Document
        Document doc = new Document();
        // Добавьте новую страницу к объекту документа
        Page page = doc.getPages().add();
        // Создайте объект BackgroundArtifact
        BackgroundArtifact background = new BackgroundArtifact();
        // Укажите изображение для объекта backgroundartifact
        background.setBackgroundImage(new FileInputStream(myDir + "logo.png"));
        // Добавьте backgroundartifact в коллекцию артефактов страницы
        page.getArtifacts().add(background);
        // Сохраните документ
        doc.save(_dataDir + "BackGround.pdf");
    }
}
```