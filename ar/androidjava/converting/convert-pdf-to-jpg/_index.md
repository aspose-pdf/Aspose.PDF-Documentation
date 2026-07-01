---
title: تحويل PDF إلى JPG
linktitle: تحويل PDF إلى JPG
type: docs
weight: 10
url: /ar/androidjava/convert-pdf-to-jpg/
description:  تصف هذه الصفحة كيفية تحويل صفحات PDF إلى صورة JPEG، وتحويل جميع الصفحات والصفحات الفردية إلى صور JPEG باستخدام Aspose.PDF for Android via Java.
lastmod: "2026-06-30"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## تحويل صفحات PDF إلى صور JPG

تسمح لك فئة JpegDevice بتحويل صفحات PDF إلى صور JPEG. توفر هذه الفئة طريقة تسمى process(..) والتي تسمح لك بتحويل صفحة معينة من ملف PDF إلى صورة JPEG.

{{% alert color="primary" %}}

جرّب عبر الإنترنت. يمكنك التحقق من جودة تحويل Aspose.PDF وعرض النتائج عبر الإنترنت في هذا الرابط  [products.aspose.app/pdf/conversion/pdf-to-jpg](https://products.aspose.app/pdf/conversion/pdf-to-jpg)

{{% /alert %}}


## تحويل صفحة PDF واحدة إلى صورة JPG

تتيح لك Aspose.PDF for Android عبر Java تحويل صفحة واحدة إلى صيغة Jpeg.

لتحويل صفحة واحدة فقط إلى صورة JPEG:

1. إنشاء كائن من فئة Document للحصول على الصفحة التي تريد تحويلها.
1. استدعِ طريقة process(..) لتحويل الصفحة إلى صورة JPEG.

توضح مقطع الشيفرة التالي الخطوات لتحويل الصفحة الأولى من PDF إلى تنسيق Jpeg.

```java
public void convertPDFtoJPEG() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-JPEG.jpeg");
        // Create stream object to save the output image
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Create Resolution object
            Resolution resolution = new Resolution(300);

            // Create JpegDevice object with particular resolution
            JpegDevice JpegDevice = new JpegDevice(resolution);

            // Convert a particular page and save the image to stream
            JpegDevice.process(document.getPages().get_Item(1), imageStream);

            // Close the stream
            imageStream.close();

            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }

```

## تحويل جميع صفحات PDF إلى صورة JPG

يتيح لك Aspose.PDF for Android via Java تحويل جميع الصفحات في ملف PDF إلى صور:

1. تكرار المرور عبر جميع الصفحات في الملف.
1. قم بتحويل كل صفحة على حدة:
    - إنشاء كائن من فئة Document لتحميل مستند PDF.
    - احصل على الصفحة التي تريد تحويلها.
    - استدعِ طريقة Process لتحويل الصفحة إلى Jpeg.

يظهر المقتطف البرمجي التالي كيفية تحويل جميع صفحات PDF إلى صور Jpeg.

```java
public void convertPDFtoJPEG_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Loop through all the pages of PDF file
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Create stream object to save the output image
            File file = new File(fileStorage, "PDF-to-JPEG"+pageCount+".jpeg");
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
            JpegDevice JpegDevice = new JpegDevice(resolution);

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

## تحويل صفحة PDF معينة إلى صورة JPG

```java
   public void convertPDFtoJPEG_ParticularPageRegion() {
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
        JpegDevice JpegDevice = new JpegDevice(resolution);

        File file = new File(fileStorage, "PDF-to-JPEG.jpeg");
        try {
            // Convert a particular page and save the image to stream
            JpegDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```
