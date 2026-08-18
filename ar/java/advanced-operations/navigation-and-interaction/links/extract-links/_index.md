---
title: استخراج روابط PDF في جافا
linktitle: استخراج الروابط
type: docs
weight: 30
url: /java/extract-links/
description: تعرف على كيفية استخراج التعليقات التوضيحية للارتباطات والارتباطات التشعبية من مستندات PDF في Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم باستخراج التعليقات التوضيحية للارتباط وأهداف URI من ملفات PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية استخراج التعليقات التوضيحية للارتباط من مستندات PDF باستخدام Aspose.PDF لـ Java. فهو يوضح كيفية تعداد التعليقات التوضيحية للارتباط على الصفحة، وقراءة فهرس الصفحة والمستطيل، واستخراج أهداف URI من مثيلات GoToURIAction.
---
يمكنك فحص روابط PDF من خلال تكرار التعليقات التوضيحية للصفحة وتصفية `AnnotationType.Link`.

## استخراج التعليقات التوضيحية الارتباط

استخدم هذا المثال عندما تحتاج إلى الموقع ومعلومات الصفحة لتعليقات الارتباط التوضيحية على الصفحة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بالتكرار من خلال التعليقات التوضيحية للصفحة وقم بتصفية التعليقات التوضيحية للارتباط.
1. اقرأ فهرس الصفحة والمستطيل لكل رابط مطابق.

```java
public static void extractLinkAnnotation(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link && annotation instanceof LinkAnnotation) {
                LinkAnnotation linkAnnotation = (LinkAnnotation) annotation;
                System.out.println("Page: " + linkAnnotation.getPageIndex()
                        + ", location: " + linkAnnotation.getRect());
            }
        }
    }
}
```

## استخراج وجهات الارتباط التشعبي

استخدم هذا المثال عندما تحتاج إلى قراءة عناوين URI المستهدفة من التعليقات التوضيحية لرابط الويب.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. ابحث عن كائنات [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) التي يكون الإجراء الخاص بها هو [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/).
1. قم بطباعة فهرس الصفحة وهدف URI لكل ارتباط تشعبي.

```java
public static void extractHyperlinks(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link && annotation instanceof LinkAnnotation) {
                LinkAnnotation linkAnnotation = (LinkAnnotation) annotation;
                if (linkAnnotation.getAction() instanceof GoToURIAction) {
                    GoToURIAction action = (GoToURIAction) linkAnnotation.getAction();
                    System.out.println("Page " + linkAnnotation.getPageIndex() + ", URI:" + action.getURI());
                }
            }
        }
    }
}
```
