---
title: إضافة ختم صفحة PDF
type: docs
weight: 10
url: /ar/java/add-pdf-page-stamp/
description: يشرح هذا القسم كيفية العمل مع Aspose.PDF Facades باستخدام فئة PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---

## إضافة ختم صفحة PDF على جميع الصفحات في ملف PDF

تسمح لك فئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) بإضافة ختم صفحة PDF على جميع صفحات ملف PDF.
 In order to add PDF page stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) and [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) classes.

من أجل إضافة ختم صفحة PDF، تحتاج أولاً إلى إنشاء كائنات من فئات [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) و [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). تحتاج أيضًا إلى إنشاء ختم صفحة PDF باستخدام [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) طريقة فئة [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). يمكنك تعيين سمات أخرى مثل الأصل، التدوير، الخلفية وغيرها باستخدام كائن [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) أيضًا. بعد ذلك، يمكنك إضافة الختم في ملف PDF باستخدام طريقة [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades.PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) لفئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). وأخيرًا، احفظ ملف PDF الناتج باستخدام طريقة [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) لفئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). يوضح لك مقتطف الشفرة التالي كيفية إضافة ختم صفحة PDF على جميع الصفحات في ملف PDF.

```csharp
public static void AddPageStampOnAllPages()
        {
            // إنشاء كائن PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // فتح المستند
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // إنشاء الختم
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindPdf(_dataDir + "pagestamp.pdf", 1);
            stamp.SetOrigin(20, 20);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // إضافة الختم إلى ملف PDF
            fileStamp.AddStamp(stamp);

            // حفظ ملف PDF المحدّث
            fileStamp.Save(_dataDir + "PageStampOnAllPages.pdf");

            // إغلاق fileStamp
            fileStamp.Close();
        }
```

## إضافة ختم صفحة PDF إلى صفحات معينة في ملف PDF

تسمح لك فئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) بإضافة ختم صفحة PDF على صفحات معينة في ملف PDF.
 لتتمكن من إضافة ختم لصفحة PDF، تحتاج أولاً إلى إنشاء كائنات من فئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) وفئة [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). You also need to create the PDF page stamp using [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) method of [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) class.

أنت بحاجة أيضًا إلى إنشاء ختم صفحة PDF باستخدام طريقة [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) لفئة [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). يمكنك ضبط سمات أخرى مثل الأصل، التدوير، الخلفية وغيرها. using [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) كائن أيضًا. كما تريد إضافة ختم صفحة PDF على صفحات معينة من ملف PDF، تحتاج أيضًا إلى تعيين خاصية [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#setPages-int:A-) في فئة [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). تتطلب هذه الخاصية مصفوفة أعداد صحيحة تحتوي على أرقام الصفحات التي تريد إضافة الختم عليها. ثم يمكنك إضافة الختم في ملف PDF باستخدام طريقة [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). أخيرًا، قم بحفظ ملف PDF الناتج باستخدام طريقة [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) من فئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). يوضح لك مقتطف الكود التالي كيفية إضافة ختم صفحة PDF على صفحات معينة في ملف PDF.

```csharp
public static void AddPageStampOnCertainPages()
        {
            // إنشاء كائن PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // فتح المستند
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // إنشاء الختم
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindPdf(_dataDir + "pagestamp.pdf", 1);
            stamp.SetOrigin(20, 20);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;
            stamp.Pages = new[] { 1, 3 };
            // إضافة الختم إلى ملف PDF
            fileStamp.AddStamp(stamp);

            // حفظ ملف PDF المحدث
            fileStamp.Save(_dataDir + "PageStampOnAllPages.pdf");

            // إغلاق fileStamp
            fileStamp.Close();
        }

        // إضافة أرقام صفحات PDF
        public enum PageNumPosition
        {
            PosBottomMiddle, PosBottomRight, PosUpperRight, PosSidesRight, PosUpperMiddle, PosBottomLeft, PosSidesLeft, PosUpperLeft
        }
```

## إضافة رقم الصفحة في ملف PDF (واجهات)

تسمح لك فئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) بإضافة أرقام الصفحات في ملف PDF.
 In order to add page numbers, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class.  
من أجل إضافة أرقام الصفحات، تحتاج أولاً إلى إنشاء كائن من فئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). إذا كنت تريد عرض رقم الصفحة مثل "صفحة X من N" حيث X هو رقم الصفحة الحالي وN هو العدد الإجمالي للصفحات في ملف PDF، فأنت بحاجة أولاً للحصول على عدد الصفحات باستخدام خاصية getNumberOfpages لفئة [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo). للحصول على رقم الصفحة الحالية، يمكنك استخدام علامة **#** في النص في أي مكان تريده. يمكنك تنسيق نص رقم الصفحة باستخدام فئة [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText). إذا كنت ترغب في بدء ترقيم الصفحات من رقم معين، يمكنك ضبط خاصية setStartingNumber. بمجرد أن تكون جاهزًا لإضافة رقم الصفحة في الملف، تحتاج إلى استدعاء طريقة addPageNumber لفئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). وأخيرًا، احفظ ملف PDF الناتج باستخدام طريقة Save لفئة [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp).

يوضح لك مقطع الشيفرة البرمجية التالي كيفية إضافة رقم الصفحة في ملف PDF.
```java
 public static void AddPageNumberInPdfFile() {
        // إنشاء كائن PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // فتح المستند
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // الحصول على العدد الإجمالي للصفحات
        int totalPages = new PdfFileInfo(_dataDir + "sample.pdf").getNumberOfPages();

        // إنشاء نص منسق لرقم الصفحة
        FormattedText formattedText = new FormattedText("Page # of " + totalPages, java.awt.Color.WHITE,
                java.awt.Color.GRAY, FontStyle.TimesBoldItalic, EncodingType.Winansi, false, 12);

        // تحديد الرقم الابتدائي للصفحة الأولى؛ قد ترغب في البدء من 2 أو أكثر
        fileStamp.setStartingNumber(1);

        // إضافة رقم الصفحة
        fileStamp.addPageNumber(formattedText, (int) PageNumPosition.PosUpperRight.ordinal());

        // حفظ ملف PDF المحدث
        fileStamp.save(_dataDir + "AddPageNumber_out.pdf");

        // إغلاق fileStamp
        fileStamp.close();
    }
```


### نمط ترقيم خاص

The [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class offers the feature to add Page Number information as stamp object inside PDF document. Prior to this release, the class only supported 1,2,3,4 as page numbering style. However, there has been a requirement from some customers to use custom numbering style when placing page number stamp inside PDF document. In order to accomplish this requirement, [NumberingStyle](https://reference.aspose.com/pdf/java/com.aspose.pdf/numberingstyle) property has been introduced, which accepts the values from [NumberingStyle](https://reference.aspose.com/pdf/java/com.aspose.pdf/numberingstyle) enumeration. Specified below are values offered in this enumeration.

```java
 public static void AddCustomPageNumberInPdfFile() {
        // إنشاء كائن PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // فتح المستند
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // الحصول على العدد الإجمالي للصفحات
        int totalPages = new PdfFileInfo(_dataDir + "sample.pdf").getNumberOfPages();

        // إنشاء نص منسق لرقم الصفحة
        FormattedText formattedText = new FormattedText("Page # of " + totalPages, java.awt.Color.WHITE,
                java.awt.Color.GRAY, FontStyle.TimesBoldItalic, EncodingType.Winansi, false, 12);

        // تحديد نمط الترقيم كأرقام رومانية كبيرة
        fileStamp.setNumberingStyle(NumberingStyle.NumeralsRomanUppercase);

        // تعيين الرقم المبدئي للصفحة الأولى؛ قد ترغب في البدء من 2 أو أكثر
        fileStamp.setStartingNumber(1);

        // إضافة رقم الصفحة
        fileStamp.addPageNumber(formattedText, PageNumPosition.PosUpperRight.ordinal());

        // حفظ ملف PDF المحدث
        fileStamp.save(_dataDir + "AddPageNumber_out.pdf");

        // إغلاق fileStamp
        fileStamp.close();
    }
```