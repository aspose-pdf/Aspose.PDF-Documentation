---
title: 在 PDF 中使用操作
linktitle: 操作
type: docs
weight: 20
url: zh/cpp/actions/
description: 本节解释如何使用 C++ 以编程方式向文档和表单字段添加操作。
lastmod: "2022-01-25"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 在 PDF 文件中添加超链接

PDF 文档是一种分享信息的好方法。它们易于阅读、编辑和分发。然而，在 PDF 文档中创建链接可能具有挑战性。让我们来看看如何操作。

可以向 PDF 文件添加超链接，以便读者可以导航到 PDF 的其他部分或外部内容。

例如，您可能希望为电子书添加一个可点击的目录，引用文章的外部资源，或快速导航读者到网站上的不同页面以获取更多关于某个主题的信息。

要通过几个简单的步骤创建超链接，请执行以下操作：

1. 创建一个[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)类对象。
1. 获取要添加链接的[Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)类。
1. 使用Page和[Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle/)对象创建一个[LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/)对象。Rectangle对象用于指定页面上要添加链接的位置。
1. 将Action属性设置为[GoToURIAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_u_r_i_action)对象，该对象指定远程URI的位置。
1. 要显示超链接文本，请在类似于放置[LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation)对象的位置添加一个文本字符串。
1. 要添加自由文本：

- 实例化一个[FreeTextAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.free_text_annotation)对象。 它还接受 Page 和 Rectangle 对象作为参数，因此可以提供与 LinkAnnotation 构造函数中指定的相同值。

- 使用 [FreeTextAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.free_text_annotation) 对象的 Contents 属性，指定应在输出 PDF 中显示的字符串。

- 可选择将 [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) 和 FreeTextAnnotation 对象的边框宽度设置为 0，以便它们不会出现在 PDF 文档中。

- 一旦定义了 [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) 和 [FreeTextAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.free_text_annotation) 对象，将这些链接添加到 [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) 对象的 Annotations 集合中。

- 最后，使用 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 对象的 Save 方法保存更新后的 PDF。
以下代码片段向您展示如何向 PDF 文件添加超链接。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddHyperlinkInPDFFile() {

String _dataDir("C:\\Samples\\");

// 打开文档

auto document = MakeObject<Document>(_dataDir + u"AddHyperlink.pdf");

// 创建链接

auto page = document->get_Pages()->idx_get(1);

// 创建链接注释对象

auto link = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, MakeObject<Rectangle>(100, 100, 300, 300));

// 为链接注释创建边框对象

auto border = MakeObject<Aspose::Pdf::Annotations::Border>(link);

// 将边框宽度值设置为 0

border->set_Width(0);

// 设置链接注释的边框

link->set_Border(border);

// 指定链接类型为远程 URI

link->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToURIAction>("www.aspose.com"));

// 将链接注释添加到 PDF 文件第一页的注释集合中

page->get_Annotations()->Add(link);


// 创建自由文本注释

auto textAnnotation = MakeObject<Aspose::Pdf::Annotations::FreeTextAnnotation>(


page,


MakeObject<Rectangle>(100, 100, 300, 300),


MakeObject<Aspose::Pdf::Annotations::DefaultAppearance>(



FontRepository::FindFont(u"TimesNewRoman"), 10, Color::get_Blue()));


// 要添加为自由文本的字符串

textAnnotation->set_Contents(u"Link to Aspose website");

// 设置自由文本注释的边框

textAnnotation->set_Border(border);

// 将自由文本注释添加到文档第一页的注释集合中

page->get_Annotations()->Add(textAnnotation);


// 保存更新后的文档

document->Save(_dataDir + u"AddHyperlink_out.pdf");

}
```

## 创建指向同一 PDF 中页面的超链接

Aspose.PDF for C++ 为 PDF 创建及其操作提供了出色的功能。它还提供了向 PDF 页面添加链接的功能，链接可以直接指向另一个 PDF 文件中的页面、一个网页 URL、启动一个应用程序的链接，甚至指向同一 PDF 文件中的页面。为了添加本地超链接（指向同一 PDF 文件中的页面的链接），在 Aspose.PDF 命名空间中添加了一个名为 [LocalHyperlink](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.local_hyperlink) 的类，该类具有一个名为 TargetPageNumber 的属性，用于指定超链接的目标/目标页面。

为了添加本地超链接，我们需要创建一个 TextFragment，以便链接可以与该 TextFragment 关联。 [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment) 类有一个名为 Hyperlink 的属性，用于关联 LocalHyperlink 实例。以下代码片段显示了实现此要求的步骤。

```cpp
void CreateHyperlinkToPagesInSamePDF() {

String _dataDir("C:\\Samples\\");


// 创建 Document 实例

auto document = MakeObject<Document>();


// 向 PDF 文件的页面集合中添加页面

auto page = document->get_Pages()->Add();


// 创建 Text Fragment 实例

auto text = MakeObject<TextFragment>(u"link page number test to page 2");


// 创建本地超链接实例

auto link = MakeObject<LocalHyperlink>();


// 为链接实例设置目标页面

link->set_TargetPageNumber(2);


// 设置 TextFragment 超链接

text->set_Hyperlink(link);


// 将文本添加到 Page 的段落集合中

page->get_Paragraphs()->Add(text);


// 创建新的 TextFragment 实例

text = new TextFragment(u"link page number test to page 1");


// TextFragment 应该添加到新页面上

text->set_IsInNewPage(true);


// 创建另一个本地超链接实例

link = new LocalHyperlink();


// 为第二个超链接设置目标页面

link->set_TargetPageNumber(1);


// 设置第二个 TextFragment 的链接

text->set_Hyperlink(link);


// 将文本添加到页面对象的段落集合中

page->get_Paragraphs()->Add(text);


// 保存更新后的文档

document->Save(_dataDir + u"CreateLocalHyperlink_out.pdf");
}
```
## 获取 PDF 超链接目标（URL）

链接在 PDF 文件中表示为注释，可以添加、更新或删除。Aspose.PDF for C++ 还支持获取 PDF 文件中超链接的目标（URL）。

要获取链接的 URL：

1. 创建一个 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 对象。
1. 获取要从中提取链接的 [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)。
1. 使用 [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) 类从指定页面提取所有 [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation) 对象。
1. 将 [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) 对象传递给 [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) 对象的 Accept 方法。 将所有选定的链接注释获取到一个 IList 对象中，使用 [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) 对象的 Selected 属性。
1. 最后，将 LinkAnnotation Action 提取为 GoToURIAction。

以下代码片段显示了如何从 PDF 文件中获取超链接目标（URL）。

```cpp
void GetPDFHyperlinkDestination() {

String _dataDir("C:\\Samples\\");


auto document = new Document(_dataDir + u"Aspose-app-list.pdf");

// 提取动作

auto page = document->get_Pages()->idx_get(1);


auto selector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(


MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial()));

page->Accept(selector);


auto list = selector->get_Selected();

// 遍历列表中的每个项目

if (list->get_Count() == 0)


Console::WriteLine(u"没有找到超链接...");

else {


// 遍历所有书签


for (auto annot : list) {



auto la = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(annot);



if (la != nullptr) {




auto action = System::DynamicCast<Aspose::Pdf::Annotations::GoToURIAction>(la->get_Action());




// 打印目标 URL




Console::WriteLine(u"目标: " + action->get_URI());



}


}

} // end else
}
```
## 获取超链接文本

超链接有两个部分：文档中显示的文本和目标URL。在某些情况下，我们需要的是文本而不是URL。

PDF文件中的文本和注释/动作由不同的实体表示。页面上的文本只是一组单词和字符，而注释则带来了一些互动性，例如超链接固有的互动性。

要找到URL内容，您需要同时处理注释和文本。[Annotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation) 对象本身没有文本，但位于页面上的文本下方。因此，要获取文本，Annotation提供URL的界限，而Text对象提供URL内容。请参见以下代码片段。

```cpp
  void GetHyperlinkText() {

String _dataDir("C:\\Samples\\");

auto document = MakeObject<Document>(_dataDir + u"aspose-app-list.pdf");

// 提取动作

auto page = document->get_Pages()->idx_get(1);


for (auto annot : page->get_Annotations()) {


auto la = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(annot);


if (la != nullptr) {



// 打印每个链接注释的URL



auto action = System::DynamicCast<Aspose::Pdf::Annotations::GoToURIAction>(la->get_Action());



Console::WriteLine(u"URI: " + action->get_URI());




auto absorber = MakeObject<TextAbsorber>();



absorber->get_TextSearchOptions()->set_LimitToPageBounds(true);



absorber->get_TextSearchOptions()->set_Rectangle(annot->get_Rect());



page->Accept(absorber);



String extractedText = absorber->get_Text();



// 打印与超链接关联的文本



Console::WriteLine(extractedText);


}

}
}
```

## 从 PDF 文件中移除文档打开动作

[如何在查看文档时指定 PDF 页面](#how-to-specify-pdf-page-when-viewing-document) 解释了如何让文档在不同于第一页的页面上打开。当连接多个文档时，如果一个或多个文档设置了 GoTo 动作，您可能希望将其移除。例如，如果合并两个文档，而第二个文档有一个 GoTo 动作将您带到第二页，则输出文档将打开在第二个文档的第二页，而不是合并文档的第一页。为了避免这种行为，移除打开动作命令。

要移除打开动作：

1. 将 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 对象的 [OpenAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a24b876bb6bee957feac48ac8031dc28e) 属性设置为 null。
1. 使用 Document 对象的 Save 方法保存更新的 PDF。


以下代码片段展示了如何从 PDF 文件中移除文档打开动作。

```cpp
void RemoveDocumentOpenActionFromPDFFile()
{

String _dataDir("C:\\Samples\\");

// 打开文档

auto document = new Document(_dataDir + u"RemoveOpenAction.pdf");

// 移除文档打开动作

document->set_OpenAction(nullptr);


// 保存更新后的文档

document->Save(_dataDir + u"RemoveOpenAction_out.pdf");
}
```

## 如何在查看文档时指定 PDF 页面 {#how-to-specify-pdf-page-when-viewing-document}

在 PDF 查看器（如 Adobe Reader）中查看 PDF 文件时，文件通常会在第一页打开。然而，可以设置文件在不同的页面上打开。

'XYZExplicitDestination' 类允许您指定要打开的 PDF 文件中的页面。当将 GoToAction 对象值传递给 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 类的 OpenAction 属性时，文档将在与 XYZExplicitDestination 对象指定的页面打开。以下代码片段演示了如何指定页面作为文档打开动作。

```cpp
void HowToSpecifyPDFPageWhenViewingDocument()
{

String _dataDir("C:\\Samples\\");

// 加载 PDF 文件

auto document = new Document(_dataDir + u"SpecifyPageWhenViewing.pdf");

// 获取文档的第二页实例

auto page2 = document->get_Pages()->idx_get(2);

// 创建变量以设置目标页面的缩放因子

double zoom = 1;

// 创建 GoToAction 实例

auto action = MakeObject<Aspose::Pdf::Annotations::GoToAction>(page2);

// 跳转到第 2 页

action->set_Destination(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(page2, 0, page2->get_Rect()->get_Height(), zoom));

// 设置文档打开动作

document->set_OpenAction(action);

// 保存更新后的文档

document->Save(_dataDir + u"goto2page_out.pdf");
}
```