---
title: 识别表单字段名称
type: docs
weight: 10
url: /net/identifying-form-fields-names/
description: Aspose.PDF.Facades 允许您使用 Form 类识别表单字段名称。
lastmod: "2021-06-05"
draft: false
---

[Aspose.PDF for .NET](/pdf/net/) 提供了创建、编辑和填写已创建的 PDF 表单的功能。[Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) 命名空间包含 [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) 类，其中包含名为 [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index) 的函数，它接受两个参数，即字段名称和字段值。因此，为了填写表单字段，您必须了解确切的表单字段名称。

## 实施细节

我们经常会遇到这样一种情况，我们需要填写在某些工具中创建的表单，即。 Adobe Designer，并且我们不确定表单字段的名称。因此，为了填写表单字段，首先我们需要读取所有PDF表单字段的名称。[Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form)类提供了一个名为[FieldNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/properties/fieldnames)的属性，该属性返回整个字段的名称，如果PDF不包含任何字段，则返回null。然而，当使用此属性时，我们获取PDF表单中整个字段的名称，并且我们可能不确定哪个名称对应表单上的哪个字段。

作为解决此问题的方法，我们将使用每个字段的外观属性。 Form 类有一个名为 [GetFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getfieldfacade) 的函数，它返回属性，包括位置、颜色、边框样式、字体、列表项等。要保存这些值，我们需要使用 [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormFieldFacade) 类，该类用于记录字段的视觉属性。一旦我们有了这些属性，我们可以在每个字段下方添加一个文本字段来显示字段名称。

{{% alert color="primary" %}}
此时，出现一个问题：“我们如何确定添加文本字段的位置？”
{{% /alert %}}

{{% alert color="primary" %}}
这个问题的解决方案是在 [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormFieldFacade) 类中的 Box 属性，它保存字段的位置。 我们需要将这些值保存到一个矩形类型的数组中，并使用这些值来识别添加新文本字段的位置。

在 [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) 命名空间中，我们有一个名为 [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor) 的类，它提供了操作 PDF 表单的功能。打开一个 PDF 表单；在每个现有表单字段下添加一个文本字段，并以新名称保存 PDF 表单。