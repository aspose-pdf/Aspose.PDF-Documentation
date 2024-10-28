---
title: Aspose.PDF Java for Ruby
type: docs
weight: 20
url: /java/aspose-pdf-java-for-ruby/
lastmod: "2021-06-05"
---

## 介绍

### Rjb - Ruby Java 桥接

RJB 是一个桥接程序，通过 Java 本机接口连接 Ruby 和 Java。Rake + Rjb 是比 Maven 和 Ant 更强大和有用的构建工具。您可以使用 Rjb 的模拟来测试您的 Java 业务逻辑类本身。它有助于将 Struts 的模型对象迁移到您的 RoR 应用程序中。但请注意构建 Swing 应用程序时，Ruby（和 Rjb）不考虑 JVM 的本机线程处理。

### Aspose.PDF for Java

Aspose.PDF for Java 是一个 PDF 文档创建组件，使您的 Java 应用程序能够在不使用 Adobe Acrobat 的情况下读取、写入和操作 PDF 文档。

Aspose.PDF for Java 是一个价格合理的组件，提供了惊人的丰富功能，包括：PDF 压缩选项、表格创建和操作、图形支持、图像功能、广泛的超链接功能、扩展的安全控制和自定义字体处理。

Aspose.PDF for Java 允许您通过提供的 API 和 XML 模板直接创建 PDF 文件。使用 Aspose.PDF for Java 还可以让您在短时间内为应用程序添加 PDF 功能。

### Aspose.PDF Java for Ruby

项目 Aspose.PDF Java for Ruby 展示了如何在 Ruby 中使用 Aspose.PDF Java API 执行不同的任务。该项目旨在为希望在其 Ruby 项目中使用 Rjb（Ruby Java Bridge）利用 Aspose.PDF for Java 的 Ruby 开发人员提供有用的示例。

## 系统要求和支持的平台

### 系统要求

以下是使用 Aspose.PDF Java for Ruby 的系统要求：

- 配置了 Rjb Gem
- 下载了 Aspose.PDF 组件

### 支持的平台

以下是支持的平台：

- Ruby 2.2.x 或以上版本及相应的 DevKit。
- Java 1.5 或以上版本

## 下载

### 下载所需的库

下载下面提到的所需库。这些是执行 Aspose.PDF Java for Ruby 示例所需的。

- [Aspose.PDF for Java 组件](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf)

### 从社交编码网站下载示例

以下版本的运行示例可在下面提到的社交编码网站下载：

GitHub

- [Aspose.PDF Java for Ruby](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_Ruby)

## 安装和使用

### 安装

安装 Aspose.PDF Java for Ruby gem 非常简单，请遵循以下简单步骤：

1. 运行以下命令。

{{< highlight java >}}

 $ gem install aspose-pdfjava

{{< /highlight >}}

1. 从以下链接下载所需的 Aspose.PDF for Java 组件。
   <https://downloads.aspose.com/pdf/java>
1. 在 Aspose.PDF Java for Ruby gem 的根目录创建 "jars" 文件夹，并将下载的组件复制到其中。

### 使用

包含用于 helloworld 示例的必需文件。

{{< highlight java >}}

 require File.dirname(File.dirname(File.dirname(__FILE__))) + '/lib/aspose-pdfjava'

include Asposepdfjava

include Asposepdfjava::HelloWorld


initialize_aspose_pdf

{{< /highlight >}}

让我们理解上面的代码。

1. 第一行确保 aspose pdf 已加载并可用。
1. 包含访问 aspose pdf 所需的文件。
1. 初始化库。aspose JAVA 类从 aspose.yml 文件中提供的路径加载。

## 支持、扩展和贡献

### 支持

从 Aspose 成立的第一天起，我们就知道仅仅给客户提供好的产品是不够的。我们还需要提供良好的服务。我们自己也是开发者，理解当技术问题或软件中的一个小问题阻碍你完成所需工作时的挫败感。我们在这里是为了解决问题，而不是制造问题。

这就是为什么我们提供免费支持。任何使用我们产品的人，无论他们是购买了还是在使用评估版本，都应该得到我们的全力关注和尊重。

您可以使用以下任一平台记录与 Aspose.PDF Java for Ruby 相关的问题或建议：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)

### 扩展和贡献

Aspose.PDF Java for Ruby 是开源的，其源代码可在以下列出的主要社交编码网站上获取。我们鼓励开发者下载源代码，并通过建议或添加新功能或改进现有功能来贡献，以便其他人也能从中受益。

### 源代码

您可以从以下位置之一获取最新的源代码：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_Ruby)

## 示例代码示例

本节包括以下主题：

- [下载和配置 Ruby 中的 Aspose.Pdf](/pdf/java/download-and-configure-aspose-pdf-in-ruby/)
- [Ruby 程序员指南](/pdf/java/ruby-programmers-guide/)
  - [在 Ruby 中处理文档对象](/pdf/java/working-with-document-object-in-ruby/)
    - [在 Ruby 中添加 JavaScript](/pdf/java/adding-javascript-in-ruby/)
    - [在 Ruby 中向 PDF 文件添加图层](/pdf/java/add-layers-to-pdf-file-in-ruby/)

    - [在 Ruby 中为现有 PDF 添加目录](/pdf/java/add-toc-to-existing-pdf-in-ruby/)
- [获取文档窗口和页面显示属性（Ruby）](/pdf/java/get-document-window-and-page-display-properties-in-ruby/)
- [获取 PDF 文件信息（Ruby）](/pdf/java/get-pdf-file-information-in-ruby/)
- [从 PDF 文件获取 XMP 元数据（Ruby）](/pdf/java/get-xmp-metadata-from-pdf-file-in-ruby/)
- [优化 PDF 文档以用于网络（Ruby）](/pdf/java/optimize-pdf-document-for-the-web-in-ruby/)
- [优化 PDF 文件大小（Ruby）](/pdf/java/optimize-pdf-file-size-in-ruby/)
- [从 PDF 中移除元数据（Ruby）](/pdf/java/remove-metadata-from-pdf-in-ruby/)
- [设置文档窗口和页面显示属性（Ruby）](/pdf/java/set-document-window-and-page-display-properties-in-ruby/)
- [设置 PDF 过期时间（Ruby）](/pdf/java/set-pdf-expiration-in-ruby/)
- [设置 PDF 文件信息（Ruby）](/pdf/java/set-pdf-file-information-in-ruby/)
- [在 Ruby 中处理页面](/pdf/java/working-with-pages-in-ruby/)

  - [合并 PDF 文件（Ruby）](/pdf/java/concatenate-pdf-files-in-ruby/)
- [从 PDF 文件中删除特定页面在 Ruby 中](/pdf/java/delete-a-particular-page-from-the-pdf-file-in-ruby/)
- [在 Ruby 中获取 PDF 文件中的特定页面](/pdf/java/get-a-particular-page-in-a-pdf-file-in-ruby/)
- [在 Ruby 中获取 PDF 页数](/pdf/java/get-page-count-of-pdf-in-ruby/)
- [在 Ruby 中获取页面属性](/pdf/java/get-page-properties-in-ruby/)
- [在 Ruby 中在 PDF 文件末尾插入一个空白页面](/pdf/java/insert-an-empty-page-at-end-of-pdf-file-in-ruby/)
- [在 Ruby 中将空白页面插入 PDF 文件](/pdf/java/insert-an-empty-page-into-a-pdf-file-in-ruby/)
- [在 Ruby 中将 PDF 文件拆分为单独的页面](/pdf/java/split-pdf-file-into-individual-pages-in-ruby/)
- [在 Ruby 中更新页面尺寸](/pdf/java/update-page-dimensions-in-ruby/)
- [在 Ruby 中处理文本](/pdf/java/working-with-text-in-ruby/)
- [在 Ruby 中使用 DOM 添加 HTML 字符串](/pdf/java/add-html-string-using-dom-in-ruby/)
- [在 Ruby 中向现有 PDF 文件添加文本](/pdf/java/add-text-to-an-existing-pdf-file-in-ruby/)
- [从 PDF 文档的所有页面提取文本在 Ruby 中](/pdf/java/extract-text-from-all-the-pages-of-a-pdf-document-in-ruby/)
  - [在 Ruby 中处理文档转换](/pdf/java/working-with-document-conversion-in-ruby/)
    - [在 Ruby 中将 HTML 转换为 PDF 格式](/pdf/java/convert-html-to-pdf-format-in-ruby/)
    - [在 Ruby 中将 PDF 页面转换为图像](/pdf/java/convert-pdf-pages-to-images-in-ruby/)
    - [在 Ruby 中将 PDF 转换为 DOC 或 DOCX 格式](/pdf/java/convert-pdf-to-doc-or-docx-format-in-ruby/)
    - [在 Ruby 中将 PDF 转换为 Excel 工作簿](/pdf/java/convert-pdf-to-excel-workbook-in-ruby/)
    - [在 Ruby 中将 PDF 转换为 SVG 格式](/pdf/java/convert-pdf-to-svg-format-in-ruby/)
    - [在 Ruby 中将 SVG 文件转换为 PDF 格式](/pdf/java/convert-svg-file-to-pdf-format-in-ruby/)
- [支持、扩展和贡献 Aspose.Pdf 在 Ruby 中](/pdf/java/support-extend-and-contribute-to-aspose-pdf-in-ruby/)