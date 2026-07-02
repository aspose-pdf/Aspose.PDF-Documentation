---
title: تحويل PDF إلى PNG
linktitle: تحويل PDF إلى PNG
type: docs
weight: 20
url: /ar/androidjava/convert-pdf-to-png/
lastmod: "2026-06-30"
description: تصف هذه الصفحة كيفية تحويل صفحات PDF إلى صورة PNG، وتحويل جميع الصفحات والصفحات الفردية إلى صور PNG باستخدام Aspose.PDF for Android via Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

استخدم مكتبة **Aspose.PDF for Android via Java** لتحويل صفحات PDF إلى <abbr title="Portable Network Graphics">PNG</abbr> الصور بطريقة قابلة للوصول ومريحة.

تسمح لك فئة PngDevice بتحويل صفحات PDF إلى صور PNG. توفر هذه الفئة طريقة تسمى Process والتي تتيح لك تحويل صفحة معينة من ملف PDF إلى تنسيق صورة PNG.

## تحويل صفحات PDF إلى صور PNG

لتحويل جميع الصفحات في ملف PDF إلى ملفات PNG، قم بالتكرار عبر الصفحات الفردية وتحويل كل منها إلى تنسيق PNG. يوضح المقتطع البرمجي التالي كيفية التنقل عبر جميع صفحات ملف PDF وتحويل كل صفحة إلى صورة PNG.

{{% alert color="primary" %}} 

جربه عبر الإنترنت. يمكنك التحقق من جودة تحويل Aspose.PDF وعرض النتائج عبر الإنترنت عبر هذا الرابط [products.aspose.app/pdf/conversion/pdf-to-png](https://products.aspose.app/pdf/conversion/pdf-to-png)

{{% /alert %}}

## تحويل صفحة PDF واحدة إلى صورة PNG

مرّر فهرس الصفحة كوسيط إلى طريقة Process(..).
يعرض مقتطف الشيفرة التالي الخطوات لتحويل الصفحة الأولى من PDF إلى تنسيق PNG.

```java
   public void convertPDFtoPNG() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-PNG.png");
        // Create stream object to save the output image
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Create Resolution object
            Resolution resolution = new Resolution(300);

            // Create PngDevice object with particular resolution
            PngDevice PngDevice = new PngDevice(resolution);

            // Convert a particular page and save the image to stream
            PngDevice.process(document.getPages().get_Item(1), imageStream);

            // Close the stream
            imageStream.close();
            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }

```

## تحويل جميع صفحات PDF إلى صورة PNG

Aspose.PDF for Android via Java يوضح لك كيفية تحويل جميع الصفحات في ملف PDF إلى صور:

1. تنقل عبر جميع الصفحات في الملف.
1. قم بتحويل كل صفحة على حدة:
    1. أنشئ كائنًا من فئة Document لتحميل مستند PDF.
    1. احصل على الصفحة التي تريد تحويلها.
    1. استدعِ طريقة Process لتحويل الصفحة إلى PNG.

يوضح مقطع الشيفرة التالي كيفية تحويل جميع صفحات PDF إلى صور PNG.

```java
 public void convertPDFtoPNG_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Loop through all the pages of PDF file
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Create stream object to save the output image
            File file = new File(fileStorage, "PDF-to-PNG"+pageCount+".png");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // Create Resolution object
            Resolution resolution = new Resolution(300);
            // Create JpegDevice object with particular resolution
            PngDevice JpegDevice = new PngDevice(resolution);

            // Convert a particular page and save the image to stream
            JpegDevice.process(document.getPages().get_Item(pageCount), imageStream);

            // Close the stream
            try {
                imageStream.close();
            } catch (Exception e) {
                resultMessage.setText(e.getMessage());
                return;
            }
        }
        resultMessage.setText(R.string.success_message);
    }
```

## تحويل صفحة PDF معينة إلى صورة PNG

Aspose.PDF لنظام Android عبر Java يوضح لك كيفية تحويل صفحة معينة إلى تنسيق PNG:

```java
public void convertPDFtoPNG_ParticularPageRegion() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Get rectangle of particular page region
        //x=0,y=0, w=200, h=125;
        Rectangle pageRect = new Rectangle(0, 0, 200, 125);
        // set CropBox value as per rectangle of desired page region
        document.getPages().get_Item(1).setCropBox(pageRect);
        // save cropped document into stream
        ByteArrayOutputStream outStream = new ByteArrayOutputStream();
        document.save(outStream);

        // open cropped PDF document from stream and convert to image
        document = new Document(new ByteArrayInputStream(outStream.toByteArray()));
        // Create Resolution object
        Resolution resolution = new Resolution(300);
        // Create Jpeg device with specified attributes
        PngDevice PngDevice = new PngDevice(resolution);

        File file = new File(fileStorage, "PDF-to-PNG.png");
        try {
            // Convert a particular page and save the image to stream
            PngDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```
