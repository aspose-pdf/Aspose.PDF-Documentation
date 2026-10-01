---
title: قارن مستندات PDF في Java
linktitle: قارن PDF
type: docs
weight: 130
url: /ar/java/compare-pdf-documents/
description: تعلم كيفية مقارنة مستندات PDF في Java باستخدام عرض الفرق جنبًا إلى جنب وعرض رسومي مع Aspose.PDF.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قارن صفحات PDF والمستندات الكاملة مع عرض الفرق البصري في Java
Abstract: تشرح هذه المقالة كيفية مقارنة وثائق PDF باستخدام Aspose.PDF for Java. تعلّم كيفية مقارنة صفحات محددة أو ملفات PDF كاملة مع إخراج جنبًا إلى جنب، وإنشاء تقارير اختلافات PDF رسومية، وتصدير اختلافات الصور على مستوى الصفحات.
---
يوفر Aspose.PDF for Java واجهات برمجة تطبيقات للمقارنة جنبًا إلى جنب والرسومية لاكتشاف الاختلافات بين ملفات PDF.

## قارن الصفحات وصدّر صور الاختلاف

استخدم هذا المثال عندما تحتاج إلى إخراج اختلاف مبني على الصورة لزوج محدد من صفحات PDF.

1. افتح كلا ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) الكائنات.
1. استخدم [GraphicalPdfComparer](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/graphicalpdfcomparer/) للحصول على مستوى الصفحة [ImagesDifference](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/imagesdifference/).
1. استخدم 'GraphicalPdfComparer' للحصول على مستوى الصفحة 'ImagesDifference'.
1. تصدير صور الفروقات المُولَّدة وإتلاف نتيجة المقارنة.

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

## قارن الصفحات المحددة جنبًا إلى جنب

استخدم هذا المثال عندما يجب مقارنة الصفحات المحددة فقط وحفظها كنتيجة PDF جنبًا إلى جنب

1. افتح كلا ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) الكائنات.
1. تكوين [SideBySideComparisonOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/sidebysidecomparisonoptions/) لوضع المقارنة المطلوب.
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

## قارن مستندات PDF بالكامل رسوميًا

هذا المثال يولد تقرير PDF رسومي يبرز الفروق البصرية عبر المستندات بالكامل.

1. افتح كلا ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) الكائنات.
1. قم بتكوين [GraphicalPdfComparer](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/graphicalpdfcomparer/) الحدّ، اللون، والدقة.
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

## قارن المستندات بالكامل جنبًا إلى جنب

استخدم هذا المثال عندما يجب مقارنة المستندات بالكامل صفحة بصفحة في مخرجات PDF جنبًا إلى جنب.

1. افتح كلا ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) الكائنات.
1. تكوين [SideBySideComparisonOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/sidebysidecomparisonoptions/) للسلوك المقارن المطلوب.
1. قارن المستندات الكاملة واحفظ النتيجة كملف PDF.

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
