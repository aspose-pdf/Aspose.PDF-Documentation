---
title: 将文件转换为PDF通过工作流活动
type: docs
weight: 50
url: zh/sharepoint/converting-a-file-to-pdf-via-workflow-activity/
lastmod: "2020-12-16"
description: PDF SharePoint API可以在将文档转换为PDF的SharePoint工作流中使用。
---

{{% alert color="primary" %}}

工作流支持是Microsoft Office SharePoint Server的关键功能。工作流有助于根据业务逻辑自动化文档的移动，并简化文档组织的成本和时间。本文演示了如何在将文档转换为PDF的工作流中使用Aspose.PDF for SharePoint。

{{% /alert %}}
## **设置工作流**

此示例创建一个工作流，将文档库中的任何新项目转换为PDF格式，并将其存储在另一个文档库中。示例使用**个人文档**库作为源库，使用**共享文档**库中的**Pdf**子文件夹作为目标库。

Aspose.PDF for SharePoint支持HTML、文本和图像文件的转换。

### **设计工作流程使用SharePoint Designer**

1. 打开**SharePoint Designer**并连接到将要实现工作流的网站。
2. 从**站点对象**中选择**Workflows**，然后打开**List Workflow**。
3. 选择**个人文档**库以创建并附加新的列表工作流到文档库。

   **从菜单中选择个人文档**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_1.png)

4. 通过输入工作流名称和描述来创建并附加列表工作流到**个人文档**库。
5. 点击**OK**完成这一步。

   **创建列表工作流**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_2.png)

出现工作流步骤编辑器。此编辑器用于定义工作流的条件和操作。现在从**Aspose Actions**添加一个操作，在没有任何条件的情况下将新文档转换为PDF。
1. 从**操作**菜单中选择**通过 Aspose.PDF 将文件转换为 PDF**操作。

   **选择和操作**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_3.png)

1. 配置操作参数：
   1. 将**此文件夹**参数设置为目标文件夹。
   1. 将其他操作参数保留为默认值，或使用操作属性窗口进行设置。**覆盖**参数的默认值为 false。

   **工作流编辑器**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_4.png)

**设置目标库**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_5.png)

**设置属性**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_6.png)

1. 从**工作流**菜单中，选择**工作流设置**。
1. 选择**在创建新项目时自动启动工作流**，并清除**启动选项**中的其他选项。

   **设置启动选项**
![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_7.png)

工作流设计已完成。

1. 保存并发布工作流以在 SharePoint 站点上实施。

### **测试工作流**

要测试工作流：

1. 打开 SharePoint 站点并上传新文档到**个人文档**文档库。  
   Aspose.PDF for SharePoint 支持从 HTML 文件、文本文件和图像（JPG、PNG、GIF、TIFF 和 BMP*）转换为 PDF。工作流配置为在新项目创建时自动启动，因此文件会自动处理。
1. 刷新浏览器。  
   工作流状态显示在工作流列中，在本例中为 **Aspose.PDF Workflow**。

   **将文档添加到源库**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_8.png)

1. 打开目标文档库以查看已转换的文档。在此示例中，路径为 **Shared Documents/Pdf**。

   **目标库**
![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_9.png)