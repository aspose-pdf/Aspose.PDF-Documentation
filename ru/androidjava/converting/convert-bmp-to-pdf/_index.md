---
title: Конвертировать BMP в PDF
linktitle: Конвертировать BMP в PDF
type: docs
weight: 220
url: /ru/androidjava/convert-bmp-to-pdf/
lastmod: "2026-07-01"
description: Вы можете легко конвертировать BMP‑bitmap‑файлы в PDF, используемый для хранения цифровых bitmap‑изображений отдельно от устройства отображения, используя Aspose.PDF для Android через Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

BMP‑изображения — это файлы с расширением .BMP, представляющие файлы Bitmap Image, которые используются для хранения цифровых bitmap‑изображений. Эти изображения независимы от графического адаптера и также называются форматом файлов device independent bitmap (DIB).
Вы можете конвертировать BMP в PDF с помощью Aspose.PDF for Java API. Поэтому вы можете выполнить следующие шаги для конвертации BMP‑изображений:

1. Инициализировать новый Document
1. Загрузите пример BMP‑изображения
1. Наконец, сохраните выходной PDF-файл

Таким образом, следующий фрагмент кода следует этим шагам и показывает, как преобразовать BMP в PDF с использованием Java:

```java
public void convertBMPtoPDF () {
        // Initialize document object
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/sample.bmp");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Load sample BMP image file
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "BMP-to-PDF.pdf");

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


