---
title: إضافة وحذف علامة مرجعية
linktitle: إضافة وحذف علامة مرجعية
type: docs
weight: 10
url: ar/java/add-and-delete-bookmark/
description: يمكنك إضافة علامة مرجعية إلى مستند PDF باستخدام Java. من الممكن حذف جميع العلامات المرجعية أو علامات معينة من مستند PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## إضافة علامة مرجعية إلى مستند PDF

تُحفظ العلامات المرجعية في مجموعة [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection) الخاصة بكائن المستند، نفسها في مجموعة [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection).

لإضافة علامة مرجعية إلى PDF:

1. افتح مستند PDF باستخدام كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
2. قم بإنشاء علامة مرجعية وحدد خصائصها.
3. أضف مجموعة [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection) إلى مجموعة الخطوط العريضة.

يوضح لك مقتطف الشفرة التالي كيفية إضافة علامة مرجعية في مستند PDF.

```java
package com.aspose.pdf.examples;

import java.io.IOException;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.Bookmark;
import com.aspose.pdf.facades.Bookmarks;
import com.aspose.pdf.facades.PdfBookmarkEditor;

public class ExampleBookmarks {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Bookmarks/";

    private static String GetDataDir() {
        String os = System.getProperty("os.name");
        if (os.startsWith("Windows"))
            _dataDir = "C:\\Samples\\Bookmarks\\";
        return _dataDir;
    }

    public static void AddBookmarks() throws IOException {

        Document pdfDocument = new Document(GetDataDir() + "AddBookmark.pdf");

        // إنشاء كائن إشارة مرجعية
        OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.getOutlines());
        pdfOutline.setTitle("اختبار المخطط");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);

        // تعيين رقم صفحة الوجهة
        pdfOutline.setAction(new GoToAction(pdfDocument.getPages().get_Item(2)));

        // إضافة إشارة مرجعية في مجموعة المخطط الخاصة بالوثيقة.
        pdfDocument.getOutlines().add(pdfOutline);

        // حفظ الوثيقة المحدثة
        pdfDocument.save(_dataDir + "AddBookmark_out.pdf");
    }
```


## إضافة إشارة مرجعية فرعية إلى مستند PDF

يمكن أن تكون الإشارات المرجعية متداخلة، مما يشير إلى علاقة هرمية مع إشارات مرجعية رئيسية وفرعية. يشرح هذا المقال كيفية إضافة إشارة مرجعية فرعية، وهي إشارة مرجعية من المستوى الثاني، إلى ملف PDF.

لإضافة إشارة مرجعية فرعية إلى ملف PDF، يجب أولاً إضافة إشارة مرجعية رئيسية:

1. افتح المستند.
2. أضف إشارة مرجعية إلى [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection)، محدداً خصائصها.
3. أضف OutlineItemCollection إلى مجموعة [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) الخاصة بكائن المستند.

يتم إنشاء الإشارة المرجعية الفرعية تمامًا مثل الإشارة المرجعية الرئيسية، كما هو موضح أعلاه، ولكن يتم إضافتها إلى مجموعة الإشارات المرجعية الرئيسية.

توضح الشيفرات البرمجية التالية كيفية إضافة إشارة مرجعية فرعية إلى مستند PDF.

```java
    public static void AddChildBookmark() {
        // افتح المستند
        Document pdfDocument = new Document(GetDataDir() + "AddChildBookmark.pdf");

        // إنشاء كائن إشارة مرجعية رئيسية
        OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.getOutlines());
        pdfOutline.setTitle("Parent Outline");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);

        // إنشاء كائن إشارة مرجعية فرعية
        OutlineItemCollection pdfChildOutline = new OutlineItemCollection(pdfDocument.getOutlines());
        pdfChildOutline.setTitle("Child Outline");
        pdfChildOutline.setItalic(true);
        pdfChildOutline.setBold(true);

        // إضافة الإشارة المرجعية الفرعية إلى مجموعة الإشارات المرجعية الرئيسية
        pdfOutline.add(pdfChildOutline);
        // إضافة الإشارة المرجعية الرئيسية إلى مجموعة الإشارات المرجعية الخاصة بالمستند.
        pdfDocument.getOutlines().add(pdfOutline);

        // حفظ النتيجة
        pdfDocument.save(_dataDir + "AddChildBookmark_out.pdf");
    }
```


## حذف جميع الإشارات المرجعية من مستند PDF

تُحفظ جميع الإشارات المرجعية في ملف PDF في مجموعة [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection). تشرح هذه المقالة كيفية حذف جميع الإشارات المرجعية من ملف PDF.

لحذف جميع الإشارات المرجعية من ملف PDF:

1. قم باستدعاء طريقة الحذف لمجموعة [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection).
2. احفظ الملف المعدل باستخدام طريقة الحفظ لكائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

توضح مقاطع الشيفرة التالية كيفية حذف جميع الإشارات المرجعية من مستند PDF.

```java
    public static void DeleteAllBookmarksFromPDFDocument() {
        // افتح المستند
        Document pdfDocument = new Document(GetDataDir() + "DeleteAllBookmarks.pdf");

        // احذف جميع الإشارات المرجعية
        pdfDocument.getOutlines().delete();

        // احفظ الملف المحدث
        pdfDocument.save(_dataDir + "DeleteAllBookmarks_out.pdf");
    }
```

## حذف إشارة مرجعية معينة من مستند PDF

[حذف جميع المرفقات من مستند PDF](https://docs.aspose.com/pdf/java/working-with-attachments/) أظهر كيفية حذف جميع المرفقات من ملف PDF. من الممكن أيضًا إزالة مرفقات محددة فقط.

لحذف إشارة مرجعية معينة من ملف PDF:

1. مرر عنوان الإشارة المرجعية كمعامل إلى طريقة [Delete](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection#delete--) لمجموعة [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection).
2. ثم احفظ الملف المحدث باستخدام طريقة Save لكائن Document.

توفر فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) مجموعة [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection). تقوم طريقة [Delete](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection#delete--) بإزالة أي إشارة مرجعية بالعنوان المُمرّر للطريقة.

تُظهر مقتطفات الشيفرة التالية كيفية حذف إشارة مرجعية معينة من مستند PDF.

```java
    public static void DeleteParticularBookmarkPDFDocument() {
        // افتح المستند
        Document pdfDocument = new Document(GetDataDir() + "DeleteParticularBookmark.pdf");

        // حذف العنوان المحدد بواسطة العنوان
        pdfDocument.getOutlines().delete("Child Outline");

        // حفظ الملف المحدث
        pdfDocument.save(_dataDir + "DeleteParticularBookmark_out.pdf");
    }
```