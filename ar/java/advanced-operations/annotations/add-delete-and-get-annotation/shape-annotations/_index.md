---
title: التعليقات التوضيحية للشكل عبر Java
linktitle: التعليقات التوضيحية للأشكال
type: docs
weight: 20
url: /java/shape-annotations/
description: تعرف على كيفية إضافة التعليقات التوضيحية المربعة والدائرة والمضلعة والمتعددة الخطوط وفحصها وحذفها في مستندات PDF باستخدام Aspose.PDF لـ Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: العمل مع التعليقات التوضيحية الهندسية لملفات PDF في Java.
Abstract: تشرح هذه المقالة كيفية إنشاء التعليقات التوضيحية الهندسية وفحصها وإزالتها في مستندات PDF باستخدام Aspose.PDF لـ Java. وهو يغطي التعليقات التوضيحية المربعة والدائرة والمضلعة والمتعددة الخطوط مع تكوين اللون والعتامة والنوافذ المنبثقة والنقطة.
---
تغطي التعليقات التوضيحية للأشكال في هذا القسم أنواع التعليقات التوضيحية الهندسية مثل المربعات والدوائر والمضلعات والخطوط المتعددة والخطوط.

## أضف تعليقات توضيحية مربعة ودائرة ومضلعة ومتعددة الخطوط

استخدم هذه الأمثلة عندما تحتاج إلى وضع تعليقات توضيحية هندسية بألوان مخصصة أو عتامة أو بيانات منبثقة أو صفائف نقطية.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء التعليق التوضيحي للشكل المطلوب وقم بتكوين مستطيله ونقاطه وخصائصه المرئية.
1. أضف التعليق التوضيحي إلى الصفحة واحفظ المستند المحدث.

```java
public static void squareAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        SquareAnnotation squareAnnotation = new SquareAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(60, 600, 250, 450, true));
        squareAnnotation.setTitle("John Smith");
        squareAnnotation.setColor(Color.getBlue());
        squareAnnotation.setInteriorColor(Color.getBlueViolet());
        squareAnnotation.setOpacity(0.25);

        document.getPages().get_Item(1).getAnnotations().add(squareAnnotation);
        document.save(outputFile.toString());
    }
}
```

```java
public static void circleAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        CircleAnnotation circleAnnotation = new CircleAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(270, 160, 483, 383, true));
        circleAnnotation.setTitle("John Smith");
        circleAnnotation.setColor(Color.getRed());
        circleAnnotation.setInteriorColor(Color.getMistyRose());
        circleAnnotation.setOpacity(0.5);
        circleAnnotation.setPopup(new PopupAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(842, 316, 1021, 459, true)));

        document.getPages().get_Item(1).getAnnotations().add(circleAnnotation);
        document.save(outputFile.toString());
    }
}
```

```java
public static void polygonAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PolygonAnnotation polygonAnnotation = new PolygonAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(200, 300, 400, 400, true),
                new Point[]{
                        new Point(200, 300),
                        new Point(220, 300),
                        new Point(250, 330),
                        new Point(300, 304),
                        new Point(300, 400)
                });
        polygonAnnotation.setTitle("John Smith");
        polygonAnnotation.setColor(Color.getBlue());
        polygonAnnotation.setInteriorColor(Color.getBlueViolet());
        polygonAnnotation.setOpacity(0.25);

        document.getPages().get_Item(1).getAnnotations().add(polygonAnnotation);
        document.save(outputFile.toString());
    }
}
```

```java
public static void polylineAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PolylineAnnotation polylineAnnotation = new PolylineAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(270, 193, 571, 383, true),
                new Point[]{
                        new Point(545, 150),
                        new Point(545, 190),
                        new Point(667, 190),
                        new Point(667, 110),
                        new Point(626, 111)
                });
        polylineAnnotation.setTitle("John Smith");
        polylineAnnotation.setColor(Color.getRed());
        polylineAnnotation.setPopup(new PopupAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(842, 196, 1021, 338, true)));

        document.getPages().get_Item(1).getAnnotations().add(polylineAnnotation);
        document.save(outputFile.toString());
    }
}
```

## احصل على تعليقات توضيحية مربعة ودائرة ومضلعة ومتعددة الخطوط

تقوم هذه الأمثلة بفحص مجموعة التعليقات التوضيحية للصفحة وطباعة مستطيلات التعليقات التوضيحية الهندسية حسب النوع.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. التكرار من خلال التعليقات التوضيحية للصفحة.
1. قم بالتصفية حسب قيمة [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/) المطلوبة ثم قم بطباعة المستطيل.

```java
public static void squareAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Square) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

```java
public static void circleAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Circle) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

```java
public static void polygonAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Polygon) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

```java
public static void polylineAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.PolyLine) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

## حذف التعليقات التوضيحية المربعة والدائرة والمضلعة والمتعددة الخطوط

استخدم هذه الأمثلة عندما يجب إزالة التعليقات التوضيحية للأشكال من نوع معين من الصفحة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. جمع الشروح من النوع الهندسي المطلوب.
1. احذف التعليقات التوضيحية المجمعة واحفظ ملف الإخراج.

```java
public static void squareAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Square) {
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

```java
public static void circleAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Circle) {
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

```java
public static void polygonAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Polygon) {
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

```java
public static void polylineAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.PolyLine) {
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

## إضافة تعليق توضيحي للخط

ينشئ هذا المثال تعليقًا توضيحيًا سطريًا بنهايات الأسهم وتنسيق الحدود وملاحظة منبثقة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [LineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/lineannotation/) بنقاط البداية والنهاية.
1. قم بتكوين المظهر، وأضف النافذة المنبثقة، واحفظ المستند.

```java
public static void lineAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        LineAnnotation lineAnnotation = new LineAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(550, 93, 562, 439, true),
                new Point(556, 99),
                new Point(556, 443));
        lineAnnotation.setTitle("John Smith");
        lineAnnotation.setColor(Color.getRed());
        lineAnnotation.setStartingStyle(LineEnding.OpenArrow);
        lineAnnotation.setEndingStyle(LineEnding.OpenArrow);

        Border border = new Border(lineAnnotation);
        border.setWidth(3);
        lineAnnotation.setBorder(border);

        PopupAnnotation popup = new PopupAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(842, 124, 1021, 266, true));
        lineAnnotation.setPopup(popup);

        document.getPages().get_Item(1).getAnnotations().add(lineAnnotation);
        document.save(outputFile.toString());
    }
}
```

## الحصول على التعليقات التوضيحية للخط

يقرأ هذا المثال التعليقات التوضيحية للأسطر ويطبع إحداثيات البداية والنهاية الخاصة بها.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بالمراجعة خلال التعليقات التوضيحية للصفحة وحدد [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Line`.
1. أرسل كل تطابق إلى [LineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/lineannotation/) واطبع إحداثياته.

```java
public static void lineAnnotationsGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Line) {
                LineAnnotation la = (LineAnnotation) annotation;
                System.out.printf("[%s,%s]-[%s,%s]%n",
                        la.getStarting().getX(), la.getStarting().getY(),
                        la.getEnding().getX(), la.getEnding().getY());
            }
        }
    }
}
```

## حذف التعليقات التوضيحية للخط

استخدم هذا الأسلوب عندما يجب إزالة التعليقات التوضيحية للأسطر من الصفحة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. جمع التعليقات التوضيحية من النوع [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Line`.
1. احذف التعليقات التوضيحية المجمعة واحفظ المستند.

```java
public static void lineAnnotationsDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : page.getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Line) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            page.getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## مواضيع ذات صلة بالتعليقات

- [التعليقات التوضيحية التفاعلية](/pdf/java/interactive-annotations/)
- [التعليقات التوضيحية الترميزية](/pdf/java/markup-annotations/)
- [التعليقات التوضيحية الأمنية](/pdf/java/security-annotations/)
- [التعليقات التوضيحية النصية](/pdf/java/text-based-annotations/)
- [التعليقات التوضيحية للعلامة المائية](/pdf/java/watermark-annotations/)
- [استيراد وتصدير التعليقات التوضيحية](/pdf/java/import-export-annotations/)
