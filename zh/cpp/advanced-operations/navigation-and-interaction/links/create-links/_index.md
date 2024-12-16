---
title: 在PDF文件中创建链接使用C++
linktitle: 创建链接
type: docs
weight: 10
url: /zh/cpp/create-links/
description: 本节解释如何使用C++在PDF文档中创建链接。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 创建链接

通过在文档中添加应用程序链接，可以从文档中链接到应用程序。这在您希望读者在教程中的特定点采取某个行动或创建功能丰富的文档时很有用。要创建应用程序链接：

1. 创建一个[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)对象。
1. 获取要添加链接的[Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)。
1. 使用Page和[Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle)对象创建一个[LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/)对象。
1. 设置链接属性使用[LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/)对象。
1. 还要设置[LaunchAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.launch_action/)对象的Action属性。
1. 在创建[LaunchAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.launch_action/)对象时，指定您要启动的应用程序。
1. 将链接添加到Page对象的[Annotations](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.annotations)属性。
1. 最后，使用Document对象的Save方法保存更新的PDF。

以下代码片段显示如何在PDF文件中创建到应用程序的链接。

```cpp
using namespace System;
using namespace Aspose::Pdf;

void CreateLink() 
{
    String _dataDir("C:\\Samples\\");
    // 创建 Document 实例
    auto document = MakeObject<Document>(_dataDir + u"CreateApplicationLink.pdf");

    // 将页面添加到 PDF 文件的页面集合
    auto page = document->get_Pages()->idx_get(1);

    auto link = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, MakeObject<Rectangle>(100, 200, 300, 300));
    link->set_Color(Aspose::Pdf::Color::get_Green());
    link->set_Action(MakeObject<Aspose::Pdf::Annotations::LaunchAction>(document, _dataDir + u"sample.pdf"));
    page->get_Annotations()->Add(link);

    // 保存更新的文档
    document->Save(_dataDir + u"CreateApplicationLink.pdf");
}
```
### 在 PDF 文件中创建 PDF 文档链接

Aspose.PDF for C++ 允许您添加链接到外部 PDF 文件，以便您可以将多个文档链接在一起。要创建 PDF 文档链接：

1. 首先，创建一个 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 对象。
1. 然后，获取要添加链接的特定 [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)。
1. 使用 Page 和 [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle) 对象创建一个 [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) 对象。
1. 使用 [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) 对象设置链接属性。
1. 将 Action 属性设置为 [GoToRemoteAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_remote_action/) 对象。 在创建GoToRemoteAction对象时，指定应该启动的PDF文件，以及它应该打开的页码。
1. 将链接添加到Page对象的Annotations集合中。
2. 使用Document对象的Save方法保存更新后的PDF。

以下代码片段显示了如何在PDF文件中创建PDF文档链接。

 ```cpp
void CreatePDFDocumentLink() 
{

    String _dataDir("C:\\Samples\\");
    // 创建Document实例
    auto document = MakeObject<Document>(_dataDir + u"CreateDocumentLink.pdf");

    // 向PDF文件的页面集合中添加页面
    auto page = document->get_Pages()->idx_get(1);

    auto link = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, MakeObject<Rectangle>(100, 200, 300, 300));
    link->set_Color(Aspose::Pdf::Color::get_Green());

    link->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToRemoteAction>(_dataDir + u"sample.pdf", 1));
    page->get_Annotations()->Add(link);

    // 保存更新后的文档
    document->Save(_dataDir + u"CreateDocumentLink_out.pdf");
}
```