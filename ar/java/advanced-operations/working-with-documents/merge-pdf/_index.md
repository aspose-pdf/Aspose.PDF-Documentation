---
title: دمج ملفات PDF في جافا
linktitle: دمج ملفات PDF
type: docs
weight: 50
url: /java/merge-pdf-documents/
description: تعرف على كيفية دمج ملفات PDF متعددة في مستند واحد في Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: ادمج المستندات الكاملة والنطاقات المحددة والصفحات البديلة مع Java
Abstract: تشرح هذه المقالة كيفية دمج مستندات PDF باستخدام Aspose.PDF لـ Java. وهو يغطي دمج ملفين، ودمج مستندات متعددة، واختيار نطاقات الصفحات، وإدراج مستند في آخر في موضع محدد، وتبديل الصفحات، وإنشاء مخرجات مدمجة باستخدام الإشارات المرجعية للأقسام.
---
يدعم Aspose.PDF for Java العديد من إستراتيجيات الدمج اعتمادًا على كيفية تجميع المخرجات.

## دمج وثيقتين PDF

استخدم هذا الأسلوب عندما تحتاج إلى أبسط عملية دمج وتريد إلحاق مستند كامل بآخر.

1. افتح كائني PDF [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) المصدرين.
1. قم بإضافة مجموعة [الصفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) من المستند الثاني إلى المستند الأول.
1. احفظ ملف PDF المحدث [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void mergeTwoDocuments(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        document1.getPages().add(document2.getPages());
        document1.save(outputFile.toString());
    }
}
```

## انسخ نطاق الصفحات المحدد بين المستندات

تحافظ هذه الطريقة المساعدة على منطق دمج نطاق الصفحات في مكان واحد حتى تتمكن الأمثلة الأخرى من إعادة استخدام نفس روتين النسخ الذي تم التحقق من صحته.

1. افتح أو استقبل كائنات PDF [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) المصدر والوجهة.
1. قم بتطبيع نطاق الصفحات المطلوب بحيث يبقى ضمن مجموعة [الصفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) المتوفرة.
1. أضف كل صفحة من النطاق الذي تم التحقق من صحته إلى المستند الوجهة.

```java
private static void appendPageRange(Document sourceDocument, Document destinationDocument, int startPage, int endPage) {
    int totalPages = sourceDocument.getPages().size();
    if (totalPages == 0) {
        return;
    }

    int start = Math.max(1, startPage);
    int end = Math.min(endPage, totalPages);
    if (start > end) {
        return;
    }

    for (int pageNumber = start; pageNumber <= end; pageNumber++) {
        destinationDocument.getPages().add(sourceDocument.getPages().get_Item(pageNumber));
    }
}
```

## دمج مستندات PDF متعددة في ملف واحد

استخدم هذا النمط عندما تحتاج إلى دمج قائمة ملفات الإدخال في مستند إخراج واحد بالتسلسل.

1. قم بإنشاء ملف PDF فارغ [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. افتح كل ملف إدخال واحدًا تلو الآخر وانسخ نطاق [الصفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) بالكامل إلى مستند الإخراج.
1. احفظ النتيجة المدمجة بعد معالجة كافة الملفات المصدر.

```java
public static void mergeMultipleDocuments(List<Path> inputFiles, Path outputFile) {
    try (Document outputDocument = new Document()) {
        for (Path inputFile : inputFiles) {
            try (Document sourceDocument = new Document(inputFile.toString())) {
                appendPageRange(sourceDocument, outputDocument, 1, sourceDocument.getPages().size());
            }
        }
        outputDocument.save(outputFile.toString());
    }
}
```

## دمج نطاقات الصفحات المحددة من وثيقتين

يقوم هذا المثال بإنشاء ملف إخراج مخصص عن طريق أخذ نطاقات صفحات محددة فقط من كل مستند مصدر.

1. افتح كلا كائني PDF [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) المصدرين وقم بإنشاء مستند إخراج جديد.
1. قم بإضافة نطاقات [الصفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) المطلوبة فقط من كل مستند مصدر.
1. احفظ مستند الإخراج المجمع.

```java
public static void mergeSelectedPageRanges(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString());
         Document outputDocument = new Document()) {
        appendPageRange(document1, outputDocument, 1, 2);
        appendPageRange(document2, outputDocument, 2, 3);
        outputDocument.save(outputFile.toString());
    }
}
```

## أدخل مستند PDF في مستند آخر في موضع محدد

استخدم هذا الأسلوب عندما يجب أن يظهر مستند داخل مستند آخر بدلاً من ظهوره قبله أو بعده فقط.

1. افتح القاعدة وأدرج كائنات PDF [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وقم بإنشاء مستند إخراج جديد.
1. انسخ الجزء الأول من المستند الأساسي، ثم ألحق المستند المدرج بالكامل، وأخيرًا ألحق نطاق [الصفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) الأساسي المتبقي.
1. احفظ النتيجة المعاد ترتيبها في ملف جديد.

```java
public static void mergeInsertDocumentAtPosition(Path inputFile1, Path inputFile2, int insertAfterPage, Path outputFile) {
    try (Document baseDocument = new Document(inputFile1.toString());
         Document insertDocument = new Document(inputFile2.toString());
         Document outputDocument = new Document()) {
        int baseTotalPages = baseDocument.getPages().size();
        int insertIndex = Math.max(0, Math.min(insertAfterPage, baseTotalPages));

        appendPageRange(baseDocument, outputDocument, 1, insertIndex);
        appendPageRange(insertDocument, outputDocument, 1, insertDocument.getPages().size());
        appendPageRange(baseDocument, outputDocument, insertIndex + 1, baseTotalPages);

        outputDocument.save(outputFile.toString());
    }
}
```

## دمج مستندين PDF بالتناوب بين الصفحات

يقوم هذا المثال بتشذير صفحات من وثيقتين، وهو أمر مفيد عندما يجب أن يساهم كلا المدخلين صفحة تلو الأخرى في الإخراج النهائي.

1. افتح كلا كائني PDF [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) المصدرين وقم بإنشاء مستند إخراج جديد.
1. قم بالمراجعة عبر الحد الأقصى لعدد الصفحات المتاحة وأضف كل [صفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) المتوفرة من المستندين الأول والثاني على التوالي.
1. احفظ مستند الإخراج المشذّب.

```java
public static void mergeAlternatingPages(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString());
         Document outputDocument = new Document()) {
        int document1Pages = document1.getPages().size();
        int document2Pages = document2.getPages().size();
        int maxPages = Math.max(document1Pages, document2Pages);

        for (int pageNumber = 1; pageNumber <= maxPages; pageNumber++) {
            if (pageNumber <= document1Pages) {
                outputDocument.getPages().add(document1.getPages().get_Item(pageNumber));
            }
            if (pageNumber <= document2Pages) {
                outputDocument.getPages().add(document2.getPages().get_Item(pageNumber));
            }
        }

        outputDocument.save(outputFile.toString());
    }
}
```

## دمج المستندات مع الصفحات الفاصلة والإشارات المرجعية

استخدم هذا النمط عندما يظل الملف المدمج سهل التنقل ويظهر بوضوح مكان بدء كل مستند مصدر.

1. قم بإنشاء ملف PDF فارغ [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وافتح كل ملف مصدر على حدة.
1. قم بإضافة فاصل [صفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) مع عنوان، ثم قم بإنشاء إشارة مرجعية [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/) لهذا القسم.
1. قم بإلحاق الصفحات المصدر، وقم بإضافة إشارة مرجعية بشكل اختياري تشير إلى صفحة المحتوى الأولى، ثم احفظ المستند المدمج النهائي.

```java
public static void mergeWithSectionSeparatorsAndBookmarks(List<Path> inputFiles, Path outputFile) {
    try (Document outputDocument = new Document()) {
        int sectionIndex = 1;
        for (Path inputFile : inputFiles) {
            try (Document sourceDocument = new Document(inputFile.toString())) {
                int sourcePageCount = sourceDocument.getPages().size();

                Page separatorPage = outputDocument.getPages().add();
                separatorPage.getParagraphs().add(new TextFragment(
                        "Section " + sectionIndex + ": " + inputFile.getFileName()));

                OutlineItemCollection sectionBookmark = new OutlineItemCollection(outputDocument.getOutlines());
                sectionBookmark.setTitle("Section " + sectionIndex);
                sectionBookmark.setAction(new GoToAction(separatorPage));
                outputDocument.getOutlines().add(sectionBookmark);

                int firstContentPageNumber = outputDocument.getPages().size() + 1;
                appendPageRange(sourceDocument, outputDocument, 1, sourcePageCount);

                if (sourcePageCount > 0 && firstContentPageNumber <= outputDocument.getPages().size()) {
                    OutlineItemCollection contentBookmark = new OutlineItemCollection(outputDocument.getOutlines());
                    contentBookmark.setTitle("Section " + sectionIndex + " Content");
                    contentBookmark.setAction(new GoToAction(outputDocument.getPages().get_Item(firstContentPageNumber)));
                    sectionBookmark.add(contentBookmark);
                }
            }
            sectionIndex++;
        }

        outputDocument.save(outputFile.toString());
    }
}
```
