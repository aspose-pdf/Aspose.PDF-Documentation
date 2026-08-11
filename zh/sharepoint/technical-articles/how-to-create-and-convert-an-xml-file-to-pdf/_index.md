---
title: 如何创建 XML 文件并将其转换为 PDF
linktitle: 如何创建 XML 文件并将其转换为 PDF
type: docs
weight: 30
url: /zh/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/
lastmod: "2020-12-16"
description: PDF SharePoint API 能够创建 XML 文件并将其转换为 PDF 格式。
---

{{% alert color="primary" %}}

Aspose.PDF for SharePoint 构建于我们屡获殊荣的 Aspose.PDF for .NET 组件之上。 Aspose.PDF for .NET 提供了从头开始创建 PDF 文档到操作现有 PDF 文件的显着功能。在这些功能中，XML 到 PDF 转换是该产品支持的重要功能之一。因此我们相信Aspose.PDF for SharePoint 也能够将XML 文件转换为PDF 格式。

{{% /alert %}}

## 创建 XML 文件并将其转换为 PDF

{{% alert color="primary" %}}

本文将逐步引导您完成创建 XML 文件并将其转换为 PDF 的过程：

1. [创建 XML 文件](/pdf/zh/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-1-create-xml-file)。
2. [创建 PDF 模板](/pdf/zh/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-2-create-pdf-template)。
3. [加载 XML 模板](/pdf/zh/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-3-load-xml-template)。
4. [指定源路径的路径](/pdf/zh/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-4-specify-source-file-path)。
5. [指定文件属性](/pdf/zh/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-5-specify-file-properties)。
6. [将文件导出为 PDF](/pdf/zh/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-6-export-to-pdf)。
7. [保存PDF文件](/pdf/zh/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-7-save-pdf-document)

### 第 1 步：创建 XML 文件

首先创建一个基于 Aspose.PDF for .NET 文档对象模型的 XML 文件。

根据Aspose.PDF for .NET DOM，PDF文档包含Section对象的集合，而Section包含一个或多个Paragraph元素。文本是段落级对象，可能包含一个或多个段。下面，将示例文本字符串添加到 Segment 对象并添加到 Text 对象。最后，Text 元素被添加到Section 对象的段落集合中。

```xml

<?xml version="1.0" encoding="utf-8" ?>

  <Pdf xmlns="Aspose.PDF">

   <Section>

    <Text>

            <Segment>Hello World</Segment>

    </Text>

   </Section>

  </Pdf>

```

### 第 2 步：创建 PDF 模板

在继续之前，请确保在将进行转换的系统上正确安装和配置 SharePoint Foundation Server 2010。

1. 登录到 SharePoint 网站。
1. 选择**网站操作**和**所有项目**。
1. 选择 **创建** 选项，然后从列表中选择 **PDF 模板**。
1. 输入模板名称。
1. 单击**创建**。

![Create PDF Template](how-to-create-and-convert-an-xml-file-to-pdf_1.png)

### 第 3 步：加载 XML 模板

创建模板后，加载[XML 文件](/pdf/zh/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/)

1. 在 PDF 模板页面上，选择“**添加新项目**”。

![Load XML Template](how-to-create-and-convert-an-xml-file-to-pdf_2.png)

### 步骤4：指定源文件路径

在文档上传对话框中：

1. 单击 **浏览** 并找到系统上的 XML 文件。您可以启用复选框来覆盖现有文件选项。
1. 按 **确定** 按钮。

![Specify Source File Path](how-to-create-and-convert-an-xml-file-to-pdf_3.png)

### 步骤 5：指定文件属性

加载文件后，将信息添加到必填字段（标有红色星号：*）。

对于此示例，已添加示例描述并完成以下字段：

1. 该文档的简要说明。
1. 在“分配的列表类型”字段中输入“AllListTypes”。
1. 从“类型”菜单中选择“列表”。
   确保状态保持**活动**。
1. 单击“**保存**”保存属性。

![Specify File Properties](how-to-create-and-convert-an-xml-file-to-pdf_4.png)

### 第 6 步：导出为 PDF

将 XML 文件添加到 PDF 模板后：
任何一个：

1. 右键单击 test.xml 文件。
1. 从菜单中选择 **导出为 PDF**。

或者：

1. 从 **库工具** 中选择 **Aspose 工具**。
1. 单击**导出**。

![Export to PDF](how-to-create-and-convert-an-xml-file-to-pdf_5.png)

### 第7步：保存PDF文档

1. 在“导出为 PDF”对话框中，选择“**模板存储**”（存储源文件的位置）。
1. 从 **模板名称** 菜单中选择要导出的文件。
1. 单击 **导出为 PDF** 以保存最终的 PDF 文档。

![Save PDF Document](how-to-create-and-convert-an-xml-file-to-pdf_6.png)

## 打开 PDF

PDF文档已保存并可以打开。在下图中，请注意 XML 段标记中的短语“Hello World”。另请注意，PDF 生成器是 Aspose.PDF for SharePoint。

![開啟PDF文件](how-to-create-and-convert-an-xml-file-to-pdf_7.png)

{{% /alert %}}
