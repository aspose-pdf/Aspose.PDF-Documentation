---
title: تحسين أو ضغط أو تقليل حجم PDF في Java
linktitle: تحسين مستند PDF
type: docs
weight: 40
url: ar/java/optimize-pdf/
description: تحسين ملف PDF، تقليص جميع الصور، تقليل حجم PDF، إزالة تضمين الخطوط، إزالة الكائنات غير المستخدمة باستخدام Java.
lastmod: "2021-06-05"
---

يمكن أن يحتوي مستند PDF في بعض الأحيان على بيانات إضافية. تقليل حجم ملف PDF سيساعدك على تحسين نقل الشبكة والتخزين. هذا مفيد بشكل خاص للنشر على صفحات الويب، والمشاركة على الشبكات الاجتماعية، والإرسال عبر البريد الإلكتروني، أو الأرشفة في التخزين. يمكننا استخدام عدة تقنيات لتحسين PDF:

- تحسين محتوى الصفحة للتصفح عبر الإنترنت
- تقليص أو ضغط جميع الصور
- تمكين إعادة استخدام محتوى الصفحة
- دمج التدفقات المكررة
- إزالة تضمين الخطوط
- إزالة الكائنات غير المستخدمة
- إزالة أو تسطيح حقول النماذج
- إزالة أو تسطيح التعليقات التوضيحية

## تحسين مستند PDF للويب

يشير التحسين أو الخطية إلى عملية جعل ملف PDF مناسبًا للتصفح عبر الإنترنت باستخدام متصفح الويب.
 Aspose.PDF يدعم هذه العملية.

لتحسين ملف PDF لعرض الويب:

1. افتح المستند المدخل في كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
2. استخدم طريقة [optimize()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#optimize--).
3. احفظ المستند المحسن باستخدام طريقة save(..).

يوضح مقطع الشيفرة التالي كيفية تحسين مستند PDF للويب.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.time.Clock;
import java.time.Duration;

import com.aspose.pdf.*;
import com.aspose.pdf.optimization.ImageCompressionVersion;
import com.aspose.pdf.optimization.ImageEncoding;

public class ExampleOptimize {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void OptimizePDFDocumentForTheWeb() {

        // افتح المستند
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // تحسين للويب
        pdfDocument.optimize();

        // احفظ المستند الناتج
        pdfDocument.save(_dataDir + "OptimizeDocument_out.pdf");
    }
```

## تقليل حجم ملف PDF

يشرح هذا الموضوع الخطوات اللازمة لتحسين/تقليل حجم ملف PDF. توفر Aspose.PDF API فئة [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.optimization/class-use/OptimizationOptions) التي تتيح المرونة لتحسين ملف PDF الناتج عن طريق إزالة الكائنات غير الضرورية وضغط ملفات PDF التي تحتوي على صور. يتم توضيح كلا الخيارين في الأقسام التالية.

### إزالة الكائنات غير الضرورية
يمكننا تحسين حجم مستندات PDF عن طريق إزالة الكائنات المكررة وغير المستخدمة. يوضح المقتطف التالي من الكود كيفية القيام بذلك.

```java
public static void ReduceSizePDF() {

        // فتح المستند
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // تحسين مستند PDF. لاحظ، مع ذلك، أن هذه الطريقة لا يمكنها ضمان
        // تقليص المستند
        pdfDocument.optimizeResources();

        // حفظ المستند الناتج
        pdfDocument.save(_dataDir + "OptimizeDocument_out.pdf");
    }
```

## تقليص أو ضغط جميع الصور

إذا كان ملف PDF المصدر يحتوي على صور، فكر في ضغط الصور وتحديد جودتها. لتمكين ضغط الصور، مرر القيمة true كمعامل إلى الأسلوب setCompressImages(..). سيتم إعادة ضغط جميع الصور في المستند. يتم تعريف الضغط بواسطة الأسلوب setImageQuality(..)، وهو قيمة الجودة بالنسبة المئوية. 100% تعني جودة وحجم صورة غير متغيرين. لتقليل حجم الصورة، مرر معامل أقل من 100 إلى الأسلوب setImageQuality(..).

```java
public static void ShrinkingCompressing() {
        // افتح المستند
        Document pdfDocument = new Document(_dataDir + "Shrinkimage.pdf");

        // تهيئة خيارات التحسين
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        // تعيين خيار ضغط الصور
        optimizationOptions.getImageCompressionOptions().setCompressImages(true);

        // تعيين خيار جودة الصورة
        optimizationOptions.getImageCompressionOptions().setImageQuality(50);

        // تحسين مستند PDF باستخدام خيارات التحسين
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "Shrinkimage_out.pdf";
        // حفظ المستند المحدث
        pdfDocument.save(_dataDir);
    }
```

طريقة أخرى هي تغيير حجم الصور بدقة أقل. في هذه الحالة، يجب علينا تعيين ResizeImages إلى true و MaxResolution إلى القيمة المناسبة.

```java
public static void ShrinkingCompressing2() {
        // فتح المستند
        Document pdfDocument = new Document(_dataDir + "ResizeImage.pdf");

        // تهيئة OptimizationOptions
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        // تعيين خيار CompressImages
        optimizationOptions.getImageCompressionOptions().setCompressImages(true);
        // تعيين خيار ImageQuality
        optimizationOptions.getImageCompressionOptions().setImageQuality(75);

        // تعيين خيار ResizeImage
        optimizationOptions.getImageCompressionOptions().setResizeImages(true);

        // تعيين خيار MaxResolution
        optimizationOptions.getImageCompressionOptions().setMaxResolution(300);

        // تحسين مستند PDF باستخدام OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "ResizeImages_out.pdf";
        // حفظ المستند المحدث
        pdfDocument.save(_dataDir);
    }
```

Another important issue is the execution time. But again, we can manage this setting too. Currently, we can use two algorithms - Standard and Fast. To control the execution time we should set a Version property. The following snippet demonstrates the Fast algorithm:

```java
public static void ShrinkingCompressing3() {

        Clock clock = Clock.systemUTC();

        Duration tickDuration = Duration.ofNanos(250000);
        Clock clock1 = Clock.tick(clock, tickDuration);
        System.out.println("Start : " + clock.instant());

        // فتح المستند
        Document pdfDocument = new Document(_dataDir + "ResizeImage.pdf");

        // تهيئة خيارات التحسين
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        // تعيين خيار ضغط الصور
        optimizationOptions.getImageCompressionOptions().setCompressImages(true);

        // تعيين خيار جودة الصورة
        optimizationOptions.getImageCompressionOptions().setImageQuality(75);

        // تعيين إصدار ضغط الصورة إلى سريع
        optimizationOptions.getImageCompressionOptions().setVersion(ImageCompressionVersion.Fast);

        // تحسين مستند PDF باستخدام خيارات التحسين
        pdfDocument.optimizeResources(optimizationOptions);

        _dataDir = _dataDir + "ResizeImages_out.pdf";

        // حفظ المستند المحدث
        pdfDocument.save(_dataDir);
        System.out.println("Finish : " + clock1.instant());
    }
```

## إزالة الكائنات غير المستخدمة

قد يحتوي مستند PDF أحيانًا على كائنات PDF غير مرجعية من أي كائن آخر في المستند. قد يحدث هذا، على سبيل المثال، عند إزالة صفحة من شجرة صفحات المستند ولكن لم تتم إزالة كائن الصفحة نفسه. إزالة هذه الكائنات لا تجعل المستند غير صالح بل تقلل من حجمه.

```java
    public static void RemovingUnusedObjects() {

        // فتح المستند
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        
        optimizationOptions.setRemoveUnusedObjects(true);
        pdfDocument.optimizeResources(optimizationOptions);
        
        _dataDir = _dataDir + "emoveUnusedObjects_out.pdf";

        // حفظ المستند المحدث
        pdfDocument.save(_dataDir);

    }
```
## إزالة التدفقات غير المستخدمة

أحيانًا يحتوي المستند على تدفقات موارد غير مستخدمة.
 هذه التدفقات ليست "كائنات غير مستخدمة" لأنها مشار إليها من خلال قاموس موارد الصفحة. قد يحدث هذا في الحالات التي تم فيها إزالة صورة من الصفحة ولكن ليس من موارد الصفحة. أيضًا، تحدث هذه الحالة غالبًا عندما يتم استخراج الصفحات من المستند وتكون صفحات المستند تحتوي على موارد "مشتركة"، أي نفس كائن الموارد. يتم تحليل محتويات الصفحة لتحديد ما إذا كان تدفق المورد مستخدمًا أم لا. يتم إزالة التدفقات غير المستخدمة. أحيانًا يؤدي ذلك إلى تقليل حجم المستند.

```java
public static void RemovingUnusedStream() {
        // فتح المستند
        Document pdfDocument = new Document(_dataDir + 
        "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setRemoveUnusedStreams(true);
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "removeUnusedObjects_out.pdf";
        
        // حفظ المستند المحدث
        pdfDocument.save(_dataDir);
        
    }
```
## ربط التدفقات المكررة

أحيانًا يحتوي المستند على عدة تدفقات موارد متطابقة (على سبيل المثال الصور). قد يحدث هذا على سبيل المثال عندما يتم دمج مستند مع نفسه. يحتوي المستند الناتج على نسختين مستقلتين من نفس تدفق المورد. نقوم بتحليل جميع تدفقات الموارد ونقارنها. إذا كانت التدفقات مكررة، يتم دمجها، أي أنه يتم الاحتفاظ بنسخة واحدة فقط، ويتم تغيير المراجع بشكل مناسب ويتم إزالة نسخ الكائن. أحيانًا يؤدي ذلك إلى تقليل حجم المستند.

```java
    public static void LinkingDuplicateStream() {
        // فتح المستند
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setRemoveUnusedStreams(true);
        
        // تحسين مستند PDF باستخدام خيارات التحسين
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        
        // حفظ المستند المحدث
        pdfDocument.save(_dataDir);
    }
```

بالإضافة إلى ذلك، يمكننا استخدام إعدادات AllowReusePageContent. إذا تم تعيين هذه الخاصية إلى true، سيتم إعادة استخدام محتوى الصفحة عند تحسين المستند للصفحات المتطابقة.

```java
public static void AllowReusePageContent() {
        // فتح المستند
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setAllowReusePageContent(true);
        
        // تحسين مستند PDF باستخدام خيارات التحسين
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        
        // حفظ المستند المحدث
        pdfDocument.save(_dataDir);
    }
```
## إزالة تضمين الخطوط

إذا كان المستند يستخدم خطوطًا مدمجة، فهذا يعني أن جميع بيانات الخطوط موجودة في المستند.
 الميزة هي أن المستند يمكن عرضه بغض النظر عما إذا كان الخط مثبتًا على جهاز المستخدم أم لا. لكن تضمين الخطوط يجعل المستند أكبر. تعمل طريقة إزالة تضمين الخطوط على إزالة جميع الخطوط المضمنة. هذا يقلل من حجم المستند ولكن قد يصبح المستند غير قابل للقراءة إذا لم يكن الخط الصحيح مثبتًا.

```java
    public static void UnembedFonts() {
        // افتح المستند
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setUnembedFonts(true);
        
        // تحسين مستند PDF باستخدام خيارات التحسين
        pdfDocument.optimizeResources(optimizationOptions);
        
        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        // احفظ المستند المحدث
        pdfDocument.save(_dataDir);
    }
```

## إزالة أو تسوية التعليقات التوضيحية

يمكن حذف التعليقات التوضيحية عندما لا تكون ضرورية. عندما تكون هناك حاجة إليها ولكن لا تتطلب تحريرًا إضافيًا، يمكن تسويتها. كلتا التقنيتين ستقللان من حجم الملف.

```java
    public static void FlatteningAnnotations() {
        // افتح المستند
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");

        for (Page page : pdfDocument.getPages()) {
            for (Annotation annotation : page.getAnnotations())
                annotation.flatten();
        }

        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        // احفظ المستند المحدث
        pdfDocument.save(_dataDir);
    }

```
## إزالة حقول النماذج

إذا كان مستند الـ PDF يحتوي على AcroForms، يمكننا محاولة تقليل حجم الملف عن طريق تسوية حقول النماذج.

```java
    public static void RemovingFormFields() {
        // افتح المستند
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");

        // تسوية النماذج
        if (pdfDocument.getForm().getFields().length > 0) {
            for (Field field : pdfDocument.getForm().getFields()) {
                field.flatten();
            }
        }
        _dataDir = _dataDir + "FlattenForms_out.pdf";
        // احفظ المستند المحدث
        pdfDocument.save(_dataDir);
    }

```
## تحويل ملف PDF من نظام ألوان RGB إلى تدرج الرمادي

يتكون ملف PDF من نصوص وصور ومرفقات وتعليقات توضيحية ورسوم بيانية وأشياء أخرى. قد تواجه متطلبًا لتحويل ملف PDF من نظام ألوان RGB إلى تدرج الرمادي بحيث يكون أسرع أثناء طباعة تلك الملفات. أيضًا عند تحويل الملف إلى تدرج الرمادي، يتم تقليل حجم المستند ولكن مع هذا التغيير، قد تنخفض جودة المستند. حاليًا، هذه الميزة مدعومة بواسطة ميزة Pre-Flight في Adobe Acrobat، ولكن عند الحديث عن أتمتة المكاتب، فإن Aspose.PDF هو الحل الأمثل لتوفير مثل هذه الامتيازات لمعالجة المستندات.

لتحقيق هذا المتطلب، يمكن استخدام الشيفرة المصدرية التالية.

```java
    public static void ConvertRGBtoGrayscale() {

        // فتح المستند
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");

        com.aspose.pdf.RgbToDeviceGrayConversionStrategy strategy = new com.aspose.pdf.RgbToDeviceGrayConversionStrategy();
        for (int idxPage = 1; idxPage <= pdfDocument.getPages().size(); idxPage++) {
            Page page = pdfDocument.getPages().get_Item(idxPage);
            strategy.convert(page);
        }
        pdfDocument.save("output.pdf");
    }
```

## ضغط FlateDecode

يوفر Aspose.PDF for Java دعمًا لضغط FlateDecode لوظيفة تحسين PDF. يوضح مقتطف الشيفرة التالي كيفية استخدام الخيار في التحسين لتخزين الصور بضغط FlateDecode:

```java
    public static void FlateDecodeCompression() {

        // فتح المستند
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        optimizationOptions.getImageCompressionOptions().setEncoding(ImageEncoding.Flate);

        // تحسين مستند PDF باستخدام خيارات التحسين
        pdfDocument.optimizeResources(optimizationOptions);

        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        // حفظ المستند المحدث
        pdfDocument.save(_dataDir);
    }
```
## تخزين الصورة في XImageCollection

يوفر Aspose.PDF for Java القدرة على تخزين صور جديدة في [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/XImageCollection) بضغط FlateDecode.
 لتفعيل هذا الخيار يمكنك استخدام علم ImageFilterType.Flate. يوضح مقتطف الشيفرة التالي كيفية استخدام هذه الوظيفة:

```java
    public static void StoreImageInXImageCollection() {
        // تهيئة المستند
        Document document = new Document();
        document.getPages().add();
        Page page = document.getPages().get_Item(1);

        // تحميل الصورة في التدفق
        java.io.FileInputStream imageStream = null;
        try {
            imageStream = new java.io.FileInputStream(new java.io.File("input_image1.jpg"));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
            return;
        }
        page.getResources().getImages().add(imageStream, ImageFilterType.Flate);
        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());
        page.getContents().add(new com.aspose.pdf.operators.GSave());

        // تعيين الإحداثيات
        int lowerLeftX = 0;
        int lowerLeftY = 0;
        int upperRightX = 600;
        int upperRightY = 600;
        Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0,
                rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });
        // باستخدام عامل ConcatenateMatrix (دمج المصفوفات): يحدد كيفية وضع الصورة
        page.getContents().add(new com.aspose.pdf.operators.ConcatenateMatrix(matrix));
        page.getContents().add(new com.aspose.pdf.operators.Do(ximage.getName()));
        page.getContents().add(new com.aspose.pdf.operators.GRestore());

        document.save(_dataDir + "FlateDecodeCompression.pdf");
    }

}
```