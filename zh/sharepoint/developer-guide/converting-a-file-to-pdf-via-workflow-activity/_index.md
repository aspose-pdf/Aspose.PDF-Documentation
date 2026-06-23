---
title: 通过工作流活动将文件转换为 PDF
linktitle: 通过工作流活动将文件转换为 PDF
type: docs
weight: 50
url: /zh/sharepoint/converting-a-file-to-pdf-via-workflow-activity/
lastmod: "2026-06-18"
description: PDF SharePoint API 可在将文档转换为 PDF 的 SharePoint 工作流中使用。
---

{{% alert color="primary" %}}

对工作流的支持是 Microsoft Office SharePoint Server 的关键功能。工作流帮助根据业务逻辑自动化文档的流转，并简化文档组织的成本和时间。本篇文章演示如何在工作流中使用 Aspose.PDF for SharePoint 将文档转换为 PDF。

{{% /alert %}}
## **设置工作流**

此示例创建一个工作流，将文档库中的任何新项目转换为 PDF 格式并存储到另一个文档库中。示例使用 **Personal Documents** 库作为源库，使用 **Shared Documents** 库中的 **Pdf** 子文件夹作为目标库。

Aspose.PDF for SharePoint 支持 HTML、文本和图像文件的转换。

### **使用 SharePoint Designer 设计工作流**

1. 打开 **SharePoint Designer** 并连接到将实现工作流的站点。
1. 从 **site objects** 中选择 **Workflows**，然后打开 **List Workflow**。
1. 选择 **Personal Documents** 库，以在文档库中创建并附加一个新的列表工作流。

   **从菜单中选择 Personal Documents**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_1.png)


1. 通过输入工作流名称和描述，将列表工作流创建并附加到 **Personal Documents** 库。
1. 单击 **OK** 完成此步骤。

   **创建列表工作流**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_2.png)



出现工作流步骤编辑器。该编辑器用于为工作流定义条件和操作。现在，从 **Aspose Actions** 添加一个操作，将新文档转换为 PDF，且没有任何条件。

1. 从 **Action** 菜单中选择 **Convert file to PDF via Aspose.PDF** 操作。

   **选择操作**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_3.png)


1. 配置操作参数：
   1. 将 **this folder** 参数设置为目标文件夹。
   1. 可以保持其他操作参数为默认值，或在操作属性窗口中进行设置。**Overwrite** 参数的默认值为 false。

      **工作流编辑器**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_4.png)



**设置目标库**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_5.png)



**设置属性**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_6.png)




1. 在 **Workflow** 菜单中，选择 **Workflow Settings**。
1. 选择 **在创建新项目时自动启动工作流**，并清除 **启动选项** 中的其他选项。

   **设置启动选项**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_7.png)



工作流设计已完成。

1. 保存并发布工作流，以在 SharePoint 网站上实施它。

### **测试工作流**

测试工作流的方法：

1. 打开 SharePoint 站点并将新文档上传到 **Personal Documents** 文档库。
   Aspose.PDF for SharePoint 支持将 HTML 文件、文本文件和图像（JPG、PNG、GIF、TIFF 和 BMP*）转换为 PDF。工作流已配置为在创建新项时自动启动，文件会自动处理。
1. 刷新浏览器。
   工作流状态显示在工作流列中，此例为 **Aspose.PDF Workflow**。

   **将文档添加到源库**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_8.png)




1. 打开目标文档库以查看已转换的文档。本示例中的路径为 **Shared Documents/Pdf**。

   **目标库**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_9.png)

