---
title: إدارة الرأس والتذييل
type: docs
weight: 40
url: ar/java/manage-header-and-footer/
description: يشرح هذا القسم كيفية إدارة الرأس والتذييل باستخدام Aspose.PDF Facades باستخدام Class PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---

## إضافة رأس إلى ملف PDF

تسمح لك فئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) بإضافة رأس إلى ملف PDF.
 من أجل إضافة رأس، تحتاج أولاً إلى إنشاء كائن من فئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). يمكنك تنسيق نص العنوان باستخدام فئة [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText). بمجرد أن تكون جاهزًا لإضافة العنوان في الملف، تحتاج إلى استدعاء طريقة [addHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addHeader-com.aspose.pdf.facades.FormattedText-float-) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). تحتاج أيضًا إلى تحديد هامش أعلى على الأقل في طريقة [addHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addHeader-com.aspose.pdf.facades.FormattedText-float-). أخيرًا، احفظ ملف PDF الناتج باستخدام طريقة [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) لفئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). يوضح لك مقتطف الشيفرة البرمجية التالي كيفية إضافة العنوان في ملف PDF.

```java
 public static void AddHeader() {
        // إنشاء كائن PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // فتح المستند
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // إنشاء نص منسق لرقم الصفحة
        FormattedText formattedText = new FormattedText("Aspose - خبراء تنسيق الملفات لديك!", java.awt.Color.YELLOW,
                java.awt.Color.BLACK, FontStyle.Courier, EncodingType.Winansi, false, 14);

        // إضافة العنوان
        fileStamp.addHeader(formattedText, 20);

        // حفظ ملف PDF المحدث
        fileStamp.save(_dataDir + "AddHeader_out.pdf");

        // إغلاق fileStamp
        fileStamp.close();
    }
```

## إضافة تذييل في ملف PDF

تسمح لك فئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) بإضافة تذييل في ملف PDF.
 من أجل إضافة تذييل، تحتاج أولاً إلى إنشاء كائن من فئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). يمكنك تنسيق نص التذييل باستخدام فئة [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText). بمجرد أن تكون جاهزًا لإضافة تذييل في الملف، تحتاج إلى استدعاء طريقة [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). تحتاج أيضًا إلى تحديد على الأقل الهامش السفلي في طريقة [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-). وأخيرًا، احفظ ملف PDF الناتج باستخدام طريقة [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) لفئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). يوضح لك مقتطف الشيفرة التالي كيفية إضافة تذييل في ملف PDF.

```java
 public static void AddFooter() {
        // إنشاء كائن PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // فتح المستند
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // إنشاء نص منسق لرقم الصفحة
        FormattedText formattedText = new FormattedText("Aspose - خبراء تنسيق ملفك!", java.awt.Color.BLUE,
                java.awt.Color.GRAY, FontStyle.Courier, EncodingType.Winansi, false, 14);

        // إضافة تذييل
        fileStamp.addFooter(formattedText, 10);

        // حفظ ملف PDF المحدث
        fileStamp.save(_dataDir + "AddFooter_out.pdf");

        // إغلاق fileStamp
        fileStamp.close();
    }
```

## إضافة صورة إلى رأس ملف PDF موجود

تتيح لك فئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) إضافة صورة في رأس ملف PDF.
 من أجل إضافة صورة في الرأس، تحتاج أولاً إلى إنشاء كائن من فئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). بعد ذلك، تحتاج إلى استدعاء طريقة [addHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addHeader-com.aspose.pdf.facades.FormattedText-float-) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). يمكنك تمرير الصورة إلى طريقة [addHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addHeader-com.aspose.pdf.facades.FormattedText-float-). أخيرًا، احفظ ملف PDF الناتج باستخدام طريقة [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). يوضح لك مقتطف الكود التالي كيفية إضافة صورة في رأس ملف PDF.

```java
public static void AddImageHeader() {
        // إنشاء كائن PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // فتح المستند
        fileStamp.bindPdf(_dataDir + "sample.pdf");
        FileInputStream fs;
        try {
            fs = new FileInputStream(_dataDir + "aspose-logo.png");
            // إضافة رأس
            fileStamp.addHeader(fs, 10);

            // حفظ ملف PDF المحدّث
            fileStamp.save(_dataDir + "AddImage-Header_out.pdf");
        } catch (FileNotFoundException e) {

            e.printStackTrace();
        }

        // إغلاق fileStamp
        fileStamp.close();
    }
```

## إضافة صورة في تذييل ملف PDF موجود

تسمح لك فئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) بإضافة صورة في تذييل ملف PDF.
 من أجل إضافة صورة في التذييل، تحتاج أولاً إلى إنشاء كائن من فئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). بعد ذلك، تحتاج إلى استدعاء طريقة [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-) الخاصة بفئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). يمكنك تمرير الصورة إلى طريقة [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-). أخيرًا، احفظ ملف PDF الناتج باستخدام طريقة [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) الخاصة بفئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). يوضح لك مقطع الشيفرة التالي كيفية إضافة صورة في تذييل ملف PDF.

```java
    public static void AddImageFooter() {
        // إنشاء كائن PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // فتح الوثيقة
        fileStamp.bindPdf(_dataDir + "sample.pdf");
        FileInputStream fs;
        try {
            fs = new FileInputStream(_dataDir + "aspose-logo.png");
            // إضافة التذييل
            fileStamp.addFooter(fs, 10);

            // حفظ ملف PDF المحدث
            fileStamp.save(_dataDir + "AddImage-Footer_out.pdf");
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        // إغلاق fileStamp
        fileStamp.close();
    }
```