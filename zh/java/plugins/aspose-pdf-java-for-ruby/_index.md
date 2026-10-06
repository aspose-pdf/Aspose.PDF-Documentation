---
title: 适用于 Ruby 的 Aspose.PDF Java
linktitle: 适用于 Ruby 的 Aspose.PDF Java
type: docs
weight: 20
url: /zh/java/aspose-pdf-java-for-ruby/
description: 探索如何在 Ruby 中使用 Aspose.PDF for Java。将 Ruby 脚本的强大功能与高级 PDF 操作特性相结合。
lastmod: "2026-10-06"
---
## 介绍

### Rjb - Ruby Java 桥接

RJB 是一个桥接程序，使用 Java 本地接口在 Ruby 和 Java 之间进行连接。Rake + Rjb 是比 Maven 和 Ant 更强大且更实用的构建工具。您可以使用 Rjb 的 mock 直接测试 Java 业务逻辑类本身。它有助于将 Struts 的 Model Object 迁移到您的 RoR 应用程序中。但在构建 buildSwing 应用程序时要小心，Ruby（以及 Rjb）并不考虑 JVM 的本机线程处理。

### Aspose.PDF for Java

Aspose.PDF for Java 是一个 PDF 文档创建组件，使您的 Java 应用程序能够在不使用 Adobe Acrobat 的情况下读取、写入和操作 PDF 文档。

Aspose.PDF for Java 是一个价格实惠的组件，提供了令人难以置信的丰富功能，包括：PDF 压缩选项、表格创建和操作、图形支持、图像功能、广泛的超链接功能、扩展的安全控制以及自定义字体处理。

Aspose.PDF for Java 允许您通过提供的 API 和 XML 模板直接创建 PDF 文件。使用 Aspose.PDF for Java 还可以让您在短时间内为您的应用程序添加 PDF 功能。

### Aspose.PDF Java for Ruby

Project Aspose.PDF Java for Ruby 展示了如何使用 Aspose.PDF Java APIs 在 Ruby 中执行不同的任务。该项目旨在为希望在 Ruby 项目中使用 Rjb（Ruby Java Bridge）利用 Aspose.PDF for Java 的 Ruby 开发者提供有用的示例。

## 系统要求和受支持的平台

### 系统要求

以下是使用 Aspose.PDF Java for Ruby 的系统要求：

- 已配置 Rjb Gem
- 已下载 Aspose.PDF 组件

### 支持的平台

以下是受支持的平台：

- Ruby 2.2.x 或更高版本以及相应的 DevKit。
- Java 1.5或更高
В

## 下载

### 下载所需的库

下载下面提到的必需库。这些是运行 Aspose.PDF for Java for Ruby 示例所必需的。

- [Aspose.PDF for Java 组件](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf)

### 从社交编码站点下载示例

以下运行示例的发行版可在下面提到的社交编码站点下载：

GitHub

- [Aspose.PDF Java for Ruby](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_Ruby)

## 安装和使用

### 安装

安装 Aspose.PDF Java for Ruby gem 非常简单易行，请按照以下简单步骤操作：

1. 运行以下命令。

{{< highlight java >}}

 $ gem install aspose-pdfjava

{{< /highlight >}}

1. 下载所需的 Aspose.PDF for Java 组件，请访问以下链接。
   <https://downloads.aspose.com/pdf/java>
1. 在 Aspose.PDF Java for Ruby gem 的根目录创建 \u0022jars\u0022 文件夹，并将下载的组件复制到该文件夹中。

### 使用

包含用于运行 helloworld 示例所需的文件。

{{< highlight java >}}

 require File.dirname(File.dirname(File.dirname(__FILE__))) + '/lib/aspose-pdfjava'

include Asposepdfjava

include Asposepdfjava::HelloWorld

initialize_aspose_pdf

{{< /highlight >}}

让我们了解上述代码。

1. 第一行确保已加载并可用 Aspose.PDF。
1. 包含访问 Aspose.PDF 所需的文件。
1. 初始化库。Aspose JAVA 类从 aspose.yml 文件中提供的路径加载/

## 支持、扩展和贡献

### 支持

从 Aspose 创立伊始，我们就知道仅仅为客户提供优质产品是不够的。我们还需要提供出色的服务。我们自己也是开发者，深知当技术问题或软件的怪癖阻止你完成所需工作时是多么令人沮丧。我们在这里是为了解决问题，而不是制造问题。

这就是我们提供免费支持的原因。任何使用我们产品的人，无论是已购买还是正在试用，都值得我们全力关注和尊重。

您可以使用以下任意平台记录与 Aspose.PDF Java for Ruby 相关的任何问题或建议：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)

### 扩展并贡献

Aspose.PDF Java for Ruby 是开源的，其源代码可在下列主要社交编程网站上获得。鼓励开发者下载源代码并通过提出建议、添加新功能或改进现有功能来贡献代码，从而使其他人也能受益。

### 源代码

您可以从以下位置之一获取最新的源代码：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_Ruby)

## 示例代码示例

本节包括以下主题：

- [在 Ruby 中下载并配置 Aspose.Pdf](/pdf/zh/java/download-and-configure-aspose-pdf-in-ruby/)
- [Ruby 程序员指南](/pdf/zh/java/ruby-programmers-guide/)
  - [在 Ruby 中使用文档对象](/pdf/zh/java/working-with-document-object-in-ruby/)
    - [在 Ruby 中添加 JavaScript](/pdf/zh/java/adding-javascript-in-ruby/)
    - [在 Ruby 中向 PDF 文件添加图层](/pdf/zh/java/add-layers-to-pdf-file-in-ruby/)
    - [在 Ruby 中向现有 PDF 添加目录](/pdf/zh/java/add-toc-to-existing-pdf-in-ruby/)
    - [在 Ruby 中获取文档窗口和页面显示属性](/pdf/zh/java/get-document-window-and-page-display-properties-in-ruby/)
    - [在 Ruby 中获取 PDF 文件信息](/pdf/zh/java/get-pdf-file-information-in-ruby/)
    - [在 Ruby 中获取 PDF 文件的 XMP 元数据](/pdf/zh/java/get-xmp-metadata-from-pdf-file-in-ruby/)
    - [在 Ruby 中优化适用于 Web 的 PDF 文档](/pdf/zh/java/optimize-pdf-document-for-the-web-in-ruby/)
    - [在 Ruby 中优化 PDF 文件大小](/pdf/zh/java/optimize-pdf-file-size-in-ruby/)
    - [在 Ruby 中移除 PDF 元数据](/pdf/zh/java/remove-metadata-from-pdf-in-ruby/)
    - [在 Ruby 中设置文档窗口和页面显示属性](/pdf/zh/java/set-document-window-and-page-display-properties-in-ruby/)
    - [在 Ruby 中设置 PDF 过期](/pdf/zh/java/set-pdf-expiration-in-ruby/)
    - [在 Ruby 中设置 PDF 文件信息](/pdf/zh/java/set-pdf-file-information-in-ruby/)
  - [在 Ruby 中处理页面](/pdf/zh/java/working-with-pages-in-ruby/)
    - [在 Ruby 中合并 PDF 文件](/pdf/zh/java/concatenate-pdf-files-in-ruby/)
    - [在 Ruby 中删除 PDF 文件的特定页面](/pdf/zh/java/delete-a-particular-page-from-the-pdf-file-in-ruby/)
    - [在 Ruby 中获取 PDF 文件的特定页面](/pdf/zh/java/get-a-particular-page-in-a-pdf-file-in-ruby/)
    - [在 Ruby 中获取 PDF 页数](/pdf/zh/java/get-page-count-of-pdf-in-ruby/)
    - [在 Ruby 中获取页面属性](/pdf/zh/java/get-page-properties-in-ruby/)
    - [在 Ruby 中在 PDF 文件末尾插入空白页](/pdf/zh/java/insert-an-empty-page-at-end-of-pdf-file-in-ruby/)
    - [在 Ruby 中向 PDF 文件插入空白页](/pdf/zh/java/insert-an-empty-page-into-a-pdf-file-in-ruby/)
    - [在 Ruby 中将 PDF 文件拆分为单独的页面](/pdf/zh/java/split-pdf-file-into-individual-pages-in-ruby/)
    - [在 Ruby 中更新页面尺寸](/pdf/zh/java/update-page-dimensions-in-ruby/)
  - [在 Ruby 中处理文本](/pdf/zh/java/working-with-text-in-ruby/)
    - [在 Ruby 中使用 DOM 添加 HTML 字符串](/pdf/zh/java/add-html-string-using-dom-in-ruby/)
    - [在 Ruby 中向现有 PDF 文件添加文字](/pdf/zh/java/add-text-to-an-existing-pdf-file-in-ruby/)
    - [在 Ruby 中提取 PDF 文档所有页面的文本](/pdf/zh/java/extract-text-from-all-the-pages-of-a-pdf-document-in-ruby/)
  - [在 Ruby 中进行文档转换](/pdf/zh/java/working-with-document-conversion-in-ruby/)
    - [在 Ruby 中将 HTML 转换为 PDF 格式](/pdf/zh/java/convert-html-to-pdf-format-in-ruby/)
    - [在 Ruby 中将 PDF 页面转换为图像](/pdf/zh/java/convert-pdf-pages-to-images-in-ruby/)
    - [在 Ruby 中将 PDF 转换为 DOC 或 DOCX 格式](/pdf/zh/java/convert-pdf-to-doc-or-docx-format-in-ruby/)
    - [在 Ruby 中将 PDF 转换为 Excel 工作簿](/pdf/zh/java/convert-pdf-to-excel-workbook-in-ruby/)
    - [在 Ruby 中将 PDF 转换为 SVG 格式](/pdf/zh/java/convert-pdf-to-svg-format-in-ruby/)
    - [在 Ruby 中将 SVG 文件转换为 PDF 格式](/pdf/zh/java/convert-svg-file-to-pdf-format-in-ruby/)
- [在 Ruby 中支持、扩展并为 Aspose.Pdf 做出贡献](/pdf/zh/java/support-extend-and-contribute-to-aspose-pdf-in-ruby/)
