---
title: تحسين ملفات PDF في Java
linktitle: تحسين PDF
type: docs
weight: 30
url: /ar/java/optimize-pdf/
description: تعلم كيفية تحسين وضغط وتقليل حجم ملف PDF في Java باستخدام Aspose.PDF.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: ضغط موارد PDF وتقليل حجم الملف باستخدام Java
Abstract: يشرح هذا المقال كيفية تحسين ملفات PDF باستخدام Aspose.PDF for Java. يغطي تحسين المستند بالكامل، ضغط الموارد، خفض جودة الصور، إزالة الكائنات والتدفقات غير المستخدمة، ربط التدفقات المكررة، فك تضمين الخطوط، تسطيح التعليقات التوضيحية والنماذج، تحويل إلى تدرج الرمادي، وضغط الصور باستخدام Flate.
---
Aspose.PDF for Java يكشف عن ميزات التحسين عبر `Document.optimize`, `optimizeResources`, و `OptimizationOptions`.

## تحسين ملف PDF باستخدام تحسين المستند العام

استخدم هذا المثال عندما تريد أن يقوم Aspose.PDF بتطبيق روتين تحسين المستند الكامل المدمج.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اتصال `optimize()` على المستند.
1. احفظ الملف المُحسّن وقارن بين الأحجام الأصلية والصادرة

```java
public static void optimizePdf(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        document.optimize();
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## تقليل حجم PDF عن طريق تحسين الموارد

يركز هذا المثال على تحسين مستوى الموارد دون تكوين الخيارات الفردية يدويًا.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. تشغيل `optimizeResources()` لتحسين الموارد الداخلية.
1. احفظ النتيجة واطبع أحجام ملفات الإدخال والإخراج.

```java
public static void reduceSizePdf(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        document.optimizeResources();
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## ضغط جميع الصور في PDF

استخدم هذا النهج عندما تحتاج المستندات التي تحتوي على الكثير من الصور إلى حجم ملف أصغر ويكون تقليل بعض جودة الصورة مقبولًا.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. إنشاء [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) وتمكين ضغط الصورة بمستوى الجودة المطلوب.
1. حسّن موارد المستند باستخدام تلك الإعدادات.
1. احفظ الملف المُحسّن وقارن أحجام الملفات.

```java
public static void shrinkingOrCompressingAllImages(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.getImageCompressionOptions().setCompressImages(true);
        optimizeOptions.getImageCompressionOptions().setImageQuality(50);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## إزالة الكائنات غير المستخدمة من ملف PDF

يعمل هذا المثال على إزالة الكائنات غير المستخدمة التي قد تبقى في بنية المستند بعد التعديلات أو عمليات الدمج.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. إنشاء [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) وتمكين إزالة الكائنات غير المستخدمة.
1. قم بتحسين الموارد واحفظ الملف المحدث.
1. اطبع أحجام الملفات الأصلية والمخفضة.

```java
public static void removingUnusedObjects(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setRemoveUnusedObjects(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## إزالة التدفقات غير المستخدمة من ملف PDF

استخدم هذا النهج عندما تريد التخلص من بيانات التدفق التي لم تعد مُشار إليها من قبل المستند.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. تكوين [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) لإزالة التدفقات غير المستخدمة.
1. حسّن الموارد، احفظ مستند الإخراج، وقارن أحجام الملفات.

```java
public static void removingUnusedStreams(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setRemoveUnusedStreams(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## ربط التدفقات المكررة في ملف PDF

يُزيل هذا المثال التكرار في التدفقات المتكررة بحيث يمكن تخزين المحتوى المتطابق مرة واحدة فقط.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. إنشاء [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) وتمكين ربط تدفق مكرر.
1. قم بتحسين الموارد، احفظ مستند الإخراج، واطبع أحجام الملفات.

```java
public static void linkingDuplicateStreams(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setLinkDuplicateStreams(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## إلغاء تضمين الخطوط من ملف PDF

استخدم هذا الخيار عندما يكون تقليل حجم الملف أكثر أهمية من الاحتفاظ ببيانات الخط المضمنة في الإخراج.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. تكوين [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) لإلغاء تضمين الخطوط.
1. حسّن الموارد، احفظ المستند، وقارن أحجام الملفات.

```java
public static void unembedFonts(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setUnembedFonts(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## تسطيح التعليقات التوضيحية في ملف PDF

هذا المثال يحول التعليقات التوضيحية إلى محتوى ثابت للصفحة بحيث لا تظل كائنات تفاعلية.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. التكرار عبر كل [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) وخاصته [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) مجموعة.
1. قم بتسوية كل التعليقات التوضيحية واحفظ المستند المحدث.

```java
public static void flattenAnnotations(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            for (Annotation annotation : page.getAnnotations()) {
                annotation.flatten();
            }
        }
        document.save(outputFile.toString());
    }
}
```

## تسطيح حقول نموذج PDF

استخدم هذا النهج عندما يجب أن تصبح حقول النموذج القابلة للملء محتوى ثابتًا قبل التوزيع أو الأرشفة.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. تحقق مما إذا كان المستند يحتوي على أدوات النماذج.
1. سطح كل [Field](https://reference.aspose.com/pdf/java/com.aspose.pdf/field/) مُمَثَّل بـ [WidgetAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/widgetannotation/).
1. احفظ ملف الإخراج واطبع أحجام الملفات.

```java
public static void flattenForms(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getForm() != null && document.getForm().size() > 0) {
            for (WidgetAnnotation annotation : document.getForm()) {
                if (annotation instanceof Field field) {
                    field.flatten();
                }
            }
        }
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## تحويل ملف PDF إلى تدرج الرمادي

هذا المثال يغيّر كل صفحة إلى التدرج الرمادي، مما يمكن أن يساعد في تقليل تعقيد الألوان وتوحيد المخرجات لأغراض الأرشفة أو عمليات الطباعة.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. التكرار عبر كل [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) في المستند.
1. اتصال `makeGrayscale()` على كل صفحة واحفظ ملف الإخراج.

```java
public static void convertPdfFromRgbColorspaceToGrayscale(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            page.makeGrayscale();
        }
        document.save(outputFile.toString());
    }
}
```

## استخدم ضغط الصور FlateDecode

استخدم هذا النمط عندما تريد تطبيق ضغط Flate-based على الصور أثناء تحسين موارد PDF.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. إنشاء [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) وضع ترميز الصورة إلى [ImageEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageencoding/).`Flate`.
1. حسّن موارد المستند واحفظ ملف الإخراج.

```java
public static void usingFlatedecodeCompression(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizationOptions = new OptimizationOptions();
        optimizationOptions.getImageCompressionOptions().setEncoding(ImageEncoding.Flate);
        document.optimizeResources(optimizationOptions);
        document.save(outputFile.toString());
    }
}
```

## اطبع أحجام الملفات الأصلية والمحسّنة

هذه الطريقة المساعدة تُبلغ عن الفرق في الحجم بين ملف المصدر وملف الإخراج المُحسّن.

1. اقرأ حجم ملف الإدخال.
1. قراءة حجم ملف الإخراج.
1. اطبع القيمتين في رسالة حالة واحدة.

```java
private static void printFileSizes(Path inputFile, Path outputFile) throws Exception {
    System.out.println("Original file size: " + Files.size(inputFile)
            + ". Reduced file size: " + Files.size(outputFile));
}
```
