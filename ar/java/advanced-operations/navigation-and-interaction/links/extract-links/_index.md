---
title: استخراج روابط PDF في Java
linktitle: استخراج الروابط
type: docs
weight: 30
url: /ar/java/extract-links/
description: تعرّف على كيفية استخراج تعليقات الروابط والروابط التشعبية من مستندات PDF باستخدام Java.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استخراج تعليقات الروابط ووجهات URI من ملفات PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية استخراج تعليقات الروابط من مستندات PDF باستخدام Aspose.PDF for Java. تُظهر كيفية تعداد تعليقات الروابط على صفحة، وقراءة فهرس الصفحة ومستطيلها، واستخراج هدف URI من مثيلات GoToURIAction.
---
يمكنك فحص روابط PDF عن طريق التكرار عبر ملاحظات الصفحة وتصفية `AnnotationType.Link`.

## استخراج تعليقات الروابط

استخدم هذا المثال عندما تحتاج إلى معلومات الموقع والصفحة لتعليقات الروابط على صفحة.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. استعرض تعليقات الصفحة وقم بفلترة تعليقات الروابط.
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

## استخراج وجهات الروابط التشعبية

استخدم هذا المثال عندما تحتاج إلى قراءة عناوين URI الهدف من تعليقات الروابط التشعبية على الويب.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. ابحث الكائنات [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) التي يكون إجراءها هو [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/).
1. اطبع فهرس الصفحة والهدف URI لكل ارتباط تشعبي.

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
