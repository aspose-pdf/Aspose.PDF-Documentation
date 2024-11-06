---
title: ملء AcroForm
linktitle: ملء AcroForm
type: docs
weight: 20
url: ar/cpp/fill-form/
description: يشرح هذا القسم كيفية ملء حقل نموذج في مستند PDF باستخدام Aspose.PDF لـ C++.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

تُعد مستندات PDF الأفضل، ونوع الملفات المفضل حقًا، لإنشاء النماذج.

يشرح هذا الموضوع كيفية ملء نماذج PDF باستخدام Aspose.PDF لـ C++.

يتيح لك Aspose.PDF لـ C++ ملء حقل نموذج، والحصول على الحقل من مجموعة النموذج لكائن المستند.

دعونا ننظر إلى المثال التالي لكيفية حل هذه المهمة:

```cpp
using namespace System;
using namespace Aspose::Pdf;

void FillAcroform()
{
    String _dataDir("C:\\Samples\\");

    // افتح المستند
    auto document = MakeObject<Document>(_dataDir + u"FillFormField.pdf");

    // احصل على الحقل
    auto textBoxField = System::DynamicCast<Aspose::Pdf::Forms::TextBoxField>(document->get_Form()->idx_get(u"textbox1"));

    // تعديل قيمة الحقل
    textBoxField->set_Value(u"القيمة المراد تعبئتها في الحقل");

    // حفظ المستند المحدث
    document->Save(_dataDir + u"FillFormField_out.pdf");

}
```