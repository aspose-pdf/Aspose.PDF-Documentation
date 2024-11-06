---
title: استبدال الصورة في ملف PDF موجود باستخدام C++
linktitle: استبدال الصورة
type: docs
weight: 70
url: ar/cpp/replace-image-in-existing-pdf-file/
description: يصف هذا القسم كيفية استبدال الصورة في ملف PDF موجود باستخدام مكتبة ++.
lastmod: "2021-12-18"
---

تسمح لك طريقة الاستبدال في مجموعة الصور باستبدال صورة في ملف PDF موجود.

يمكن العثور على مجموعة الصور في مجموعة الموارد لصفحة معينة. لاستبدال صورة:

1. افتح ملف PDF باستخدام كائن المستند.
2. استبدل صورة معينة، واحفظ ملف PDF المحدث باستخدام طريقة الحفظ لكائن المستند.

يوضح لك مقطع الشفرة التالي كيفية استبدال صورة في ملف PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ReplaceImage() {
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"input.pdf");
    // Replace a particular image
    document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->Replace(1, System::IO::File::OpenRead(u"lovely.jpg"));
    // Save updated PDF file
    document->Save(_dataDir + u"output.pdf");
}
```