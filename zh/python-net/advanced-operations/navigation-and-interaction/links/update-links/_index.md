---
title: 在 Python 中更新 PDF 链接
linktitle: 更新链接
type: docs
weight: 20
url: /zh/python-net/update-links/
description: 了解如何在 Python 中更新 PDF 链接的外观和目标。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何在 PDF 中更新链接
Abstract: Aspose.PDF for Python via .NET 的链接更新指南通过 Python 带领开发人员完成在 PDF 文档中修改超链接行为的过程。它说明了如何更改链接目标，以指向特定页面、外部网站或其他 PDF 文件。文档还涵盖了如何调整链接注释的外观，包括文本颜色，并为每种情况提供实用的代码示例。无论是纠正过时的 URL 还是提升导航体验，此资源都提供了一个清晰且高效的编程方式来管理链接。
---

## 更新 LinkAnnotation 文本颜色

此示例演示如何使用 Aspose.PDF for Python 检测 PDF 第1页上的所有链接注释，然后通过将其字体颜色更改为红色来突出显示每个链接附近的文本。它使用 TextFragmentAbsorber，并在每个链接矩形周围稍微扩展的区域内查找并修改附近的文本。

此可用于：

- 在文档中直观地标记链接
- 通过强调链接内容来提升可访问性
- 在审阅或导出之前对 PDF 文件进行预处理

对于这些链接注释，脚本检索其矩形边界并略微扩大该区域以包含附近的文本，从而实现更广泛的视觉识别。随后，它在此扩展区域上应用 TextFragmentAbsorber，以提取位于其中的任何文本片段。通过将这些捕获的片段的字体颜色更改为红色，对周围文本进行标记，以强调和审阅。应用所有这些更新后，修改后的文档保存到输出路径，保留已高亮的注释及其关联的文本。

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def link_annotation_update_text_color(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        ta = ap.text.TextFragmentAbsorber()
        rect = la.rect
        rect.llx -= 2
        rect.lly -= 2
        rect.urx += 2
        rect.ury += 2
        ta.text_search_options = ap.text.TextSearchOptions(rect)
        ta.visit(document.pages[1])
        for textFragment in ta.text_fragments:
            textFragment.text_state.foreground_color = ap.Color.red

    document.save(outfile)
```

## 更新边框

脚本聚焦于文档的第一页，并过滤掉所有注释，仅选择 LINK 类型的注释——这些通常代表交互元素，例如超链接或导航触发器。对于每个此类链接注释，代码将其强制转换为 LinkAnnotation 类型，并将其颜色属性更新为红色，以视觉上突出显示，使其在其他内容中脱颖而出。所有链接注释均被修改后，更新后的文档被保存到定义的输出位置，保留新的样式。

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def link_annotation_update_border(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        link_annotation = cast(ap.annotations.LinkAnnotation, la)
        link_annotation.color = ap.Color.red

    document.save(outfile)
```

## 更新 Web 目标

一旦路径就绪，原始文档将使用 Aspose.PDF 库加载，使其内容可供修改。脚本随后聚焦于文档的首页，过滤掉所有注释，仅选择链接类型的注释，这类注释通常代表可点击的区域或超链接。为了避免类型错误并确保安全处理，脚本使用 is_assignable 检查每个注释，然后将其转换为相应的 LinkAnnotation 类型。如果该链接关联了 GoToURIAction，即指向网页地址，脚本会更新该 URI，以将用户重定向至 "https://www.aspose.com". 最后，在应用所有所需更改后，修改后的文档会保存到指定的输出路径。

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def link_annotation_update_web_destination(infile, outfile):
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
                action.uri = "https://www.aspose.com"
    document.save(outfile)
```

## 相关链接主题

- [在 Python 中处理 PDF 链接](/pdf/zh/python-net/links/)
- [在 Python 中创建 PDF 链接](/pdf/zh/python-net/create-links/)
- [在 Python 中提取 PDF 链接](/pdf/zh/python-net/extract-links/)