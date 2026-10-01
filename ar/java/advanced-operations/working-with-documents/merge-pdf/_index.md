---
title: دمج ملفات PDF في Java
linktitle: دمج ملفات PDF
type: docs
weight: 50
url: /ar/java/merge-pdf-documents/
description: تعرّف على كيفية دمج ملفات PDF متعددة في مستند واحد باستخدام Java.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: اجمع المستندات الكاملة، والنطاقات المحددة، والصفحات المتناوبة باستخدام Java
Abstract: تشرح هذه المقالة كيفية دمج مستندات PDF باستخدام Aspose.PDF for Java. وتغطي دمج ملفين، دمج مستندات متعددة، تحديد نطاقات الصفحات، إدراج مستند داخل آخر في موضع محدد، تبديل الصفحات، وبناء مخرجات مدمجة مع إشارات مرجعية للأقسام.
---
يدعم Aspose.PDF for Java عدة استراتيجيات دمج تعتمد على كيفية تجميع المخرجات.

## دمج مستندين PDF

استخدم هذا الأسلوب عندما تحتاج إلى أبسط عملية دمج وتريد إلحاق مستند كامل بآخر.

1. افتح كلا ملفي PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) كائنات.
1. أضف الـ [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) تجميع من المستند الثاني إلى المستند الأول.
1. احفظ ملف PDF المحدث [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void mergeTwoDocuments(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        document1.getPages().add(document2.getPages());
        document1.save(outputFile.toString());
    }
}
```

## نسخ نطاق صفحات محدد بين المستندات

تحتفظ هذه الطريقة المساعدة بمنطق دمج نطاق الصفحات في مكان واحد حتى تتمكن الأمثلة الأخرى من إعادة استخدام روتين النسخ المُتحقق منه نفسه.

1. افتح أو استلم ملف PDF المصدر والوجهة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) كائنات.
1. قُم بتطبيع نطاق الصفحات المطلوب بحيث يبقى ضمن المتاح [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) مجموعة.
1. أضف كل صفحة من النطاق المُتحقق إلى المستند الهدف.

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

استخدم هذا النمط عندما تحتاج إلى دمج قائمة من ملفات الإدخال في مستند إخراج واحد بشكل متتابع.

1. إنشاء ملف PDF فارغ [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. افتح كل ملف إدخال واحدًا في كل مرة وانسخ محتواه بالكامل [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) نطاق إلى مستند الإخراج.
1. احفظ النتيجة المدمجة بعد معالجة جميع ملفات المصدر.

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

## دمج نطاقات الصفحات المحددة من مستندين

هذا المثال ينشئ ملف إخراج مخصص بأخذ نطاقات صفحات محددة فقط من كل مستند مصدر.

1. افتح كلا ملفي PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) الكائنات وإنشاء مستند إخراج جديد.
1. أضف فقط المطلوب [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) نطاقات من كل مستند مصدر.
1. احفظ المستند الناتج المجمع.

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

## إدراج مستند PDF واحد داخل آخر في موضع محدد

استخدم هذا النهج عندما يجب أن يظهر مستند داخل آخر بدلاً من أن يكون فقط قبله أو بعده.

1. افتح ملف PDF الأساسي والملف المدرج [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) الكائنات وإنشاء مستند إخراج جديد.
1. انسخ الجزء الأول من المستند الأساسي، ثم أضف المستند المدخل بالكامل، وأخيرًا أضف الجزء المتبقي من الأساسي [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) النطاق.
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

## دمج مستندي PDF بالتناوب بين الصفحات

هذا المثال يدمج الصفحات من مستندين بشكل متبادل، وهو مفيد عندما ينبغي لكلا المدخلين المساهمة صفحةً بصفحة في النتيجة النهائية.

1. افتح كلا ملفي PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) الكائنات وإنشاء مستند إخراج جديد.
1. قم بالتنقل عبر الحد الأقصى لعدد الصفحات المتاحة وأضف كل صفحة متاحة [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) من المستندين الأول والثاني على التوالي.
1. احفظ مستند الإخراج المتداخل.

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

## دمج المستندات مع صفحات فواصل والإشارات المرجعية

استخدم هذا النمط عندما يجب أن يظل الملف المدمج سهل التنقل ويظهر بوضوح مكان بدء كل مستند مصدر.

1. إنشاء ملف PDF فارغ [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وافتح كل ملف مصدر بالتتابع.
1. إضافة فاصل [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) مع عنوان، ثم أنشئ [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/) إشارة مرجعية لهذا القسم.
1. أرفق الصفحات المصدر، وبشكل اختياري أضف إشارة مرجعية تشير إلى صفحة المحتوى الأولى، ثم احفظ المستند المدمج النهائي.

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
