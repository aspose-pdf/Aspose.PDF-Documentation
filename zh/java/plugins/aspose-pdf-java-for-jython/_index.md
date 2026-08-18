---
title: 用于 Jython 的 Aspose.PDF Java
linktitle: 用于 Jython 的 Aspose.PDF Java
type: docs
weight: 60
url: /java/aspose-pdf-java-for-jython/
description: 将 Aspose.PDF for Java 的强大功能与 Jython 相结合。在基于 Python 的 Java 环境中轻松操作 PDF 文件。
lastmod: "2026-06-09"
---
## 介绍

### 什么是 Jython？

Jython 是 Python 的 Java 实现，它将表达能力与清晰度结合在一起。 Jython 可免费用于商业和非商业用途，并与源代码一起分发。 Jython 是 Java 的补充，特别适合以下任务：

- **嵌入式脚本** - Java 程序员可以将 Jython 库添加到他们的系统中，以允许最终用户编写简单或复杂的脚本，为应用程序添加功能。
- **交互式实验** - Jython 提供了一个交互式解释器，可用于与 Java 包或正在运行的 Java 应用程序进行交互。这允许程序员使用 Jython 实验和调试任何 Java 系统。
- **快速应用程序开发** - Python 程序通常比同等 Java 程序短 2-10 倍。这直接转化为程序员生产力的提高。 Python 和 Java 之间的无缝交互允许开发人员在开发和交付产品期间自由混合这两种语言。

### Aspose.PDF for Java

Aspose.PDF for Java 是一个 PDF 文档创建组件，使您的 Java 应用程序能够在不使用 Adob​​e Acrobat 的情况下读取、写入和操作 PDF 文档。

Aspose.PDF for Java 是一个价格实惠的组件，提供了令人难以置信的丰富功能，其中包括：PDF 压缩选项、表格创建和操作、图形支持、图像功能、广泛的超链接功能、扩展的安全控制和自定义字体处理。

Aspose.PDF for Java 允许您直接通过提供的 API 和 XML 模板创建 PDF 文件。使用 Aspose.PDF for Java 还可以让您立即将 PDF 功能添加到您的应用程序中。

### 用于 Jython 的 Aspose.PDF Java

Aspose.PDF Java for Jython 是一个演示/提供 Aspose.PDF for Java API 在 Jython 中使用示例的项目。

## 系统要求和支持的平台

### 系统要求

以下是使用 Aspose.PDF Java for Jython 的系统要求：

- 安装了Java 1.5或以上版本
- 下载的Aspose.PDF组件
- Jython 2.7.0

### 支持的平台

以下是支持的平台：

- Aspose.PDF 15.4 及更高版本。
- Java IDE（Eclipse、NetBeans ...）

## 下载安装及使用

### 正在下载

可以从 GitHub 下载以下版本的运行示例：

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose-Pdf-Java-for-Jython)

下载 Aspose.PDF for Java 组件：

- [Aspose.PDF for Java](https://downloads.aspose.com/pdf/java)

### 安装中

- 将下载的 Aspose.PDF for Java jar 文件放入“lib”目录中。
- 将“your-lib”替换为 _*init*_.py 文件中下载的 jar 文件名。

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

从 Aspose 成立的第一天起，我们就知道仅仅为客户提供好的产品是不够的。我们还需要提供良好的服务。我们本身就是开发人员，了解当技术问题或软件中的怪癖阻止您做您需要做的事情时是多么令人沮丧。我们来这里是为了解决问题，而不是制造问题。

这就是我们提供免费支持的原因。任何使用我们产品的人，无论是购买过的还是正在使用评价的，都值得我们充分的关注和尊重。

您可以使用以下任一平台记录与 Aspose.PDF Java for Jython 相关的任何问题或建议：

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)

### 扩展和贡献

Aspose.PDF Java for Jython 是开源的，其源代码可在下面列出的主要社交编码网站上找到。我们鼓励开发人员下载源代码并通过建议或添加新功能或改进现有功能来做出贡献，以便其他人也可以从中受益。

### 源代码

您可以从以下位置之一获取最新的源代码

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java)
