---
title: 在 .NET 中通过 Python 使用伪元素
linktitle: 使用伪元素
type: docs
weight: 170
url: /zh/python-net/artifacts/
description: Aspose.PDF for Python via .NET 允许您向 PDF 页面添加背景图像，并使用 Artifact 类获取每个水印。
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 向 PDF 添加伪元素
Abstract: 本文探讨了 PDF 文档中伪元素的概念和应用，特别关注它们在提升可访问性和性能方面的作用。伪元素是非内容元素，例如装饰性或布局组件，且不传达文档含义。文章重点介绍了在 Aspose.PDF for Python via .NET 库中使用 `Artifact` 类来管理这些元素，提供了 `custom_type`、`contents` 和 `opacity` 等属性，以实现细致的自定义。还介绍了用于处理特定伪元素类型的相关类。实用示例演示了检索水印、添加背景图像、统计伪元素类型以及实现 Bates 编号等操作。
---

PDF 中的伪元素是图形对象或其他不属于文档实际内容的元素。它们通常用于装饰、布局或背景目的。伪元素的例子包括页眉、页脚、分隔线或不传达任何意义的图像。

PDF 中使用伪元素的目的是区分内容元素和非内容元素。这对可访问性至关重要，因为屏幕阅读器和其他辅助技术可以忽略伪元素，专注于相关内容。伪元素还可以提升 PDF 文档的性能和质量，因为它们可以在打印、搜索或复制时被省略。

要在 PDF 中将元素创建为伪元素，需要使用 [Artifact 类](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/)。
它包含以下有用属性：

- **custom_type** - 获取伪元素类型的名称。如果伪元素类型非标准，可使用此属性。
- **custom_subtype** - 获取伪元素子类型的名称。如果伪元素子类型不是标准子类型，可使用此属性。
- **type** - 获取伪元素类型。
- **subtype** - 获取伪元素子类型。如果伪元素具有非标准子类型，可通过 CustomSubtype 读取子类型名称。
- **contents** - 获取伪元素内部操作符的集合。
- **form** - 获取伪元素的 XForm（如果使用了 XForm）。
- **rectangle** - 获取伪元素的矩形。
- **position** - 获取或设置伪元素位置。如果指定了此属性，则会忽略边距和对齐方式。
- **right_margin** - 伪元素的右边距。如果在 Position 属性中显式指定了位置，则此值被忽略。
- **left_margin** - 伪元素的左边距。如果在 Position 属性中显式指定了位置，则此值被忽略。
- **top_margin** - 伪元素的上边距。如果在 Position 属性中显式指定了位置，则此值被忽略。
- **bottom_margin** - 伪元素的下边距。如果在 Position 属性中显式指定了位置，则此值被忽略。
- **artifact_horizontal_alignment** - 伪元素的水平对齐方式。如果在 Position 属性中显式指定了位置，则此值被忽略。
- **artifact_vertical_alignment** - 伪元素的垂直对齐方式。如果在 Position 属性中显式指定了位置，则此值被忽略。
- **rotation** - 获取或设置伪元素的旋转角度。
- **text** - 获取伪元素的文本。
- **image** - 获取伪元素的图像（如果存在）。
- **opacity** - 获取或设置伪元素的透明度。可能的取值范围为 0..1。
- **lines** - 多行文本伪元素的行集合。
- **text_state** - 伪元素文本的文本状态。
- **is_background** - 如果为 true，则伪元素放置在页面内容后面。

以下类也可能对处理伪元素有用：

- [ArtifactCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)
- [BackgroundArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/)
- [HeaderArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerartifact/)
- [FooterArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/footerartifact/)
- [WatermarkArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/watermarkartifact/)
- [Bates 编号](https://reference.aspose.com/pdf/python-net/aspose.pdf/)

请查看本文的以下章节：

- [添加背景](/pdf/python-net/add-backgrounds/) - 使用 Python 向 PDF 文件添加背景图像。
- [添加 Bates 编号](/pdf/python-net/add-bates-numbering/) - 向 PDF 添加 Bates 编号。
- [添加水印](/pdf/python-net/add-watermarks/) - 了解如何使用 Python 向 PDF 添加水印。
- [统计伪元素](/pdf/python-net/counting-artifacts/) - 使用 Python 统计 PDF 中的伪元素。

