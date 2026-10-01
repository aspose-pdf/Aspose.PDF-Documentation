---
title: تغيير حجم صفحة PDF في Java
linktitle: تغيير حجم الصفحة
type: docs
weight: 40
url: /ar/java/change-page-size/
description: تعرّف على كيفية قراءة وتغيير أبعاد صفحات PDF في Java.
lastmod: "2026-10-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قراءة وتحديث أبعاد الصفحات والصناديق باستخدام Java
Abstract: توضح هذه المقالة كيفية قراءة وتعديل أبعاد صفحات PDF باستخدام Aspose.PDF for Java. تغطي الحصول على حجم الصفحة، قياس حجم الصفحة مع تطبيق الدوران، وتحديث الصفحة الأولى إلى حجم جديد مع طباعة أبعاد الصناديق قبل وبعد التغيير.
---
يمكن لـ Aspose.PDF for Java كل من الإبلاغ عن أبعاد الصفحات وتحديثها.

## تغيير حجم الصفحة

استخدم هذا المثال عندما تحتاج إلى تغيير حجم صفحة موجودة وفحص صناديق الصفحة قبل وبعد التغيير.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. احصل على الهدف [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) وطباعة قيم الصندوق الحالية.
1. حدد حجم الصفحة الجديد واحفظ المستند.

```java
public static void setPageSize(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        printBoxes("Before set", page);
        page.setPageSize(597.6, 842.4);
        printBoxes("After set", page);
        document.save(outputFile.toString());
    }
}
```

## احصل على حجم الصفحة

استخدم هذا المثال عندما تحتاج إلى قراءة الأبعاد الظاهرة للصفحة.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. احصل على مستطيل الصفحة مع تمكين معالجة الدوران.
1. اطبع عرض الصفحة وارتفاعها.

```java
public static void getPageSize(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Rectangle rectangle = document.getPages().get_Item(1).getPageRect(true);
        System.out.println(rectangle.getWidth() + " : " + rectangle.getHeight());
    }
}
```

## احصل على حجم الصفحة مع تطبيق الدوران

استخدم هذا المثال عندما تحتاج إلى مقارنة أبعاد الصفحة قبل وبعد مراعاة الدوران

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. دوِّر الهدف [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. قراءة مستطيل الصفحة مع معالجة الدوران وبدونها وإخراج القيمتين.

```java
public static void getPageSizeRotation(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        page.setRotate(Rotation.on90);
        Rectangle rectangle = page.getPageRect(false);
        System.out.println(rectangle.getWidth() + " : " + rectangle.getHeight());
        rectangle = page.getPageRect(true);
        System.out.println(rectangle.getWidth() + " : " + rectangle.getHeight());
    }
}
```
