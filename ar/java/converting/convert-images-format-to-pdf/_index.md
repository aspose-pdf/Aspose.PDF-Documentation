---
title: تحويل تنسيقات الصور المختلفة إلى PDF
linktitle: تحويل الصور إلى PDF
type: docs
weight: 60
url: ar/java/convert-images-format-to-pdf/
lastmod: "2021-11-19"
description: يوضح هذا الموضوع كيفية استخدام مكتبة Aspose.PDF for Java لتحويل تنسيقات الصور المختلفة إلى PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF for Java** يتيح لك تحويل تنسيقات مختلفة من الصور إلى ملفات PDF. تعرض مكتبتنا مقتطفات من الشيفرة لتحويل أكثر تنسيقات الصور شيوعًا، مثل - BMP وCGM وDICOM وEMF وJPG وPNG وSVG وTIFF.

## تحويل BMP إلى PDF

تحويل ملفات BMP إلى مستند PDF باستخدام مكتبة **Aspose.PDF for Java**.

صور <abbr title="ملف صورة نقطية">BMP</abbr> هي ملفات بامتداد .BMP تمثل ملفات الصور النقطية التي تُستخدم لتخزين الصور الرقمية النقطية. هذه الصور مستقلة عن محول الرسوميات وتُعرف أيضًا بتنسيق ملف نقطية مستقل عن الجهاز (DIB).
يمكنك تحويل BMP إلى PDF باستخدام Aspose.PDF for Java API.
 لذلك، يمكنك اتباع الخطوات التالية لتحويل الصور BMP:

1. تهيئة مستند جديد
2. تحميل ملف صورة BMP نموذجي
3. وأخيراً، حفظ ملف PDF الناتج

لذلك، يتبع جزء الشيفرة التالي هذه الخطوات ويعرض كيفية تحويل BMP إلى PDF باستخدام Java:

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertBMPtoPDF {

    private ConvertBMPtoPDF() {
    }

    private static Path _dataDir = Paths.get("<set path to samples>");

    public static void main(String[] args) throws FileNotFoundException {
        // تهيئة كائن الوثيقة
        Document document = new Document();

        Page page = document.getPages().add();        
        Image image = new Image();
        
        // تحميل ملف صورة BMP نموذجي
        image.setFile(Paths.get(_dataDir.toString(), "Sample.bmp").toString());
        page.getParagraphs().add(image);
        
        // حفظ مستند PDF الناتج
        document.save(Paths.get(_dataDir.toString(),"BMPtoPDF.pdf").toString());
    }
}
```

{{% alert color="success" %}}
**حاول تحويل BMP إلى PDF عبر الإنترنت**

تقدم لك Aspose تطبيقًا مجانيًا عبر الإنترنت ["BMP إلى PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل BMP إلى PDF باستخدام التطبيق المجاني](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## تحويل CGM إلى PDF

<abbr title="Computer Graphics Metafile">CGM</abbr> هو معيار ISO يوفر تنسيق ملف صورة ثنائي الأبعاد قائم على المتجهات لتخزين واسترجاع معلومات الرسوميات. CGM هو تنسيق مستقل عن الجهاز. CGM هو تنسيق رسوميات متجهة يدعم ثلاث طرق ترميز مختلفة: ثنائية (الأفضل لسرعة قراءة البرنامج)، قائمة على الأحرف (تنتج أصغر حجم ملف وتسمح بنقل البيانات بشكل أسرع) أو ترميز النص الواضح (يسمح للمستخدمين بقراءة وتعديل الملف باستخدام محرر نصوص).

يُظهر لك مقتطف الشيفرة التالي كيفية تحويل ملفات CGM إلى تنسيق PDF باستخدام Aspose.PDF for Java.

1. إنشاء فئة [CgmLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/cgmloadoptions/).
1. إنشاء مثيل من فئة [Document](https://reference.aspose.com/page/java/com.aspose.page/Document) مع ذكر اسم الملف المصدر والخيارات.
1. حفظ المستند بالاسم المطلوب.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertCGMtoPDF {

    private ConvertCGMtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // إنشاء CGM LoadOptions
        CgmLoadOptions options = new CgmLoadOptions();

        // تهيئة كائن المستند
        String cgmFileName = Paths.get(_dataDir.toString(), "corvette.cgm").toString();
        Document document = new Document(cgmFileName, options);

        // حفظ مستند PDF الناتج
        document.save(Paths.get(_dataDir.toString(),"CGMtoPDF.pdf").toString());
    }
}
```


## تحويل DICOM إلى PDF

<abbr title="التصوير الرقمي والاتصالات في الطب">DICOM</abbr> هو معيار للتعامل مع المعلومات في التصوير الطبي وتخزينها وطباعتها ونقلها. يتضمن تعريف صيغة الملف وبروتوكول الاتصالات الشبكية.

Aspose.PDF لـ Java يتيح لك تحويل ملفات DICOM إلى صيغة PDF، تحقق من مقطع الكود التالي:

1. تحميل الصورة في التدفق
1. تهيئة [كائن المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)
1. تحميل ملف صورة DICOM النموذجي
1. حفظ مستند PDF الناتج

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertDICOMtoPDF {

    private ConvertDICOMtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // تحميل الصورة في التدفق
        FileInputStream imageStream = new FileInputStream(
            new java.io.File(Paths.get(_dataDir.toString(),"0002.dcm").toString()));

        // تهيئة كائن المستند
        Document document = new Document();
        document.getPages().add();
        
        // تحميل ملف صورة DICOM النموذجي
        Image image = new Image();
        image.setFileType(ImageFileType.Dicom);
        image.setImageStream(imageStream);

        document.getPages().get_Item(1).getParagraphs().add(image);

        // حفظ مستند PDF الناتج
        document.save(Paths.get(_dataDir.toString(),"CGMtoPDF.pdf").toString());
    }
}
```


{{% alert color="success" %}}
**حاول تحويل DICOM إلى PDF عبر الإنترنت**

تقدم Aspose لك تطبيقًا مجانيًا عبر الإنترنت ["DICOM إلى PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/) ، حيث يمكنك محاولة استكشاف الوظيفة والجودة التي يعمل بها.

[![Aspose.PDF تحويل DICOM إلى PDF باستخدام التطبيق المجاني](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## تحويل EMF إلى PDF

تنسيق الملف الوصفي المحسن (<abbr title="Enhanced metafile format">EMF</abbr>) يخزن الصور الرسومية بشكل مستقل عن الجهاز. يتكون الملفات الوصفية لـ EMF من سجلات بطول متغير بترتيب زمني يمكنها عرض الصورة المخزنة بعد تحليلها على أي جهاز إخراج.

لدينا عدة طرق لتحويل EMF إلى PDF.

## باستخدام فئة Image

يتكون مستند PDF من صفحات وتحتوي كل صفحة على كائنات فقرة واحدة أو أكثر. يمكن أن تكون الفقرة نصًا أو صورة أو جدولًا أو صندوقًا عائمًا أو رسمًا بيانيًا أو عنوانًا أو حقل نموذج أو مرفقًا.

لتحويل ملف صورة إلى تنسيق PDF، قم بتضمينه في فقرة.

من الممكن تحويل الصور في موقع مادي على القرص الصلب المحلي، أو الموجودة في عنوان URL على الويب أو في كائن Stream.

لإضافة صورة:

1. قم بإنشاء كائن من فئة com.aspose.pdf.Image.
1. أضف الصورة إلى مجموعة [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/paragraphs) في مثيل الصفحة.
1. حدد المسار أو مصدر الصورة.
   - إذا كانت الصورة في موقع على القرص الصلب، حدد موقع المسار باستخدام الطريقة [Image.setFile(…)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image).
   - إذا كانت الصورة موجودة في FileInputStream، مرر الكائن الذي يحتوي على الصورة إلى الطريقة [Image.setImageStream(…)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image).

يوضح مقطع الشيفرة التالي كيفية تحميل كائن الصورة، وضبط هامش الصفحة، ووضع الصورة على الصفحة وحفظ الناتج كملف PDF.

```java
package com.aspose.pdf.examples;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;

/**
 * تحويل EMF إلى PDF
 */

import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import javax.imageio.ImageIO;

import com.aspose.pdf.*;

public final class ConvertEMFtoPDF {

    private ConvertEMFtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {

        convertEMFtoPDF_01();
        convertEMFtoPDF_02();
    }

    

    public static void convertEMFtoPDF_01() throws FileNotFoundException {                
        // إنشاء كائن مستند
        Document doc = new Document();
        // أضف صفحة إلى مجموعة الصفحات في المستند
        Page page = doc.getPages().add();
        // تحميل ملف الصورة المصدر إلى كائن Stream
        java.io.FileInputStream fs = new java.io.FileInputStream(
            Paths.get(_dataDir.toString(),"source.emf").toString());

        // ضبط الحدود لتتناسب الصورة، إلخ.
        page.getPageInfo().getMargin().setBottom(0);
        page.getPageInfo().getMargin().setTop(0);
        page.getPageInfo().getMargin().setLeft(0);
        page.getPageInfo().getMargin().setRight(0);

        page.setCropBox(new Rectangle(0, 0, 400, 400));
        // إنشاء كائن صورة
        Image image1 = new Image();
        // أضف الصورة إلى مجموعة الفقرات في القسم
        page.getParagraphs().add(image1);
        // تعيين تدفق ملف الصورة
        image1.setImageStream(fs);
        // حفظ ملف PDF الناتج
        doc.save("EMFtoPDF_01.pdf");
    }   
    public static void convertEMFtoPDF_02() throws IOException {
        // راجع الشيفرة أدناه
    } 
}
```


### إضافة صورة من BufferedImage

يقدم Aspose.PDF for Java أيضًا ميزة تحميل الصورة من مثيل Stream حيث يمكن تحميل الصورة إلى كائن BufferedImage ويمكن وضعها داخل مجموعة الفقرات في ملف Pdf.

```java
public static void convertEMFtoPDF_02() throws IOException {    
    Document doc = new Document();
    // إضافة صفحة إلى مجموعة الصفحات في ملف Pdf
    Page page = doc.getPages().add();
    // إنشاء مثيل للصورة
    Image image1 = new Image();
    // إنشاء مثيل BufferedImage
    java.awt.image.BufferedImage bufferedImage = ImageIO.read(new File("source.emf"));
    ByteArrayOutputStream baos = new ByteArrayOutputStream();
    // كتابة الصورة المخبأة إلى مثيل OutputStream
    ImageIO.write(bufferedImage, "emf", baos);
    baos.flush();
    ByteArrayInputStream bais = new ByteArrayInputStream(baos.toByteArray());
    // إضافة الصورة إلى مجموعة الفقرات في الصفحة الأولى
    page.getParagraphs().add(image1);
    // تعيين تدفق الصورة كـ OutputStream يحتفظ بالصورة المخبأة
    image1.setImageStream(bais);
    // حفظ ملف PDF الناتج
    doc.save("BufferedImage.pdf");
}
```


## إضافة صورة باستخدام مشغلي PDF

يحتوي كل كائن صفحة PDF على الطريقتين [getResources()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) و[getContents()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getContents--). يمكن أن تكون الموارد صورًا ونماذج، على سبيل المثال، بينما يتم تمثيل المحتوى بمجموعة من مشغلي PDF. لكل مشغل اسم وحجج خاصة به.

يستخدم هذا المثال المشغلين لإضافة صورة إلى ملف PDF.

لإضافة صورة إلى ملف PDF موجود:

1. أنشئ كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) وافتح مستند PDF المدخل.
2. احصل على الصفحة التي تريد إضافة صورة إليها.
3. أضف الصورة إلى مجموعة [getResources()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) الخاصة بالصفحة.
4. استخدم المشغلين لوضع الصورة على الصفحة:
   1. استخدم المشغل GSave لحفظ الحالة الرسومية الحالية.
   2. استخدم المشغل ConcatenateMatrix لتحديد مكان وضع الصورة.

1. استخدم المشغل Do لرسم الصورة على الصفحة.
2. أخيرًا، استخدم المشغل GRestore لحفظ الحالة الرسومية المحدثة.
3. احفظ الملف.

يعرض مقتطف الكود التالي كيفية إضافة صورة إلى مستند PDF.

```java
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.Pdf-for-Java
// افتح مستند
Document pdfDocument1 = new Document("input.pdf");

// تعيين الإحداثيات
int lowerLeftX = 100;
int lowerLeftY = 100;
int upperRightX = 200;
int upperRightY = 200;

// الحصول على الصفحة التي تريد إضافة الصورة إليها
Page page = pdfDocument1.getPages().get_Item(1);

// تحميل الصورة في تدفق
java.io.FileInputStream imageStream = new java.io.FileInputStream(new java.io.File("input_image1.jpg"));

// إضافة صورة إلى مجموعة الصور في موارد الصفحة
page.getResources().getImages().add(imageStream);

// استخدام المشغل GSave: هذا المشغل يحفظ الحالة الرسومية الحالية
page.getContents().add(new Operator.GSave());

// إنشاء كائنات مستطيل ومصفوفة
Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0, rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });

// استخدام المشغل ConcatenateMatrix (دمج المصفوفة): يحدد كيفية وضع الصورة
page.getContents().add(new Operator.ConcatenateMatrix(matrix));
XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());

// استخدام المشغل Do: هذا المشغل يرسم الصورة
page.getContents().add(new Operator.Do(ximage.getName()));

// استخدام المشغل GRestore: هذا المشغل يستعيد الحالة الرسومية
page.getContents().add(new Operator.GRestore());

// احفظ ملف PDF الجديد
pdfDocument1.save("Updated_document.pdf");

// أغلق تدفق الصورة
imageStream.close();
```


{{% alert color="success" %}}
**حاول تحويل EMF إلى PDF عبر الإنترنت**

تقدم لك Aspose تطبيقًا مجانيًا عبر الإنترنت ["EMF to PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF EMF إلى PDF باستخدام التطبيق المجاني](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## تحويل JPG إلى PDF

لا داعي للتساؤل عن كيفية تحويل JPG إلى PDF، لأن مكتبة Apose.PDF لـ Java لديها أفضل حل.

يمكنك بسهولة كبيرة تحويل صور JPG إلى PDF باستخدام Aspose.PDF لـ Java باتباع الخطوات التالية:

1. تهيئة كائن من فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)
1. تحميل صورة JPG وإضافتها إلى الفقرة
1. حفظ ملف PDF الناتج

يوضح مقتطف الشيفرة أدناه كيفية تحويل صورة JPG إلى PDF باستخدام Java:

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertJPEGtoPDF {

    private static Path _dataDir = Paths.get("/home/aspose/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        // تهيئة كائن الوثيقة
        Document document = new Document();

        Page page = document.getPages().add();
        Image image = new Image();

        // تحميل ملف صورة JPEG النموذجية
        image.setFile(Paths.get(_dataDir.toString(), "Sample.jpg").toString());
        page.getParagraphs().add(image);

        // حفظ ملف PDF الناتج
        document.save(Paths.get(_dataDir.toString(),"JPEGtoPDF.pdf").toString());
    }
}
```


{{% alert color="success" %}}
**حاول تحويل JPG إلى PDF عبر الإنترنت**

تقدم لك Aspose تطبيقًا مجانيًا عبر الإنترنت ["JPG إلى PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من JPG إلى PDF باستخدام التطبيق المجاني](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## تحويل PNG إلى PDF

يدعم **Aspose.PDF for Java** ميزة تحويل صور PNG إلى تنسيق PDF. تحقق من مقتطف الكود التالي لتحقيق مهمتك.

يشير <abbr title="Portable Network Graphics">PNG</abbr> إلى نوع من تنسيقات ملفات الصور النقطية التي تستخدم الضغط غير الفاقد، مما يجعله شائعًا بين مستخدميه.

يمكنك تحويل PNG إلى صورة PDF باستخدام الخطوات التالية:

1. تحميل صورة PNG المدخلة
1. قراءة قيم الطول والعرض
1. إنشاء مستند جديد وإضافة صفحة
1. تعيين أبعاد الصفحة
1. حفظ الملف الناتج

علاوة على ذلك، يوضح مقتطف الكود أدناه كيفية تحويل PNG إلى PDF في تطبيقات Java الخاصة بك:

```java
package com.aspose.pdf.examples;

/**
 * تحويل PNG إلى PDF
 */

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertPNGtoPDF {

    private ConvertPNGtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        // تهيئة كائن المستند
        Document document = new Document();

        Page page = document.getPages().add();
        Image image = new Image();

        // تحميل ملف صورة BMP النموذجي
        image.setFile(Paths.get(_dataDir.toString(), "Sample.png").toString());


        page.getPageInfo().getMargin().setBottom(0);
        page.getPageInfo().getMargin().setTop(0);
        page.getPageInfo().getMargin().setRight (0);
        page.getPageInfo().getMargin().setLeft (0);
        page.getParagraphs().add(image);

        // حفظ مستند PDF الناتج
        document.save(Paths.get(_dataDir.toString(), "PNGtoPDF.pdf").toString());
    }
}
```


{{% alert color="success" %}}
**حاول تحويل PNG إلى PDF عبر الإنترنت**

تقدم لك Aspose تطبيقًا مجانيًا عبر الإنترنت ["PNG إلى PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PNG إلى PDF باستخدام التطبيق المجاني](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## تحويل SVG إلى PDF

رسومات المتجهات القابلة للتطوير (SVG) هي مجموعة من المواصفات لصيغة ملفات XML للرسم المتجهي ثنائي الأبعاد، سواء كان ثابتًا أو ديناميكيًا (تفاعليًا أو متحركًا). تعتبر مواصفات SVG معيارًا مفتوحًا قيد التطوير من قبل اتحاد شبكة الويب العالمية (W3C) منذ عام 1999.

يتم تعريف صور SVG وسلوكياتها في ملفات نصية بتنسيق XML.
 هذا يعني أنه يمكن البحث عنها وفهرستها وبرمجتها، وإذا لزم الأمر، ضغطها. كملفات XML، يمكن إنشاء وتحرير صور SVG بأي محرر نصوص، ولكن من الأكثر ملاءمة غالبًا إنشاؤها باستخدام برامج الرسم مثل Inkscape

## كيفية تحويل ملف SVG إلى تنسيق PDF

لتحويل ملفات SVG إلى PDF، استخدم الفئة المسماة [SvgLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgloadoptions) والتي تُستخدم لتهيئة كائن [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions). لاحقًا، يتم تمرير هذا الكائن كمعامل أثناء تهيئة كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) ويساعد محرك عرض PDF في تحديد تنسيق إدخال المستند المصدر.

يوضح مقتطف الشيفرة التالي عملية تحويل ملف SVG إلى تنسيق PDF.

```java
// تهيئة كائن المستند

String pdfDocumentFileName = Paths.get(_dataDir.toString(), "svg_test.pdf").toString();
String svgDocumentFileName = Paths.get(_dataDir.toString(), "car.svg").toString();

SvgLoadOptions option = new SvgLoadOptions();
Document pdfDocument = new Document(svgDocumentFileName, option);
pdfDocument.save(pdfDocumentFileName);
```

{{% alert color="success" %}}
**حاول تحويل صيغة SVG إلى PDF عبر الإنترنت**

يقدم لك Aspose.PDF for Java تطبيقًا مجانيًا عبر الإنترنت ["SVG إلى PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf)، حيث يمكنك تجربة فحص الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل SVG إلى PDF باستخدام التطبيق المجاني](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

## تحويل TIFF إلى PDF

يدعم **Aspose.PDF for Java** تنسيق الملفات، سواء كانت صورة <abbr title="تنسيق ملف صورة مُعنون">TIFF</abbr> ذات إطار واحد أو متعددة الإطارات. يعني هذا أنه يمكنك تحويل صورة TIFF إلى PDF في تطبيقات Java الخاصة بك.

TIFF أو TIF، تنسيق ملف صورة مُعنون، يمثل الصور النقطية التي تُستخدم على مجموعة متنوعة من الأجهزة التي تتوافق مع هذا المعيار لتنسيق الملفات.
 TIFF يمكن أن تحتوي الصورة على عدة إطارات مع صور مختلفة. يتم دعم صيغة ملف Aspose.PDF أيضًا، سواء كانت صورة TIFF بإطار واحد أو بإطارات متعددة. لذا يمكنك تحويل صورة TIFF إلى PDF في تطبيقات Java الخاصة بك. لذلك، سننظر في مثال لتحويل صورة TIFF متعددة الصفحات إلى مستند PDF متعدد الصفحات بالخطوات التالية:

1. إنشاء مثيل لفئة Document
1. تحميل صورة TIFF المدخلة
1. أخيرًا، حفظ الصورة كصفحة PDF

علاوة على ذلك، يوضح جزء الشيفرة التالي كيفية تحويل صورة TIFF متعددة الصفحات أو متعددة الإطارات إلى PDF:

```java
import com.aspose.pdf.Document;
import com.aspose.pdf.Image;
import com.aspose.pdf.Page;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * تحويل TIFF إلى PDF.
 */
public final class ConvertTIFFtoPDF {

    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    private ConvertTIFFtoPDF() {
    }

    public static void run() throws IOException {
        // تهيئة كائن الوثيقة
        Document document = new Document();

        Page page = document.getPages().add();
        Image image = new Image();

        image.setFile(Paths.get(DATA_DIR.toString(), "Sample.tiff").toString());
        page.getParagraphs().add(image);

        // حفظ وثيقة PDF الناتجة
        document.save(Paths.get(DATA_DIR.toString(), "TIFFtoPDF.pdf").toString());
        document.close();
    }    
}
```