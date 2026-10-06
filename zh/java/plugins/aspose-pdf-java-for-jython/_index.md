---
title: 适用于 Jython 的 Aspose.PDF Java
linktitle: 适用于 Jython 的 Aspose.PDF Java
type: docs
weight: 60
url: /zh/java/aspose-pdf-java-for-jython/
description: 将 Aspose.PDF for Java 的强大功能与 Jython 相结合。在基于 Python 的 Java 环境中轻松操作 PDF 文件。
lastmod: "2026-10-06"
---
## 介绍

### 什么是 Jython？

Jython 是 Python 的 Java 实现，兼具表现力和清晰度。Jython 可免费用于商业和非商业用途，并提供源代码。Jython 与 Java 互补，尤其适用于以下任务：

- **Embedded scripting** - Java 程序员可以将 Jython 库添加到他们的系统中，以允许最终用户编写简单或复杂的脚本，为应用程序添加功能。
- **Interactive experimentation** - Jython 提供了一个交互式解释器，可用于与 Java 包或正在运行的 Java 应用程序交互。这使得程序员能够使用 Jython 对任何 Java 系统进行实验和调试。
- **Rapid application development** - Python 程序通常比等效的 Java 程序短 2-10 倍。这直接转化为程序员生产力的提升。Python 与 Java 之间的无缝交互使开发者能够在开发阶段以及产品交付时自由混合这两种语言。

### Aspose.PDF for Java

Aspose.PDF for Java 是一个 PDF 文档创建组件，使您的 Java 应用程序能够在不使用 Adobe Acrobat 的情况下读取、写入和操作 PDF 文档。

Aspose.PDF for Java 是一款价格实惠的组件，提供了极其丰富的功能，包括：PDF 压缩选项、表格创建与操作、图形支持、图像功能、广泛的超链接功能、扩展的安全控制以及自定义字体处理。

Aspose.PDF for Java 允许您通过提供的 API 和 XML 模板直接创建 PDF 文件。使用 Aspose.PDF for Java 还能让您快速为应用程序添加 PDF 功能。

### Aspose.PDF Java for Jython

Aspose.PDF Java for Jython 是一个演示/提供 Aspose.PDF for Java API 在 Jython 中使用示例的项目。

## 系统要求和受支持的平台

### 系统要求

以下是使用 Aspose.PDF Java for Jython 的系统要求：

- 已安装 Java 1.5 或更高版本
- 已下载 Aspose.PDF 组件
- Jython 2.7.0

### 受支持的平台

以下是受支持的平台：

- Aspose.PDF 15.4 及以上。
- Java IDE（Eclipse，NetBeans ...）

## 下载、安装和使用

### 下载

以下运行示例的发布版本可从 GitHub 下载：

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose-Pdf-Java-for-Jython)

下载 Aspose.PDF for Java 组件：

- [Aspose.PDF for Java](https://downloads.aspose.com/pdf/java)

### 安装

- 将下载的 Aspose.PDF for Java jar 文件放入 "lib" 目录。
- 将 "your-lib" 替换为下载的 jar 文件名，在 _*init*_.py 文件中。

### 使用

您可以使用以下示例代码将 Pdf 转换为 doc 文档：

```java
from aspose-pdf import Settings
from com.aspose.pdf import Document

class PdfToDoc:

    def __init__(self):
        dataDir = Settings.dataDir + 'WorkingWithDocumentConversion/PdfToDoc/'

        # Open the target document
        pdf = Document(dataDir + 'input1.pdf')

        # Save the concatenated output file (the target document)
        pdf.save(dataDir + "output.doc")

        print "Document has been converted successfully"

if __name__ == '__main__':

    PdfToDoc()
```

## 支持、扩展和贡献

### 支持

从 Aspose 成立伊始，我们就知道仅仅提供给客户优秀的产品是不够的。我们还必须提供优质的服务。我们自己也是开发者，深知当技术问题或软件的怪癖阻止你完成所需工作时的沮丧感。我们在此是为了解决问题，而不是制造问题。

这就是我们提供免费支持的原因。无论是已购买产品还是正在试用的用户，所有使用我们产品的人都值得我们全力关注和尊重。

您可以使用以下任意平台记录与\u0412\u00A0Aspose.PDF Java for Jython 相关的任何问题或建议：

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)

### 扩展与贡献

Aspose.PDF Java for Jython 是开源的，其源代码可在以下列出的主要社交编码网站上获取。鼓励开发者下载源代码并通过提出建议、添加新功能或改进现有功能来贡献代码，使其他人也能受益。

### 源代码

您可以从以下位置之一获取最新的源代码

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java)
