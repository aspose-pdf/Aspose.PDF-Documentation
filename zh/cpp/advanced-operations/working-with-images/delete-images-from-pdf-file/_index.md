---
title: 使用C++从PDF文件中删除图像
linktitle: 删除图像
type: docs
weight: 20
url: /zh/cpp/delete-images-from-pdf-file/
description: 本节解释如何使用Aspose.PDF for C++从PDF文件中删除图像。
lastmod: "2021-12-18"
---

要从PDF文件中删除图像：

1. 创建一个[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)对象并打开输入的PDF文件。
1. 从Document对象的[Pages collection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection)中获取包含图像的页面。
1. 图像保存在页面的Resources集合中的Images集合中。
1. 使用Images集合的Delete方法删除图像。
1. 使用Document对象的Save方法保存输出。

以下代码片段展示了如何从PDF文件中删除图像。

```cpp
void WorkingWithImages::DeleteImagesFromPDFFile()
{
    String _dataDir("C:\\Samples\\");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + u"DeleteImages.pdf");

    // 删除特定图像
    document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->Delete(1);

    // 保存更新后的PDF文件
    document->Save(_dataDir + u"DeleteImages_out.pdf");
}
```