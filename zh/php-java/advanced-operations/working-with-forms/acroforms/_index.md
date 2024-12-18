---
title: 在 PDF 中使用 AcroForms
linktitle: AcroForms
type: docs
weight: 10
url: /zh/php-java/acroforms/
description: 使用 Aspose.PDF for PHP via Java，您可以从头创建表单、填写 PDF 文档中的表单字段、从表单中提取数据、在现有表单中添加或删除字段。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## AcroForms 的基础知识

**AcroForms** 是原始的 PDF 表单技术。AcroForms 是一种面向页面的表单。它们首次于 1998 年推出。它们接受表单数据格式或 FDF 和 XML 表单数据格式或 xFDF 的输入。第三方供应商支持 AcroForms。当 Adobe 推出 AcroForms 时，他们称之为“用 Adobe Acrobat Pro/Standard 制作的 PDF 表单，而不是一种特殊类型的静态或动态 XFA 表单。AcroForms 是可移植的，并且可以在所有平台上运行。

您可以使用 AcroForms 向 PDF 表单文档添加额外的页面。
 感谢模板的概念，您可以使用AcroForms支持使用多个数据库记录填充表单。

PDF 1.7支持两种不同的方法来集成数据和PDF表单。

*AcroForms（也称为Acrobat表单）*，在PDF 1.2格式规范中引入和包含。

*Adobe XML Forms Architecture (XFA) forms*，在PDF 1.5格式规范中作为可选功能引入。XFA规范不包含在PDF规范中，它只是被引用。

为了理解**Acroforms**与**XFA**表单，我们需要先了解基础知识。首先，二者都是您可以使用的PDF表单。Acroforms是较早出现的，创建于1998年，仍被称为经典PDF表单。XFA表单是您可以保存为PDF的网页，出现于2003年。在PDF开始接受XFA表单之前，花费了一段时间。

AcroForms具有XFA中没有的功能，反之亦然，XFA也有一些AcroForms中没有的功能。例如：

- AcroForms支持“模板”的概念，允许将额外页面添加到PDF表单文档中，以支持使用多个数据库记录填充表单。- XFA 支持文档重排的概念，允许字段在需要时调整大小以容纳数据。

因此，PDF 是表单的最佳文件格式，因为它们可以电子分发，并且可以在文档中填写信息，然后发送回发件人，而无需通过传统邮件打印或邮寄。

有关表单处理可能性的更详细研究，请查看以下部分中的文章：

-[创建 AcroForm](/pdf/zh/php-java/create-form/) - 从头创建表单，使用 PHP 添加 RadioButtonField、TextBoxField、Caption Field。

-[填写 AcroForm](/pdf/zh/php-java/fill-form/) - 要填写表单字段，从 Document 对象的 Form 集合中获取字段。

-[提取数据 AcroForm](/pdf/zh/php-java/extract-form/) - 获取所有和个别字段的值等。

-[修改 AcroForm](/pdf/zh/php-java/modifing-form/) - 获取/设置 FieldLimit，移除现有表单中的字段，设置非 14 核心 PDF 字体的表单字段字体，使用 PHP。