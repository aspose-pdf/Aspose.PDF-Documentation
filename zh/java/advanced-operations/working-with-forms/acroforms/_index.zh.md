---
title: 在PDF中使用AcroForms
linktitle: AcroForms
type: docs
weight: 10
url: /java/acroforms/
description: 使用Aspose.PDF for Java，您可以从头开始创建表单、填写PDF文档中的表单字段、从表单中提取数据、在现有表单中添加或删除字段。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## AcroForms的基本原理

**AcroForms** 是最初的PDF表单技术。AcroForms是面向页面的表单。它们首次推出于1998年。它们接受表单数据格式（FDF）和XML表单数据格式（xFDF）的输入。第三方供应商支持AcroForms。当Adobe推出AcroForms时，他们将其称为“由Adobe Acrobat Pro/Standard创建的PDF表单，而不是特殊类型的静态或动态XFA表单。AcroForms是可移植的，并且在所有平台上都能工作。

您可以使用AcroForms向PDF表单文档中添加额外的页面。
 感谢模板的概念，您可以使用AcroForms支持用多个数据库记录填充表单。

PDF 1.7支持两种不同的方法来集成数据和PDF表单。

*AcroForms（也称为Acrobat表单）*，在PDF 1.2格式规范中引入和包含。

*Adobe XML Forms Architecture (XFA) forms*，在PDF 1.5格式规范中作为可选功能引入（XFA规范未包含在PDF规范中，仅被引用。

为了理解**Acroforms**与**XFA**表单，我们首先需要了解基础知识。首先，这两者都是可以使用的PDF表单。Acroforms是较古老的，于1998年创建，仍被称为经典PDF表单。XFA表单是可以保存为PDF的网页，出现在2003年。PDF开始接受XFA表单花费了一些时间。

AcroForms具有XFA没有的功能，反之亦然。例如：

- AcroForms支持“模板”的概念，允许向PDF表单文档添加额外的页面以支持用多个数据库记录填充表单。- XFA 支持文档重排的概念，允许字段根据需要调整大小以适应数据。

因此，PDF 是用于表单的最佳文件格式，因为它们可以以电子方式分发，并在文档内填写信息后发送回发送者，而无需通过传统邮件打印或邮寄。

要详细了解使用表单的可能性，请研究以下部分中的文章：

-[创建 AcroForm](/pdf/java/create-form/) - 从头开始创建表单，使用 Java 添加 RadioButtonField、TextBoxField、Caption Field。

-[填写 AcroForm](/pdf/java/fill-form/) - 要填写表单字段，从 Document 对象的 Form 集合中获取字段。

-[提取数据 AcroForm](/pdf/java/extract-form/) - 从所有和单个字段获取值等。

-[修改 AcroForm](/pdf/java/modifing-form/) - 获取/设置 FieldLimit，删除现有表单中的字段，使用 Java 设置非 14 核心 PDF 字体的表单字段字体。