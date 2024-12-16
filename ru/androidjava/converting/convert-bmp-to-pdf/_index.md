---
title: Convert BMP to PDF 
linktitle: Convert BMP to PDF
type: docs
weight: 220
url: /ru/androidjava/convert-bmp-to-pdf/
lastmod: "2021-06-05"
description: Вы можете легко конвертировать BMP-файлы в PDF, используемые для хранения цифровых растровых изображений отдельно от устройства отображения, используя Aspose.PDF. для Android через Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

BMP-изображения — это файлы с расширением .BMP, представляющие файлы растровых изображений, которые используются для хранения цифровых растровых изображений. Эти изображения не зависят от графического адаптера и также называются форматом файла независимого от устройства растрового изображения (DIB).
Вы можете конвертировать BMP в PDF с помощью Aspose.PDF for Java API. Таким образом, вы можете следовать следующим шагам для преобразования BMP-изображений:

1. Инициализируйте новый документ
1. Загрузите образец BMP-файла
1. Наконец, сохраните выходной PDF-файл

Таким образом, следующий фрагмент кода следует этим шагам и показывает, как конвертировать BMP в PDF, используя Java:

```java
public void convertBMPtoPDF () {
        // Инициализируйте объект документа
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

        // Загрузите образец BMP-файла
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "BMP-to-PDF.pdf");

        // Сохраните выходной документ
        try {
            document.save(pdfFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```