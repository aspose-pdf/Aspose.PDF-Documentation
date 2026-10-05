---
title: إنشاء روابط PDF في Java
linktitle: إنشاء روابط
type: docs
weight: 10
url: /ar/java/create-links/
description: تعرف على كيفية إنشاء روابط PDF داخلية وخارجية وعن بُعد في Java.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إنشاء تعليقات توضيحية للروابط في ملفات PDF باستخدام Java
Abstract: تُظهر هذه المقالة كيفية إنشاء تعليقات ارتباطية باستخدام Aspose.PDF for Java. وتغطي إجراءات الإطلاق، والتنقل إلى مستند بعيد، والتنقل داخل المستند إلى صفحات، وروابط الويب القائمة على URI عن طريق إرفاق الإجراءات إلى كائنات LinkAnnotation.
---
Aspose.PDF for Java يستخدم `LinkAnnotation` مع كائن إجراء لتحديد سلوك الرابط.

## .إنشاء ارتباط بإجراء إطلاق

استخدم هذا المثال عندما يجب على تعليق ارتباط إطلاق ملف خارجي أو هدف.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وحدد الصفحة المستهدفة.
1. أنشئ كائنًا من الفئة [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) وتهيئة حدوده ولونه.
1. عيّن [LaunchAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/launchaction/) واحفظ المستند.

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

## إنشاء ارتباط ذهاب إلى عن بُعد

استخدم هذا المثال عندما يجب أن يفتح الارتباط صفحةً في مستند PDF آخر.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ كائنًا من الفئة [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) على الصفحة الهدف.
1. عيّن [GoToRemoteAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoremoteaction/) واحفظ ملف الإخراج.

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

## إنشاء ارتباط انتقالي داخلي

استخدم هذا المثال عندما يجب أن ينتقل الارتباط إلى صفحة أخرى داخل نفس مستند PDF.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ كائنًا من الفئة [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) واضبط مظهره.
1. عيّن [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) إلى صفحة الوجهة واحفظ المستند.

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

## إنشاء رابط URI

استخدم هذا المثال عندما يجب أن يفتح الرابط مورد ويب من خلال إجراء URI.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ كائنًا من الفئة [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) في الصفحة.
1. عيّن [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/) واحفظ ملف الإخراج.

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
