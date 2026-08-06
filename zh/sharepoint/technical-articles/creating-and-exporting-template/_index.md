---
title: 创建和导出模板
linktitle: Creating and Exporting Template
type: docs
weight: 10
url: /zh/sharepoint/creating-and-exporting-template/
lastmod: "2020-12-16"
description: You can create and export templates to PDF in SharePoint using PDF SharePoint API.
---

{{% alert color="primary" %}}

本文介绍如何使用 Aspose.PDF for SharePoint 创建和导出模板。

从Aspose.PDF for SharePoint 1.9.2开始，PDF模板支持还涵盖了SharePoint子网站。

{{% /alert %}}

## 创建和导出模板

{{% alert color="primary" %}}

To use the Aspose.PDF for SharePoint export feature, first create a list that uses “PDF Templates”.

创建使用 PDF 模板的列表：

![Create PDF Template List](creating-and-exporting-template_1.png)

创建两个文档模板：任务表单模板和任务列表模板：

![Document Templates](creating-and-exporting-template_2.png)

模板表单允许您输入以下信息：

- **Name**: the template's file name.
- **标题**：模板的标题。 （默认情况下，与文件名相同。）
- **描述**：模板的描述。良好的描述使模板更易于使用。
- **分配的列表类型**：逗号分隔的列表 ID（与模板相关。此字段还可能包含值
- **所有列表类型**。仅当 **Type** 字段设置为 **List** 时，此字段才适用。
- **分配的内容类型**：与模板相关的逗号分隔内容类型 ID。该字段可能包含设置为 **AllListTypes**。仅当 **Type** 字段设置为 **Item** 时，此字段才适用。
- **类型**：列表模板或项目模板。
- **状态**：选项为活动、非活动（对所有人不可见）和调试（仅对管理员可见）。

任务列表模板形式：

![Task List Templates](creating-and-exporting-template_3.png)

任务表单模板形式：

![Task Form Templates](creating-and-exporting-template_4.png)

保存后，新模板将显示在模板列表中，可供使用：

两个任务列表模板：*

![Task List Templates](creating-and-exporting-template_5.png)

任务表单模板：

![Task Form Templates](creating-and-exporting-template_6.png)

### 开发模板

模板是基于 Aspose XML PDF 的 XML 文件。要制作列表模板，请将与 SharePoint 目标内容类型字段的内部名称相关的特殊标记放入 XML PDF 文件中。

### 标记

- **SPListItemsCount** – 替换为列表项计数。
- **SPListTitle** – 替换为列表标题。
- **SPTableIterator** – 放置到第一个表格单元格并标记表格以进行完整迭代。
- **SPRowIterator** – 放置到第一个表格单元格并标记表格以进行行迭代。
- **SPField** – 替换为项目字段的值。

如需参考，请下载[模板 XML 文件](attachments/8421394/8618082.zip)。

### 导出为 PDF

When a template is completely configured, you are ready to export lists or items to PDF files.

使用任务列表模板将列表导出为 PDF：

![Export to PDF](creating-and-exporting-template_7.png)

{{% /alert %}}

