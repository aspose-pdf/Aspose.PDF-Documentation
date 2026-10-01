---
title: التعليقات التوضيحية للعلامات باستخدام Java
linktitle: التعليقات التوضيحية للعلامات
type: docs
weight: 30
url: /ar/java/markup-annotations/
description: تعرّف على كيفية إضافة وفحص وحذف تعليقات توضيحية للتمييز، التسطير، الخط المتعرج، والخط المشطوب في مستندات PDF باستخدام Aspose.PDF for Java.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: اعمل مع تعليقات التنسيق في ملفات PDF باستخدام Java.
Abstract: توضح هذه المقالة كيفية إنشاء وفحص وإزالة تعليقات توضيحية للنص في مستندات PDF باستخدام Aspose.PDF for Java. تغطي المقالة تعليقات تمييز، وتسطير، وتمويج، وشطب بناءً على أمثلة Java الموجودة في المستودع.
---
تركز تدفقات عمل تعليقات الترميز في هذا القسم على التعليقات بنمط الملاحظة، وعلامات المؤشر، وسيناريوهات الاستبدال‑المراجعة المجمعة.

## إضافة ملاحظة نصية

استخدم هذا المثال عندما تحتاج إلى وضع تعليقة نصية بنمط الملاحظة اللاصقة مع بيانات تعريف منبثقة على صفحة.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. إنشاء [TextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/textannotation/) وقم بتكوين عنوانه ومحتوياته وأيقونته والنافذة المنبثقة.
1. أضف التعليق إلى الصفحة واحفظ المستند.

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

## الحصول على تعليقات النص

يقوم هذا المثال بفحص الصفحة ويطبع المستطيل الخاص بكل تعليق نصي.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. التكرار عبر التعليقات التوضيحية في الصفحة.
1. تصفية التعليقات التوضيحية حسب [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Text` وطباعة مستطيلاتهم.

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

## حذف تعليقات النص

استخدم هذا النهج عندما يجب إزالة التعليقات النصية الموجودة من المستند.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. جمع التعليقات من النوع [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Text`.
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

## إضافة توضيح caret

استخدم هذا المثال عندما تحتاج إلى وضع علامة على النص المُدرج باستخدام تعليق مراجعة على نمط ^.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. إنشاء [CaretAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/caretannotation/) وإعداد النافذة المنبثقة ومظهرها.
1. أضف التعليق إلى الصفحة واحفظ المستند.

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

## احصل على تعليقات المؤشر

هذا المثال يقرأ تعليقات caret التوضيحية الموجودة ويطبع مواقعها.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. التكرار عبر تعليقات الصفحة.
1. تصفية التعليقات التوضيحية حسب [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Caret` وطباعة مستطيلاتهم.

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

## حذف تعليقات المؤشر

استخدم هذا النهج عندما يجب إزالة تعليقات المؤشر من الصفحة.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اجمع التعليقات التي نوعها هو [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Caret`.
1. احذف التعليقات التي تم جمعها واحفظ مستند الإخراج.

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

## إضافة تعليقات استبدال مُجمَّعة

يجمع هذا المثال بين تعليقة caret وتعليقة strikeout لتمثيل تعليق مراجعة بنمط الاستبدال.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. إنشاء التعليق caret والمرتبط [StrikeOutAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/strikeoutannotation/).
1. ربط التعليقات التوضيحية عبر `setInReplyTo` و `setReplyType`, ثم احفظ المستند.

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

## احصل على التعليقات التوضيحية المستبدلة المجمعة

هذا المثال يكتشف التعليقات التوضيحية المشطوبة التي تشارك في سير عمل الاستبدال المجمّع.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. التكرار عبر تعليقات الصفحة واختيار تعليقات الشطب.
1. تحقق من علاقة الرد واطبع مستطيل التعليقات المتطابقة.

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

## حذف التعليقات التوضيحية المُجمَّعة المستبدلة

استخدم هذا النهج عندما يجب إزالة تعليقات الخط المتوسط للمراجعة والاستبدال من الصفحة.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اجمع تعليقات الشطب التي تمثل ترميز الاستبدال.
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

## مواضيع التعليقات التوضيحية ذات الصلة

- [ملاحظات نصية](/pdf/ar/java/text-based-annotations/)
- [التعليقات التفاعلية](/pdf/ar/java/interactive-annotations/)
- [تعليقات الشكل](/pdf/ar/java/shape-annotations/)
- [تعليقات وسائط](/pdf/ar/java/media-annotations/)
- [ملاحظات الأمان](/pdf/ar/java/security-annotations/)
- [تعليقات العلامة المائية](/pdf/ar/java/watermark-annotations/)
