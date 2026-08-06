---
title: 通过工作流程活动将文件转换为 PDF
linktitle: 通过工作流程活动将文件转换为 PDF
type: docs
weight: 50
url: /zh/sharepoint/converting-a-file-to-pdf-via-workflow-activity/
lastmod: "2020-12-16"
description: PDF SharePoint API 可以在将文档转换为 PDF 的 SharePoint 工作流中使用。
---

{{% alert color="primary" %}}

Support for workflows is key functionality of Microsoft Office SharePoint Server. Workflows help automate movement of documents according to business logic and streamline the cost and time of document organization. This article demonstrates how to use Aspose.PDF for SharePoint in a workflow that converts a document to PDF.

{{% /alert %}}

## Setting up a Workflow

此示例创建一个工作流，将文档库中的任何新项目转换为 PDF 格式并将其存储在另一个文档库中。该示例使用 **个人文档** 库作为源库，使用 **共享文档** 库中的 *​​Pdf** 子文件夹作为目标库。

Aspose.PDF for SharePoint supports conversion of HTML, text and image files.

### Design the Workflow using SharePoint Designer

1. Open **SharePoint Designer** and connect to the site where the workflow will be implemented.
1. Select **Workflows** from **site objects** and then open **List Workflow**.
1. 选择 **个人文档** 库以创建新的列表工作流程并将其附加到文档库。

   **从菜单中选择个人文档**

![Converting file to PDF via Workflow Activity_1](converting-a-file-to-pdf-via-workflow-activity_1.png)

1. Create and attach the list workflow to the **Personal Documents** library by typing a workflow name and description.
1. Click **OK** to complete this step.

   **Creating a list workflow**

![Converting file to PDF via Workflow Activity_2](converting-a-file-to-pdf-via-workflow-activity_2.png)

将出现工作流程步骤编辑器。这用于定义工作流程的条件和操作。现在添加一个操作，从 **Aspose Actions** 无条件地将新文档转换为 PDF。

1. Select the **Convert file to PDF via Aspose.PDF** action from the **Action** menu.

   **Selecting and action**

![Converting file to PDF via Workflow Activity_3](converting-a-file-to-pdf-via-workflow-activity_3.png)

1. Configure the action parameters:
   1. Set **this folder** parameter to the destination folder.
   1. Either leave the other action parameters as default values or set using the action properties window. The default value for the **Overwrite** parameter is false.

      **The Workflow Editor**

![Converting file to PDF via Workflow Activity_4](converting-a-file-to-pdf-via-workflow-activity_4.png)

**Setting the destination library**

![Converting file to PDF via Workflow Activity_5](converting-a-file-to-pdf-via-workflow-activity_5.png)

**Setting the properties**

![Converting file to PDF via Workflow Activity_6](converting-a-file-to-pdf-via-workflow-activity_6.png)

1. 从 **工作流程** 菜单中，选择 **工作流程设置**。
1. 选择**创建新项目时自动启动工作流程**并从**启动选项**中清除其他选项。

   **Setting the start options**

![Converting file to PDF via Workflow Activity_7](converting-a-file-to-pdf-via-workflow-activity_7.png)

The workflow design is finished.

1. 保存并发布工作流以在 SharePoint 网站上实施它。

### Test the Workflow

To test the workflow:

1. 打开 SharePoint 网站并将新文档上传到 **个人文档** 文档库。
   Aspose.PDF for SharePoint supports conversion from HTML files, text files, and images (JPG, PNG, GIF, TIFF and BMP*) to PDF. The workflow is configured to start automatically when a new item is created, so files are process automatically.
1. 刷新浏览器。
   工作流程状态显示在工作流程列中，在本例中为 **Aspose.PDF Workflow**。

   **Adding a document to the source library**

![Converting file to PDF via Workflow Activity_8](converting-a-file-to-pdf-via-workflow-activity_8.png)

1. Open the destination document library to view the converted document. **Shared Documents/Pdf** is the path in this example.

   **目标图书馆**

![Converting file to PDF via Workflow Activity_9](converting-a-file-to-pdf-via-workflow-activity_9.png)

