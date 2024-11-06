---
title: 安装 Aspose.PDF for Java
linktitle: 安装
type: docs
weight: 20
url: zh/java/installation/
description: 本节展示了产品描述和安装 Aspose.PDF for Java 的说明，包括自行安装和使用 NuGet。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Aspose.PDF for Java 组件

{{% alert color="primary" %}}

**Aspose.PDF 是一个 Java** 组件，旨在允许开发人员以编程方式动态创建 PDF 文档，无论是简单还是复杂的。Aspose.PDF for Java 允许开发人员将表格、图形、图像、超链接、自定义字体等插入 PDF 文档中。此外，也可以压缩 PDF 文档。Aspose.PDF for Java 提供出色的安全功能，以开发安全的 PDF 文档。Aspose.PDF for Java 最显著的特点是支持通过 API 和 XML 模板创建 PDF 文档。

{{% /alert %}}

## 产品描述

**Aspose.PDF for Java** 是使用 Java 实现的，它适用于 JDK 1.8 及以上版本。Aspose.PDF for Java 可以与任何应用程序集成，例如 JSP/JSF 网络应用程序或 Windows 应用程序。

**Aspose.PDF for Java** 速度快且重量轻。它能够高效地创建 PDF 文档，并帮助您的应用程序更好地运行。由于其价格、卓越的性能和出色的支持，Aspose.PDF for Java 是我们客户在创建 PDF 文档时的首选。
使用该库，您可以实现从头创建 PDF 文件的丰富功能，或者在不安装 Adobe Acrobat 的情况下完全处理现有的 PDF 文档。

# 安装

## 评估 Aspose.PDF for Java

{{% alert color="primary" %}}

您可以下载 [Aspose.PDF for Java](https://releases.aspose.com/java/repo/com/aspose/aspose-pdf/) 进行评估。
 评估下载与购买下载相同。当您添加几行代码以[应用许可证](/pdf/java/licensing/)时，评估版本就会被授权。

{{% /alert %}}

Aspose.PDF的评估版本提供完整的产品功能，但有两个限制：

- 它插入一个评估水印。
- 任何集合的元素不超过四个可以查看/编辑。
- **显示评估水印的文档**

![Aspose.PDF的评估](evaluate-aspose-pdf_1.png)

{{% alert color="primary" %}}

如果您希望在没有评估版本限制的情况下测试Java版的Aspose.PDF，您也可以申请30天的临时许可证。请参考[如何获取临时许可证？](https://purchase.aspose.com/temporary-license)

{{% /alert %}}

## 从Aspose仓库安装Java版的Aspose.PDF

Aspose在[Aspose仓库](https://releases.aspose.com/java/repo/com/aspose/aspose-pdf/)上托管所有Java API。 你可以在你的 Maven 项目中通过简单的配置直接使用 Aspose.PDF for Java API。

### 指定 Aspose 仓库配置

首先，你需要在 Maven pom.xml 中指定 Aspose 仓库的配置/位置，如下所示：

```xml
 <repositories>
    <repository>
        <id>AsposeJavaAPI</id>
        <name>Aspose Java API</name>
        <url>https://releases.aspose.com/java/repo/</url>
    </repository>
</repositories>
```

### 定义 Aspose.PDF for Java API 依赖

然后，在你的 pom.xml 中定义 Aspose.PDF for Java API 依赖，如下所示：

```xml
 <dependencies>
    <dependency>
        <groupId>com.aspose</groupId>
        <artifactId>aspose-pdf</artifactId>
        <version>21.7</version>
    </dependency>
</dependencies>
```

完成上述步骤后，Aspose.PDF for Java 依赖将最终在你的 Maven 项目中定义。

### JDK 11 兼容性和使用指南

该 API 针对 Java 11 环境进行了优化，所有测试和功能都能很好地运行。 然而，对于某些类，你应该添加外部依赖来添加类的类路径：javax.xml.bind.annotation.adapters.HexBinaryAdapter，该类已从JRE中删除。

例如：

```xml
 <dependency>
    <groupId>javax.xml.bind</groupId>
    <artifactId>jaxb-api</artifactId>
    <version>2.3.0</version>
</dependency>
```