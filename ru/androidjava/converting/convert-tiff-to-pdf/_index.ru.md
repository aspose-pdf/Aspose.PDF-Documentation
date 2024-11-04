---
title: Convert TIFF to PDF 
linktitle: Convert TIFF to PDF
type: docs
weight: 210
url: /androidjava/convert-tiff-to-pdf/
lastmod: "2021-06-05"
description: Aspose.PDF for Android via Java позволяет конвертировать многостраничные или многокадровые изображения TIFF в приложения PDF.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Android via Java** поддерживает формат файла, будь то однофреймовое или многофреймовое изображение <abbr title="Tag Image File Format">TIFF</abbr>. Это означает, что вы можете конвертировать изображение TIFF в PDF в своих Java-приложениях.

TIFF или TIF, Tagged Image File Format, представляет растровые изображения, предназначенные для использования на различных устройствах, соответствующих этому стандарту формата файла.
 TIFF изображение может содержать несколько кадров с различными изображениями. Формат файла Aspose.PDF также поддерживается, будь то одно- или многокадровое TIFF изображение. Таким образом, вы можете конвертировать TIFF изображение в PDF в ваших Java приложениях. Поэтому мы рассмотрим пример конвертации многостраничного TIFF изображения в многостраничный PDF документ с использованием следующих шагов:

1. Создайте экземпляр класса Document
1. Загрузите входное TIFF изображение
1. Получите FrameDimension кадров
1. Добавьте новую страницу для каждого кадра
1. Наконец, сохраните изображения на страницах PDF

Более того, следующий фрагмент кода показывает, как конвертировать многостраничное или многокадровое TIFF изображение в PDF:

```java
 public void convertTIFFtoPDF () {
        // Инициализировать объект документа
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/sample.tiff");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Загрузить пример файла TIFF изображения
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "TIFF-to-PDF.pdf");

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