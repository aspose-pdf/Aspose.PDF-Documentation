---
title: 在 Python 中使用 PDF 工件
linktitle: 使用工件
type: docs
weight: 170
url: /zh/python-net/artifacts/
description: 在 Python 中添加、检查和删除 PDF 工件，包括背景、水印、页眉、页脚以及 Bates 编号。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中管理 PDF 页面工件
Abstract: 查找有关添加和删除 PDF 工件、检查水印详细信息以及使用 Aspose.PDF for Python via .NET 按子类型计数分页工件的指南。
---

PDF 工件标记页面元素，例如装饰性背景、连续页眉和页脚以及水印。在标记的 PDF 中，辅助技术可以跳过工件，专注于文档的有意义内容。

## 选择指南

### 添加工件

- [添加背景](/pdf/zh/python-net/add-backgrounds/)
- [添加水印](/pdf/zh/python-net/add-watermarks/)
- [添加贝茨编号](/pdf/zh/python-net/add-bates-numbering/)
- [添加页眉和页脚](/pdf/zh/python-net/artifacts-header-footer/)

### 检查工件

- [按子类型统计分页工件](/pdf/zh/python-net/counting-artifacts/)
- [提取水印详情](/pdf/zh/python-net/extract-watermarks/)

### 删除工件

- [删除背景](/pdf/zh/python-net/remove-backgrounds/)
- [删除水印](/pdf/zh/python-net/remove-watermarks/)
- [删除 Bates 编号](/pdf/zh/python-net/remove-bates-numbering/)
- [删除页眉和页脚](/pdf/zh/python-net/remove-headers-footers/)

## 工件 API

`artifacts` 属性返回页面的 [`ArtifactCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/) 集合。[`Artifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) 类提供 [`BackgroundArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/)、[`WatermarkArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/watermarkartifact/)、[`HeaderArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerartifact/)、[`FooterArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/footerartifact/) 和 [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) 等专用类共有的属性。

| 任务 | 属性 |
| --- | --- |
| 识别工件 | 使用 `type` 和 `subtype` 用于标准分类和 `custom_type` 和 `custom_subtype` 用于自定义名称。 |
| 检查其内容 | 使用 `text`, `image`, 和 `lines` 对于文本和图像，或 `contents` 和 `form` 用于 PDF 操作符和相关的 XForm。 |
| 在页面上定位它 | 使用 `rectangle` 检查其边界。设置 `position` 用于显式放置或使用 `left_margin`, `right_margin`, `top_margin`, `bottom_margin`, `artifact_horizontal_alignment`, 和 `artifact_vertical_alignment`. 显式位置会覆盖边距和对齐。 |
| 控制其外观 | 使用 `rotation`, `opacity` (从 0 到 1)，以及 `text_state`. 设置 `is_background` 将工件放置在页面内容后面。 |
