---
title: 将HTML转换为PDF在Python中
linktitle: 将HTML转换为PDF文件
type: docs
weight: 40
url: /python-java/convert-html-to-pdf/
lastmod: "2023-04-06"
description: 本主题向您展示如何使用Aspose.PDF. for Python将HTML转换为PDF和MHTML转换为PDF。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## 概述

通过Java的Aspose.PDF for Python是一个专业解决方案，允许您在应用程序中从网页和原始HTML代码创建PDF文件。

本文解释了如何**使用Python将HTML转换为PDF**。它涵盖了以下主题。

_格式_: **HTML**
- [Python HTML到PDF](#python-html-to-pdf)
- [Python 将HTML转换为PDF](#python-html-to-pdf)
- [Python 如何将HTML转换为PDF](#python-html-to-pdf)

## Python HTML到PDF转换

**Aspose.PDF for Python**是一个PDF操作API，可让您无缝地将任何现有的HTML文档转换为PDF。HTML到PDF的转换过程可以灵活定制。

## 将HTML转换为PDF

以下Python代码示例显示了如何将HTML文档转换为PDF。

1. 创建一个 [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) 类的实例。
2. 初始化 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象。
3. 通过调用 **Document.Save()** 方法保存输出的 PDF 文档。

```python

from asposepdf import Api


# 初始化许可证
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

# 从字节数组转换
documentName = "input.html"
with open(documentName, "rb") as file:
    byte_array = file.read()
doc = Api.Document(byte_array, Api.LoadFormat.HTML)
documentOutName = "result_fromHtml.pdf"
doc.save(documentOutName)

# 从文件转换
documentName = "input.html"
doc = Api.Document(documentName, Api.LoadFormat.HTML)
documentOutName = "result2_fromHtml.pdf"
doc.save(documentOutName)
```

{{% alert color="success" %}}
**尝试在线将 HTML 转换为 PDF**

Aspose 为您提供在线免费应用程序 ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf)，您可以尝试研究其功能和质量。

[![Aspose.PDF 转换 HTML 到 PDF 使用免费应用](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}