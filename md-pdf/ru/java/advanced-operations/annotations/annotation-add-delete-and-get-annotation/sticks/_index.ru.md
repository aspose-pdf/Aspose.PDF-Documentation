---
title: PDF Sticky Annotations 
linktitle: Sticky Annotation
type: docs
weight: 50
url: /java/sticky-annotations/
description: Эта тема о липких аннотациях, в качестве примера мы показываем аннотацию водяного знака в тексте. Она используется для представления графики на странице. Ознакомьтесь с фрагментом кода для решения этой задачи.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Добавление аннотации водяного знака

Аннотация водяного знака используется для представления графики, которая должна быть напечатана в фиксированном размере и положении на странице, независимо от размеров печатной страницы.

Вы можете добавить текст водяного знака, используя [WatermarkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/WatermarkAnnotation) в определенной позиции страницы PDF. Прозрачность водяного знака также может контролироваться с помощью свойства непрозрачности.

Пожалуйста, ознакомьтесь с следующим фрагментом кода для добавления WatermarkAnnotation.

```java
 package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleWatermarkAnnotation {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddWaterMarkAnnotation()
    {
        // Загрузите PDF файл
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        // Создайте аннотацию
        WatermarkAnnotation wa = new WatermarkAnnotation(page, new Rectangle(100, 500, 400, 600));

        // Добавьте аннотацию в коллекцию аннотаций страницы
        page.getAnnotations().add(wa);

        // Создайте TextState для настройки шрифта
        TextState ts = new TextState();

        ts.setForegroundColor(Color.getBlue());
        ts.setFont(FontRepository.findFont("Times New Roman"));
        ts.setFontSize(32);

        // Установите уровень прозрачности текста аннотации
        wa.setOpacity(0.5);

        // Добавьте текст в аннотацию
        wa.setTextAndState(new String[] { "Aspose.PDF", "Watermark", "Demo" }, ts);

        // Сохраните документ
        document.save(_dataDir + "sample_watermark.pdf");
    }
}
```


## Получить Аннотацию Водяного Знака

```java
    public static void GetWatermarkAnnotation() {
        // Загрузить PDF файл
        Document document = new Document(_dataDir + "sample_watermark.pdf");

        // Отфильтровать аннотации с использованием AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new WatermarkAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> WatermarkAnnotations = annotationSelector.getSelected();

        // вывести результаты
        for (Annotation fa : WatermarkAnnotations) {
            System.out.println(fa.getRect());
        }
    }
```

## Удалить Аннотацию Водяного Знака

```java
    public static void DeleteWatermarkAnnotation() {
         // Загрузить PDF файл
         Document document = new Document(_dataDir + "sample_watermark.pdf");

         // Отфильтровать аннотации с использованием AnnotationSelector
         Page page = document.getPages().get_Item(1);
         AnnotationSelector annotationSelector = new AnnotationSelector(
                 new WatermarkAnnotation(page, Rectangle.getTrivial()));
         page.accept(annotationSelector);
         List<Annotation> WatermarkAnnotations = annotationSelector.getSelected();

         // удалить аннотации
         for (Annotation fa : WatermarkAnnotations) {
            page.getAnnotations().delete(fa);
        }
        document.save(_dataDir + "sample_watermark_del.pdf");
    }
```