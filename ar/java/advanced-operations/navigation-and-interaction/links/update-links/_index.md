---
title: تحديث روابط PDF في جافا
linktitle: تحديث الروابط
type: docs
weight: 20
url: /java/update-links/
description: تعرف على كيفية تحديث مظهر رابط PDF ووجهاته في Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بتحديث مظهر التعليقات التوضيحية للارتباط ووجهات الويب في ملفات PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية تحديث التعليقات التوضيحية للارتباط الموجود باستخدام Aspose.PDF لـ Java. توضح الأمثلة تغيير لون النص الذي يغطيه الرابط، وتحديث لون التعليق التوضيحي للارتباط، واستبدال عنوان URI المستهدف لروابط الويب.
---
يمكن تحرير الروابط الموجودة من خلال العثور على التعليق التوضيحي للرابط على الصفحة وتحديث مظهره أو الإجراء الخاص به.

## تحديث لون النص المرتبط

استخدم هذا المثال عندما يجب إعادة تلوين منطقة النص التي يغطيها التعليق التوضيحي للارتباط.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. ابحث عن التعليقات التوضيحية للارتباط وقم بإنشاء مستطيل بحث نصي من كل منطقة من مناطق التعليقات التوضيحية.
1. أعد تلوين أجزاء النص المتطابقة واحفظ المستند.

```java
public static void linkAnnotationUpdateTextColor(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link) {
                TextFragmentAbsorber absorber = new TextFragmentAbsorber();
                Rectangle rect = annotation.getRect();
                rect.setLLX(rect.getLLX() - 2);
                rect.setLLY(rect.getLLY() - 2);
                rect.setURX(rect.getURX() + 2);
                rect.setURY(rect.getURY() + 2);
                absorber.setTextSearchOptions(new TextSearchOptions(rect));
                absorber.visit(document.getPages().get_Item(1));
                for (TextFragment textFragment : absorber.getTextFragments()) {
                    textFragment.getTextState().setForegroundColor(Color.getRed());
                }
            }
        }

        document.save(outputFile.toString());
    }
}
```

## تحديث لون حدود الرابط

استخدم هذا المثال عندما يجب تغيير اللون المرئي للتعليقات التوضيحية للارتباط الموجود.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بالتكرار خلال التعليقات التوضيحية للصفحة وقم بالتصفية بحثًا عن كائنات [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/).
1. قم بتحديث لون التعليق التوضيحي للارتباط واحفظ المستند.

```java
public static void linkAnnotationUpdateBorder(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link && annotation instanceof LinkAnnotation) {
                LinkAnnotation linkAnnotation = (LinkAnnotation) annotation;
                linkAnnotation.setColor(Color.getRed());
            }
        }

        document.save(outputFile.toString());
    }
}
```

## قم بتحديث وجهة رابط الويب

استخدم هذا المثال عندما يشير رابط الويب الموجود إلى عنوان URI جديد.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. ابحث عن التعليقات التوضيحية للارتباط الذي يكون الإجراء الخاص به هو [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/).
1. استبدل URI واحفظ المستند المحدث.

```java
public static void linkAnnotationUpdateWebDestination(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link && annotation instanceof LinkAnnotation) {
                LinkAnnotation linkAnnotation = (LinkAnnotation) annotation;
                if (linkAnnotation.getAction() instanceof GoToURIAction) {
                    GoToURIAction action = (GoToURIAction) linkAnnotation.getAction();
                    action.setURI("https://www.aspose.com");
                }
            }
        }
        document.save(outputFile.toString());
    }
}
```
