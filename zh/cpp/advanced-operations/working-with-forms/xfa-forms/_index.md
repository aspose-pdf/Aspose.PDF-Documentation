---
title: 使用 C++ 操作 XFA 表单
linktitle: XFA 表单
type: docs
weight: 20
url: /zh/cpp/xfa-forms/
description: Aspose.PDF for C++ API 允许您在 PDF 文档中使用 XFA 和 XFA Acroform 字段。Aspose.PDF.Facades。
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

XFA 表单是 XML 表单架构，是由 JetForm 提出和开发的一系列专有 XML 规范，用于改进网页表单的处理。 从 PDF 1.5 规范开始，它也可以用于 PDF 文件。

使用 [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.facades) 的 [Form](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.form/) 类填充 XFA 字段。

## 填充 XFA 字段

以下代码片段向您展示了如何在 XFA 表单中填充字段。

```cpp
using namespace System;
using namespace System::Collections::Generic;

using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void FillXFA() {
    String _dataDir("C:\\Samples\\");

    // 加载 XFA 表单
    auto document = MakeObject<Document>(_dataDir + u"FillXFAFields.pdf");

    // 获取 XFA 表单字段的名称
    auto names = document->get_Form()->get_XFA()->get_FieldNames();

    // 设置字段值

    document->get_Form()->get_XFA()->idx_set(names->idx_get(0),u"Field 0");
    document->get_Form()->get_XFA()->idx_set(names->idx_get(1),u"Field 1");

    // 保存更新后的文档
    document->Save(_dataDir + u"Filled_XFA_out.pdf");
}
```

## 将 XFA 转换为 AcroForm

{{% alert color="primary" %}}

在线尝试
您可以通过此链接在线检查 Aspose.PDF 转换的质量并查看结果：[products.aspose.app/pdf/xfa/acroform](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

动态表单基于称为 XFA 的 XML 规范，即“XML 表单架构”。关于表单的信息（就 PDF 而言）非常模糊——它指定了字段的存在、属性和 JavaScript 事件，但没有指定任何渲染。

目前，PDF 支持两种不同的方法来集成数据和 PDF 表单：

- AcroForms（也称为 Acrobat 表单），在 PDF 1.2 格式规范中引入并包含。
- Adobe XML Forms Architecture (XFA) 表单，在 PDF 1.5 格式规范中作为可选功能引入（XFA 规范未包含在 PDF 规范中，仅被引用。）

我们无法提取或操作 XFA 表单的页面，因为表单内容是在运行时（在 XFA 表单查看期间）在尝试显示或渲染 XFA 表单的应用程序中生成的。 Aspose.PDF 具有一个功能，允许开发人员将 XFA 表单转换为标准的 AcroForms。

```cpp
void ConvertXFAtoAcroForms() {

    String _dataDir("C:\\Samples\\");

    // 加载 XFA 表单
    auto document = MakeObject<Document>(_dataDir + u"DynamicXFAToAcroForm.pdf");

    // 将表单字段类型设置为标准 AcroForm
    document->get_Form()->set_Type(Aspose::Pdf::Forms::FormType::Standard);

    // 保存生成的 PDF
    document->Save(_dataDir + u"Standard_AcroForm_out.pdf");
}
```

## 获取 XFA 字段属性

要访问字段属性，首先使用 Document.Form.XFA.Teamplate 访问字段模板。以下代码片段展示了获取 XFA 表单字段的 X 和 Y 坐标的步骤。

```cpp
void GetXFAProprties() {

    String _dataDir("C:\\Samples\\");
    // 加载 XFA 表单
    auto document = MakeObject<Document>(_dataDir + u"GetXFAProperties.pdf");

    auto names = document->get_Form()->get_XFA()->get_FieldNames();

    // 设置字段值
    document->get_Form()->get_XFA()->idx_set(names->idx_get(0), u"Field 0");
    document->get_Form()->get_XFA()->idx_set(names->idx_get(0), u"Field 1");

    // 获取字段位置
    Console::WriteLine(document->get_Form()->get_XFA()->GetFieldTemplate(names[0])->get_Attributes()->idx_get(u"x")->get_Value());

    // 获取字段位置
    Console::WriteLine(document->get_Form()->get_XFA()->GetFieldTemplate(names[0])->get_Attributes()->idx_get(u"y")->get_Value());

    // 保存更新后的文档
    document->Save(_dataDir + u"Filled_XFA_out.pdf");
}
```