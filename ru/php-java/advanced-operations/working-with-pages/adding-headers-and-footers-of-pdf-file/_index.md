---
title: Добавление Заголовка и Нижнего Колонтитула в PDF
linktitle: Добавление Заголовка и Нижнего Колонтитула в PDF
type: docs
weight: 70
url: /ru/php-java/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF для PHP через Java позволяет добавлять заголовки и нижние колонтитулы в ваш PDF файл с помощью класса TextStamp.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF штампы часто используются в контрактах, отчетах и ограниченных материалах, чтобы подтвердить, что документы были просмотрены и помечены как "прочитано", "квалифицировано" или "конфиденциально" и т.д. Эта статья покажет вам, как мы можем добавить штампы изображений и текстовые штампы в PDF документы, используя **Aspose.PDF для PHP через Java**.

Если вы прочитаете приведенные выше фрагменты кода построчно, вы должны обнаружить, что синтаксис и логика кода довольно просты для понимания.

## Добавление Текста в Заголовок PDF Файла

Вы можете использовать класс [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) для добавления текста в заголовок PDF файла.
 TextStamp класс предоставляет свойства, необходимые для создания штампа на основе текста, такие как размер шрифта, стиль шрифта и цвет шрифта и т.д. Чтобы добавить текст в заголовок, вам нужно создать объект Document и объект TextStamp, используя необходимые свойства. После этого вы можете вызвать метод AddStamp класса Page, чтобы добавить текст в заголовок PDF.

Вам нужно установить свойство TopMargin таким образом, чтобы оно корректировало текст в области заголовка вашего PDF. Также необходимо установить HorizontalAlignment в положение Center и VerticalAlignment в положение Top.

Следующий фрагмент кода показывает, как добавить текст в заголовок PDF файла с помощью PHP.

```php

    // Открыть документ
    $document = new Document($inputFile);

    // Создать заголовок
    $textStamp = new TextStamp("Текст заголовка");
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    // Установить свойства штампа
    $textStamp->setTopMargin(10);
    $textStamp->setHorizontalAlignment($horizontalAlignment->Center);
    $textStamp->setVerticalAlignment($verticalAlignment->Top);

    $pages = $document->getPages();

    // Добавить подвал на первую страницу
    $page = $pages->get_Item(1);
    $page->addStamp($textStamp);
    
    // Сохранить выходной документ
    $document->save($outputFile);
    $document->close();
```

## Добавление текста в нижний колонтитул PDF-файла

Вы можете использовать класс TextStamp для добавления текста в нижний колонтитул PDF-файла. Класс TextStamp предоставляет свойства, необходимые для создания штампа на основе текста, такие как размер шрифта, стиль шрифта и цвет шрифта и т.д. Чтобы добавить текст в нижний колонтитул, вам нужно создать объект Document и объект TextStamp, используя необходимые свойства. После этого вы можете вызвать метод addStamp страницы для добавления текста в нижний колонтитул PDF.

Следующий фрагмент кода показывает, как добавить текст в нижний колонтитул PDF-файла с помощью PHP.

```php

    // Открыть документ
    $document = new Document($inputFile);

    // Создать заголовок
    $textStamp = new TextStamp("Header Text");
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    // Установить свойства штампа
    $textStamp->setBottomMargin(10);
    $textStamp->setHorizontalAlignment($horizontalAlignment->Center);
    $textStamp->setVerticalAlignment($verticalAlignment->Bottom);

    $pages = $document->getPages();

    // Добавить нижний колонтитул на первую страницу
    $page = $pages->get_Item(1);
    $page->addStamp($textStamp);
    
    // Сохранить выходной документ
    $document->save($outputFile);
    $document->close();
```


## Добавление изображения в заголовок PDF файла

Вы можете использовать класс [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp) для добавления изображения в заголовок PDF файла. Класс Image Stamp предоставляет свойства, необходимые для создания штампа на основе изображения, такие как размер шрифта, стиль шрифта и цвет шрифта и т.д. Для того чтобы добавить изображение в заголовок, вам нужно создать объект Document и объект Image Stamp с использованием необходимых свойств. После этого вы можете вызвать метод [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/class-use/Stamp) страницы, чтобы добавить изображение в заголовок PDF.

```php

    // Открыть документ
    $document = new Document($inputFile);
    
    // Создать нижний колонтитул
    $imageStamp = new ImageStamp($inputImage);
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    // Установить свойства штампа
    $imageStamp->setTopMargin(10);
    $imageStamp->setHorizontalAlignment($horizontalAlignment->Center);
    $imageStamp->setVerticalAlignment($verticalAlignment->Top);

    $pages = $document->getPages();

    // Добавить нижний колонтитул на первую страницу
    $page = $pages->get_Item(1);
    $page->addStamp($imageStamp);

    // Сохранить выходной документ
    $document->save($outputFile);
    $document->close();
```


Ниже приведен фрагмент кода, который показывает, как добавить изображение в заголовок PDF файла с помощью PHP.

## Добавление изображения в подвал PDF файла

Вы можете использовать класс Image Stamp, чтобы добавить изображение в подвал PDF файла. Класс Image Stamp предоставляет свойства, необходимые для создания штампа на основе изображения, такие как размер шрифта, стиль шрифта и цвет шрифта и т. д. Для добавления изображения в подвал необходимо создать объект Document и объект Image Stamp, используя необходимые свойства. После этого вы можете вызвать метод AddStamp страницы, чтобы добавить изображение в подвал PDF.

{{% alert color="primary" %}}

Необходимо установить свойство BottomMargin таким образом, чтобы оно корректировало изображение в области подвала вашего PDF. Также необходимо установить [HorizontalAlignment](https://reference.aspose.com/pdf/java/com.aspose.pdf/HorizontalAlignment) в `Center` и [VerticalAlignment](https://reference.aspose.com/pdf/java/com.aspose.pdf/VerticalAlignment) в `Bottom`.

{{% /alert %}}

Ниже приведен фрагмент кода, который показывает, как добавить изображение в подвал PDF файла с помощью PHP.

```php

    // Открыть документ
    $document = new Document($inputFile);
    
    // Создать нижний колонтитул
    $imageStamp = new ImageStamp($inputImage);
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    // Установить свойства штампа
    $imageStamp->setBottomMargin(10);
    $imageStamp->setHorizontalAlignment($horizontalAlignment->Center);
    $imageStamp->setVerticalAlignment($verticalAlignment->Bottom);

    $pages = $document->getPages();

    // Добавить нижний колонтитул на первую страницу
    $page = $pages->get_Item(1);
    $page->addStamp($imageStamp);

    // Сохранить выходной документ
    $document->save($outputFile);
    $document->close();
```

## Добавление различных заголовков в один PDF-файл

Мы знаем, что можем добавить TextStamp в раздел Заголовок/Нижний колонтитул документа, используя свойства TopMargin или Bottom Margin, но иногда может потребоваться добавить несколько заголовков/нижних колонтитулов в один PDF-документ. **Aspose.PDF для PHP через Java** объясняет, как это сделать.

Чтобы выполнить это требование, мы создадим отдельные объекты [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) (количество объектов зависит от количества требуемых заголовков/нижних колонтитулов) и добавим их в PDF-документ.
 Мы также можем указать различную информацию о форматировании для каждого отдельного объекта штампа. В следующем примере мы создали объект [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) и три объекта [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp), а затем использовали метод [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/class-use/Stamp) страницы, чтобы добавить текст в раздел заголовка PDF. Следующий фрагмент кода показывает, как добавить изображение в нижний колонтитул PDF файла с помощью Aspose.PDF для PHP через Java.

```php

    // Открыть документ
    $document = new Document($inputFile);

    // Создать три штампа
    $stamp1 = new TextStamp("Header 1");
    $stamp2 = new TextStamp("Header 2");
    $stamp3 = new TextStamp("Header 3");
    
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();
    $fontStyles = new FontStyles();

    // Установить выравнивание штампа (разместить штамп сверху страницы, по центру по горизонтали)
    $stamp1->setVerticalAlignment ($verticalAlignment->Top);
    $stamp1->setHorizontalAlignment($horizontalAlignment->Center);

    // Указать стиль шрифта как Bold
    $stamp1->getTextState()->setFontStyle($fontStyles->Bold);
    // Установить передний цвет текста как красный
    $stamp1->getTextState()->setForegroundColor((new Color())->getRed());
    // Указать размер шрифта как 14
    $stamp1->getTextState()->setFontSize(14);

    // Теперь нам нужно установить вертикальное выравнивание для второго объекта штампа как Top
    $stamp2->setVerticalAlignment($verticalAlignment->Top);
    // Установить горизонтальное выравнивание штампа как по центру
    $stamp2->setHorizontalAlignment($horizontalAlignment->Center);
    // Установить коэффициент масштабирования для объекта штампа
    $stamp2->setZoom(10);

    // Установить форматирование для третьего объекта штампа
    // Указать информацию о вертикальном выравнивании для объекта штампа как TOP
    $stamp3->setVerticalAlignment($verticalAlignment->Top);
    // Установить информацию о горизонтальном выравнивании для объекта штампа как по центру
    $stamp3->setHorizontalAlignment ($horizontalAlignment->Center);
    // Установить угол поворота для объекта штампа
    $stamp3->setRotateAngle(35);
    // Установить розовый как цвет фона для штампа
    $stamp3->getTextState()->setBackgroundColor ((new Color())->getPink());  
    // Изменить информацию о шрифте для штампа на Verdana
    $stamp3->getTextState()->setFont ((new FontRepository())->findFont("Verdana"));

    // Первый штамп добавляется на первую страницу;
    $document->getPages()->get_Item(1)->addStamp($stamp1);
    // Второй штамп добавляется на вторую страницу;
    $document->getPages()->get_Item(2)->addStamp($stamp2);
    // Третий штамп добавляется на третью страницу.
    $document->getPages()->get_Item(3)->addStamp($stamp3);
    
    // Сохранить выходной документ
    $document->save($outputFile);
    $document->close();
```