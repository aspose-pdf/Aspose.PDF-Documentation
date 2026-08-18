---
title: التعليقات التوضيحية الترميزية باستخدام Java
linktitle: التعليقات التوضيحية الترميزية
type: docs
weight: 30
url: /java/markup-annotations/
description: تعرف على كيفية إضافة التعليقات التوضيحية المميزة والتسطير والمتعرجة والشطب وفحصها وحذفها في مستندات PDF باستخدام Aspose.PDF لـ Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: العمل مع التعليقات التوضيحية الترميزية في ملفات PDF باستخدام Java.
Abstract: تشرح هذه المقالة كيفية إنشاء التعليقات التوضيحية للعلامات النصية وفحصها وإزالتها في مستندات PDF باستخدام Aspose.PDF لـ Java. ويغطي التعليقات التوضيحية المميزة والتسطير والمتعرج والشطب بناءً على أمثلة Java الخاصة بالمستودع.
---
تركز عمليات سير عمل التعليقات التوضيحية الترميزية في هذا القسم على تعليقات نمط الملاحظة وعلامات الإقحام وسيناريوهات مراجعة الاستبدال المجمعة.

## إضافة تعليق توضيحي للنص

استخدم هذا المثال عندما تحتاج إلى وضع تعليق توضيحي نصي على نمط الملاحظة اللاصقة مع بيانات تعريف منبثقة على الصفحة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [TextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/textannotation/) وقم بتكوين عنوانه ومحتوياته وأيقونته والقائمة المنبثقة.
1. أضف التعليق التوضيحي إلى الصفحة واحفظ المستند.

```java
public static void textAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextAnnotation textAnnotation = new TextAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299.988, 613.664, 428.708, 680.769, true));
        textAnnotation.setTitle("Aspose User");
        textAnnotation.setSubject("Sticky Note");
        textAnnotation.setContents("This is a text annotation added by Aspose.PDF for Java");
        textAnnotation.setFlags(AnnotationFlags.Print);
        textAnnotation.setColor(Color.getBlue());
        textAnnotation.setIcon(TextIcon.Help);

        PopupAnnotation popup = new PopupAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(428.708, 613.664, 528.708, 713.664, true));
        popup.setOpen(true);
        textAnnotation.setPopup(popup);

        document.getPages().get_Item(1).getAnnotations().add(textAnnotation, false);
        document.save(outputFile.toString());
    }
}
```

## الحصول على التعليقات التوضيحية النصية

يقوم هذا المثال بمسح الصفحة وطباعة مستطيل كل تعليق توضيحي للنص.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. كرر من خلال التعليقات التوضيحية الموجودة على الصفحة.
1. قم بتصفية التعليقات التوضيحية حسب [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Text` واطبع مستطيلاتها.

```java
public static void textAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Text) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

## حذف التعليقات التوضيحية النصية

استخدم هذا الأسلوب عندما يجب إزالة التعليقات التوضيحية النصية الموجودة من المستند.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. جمع التعليقات التوضيحية من النوع [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Text`.
1. احذف التعليقات التوضيحية المجمعة واحفظ ملف الإخراج.

```java
public static void textAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Text) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## إضافة تعليق توضيحي لعلامة الإقحام

استخدم هذا المثال عندما تحتاج إلى وضع علامة على النص المدرج باستخدام تعليق توضيحي للمراجعة على نمط علامة الإقحام.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [CaretAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/caretannotation/) وقم بتكوين النافذة المنبثقة والمظهر الخاص بها.
1. أضف التعليق التوضيحي إلى الصفحة واحفظ المستند.

```java
public static void caretAnnotationsAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        CaretAnnotation caretAnnotation = new CaretAnnotation(
                page,
                new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        caretAnnotation.setTitle("Aspose User");
        caretAnnotation.setSubject("Inserted text 1");
        caretAnnotation.setFlags(AnnotationFlags.Print);
        caretAnnotation.setColor(Color.getBlue());
        caretAnnotation.setPopup(new PopupAnnotation(
                page,
                new Rectangle(310, 713, 410, 730, true)));
        page.getAnnotations().add(caretAnnotation);

        document.save(outputFile.toString());
    }
}
```

## الحصول على التعليقات التوضيحية لعلامة الإقحام

يقرأ هذا المثال التعليقات التوضيحية لعلامة الإقحام الموجودة ويطبع مواقعها.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. التكرار من خلال التعليقات التوضيحية للصفحة.
1. قم بتصفية التعليقات التوضيحية حسب [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Caret` واطبع مستطيلاتها.

```java
public static void caretAnnotationsGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        for (Annotation annot : page.getAnnotations()) {
            if (annot.getAnnotationType() == AnnotationType.Caret) {
                System.out.println(annot.getRect());
            }
        }
    }
}
```

## حذف التعليقات التوضيحية لعلامة الإقحام

استخدم هذا الأسلوب عندما يجب إزالة التعليقات التوضيحية لعلامة الإقحام من الصفحة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. جمع التعليقات التوضيحية التي يكون نوعها [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Caret`.
1. احذف التعليقات التوضيحية المجمعة واحفظ مستند الإخراج.

```java
public static void caretAnnotationsDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        List<Annotation> caretAnnotations = new ArrayList<>();
        for (Annotation annot : page.getAnnotations()) {
            if (annot.getAnnotationType() == AnnotationType.Caret) {
                caretAnnotations.add(annot);
            }
        }
        for (Annotation annot : caretAnnotations) {
            page.getAnnotations().delete(annot);
        }
        document.save(outputFile.toString());
    }
}
```

## إضافة التعليقات التوضيحية البديلة المجمعة

يجمع هذا المثال بين تعليق توضيحي لعلامة الإقحام وتعليق توضيحي مشطب لتمثيل تعليق مراجعة نمط الاستبدال.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء تعليق توضيحي لعلامة الإقحام و[StrikeOutAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/strikeoutannotation/) ذي الصلة.
1. اربط التعليقات التوضيحية من خلال `setInReplyTo` و`setReplyType`، ثم احفظ المستند.

```java
public static void replaceAnnotationsAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        CaretAnnotation caretAnnotation = new CaretAnnotation(
                page,
                new Rectangle(361.246, 727.908, 370.081, 735.107, true));
        caretAnnotation.setFlags(AnnotationFlags.Print);
        caretAnnotation.setSubject("Inserted text 2");
        caretAnnotation.setTitle("Aspose User");
        caretAnnotation.setColor(Color.getBlue());
        caretAnnotation.setPopup(new PopupAnnotation(
                page,
                new Rectangle(310, 713, 410, 730, true)));

        StrikeOutAnnotation strikeoutAnnotation = new StrikeOutAnnotation(
                page,
                new Rectangle(318.407, 727.826, 368.916, 740.098, true));
        strikeoutAnnotation.setColor(Color.getBlue());
        strikeoutAnnotation.setQuadPoints(new Point[]{
                new Point(321.66, 739.416),
                new Point(365.664, 739.416),
                new Point(321.66, 728.508),
                new Point(365.664, 728.508)
        });
        strikeoutAnnotation.setSubject("Cross-out");
        strikeoutAnnotation.setInReplyTo(caretAnnotation);
        strikeoutAnnotation.setReplyType(ReplyType.Group);

        page.getAnnotations().add(caretAnnotation);
        page.getAnnotations().add(strikeoutAnnotation);

        document.save(outputFile.toString());
    }
}
```

## الحصول على استبدال التعليقات التوضيحية المجمعة

يكشف هذا المثال عن التعليقات التوضيحية المشطبة التي تشارك في سير عمل الاستبدال المجمع.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بالتكرار خلال التعليقات التوضيحية للصفحة وحدد التعليقات التوضيحية المشطبة.
1. تحقق من علاقة الرد واطبع مستطيل التعليقات التوضيحية المطابقة.

```java
public static void replaceAnnotationsGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        for (Annotation annot : page.getAnnotations()) {
            if (annot.getAnnotationType() == AnnotationType.StrikeOut) {
                StrikeOutAnnotation sa = (StrikeOutAnnotation) annot;
                if (sa.getInReplyTo() != null && sa.getReplyType() == ReplyType.Group) {
                    System.out.println("Replace annotation rect: " + sa.getRect());
                }
            }
        }
    }
}
```

## حذف التعليقات التوضيحية واستبدالها المجمعة

استخدم هذا الأسلوب عندما يجب إزالة التعليقات التوضيحية لخطة مراجعة الاستبدال من الصفحة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اجمع التعليقات التوضيحية التي تمثل علامة الاستبدال.
1. احذف التعليقات التوضيحية المجمعة واحفظ المستند المحدث.

```java
public static void replaceAnnotationsDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        List<StrikeOutAnnotation> replaceAnnotations = new ArrayList<>();
        for (Annotation annot : page.getAnnotations()) {
            if (annot.getAnnotationType() == AnnotationType.StrikeOut) {
                replaceAnnotations.add((StrikeOutAnnotation) annot);
            }
        }
        for (StrikeOutAnnotation annot : replaceAnnotations) {
            page.getAnnotations().delete(annot);
        }
        document.save(outputFile.toString());
    }
}
```

## مواضيع ذات صلة بالتعليقات

- [التعليقات التوضيحية النصية](/pdf/java/text-based-annotations/)
- [التعليقات التوضيحية التفاعلية](/pdf/java/interactive-annotations/)
- [التعليقات التوضيحية للشكل](/pdf/java/shape-annotations/)
- [تعليقات الوسائط](/pdf/java/media-annotations/)
- [التعليقات التوضيحية الأمنية](/pdf/java/security-annotations/)
- [التعليقات التوضيحية للعلامة المائية](/pdf/java/watermark-annotations/)
