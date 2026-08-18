---
title: احصل على إشارات PDF المرجعية وتحديثها وتوسيعها في Java
linktitle: الحصول على إشارة مرجعية وتحديثها وتوسيعها
type: docs
weight: 20
url: /java/get-update-and-expand-bookmark/
description: تعرف على كيفية استرداد الإشارات المرجعية وتحديثها وتوسيعها في مستندات PDF باستخدام Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: فحص خصائص الإشارة المرجعية وتوسيع الخطوط العريضة في ملفات PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية قراءة الإشارات المرجعية وتحديثها وتوسيعها باستخدام Aspose.PDF لـ Java. وهو يغطي التكرار من خلال عناصر المخطط التفصيلي، واستخراج أرقام صفحات الإشارات المرجعية باستخدام PdfBookmarkEditor، وقراءة الإشارات المرجعية الفرعية، وتحديث عناوين الإشارات المرجعية ونمطها، وإجبار الخطوط العريضة على الفتح عند عرض المستند.
---
يعرض Aspose.PDF لـ Java الإشارات المرجعية من خلال كل من نموذج المخطط التفصيلي للمستند والواجهة `PdfBookmarkEditor`.

## الحصول على خصائص المرجعية

استخدم هذا المثال عندما تحتاج إلى فحص إدخالات الإشارة المرجعية ذات المستوى الأعلى في المخطط التفصيلي للمستند.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. التكرار من خلال مجموعة الخطوط العريضة.
1. اقرأ واطبع عنوان الإشارة المرجعية ونمطها وقيم الألوان.

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

## الحصول على أرقام الصفحات المرجعية

يستخدم هذا المثال `PdfBookmarkEditor` لاستخراج عناوين الإشارات المرجعية والمستويات وأرقام الصفحات والإجراءات.

1. قم بربط ملف PDF المصدر بـ [PdfBookmarkEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdfbookmarkeditor/).
1. قم باستخراج مجموعة الإشارات المرجعية وكررها.
1. اطبع المستوى والعنوان ورقم الصفحة ومعلومات الإجراء لكل إشارة مرجعية.

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

## الحصول على الإشارات المرجعية للأطفال

استخدم هذا المثال عندما تحتاج إلى فحص عناصر المخطط التفصيلي ذات المستوى الأعلى والمتداخلة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بالتكرار من خلال الخطوط العريضة للمستوى الأعلى وطباعة خصائصها.
1. اكتشاف الإشارات المرجعية الفرعية، ثم تكرارها وطباعة خصائصها.

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

استخدم هذا المثال عندما يجب تعديل عنوان ونمط الإشارة المرجعية الموجودة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بالوصول إلى عنصر المخطط التفصيلي الهدف والإشارة المرجعية التابعة له.
1. قم بتحديث خصائص الإشارة المرجعية واحفظ المستند.

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

## قم بتوسيع الإشارات المرجعية بشكل افتراضي

استخدم هذا المثال عندما يجب أن تفتح لوحة الإشارات المرجعية وتعرض عناصر المخطط التفصيلي الموسعة عند عرض المستند.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بتعيين وضع الصفحة لاستخدام المخططات التفصيلية ووضع علامة على كل عنصر مخطط تفصيلي على أنه مفتوح.
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
