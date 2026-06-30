---
title: تحويل PDF إلى TIFF
linktitle: تحويل PDF إلى TIFF
type: docs
weight: 30
url: /ar/androidjava/convert-pdf-to-tiff/
lastmod: "2026-06-30"
description: تصفّح هذه المقالة كيفية تحويل الصفحات في مستند PDF إلى صورة TIFF. ستتعلم كيفية تحويل جميع الصفحات أو صفحة واحدة إلى صور TIFF باستخدام Aspose.PDF for Android عبر Android عبر Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Android via Java** يجعل من الممكن تحويل صفحات PDF إلى صور TIFF.

ال [فئة TiffDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice) يتيح لك تحويل صفحات PDF إلى صور TIFF. توفر هذه الفئة طريقة تسمى Process تسمح لك بتحويل جميع الصفحات في ملف PDF إلى صورة TIFF واحدة.

{{% alert color="primary" %}}

جرّبه عبر الإنترنت. يمكنك التحقق من جودة تحويل Aspose.PDF وعرض النتائج عبر الإنترنت عبر هذا الرابط [products.aspose.app/pdf/conversion/pdf-to-tiff](https://products.aspose.app/pdf/conversion/pdf-to-tiff)

{{% /alert %}}

## تحويل صفحات PDF إلى صورة TIFF واحدة

Aspose.PDF for Android via Java يشرح كيفية تحويل جميع الصفحات في ملف PDF إلى صورة TIFF واحدة:

1. إنشاء كائن من الفئة Document.
1. استدعِ طريقة Process لتحويل المستند.
1. لتعيين خصائص ملف الإخراج، استخدم الفئة TiffSettings.

المقتطف البرمجي التالي يوضح كيفية تحويل جميع صفحات PDF إلى صورة TIFF واحدة.

```java
public void convertPDFtoTiffSinglePage() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Create Resolution object
        Resolution resolution = new Resolution(300);

        // Create TiffSettings object
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.None);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setShape(ShapeType.Landscape);

        // Create TIFF device
        TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
        File file = new File(fileStorage, "PDF-to-TIFF.tiff");
        try {
            // Convert a particular page and save the image to stream
            tiffDevice.process(document, 1, 1, file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }

```

## تحويل صفحة واحدة إلى صورة TIFF

تسمح Aspose.PDF for Android عبر Java بتحويل صفحة محددة في ملف PDF إلى صورة TIFF، استخدم نسخة محملة من طريقة Process(..) التي تأخذ رقم الصفحة كوسيطة للتحويل. يوضح مقطع الكود التالي كيفية تحويل الصفحة الأولى من ملف PDF إلى تنسيق TIFF.

```java
public void convertPDFtoTiffAllPages() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }


        // Create Resolution object
        Resolution resolution = new Resolution(300);

        // Create TiffSettings object
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.None);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setShape(ShapeType.Landscape);
        tiffSettings.setSkipBlankPages(false);

        // Create TIFF device
        TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
        File file = new File(fileStorage, "AllPagesToTIFF_out.tif");
        try {
            // Convert a particular page and save the image to stream
            tiffDevice.process(document, file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```

## استخدم خوارزمية برادلي أثناء التحويل

Aspose.PDF for Android via Java يدعم ميزة تحويل PDF إلى TIFF باستخدام ضغط LZW، ثم يمكن تطبيق Binarization باستخدام AForge. ومع ذلك، طلب أحد العملاء أنه لبعض الصور، يحتاجون إلى الحصول على Threshold باستخدام Otsu، لذلك يرغبون أيضًا في استخدام Bradley.

```java
public void convertPDFtoTiffBradleyBinarization() {
        //Not implemented in Aspose.PDF for Android
        throw new NotImplementedException();
    }

    public static void convertPDFtoTIFF_Pixelated() {

        //Not implemented in Aspose.PDF for Android
        throw new NotImplementedException();
    }
```

