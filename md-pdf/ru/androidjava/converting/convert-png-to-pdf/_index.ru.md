---
title: Конвертировать PNG в PDF 
linktitle: Конвертировать PNG в PDF
type: docs
weight: 200
url: /androidjava/convert-png-to-pdf/
lastmod: "2021-06-05"
description: В этой статье показано, как конвертировать PNG в PDF с помощью библиотеки Aspose.PDF в ваших Android через Java приложениях. Вы можете конвертировать изображения PNG в формат PDF, используя простые шаги.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF для Android через Java** поддерживает функцию конвертации изображений PNG в формат PDF. Проверьте следующий фрагмент кода для выполнения вашей задачи.

<abbr title="Portable Network Graphics">PNG</abbr> относится к типу формата растрового изображения, который использует безупречное сжатие, что делает его популярным среди пользователей.

Вы можете конвертировать PNG в изображение PDF, используя следующие шаги:

1. Загрузите входное изображение PNG
1. Прочитайте значения высоты и ширины
1. Создайте новый документ и добавьте страницу
1. Установите размеры страницы
1. Сохраните выходной файл

Кроме того, ниже приведен фрагмент кода, который показывает, как конвертировать PNG в PDF в ваших Java приложениях:

```java
    public void convertPNGtoPDF () {
        // Инициализировать объект документа
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