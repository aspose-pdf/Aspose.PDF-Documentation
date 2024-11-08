---
title: إضافة ختم نص وصورة
type: docs
weight: 20
url: /ar/java/add-text-and-image-stamp/
description: تشرح هذه القسم كيفية إضافة ختم نص وصورة باستخدام com.aspose.pdf.facades باستخدام فئة PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---

## إضافة ختم نص على جميع الصفحات في ملف PDF

تسمح لك فئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) بإضافة ختم نص على جميع صفحات ملف PDF.
 In order to add text stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) and [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) classes.

من أجل إضافة ختم نصي، تحتاج أولاً إلى إنشاء كائنات من فئات [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) و [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). أنت تحتاج أيضًا إلى إنشاء ختم النص باستخدام طريقة BindLogo من فئة [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). يمكنك تعيين سمات أخرى مثل الأصل، الدوران، الخلفية إلخ. باستخدام كائن [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) أيضًا. ثم يمكنك إضافة الختم في ملف PDF باستخدام طريقة [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). أخيرًا، احفظ ملف PDF الناتج باستخدام طريقة [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). يوضح لك مقطع الشفرة التالي كيفية إضافة ختم نص على جميع الصفحات في ملف PDF.

```java
 public static void AddTextStampOnAllPagesInPdfFile() {
        // إنشاء كائن PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // فتح المستند
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // إنشاء الختم
        Stamp stamp = new Stamp();
        stamp.bindLogo(new FormattedText("Hello World!", java.awt.Color.BLUE, java.awt.Color.GRAY, FontStyle.Helvetica,
                EncodingType.Winansi, true, 14));
        stamp.setOrigin(10, 400);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // إضافة الختم إلى ملف PDF
        fileStamp.addStamp(stamp);

        // حفظ ملف PDF المحدث
        fileStamp.save(_dataDir + "AddTextStamp-All_out.pdf");

        // إغلاق fileStamp
        fileStamp.close();
    }
```

## إضافة ختم نصي على صفحات معينة في ملف PDF

تتيح لك فئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) إضافة ختم نصي على صفحات معينة من ملف PDF.
 In order to add text stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp)and [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) classes.

من أجل إضافة ختم نصي، تحتاج أولاً إلى إنشاء كائنات من فئات [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) و [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). You also need to create the text stamp using [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) method of [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) class.  
تحتاج أيضًا إلى إنشاء ختم النص باستخدام طريقة [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) من فئة [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). يمكنك تعيين سمات أخرى مثل الأصل، التدوير، الخلفية إلخ. باستخدام [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) object أيضًا. كما تريد إضافة ختم نصي على صفحات معينة من ملف PDF، تحتاج أيضًا إلى تعيين خاصية [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#setPages-int:A-) من فئة [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). تتطلب هذه الخاصية مصفوفة أعداد صحيحة تحتوي على أرقام الصفحات التي تريد إضافة الختم عليها. بعد ذلك يمكنك إضافة الختم في ملف PDF باستخدام طريقة [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). وأخيرًا، احفظ ملف PDF الناتج باستخدام طريقة [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). يوضح لك مقطع الشيفرة التالي كيفية إضافة ختم نصي على صفحات معينة في ملف PDF.

```java
 public static void AddTextStampOnParticularPagesInPdfFile() {
        // إنشاء كائن PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // فتح المستند
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // إنشاء الختم
        Stamp stamp = new Stamp();
        stamp.bindLogo(new FormattedText("Hello World!", java.awt.Color.BLUE, java.awt.Color.GRAY, FontStyle.Helvetica,
                EncodingType.Winansi, true, 14));
        stamp.setOrigin(10, 400);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // تعيين الصفحات المحددة
        stamp.setPages(new int[] { 2 });

        // إضافة الختم إلى ملف PDF
        fileStamp.addStamp(stamp);

        // حفظ ملف PDF المحدث
        fileStamp.save(_dataDir + "AddTextStamp-Page_out.pdf");

        // إغلاق fileStamp
        fileStamp.close();
    }
```

## إضافة ختم صورة على جميع الصفحات في ملف PDF

تسمح لك فئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) بإضافة ختم صورة على جميع صفحات ملف PDF.
 In order to add image stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) and [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) classes.

من أجل إضافة ختم الصورة، تحتاج أولاً إلى إنشاء كائنات من فئات [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) و[Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). تحتاج أيضًا إلى إنشاء ختم الصورة باستخدام طريقة [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) من فئة [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). يمكنك تعيين سمات أخرى مثل الأصل والدوران والخلفية وما إلى ذلك باستخدام كائن [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) أيضًا. ثم يمكنك إضافة الختم في ملف PDF باستخدام طريقة [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). أخيرًا، احفظ ملف PDF الناتج باستخدام طريقة [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). يظهر مقتطف الشيفرة التالي كيفية إضافة ختم الصورة على جميع الصفحات في ملف PDF.

```java
public static void AddImageStampOnParticularPagesInPdfFile() {
        // إنشاء كائن PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // فتح المستند
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // إنشاء الختم
        Stamp stamp = new Stamp();
        stamp.bindImage(_dataDir + "aspose-logo.png");
        stamp.setOrigin(10, 200);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // إضافة الختم إلى ملف PDF
        fileStamp.addStamp(stamp);

        // حفظ ملف PDF المحدث
        fileStamp.save(_dataDir + "AddImageStamp-All_out.pdf");

        // إغلاق fileStamp
        fileStamp.close();
    }
```

### التحكم في جودة الصورة عند إضافتها كختم

عند إضافة صورة ككائن ختم، يمكنك أيضًا التحكم في جودة الصورة. من أجل تحقيق هذا المتطلب، تمت إضافة خاصية الجودة لفئة [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). تشير إلى جودة الصورة كنسبة مئوية (القيم الصحيحة هي 0..100).

## إضافة ختم صورة على صفحات معينة في ملف PDF

تسمح لك فئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) بإضافة ختم صورة على صفحات معينة من ملف PDF.
 In order to add image stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) and [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) classes.

من أجل إضافة ختم الصورة، تحتاج أولاً إلى إنشاء كائنات من فئات [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) و[Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). You also need to create the image stamp using [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) method of [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) class.  
تحتاج أيضًا إلى إنشاء ختم الصورة باستخدام طريقة [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) من فئة [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). يمكنك تعيين سمات أخرى مثل الأصل، التدوير، الخلفية إلخ. باستخدام [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) أيضًا. كما تريد إضافة ختم الصورة على صفحات معينة من ملف PDF، تحتاج أيضًا إلى تعيين خاصية [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#setPages-int:A-) في فئة [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). تتطلب هذه الخاصية مصفوفة أعداد صحيحة تحتوي على أرقام الصفحات التي تريد إضافة الختم عليها. بعد ذلك يمكنك إضافة الختم في ملف PDF باستخدام طريقة [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). أخيرًا، احفظ ملف PDF الناتج باستخدام طريقة [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). يوضح لك مقطع الشيفرة التالي كيفية إضافة ختم الصورة على صفحات معينة في ملف PDF.

```java
  public static void AddImageStampOnAllPagesInPdfFile() {
        // إنشاء كائن PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // فتح المستند
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // إنشاء الختم
        Stamp stamp = new Stamp();
        stamp.bindImage(_dataDir + "aspose-logo.png");
        stamp.setOrigin(10, 200);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // تعيين صفحات معينة
        stamp.setPages(new int[] { 2 });

        // إضافة الختم إلى ملف PDF
        fileStamp.addStamp(stamp);

        // حفظ ملف PDF المحدث
        fileStamp.save(_dataDir + "AddImageStamp-Page_out.pdf");

        // إغلاق fileStamp
        fileStamp.close();
    }
```