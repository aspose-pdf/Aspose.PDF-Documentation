---
title: PDF Tooltip using using C++
linktitle: PDF Tooltip
type: docs
weight: 20
url: /zh/cpp/pdf-tooltip/
description: 了解如何使用 C++ 和 Aspose.PDF 向 PDF 文档中的文本片段添加工具提示
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 通过添加不可见按钮向搜索文本添加工具提示

本文演示了如何在 C++ 中向现有 PDF 文档中的文本添加工具提示。Aspose.PDF 支持通过在 PDF 文件中搜索的文本上添加不可见按钮来创建工具提示。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddTooltipToSearchedText() {

    String _dataDir("C:\\Samples\\");

    // 用于输出文件名的字符串
    String outputFileName("Tooltip_out.pdf");

    // 创建包含文本的示例文档
    auto document = MakeObject<Document>();
    document->get_Pages()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>("将鼠标光标移到此处以显示工具提示"));

    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(MakeObject<TextFragment>("将鼠标光标移到此处以显示一个非常长的工具提示"));

    document->Save(outputFileName);

    // 打开包含文本的文档
    auto document = MakeObject<Document>(outputFileName);
    // 创建 TextAbsorber 对象以查找所有匹配正则表达式的短语
    auto absorber = MakeObject<TextFragmentAbsorber>("将鼠标光标移到此处以显示工具提示");
    // 接受文档页面的吸收器
    document->get_Pages()->Accept(absorber);

    // 获取提取的文本片段
    auto textFragments = absorber->get_TextFragments();

    // 遍历片段
    for(auto fragment : textFragments)
    {
        // 在文本片段位置创建不可见按钮
        auto field = MakeObject<Aspose::Pdf::Forms::ButtonField>(fragment->get_Page(), fragment->get_Rectangle());
        // AlternateName 值将作为工具提示由查看器应用程序显示
        field->set_AlternateName (u"文本的工具提示。");
        // 将按钮字段添加到文档中
        document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(field));
    }

    // 接下来是非常长的工具提示示例
    absorber = MakeObject<TextFragmentAbsorber>("将鼠标光标移到此处以显示一个非常长的工具提示");
    document->get_Pages()->Accept(absorber);
    textFragments = absorber->get_TextFragments();

    for(auto fragment : textFragments)
    {
        auto field = MakeObject<Aspose::Pdf::Forms::ButtonField>(fragment->get_Page(), fragment->get_Rectangle());
        // 设置非常长的文本
        field->set_AlternateName(String("Lorem ipsum dolor sit amet, consectetur adipiscing elit,\
            sed do eiusmod tempor incididunt ut labore et dolore magna\
            aliqua. Ut enim ad minim veniam, quis nostrud exercitation\
            ullamco laboris nisi ut aliquip ex ea commodo consequat.\
            Duis aute irure dolor in reprehenderit in voluptate velit\
            esse cillum dolore eu fugiat nulla pariatur. Excepteur sint\
            occaecat cupidatat non proident, sunt in culpa qui officia\
            deserunt mollit anim id est laborum."));
        document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(field));
    }

    // 保存文档
    document->Save(outputFileName);

}
```

## 创建一个隐藏文本块并在鼠标悬停时显示

Aspose.PDF for C++ 实现了一个隐藏动作功能，通过该功能，当鼠标进入/退出某个不可见按钮时，可以显示/隐藏文本字段（或任何其他类型的注释）。为此，使用 Aspose.Pdf.Annotations.HideAction 类为文本块分配隐藏/显示动作。使用以下代码片段在鼠标输入/输出时显示/隐藏文本块。

还请注意，PDF 文档上的动作在各自的阅读器（如 Adobe Reader）中运行良好，但对于其他 PDF 阅读器（如网页浏览器插件）不提供任何保证。我们做了一个简短的调查，发现：

- 在 Internet Explorer v.11.0 中，PDF 文档中隐藏动作的所有实现都运行良好。
- 在 Opera v.12.14 中，隐藏动作的所有实现也能正常工作，但在第一次打开文档时我们发现了一些响应延迟。

- 只有使用接受字段名称的 HideAction 构造函数的实现才能在 Google Chrome v.61.0 浏览文档时工作；如果在 Google Chrome 中浏览很重要，请使用相应的构造函数：

>buttonField.Actions.OnEnter = new HideAction(floatingField.FullName, false);
>buttonField.Actions.OnExit = new HideAction(floatingField.FullName);

```cpp
void CreateHiddenTextBlock() {

    String _dataDir("C:\\Samples\\");

    // 输出文件名的字符串
    String outputFileName("TextBlock_HideShow_MouseOverOut_out.pdf");

    // 创建带有文本的示例文档
    auto document = MakeObject<Document>();

    document->get_Pages()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>("将鼠标光标移动到此处以显示浮动文本"));
    document->Save(outputFileName);

    // 打开带有文本的文档
    auto document = MakeObject<Document>(outputFileName);

    // 创建 TextAbsorber 对象以查找所有匹配正则表达式的短语
    auto absorber = MakeObject<TextFragmentAbsorber>("将鼠标光标移动到此处以显示浮动文本");
    // 接受文档页面的吸收器
    document->get_Pages()->Accept(absorber);
    // 获取第一个提取的文本片段
    auto textFragments = absorber->get_TextFragments();
    auto fragment = textFragments->idx_get(1);

    // 在页面的指定矩形中为浮动文本创建隐藏文本字段
    auto floatingField = MakeObject<Aspose::Pdf::Forms::TextBoxField>(fragment->get_Page(), MakeObject<Rectangle>(100, 700, 220, 740));
    // 设置要显示为字段值的文本
    floatingField->set_Value(u"这是“浮动文本字段”。");
    // 我们建议在此场景下将字段设置为“只读”
    floatingField->set_ReadOnly(true);
    // 设置“隐藏”标志以使字段在打开文档时不可见
    floatingField->set_Flags(floatingField->get_Flags() | Aspose::Pdf::Annotations::AnnotationFlags::Hidden);

    // 设置唯一字段名称不是必须的但允许
    floatingField->set_PartialName (u"FloatingField_1");

    // 设置字段外观的特征不是必须的但会更好
    floatingField->set_DefaultAppearance(MakeObject<Aspose::Pdf::Annotations::DefaultAppearance>("Helv", 10, Color::get_Blue()));
    floatingField->get_Characteristics()->set_Background (System::Drawing::Color::get_LightBlue());
    floatingField->get_Characteristics()->set_Border (System::Drawing::Color::get_DarkBlue());
    floatingField->set_Border(MakeObject<Aspose::Pdf::Annotations::Border>(floatingField));
    floatingField->get_Border()->set_Width (1);
    floatingField->set_Multiline (true);

    // 将文本字段添加到文档中
    document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(floatingField));

    // 在文本片段位置创建不可见按钮
    auto buttonField = MakeObject<Aspose::Pdf::Forms::ButtonField>(fragment->get_Page(), fragment->get_Rectangle());
    // 为指定字段（注释）和不可见标志创建新的隐藏动作。
    // （如果您在上面指定了浮动字段的名称，也可以通过名称引用它。）
    // 在不可见按钮字段上添加鼠标进入/退出动作
    buttonField->get_Actions()->set_OnEnter(MakeObject<Aspose::Pdf::Annotations::HideAction>(floatingField, false));
    buttonField->get_Actions()->set_OnExit(MakeObject<Aspose::Pdf::Annotations::HideAction>(floatingField));

    // 将按钮字段添加到文档中
    document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(buttonField));

    // 保存文档
    document->Save(outputFileName);
}
```