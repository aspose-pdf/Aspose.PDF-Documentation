---
title: 提取 AcroForm 数据使用 C++
linktitle: 提取数据 AcroForm
type: docs
weight: 30
url: zh/cpp/extract-form/
description: 本节解释如何使用 Aspose.PDF for C++ 从 PDF 文档中提取表单。
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 从 PDF 文档的所有字段获取值

要从 PDF 文档的所有字段中获取值，您需要遍历所有表单字段，然后使用 Value 属性获取值。从 Form 集合中获取每个字段，在称为 Field 的基本字段类型中访问其 Value 属性。

以下代码片段显示了如何从 PDF 文档中获取所有字段的值。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;

void ExtractDataFromForm()
{
    String _dataDir("C:\\Samples\\");
    // 打开文档
    auto document = MakeObject<Document>(_dataDir + u"GetValuesFromAllFields.pdf");

    // 从所有字段获取值
    for(auto wa : document->get_Form())
    {
        auto formField = System::DynamicCast<Aspose::Pdf::Forms::Field>(wa);

        Console::WriteLine(u"字段名称 : {0} ", formField->get_PartialName());
        Console::WriteLine(u"值 : {0} ", formField->get_Value());
    }
}
```

## 从 PDF 文档的单个字段获取值

表单字段的 Value 属性允许您获取特定字段的值。要获取值，请从 Document 对象的 Form 集合中获取表单字段。此示例选择一个 [TextBoxField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.text_box_field) 并使用 Value 属性检索其值。

以下代码片段展示了如何获取 PDF 文档中单个字段的值。

```cpp
void GetValueFromIndividualField(){

    String _dataDir("C:\\Samples\\");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + u"GetValueFromField.pdf");

    // 获取字段
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));

    // 获取字段值
    Console::WriteLine(u"PartialName : {0} ", textBoxField->get_PartialName());
    Console::WriteLine(u"Value : {0} ", textBoxField->get_Value());
}
```

要获取提交按钮的 URL，请使用以下代码行。

```cpp
void GetSubmitButtonURL()
{
    String _dataDir("C:\\Samples\\");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + u"GetValueFromField.pdf");
    auto act = System::DynamicCast<Aspose::Pdf::Annotations::SubmitFormAction>(document->get_Form()->idx_get(1)->get_OnActivated());

    if (act != nullptr)
        Console::WriteLine(act->get_Url()->get_Name());
}
```

## 从PDF文件的特定区域获取表单字段

有时，您可能知道文档中表单字段的位置，但不知道其名称。例如，如果您只有一个打印表单的示意图。使用Aspose.PDF for C++，这不是问题。您可以找出PDF文件中给定区域内的字段。要从PDF文件的特定区域获取表单字段：

1. 使用Document对象打开PDF文件。
1. 创建矩形对象以获取该区域的字段
1. 从文档的Forms集合中获取表单。
1. 显示字段名称和值

以下代码片段显示了如何在PDF文件的特定矩形区域中获取表单字段。
```

```cpp
void GetFormFieldsFromSpecificRegion()
{
    String _dataDir("C:\\Samples\\");

    // 打开pdf文件
    auto document = MakeObject<Aspose::Pdf::Document>(_dataDir + u"GetFieldsFromRegion.pdf");

    // 创建矩形对象以获取该区域的字段
    auto rectangle = MakeObject<Aspose::Pdf::Rectangle>(35, 30, 500, 500);

    // 获取矩形区域内的字段
    auto fields = document->get_Form()->GetFieldsInRect(rectangle);

    // 显示字段名称和值
    for(auto field : fields)
    {
        // 显示所有位置的图像放置属性
        Console::WriteLine(u"字段名称: {0} - 字段值: {1}", field->get_FullName(), field->get_Value());
    }
}
```