---
title: 使用C++为PDF添加水印
linktitle: 添加水印
type: docs
weight: 90
url: zh/cpp/add-watermarks/
description: 本文解释了使用C++编程在PDF中处理工件和获取水印的功能。
lastmod: "2021-12-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

水印是一个半透明的图像，通常包含一个徽标或印章，用于识别谁创建了该文档或图像。

**Aspose.PDF for C++**允许使用Artifact类向PDF文档添加水印。请查看本文以解决您的任务。

使用Adobe Acrobat创建的水印被称为工件（如PDF规范的14.8.2.2真实内容和工件中所述）。为了处理工件，Aspose.PDF有两个类：[Artifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact)和[ArtifactCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact_collection)。

为了获取特定页面上的所有工件，[Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)类拥有Artifacts属性。 这个主题解释了如何处理PDF文件中的工件。

## 处理工件

[Artifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact) 类包含以下属性：

**Artifact.Type** – 获取工件类型（支持 Artifact.ArtifactType 枚举的值，其中包括 Background, Layout, Page, Pagination 和 Undefined）。
**Artifact.Subtype** – 获取工件子类型（支持 Artifact.ArtifactSubtype 枚举的值，其中包括 Background, Footer, Header, Undefined, Watermark）。

{{% alert color="primary" %}}

请注意，使用 Adobe Acrobat 创建的水印具有 Pagination 类型和 Watermark 子类型。

{{% /alert %}}

**Artifact.Contents** – 获取工件内部操作符的集合。其支持的类型是 System.Collections.ICollection。
**Artifact.Form** – 获取工件的 XForm（如果使用了 XForm）。水印、页眉和页脚工件包含显示所有工件内容的 XForm。

**Artifact.Image** – 获取工件的图像（如果图像存在，否则为 null）。**Artifact.Text** – 获取工件的文本。  
**Artifact.Rectangle** – 获取工件在页面上的位置。  
**Artifact.Rotation** – 获取工件的旋转角度（以度为单位，正值表示逆时针旋转）。  
**Artifact.Opacity** – 获取工件的不透明度。可能的值范围是0到1，其中1是完全不透明。

## 编程示例：如何在PDF文件上添加水印

以下代码片段展示了如何使用C++在PDF文件的第一页获取每个水印。

```cpp
void GettingWatermarks() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("watermark.pdf");
    String outputFileName("watermark_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto artifact = MakeObject<WatermarkArtifact>();
    auto textState = MakeObject<TextState>();
    textState->set_FontSize(72);
    textState->set_ForegroundColor(Color::get_Blue());
    textState->set_Font(FontRepository::FindFont(u"Courier"));
    artifact->SetTextAndState(u"WATERMARK", textState);
    artifact->set_ArtifactHorizontalAlignment (HorizontalAlignment::Center);
    artifact->set_ArtifactVerticalAlignment (VerticalAlignment::Center);
    artifact->set_Rotation(45);
    artifact->set_Opacity(0.5);
    artifact->set_IsBackground(true);

    document->get_Pages()->idx_get(1)->get_Artifacts()->Add(artifact);

    document->Save(_dataDir + outputFileName);
}
```