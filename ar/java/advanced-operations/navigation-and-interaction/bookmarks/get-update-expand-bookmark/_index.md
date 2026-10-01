---
title: الحصول على إشارات PDF وتحديثها وتوسيعها في Java
linktitle: الحصول على إشارة وتحديثها وتوسيعها
type: docs
weight: 20
url: /ar/java/get-update-and-expand-bookmark/
description: تعلم كيفية استرجاع وتحديث وتوسيع الإشارات في مستندات PDF باستخدام Java.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: افحص خصائص الإشارة وقم بتوسيع المخطط التفصيلي في ملفات PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية قراءة وتحديث وتوسيع العلامات المرجعية باستخدام Aspose.PDF for Java. وتغطي التكرار عبر عناصر المخطط، استخراج أرقام صفحات العلامات المرجعية باستخدام PdfBookmarkEditor، قراءة العلامات المرجعية الفرعية، تحديث عناوين العلامات المرجعية وتنسيقها، وإجبار المخططات على الفتح عند عرض المستند.
---
Aspose.PDF for Java يتيح الإشارات المرجعية من خلال كلٍ من نموذج مخطط المستند و `PdfBookmarkEditor` واجهة.

## احصل على خصائص العلامة المرجعية

استخدم هذا المثال عندما تحتاج إلى فحص إدخالات العلامات المرجعية المستوى العلوي في مخطط المستند.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. التنقل عبر مجموعة المخططات.
1. قراءة وطباعة عنوان الإشارة المرجعية، والنمط، وقيم اللون.

```java
public static void getBookmarks(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getOutlines().size(); i++) {
            OutlineItemCollection outlineItem = document.getOutlines().get_Item(i);
            System.out.println(outlineItem.getTitle());
            System.out.println(outlineItem.getItalic());
            System.out.println(outlineItem.getBold());
            System.out.println(outlineItem.getColor());
        }
    }
}
```

## احصل على أرقام صفحات العلامات المرجعية

هذا المثال يستخدم `PdfBookmarkEditor` لاستخراج عناوين الإشارات المرجعية، المستويات، أرقام الصفحات، والإجراءات.

1. ربط ملف PDF المصدر بـ [PdfBookmarkEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdfbookmarkeditor/).
1. استخرج مجموعة العلامات المرجعية وتكرّر عبرها.
1. اطبع المستوى والعنوان ورقم الصفحة ومعلومات الإجراء لكل علامة مرجعية.

```java
public static void getBookmarkPageNumber(Path inputFile) {
    PdfBookmarkEditor bookmarkEditor = new PdfBookmarkEditor();
    try {
        bookmarkEditor.bindPdf(inputFile.toString());
        for (Bookmark bookmark : bookmarkEditor.extractBookmarks()) {
            String levelSeparator = "";
            for (int i = 0; i < bookmark.getLevel(); i++) {
                levelSeparator += "----";
            }

            System.out.println(levelSeparator + " Title: " + bookmark.getTitle());
            System.out.println(levelSeparator + " Page Number: " + bookmark.getPageNumber());
            System.out.println(levelSeparator + " Page Action: " + bookmark.getAction());
        }
    } finally {
        bookmarkEditor.close();
    }
}
```

## احصل على العلامات المرجعية الفرعية

استخدم هذا المثال عندما تحتاج إلى فحص كل من عناصر المخطط ذات المستوى الأعلى والعناصر المتداخلة

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. تكرار عبر المخططات ذات المستوى الأعلى وطباعة خصائصها
1. اكتشف العلامات المرجعية الفرعية، ثم تكرار عبرها وطباعة خصائصها

```java
public static void getChildBookmarks(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getOutlines().size(); i++) {
            OutlineItemCollection outlineItem = document.getOutlines().get_Item(i);
            System.out.println(outlineItem.getTitle());
            System.out.println(outlineItem.getItalic());
            System.out.println(outlineItem.getBold());
            System.out.println(outlineItem.getColor());
            int count = outlineItem.size();
            if (count > 0) {
                System.out.println("Child Bookmarks");
                for (int j = 1; j <= outlineItem.size(); j++) {
                    OutlineItemCollection childOutlineItem = outlineItem.get_Item(j);
                    System.out.println(childOutlineItem.getTitle());
                    System.out.println(childOutlineItem.getItalic());
                    System.out.println(childOutlineItem.getBold());
                    System.out.println(childOutlineItem.getColor());
                }
            }
        }
    }
}
```

## تحديث الإشارات المرجعية

استخدم هذا المثال عندما يجب تعديل عنوان الإشارة المرجعية الحالية والنمط.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. الوصول إلى عنصر المخطط المستهدف وعلامة مرجعية فرعية.
1. قم بتحديث خصائص العلامة المرجعية واحفظ المستند.

```java
public static void updateBookmarks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        OutlineItemCollection outline = document.getOutlines().get_Item(1);
        OutlineItemCollection childOutline = outline.get_Item(1);
        childOutline.setTitle("Updated Outline");
        childOutline.setItalic(true);
        childOutline.setBold(true);

        document.save(outputFile.toString());
    }
}
```

## توسيع الإشارات المرجعية افتراضيًا

استخدم هذا المثال عندما يجب أن تُفتح لوحة الإشارات المرجعية وتظهر عناصر المخطط الموسَّعة عند عرض المستند.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اضبط وضع الصفحة لاستخدام المخططات وعَلِّم كل عنصر مخطط بأنه مفتوح.
1. احفظ المستند المحدث.

```java
public static void expandedBookmarks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.setPageMode(PageMode.UseOutlines);
        for (int i = 1; i <= document.getOutlines().size(); i++) {
            OutlineItemCollection item = document.getOutlines().get_Item(i);
            item.setOpen(true);
        }
        document.save(outputFile.toString());
    }
}
```
