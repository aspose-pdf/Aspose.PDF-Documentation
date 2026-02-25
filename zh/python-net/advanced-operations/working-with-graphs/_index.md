---
title: 使用 Python 在 PDF 中处理图表
linktitle: 处理图表
type: docs
weight: 70
url: /zh/python-net/working-with-graphs/
description: 本文解释了图的概念、如何创建填充矩形对象以及其他功能。
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 向 PDF 添加图表
Abstract: 本文讨论了在 PDF 文档中集成图表，这是使用 Adobe Acrobat Writer 或类似 PDF 处理工具的开发者的常见需求。它介绍了 Aspose.PDF for Python via .NET 中的 Graph 类，该类通过允许向 PDF 文档添加各种形状来简化此任务。Graph 类是段落级别的元素，可以添加到 Page 实例的 Paragraphs 集合中，并支持包括弧线（Arc）、圆形（Circle）、曲线（Curve）、直线（Line）、矩形（Rectangle）和椭圆（Ellipse）在内的形状集合。每种形状都有其独特的用途，例如弧线用于表示邻接，圆形用于展示数据部分，曲线用于描绘连接线，直线用于显示连续数据趋势，矩形用于解决空间问题，椭圆用于形成椭圆形状。文章还提供了这些形状的可视化示例，以帮助理解。
---

## 什么是图

在 PDF 文档中添加图表是开发者在使用 Adobe Acrobat Writer 或其他 PDF 处理应用程序时的常见任务。PDF 应用程序中可以使用多种类型的图表。
[Aspose.PDF for Python via .NET](/pdf/python-net/) 也支持向 PDF 文档添加图表。为此提供了 Graph 类。Graph 是段落级别的元素，可以添加到 Page 实例的 Paragraphs 集合中。Graph 实例包含一个形状集合。

以下类型的形状受 [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) 类支持：

- [Arc](/pdf/python-net/add-arc/) - 有时也称为旗帜，是一对相邻顶点的有序对，但有时也称为有向线。
- [Circle](/pdf/python-net/add-circle/) - 使用被划分为扇形的圆来显示数据。我们使用圆形图（亦称饼图）来展示数据如何表示整体或一个群体的各部分。
- [Curve](/pdf/python-net/add-curve/) - 是投影直线的连通并集，每条直线在普通双点处与另外三条相交。
- [Line](/pdf/python-net/add-line) - 折线图用于显示连续数据，并且在显示随时间变化的趋势时，可用于预测未来事件。
- [Rectangle](/pdf/python-net/add-rectangle/) - 是图表中常见的基本形状之一，它在帮助您解决问题时非常有用。
- [Ellipse](/pdf/python-net/add-ellipse/) - 是平面上一组点，形成椭圆形的弧形。

上述细节也在下图中展示：

![图表中的图示](graphs.png)


