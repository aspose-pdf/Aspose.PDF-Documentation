---
title: 程序化删除PDF页面 
linktitle: 删除PDF页面
type: docs
weight: 30
url: /cpp/delete-pages/
description: 您可以使用C++库从PDF文件中删除页面。
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

您可以使用Aspose.PDF for C++从PDF文件中删除页面。要从[PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection)集合中删除特定页面。

## 从PDF文件中删除页面

1. 调用[Delete](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a02bb7a96e66ef6e10bcf4930b299b3b7)方法并指定页面的索引
1. 调用Save方法保存更新的PDF文件
以下代码片段演示了如何使用C++从PDF文件中删除特定页面。

```cpp
void DeletePDFPages() {
    String _dataDir("C:\\Samples\\");
    String inputFileName("DeleteParticularPage.pdf");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // 删除特定页面
    document->get_Pages()->Delete(2);

    // 保存更新的PDF
    document->Save(_dataDir + inputFileName);
}
```