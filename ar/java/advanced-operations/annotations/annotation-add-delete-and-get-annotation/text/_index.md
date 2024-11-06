---
title: PDF Text Annotation
Texttitle: Text Annotation
type: docs
weight: 10
url: ar/java/text-annotation/
description: Aspose.PDF for Java يسمح لك بإضافة، الحصول على، وحذف تعليقات النص من مستند PDF الخاص بك.
lastmod: "2021-11-24"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

إضافة، حذف، والحصول على تعليق متشابهة لأنواع مختلفة من التعليقات. دعنا نأخذ مثالاً على تعليق النص.

## كيفية إضافة تعليق نص إلى ملف PDF موجود

في هذا البرنامج التعليمي، ستتعلم كيفية إضافة النص إلى مستند PDF موجود. تتيح لك أداة النص إضافة النص في أي مكان في المستند. تعليق النص هو تعليق مرتبط بموقع محدد في مستند PDF. عند إغلاقه، يتم عرض التعليق كأيقونة؛ وعند فتحه، يجب أن يعرض نافذة منبثقة تحتوي على نص الملاحظة بالخط والحجم الذي يختاره القارئ.

يتم احتواء التعليقات بواسطة مجموعة [Annotations](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/AnnotationCollection) من صفحة معينة.
 هذا التجميع يحتوي على التعليقات التوضيحية لتلك الصفحة الفردية فقط؛ كل صفحة لها تجميع التعليقات التوضيحية الخاص بها.

لإضافة تعليق توضيحي إلى صفحة معينة، أضفه إلى تجميع التعليقات التوضيحية لتلك الصفحة باستخدام طريقة Add.

1. أولاً، قم بإنشاء التعليق التوضيحي الذي تريد إضافته إلى ملف PDF.
2. ثم افتح ملف PDF المدخل.
3. أضف التعليق التوضيحي إلى تجميع التعليقات التوضيحية لكائن [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).

يعرض لك مقطع الشيفرة التالي كيفية إضافة تعليق توضيحي في صفحة PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleTextAnnotation {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    public static void AddTextAnnotation()
    {
        // تحميل ملف PDF
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);
        Rectangle rect = new Rectangle(200, 750, 400, 790);
        TextAnnotation textAnnotation = new TextAnnotation(page, rect);

        textAnnotation.setTitle("Aspose User");
        textAnnotation.setSubject("Sample Subject");
        textAnnotation.setState (AnnotationState.Accepted);
        textAnnotation.setContents("Sample contents for the annotation");
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

## إضافة تعليق نص حر جديد (أو إنشاء)

يعرض التعليق النصي الحر النص مباشرة على الصفحة. تتيح طريقة PdfContentEditor.CreateFreeText إنشاء هذا النوع من التعليقات. في المقتطف التالي، نضيف تعليق نص حر فوق أول ظهور للسلسلة.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleFreeTextAnnotation {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    public static void AddFreeTextAnnotation()
    {
        // تحميل ملف PDF
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        DefaultAppearance defaultAppearance = new DefaultAppearance();
        defaultAppearance.setFontName("Helvetica");
        defaultAppearance.setFontSize(12);
        defaultAppearance.setTextColor(java.awt.Color.BLUE);

        FreeTextAnnotation freeTextAnnotation = new FreeTextAnnotation(page, new Rectangle(300.0, 770.0, 400.0, 790.0), defaultAppearance);

        freeTextAnnotation.setRichText("عرض نص حر");
        page.getAnnotations().add(freeTextAnnotation);
        document.save(_dataDir + "sample_freetext.pdf");
    }
}
```


## الحصول على تعليق نصي مجاني

Aspose.PDF لـ Java يتيح لك الحصول على تعليق نصي مجاني من مستند PDF الخاص بك.

يرجى التحقق من مقتطف الشيفرة التالي لحل هذه المهمة:

```java
public static void GetFreeTextAnnotation() {
        // تحميل ملف PDF
        Document document = new Document(_dataDir + "sample_freetext.pdf");

        // تصفية التعليقات باستخدام AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new FreeTextAnnotation(page, Rectangle.getTrivial(), new DefaultAppearance()));
        page.accept(annotationSelector);
        List<Annotation> freeTextAnnotations = annotationSelector.getSelected();

        // طباعة النتائج
        for (Annotation fa : freeTextAnnotations) {
            System.out.println(fa.getRect());
        }
    }
```

## حذف تعليق نصي مجاني

Aspose.PDF لـ Java يتيح لك حذف تعليق نصي مجاني من مستند PDF الخاص بك.

يرجى التحقق من مقتطف الشيفرة التالي لحل هذه المهمة:

```java
  public static void DeleteFreeTextAnnotation() {
         // تحميل ملف PDF
         Document document = new Document(_dataDir + "sample_freetext.pdf");

         // تصفية التعليقات التوضيحية باستخدام AnnotationSelector
         Page page = document.getPages().get_Item(1);
         AnnotationSelector annotationSelector = new AnnotationSelector(
                 new FreeTextAnnotation(page, Rectangle.getTrivial(), new DefaultAppearance()));
         page.accept(annotationSelector);
         List<Annotation> freeTextAnnotations = annotationSelector.getSelected();

         // حذف التعليقات التوضيحية
         for (Annotation fa : freeTextAnnotations) {
            page.getAnnotations().delete(fa);
        }
        document.save(_dataDir + "sample_freetext_del.pdf");
    }
```

## حذف جميع التعليقات التوضيحية من صفحة في ملف PDF

تحتوي مجموعة [AnnotationCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/AnnotationCollection) الخاصة بكائن [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) على جميع التعليقات التوضيحية لتلك الصفحة المعينة.
 لحذف جميع التعليقات التوضيحية من صفحة، قم باستدعاء طريقة *Delete* من مجموعة AnnotationCollection.

يوضح لك مقطع الشيفرة التالي كيفية حذف جميع التعليقات التوضيحية من صفحة معينة.

```java
    public static void DeleteTextAnnotation() {
         // تحميل ملف PDF
         Document document = new Document(_dataDir + "sample_textannot.pdf");

         // تصفية التعليقات التوضيحية باستخدام AnnotationSelector
         Page page = document.getPages().get_Item(1);
         AnnotationSelector annotationSelector = new AnnotationSelector(
                 new TextAnnotation(page, Rectangle.getTrivial()));
         page.accept(annotationSelector);
         List<Annotation> TextAnnotations = annotationSelector.getSelected();

         // حذف التعليقات التوضيحية
         for (Annotation fa : TextAnnotations) {
            page.getAnnotations().delete(fa);
        }
        document.save(_dataDir + "sample_textannot_del.pdf");
    }
```

## الحصول على جميع التعليقات التوضيحية من صفحة مستند PDF

تسمح لك Aspose.PDF بالحصول على التعليقات التوضيحية من مستند كامل أو من صفحة معينة. للحصول على جميع التعليقات التوضيحية من الصفحة في مستند PDF، قم بالمرور عبر مجموعة [AnnotationCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/AnnotationCollection) لموارد الصفحة المطلوبة. يوضح لك مقطع الشفرة التالي كيفية الحصول على جميع التعليقات التوضيحية لصفحة.

```java
  public static void GetTextAnnotation() {
        // تحميل ملف PDF
        Document document = new Document(_dataDir + "sample_textannot.pdf");

        // تصفية التعليقات التوضيحية باستخدام AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new TextAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> TextAnnotations = annotationSelector.getSelected();

        // طباعة النتائج
        for (Annotation fa : TextAnnotations) {
            System.out.println(fa.getRect());
        }
    }
```