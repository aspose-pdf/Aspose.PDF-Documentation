---
title: 在 Python 中使用 PDF 图形
linktitle: 使用图形
type: docs
weight: 70
url: /zh/python-net/working-with-graphs/
description: 学习如何在 Python 中的 PDF 文件里绘制图形和形状，包括弧线、圆形、曲线、直线、矩形和椭圆。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 在 PDF 文件中绘制和自定义矢量图形形状
Abstract: 本节介绍 Aspose.PDF for Python via .NET 中的 Graph 类，并解释如何在 PDF 文档中创建常见的矢量形状。学习如何添加和设置弧线、圆形、曲线、直线、矩形、椭圆的样式，并验证形状边界。
---

## 什么是 Graph

[Aspose.PDF for Python via .NET](/pdf/zh/python-net/) 提供 [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) 用于在 PDF 文档中绘制矢量图形的类。

`Graph` 是段落级别的元素，因此你通过页面将其添加到页面中。 `paragraphs` 集合。每个图表包含一个 `Shapes` 可以添加绘图对象（如直线、弧线、圆形、曲线、矩形和椭圆）的集合。

当您需要在 Python 中直接在 PDF 页面上绘制矢量图形时，请使用本节，无论是用于图表、图示、插图还是自定义页面注释。

## 已覆盖的 Graph Shapes

以下形状类型受 [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) 类：

- [弧](/pdf/zh/python-net/add-arc/) - 绘制部分圆形和弧形图表元素的弧段。
- [圆形](/pdf/zh/python-net/add-circle/) - 为标记和视觉高亮创建圆形轮廓或实心圆。
- [曲线](/pdf/zh/python-net/add-curve/) - 为自定义路径和光滑图形元素添加贝塞尔曲线。
- [线](/pdf/zh/python-net/add-line/) - 绘制直线，包括样式化和虚线。
- [矩形](/pdf/zh/python-net/add-rectangle/) - 创建带轮廓、填充、渐变或透明的矩形形状。
- [Ellipse](/pdf/zh/python-net/add-ellipse/) - 绘制椭圆形状，并在需要时在其中添加文本。

您还可以通过边界检查来验证形状放置：

- [使用 Python 检查 PDF 图形中的形状边界](/pdf/zh/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/)

本节的示例在下图中说明：

![图表中的图形](graphs.png)

