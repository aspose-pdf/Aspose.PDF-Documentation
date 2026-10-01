---
title: إضافة صورة إلى PDF باستخدام Java
linktitle: إضافة صورة
type: docs
weight: 10
url: /ar/java/add-image-to-existing-pdf-file/
description: تعلم كيفية إضافة صور إلى ملفات PDF الحالية باستخدام Java.
lastmod: "2026-10-01"
TechArticle: true
AlternativeHeadline: إضافة صور إلى ملفات PDF الحالية باستخدام Java
Abstract: توضح هذه المقالة كيفية إضافة صور إلى مستندات PDF باستخدام Aspose.PDF for Java. وتتناول وضع صورة عند إحداثيات ثابتة، وإضافة صور عبر مشغلات الصفحة ذات المستوى المنخفض، وتعيين نص بديل لتحسين إمكانية الوصول، وتضمين بيانات الصورة باستخدام ضغط Flate.
---
يدعم Aspose.PDF for Java كل من وضع الصور على مستوى عالٍ والرسم القائم على المشغلات ذات المستوى المنخفض.

## إضافة صورة باستخدام إحداثيات الصفحة

استخدم هذا المثال عندما تحتاج إلى وضع صورة في موضع ثابت على صفحة PDF.

1. إنشاء ملف PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحة.
1. اتصال `page.addImage()` مع مسار الصورة المصدر والمستطيل الهدف.
1. احفظ ملف PDF المُولَّد.

```java
public static void addImage(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.addImage(imageFile.toString(), new Rectangle(20, 730, 120, 830, true));
        document.save(outputFile.toString());
    }
}
```

## أضف صورة باستخدام مشغلات الصفحة

استخدم هذا المثال عندما تحتاج إلى التحكم منخفض المستوى في موضع الصورة وتكبيرها/تصغيرها عبر عوامل تشغيل الصفحة.

1. إنشاء ملف PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وافتح تدفق صورة المصدر.
1. أضف الصورة إلى موارد الصفحة واحسب المستطيل الهدف.
1. اكتب عوامل تشغيل الرسومات المطلوبة واحفظ المستند.

```java
public static void addImageUsingOperators(Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document();
         InputStream imageStream = Files.newInputStream(imageFile)) {
        Page page = document.getPages().add();
        page.setPageSize(842, 595);

        XImageCollection resourcesImages = page.getResources().getImages();
        String imageId = resourcesImages.add(imageStream);
        XImage xImage = resourcesImages.get_Item(resourcesImages.size());

        Rectangle rectangle = new Rectangle(
                0,
                0,
                page.getMediaBox().getWidth(),
                (page.getMediaBox().getWidth() * xImage.getHeight()) / xImage.getWidth(),
                true);

        page.getContents().add(new GSave());

        Matrix matrix = new Matrix(
                rectangle.getURX() - rectangle.getLLX(),
                0,
                0,
                rectangle.getURY() - rectangle.getLLY(),
                rectangle.getLLX(),
                rectangle.getLLX() + (page.getMediaBox().getHeight() - rectangle.getHeight()) / 2);
        page.getContents().add(new ConcatenateMatrix(matrix));
        page.getContents().add(new Do(imageId));
        page.getContents().add(new GRestore());

        document.save(outputFile.toString());
    }
}
```

## أضف صورة وحدد نصًا بديلًا

استخدم هذا المثال عندما ينبغي أن تتضمن الصورة بيانات ميتا للوصول لقراء الشاشة.

1. إنشاء ملف PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف الصورة إلى الصفحة.
1. احصل على العنصر المُدرَج [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/) من موارد الصفحة.
1. قم بتعيين النص البديل واحفظ ملف PDF.

```java
public static void addImageSetAlternativeTextForImage(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.setPageSize(842, 595);

        page.addImage(imageFile.toString(), new Rectangle(0, 0, 842, 595, true));

        XImage xImage = page.getResources().getImages().get_Item(1);
        boolean result = xImage.trySetAlternativeText("Alternative text for image", page);
        if (result) {
            System.out.println("Text has been added successfuly");
        }
        document.save(outputFile.toString());
    }
}
```

## أضف صورة باستخدام ضغط Flate

استخدم هذا المثال عندما تريد تضمين بيانات الصورة باستخدام ضغط Flate.

1. إنشاء ملف PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وفتح تدفق الصورة.
1. أضف الصورة إلى موارد الصفحة باستخدام `ImageFilterType.Flate`.
1. ارسم الصورة عبر عمليات الصفحة واحفظ النتيجة.

```java
public static void addImageToPdfWithFlateCompression(Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document();
         InputStream imageStream = Files.newInputStream(imageFile)) {
        Page page = document.getPages().add();
        XImageCollection resourcesImages = page.getResources().getImages();
        String imageId = resourcesImages.add(imageStream, ImageFilterType.Flate);

        page.getContents().add(new GSave());

        Rectangle rectangle = new Rectangle(0, 0, 600, 600, true);
        Matrix matrix = new Matrix(
                rectangle.getURX() - rectangle.getLLX(),
                0,
                0,
                rectangle.getURY() - rectangle.getLLY(),
                rectangle.getLLX(),
                rectangle.getLLY());

        page.getContents().add(new ConcatenateMatrix(matrix));
        page.getContents().add(new Do(imageId));
        page.getContents().add(new GRestore());

        document.save(outputFile.toString());
    }
}
```
