---
title: 添加多行水印
type: docs
weight: 10
url: /net/adding-multi-line-watermark-to-existing-pdf/
description: 本节说明如何使用FormattedText类向现有PDF添加多行水印。
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

许多用户希望在他们的PDF文档上添加多行文本水印。他们通常尝试使用`\n`和`<br>`，但这些类型的字符不受Aspose.Pdf.Facades命名空间支持。因此，为了实现这一点，我们在Aspose.Pdf.Facades命名空间的[FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext)类中添加了一个名为[AddNewLineText()](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext/methods/addnewlinetext/index)的方法。

{{% /alert %}}

## 实现

请参考以下代码段以在现有PDF中添加多行水印。

```csharp

// 实例化一个印章对象
Stamp logoStamp = new Stamp();

// 实例化FormattedText类的对象
FormattedText formatText = new FormattedText("Hello World!",
System.Drawing.Color.FromArgb(180, 0, 0), FontStyle.TimesItalic, EncodingType.Winansi, false, 50);

// 为印章添加另一行
formatText.AddNewLineText("Good Luck");
// 绑定Logo到PDF
logoStamp.BindLogo(formatText);
```