---
title: PDFの個々のページを編集する
type: docs
weight: 20
url: /ja/net/editing-a-pdf-s-individual-pages-using-pdfpageeditor-class/
description: このセクションでは、PdfPageEditorクラスを使用してPDFの個々のページを編集する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

[Aspose.PDF for .NET](/pdf/ja/net/)のAspose.Pdf.Facades名前空間は、PDFファイル内の個々のページを操作することを可能にします。この機能は、ページの表示、配置、トランジションなどを扱うのに役立ちます。PdfPageEditorクラスは、この機能を実現するのに役立ちます。この記事では、このクラスが提供するプロパティとメソッド、およびこれらのメソッドの動作について見ていきます。

{{% /alert %}}

## 説明

[PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor)クラスは、[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor)クラスや[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor)クラスとは異なります。 まず、違いを理解する必要があり、その後で PdfPageEditor クラスをよりよく理解できるようになります。PdfFileEditor クラスは、ページの追加、削除、結合など、ファイル内のすべてのページを操作できるようにしますが、PdfContentEditor クラスは、ページ内のテキストやその他のオブジェクトなどの内容を操作するのに役立ちます。一方で、PdfPageEditor クラスは、ページの回転、ズーム、整列など、個々のページ自体のみを操作します。

このクラスが提供する機能は、大きく分けて遷移、整列、表示の3つの主要なカテゴリに分類できます。これらのカテゴリについて以下で説明します：

### Transition

このクラスは、遷移に関連する2つのプロパティを含んでいます。 [TransitionType](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/transitiontype) と [TransitionDuration](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/transitionduration)。TransitionTypeは、プレゼンテーション中に別のページからこのページに移動する際に使用されるトランジションスタイルを指定します。TransitionDurationはページの表示時間を指定します。

### Alignment

PdfPageEditor クラスは、水平および垂直の両方の配置をサポートしています。 それは、目的を果たすために2つのプロパティ、すなわち[Alignment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/alignment)と[VerticalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/VerticalAlignment)を提供します。Alignmentプロパティは、コンテンツを水平に整列させるために使用されます。Alignmentプロパティは、AlignmentTypeの値を取り、Center、Left、Rightの3つのオプションを含みます。VerticalAlignmentプロパティは、VerticalAlignmentTypeの値を取り、Bottom、Center、Topの3つのオプションを含みます。

### Display

表示カテゴリには、PageSize、Rotation、Zoom、DisplayDurationのようなプロパティを含めることができます。 PageSizeプロパティは、ファイル内の個々のページのサイズを指定します。このプロパティは、A0、A1、A2、A3、A4、A5、A6、B5、Letter、Ledger、P11x17などの定義済みページサイズをカプセル化するPageSizeオブジェクトを入力として受け取ります。Rotationプロパティは、個々のページの回転を設定するために使用されます。これは、0、90、180、または270の値を取ることができます。Zoomプロパティは、ページのズーム係数を設定し、入力として浮動小数点値を取ります。このクラスはまた、ファイル内の個々のページのページサイズとページの回転を取得するためのメソッドを提供します。

以下のコードスニペットで上記のメソッドのサンプルを見つけることができます：

## 結論
{{% alert color="primary" %}}

この記事では、[PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor)クラスを詳しく見てきました。 ```
私たちは、このクラスが提供するプロパティとメソッドを詳しく説明しました。これにより、クラス内の個々のページの操作が非常に簡単でシンプルな作業になります。
{{% /alert %}}
