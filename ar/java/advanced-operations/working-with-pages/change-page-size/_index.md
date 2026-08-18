---
title: تغيير حجم صفحة PDF في جافا
linktitle: تغيير حجم الصفحة
type: docs
weight: 40
url: /java/change-page-size/
description: تعرف على كيفية قراءة أبعاد صفحة PDF وتغييرها في Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قراءة وتحديث أبعاد ومربعات الصفحة باستخدام Java
Abstract: توضح هذه المقالة كيفية قراءة أبعاد صفحة PDF وتعديلها باستخدام Aspose.PDF لـ Java. ويغطي الحصول على حجم الصفحة، وقياس حجم الصفحة مع تطبيق التدوير، وتحديث الصفحة الأولى إلى حجم جديد أثناء طباعة أبعاد الصندوق قبل التغيير وبعده.
---
يمكن لـ Aspose.PDF لـ Java الإبلاغ عن أبعاد الصفحة وتحديثها.

## تغيير حجم الصفحة

استخدم هذا المثال عندما تحتاج إلى تغيير حجم صفحة موجودة وفحص مربعات الصفحة قبل التغيير وبعده.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. احصل على الهدف [الصفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) واطبع قيم المربع الحالية الخاصة به.
1. اضبط حجم الصفحة الجديد واحفظ المستند.

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

## الحصول على حجم الصفحة

استخدم هذا المثال عندما تحتاج إلى قراءة الأبعاد المرئية للصفحة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. احصل على مستطيل الصفحة مع تمكين معالجة التدوير.
1. إخراج عرض الصفحة وارتفاعها.

```java
public static void getPageSize(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Rectangle rectangle = document.getPages().get_Item(1).getPageRect(true);
        System.out.println(rectangle.getWidth() + " : " + rectangle.getHeight());
    }
}
```

## احصل على حجم الصفحة مع تطبيق التدوير

استخدم هذا المثال عندما تحتاج إلى مقارنة أبعاد الصفحة قبل وبعد حساب التدوير.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بتدوير الهدف [الصفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. اقرأ مستطيل الصفحة مع وبدون معالجة التدوير وقم بإخراج القيمتين.

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
