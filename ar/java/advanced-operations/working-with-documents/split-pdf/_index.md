---
title: تقسيم ملفات PDF في جافا
linktitle: تقسيم ملفات PDF
type: docs
weight: 60
url: /java/split-pdf-document/
description: تعرف على كيفية تقسيم صفحات PDF إلى ملفات PDF منفصلة في Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قم بتقسيم مستندات PDF حسب الصفحات والنطاقات والمجموعات وأنماط أسماء الملفات باستخدام Java
Abstract: تشرح هذه المقالة كيفية تقسيم مستندات PDF باستخدام Aspose.PDF لـ Java. ويغطي التقسيم إلى صفحات مفردة، وجزأين أو ثلاثة أجزاء، وصفحات فردية وزوجية، وأجزاء ذات حجم ثابت، ونطاقات مخصصة، والصفحة الأولى أو الأخيرة بالإضافة إلى الباقي، ومجموعات الصفحات المخصصة، وإنشاء اسم ملف ثابت.
---
يدعم Aspose.PDF for Java العديد من أنماط التقسيم التي تتجاوز إخراج صفحة واحدة لكل ملف.

## تقسيم ملف PDF إلى ملفات ذات صفحة واحدة

استخدم هذا الأسلوب عندما تصبح كل صفحة مصدر وثيقة مخرجات منفصلة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [مستند] PDF جديد (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) لكل [صفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) تريد تصديرها.
1. أضف [الصفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) المحددة إلى المستند الجديد.
1. احفظ كل مخرج PDF [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void splitDocuments(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        for (int pageNumber = 1; pageNumber <= document.getPages().size(); pageNumber++) {
            try (Document newDocument = new Document()) {
                newDocument.getPages().add(document.getPages().get_Item(pageNumber));
                newDocument.save(outputDir.resolve("Page_" + pageNumber + ".pdf").toString());
            }
        }
    }
}
```

## قم بتقسيم ملف PDF إلى قسمين

يقسم هذا المثال المستند المصدر إلى ملفي إخراج متسلسلين استنادًا إلى نقطة المنتصف.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. احسب النقطة الوسطى لمجموعة [الصفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) المتوفرة.
1. انسخ النصف الأول من الصفحات في مستند إخراج واحد والصفحات المتبقية في مستند آخر.
1. احفظ كلا الوثيقتين الناتجتين.

```java
public static void splitDocumentsIntoTwoParts(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        int midPoint = totalPages / 2;

        try (Document firstDocument = new Document()) {
            for (int pageNumber = 1; pageNumber <= midPoint; pageNumber++) {
                firstDocument.getPages().add(document.getPages().get_Item(pageNumber));
            }
            firstDocument.save(outputDir.resolve("Part_1.pdf").toString());
        }

        try (Document secondDocument = new Document()) {
            for (int pageNumber = midPoint + 1; pageNumber <= totalPages; pageNumber++) {
                secondDocument.getPages().add(document.getPages().get_Item(pageNumber));
            }
            secondDocument.save(outputDir.resolve("Part_2.pdf").toString());
        }
    }
}
```

## قم بتقسيم ملف PDF إلى مجموعات صفحات ذات حجم ثابت

استخدم هذا النمط عندما يجب أن يحتوي كل ملف إخراج على نفس عدد الصفحات، باستثناء الجزء الأخير.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بالتنقل عبر مجموعة [الصفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) في مجموعات `pagesPerPart`.
1. قم بإنشاء مستند إخراج جديد لكل مجموعة وانسخ نطاق الصفحات المحسوب فيه.
1. احفظ كل جزء باسم الملف الذي تم إنشاؤه.

```java
public static void splitDocumentsEveryNPages(Path inputFile, Path outputDir, int pagesPerPart) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        int partIndex = 1;

        for (int startPage = 1; startPage <= totalPages; startPage += pagesPerPart) {
            int endPage = Math.min(startPage + pagesPerPart - 1, totalPages);
            try (Document partDocument = new Document()) {
                for (int pageNumber = startPage; pageNumber <= endPage; pageNumber++) {
                    partDocument.getPages().add(document.getPages().get_Item(pageNumber));
                }
                partDocument.save(outputDir.resolve("Every_" + pagesPerPart + "_Part_" + partIndex + ".pdf").toString());
            }
            partIndex++;
        }
    }
}
```

## قم بتقسيم ملف PDF حسب نطاقات الصفحات المخصصة

يتيح لك هذا المثال تحديد صفحات البداية والنهاية الواضحة لكل مستند مخرجات.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. حدد نطاقات [الصفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) المطلوبة في صفيف أو مجموعة أخرى.
1. تحقق من صحة كل نطاق مقابل عدد الصفحات المصدر وانسخ الصفحات المطابقة في مستند جديد.
1. احفظ كل ملف إخراج يستند إلى النطاق.

```java
public static void splitDocumentsByPageRanges(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        Integer[][] ranges = {{1, 3}, {4, 6}, {7, null}};

        for (int index = 0; index < ranges.length; index++) {
            int startPage = ranges[index][0];
            Integer endPage = ranges[index][1];
            if (startPage > totalPages) {
                continue;
            }

            int effectiveEnd = endPage == null ? totalPages : Math.min(endPage, totalPages);
            if (startPage > effectiveEnd) {
                continue;
            }

            try (Document rangeDocument = new Document()) {
                for (int pageNumber = startPage; pageNumber <= effectiveEnd; pageNumber++) {
                    rangeDocument.getPages().add(document.getPages().get_Item(pageNumber));
                }
                rangeDocument.save(outputDir.resolve(
                        "Range_" + (index + 1) + "_" + startPage + "_to_" + effectiveEnd + ".pdf").toString());
            }
        }
    }
}
```

## قم بتقسيم الصفحة الأولى والصفحات المتبقية

استخدم هذا الأسلوب عندما يجب تصدير صفحة الغلاف بشكل منفصل عن بقية المستند.

1. افتح ملف PDF [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) المصدر وتأكد من احتوائه على صفحات.
1. قم بإنشاء مستند إخراج واحد لـ [الصفحة] الأولى (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. قم بإنشاء مستند آخر لنطاق الصفحات المتبقي عند توفر أكثر من صفحة واحدة.
1. حفظ كلا النتائج.

```java
public static void splitDocumentsFirstPageAndRest(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        if (totalPages == 0) {
            return;
        }

        try (Document firstPageDocument = new Document()) {
            firstPageDocument.getPages().add(document.getPages().get_Item(1));
            firstPageDocument.save(outputDir.resolve("First_Page.pdf").toString());
        }

        if (totalPages == 1) {
            return;
        }

        try (Document remainingPagesDocument = new Document()) {
            for (int pageNumber = 2; pageNumber <= totalPages; pageNumber++) {
                remainingPagesDocument.getPages().add(document.getPages().get_Item(pageNumber));
            }
            remainingPagesDocument.save(outputDir.resolve("Remaining_Pages.pdf").toString());
        }
    }
}
```

## تقسيم الصفحة الأخيرة والصفحات السابقة

يفصل هذا المثال الصفحة الأخيرة عن بقية المستند، وهو أمر مفيد لاستخراج صفحات الملخص أو التوقيع.

1. افتح ملف PDF [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) المصدر وتأكد من أنه ليس فارغًا.
1. انسخ [الصفحة] الأخيرة (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) إلى مستند إخراج جديد.
1. قم بإزالة تلك الصفحة من المستند الأصلي عندما تظل الصفحات السابقة موجودة.
1. احفظ الصفحة الأخيرة والصفحات المتبقية كملفات منفصلة.

```java
public static void splitDocumentsLastPageAndRest(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        if (totalPages == 0) {
            return;
        }

        try (Document lastPageDocument = new Document()) {
            lastPageDocument.getPages().add(document.getPages().get_Item(totalPages));
            lastPageDocument.save(outputDir.resolve("Last_Page.pdf").toString());
        }

        if (totalPages == 1) {
            return;
        }

        document.getPages().delete(totalPages);
        document.save(outputDir.resolve("Previous_Pages.pdf").toString());
    }
}
```

## قم بتقسيم ملف PDF إلى ثلاثة أجزاء

استخدم هذا النمط عندما يجب تقسيم المستند إلى ثلاثة أقسام متتالية ذات حجم متساوٍ تقريبًا.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وحدد العدد الإجمالي للصفحات.
1. احسب الحجم التقريبي لكل جزء إخراج.
1. قم بإنشاء ما يصل إلى ثلاثة مستندات وانسخ نطاقات [الصفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) المطابقة.
1. احفظ كل جزء تم إنشاؤه.

```java
public static void splitDocumentsIntoThreeParts(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        if (totalPages == 0) {
            return;
        }

        int partSize = Math.max(1, (totalPages + 2) / 3);
        for (int partIndex = 0; partIndex < 3; partIndex++) {
            int startPage = partIndex * partSize + 1;
            int endPage = Math.min((partIndex + 1) * partSize, totalPages);
            if (startPage > totalPages) {
                break;
            }

            try (Document partDocument = new Document()) {
                for (int pageNumber = startPage; pageNumber <= endPage; pageNumber++) {
                    partDocument.getPages().add(document.getPages().get_Item(pageNumber));
                }
                partDocument.save(outputDir.resolve("Three_Parts_" + (partIndex + 1) + ".pdf").toString());
            }
        }
    }
}
```

## قم بتقسيم ملف PDF إلى مجموعات صفحات مخصصة

يوضح هذا المثال كيفية إنشاء ملفات الإخراج من مجموعات الصفحات غير المتسلسلة بدلاً من النطاقات المستمرة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. حدد مجموعات مخصصة من أرقام [الصفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. قم بإنشاء مستند إخراج جديد لكل مجموعة وأضف الصفحات الصالحة فقط من تلك المجموعة.
1. احفظ كل مستند مجموعة غير فارغ.

```java
public static void splitDocumentsCustomPageGroups(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        List<List<Integer>> groups = List.of(
                List.of(1, 2, 5),
                List.of(3, 4, 6, 7));

        int groupIndex = 1;
        for (List<Integer> group : groups) {
            try (Document groupDocument = new Document()) {
                for (Integer pageNumber : group) {
                    if (pageNumber >= 1 && pageNumber <= totalPages) {
                        groupDocument.getPages().add(document.getPages().get_Item(pageNumber));
                    }
                }
                if (groupDocument.getPages().size() > 0) {
                    groupDocument.save(outputDir.resolve("Custom_Group_" + groupIndex + ".pdf").toString());
                }
            }
            groupIndex++;
        }
    }
}
```

## قم بتقسيم ملف PDF إلى صفحات مفردة بأسماء ملفات ثابتة

استخدم هذا الإصدار عندما تظل أسماء المخرجات قابلة للفرز بشكل معجمي، على سبيل المثال في خطوط الأنابيب الآلية.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء مستند إخراج واحد لكل [صفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. احفظ كل ملف برقم صفحة مبطن صفر.

```java
public static void splitDocumentsWithStableFilenames(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        for (int pageNumber = 1; pageNumber <= document.getPages().size(); pageNumber++) {
            try (Document newDocument = new Document()) {
                newDocument.getPages().add(document.getPages().get_Item(pageNumber));
                newDocument.save(outputDir.resolve(String.format("Page_%03d.pdf", pageNumber)).toString());
            }
        }
    }
}
```

## قم بتقسيم ملف PDF إلى صفحات فردية وزوجية

يقوم هذا المثال بإنشاء مخرجين عن طريق فصل الصفحات وفقًا لتكافؤ أرقام الصفحات الخاصة بها.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء مستند إخراج واحد لأرقام [الصفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) الفردية وآخر لأرقام الصفحات الزوجية.
1. قم بالتكرار عبر الصفحات المصدر مع الزيادة المطلوبة لكل مستند مخرجات.
1. احفظ نتائج الصفحات الفردية والصفحات الزوجية بشكل منفصل.

```java
public static void splitDocumentsOddEvenPages(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();

        try (Document oddDocument = new Document()) {
            for (int pageNumber = 1; pageNumber <= totalPages; pageNumber += 2) {
                oddDocument.getPages().add(document.getPages().get_Item(pageNumber));
            }
            oddDocument.save(outputDir.resolve("Odd_Pages.pdf").toString());
        }

        try (Document evenDocument = new Document()) {
            for (int pageNumber = 2; pageNumber <= totalPages; pageNumber += 2) {
                evenDocument.getPages().add(document.getPages().get_Item(pageNumber));
            }
            evenDocument.save(outputDir.resolve("Even_Pages.pdf").toString());
        }
    }
}
```
