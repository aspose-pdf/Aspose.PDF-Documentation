---
title: 在文本框字段中对齐文本
type: docs
weight: 20
url: /net/justify-text-in-a-textbox-field/
description: 本文向您展示如何使用Form类在文本框字段中对齐文本。
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

在本文中，我们将向您展示如何在PDF文件的文本框字段中对齐文本。

{{% /alert %}}

## 实现细节

[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) 类在 [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) 中提供了装饰PDF表单字段的功能。 现在，如果您的需求是在文本框字段中对齐文本，您可以轻松实现这一点，使用 [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) 枚举的 [AlignJustified](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade/fields/alignjustified) 值并调用 [FormEditor.DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield/index) 方法。在下面的示例中，我们将首先使用 [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) 类的 [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index) 方法填充一个文本框字段。之后，我们将使用 FormEditor 类来对文本框字段中的文本进行对齐。以下代码片段向您展示了如何在文本框字段中对齐文本。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-JustifyText-JustifyText.cs" >}}
请注意，PDF 不支持两端对齐，因此当您在文本框字段中输入文本时，文本将左对齐。但是，当字段不活动时，文本是两端对齐的。