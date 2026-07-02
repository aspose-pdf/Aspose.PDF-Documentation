---
title: Конвертировать TIFF в PDF
linktitle: Конвертировать TIFF в PDF
type: docs
weight: 210
url: /ru/androidjava/convert-tiff-to-pdf/
lastmod: "2026-07-01"
description: Aspose.PDF for Android via Java позволяет конвертировать многостраничные или многокадровые изображения TIFF в PDF‑приложения.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Android via Java** поддерживает формат файлов, будь то одиночный кадр или многокадровый <abbr title="Tag Image File Format">TIFF</abbr> изображение. Это означает, что вы можете конвертировать изображение TIFF в PDF в ваших Java‑приложениях.

TIFF или TIF, Tagged Image File Format, представляет растровые изображения, предназначенные для использования на различных устройствах, соответствующих этому стандарту формата файла. Изображение TIFF может содержать несколько кадров с разными изображениями. Формат Aspose.PDF также поддерживается, будь то однокадровое или многокадровое изображение TIFF. Таким образом, вы можете конвертировать изображение TIFF в PDF в ваших Java‑приложениях. Поэтому мы рассмотрим пример конвертации многостраничного изображения TIFF в многостраничный документ PDF с помощью следующих шагов:

1. Создайте экземпляр класса Document
1. Загрузите входное изображение TIFF
1. Получите FrameDimension кадров
1. Добавьте новую страницу для каждого кадра
1. Наконец, сохраните изображения на страницах PDF

Более того, следующий фрагмент кода показывает, как преобразовать многостраничное или многокадровое TIFF‑изображение в PDF:

```java
 public void convertTIFFtoPDF () {
        // Initialize document object
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

        // Load sample TIFF image file
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "TIFF-to-PDF.pdf");

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


