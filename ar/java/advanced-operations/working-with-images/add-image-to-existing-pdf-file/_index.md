---
title: إضافة صورة إلى PDF باستخدام جافا
linktitle: إضافة صورة
type: docs
weight: 10
url: /java/add-image-to-existing-pdf-file/
description: تعرف على كيفية إضافة الصور إلى ملفات PDF الموجودة في Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: أضف صورًا إلى ملفات PDF الموجودة باستخدام Java
Abstract: توضح هذه المقالة كيفية إضافة صور إلى مستندات PDF باستخدام Aspose.PDF لـ Java. ويغطي وضع صورة في إحداثيات ثابتة، وإضافة الصور من خلال عوامل تشغيل الصفحة ذات المستوى المنخفض، وتعيين نص بديل لإمكانية الوصول، وتضمين بيانات الصورة باستخدام ضغط Flate.
---
يدعم Aspose.PDF for Java كلاً من وضع الصور عالي المستوى والرسم المستند إلى عامل التشغيل منخفض المستوى.

## أضف صورة بإحداثيات الصفحة

استخدم هذا المثال عندما تحتاج إلى وضع صورة في موضع ثابت على صفحة PDF.

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف صفحة.
1. اتصل `page.addImage()` بمسار الصورة المصدر والمستطيل المستهدف.
1. احفظ ملف PDF الذي تم إنشاؤه.

```java
public static void addImage(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.addImage(imageFile.toString(), new Rectangle(20, 730, 120, 830, true));
        document.save(outputFile.toString());
    }
}
```

## أضف صورة باستخدام عوامل تشغيل الصفحة

استخدم هذا المثال عندما تحتاج إلى تحكم منخفض المستوى في موضع الصورة وقياسها من خلال عوامل تشغيل الصفحة.

1. قم بإنشاء ملف PDF [مستند] جديد (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وافتح تدفق الصور المصدر.
1. أضف الصورة إلى موارد الصفحة واحسب المستطيل المستهدف.
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

## أضف صورة وقم بتعيين نص بديل

استخدم هذا المثال عندما يجب أن تتضمن الصورة بيانات تعريف إمكانية الوصول لقارئات الشاشة.

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف الصورة إلى الصفحة.
1. احصل على [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/) المدرج من موارد الصفحة.
1. قم بتعيين النص البديل وحفظ ملف PDF.

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

## إضافة صورة مع ضغط Flate

استخدم هذا المثال عندما تريد تضمين بيانات الصورة باستخدام ضغط Flate.

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وافتح دفق الصور.
1. أضف الصورة إلى موارد الصفحة باستخدام `ImageFilterType.Flate`.
1. ارسم الصورة من خلال عوامل تشغيل الصفحة واحفظ النتيجة.

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
