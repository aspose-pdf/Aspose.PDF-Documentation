---
title: Конвертировать JPG в PDF 
linktitle: Конвертировать JPG в PDF 
type: docs
weight: 190
url: /androidjava/convert-jpg-to-pdf/
lastmod: "2021-06-05"
description: Узнайте, как легко конвертировать JPG изображения в PDF файл. Также вы можете конвертировать изображение в PDF с такой же высотой и шириной страницы.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Не нужно задумываться, как конвертировать JPG в PDF, потому что библиотека Apose.PDF для Android через Java имеет лучшее решение.

Вы можете очень легко конвертировать JPG изображения в PDF с помощью Aspose.PDF для Android через Java, следуя следующим шагам:

1. Инициализируйте объект класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)
1. Загрузите JPG изображение и добавьте в абзац
1. Сохраните выходной PDF

Пример кода ниже показывает, как конвертировать JPG изображение в PDF:

```java
public void convertJPEGtoPDF () {
        // Инициализировать объект документа
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/sample.jpg");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Загрузить образец JPEG файла изображения
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "JPEG-to-PDF.pdf");

        // Сохранить выходной документ
        try {
            document.save(pdfFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```