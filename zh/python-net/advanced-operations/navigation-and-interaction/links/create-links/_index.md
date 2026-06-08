---
title: 在 Python 中创建 PDF 链接
linktitle: 创建链接
type: docs
weight: 10
url: /zh/python-net/create-links/
description: 了解如何在 Python 中创建内部、外部和远程 PDF 链接。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何在 PDF 中创建链接
Abstract: Aspose.PDF for Python via .NET 创建链接的指南为开发人员提供了使用 Python 向 PDF 文档添加交互式超链接的实用说明。它涵盖了如何创建各种类型的链接，包括启动外部应用程序、在同一文档内导航到特定页面或打开其他 PDF 文件的链接。文档解释了如何使用 LinkAnnotation 对象、使用 Rectangle 定义可点击区域，以及分配诸如 LaunchAction 或 GoToRemoteAction 等操作。通过清晰的代码示例和一步步的指导，该资源帮助开发人员在 Python 应用程序中提升 PDF 的导航和交互性。
---

## PDF 文档中的链接

根据 PDF 1.7 规范（ISO 32000-1:2008），**链接注释**可以触发多种类型的动作，这些动作定义了注释激活时会发生什么。以下是支持的主要动作：

1. **GoTo** – 导航到同一文档中的目标。
1. **GoToR** – 跳转到另一个 PDF 文件中的目标（远程跳转）。
1. **URI** – 打开统一资源标识符，通常是网页链接。
1. **Launch** – 启动一个应用程序或打开一个文件（取决于平台，且通常出于安全原因受到限制）。
1. **Named** – 执行预定义的操作，例如转到下一页或打印文档。
1. **JavaScript** – 执行嵌入的 JavaScript 代码（因安全考虑需谨慎使用）。
1. **SubmitForm** – 将表单数据提交到指定的 URL。
1. **ResetForm** – 将表单字段重置为默认值。
1. **ImportData** – 将数据从外部文件导入文档。

通过在文档中添加指向应用程序的链接，可以实现从文档链接到应用程序。这在例如希望读者在教程的特定位置执行某个操作，或创建功能丰富的文档时非常有用。

使用‘LaunchAction’创建应用程序链接：

```python
import aspose.pdf as ap
from os import path
import sys

def create_link_annotation_launch_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    border = ap.annotations.Border(link)
    border.width = 5
    border.dash = ap.annotations.Dash(1, 1)
    link.color = ap.Color.green
    link.action = ap.annotations.LaunchAction(document, "sample.pdf")
    page.annotations.append(link)
    document.save(outfile)
```

## 在 PDF 文件中创建 PDF 文档链接

### 使用 GoToRemoteAction

此代码片段演示了如何使用 Python PDF 库向 PDF 文档的特定页面添加链接注释。

1. 打开 PDF 文档
1. 选择文档的第二页（索引 1）
1. 创建链接注释：
1. 位于坐标 (10, 580, 120, 600) 处
1. 颜色为绿色
1. 在第一页链接到 'sample.pdf'
1. 将链接注释添加到页面
1. 将修改后的文档保存到输出文件路径

使用 'GoToRemoteAction' 创建 PDF 文档链接：

```python
import aspose.pdf as ap
from os import path
import sys

def create_link_annotation_go_to_remote_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    link.color = ap.Color.green
    link.action = ap.annotations.GoToRemoteAction("sample.pdf", 1)
    page.annotations.append(link)
    document.save(outfile)
```

### 使用 GoToAction

此代码演示了如何使用 Aspose.PDF for Python 向 PDF 文档的特定页面添加链接注释。该链接显示为绿色、虚线边框的矩形，并允许用户在同一 PDF 中导航到另一页。要使用 'GoToAction' 创建 PDF 文档链接：

```python
import aspose.pdf as ap
from os import path
import sys

def create_link_annotation_go_to_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    border = ap.annotations.Border(link)
    border.width = 5
    border.dash = ap.annotations.Dash(1, 1)
    link.color = ap.Color.green
    if document.pages.length >= 4:
        link.action = ap.annotations.GoToAction(document.pages[4])
    else:
        link.action = ap.annotations.GoToAction(document.pages[document.pages.length])
    page.annotations.append(link)
    document.save(outfile)
```

### 应用 GoToURIAction

下一个示例演示如何使用 Aspose.PDF for Python 向 PDF 文档添加链接批注。该链接在首页上显示为绿色可点击区域，点击后会通过 GoToURIAction 在网页浏览器中打开 Aspose.PDF for Python 文档。

此功能可用于在 PDF 中直接嵌入有用的外部参考、文档或支持链接。

1. 加载 PDF 文档。使用 ap.Document 打开现有的 PDF 文件。
1. 访问第一页。使用 document.pages[1] 访问第一页（Aspose 使用基于 1 的索引）。
1. 创建链接注释。创建一个 LinkAnnotation 对象，并使用 ap.Rectangle 指定可点击的矩形区域。
1. 设置注释外观。使用 link.color = ap.Color.green 将注释的颜色设置为绿色。
1. 分配一个 URI 操作。使用 GoToURIAction 将注释链接到外部 URL。
1. 将注释添加到页面。将配置好的链接注释追加到第一页的注释集合中。
1. 保存已修改的文档。将更新后的 PDF 文档保存到指定的输出路径。

```python
import aspose.pdf as ap
from os import path
import sys
    
def create_link_annotation_go_to_URI_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    link.color = ap.Color.green
    link.action = ap.annotations.GoToURIAction("https://docs.aspose.com/pdf/python")
    page.annotations.append(link)
    document.save(outfile)
```

## 相关链接主题

- [在 Python 中处理 PDF 链接](/pdf/zh/python-net/links/)
- [在 Python 中从 PDF 提取链接](/pdf/zh/python-net/extract-links/)
- [使用 Python 更新 PDF 中的链接](/pdf/zh/python-net/update-links/)