---
title: 複数行の透かしを追加する
type: docs
weight: 10
url: /net/adding-multi-line-watermark-to-existing-pdf/
description: このセクションでは、FormattedTextクラスを使用して既存のPDFに複数行の透かしを追加する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

多くのユーザーがPDFドキュメントに複数行のテキストをスタンプしたいと考えています。通常、`\n` や `<br>` を使用しようとしますが、これらのタイプの文字はAspose.Pdf.Facades名前空間ではサポートされていません。そのため、これを可能にするために、Aspose.Pdf.Facades名前空間の[FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext)クラスに[AddNewLineText()](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext/methods/addnewlinetext/index)という別のメソッドを追加しました。

{{% /alert %}}

## 実装

既存のPDFに複数行の透かしを追加するには、以下のコードチャンクを参照してください。

```csharp

// スタンプオブジェクトをインスタンス化
Stamp logoStamp = new Stamp();

// FormattedTextクラスのオブジェクトをインスタンス化
FormattedText formatText = new FormattedText("Hello World!",
System.Drawing.Color.FromArgb(180, 0, 0), FontStyle.TimesItalic, EncodingType.Winansi, false, 50);

// スタンプのために別の行を追加
formatText.AddNewLineText("Good Luck");
// PDFにロゴをバインド
logoStamp.BindLogo(formatText);
```
```