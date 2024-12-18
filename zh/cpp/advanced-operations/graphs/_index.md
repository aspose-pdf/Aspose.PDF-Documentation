---
title: 在 PDF 中使用图形
linktitle: 使用图形
type: docs
weight: 70
url: /zh/cpp/graphs/
description: 本文解释了什么是图形，如何创建填充矩形对象，如何在图形对象内添加文本，如何向 PDF 添加线条对象等。
lastmod: "2021-12-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 什么是图形

在使用 Adobe Acrobat Writer 或其他 PDF 处理应用程序时，开发人员在 PDF 文档中添加图形是一个非常常见的任务。在 PDF 应用程序中可以使用多种类型的图形。
[Aspose.PDF for C++](/pdf/zh/cpp/) 也支持在 PDF 文档中添加图形。为此，提供了 Graph 类。图形是段落级别的元素，可以添加到页面实例中的段落集合中。一个 Graph 实例包含一个形状集合。

[Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph) 类支持以下类型的形状：

- [Arc](/pdf/zh/cpp/add-arc/) - 有时也称为旗帜，是相邻顶点的有序对，但有时也称为有向线。
- [Circle](/pdf/zh/cpp/add-circle/) - 使用分成扇形的圆圈显示数据。我们使用圆形图（也称为饼图）来展示数据如何表示一个整体或一个组的一部分。
- [Curve](/pdf/zh/cpp/add-curve/) - 是投影线的连接并集，每条线在普通双点中与另外三条线相交。
- [Line](/pdf/zh/cpp/add-line) - 折线图用于显示连续数据，并且在显示随时间变化的趋势时，可以用于预测未来事件。
- [Rectangle](/pdf/zh/cpp/add-rectangle/) - 是图中许多基本形状之一，它在帮助你解决问题时非常有用。
- [Ellipse](/pdf/zh/cpp/add-ellipse/) - 是平面上的一组点，形成椭圆形的曲线形状。

上面的细节也在下面的图中描绘：

![Figures in Graphs](graph.png)