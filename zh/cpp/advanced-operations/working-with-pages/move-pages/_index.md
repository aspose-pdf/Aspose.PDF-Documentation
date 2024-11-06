---
title: 使用 C++ 以编程方式移动 PDF 页面
linktitle: 移动 PDF 页面
type: docs
weight: 20
url: zh/cpp/move-pages/
description: 尝试使用 Aspose.PDF for C++ 将页面移动到所需位置或 PDF 文件的末尾。
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 将页面从一个 PDF 文档移动到另一个

在文档中移动 PDF 页面是一项非常有趣且流行的任务。
本主题解释了如何使用 C++ 将页面从一个 PDF 文档移动到另一个文档的末尾。
要移动页面，我们应该：

1. 使用源 PDF 文件创建一个 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 类对象。
1. 从 [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) 集合中获取页面。
1. 将页面 [添加](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1) 到目标文档。
1. 使用 Save 方法保存输出 PDF。
1. [删除](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#afaa57836d1b206e396f2cb7dd91b5d15)源文档中的页面。
1. 使用Save方法保存源PDF。

下面的代码片段展示了如何移动一页。

```cpp
void MovePage()
{
    // 打开文档
    String _dataDir("C:\\Samples\\");
    String srcFileName("<enter file name>");
    String dstFileName("<enter file name>");

    auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);
    auto dstDocument = MakeObject<Document>();

    auto page = srcDocument->get_Pages()->idx_get(2);
    dstDocument->get_Pages()->Add(page);
    // 保存输出文件
    dstDocument->Save(srcFileName);
    srcDocument->get_Pages()->Delete(2);
    srcDocument->Save(dstFileName);
}
```

## 从一个PDF文档移动一批页面到另一个

1. 使用源PDF文件创建一个[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)类对象。
1. 定义一个包含要移动的页码的数组。
1. 运行循环遍历数组：
1. 从[PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection)集合中获取页面。
1. 将页面[添加](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1)到目标文档。
1. 使用Save方法保存输出PDF。
1. 删除源文档中的[页面](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#afaa57836d1b206e396f2cb7dd91b5d15)。
1. 使用Save方法保存源PDF。

以下代码片段向您展示了如何在PDF文件末尾插入一个空页面。

```cpp
void MoveBunchPages()
{
    // 打开文档
    String _dataDir("C:\\Samples\\");
    String srcFileName("<enter file name>");
    String dstFileName("<enter file name>");

    auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);
    auto dstDocument = MakeObject<Document>();


    auto pages = MakeArray<int>({ 1,3 });

    for (auto pageIndex : pages)
    {
        auto page = srcDocument->get_Pages()->idx_get(pageIndex);
        dstDocument->get_Pages()->Add(page);
    }
    // 保存输出文件
    dstDocument->Save(srcFileName);
    srcDocument->get_Pages()->Delete();
    srcDocument->Save(dstFileName);
}
```
## 在当前 PDF 文档中移动页面到新位置

1. 使用源 PDF 文件创建一个 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 类对象。
1. 从 [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) 集合中获取页面。
1. 将页面[添加](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1)到新位置（例如到末尾）。
1. 删除先前位置的[页面](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#afaa57836d1b206e396f2cb7dd91b5d15)。
1. 使用 Save 方法保存输出 PDF。

```cpp
void MovePagesInOnePDF()
{
    // 打开文档
    String _dataDir("C:\\Samples\\");
    String srcFileName("<enter file name>");
    String dstFileName("<enter file name>");

    auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);
    auto dstDocument = MakeObject<Document>();

    auto page = srcDocument->get_Pages()->idx_get(2);
    srcDocument->get_Pages()->Add(page);
    srcDocument->get_Pages()->Delete(2);

    // 保存输出文件
    srcDocument->Save(dstFileName);
}
```