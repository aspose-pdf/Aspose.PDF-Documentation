---
title: PDF Липкие Аннотации 
linktitle: Липкая Аннотация
type: docs
weight: 50
url: ru/php-java/sticky-annotations/
description: Эта тема о липких аннотациях, в качестве примера мы показываем водяной знак аннотации в тексте. Он используется для представления графики на странице. Проверьте фрагмент кода, чтобы решить эту задачу.
lastmod: "2024-06-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Добавить Водяной Знак Аннотации

Водяной знак аннотации должен использоваться для представления графики, которая будет напечатана в фиксированном размере и положении на странице, независимо от размеров напечатанной страницы.

Вы можете добавить текст водяного знака, используя [WatermarkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/WatermarkAnnotation) в определенной позиции на странице PDF. Непрозрачность водяного знака также может быть контролируема с помощью свойства opacity.

Пожалуйста, проверьте следующий фрагмент кода, чтобы добавить WatermarkAnnotation.

```php

    // Открыть документ
    $document = new Document($inputFile);
    $fontRepository = new FontRepository();
    $colors = new Color();
    // получить конкретную страницу
    $page = $document->getPages()->get_Item(1);
    
    //Создать аннотацию
    $wa = new WatermarkAnnotation($page, new Rectangle(100, 500, 400, 600));

    //Добавить аннотацию в коллекцию аннотаций страницы
    $page->getAnnotations()->add($wa);

    //Создать TextState для настройки шрифта
    $ts = new TextState();

    $ts->setForegroundColor($colors->getBlue());
    $ts->setFont($fontRepository->findFont("Times New Roman"));
    $ts->setFontSize(32);

    //Установить уровень непрозрачности текста аннотации
    $wa->setOpacity(0.5);
            
    $watermarkStrings = ["Aspose.PDF", "Watermark", "Demo" ];
    //Добавить текст к аннотации
    $wa->setTextAndState($watermarkStrings, $ts);

    // Сохранить результирующий PDF документ.    
    $document->save($outputFile);
    $document->close();
```