---
title: .NETで他のファイル形式をPDFに変換する
linktitle: 他のファイル形式をPDFに変換する
type: docs
weight: 80
url: /net/convert-other-files-to-pdf/
lastmod: "2021-11-01"
description: このトピックでは、Aspose.PDFを使用してEPUB、MD、PCL、XPS、PS、XML、LaTeXなどの他のファイル形式をPDFドキュメントに変換する方法を紹介します。
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## 概要

この記事では、**C#を使用してさまざまな他のタイプのファイル形式をPDFに変換する方法**について説明します。次のトピックをカバーしています。

以下のコードスニペットも[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリで動作します。

_形式_: **EPUB**
- [C# EPUBをPDFに変換](#csharp-convert-epub-to-pdf)
- [C# EPUBをPDFに変換する](#csharp-convert-epub-to-pdf)
- [C# EPUBファイルをPDFに変換する方法](#csharp-convert-epub-to-pdf)

_形式_: **Markdown**
- [C# MarkdownをPDFに変換](#csharp-convert-markdown-to-pdf)
- [C# MarkdownをPDFに変換する](#csharp-convert-markdown-to-pdf)
- [C# MarkdownファイルをPDFに変換する方法](#csharp-convert-markdown-to-pdf)
- [C# MarkdownファイルをPDFに変換する方法](#csharp-convert-markdown-to-pdf)

_形式_: **MD**
- [C# MDをPDFに変換](#csharp-convert-md-to-pdf)
- [C# MDをPDFに変換する](#csharp-convert-md-to-pdf)
- [C# MDファイルをPDFに変換する方法](#csharp-convert-md-to-pdf)

_形式_: **PCL**
- [C# PCLをPDFに変換](#csharp-convert-pcl-to-pdf)
- [C# PCLをPDFに変換する](#csharp-convert-pcl-to-pdf)
- [C# PCLファイルをPDFに変換する方法](#csharp-convert-pcl-to-pdf)

_形式_: **Text**
- [C# テキストをPDFに変換](#csharp-convert-text-to-pdf)
- [C# テキストをPDFに変換する](#csharp-convert-text-to-pdf)
- [C# テキストファイルをPDFに変換する方法](#csharp-convert-text-to-pdf)

_形式_: **TXT**
- [C# TXTをPDFに変換](#csharp-convert-txt-to-pdf)
- [C# TXTをPDFに変換する](#csharp-convert-txt-to-pdf)
- [C# TXTファイルをPDFに変換する方法](#csharp-convert-txt-to-pdf)

_形式_: **Plain Text**
- [C# プレーンテキストをPDFに変換](#csharp-convert-plain-text-to-pdf)
- [C# プレーンテキストをPDFに変換する](#csharp-convert-plain-text-to-pdf)
- [C# プレーンテキストファイルをPDFに変換する方法](#csharp-convert-plain-text-to-pdf)
- [C# プレーンテキストファイルをPDFに変換する方法](#csharp-convert-plain-text-to-pdf)

_形式_: **プレフォーマットされたTXT**
- [C# プレフォーマットテキストをPDFに変換](#csharp-convert-pre-formatted-txt-to-pdf)
- [C# プレフォーマットテキストをPDFに変換](#csharp-convert-pre-formatted-txt-to-pdf)
- [C# プレフォーマットテキストファイルをPDFに変換する方法](#csharp-convert-pre-formatted-txt-to-pdf)

_形式_: **プレテキスト**
- [C# プレテキストをPDFに変換](#csharp-convert-pre-text-to-pdf)
- [C# プレテキストをPDFに変換](#csharp-convert-pre-text-to-pdf)
- [C# プレテキストファイルをPDFに変換する方法](#csharp-convert-pre-text-to-pdf)

_形式_: **XPS**
- [C# XPSをPDFに変換](#csharp-convert-xps-to-pdf)
- [C# XPSをPDFに変換](#csharp-convert-xps-to-pdf)
- [C# XPSファイルをPDFに変換する方法](#csharp-convert-xps-to-pdf)

## EPUBをPDFに変換

**Aspose.PDF for .NET** はEPUBファイルをPDF形式に簡単に変換できます。

<abbr title="電子出版">EPUB</abbr> (電子出版の略) は国際デジタル出版フォーラム (IDPF) からの無料でオープンな電子書籍標準です。
<abbr title="electronic publication">EPUB</abbr>（電子出版物の略）は、国際デジタル出版フォーラム（IDPF）からの無料でオープンな電子書籍標準です。

EPUBは固定レイアウトコンテンツもサポートしています。このフォーマットは、出版社および変換ハウスが社内で使用するための単一フォーマットとして意図されており、配布や販売にも利用できます。これはOpen eBook標準を置き換えるものです。バージョンEPUB 3は、標準化されたベストプラクティス、研究、情報、イベントのための業界団体であるブックインダストリーサディグループ（BISG）によっても支持されています。

{{% alert color="success" %}}
**EPUBをPDFオンラインに変換してみてください**

Aspose.PDF for .NETは、無料のアプリケーション["EPUB to PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf)をオンラインで提供しています。ここで機能性と品質を試すことができます。

[![Aspose.PDF Convertion EPUB to PDF with Free App](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

<a name="csharp-convert-epub-to-pdf" id="csharp-convert-epub-to-pdf"><strong><em>手順:</em> C#でEPUBをPDFに変換</strong></a>
<a name="csharp-convert-epub-to-pdf" id="csharp-convert-epub-to-pdf"><strong><em>手順:</em> C#でEPUBをPDFに変換する</strong></a>

1. [EpubLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/epubloadoptions) クラスのインスタンスを作成します。
2. ソースファイル名とオプションを指定して [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) クラスのインスタンスを作成します。
3. 希望のファイル名でドキュメントを保存します。

次のコードスニペットは、C#でEPUBファイルをPDF形式に変換する方法を示しています。

```csharp
public static void ConvertEPUBtoPDF()
{
    EpubLoadOptions option = new EpubLoadOptions();
    Document pdfDocument= new Document(_dataDir + "WebAssembly.epub", option);
    pdfDocument.Save(_dataDir + "epub_test.pdf");
}
```

また、変換のためにページサイズを設定することもできます。新しいページサイズを定義するためには、`SizeF` オブジェクトを作成し、[EpubLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/epubloadoptions/constructors/main) コンストラクタに渡します。

```csharp
public static void ConvertEPUBtoPDFAdv()
{
    EpubLoadOptions option = new EpubLoadOptions(new SizeF(1190, 1684));
    Document pdfDocument= new Document(_dataDir + "WebAssembly.epub", option);
    pdfDocument.Save(_dataDir + "epub_test.pdf");
}
```
## MarkdownをPDFに変換

**この機能はバージョン19.6以降でサポートされています。**

{{% alert color="success" %}}
**オンラインでMarkdownをPDFに変換してみましょう**

Aspose.PDF for .NETは、無料のオンラインアプリケーション ["Markdown to PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf) を提供しています。ここで機能と品質を試すことができます。

[![Aspose.PDF Convertion Markdown to PDF with Free App](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

Aspose.PDF for .NETは、入力された[Markdown](https://daringfireball.net/projects/markdown/syntax)データファイルに基づいてPDFドキュメントを作成する機能を提供します。MarkdownをPDFに変換するには、[MdLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/mdloadoptions)を使用して[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)を初期化する必要があります。

次のコードスニペットは、Aspose.PDFライブラリを使用してこの機能を使用する方法を示しています：

<a name="csharp-convert-markdown-to-pdf" id="csharp-convert-markdown-to-pdf"><strong><em>手順:</em> C#でMarkdownをPDFに変換</strong></a>
<a name="csharp-convert-markdown-to-pdf" id="csharp-convert-markdown-to-pdf"><strong><em>手順：</em> C#でMarkdownをPDFに変換する</strong></a> |
<a name="csharp-convert-md-to-pdf" id="csharp-convert-md-to-pdf"><strong><em>手順：</em> C#でMDをPDFに変換する</strong></a>

1. [MdLoadOptions ](https://reference.aspose.com/pdf/net/aspose.pdf/mdloadoptions/) クラスのインスタンスを作成します。
2. ソースファイル名とオプションを指定して [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) クラスのインスタンスを作成します。
3. 希望のファイル名でドキュメントを保存します。

```csharp
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Markdownドキュメントを開く
Document pdfDocument = new Document(dataDir + "sample.md", new MdLoadOptions());
// ドキュメントをPDF形式で保存
pdfDocument.Save(dataDir + "MarkdownToPDF.pdf");
```

## PCLからPDFへの変換

<abbr title="Printer Command Language">PCL</abbr> (Printer Command Language) は、標準プリンタ機能にアクセスするために開発されたHewlett-Packardのプリンタ言語です。
<abbr title="Printer Command Language">PCL</abbr>（プリンターコマンド言語）は、標準的なプリンター機能にアクセスするために開発されたヒューレット・パッカードのプリンター言語です。

{{% alert color="success" %}}
**オンラインでPCLをPDFに変換してみてください**

Aspose.PDF for .NETは、無料のアプリケーション["PCL to PDF"](https://products.aspose.app/pdf/conversion/pcl-to-pdf)を提供しています。ここで機能性と品質を試すことができます。

[![Aspose.PDF Convertion PCL to PDF with Free App](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

**現在、PCL5およびそれ以前のバージョンのみがサポートされています**

<table>
    <thead>
        <tr>
            <th>
                コマンドセット
            </th>
            <th>
                サポート状況
            </th>
            <th>
                例外
            </th>
            <th>
                説明
            </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                ジョブ制御コマンド

<tr>
    <td>
        ジョブ制御コマンド
    </td>
    <td>
        +
    </td>
    <td>
        両面印刷モード
    </td>
    <td>
        印刷プロセスを制御する：コピー数、出力ビン、シンプレックス/デュプレックス印刷、左および上のオフセットなど。
    </td>
</tr>
<tr>
    <td>
        ページ制御コマンド
    </td>
    <td>
        +
    </td>
    <td>
        パーフォレーションスキップコマンド
    </td>
    <td>
        ページのサイズ、余白、ページの向き、行間、文字間の距離などを指定する。
    </td>
</tr>
<tr>
    <td>
        カーソル位置決めコマンド
    </td>
    <td>
        +
    </td>
    <td>
        &nbsp;
    </td>
    <td>
        カーソル位置を指定し、テキスト、ラスターまたはベクター画像の起点と詳細を定める。
    </td>
</tr>
```

<tr>
    <td>
        カーソルの位置を指定し、テキスト、ラスターやベクター画像、詳細の原点となります。
    </td>
</tr>
<tr>
    <td>
        フォント選択コマンド
    </td>
    <td>
        +
    </td>
    <td>
        <ol>
            <li>透明プリントデータコマンド。</li>
            <li>組み込みソフトフォント。現在のバージョンではソフトフォントを作成する代わりに、当社のライブラリは対象のマシンにインストールされている既存の「ハード」TrueTypeフォントから適切なフォントを選択します。<br/>
                適合性は幅/高さの比率によって定義されます。<br/>
                この機能はビットマップとTrueTypeフォントにのみ機能し、ソースファイルのテキストがソフトフォントで印刷されたテキストと関連性があることを保証しません。<br/>
                ソフトフォントの文字コードがデフォルトのものと一致しない可能性があります。
            </li>
            <li>ユーザー定義シンボルセット。</li>
        </ol>
    </td>
</tr>
```


<li>ユーザー定義のシンボルセット。</li>
</ol>
</td>
<td>
PCLファイルからソフト（埋め込み）フォントをロードして、メモリ内で管理することを許可します。
</td>
</tr>
<tr>
<td>
ラスターグラフィックスコマンド
</td>
<td>
+
</td>
<td>
黒白のみ
</td>
<td>
PCLファイルからラスター画像をメモリにロードし、幅、高さ、圧縮タイプ、解像度などのラスターパラメータを指定します。<br>
</td>
</tr>
<tr>
<td>
カラーコマンド
</td>
<td>
+
</td>
<td>
&nbsp;
</td>
<td>
すべての印刷可能オブジェクトに対して色付けを許可します。
</td>
</tr>
<tr>
<td>
プリントモデルコマンド
```
```
モデルコマンドの印刷
テキスト、ラスター画像、およびラスター事前定義された矩形領域を塗りつぶすことを許可し、<br>
パターンとソースラスター画像の透明度モードを指定します。<br> 事前定義されたパターンには、ハッチング、クロスハッチ、
およびシェーディングがあります。

矩形領域塗りつぶしコマンド
パターンを使用して矩形領域を作成および塗りつぶすことを許可します。

HP-GL/2 ベクターグラフィックスコマンド
スクリーンドベクターコマンド（SV）、透明度モードコマンド（TR）、透明データコマンド（TD）、RO
```
スクリーンベクターコマンド（SV）、透明度モードコマンド（TR）、透明データコマンド（TD）、RO（座標系の回転）、スケーラブルまたはビットマップフォントコマンド（SB）、文字スラントコマンド（SL）および追加スペース（ES）は実装されていません。DV（可変テキストパスの定義）コマンドはベータ版で実現されています。

HP-GL/2ベクターイメージをPCLファイルからメモリにロードすることを許可します。ベクターイメージは印刷可能領域の左下隅に原点を持ち、拡大・縮小、移動、回転、クリッピングが可能です。<br>
ベクターイメージは、ラベルとしてのテキストや、長方形、円、楕円、線、弧、ベジェ曲線、および単純な図形から構成される複雑な図形を含むことができます。<br>ラベルの文字を含む閉じた図形は、ソリッドフィルまたはベクターパターンで塗りつぶすことができます。<br>パターンは、ハッチング、クロスハッチ、シェーディング、ラスターユーザー定義、PCLハッチングまたはクロスハッチ、およびPCL

ハッチング、クロスハッチ、シェーディング、ユーザー定義のラスター、PCLハッチングまたはクロスハッチ、PCLユーザー定義。PCLパターンはラスターです。ラベルは個別に回転、拡大/縮小、上、下、左、右の四方向に向けることができます。左方向と右方向は文字が連続して配置されます。上方向と下方向は文字が縦に配置されます。

マクロ
―
&nbsp;
PCLコマンドのシーケンスをメモリにロードして何度も使用することができます。例えば、ページヘッダーを印刷する場合や一連のページに同じフォーマットを設定する場合などです。

Unicodeテキスト
―
```

            </td>
            <td>
                &nbsp;
            </td>
            <td>
                非ASCII文字の印刷を許可します。Unicodeテキストを含むサンプルファイルがないため、実装されていません。<br>
            </td>
        </tr>
        <tr>
            <td>
                PCL6 (PCL-XL)
            </td>
            <td>
                &nbsp;
            </td>
            <td>
                テストファイルが不足しているため、ベータ版でのみ実現されました。埋め込みフォントもサポートされていません。<br> JetReady拡張は、JetReady仕様を持つことが不可能なためサポートされていません。
            </td>
            <td>
                バイナリファイル形式。
            </td>
        </tr>
    </tbody>
</table>

### PCLファイルをPDF形式に変換する

PCLからPDFへの変換を可能にするために、Aspose.PDFには[`PclLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/pclloadoptions) クラスがあり、LoadOptionsオブジェクトを初期化するために使用されます。
```
PCLからPDFへの変換を可能にするために、Aspose.PDFは[`PclLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/pclloadoptions)クラスを使用してLoadOptionsオブジェクトを初期化します。

以下のコードスニペットは、PCLファイルをPDF形式に変換するプロセスを示しています。

<a name="csharp-convert-pcl-to-pdf" id="csharp-convert-pcl-to-pdf"><strong><em>手順:</em> C#でPCLをPDFに変換する</strong></a>

1. [PclLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pclloadoptions/)クラスのインスタンスを作成します。
2. ソースファイル名とオプションを指定して[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/)クラスのインスタンスを作成します。
3. 希望のファイル名でドキュメントを保存します。

```csharp
public static void ConvertPCLtoPDF()
{
    PclLoadOptions options = new PclLoadOptions();
    Document pdfDocument= new Document(_dataDir + "demo.pcl", options);
    pdfDocument.Save(_dataDir + "pcl_test.pdf");
}
```

変換プロセス中のエラー検出も監視できます。
変換プロセス中にエラーの検出を監視することもできます。

```csharp
public static void ConvertPCLtoPDFAvdanced()
{
    PclLoadOptions options = new PclLoadOptions { SupressErrors = true };
    Document pdfDocument= new Document(_dataDir + "demo.pcl", options);
    if (options.Exceptions!=null)
        foreach (var ex in options.Exceptions)
        {
            Console.WriteLine(ex.Message);
        }
    pdfDocument.Save(_dataDir + "pcl_test.pdf");
}
```

### 既知の問題点

1. 印刷方向が0°でない場合、テキスト文字列と画像の原点が元のPCLファイルと若干異なる場合があります。ベクター画像についても、ベクタープロットの座標系が回転している場合（ROコマンドが先行している場合）同様です。
1. ベクター画像のラベルの原点が、次の一連のコマンドに影響を受ける場合、元のPCLファイルと異なる場合があります：ラベル原点（LO）、可変テキストパスの定義（DV）、絶対方向（DI）、相対方向（DR）。
1.
1. 解析されたPCLファイルにIntellifontまたはUniversalソフトフォントが含まれている場合、例外が発生します。これは、IntellifontおよびUniversalフォントが全くサポートされていないためです。
1. 解析されたPCLファイルにマクロコマンドが含まれている場合、解析結果はソースファイルと大きく異なります。これは、マクロコマンドがサポートされていないためです。

## テキストをPDFに変換

**Aspose.PDF for .NET**は、プレーンテキストおよび事前にフォーマットされたテキストファイルをPDF形式に変換する機能をサポートしています。

テキストをPDFに変換するということは、PDFページにテキストフラグメントを追加することを意味します。テキストファイルに関しては、2種類のテキストが扱われます: プリフォーマッティング（例えば、1行に80文字の25行）と非フォーマットテキスト（プレーンテキスト）。ニーズに応じて、この追加を自分たちで制御することも、ライブラリのアルゴリズムに任せることもできます。

{{% alert color="success" %}}
**オンラインでTEXTをPDFに変換してみる**

Aspose.PDF for .NETは、無料のオンラインアプリケーション["テキストをPDFに"](https://products.aspose.app/pdf/conversion/txt-to-pdf)を提供しており、そこで機能や品質を試すことができます。

Aspose.PDF for .NET は無料のオンラインアプリケーション ["Text to PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf) を提供しており、その機能や品質を試すことができます。

[![Aspose.PDFでテキストをPDFに変換する無料アプリ](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

### プレーンテキストファイルをPDFに変換

プレーンテキストファイルの場合、以下の技術を使用できます：

<a name="csharp-convert-text-to-pdf" id="csharp-convert-text-to-pdf"><strong><em>手順：</em> C#でテキストをPDFに変換する</strong></a> |
<a name="csharp-convert-txt-to-pdf" id="csharp-convert-txt-to-pdf"><strong><em>手順：</em> C#でTXTをPDFに変換する</strong></a> |
<a name="csharp-convert-plain-text-to-pdf" id="csharp-convert-plain-text-to-pdf"><strong><em>手順：</em> C#でプレーンテキストをPDFに変換する</strong></a>

1. _TextReader_ を使用して全文を読み取ります；
2.
2.
3. [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment/) の新しいオブジェクトを作成し、そのコンストラクターに _TextReader_ オブジェクトを渡す;
4. _Paragraphs_ コレクションに _TextFragment_ オブジェクトを段落として追加します。テキストの量がページより多い場合、ライブラリのアルゴリズムが自動的に追加ページを追加します;
5. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) クラスの **Save** メソッドを使用します;

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// ソーステキストファイルを読み込む
TextReader tr = new StreamReader(dataDir + "log.txt");

// 空のコンストラクタを呼び出すことによりDocumentオブジェクトのインスタンスを作成します
Document pdfDocument= new Document();

// DocumentのPagesコレクションに新しいページを追加
Page page = pdfDocument.Pages.Add();

// TextFragmetのインスタンスを作成し、リーダーオブジェクトからテキストをそのコンストラクタの引数として渡します
TextFragment text = new TextFragment(tr.ReadToEnd());

// 段落コレクションに新しいテキスト段落を追加し、TextFragmentオブジェクトを渡します
page.Paragraphs.Add(text);

// 結果のPDFファイルを保存
pdfDocument.Save(dataDir + "TexttoPDF_out.pdf");
```
### プリフォーマットされたテキストファイルをPDFに変換する

プリフォーマットされたテキストの変換はプレーンテキストと似ていますが、マージン、フォントタイプ、フォントサイズの設定などの追加アクションが必要です。明らかにフォントはモノスペースである必要があります（例：Courier New）。

C#でプリフォーマットされたテキストをPDFに変換する手順に従ってください：

<a name="csharp-convert-pre-text-to-pdf" id="csharp-convert-pre-text-to-pdf"><strong><em>手順：</em>C#でプリテキストをPDFに変換する</strong></a> |
<a name="csharp-convert-pre-formatted-txt-to-pdf" id="csharp-convert-pre-formatted-txt-to-pdf"><strong><em>手順：</em>C#でプリフォーマットされたTXTをPDFに変換する</strong></a>

1. テキスト全体を文字列の配列として読み込む；
2. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) オブジェクトをインスタンス化し、[Pages](https://reference.aspose.com/pdf/net/aspose.pdf/document/pages/) コレクションに新しいページを追加する；
3.
この場合、ライブラリのアルゴリズムも余分なページを追加しますが、このプロセスを自分たちで制御することができます。
次の例は、事前にフォーマットされたテキストファイル（80x25）をA4サイズのPDFドキュメントに変換する方法を示しています。

```csharp
public static void ConvertPreFormattedTextToPdf()
{
    // テキストファイルを文字列の配列として読み込む
    var lines = System.IO.File.ReadAllLines(_dataDir + "rfc822.txt");

    // 空のコンストラクタを呼び出すことによりDocumentオブジェクトをインスタンス化
    Document pdfDocument= new Document();

    // DocumentのPagesコレクションに新しいページを追加
    Page page = pdfDocument.Pages.Add();

    // より良いプレゼンテーションのために左右のマージンを設定
    page.PageInfo.Margin.Left = 20;
    page.PageInfo.Margin.Right = 10;
    page.PageInfo.DefaultTextState.Font = FontRepository.FindFont("Courier New");
    page.PageInfo.DefaultTextState.FontSize = 12;

    foreach (var line in lines)
    {
        // 行が「フォームフィード」文字を含むかどうかを確認
        // https://en.wikipedia.org/wiki/Page_break を参照
        if (line.StartsWith("\x0c"))
        {
            page = pdfDocument.Pages.Add();
            page.PageInfo.Margin.Left = 20;
            page.PageInfo.Margin.Right = 10;
            page.PageInfo.DefaultTextState.Font = FontRepository.FindFont("Courier New");
            page.PageInfo.DefaultTextState.FontSize = 12;
        }
        else
        {
            // TextFragmentのインスタンスを作成し、
            // 引数として行をその
            // コンストラクタに渡す
            TextFragment text = new TextFragment(line);

            // パラグラフコレクションに新しいテキストパラグラフを追加し、TextFragmentオブジェクトを渡す
            page.Paragraphs.Add(text);
        }
    }

    // 結果のPDFファイルを保存
    pdfDocument.Save(_dataDir + "TexttoPDF_out.pdf");
}
```
## XPSをPDFに変換

**Aspose.PDF for .NET** は、<abbr title="XML Paper Specification">XPS</abbr>ファイルをPDF形式に変換する機能をサポートしています。この記事をチェックして、あなたのタスクを解決してください。

XPSファイルタイプは、主にMicrosoft CorporationによるXML Paper Specificationと関連しています。XML Paper Specification（XPS）は、以前はMetroとコードネームが付けられ、Next Generation Print Path（NGPP）のマーケティングコンセプトが包含されていたもので、MicrosoftがWindowsオペレーティングシステムに文書作成と閲覧を統合するための取り組みです。

{{% alert color="primary" %}}

ファイル形式は基本的にはZIP圧縮されたXMLファイルで、主に配布と保存に使用されます。編集が非常に難しく、主にMicrosoftによって実装されています。

{{% /alert %}}

Aspose.PDF for .NETでXPSをPDFに変換するために、[LoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/loadoptions)オブジェクトを初期化するために使用される[XpsLoadOption](https://reference.aspose.com/pdf/net/aspose.pdf/xpsloadoptions)というクラスを導入しました。
Aspose.PDF for .NETを使用してXPSをPDFに変換するために、[LoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/loadoptions)オブジェクトを初期化するために使用される[XpsLoadOption](https://reference.aspose.com/pdf/net/aspose.pdf/xpsloadoptions)というクラスを導入しました。

{{% alert color="primary" %}}

XPおよびWindows 7の両方で、コントロールパネルにアクセスしてプリンターを見ると、XPSプリンタがプリインストールされているはずです。これらのファイルを作成するには、そのプリンタを出力デバイスとして使用できます。Windows 7では、ファイルをダブルクリックするだけでXPSビューアで開くことができるはずです。また、MicrosoftのウェブサイトからXPSビューアをダウンロードすることもできます。

{{% /alert %}}

次のコードスニペットは、C#でXPSファイルをPDF形式に変換するプロセスを示しています。

<a name="csharp-convert-xps-to-pdf" id="csharp-convert-xps-to-pdf"><strong><em>手順:</em> C#でXPSをPDFに変換</strong></a>

1. [XpsLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/xpsloadoptions/)クラスのインスタンスを作成します。
2.
2.
3. ドキュメントをPDF形式で保存し、希望のファイル名を付けます。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// XPSロードオプションを使用してLoadOptionオブジェクトをインスタンス化します
Aspose.Pdf.LoadOptions options = new XpsLoadOptions();

// ドキュメントオブジェクトを作成します
Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "XPSToPDF.xps", options);

// 結果のPDFドキュメントを保存します
document.Save(dataDir + "XPSToPDF_out.pdf");
```

{{% alert color="success" %}}
**XPS形式をPDFオンラインに変換してみてください**

Aspose.PDF for .NETは、機能性と品質を調査できる無料オンラインアプリケーション["XPS to PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/)をご提供しています。

[![Aspose.PDF Convertion XPS to PDF with Free App](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}

## PostScriptをPDFに変換

**Aspose.PDF for .NET** はPostScriptファイルをPDF形式に変換する機能をサポートしています。Aspose.PDFの特徴の一つとして、変換中に使用するフォントフォルダのセットを設定することができます。

PostScriptファイルをPDF形式に変換するために、Aspose.PDF for .NETは[PsLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/psloadoptions)クラスを提供しています。このクラスはLoadOptionsオブジェクトの初期化に使用されます。後に、このオブジェクトはDocumentオブジェクトコンストラクタに引数として渡すことができ、PDFレンダリングエンジンがソースドキュメントの形式を判別するのに役立ちます。

以下のコードスニペットを使用して、Aspose.PDF for .NETでPostScriptファイルをPDF形式に変換できます：

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string _dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// PsLoadOptionsの新しいインスタンスを作成
PsLoadOptions options = new PsLoadOptions();
// 作成したロードオプションで.psドキュメントを開く
Document pdfDocument = new Document(_dataDir + "input.ps", options);
// ドキュメントを保存
pdfDocument.Save(dataDir + "PSToPDF.pdf");
```
変換中に使用されるフォントフォルダのセットを設定することもできます：

```csharp
public static void ConvertPostscriptToPDFAvdanced()
{
    PsLoadOptions options = new PsLoadOptions
    {
        FontsFolders = new [] { @"c:\tmp\fonts1", @"c:\tmp\fonts2"}
    };
    Document pdfDocument = new Document(_dataDir + "input.ps", options);
    pdfDocument.Save(_dataDir + "ps_test.pdf");
}
```

## XMLをPDFに変換する

XML形式は構造化データを保存するために使用されます。Aspose.PDFでXMLをPDFに変換する方法はいくつかあります：

1. XSLTを使用して任意のXMLデータをHTMLに変換し、以下に記述されているようにHTMLをPDFに変換する
1. Aspose.PDF XSDスキーマを使用してXMLドキュメントを生成する
1. XSL-FO標準に基づいたXMLドキュメントを使用する

{{% alert color="success" %}}
**オンラインでXMLをPDFに変換してみる**

Aspose.PDF for .NETは、無料のオンラインアプリケーション["XML to PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf)を提供しています。ここで機能や品質を試すことができます。
Aspose.PDF for .NETは、無料のオンラインアプリケーション ["XML to PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf)を提供しており、その機能と品質を試すことができます。

[![Aspose.PDF Convertion XML to PDF with Free App](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
{{% /alert %}}

## XSL-FOをPDFに変換

XSL-FOファイルをPDFに変換するには、従来のAspose.PDF技術を使用して[Document](https://reference.aspose.com/page/net/aspose.page/document)オブジェクトを[XslFoLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/xslfoloadoptions)とともにインスタンス化します。しかし、ファイル構造が正しくない場合があります。この場合、XSL-FOコンバーターではエラー処理戦略を設定することができます。`ThrowExceptionImmediately`, `TryIgnore`, または `InvokeCustomHandler`を選択できます。

```csharp
public static void Convert_XSLFO_to_PDF()
{
    // XslFoLoadOptionオブジェクトをインスタンス化
    var options = new XslFoLoadOptions(".\\samples\\employees.xslt");
    // エラー処理戦略を設定
    options.ParsingErrorsHandlingType = XslFoLoadOptions.ParsingErrorsHandlingTypes.ThrowExceptionImmediately;
    // Documentオブジェクトを作成
    var pdfDocument = new Aspose.Pdf.Document(".\\samples\\employees.xml", options);
    pdfDocument.Save(_dataDir + "data_xml.pdf");
}
```
## LaTeX/TeXをPDFに変換する

LaTeXファイル形式は、TeXファミリーの言語の派生形式であるLaTeXをマークアップとして使用するテキストファイル形式です。LaTeX（ˈleɪtɛk/lay-tekまたはlah-tek）は、ドキュメント作成システムおよびドキュメントマークアップ言語です。これは、数学、物理学、コンピュータ科学を含む多くの分野で科学文書のコミュニケーションと出版に広く使用されています。また、サンスクリット語やアラビア語などの複雑な多言語資料を含む書籍や記事の準備と出版においても重要な役割を果たしています。LaTeXは、その出力をフォーマットするためにTeX組版プログラムを使用し、自身がTeXマクロ言語で書かれています。

{{% alert color="success" %}}
**オンラインでLaTeX/TeXをPDFに変換してみる**

Aspose.PDF for .NETは、無料のアプリケーション["LaTex to PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf)を提供しています。ここで機能と品質を試すことができます。

[![Aspose.PDF Convertion LaTeX/TeX to PDF with Free App](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
[![Aspose.PDF Convertion LaTeX/TeX to PDF with Free App](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}

Aspose.PDF for .NETはTeXファイルをPDF形式に変換する機能をサポートしています。この要件を達成するために、Aspose.Pdf名前空間には[LatexLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/latexloadoptions)というクラスがあり、LaTexファイルを読み込み、[Document class](https://reference.aspose.com/pdf/net/aspose.pdf/document)を使用してPDF形式で出力をレンダリングする機能を提供します。
次のコードスニペットは、C#でLaTexファイルをPDF形式に変換するプロセスを示しています。

```csharp
public static void ConvertTeXtoPDF()
{
    // Latex Loadオプションオブジェクトをインスタンス化
    TeXLoadOptions options = new TeXLoadOptions();
    // Documentオブジェクトを作成
    Aspose.Pdf.Document pdfDocument= new Aspose.Pdf.Document(_dataDir + "samplefile.tex", options);
    // 出力をPDFファイルに保存
    pdfDocument.Save(_dataDir + "TeXToPDF_out.pdf");
}
```
