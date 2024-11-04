---
title: 在PDF中旋转文本使用C++
linktitle: 在PDF中旋转文本
type: docs
weight: 50
url: /cpp/rotate-text-inside-pdf/
description: 了解将文本旋转到PDF的不同方法。Aspose.PDF允许您将文本旋转到任意角度，旋转文本片段或整个段落。
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 使用旋转属性在PDF中旋转文本

通过使用[TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/)类的Rotation属性，您可以在各种角度旋转文本。文本旋转可以用于文档生成的不同场景。您可以以度为单位指定旋转角度，以根据您的要求旋转文本。请查看以下不同场景，您可以在其中实现文本旋转。

## 使用TextFragment和TextBuilder实现旋转

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ImplementRotationUsingTextFragmentAndTextBuilder() {

    String _dataDir("C:\\Samples\\");

    // 初始化文档对象
    auto document = MakeObject<Document>();
    // 获取特定页面
    auto page = document->get_Pages()->Add();
    // 创建文本片段
    auto textFragment1 = MakeObject<TextFragment>("main text");
    textFragment1->set_Position(MakeObject<Position>(100, 600));

    // 设置文本属性
    textFragment1->get_TextState()->set_FontSize(12);
    textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // 创建旋转文本片段
    auto textFragment2 = MakeObject<TextFragment>("rotated text");
    textFragment2->set_Position(MakeObject<Position>(200, 600));
    // 设置文本属性
    textFragment2->get_TextState()->set_FontSize(12);
    textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    textFragment2->get_TextState()->set_Rotation(45);

    // 创建旋转文本片段
    auto textFragment3 = MakeObject<TextFragment>("rotated text");
    textFragment3->set_Position(MakeObject<Position>(300, 600));

    // 设置文本属性
    textFragment3->get_TextState()->set_FontSize(12);
    textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    textFragment3->get_TextState()->set_Rotation(90);

    // 创建TextBuilder对象
    auto textBuilder = MakeObject<TextBuilder>(page);
    // 将文本片段附加到PDF页面
    textBuilder->AppendText(textFragment1);
    textBuilder->AppendText(textFragment2);
    textBuilder->AppendText(textFragment3);

    // 保存文档
    document->Save(_dataDir + u"TextFragmentTests_Rotated1_out.pdf");
}
```

## 使用 TextParagraph 和 TextBuilder 实现旋转（旋转片段）

```cpp
void ImplementRotationUsingTextParagraphAndTextBuilder_RotatedFragments() {

    String _dataDir("C:\\Samples\\");

    // 初始化文档对象
    auto document = MakeObject<Document>();
    // 获取特定页面
    auto page = document->get_Pages()->Add();
    auto paragraph = MakeObject<TextParagraph>();
    paragraph->set_Position(MakeObject<Position>(200, 600));

    // 创建文本片段
    auto textFragment1 = MakeObject<TextFragment>("rotated text");
    // 设置文本属性
    textFragment1->get_TextState()->set_FontSize(12);
    textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    // 设置旋转
    textFragment1->get_TextState()->set_Rotation(45);

    // 创建文本片段
    auto textFragment2 = MakeObject<TextFragment>("main text");
    // 设置文本属性
    textFragment2->get_TextState()->set_FontSize(12);
    textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // 创建文本片段
    auto textFragment3 = MakeObject<TextFragment>("another rotated text");
    // 设置文本属性
    textFragment3->get_TextState()->set_FontSize(12);
    textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    // 设置旋转
    textFragment3->get_TextState()->set_Rotation(-45);

    // 将文本片段追加到段落中
    paragraph->AppendLine(textFragment1);
    paragraph->AppendLine(textFragment2);
    paragraph->AppendLine(textFragment3);
    // 创建 TextBuilder 对象
    auto textBuilder = MakeObject<TextBuilder>(page);
    // 将文本段落追加到 PDF 页面
    textBuilder->AppendParagraph(paragraph);
    // 保存文档
    document->Save(_dataDir + u"TextFragmentTests_Rotated2_out.pdf");

}
```

## 使用 TextFragment 和 Page.Paragraphs 实现旋转

```cpp
void ImplementRotationUsingTextFragmentAndPageParagraphs() {

    String _dataDir("C:\\Samples\\");

    // 初始化文档对象
    auto document = MakeObject<Document>();
    // 获取特定页面
    auto page = document->get_Pages()->Add();
    // 创建文本片段
    auto textFragment1 = MakeObject<TextFragment>("main text");
    // 设置文本属性
    textFragment1->get_TextState()->set_FontSize(12);
    textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // 创建文本片段
    auto textFragment2 = MakeObject<TextFragment>("rotated text");

    // 设置文本属性
    textFragment2->get_TextState()->set_FontSize(12);
    textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // 设置旋转
    textFragment2->get_TextState()->set_Rotation(315);

    // 创建文本片段
    auto textFragment3 = MakeObject<TextFragment>("rotated text");
    // 设置文本属性
    textFragment3->get_TextState()->set_FontSize(12);
    textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // 设置旋转
    textFragment3->get_TextState()->set_Rotation(270);
    page->get_Paragraphs()->Add(textFragment1);
    page->get_Paragraphs()->Add(textFragment2);
    page->get_Paragraphs()->Add(textFragment3);

    // 保存文档
    document->Save(_dataDir + u"TextFragmentTests_Rotated3_out.pdf");
}
```

## 使用 TextParagraph 和 TextBuilder 实现旋转（整个段落旋转）

```cpp
void ImplementRotationUsingTextParagraphAndTextBuilder() {

    String _dataDir("C:\\Samples\\");

    // 初始化文档对象
    auto document = MakeObject<Document>();
    // 获取特定页面
    auto page = document->get_Pages()->Add();
    for (int i = 0; i < 4; i++) {
        auto paragraph = MakeObject<TextParagraph>();
        paragraph->set_Position(MakeObject<Position>(200, 600));
        // 指定旋转
        paragraph->set_Rotation(i * 90 + 45);
        // 创建文本片段
        auto textFragment1 = MakeObject<TextFragment>("段落文本");
        // 创建文本片段
        textFragment1->get_TextState()->set_FontSize(12);
        textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
        textFragment1->get_TextState()->set_BackgroundColor(Color::get_LightGray());
        textFragment1->get_TextState()->set_ForegroundColor(Color::get_Blue());

        // 创建文本片段
        auto textFragment2 = MakeObject<TextFragment>("第二行文本");
        // 设置文本属性
        textFragment2->get_TextState()->set_FontSize(12);
        textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
        textFragment2->get_TextState()->set_BackgroundColor(Color::get_LightGray());
        textFragment2->get_TextState()->set_ForegroundColor(Color::get_Blue());

        // 创建文本片段
        auto textFragment3 = MakeObject<TextFragment>("还有一些更多的文本...");
        // 设置文本属性
        textFragment3->get_TextState()->set_FontSize(12);
        textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
        textFragment3->get_TextState()->set_BackgroundColor(Color::get_LightGray());
        textFragment3->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment3->get_TextState()->set_Underline(true);

        paragraph->AppendLine(textFragment1);
        paragraph->AppendLine(textFragment2);
        paragraph->AppendLine(textFragment3);
        // 创建 TextBuilder 对象
        auto textBuilder = MakeObject<TextBuilder>(page);
        // 将文本片段附加到 PDF 页面
        textBuilder->AppendParagraph(paragraph);
    }
    // 保存文档
    document->Save(_dataDir + u"TextFragmentTests_Rotated4_out.pdf");
}
```