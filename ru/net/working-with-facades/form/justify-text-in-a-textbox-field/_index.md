---
title: Выравнивание текста в поле текстового поля
type: docs
weight: 20
url: ru/net/justify-text-in-a-textbox-field/
description: В этой статье показано, как выровнять текст в поле текстового поля с использованием класса Form.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

В этой статье мы покажем, как выровнять текст в поле текстового поля в файле PDF.

{{% /alert %}}

## Подробности реализации

Класс [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) в [пространстве имен Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) предлагает возможность украшать поле формы PDF. Теперь, если вам необходимо выровнять текст в текстовом поле, вы можете легко достичь этого, используя значение [AlignJustified](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade/fields/alignjustified) перечисления [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) и вызов метода [FormEditor.DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield/index). В примере ниже, сначала мы заполним текстовое поле, используя метод [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index) класса [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form). После этого мы используем класс FormEditor для выравнивания текста в текстовом поле. Следующий фрагмент кода показывает, как выровнять текст в текстовом поле.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-JustifyText-JustifyText.cs" >}}
Пожалуйста, обратите внимание, что выравнивание по ширине не поддерживается в PDF, поэтому текст будет выровнен по левому краю, когда вы вводите текст в поле текстового поля. Но когда поле не активно, текст выравнивается по ширине.