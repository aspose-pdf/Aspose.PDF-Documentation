---
title: PDF Highlights Annotation using C++
linktitle: Highlights Annotation
type: docs
weight: 20
url: /cpp/highlights-annotation/
description: 标记注释在文档的文本中以高亮、下划线、删除线或波浪线的形式呈现。
lastmod: "2021-11-24"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

文本标记注释应在文档的文本中显示为高亮、下划线、删除线或波浪线。当打开时，它们应显示一个包含相应注释文本的弹出窗口。

您可以使用 PDF 查看器控件中提供的属性窗口编辑 PDF 中文本标记注释的属性。您可以更改文本标记注释的颜色、不透明度、作者和主题。

您可以使用 highlightSettings 属性获取或设置高亮注释设置。 highlightSettings属性用于设置高亮注释的颜色、不透明度、作者、主题、修改日期和isLocked属性。

也可以使用strikethroughSettings属性获取或设置删除线注释设置。strikethroughSettings属性用于设置删除线注释的颜色、不透明度、作者、主题、修改日期和isLocked属性。

下一个功能是使用underlineSettings属性获取或设置下划线注释的设置。underlineSettings属性用于设置下划线注释的颜色、不透明度、作者、主题、修改日期和isLocked属性。

## 添加文本标记注释

为了向PDF文档添加文本标记注释，我们需要执行以下操作：

1. 加载PDF文件 - 新建[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)对象。
1. 创建注释：

    - [HighlightAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.highlight_annotation)并设置参数（标题、颜色）。- [StrikeOutAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.strike_out_annotation) 并设置参数 (title, color)。
- [SquigglyAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.squiggly_annotation) 并设置参数 (title, color)。
- [UnderlineAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.underline_annotation) 并设置参数 (title, color)。

1. 然后我们应该将所有注释添加到页面。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void TextMarkupAnnotations::AddTextMarkupAnnotation()
{
    String _dataDir("C:\\Samples\\");

    try
    {
        // 加载PDF文件
        auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
        auto tfa = MakeObject<Aspose::Pdf::Text::TextFragmentAbsorber>(u"PDF");
        tfa->Visit(document->get_Pages()->idx_get(1));

        // 创建注释
        auto highlightAnnotation = MakeObject<Aspose::Pdf::Annotations::HighlightAnnotation>(
        document->get_Pages()->idx_get(1),
        tfa->get_TextFragments()->idx_get(1)->get_Rectangle());
        highlightAnnotation->set_Title(u"Aspose User");
        highlightAnnotation->set_Color(Color::get_LightGreen());

        auto strikeOutAnnotation = MakeObject<Aspose::Pdf::Annotations::StrikeOutAnnotation>(
        document->get_Pages()->idx_get(1),
        tfa->get_TextFragments()->idx_get(2)->get_Rectangle());
        strikeOutAnnotation->set_Title(u"Aspose User");
        strikeOutAnnotation->set_Color(Color::get_Blue());

        auto squigglyAnnotation = MakeObject<Aspose::Pdf::Annotations::SquigglyAnnotation>(
        document->get_Pages()->idx_get(1),
        tfa->get_TextFragments()->idx_get(3)->get_Rectangle());
        squigglyAnnotation->set_Title(u"Aspose User");
        squigglyAnnotation->set_Color(Color::get_Blue());

        auto underlineAnnotation = MakeObject<Aspose::Pdf::Annotations::UnderlineAnnotation>(
        document->get_Pages()->idx_get(1),
        tfa->get_TextFragments()->idx_get(4)->get_Rectangle());
        underlineAnnotation->set_Title(u"Aspose User");
        underlineAnnotation->set_Color(Color::get_Blue());

        // 将注释添加到页面
        document->get_Pages()->idx_get(1)->get_Annotations()->Add(highlightAnnotation);
        document->get_Pages()->idx_get(1)->get_Annotations()->Add(squigglyAnnotation);
        document->get_Pages()->idx_get(1)->get_Annotations()->Add(strikeOutAnnotation);
        document->get_Pages()->idx_get(1)->get_Annotations()->Add(underlineAnnotation);
        document->Save(_dataDir + u"sample_mod.pdf");
    }
    catch (Exception ex)
    {
        Console::WriteLine(ex->get_Message());
    }
}
```

如果您想突出显示多行片段，您应该使用高级示例：

```cpp
/// <summary>
/// 用于突出显示多行片段的高级示例
/// </summary>

System::SmartPtr<Aspose::Pdf::Annotations::HighlightAnnotation> HighLightTextFragment(
    System::SmartPtr<Aspose::Pdf::Page> page,
    System::SmartPtr<TextFragment> textFragment,
    System::SharedPtr<Color> color);

void TextMarkupAnnotations::AddHighlightAnnotationAdvanced()
{
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"sample_mod.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto tfa = MakeObject<TextFragmentAbsorber>(
        u"Adobe\\W+Acrobat\\W+Reader",
        MakeObject<Aspose::Pdf::Text::TextSearchOptions>(true));

    tfa->Visit(page);

    for (auto textFragment : tfa->get_TextFragments())
    {
        auto highlightAnnotation = HighLightTextFragment(page, textFragment, Color::get_Yellow());
        page->get_Annotations()->Add(highlightAnnotation);
    }
    document->Save(_dataDir + u"sample_mod.pdf");
}


System::SmartPtr<Aspose::Pdf::Annotations::HighlightAnnotation> HighLightTextFragment(
    System::SmartPtr<Aspose::Pdf::Page> page,
    System::SmartPtr<TextFragment> textFragment,
    System::SharedPtr<Color> color)
{
    if (textFragment->get_Segments()->get_Count() == 1)
    {
        auto ha = MakeObject<Aspose::Pdf::Annotations::HighlightAnnotation>
        (page, textFragment->get_Segments()->idx_get(1)->get_Rectangle());
        ha->set_Title(u"Aspose User");
        ha->set_Color(color);

        ha->set_Modified(DateTime::get_Now());

        auto quadPoints = MakeArray<System::SharedPtr<Point>>(4);

        quadPoints[0] = MakeObject<Point>(textFragment->get_Segments()->idx_get(1)->get_Rectangle()->get_LLX(),
        textFragment->get_Segments()->idx_get(1)->get_Rectangle()->get_URY());
        quadPoints[1] = MakeObject<Point>(textFragment->get_Segments()->idx_get(1)->get_Rectangle()->get_URX(),
        textFragment->get_Segments()->idx_get(1)->get_Rectangle()->get_URY());
        quadPoints[2] = MakeObject<Point>(textFragment->get_Segments()->idx_get(1)->get_Rectangle()->get_LLX(),
        textFragment->get_Segments()->idx_get(1)->get_Rectangle()->get_LLY());
        quadPoints[3] = MakeObject<Point>(textFragment->get_Segments()->idx_get(1)->get_Rectangle()->get_URX(),
        textFragment->get_Segments()->idx_get(1)->get_Rectangle()->get_LLY());
        ha->set_QuadPoints(quadPoints);
        return ha;
    }

    auto offset = 0;
    auto quadPoints = MakeArray<System::SharedPtr<Point>>(textFragment->get_Segments()->get_Count() * 4);

    for (auto segment : textFragment->get_Segments())
    {
        quadPoints[offset + 0] = MakeObject<Point>(segment->get_Rectangle()->get_LLX(), segment->get_Rectangle()->get_URY());
        quadPoints[offset + 1] = MakeObject<Point>(segment->get_Rectangle()->get_URX(), segment->get_Rectangle()->get_URY());
        quadPoints[offset + 2] = MakeObject<Point>(segment->get_Rectangle()->get_LLX(), segment->get_Rectangle()->get_LLY());
        quadPoints[offset + 3] = MakeObject<Point>(segment->get_Rectangle()->get_URX(), segment->get_Rectangle()->get_LLY());
        offset += 4;
    }

    double llx = quadPoints[0]->get_X();
    double lly = quadPoints[0]->get_Y();
    double urx = quadPoints[0]->get_X();
    double ury = quadPoints[0]->get_Y();
    for (auto &pt : quadPoints) {
        if (llx > pt->get_X())
        llx = pt->get_X();
        if (lly > pt->get_Y())
        lly = pt->get_Y();
        if (urx < pt->get_X())
        urx = pt->get_X();
        if (ury < pt->get_Y())
        ury = pt->get_Y();
    }

    auto ha = MakeObject<Aspose::Pdf::Annotations::HighlightAnnotation>
        (page, textFragment->get_Segments()->idx_get(1)->get_Rectangle());
    ha->set_Title(u"Aspose User");
    ha->set_Color(color);

    ha->set_Modified(DateTime::get_Now());

    ha->set_QuadPoints(quadPoints);
    return ha;
}


/// <summary>
/// 如何获取高亮文本
/// </summary>
void TextMarkupAnnotations::GetHighlightedText()
{
    String _dataDir("C:\\Samples\\");

    // 加载PDF文件
    auto document = MakeObject<Document>(_dataDir + u"sample_mod.pdf");
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::HighlightAnnotation>(page, Rectangle::get_Trivial()));

    for (auto ta : annotationSelector->get_Selected())
    {
        auto ha = System::DynamicCast<Aspose::Pdf::Annotations::HighlightAnnotation>(ta);
        Console::WriteLine(ha->GetMarkedText());
    }
}
```

## 获取文本标记注释

请尝试使用以下代码片段从 PDF 文档中获取文本标记注释。

```cpp
void TextMarkupAnnotations::GetTextMarkupAnnotation()
{
    String _dataDir("C:\\Samples\\");

    // 加载 PDF 文件
    auto document = MakeObject<Document>(_dataDir + u"sample_mod.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::HighlightAnnotation>(page, Rectangle::get_Trivial()));

    for (auto ta : annotationSelector->get_Selected())
    {
        Console::WriteLine(u"{0} {1}", ta->get_AnnotationType(), ta->get_Rect());
    }
}
```

## 删除文本标记注释

以下代码片段展示了如何从 PDF 文件中删除文本标记注释。

```cpp
void TextMarkupAnnotations::DeleteTextMarkupAnnotation() {

    String _dataDir("C:\\Samples\\");

    // 加载 PDF 文件
    auto document = MakeObject<Document>(_dataDir + u"sample_mod.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector1 = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::HighlightAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector1);
    auto annotationSelector2 = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::SquigglyAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector2);

    for (auto ta : annotationSelector1->get_Selected()) {
        page->get_Annotations()->Delete(ta);
    }
    for (auto ta : annotationSelector2->get_Selected()) {
        page->get_Annotations()->Delete(ta);
    }
    document->Save(_dataDir + u"sample_del.pdf");
}
```