---
title: تحسين ملفات PDF في جافا
linktitle: تحسين قوات الدفاع الشعبي
type: docs
weight: 30
url: /java/optimize-pdf/
description: تعرف على كيفية تحسين حجم ملف PDF وضغطه وتقليله في Java باستخدام Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: ضغط موارد PDF وتقليل حجم الملف باستخدام Java
Abstract: تشرح هذه المقالة كيفية تحسين ملفات PDF باستخدام Aspose.PDF لـ Java. وهو يغطي تحسين المستند بالكامل، وضغط الموارد، وتقليل جودة الصورة، وإزالة الكائنات والتدفقات غير المستخدمة، وربط التدفقات المكررة، وإلغاء تضمين الخطوط، وتسوية التعليقات التوضيحية والنماذج، وتحويل التدرج الرمادي، وضغط الصور Flate.
---
يعرض Aspose.PDF لـ Java ميزات التحسين من خلال `Document.optimize` و`optimizeResources` و`OptimizationOptions`.

## قم بتحسين ملف PDF باستخدام التحسين العام للمستندات

استخدم هذا المثال عندما تريد أن يقوم Aspose.PDF بتطبيق روتين تحسين المستند بالكامل المضمن.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اتصل `optimize()` على المستند.
1. احفظ الملف الأمثل وقارن بين الحجم الأصلي وحجم الإخراج.

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

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بتشغيل `optimizeResources()` لتحسين الموارد الداخلية.
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

## ضغط جميع الصور في ملف PDF

استخدم هذا الأسلوب عندما تحتاج المستندات ذات الصور الثقيلة إلى حجم ملف أصغر ويكون تقليل جودة الصورة مقبولاً.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ [خيارات التحسين](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) وقم بتمكين ضغط الصور بمستوى الجودة المطلوب.
1. قم بتحسين موارد المستند باستخدام هذه الإعدادات.
1. احفظ الملف الأمثل وقارن أحجام الملفات.

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

## قم بإزالة الكائنات غير المستخدمة من ملف PDF

يقوم هذا المثال بإزالة الكائنات غير المستخدمة التي قد تبقى في بنية المستند بعد عمليات التحرير أو الدمج.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [خيارات التحسين](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) وقم بتمكين إزالة الكائنات غير المستخدمة.
1. تحسين الموارد وحفظ الملف المحدث.
1. طباعة أحجام الملفات الأصلية والمصغرة.

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

استخدم هذا الأسلوب عندما تريد تجاهل بيانات الدفق التي لم تعد تشير إليها الوثيقة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بتكوين [خيارات التحسين](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) لإزالة التدفقات غير المستخدمة.
1. قم بتحسين الموارد، وحفظ مستند الإخراج، ومقارنة أحجام الملفات.

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

يعمل هذا المثال على إلغاء تكرار التدفقات المتكررة بحيث يمكن تخزين المحتوى المتطابق مرة واحدة فقط.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ [خيارات التحسين](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) وقم بتمكين ربط الدفق المكرر.
1. قم بتحسين الموارد، وحفظ مستند الإخراج، وطباعة أحجام الملفات.

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

استخدم هذا الخيار عندما يكون تقليل حجم الملف أكثر أهمية من الاحتفاظ ببيانات الخط المضمنة في المخرجات.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بتكوين [خيارات التحسين](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) لإلغاء تضمين الخطوط.
1. قم بتحسين الموارد وحفظ المستند ومقارنة أحجام الملفات.

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

## تسوية التعليقات التوضيحية في ملف PDF

يقوم هذا المثال بتحويل التعليقات التوضيحية إلى محتوى صفحة ثابت بحيث لا تظل كائنات تفاعلية.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بالتكرار خلال كل [صفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ومجموعة [التعليقات التوضيحية](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) الخاصة بها.
1. قم بتسوية كل تعليق توضيحي واحفظ المستند المحدث.

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

## تسوية حقول نموذج PDF

استخدم هذا الأسلوب عندما تصبح حقول النموذج القابلة للتعبئة محتوى ثابتًا قبل التوزيع أو الأرشفة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. تحقق مما إذا كانت الوثيقة تحتوي على عناصر واجهة مستخدم النموذج.
1. قم بتسوية كل [حقل](https://reference.aspose.com/pdf/java/com.aspose.pdf/field/) الذي يمثله [تعليق القطعة](https://reference.aspose.com/pdf/java/com.aspose.pdf/widgetannotation/).
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

## تحويل ملف PDF إلى تدرج رمادي

يقوم هذا المثال بتغيير كل صفحة إلى التدرج الرمادي، مما يمكن أن يساعد في تقليل تعقيد الألوان وتوحيد الإخراج لسير عمل الأرشفة أو الطباعة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بالتكرار خلال كل [صفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) في المستند.
1. اتصل بـ `makeGrayscale()` في كل صفحة واحفظ ملف الإخراج.

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

## استخدم FlateDecode لضغط الصور

استخدم هذا النمط عندما تريد تطبيق الضغط المستند إلى Flate على الصور أثناء تحسين موارد PDF.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ [خيارات التحسين](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) واضبط ترميز الصورة على [ImageEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageencoding/).`Flate`.
1. تحسين موارد الوثيقة وحفظ ملف الإخراج.

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

## طباعة أحجام الملفات الأصلية والمحسنة

تقوم هذه الطريقة المساعدة بالإبلاغ عن اختلاف الحجم بين الملف المصدر وملف الإخراج الأمثل.

1. قراءة حجم ملف الإدخال.
1. قراءة حجم ملف الإخراج.
1. اطبع كلا القيمتين في رسالة حالة واحدة.

```java
private static void printFileSizes(Path inputFile, Path outputFile) throws Exception {
    System.out.println("Original file size: " + Files.size(inputFile)
            + ". Reduced file size: " + Files.size(outputFile));
}
```
