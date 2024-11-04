---
title: 在 SharePoint 中创建安全 PDF

linktitle: 创建安全 PDF

type: docs

weight: 60

url: /sharepoint/creating-a-secure-pdf/

lastmod: "2020-12-16"

description: 使用 PDF SharePoint API，您可以在 SharePoint 中生成安全的、加密的 PDF 并指定其密码。

---

{{% alert color="primary" %}}

Aspose.PDF for SharePoint 支持创建安全的 PDF。安装 Aspose.PDF for SharePoint 后，站点设置中会添加一个 **PDF Secure Settings** 选项。在这里，您可以设置用户密码、所有者密码以及从算法列表中选择的任何值来加密输出 PDF。算法列表提供了不同组合的加密算法和密钥大小。传递您选择的值。

本文演示了如何使用 Aspose.PDF for SharePoint 生成加密 PDF。

{{% /alert %}}

## **创建安全 PDF**

为了演示该功能，首先我们为所有者和用户密码以及加密算法配置 **PDF Secure Setting** 选项。 The example then merges two documents from a document library.

### **设置 PDF 安全设置选项**

从站点设置中打开 **PDF 安全设置** 选项并设置算法、所有者密码和用户密码。

在加密 PDF 文件时指定不同的用户和所有者密码。

- 如果设置了用户密码，则需要提供该密码才能打开 PDF。Acrobat Reader 会提示用户输入用户密码。如果错误，文档将不会打开。

- 如果设置了所有者密码，则控制如打印、编辑、提取、评论等权限。Acrobat Reader 根据权限设置不允许使用这些功能。如果要设置/更改权限，Acrobat 需要此密码。

![todo:image_alt_text](creating-a-secure-pdf_1.png)

### **合并文档**

使用 **转换为 PDF** 选项合并两个文档。此功能将多个非 PDF 文件（HTML、文本或图像）合并为一个 PDF 文件。

1. 打开文档库并从列表中选择所需的文档。

![todo:image_alt_text](creating-a-secure-pdf_2.png)

1. 使用库工具中的**合并为PDF**选项保存输出文件。系统会提示您将输出文件保存到磁盘。

![todo:image_alt_text](creating-a-secure-pdf_3.png)

### **输出**

输出文件已加密。

![todo:image_alt_text](creating-a-secure-pdf_4.png)