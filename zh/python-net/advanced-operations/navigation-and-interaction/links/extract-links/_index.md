---
title: 在 Python 中提取 PDF 链接
linktitle: 提取链接
type: docs
weight: 30
url: /zh/python-net/extract-links/
description: 了解如何在 Python 中从 PDF 文档中提取链接注释和超链接。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何从 PDF 中提取链接
Abstract: Aspose.PDF for Python via .NET 关于提取链接的指南阐述了如何使用 Python 以编程方式从 PDF 文档中检索超链接注释。文档包含实用的代码示例，并强调此功能可用于链接审计、导航分析或构建交互式文档特性等任务。无论是处理单页 PDF 还是大批量文档，此指南都提供了清晰高效的超链接提取方法。
---

## 从 PDF 文件中提取链接

此示例演示如何使用 Aspose.PDF for Python 遍历 PDF 首页上的所有链接注释。它会过滤注释以识别类型为 LinkAnnotation 的注释，安全地进行类型转换，然后打印它们的页面索引和在页面上的矩形位置。

这可用于调试、分析或对 PDF 中现有链接注释进行自动更新。

1. 加载 PDF 文档。使用 ap.Document(path_infile) 打开文件。
1. 访问第一页的注释。使用 document.pages[1].annotations 检索所有注释。
1. 仅过滤 LinkAnnotation 类型。检查每个 annotation 的 annotation_type。
1. 对 LinkAnnotation 进行类型转换和处理。使用 is_assignable() 和 cast() 确保安全访问 LinkAnnotation 属性。
1. 打印注释详情。输出每个链接的页面索引和矩形（位置）。

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def extract_link_annotation(infile):

    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        if is_assignable(la, ap.annotations.LinkAnnotation):
            annotation = cast(ap.annotations.LinkAnnotation, la)
            print(f"Page: {annotation.page_index}, location: {annotation.rect}")
```

## 从 PDF 文件中提取超链接

此代码演示了如何使用 Aspose.PDF for Python 从 PDF 文档的第一页提取所有 LinkAnnotation 对象，然后识别其中包含 GoToURIAction 的对象。对于每个此类链接，它会打印出页面索引和目标 URI。

这对于以下任务很有用：

- 审计 PDF 中的外部链接
- 提取文档或支持 URL
- 检测失效或过时的超链接

1. 加载 PDF 文档。使用 ap.Document 打开文件。
1. 获取第一页中的所有链接注释。过滤注释，仅保留类型为 AnnotationType.LINK 的注释。
1. 进行类型检查并转换为 LinkAnnotation。确保每个注释确实是 LinkAnnotation 后再访问其属性。
1. 检查链接的动作类型。过滤出使用 GoToURIAction 的链接（即指向网页 URL 的链接）。
1. 提取并打印 URI 和页面索引。使用 .uri 获取外部链接，使用 .page_index 获取上下文。

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def extract_hyperlinks(infile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        if is_assignable(la, ap.annotations.LinkAnnotation):
            annotation = cast(ap.annotations.LinkAnnotation, la)
            if is_assignable(annotation.action, ap.annotations.GoToURIAction):
                action = cast(ap.annotations.GoToURIAction, annotation.action)
                print(f"Page {annotation.page_index}, URI:{action.uri}")
```

## 相关链接主题

- [在 Python 中处理 PDF 链接](/pdf/zh/python-net/links/)
- [在 Python 中创建 PDF 链接](/pdf/zh/python-net/create-links/)
- [使用 Python 更新 PDF 中的链接](/pdf/zh/python-net/update-links/)