---
title: テキストボックスフィールドでテキストを両端揃えする
type: docs
weight: 20
url: ja/net/justify-text-in-a-textbox-field/
description: この記事では、フォームクラスを使用してテキストボックスフィールドでテキストを両端揃えする方法を示します。
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

この記事では、PDFファイルのテキストボックスフィールドでテキストを両端揃えする方法を紹介します。

{{% /alert %}}

## 実装の詳細

[Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades)の[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor)クラスは、PDFフォームフィールドを装飾する機能を提供します。 今、もしあなたの要件がテキストボックスフィールド内のテキストを両端揃えにすることであれば、[FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade)列挙の[AlignJustified](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade/fields/alignjustified)値を使用し、[FormEditor.DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield/index)メソッドを呼び出すことで簡単に実現できます。以下の例では、まず[Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form)クラスの[FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index)メソッドを使用してテキストボックスフィールドを埋めます。その後、FormEditorクラスを使用してテキストボックスフィールド内のテキストを両端揃えにします。以下のコードスニペットは、テキストボックスフィールド内のテキストを両端揃えにする方法を示しています。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-JustifyText-JustifyText.cs" >}}
以下にご依頼の翻訳を行います。

---

Please note that justified alignment is not supported by PDF that's why text will be aligned left when you input the text in the Textbox Field. But when field is not active text is justified.
日本語: PDFでは両端揃えがサポートされていないため、テキストボックスフィールドにテキストを入力すると左揃えになります。しかし、フィールドがアクティブでない場合はテキストが両端揃えになります。