---
title: Добавление изображений штампов в PDF программно
linktitle: Изображения штампы в PDF файле
type: docs
weight: 10
url: /ru/java/image-stamps-in-pdf-page/
description: Добавьте изображение штампа в свой PDF документ, используя класс ImageStamp с библиотекой Aspose.PDF для Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Добавление изображения штампа в PDF файл

Вы можете использовать класс [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) для добавления изображения в качестве штампа в PDF документ. Класс [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) предоставляет методы для задания высоты, ширины и непрозрачности и т.д.

Чтобы добавить изображение штампа:

1. Создайте объект [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) и объект ImageStamp, используя необходимые свойства.

1. Вызовите метод [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) класса [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) для добавления штампа в PDF.

Следующий пример кода показывает, как добавить изображение штампа в PDF файл.

```java
public static void AddImageStampInPDFFile() {
        // Открываем документ
        Document pdfDocument = new Document(_dataDir + "AddImageStamp.pdf");

        // Создаем изображение штампа
        ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.png");
        imageStamp.setBackground(true);
        imageStamp.setXIndent(100);
        imageStamp.setYIndent(100);
        imageStamp.setHeight(48);
        imageStamp.setWidth(225);
        imageStamp.setRotate(Rotation.on270);
        imageStamp.setOpacity(0.5);

        // Добавляем штамп на конкретную страницу
        pdfDocument.getPages().get_Item(1).addStamp(imageStamp);

        // Сохраняем выводной документ
        pdfDocument.save(_dataDir + "AddImageStamp_out.pdf");

    }
```


## Контроль качества изображения при добавлении штампа

Класс [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) позволяет добавить изображение в качестве штампа в PDF-документ. Он также позволяет контролировать качество изображения при добавлении его в качестве водяного знака в PDF-файл. Для этого в класс [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) был добавлен метод с именем setQuality(...). Аналогичный метод также можно найти в классе [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/Stamp) пакета com.aspose.pdf.facades.

Следующий фрагмент кода показывает, как контролировать качество изображения при добавлении его в качестве штампа в PDF-файл.

```java
 public static void ControlImageQualityWhenAddingStamp() {
        // Открыть документ
        Document pdfDocument = new Document(_dataDir + "AddImageStamp.pdf");

        // Создать штамп изображения
        ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.png");
        imageStamp.setQuality(10);
        pdfDocument.getPages().get_Item(1).addStamp(imageStamp);

        pdfDocument.save(_dataDir + "ControlImageQuality_out.pdf");
    }
```


## Изображение Штамп как Фон в Плавающем Блоке

Aspose.PDF API позволяет добавить изображение штамп как фон в плавающем блоке. Свойство BackgroundImage класса FloatingBox может быть использовано для установки фонового изображения штампа для плавающего блока, как показано в следующем примере кода.

```java
public static void ImageStampAsBackgroundInFloatingBox() {
        // Создать объект Document
        Document doc = new Document();
        // Добавить страницу в PDF документ
        Page page = doc.getPages().add();

        // Создать объект FloatingBox
        FloatingBox aBox = new FloatingBox(200, 100);

        // Установить левую позицию для FloatingBox
        aBox.setLeft(40);
        // Установить верхнюю позицию для FloatingBox
        aBox.setTop(80);
        // Установить горизонтальное выравнивание для FloatingBox
        aBox.setHorizontalAlignment(HorizontalAlignment.Center);
        // Добавить текстовый фрагмент в коллекцию абзацев FloatingBox
        aBox.getParagraphs().add(new TextFragment("основной текст"));
        // Установить границу для FloatingBox
        aBox.setBorder(new BorderInfo(BorderSide.All, Color.getRed()));

        // Добавить фоновое изображение
        Image img = new Image();
        img.setFile(_dataDir + "aspose-logo.png");
        aBox.setBackgroundImage(img);

        // Установить фоновый цвет для FloatingBox
        aBox.setBackgroundColor(Color.getYellow());

        // Добавить FloatingBox в коллекцию абзацев объекта страницы
        page.getParagraphs().add(aBox);
        // Сохранить PDF документ
        doc.save(_dataDir + "AddImageStampAsBackgroundInFloatingBox_out.pdf");
    }
}
```