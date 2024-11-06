---
title: .NET 5を使用してPDFファイルをマージする
linktitle: PDFをマージする方法
type: docs
weight: 75
url: ja/net/how-to-concatenate-pdf-files-in-different-ways/
description: この記事では、既存の複数のPDFファイルを単一のPDFファイルに結合するための可能な方法を説明します。
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

この記事では、[Aspose.PDF for .NET](/pdf/net/)コンポーネントを使用して、複数のPDFドキュメントを単一のPDFドキュメントに[結合](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index)する方法について説明します。[Aspose.PDF for .NET](/pdf/net/)は、この作業を簡単にします。

{{% /alert %}}

あなたがしなければならないことは、[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor)クラスの[Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index)メソッドを呼び出すだけです。すると、入力されたすべてのPDFファイルが結合され、単一のPDFファイルが生成されます。 アプリケーションを作成して、PDFファイルの連結を練習しましょう。Visual Studio.NET 2019を使用してアプリケーションを作成します。

{{% alert color="primary" %}}

Aspose.PDF for .NETは、ASP.NET WebアプリケーションやWindowsアプリケーションを含む.NET Framework上で動作するあらゆる種類のアプリケーションで使用できます。

{{% /alert %}}

## 異なる方法でPDFファイルを連結する方法

フォームには、PDFファイルを参照するためのそれぞれのリンクラベル（linkLabel1、linkLabel2、linkLabel3）を持つ3つのテキストボックス（textBox1、textBox2、textBox3）があります。"Browse"リンクラベルをクリックすると、PDFファイルを選択できる入力ファイルダイアログ（inputFileDialog1）が表示されます（連結するため）。

```csharp

private void linkLabel1_LinkClicked(object sender, System.Windows.Forms.LinkLabelLinkClickedEventArgs e)
{
  if(openFileDialog1.ShowDialog()==DialogResult.OK)
  {
     textBox1.Text=openFileDialog1.FileName;
  }
}
```

PDFファイルの連結のための[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor)クラスのデモンストレーションとして、Windowsフォームアプリケーションのビューが示されています。
![PDFファイルを連結する](how-to-concatenate-pdf-files-in-different-ways_1.png)

PDFファイルを選択してOKボタンをクリックすると、パス付きの完全なファイル名が関連するテキストボックスに割り当てられます。

![PDFファイルを選択](how-to-concatenate-pdf-files-in-different-ways_2.png)

同様に、以下のようにして連結するために2つまたは3つの入力PDFファイルを選択できます。

![2つまたは3つの入力PDFファイルを選択](how-to-concatenate-pdf-files-in-different-ways_3.png)

最後のテキストボックス（textBox4）は、この出力ファイルが作成される出力PDFファイルの宛先パスとその名前を受け取ります。

![出力PDFファイルの宛先パス](how-to-concatenate-pdf-files-in-different-ways_4.png)

![連結メソッド](how-to-concatenate-pdf-files-in-different-ways_5.png)

## Concatenate() メソッド

Concatenate() メソッドは3つの方法で使用できます。それぞれの方法を詳しく見てみましょう：

### アプローチ 1

- Concatenate(string firstInputFile, string secInputFile, string outputFile)

このアプローチは、2つのPDFファイルだけを結合する必要がある場合にのみ適しています。 最初の2つの引数（firstInputFileとsecInputFile）は、連結される2つの入力PDFファイルのストレージパスを含む完全なファイル名を提供します。3番目の引数（outputFile）は、出力PDFファイルの希望するファイル名とパスを提供します。

![ファイル名を使用して2つのPDFを連結する](how-to-concatenate-pdf-files-in-different-ways_6.png)

```csharp
private void button1_Click(object sender, System.EventArgs e)
{
  PdfFileEditor pdfEditor = new PdfFileEditor();
  pdfEditor.Concatenate(textBox1.Text,textBox2.Text,textBox4.Text);
}
```

### アプローチ 2

- Concatenate(System.IO.Stream firstInputStream, System.IO.Stream secInputStream, System.IO.Stream outputStream)

上記のアプローチと同様に、このアプローチも2つのPDFファイルを結合することを可能にします。 最初の2つの引数（firstInputStreamとsecInputStream）は、連結される2つの入力PDFファイルをストリーム（ストリームはビット/バイトの配列）として提供します。3番目の引数（outputStream）は、目的の出力PDFファイルのストリーム表現を提供します。

![ファイルストリームを使用して2つのPDFを連結する](how-to-concatenate-pdf-files-in-different-ways_7.png)

```csharp
private void button2_Click(object sender, System.EventArgs e)
{
  FileStream pdf1 = new FileStream(textBox1.Text,FileMode.Open);
  FileStream pdf2 = new FileStream(textBox2.Text,FileMode.Open);
  FileStream outputPDF = new FileStream(textBox4.Text,FileMode.Create);
  PdfFileEditor pdfEditor = new PdfFileEditor();
  pdfEditor.Concatenate(pdf1,pdf2,outputPDF);
  outputPDF.Close();
}
```

### アプローチ3

- Concatenate(System.IO.Stream inputStreams[], System.IO.Stream outputStream)

2つ以上のPDFファイルを結合したい場合は、このアプローチが最適な選択肢です。 First argument (inputStreams[]) は、結合されるべきストリームの配列形式の入力PDFファイルを提供します。Second argument (outputStream) は、目的の出力PDFファイルのストリーム表現を提供します。

![複数のPDFをストリームの配列を使用して結合する](how-to-concatenate-pdf-files-in-different-ways_8.png)

```csharp
private void button3_Click(object sender, System.EventArgs e)
{
  FileStream pdf1 = new FileStream(textBox1.Text,FileMode.Open);
  FileStream pdf2 = new FileStream(textBox2.Text,FileMode.Open);
  FileStream pdf3 = new FileStream(textBox3.Text,FileMode.Open);
  Stream[] pdfStreams = new Stream[]{pdf1,pdf2,pdf3};
  FileStream outputPDF = new FileStream(textBox4.Text,FileMode.Create);
  PdfFileEditor pdfEditor = new PdfFileEditor();
  pdfEditor.Concatenate(pdfStreams,outputPDF);
  outputPDF.Close();
}
```