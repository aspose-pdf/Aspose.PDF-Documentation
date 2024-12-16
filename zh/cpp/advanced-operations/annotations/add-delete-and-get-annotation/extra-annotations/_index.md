---
title: 额外注释使用C++
linktitle: 额外注释
type: docs
weight: 60
url: /zh/cpp/extra-annotations/
description: 本节描述如何从PDF文档中添加、获取和删除额外类型的注释。
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 如何在现有PDF文件中添加插入符注释

插入符注释是一个表示文本编辑的符号。插入符注释也是标记注释，因此插入符类派生自标记类，并且还提供获取或设置插入符注释属性和重置插入符注释外观流程的功能。

创建插入符注释的步骤：

1. 加载PDF文件 - new [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. 创建新的[插入符注释](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.caret_annotation/)并设置插入符参数（新矩形、标题、主题、标志、颜色、宽度、起始样式和结束样式）。此注释用于指示文本的插入。
1. 创建新的[插入符注释](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.caret_annotation/)并设置插入符参数（新矩形、标题、主题、标志、颜色、宽度、起始样式和结束样式）。此注释用于指示文本的替换。
1. 创建新的[删除线注释](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.strike_out_annotation/)并设置参数（新矩形、标题、颜色、新四边形点和新点、主题、回复对象、回复类型）。
1. 然后我们可以将注释添加到页面。

以下代码片段显示了如何将插入符注释添加到PDF文件：

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void MarkupAnnotations::AddCaretAnnotation() {
    String _dataDir("C:\\Samples\\");

    // 加载PDF文件
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    // 此注释用于指示文本的插入
    auto caretAnnotation1 = MakeObject<CaretAnnotation>(
        document->get_Pages()->idx_get(1),
        MakeObject<Rectangle>(299.988, 713.664, 308.708, 720.769));
    caretAnnotation1->set_Title(u"Aspose User");
    caretAnnotation1->set_Subject(u"Inserted text 1");
    caretAnnotation1->set_Flags(AnnotationFlags::Print);
    caretAnnotation1->set_Color(Color::get_Blue());

    // 此注释用于指示文本的替换
    auto caretAnnotation2 = MakeObject<CaretAnnotation>(
        document->get_Pages()->idx_get(1),
        new Rectangle(361.246, 727.908, 370.081, 735.107));

    caretAnnotation2->set_Title(u"Aspose User");
    caretAnnotation2->set_Flags(AnnotationFlags::Print);
    caretAnnotation2->set_Subject(u"Inserted text 2");
    caretAnnotation2->set_Color(Color::get_Blue());

    auto strikeOutAnnotation = MakeObject<StrikeOutAnnotation>(
        document->get_Pages()->idx_get(1),
        MakeObject<Rectangle>(318.407, 727.826, 368.916, 740.098));

    strikeOutAnnotation->set_Color(Color::get_Blue());

    strikeOutAnnotation->set_QuadPoints(
        MakeArray<System::SharedPtr<Point>>({
            MakeObject<Point>(321.66, 739.416),
            MakeObject<Point>(365.664, 739.416),
            MakeObject<Point>(321.66, 728.508),
            MakeObject<Point>(365.664, 728.508) }));

    strikeOutAnnotation->set_Subject(u"Cross-out");
    strikeOutAnnotation->set_InReplyTo(caretAnnotation2);
    strikeOutAnnotation->set_ReplyType(ReplyType::Group);

    document->get_Pages()->idx_get(1)->get_Annotations()->Add(caretAnnotation1);
    document->get_Pages()->idx_get(1)->get_Annotations()->Add(caretAnnotation2);
    document->get_Pages()->idx_get(1)->get_Annotations()->Add(strikeOutAnnotation);

    document->Save(_dataDir + u"sample_caret.pdf");
}
```
### 获取插入符号注释

请尝试使用以下代码片段在 PDF 文档中获取插入符号注释

```cpp
void MarkupAnnotations::GetCaretAnnotation() {

    String _dataDir("C:\\Samples\\");
    // 加载 PDF 文件
    auto document = MakeObject<Document>(_dataDir + u"sample_caret.pdf");

    // 使用 AnnotationSelector 过滤注释
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<CaretAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto caretAnnotations = annotationSelector->get_Selected();

    // 打印结果
    for (auto ca : caretAnnotations) {
        Console::WriteLine(ca->get_Rect());
    }
}
```

### 删除插入符号注释

以下代码片段显示了如何从 PDF 文件中删除插入符号注释。

```cpp

void MarkupAnnotations::DeleteCaretAnnotation() {

    String _dataDir("C:\\Samples\\");
    // 加载 PDF 文件
    auto document = MakeObject<Document>(_dataDir + u"sample_caret.pdf");

    // 使用 AnnotationSelector 过滤注释
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<CaretAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto caretAnnotations = annotationSelector->get_Selected();

    // 删除注释
    for (auto ca : caretAnnotations) {
        document->get_Pages()->idx_get(1)->get_Annotations()->Delete(ca);
    }
    document->Save(_dataDir + u"sample_caret_del.pdf");
}
```

## 如何添加链接注释

[链接注释](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation) 是一个超文本链接，指向文档中其他位置的目标或要执行的操作。

链接是可以放置在页面任何位置的矩形区域。每个链接都有一个与之关联的 PDF 操作。当用户点击此链接的区域时，将执行此操作。

以下代码片段展示了如何使用电话号码示例向 PDF 文件添加链接注释：

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddLinkAnnotation() {
    String _dataDir("C:\\Samples\\");

    // 加载 PDF 文件
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    auto page = document->get_Pages()->idx_get(1);

    // 创建 TextFragmentAbsorber 对象以查找电话号码
    auto textFragmentAbsorber = MakeObject<Aspose::Pdf::Text::TextFragmentAbsorber>("678-555-0103");

    // 仅接受第 1 页的吸收器
    page->Accept(textFragmentAbsorber);

    auto phoneNumberFragment = textFragmentAbsorber->get_TextFragments()->idx_get(1);

    // 创建链接注释并设置操作以拨打电话号码
    auto linkAnnotation = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, phoneNumberFragment->get_Rectangle());
    linkAnnotation->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToURIAction>("callto:678-555-0103"));

    // 添加注释到页面
    page->get_Annotations()->Add(linkAnnotation);
    document->Save(_dataDir + u"SimpleResume_mod.pdf");
}
```

### 获取链接注释

请尝试使用以下代码片段从 PDF 文档中获取链接注释。

```cpp
void GetLinkAnnotations() {

    String _dataDir("C:\\Samples\\");
    // 加载 PDF 文件
    auto document = MakeObject<Document>(_dataDir + u"SimpleResume_mod.pdf");

    // 使用 AnnotationSelector 过滤注释
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial(), Point::get_Trivial(), Point::get_Trivial()));
    page->Accept(annotationSelector);

    auto linkAnnotations = annotationSelector->get_Selected();

    // 打印结果
    for (auto la : linkAnnotations) {

        auto l = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(la);

        // 打印每个链接注释的 URL
        Console::WriteLine(u"URI: " + System::DynamicCast<Aspose::Pdf::Annotations::GoToURIAction>(l->get_Action())->get_URI());

        auto absorber = MakeObject<TextAbsorber>();
        absorber->get_TextSearchOptions()->set_LimitToPageBounds(true);
        absorber->get_TextSearchOptions()->set_Rectangle(l->get_Rect());
        page->Accept(absorber);

        String extractedText = absorber->get_Text();

        // 打印与超链接关联的文本
        Console::WriteLine(extractedText);
    }
}
```

### 删除链接注释

以下代码片段展示了如何从 PDF 文件中删除链接注释。为此，我们需要找到并删除第一页上的所有链接注释。之后，我们将保存删除注释的文档。

```cpp
void DeleteLinkAnnotations()
{
    String _dataDir("C:\\Samples\\");
    // 加载 PDF 文件
    auto document = MakeObject<Document>(_dataDir + u"SimpleResume_mod.pdf");

    // 使用 AnnotationSelector 过滤注释
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial(), Point::get_Trivial(), Point::get_Trivial()));
    page->Accept(annotationSelector);

    auto lineAnnotations = annotationSelector->get_Selected();

    // 打印结果
    for (auto la : lineAnnotations) {
        page->get_Annotations()->Delete(la);
    }

    // 保存删除注释的文档
    document->Save(_dataDir + u"SimpleResume_del.pdf");
}
```

## 使用 Aspose.PDF for C++ 通过涂抹注释对特定页面区域进行涂抹

Aspose.PDF for C++ 支持在现有 PDF 文件中添加和操作注释的功能。最近，我们的一些客户提出了一个要求，需要对 PDF 文档的某个页面区域进行涂抹（删除文本、图像等元素）。为了满足这一要求，提供了一个名为 RedactionAnnotation 的类，可以用来涂抹特定的页面区域，或者可以用来操作现有的涂抹注释并对其进行涂抹（即展平注释并删除其下的文本）。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void RedactAnnotation::AddRedactionAnnotation() {

    String _dataDir("C:\\Samples\\");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // 为特定页面区域创建 RedactionAnnotation 实例
    auto annot = MakeObject<RedactionAnnotation>(page, MakeObject<Rectangle>(200, 500, 300, 600));
    annot->set_FillColor(Color::get_Green());
    annot->set_BorderColor(Color::get_Yellow());
    annot->set_Color(Color::get_Blue());

    // 要在涂抹注释上打印的文本
    annot->set_OverlayText(u"REDACTED");
    annot->set_TextAlignment(HorizontalAlignment::Center);

    // 在涂抹注释上重复覆盖文本
    annot->set_Repeat(true);

    // 将注释添加到第一页的注释集合中
    page->get_Annotations()->Add(annot);

    // 展平注释并涂抹页面内容（即删除涂抹注释下的文本和图像）
    annot->Redact();
    document->Save(_dataDir + u"RedactPage_out.pdf");
}
```

## Facades 方法

Aspose.PDF.Facades 支持 [PdfAnnotationEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor/) 类，该类提供了操作 PDF 文件内现有注释的功能。

此类包含一个名为 [RedactArea(..)](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor#a35ebd333b63b6df2c0c299c7331e3c63) 的方法，该方法提供了删除特定页面区域的功能。

```cpp
void RedactAnnotation::AddRedactionAnnotationViaFacades() {

    String _dataDir("C:\\Samples\\");

    auto editor = MakeObject<Aspose::Pdf::Facades::PdfAnnotationEditor>();

    editor->BindPdf(_dataDir + u"sample.pdf");

    // 涂黑特定页面区域
    editor->RedactArea(1, MakeObject<Rectangle>(100, 100, 20, 70), System::Drawing::Color::get_White());
    editor->BindPdf(_dataDir + u"sample.pdf");
    editor->Save(_dataDir + u"FacadesApproach_out.pdf");
}
```