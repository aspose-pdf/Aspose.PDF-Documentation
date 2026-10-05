---
title: تحديث روابط PDF في Java
linktitle: تحديث الروابط
type: docs
weight: 20
url: /ar/java/update-links/
description: تعلم كيفية تحديث مظهر روابط PDF والوجهات في Java.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تحديث مظهر تعليقات الروابط والوجهات الويب في ملفات PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية تحديث تعليقات الارتباط الموجودة باستخدام Aspose.PDF for Java. توضح الأمثلة تغيير لون النص المغطى برابط، وتحديث لون تعليق الارتباط، واستبدال عنوان URI الهدف للروابط على الويب.
---
يمكن تعديل الروابط الموجودة عن طريق العثور على تعليق الارتباط في الصفحة وتحديث إما مظهره أو إجراءه.

## تحديث لون النص المرتبط

استخدم هذا المثال عندما يجب إعادة تلوين منطقة النص التي يغطيها تعليق الارتباط.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. ابحث عن تعليقات الروابط وأنشئ مستطيل بحث نصي من كل منطقة تعليقة.
1. أعد تلوين مقاطع النص المتطابقة واحفظ المستند.

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

استخدم هذا المثال عندما يجب تغيير اللون المرئي لتعليقات الروابط الموجودة.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. مرّ على تعليقات الصفحة وتصفية لـ الكائنات [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/).
1. حدّث لون التعليق التوضيحي للارتباط واحفظ المستند.

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

## تحديث وجهة رابط الويب

استخدم هذا المثال عندما ينبغي لرابط ويب موجود أن يشير إلى URI جديد.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. ابحث عن تعليقات الارتباط التي يكون الإجراء الخاص بها [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/).
1. استبدل عنوان URI واحفظ المستند المحدث.

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
