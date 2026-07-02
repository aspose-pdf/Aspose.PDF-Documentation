---
title: تحويل PDF إلى BMP
linktitle: تحويل PDF إلى BMP
type: docs
weight: 40
url: /ar/androidjava/convert-pdf-to-bmp/
lastmod: "2026-06-30"
description: تصف هذه المقالة كيفية تحويل صفحات PDF إلى صورة BMP، وتحويل جميع الصفحات إلى صور BMP، وتحويل صفحة PDF واحدة إلى صورة BMP باستخدام Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

ال [BmpDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice) الصف يسمح لك بتحويل صفحات PDF إلى <abbr title="Bitmap Image File">BMP</abbr> الصور. توفر هذه الفئة طريقة تسمى [Process](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice/methods/process) والتي تتيح لك تحويل صفحة معينة من ملف PDF إلى تنسيق صورة Bmp.

{{% alert color="primary" %}}

جرّب عبر الإنترنت. يمكنك التحقق من جودة تحويل Aspose.PDF وعرض النتائج عبر الإنترنت على هذا الرابط [products.aspose.app/pdf/conversion/pdf-to-bmp](https://products.aspose.app/pdf/conversion/pdf-to-bmp)

{{% /alert %}}

تسمح لك فئة BmpDevice بتحويل صفحات PDF إلى صور BMP. توفر هذه الفئة طريقة تُدعى process(..) التي تسمح لك بتحويل صفحة معينة من ملف PDF إلى صورة BMP.

## تحويل صفحة PDF إلى صورة BMP

لتحويل صفحة PDF إلى صورة BMP:

1. أنشئ كائنًا من فئة Document للحصول على الصفحة المحددة التي تريد تحويلها.
1. استدعِ طريقة process(..) لتحويل الصفحة إلى BMP.

تظهر لك الشيفرة التالية كيفية تحويل صفحة معينة إلى صورة BMP.

```java
//Convert PDF to BMP
    public void convertPDFtoBMP() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-BMP.bmp");
        // Create stream object to save the output image
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Create Resolution object
            Resolution resolution = new Resolution(300);

            // Create BmpDevice object with particular resolution
            BmpDevice BmpDevice = new BmpDevice(resolution);

            // Convert a particular page and save the image to stream
            BmpDevice.process(document.getPages().get_Item(1), imageStream);

            // Close the stream
            imageStream.close();
            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }
```

## تحويل جميع صفحات PDF إلى صور BMP

لتحويل جميع صفحات ملف PDF إلى تنسيق BMP، تحتاج إلى التكرار للحصول على كل صفحة منفردة وتحويلها إلى تنسيق BMP. يوضح المقتطف البرمجي التالي كيفية التنقل عبر جميع صفحات ملف PDF وتحويلها إلى BMP.

```java
public void convertPDFtoBMP_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Loop through all the pages of PDF file
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Create stream object to save the output image
            File file = new File(fileStorage, "PDF-to-BMP"+pageCount+".BMP");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // Create Resolution object
            Resolution resolution = new Resolution(300);
            // Create BmpDevice object with particular resolution
            BmpDevice BmpDevice = new BmpDevice(resolution);

            // Convert a particular page and save the image to stream
            BmpDevice.process(document.getPages().get_Item(pageCount), imageStream);

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

## تحويل منطقة صفحة معينة إلى صورة (DOM)

يمكننا تحويل مستندات PDF إلى صيغ صور مختلفة باستخدام كائنات أجهزة الصور في Aspose.PDF. ومع ذلك، في بعض الأحيان تكون هناك حاجة لتحويل منطقة صفحة معينة إلى صيغة صورة. يمكننا تلبية هذا المتطلب عبر خطوتين. أولاً نقوم بقص صفحة PDF إلى المنطقة المطلوبة، ثم نحولها إلى صورة باستخدام كائن جهاز الصورة المطلوب.

توضح لك المقتطف البرمجي التالي كيفية تحويل صفحات PDF إلى صور.

```java
public void convertPDFtoBmp_ParticularPageRegion() {
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
        // Create BMP device with specified attributes
        BmpDevice BmpDevice = new BmpDevice(resolution);

        File file = new File(fileStorage, "PDF-to-BMP.BMP");
        try {
            // Convert a particular page and save the image to stream
            BmpDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
        resultMessage.setText(R.string.success_message);
    }
```
