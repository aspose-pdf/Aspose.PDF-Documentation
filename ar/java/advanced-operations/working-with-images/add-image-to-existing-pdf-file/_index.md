---
title: إضافة صورة إلى ملف PDF موجود
linktitle: إضافة صورة
type: docs
weight: 10
url: ar/java/add-image-to-existing-pdf-file/
description: يصف هذا القسم كيفية إضافة صورة إلى ملف PDF موجود باستخدام مكتبة Java.
lastmod: "2021-06-05"
---

تحتوي كل صفحة PDF على خصائص الموارد والمحتوى. يمكن أن تكون الموارد صورًا ونماذج على سبيل المثال، بينما يتم تمثيل المحتوى بمجموعة من مشغلي PDF. لكل مشغل اسمه وحجته. يستخدم هذا المثال المشغلين لإضافة صورة إلى ملف PDF.

لإضافة صورة إلى ملف PDF موجود:

- إنشاء كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) وفتح مستند PDF المدخل.
- احصل على الصفحة التي تريد إضافة صورة إليها.
- أضف الصورة إلى مجموعة [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) الخاصة بالصفحة.
- استخدم المشغلين لوضع الصورة على الصفحة:
- استخدم مشغل GSave لحفظ الحالة الرسومية الحالية.

- استخدم مشغل [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators.class-use/concatenatematrix) لتحديد مكان وضع الصورة.
- استخدم عامل [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/class-use/Do) لرسم الصورة على الصفحة.
- أخيرًا، استخدم عامل [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators.class-use/grestore) لحفظ الحالة الرسومية المحدثة.
- احفظ الملف.

يوضح مقتطف الشيفرة التالي كيفية إضافة الصورة في مستند PDF.

```java
package com.aspose.pdf.examples;

import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;

import javax.imageio.ImageIO;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.PdfFileMend;
import com.aspose.pdf.operators.*;

public class ExampleAddImages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddImageToExistingPDF() throws IOException {
        // افتح مستند
        Document pdfDocument1 = new Document(_dataDir + "sample.pdf");

        // تحديد الإحداثيات
        int lowerLeftX = 50;
        int lowerLeftY = 750;
        int upperRightX = 100;
        int upperRightY = 800;

        // احصل على الصفحة التي تريد إضافة الصورة إليها
        Page page = pdfDocument1.getPages().get_Item(1);

        // تحميل الصورة في تدفق البيانات
        java.io.FileInputStream imageStream = new java.io.FileInputStream(new java.io.File(_dataDir + "logo.png"));

        // أضف صورة إلى مجموعة الصور في موارد الصفحة
        page.getResources().getImages().add(imageStream);

        // باستخدام عامل GSave: هذا العامل يحفظ الحالة الرسومية الحالية
        page.getContents().add(new GSave());

        // إنشاء كائنات Rectangle و Matrix
        Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0,
                rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });

        // باستخدام عامل ConcatenateMatrix (دمج المصفوفات): يحدد كيفية وضع الصورة
        page.getContents().add(new ConcatenateMatrix(matrix));
        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());

        // باستخدام عامل Do: هذا العامل يرسم الصورة
        page.getContents().add(new Do(ximage.getName()));

        // باستخدام عامل GRestore: هذا العامل يستعيد الحالة الرسومية
        page.getContents().add(new GRestore());

        // احفظ ملف PDF الجديد
        pdfDocument1.save(_dataDir + "updated_document.pdf");

        // إغلاق تدفق البيانات للصورة
        imageStream.close();
    }
```


## إضافة صورة من BufferedImage إلى PDF

بدءًا من إصدار Aspose.PDF for Java 9.5.0، قمنا بتقديم الدعم لإضافة صورة من مثيل BufferedImage إلى مستند PDF. من أجل دعم هذا المتطلب، تم تنفيذ طريقة: [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection).add(BufferedImage image);

```java
    public static void AddingImageFromBufferedImageIntoPDF() throws IOException {
        BufferedImage originalImage = ImageIO.read(new File("anyImage.jpg"));
        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();
        page.getResources().getImages().add(originalImage);
    }
```

يمكنك استخدام أي InputStream وليس فقط كائن FileInputStream لإضافة صورة. لذلك عند استخدام كائن java.io.ByteArrayInputStream، لا تحتاج إلى تخزين أي ملفات على النظام:

```java
    public static void AddingImageFromBufferedImageIntoPDF2() throws IOException {
        BufferedImage originalImage = ImageIO.read(new File("anyImage.jpg"));
        ByteArrayOutputStream baos = new ByteArrayOutputStream();

        Document pdfDocument = new Document();
        ImageIO.write(originalImage, "jpg", baos);
        baos.flush();
        Page page = pdfDocument.getPages().get_Item(1);
        page.getResources().getImages().add(new ByteArrayInputStream(baos.toByteArray()));
    }
```


## إضافة صورة إلى ملف PDF موجود (Facades)

هناك أيضًا طريقة بديلة وأسهل لإضافة صورة إلى ملف PDF. يمكنك استخدام طريقة AddImage في فئة [PdfFileMend](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileMend). تتطلب طريقة AddImage إضافة الصورة، ورقم الصفحة الذي تحتاج الصورة إلى إضافتها فيه والمعلومات الخاصة بالإحداثيات. بعد ذلك، قم بحفظ ملف PDF المحدث باستخدام طريقة Close.

يظهر لك مقطع الشيفرة التالي كيفية إضافة صورة في ملف PDF موجود.

```java
    public static void AddImageInAnExistingPDFFile_Facades() {
        // فتح المستند
        PdfFileMend mender = new PdfFileMend();

        // إنشاء كائن PdfFileMend لإضافة النص
        mender.bindPdf(_dataDir + "AddImage.pdf");

        // إضافة صورة في ملف PDF
        mender.addImage(_dataDir + "aspose-logo.jpg", 1, 100, 600, 200, 700);

        // حفظ التغييرات
        mender.save(_dataDir + "AddImage_out.pdf");

        // إغلاق كائن PdfFileMend
        mender.close();
    }
```


## إضافة مرجع لصورة واحدة عدة مرات في مستند PDF

أحيانًا يكون لدينا متطلب لاستخدام نفس الصورة عدة مرات في مستند PDF. إضافة نسخة جديدة يزيد من حجم مستند PDF الناتج. لقد أضفنا طريقة جديدة XImageCollection.add(XImage) التي تدعم كائن XImage للإضافة في مجموعة الصور. تتيح هذه الطريقة إضافة مرجع لنفس كائن PDF كالصورة الأصلية التي تعمل على تحسين حجم مستند PDF.

```java
    public static void AddReferenceOfaSingleImageMultipleTimes() throws FileNotFoundException {
        Rectangle imageRectangle = new Rectangle(0, 0, 30, 15);
        Document document = new Document(_dataDir + "sample.pdf");
        document.getPages().add();
        document.getPages().add();
        java.io.FileInputStream imageStream = new java.io.FileInputStream(
                new java.io.File(_dataDir + "aspose-logo.png"));

        XImage image = null;

        for (Page page : document.getPages()) {
            WatermarkAnnotation annotation = new WatermarkAnnotation(page, page.getRect());
            XForm form = annotation.getAppearance().get_Item("N");
            form.setBBox(page.getRect());
            String name;
            if (image == null) {
                name = form.getResources().getImages().add(imageStream);
                image = form.getResources().getImages().get_Item(name);
            } else {
                name = form.getResources().getImages().add(image);
            }
            form.getContents().add(new GSave());
            form.getContents().add(new ConcatenateMatrix(
                    new Matrix(imageRectangle.getWidth(), 0, 0, imageRectangle.getHeight(), 0, 0)));
            form.getContents().add(new Do(name));
            form.getContents().add(new GRestore());
            page.getAnnotations().add(annotation, false);
            imageRectangle = new Rectangle(0, 0, imageRectangle.getWidth() * 1.01, imageRectangle.getHeight() * 1.01);
        }
        document.save(_dataDir + "output.pdf");
    }
```


## تحديد ما إذا كانت الصورة داخل PDF ملونة أو بالأبيض والأسود

يمكن تطبيق أنواع مختلفة من الضغط على الصور لتقليل حجمها. يعتمد نوع الضغط المطبق على الصورة على ColorSpace للصورة المصدرية، أي إذا كانت الصورة ملونة (RGB)، فسيتم تطبيق ضغط JPEG2000، وإذا كانت بالأبيض والأسود، فيجب تطبيق ضغط JBIG2/JBIG2000. لذلك، فإن تحديد نوع كل صورة واستخدام نوع الضغط المناسب سيخلق أفضل وأمثل مخرجات.

قد يحتوي ملف PDF على عناصر مثل النصوص والصور والرسوميات والمرفقات والتعليقات التوضيحية وما إلى ذلك، وإذا كان ملف PDF المصدر يحتوي على صور، يمكننا تحديد مساحة لون الصورة وتطبيق الضغط المناسب للصورة لتقليل حجم ملف PDF. يوضح مقتطف الشيفرة التالي الخطوات لتحديد ما إذا كانت الصورة داخل PDF ملونة أو بالأبيض والأسود.

```java
    public static void CheckColors() {

        Document document = new Document(_dataDir + "test4.pdf");
        try {
            // التكرار عبر جميع صفحات ملف PDF
            for (Page page : (Iterable<Page>) document.getPages()) {
                // إنشاء مثيل لامتصاص موضع الصورة
                ImagePlacementAbsorber abs = new ImagePlacementAbsorber();
                page.accept(abs);
                for (ImagePlacement ia : (Iterable<ImagePlacement>) abs.getImagePlacements()) {
                    /* نوع اللون */
                    int colorType = ia.getImage().getColorType();
                    switch (colorType) {
                    case ColorType.Grayscale:
                        System.out.println("صورة بالأبيض والأسود");
                        break;
                    case ColorType.Rgb:
                        System.out.println("صورة ملونة");
                        break;
                    }
                }
            }
        } catch (Exception ex) {
            System.out.println("خطأ في قراءة الملف = " + document.getFileName());
        }
    }
}
```