---
title: 高度な機能
type: docs
weight: 210
url: /ja/net/advanced-features/
---

## ブラウザにPDFをダウンロードするために送信する

ASP.NETアプリケーションを開発しているとき、物理的に保存せずにウェブブラウザにPDFファイルをダウンロードするために送信する必要があります。これを実現するために、PDFドキュメントを生成した後にMemoryStreamオブジェクトに保存し、そのMemoryStreamからバイトをResponseオブジェクトに渡すことができます。これを行うと、ブラウザが生成されたPDFドキュメントをダウンロードします。

以下のコードスニペットは上記の機能を示しています：

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-Examples.Web-SendPdfToBrowserForDownload.aspx-1.cs" >}}

## PDFファイルから埋め込まれたファイルを抽出する

PDF形式のファイルを扱う際に、Aspose.PDFは高度な機能で際立っています。他のツールがこの機能を提供するよりもはるかに優れた方法で埋め込まれたファイルを抽出します。

Aspose.PDF for .NETを使用すると、埋め込まれたフォント、画像、ビデオ、またはオーディオなど、任意の埋め込まれたファイルを効率的に抽出できます。
Aspose.PDF for .NETを使用すると、埋め込まれたフォント、画像、ビデオ、またはオーディオである可能性のある任意の埋め込みファイルを効率的に抽出できます。

次のコードスニペットは、PDFファイルからすべての埋め込みファイルを抽出します：

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-DocumentConversion-PDFToXML-PDFToXML.cs" >}}

## 数学表現を追加するためのLatexスクリプトの使用

Aspose.PDFを使用すると、latexスクリプトを使用してPDFドキュメント内に数学表現/式を追加できます。次の例は、この機能がテーブルセル内に数学式を追加するために2つの異なる方法でどのように使用できるかを示しています：

### 前文およびドキュメント環境なし

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Text-UseLatexScript-WithoutPreambleanddocument.cs" >}}

### 前文およびドキュメント環境あり

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Text-UseLatexScript2-WithPreambleanddocument.cs" >}}

### Latexタグのサポート

changefreq: "monthly"
type: docs
### Latexタグのサポート

align環境はamsmathパッケージで定義されており、proof環境はamsthmパッケージで定義されています。したがって、ドキュメントのプリアンブルでこれらのパッケージを\usepackageコマンドを使用して指定する必要があります。そして、これは以下のコードサンプルに示されているように、LaTeXテキストをdocument環境に入れる必要があることを意味します。

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Text-UseLatexScript3-UseLatexScript3.cs" >}}
