---
title: 使用 C++ 替换现有 PDF 文件中的图像
linktitle: 替换图像
type: docs
weight: 70
url: zh/cpp/replace-image-in-existing-pdf-file/
description: 本节介绍如何使用 ++ 库替换现有 PDF 文件中的图像。
lastmod: "2021-12-18"
---

Images 集合的 Replace 方法允许您替换现有 PDF 文件中的图像。

Images 集合可以在页面的 Resources 集合中找到。要替换图像：

1. 使用 Document 对象打开 PDF 文件。
2. 替换特定图像，使用 Document 对象的 Save 方法保存更新后的 PDF 文件。

以下代码片段演示了如何在 PDF 文件中替换图像。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ReplaceImage() {
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"input.pdf");
    // 替换特定图像
    document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->Replace(1, System::IO::File::OpenRead(u"lovely.jpg"));
    // 保存更新后的 PDF 文件
    document->Save(_dataDir + u"output.pdf");
}
```