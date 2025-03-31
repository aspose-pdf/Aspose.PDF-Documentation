---
title: تحويل PDF إلى BMP
linktitle: تحويل PDF إلى BMP
type: docs
weight: 40
url: /ar/androidjava/convert-pdf-to-bmp/
lastmod: "2021-06-05"
description: تصف هذه المقالة كيفية تحويل صفحات PDF إلى صورة BMP، تحويل جميع الصفحات إلى صور BMP وتحويل صفحة PDF واحدة إلى صورة BMP باستخدام Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

تسمح لك فئة [BmpDevice](https://reference.aspose.com/pdf/ar/net/aspose.pdf.devices/bmpdevice) بتحويل صفحات PDF إلى صور <abbr title="ملف صورة نقطية">BMP</abbr>. توفر هذه الفئة طريقة تسمى [Process](https://reference.aspose.com/pdf/ar/net/aspose.pdf.devices/bmpdevice/methods/process) والتي تتيح لك تحويل صفحة معينة من ملف PDF إلى تنسيق صورة Bmp.

{{% alert color="primary" %}}

جرّب عبر الإنترنت. يمكنك التحقق من جودة تحويل Aspose.PDF وعرض النتائج عبر الإنترنت على هذا الرابط [products.aspose.app/pdf/conversion/pdf-to-bmp](https://products.aspose.app/pdf/conversion/pdf-to-bmp)

{{% /alert %}}

تسمح لك فئة BmpDevice بتحويل صفحات PDF إلى صور BMP.
 ## تحويل صفحة PDF إلى صورة BMP

تقدم هذه الفئة طريقة باسم process(..) التي تتيح لك تحويل صفحة معينة من ملف PDF إلى صورة BMP.

## تحويل صفحة PDF إلى صورة BMP

لتحويل صفحة PDF إلى صورة BMP:

1. قم بإنشاء كائن من فئة Document للحصول على الصفحة المحددة التي تريد تحويلها.
2. استدعِ الطريقة process(..) لتحويل الصفحة إلى BMP.

يظهر لك مقطع الشيفرة التالي كيفية تحويل صفحة معينة إلى صورة BMP.

```java
// تحويل PDF إلى BMP
    public void convertPDFtoBMP() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-BMP.bmp");
        // إنشاء كائن stream لحفظ صورة الإخراج
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // إنشاء كائن Resolution
            Resolution resolution = new Resolution(300);

            // إنشاء كائن BmpDevice بدقة معينة
            BmpDevice BmpDevice = new BmpDevice(resolution);

            // تحويل صفحة معينة وحفظ الصورة في stream
            BmpDevice.process(document.getPages().get_Item(1), imageStream);

            // إغلاق stream
            imageStream.close();
            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }
```

## تحويل جميع صفحات PDF إلى صور BMP

لتحويل جميع صفحات ملف PDF إلى تنسيق BMP، تحتاج إلى التكرار للحصول على كل صفحة فردية وتحويلها إلى تنسيق BMP. يوضح لك مقطع الشيفرة التالي كيفية المرور عبر جميع صفحات ملف PDF وتحويلها إلى BMP.

```java
public void convertPDFtoBMP_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // التكرار عبر جميع صفحات ملف PDF
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // إنشاء كائن تدفق لحفظ صورة المخرجات
            File file = new File(fileStorage, "PDF-to-BMP"+pageCount+".BMP");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // إنشاء كائن Resolution
            Resolution resolution = new Resolution(300);
            // إنشاء كائن BmpDevice بدقة معينة
            BmpDevice BmpDevice = new BmpDevice(resolution);

            // تحويل صفحة معينة وحفظ الصورة في التدفق
            BmpDevice.process(document.getPages().get_Item(pageCount), imageStream);

            // إغلاق التدفق
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


## تحويل منطقة معينة من الصفحة إلى صورة (DOM)

يمكننا تحويل مستندات PDF إلى تنسيقات صور مختلفة باستخدام كائنات أجهزة الصور الخاصة بـ Aspose.PDF. ومع ذلك، في بعض الأحيان يكون هناك حاجة لتحويل منطقة معينة من الصفحة إلى تنسيق صورة. يمكننا تحقيق هذا المطلب على خطوتين. في البداية، نقوم بقص صفحة PDF إلى المنطقة المطلوبة ومن ثم تحويلها إلى صورة باستخدام كائن جهاز الصورة المطلوب.

يظهر لك مقتطف الكود التالي كيفية تحويل صفحات PDF إلى صور.

```java
public void convertPDFtoBmp_ParticularPageRegion() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // الحصول على مستطيل منطقة معينة من الصفحة
        //x=0,y=0, w=200, h=125;
        Rectangle pageRect = new Rectangle(0, 0, 200, 125);
        // تعيين قيمة CropBox وفقًا لمستطيل المنطقة المطلوبة من الصفحة
        document.getPages().get_Item(1).setCropBox(pageRect);
        // حفظ المستند المقصوص في التدفق
        ByteArrayOutputStream outStream = new ByteArrayOutputStream();
        document.save(outStream);

        // فتح مستند PDF المقصوص من التدفق وتحويله إلى صورة
        document = new Document(new ByteArrayInputStream(outStream.toByteArray()));
        // إنشاء كائن دقة
        Resolution resolution = new Resolution(300);
        // إنشاء جهاز BMP بالخصائص المحددة
        BmpDevice BmpDevice = new BmpDevice(resolution);

        File file = new File(fileStorage, "PDF-to-BMP.BMP");
        try {
            // تحويل صفحة معينة وحفظ الصورة في التدفق
            BmpDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
        resultMessage.setText(R.string.success_message);
    }
```