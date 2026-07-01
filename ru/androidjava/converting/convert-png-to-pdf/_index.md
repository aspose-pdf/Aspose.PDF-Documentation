---
title: Конвертировать PNG в PDF
linktitle: Конвертировать PNG в PDF
type: docs
weight: 200
url: /ru/androidjava/convert-png-to-pdf/
lastmod: "2026-07-01"
description: В этой статье показано, как конвертировать PNG в PDF с помощью библиотеки Aspose.PDF в ваших Android‑приложениях на Java. Вы можете конвертировать PNG‑изображения в формат PDF, используя простые шаги.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Android via Java** поддерживает функцию конвертации PNG‑изображений в формат PDF. Посмотрите следующий фрагмент кода для реализации вашей задачи.

<abbr title="Portable Network Graphics">PNG</abbr> относится к типу растрового формата файлов изображений, использующему без потерь сжатие, что делает его популярным среди пользователей.

Вы можете конвертировать PNG в PDF изображение, используя следующие шаги:

1. Загрузите входное PNG‑изображение
1. Читать значения высоты и ширины
1. Создайте новый документ и добавить страницу
1. Установите размеры страницы
1. Сохраните выходной файл

Кроме того, приведенный ниже фрагмент кода показывает, как преобразовать PNG в PDF в ваших Java‑приложениях:

```java
    public void convertPNGtoPDF () {
        // Initialize document object
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/sample.png");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
```


