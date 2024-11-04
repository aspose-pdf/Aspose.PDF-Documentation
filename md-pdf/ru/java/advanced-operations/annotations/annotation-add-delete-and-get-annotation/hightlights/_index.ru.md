---
title: PDF Highlights Annotation 
linktitle: Highlights Annotation
type: docs
weight: 20
url: /java/highlights-annotation/
description: Аннотации разметки представлены в тексте как выделения, подчеркивания, зачеркивания или волнистые подчеркивания в тексте документа.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Аннотации разметки текста должны отображаться в виде выделений, подчеркиваний, зачеркиваний или волнистых подчеркиваний в тексте документа. При открытии они должны отображать всплывающее окно, содержащее текст связанной заметки.

Свойства аннотаций разметки текста в PDF-документе можно редактировать с помощью окна свойств, предоставленного в элементе управления просмотрщиком PDF. Можно изменить цвет, непрозрачность, автора и тему аннотации разметки текста.

Возможно получить или установить настройки аннотаций выделения с помощью свойства highlightSettings.
 Свойство highlightSettings используется для установки цвета, непрозрачности, автора, темы, даты изменения и свойства isLocked для аннотаций выделения.

Также возможно получить или установить настройки аннотаций зачёркивания, используя свойство strikethroughSettings. Свойство strikethroughSettings используется для установки цвета, непрозрачности, автора, темы, даты изменения и свойства isLocked для аннотаций зачёркивания.

Следующая возможность - это возможность получить или установить настройки аннотаций подчёркивания с помощью свойства underlineSettings. Свойство underlineSettings используется для установки цвета, непрозрачности, автора, темы, даты изменения и свойства isLocked для аннотаций подчёркивания.

## Добавление аннотации разметки текста

Для того чтобы добавить аннотацию разметки текста в PDF-документ, необходимо выполнить следующие действия:

1. Загрузите PDF-файл - новый объект [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
2. Создайте аннотации:

   - [HighlightAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/HighlightAnnotation) и установите параметры (заголовок, цвет).- [StrikeOutAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/StrikeOutAnnotation) и установить параметры (заголовок, цвет).
- [SquigglyAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/SquigglyAnnotation) и установить параметры (заголовок, цвет).
- [UnderlineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/UnderlineAnnotation) и установить параметры (заголовок, цвет).

1. После этого нам нужно добавить все аннотации на страницу.

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleTextMarkupAnnotation {
    // Путь к каталогу документов.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddTextMarkupAnnotation() {
        try {
            // Загрузить PDF файл
            Document document = new Document(_dataDir + "sample.pdf");
            Page page = document.getPages().get_Item(1);
            TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
            tfa.visit(page);

            // Создать аннотации
            HighlightAnnotation highlightAnnotation = new HighlightAnnotation(page,
                    tfa.getTextFragments().get_Item(1).getRectangle());
            highlightAnnotation.setTitle("Aspose User");
            highlightAnnotation.setColor(Color.getLightGreen());

            StrikeOutAnnotation strikeOutAnnotation = new StrikeOutAnnotation(page,
                    tfa.getTextFragments().get_Item(2).getRectangle());
            strikeOutAnnotation.setTitle("Aspose User");
            strikeOutAnnotation.setColor(Color.getBlue());

            SquigglyAnnotation squigglyAnnotation = new SquigglyAnnotation(page,
                    tfa.getTextFragments().get_Item(3).getRectangle());
            squigglyAnnotation.setTitle("Aspose User");
            squigglyAnnotation.setColor(Color.getRed());

            UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(page,
                    tfa.getTextFragments().get_Item(4).getRectangle());
            underlineAnnotation.setTitle("Aspose User");
            underlineAnnotation.setColor(Color.getViolet());

            // Добавить аннотации на страницу
            page.getAnnotations().add(highlightAnnotation);
            page.getAnnotations().add(squigglyAnnotation);
            page.getAnnotations().add(strikeOutAnnotation);
            page.getAnnotations().add(underlineAnnotation);
            document.save(_dataDir + "sample_mod.pdf");
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
}
```


Если вы хотите выделить многострочный фрагмент, вам следует использовать расширенный пример:

```java
    /// <summary>
    /// Расширенный пример для выделения многострочного фрагмента
    /// </summary>
    public static void AddHighlightAnnotationAdvanced() {
        Document document = new Document(_dataDir + "sample_mod.pdf");
        Page page = document.getPages().get_Item(1);
        TextFragmentAbsorber tfa = new TextFragmentAbsorber("Adobe\\W+Acrobat\\W+Reader", new TextSearchOptions(true));
        tfa.visit(page);
        for (TextFragment textFragment : tfa.getTextFragments()) {
            HighlightAnnotation highlightAnnotation = HighLightTextFragment(page, textFragment, Color.getYellow());
            page.getAnnotations().add(highlightAnnotation);
        }
        document.save(_dataDir + "sample_mod.pdf");
    }

    private static HighlightAnnotation HighLightTextFragment(Page page, TextFragment textFragment, Color color) {
        HighlightAnnotation ha;
        if (textFragment.getSegments().size() == 1) {
            ha = new HighlightAnnotation(page, textFragment.getSegments().get_Item(1).getRectangle());
            ha.setTitle("Aspose User");
            ha.setColor(color);
            ha.setModified(new Date());
            Rectangle rect = textFragment.getSegments().get_Item(1).getRectangle();
            ha.setQuadPoints(
                    new Point[] { new Point(rect.getLLX(), rect.getURY()), new Point(rect.getURX(), rect.getURY()),
                            new Point(rect.getLLX(), rect.getLLY()), new Point(rect.getURX(), rect.getLLY()) });
            return ha;
        }

        int offset = 0;
        Point[] quadPoints = new Point[textFragment.getSegments().size() * 4];
        for (TextSegment segment : textFragment.getSegments()) {
            Rectangle r = segment.getRectangle();
            quadPoints[offset + 0] = new Point(r.getLLX(), r.getURY());
            quadPoints[offset + 1] = new Point(r.getURX(), r.getURY());
            quadPoints[offset + 2] = new Point(r.getLLX(), r.getLLY());
            quadPoints[offset + 3] = new Point(r.getURX(), r.getLLY());
            offset += 4;
        }

        double llx = quadPoints[0].getX();
        double lly = quadPoints[0].getY();
        double urx = quadPoints[0].getX();
        double ury = quadPoints[0].getY();
        for (Point pt : quadPoints) {
            if (llx > pt.getX())
                llx = pt.getX();
            if (lly > pt.getY())
                lly = pt.getY();
            if (urx < pt.getX())
                urx = pt.getX();
            if (ury < pt.getY())
                ury = pt.getY();
        }
        ha = new HighlightAnnotation(page, new Rectangle(llx, lly, urx, ury));
        ha.setTitle("Aspose User");
        ha.setColor(color);
        ha.setModified(new Date());
        ha.setQuadPoints(quadPoints);
        return ha;
    }

    /// <summary>
    /// Как получить выделенный текст
    /// </summary>
    public static void GetHighlightedText() {
        // Загрузить PDF файл
        Document document = new Document(_dataDir + "sample_mod.pdf");
        Page page = document.getPages().get_Item(1);

        AnnotationSelector annotationSelector1 = new AnnotationSelector(
                new HighlightAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector1);
        List<Annotation> highlightAnnotations = annotationSelector1.getSelected();
        for (Annotation ta : highlightAnnotations) {
            System.out.println("[" + ((HighlightAnnotation) ta).getMarkedText() + "]");
        }
    }
```


## Получение Аннотации Текстовой Разметки

Пожалуйста, попробуйте использовать следующий фрагмент кода для получения аннотации текстовой разметки из PDF документа.

```java
     public static void GetTextMarkupAnnotation() {
        // Загрузить PDF файл
        Document document = new Document(_dataDir + "sample_mod.pdf");
        Page page = document.getPages().get_Item(1);

        AnnotationSelector annotationSelector1 = new AnnotationSelector(
                new HighlightAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector1);
        AnnotationSelector annotationSelector2 = new AnnotationSelector(
                new SquigglyAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector2);

        List<Annotation> textMarkupAnnotations = annotationSelector1.getSelected();
        textMarkupAnnotations.addAll(annotationSelector2.getSelected());

        // вывести результаты
        for (Annotation ta : textMarkupAnnotations) {
            System.out.printf("[" + ta.getAnnotationType() + ta.getRect() + "]");
        }
    }
```


## Удаление аннотации разметки текста

Следующий фрагмент кода показывает, как удалить аннотацию разметки текста из PDF-файла.

```java
   public static void DeleteTextMarkupAnnotation() {
        // Загрузить PDF файл
        Document document = new Document(_dataDir + "sample_mod.pdf");
        Page page = document.getPages().get_Item(1);

        AnnotationSelector annotationSelector1 = new AnnotationSelector(
                new HighlightAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector1);
        AnnotationSelector annotationSelector2 = new AnnotationSelector(
                new SquigglyAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector2);

        List<Annotation> textMarkupAnnotations = annotationSelector1.getSelected();
        textMarkupAnnotations.addAll(annotationSelector2.getSelected());

        // вывести результаты
        for (Annotation ta : textMarkupAnnotations) {
            page.getAnnotations().delete(ta);
        }
        document.save(_dataDir + "sample_del.pdf");
    }
```