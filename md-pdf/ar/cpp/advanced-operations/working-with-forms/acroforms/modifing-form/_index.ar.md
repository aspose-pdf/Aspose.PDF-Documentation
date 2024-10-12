---
title: تعديل AcroForm
linktitle: تعديل AcroForm
type: docs
weight: 40
url: /cpp/modifing-form/
description: تعديل النموذج في ملف PDF الخاص بك باستخدام مكتبة Aspose.PDF لـ C++. يمكنك إضافة أو إزالة الحقول في النموذج الموجود، والحصول على الحد من الحقل وتعيينه وما إلى ذلك.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## الحصول على أو تعيين حد الحقل

تسمح لك طريقة SetFieldLimit(field, limit) في فئة FormEditor بتعيين حد للحقل، وهو الحد الأقصى لعدد الأحرف التي يمكن إدخالها في حقل.

```cpp
void SetFieldLimitDom() {
    String _dataDir("C:\\Samples\\");
    // افتح المستند
    auto document = MakeObject<Document>(_dataDir + u"GetValuesFromAllFields.pdf");
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));
    textBoxField->set_MaxLen(15);
    document->Save(_dataDir + u"GetValuesFromAllFields.pdf");
}
```

وبالمثل، تمتلك Aspose.PDF طريقة تحصل على حد الحقل باستخدام نهج DOM. النص البرمجي التالي يوضح الخطوات.

```cpp
void GetFieldLimitDom() {
    String _dataDir("C:\\Samples\\");
    // فتح المستند
    auto document = MakeObject<Document>(_dataDir + u"GetValuesFromAllFields.pdf");
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));
    Console::WriteLine(u"الحد: {0}", textBoxField->get_MaxLen());        
}
```

يمكنك أيضًا تعيين والحصول على نفس القيمة باستخدام فضاء الأسماء *Aspose.PDF.Facades* باستخدام النص البرمجي التالي.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;

void SetFieldLimitFacade(){
    String _dataDir("C:\\Samples\\");
    // إضافة حقل مع الحد
    auto form = MakeObject<Aspose::Pdf::Facades::FormEditor>(_dataDir + u"input.pdf", _dataDir + u"SetFieldLimit_out.pdf");
    form->SetFieldLimit(u"textbox1", 15);
    form->Save();
}
```

```cpp
void GetFieldLimitFacade(){
    String _dataDir("C:\\Samples\\");
    // إضافة حقل مع الحد
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + u"input.pdf");
    Console::WriteLine(u"الحد: {0}", form->GetFieldLimit(u"textbox1"));
}
```
## تعيين خط مخصص لحقل النموذج

يمكن تكوين الحقول في ملفات Adobe PDF لاستخدام خطوط افتراضية محددة. في الإصدارات المبكرة من Aspose.PDF، كان يتم دعم 14 خطًا افتراضيًا فقط. الإصدارات اللاحقة سمحت للمطورين بتطبيق أي خط. لتعيين وتحديث الخط الافتراضي المستخدم لحقول النموذج، استخدم الفئة DefaultAppearance (Font font, double size, Color color). يمكن العثور على هذه الفئة تحت المساحة Aspose.PDF.InteractiveFeatures. لاستخدام هذا الكائن، استخدم خاصية DefaultAppearance من الفئة Field.

يُظهر مقطع الكود التالي كيفية تعيين الخط الافتراضي لحقول النموذج في PDF.

```cpp
void SetCustomFontForField() {

    String _dataDir("C:\\Samples\\");

    // فتح المستند
    auto document = new Document(_dataDir + u"FormFieldFont14.pdf");

    // الحصول على حقل نموذج معين من المستند
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));

    // إنشاء كائن الخط
    auto font = Aspose::Pdf::Text::FontRepository::FindFont(u"ComicSansMS");

    // تعيين معلومات الخط لحقل النموذج

    textBoxField->set_DefaultAppearance(MakeObject<Aspose::Pdf::Annotations::DefaultAppearance>(font, 10, System::Drawing::Color::get_Black()));

    // حفظ المستند المحدث
    document->Save(_dataDir + u"FormFieldFont14.pdf");
}
```

## حذف الحقول من النموذج الحالي

تحتوي جميع حقول النموذج على مجموعة Forms الخاصة بكائن Document. توفر هذه المجموعة طرقًا مختلفة لإدارة حقول النموذج، بما في ذلك طريقة Delete. إذا كنت ترغب في حذف حقل معين، قم بتمرير اسم الحقل كمعامل لطريقة Delete ثم قم بحفظ مستند PDF المحدث. يوضح مقطع الشيفرة التالي كيفية حذف حقل معين من مستند PDF.

```cpp
void DeleteFormField() {    
    String _dataDir("C:\\Samples\\");

    // فتح المستند
    auto document = new Document(_dataDir + u"DeleteFormField.pdf");

    // حذف حقل معين بالاسم
    document->get_Form()->Delete(u"textbox1");
    
    // حفظ المستند المعدل
    document->Save(_dataDir + u"DeleteFormField_out.pdf");
}
```