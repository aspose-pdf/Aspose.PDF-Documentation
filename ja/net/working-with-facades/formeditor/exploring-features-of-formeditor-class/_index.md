---
title: FormEditorクラスの機能を探る
type: docs
weight: 10
url: ja/net/exploring-features-of-formeditor-class/
description: Aspose.PDF for .NETライブラリでFormEditorクラスの機能を探る詳細を学ぶことができます
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

PDFドキュメントには時々、AcroFormとして知られるインタラクティブなフォームが含まれています。これは、ウェブページで使用されるフォームのようなものです。これらのフォームには、テキストボックス、チェックボックス、ボタンなど、さまざまな種類のコントロールが含まれています。PDFファイルを扱う開発者は、時にはこれらのフォームを編集する必要があるかもしれません。この記事では、[Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades)がどのようにそれを可能にするかについて詳しく見ていきます。

{{% /alert %}}

## 実装の詳細

開発者は、[Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades)を使用して、新しいフォームやフォームフィールドをPDFドキュメントに追加するだけでなく、既存のフィールドを編集することもできます。 この記事の範囲は、フォーム編集を扱う[Aspose.PDF for .NET](/pdf/net/)の機能に限定されています。

[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor)は、開発者がフォームフィールドを編集できるようにする多くのメソッドとプロパティを含むクラスです。新しいフィールドを追加するだけでなく、既存のフィールドを削除したり、あるフィールドを別の位置に移動したり、フィールド名や属性を変更したりすることができます。このクラスが提供する機能のリストは非常に包括的で、このクラスを使用してフォームフィールドを操作するのは非常に簡単です。

これらのメソッドは、フィールドを操作するために使用されるものと、これらのフィールドの新しい属性を設定するために使用されるものの2つの主要なカテゴリに分けることができます。 最初のカテゴリに分類できるメソッドには、AddField、AddListItem、RemoveListItem、CopyInnerField、CopyOuterField、DelListItem、MoveField、RemoveField、および RenameField などが含まれます。2 番目のカテゴリのメソッドには、SetFieldAlignment、SetFieldAppearance、SetFieldAttribute、SetFieldLimit、SetFieldScript を含めることができます。次のコードスニペットは、FormEditor クラスのいくつかのメソッドを実際に示しています：

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-FormEditorFeatures-FormEditorFeatures.cs" >}}