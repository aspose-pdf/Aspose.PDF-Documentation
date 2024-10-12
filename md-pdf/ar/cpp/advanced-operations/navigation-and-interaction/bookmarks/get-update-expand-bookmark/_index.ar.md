---
title: احصل على إشارة مرجعية، قم بتحديثها وقم بتوسيعها
linktitle: احصل على إشارة مرجعية، قم بتحديثها وقم بتوسيعها
type: docs
weight: 20
url: /cpp/get-update-and-expand-bookmark/
description: مكتبة Aspose.PDF لـ C++ تتيح لك الحصول على تحديث في ملف PDF لدينا.
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## الحصول على الإشارات المرجعية

تحتوي مجموعة [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection) الخاصة بكائن [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) على جميع الإشارات المرجعية لملف PDF. يشرح هذا المقال كيفية الحصول على الإشارات المرجعية من ملف PDF، وكيفية معرفة أي صفحة تكون الإشارة المرجعية عليها.

للحصول على الإشارات المرجعية، قم بالتكرار خلال مجموعة [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection) واحصل على كل إشارة مرجعية في مجموعة OutlineItemCollection. The OutlineItemCollection توفر الوصول إلى جميع سمات العلامة المرجعية. يوضح لك مقتطف الشيفرة التالي كيفية الحصول على العلامات المرجعية من ملف PDF.

```cpp
void GettingBookmarks() {

String _dataDir("C:\\Samples\\Bookmarks\\");

// افتح المستند

auto pdfDocument = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");

// قم بالتكرار عبر جميع العلامات المرجعية

for (auto outlineItem : pdfDocument->get_Outlines()) {


Console::WriteLine(u"العنوان :- " + outlineItem->get_Title());


Console::WriteLine(u"مائل :- " + outlineItem->get_Italic());


Console::WriteLine(u"عريض :- " + outlineItem->get_Bold());


Console::WriteLine(u"اللون :- {0}", outlineItem->get_Color());

}
}
```

## الحصول على رقم صفحة العلامة المرجعية

بمجرد إضافة علامة مرجعية يمكنك معرفة الصفحة التي توجد بها عن طريق الحصول على رقم الصفحة المرتبطة بجسم العلامة المرجعية.

```cpp
void GettingBookmarksPageNumber() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// إنشاء PdfBookmarkEditor

auto bookmarkEditor = MakeObject<Aspose::Pdf::Facades::PdfBookmarkEditor>();

// فتح ملف PDF

bookmarkEditor->BindPdf(_dataDir + u"UpdateBookmarks.pdf");

// استخراج العلامات المرجعية

auto bookmarks = bookmarkEditor->ExtractBookmarks();

for (auto bookmark : bookmarks) {


String strLevelSeprator("");


for (int i = 1; i < bookmark->get_Level(); i++) {



strLevelSeprator += u"---- ";


}


Console::WriteLine(u"العنوان :- " + strLevelSeprator + bookmark->get_Title());


Console::WriteLine(u"رقم الصفحة :- " + strLevelSeprator + bookmark->get_PageNumber());


Console::WriteLine(u"إجراء الصفحة :- " + strLevelSeprator + bookmark->get_Action());

}
}
```
## تحديث العلامات المرجعية في مستند PDF

لتحديث علامة مرجعية في ملف PDF، أولاً، احصل على العلامة المرجعية المحددة من مجموعة OutlineColletion لكائن Document عن طريق تحديد فهرس العلامة المرجعية. بمجرد استرجاع العلامة المرجعية في كائن [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection)، يمكنك تحديث خصائصها ثم حفظ ملف PDF المحدث باستخدام طريقة Save. توضح مقاطع الشيفرة التالية كيفية تحديث العلامات المرجعية في مستند PDF.

```cpp
void UpdateBookmarksInPDFDocument() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// فتح المستند

auto pdfDocument = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");

// احصل على كائن العلامة المرجعية

auto pdfOutline = pdfDocument->get_Outlines()->idx_get(1);


// تحديث كائن العلامة المرجعية

pdfOutline->set_Title(u"Updated Outline");

pdfOutline->set_Italic(true);

pdfOutline->set_Bold(true);

// تعيين الصفحة المستهدفة كصفحة 2

pdfOutline->set_Destination(MakeObject<Aspose::Pdf::Annotations::GoToAction>(pdfDocument->get_Pages()->idx_get(2)));


// حفظ الناتج

pdfDocument->Save(_dataDir + u"Bookmarkupdated_output.pdf");
}
```

## تحديث الإشارات المرجعية الفرعية في مستند PDF

لتحديث إشارة مرجعية فرعية:

1. استرجع الإشارة المرجعية الفرعية التي ترغب في تحديثها من ملف PDF من خلال الحصول أولاً على الإشارة المرجعية الرئيسية ثم الإشارة المرجعية الفرعية باستخدام القيم المناسبة للفهرس.
2. احفظ الملف المحدث باستخدام طريقة الحفظ.

{{% alert color="primary" %}}

احصل على إشارة مرجعية من مجموعة OutlineCollection لكائن المستند عن طريق تحديد فهرس الإشارة المرجعية، ثم احصل على الإشارة المرجعية الفرعية عن طريق تحديد فهرس هذه الإشارة المرجعية الرئيسية.

{{% /alert %}}

يوضح لك مقطع الشيفرة التالي كيفية تحديث الإشارات المرجعية الفرعية في مستند PDF.

```cpp
void UpdateChildBookmarksInPDFDocument() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// افتح المستند

auto pdfDocument = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");

// احصل على كائن الإشارة المرجعية

auto pdfOutline = pdfDocument->get_Outlines()->idx_get(1);

// احصل على كائن الإشارة المرجعية الفرعية

auto childOutline = pdfOutline->idx_get(1);


// قم بتحديث كائن الإشارة المرجعية

childOutline->set_Title(u"Updated Outline");

childOutline->set_Italic(true);

childOutline->set_Bold(true);

// حدد الصفحة المستهدفة كصفحة 2

childOutline->set_Destination(MakeObject<Aspose::Pdf::Annotations::GoToAction>(pdfDocument->get_Pages()->idx_get(2)));


// احفظ الناتج

pdfDocument->Save(_dataDir + u"Bookmarkupdated_output.pdf");
}
```

## الإشارات المرجعية الموسعة عند عرض المستند

تُحفظ الإشارات المرجعية في مجموعة [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection) الخاصة بكائن المستند، وهي نفسها في مجموعة [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection). ومع ذلك، قد نحتاج إلى أن تكون جميع الإشارات المرجعية موسعة عند عرض ملف PDF.

من أجل تحقيق هذا المتطلب، يمكننا تعيين حالة الفتح لكل عنصر مخطط/إشارة مرجعية كـ Open. يوضح المقتطف البرمجي التالي كيفية تعيين حالة الفتح لكل إشارة مرجعية كموسعة في مستند PDF.

```cpp
void ExpandedBookmarks() {

String _dataDir("C:\\Samples\\Bookmarks\\");

auto doc = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");

// تعيين وضع عرض الصفحة أي عرض الصور المصغرة، ملء الشاشة، عرض لوحة المرفقات

doc->set_PageMode(PageMode::UseOutlines);

// طباعة العدد الإجمالي للإشارات المرجعية في ملف PDF

Console::WriteLine(doc->get_Outlines()->get_Count());

// الانتقال عبر كل عنصر مخطط في مجموعة المخططات لملف PDF

for (int counter = 1; counter <= doc->get_Outlines()->get_Count(); counter++) {

// تعيين حالة الفتح لعنصر المخطط

doc->get_Outlines()->idx_get(counter)->set_Open(true);

}

// حفظ ملف PDF

doc->Save(_dataDir + u"Bookmarks_Expanded.pdf");
}
```