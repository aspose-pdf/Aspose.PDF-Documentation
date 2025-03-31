---
title: .NET 5を使用してPDFファイルをマージする
linktitle: PDFをマージする方法
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 75
url: /ja/net/how-to-concatenate-pdf-files-in-different-ways/
description: この記事では、既存のPDFファイルを任意の数だけ連結して1つのPDFファイルにする方法を説明します。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Merge PDF files",
    "alternativeHeadline": "Effortlessly Combine Multiple PDFs",
    "abstract": "新機能を使用して、複数のPDFファイルをシームレスに1つのドキュメントにマージします。この機能により、開発者は簡単なメソッド呼び出しを通じて任意の数のPDFを連結でき、PDF管理と操作の生産性が向上します。この機能をASP.NETやWindowsアプリケーションなど、さまざまな.NETアプリケーションに簡単に統合でき、異なるニーズに応じた多様なアプローチが可能です。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "840",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/how-to-concatenate-pdf-files-in-different-ways/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/how-to-concatenate-pdf-files-in-different-ways/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

{{% alert color="primary" %}}

この記事では、[Aspose.PDF for .NET](/pdf/ja/net/)コンポーネントの助けを借りて、複数のPDFドキュメントを1つのPDFドキュメントに[連結](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index)する方法を説明します。[Aspose.PDF for .NET](/pdf/ja/net/)は、この作業を簡単にします。

{{% /alert %}}

すべての入力PDFファイルを連結し、1つのPDFファイルを生成するには、[PdfFileEditor](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffileeditor)クラスの[Concatenate](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index)メソッドを呼び出すだけです。PDFファイルの連結を練習するためのアプリケーションを作成しましょう。Visual Studio.NET 2019を使用してアプリケーションを作成します。

{{% alert color="primary" %}}

Aspose.PDF for .NETは、ASP.NETウェブアプリケーションやWindowsアプリケーションなど、.NET Framework上で動作するあらゆる種類のアプリケーションで使用できます。

{{% /alert %}}

## PDFファイルをさまざまな方法で連結する方法

フォームには、PDFファイルを参照するためのそれぞれのリンクラベル（linkLabel1、linkLabel2、linkLabel3）を持つ3つのテキストボックス（textBox1、textBox2、textBox3）があります。「参照」リンクラベルをクリックすると、PDFファイルを選択できる入力ファイルダイアログ（inputFileDialog1）が表示されます。

```csharp
private void linkLabel1_LinkClicked(object sender, System.Windows.Forms.LinkLabelLinkClickedEventArgs e)
{
    if (openFileDialog1.ShowDialog()==DialogResult.OK)
    {
        textBox1.Text=openFileDialog1.FileName;
    }
}
```

PDFファイルの連結のための[PdfFileEditor](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdffileeditor)クラスのデモンストレーションとして、ウィンドウフォームアプリケーションのビューが表示されています。

![PDFファイルを連結する](how-to-concatenate-pdf-files-in-different-ways_1.png)

PDFファイルを選択してOKボタンをクリックすると、関連するテキストボックスに完全なファイル名とパスが割り当てられます。

![PDFファイルを選択](how-to-concatenate-pdf-files-in-different-ways_2.png)

同様に、以下のように2つまたは3つの入力PDFファイルを選択して連結できます。

![2つまたは3つの入力PDFファイルを選択](how-to-concatenate-pdf-files-in-different-ways_3.png)

最後のテキストボックス（textBox4）には、出力PDFファイルの名前とともに出力ファイルが作成される宛先パスを入力します。

![出力PDFファイルの宛先パス](how-to-concatenate-pdf-files-in-different-ways_4.png)

![Concatenateメソッド](how-to-concatenate-pdf-files-in-different-ways_5.png)

## Concatenate()メソッド

Concatenate()メソッドは3つの方法で使用できます。それぞれを詳しく見てみましょう。

### アプローチ1

- Concatenate(string firstInputFile, string secInputFile, string outputFile)

このアプローチは、2つのPDFファイルを結合する必要がある場合にのみ適しています。最初の2つの引数（firstInputFileとsecInputFile）は、連結する2つの入力PDFファイルの完全なファイル名とその保存パスを提供します。3番目の引数（outputFile）は、出力PDFファイルの希望するファイル名とパスを提供します。

![ファイル名を使用して2つのPDFを連結](how-to-concatenate-pdf-files-in-different-ways_6.png)

```csharp
private void button1_Click(object sender, System.EventArgs e)
{
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    pdfEditor.Concatenate(textBox1.Text,textBox2.Text,textBox4.Text);
}
```

### アプローチ2

- Concatenate(Stream firstInputStream, Stream secInputStream, Stream outputStream)

上記のアプローチと同様に、このアプローチも2つのPDFファイルを結合することを可能にします。最初の2つの引数（firstInputStreamとsecInputStream）は、連結する2つの入力PDFファイルをストリームとして提供します（ストリームはビット/バイトの配列です）。3番目の引数（outputStream）は、希望する出力PDFファイルのストリーム表現を提供します。

![ファイルストリームを使用して2つのPDFを連結](how-to-concatenate-pdf-files-in-different-ways_7.png)

```csharp
private void button2_Click(object sender, System.EventArgs e)
{
    using (var pdf1 = new FileStream(textBox1.Text, FileMode.Open))
    {
        using (var pdf2 = new FileStream(textBox2.Text, FileMode.Open))
        {
            using (var outputStream = new FileStream(textBox4.Text, FileMode.Create))
            {
                var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
                pdfEditor.Concatenate(pdf1, pdf2, outputStream);
            }
        }
    }
}
```

### アプローチ3

- Concatenate(Stream inputStreams[], Stream outputStream)

2つ以上のPDFファイルを結合したい場合、このアプローチが最適です。最初の引数（inputStreams[]）は、連結する入力PDFファイルをストリームの配列として提供します。2番目の引数（outputStream）は、希望する出力PDFファイルのストリーム表現を提供します。

![ストリームの配列を使用して複数のPDFを連結](how-to-concatenate-pdf-files-in-different-ways_8.png)

```csharp
private void button3_Click(object sender, System.EventArgs e)
{
    using (var pdf1 = new FileStream(textBox1.Text, FileMode.Open))
    {
        using (var pdf2 = new FileStream(textBox2.Text, FileMode.Open))
        {
            using (var pdf3 = new FileStream(textBox3.Text, FileMode.Open))
            {
                var pdfStreams = new Stream[] { pdf1, pdf2, pdf3 };
                using (var outputStream = new FileStream(textBox4.Text, FileMode.Create))
                {
                    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
                    pdfEditor.Concatenate(pdfStreams, outputStream);
                }
            }
        }
    }
}
```