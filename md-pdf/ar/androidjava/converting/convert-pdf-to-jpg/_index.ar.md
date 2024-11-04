---
title: تحويل PDF إلى JPG 
linktitle: تحويل PDF إلى JPG
type: docs
weight: 10
url: /androidjava/convert-pdf-to-jpg/
description: تصف هذه الصفحة كيفية تحويل صفحات PDF إلى صور JPEG، تحويل جميع الصفحات وصفحات محددة إلى صور JPEG باستخدام Aspose.PDF for Android عبر Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## تحويل صفحات PDF إلى صور JPG

تسمح لك فئة JpegDevice بتحويل صفحات PDF إلى صور JPEG. توفر هذه الفئة طريقة تسمى process(..) والتي تتيح لك تحويل صفحة معينة من ملف PDF إلى صورة JPEG.

{{% alert color="primary" %}}

جرب عبر الإنترنت. يمكنك التحقق من جودة تحويل Aspose.PDF وعرض النتائج عبر الإنترنت في هذا الرابط [products.aspose.app/pdf/conversion/pdf-to-jpg](https://products.aspose.app/pdf/conversion/pdf-to-jpg)

{{% /alert %}}


## تحويل صفحة واحدة من PDF إلى صورة JPG

يتيح لك Aspose.PDF for Android عبر Java تحويل صفحة واحدة إلى تنسيق Jpeg.

لتحويل صفحة واحدة فقط إلى صورة JPEG:

1. قم بإنشاء كائن من فئة المستند للحصول على الصفحة التي تريد تحويلها.
1. قم باستدعاء الطريقة process(..) لتحويل الصفحة إلى صورة JPEG.

يظهر مقتطف الشيفرة التالي الخطوات لتحويل الصفحة الأولى من PDF إلى صيغة Jpeg.

```java
public void convertPDFtoJPEG() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-JPEG.jpeg");
        // إنشاء كائن التدفق لحفظ صورة الإخراج
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // إنشاء كائن الدقة
            Resolution resolution = new Resolution(300);

            // إنشاء كائن JpegDevice بدقة معينة
            JpegDevice JpegDevice = new JpegDevice(resolution);

            // تحويل صفحة معينة وحفظ الصورة في التدفق
            JpegDevice.process(document.getPages().get_Item(1), imageStream);

            // إغلاق التدفق
            imageStream.close();

            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }

```


## تحويل جميع صفحات PDF إلى صورة JPG

تتيح لك Aspose.PDF for Android عبر Java تحويل جميع الصفحات في ملف PDF إلى صور:

1. قم بالتكرار عبر جميع الصفحات في الملف.
2. قم بتحويل كل صفحة بشكل فردي:
   - قم بإنشاء كائن من فئة Document لتحميل مستند PDF.
   - احصل على الصفحة التي تريد تحويلها.
   - استدعاء طريقة Process لتحويل الصفحة إلى Jpeg.

يظهر لك مقطع الشيفرة التالي كيفية تحويل جميع صفحات PDF إلى صور Jpeg.

```java
public void convertPDFtoJPEG_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // التكرار عبر جميع صفحات ملف PDF
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // إنشاء كائن تيار لحفظ صورة الإخراج
            File file = new File(fileStorage, "PDF-to-JPEG"+pageCount+".jpeg");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // إنشاء كائن Resolution
            Resolution resolution = new Resolution(300);
            // إنشاء كائن JpegDevice بدقة محددة
            JpegDevice JpegDevice = new JpegDevice(resolution);

            // تحويل صفحة معينة وحفظ الصورة في التيار
            JpegDevice.process(document.getPages().get_Item(pageCount), imageStream);

            // إغلاق التيار
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


## تحويل صفحة معينة من PDF إلى صورة JPG

```java
   public void convertPDFtoJPEG_ParticularPageRegion() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // الحصول على مستطيل لمنطقة صفحة معينة
        //x=0,y=0, w=200, h=125;
        Rectangle pageRect = new Rectangle(0, 0, 200, 125);
        // تعيين قيمة CropBox حسب مستطيل منطقة الصفحة المطلوبة
        document.getPages().get_Item(1).setCropBox(pageRect);
        // حفظ المستند المقتطع في المجرى
        ByteArrayOutputStream outStream = new ByteArrayOutputStream();
        document.save(outStream);

        // فتح مستند PDF المقتطع من المجرى وتحويله إلى صورة
        document = new Document(new ByteArrayInputStream(outStream.toByteArray()));
        // إنشاء كائن Resolution
        Resolution resolution = new Resolution(300);
        // إنشاء جهاز Jpeg مع الخصائص المحددة
        JpegDevice JpegDevice = new JpegDevice(resolution);

        File file = new File(fileStorage, "PDF-to-JPEG.jpeg");
        try {
            // تحويل صفحة معينة وحفظ الصورة في المجرى
            JpegDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```