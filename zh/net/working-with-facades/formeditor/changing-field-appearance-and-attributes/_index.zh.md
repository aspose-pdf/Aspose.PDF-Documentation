---
title: 字段外观和属性
type: docs
weight: 20
url: /net/changing-field-appearance-and-attributes/
description: 本节解释如何使用FormEditor类更改字段外观和属性。
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor) 类位于 [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades)，不仅允许您更改表单字段的外观和感觉，还可以更改字段的行为。在本文中，我们将看到如何使用FormEditor类来更改字段外观、字段属性以及字段限制。

{{% /alert %}}

## 实现细节

[SetFieldAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldappearance) 方法用于更改表单字段的外观。 它将 AnnotationFlag 作为参数。AnnotationFlag 是一个枚举，其中有不同的成员，如 Hidden 或 NoRotate 等。

[SetFieldAttributes](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldattribute) 方法用于更改表单字段的属性。传递给此方法的参数是 PropertyFlag 枚举，其中包含成员，如 ReadOnly 或 Required 等。

[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor) 类还提供了一种设置字段限制的方法。它告诉字段可以填充多少字符。下面的代码片段向您展示了如何使用所有这些方法。