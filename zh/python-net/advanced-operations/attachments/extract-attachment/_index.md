---
title: 从 PDF 中提取附件
linktitle: 提取附件
type: docs
weight: 50
url: /zh/python-net/extract-attachment/
description: 了解如何使用 Python 和 Aspose.PDF 处理 PDF 附件。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Python 中管理 PDF 附件的完整指南：添加、提取和处理嵌入文件"
Abstract: PDF 附件被广泛用于将支持文档、报告、图像和其他资源直接存储在 PDF 文件内部。本文提供了使用 Python 通过 Aspose.PDF 处理 PDF 附件的完整概述。它解释了如何将外部文件嵌入现有 PDF、提取特定或全部附件、检查诸如文件大小和时间戳等元数据，以及恢复存储为 FileAttachment 注释的文件。每个示例演示了用于自动化附件工作流、提升文档可移植性和简化文件管理的实用技术。无论是构建企业文档系统还是自定义自动化脚本，开发者都可以使用这些方法高效地管理 PDF 文档中的嵌入文件。
---

## 从 PDF 提取特定附件

使用 Python 和 Aspose.PDF 从 PDF 文档中提取单个嵌入文件。它通过名称搜索附件，获取其内容，并将其保存为独立的文件。这对于访问嵌入的文档（如报告、日志或存储在 PDF 中的支持文件）非常有用。

1. 定义函数 'extract_single_attachment()'。
1. 打开 PDF 文档。
1. 搜索附件。
1. 提取附件内容。

```python
import aspose.pdf as ap

def extract_single_attachment(infile, attachment_name, outfile):
    with ap.Document(infile) as document:
        print(f"Extracting attachment: {attachment_name}")

        attachment_found = False
        for file_spec in document.embedded_files:
            if file_spec.name == attachment_name:
                with open(outfile, "wb") as f:
                    f.write(file_spec.contents.read())
                print("Attachment extracted successfully")
                attachment_found = True
                break

        if not attachment_found:
            raise ValueError(f"Attachment '{attachment_name}' not found in PDF")
```

## 显示文件附件的元数据

此辅助函数从文件规范对象中打印元数据信息。它通常在使用 Aspose.PDF 处理 PDF 中的嵌入式文件附件时使用，使开发人员能够检查诸如校验和、创建日期、修改日期和文件大小等细节。

```python
def _print_file_params(params):
    """Helper to print file specification parameters."""
    if params:
        print(f"CheckSum: {params.check_sum}")
        print(f"Creation Date: {params.creation_date}")
        print(f"Modification Date: {params.mod_date}")
        print(f"Size: {params.size}")
```

## 提取并检查所有 PDF 附件

此代码片段展示了如何使用 Python 和 Aspose.PDF 从 PDF 文档中提取所有嵌入文件。它不仅将每个附件保存到指定文件夹，还打印出文件名、描述、MIME 类型、校验和和时间戳等详细元数据。这对于审计、导出或处理 PDF 文件中的嵌入内容非常有用。

```python
from os import path
import aspose.pdf as ap

def extract_attachments(infile, output_dir):
    with ap.Document(infile) as document:
        print(f"Total files: {len(document.embedded_files)}")

        for file_spec in document.embedded_files:
            print(f"Name: {file_spec.name}")
            print(f"Description: {file_spec.description}")
            print(f"Mime Type: {file_spec.mime_type}")
            _print_file_params(file_spec.params)

            output_path = path.join(output_dir, file_spec.name)
            with open(output_path, "wb") as f:
                f.write(file_spec.contents.read())
```

## 从 PDF 附件注释中提取文件

使用 Python 和 Aspose.PDF 从 PDF 中的 FileAttachment 注释提取嵌入式文件。它在首页搜索第一个附件注释，检索嵌入的文件，并将其保存到选定的输出目录。当 PDF 包含可点击的文件附件图标而不是标准的嵌入文件集合时，这非常有用。

```python
from os import path
import aspose.pdf as ap
from aspose.pycore import cast

def extract_file_attachment_annotation(infile, output_dir):
    # Open PDF document
    with ap.Document(infile) as document:

        # Get first page
        page = document.pages[1]

        # Find first FileAttachment annotation
        file_attachment = next(
            (
                annot
                for annot in page.annotations
                if annot.annotation_type == ap.annotations.AnnotationType.FILE_ATTACHMENT
            ),
            None,
        )

        if file_attachment is None:
            print("No FileAttachment annotation found on the first page.")
            return

        # Cast to FileAttachmentAnnotation
        faa = cast(ap.annotations.FileAttachmentAnnotation, file_attachment)

        # Access embedded file
        file_spec = faa.file
        print(f"File name: {file_spec.name}")

        # Save embedded file to disk
        output_path = path.join(output_dir, f"extracted-{file_spec.name}")
        with open(output_path, "wb") as f:
            f.write(file_spec.contents.read())

        print(f"Extracted to: {output_path}")
```