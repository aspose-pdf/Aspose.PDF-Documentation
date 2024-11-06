---
title: 与图形一起工作 
linktitle: 与图形一起工作
type: docs
weight: 70
url: zh/java/graphs/
description: 本文解释了什么是图形，如何创建一个填充的矩形对象，如何在图形对象中添加文本，如何向 PDF 添加线条对象等。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 什么是图形

图形的主要目的是以视觉形式展示数值事实，以便快速、轻松和清晰地理解。因此，图形是收集数据的视觉表现。数据也可以以表格的形式呈现；然而，图形呈现更容易理解。这尤其适用于需要显示趋势或比较的情况。

在处理 Adobe Acrobat Writer 或其他 PDF 处理应用程序时，将图形添加到 PDF 文档是开发人员非常常见的任务。
 有许多类型的图表可以用于PDF应用程序。PDF内容流中使用的图形操作符描述了要在光栅输出设备上再现的页面的外观。

[Aspose.PDF for Java](/pdf/java/) 同样支持向PDF文档添加图形。为此，提供了Graph类。Graph是一个段落级的元素，可以被添加到Page实例中的Paragraphs集合中。一个Graph实例包含一个Shapes的集合。

[Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph) 类支持以下类型的形状：

- [Arc](/pdf/java/add-arc/) - 有时也称为旗帜，是相邻顶点的有序对，有时也称为有向线。
- [Circle](/pdf/java/add-circle/) - 使用被分成扇区的圆来显示数据。我们使用圆形图（也称为饼图）来显示数据如何表示一个整体或一个组的部分。

- [Curve](/pdf/java/add-curve/) - 是投影线的连接并集，每条线在普通双点处与其他三条线相交。- [Line](/pdf/java/add-line) - 折线图用于显示连续数据，当它们显示随时间变化的趋势时，可以在预测未来事件时非常有用。
- [Rectangle](/pdf/java/add-rectangle/) - 是图形中许多基本形状之一，它可以在帮助您解决问题时非常有用。
- [Ellipse](/pdf/java/add-ellipse/) - 是平面上的一组点，形成椭圆形、曲线形状。

上述细节也在下图中描绘：

![Figures in Graphs](graph.png)