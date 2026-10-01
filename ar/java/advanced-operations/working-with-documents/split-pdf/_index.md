---
title: تقسيم ملفات PDF في Java
linktitle: تقسيم ملفات PDF
type: docs
weight: 60
url: /ar/java/split-pdf-document/
description: تعلم كيفية تقسيم صفحات PDF إلى ملفات PDF منفصلة باستخدام Java.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قسّم مستندات PDF حسب الصفحات، والنطاقات، والمجموعات، وأنماط أسماء الملفات باستخدام Java
Abstract: تشرح هذه المقالة كيفية تقسيم مستندات PDF باستخدام Aspose.PDF for Java. وتغطي تقسيمها إلى صفحات منفردة، إلى جزئين أو ثلاثة أجزاء، الصفحات الفردية والزوجية، قطع بحجم ثابت، نطاقات مخصصة، الصفحة الأولى أو الأخيرة مع البقية، مجموعات صفحات مخصصة، وتوليد أسماء ملفات ثابتة.
---
يدعم Aspose.PDF for Java عدة أنماط تقسيم تتجاوز إخراج صفحة واحدة لكل ملف.

## قسّم ملف PDF إلى ملفات صفحة واحدة

استخدم هذا الأسلوب عندما يجب أن يصبح كل صفحة مصدر مستندًا ناتجًا منفصلًا.

1. افتح PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. إنشاء PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) لكل [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) أنت تريد التصدير.
1. إضافة المحدد [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) إلى المستند الجديد.
1. احفظ كل PDF ناتج [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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

## قسّم ملف PDF إلى جزأين

يقوم هذا المثال بتقسيم المستند الأصلي إلى ملفي إخراج متتاليين بناءً على نقطة المنتصف.

1. افتح PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. احسب نقطة المنتصف المتاحة [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) مجموعة.
1. انسخ النصف الأول من الصفحات إلى مستند إخراج واحد والبقية إلى مستند آخر.
1. احفظ كلا المستندين الناتجين.

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

## قسّم ملف PDF إلى مجموعات صفحات بحجم ثابت

استخدم هذا النمط عندما يجب أن يحتوي كل ملف ناتج على نفس عدد الصفحات، باستثناء الجزء الأخير إذا لزم الأمر.

1. افتح PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. التكرار عبر [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) تجميع في مجموعات من `pagesPerPart`.
1. إنشاء مستند إخراج جديد لكل مجموعة ونسخ نطاق الصفحات المحسوب إليه.
1. احفظ كل جزء باسم ملف تم إنشاؤه.

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

## تقسيم ملف PDF حسب نطاقات صفحات مخصصة

يتيح لك هذا المثال تحديد صفحات البداية والنهاية الصريحة لكل مستند ناتج.

1. افتح PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. عرّف المطلوب [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) نطاقات في مصفوفة أو مجموعة أخرى.
1. تحقق من صحة كل نطاق مقابل عدد صفحات المصدر وانسخ الصفحات المطابقة إلى مستند جديد.
1. احفظ كل ملف إخراج يعتمد على النطاق.

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

## قسّم الصفحة الأولى والصفحات المتبقية

استخدم هذا النهج عندما يجب تصدير صفحة الغلاف بصورة منفصلة عن باقي المستند.

1. افتح PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وتأكد من أنه يحتوي على صفحات.
1. إنشاء مستند إخراج واحد للأول [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. إنشاء مستند آخر لنطاق الصفحات المتبقية عندما تكون هناك أكثر من صفحة واحدة متاحة.
1. احفظ كلا النتيجتين.

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

## قسم الصفحة الأخيرة والصفحات السابقة

يفصل هذا المثال الصفحة الأخيرة عن باقي المستند، وهو مفيد لاستخراج صفحات الملخص أو التوقيع.

1. افتح PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وتأكد من أنه غير فارغ.
1. انسخ الأخير [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) إلى مستند إخراج جديد.
1. قم بإزالة تلك الصفحة من المستند الأصلي عندما لا تزال الصفحات السابقة موجودة.
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

## قسّم ملف PDF إلى ثلاثة أجزاء

استخدم هذا النمط عندما يجب تقسيم المستند إلى ثلاثة أقسام متتالية بحجم تقريبًا متساوٍ.

1. افتح PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وحدد إجمالي عدد الصفحات.
1. احسب الحجم التقريبي لكل جزء من الإخراج.
1. إنشاء ما يصل إلى ثلاثة مستندات ونسخ المطابقة [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) نطاقات.
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

## قسّم ملف PDF إلى مجموعات صفحات مخصصة

يوضح هذا المثال كيفية إنشاء ملفات الإخراج من مجموعات صفحات غير متسلسلة بدلاً من النطاقات المتصلة.

1. افتح PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. تعريف مجموعات مخصصة من [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) الأرقام.
1. أنشئ مستند إخراج جديد لكل مجموعة وأضف فقط الصفحات الصالحة من تلك المجموعة.
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

## قسّم ملف PDF إلى صفحات منفردة بأسماء ملفات ثابتة

استخدم هذا الإصدار عندما يجب أن تظل أسماء المخرجات قابلة للترتيب الحرفي، على سبيل المثال في خطوط الأنابيب الآلية.

1. افتح PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. إنشاء مستند إخراج واحد لكل [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. احفظ كل ملف برقم صفحة مملوء بالأصفار.

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

## قسّم ملف PDF إلى الصفحات الفردية والزوجية

ينشئ هذا المثال مخرجين عن طريق فصل الصفحات وفقاً لزوجية أو فردية رقم الصفحة.

1. افتح PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. إنشاء مستند إخراج واحد للعدد الفردي [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) الأرقام وآخر لأرقام الصفحات الزوجية.
1. قم بالتكرار عبر الصفحات المصدرية بالزيادة المطلوبة لكل مستند إخراج.
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
