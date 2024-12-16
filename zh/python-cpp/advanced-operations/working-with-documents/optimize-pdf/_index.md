---
title: 优化、压缩或减少PDF大小在Python中
linktitle: 优化PDF
type: docs
weight: 30
url: /zh/python-cpp/optimize-pdf/
description: 优化PDF文件，缩小所有图像，减少PDF大小，取消嵌入字体，使用Python删除未使用的对象。
lastmod: "2023-12-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

PDF文档有时可能包含额外的数据。减少PDF文件的大小将有助于优化网络传输和存储。这对于网页发布、社交网络分享、通过电子邮件发送或存储归档尤为方便。我们可以使用几种技术来优化PDF：

- 为在线浏览优化页面内容
- 缩小或压缩所有图像
- 启用重用页面内容
- 合并重复流
- 取消嵌入字体
- 删除未使用的对象
- 删除或扁平化表单字段
- 删除或扁平化注释

{{% alert color="primary" %}}

优化方法的详细解释可以在优化方法概述页面中找到。

{{% /alert %}}

## 优化 PDF 文档以用于网络

优化或为 Web 进行线性化，指的是通过网络浏览器使 PDF 文件适合在线浏览的过程。要优化文件以用于网络显示：

以下代码片段显示了如何优化 PDF 文档以用于网络。

```python

    import AsposePDFPythonWrappers as ap

    # 文档目录的路径。
    dataDir = "..."

    # 打开文档
    document = ap.Document(dataDir + "OptimizeDocument.pdf")

    # 为网络优化
    document.optimize()

    dataDir = dataDir + "OptimizeDocument_out.pdf"

    # 保存输出文档
    document.Save(dataDir)
```