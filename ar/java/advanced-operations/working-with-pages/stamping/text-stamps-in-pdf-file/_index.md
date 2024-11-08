---
title: إضافة أختام نصية في PDF برمجياً
linktitle: الأختام النصية في ملف PDF
type: docs
weight: 20
url: /ar/java/text-stamps-in-the-pdf-file/
description: إضافة ختم نصي إلى ملف PDF باستخدام فئة TextStamp مع Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## إضافة ختم نصي باستخدام Java

يوفر Aspose.PDF for Java فئة [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) لإضافة ختم نصي في ملف PDF.
 [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) توفر الفئة الأساليب اللازمة لتحديد حجم الخط، نمط الخط، ولون الخط وما إلى ذلك لكائن الختم. من أجل إضافة ختم نصي، أولاً تحتاج إلى إنشاء كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) وكائن [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) باستخدام الأساليب المطلوبة. بعد ذلك، يمكنك استدعاء أسلوب [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) من فئة [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) لإضافة الختم في مستند PDF.

يعرض لك مقطع الشيفرة التالي كيفية إضافة ختم نصي في ملف PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.*;
import com.aspose.pdf.facades.Stamp;

public class ExampleStampingImage {
    // المسار إلى دليل المستندات.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddTextStamp() {
        // فتح المستند
        Document pdfDocument = new Document("input.pdf");
        // إنشاء ختم نصي
        TextStamp textStamp = new TextStamp("Sample Stamp");
        // تعيين ما إذا كان الختم هو الخلفية
        textStamp.setBackground(true);
        // تعيين الأصل
        textStamp.setXIndent(100);
        textStamp.setYIndent(100);
        // تدوير الختم
        textStamp.setRotate(Rotation.on90);
        // تعيين خصائص النص
        textStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        textStamp.getTextState().setFontSize(14.0F);
        textStamp.getTextState().setFontStyle(FontStyles.Bold);
        textStamp.getTextState().setFontStyle(FontStyles.Italic);
        textStamp.getTextState().setForegroundColor(Color.getGreen());
        // إضافة الختم إلى صفحة معينة
        pdfDocument.getPages().get_Item(1).addStamp(textStamp);
        // حفظ مستند الإخراج
        pdfDocument.save("TextStamp_output.pdf");
    }
```

## تعريف المحاذاة لكائن TextStamp

إضافة العلامات المائية إلى مستندات PDF هي واحدة من الميزات المطلوبة بشكل متكرر وAspose.PDF لـ Java قادر تمامًا على إضافة صور وكذلك علامات مائية نصية. توفر فئة [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) ميزة إضافة الأختام النصية فوق ملف PDF. مؤخرًا كانت هناك حاجة لدعم ميزة تحديد محاذاة النص عند استخدام كائن [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp). لذا من أجل تلبية هذا الطلب، قمنا بتقديم طريقة setTextAlignment(..) في فئة [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp). باستخدام هذه الطريقة، يمكنك تحديد محاذاة النص الأفقية.

توضح مقتطفات الشيفرة التالية مثالاً على كيفية تحميل مستند PDF موجود وإضافة [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) فوقه.

```java
    public static void DefineAlignmentTextStamp() {
        // إنشاء كائن Document مع ملف الإدخال
        Document pdfDocument = new Document("input.pdf");
        // إنشاء كائن FormattedText مع سلسلة نصية مثال
        FormattedText text = new FormattedText("This");
        
        // إضافة سطر نصي جديد إلى FormattedText
        text.addNewLineText("is sample");
        text.addNewLineText("Center Aligned");
        text.addNewLineText("TextStamp");
        text.addNewLineText("Object");
        // إنشاء كائن TextStamp باستخدام FormattedText
        TextStamp stamp = new TextStamp(text);
        // تحديد المحاذاة الأفقية لختم النص كمحاذاة مركزية
        stamp.setHorizontalAlignment(HorizontalAlignment.Center);
        // تحديد المحاذاة الرأسية لختم النص كمحاذاة مركزية
        stamp.setVerticalAlignment(VerticalAlignment.Center);
        // تحديد المحاذاة الأفقية للنص لختم النص كمحاذاة مركزية
        stamp.setTextAlignment(HorizontalAlignment.Center);
        // ضبط الهامش العلوي لكائن الختم
        stamp.setTopMargin(20);
        // إضافة الختم إلى جميع صفحات ملف PDF
        pdfDocument.getPages().get_Item(1).addStamp(stamp);
        
        // حفظ مستند الإخراج
        pdfDocument.save("TextStamp_output.pdf");
    }
```


## ملء نص الحدود كختم في ملف PDF

لقد قمنا بتنفيذ إعداد وضع العرض لسيناريوهات إضافة النص وتحريره. لعرض نص الحدود، يرجى إنشاء كائن [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextState) وضبط RenderingMode إلى TextRenderingMode.StrokeText وأيضًا اختيار اللون لخاصية StrokingColor. لاحقًا، اربط TextState بالختم باستخدام طريقة BindTextState().

يُوضح مقتطف الشيفرة التالي كيفية إضافة نص ملء الحدود:

```java
   public static void FillStrokeTextAsStampInPDFFile(){
        // إنشاء كائن TextState لنقل الخصائص المتقدمة
        TextState ts = new TextState();
        
        // تعيين اللون للحدود
        ts.setStrokingColor(Color.getGray());
        
        // تعيين وضع عرض النص
        ts.setRenderingMode (TextRenderingMode.StrokeText);
        
        // تحميل مستند PDF مدخل
        PdfFileStamp fileStamp = new PdfFileStamp(new Document(_dataDir + "input.pdf"));

        Stamp stamp = new Stamp();
        stamp.bindLogo(new FormattedText("PAID IN FULL", java.awt.Color.GRAY, "Arial", EncodingType.Winansi, true, 78));

        // ربط TextState
        stamp.bindTextState(ts);
        // تعيين أصل X,Y
        stamp.setOrigin(100, 100);
        stamp.setOpacity (5);
        stamp.setBlendingSpace (BlendingColorSpace.DeviceRGB);
        stamp.setRotation (45.0F);
        stamp.setBackground(false);
        // إضافة الختم
        fileStamp.addStamp(stamp);
        fileStamp.save(_dataDir + "ouput_out.pdf");
        fileStamp.close();
    }
```