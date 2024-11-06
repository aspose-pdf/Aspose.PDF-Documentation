---
title: إضافة ختم صورة في ملف PDF برمجياً
linktitle: أختام الصور في ملف PDF
type: docs
weight: 10
url: ar/java/image-stamps-in-pdf-page/
description: أضف ختم الصورة في مستند PDF الخاص بك باستخدام فئة ImageStamp مع مكتبة Aspose.PDF لـ Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## إضافة ختم صورة في ملف PDF

يمكنك استخدام فئة [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) لإضافة صورة كختم في مستند PDF. توفر فئة [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) طرقًا لتحديد الارتفاع والعرض والشفافية وغيرها.

لإضافة ختم صورة:

1. قم بإنشاء كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) وكائن ImageStamp باستخدام الخصائص المطلوبة.

1. استدعاء طريقة [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) من فئة [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) لإضافة الطابع إلى ملف الـ PDF.

يوضح مقتطف الكود التالي كيفية إضافة طابع صورة في ملف PDF.

```java
public static void AddImageStampInPDFFile() {
        // فتح المستند
        Document pdfDocument = new Document(_dataDir + "AddImageStamp.pdf");

        // إنشاء طابع الصورة
        ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.png");
        imageStamp.setBackground(true);
        imageStamp.setXIndent(100);
        imageStamp.setYIndent(100);
        imageStamp.setHeight(48);
        imageStamp.setWidth(225);
        imageStamp.setRotate(Rotation.on270);
        imageStamp.setOpacity(0.5);

        // إضافة الطابع إلى صفحة معينة
        pdfDocument.getPages().get_Item(1).addStamp(imageStamp);

        // حفظ المستند الناتج
        pdfDocument.save(_dataDir + "AddImageStamp_out.pdf");

    }
```


## التحكم في جودة الصورة عند إضافة ختم

تسمح لك فئة [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) بإضافة صورة كختم في مستند PDF. كما تتيح لك التحكم في جودة الصورة عند إضافة صورة كعلامة مائية في ملف PDF. للسماح بذلك، تمت إضافة طريقة باسم setQuality(...) إلى فئة [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp). يمكن العثور على طريقة مشابهة أيضًا في فئة [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/Stamp) في الحزمة com.aspose.pdf.facades.

يوضح لك مقتطف الشيفرة التالي كيفية التحكم في جودة الصورة عند إضافتها كختم في ملف PDF.

```java
 public static void ControlImageQualityWhenAddingStamp() {
        // افتح المستند
        Document pdfDocument = new Document(_dataDir + "AddImageStamp.pdf");

        // إنشاء ختم الصورة
        ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.png");
        imageStamp.setQuality(10);
        pdfDocument.getPages().get_Item(1).addStamp(imageStamp);

        pdfDocument.save(_dataDir + "ControlImageQuality_out.pdf");
    }
```


## ختم الصورة كخلفية في صندوق عائم

تتيح لك Aspose.PDF API إضافة ختم صورة كخلفية في صندوق عائم. يمكن استخدام خاصية BackgroundImage لفئة FloatingBox لتعيين ختم الصورة الخلفية لصندوق عائم كما هو موضح في نموذج الكود التالي.

```java
public static void ImageStampAsBackgroundInFloatingBox() {
        // إنشاء كائن Document
        Document doc = new Document();
        // إضافة صفحة إلى مستند PDF
        Page page = doc.getPages().add();

        // إنشاء كائن FloatingBox
        FloatingBox aBox = new FloatingBox(200, 100);

        // تعيين موضع اليسار لـ FloatingBox
        aBox.setLeft(40);
        // تعيين موضع الأعلى لـ FloatingBox
        aBox.setTop(80);
        // تعيين المحاذاة الأفقية لـ FloatingBox
        aBox.setHorizontalAlignment(HorizontalAlignment.Center);
        // إضافة جزء نص إلى مجموعة الفقرات لـ FloatingBox
        aBox.getParagraphs().add(new TextFragment("النص الرئيسي"));
        // تعيين الحدود لـ FloatingBox
        aBox.setBorder(new BorderInfo(BorderSide.All, Color.getRed()));

        // إضافة صورة الخلفية
        Image img = new Image();
        img.setFile(_dataDir + "aspose-logo.png");
        aBox.setBackgroundImage(img);

        // تعيين لون الخلفية لـ FloatingBox
        aBox.setBackgroundColor(Color.getYellow());

        // إضافة FloatingBox إلى مجموعة الفقرات لكائن الصفحة
        page.getParagraphs().add(aBox);
        // حفظ مستند PDF
        doc.save(_dataDir + "AddImageStampAsBackgroundInFloatingBox_out.pdf");
    }
}
```