---
title: 在 Python 中使用 PDF 工件
linktitle: 使用工件
type: docs
weight: 170
url: /zh/python-net/artifacts/
description: 了解如何在 Python 中使用 PDF 工件来添加背景、浮水印和 Bates 编号，并使用 Aspose.PDF for Python via .NET 对工件类型进行计数。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中添加背景、浮水印和 Bates 编号工件
Abstract: 本文阐述了如何在 Aspose.PDF for Python via .NET 中使用 PDF 工件。了解工件是什么、它们为何对可访问性和文档布局重要，以及如何在 PDF 文件中使用 Python 添加背景图像、应用浮水印、添加 Bates 编号并检查工件类型。
---

PDF 中的工件是图形对象或其他不属于文档实际内容的元素。它们通常用于装饰、布局或背景目的。工件的例子包括页面页眉、页脚、分隔线或不传达任何意义的图像。

PDF 中的 artifact 旨在区分内容元素和非内容元素。这对可访问性很重要，因为屏幕阅读器和其他辅助技术可以忽略 artifact 并专注于相关内容。artifact 还可以提升 PDF 文档的性能和质量，因为它们可以在打印、搜索或复制时被省略。

当您需要在 Python 中创建或检查非内容 PDF 元素（如文档背景、页面水印和 Bates 编号标记）时，请使用本节。以下指南展示了 Aspose.PDF for Python via .NET 支持的主要 artifact 工作流。

要在 PDF 中将元素创建为 artifact，您需要使用 [Artifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) 类。
它包含以下有用属性：

- **custom_type** - 获取工件类型的名称。若工件类型为非标准类型，可使用此属性。
- **custom_subtype** - 获取工件子类型的名称。若工件子类型不是标准子类型，可使用此属性。
- **type** - 获取工件类型。
- **subtype** - 获取工件子类型。如果工件拥有非标准子类型，可通过 CustomSubtype 读取子类型名称。
- **contents** - 获取工件内部运算符的集合。
- **form** - 获取工件的 XForm（如果使用了 XForm）。
- **rectangle** - 获取工件的矩形。
- **position** - 获取或设置工件的位置。如果指定了此属性，则会忽略边距和对齐方式。
- **right_margin** - 工件的右边距。如果在 Position 属性中显式指定了位置，则此值将被忽略。
- **left_margin** - 工件的左边距。如果在 Position 属性中显式指定了位置，则此值将被忽略。
- **top_margin** - 工件的上边距。如果在 Position 属性中显式指定了位置，则此值将被忽略。
- **bottom_margin** - 工件的下边距。如果在 Position 属性中显式指定了位置，则此值将被忽略。
- **artifact_horizontal_alignment** - 构件的水平对齐方式。如果在 Position 属性中显式指定了位置，则此值被忽略。
- **artifact_vertical_alignment** - 构件的垂直对齐方式。如果在 Position 属性中显式指定了位置，则此值被忽略。
- **rotation** - 获取或设置构件的旋转角度。
- **text** - 获取构件的文本。
- **image** - 获取构件的图像（如果存在）。
- **opacity** - 获取或设置构件的不透明度。可能的取值范围为 0..1。
- **lines** - 多行文本工件的行。
- **text_state** - 工件文本的文本状态。
- **is_background** - 如果为 true，工件将放置在页面内容之后。

以下类在处理工件时可能也很有用：

- [ArtifactCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)
- [BackgroundArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/)
- [HeaderArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerartifact/)
- [页脚工件](https://reference.aspose.com/pdf/python-net/aspose.pdf/footerartifact/)
- [水印工件](https://reference.aspose.com/pdf/python-net/aspose.pdf/watermarkartifact/)
- [BatesN工件](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/)

## 本节涵盖的工件工作流

请查看文章的以下章节：

- [添加背景](/pdf/zh/python-net/add-backgrounds/) - 使用 Python 向 PDF 文件添加背景图像。
- [添加贝茨编号](/pdf/zh/python-net/add-bates-numbering/) - 为 PDF 添加贝茨编号。
- [添加水印](/pdf/zh/python-net/add-watermarks/) - 如何使用 Python 为 PDF 添加水印。
- [统计工件](/pdf/zh/python-net/counting-artifacts/) - 使用 Python 统计 PDF 中的伪影。
- [管理 PDF 页眉和页脚](/pdf/zh/python-net/artifacts-header-footer/) - 管理 PDF 文档的页眉和页脚。

- 当您需要在不更改主文档内容流的情况下管理装饰性或结构性 PDF 元素时，这些教程非常有用。
