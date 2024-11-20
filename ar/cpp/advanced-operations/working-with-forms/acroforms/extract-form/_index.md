---
title: استخراج بيانات AcroForm باستخدام C++
linktitle: استخراج بيانات AcroForm
type: docs
weight: 30
url: /ar/cpp/extract-form/
description: يوضح هذا القسم كيفية استخراج النماذج من مستند PDF الخاص بك باستخدام Aspose.PDF for C++.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## الحصول على القيم من جميع حقول مستند PDF

للحصول على القيم من جميع الحقول في مستند PDF، تحتاج إلى التنقل عبر جميع حقول النموذج ثم الحصول على القيمة باستخدام خاصية Value. احصل على كل حقل من مجموعة النموذج، في نوع الحقل الأساسي المسمى Field وادخل إلى خاصية Value الخاصة به.

توضح مقتطفات الشفرة التالية كيفية الحصول على القيم من جميع الحقول من مستند PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;

void ExtractDataFromForm()
{
    String _dataDir("C:\\Samples\\");
    // افتح المستند
    auto document = MakeObject<Document>(_dataDir + u"GetValuesFromAllFields.pdf");

    // احصل على القيم من جميع الحقول
    for(auto wa : document->get_Form())
    {
        auto formField = System::DynamicCast<Aspose::Pdf::Forms::Field>(wa);

        Console::WriteLine(u"Field Name : {0} ", formField->get_PartialName());
        Console::WriteLine(u"Value : {0} ", formField->get_Value());
    }
}
```
```

## الحصول على قيمة من حقل فردي في مستند PDF

تسمح لك خاصية قيمة الحقل النموذجي بالحصول على قيمة حقل معين. للحصول على القيمة، احصل على الحقل النموذجي من مجموعة النموذج الخاصة بكائن المستند. يختار هذا المثال [TextBoxField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.text_box_field) ويستعيد قيمته باستخدام خاصية القيمة.

يوضح مقتطف الكود التالي كيفية الحصول على قيم الحقول الفردية في مستند PDF.

```cpp
void GetValueFromIndividualField(){

    String _dataDir("C:\\Samples\\");

    // افتح المستند
    auto document = MakeObject<Document>(_dataDir + u"GetValueFromField.pdf");

    // احصل على حقل
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));

    // احصل على قيمة الحقل
    Console::WriteLine(u"PartialName : {0} ", textBoxField->get_PartialName());
    Console::WriteLine(u"Value : {0} ", textBoxField->get_Value());
}
```

للحصول على عنوان URL لزر الإرسال، استخدم الأسطر التالية من الكود.

```cpp
void GetSubmitButtonURL()
{
    String _dataDir("C:\\Samples\\");

    // Open document
    auto document = MakeObject<Document>(_dataDir + u"GetValueFromField.pdf");
    auto act = System::DynamicCast<Aspose::Pdf::Annotations::SubmitFormAction>(document->get_Form()->idx_get(1)->get_OnActivated());

    if (act != nullptr)
        Console::WriteLine(act->get_Url()->get_Name());
}
```

## الحصول على حقول النموذج من منطقة معينة في ملف PDF

في بعض الأحيان، قد تعرف مكان حقل النموذج في المستند، ولكن لا تعرف اسمه. على سبيل المثال، إذا كان كل ما لديك لتبدأ به هو مخطط لنموذج مطبوع. مع Aspose.PDF for C++، هذا ليس مشكلة. يمكنك معرفة الحقول الموجودة في منطقة معينة من ملف PDF. للحصول على حقول النموذج من منطقة معينة من ملف PDF:

1. افتح ملف PDF باستخدام كائن Document.
2. قم بإنشاء كائن مستطيل للحصول على الحقول في تلك المنطقة
3. احصل على النموذج من مجموعة Forms الخاصة بالمستند.
4. عرض أسماء الحقول والقيم

يظهر جزء الكود التالي كيفية الحصول على حقول النموذج في منطقة مستطيلة معينة من ملف PDF.

```cpp
void GetFormFieldsFromSpecificRegion()
{
    String _dataDir("C:\\Samples\\");

    // فتح ملف pdf
    auto document = MakeObject<Aspose::Pdf::Document>(_dataDir + u"GetFieldsFromRegion.pdf");

    // إنشاء كائن مستطيل للحصول على الحقول في تلك المنطقة
    auto rectangle = MakeObject<Aspose::Pdf::Rectangle>(35, 30, 500, 500);

    // الحصول على الحقول في المنطقة المستطيلة
    auto fields = document->get_Form()->GetFieldsInRect(rectangle);

    // عرض أسماء الحقول والقيم
    for(auto field : fields)
    {
        // عرض خصائص وضع الصورة لجميع المواقع
        Console::WriteLine(u"اسم الحقل: {0} - قيمة الحقل: {1}", field->get_FullName(), field->get_Value());
    }
}
```