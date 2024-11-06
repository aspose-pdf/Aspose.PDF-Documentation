---
title: Добавление штампов изображений в PDF программно 
linktitle: Штампы изображений в PDF файле
type: docs
weight: 10
url: ru/php-java/image-stamps-in-pdf-page/
description: Добавьте штамп изображения в ваш PDF документ, используя класс ImageStamp с библиотекой Aspose.PDF для PHP через Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Добавление штампа изображения в PDF файл

Вы можете использовать класс [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) для добавления изображения в качестве штампа в PDF документ. Класс [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) предоставляет методы для задания высоты, ширины, прозрачности и т.д.

Чтобы добавить штамп изображения:

1. Создайте объект [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) и объект ImageStamp, используя необходимые свойства.

1. Вызовите метод [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) класса [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page), чтобы добавить штамп в PDF.

Следующий фрагмент кода показывает, как добавить штамп изображения в файл PDF.

```php

    // Открыть документ
    $document = new Document($inputFile);        
    $pages = $document->getPages();
  
    // Создать штамп изображения
    $imageStamp = new ImageStamp($inputImageFile);
    $imageStamp->setBackground(true);
    $imageStamp->setXIndent(100);
    $imageStamp->setYIndent(100);
    $imageStamp->setHeight(48);
    $imageStamp->setWidth(225);
    $imageStamp->setRotate((new Rotation())->getOn270());
    $imageStamp->setOpacity(0.5);

    // Добавить штамп на определенную страницу
    $document->getPages()->get_Item(1)->addStamp($imageStamp);

    // Сохранить выходной документ
    $document->save($outputFile);
    $document->close()
```

## Контроль качества изображения при добавлении штампа

Класс [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) позволяет добавить изображение в качестве штампа в PDF документ.
 Он также позволяет управлять качеством изображения при добавлении изображения в качестве водяного знака в PDF файл. Для этого в класс [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) был добавлен метод с именем setQuality(...). Аналогичный метод также можно найти в классе [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/Stamp) пакета com.aspose.pdf.facades.

Следующий фрагмент кода показывает, как управлять качеством изображения при добавлении в качестве штампа в PDF файл.

```php

    // Открыть документ
    $document = new Document($inputFile);        
    $pages = $document->getPages();

    // Создать штамп изображения
    $imageStamp = new ImageStamp($inputImageFile);
    $imageStamp->setQuality(10);

    $document->getPages()->get_Item(1)->addStamp($imageStamp);

    // Сохранить выходной документ
    $document->save($outputFile);
    $document->close();        
```

## Штамп изображения как фон в плавающем блоке

API Aspose.PDF позволяет добавить штамп изображения в качестве фона в плавающий блок. Свойство BackgroundImage класса FloatingBox может быть использовано для установки изображения фона для плавающего блока, как показано в следующем примере кода.

Этот фрагмент кода демонстрирует процесс создания PDF-документа и добавления в него FloatingBox. FloatingBox содержит текстовый фрагмент, границу, фоновое изображение и цвет фона. Полученный документ затем сохраняется в выходной файл.

```php

    // Открыть документ
    $document = new Document($inputFile);
    $colors = new Color();
    $pages = $document->getPages();

    // Добавить страницу в PDF-документ
    $page = $pages->add();

    // Создать объект FloatingBox
    $aBox = new FloatingBox(200, 100);

    // Установить левую позицию для FloatingBox
    $aBox->setLeft(40);

    // Установить верхнюю позицию для FloatingBox
    $aBox->setTop(80);

    // Установить горизонтальное выравнивание для FloatingBox
    $aBox->setHorizontalAlignment((new HorizontalAlignment())->getCenter());

    // Добавить текстовый фрагмент в коллекцию абзацев FloatingBox
    $aBox->getParagraphs()->add(new TextFragment("main text"));

    // Установить границу для FloatingBox
    $aBox->setBorder(new BorderInfo(BorderSide::$All, $colors->getRed()));

    // Добавить фоновое изображение
    $img = new Image();
    $img->setFile($inputImageFile);
    $aBox->setBackgroundImage($img);

    // Установить цвет фона для FloatingBox
    $aBox->setBackgroundColor($colors->getYellow());

    // Добавить FloatingBox в коллекцию абзацев объекта страницы
    $page->getParagraphs()->add($aBox);
    
    // Сохранить выходной документ
    $document->save($outputFile);
    $document->close();
```