---
title: Использование дополнительных типов аннотаций PDF
linktitle: Дополнительные Аннотации
type: docs
weight: 60
url: ru/java/extra-annotations/
description: В этом разделе описывается, как добавлять, получать и удалять дополнительные виды аннотаций из вашего PDF документа.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Как добавить аннотацию вставки в существующий PDF файл

Аннотация вставки - это символ, указывающий на редактирование текста. Аннотация вставки также является аннотацией разметки, поэтому класс Caret наследуется от класса Markup и также предоставляет функции для получения или установки свойств аннотации вставки и сброса потока внешнего вида аннотации вставки.

Шаги, с помощью которых мы создаем аннотацию вставки:

1. Загрузите PDF файл - new [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. Создайте новый [Caret Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/CaretAnnotation) и установите параметры Caret (новый Rectangle, title, Subject, Flags, color, width, StartingStyle и EndingStyle). Эта аннотация используется для указания вставки текста.
1. Создайте новый [StrikeOutAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/StrikeOutAnnotation) и установите параметры (новый Rectangle, title, color, new QuadPoints и новые точки, Subject, InReplyTo, ReplyType).
1. После этого мы можем добавить аннотации на страницу.

Следующий фрагмент кода показывает, как добавить аннотацию Caret в PDF файл:

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleCaretAnnotation {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddCaretAnnotation() {
        // Загрузить PDF файл
        Document document = new Document(_dataDir + "sample.pdf");
        // Эта аннотация используется для указания вставки текста
        CaretAnnotation caretAnnotation1 = new CaretAnnotation(
                document.getPages().get_Item(1), new Rectangle(299.988, 713.664, 308.708, 720.769));
        caretAnnotation1.setTitle("Пользователь Aspose");
        caretAnnotation1.setSubject("Вставленный текст 1");
        caretAnnotation1.setFlags(AnnotationFlags.Print);
        caretAnnotation1.setColor(Color.getBlue());

        // Эта аннотация используется для указания замены текста
        CaretAnnotation caretAnnotation2 = new CaretAnnotation(
                document.getPages().get_Item(1), new Rectangle(361.246, 727.908, 370.081, 735.107));

        caretAnnotation2.setTitle("Пользователь Aspose");
        caretAnnotation2.setFlags(AnnotationFlags.Print);
        caretAnnotation2.setSubject("Вставленный текст 2");
        caretAnnotation2.setColor(Color.getBlue());

        StrikeOutAnnotation strikeOutAnnotation = new StrikeOutAnnotation(
                document.getPages().get_Item(1), new Rectangle(318.407, 727.826, 368.916, 740.098));

        strikeOutAnnotation.setColor(Color.getBlue());
        strikeOutAnnotation.setQuadPoints(new Point[] { new Point(321.66, 739.416),
                new Point(365.664, 739.416), new Point(321.66, 728.508),
                new Point(365.664, 728.508) });

        strikeOutAnnotation.setSubject("Зачеркнуть");
        strikeOutAnnotation.setInReplyTo(caretAnnotation2);
        strikeOutAnnotation.setReplyType(ReplyType.Group);

        document.getPages().get_Item(1).getAnnotations().add(caretAnnotation1);
        document.getPages().get_Item(1).getAnnotations().add(caretAnnotation2);
        document.getPages().get_Item(1).getAnnotations().add(strikeOutAnnotation);

        document.save(_dataDir + "sample_caret.pdf");

    }
```


## Получение Аннотации Карет

Пожалуйста, попробуйте использовать следующий код для получения аннотации карет в PDF документе

```java
    public static void GetCaretAnnotation() {
        // Загрузите PDF файл
        Document document = new Document(_dataDir + "sample_caret.pdf");

        // Фильтрация аннотаций с использованием AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new CaretAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> caretAnnotations = annotationSelector.getSelected();

        // вывод результатов
        for (Annotation ca : caretAnnotations) {
            System.out.println(ca.getRect());
        }
    }
```

## Удаление Аннотации Карет

Следующий код показывает, как удалить аннотацию карет из PDF файла.

```java
public static void DeleteCaretAnnotation() {
        // Загрузите PDF файл
        Document document = new Document(_dataDir + "sample_caret.pdf");

        // Фильтрация аннотаций с использованием AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new CaretAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> caretAnnotations = annotationSelector.getSelected();

        // удаление аннотации
        for (Annotation ca : caretAnnotations) {
            document.getPages().get_Item(1).getAnnotations().delete(ca);
        }
        document.save(_dataDir + "sample_caret_del.pdf");
    }
```


A [Link Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) является гипертекстовой ссылкой, которая ведет к месту назначения в другом месте документа или к действию, которое должно быть выполнено.

## Добавить аннотацию ссылки

Ссылка — это прямоугольная область, которую можно разместить в любом месте на странице. Каждая ссылка имеет соответствующее действие PDF, связанное с ней. Это действие выполняется, когда пользователь нажимает в области этой ссылки.

Следующий фрагмент кода показывает, как добавить аннотацию ссылки в PDF-файл, используя пример с номером телефона:

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleLinkAnnotation {

    // Путь к каталогу документов.

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddLinkAnnotation() {
        try {
            // Загрузить PDF-файл
            Document document = new Document(_dataDir + "SimpleResume.pdf");
            Page page = document.getPages().get_Item(1);

            // Создать объект TextFragmentAbsorber для поиска номера телефона
            TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("678-555-0103");

            // Применить абсорбер только для 1-й страницы
            page.accept(textFragmentAbsorber);

            TextFragment phoneNumberFragment = textFragmentAbsorber.getTextFragments().get_Item(1);

            // Создать аннотацию ссылки и установить действие для вызова телефонного номера
            LinkAnnotation linkAnnotation = new LinkAnnotation(page, phoneNumberFragment.getRectangle());
            linkAnnotation.setAction(new GoToURIAction("callto:678-555-0103"));

            // Добавить аннотацию на страницу
            page.getAnnotations().add(linkAnnotation);
            document.save(_dataDir + "SimpleResume_mod.pdf");
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
```


## Получить Аннотацию Ссылки

Пожалуйста, попробуйте использовать следующий фрагмент кода, чтобы получить LinkAnnotation из PDF-документа.

```java
    public static void GetLinkAnnotations() {

        // Загрузить PDF файл
        Document document = new Document(_dataDir + "SimpleResume_mod.pdf");

        // Отфильтровать аннотации с использованием AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> linkAnnotations = annotationSelector.getSelected();

        // вывести результаты
        for (Annotation la : linkAnnotations) {

            LinkAnnotation l = (LinkAnnotation) la;

            // Вывести URL каждой аннотации ссылки
            System.out.println("URI: " + ((GoToURIAction) l.getAction()).getURI());

            TextAbsorber absorber = new TextAbsorber();
            absorber.getTextSearchOptions().setLimitToPageBounds(true);
            absorber.getTextSearchOptions().setRectangle(l.getRect());
            page.accept(absorber);

            String extractedText = absorber.getText();

            // Вывести текст, связанный с гиперссылкой
            System.out.println(extractedText);
        }
    }
```


## Удаление аннотации ссылки

Следующий фрагмент кода показывает, как удалить аннотацию ссылки из PDF-файла. Для этого нам нужно найти и удалить все аннотации ссылки на первой странице. После этого мы сохраним документ с удаленной аннотацией.

```java
    public static void DeleteLinkAnnotations() {
        // Загрузить PDF файл
        Document document = new Document(_dataDir + "SimpleResume_mod.pdf");

        // Фильтрация аннотаций с использованием AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> linkAnnotations = annotationSelector.getSelected();

        for (Annotation la : linkAnnotations)
            page.getAnnotations().delete(la);

        // Сохранить документ с удаленной аннотацией
        document.save(_dataDir + "SimpleResume_del.pdf");
    }
```

## Сокрытие определенной области страницы с использованием аннотации редактирования с помощью Aspose.PDF для Java

Aspose.PDF for Java поддерживает возможность добавления и управления аннотациями в существующем PDF файле. Недавно некоторые из наших клиентов выразили необходимость редактирования (удаления текста, изображений и т.д. элементов) определенного региона страницы PDF документа. Для выполнения этого требования предоставлен класс под названием RedactionAnnotation, который может быть использован для редактирования определенных регионов страницы или для управления существующими RedactionAnnotations и их редактирования (т.е. уплощения аннотации и удаления текста под ней).

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.PdfAnnotationEditor;

public class ExampleRedactAnnotation {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void RedactionAnnotation() {

        // Открыть документ
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        // Создать экземпляр RedactionAnnotation для определенного региона страницы
        RedactionAnnotation annot = new RedactionAnnotation(page, new Rectangle(200, 500, 300, 600));
        annot.setFillColor(Color.getGreen());
        annot.setBorderColor(Color.getYellow());
        annot.setColor(Color.getBlue());

        // Текст для печати на редактируемой аннотации
        annot.setOverlayText("REDACTED");
        annot.setTextAlignment(HorizontalAlignment.Center);

        // Повторить наложенный текст на редактируемой аннотации
        annot.setRepeat(true);

        // Добавить аннотацию в коллекцию аннотаций первой страницы
        page.getAnnotations().add(annot);

        // Уплощает аннотацию и редактирует содержимое страницы (т.е. удаляет текст и изображение
        // Под редактируемой аннотацией)
        annot.redact();
        document.save(_dataDir + "RedactPage_out.pdf");
    }
```


## Facades подход

Пространство имен Aspose.PDF.Facades также содержит класс под названием [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor), который предоставляет возможность изменять существующие аннотации внутри PDF файла. Этот класс содержит метод с именем [RedactArea(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Redaction#getredactArea-com.aspose.pdf.Page-com.aspose.pdf.Rectangle-java.awt.Color-), который предоставляет возможность удалять определенные области страницы.

```java
    public static void RedactionAnnotationFacades(){
        PdfAnnotationEditor editor = new PdfAnnotationEditor();

        editor.bindPdf(_dataDir + "sample.pdf");

        // Редактировать определенную область страницы
        editor.redactArea(1, new Rectangle(100, 100, 20, 70), java.awt.Color.white);
        editor.bindPdf(_dataDir + "sample.pdf");
        editor.save( _dataDir + "FacadesApproach_out.pdf");
    }
```