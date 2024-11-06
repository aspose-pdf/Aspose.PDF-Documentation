---
title: استخدام أنواع إضافية من تعليقات PDF التوضيحية
linktitle: التعليقات التوضيحية الإضافية
type: docs
weight: 60
url: ar/java/extra-annotations/
description: يصف هذا القسم كيفية إضافة، والحصول على، وحذف أنواع إضافية من التعليقات التوضيحية في مستند PDF الخاص بك.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## كيفية إضافة تعليق توضيحي على شكل Caret إلى ملف PDF موجود

التعليق التوضيحي على شكل Caret هو رمز يشير إلى تحرير النص. التعليق التوضيحي على شكل Caret هو أيضًا تعليق توضيحي للترميز، لذا فإن فئة Caret مشتقة من فئة Markup وتوفر أيضًا وظائف للحصول على أو تعيين خصائص التعليق التوضيحي على شكل Caret وإعادة ضبط تدفق مظهر التعليق التوضيحي على شكل Caret.

الخطوات التي نستخدمها لإنشاء تعليق توضيحي على شكل Caret:

1. تحميل ملف PDF - جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. قم بإنشاء [Caret Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/CaretAnnotation) جديد واضبط معلمات Caret (مستطيل جديد، العنوان، الموضوع، العلامات، اللون، العرض، نمط البداية ونمط النهاية). يتم استخدام هذا التعليق للإشارة إلى إدراج النص.
1. قم بإنشاء [StrikeOutAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/StrikeOutAnnotation) جديد واضبط المعلمات (مستطيل جديد، العنوان، اللون، نقاط رباعية جديدة ونقاط جديدة، الموضوع، InReplyTo، ReplyType).
1. بعد ذلك يمكننا إضافة التعليقات إلى الصفحة.

يظهر مقطع الشيفرة التالي كيفية إضافة Caret Annotation إلى ملف PDF:

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleCaretAnnotation {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddCaretAnnotation() {
        // تحميل ملف PDF
        Document document = new Document(_dataDir + "sample.pdf");
        // يتم استخدام هذا التعليق للإشارة إلى إدراج النص
        CaretAnnotation caretAnnotation1 = new CaretAnnotation(
                document.getPages().get_Item(1), new Rectangle(299.988, 713.664, 308.708, 720.769));
        caretAnnotation1.setTitle("Aspose User");
        caretAnnotation1.setSubject("Inserted text 1");
        caretAnnotation1.setFlags(AnnotationFlags.Print);
        caretAnnotation1.setColor(Color.getBlue());

        // يتم استخدام هذا التعليق للإشارة إلى استبدال النص
        CaretAnnotation caretAnnotation2 = new CaretAnnotation(
                document.getPages().get_Item(1), new Rectangle(361.246, 727.908, 370.081, 735.107));

        caretAnnotation2.setTitle("Aspose User");
        caretAnnotation2.setFlags(AnnotationFlags.Print);
        caretAnnotation2.setSubject("Inserted text 2");
        caretAnnotation2.setColor(Color.getBlue());

        StrikeOutAnnotation strikeOutAnnotation = new StrikeOutAnnotation(
                document.getPages().get_Item(1), new Rectangle(318.407, 727.826, 368.916, 740.098));

        strikeOutAnnotation.setColor(Color.getBlue());
        strikeOutAnnotation.setQuadPoints(new Point[] { new Point(321.66, 739.416),
                new Point(365.664, 739.416), new Point(321.66, 728.508),
                new Point(365.664, 728.508) });

        strikeOutAnnotation.setSubject("Cross-out");
        strikeOutAnnotation.setInReplyTo(caretAnnotation2);
        strikeOutAnnotation.setReplyType(ReplyType.Group);

        document.getPages().get_Item(1).getAnnotations().add(caretAnnotation1);
        document.getPages().get_Item(1).getAnnotations().add(caretAnnotation2);
        document.getPages().get_Item(1).getAnnotations().add(strikeOutAnnotation);

        document.save(_dataDir + "sample_caret.pdf");

    }
```


## الحصول على تعليق توضيحي

يرجى محاولة استخدام مقتطف الشيفرة التالي للحصول على تعليق توضيحي في مستند PDF

```java
    public static void GetCaretAnnotation() {
        // تحميل ملف PDF
        Document document = new Document(_dataDir + "sample_caret.pdf");

        // تصفية التعليقات التوضيحية باستخدام AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new CaretAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> caretAnnotations = annotationSelector.getSelected();

        // طباعة النتائج
        for (Annotation ca : caretAnnotations) {
            System.out.println(ca.getRect());
        }
    }
```

## حذف تعليق توضيحي

يوضح مقتطف الشيفرة التالي كيفية حذف تعليق توضيحي من ملف PDF.

```java
public static void DeleteCaretAnnotation() {
        // تحميل ملف PDF
        Document document = new Document(_dataDir + "sample_caret.pdf");

        // تصفية التعليقات التوضيحية باستخدام AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new CaretAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> caretAnnotations = annotationSelector.getSelected();

        // حذف التعليق التوضيحي
        for (Annotation ca : caretAnnotations) {
            document.getPages().get_Item(1).getAnnotations().delete(ca);
        }
        document.save(_dataDir + "sample_caret_del.pdf");
    }
```


A [Link Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) هو رابط نص تشعبي يؤدي إلى وجهة في مكان آخر في المستند أو إلى إجراء ليتم تنفيذه.

## إضافة تعليق توضيحي للرابط

الرابط هو منطقة مستطيلة يمكن وضعها في أي مكان على الصفحة. يحتوي كل رابط على إجراء PDF المقابل المرتبط به. يتم تنفيذ هذا الإجراء عندما ينقر المستخدم في منطقة هذا الرابط.

يعرض مقطع الشيفرة التالي كيفية إضافة تعليق توضيحي للرابط إلى ملف PDF باستخدام مثال رقم الهاتف:

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleLinkAnnotation {

    // المسار إلى دليل المستندات.

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddLinkAnnotation() {
        try {
            // تحميل ملف PDF
            Document document = new Document(_dataDir + "SimpleResume.pdf");
            Page page = document.getPages().get_Item(1);

            // إنشاء كائن TextFragmentAbsorber للعثور على رقم هاتف
            TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("678-555-0103");

            // قبول الممتص للصفحة الأولى فقط
            page.accept(textFragmentAbsorber);

            TextFragment phoneNumberFragment = textFragmentAbsorber.getTextFragments().get_Item(1);

            // إنشاء تعليق توضيحي للرابط وتعيين الإجراء للاتصال برقم هاتف
            LinkAnnotation linkAnnotation = new LinkAnnotation(page, phoneNumberFragment.getRectangle());
            linkAnnotation.setAction(new GoToURIAction("callto:678-555-0103"));

            // إضافة التعليق التوضيحي إلى الصفحة
            page.getAnnotations().add(linkAnnotation);
            document.save(_dataDir + "SimpleResume_mod.pdf");
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
```


## الحصول على تعليقات الارتباط

يرجى محاولة استخدام شفرة البرنامج التالية للحصول على LinkAnnotation من مستند PDF.

```java
    public static void GetLinkAnnotations() {

        // تحميل ملف PDF
        Document document = new Document(_dataDir + "SimpleResume_mod.pdf");

        // تصفية التعليقات باستخدام AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> linkAnnotations = annotationSelector.getSelected();

        // طباعة النتائج
        for (Annotation la : linkAnnotations) {

            LinkAnnotation l = (LinkAnnotation) la;

            // طباعة عنوان URL لكل تعليق ارتباط
            System.out.println("URI: " + ((GoToURIAction) l.getAction()).getURI());

            TextAbsorber absorber = new TextAbsorber();
            absorber.getTextSearchOptions().setLimitToPageBounds(true);
            absorber.getTextSearchOptions().setRectangle(l.getRect());
            page.accept(absorber);

            String extractedText = absorber.getText();

            // طباعة النص المرتبط بالرابط
            System.out.println(extractedText);
        }
    }
```


## حذف تعليق الرابط

يُظهر مقتطف الشيفرة التالي كيفية حذف تعليق الرابط من ملف PDF. لهذا، نحتاج إلى العثور وإزالة جميع تعليقات الروابط في الصفحة الأولى. بعد ذلك، سنحفظ المستند مع إزالة التعليقات.

```java
    public static void DeleteLinkAnnotations() {
        // تحميل ملف PDF
        Document document = new Document(_dataDir + "SimpleResume_mod.pdf");

        // تصفية التعليقات باستخدام AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> linkAnnotations = annotationSelector.getSelected();

        for (Annotation la : linkAnnotations)
            page.getAnnotations().delete(la);

        // حفظ المستند مع إزالة التعليقات
        document.save(_dataDir + "SimpleResume_del.pdf");
    }
```

## تنقيح منطقة معينة من الصفحة باستخدام تعليق التنقيح باستخدام Aspose.PDF for Java

Aspose.PDF لـ Java يدعم ميزة إضافة وكذلك معالجة التعليقات التوضيحية في ملف PDF موجود. مؤخرًا قام بعض عملائنا بنشر طلب لحجب (إزالة النصوص، الصور، إلخ من) منطقة معينة من صفحات مستند PDF. من أجل تلبية هذا المتطلب، تم توفير فئة باسم RedactionAnnotation، والتي يمكن استخدامها لحجب مناطق معينة من الصفحة أو يمكن استخدامها لمعالجة التعليقات التوضيحية للحجب الموجودة وحجبها (أي تسطيح التعليق وإزالة النص تحته).

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.PdfAnnotationEditor;

public class ExampleRedactAnnotation {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void RedactionAnnotation() {

        // فتح المستند
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        // إنشاء مثيل RedactionAnnotation لمنطقة صفحة محددة
        RedactionAnnotation annot = new RedactionAnnotation(page, new Rectangle(200, 500, 300, 600));
        annot.setFillColor(Color.getGreen());
        annot.setBorderColor(Color.getYellow());
        annot.setColor(Color.getBlue());

        // النص المراد طباعته على تعليق الحجب
        annot.setOverlayText("REDACTED");
        annot.setTextAlignment(HorizontalAlignment.Center);

        // تكرار النص المغطى على تعليق الحجب
        annot.setRepeat(true);

        // إضافة التعليق إلى مجموعة التعليقات التوضيحية للصفحة الأولى
        page.getAnnotations().add(annot);

        // تسطيح التعليق وحجب محتويات الصفحة (أي إزالة النص والصورة
        // تحت التعليق المحجوب)
        annot.redact();
        document.save(_dataDir + "RedactPage_out.pdf");
    }
```


## نهج الواجهات

توفر مساحة الأسماء Aspose.PDF.Facades أيضًا فئة تسمى [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) والتي توفر ميزة التلاعب بالتعليقات التوضيحية الموجودة داخل ملف PDF. تحتوي هذه الفئة على طريقة تسمى [RedactArea(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Redaction#getredactArea-com.aspose.pdf.Page-com.aspose.pdf.Rectangle-java.awt.Color-) والتي توفر القدرة على إزالة مناطق معينة من الصفحة.

```java
    public static void RedactionAnnotationFacades(){
        PdfAnnotationEditor editor = new PdfAnnotationEditor();

        editor.bindPdf(_dataDir + "sample.pdf");

        // إزالة منطقة معينة من الصفحة
        editor.redactArea(1, new Rectangle(100, 100, 20, 70), java.awt.Color.white);
        editor.bindPdf(_dataDir + "sample.pdf");
        editor.save( _dataDir + "FacadesApproach_out.pdf");
    }
```