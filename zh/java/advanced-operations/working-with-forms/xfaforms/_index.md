---
title: 在 PDF 中使用 XFA 表单
linktitle: XFA 表单
type: docs
weight: 20
url: zh/java/xfa-forms/
description: 使用 Aspose.PDF for Java，您可以从头创建表单、填写 PDF 文档中的表单字段、从表单中提取数据、在现有表单中添加或删除字段。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

XFA 代表 XML 表单架构。它是一套专有的 XML 规范，最初于 1999 年用于 Web 表单，现在已可用于 PDF。

## 将动态 XFA 表单转换为标准 AcroForm

动态表单基于一种称为 XFA 的 XML 规范，即“XML 表单架构”。它还可以将动态 XFA 表单转换为标准 Acroform。关于表单的信息（就 PDF 而言）非常模糊——它指定了字段的存在、属性和 JavaScript 事件，但未指定任何渲染。XFA 表单的对象是在加载文档时绘制的。

目前 PDF 支持两种不同的方法来集成数据和 PDF 表单：

- AcroForms（也称为 Acrobat 表单），在 PDF 1.2 格式规范中引入和包含。

- Adobe XML Forms Architecture (XFA) 表单，在 PDF 1.5 格式规范中作为可选功能引入。（XFA 规范不包含在 PDF 规范中，仅被引用。）

无法提取或操作 XFA 表单的页面，因为表单内容是在运行时（在 XFA 表单查看期间）由尝试显示或渲染 XFA 表单的应用程序生成的。Aspose.PDF 具有一个功能，允许开发人员将 XFA 表单转换为标准 AcroForms。

```java
// 加载动态 XFA 表单
Document document = new Document("XFAform.pdf");
// 将表单字段类型设置为标准 AcroForm
document.getForm().setType(FormType.Standard);
// 保存结果 PDF
document.save("Standard_AcroForm.pdf");
```