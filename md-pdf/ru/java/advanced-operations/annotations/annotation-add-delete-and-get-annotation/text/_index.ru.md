---
title: PDF Text Annotation
Texttitle: Аннотация текста
type: docs
weight: 10
url: /java/text-annotation/
description: Aspose.PDF для Java позволяет добавлять, получать и удалять текстовые аннотации из вашего PDF документа.
lastmod: "2021-11-24"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

Добавление, удаление и получение аннотаций схожи для различных типов аннотаций. Давайте рассмотрим это на примере текстовой аннотации.

## Как добавить текстовую аннотацию в существующий PDF файл

В этом уроке вы узнаете, как добавить текст в существующий PDF документ. Инструмент текста позволяет добавлять текст в любое место документа. Текстовая аннотация - это аннотация, прикрепленная к определенному месту в PDF документе. В закрытом состоянии аннотация отображается как значок; в открытом - должна отображаться всплывающее окно, содержащее текст заметки в выбранном пользователем шрифте и размере.

Аннотации содержатся в коллекции [Annotations](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/AnnotationCollection) конкретной страницы.
 This collection содержит аннотации только для этой отдельной страницы; каждая страница имеет свою собственную коллекцию аннотаций.

Чтобы добавить аннотацию на определенную страницу, добавьте ее в коллекцию аннотаций этой страницы с помощью метода Add.

1. Сначала создайте аннотацию, которую вы хотите добавить в PDF.
1. Затем откройте входной PDF.
1. Добавьте аннотацию в коллекцию аннотаций объекта [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).

Следующий фрагмент кода показывает, как добавить аннотацию на страницу PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleTextAnnotation {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    public static void AddTextAnnotation()
    {
        // Загрузить PDF файл
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);
        Rectangle rect = new Rectangle(200, 750, 400, 790);
        TextAnnotation textAnnotation = new TextAnnotation(page, rect);

        textAnnotation.setTitle("Aspose User");
        textAnnotation.setSubject("Sample Subject");
        textAnnotation.setState (AnnotationState.Accepted);
        textAnnotation.setContents("Пример содержимого для аннотации");
        textAnnotation.setOpen(true);
        textAnnotation.setIcon(TextIcon.Circle);

        Border border = new Border(textAnnotation);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        textAnnotation.setBorder(border);
        textAnnotation.setRect(rect);

        page.getAnnotations().add(textAnnotation);
        document.save(_dataDir + "sample_textannot.pdf");
    }
}
```

## Добавить Новую (или Создать) Аннотацию Свободного Текста

Аннотация свободного текста отображает текст непосредственно на странице. Метод PdfContentEditor.CreateFreeText позволяет создать этот тип аннотации. В следующем примере мы добавляем аннотацию свободного текста над первым вхождением строки.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleFreeTextAnnotation {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    public static void AddFreeTextAnnotation()
    {
        // Загрузить PDF файл
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        DefaultAppearance defaultAppearance = new DefaultAppearance();
        defaultAppearance.setFontName("Helvetica");
        defaultAppearance.setFontSize(12);
        defaultAppearance.setTextColor(java.awt.Color.BLUE);

        FreeTextAnnotation freeTextAnnotation = new FreeTextAnnotation(page, new Rectangle(300.0, 770.0, 400.0, 790.0), defaultAppearance);

        freeTextAnnotation.setRichText("Демонстрация Свободного Текста");
        page.getAnnotations().add(freeTextAnnotation);
        document.save(_dataDir + "sample_freetext.pdf");
    }
}
```


## Получить Аннотацию Свободного Текста

Aspose.PDF для Java позволяет получить аннотацию свободного текста из вашего PDF документа.

Пожалуйста, ознакомьтесь с следующим фрагментом кода для выполнения этой задачи:

```java
public static void GetFreeTextAnnotation() {
        // Загрузить PDF файл
        Document document = new Document(_dataDir + "sample_freetext.pdf");

        // Фильтрация аннотаций с использованием AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new FreeTextAnnotation(page, Rectangle.getTrivial(), new DefaultAppearance()));
        page.accept(annotationSelector);
        List<Annotation> freeTextAnnotations = annotationSelector.getSelected();

        // напечатать результаты
        for (Annotation fa : freeTextAnnotations) {
            System.out.println(fa.getRect());
        }
    }
```

## Удалить Аннотацию Свободного Текста

Aspose.PDF для Java позволяет удалить аннотацию свободного текста из вашего PDF документа.

Пожалуйста, ознакомьтесь с следующим фрагментом кода для выполнения этой задачи:

```java
  public static void DeleteFreeTextAnnotation() {
         // Загрузить PDF файл
         Document document = new Document(_dataDir + "sample_freetext.pdf");

         // Фильтрация аннотаций с использованием AnnotationSelector
         Page page = document.getPages().get_Item(1);
         AnnotationSelector annotationSelector = new AnnotationSelector(
                 new FreeTextAnnotation(page, Rectangle.getTrivial(), new DefaultAppearance()));
         page.accept(annotationSelector);
         List<Annotation> freeTextAnnotations = annotationSelector.getSelected();

         // удаление аннотаций
         for (Annotation fa : freeTextAnnotations) {
            page.getAnnotations().delete(fa);
        }
        document.save(_dataDir + "sample_freetext_del.pdf");
    }
```

## Удалить все аннотации со страницы PDF файла

Коллекция [AnnotationCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/AnnotationCollection) объекта [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) содержит все аннотации для этой конкретной страницы.
 Чтобы удалить все аннотации с страницы, вызовите метод *Delete* коллекции AnnotationCollection.

Следующий фрагмент кода показывает, как удалить все аннотации с конкретной страницы.

```java
    public static void DeleteTextAnnotation() {
         // Загрузить PDF файл
         Document document = new Document(_dataDir + "sample_textannot.pdf");

         // Фильтрация аннотаций с использованием AnnotationSelector
         Page page = document.getPages().get_Item(1);
         AnnotationSelector annotationSelector = new AnnotationSelector(
                 new TextAnnotation(page, Rectangle.getTrivial()));
         page.accept(annotationSelector);
         List<Annotation> TextAnnotations = annotationSelector.getSelected();

         // удаление аннотаций
         for (Annotation fa : TextAnnotations) {
            page.getAnnotations().delete(fa);
        }
        document.save(_dataDir + "sample_textannot_del.pdf");
    }
```

## Получение всех аннотаций со страницы PDF документа

Aspose.PDF позволяет получать аннотации из всего документа или с заданной страницы. Чтобы получить все аннотации со страницы в PDF документе, выполните перебор коллекции [AnnotationCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/AnnotationCollection) нужных ресурсов страницы. Следующий фрагмент кода показывает, как получить все аннотации страницы.

```java
  public static void GetTextAnnotation() {
        // Загрузить PDF файл
        Document document = new Document(_dataDir + "sample_textannot.pdf");

        // Отфильтровать аннотации, используя AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new TextAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> TextAnnotations = annotationSelector.getSelected();

        // вывести результаты
        for (Annotation fa : TextAnnotations) {
            System.out.println(fa.getRect());
        }
    }
```