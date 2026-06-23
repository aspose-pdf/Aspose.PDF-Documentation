---
title: 创建和导出模板
linktitle: 创建和导出模板
type: docs
weight: 10
url: /zh/sharepoint/creating-and-exporting-template/
lastmod: "2026-06-18"
description: 您可以使用 PDF SharePoint API 在 SharePoint 中创建并导出 PDF 模板。
---

{{% alert color="primary" %}}

本文展示了如何使用 Aspose.PDF for SharePoint 创建和导出模板。

从 Aspose.PDF for SharePoint 1.9.2 开始，PDF 模板支持也覆盖 SharePoint 子站点。

{{% /alert %}}

## **创建和导出模板**
{{% alert color="primary" %}}

要使用 Aspose.PDF for SharePoint 的导出功能，首先创建一个使用“PDF Templates”的列表。

创建使用 PDF 模板的列表：

![todo:image_alt_text](creating-and-exporting-template_1.png)

创建了两个文档模板，Task Form Templates 和 Task List Templates：

![todo:image_alt_text](creating-and-exporting-template_2.png)



模板表单允许您输入以下信息：

- **Name**：模板的文件名。
- **Title**：模板的标题。（默认情况下，与文件名相同。）
- **Description**：模板的描述。良好的描述可以使模板更易于使用。
- **已分配的列表类型**：逗号分隔的列表 ID（与模板相关。此字段还可能包含值 **AllListTypes**。仅在 **Type** 字段设置为 **List** 时适用）。
- **已分配的内容类型**：逗号分隔的内容类型 ID（与模板相关。此字段可能被设置为 **AllListTypes**。仅在 **Type** 字段设置为 **Item** 时适用）。
- **Type**：列表模板或项目模板之一。
- **Status**：选项包括 active、inactive（对所有人不可见）和 debugging（仅对管理员可见）。

**任务列表模板表单**：

![todo:image_alt_text](creating-and-exporting-template_3.png)




**任务表单模板表单**：

![todo:image_alt_text](creating-and-exporting-template_4.png)




保存后，新的模板会出现在模板列表中，随时可用：

**两个任务列表模板：**

![todo:image_alt_text](creating-and-exporting-template_5.png)



**一个任务表单模板：**

![todo:image_alt_text](creating-and-exporting-template_6.png)



#### **开发模板**
模板是基于 Aspose XML PDF 的 XML 文件。要为列表制作模板，请在 XML PDF 文件中放入与 SharePoint 目标内容类型字段的内部名称相关的特殊标记。
##### **标记**
- **SPListItemsCount** – 替换为列表项的计数。
- **SPListTitle** – 替换为列表标题。
- **SPTableIterator** – 放置在第一个表格单元格并标记表格进行完整迭代。
- **SPRowIterator** – 放置在第一个表格单元格并标记表格进行行迭代。
- **SPField** – 替换为项目字段的值。

供参考，请下载 [模板 XML 文件](attachments/8421394/8618082.zip).
#### **导出为 PDF**
当模板完全配置好后，您可以将列表或项目导出为 PDF 文件。

**使用任务列表模板将列表导出为 PDF：**

![todo:image_alt_text](creating-and-exporting-template_7.png)

{{% /alert %}}
