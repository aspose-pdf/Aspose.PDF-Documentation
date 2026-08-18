---
title: مقارنة مستندات PDF في جافا
linktitle: قارن قوات الدفاع الشعبي
type: docs
weight: 130
url: /java/compare-pdf-documents/
description: تعرف على كيفية مقارنة مستندات PDF في Java باستخدام مخرجات الفرق الرسومية جنبًا إلى جنب باستخدام Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قارن بين صفحات PDF والمستندات الكاملة مع مخرجات الفرق المرئي في Java
Abstract: تشرح هذه المقالة كيفية مقارنة مستندات PDF باستخدام Aspose.PDF لـ Java. تعرف على كيفية مقارنة صفحات معينة أو ملفات PDF بأكملها مع الإخراج جنبًا إلى جنب، وإنشاء تقارير فروق PDF رسومية، وتصدير اختلافات الصور على مستوى الصفحة.
---
يوفر Aspose.PDF for Java كلاً من واجهات برمجة التطبيقات للمقارنة الرسومية جنبًا إلى جنب لاكتشاف الاختلافات بين ملفات PDF.

## مقارنة الصفحات وتصدير الصور المختلفة

استخدم هذا المثال عندما تحتاج إلى إخراج اختلافات مستندة إلى الصورة لزوج معين من صفحات PDF.

1. افتح كائني PDF [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) المصدرين.
1. استخدم [GraphicalPdfComparer](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/graphicalpdfcomparer/) للحصول على [ImagesDifference](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/imagesdifference/) على مستوى الصفحة.
1. استخدم "GraphicalPdfComparer" للحصول على "ImagesDifference" على مستوى الصفحة.
1. قم بتصدير صور الفرق التي تم إنشاؤها والتخلص من نتيجة المقارنة.

```java
public static void comparePdfWithGetDifferenceMethod(
        Path inputFile1, Path inputFile2, Path diffOutputFile, Path destinationOutputFile) throws Exception {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        GraphicalPdfComparer comparer = new GraphicalPdfComparer();
        ImagesDifference imagesDifference = comparer.getDifference(document1.getPages().get_Item(1),
                document2.getPages().get_Item(1));

        ImageIO.write(imagesDifference.differenceToImage(Color.getRed(), Color.getWhite()),
                "png", diffOutputFile.toFile());
        ImageIO.write(imagesDifference.getDestinationImage(), "png", destinationOutputFile.toFile());
        imagesDifference.dispose();
    }
    System.out.println("Difference images saved to " + diffOutputFile + " and " + destinationOutputFile);
}
```

## مقارنة صفحات محددة جنبًا إلى جنب

استخدم هذا المثال عندما يجب مقارنة الصفحات المحددة فقط وحفظها كنتيجة PDF جنبًا إلى جنب.

1. افتح كائني PDF [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) المصدرين.
1. قم بتكوين [SideBySideComparisonOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/sidebysidecomparisonoptions/) لوضع المقارنة المطلوب.
1. قارن الصفحات المحددة واحفظ ملف PDF الناتج.

```java
public static void comparingSpecificPages(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        SideBySideComparisonOptions options = new SideBySideComparisonOptions();
        options.setAdditionalChangeMarks(true);
        options.setComparisonMode(ComparisonMode.IgnoreSpaces);

        SideBySidePdfComparer.compare(document1.getPages().get_Item(1), document2.getPages().get_Item(1),
                outputFile.toString(), options);
    }
    System.out.println("Specific pages comparison saved to " + outputFile);
}
```

## قارن مستندات PDF الكاملة بيانياً

يقوم هذا المثال بإنشاء تقرير PDF رسومي يسلط الضوء على الاختلافات المرئية عبر المستندات بأكملها.

1. افتح كائني PDF [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) المصدرين.
1. قم بتكوين حد [GraphicalPdfComparer](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/graphicalpdfcomparer/) واللون والدقة.
1. قارن المستندات الكاملة واحفظ ملف PDF الناتج الرسومي.

```java
public static void comparePdfWithCompareDocumentsToPdfMethod(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        GraphicalPdfComparer pdfComparer = new GraphicalPdfComparer();
        pdfComparer.setThreshold(3.0);
        pdfComparer.setColor(Color.getBlue());
        pdfComparer.setResolution(new Resolution(300));
        pdfComparer.compareDocumentsToPdf(document1, document2, outputFile.toString());
    }
    System.out.println("Graphical comparison saved to " + outputFile);
}
```

## قارن المستندات بأكملها جنبًا إلى جنب

استخدم هذا المثال عندما يجب مقارنة المستندات بأكملها صفحة بصفحة في مخرجات PDF جنبًا إلى جنب.

1. افتح كائني PDF [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) المصدرين.
1. قم بتكوين [SideBySideComparisonOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/sidebysidecomparisonoptions/) لسلوك المقارنة المطلوب.
1. قارن المستندات الكاملة واحفظ النتيجة بصيغة PDF.

```java
public static void comparingEntireDocuments(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        SideBySideComparisonOptions options = new SideBySideComparisonOptions();
        options.setAdditionalChangeMarks(true);
        options.setComparisonMode(ComparisonMode.IgnoreSpaces);

        SideBySidePdfComparer.compare(document1, document2, outputFile.toString(), options);
    }
    System.out.println("Entire document comparison saved to " + outputFile);
}
```
