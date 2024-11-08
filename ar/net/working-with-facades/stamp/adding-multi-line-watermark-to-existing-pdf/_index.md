---
title: إضافة العلامة المائية متعددة الأسطر
type: docs
weight: 10
url: /ar/net/adding-multi-line-watermark-to-existing-pdf/
description: يشرح هذا القسم كيفية إضافة علامة مائية متعددة الأسطر إلى PDF موجود باستخدام فئة FormattedText.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

يرغب الكثير من المستخدمين في ختم مستنداتهم بصيغة PDF بنص متعدد الأسطر. عادةً ما يحاولون استخدام `\n` و `<br>` ولكن هذه الأنواع من الأحرف غير مدعومة بواسطة فضاء الأسماء Aspose.Pdf.Facades. لذلك، لجعل ذلك ممكنًا، قمنا بإضافة طريقة أخرى باسم [AddNewLineText()](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext/methods/addnewlinetext/index) في فئة [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) لفضاء الأسماء Aspose.Pdf.Facades.

{{% /alert %}}

## التنفيذ

يرجى الرجوع إلى الجزء التالي من الشفرة لإضافة علامة مائية متعددة الأسطر في PDF موجود.

```csharp

// إنشاء كائن ختم
Stamp logoStamp = new Stamp();

// إنشاء كائن من فئة FormattedText
FormattedText formatText = new FormattedText("Hello World!",
System.Drawing.Color.FromArgb(180, 0, 0), FontStyle.TimesItalic, EncodingType.Winansi, false, 50);

// إضافة سطر آخر للختم
formatText.AddNewLineText("Good Luck");
// ربط الشعار بـ PDF
logoStamp.BindLogo(formatText);
```
```