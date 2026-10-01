---
title: التعليقات التوضيحية القائمة على النص باستخدام جافا
linktitle: التعليقات النصية
type: docs
weight: 10
url: /ar/java/text-based-annotations/
description: تعلم كيفية إنشاء وفحص وحذف التعليقات التوضيحية القائمة على النص في PDF باستخدام Aspose.PDF for Java، بما في ذلك النص الحر، والتمييز، والخط عبر، والخط المتموج، وتحت الخط.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: اعمل مع تعليقات PDF النصية في Java.
Abstract: توضح هذه المقالة كيفية التعامل مع خمسة أنواع من التعليقات التوضيحية القائمة على النص في Aspose.PDF for Java، بما في ذلك تعليقات النص الحر، وتحديد النص (highlight)، والشطب (strikeout)، والخط المتعرج (squiggly)، وتسطير النص (underline). تعلّم كيفية إضافة التعليقات التوضيحية، واسترجاعها، وحذفها، بالإضافة إلى تقنيات متقدمة مثل وضع علامات على النص وتسطح العلامات التفاعلية.
---
التعليقات التوضيحية المعتمدة على النص تمكّن المراجعين والمطورين من إضافة ملاحظات تفاعلية وتظليل وتوسيم إلى مستندات PDF دون تعديل المحتوى الأساسي. يغطي هذا القسم خمسة أنواع عملية من التعليقات التوضيحية تُستخدم في سير عمل مراجعة المستندات، سيناريوهات الامتثال، ودورات التغذية الراجعة التعاونية.

## دليل سريع: أنواع التعليقات التوضيحية

يغطي هذا المقال أنواع التعليقات التوضيحية القائمة على النص التالية:

- **نص حر**: صناديق نص قابلة للتحرير لإضافة الملاحظات والتعليقات
- **Highlight**: تأكيد بصري على مقاطع النص المهمة
- **شطب**: وضع علامة على النص للحذف أو المراجعة أثناء الاستعراض
- **متموج**: خط تحت متموج للدلالة على الأخطاء أو المخاوف
- **Underline**: تأكيد تحت خط تقليدي مع دقة رباعية النقاط اختيارية

## إضافة، جلب، وحذف تعليقات النص الحر

تعمل التعليقات التوضيحية للنص الحر كصناديق نصية عائمة يمكن تعديلها دون التأثير على بنية المستند. استخدم هذه الأمثلة لإضافة صناديق التعليقات، وفحص خصائصها، أو إزالتها.

### إضافة تعليقات نصية حرة

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. إنشاء [FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/freetextannotation/) مع مستطيل وإعدادات المظهر.
1. أضف التعليق التوضيحي إلى الصفحة واحفظ المستند.

```java
public static void freeTextAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FreeTextAnnotation freeTextAnnotation = new FreeTextAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299, 713, 308, 720, true),
                new DefaultAppearance());
        freeTextAnnotation.setTitle("Aspose User");
        freeTextAnnotation.setColor(Color.getLightGreen());

        document.getPages().get_Item(1).getAnnotations().add(freeTextAnnotation);
        document.save(outputFile.toString());
    }
}
```

### احصل على تعليقات نصية مجانية

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. التمرير عبر التعليقات التوضيحية في الصفحة وتصفية حسب [AnnotationType.FreeText](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).
1. استرجاع خصائص التعليقات أو الحدود.

```java
public static void freeTextAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.FreeText) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

### احذف تعليقات النص الحر

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اعثر على ملاحظات النص الحر عن طريق التنقل عبر ملاحظات الصفحة وتصفية حسب النوع.
1. أضف التعليقات التوضيحية المتطابقة إلى قائمة الحذف وأزلها من الصفحة.
1. احفظ المستند المحدث.

```java
public static void freeTextAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.FreeText) {
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

## إضافة، الحصول على، وحذف تعليقات التمييز

تُشير التعليقات التوضيحية المظللة إلى المقاطع المهمة بطبقة نصف شفافة. استخدم هذه الأمثلة لإنشاء تظليلات للمراجعة المستندية، وتحديد مواقع التظليل الحالية، وتنظيف التنسيق.

### إضافة تعليقات توضيحية متميزة

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. إنشاء [HighlightAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/highlightannotation/) مع مستطيل يحدد منطقة التمييز.
1. أضف التعليق التوضيحي إلى الصفحة واحفظ المستند.

```java
public static void textHighlightAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HighlightAnnotation highlightAnnotation = new HighlightAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(300, 750, 320, 770, true));

        document.getPages().get_Item(1).getAnnotations().add(highlightAnnotation);
        document.save(outputFile.toString());
    }
}
```

### احصل على تعليقات التمييز

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. التكرار عبر التعليقات التوضيحية وتصفية حسب [نوع التعليق التوضيحي.تمييز](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).
1. اقرأ خصائص التعليقات التوضيحية مثل الحدود أو اللون.

```java
public static void textHighlightAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Highlight) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

### حذف تعليقات التمييز

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اجمع تعليقات التمييز عن طريق تصفية التعليقات حسب النوع.
1. إزالة كل تعليقات توضيحية من الصفحة.
1. احفظ المستند المحدث.

```java
public static void textHighlightAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Highlight) {
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

## إضافة، الحصول على، وحذف تعليقات الشطب

تعليقات الشطب تشطب النص للإشارة إلى الحذف أو الرفض أو المراجعة. استخدم هذه الأمثلة لتطبيق تنسيق الشطب أثناء مراجعة المستند، والبحث عن النص المشطوب، وإزالة تعليقات الشطب.

### إضافة تعليقات شطب

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. إنشاء [StrikeOutAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/strikeoutannotation/) مع مستطيل، عنوان، ولون.
1. أضف التعليق التوضيحي إلى الصفحة واحفظ المستند.

```java
public static void textStrikeoutAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        StrikeOutAnnotation strikeoutAnnotation = new StrikeOutAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        strikeoutAnnotation.setTitle("Aspose User");
        strikeoutAnnotation.setSubject("Inserted text 1");
        strikeoutAnnotation.setFlags(AnnotationFlags.Print);
        strikeoutAnnotation.setColor(Color.getBlue());

        document.getPages().get_Item(1).getAnnotations().add(strikeoutAnnotation);
        document.save(outputFile.toString());
    }
}
```

### احصل على تعليقات الخط المشطوب

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. التكرار عبر التعليقات التوضيحية وتصفية حسب [AnnotationType.StrikeOut](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).
1. قراءة بيانات تعريف التعليق أو الحدود.

```java
public static void textStrikeoutAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.StrikeOut) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

### حذف التعليقات المشطوبة

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. جمع التعليقات المشطوبة عن طريق التصفية حسب النوع.
1. إزالة كل تعليقات توضيحية من الصفحة.
1. احفظ المستند المحدث.

```java
public static void textStrikeoutAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.StrikeOut) {
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

## إضافة، الحصول على، وحذف التعليقات التوضيحية المتعرجة

تُظهر تعليقات متعرّجة (تسطير متموج) الأخطاء المحتملة أو المخاوف أو العناصر التي تتطلب الانتباه. استخدم هذه الأمثلة لتعليم النص المشكوك فيه، وفحص التعليقات المتعرّجة، وإزالتها من المستندات.

### إضافة تعليقات توضيحية متموجة

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. إنشاء [SquigglyAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/squigglyannotation/) مع مستطيل وعنوان.
1. أضف التعليق التوضيحي إلى الصفحة واحفظ المستند.

```java
public static void textSquigglyAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        SquigglyAnnotation squigglyAnnotation = new SquigglyAnnotation(
                page,
                new Rectangle(67, 317, 261, 459, true));
        squigglyAnnotation.setTitle("John Smith");
        squigglyAnnotation.setColor(Color.getBlue());

        page.getAnnotations().add(squigglyAnnotation);
        document.save(outputFile.toString());
    }
}
```

### احصل على التعليقات التوضيحية المتعرجة

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. التكرار عبر التعليقات التوضيحية وتصفية حسب [AnnotationType.Squiggly](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).
1. قراءة حدود التعليق أو البيانات الوصفية.

```java
public static void textSquigglyAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Squiggly) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

### احذف التعليقات المتعرجة

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. جمع التعليقات التوضيحية المتعرجة عن طريق التصفية حسب النوع.
1. إزالة كل تعليقات توضيحية من الصفحة.
1. احفظ المستند المحدث.

```java
public static void textSquigglyAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Squiggly) {
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

## إضافة، الحصول على، وحذف تعليقات التسطير

تُبرز تعليقات التسطير الفقرات المهمة بخط سفلي تقليدي. استخدم هذه الأمثلة لإنشاء خطوط سفلية، وقراءة محتوى النص المحدد، وحذف تعليقات التسطير من الصفحات.

### إضافة تعليقات تحتية

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. إنشاء [UnderlineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/underlineannotation/) مع مستطيل ولون.
1. أضف التعليق التوضيحي إلى الصفحة واحفظ المستند.

```java
public static void textUnderlineAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        underlineAnnotation.setTitle("Aspose User");
        underlineAnnotation.setSubject("Inserted Underline 1");
        underlineAnnotation.setFlags(AnnotationFlags.Print);
        underlineAnnotation.setColor(Color.getBlue());

        document.getPages().get_Item(1).getAnnotations().add(underlineAnnotation);
        document.save(outputFile.toString());
    }
}
```

### احصل على تعليقات التسطير

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. التكرار عبر التعليقات التوضيحية وتصفية حسب [AnnotationType.Underline](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).
1. قراءة خصائص التعليق أو الحدود.

```java
public static void textUnderlineAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

### حذف تعليقات التسطير

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. جمع تعليقات الخط السفلي عن طريق التصفية حسب النوع.
1. إزالة كل تعليقات توضيحية من الصفحة.
1. احفظ المستند المحدث.

```java
public static void textUnderlineAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
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

## إضافة تعليق تحت خط مع نقاط رباعية

يحدد هذا المثال مساحة التَسْطير صراحةً من خلال نقاط الرباعية المستمدة من مستطيل.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. إنشاء [UnderlineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/underlineannotation/) و احسب نقاط الرباعية الخاصة به.
1. أضف التعليق التوضيحي إلى الصفحة واحفظ المستند.

```java
public static void textUnderlineWithQuadPointsAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Rectangle rect = new Rectangle(299.988, 713.664, 308.708, 720.769, true);
        UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(
                document.getPages().get_Item(1), rect);
        underlineAnnotation.setTitle("Aspose User");
        underlineAnnotation.setSubject("Inserted Underline with Quad Points");
        underlineAnnotation.setFlags(AnnotationFlags.Print);
        underlineAnnotation.setColor(Color.getBlue());
        underlineAnnotation.setQuadPoints(new com.aspose.pdf.Point[]{
                new com.aspose.pdf.Point(rect.getLLX(), rect.getLLY()),
                new com.aspose.pdf.Point(rect.getURX(), rect.getLLY()),
                new com.aspose.pdf.Point(rect.getURX(), rect.getURY()),
                new com.aspose.pdf.Point(rect.getLLX(), rect.getURY())
        });

        document.getPages().get_Item(1).getAnnotations().add(underlineAnnotation);
        document.save(outputFile.toString());
    }
}
```

## احصل على النص المميز من تعليقات التسطير

استرجع النص الفعلي المغطى بتعليقات التسطير. تظهر هذه الأمثلة نهجين: قراءة النص المعلَّم بالكامل كسلسلة واحدة، أو معالجة أجزاء النص بشكل فردي لتحليل تفصيلي.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. التكرار عبر تعليقات التسطير في الصفحة.
1. اقرأ أيًا منهما `getMarkedText()` أو `getMarkedTextFragments()` وطبع النتائج.

```java
public static void textUnderlineMarkedTextGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
                UnderlineAnnotation ua = (UnderlineAnnotation) annotation;
                System.out.println("Marked text: " + ua.getMarkedText());
            }
        }
    }
}
```

```java
public static void textUnderlineMarkedFragmentsGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
                UnderlineAnnotation ua = (UnderlineAnnotation) annotation;
                for (TextFragment fragment : ua.getMarkedTextFragments()) {
                    System.out.println("Fragment text: " + fragment.getText());
                }
            }
        }
    }
}
```

## حذف تعليقات الخط السفلي حسب العنوان

قم بإزالة التعليقات التوضيحية انتقائيًا عن طريق التصفية بناءً على خصائص البيانات الوصفية مثل العنوان. يتيح هذا النهج تنظيفًا مستهدفًا للتعليقات التوضيحية وفقًا للمؤلف أو الغرض.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. تصفية التعليقات التوضيحية المسطّرة حسب العنوان.
1. احذف التعليقات التوضيحية المطابقة واحفظ المستند المُحدَّث.

```java
public static void textUnderlineByTitleDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<UnderlineAnnotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Underline) {
                UnderlineAnnotation ua = (UnderlineAnnotation) annotation;
                if ("Aspose User".equals(ua.getTitle())) {
                    toDelete.add(ua);
                }
            }
        }
        for (UnderlineAnnotation ua : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(ua);
        }
        document.save(outputFile.toString());
    }
}
```

## إضافة وتعطيل ملاحظة تحتية

حوّل التعليق التوضيحي للخط السفلي التفاعلي إلى محتوى صفحة دائم عن طريق تسويته. يمنع ذلك أي تعديل إضافي مع الحفاظ على مظهر الخط السفلي في أي عارض PDF.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أضف [UnderlineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/underlineannotation/) إلى الصفحة.
1. اتصال `flatten()` على التعليق واحفظ ملف الإخراج.

```java
public static void textUnderlineFlattenAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        underlineAnnotation.setTitle("Aspose User");
        underlineAnnotation.setSubject("Inserted Underline to Flatten");
        underlineAnnotation.setFlags(AnnotationFlags.Print);
        underlineAnnotation.setColor(Color.getBlue());

        document.getPages().get_Item(1).getAnnotations().add(underlineAnnotation);
        underlineAnnotation.flatten();

        document.save(outputFile.toString());
    }
}
```

## مواضيع التعليقات التوضيحية ذات الصلة

- [توضيحات تفاعلية](/pdf/ar/java/interactive-annotations/)
- [التعليقات التوضيحية](/pdf/ar/java/markup-annotations/)
- [تعليقات الأمان](/pdf/ar/java/security-annotations/)
- [تعليقات توضيحية على الشكل](/pdf/ar/java/shape-annotations/)
- [تعليقات توضيحية للعلامة المائية](/pdf/ar/java/watermark-annotations/)
- [استيراد وتصدير التعليقات التوضيحية](/pdf/ar/java/import-export-annotations/)
