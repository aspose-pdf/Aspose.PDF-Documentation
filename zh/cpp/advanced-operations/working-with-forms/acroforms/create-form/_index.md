---
title: 使用C++创建AcroForms
linktitle: 创建AcroForms
type: docs
weight: 10
url: /zh/cpp/create-form/
description: 本节介绍如何使用Aspose.PDF for C++从头开始在PDF文档中创建AcroForms。
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 在PDF文档中添加表单字段

[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 类提供了一个名为Form的集合，用于管理PDF文档中的表单字段。

要添加表单字段：

1. 创建要添加的表单字段。
2. 调用[Form](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.forms)集合的add方法。

此示例展示了如何添加[TextBoxField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.text_box_field)。您可以使用相同的方法添加任何表单字段：

1. 首先，创建一个字段对象并设置其属性。
2. 然后，将字段添加到Form集合中。

### 添加TextBoxField

文本字段是一个表单元素，允许接收者在您的表单中输入文本。 这将用于任何时候您想允许用户自由输入他们想要的内容。

以下代码片段展示了如何向 PDF 文档添加一个 TextBoxField。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;
using namespace Aspose::Pdf::Annotations;
void AddingTextBoxField()
{
    String _dataDir("C:\\Samples\\");
    // 打开文档
    auto document = MakeObject<Document>(_dataDir + u"TextField.pdf");

    // 创建一个字段
    auto textBoxField = MakeObject<TextBoxField>(document->get_Pages()->idx_get(1), MakeObject<Aspose::Pdf::Rectangle>(100, 200, 300, 300));
    textBoxField->set_PartialName (u"textbox1");
    textBoxField->set_Value (u"Text Box");

    // TextBoxField.Border = new Border(
    auto border = MakeObject<Aspose::Pdf::Annotations::Border>(textBoxField);
    border->set_Width(5);
    border->set_Dash (MakeObject<Aspose::Pdf::Annotations::Dash>(1, 1));
    textBoxField->set_Border(border);

    textBoxField->set_Color(Aspose::Pdf::Color::get_Green());

    // 将字段添加到文档
    document->get_Form()->Add(textBoxField, 1);

    // 保存修改后的 PDF
    document->Save(_dataDir + u"TextBox_out.pdf");
}
```
## 添加 RadioButtonField

单选按钮通常用于多项选择题，在这种情况下只能选择一个答案。

以下代码片段显示了如何在 PDF 文档中添加 [RadioButtonField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.radio_button_field)。

```cpp
void AddingRadioButtonField()
{
    String _dataDir("C:\\Samples\\");
    // 打开文档
    auto document = MakeObject<Document>();

    // 向 PDF 文件添加页面
    document->get_Pages()->Add();

    // 实例化 RadioButtonField 对象，将页码作为参数

    auto radio = MakeObject<RadioButtonField>(document->get_Pages()->idx_get(1));

    // 添加第一个单选按钮选项，并使用 Rectangle 对象指定其起始位置
    radio->AddOption(u"Option 1", MakeObject<Rectangle>(0, 0, 20, 20));
    // 添加第二个单选按钮选项
    radio->AddOption(u"Option 2", MakeObject<Rectangle>(20, 20, 40, 40));
    // 将单选按钮添加到 Document 对象的表单对象中
    document->get_Form()->Add(radio,1);

    // 保存 PDF 文件
    document->Save(_dataDir + u"RadioButton_out.pdf");
}
```

以下代码片段展示了添加[RadioButtonField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.radio_button_field)的步骤，其中包含三个选项，并将它们放置在表格单元格内。

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

    // 保存PDF文件
    document->Save(_dataDir + u"RadioButtonWithOptions_out.pdf");
}
```

## 为 RadioButtonField 添加标题

以下代码片段展示了如何添加与 [RadioButtonField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.radio_button_field) 关联的标题：

```cpp
void AddingCaptionToRadioButtonField()
{
    String _dataDir("C:\\Samples\\");
    auto document = MakeObject<Document>();

    // 加载源 PDF 表单
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

            // 创建 TextParagraph 对象
            auto par = MakeObject<Aspose::Pdf::Text::TextParagraph>();

            // 设置段落位置
            par->set_Position(MakeObject<Aspose::Pdf::Text::Position>(field0->get_Rect()->get_LLX(), field0->get_Rect()->get_LLY() + updatedFragment->get_TextState()->get_FontSize()));
            // 指定单词换行模式
        par->get_FormattingOptions()->set_WrapMode(Aspose::Pdf::Text::TextFormattingOptions::WordWrapMode::ByWords);

            // 向段落中添加新的 TextFragment
            par->AppendLine(updatedFragment);

            // 使用 TextBuilder 添加 TextParagraph
            auto textBuilder = MakeObject<Aspose::Pdf::Text::TextBuilder>(PDF_Template_PDF_HTML->get_Pages()->idx_get(1));
            textBuilder->AppendParagraph(par);

            field0->DeleteOption(u"item1");
        }
    }
    PDF_Template_PDF_HTML->Save(_dataDir + u"RadioButtonField_out.pdf");
}
```

## 添加组合框字段

组合框是一种表单字段，它将在您的文档中添加一个下拉菜单。

以下代码片段展示了如何在 PDF 文档中添加[组合框](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.combo_box_field)字段。

```cpp
void AddingComboBoxField()
{
    String _dataDir("C:\\Samples\\");
    // 创建文档对象
    auto document = MakeObject<Document>();
    // 向文档对象添加页面
    document->get_Pages()->Add();
    // 实例化组合框字段对象
    auto combo = MakeObject<ComboBoxField>(document->get_Pages()->idx_get(1),
        MakeObject<Rectangle>(100, 600, 150, 616));

    // 向组合框添加选项
    combo->AddOption(u"Red");
    combo->AddOption(u"Yellow");
    combo->AddOption(u"Green");
    combo->AddOption(u"Blue");

    // 将组合框对象添加到文档对象的表单字段集合中
    document->get_Form()->Add(combo);

    // 保存 PDF 文档
    document->Save(_dataDir + u"ComboBox_out.pdf");
}
```

## 为表单添加工具提示

The Document 类提供了一个名为 Form 的集合，用于管理 PDF 文档中的表单字段。要为表单字段添加工具提示，请使用 Field 类的 AlternateName。Adobe Acrobat 使用“替代名称”作为字段工具提示。

以下代码片段展示了如何使用 C++ 向表单字段添加工具提示。

```cpp
void AddTooltipToFormField()
{
    String _dataDir("C:\\Samples\\");
    // 加载源 PDF 表单
    auto document = new Document(_dataDir + u"AddTooltipToField.pdf");

    // 为文本字段设置工具提示
    //(doc.Form["textbox1"] as Field).AlternateName = "Text box tool tip";

    // 保存更新后的文档
    document->Save(_dataDir + u"AddTooltipToField_out.pdf");
}
```