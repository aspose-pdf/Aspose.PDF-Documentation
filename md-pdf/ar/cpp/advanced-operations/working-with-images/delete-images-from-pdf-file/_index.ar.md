---
title: حذف الصور من ملف PDF باستخدام C++
linktitle: حذف الصور
type: docs
weight: 20
url: /cpp/delete-images-from-pdf-file/
description: يشرح هذا القسم كيفية حذف الصور من ملف PDF باستخدام Aspose.PDF لـ C++.
lastmod: "2021-12-18"
---

لحذف صورة من ملف PDF:

1. قم بإنشاء كائن [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) وافتح ملف PDF المدخل.
1. احصل على الصفحة التي تحتوي على الصورة من مجموعة الصفحات [Pages collection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) لكائن Document.
1. يتم الاحتفاظ بالصور في مجموعة الصور، الموجودة في مجموعة الموارد الخاصة بالصفحة.
1. احذف صورة باستخدام طريقة الحذف لمجموعة الصور.
1. احفظ الناتج باستخدام طريقة الحفظ لكائن Document.

يظهر مقطع الشيفرة التالي كيفية حذف صورة من ملف PDF.

```cpp
void WorkingWithImages::DeleteImagesFromPDFFile()
{
    String _dataDir("C:\\Samples\\");

    // افتح المستند
    auto document = MakeObject<Document>(_dataDir + u"DeleteImages.pdf");

    // احذف صورة معينة
    document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->Delete(1);

    // احفظ ملف PDF المحدث
    document->Save(_dataDir + u"DeleteImages_out.pdf");
}
```