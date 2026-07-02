---
title: Преобразовать JPG в PDF
linktitle: Преобразовать JPG в PDF
type: docs
weight: 190
url: /ru/androidjava/convert-jpg-to-pdf/
lastmod: "2026-07-01"
description: Узнайте, как легко конвертировать изображения JPG в файл PDF. Кроме того, вы можете конвертировать изображение в PDF с теми же высотой и шириной страницы.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Не нужно задаваться вопросом, как конвертировать JPG в PDF, потому что библиотека Apose.PDF for Android via Java предлагает лучшее решение.

Вы можете очень легко конвертировать изображения JPG в PDF с помощью Aspose.PDF for Android via Java, следуя этим шагам:

1. Инициализировать объект [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) класс
1. Загрузите JPG изображение и добавить в абзац
1. Сохраните выходной PDF

Приведённый ниже фрагмент кода показывает, как преобразовать JPG изображение в PDF:

```java
public void convertJPEGtoPDF () {
        // Initialize document object
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

        // Load sample JPEG image file
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "JPEG-to-PDF.pdf");

        // Save output document
        try {
            document.save(pdfFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

