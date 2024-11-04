---
title: 从PDF文档页面搜索并获取文本
linktitle: 搜索并获取文本
type: docs
weight: 60
url: /cpp/search-and-get-text-from-pdf/
description: 本文解释了如何使用各种工具从PDF文档中搜索并获取文本。我们可以使用正则表达式从特定页面或整个页面进行搜索。
lastmod: "2021-12-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 从PDF文档的所有页面搜索并获取文本

[TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment_absorber/) 类允许您从PDF文档的所有页面中找到与特定短语匹配的文本。为了从整个文档中搜索文本，您需要调用 [Pages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) 集合的 Accept 方法。'Accept' 方法将 TextFragmentAbsorber 对象作为参数，返回一个 TextFragment 对象的集合。

以下代码片段向您展示了如何从所有页面中搜索文本。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void SearchAndGetTextFromAllThePagesOfPDFDocument() {
    String _dataDir("C:\\Samples\\");

    auto document = new Document(_dataDir + u"sample.pdf");

    // 创建 TextAbsorber 对象以查找所有输入搜索短语的实例
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("document");

    // 接受所有页面的吸收器
    document->get_Pages()->Accept(textFragmentAbsorber);

    // 将提取的文本片段放入集合中
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // 遍历片段
    for (auto textFragment : textFragmentCollection) {
        Console::WriteLine(u"文本 :- {0}", textFragment->get_Text());
        Console::WriteLine(u"位置 :- {0}", textFragment->get_Position());
        Console::WriteLine(u"X 缩进 :- {0}", textFragment->get_Position()->get_XIndent());
        Console::WriteLine(u"Y 缩进 :- {0}", textFragment->get_Position()->get_YIndent());
        Console::WriteLine(u"字体 - 名称 :- {0}", textFragment->get_TextState()->get_Font()->get_FontName());
        Console::WriteLine(u"字体 - 是否可访问 :- {0}", textFragment->get_TextState()->get_Font()->get_IsAccessible());
        Console::WriteLine(u"字体 - 是否嵌入 :- {0}", textFragment->get_TextState()->get_Font()->get_IsEmbedded());
        Console::WriteLine(u"字体 - 是否子集 :- {0}", textFragment->get_TextState()->get_Font()->get_IsSubset());
        Console::WriteLine(u"字体大小 :- {0}", textFragment->get_TextState()->get_FontSize());
        Console::WriteLine(u"前景色 :- {0}", textFragment->get_TextState()->get_ForegroundColor());
    }
}
```

## Search and Get Text from all pages using Regular Expression

TextFragmentAbsorber 帮助您根据正则表达式从所有页面中搜索和检索文本。 首先，您需要将正则表达式作为短语传递给 [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment_absorber/) 构造函数。之后，您必须设置 TextFragmentAbsorber 对象的 [TextSearchOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_search_options/) 属性。此属性需要 TextSearchOptions 对象，并且您需要在创建新对象时将 true 作为参数传递给其构造函数。由于您希望从所有页面检索匹配的文本，因此需要调用 Pages 集合的 Accept 方法。[TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment_absorber/) 返回一个 TextFragmentCollection，其中包含与正则表达式指定的条件匹配的所有片段。以下代码片段向您展示如何基于正则表达式搜索并从所有页面获取文本。

```cpp
void SearchAndGetTextFromPagesUsingRegularExpression()
{
    String _dataDir("C:\\Samples\\");

    auto document = new Document(_dataDir + u"sample.pdf");

    // Create TextAbsorber object to find all instances of the input search phrase
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>(u"\\d{4}-\\d{4}"); // like 1999-2000

    // Set text search option to specify regular expression usage
    auto textSearchOptions = MakeObject<TextSearchOptions>(true);
    textFragmentAbsorber->set_TextSearchOptions(textSearchOptions);

    // Accept the absorber for first page of document
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Get the extracted text fragments into collection
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Loop through the fragments
    for (auto textFragment : textFragmentCollection) {
        Console::WriteLine(u"Text :- {0}", textFragment->get_Text());
        Console::WriteLine(u"Position :- {0}", textFragment->get_Position());
        Console::WriteLine(u"XIndent :- {0}", textFragment->get_Position()->get_XIndent());
        Console::WriteLine(u"YIndent :- {0}", textFragment->get_Position()->get_YIndent());
        Console::WriteLine(u"Font - Name :- {0}", textFragment->get_TextState()->get_Font()->get_FontName());
        Console::WriteLine(u"Font - IsAccessible :- {0}", textFragment->get_TextState()->get_Font()->get_IsAccessible());
        Console::WriteLine(u"Font - IsEmbedded - {0}", textFragment->get_TextState()->get_Font()->get_IsEmbedded());
        Console::WriteLine(u"Font - IsSubset :- {0}", textFragment->get_TextState()->get_Font()->get_IsSubset());
        Console::WriteLine(u"Font Size :- {0}", textFragment->get_TextState()->get_FontSize());
        Console::WriteLine(u"Foreground Color :- {0}", textFragment->get_TextState()->get_ForegroundColor());
    }
}
```