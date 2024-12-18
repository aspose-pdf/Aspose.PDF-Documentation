---
title: Добавление многострочного водяного знака
type: docs
weight: 10
url: /ru/net/adding-multi-line-watermark-to-existing-pdf/
description: Этот раздел объясняет, как добавить многострочный водяной знак в существующий PDF с помощью класса FormattedText.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

Многие пользователи хотят штамповать свои PDF-документы многострочным текстом. Они обычно пытаются использовать `\n` и `<br>`, но такие типы символов не поддерживаются пространством имен Aspose.Pdf.Facades. Поэтому, чтобы сделать это возможным, мы добавили другой метод с именем [AddNewLineText()](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext/methods/addnewlinetext/index) в класс [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) пространства имен Aspose.Pdf.Facades.

{{% /alert %}}

## Реализация

Пожалуйста, обратитесь к следующему фрагменту кода, чтобы добавить многострочный водяной знак в существующий PDF.

```csharp

// Создать объект штампа
Stamp logoStamp = new Stamp();

// Создать объект класса FormattedText
FormattedText formatText = new FormattedText("Hello World!",
System.Drawing.Color.FromArgb(180, 0, 0), FontStyle.TimesItalic, EncodingType.Winansi, false, 50);

// Добавить другую строку для штампа
formatText.AddNewLineText("Good Luck");
// Привязать логотип к PDF
logoStamp.BindLogo(formatText);
```
```