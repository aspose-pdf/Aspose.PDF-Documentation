---
title: 用C++替换PDF中的文本
linktitle: 替换PDF中的文本
type: docs
weight: 40
url: /cpp/replace-text-in-pdf/
description: 了解有关从PDF中替换和删除文本的各种方法。Aspose.PDF允许在特定区域或使用正则表达式替换文本。
lastmod: "2021-12-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

有时候，需要在PDF文档中更正或替换文本。试图手动完成这项任务将是一项艰巨的任务，因此这里是解决该问题的方法。

坦率地说，编辑PDF文件并不是一件容易的事情。因此，当您需要在编辑PDF文件时将一个单词替换为另一个单词时，这将是非常困难的，因为这将花费您很长时间。此外，您可能会遇到许多输出问题，例如格式化或字体损坏。如果您想轻松地在PDF文件中查找和替换文本，我们建议您使用Aspose.Pdf库软件，因为它可以在几分钟内完成这项工作。

在本文中，我们将向您展示如何使用Aspose.PDF for C++成功查找和替换PDF文件中的文本。

## 在 PDF 文档的所有页面中替换文本

{{% alert color="primary" %}}

您可以尝试使用 Aspose.PDF 在文档中查找并替换文本，并在此[链接](https://products.aspose.app/pdf/redaction)在线获取结果

{{% /alert %}}

为了在 PDF 文档的所有页面中替换文本，您首先需要使用 TextFragmentAbsorber 来查找您想要替换的特定短语。之后，您需要遍历所有的 TextFragments 以替换文本并更改任何其他属性。一旦完成这些操作，您只需使用 Document 对象的 Save 方法保存输出 PDF。以下代码片段向您展示了如何在 PDF 文档的所有页面中替换文本。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ReplaceTextOnAllPages() {

    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // 创建 TextAbsorber 对象以查找输入搜索短语的所有实例
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("Web");

    // 接受文档第一页的吸收器
    document->get_Pages()->Accept(textFragmentAbsorber);

    // 将提取的文本碎片放入集合中
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // 遍历碎片
    for (auto textFragment : textFragmentCollection) {
        // 更新文本和其他属性
        textFragment->set_Text(u"World Wide Web");
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));
        textFragment->get_TextState()->set_FontSize(12);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
    }
    // 保存更新后的 PDF 文件
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

## 替换特定页面区域的文本

为了替换特定页面区域的文本，首先，我们需要实例化 `TextFragmentAbsorber` 对象，使用 `TextSearchOptions.Rectangle` 属性指定页面区域，然后遍历所有的 `TextFragments` 来替换文本。一旦这些操作完成，我们只需要使用 `Document` 对象的 `Save` 方法保存输出的 PDF。以下代码片段展示了如何替换 PDF 文档所有页面的文本。

```cpp
void ReplaceTextInParticularRegion() {

    String _dataDir("C:\\Samples\\");

    // 加载 PDF 文件
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // 实例化 TextFragment Absorber 对象
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("PDF");

    // 在页面边界内搜索文本
    textFragmentAbsorber->get_TextSearchOptions()->set_LimitToPageBounds(true);

    // 为 TextSearch Options 指定页面区域
    textFragmentAbsorber->get_TextSearchOptions()->set_Rectangle(new Rectangle(100, 700, 400, 770));

    // 从 PDF 文件的第一页搜索文本
    document->get_Pages()->idx_get(1)->Accept(textFragmentAbsorber);

    // 遍历各个 TextFragment
    for (auto tf : textFragmentAbsorber->get_TextFragments()) {
        // 用 "---" 替换文本
        tf->set_Text(u"---");
    }

    // 保存更新后的 PDF 文件
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

## 根据正则表达式替换文本

如果你想根据正则表达式替换一些短语，首先需要使用 TextFragmentAbsorber 找到所有符合该特定正则表达式的短语。你需要将正则表达式作为参数传递给 TextFragmentAbsorber 构造函数。你还需要创建一个 TextSearchOptions 对象来指定是否使用正则表达式。一旦你在 TextFragments 中得到匹配的短语，你需要遍历所有这些短语并根据需要进行更新。最后，你需要使用 Document 对象的 Save 方法保存更新后的 PDF。以下代码片段向你展示了如何根据正则表达式替换文本。

```cpp
void ReplaceTextWithRegularExpression() {

    String _dataDir("C:\\Samples\\");

    // 加载 PDF 文件
    auto document = MakeObject<Document>(_dataDir + u"Sample.pdf");
    // 创建 TextAbsorber 对象以查找所有输入搜索短语的实例
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("\\d{4}-\\d{4}");
    // 如 1999-2000

    // 设置文本搜索选项以指定正则表达式使用
    auto textSearchOptions = new TextSearchOptions(true);
    textFragmentAbsorber->set_TextSearchOptions(textSearchOptions);

    // 为文档的第一页接受吸收器
    document->get_Pages()->Accept(textFragmentAbsorber);

    // 将提取的文本片段放入集合
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // 遍历片段
    for (auto textFragment : textFragmentCollection) {
        // 更新文本和其他属性
        textFragment->set_Text(u"ABCD-EFGH");
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));
        textFragment->get_TextState()->set_FontSize(12);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
    }

    // 保存更新后的 PDF 文件
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

## 替换现有 PDF 文件中的字体

Aspose.PDF for C++ 支持在 PDF 文档中替换文本的功能。然而，有时您可能只需要替换 PDF 文档中使用的字体。因此，与其替换文本，不如仅替换使用的字体。TextFragmentAbsorber 构造函数的一个重载接受 TextEditOptions 对象作为参数，我们可以使用 TextEditOptions.FontReplace 枚举中的 RemoveUnusedFonts 值来实现我们的需求。以下代码片段显示了如何替换 PDF 文档中的字体。

```cpp
void ReplaceFonts() {
    String _dataDir("C:\\Samples\\");

    // 实例化 Document 对象
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // 搜索文本片段并设置编辑选项为移除未使用的字体
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>(
        MakeObject<TextEditOptions>(TextEditOptions::FontReplace::RemoveUnusedFonts));

    // 接受文档所有页面的吸收器
    document->get_Pages()->Accept(textFragmentAbsorber);

    // 遍历所有的 TextFragments
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();
    for (auto textFragment : textFragmentCollection) {
        String fontName = textFragment->get_TextState()->get_Font()->get_FontName();
        // 如果字体名称是 ArialMT，则将其替换为 Arial
        if (fontName.Equals(u"ArialMT")) {
            textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
        }
    }

    // 保存更新后的 PDF 文件
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

在下一个代码片段中，您将看到如何在替换文本时使用非英文字体：

```cpp
void UseNonEnglishFontWhenReplacingText() {

    String _dataDir("C:\\Samples\\");

    // 实例化 Document 对象
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // 将每个“PDF”单词更改为某些特定字体的日文文本
    // 可能已在操作系统中安装的 MSGothic
    // 另外，它可能是支持象形文字的其他字体
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("PDF");

    // 创建文本搜索选项实例
    auto searchOptions = MakeObject<TextSearchOptions>(true);
    textFragmentAbsorber->set_TextSearchOptions(searchOptions);

    // 接受文档所有页面的吸收器
    document->get_Pages()->Accept(textFragmentAbsorber);

    // 将提取的文本片段放入集合中
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // 遍历片段
    for (auto textFragment : textFragmentCollection) {
        // 更新文本和其他属性
        textFragment->set_Text(u"ファイル");
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"TakaoMincho"));
        textFragment->get_TextState()->set_FontSize(12);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
    }
    // 保存更新后的文档
    document->Save(_dataDir + u"Japanese_Text.pdf");
}
```

## 文本替换应自动重新排列页面内容

Aspose.PDF for C++ 支持在 PDF 文件中查找和替换文本。然而，最近一些客户在替换文本时遇到了问题，当特定的 TextFragment 被替换为较小的内容时，结果 PDF 中显示了一些额外的空白，或者如果 TextFragment 被替换为更长的字符串，则单词会重叠现有页面内容。因此，需要引入一种机制，在替换 PDF 文档中的文本后重新排列其内容。

为了解决上述情况，Aspose.PDF for C++ 已进行了改进，以便在 PDF 文件中替换文本时不会发生此类问题。以下代码片段演示了如何在 PDF 文件中替换文本，并且页面内容应自动重新排序。

```cpp
void RearrangeContent() {
    String _dataDir("C:\\Samples\\");

    // 实例化 Document 对象
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // 使用正则表达式创建 TextFragment Absorber 对象
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("[PDF,Web]");

    auto textSearchOptions = MakeObject<TextSearchOptions>(true);
    textFragmentAbsorber->set_TextSearchOptions(textSearchOptions);

    // 您还可以指定 ReplaceAdjustment.WholeWordsHyphenation 选项，
    // 如果替换后当前行变得过长或过短，则在下一行或当前行换行：
    //textFragmentAbsorber->get_TextReplaceOptions()->set_ReplaceAdjustmentAction(TextReplaceOptions::ReplaceAdjustment::WholeWordsHyphenation);

    // 接受文档所有页面的 absorber
    document->get_Pages()->Accept(textFragmentAbsorber);

    // 将提取的文本片段获取到集合中
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // 替换每个 TextFragment
    for (auto textFragment : textFragmentCollection) {
        // 设置被替换文本片段的字体
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
        // 设置字体大小
        textFragment->get_TextState()->set_FontSize(10);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
        // 用比占位符更大的字符串替换文本
        textFragment->set_Text(u"This is a larger string for the testing of this feature");
    }
    // 保存结果 PDF
    document->Save(_dataDir + u"RearrangeContentsUsingTextReplacement_out.pdf");
}
```

## PDF创建期间渲染可替换符号

可替换符号是在文本字符串中可以在运行时替换为相应内容的特殊符号。目前Aspose.PDF命名空间的新文档对象模型支持的可替换符号有 `$P`，`$p`，`\n`，`\r`。`$p` 和 `$P` 用于处理运行时的页码。`$p` 被替换为当前段落类所在页的页码。`$P` 被替换为文档中的总页数。当将 `TextFragment` 添加到PDF文档的段落集合时，它不支持文本内的换行。然而，为了添加带换行的文本，请使用带有 `TextParagraph` 的 `TextFragment`：

- 在TextFragment中使用 "\r\n" 或 Environment.NewLine，而不是单独的 "\n"；
- 创建一个TextParagraph对象。它将添加带有分行的文本；
- 使用TextParagraph.AppendLine添加TextFragment；
- 使用TextBuilder.AppendParagraph添加TextParagraph。

## 可替换符号在页眉/页脚区域

可替换符号也可以放置在 PDF 文件的页眉/页脚部分。查看以下代码片段以了解如何将可替换符号添加到页脚部分。

```csharp
void ReplaceableSymbolsInHeaderFooterArea() {

    auto document = MakeObject<Document>();
    auto page = doc.getPages().add();

    auto marginInfo = MakeObject<MarginInfo>();
    marginInfo->set_Top(90);
    marginInfo->set_Bottom(50);
    marginInfo->set_Left(50);
    marginInfo->set_Right(50);

    // 将 marginInfo 实例分配给 PageInfo 的 Margin 属性
    page.getPageInfo()->set_Margin(marginInfo);

    auto hfFirst = MakeObject<HeaderFooter>();
    page->set_Header(hfFirst);
    hfFirst->get_Margin()->set_Left(50);
    hfFirst->get_Margin()->set_Right(50);

    // 实例化一个文本段落，将存储要显示为页眉的内容
    auto t1 = MakeObject<TextFragment>("report title");
    t1->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    t1->get_TextState()->set_FontSize(16);
    t1->get_TextState()->set_ForegroundColor(Color::get_Black());
    t1->get_TextState()->set_FontStyle(FontStyles::Bold);
    t1->get_TextState()->set_HorizontalAlignment(HorizontalAlignment::Center);
    t1->get_TextState()->set_LineSpacing(5.0f);
    hfFirst->get_Paragraphs()->Add(t1);

    auto t2 = MakeObject<TextFragment>("Report_Name");
    t2->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    t2->get_TextState()->set_ForegroundColor(Color::get_Black());
    t2->get_TextState()->set_HorizontalAlignment(HorizontalAlignment::Center);
    t2->get_TextState()->set_LineSpacing(5.0f);
    t2->get_TextState()->set_FontSize(12);
    hfFirst->get_Paragraphs()->Add(t2);

    // 为该部分创建一个 HeaderFooter 对象
    auto hfFoot = MakeObject<HeaderFooter>();

    // 将 HeaderFooter 对象设置为奇数和偶数页脚
    page->set_Footer(hfFoot);
    hfFoot->get_Margin()->set_Left(50);
    hfFoot->get_Margin()->set_Right(50);

    // 添加包含当前页码的文本段落
    auto t3 = MakeObject<TextFragment>("Generated on test date");
    auto t4 = MakeObject<TextFragment>("report name ");
    auto t5 = MakeObject<TextFragment>("Page $p of $P");

    // 实例化一个表格对象
    auto tab2 = MakeObject<Table>();

    // 将表格添加到所需部分的段落集合中
    hfFoot->get_Paragraphs()->Add(tab2);

    // 设置表格的列宽
    tab2->set_ColumnWidths(u"165 172 165");

    // 在表格中创建行，然后在行中创建单元格
    auto row3 = tab2->get_Rows()->Add();

    row3->get_Cells()->Add();
    row3->get_Cells()->Add();
    row3->get_Cells()->Add();

    // 将文本的垂直对齐方式设置为居中对齐
    row3->get_Cells()->idx_get(0)->set_Alignment(HorizontalAlignment::Left);
    row3->get_Cells()->idx_get(1)->set_Alignment(HorizontalAlignment::Center);
    row3->get_Cells()->idx_get(2)->set_Alignment(HorizontalAlignment::Right);

    row3->get_Cells()->idx_get(0)->get_Paragraphs()->Add(t3);
    row3->get_Cells()->idx_get(1)->get_Paragraphs()->Add(t4);
    row3->get_Cells()->idx_get(2)->get_Paragraphs()->Add(t5);

    auto table = MakeObject<Table>();

    table->set_ColumnWidths(u"33% 33% 34%");
    table->set_DefaultCellPadding(new MarginInfo());
    table->get_DefaultCellPadding()->set_Top(10);
    table->get_DefaultCellPadding()->set_Bottom(10);

    // 将表格添加到所需部分的段落集合中
    page.getParagraphs().add(table);

    // 使用 BorderInfo 对象设置默认单元格边框
    table->set_DefaultCellBorder(MakeObject<BorderInfo>(BorderSide::All, 0.1f));

    // 使用另一个自定义 BorderInfo 对象设置表格边框
    table->set_Border(MakeObject<BorderInfo>(BorderSide::All, 1.0f));

    table->set_RepeatingRowsCount(1);

    // 在表格中创建行，然后在行中创建单元格
    auto row1 = table->get_Rows()->Add();

    row1->get_Cells()->Add(u"col1");
    row1->get_Cells()->Add(u"col2");
    row1->get_Cells()->Add(u"col3");

    String CRLF ("\r\n");

    for (int i = 0; i <= 10; i++) {
        auto row = table->get_Rows()->Add();
        row->set_IsRowBroken(true);
        for (int c = 0; c <= 2; c++) {
            SharedPtr<Cell> c1;
            if (c == 2)
                c1 = row->get_Cells()->Add(
                    u"Aspose.Total for C++ is a compilation of every Java component offered by Aspose. It is compiled on a"
                    + CRLF
                    + u"daily basis to ensure it contains the most up to date versions of each of our Java components. "
                    + CRLF
                    + u"daily basis to ensure it contains the most up to date versions of each of our Java components. "
                    + CRLF
                    + u"Using Aspose.Total for C++ developers can create a wide range of applications.");
            else
                c1 = row->get_Cells()->Add(u"item1" + c);
            c1->set_Margin(new MarginInfo());
            c1->get_Margin()->set_Left(30);
            c1->get_Margin()->set_Top(10);
            c1->get_Margin()->set_Bottom(10);
        }
    }

    _dataDir = _dataDir + "ReplaceableSymbolsInHeaderFooter_out.pdf";
    doc.save(_dataDir);
}
```

## 从 PDF 文档中删除所有文本

### 使用操作符删除所有文本

在某些文本操作中，您需要从 PDF 文档中删除所有文本，为此，您通常需要将找到的文本设置为空字符串值。事实是更改一组文本片段的文本会导致一些操作来检查和调整文本的位置。这些操作在文本编辑脚本中是必需的。困难在于您无法确定在循环中处理的脚本中将删除多少文本块。

因此，我们建议在从 PDF 页面中删除所有文本的场景中使用不同的方法。

以下代码片段展示了如何快速解决此任务。

```cpp
void RemoveAllTextUsingOperators() {

    String _dataDir("C:\\Samples\\");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // 遍历 PDF 文档的所有页面
    for (int i = 1; i <= document->get_Pages()->get_Count(); i++) {
        auto page = document->get_Pages()->idx_get(i);
        auto operatorSelector = MakeObject<OperatorSelector>(MakeObject<Aspose::Pdf::Operators::TextShowOperator>());
        // 选择页面上的所有文本
        page->get_Contents()->Accept(operatorSelector);
        // 删除所有文本
        page->get_Contents()->Delete(operatorSelector->get_Selected());
    }
    // 保存文档
    document->Save(_dataDir + u"RemoveAllText_out.pdf");
}
```