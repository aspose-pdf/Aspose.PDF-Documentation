---
title: إنشاء روابط PDF في جافا
linktitle: إنشاء الروابط
type: docs
weight: 10
url: /java/create-links/
description: تعرف على كيفية إنشاء روابط PDF داخلية وخارجية وعن بعد في Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إنشاء تعليقات توضيحية للارتباط في ملفات PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية إنشاء تعليقات توضيحية للارتباط باستخدام Aspose.PDF لـ Java. ويغطي إجراءات التشغيل، والتنقل عن بعد في المستندات، والتنقل في الصفحة داخل المستند، وروابط الويب المستندة إلى URI عن طريق ربط الإجراءات بكائنات LinkAnnotation.
---
يستخدم Aspose.PDF لـ Java `LinkAnnotation` مع كائن الإجراء لتحديد سلوك الارتباط.

## قم بإنشاء رابط إجراء الإطلاق

استخدم هذا المثال عندما يجب أن يقوم التعليق التوضيحي للارتباط بتشغيل ملف أو هدف خارجي.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وحدد الصفحة المستهدفة.
1. أنشئ [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) وقم بتكوين حدوده ولونه.
1. قم بتعيين [LaunchAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/launchaction/) واحفظ المستند.

```java
public static void createLinkAnnotationLaunchAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        Border border = new Border(link);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        link.setBorder(border);
        link.setColor(Color.getGreen());
        link.setAction(new LaunchAction(document, inputFile.toString()));
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```

## قم بإنشاء رابط الانتقال عن بعد

استخدم هذا المثال عندما يجب أن يفتح الرابط صفحة في مستند PDF آخر.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) على الصفحة المستهدفة.
1. قم بتعيين [GoToRemoteAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoremoteaction/) واحفظ ملف الإخراج.

```java
public static void createLinkAnnotationGoToRemoteAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        link.setColor(Color.getGreen());
        link.setAction(new GoToRemoteAction(inputFile.toString(), 1));
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```

## قم بإنشاء رابط انتقال داخلي

استخدم هذا المثال عندما ينتقل الرابط إلى صفحة أخرى داخل مستند PDF نفسه.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) وقم بتكوين مظهره.
1. قم بتعيين [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) إلى الصفحة الوجهة واحفظ المستند.

```java
public static void createLinkAnnotationGoToAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        Border border = new Border(link);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        link.setBorder(border);
        link.setColor(Color.getGreen());
        if (document.getPages().size() >= 4) {
            link.setAction(new GoToAction(document.getPages().get_Item(4)));
        } else {
            link.setAction(new GoToAction(document.getPages().get_Item(document.getPages().size())));
        }
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```

## قم بإنشاء رابط URI

استخدم هذا المثال عندما يجب أن يفتح الارتباط مورد ويب من خلال إجراء URI.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) على الصفحة.
1. قم بتعيين [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/) واحفظ ملف الإخراج.

```java
public static void createLinkAnnotationGoToUriAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        link.setColor(Color.getGreen());
        link.setAction(new GoToURIAction("https://docs.aspose.com/pdf/python"));
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```
