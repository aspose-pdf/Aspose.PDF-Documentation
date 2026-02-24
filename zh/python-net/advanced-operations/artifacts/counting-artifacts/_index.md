---
title: 在 Python via .NET 中统计特定类型的人工制品
linktitle: 统计人工制品
type: docs
weight: 40
url: /zh/python-net/counting-artifacts/
description: 本文示例说明如何使用 Aspose.PDF for Python via .NET 检查 PDF 文档中的分页人工制品。
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 对 PDF 中的人工制品进行计数
Abstract: 分页人工制品（如水印、背景、页眉和页脚）在 PDF 文档中常用于提供结构、品牌和标识。此示例演示如何使用 Aspose.PDF for Python via .NET 以编程方式检查并计数这些人工制品。通过在页面上过滤人工制品并按子类型分组，开发人员可以快速分析文档构成并验证特定元素的存在。提供的代码展示了如何打开 PDF、从首页提取分页人工制品、统计每个子类型的数量并输出结果，提供了一种实用的文档审计和验证方法。
---

## 特定类型的人工制品计数

使用 Aspose.PDF for Python via .NET 检查并计数 PDF 中的分页人工制品（[`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)）。分页人工制品包括水印、背景、页眉和页脚等应用于页面以实现布局和标识的元素。通过过滤位于 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 上的 [`Artifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) 对象并按子类型（`Artifact.ArtifactSubtype`）分组，开发者可以快速分析文档结构并验证特定元素的存在。

要计算特定类型人工制品的总数量（例如，水印的总数），请使用以下代码。示例通过 [`Artifact.ArtifactType`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/#properties) 对页面的 [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) 集合（[`ArtifactCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)）进行过滤，然后统计子类型（`Artifact.ArtifactSubtype`）的数量。

1. 打开 PDF 文档（参见 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)）。
1. 使用页面的 [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) 集合过滤分页人工制品。
1. 按子类型（`Artifact.ArtifactSubtype`）计数人工制品。
1. 打印结果。

```python

import aspose.pdf as ap

def count_pagination_artifacts(path_infile):
    # Open the PDF document
    with ap.Document(path_infile) as document:
        
        # Extract pagination artifacts from the first page
        pagination_artifacts = [
            artifact for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
        ]

        # Count artifacts by subtype
        watermarks = sum(1 for artifact in pagination_artifacts 
                         if artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK)
        backgrounds = sum(1 for artifact in pagination_artifacts 
                          if artifact.subtype == ap.Artifact.ArtifactSubtype.BACKGROUND)
        headers = sum(1 for artifact in pagination_artifacts 
                      if artifact.subtype == ap.Artifact.ArtifactSubtype.HEADER)
        footers = sum(1 for artifact in pagination_artifacts 
                      if artifact.subtype == ap.Artifact.ArtifactSubtype.FOOTER)

        # Display results
        print(f"Watermarks: {watermarks}")
        print(f"Backgrounds: {backgrounds}")
        print(f"Headers: {headers}")
        print(f"Footers: {footers}")
```

