---
title: العمل مع نماذج XFA باستخدام C++
linktitle: نماذج XFA
type: docs
weight: 20
url: /cpp/xfa-forms/
description: تتيح لك Aspose.PDF for C++ API العمل مع حقول XFA و XFA Acroform في مستند PDF. Aspose.PDF.Facades.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

نماذج XFA هي بنية نماذج XML، وهي مجموعة من المواصفات XML المملوكة التي اقترحتها وطورها JetForm لتحسين التعامل مع النماذج عبر الويب. يمكن استخدامها أيضًا في ملفات PDF بدءًا من مواصفات PDF 1.5.

املأ حقول XFA باستخدام فئة [Form](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.form/) بواسطة [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.facades).

## املأ حقول XFA

يُظهر لك المقتطف البرمجي التالي كيفية ملء الحقول في نموذج XFA.

```cpp
using namespace System;
using namespace System::Collections::Generic;

using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void FillXFA() {
    String _dataDir("C:\\Samples\\");

    // Load XFA form
    auto document = MakeObject<Document>(_dataDir + u"FillXFAFields.pdf");

    // Get names of XFA form fields
    auto names = document->get_Form()->get_XFA()->get_FieldNames();

    // Set field values

    document->get_Form()->get_XFA()->idx_set(names->idx_get(0),u"Field 0");
    document->get_Form()->get_XFA()->idx_set(names->idx_get(1),u"Field 1");

    // Save the updated document
    document->Save(_dataDir + u"Filled_XFA_out.pdf");
}
```

## تحويل XFA إلى AcroForm

{{% alert color="primary" %}}

جرب عبر الإنترنت
يمكنك التحقق من جودة تحويل Aspose.PDF وعرض النتائج عبر الإنترنت من خلال هذا الرابط: [products.aspose.app/pdf/xfa/acroform](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

النماذج الديناميكية تستند إلى مواصفة XML تعرف باسم XFA، "هندسة نماذج XML". المعلومات حول النموذج (بقدر ما يتعلق الأمر بـ PDF) غامضة جدًا – فهي تحدد وجود الحقول، مع الخصائص، والأحداث JavaScript، ولكنها لا تحدد أي عرض.

حاليًا، يدعم PDF طريقتين مختلفتين لدمج البيانات ونماذج PDF:

- AcroForms (المعروفة أيضًا بنماذج Acrobat)، التي تم تقديمها وتضمينها في مواصفة تنسيق PDF 1.2.
- نماذج Adobe XML Forms Architecture (XFA)، التي تم تقديمها في مواصفة تنسيق PDF 1.5 كميزة اختيارية (مواصفة XFA غير مضمنة في مواصفة PDF، وإنما يتم الإشارة إليها فقط.)

لا يمكننا استخراج أو معالجة صفحات نماذج XFA، لأن محتوى النموذج يتم إنشاؤه في وقت التشغيل (أثناء عرض نموذج XFA) داخل التطبيق الذي يحاول عرض أو تقديم نموذج XFA. Aspose.PDF لديها ميزة تسمح للمطورين بتحويل نماذج XFA إلى نماذج AcroForms القياسية.

```cpp
void ConvertXFAtoAcroForms() {

    String _dataDir("C:\\Samples\\");

    // Load XFA form
    auto document = MakeObject<Document>(_dataDir + u"DynamicXFAToAcroForm.pdf");

    // Set the form fields type as standard AcroForm
    document->get_Form()->set_Type(Aspose::Pdf::Forms::FormType::Standard);

    // Save the resultant PDF
    document->Save(_dataDir + u"Standard_AcroForm_out.pdf");
}
```

## الحصول على خصائص حقل XFA

للوصول إلى خصائص الحقل، استخدم أولاً Document.Form.XFA.Teamplate للوصول إلى قالب الحقل. يُظهر مقطع الشفرة التالي خطوات الحصول على إحداثيات X و Y لحقل نموذج XFA.

```cpp
void GetXFAProprties() {

    String _dataDir("C:\\Samples\\");
    // Load XFA form
    auto document = MakeObject<Document>(_dataDir + u"GetXFAProperties.pdf");

    auto names = document->get_Form()->get_XFA()->get_FieldNames();

    // Set field values
    document->get_Form()->get_XFA()->idx_set(names->idx_get(0), u"Field 0");
    document->get_Form()->get_XFA()->idx_set(names->idx_get(0), u"Field 1");

    // Get field position
    Console::WriteLine(document->get_Form()->get_XFA()->GetFieldTemplate(names[0])->get_Attributes()->idx_get(u"x")->get_Value());

    // Get field position
    Console::WriteLine(document->get_Form()->get_XFA()->GetFieldTemplate(names[0])->get_Attributes()->idx_get(u"y")->get_Value());

    // Save the updated document
    document->Save(_dataDir + u"Filled_XFA_out.pdf");
}
```