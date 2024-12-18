---
title: 修改AcroForm
linktitle: 修改AcroForm
type: docs
weight: 40
url: /zh/cpp/modifing-form/
description: 使用Aspose.PDF for C++库修改PDF文件中的表单。您可以在现有表单中添加或删除字段，获取和设置字段限制等。
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 获取或设置字段限制

FormEditor类的SetFieldLimit(field, limit)方法允许您设置字段限制，即可以输入到字段中的最大字符数。

```cpp
void SetFieldLimitDom() {
    String _dataDir("C:\\Samples\\");
    // 打开文档
    auto document = MakeObject<Document>(_dataDir + u"GetValuesFromAllFields.pdf");
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));
    textBoxField->set_MaxLen(15);
    document->Save(_dataDir + u"GetValuesFromAllFields.pdf");
}
```

类似地，Aspose.PDF具有使用DOM方法获取字段限制的方法。 以下代码片段显示了步骤。

```cpp
void GetFieldLimitDom() {
    String _dataDir("C:\\Samples\\");
    // 打开文档
    auto document = MakeObject<Document>(_dataDir + u"GetValuesFromAllFields.pdf");
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));
    Console::WriteLine(u"Limit: {0}", textBoxField->get_MaxLen());        
}
```

您还可以使用以下代码片段通过 *Aspose.PDF.Facades* 命名空间设置和获取相同的值。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;

void SetFieldLimitFacade(){
    String _dataDir("C:\\Samples\\");
    // 添加带限制的字段
    auto form = MakeObject<Aspose::Pdf::Facades::FormEditor>(_dataDir + u"input.pdf", _dataDir + u"SetFieldLimit_out.pdf");
    form->SetFieldLimit(u"textbox1", 15);
    form->Save();
}
```

```cpp
void GetFieldLimitFacade(){
    String _dataDir("C:\\Samples\\");
    // 添加带限制的字段
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + u"input.pdf");
    Console::WriteLine(u"Limit: {0}", form->GetFieldLimit(u"textbox1"));
}
```
## 为表单字段设置自定义字体

Adobe PDF 文件中的表单字段可以配置为使用特定的默认字体。在早期版本的 Aspose.PDF 中，只支持 14 种默认字体。后来的版本允许开发人员应用任何字体。要设置和更新用于表单字段的默认字体，请使用 DefaultAppearance (Font font, double size, Color color) 类。此类可以在 Aspose.PDF.InteractiveFeatures 命名空间下找到。要使用此对象，请使用 Field 类的 DefaultAppearance 属性。

以下代码片段演示了如何为 PDF 表单字段设置默认字体。

```cpp
void SetCustomFontForField() {

    String _dataDir("C:\\Samples\\");

    // 打开文档
    auto document = new Document(_dataDir + u"FormFieldFont14.pdf");

    // 从文档获取特定的表单字段
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));

    // 创建字体对象
    auto font = Aspose::Pdf::Text::FontRepository::FindFont(u"ComicSansMS");

    // 设置表单字段的字体信息

    textBoxField->set_DefaultAppearance(MakeObject<Aspose::Pdf::Annotations::DefaultAppearance>(font, 10, System::Drawing::Color::get_Black()));

    // 保存更新后的文档
    document->Save(_dataDir + u"FormFieldFont14.pdf");
}
```

## 从现有表单中删除字段

所有表单字段都包含在 Document 对象的 Form 集合中。此集合提供了管理表单字段的不同方法，包括 Delete 方法。如果要删除特定字段，请将字段名称作为参数传递给 Delete 方法，然后保存更新后的 PDF 文档。以下代码片段显示了如何从 PDF 文档中删除特定字段。

```cpp
void DeleteFormField() {    
    String _dataDir("C:\\Samples\\");

    // 打开文档
    auto document = new Document(_dataDir + u"DeleteFormField.pdf");

    // 按名称删除特定字段
    document->get_Form()->Delete(u"textbox1");
    
    // 保存修改后的文档
    document->Save(_dataDir + u"DeleteFormField_out.pdf");
}
```