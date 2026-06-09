---
title: 在 Python 中将 PDF/A 和 PDF/UA 转换为 PDF
linktitle: 将 PDF/A 和 PDF/UA 转换为 PDF
type: docs
weight: 120
url: /zh/python-net/convert-pdf_x-to-pdf/
lastmod: "2026-06-08"
description: 了解如何使用 Aspose.PDF for Python via .NET 在 Python 中移除 PDF 文件的 PDF/A 和 PDF/UA 合规性，并将其保存为标准 PDF 文档。
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: 在 Python 中如何将 PDF/A 和 PDF/UA 转换为标准 PDF
Abstract: 本文解释了如何使用 Aspose.PDF for Python via .NET 从基于标准的 PDF 文档中移除 PDF/A 和 PDF/UA 合规性。它涵盖了您可能需要标准 PDF 而不是归档或受可访问性限制的文件的场景，并展示了在移除合规性元数据和限制后如何保存结果。
---

当您需要将基于标准的 PDF（例如 PDF/A 或 PDF/UA）转换回普通 PDF 文档，以便进行下游编辑、处理或再分发时，请使用此页面。

符合标准的 PDF 对于归档、打印和可访问性工作流很有帮助，但在某些情况下，你可能需要在将文件集成到其他系统或管道之前移除这些合规性。Aspose.PDF for Python via .NET 让你可以以编程方式做到这一点，然后将结果保存为标准 PDF 文件。

## 将 PDF/A 转换为 PDF

此示例从 PDF 中移除 PDF/A 合规性元数据和限制，使文档能够再次保存为普通 PDF 文件。

1. 使用 'ap.Document' 加载 PDF 文档。
1. 调用 'remove_pdfa_compliance()' 来剥离所有与 PDF/A 相关的合规设置和元数据。
1. 将生成的 PDF 保存到输出路径。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDFA_to_PDF(infile, outfile):
    document = ap.Document(infile)
    document.remove_pdfa_compliance()
    document.save(outfile)
```

## 移除 PDF/UA 合规性

本示例演示如何移除与 PDF/UA 相关的合规性，使文档能够以标准 PDF 保存，用于非无障碍特定的工作流。

1. 使用 'ap.Document()' 加载 PDF 文档。
1. 调用 'document.remove_pdfa_compliance()' 以移除任何 PDF/A 限制或合规性设置。
1. 将修改后的 PDF 保存到 'path_outfile'。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDFUA_to_PDF(infile, outfile):
    document = ap.Document(infile)
    document.remove_pdf_ua_compliance()
    document.save(outfile)
```

## 何时使用此工作流

- 在将文档发送到不需要 PDF/A 或 PDF/UA 限制的工具链之前，删除合规性设置。
- 当不再需要归档或可访问性元数据时，简化下游文档处理。
- 在将输入 PDF 导出为其他格式之前，标准化它们。

## 相关转换

- [将 PDF 转换为 PDF/A、PDF/E 和 PDF/X](/pdf/zh/python-net/convert-pdf-to-pdf_x/) 如果您需要相反的工作流并希望创建符合标准的 PDF。
- [转换 PDF 为 Word](/pdf/zh/python-net/convert-pdf-to-word/) 用于在移除合规约束后生成可编辑的文档输出。
- [将 PDF 转换为 HTML](/pdf/zh/python-net/convert-pdf-to-html/) 用于从标准 PDF 文件生成适合浏览器的输出。
