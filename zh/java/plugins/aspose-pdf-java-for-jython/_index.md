---
title: Aspose.PDF Java for Jython
type: docs
weight: 60
url: zh/java/aspose-pdf-java-for-jython/
lastmod: "2021-06-05"
---

## 介绍

### 什么是 Jython？

Jython 是 Python 的 Java 实现，结合了表达能力和清晰性。Jython 可以免费用于商业和非商业用途，并附带源代码分发。Jython 是 Java 的补充，特别适合以下任务：

- **嵌入式脚本** - Java 程序员可以将 Jython 库添加到他们的系统中，以允许最终用户编写简单或复杂的脚本，从而为应用程序增加功能。
- **交互式实验** - Jython 提供了一个交互式解释器，可以用来与 Java 包或正在运行的 Java 应用程序进行交互。这使程序员可以使用 Jython 来实验和调试任何 Java 系统。
- **快速应用程序开发** - Python 程序通常比等效的 Java 程序短 2-10 倍。
 这直接转化为程序员生产力的提高。Python和Java之间的无缝交互使开发人员可以在开发和发布产品时自由混合使用这两种语言。

### Aspose.PDF for Java

Aspose.PDF for Java 是一个 PDF 文档创建组件，它使您的 Java 应用程序能够在不使用 Adobe Acrobat 的情况下读取、写入和操作 PDF 文档。

Aspose.PDF for Java 是一个价格实惠的组件，提供了丰富的功能，其中包括：PDF 压缩选项、表格创建和操作、图形支持、图像功能、广泛的超链接功能、扩展的安全控制和自定义字体处理。

Aspose.PDF for Java 允许您通过提供的 API 和 XML 模板直接创建 PDF 文件。使用 Aspose.PDF for Java 还可以让您在短时间内为您的应用程序添加 PDF 功能。

### Aspose.PDF Java for Jython

Aspose.PDF Java for Jython 是一个项目，演示/提供了 Jython 中 Aspose.PDF for Java API 的使用示例。
## 系统要求和支持的平台

### 系统要求

以下是使用 Aspose.PDF Java for Jython 的系统要求：

- 安装 Java 1.5 或更高版本
- 下载 Aspose.PDF 组件
- Jython 2.7.0

### 支持的平台

以下是支持的平台：

- Aspose.PDF 15.4 及以上版本。
- Java IDE (Eclipse, NetBeans ...)

## 下载安装和使用

### 下载

以下运行示例的版本可从 GitHub 下载：

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose-Pdf-Java-for-Jython)

下载 Aspose.PDF for Java 组件：

- [Aspose.PDF for Java](https://downloads.aspose.com/pdf/java)

### 安装

- 将下载的 Aspose.PDF for Java jar 文件放入 "lib" 目录。
- 在 _*init*_.py 文件中将 "your-lib" 替换为下载的 jar 文件名。

### 使用

您可以使用以下示例代码将 Pdf 转换为 doc 文档：

```java
from aspose-pdf import Settings
from com.aspose.pdf import Document

class PdfToDoc:

    def __init__(self):
        dataDir = Settings.dataDir + 'WorkingWithDocumentConversion/PdfToDoc/'


        # 打开目标文档
        pdf = Document(dataDir + 'input1.pdf')

        # 保存合并的输出文件（目标文档）
        pdf.save(dataDir + "output.doc")

        print "文档已成功转换"


if __name__ == '__main__':       

    PdfToDoc()
```


## 支持、扩展和贡献

### 支持

从 Aspose 的第一天起，我们就知道仅仅为客户提供好的产品是不够的。我们还需要提供良好的服务。我们自己也是开发人员，理解当技术问题或软件中的小问题阻止你完成工作时的沮丧。我们在这里是为了解决问题，而不是制造问题。

这就是为什么我们提供免费支持。任何使用我们产品的人，无论是购买者还是使用评估版的用户，都值得我们给予充分的关注和尊重。

您可以使用以下任何平台记录与 Aspose.PDF Java for Jython 相关的问题或建议：

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)

### 扩展和贡献

Aspose.PDF Java for Jython 是开源的，其源代码在以下列出的主要社交编码网站上可用。
 开发者被鼓励下载源代码，并通过建议或添加新功能或改进现有功能来进行贡献，使其他人也能从中受益。

### 源代码

您可以从以下位置之一获取最新的源代码

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java)