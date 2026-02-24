---
title: 在 Python 中将 PDF/x 转换为 PDF 格式
linktitle: 将 PDF/x 转换为 PDF 格式
type: docs
weight: 120
url: /zh/python-net/convert-pdf_x-to-pdf/
lastmod: "2025-09-27"
description: 本主题展示如何使用 Aspose.PDF for Python via .NET 将 PDF/x 转换为 PDF 格式。
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: 如何将 PDF/x 转换为 PDF 格式
Abstract: 本文提供了使用 Aspose.PDF for Python 将 PDF/UA 和 PDF/A 转换为 PDF 文件的完整指南。
---

**PDF/x 转换为 PDF 格式意味着能够将 PDF/UA 和 PDF/A 转换为 PDF 文件。**

## 将 PDF/A 转换为 PDF

1. 使用 'ap.Document' 加载 PDF 文档。
1. 调用 'remove_pdfa_compliance()' 去除所有与 PDF/A 相关的合规设置和元数据。
1. 将生成的 PDF 保存到输出路径。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.remove_pdfa_compliance()
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## 移除 PDF/UA 合规性

此函数演示了一个两步转换过程：首先移除 PDF/UA（通用可访问性）合规性，然后将生成的 PDF 转换为 PDF/A-1B 格式，并自动标记以实现可访问性和语义结构。

1. 使用 'ap.Document()' 加载 PDF 文档。
1. 调用 'document.remove_pdfa_compliance()' 删除所有 PDF/A 限制或合规设置。
1. 将修改后的 PDF 保存到 'path_outfile'。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.remove_pdfa_compliance()
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```
