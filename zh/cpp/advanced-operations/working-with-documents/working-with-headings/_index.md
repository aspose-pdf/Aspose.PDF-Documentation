---
title: 在PDF中使用标题
type: docs
weight: 90
url: zh/cpp/working-with-headings/
lastmod: "2021-11-11"
description: 使用C++在您的PDF文档中创建标题编号。Aspose.PDF for C++展示了不同种类的编号样式。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 在标题中应用编号样式

文档中的任何文本都以标题开头。标题是内容不可或缺的一部分，无论风格和主题如何。
标题有助于吸引对文本的注意，并帮助用户在文档中找到他们需要的信息，提高可读性和视觉感知。使用标题样式，您还可以快速创建目录，改变文档结构。
所以，让我们看看如何使用Aspose.PDF for C++库来处理标题。

[Aspose.PDF for C++](/pdf/cpp/) 提供了许多预定义的编号样式。 这些预定义的编号样式存储在一个枚举中，NumberingStyle。NumberingStyle枚举的预定义值及其描述如下：

|**标题类型**|**描述**|
| :- | :- |
|NumeralsArabic|阿拉伯类型，例如，1,1.1,...|
|NumeralsRomanUppercase|罗马大写类型，例如，I,I.II,...|
|NumeralsRomanLowercase|罗马小写类型，例如，i,i.ii,...|
|LettersUppercase|英语大写类型，例如，A,A.B,...|
|LettersLowercase|英语小写类型，例如，a,a.b,...|

**Aspose.PDF.Heading**类的**Style**属性用于设置标题的编号样式。

|**图：预定义编号样式**|
| :- |
要获得上图所示的输出，源代码示例如下。

```cpp
void WorkingWithHeadingsInPDF() {
    // 路径名字符串
    String _dataDir("C:\\Samples\\");

    // 输入文件名字符串
    String outputFileName("ApplyNumberStyle_out.pdf");

    // 打开文档
    auto document = MakeObject<Document>();

    document->get_PageInfo()->set_Width(612.0);
    document->get_PageInfo()->set_Height(792.0);
    document->get_PageInfo()->set_Margin (MakeObject<MarginInfo>());
    document->get_PageInfo()->get_Margin()->set_Left(72);
    document->get_PageInfo()->get_Margin()->set_Right(72);
    document->get_PageInfo()->get_Margin()->set_Top (72);
    document->get_PageInfo()->get_Margin()->set_Bottom (72);
            
    auto pdfPage = document->get_Pages()->Add();
    pdfPage->get_PageInfo()->set_Width (612.0);
    pdfPage->get_PageInfo()->set_Height (792.0);
    pdfPage->get_PageInfo()->set_Margin(MakeObject<MarginInfo>());
    pdfPage->get_PageInfo()->get_Margin()->set_Left(72);
    pdfPage->get_PageInfo()->get_Margin()->set_Right(72);
    pdfPage->get_PageInfo()->get_Margin()->set_Top(72);
    pdfPage->get_PageInfo()->get_Margin()->set_Bottom(72);

    auto floatBox = MakeObject<FloatingBox>();
    floatBox->set_Margin(pdfPage->get_PageInfo()->get_Margin());

    pdfPage->get_Paragraphs()->Add(floatBox);

    auto textFragment = MakeObject<TextFragment>();
    auto segment = MakeObject<TextSegment>();

    auto heading = MakeObject<Heading>(1);
    heading->set_IsInList(true);
    heading->set_StartNumber(1);
    heading->set_Text (u"List 1");
    heading->set_Style(NumberingStyle::NumeralsRomanLowercase);
    heading->set_IsAutoSequence(true);

    floatBox->get_Paragraphs()->Add(heading);

    auto heading2 = MakeObject<Heading>(1);
    heading2->set_IsInList (true);
    heading2->set_StartNumber(13);
    heading2->set_Text (u"List 2");
    heading2->set_Style(NumberingStyle::NumeralsRomanLowercase);
    heading2->set_IsAutoSequence(true);;

    floatBox->get_Paragraphs()->Add(heading2);

    auto heading3 = MakeObject<Heading>(2);
    heading3->set_IsInList (true);
    heading3->set_StartNumber(1);
    heading3->set_Text (u"the value, as of the effective date of the plan, of property to be distributed under the plan onaccount of each allowed");
    heading3->set_Style(NumberingStyle::LettersLowercase);
    heading3->set_IsAutoSequence(true);

    floatBox->get_Paragraphs()->Add(heading3); 

    // 保存合并的输出文件
    document->Save(_dataDir + outputFileName);
}
```