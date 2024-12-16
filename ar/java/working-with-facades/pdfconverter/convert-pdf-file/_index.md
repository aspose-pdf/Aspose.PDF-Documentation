---
title: تحويل ملف PDF
type: docs
weight: 20
url: /ar/java/convert-pdf-file/
description: يشرح هذا القسم كيفية تحويل ملف PDF باستخدام Aspose.PDF Facades باستخدام فئة PdfConverter.
lastmod: "2021-06-05"
draft: false
---

## تحويل صفحات PDF إلى تنسيقات صور مختلفة (Facades)

من أجل تحويل صفحات PDF إلى تنسيقات صور مختلفة، تحتاج إلى إنشاء كائن [PdfConverter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter) وفتح ملف PDF باستخدام طريقة [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#bindPdf-java.lang.String-).

بعد ذلك، تحتاج إلى استدعاء طريقة [doConvert](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#doConvert--) لمهام التهيئة.
 ثم يمكنك التنقل بين جميع الصفحات باستخدام طريقتي [hasNextImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#hasNextImage--) و[getNextImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#getNextImage-java.io.OutputStream-). تتيح لك طريقة getNextImage إنشاء صورة لصفحة معينة. تحتاج أيضًا إلى تمرير ImageType إلى هذه الطريقة من أجل إنشاء صورة من نوع معين مثل JPEG أو GIF أو PNG إلخ.

وأخيرًا، قم باستدعاء طريقة الإغلاق لفئة [PdfConverter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter).

يُظهر لك مقتطف الشيفرة التالي كيفية تحويل صفحات PDF إلى صور.

```java
public static void ConvertPdfPagesToImages01() {
        // إنشاء كائن PdfConverter
        PdfConverter converter = new PdfConverter();

        // ربط ملف PDF المدخل
        converter.bindPdf(_dataDir + "Sample-Document-01.pdf");

        // بدء عملية التحويل
        converter.doConvert();
        
        int count=0;

        // التحقق مما إذا كانت الصفحات موجودة ثم التحويل إلى صورة واحدة تلو الأخرى
        while (converter.hasNextImage())
            converter.getNextImage(_dataDir + "page" + count + "_out.jpg", ImageType.getJpeg());
        // إغلاق كائن PdfConverter
        converter.close();
    }
```

في مقتطف الشيفرة التالي، سنوضح كيف يمكنك تغيير بعض المعلمات. باستخدام [setCoordinateType](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setCoordinateType-int-) نحدد الإطار [CropBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCoordinateType#CropBox). أيضًا، يمكننا تغيير [setResolution](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setResolution-com.aspose.pdf.devices.Resolution-) بتحديد عدد النقاط لكل بوصة. التالي هو [setFormPresentationMode](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setFormPresentationMode-int-) - وضع عرض النموذج. ثم نحدد [setStartPage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setStartPage-int-) الذي يحدد رقم الصفحة لبداية التحويل. يمكننا أيضًا تحديد الصفحة الأخيرة بتعيين نطاق.

```java
public static void ConvertPdfPagesToImages02()
    {
        // إنشاء كائن PdfConverter
        PdfConverter converter = new PdfConverter();

        // ربط ملف pdf المدخل
        converter.bindPdf(_dataDir + "sample.pdf");

        // تهيئة عملية التحويل
        converter.doConvert();
        converter.setCoordinateType(PageCoordinateType.CropBox);
        converter.setResolution (new Resolution(600));
        converter.setFormPresentationMode(FormPresentationMode.Editor);
        converter.setStartPage(2);
        int count=0;
        // التحقق من وجود الصفحات ثم التحويل إلى صورة واحدة تلو الأخرى
        while (converter.hasNextImage())
            converter.getNextImage(_dataDir + "page" + count + "_out.jpg", ImageType.getJpeg());
        // إغلاق كائن PdfConverter
        converter.close();
    }
```