---
title: 在 SharePoint 中创建安全 PDF
linktitle: 创建安全 PDF
type: docs
weight: 60
url: /zh/sharepoint/creating-a-secure-pdf/
lastmod: "2026-06-18"
description: 使用 PDF SharePoint API，您可以生成安全的加密 PDF，并在 SharePoint 中指定其密码。
---

{{% alert color="primary" %}}

Aspose.PDF for SharePoint 支持创建安全的 PDF。安装 Aspose.PDF for SharePoint 会在站点设置中添加一个 **PDF Secure Settings** 选项。在此，您可以设置用户密码、所有者密码以及算法列表中的任意值以加密输出的 PDF。算法列表提供不同的加密算法和密钥大小的组合。请选择您想要的值。

本文演示如何使用 Aspose.PDF for SharePoint 生成加密的 PDF。

{{% /alert %}}

## **创建安全 PDF**

为演示此功能，首先我们配置 **PDF Secure Setting** 选项的所有者密码、用户密码和加密算法。随后示例会合并来自文档库的两个文档。

### **设置 PDF Secure Setting 选项**

在站点设置中打开 **PDF Secure Settings** 选项，并设置算法、所有者密码和用户密码。

在加密 PDF 文件时指定不同的用户密码和所有者密码。

- 用户密码（如果设置）是打开 PDF 时需要提供的密码。Acrobat Reader 会提示用户输入用户密码。如果密码错误，文档将无法打开。
- 所有者密码（如果设置）用于控制打印、编辑、提取、注释等权限。Acrobat Reader 会根据权限设置禁用这些功能。若要设置或更改权限，Acrobat 需要此密码。

![todo:image_alt_text](creating-a-secure-pdf_1.png)

### **合并文档**

使用 **Convert to PDF** 选项合并两个文档。此功能可将多个非 PDF 文件（HTML、文本或图像）合并为一个 PDF 文件。

1. 打开文档库并从列表中选择所需的文档。

![todo:image_alt_text](creating-a-secure-pdf_2.png)


1. 使用库工具中的 **Merge to PDF** 选项保存输出文件。系统会提示将输出文件保存到磁盘。

![todo:image_alt_text](creating-a-secure-pdf_3.png)

### **输出**

输出文件已加密。

![todo:image_alt_text](creating-a-secure-pdf_4.png)

