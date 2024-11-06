---
title: تحويل PDF إلى TIFF
linktitle: تحويل PDF إلى TIFF
type: docs
weight: 30
url: ar/androidjava/convert-pdf-to-tiff/
lastmod: "2021-06-05"
description: تصف هذه المقالة كيفية تحويل الصفحات في مستند PDF إلى صورة TIFF. سوف تتعلم كيفية تحويل جميع الصفحات أو صفحة واحدة إلى صور TIFF باستخدام Aspose.PDF لنظام Android عبر Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF لنظام Android عبر Java** يجعل من الممكن تحويل صفحات PDF إلى صور TIFF.

تسمح لك [فئة TiffDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice) بتحويل صفحات PDF إلى صور TIFF. توفر هذه الفئة طريقة تسمى Process والتي تسمح لك بتحويل جميع الصفحات في ملف PDF إلى صورة TIFF واحدة.

{{% alert color="primary" %}}

جرّب عبر الإنترنت. يمكنك التحقق من جودة تحويل Aspose.PDF وعرض النتائج عبر الإنترنت على هذا الرابط [products.aspose.app/pdf/conversion/pdf-to-tiff](https://products.aspose.app/pdf/conversion/pdf-to-tiff)

{{% /alert %}}

## تحويل صفحات PDF إلى صورة TIFF واحدة

Aspose.PDF لنظام Android عبر Java يشرح كيفية تحويل جميع الصفحات في ملف PDF إلى صورة TIFF واحدة:

1. إنشاء كائن من فئة Document.
2. استدعاء طريقة Process لتحويل المستند.
3. لاعداد خصائص ملف الإخراج، استخدم فئة TiffSettings.

يظهر مقطع الشيفرة التالي كيفية تحويل جميع صفحات PDF إلى صورة TIFF واحدة.

```java
public void convertPDFtoTiffSinglePage() {
        // افتح المستند
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // إنشاء كائن Resolution
        Resolution resolution = new Resolution(300);

        // إنشاء كائن TiffSettings
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.None);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setShape(ShapeType.Landscape);

        // إنشاء جهاز TIFF
        TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
        File file = new File(fileStorage, "PDF-to-TIFF.tiff");
        try {
            // تحويل صفحة معينة وحفظ الصورة في الدفق
            tiffDevice.process(document, 1, 1, file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }

```


## تحويل صفحة واحدة إلى صورة TIFF

Aspose.PDF لأندرويد عبر Java يسمح بتحويل صفحة معينة في ملف PDF إلى صورة TIFF، استخدم نسخة مثقلة من طريقة Process(..) التي تأخذ رقم الصفحة كمعامل للتحويل. يوضح مقطع الشيفرة التالي كيفية تحويل الصفحة الأولى من PDF إلى تنسيق TIFF.

```java
public void convertPDFtoTiffAllPages() {
        // فتح المستند
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }


        // إنشاء كائن Resolution
        Resolution resolution = new Resolution(300);

        // إنشاء كائن TiffSettings
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.None);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setShape(ShapeType.Landscape);
        tiffSettings.setSkipBlankPages(false);

        // إنشاء جهاز TIFF
        TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
        File file = new File(fileStorage, "AllPagesToTIFF_out.tif");
        try {
            // تحويل صفحة معينة وحفظ الصورة في المجرى
            tiffDevice.process(document, file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```


## استخدام خوارزمية برادلي أثناء التحويل

يدعم Aspose.PDF لنظام Android عبر Java ميزة تحويل PDF إلى TIFF باستخدام ضغط LZW ومن ثم باستخدام AForge، يمكن تطبيق عملية التحويل إلى الأبيض والأسود. ومع ذلك، طلب أحد العملاء أنه لبعض الصور، يحتاجون إلى الحصول على العتبة باستخدام Otsu، لذا يرغبون أيضًا في استخدام برادلي.

```java
public void convertPDFtoTiffBradleyBinarization() {
        //لم يتم تنفيذه في Aspose.PDF لنظام Android
        throw new NotImplementedException();
    }

    public static void convertPDFtoTIFF_Pixelated() {

        //لم يتم تنفيذه في Aspose.PDF لنظام Android
        throw new NotImplementedException();
    }
```