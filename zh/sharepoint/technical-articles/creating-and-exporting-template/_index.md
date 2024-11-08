---
title: 创建和导出模板
type: docs
weight: 10
url: /zh/sharepoint/creating-and-exporting-template/
lastmod: "2020-12-16"
description: 您可以使用 SharePoint 的 PDF SharePoint API 创建和导出模板为 PDF。
---

{{% alert color="primary" %}}

本文展示了如何使用 Aspose.PDF for SharePoint 创建和导出模板。

从 Aspose.PDF for SharePoint 1.9.2 开始，PDF 模板支持也涵盖了 SharePoint 子网站。

{{% /alert %}}

## **创建和导出模板**
{{% alert color="primary" %}}

要使用 Aspose.PDF for SharePoint 的导出功能，首先创建一个使用“PDF 模板”的列表。

创建一个使用 PDF 模板的列表：

![todo:image_alt_text](creating-and-exporting-template_1.png)

创建了两个文档模板，任务表单模板和任务列表模板：

![todo:image_alt_text](creating-and-exporting-template_2.png)

模板表单让您输入以下信息：

- **Name**: 模板的文件名。
- **Title**: 模板的标题。
 - **描述**: 模板的描述。一个好的描述可以使模板更容易使用。
- **分配的列表类型**: 逗号分隔的列表ID（与模板相关。此字段也可能包含值 **AllListTypes**。此字段仅在 **Type** 字段设置为 **List** 时适用）。
- **分配的内容类型**: 逗号分隔的内容类型ID（与模板相关。此字段可能设置为 **AllListTypes**。此字段仅在 **Type** 字段设置为 **Item** 时适用）。
- **类型**: 列表模板或项目模板之一。
- **状态**: 选项为激活，未激活（对所有人不可见），以及调试（仅对管理员可见）。

**任务列表模板表单:**

![todo:image_alt_text](creating-and-exporting-template_3.png)

**任务表单模板表单:**

![todo:image_alt_text](creating-and-exporting-template_4.png)

保存后，新模板将显示在模板列表中，可以使用：

**两个任务列表模板：**
![todo:image_alt_text](creating-and-exporting-template_5.png)

**任务表单模板：**

![todo:image_alt_text](creating-and-exporting-template_6.png)

#### **开发模板**
模板是基于 Aspose XML PDF 的 XML 文件。要为列表创建模板，请将与 SharePoint 目标内容类型字段的内部名称相关的特殊标记放入 XML PDF 文件中。
##### **标记**
- **SPListItemsCount** – 被列表项的数量替换。
- **SPListTitle** – 被列表标题替换。
- **SPTableIterator** – 放置在第一个表格单元格中，并标记表格进行完整迭代。
- **SPRowIterator** – 放置在第一个表格单元格中，并标记表格进行行迭代。
- **SPField** – 被项字段的值替换。

如需参考，请下载 [模板 XML 文件](attachments/8421394/8618082.zip)。
#### **导出为 PDF**
当模板完全配置好后，您可以准备将列表或项目导出为 PDF 文件。

**使用任务列表模板将列表导出为 PDF：**
![todo:图片替代文本](creating-and-exporting-template_7.png)

{{% /alert %}}
