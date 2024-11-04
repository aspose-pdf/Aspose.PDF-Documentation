---
title: إضافة وإزالة إشارة مرجعية
linktitle: إضافة وإزالة إشارة مرجعية
type: docs
weight: 10
url: /cpp/add-and-delete-bookmark/
description: يشرح هذا الموضوع كيفية إضافة إشارة مرجعية إلى مستند PDF باستخدام مكتبة C++. كما يمكنك حذف جميع الإشارات المرجعية أو إشارة مرجعية معينة من مستند PDF.
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## إضافة إشارة مرجعية إلى مستند PDF

تُحتفظ الإشارات المرجعية في مجموعة [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection/) الخاصة بكائن المستند، وهي نفسها في مجموعة [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/).

لإضافة إشارة مرجعية إلى PDF:

1. افتح مستند PDF باستخدام كائن [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/).
1. قم بإنشاء إشارة مرجعية وقم بتحديد خصائصها.
1. أضف مجموعة [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/) إلى مجموعة المخططات.

يوضح لك المقتطف البرمجي التالي كيفية إضافة إشارة مرجعية في مستند PDF.

```cpp
void AddBookmarks() {

String _dataDir("C:\\Samples\\Bookmarks\\");

auto pdfDocument = MakeObject<Document>(_dataDir + u"AddBookmark.pdf");

// أنشئ كائن إشارة مرجعية

auto pdfOutline = MakeObject<OutlineItemCollection>(pdfDocument->get_Outlines());

pdfOutline->set_Title(u"Test Outline");

pdfOutline->set_Italic(true);

pdfOutline->set_Bold(true);

// تعيين رقم صفحة الوجهة

pdfOutline->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToAction>(pdfDocument->get_Pages()->idx_get(2)));

// أضف إشارة مرجعية في مجموعة المخططات للمستند.

pdfDocument->get_Outlines()->Add(pdfOutline);

// احفظ المستند المحدث

pdfDocument->Save(_dataDir + u"AddBookmark_out.pdf");
}
```

## إضافة إشارة مرجعية فرعية إلى مستند PDF

يمكن أن تكون الإشارات المرجعية متداخلة، مما يشير إلى علاقة هرمية مع الإشارات المرجعية الأم والفرعية. 
تشرح هذه المقالة كيفية إضافة إشارة مرجعية فرعية، أي إشارة مرجعية من المستوى الثاني، إلى ملف PDF.

لإضافة إشارة مرجعية فرعية إلى ملف PDF، يجب أولاً إضافة إشارة مرجعية رئيسية:

1. افتح مستندًا.
1. أضف إشارة مرجعية إلى [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection/)، مع تحديد خصائصها.
1. أضف OutlineItemCollection إلى مجموعة [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/) الخاصة بكائن المستند.

يتم إنشاء الإشارة المرجعية الفرعية تمامًا مثل الإشارة المرجعية الرئيسية، الموضحة أعلاه، ولكن تتم إضافتها إلى مجموعة الإشارات المرجعية الخاصة بالإشارة المرجعية الرئيسية.

توضح الشيفرات البرمجية التالية كيفية إضافة إشارة مرجعية فرعية إلى مستند PDF.

```cpp
void AddChildBookmark() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// Open document

auto pdfDocument = MakeObject<Document>(_dataDir + u"AddChildBookmark.pdf");


// Create a parent bookmark object

auto pdfOutline = MakeObject<OutlineItemCollection>(pdfDocument->get_Outlines());

pdfOutline->set_Title(u"Parent Outline");

pdfOutline->set_Italic(true);

pdfOutline->set_Bold(true);


// Create a child bookmark object

auto pdfChildOutline = MakeObject<OutlineItemCollection>(pdfDocument->get_Outlines());

pdfChildOutline->set_Title(u"Child Outline");

pdfChildOutline->set_Italic(true);

pdfChildOutline->set_Bold(true);


// Add child bookmark in parent bookmark's collection

pdfOutline->Add(pdfChildOutline);

// Add parent bookmark in the document's outline collection.

pdfDocument->get_Outlines()->Add(pdfOutline);


// Save output

pdfDocument->Save(_dataDir + u"AddChildBookmark_out.pdf");
}
```
```
## حذف جميع الإشارات المرجعية من مستند PDF

جميع الإشارات المرجعية في PDF محفوظة في مجموعة [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/). تشرح هذه المقالة كيفية حذف جميع الإشارات المرجعية من ملف PDF.

لحذف جميع الإشارات المرجعية من ملف PDF:

1. استدعاء طريقة الحذف لمجموعة [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/).
1. احفظ الملف المعدل باستخدام طريقة الحفظ لكائن [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/).

تُظهر مقتطفات الشيفرة التالية كيفية حذف جميع الإشارات المرجعية من مستند PDF.

```cpp
void DeleteAllBookmarksFromPDFDocument() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// فتح المستند

auto pdfDocument = MakeObject<Document>(_dataDir + u"DeleteAllBookmarks.pdf");


// حذف جميع الإشارات المرجعية

pdfDocument->get_Outlines()->Delete();


// حفظ الملف المحدث

pdfDocument->Save(_dataDir + u"DeleteAllBookmarks_out.pdf");
}
```

## حذف إشارة مرجعية معينة من مستند PDF

[حذف جميع المرفقات من مستند PDF](https://docs.aspose.com/pdf/cpp/working-with-attachments/) أظهر كيفية حذف جميع المرفقات من ملف PDF. من الممكن أيضًا إزالة مرفقات معينة فقط.

لحذف إشارة مرجعية معينة من ملف PDF:

1. مرر عنوان الإشارة المرجعية كمعامل إلى طريقة الحذف في مجموعة [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/).
2. ثم احفظ الملف المحدث باستخدام طريقة الحفظ لكائن المستند.

يوفر فئة [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) مجموعة [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/). تزيل طريقة [Delete](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection#a04f36a1f4f7c4fde3189399eb046a98b) أي إشارة مرجعية بالعنوان الممرر إلى الطريقة.

تظهر مقتطفات الشيفرة التالية كيفية حذف إشارة مرجعية معينة من مستند PDF.

```cpp
void DeleteParticularBookmarkPDFDocument() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// فتح المستند

auto pdfDocument = MakeObject<Document>(_dataDir + u"DeleteParticularBookmark.pdf");


// حذف إشارة مرجعية معينة بواسطة العنوان

pdfDocument->get_Outlines()->Delete(u"Child Outline");


// حفظ الملف المحدث

pdfDocument->Save(_dataDir + u"DeleteParticularBookmark_out.pdf");
}
```