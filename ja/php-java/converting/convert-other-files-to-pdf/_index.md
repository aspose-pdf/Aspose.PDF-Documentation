---
title: 様々なファイル形式をPDFに変換 
linktitle: 他のファイル形式をPDFに変換 
type: docs
weight: 80
url: /ja/php-java/convert-other-files-to-pdf/
lastmod: "2024-05-20"
description: このトピックでは、Aspose.PDFが他のファイル形式をPDFドキュメントに変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## EPUBをPDFに変換

**Aspose.PDF for PHP**は、EPUBファイルをPDF形式に簡単に変換することができます。

<abbr title="electronic publication">EPUB</abbr> は、国際電子出版フォーラム（IDPF）からの無料でオープンな電子書籍標準です。ファイルは拡張子.epubを持っています。EPUBは再フロー可能なコンテンツ用に設計されており、EPUBリーダーは特定の表示デバイスに最適化されたテキストを表示することができます。

EPUBファイルをPDF形式に変換するために、Aspose.PDF for PHPには[EpubLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/EpubLoadOptions)というクラスがあり、これを使用して元のEPUBファイルを読み込みます。
 その後、オブジェクトは[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)オブジェクト初期化の引数として渡されます。これはPDFレンダリングエンジンがソースドキュメントの入力フォーマットを決定するのに役立ちます。

以下のコードスニペットは、EPUBファイルをPDF形式に変換するプロセスを示しています。

1. EPUB [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/epubloadoptions/)を作成します。
1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document)オブジェクトを初期化します。
1. 出力PDFドキュメントを保存します。

```php
// EpubLoadOptionsの新しいインスタンスを作成
$loadOption = new EpubLoadOptions();

// 新しいDocumentオブジェクトを作成し、EPUBファイルをロード
$document = new Document($inputFile, $loadOption);

// ドキュメントをPDFファイルとして保存
$document->save($outputFile);
```

{{% alert color="success" %}}
**EPUBをPDFにオンラインで変換してみてください**

Aspose.PDF for PHPは、機能と品質を調査するためのオンライン無料アプリケーション["EPUB to PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf)を提供しています。
[![Aspose.PDF Convertion EPUB to PDF with Free App](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

## MarkdownをPDFに変換

{{% alert color="success" %}}
**MarkdownをPDFにオンラインで変換してみてください**

Aspose.PDF for PHPは、オンライン無料アプリケーション["Markdown to PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf)を提供しており、その機能と品質を試すことができます。

[![Aspose.PDF Convertion Markdown to PDF with Free App](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

Markdownは、ウェブ著者のためのテキストからHTMLへの変換ツールです。Markdownを使用すると、読み書きしやすいプレーンテキスト形式で書き、それを構造的に有効なXHTML（またはHTML）に変換することができます。

以下のコードスニペットは、Aspose.PDF for PHPでこの機能を使用する方法を示しています：

```php
// MdLoadOptions の新しいインスタンスを作成
$loadOption = new MdLoadOptions();

// Document の新しいインスタンスを作成し、入力Markdownファイルをロード
$document = new Document($inputFile, $loadOption);

// ドキュメントをPDFファイルとして保存
$document->save($outputFile);
```


## PCLをPDFに変換

<abbr title="Printer Command Language">PCL</abbr>（プリンターコマンド言語）は、標準的なプリンターの機能にアクセスするために開発されたヒューレット・パッカードのプリンター言語です。PCLレベル1から5e/5cは、受信順に処理および解釈される制御シーケンスを使用するコマンドベースの言語です。消費者レベルでは、PCLデータストリームはプリントドライバーによって生成されます。PCL出力はカスタムアプリケーションによっても簡単に生成できます。

{{% alert color="success" %}}
**PCLからPDFへの変換をオンラインで試してみてください**

Aspose.PDF for PHPは、オンラインで無料のアプリケーション["PCL to PDF"](https://products.aspose.app/pdf/conversion/pcl-to-pdf)を提供しており、その機能と品質を調査することができます。

[![Aspose.PDF Convertion PCL to PDF with Free App](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

**現在、PCL5およびそれ以前のバージョンのみサポートされています。**

|**コマンドセット**|**サポート**|**例外**|**説明**|

| :- | :- | :- | :- |
|ジョブ制御コマンド|+|両面印刷モード|印刷プロセスを制御: コピー数、出力ビン、片面/両面印刷、左と上のオフセットなど。|
|ページ制御コマンド|+|改ページスキップコマンド|ページサイズ、余白、ページの向き、行間隔、文字間隔などを指定します。|
|カーソル位置決めコマンド|+| |カーソル位置を指定し、それによりテキスト、ラスタまたはベクター画像の原点と詳細を指定します。|

|フォント選択コマンド|+|<p>1. トランスペアレント印刷データコマンド。</p><p>2. 埋め込みソフトフォント。現在のバージョンでは、ソフトフォントを作成する代わりに、ライブラリがターゲットマシンにインストールされている既存の「ハード」TrueTypeフォントから適切なフォントを選択します。<br>   適合性は幅/高さの比率によって定義されます。<br>   この機能はビットマップフォントとTrueTypeフォントにのみ対応しており、ソフトフォントで印刷されたテキストがソースファイルのものと一致することを保証しません。<br>   ソフトフォントの文字コードがデフォルトのものと一致しない場合があります。</p><p>3. ユーザー定義のシンボルセット。</p>|PCLファイルからソフト（埋め込み）フォントをロードし、メモリ内で管理することを許可します。|
|ラスターグラフィックスコマンド|+|白黒のみ|PCLファイルからラスター画像をメモリにロードし、幅、高さ、圧縮タイプ、解像度などのラスターのパラメータを指定します。|
|カラーコマンド|+| |すべての印刷可能オブジェクトに色付けを許可します。|
|プリントモデルコマンド|+| |テキスト、ラスター画像、および長方形の領域をラスターの事前定義およびユーザー定義のパターンで塗りつぶすことを許可し、パターンおよびソースラスター画像の透過モードを指定します。
 <br>定義済みパターンは、ハッチング、クロスハッチ、シェーディングのものです。|
|長方形エリア塗りつぶしコマンド|+| |パターンで長方形エリアを作成し、塗りつぶすことを可能にします。|
|HP-GL/2ベクトルグラフィックスコマンド|+|スクリーンベクトルコマンド(SV)、透過モードコマンド(TR)、透過データコマンド(TD)、RO(座標系の回転)、スケーラブルまたはビットマップフォントコマンド(SB)、文字傾斜コマンド(SL)および余分なスペース(ES)は実装されておらず、DV(変数テキストパス定義)コマンドはベータ版で実現されています。|<p>- PCLファイルからHP-GL/2ベクトル画像をメモリにロードすることを可能にします。 Vector imageは印刷可能なエリアの左下隅を原点とし、スケーリング、移動、回転、クリッピングが可能です。</p><p>- ベクター画像には、ラベルとしてのテキストや、四角形、円、楕円、線、弧、ベジェ曲線、基本的なものから構成された複雑な図形などの幾何学的な図形を含めることができます。</p><p>- ラベルの文字を含む閉じた図形は、ソリッドフィルまたはベクターパターンで塗りつぶすことができます。</p><p>- パターンには、ハッチング、クロスハッチ、シェーディング、ラスターユーザー定義、PCLハッチングまたはクロスハッチ、PCLユーザー定義があります。PCLパターンはラスタです。ラベルは個別に回転、スケーリングが可能で、上下左右の4方向に向けられます。左右の方向は、文字を一つずつ配置します。上下の方向は、文字を一つずつ下に配置します。</p>|
|Macross|―| |PCLコマンドのシーケンスをメモリにロードし、このシーケンスを何度も使用することができます。たとえば、ページヘッダを印刷したり、ページセットに対するフォーマットを設定したりするためです。|
|Unicode text|―| |非ASCII文字の印刷を可能にします。 サンプルファイルの不足により未実装<br>Unicodeテキスト|

|PCL6 (PCL-XL)| |テストファイルが不足しているため、ベータ版でのみ実現されています。埋め込みフォントもサポートされていません。JetReady拡張はJetReady仕様を持つことが不可能なためサポートされていません。|バイナリファイル形式。|

### PCLファイルをPDF形式に変換する

PCLからPDFへの変換を可能にするために、[Aspose.PDF for PHP](https://products.aspose.com/pdf/php-java)には、[PclLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PclLoadOptions)クラスがあります。このクラスは[LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions)オブジェクトを初期化するために使用されます。このオブジェクトは[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)オブジェクトの初期化時に引数として渡され、PDFレンダリングエンジンがソースドキュメントの入力形式を決定するのを助けます。

以下のコードスニペットは、PCLファイルをPDF形式に変換するプロセスを示しています。

```php
// PclLoadOptionsの新しいインスタンスを作成
$loadOption = new PclLoadOptions();

// Documentの新しいインスタンスを作成し、PCLファイルをロード
$document = new Document($inputFile, $loadOption);

// ドキュメントをPDFファイルとして保存
$document->save($outputFile);
```

### 既知の問題

1. テキスト文字列と画像の起点は、印刷方向が0ºでない場合、元のPCLファイルのものとわずかに異なる場合があります。ベクトル画像についても、ベクトルプロットの座標系が回転している場合（ROコマンドが前置されている場合）に同様です。
2. ベクトル画像内のラベルの起点は、以下のコマンドシーケンスの影響を受ける場合、元のPCLファイルのものと異なる場合があります：ラベルの起点（LO）、変数テキストパスの定義（DV）、絶対方向（DI）または相対方向（DR）。
3. テキストがビットマップまたはTrueTypeのソフト（埋め込み）フォントでレンダリングされなければならない場合、それが正しく読み取れないことがあります。現在、これらのフォントは部分的にしかサポートされていないためです（「サポートされている機能の表」の例外を参照）。この状況では、ソフトフォントの文字コードがデフォルトのものに対応する場合にのみ、テキストが正しく読み取れます。また、読み取られたテキストのスタイルは、ソフトフォントヘッダーでスタイルを設定する必要がないため、元のPCLファイルのものと異なる場合があります。

1. 解析されたPCLファイルにIntellifontまたはUniversalソフトフォントが含まれている場合、例外がスローされます。なぜなら、IntellifontおよびUniversalフォントはまったくサポートされていないからです。
1. 解析されたPCLファイルにマクロコマンドが含まれている場合、マクロコマンドはサポートされていないため、解析の結果は元のファイルと大きく異なります。

## テキストをPDFに変換

**Aspose.PDF for PHP**は、テキストファイルをPDF形式に変換する機能を提供します。この記事では、Aspose.PDFを使用してテキストファイルをどのように簡単かつ効率的にPDFに変換できるかを示します。
{{% alert color="success" %}}

テキストファイルをPDFに変換する必要がある場合、最初にリーダーでソーステキストファイルを読み込みます。テキストファイルの内容を読むためにStringBuilderを使用しました。Documentオブジェクトをインスタンス化し、Pagesコレクションに新しいページを追加します。TextFragmentの新しいオブジェクトを作成し、そのコンストラクタにStringBuilderオブジェクトを渡します。TextFragmentオブジェクトを使用してParagraphsコレクションに新しい段落を追加し、DocumentクラスのSaveメソッドを使用して結果のPDFファイルを保存します。
**テキストをPDFにオンラインで変換しよう**

Aspose.PDF for PHPは、オンラインで無料のアプリケーション["Text to PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf)を提供しており、その機能性と品質を調査することができます。

[![Aspose.PDFテキストからPDFへの変換無料アプリ](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

### プレーンテキストファイルをPDFに変換

```php
// 新しいDocumentオブジェクトを作成します。
$document = new Document();

// ドキュメントに新しいページを追加します。
$page = $document->getPages()->add();

// 入力テキストファイルの内容を読み込みます。
$text = file_get_contents($inputFile);

// 新しいFontRepositoryオブジェクトを作成します。
$fontRepository = new FontRepository();

// リポジトリで"Courier"フォントを探します。
$font = $fontRepository->findFont("Courier");

// 入力テキストで新しいTextFragmentオブジェクトを作成します。
$textFragment = new TextFragment($text);

// テキストフラグメントのフォントを"Courier"に設定します。
$textFragment->getTextState()->setFont($font);

// ページにテキストフラグメントを追加します。
$page->getParagraphs()->add($textFragment);

// ドキュメントを出力ファイルに保存します。
$document->save($outputFile);
```


## XPSをPDFに変換

**Aspose.PDF for PHP**は、<abbr title="XML Paper Specification">XPS</abbr>ファイルをPDF形式に変換する機能をサポートしています。この記事をチェックして、タスクを解決してください。

XPS、XML Paper Specificationは、ドキュメント作成と閲覧をWindowsに統合するために使用されるMicrosoftのファイル形式です。Aspose.PDF for PHPを使用すると、Adobeのポータブルファイル形式であるPDFにXPSファイルを変換することが可能です。

このファイル形式は基本的に圧縮されたXMLファイルであり、主に配布と保存に使用されます。編集が非常に困難で、主にMicrosoftによって実装されています。

[Aspose.PDF for PHP](https://products.aspose.com/pdf/php-java)を使用してXPSファイルをPDFに変換するには、[XpsLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XpsLoadOptions)クラスを使用します。
 これは、[LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions) オブジェクトを初期化するために使用されます。その後、このオブジェクトは [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) オブジェクトの初期化時に引数として渡され、PDF レンダリングエンジンがソースドキュメントの入力形式を決定するのに役立ちます。

次のコードスニペットは、XPS ファイルを PDF 形式に変換するプロセスを示しています。

```php
// XpsLoadOptions クラスの新しいインスタンスを作成
$loadOption = new XpsLoadOptions();

// Document クラスの新しいインスタンスを作成し、XPS ファイルをロード
$document = new Document($inputFile, $loadOption);

// ドキュメントを PDF ファイルとして保存
$document->save($outputFile);
```

{{% alert color="success" %}}
**XPS 形式を PDF にオンラインで変換してみてください**

Aspose.PDF for PHP では、オンラインで無料アプリケーション ["XPS to PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/) を提供しており、機能と品質を調査することができます。


[![Aspose.PDF Convertion XPS to PDF with Free App](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/){{% /alert %}}

## PostScriptをPDFに変換

**Aspose.PDF for PHP**は、PostScriptファイルをPDF形式に変換する機能をサポートしています。Aspose.PDFの機能の1つとして、変換中に使用するフォントフォルダのセットを設定することができます。

PostScriptファイルをPDF形式に変換するために、Aspose.PDF for PHPは[PsLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PsLoadOptions)クラスを提供しており、これはLoadOptionsオブジェクトを初期化するために使用されます。このオブジェクトは後でDocumentオブジェクトのコンストラクタに引数として渡すことができ、これによりPDFレンダリングエンジンはソースドキュメントの形式を判断するのに役立ちます。

以下のコードスニペットは、PostScriptファイルをPDF形式に変換するために使用できます：

```php
// 新しいPsLoadOptionsオブジェクトを作成します。
$loadOption = new PsLoadOptions();

// 新しいDocumentオブジェクトを作成し、入力PSファイルを読み込みます。
$document = new Document($inputFile, $loadOption);

// ドキュメントをPDFファイルとして保存します。
$document->save($outputFile);
```

## XMLをPDFに変換

XML形式は、構造化データを保存するために使用されます。
 いくつかの方法で<abbr title="Extensible Markup Language">XML</abbr>をAspose.PDFでPDFに変換することができます。

{{% alert color="success" %}}
**オンラインでXMLをPDFに変換してみてください**

Aspose.PDF for PHPは、オンラインで無料アプリケーション["XML to PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf)を提供しており、その機能と品質を調査することができます。

[![Aspose.PDF Convertion XML to PDF with Free App](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
{{% /alert %}}

XSL-FO標準に基づいたXMLドキュメントを使用するオプションを考慮してください。

### XSL-FOをPDFに変換

XSL-FOファイルをPDFに変換するには、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document)オブジェクトと[XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions)を使用して実装することができます。

```php
// サンプルファイルのパスを設定
$dataDir = getcwd() . DIRECTORY_SEPARATOR . "samples";
$inputFoFile = $dataDir . DIRECTORY_SEPARATOR . "sample.xslt";
$inputFile = $dataDir . DIRECTORY_SEPARATOR . "sample.xml";
$outputFile = $dataDir . DIRECTORY_SEPARATOR . "results" . DIRECTORY_SEPARATOR . 'result-xmlfo-to-pdf.pdf';

// XslFoLoadOptionsクラスの新しいインスタンスを作成し、入力XSL-FOファイルのパスを渡す
$loadOption = new XslFoLoadOptions($inputFoFile);

// Documentクラスの新しいインスタンスを作成し、入力XMLファイルとXSL-FOロードオプションを渡す
$document = new Document($inputFile, $loadOption);

// 変換されたPDFドキュメントを出力ファイルパスに保存
$document->save($outputFile);
```

## LaTeX/TeXをPDFに変換

LaTeXファイル形式は、LaTeX派生のTeX言語ファミリーのマークアップを含むテキストファイル形式であり、LaTeXはTeXシステムの派生形式です。LaTeX（ˈleɪtɛk/ レイテックまたはラーテック）は、文書作成システムおよび文書マークアップ言語です。これは、数学、物理学、コンピュータ科学を含む多くの分野で、科学文書のコミュニケーションおよび出版に広く使用されています。また、サンスクリット語やアラビア語を含む複雑な多言語資料を含む本や記事の作成および出版においても重要な役割を果たしています。LaTeXは、その出力をフォーマットするためにTeX組版プログラムを使用し、それ自体はTeXマクロ言語で書かれています。

**Aspose.PDF for PHP**は、TeXファイルをPDF形式に変換する機能をサポートしており、この要件を達成するために、com.aspose.pdfパッケージには、LaTexファイルをロードし、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)クラスを使用して出力をPDF形式でレンダリングする機能を提供するクラス[LatexLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LatexLoadOptions)が含まれています。
 以下のコードスニペットは、LaTexファイルをPDF形式に変換するプロセスを示しています。

```php
// LatexLoadOptionsクラスの新しいインスタンスを作成します
$loadOption = new LatexLoadOptions();

// Documentクラスの新しいインスタンスを作成し、TeXLoadOptionsを使用してTeXファイルを読み込みます
$document = new Document($inputFile, $loadOption);

// ドキュメントをPDFファイルとして保存します
$document->save($outputFile);
```

{{% alert color="success" %}}
**LaTeX/TeXをPDFにオンラインで変換してみてください**

Aspose.PDF for PHPは、オンラインの無料アプリケーション「[LaTex to PDF](https://products.aspose.app/pdf/conversion/tex-to-pdf)」を提供しており、その機能と品質を調査することができます。

[![Aspose.PDF Convertion LaTeX/TeX to PDF with Free App](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}