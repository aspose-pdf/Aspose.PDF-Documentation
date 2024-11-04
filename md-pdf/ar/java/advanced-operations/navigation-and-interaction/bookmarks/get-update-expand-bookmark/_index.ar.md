---
title: Get, Update and Expand a Bookmark 
linktitle: Get, Update and Expand a Bookmark
type: docs
weight: 20
url: /java/get-update-and-expand-bookmark/
description: يصف هذا المقال كيفية استخدام العلامات المرجعية في ملف PDF. باستخدام مكتبتنا لـ Java، يمكنك الحصول على العلامات المرجعية من ملف PDF، والحصول على رقم صفحة العلامات المرجعية، وتحديث العلامات المرجعية في مستند PDF، وتوسيع العلامات المرجعية عند عرض مستند.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Get Bookmarks

تحتوي مجموعة [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) الخاصة بكائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) على جميع العلامات المرجعية لملف PDF. يشرح هذا المقال كيفية الحصول على العلامات المرجعية من ملف PDF، وكيفية معرفة الصفحة التي توجد عليها علامة مرجعية معينة.

للحصول على العلامات المرجعية، قم بالتكرار عبر مجموعة [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) واحصل على كل علامة مرجعية في OutlineItemCollection.
 The OutlineItemCollection provides access to all the bookmark's attributes. The following code snippet shows you how to get bookmarks from the PDF file.

```java
    public static void GettingBookmarks() {
        // افتح المستند
        Document pdfDocument = new Document(GetDataDir() + "UpdateBookmarks.pdf");
        // حلقة لجميع الإشارات المرجعية
        for (OutlineItemCollection outlineItem : (Iterable<OutlineItemCollection>) pdfDocument.getOutlines()) {
            System.out.println("العنوان :- " + outlineItem.getTitle());
            System.out.println("مائل :- " + outlineItem.getItalic());
            System.out.println("عريض :- " + outlineItem.getBold());
            System.out.println("اللون :- " + outlineItem.getColor());
        }
    }
```

## Getting a Bookmark's Page Number

Once you have added a bookmark you can find out what page it is on by getting the destination PageNumber associated with the Bookmark object.

```java
    public static void GettingBookmarksPageNumber() {
        // أنشئ PdfBookmarkEditor
        PdfBookmarkEditor bookmarkEditor = new PdfBookmarkEditor();
        // افتح ملف PDF
        bookmarkEditor.bindPdf(GetDataDir() + "UpdateBookmarks.pdf");
        // استخراج الإشارات المرجعية
        Bookmarks bookmarks = bookmarkEditor.extractBookmarks();
        for (Bookmark bookmark : (Iterable<Bookmark>) bookmarks) {
            String strLevelSeprator = "";
            for (int i = 1; i < bookmark.getLevel(); i++) {
                strLevelSeprator += "---- ";
            }
            System.out.println("العنوان :- " + strLevelSeprator + bookmark.getTitle());
            System.out.println("رقم الصفحة :- " + strLevelSeprator + bookmark.getPageNumber());
            System.out.println("الإجراء على الصفحة :- " + strLevelSeprator + bookmark.getAction());
        }
    }
```

## تحديث الإشارات المرجعية في مستند PDF

لتحديث إشارة مرجعية في ملف PDF، أولاً، قم بالحصول على الإشارة المرجعية المحددة من مجموعة OutlineColletion الخاصة بكائن المستند عن طريق تحديد فهرس الإشارة المرجعية. بمجرد استرجاع الإشارة المرجعية إلى كائن [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection)، يمكنك تحديث خصائصها ثم حفظ ملف PDF المحدث باستخدام طريقة Save. تعرض مقتطفات الشيفرة التالية كيفية تحديث الإشارات المرجعية في مستند PDF.

```java
    public static void UpdateBookmarksInPDFDocument() {
        // فتح المستند
        Document pdfDocument = new Document(GetDataDir() + "UpdateBookmarks.pdf");
        // الحصول على كائن الإشارة المرجعية
        OutlineItemCollection pdfOutline = pdfDocument.getOutlines().get_Item(1);

        // تحديث كائن الإشارة المرجعية
        pdfOutline.setTitle("Updated Outline");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);
        // تعيين الصفحة المستهدفة كصفحة 2
        pdfOutline.setDestination(new GoToAction(pdfDocument.getPages().get_Item(2)));

        // حفظ الناتج
        pdfDocument.save(GetDataDir() + "Bookmarkupdated_output.pdf");
    }
```


## تحديث العلامات المرجعية الفرعية في مستند PDF

لتحديث علامة مرجعية فرعية:

1. استرجع العلامة المرجعية الفرعية التي تريد تحديثها من ملف PDF عن طريق الحصول أولاً على العلامة المرجعية الأصلية ثم العلامة المرجعية الفرعية باستخدام القيم المناسبة للفهرس.
2. احفظ ملف PDF المحدث باستخدام طريقة الحفظ.

{{% alert color="primary" %}}

احصل على علامة مرجعية من مجموعة OutlineCollection لكائن Document عن طريق تحديد فهرس العلامة المرجعية، ثم احصل على العلامة المرجعية الفرعية بتحديد فهرس هذه العلامة المرجعية الأصلية.

{{% /alert %}}

يوضح لك مقطع الشيفرة التالي كيفية تحديث العلامات المرجعية الفرعية في مستند PDF.

```java
    public static void UpdateChildBookmarksInPDFDocument() {
        // افتح المستند
        Document pdfDocument = new Document(GetDataDir() + "UpdateBookmarks.pdf");
        // احصل على كائن العلامة المرجعية
        OutlineItemCollection pdfOutline = pdfDocument.getOutlines().get_Item(1);
        // احصل على كائن العلامة المرجعية الفرعية
        OutlineItemCollection childOutline = pdfOutline.get_Item(1);

        // قم بتحديث كائن العلامة المرجعية
        childOutline.setTitle("Updated Outline");
        childOutline.setItalic(true);
        childOutline.setBold(true);
        // قم بتعيين الصفحة المستهدفة كصفحة 2
        childOutline.setDestination(new GoToAction(pdfDocument.getPages().get_Item(2)));

        // احفظ المخرجات
        pdfDocument.save(GetDataDir() + "Bookmarkupdated_output.pdf");
    }
```


## العلامات المرجعية الموسعة عند عرض المستند

تُحفظ العلامات المرجعية في مجموعة [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection) الخاصة بكائن الوثيقة، والتي تكون بدورها في مجموعة [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection). ومع ذلك، قد يكون لدينا متطلب لعرض جميع العلامات المرجعية بشكل موسع عند عرض ملف PDF.

لتحقيق هذا المتطلب، يمكننا تعيين حالة الفتح لكل عنصر/علامة مرجعية كـ Open. يوضح لك مقتطف الكود التالي كيفية تعيين حالة الفتح لكل علامة مرجعية كـ موسعة في مستند PDF.

```java
    public static void ExpandedBookmarks() {    
        Document doc = new Document(GetDataDir()+"UpdateBookmarks.pdf");
        // تعيين وضع عرض الصفحة أي إظهار الصور المصغرة، ملء الشاشة، إظهار لوحة المرفقات
        doc.setPageMode(PageMode.UseOutlines);
        // طباعة العدد الإجمالي للعلامات المرجعية في ملف PDF
        System.out.println(doc.getOutlines().size());
        // التنقل عبر كل عنصر علامة مرجعية في مجموعة العلامات المرجعية لملف PDF
        for (int counter = 1; counter <= doc.getOutlines().size(); counter++) {
            // تعيين حالة الفتح لعنصر العلامة المرجعية
            doc.getOutlines().get_Item(counter).setOpen(true);
        }
        // حفظ ملف PDF
        doc.save(_dataDir+"Bookmarks_Expanded.pdf");
    }
```