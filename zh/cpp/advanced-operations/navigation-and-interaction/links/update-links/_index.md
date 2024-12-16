---
title: 更新 PDF 中的链接
linktitle: 更新链接
type: docs
weight: 20
url: /zh/cpp/update-links/
description: 使用 Aspose.PDF for C++ 以编程方式更新 PDF 中的链接。本指南介绍如何更新 PDF 文件中的链接。
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 更新 PDF 文件中的链接

如在向 PDF 文件中添加超链接中所讨论的，[LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) 类可以在 PDF 文件中添加链接。还有一个类似的类用于从 PDF 文件中获取现有链接。如果需要更新现有链接，请使用此类。要更新现有链接：

1. 加载 PDF 文件。
1. 转到 PDF 文件中的特定页面。
1. 使用 [GoToAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_action) 对象的 Destination 属性指定链接目标。
1. 目标页面是使用 [XYZExplicitDestination](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.x_y_z_explicit_destination) 构造函数指定的。

### 将链接目标设置为同一文档中的页面

以下代码片段向您展示了如何更新 PDF 文件中的链接并将其目标设置为文档的第二页。

```cpp
void SetLinkTargetToAPageInTheSameDocument()
{
    String _dataDir("C:\\Samples\\");
    // 创建 Document 实例
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // 向 PDF 文件的页面集合中添加页面
    auto page = document->get_Pages()->idx_get(1);
    auto link = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(page->get_Annotations()->idx_get(1));

    // 修改链接：更改链接目标
    auto goToAction = System::DynamicCast<Aspose::Pdf::Annotations::GoToAction>(link->get_Action());

    // 指定链接对象的目标
    // 表示显式目标，该目标将页面显示在窗口的左上角坐标（left, top）位置，并将页面内容按 zoom 因子放大。
    // 第一个参数是目标页码。
    // 第二个是左坐标
    // 第三个是顶部坐标
    // 第四个参数是显示相应页面时的缩放因子。使用 2 表示页面将以 200% 缩放显示
    goToAction->set_Destination(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(1, 1, 2, 2));

    // 保存更新链接的文档
    document->Save(_dataDir + u"UpdateLinks_out.pdf");
}
```
### 将链接目标设置为网址

要更新超链接以指向网址，请实例化 [GoToURIAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_u_r_i_action) 对象并将其传递给 LinkAnnotation 的 Action 属性。以下代码片段显示了如何更新 PDF 文件中的链接并将其目标设置为网址。

```cpp
void SetLinkDestinationToWebAddress() 
{
    // 加载 PDF 文件
    String _dataDir("C:\\Samples\\");
    // 创建 Document 实例
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // 将页面添加到 PDF 文件的页面集合中
    auto page = document->get_Pages()->idx_get(1);
    auto link = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(page->get_Annotations()->idx_get(1));

    // 修改链接：更改链接动作并将目标设置为网址
    link->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToURIAction>("www.aspose.com"));

    // 保存具有更新链接的文档
    document->Save(_dataDir + u"UpdateLinks_out.pdf");
}
```

### 将链接目标设置为另一个 PDF 文件

以下代码片段展示了如何更新 PDF 文件中的链接并将其目标设置为另一个 PDF 文件。

```cpp
void SetLinkTargetToAnotherPDFFile()
{
    // 加载 PDF 文件
    String _dataDir("C:\\Samples\\");
    // 创建 Document 实例
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // 将页面添加到 PDF 文件的页面集合
    auto page = document->get_Pages()->idx_get(1);
    auto linkAnnot = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(page->get_Annotations()->idx_get(1));

    // 修改链接：更改链接动作并将目标设置为 web 地址
    auto goToR = System::DynamicCast<Aspose::Pdf::Annotations::GoToRemoteAction>(linkAnnot->get_Action());
    // 下一行更新目标，不更新文件
    goToR->set_Destination(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(2, 0, 0, 1.5));
    // 下一行更新文件
    goToR->set_File(MakeObject<FileSpecification>(_dataDir + u"input.pdf"));

    // 保存具有更新链接的文档
    document->Save(_dataDir + u"UpdateLinks_out.pdf");
}
```

### 更新 LinkAnnotation 文本颜色

链接注释不包含文本。相反，文本放置在注释下页面的内容中。因此，要更改文本的颜色，请替换页面文本的颜色，而不是尝试更改注释的颜色。以下代码片段展示了如何在 PDF 文件中更新链接注释的颜色。

```cpp
void UpdateLinkAnnotationTextColor() 
{
    // 加载 PDF 文件
    String _dataDir("C:\\Samples\\");

    // 创建 Document 实例
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // 向 PDF 文件的页面集合添加页面
    auto page = document->get_Pages()->idx_get(1);

    for (auto annotation : page->get_Annotations())
    {
        if (annotation->get_AnnotationType() == Aspose::Pdf::Annotations::AnnotationType::Link)
        {
            // 搜索注释下的文本
            auto ta = MakeObject<Aspose::Pdf::Text::TextFragmentAbsorber>();
            auto rect = annotation->get_Rect();
            rect->set_LLX(rect->get_LLX() - 10);
            rect->set_LLY(rect->get_LLY() - 10);
            rect->set_URX(rect->get_URX() + 10);
            rect->set_URY(rect->get_URY() + 10);

            ta->set_TextSearchOptions(MakeObject<Aspose::Pdf::Text::TextSearchOptions>(rect));
            ta->Visit(page);
            // 更改文本的颜色。
            for (auto tf : ta->get_TextFragments())
            {
                tf->get_TextState()->set_ForegroundColor(Color::get_Red());
            }
        }

    }
    // 保存更新链接的文档
    document->Save(_dataDir + u"UpdateLinkTextColor_out.pdf");
}
```