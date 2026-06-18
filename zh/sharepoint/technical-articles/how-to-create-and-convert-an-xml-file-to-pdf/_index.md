---
title: 如何创建并将 XML 文件转换为 PDF
linktitle: 如何创建并将 XML 文件转换为 PDF
type: docs
weight: 30
url: /zh/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/
lastmod: "2026-06-18"
description: PDF SharePoint API 能够创建并将 XML 文件转换为 PDF 格式。
---

{{% alert color="primary" %}}

Aspose.PDF for SharePoint 基于我们屡获殊荣的 Aspose.PDF for .NET 组件构建。Aspose.PDF for .NET 提供了从零创建 PDF 文档到操作现有 PDF 文件的卓越功能。在这些功能中，XML 转 PDF 转换是该产品支持的优秀功能之一。因此，我们相信 Aspose.PDF for SharePoint 同样能够将 XML 文件转换为 PDF 格式。

{{% /alert %}}

## **创建 XML 文件并将其转换为 PDF**

{{% alert color="primary" %}}

本文将一步一步带您完成创建 XML 文件并将其转换为 PDF 的过程：

1. [创建一个 XML 文件](/pdf/zh/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-1-create-xml-file).
2. [创建 PDF 模板](/pdf/zh/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-2-create-pdf-template).
3. [加载 XML 模板](/pdf/zh/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-3-load-xml-template).
4. [指定源路径的路径](/pdf/zh/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-4-specify-source-file-path).
5. [指定文件属性](/pdf/zh/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-5-specify-file-properties).
6. [将文件导出为 PDF](/pdf/zh/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-6-export-to-pdf).
7. [保存 PDF 文件](/pdf/zh/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-7-save-pdf-document).
#### **步骤 1：创建 XML 文件**
首先基于 Aspose.PDF for .NET 文档对象模型创建 XML 文件。

根据 Aspose.PDF for .NET DOM，PDF 文档包含一系列 Section 对象，且每个 Section 包含一个或多个 Paragraph 元素。Text 是段落级对象，可能包含一个或多个 segment。下面，将示例文本字符串添加到 Segment 对象，再添加到 Text 对象。最后，Text 元素被添加到 Section 对象的 paragraphs 集合中。

**XML**

{{< highlight csharp >}}



<?xml version="1.0" encoding="utf-8" ?>

  <Pdf xmlns="Aspose.PDF">

   <Section>

    <Text>

            <Segment>Hello World</Segment>

    </Text>

   </Section>

  </Pdf>



{{< /highlight >}}
#### **步骤 2：创建 PDF 模板**
在继续之前，请确保 SharePoint Foundation server 2010 已在进行转换的系统上正确安装和配置。

1. 登录到 SharePoint 站点。
1. 选择 **Site Action** 和 **All Items**。
1. 选择 **Create** 选项，并从列表中选择 **PDF Template**。
1. 输入模板名称。
1. 点击 **Create**。




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_1.png)
#### **第3步：加载 XML 模板**
模板创建后，加载 [XML 文件](/pdf/zh/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/):

1. 在 PDF 模板页面，选择 **添加新项**。




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_2.png)
#### **步骤 4：指定源文件路径**
在文档上传对话框中：

1. 单击 **浏览** 并在系统中定位 XML 文件。您可以勾选复选框以覆盖现有文件选项。
1. 按 **确定** 按钮。




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_3.png)
#### **步骤 5：指定文件属性**
加载文件后，向必填字段（标有红色星号 *）中添加信息。

在本示例中，已添加示例描述并完成以下字段：

1. 文档的简要描述。
1. 在 **Assigned List Types** 字段中输入 **AllListTypes**。
1. 从 **Type** 菜单中选择 **List**。
   确保状态保持为 **Active**。
1. 单击 **Save** 以保存属性。




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_4.png)
#### **第 6 步：导出为 PDF**
当 XML 文件已添加到 PDF 模板时：
任意一种：

1. 右键单击 test.xml 文件。
1. 从菜单中选择 **Export to PDF**。

或：

1. 从 **Library Tools** 中选择 **Aspose Tools**。
1. 点击 **Export**。




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_5.png)
#### **步骤 7：保存 PDF 文档**
1. 在 Export to PDF 对话框中，选择 **Template storage**（源文件存储的位置）。
1. 从 **Template name** 菜单中选择要导出的文件。
1. 点击 **Export to PDF** 以保存最终的 PDF 文档。




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_6.png)
#### **打开 PDF**
PDF 文档已保存并可打开。如下图所示，请注意 XML 中 {segment] 标记中的短语 “Hello World”。另请注意，PDF 生产者是 Aspose.PDF for SharePoint。




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_7.png)

{{% /alert %}}
