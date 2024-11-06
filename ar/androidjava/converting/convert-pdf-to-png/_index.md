---
title: Convert PDF to PNG 
linktitle: Convert PDF to PNG 
type: docs
weight: 20
url: ar/androidjava/convert-pdf-to-png/
lastmod: "2021-06-05"
description: تصفح هذه الصفحة كيفية تحويل صفحات PDF إلى صورة PNG، تحويل جميع الصفحات وصفحة واحدة إلى صور PNG باستخدام Aspose.PDF for Android عبر Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

استخدم مكتبة **Aspose.PDF for Android via Java** لتحويل صفحات PDF إلى صور <abbr title="Portable Network Graphics">PNG</abbr> بطريقة سهلة ومريحة.

تسمح لك فئة PngDevice بتحويل صفحات PDF إلى صور PNG. توفر هذه الفئة طريقة اسمها Process والتي تتيح لك تحويل صفحة معينة من ملف PDF إلى تنسيق صورة PNG.

## تحويل صفحات PDF إلى صور PNG

لتحويل جميع الصفحات في ملف PDF إلى ملفات PNG، قم بالتكرار عبر الصفحات الفردية وقم بتحويل كل منها إلى تنسيق PNG. يوضح مقتطف الشيفرة التالي كيفية الانتقال عبر جميع صفحات ملف PDF وتحويل كل منها إلى صورة PNG.


{{% alert color="primary" %}}

تحقق عبر الإنترنت. يمكنك التحقق من جودة تحويل Aspose.PDF وعرض النتائج عبر الإنترنت على هذا الرابط [products.aspose.app/pdf/conversion/pdf-to-png](https://products.aspose.app/pdf/conversion/pdf-to-png)

{{% /alert %}}

## تحويل صفحة PDF واحدة إلى صورة PNG

قم بتمرير مؤشر الصفحة كمعامل إلى طريقة Process(..). يوضح مقتطف الشيفرة التالي الخطوات لتحويل الصفحة الأولى من PDF إلى تنسيق PNG.

```java
   public void convertPDFtoPNG() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-PNG.png");
        // إنشاء كائن تدفق لحفظ الصورة الناتجة
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // إنشاء كائن Resolution
            Resolution resolution = new Resolution(300);

            // إنشاء كائن PngDevice بدقة معينة
            PngDevice PngDevice = new PngDevice(resolution);

            // تحويل صفحة معينة وحفظ الصورة في التدفق
            PngDevice.process(document.getPages().get_Item(1), imageStream);

            // إغلاق التدفق
            imageStream.close();
            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }

```


## تحويل جميع صفحات PDF إلى صورة PNG

يوضح لك Aspose.PDF لـ Android عبر Java كيفية تحويل جميع الصفحات في ملف PDF إلى صور:

1. قم بالتكرار عبر جميع الصفحات في الملف.
2. قم بتحويل كل صفحة بشكل فردي:
    1. إنشاء كائن من فئة Document لتحميل مستند PDF.
    2. الحصول على الصفحة التي تريد تحويلها.
    3. استدعاء طريقة Process لتحويل الصفحة إلى Png.

يُظهر لك مقتطف الشيفرة التالي كيفية تحويل جميع صفحات PDF إلى صور PNG.

```java
 public void convertPDFtoPNG_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // التكرار عبر جميع صفحات ملف PDF
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // إنشاء كائن تدفق لحفظ صورة الإخراج
            File file = new File(fileStorage, "PDF-to-PNG"+pageCount+".png");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // إنشاء كائن Resolution
            Resolution resolution = new Resolution(300);
            // إنشاء كائن JpegDevice بدقة معينة
            PngDevice JpegDevice = new PngDevice(resolution);

            // تحويل صفحة معينة وحفظ الصورة في التدفق
            JpegDevice.process(document.getPages().get_Item(pageCount), imageStream);

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


## تحويل صفحة معينة من PDF إلى صورة PNG

يوضح Aspose.PDF لـ Android عبر Java كيفية تحويل صفحة معينة إلى تنسيق PNG:

```java
public void convertPDFtoPNG_ParticularPageRegion() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // الحصول على مستطيل منطقة صفحة معينة
        //x=0,y=0, w=200, h=125;
        Rectangle pageRect = new Rectangle(0, 0, 200, 125);
        // تعيين قيمة CropBox وفقًا لمستطيل منطقة الصفحة المطلوبة
        document.getPages().get_Item(1).setCropBox(pageRect);
        // حفظ المستند المقصوص في التدفق
        ByteArrayOutputStream outStream = new ByteArrayOutputStream();
        document.save(outStream);

        // فتح مستند PDF المقصوص من التدفق وتحويله إلى صورة
        document = new Document(new ByteArrayInputStream(outStream.toByteArray()));
        // إنشاء كائن Resolution
        Resolution resolution = new Resolution(300);
        // إنشاء جهاز Jpeg بخصائص محددة
        PngDevice PngDevice = new PngDevice(resolution);

        File file = new File(fileStorage, "PDF-to-PNG.png");
        try {
            // تحويل صفحة معينة وحفظ الصورة في التدفق
            PngDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```