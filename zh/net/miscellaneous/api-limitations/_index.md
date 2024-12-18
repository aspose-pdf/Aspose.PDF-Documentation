---
title: API限制
type: docs
weight: 70
url: /zh/net/api-limitations/
---

## **Xsl Fo 到 Pdf**
以下是XSL-FO支持的已知问题。

- 不支持SVG
## **PDF创建者信息**
- 请注意，您不能对**应用程序**和**生产者**字段设置值，因为这些字段将显示Aspose Ltd. 和 Aspose.PDF for .NET x.x.x
## **其他**
以下是一些其他已知问题。

- 不支持Pdf/X。
- 不支持动态XFA表单：因为其页面是在PDF加载时，在Adobe Acrobat/Reader中创建/渲染的。因此，我们无法提取并保存任何此类虚拟页面或多个页面。相反，我们（和Adobe Acrobat）只能提取包含错误消息的一个真实页面。
- 特殊符号$p和$P如果不以空白字符结尾将不起作用。
- HTML到PDF转换：HTML是一种非常广泛的语言，每个新版本的Aspose.PDF for .NET，我们都尽力提供一个更好、更健壯的HTML到PDF转换版本（*支持所有类型的HTML*），但由于HTML文件的性质/结构和复杂性各不相同，有时我们的组件在渲染HTML内容到PDF格式时会遇到一些格式问题，这通常发生在使用结构复杂的文档时。
- HTML转PDF转换：HTML是一种非常广泛的语言，每次发布Aspose.PDF for .NET的新版本，我们都尽最大努力交付更好、更强大的HTML到PDF转换版本（*支持所有类型的HTML*），但由于HTML文件的性质/结构和复杂性各不相同，因此有时我们的组件在渲染HTML内容到PDF格式时会遇到一些格式问题，这通常发生在使用结构复杂的文档时。
- 在Macintosh的MS Word中不支持字体嵌入，同时请注意，在Windows的MS Word中，它仅限于TrueType字体。因此，在使用Aspose.PDF for.NET进行PDF到DOC转换生成的word(DOC)文件时，如果在MAC OS上的MS Word中查看这些文件，嵌入的字体将被替换。更多详情，请查看 [macsupportcentral](http://www.macsupportcentral.com/2012/05/embed-fonts-microsoft-office-word-files/).
