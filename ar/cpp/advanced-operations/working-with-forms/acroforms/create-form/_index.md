---
title: Create AcroForms using using C++
linktitle: Create AcroForms
type: docs
weight: 10
url: ar/cpp/create-form/
description: يشرح هذا القسم كيفية إنشاء AcroForms من البداية في مستندات PDF الخاصة بك باستخدام Aspose.PDF لـ C++.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## إضافة حقل نموذج في مستند PDF

يوفر فصل [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) مجموعة باسم Form تساعد في إدارة حقول النماذج في مستند PDF.

لإضافة حقل نموذج:

1. أنشئ حقل النموذج الذي تريد إضافته.
2. استدع طريقة الإضافة من مجموعة [Form](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.forms).

يوضح هذا المثال كيفية إضافة [TextBoxField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.text_box_field). يمكنك إضافة أي حقل نموذج باستخدام نفس النهج:

1. أولاً، أنشئ كائن حقل واضبط خصائصه.
2. ثم، أضف الحقل إلى مجموعة Form.

### إضافة TextBoxField

حقل النص هو عنصر نموذج يسمح للمستلم بإدخال نص في النموذج الخاص بك. هذا سيُستخدم في أي وقت تريد فيه السماح للمستخدم بحرية كتابة ما يريد.

تُظهر مقتطفات الشيفرة التالية كيفية إضافة TextBoxField إلى مستند PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;
using namespace Aspose::Pdf::Annotations;
void AddingTextBoxField()
{
    String _dataDir("C:\\Samples\\");
    // افتح المستند
    auto document = MakeObject<Document>(_dataDir + u"TextField.pdf");

    // أنشئ حقلاً
    auto textBoxField = MakeObject<TextBoxField>(document->get_Pages()->idx_get(1), MakeObject<Aspose::Pdf::Rectangle>(100, 200, 300, 300));
    textBoxField->set_PartialName (u"textbox1");
    textBoxField->set_Value (u"Text Box");

    // TextBoxField.Border = new Border(
    auto border = MakeObject<Aspose::Pdf::Annotations::Border>(textBoxField);
    border->set_Width(5);
    border->set_Dash (MakeObject<Aspose::Pdf::Annotations::Dash>(1, 1));
    textBoxField->set_Border(border);

    textBoxField->set_Color(Aspose::Pdf::Color::get_Green());

    // أضف الحقل إلى المستند
    document->get_Form()->Add(textBoxField, 1);

    // احفظ ملف PDF المعدل
    document->Save(_dataDir + u"TextBox_out.pdf");
}
```
## إضافة RadioButtonField

عادةً ما يُستخدم زر الاختيار للأسئلة ذات الاختيارات المتعددة، في السيناريو حيث يمكن اختيار إجابة واحدة فقط.

تُظهر الشيفرات التالية كيفية إضافة [RadioButtonField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.radio_button_field) في مستند PDF.

```cpp
void AddingRadioButtonField()
{
    String _dataDir("C:\\Samples\\");
    // فتح المستند
    auto document = MakeObject<Document>();

    // إضافة صفحة إلى ملف PDF
    document->get_Pages()->Add();

    // إنشاء كائن RadioButtonField مع رقم الصفحة كمعامل

    auto radio = MakeObject<RadioButtonField>(document->get_Pages()->idx_get(1));

    // إضافة خيار زر الاختيار الأول وتحديد مكانه باستخدام كائن Rectangle
    radio->AddOption(u"Option 1", MakeObject<Rectangle>(0, 0, 20, 20));
    // إضافة خيار زر الاختيار الثاني
    radio->AddOption(u"Option 2", MakeObject<Rectangle>(20, 20, 40, 40));
    // إضافة زر الاختيار إلى كائن النموذج الخاص بكائن المستند
    document->get_Form()->Add(radio,1);

    // حفظ ملف PDF
    document->Save(_dataDir + u"RadioButton_out.pdf");
}
```

النص التالي يظهر خطوات إضافة [RadioButtonField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.radio_button_field) مع ثلاث خيارات ووضعها داخل خلايا الجدول.

```cpp
void AddRadioButtonFieldInsideTableCells()
{
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto table = MakeObject<Aspose::Pdf::Table>();

    table->set_ColumnWidths(u"120 120 120");

    page->get_Paragraphs()->Add(table);

    auto r1 = table->get_Rows()->Add();
    auto c1 = r1->get_Cells()->Add();
    auto c2 = r1->get_Cells()->Add();
    auto c3 = r1->get_Cells()->Add();

    auto rf = MakeObject<RadioButtonField>(page);
    rf->set_PartialName(u"radio");
    document->get_Form()->Add(rf, 1);

    auto opt1 = MakeObject<RadioButtonOptionField>();
    auto opt2 = MakeObject<RadioButtonOptionField>();
    auto opt3 = MakeObject<RadioButtonOptionField>();

    opt1->set_OptionName(u"Item1");
    opt2->set_OptionName(u"Item2");
    opt3->set_OptionName(u"Item3");

    opt1->set_Width (15);
    opt1->set_Height(15);
    opt2->set_Width (15);
    opt2->set_Height(15);
    opt3->set_Width (15);
    opt3->set_Height(15);

    rf->Add(opt1);
    rf->Add(opt2);
    rf->Add(opt3);

    opt1->set_Border(MakeObject<Border>(opt1));
    opt1->get_Border()->set_Width(1);
    opt1->get_Border()->set_Style(BorderStyle::Solid);
    opt1->get_Characteristics()->set_Border(System::Drawing::Color::get_Black());
    opt1->get_DefaultAppearance()->set_TextColor(System::Drawing::Color::get_Red());
    opt1->set_Caption(MakeObject<Aspose::Pdf::Text::TextFragment>(u"Item1"));
    opt2->set_Border(MakeObject<Border>(opt2));
    opt2->get_Border()->set_Width(1);
    opt2->get_Border()->set_Style(BorderStyle::Solid);
    opt2->get_Characteristics()->set_Border(System::Drawing::Color::get_Black());
    opt2->get_DefaultAppearance()->set_TextColor(System::Drawing::Color::get_Red());
    opt2->set_Caption(MakeObject<Aspose::Pdf::Text::TextFragment>(u"Item2"));
    opt3->set_Border(MakeObject<Border>(opt3));
    opt3->get_Border()->set_Width(1);
    opt3->get_Border()->set_Style(BorderStyle::Solid);
    opt3->get_Characteristics()->set_Border(System::Drawing::Color::get_Black());
    opt3->get_DefaultAppearance()->set_TextColor(System::Drawing::Color::get_Red());
    opt3->set_Caption(MakeObject<Aspose::Pdf::Text::TextFragment>(u"Item3"));
    c1->get_Paragraphs()->Add(opt1);
    c2->get_Paragraphs()->Add(opt2);
    c3->get_Paragraphs()->Add(opt3);

    // حفظ ملف PDF
    document->Save(_dataDir + u"RadioButtonWithOptions_out.pdf");
}
```

## إضافة تعليق إلى RadioButtonField

يوضح مقتطف الشيفرة التالي كيفية إضافة تعليق والذي سيتم ربطه بـ [RadioButtonField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.radio_button_field):

```cpp
void AddingCaptionToRadioButtonField()
{
    String _dataDir("C:\\Samples\\");
    auto document = MakeObject<Document>();

    // تحميل نموذج PDF المصدر
    auto form1 =
        MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + u"RadioButtonField.pdf");

    auto PDF_Template_PDF_HTML = MakeObject<Document>(_dataDir + u"RadioButtonField.pdf");

    for(auto item : form1->get_FieldNames())
    {
        System::Console::WriteLine(item);
        auto radioOptions = form1->GetButtonOptionValues(item);
        if (item.Contains(u"radio1"))
        {
            auto field0 = System::DynamicCast<RadioButtonField>(PDF_Template_PDF_HTML->get_Form()->idx_get(item));
            auto fieldoption = MakeObject<RadioButtonOptionField>();
            fieldoption->set_OptionName (u"Yes");
            fieldoption->set_PartialName (u"Yesname");

            auto updatedFragment = MakeObject<Aspose::Pdf::Text::TextFragment>(u"test123");
            updatedFragment->get_TextState()->set_Font (Aspose::Pdf::Text::FontRepository::FindFont(u"Arial"));
            updatedFragment->get_TextState()->set_FontSize(10);
            updatedFragment->get_TextState()->set_LineSpacing(6.32f);

            // إنشاء كائن TextParagraph
            auto par = MakeObject<Aspose::Pdf::Text::TextParagraph>();

            // تعيين موقع الفقرة
            par->set_Position(MakeObject<Aspose::Pdf::Text::Position>(field0->get_Rect()->get_LLX(), field0->get_Rect()->get_LLY() + updatedFragment->get_TextState()->get_FontSize()));
            // تحديد وضع التفاف الكلمات
            par->get_FormattingOptions()->set_WrapMode(Aspose::Pdf::Text::TextFormattingOptions::WordWrapMode::ByWords);

            // إضافة TextFragment جديد إلى الفقرة
            par->AppendLine(updatedFragment);

            // إضافة TextParagraph باستخدام TextBuilder
            auto textBuilder = MakeObject<Aspose::Pdf::Text::TextBuilder>(PDF_Template_PDF_HTML->get_Pages()->idx_get(1));
            textBuilder->AppendParagraph(par);

            field0->DeleteOption(u"item1");
        }
    }
    PDF_Template_PDF_HTML->Save(_dataDir + u"RadioButtonField_out.pdf");
}
```

## إضافة حقل ComboBox

مربع التحرير والسرد هو حقل نموذج سيضيف قائمة منسدلة إلى المستند الخاص بك.

تُظهر مقتطفات الشيفرة التالية كيفية إضافة حقل [ComboBox](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.combo_box_field) في مستند PDF.

```cpp
void AddingComboBoxField()
{
    String _dataDir("C:\\Samples\\");
    // إنشاء كائن المستند
    auto document = MakeObject<Document>();
    // إضافة صفحة إلى كائن المستند
    document->get_Pages()->Add();
    // إنشاء كائن حقل ComboBox
    auto combo = MakeObject<ComboBoxField>(document->get_Pages()->idx_get(1),
        MakeObject<Rectangle>(100, 600, 150, 616));

    // إضافة خيار إلى ComboBox
    combo->AddOption(u"Red");
    combo->AddOption(u"Yellow");
    combo->AddOption(u"Green");
    combo->AddOption(u"Blue");

    // إضافة كائن مربع التحرير والسرد إلى مجموعة حقول النموذج لكائن المستند
    document->get_Form()->Add(combo);

    // حفظ مستند PDF
    document->Save(_dataDir + u"ComboBox_out.pdf");
}
```

## إضافة تلميح إلى النموذج

The Document class provides a collection named Form which manages form fields in a PDF document. To add a tooltip to a form field, use the Field class AlternateName. Adobe Acrobat uses the ‘alternate name’ as a field tooltip.

تقوم فئة Document بتوفير مجموعة تُسمى Form والتي تدير حقول النماذج في مستند PDF. لإضافة تلميح إلى حقل نموذج، استخدم فئة Field AlternateName. يستخدم Adobe Acrobat "الاسم البديل" كتلميح للحقل.

The code snippets that follow show how to add a tooltip to a form field with C++.

توضح مقتطفات الكود التالية كيفية إضافة تلميح إلى حقل نموذج باستخدام C++.

```cpp
void AddTooltipToFormField()
{
    String _dataDir("C:\\Samples\\");
    // Load source PDF form
    auto document = new Document(_dataDir + u"AddTooltipToField.pdf");

    // Set the tooltip for textfield
    //(doc.Form["textbox1"] as Field).AlternateName = "Text box tool tip";

    // Save the updated document
    document->Save(_dataDir + u"AddTooltipToField_out.pdf");
}
```