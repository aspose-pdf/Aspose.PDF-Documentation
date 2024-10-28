---
title: إضافة رأس وتذييل إلى ملف PDF
linktitle: إضافة رأس وتذييل
type: docs
weight: 70
url: /java/add-headers-and-footers-of-pdf-file/
description: يسمح لك Aspose.PDF for Java بإضافة رؤوس وتذييلات إلى ملف PDF الخاص بك باستخدام فئة TextStamp.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

تُستخدم الطوابع في ملفات PDF بشكل شائع في العقود والتقارير والمواد المحظورة لإثبات أن الوثائق قد تمت مراجعتها وتم وضع علامة عليها على أنها "مقروءة" أو "مؤهلة" أو "سرية"، إلخ. ستوضح لك هذه المقالة كيفية إضافة طوابع صور وطوابع نصية إلى مستندات PDF باستخدام **Aspose.PDF for Java**.

إذا قمت بقراءة الشيفرات البرمجية أعلاه سطرًا بسطر، يجب أن تجد أن البنية المنطقية للشيفرة سهلة الفهم.

## إضافة نص في رأس ملف PDF

يمكنك استخدام فئة [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) لإضافة نص في رأس ملف PDF.
 توفر فئة TextStamp الخصائص اللازمة لإنشاء ختم قائم على النص مثل حجم الخط ونمط الخط ولون الخط وما إلى ذلك. لإضافة نص في الرأس، تحتاج إلى إنشاء كائن Document وكائن TextStamp باستخدام الخصائص المطلوبة. بعد ذلك، يمكنك استدعاء طريقة AddStamp للصفحة لإضافة النص في رأس ملف PDF.

تحتاج إلى ضبط خاصية TopMargin بطريقة تعدل النص في منطقة الرأس لملف PDF الخاص بك. تحتاج أيضًا إلى ضبط HorizontalAlignment على Center وVerticalAlignment على Top.

يوضح لك جزء الشيفرة التالي كيفية إضافة نص في رأس ملف PDF باستخدام Java.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleAddPDFHeaderandFooter {
    // المسار إلى دليل المستندات.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddingTextInHeaderOfPDFFile() {

        // فتح المستند
        Document pdfDocument = new Document(_dataDir + "TextinHeader.pdf");

        // إنشاء الرأس
        TextStamp textStamp = new TextStamp("Header Text");

        // تعيين خصائص الختم
        textStamp.setTopMargin(10);
        textStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        textStamp.setVerticalAlignment(VerticalAlignment.Top);

        // إضافة الرأس على جميع الصفحات
        for (Page page : pdfDocument.getPages()) {
            page.addStamp(textStamp);
        }

        // حفظ المستند المحدث
        pdfDocument.save(_dataDir + "TextinHeader_out.pdf");
    }
```

## إضافة نص في تذييل ملف PDF

يمكنك استخدام فئة TextStamp لإضافة نص في تذييل ملف PDF. توفر فئة TextStamp الخصائص اللازمة لإنشاء ختم نصي مثل حجم الخط، نمط الخط، ولون الخط إلخ. لإضافة نص في التذييل، تحتاج إلى إنشاء كائن Document وكائن TextStamp باستخدام الخصائص المطلوبة. بعد ذلك، يمكنك استدعاء طريقة AddStamp للصفحة لإضافة النص في تذييل ملف PDF.

يوضح لك جزء الشيفرة التالي كيفية إضافة نص في تذييل ملف PDF باستخدام Java.

```java
    public static void AddingTextInFooterOfPDFFile() {
        // فتح المستند
        Document pdfDocument = new Document(_dataDir + "TextinFooter.pdf");
        // إنشاء تذييل
        TextStamp textStamp = new TextStamp("Footer Text");
        // ضبط خصائص الختم
        textStamp.setBottomMargin(10);
        textStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        textStamp.setVerticalAlignment(VerticalAlignment.Bottom);
        // إضافة التذييل على جميع الصفحات
        for (Page page : pdfDocument.getPages()) {
            page.addStamp(textStamp);
        }
        _dataDir = _dataDir + "TextinFooter_out.pdf";
        // حفظ ملف PDF المحدث
        pdfDocument.save(_dataDir);
    }
```


## إضافة صورة في رأس ملف PDF

يمكنك استخدام فئة [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp) لإضافة صورة في رأس ملف PDF. توفر فئة الختم الصوري الخصائص الضرورية لإنشاء ختم يعتمد على الصورة مثل حجم الخط، نمط الخط، ولون الخط الخ. من أجل إضافة صورة في الرأس، تحتاج إلى إنشاء كائن مستند وكائن ختم صورة باستخدام الخصائص المطلوبة. بعد ذلك، يمكنك استدعاء طريقة [AddStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/class-use/Stamp) الخاصة بالصفحة لإضافة الصورة في رأس ملف PDF.

```java
public static void AddingImageInHeaderOfPDFFile() {

// افتح المستند
Document pdfDocument = new Document(_dataDir + "ImageInHeader.pdf");

// إنشاء الرأس
ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.jpg");

// ضبط خصائص الختم
imageStamp.setTopMargin(10);
imageStamp.setHorizontalAlignment(HorizontalAlignment.Center);
imageStamp.setVerticalAlignment(VerticalAlignment.Top);
// إضافة رأس في جميع الصفحات
for (Page page : pdfDocument.getPages()) {
page.addStamp(imageStamp);
}

_dataDir = _dataDir + "ImageInHeader_out.pdf";

// حفظ ملف PDF المحدث
pdfDocument.save(_dataDir);
}
```


يظهر لك جزء الشيفرة التالي كيفية إضافة صورة في رأس ملف PDF باستخدام Java.

## إضافة صورة في تذييل ملف PDF

يمكنك استخدام فئة Image Stamp لإضافة صورة في تذييل ملف PDF. توفر فئة Image Stamp الخصائص اللازمة لإنشاء ختم قائم على الصورة مثل حجم الخط، نمط الخط، ولون الخط وما إلى ذلك. من أجل إضافة صورة في التذييل، تحتاج إلى إنشاء كائن Document وكائن Image Stamp باستخدام الخصائص المطلوبة. بعد ذلك، يمكنك استدعاء طريقة AddStamp للصفحة لإضافة الصورة في تذييل ملف PDF.

{{% alert color="primary" %}}

تحتاج إلى ضبط خاصية BottomMargin بطريقة تجعلها تعدل الصورة في منطقة تذييل ملف PDF الخاص بك. تحتاج أيضًا إلى ضبط [HorizontalAlignment](https://reference.aspose.com/pdf/java/com.aspose.pdf/HorizontalAlignment) على `Center` و [VerticalAlignment](https://reference.aspose.com/pdf/java/com.aspose.pdf/VerticalAlignment) على `Bottom`.

{{% /alert %}}

يظهر لك جزء الشيفرة التالي كيفية إضافة صورة في تذييل ملف PDF باستخدام Java.

```java
    public static void AddingImageInFooterOfPDFFile() {

        // فتح المستند
        Document pdfDocument = new Document(_dataDir + "ImageInFooter.pdf");

        // إنشاء تذييل الصفحة
        ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.jpg");

        // تعيين خصائص الختم
        imageStamp.setBottomMargin(10);
        imageStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        imageStamp.setVerticalAlignment(VerticalAlignment.Bottom);
        // إضافة تذييل الصفحة على جميع الصفحات
        for (Page page : pdfDocument.getPages()) {
            page.addStamp(imageStamp);
        }

        _dataDir = _dataDir + "ImageInFooter_out.pdf";

        // حفظ ملف PDF المحدث
        pdfDocument.save(_dataDir);
    }
```

## إضافة رؤوس مختلفة في ملف PDF واحد

نعلم أنه يمكننا إضافة TextStamp في قسم الرأس/التذييل في المستند باستخدام خصائص TopMargin أو Bottom Margin، ولكن أحيانًا قد يكون لدينا متطلبات لإضافة رؤوس/تذييلات متعددة في مستند PDF واحد.
 **Aspose.PDF for Java** يوضح كيفية القيام بذلك.

من أجل تحقيق هذا المطلب، سنقوم بإنشاء كائنات [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) فردية (عدد الكائنات يعتمد على عدد الرؤوس/التذييلات المطلوبة) وسنضيفها إلى مستند PDF. يمكننا أيضًا تحديد معلومات تنسيق مختلفة لكائن الطابع الفردي. في المثال التالي، قمنا بإنشاء كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) وثلاثة كائنات [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) ثم استخدمنا طريقة [AddStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/class-use/Stamp) الخاصة بالصفحة لإضافة النص في القسم العلوي من مستند PDF. يوضح لك المقتطف البرمجي التالي كيفية إضافة صورة في تذييل ملف PDF باستخدام Aspose.PDF for Java.

```java
public static void AddingDifferentHeadersInOnePDFFile() {

        // افتح المستند المصدر
        Document pdfDocument = new Document(_dataDir + "AddingDifferentHeaders.pdf");

        // إنشاء ثلاثة طوابع
        TextStamp stamp1 = new TextStamp("Header 1");
        TextStamp stamp2 = new TextStamp("Header 2");
        TextStamp stamp3 = new TextStamp("Header 3");

        // تعيين محاذاة الطابع (وضع الطابع في الجزء العلوي من الصفحة، محاذاة أفقية في الوسط)
        stamp1.setVerticalAlignment (VerticalAlignment.Top);
        stamp1.setHorizontalAlignment(HorizontalAlignment.Center);
        // تحديد نمط الخط كـ Bold
        stamp1.getTextState().setFontStyle(FontStyles.Bold);
        // تعيين معلومات لون الخط الأحمر
        stamp1.getTextState().setForegroundColor(Color.getRed());
        // تحديد حجم الخط كـ 14
        stamp1.getTextState().setFontSize(14);

        // الآن نحتاج إلى تعيين المحاذاة الرأسية للكائن الثاني كـ Top
        stamp2.setVerticalAlignment(VerticalAlignment.Top);
        // تعيين معلومات المحاذاة الأفقية للطابع كـ Center
        stamp2.setHorizontalAlignment(HorizontalAlignment.Center);
        // تعيين عامل التكبير لكائن الطابع
        stamp2.setZoom (10);

        // تعيين تنسيق الكائن الثالث
        // تحديد معلومات المحاذاة الرأسية للطابع كـ TOP
        stamp3.setVerticalAlignment(VerticalAlignment.Top);
        // تعيين معلومات المحاذاة الأفقية للطابع كـ Center
        stamp3.setHorizontalAlignment (HorizontalAlignment.Center);
        // تعيين زاوية الدوران للطابع
        stamp3.setRotateAngle(35);
        // تعيين اللون الوردي كلون خلفية للطابع
        stamp3.getTextState().setBackgroundColor (Color.getPink());
        
        // تغيير معلومات نوع الخط للطابع إلى Verdana
        stamp3.getTextState().setFont (FontRepository.findFont("Verdana"));
        // الطابع الأول يُضاف على الصفحة الأولى؛
        pdfDocument.getPages().get_Item(1).addStamp(stamp1);
        // الطابع الثاني يُضاف على الصفحة الثانية؛
        pdfDocument.getPages().get_Item(2).addStamp(stamp2);
        // الطابع الثالث يُضاف على الصفحة الثالثة.
        pdfDocument.getPages().get_Item(3).addStamp(stamp3);

        _dataDir = _dataDir + "multiheader_out.pdf";

        // حفظ ملف PDF المحدث
        pdfDocument.save(_dataDir);
    }

}
```