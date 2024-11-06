---
title: PDF Highlights Annotation 
linktitle: Highlights Annotation
type: docs
weight: 20
url: ar/java/highlights-annotation/
description: يتم تقديم التعليقات التوضيحية للتمييز كتمييزات أو تسطيرات أو شطبات أو تسطيرات متعرجة في نص المستند.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

يجب أن تظهر التعليقات التوضيحية على النص كتمييزات أو تسطيرات أو شطبات أو تسطيرات متعرجة ("متموجة") في نص المستند. عند الفتح، يجب أن تعرض نافذة منبثقة تحتوي على نص الملاحظة المرتبطة.

يمكن تحرير خصائص التعليقات التوضيحية على النص في مستند PDF باستخدام نافذة الخصائص المقدمة في وحدة التحكم في عارض PDF. يمكن تعديل اللون، والعتامة، والمؤلف، وموضوع التعليق التوضيحي على النص.

من الممكن الحصول على إعدادات تعليقات التمييز أو تعيينها باستخدام خاصية highlightSettings.
 The highlightSettings property is used to set the color, opacity, author, subject, modifiedDate and isLocked properties of the highlight annotations.

يتم استخدام خاصية highlightSettings لتعيين اللون، العتامة، المؤلف، الموضوع، تاريخ التعديل وخصائص القفل للتعليقات التوضيحية للتمييز.

Also possible to get or set the settings of the strikethrough annotations using the strikethroughSettings property. The strikethroughSettings property is used to set the color, opacity, author, subject, modifiedDate, and isLocked properties of the strikethrough annotations.

من الممكن أيضًا الحصول أو تعيين إعدادات التعليقات التوضيحية للشطب باستخدام خاصية strikethroughSettings. يتم استخدام خاصية strikethroughSettings لتعيين اللون، العتامة، المؤلف، الموضوع، تاريخ التعديل وخصائص القفل للتعليقات التوضيحية للشطب.

The next feature is the ability to get or set the settings of the underline annotations using the underlineSettings property. The underlineSettings property is used to set the color, opacity, author, subject, modifiedDate, and isLocked properties of the underline annotations.

الميزة التالية هي القدرة على الحصول أو تعيين إعدادات التعليقات التوضيحية للتسطير باستخدام خاصية underlineSettings. يتم استخدام خاصية underlineSettings لتعيين اللون، العتامة، المؤلف، الموضوع، تاريخ التعديل وخصائص القفل للتعليقات التوضيحية للتسطير.

## Add Text Markup Annotation

## إضافة تعليق توضيحي لنص

In order to add an Text Markup Annotation to the PDF document, we need to perform the following actions:

لإضافة تعليق توضيحي لنص إلى مستند PDF، نحتاج إلى تنفيذ الإجراءات التالية:

1. Load the PDF file - new [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object.

1. تحميل ملف PDF - إنشاء كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) جديد.

1. Create annotations:

1. إنشاء التعليقات التوضيحية:

    - [HighlightAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/HighlightAnnotation) and set parameters (title, color).

    - [HighlightAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/HighlightAnnotation) وتعيين المعلمات (العنوان، اللون).- [StrikeOutAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/StrikeOutAnnotation) وتعيين المعلمات (العنوان، اللون).
- [SquigglyAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/SquigglyAnnotation) وتعيين المعلمات (العنوان، اللون).
- [UnderlineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/UnderlineAnnotation) وتعيين المعلمات (العنوان، اللون).

1. بعد ذلك، يجب علينا إضافة جميع التعليقات التوضيحية إلى الصفحة.

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleTextMarkupAnnotation {
    // المسار إلى دليل المستندات.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddTextMarkupAnnotation() {
        try {
            // تحميل ملف PDF
            Document document = new Document(_dataDir + "sample.pdf");
            Page page = document.getPages().get_Item(1);
            TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
            tfa.visit(page);

            // إنشاء التعليقات التوضيحية
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

            // إضافة التعليقات التوضيحية إلى الصفحة
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


إذا كنت تريد تمييز جزء متعدد الأسطر، يجب عليك استخدام المثال المتقدم:

```java
    /// <summary>
    /// مثال متقدم إذا كنت تريد تمييز جزء متعدد الأسطر
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
    /// كيفية الحصول على النص المميز
    /// </summary>
    public static void GetHighlightedText() {
        // تحميل ملف PDF
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


## الحصول على تعليق توضيحي لنص

يرجى محاولة استخدام مقتطف الشيفرة التالي للحصول على تعليق توضيحي لنص من مستند PDF.

```java
     public static void GetTextMarkupAnnotation() {
        // تحميل ملف PDF
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

        // طباعة النتائج
        for (Annotation ta : textMarkupAnnotations) {
            System.out.printf("[" + ta.getAnnotationType() + ta.getRect() + "]");
        }
    }
```


## حذف تعليق تمييز النص

يوضح مقطع الشيفرة التالي كيفية حذف تعليق تمييز النص من ملف PDF.

```java
   public static void DeleteTextMarkupAnnotation() {
        // تحميل ملف PDF
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

        // طباعة النتائج
        for (Annotation ta : textMarkupAnnotations) {
            page.getAnnotations().delete(ta);
        }
        document.save(_dataDir + "sample_del.pdf");
    }
```