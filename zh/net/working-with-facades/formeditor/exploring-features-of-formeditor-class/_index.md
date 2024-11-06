---
title: 探索FormEditor类的功能
type: docs
weight: 10
url: zh/net/exploring-features-of-formeditor-class/
description: 您可以通过Aspose.PDF for .NET库了解探索FormEditor类功能的详细信息
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

PDF文档有时包含交互式表单，这些表单被称为AcroForm。它就像网页中使用的表单。这些表单包含不同类型的控件，即文本框、复选框和按钮等。处理PDF文件的开发人员有时可能需要编辑这些表单。在本文中，我们将详细了解[Aspose.Pdf.Facades命名空间](https://reference.aspose.com/pdf/net/aspose.pdf.facades)如何使我们能够做到这一点。

{{% /alert %}}

## 实现细节

开发人员可以使用[Aspose.Pdf.Facades命名空间](https://reference.aspose.com/pdf/net/aspose.pdf.facades)不仅可以在PDF文档中添加新表单和表单字段，还可以编辑现有字段。 本文的范围仅限于[Aspose.PDF for .NET](/pdf/net/)中处理表单编辑的功能。

[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor)是一个类，其中包含大多数允许开发人员编辑表单字段的方法和属性。您不仅可以添加新字段，还可以删除现有字段，将一个字段移动到另一个位置，更改字段名称或属性等。该类提供的功能列表相当全面，使用此类操作表单字段也非常简单。

这些方法可以分为两个主要类别，其中之一用于操作字段，另一个用于设置这些字段的新属性。 第一类方法包括 AddField、AddListItem、RemoveListItem、CopyInnerField、CopyOuterField、DelListItem、MoveField、RemoveField 和 RenameField 等。第二类方法可以包括 SetFieldAlignment、SetFieldAppearance、SetFieldAttribute、SetFieldLimit、SetFieldScript。以下代码片段展示了 FormEditor 类的一些方法的工作原理：

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-FormEditorFeatures-FormEditorFeatures.cs" >}}