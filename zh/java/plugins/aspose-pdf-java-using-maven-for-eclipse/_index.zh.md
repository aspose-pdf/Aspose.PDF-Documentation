---
title: Aspose.PDF Java 使用 Maven for Eclipse
type: docs
weight: 80
url: /java/aspose-pdf-java-using-maven-for-eclipse/
lastmod: "2021-06-05"
---

## 介绍

### Eclipse IDE

Eclipse IDE 是一个著名的 Java 集成开发环境 (IDE)。该 IDE 无疑是 Eclipse 开源项目最知名的产品。今天，它是 Java 的领先开发环境，市场份额约为 60%。

Eclipse IDE 可以通过额外的软件组件进行扩展。Eclipse 称这些软件组件为插件。多个开源项目和公司已经扩展了 Eclipse IDE 或在 Eclipse 框架之上创建了独立应用程序 (Eclipse RCP)。

### Aspose.PDF for Java

[Aspose.PDF for Java](https://products.aspose.com/pdf/java/) 是一个强大的 PDF 文档创建 API，使您的 Java 应用程序能够在不使用 Adobe Acrobat 的情况下读取、写入和操作 PDF 文档。

Aspose.PDF for Java 提供了丰富的功能，这些功能包括 PDF 压缩选项、表格创建和操作、图形支持、图像功能、广泛的超链接功能、扩展的安全控制和自定义字体处理。

### Aspose.PDF Java (Maven) for Eclipse

- Aspose.PDF Java (Maven) for Eclipse 是由 **Aspose.** 为 **Eclipse IDE** 提供的插件。此插件适用于使用 Maven 平台进行 Java 开发的开发人员，并希望在其项目中使用 Aspose.PDF for Java。该插件允许您创建使用 Aspose.PDF for Java API 的 maven 项目，并下载 API 的[代码示例](https://github.com/aspose-pdf/Aspose.Pdf-for-Java)。
- 该插件提供以下功能，以便在 **Eclipse IDE** 中舒适地使用 Aspose.PDF for Java API：

![todo:image_alt_text](https://i.imgur.com/KWKGljg.png)

**向导**：
该插件包含两个向导

**Aspose.PDF Maven 项目（向导）**

- 这个新项目向导允许开发人员从新建 -> 项目 -> Maven -> Aspose.PDF Maven 项目创建一个 **Maven** 项目，以使用 Aspose.PDF for Java。

- Aspose.PDF for Java API maven 依赖项的引用会自动从 [Aspose Cloud Maven Repository](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo) 获取，并添加到 pom.xml 中。
- 创建的项目将始终包含最新可用版本的 **Maven** 依赖项，用于 Aspose.PDF for Java API。
- 向导步骤还提供下载 [代码示例](https://github.com/aspose-pdf/Aspose.Pdf-for-Java) 的选项，以使用 Aspose.PDF for Java API。  
Aspose.PDF 代码示例（向导）

- 此新文件向导允许您将下载的 [代码示例](https://github.com/aspose-pdf/Aspose.Pdf-for-Java) 复制到您的项目中，以便通过新建 -> 其他 -> Java -> Aspose.PDF 代码示例来使用 Aspose.PDF for Java。
- 可用的示例以树格式显示，用户可以从中按类别选择。
- 选定类别中的所有示例将被复制到项目的 "**com.aspose.pdf.examples**" 包文件夹中，并将所需的资源复制到 "**src/main/resources**" 文件夹中，以运行这些示例。
- Aspose.PDF for Java API 的代码示例用于演示 API 的各种功能。

- 向导还将查找并更新来自 Aspose.PDF for Java 示例库的新可用代码示例。

## 系统要求和支持平台

### 系统要求

- **系统内存：** 2 GB 或更多（推荐）
- **操作系统：** 任何支持 Java 虚拟机（VM）的操作系统
- **互联网连接：** 2 MB 或更快（推荐）

### 支持平台

- Eclipse Mars.1 (4.5.1) - 推荐
- Eclipse Juno 或更高版本。

## 下载

### 下载 Eclipse IDE

在下载 Aspose.PDF Java (Maven) for Eclipse 插件之前，您需要先安装 Eclipse IDE。

要下载 Eclipse IDE

1. 访问 [https://eclipse.org](https://eclipse.org/)。
2. 下载并安装推荐的 Eclipse IDE for Java SE / EE 开发人员。

### 下载 Aspose.PDF Java (Maven) for Eclipse

以下是成功下载和安装 Aspose.PDF Java (Maven) for Eclipse 插件的三种推荐方法：

- 从 [Eclipse Marketplace](https://marketplace.eclipse.org/content/asposepdf-java-maven-eclipse) 拖放安装到您的 Eclipse 工作区。

- 或者转到 **Help** > **Install New Software...** > 在 **Work with** 中输入以下更新站点 URL
然后选择 "Aspose.PDF Java (Maven) for Eclipse" 并点击 **完成**。接受许可协议并安装插件。

## 安装

安装 Aspose.PDF Java (Maven) for Eclipse

## 使用插件

使用 Aspose.PDF Java (Maven) for Eclipse

### 如何应用 Aspose 许可证？

此插件使用 Aspose.PDF 的评估版本。一旦你对评估满意，你可以在 [Aspose 网站](https://purchase.aspose.com/buy) 购买许可证。
为了去除评估信息和功能限制，应该应用产品许可证。购买产品后，你将收到一个许可证文件。请按照以下步骤应用许可证：

- 确保许可证文件命名为 Aspose.PDF.Java.lic
- 将 **Aspose.PDF.Java.lic** 文件放置在包含 Aspose.PDF.jar 的文件夹中
- 使用以下代码激活许可证：

{{< highlight java >}}

 License license = new License();

license.setLicense("Aspose.PDF.Java.lic");

{{< /highlight >}}

## 支持、扩展与贡献

### 支持

- 如果您希望查看插件中已知/报告的问题（由用户或质量保证团队）。
- 或者您想报告在插件中发现的任何问题
- 有任何改进建议或想要提出任何功能请求

请关注 [**GitHub 问题跟踪器**](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues) 来记录在插件中发现的任何问题。

### 扩展和贡献

Aspose.PDF Java (Maven) for Eclipse 是开源的，其源代码在以下列出的主要社交编程网站上可用。我们鼓励开发人员下载源代码，并通过建议或添加新功能或改进现有功能来贡献，以便其他人也能从中受益。开发人员也可以从中学习制作自己的插件。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_Maven_for_Eclipse)

### 如何配置 Aspose.PDF Java (Maven) for Eclipse 的源代码

以下简单步骤将顺利引导您在 Eclipse IDE 中成功配置 **"Aspose.PDF Java (Maven) for Eclipse"** 插件源代码

1. 下载/克隆源代码。
1. 选择 **文件** > 导入 > 常规 > 导入到工作区的现有项目
1. 浏览到您下载的最新项目源代码
1. 选择您要导入的 Eclipse 项目
1. 点击完成
1. Aspose.PDF Java for Eclipse 插件代码现已准备好进行增强。