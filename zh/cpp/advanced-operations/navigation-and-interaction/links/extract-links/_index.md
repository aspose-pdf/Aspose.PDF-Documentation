```
---
title: 从PDF文件中提取链接
linktitle: 提取链接
type: docs
weight: 30
url: zh/cpp/extract-links/
description: 使用C#从PDF中提取链接。本主题向您解释如何使用AnnotationSelector类提取链接。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 从PDF文件中提取链接

链接在PDF文件中表示为注释，因此要提取链接，请提取所有的[LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/)对象。

1. 创建一个[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)对象。
1. 获取要提取链接的[Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)。
1.
``` 使用 [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) 类从指定页面中提取所有的 [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) 对象。
1. 将 [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) 对象传递给 Page 对象的 Accept 方法。
1. 使用 [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) 对象的 Selected 属性将所有选定的链接注释获取到 IList 对象中。

以下代码片段展示了如何从 PDF 文件中提取链接。

```cpp
void ExtractLinksFromThePDFFile() {
   
    // 加载 PDF 文件
    String _dataDir("C:\\Samples\\");

    // 创建 Document 实例
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // 将页面添加到 PDF 文件的页面集合中
    auto page = document->get_Pages()->idx_get(1);


    auto selector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(selector);
    auto list = selector->get_Selected();
    for (auto annot : list)
    {
        Console::WriteLine(u"Annotation located: {0}", annot->get_Rect());
    }
}
```