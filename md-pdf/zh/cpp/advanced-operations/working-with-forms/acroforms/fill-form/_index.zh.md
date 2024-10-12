---
title: 填写AcroForm
linktitle: 填写AcroForm
type: docs
weight: 20
url: /cpp/fill-form/
description: 本节说明如何使用Aspose.PDF for C++在PDF文档中填写表单字段。
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF文档是创建表单的最佳且真正首选的文件类型。

本主题说明如何使用Aspose.PDF for C++填写PDF表单。

Aspose.PDF for C++允许您填写表单字段，从Document对象的Form集合中获取字段。

让我们看看以下示例如何解决此任务：

```cpp
using namespace System;
using namespace Aspose::Pdf;

void FillAcroform()
{
    String _dataDir("C:\\Samples\\");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + u"FillFormField.pdf");

    // 获取字段
    auto textBoxField = System::DynamicCast<Aspose::Pdf::Forms::TextBoxField>(document->get_Form()->idx_get(u"textbox1"));

    // 修改字段值
    textBoxField->set_Value(u"要填写在字段中的值");

    // 保存更新的文档
    document->Save(_dataDir + u"FillFormField_out.pdf");

}
```