---
title: Создание AcroForms с использованием C++
linktitle: Создание AcroForms
type: docs
weight: 10
url: ru/cpp/create-form/
description: В этом разделе объясняется, как создать AcroForms с нуля в ваших PDF-документах с помощью Aspose.PDF для C++.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Добавление поля формы в PDF-документ

Класс [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) предоставляет коллекцию с именем Form, которая помогает управлять полями формы в PDF-документе.

Чтобы добавить поле формы:

1. Создайте поле формы, которое вы хотите добавить.
2. Вызовите метод добавления коллекции [Form](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.forms).

Этот пример показывает, как добавить [TextBoxField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.text_box_field). Вы можете добавить любое поле формы, используя тот же подход:

1. Сначала создайте объект поля и задайте его свойства.
2. Затем добавьте поле в коллекцию Form.

### Добавление TextBoxField

Текстовое поле — это элемент формы, который позволяет получателю ввести текст в вашу форму. Это будет использоваться всякий раз, когда вы хотите предоставить пользователю свободу вводить то, что они хотят.

Следующий фрагмент кода показывает, как добавить TextBoxField в PDF-документ.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;
using namespace Aspose::Pdf::Annotations;
void AddingTextBoxField()
{
    String _dataDir("C:\\Samples\\");
    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + u"TextField.pdf");

    // Создать поле
    auto textBoxField = MakeObject<TextBoxField>(document->get_Pages()->idx_get(1), MakeObject<Aspose::Pdf::Rectangle>(100, 200, 300, 300));
    textBoxField->set_PartialName (u"textbox1");
    textBoxField->set_Value (u"Text Box");

    // TextBoxField.Border = new Border(
    auto border = MakeObject<Aspose::Pdf::Annotations::Border>(textBoxField);
    border->set_Width(5);
    border->set_Dash (MakeObject<Aspose::Pdf::Annotations::Dash>(1, 1));
    textBoxField->set_Border(border);

    textBoxField->set_Color(Aspose::Pdf::Color::get_Green());

    // Добавить поле в документ
    document->get_Form()->Add(textBoxField, 1);

    // Сохранить измененный PDF
    document->Save(_dataDir + u"TextBox_out.pdf");
}
```
## Добавление RadioButtonField

RadioButton чаще всего используется для вопросов с несколькими вариантами ответов, в сценарии, когда можно выбрать только один ответ.

Следующие фрагменты кода показывают, как добавить [RadioButtonField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.radio_button_field) в PDF документ.

```cpp
void AddingRadioButtonField()
{
    String _dataDir("C:\\Samples\\");
    // Открыть документ
    auto document = MakeObject<Document>();

    // Добавить страницу в PDF файл
    document->get_Pages()->Add();

    // Создать объект RadioButtonField с номером страницы в качестве аргумента

    auto radio = MakeObject<RadioButtonField>(document->get_Pages()->idx_get(1));

    // Добавить первый вариант радио-кнопки и также указать его положение, используя объект Rectangle
    radio->AddOption(u"Option 1", MakeObject<Rectangle>(0, 0, 20, 20));
    // Добавить второй вариант радио-кнопки
    radio->AddOption(u"Option 2", MakeObject<Rectangle>(20, 20, 40, 40));
    // Добавить радио-кнопку в форму объекта Document
    document->get_Form()->Add(radio,1);

    // Сохранить PDF файл
    document->Save(_dataDir + u"RadioButton_out.pdf");
}
```

Следующий фрагмент кода показывает шаги по добавлению [RadioButtonField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.radio_button_field) с тремя опциями и размещению их внутри ячеек таблицы.

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

    // Сохранить PDF файл
    document->Save(_dataDir + u"RadioButtonWithOptions_out.pdf");
}
```

## Добавление подписи к RadioButtonField

Следующий фрагмент кода показывает, как добавить подпись, которая будет связана с [RadioButtonField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.radio_button_field):

```cpp
void AddingCaptionToRadioButtonField()
{
    String _dataDir("C:\\Samples\\");
    auto document = MakeObject<Document>();

    // Загрузить исходную PDF форму
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

            // Создать объект TextParagraph
            auto par = MakeObject<Aspose::Pdf::Text::TextParagraph>();

            // Установить позицию абзаца
            par->set_Position(MakeObject<Aspose::Pdf::Text::Position>(field0->get_Rect()->get_LLX(), field0->get_Rect()->get_LLY() + updatedFragment->get_TextState()->get_FontSize()));
            // Указать режим переноса слов
        par->get_FormattingOptions()->set_WrapMode(Aspose::Pdf::Text::TextFormattingOptions::WordWrapMode::ByWords);

            // Добавить новый TextFragment в абзац
            par->AppendLine(updatedFragment);

            // Добавить TextParagraph с помощью TextBuilder
            auto textBuilder = MakeObject<Aspose::Pdf::Text::TextBuilder>(PDF_Template_PDF_HTML->get_Pages()->idx_get(1));
            textBuilder->AppendParagraph(par);

            field0->DeleteOption(u"item1");
        }
    }
    PDF_Template_PDF_HTML->Save(_dataDir + u"RadioButtonField_out.pdf");
}
```

## Добавление поля ComboBox

Combo Box — это поле формы, которое добавляет выпадающее меню в ваш документ.

Следующие фрагменты кода показывают, как добавить поле [ComboBox](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.combo_box_field) в PDF-документ.

```cpp
void AddingComboBoxField()
{
    String _dataDir("C:\\Samples\\");
    // Создать объект документа
    auto document = MakeObject<Document>();
    // Добавить страницу к объекту документа
    document->get_Pages()->Add();
    // Создать объект поля ComboBox
    auto combo = MakeObject<ComboBoxField>(document->get_Pages()->idx_get(1),
        MakeObject<Rectangle>(100, 600, 150, 616));

    // Добавить опцию в ComboBox
    combo->AddOption(u"Red");
    combo->AddOption(u"Yellow");
    combo->AddOption(u"Green");
    combo->AddOption(u"Blue");

    // Добавить объект ComboBox в коллекцию полей формы объекта документа
    document->get_Form()->Add(combo);

    // Сохранить PDF-документ
    document->Save(_dataDir + u"ComboBox_out.pdf");
}
```

## Добавить подсказку к форме

The Document класс предоставляет коллекцию под названием Form, которая управляет полями формы в PDF документе. Чтобы добавить подсказку к полю формы, используйте класс Field AlternateName. Adobe Acrobat использует 'альтернативное имя' в качестве подсказки для поля.

В следующих фрагментах кода показано, как добавить подсказку к полю формы с помощью C++.

```cpp
void AddTooltipToFormField()
{
    String _dataDir("C:\\Samples\\");
    // Загрузить исходную PDF форму
    auto document = new Document(_dataDir + u"AddTooltipToField.pdf");

    // Установить подсказку для текстового поля
    //(doc.Form["textbox1"] as Field).AlternateName = "Подсказка для текстового поля";

    // Сохранить обновленный документ
    document->Save(_dataDir + u"AddTooltipToField_out.pdf");
}
```