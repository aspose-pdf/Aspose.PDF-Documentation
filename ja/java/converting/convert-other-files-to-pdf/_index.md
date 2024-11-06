---
title: 様々なファイル形式をPDFに変換する
linktitle: 他のファイル形式をPDFに変換する
type: docs
weight: 80
url: ja/java/convert-other-files-to-pdf/
lastmod: "2021-11-19"
description: このトピックでは、Aspose.PDFが他のファイル形式をPDFドキュメントに変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## EPUBをPDFに変換する

**Aspose.PDF for Java**は、EPUBファイルを簡単にPDF形式に変換することができます。

<abbr title="電子出版">EPUB</abbr>（電子出版の略）は、International Digital Publishing Forum (IDPF)による無料でオープンな電子書籍標準です。ファイルは拡張子.epubを持っています。EPUBはリフロー可能なコンテンツ向けに設計されており、EPUBリーダーは特定のディスプレイデバイスに最適化したテキストを表示することができます。

EPUBファイルをPDF形式に変換するには、Aspose.PDF for Javaには[EpubLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/EpubLoadOptions)というクラスがあり、これを使用してソースのEPUBファイルを読み込みます。
 その後、オブジェクトは[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)オブジェクトの初期化に引数として渡されます。これは、PDFレンダリングエンジンがソースドキュメントの入力形式を判断するのに役立ちます。

以下のコードスニペットは、EPUBファイルをPDF形式に変換するプロセスを示しています。

1. EPUB[`LoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/loadoptions)を作成します。
1. [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document)オブジェクトを初期化します。
1. 出力PDFドキュメントを保存します。

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertEPUBtoPDF {

    private ConvertEPUBtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // EPUB LoadOptionsを作成します
        EpubLoadOptions options = new EpubLoadOptions();

        // ドキュメントオブジェクトを初期化します
        String epubFileName = Paths.get(_dataDir.toString(), "aliceDynamic.epub").toString();
        Document document = new Document(epubFileName, options);

        // 出力PDFドキュメントを保存します
        document.save(Paths.get(_dataDir.toString(),"EPUBtoPDF.pdf").toString());
    }
}
```

{{% alert color="success" %}}
**EPUBをPDFにオンラインで変換してみてください**

Aspose.PDF for Javaは、オンラインで無料のアプリケーション["EPUB to PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf)を提供しており、その機能と品質を試すことができます。

[![Aspose.PDF 変換 EPUB to PDF 無料アプリ](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

## MarkdownをPDFに変換

**この機能はバージョン19.6以上でサポートされています。**

{{% alert color="success" %}}
**MarkdownをPDFにオンラインで変換してみてください**

Aspose.PDF for Javaは、オンラインで無料のアプリケーション["Markdown to PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf)を提供しており、その機能と品質を試すことができます。

[![Aspose.PDF 変換 Markdown to PDF 無料アプリ](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

Markdownはウェブ著者のためのテキストからHTMLへの変換ツールです。
 Markdownは、読みやすく書きやすいプレーンテキスト形式で記述し、それを構造的に有効なXHTML（またはHTML）に変換することができます。

次のコードスニペットは、Aspose.PDF for Javaを使用してこの機能を利用する方法を示しています：

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertMDtoPDF {

    private ConvertMDtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // Latexロードオプションオブジェクトをインスタンス化
        MdLoadOptions options = new MdLoadOptions();
        
        // Documentオブジェクトを作成
        String markdownFileName = Paths.get(_dataDir.toString(), "samplefile.md").toString();
        Document document = new Document(markdownFileName, options);

        // 出力PDFドキュメントを保存
        document.save(Paths.get(_dataDir.toString(),"MarkdownToPDF.pdf").toString());
    }
}

```

## Convert PCL to PDF

<abbr title="Printer Command Language">PCL</abbr>（プリンターコマンド言語）は、標準的なプリンターの機能にアクセスするために開発されたヒューレット・パッカードのプリンター言語です。PCL レベル 1 から 5e/5c までは、受信した順に処理および解釈される制御シーケンスを使用するコマンドベースの言語です。消費者レベルでは、PCL データストリームはプリンタードライバーによって生成されます。PCL 出力はカスタムアプリケーションによっても簡単に生成できます。

{{% alert color="success" %}}
**PCL から PDF へのオンライン変換を試してみてください**

Aspose.PDF for Java は、「[PCL to PDF](https://products.aspose.app/pdf/conversion/pcl-to-pdf)」という無料のオンラインアプリケーションを提供しており、その機能と品質を調査することができます。

[![Aspose.PDF Convertion PCL to PDF with Free App](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

**現在、PCL5およびそれ以前のバージョンのみがサポートされています。**

|**コマンドセット**|**サポート**|**例外**|**説明**|

| :- | :- | :- | :- |
|ジョブ制御コマンド|+|両面印刷モード|印刷プロセスを制御: コピーの数、出力ビン、片面/両面印刷、左と上のオフセットなど。|
|ページ制御コマンド|+|ミシン目スキップコマンド|ページのサイズ、余白、ページの向き、行間、文字間の距離などを指定します。|
|カーソル位置指定コマンド|+| |カーソル位置を指定し、それによりテキスト、ラスターまたはベクター画像の起点と詳細を指定します。|

|フォント選択コマンド|+|<p>1. 透過印刷データコマンド。</p><p>2. 埋め込みソフトフォント。現在のバージョンでは、ソフトフォントを作成する代わりに、ライブラリはターゲットマシンにインストールされている既存の「ハード」TrueTypeフォントから適切なフォントを選択します。<br>   適合性は幅/高さの比率によって定義されます。<br>   この機能はビットマップフォントとTrueTypeフォントでのみ機能し、ソフトフォントで印刷されたテキストがソースファイルのものと関連することを保証しません。<br>   ソフトフォント内の文字コードがデフォルトのものと一致しない可能性があるためです。</p><p>3. ユーザー定義のシンボルセット。</p>|PCLファイルからソフト（埋め込み）フォントを読み込み、メモリ内で管理することを許可します。|
|ラスタグラフィックコマンド|+|白黒のみ|PCLファイルからメモリにラスタ画像を読み込み、幅、高さ、圧縮タイプ、解像度などのラスタパラメータを指定します。|
|カラーコマンド|+| |すべての印刷可能なオブジェクトに色付けを許可します。|
|印刷モデルコマンド|+| |テキスト、ラスタ画像、矩形領域をラスタの事前定義およびユーザー定義のパターンで塗りつぶし、パターンとソースラスタ画像の透明モードを指定することを許可します。
 <br>定義済みパターンには、ハッチング、クロスハッチ、およびシェーディングのものがあります。|
|長方形の領域塗りつぶしコマンド|+| |パターンを使用して長方形の領域を作成および塗りつぶすことを可能にします。|
|HP-GL/2 ベクターグラフィックスコマンド|+|スクリーンベクターコマンド (SV)、透過モードコマンド (TR)、透過データコマンド (TD)、RO (座標系の回転)、スケーラブルまたはビットマップフォントコマンド (SB)、文字の傾斜コマンド (SL)、および余白 (ES) は実装されておらず、DV (可変テキストパスの定義) コマンドはベータ版で実現されています。|<p>- PCLファイルからメモリにHP-GL/2ベクター画像をロードすることを可能にします。 ベクター画像は、印刷可能エリアの左下隅を原点としており、スケーリング、平行移動、回転、クリッピングが可能です。</p><p>- ベクター画像は、ラベルとしてのテキストや、長方形、円、楕円、線、弧、ベジエ曲線、そして単純なものから構成された複雑な図形などの幾何学的な図形を含むことができます。</p><p>- ラベルの文字を含む閉じた図形は、単色の塗りつぶしやベクターパターンで塗りつぶすことができます。</p><p>- パターンには、ハッチング、クロスハッチング、シェーディング、ユーザー定義のラスターハッチング、PCLハッチングまたはクロスハッチング、PCLユーザー定義のものがあります。PCLパターンはラスタ形式です。ラベルは個別に回転、スケーリングが可能で、上、下、左、右の四方向に配置できます。左と右の方向は文字が次々に並ぶ配置を含み、上と下の方向は文字が上下に並ぶ配置を含みます。</p>

|Macross|―| |PCLコマンドのシーケンスをメモリにロードし、このシーケンスを何度も使用することを許可します。例えば、ページヘッダーを印刷するためや、一連のページに対して1つのフォーマットを設定するために使用します。|

|Unicode text|―| |非ASCII文字を印刷することを許可します。 未実装、<br>Unicodeテキストを含むサンプルファイルの不足のため|
|PCL6 (PCL-XL)| |テストファイルの不足のため、ベータ版でのみ実現されています。埋め込みフォントもサポートされていません。JetReady拡張はJetReady仕様を持つことが不可能であるためサポートされていません。|バイナリファイル形式。|

### PCLファイルをPDF形式に変換

PCLからPDFへの変換を可能にするために、[Aspose.PDF for Java](https://products.aspose.com/pdf/java)には[PclLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PclLoadOptions)クラスがあり、これは[LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions)オブジェクトを初期化するために使用されます。このオブジェクトは、その後、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)オブジェクトの初期化時に引数として渡され、PDFレンダリングエンジンがソースドキュメントの入力形式を決定するのに役立ちます。

以下のコードスニペットは、PCLファイルをPDF形式に変換するプロセスを示しています。

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertPCLtoPDF {

    private ConvertPCLtoPDF() {
        
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {        
        ConvertPCLtoPDF_Simple();
        ConvertPCLtoPDF_Advanced();
    }

    public static void ConvertPCLtoPDF_Simple() {
        PclLoadOptions options = new PclLoadOptions();
        Document pdfDocument= new Document(_dataDir + "demo.pcl", options);
        pdfDocument.save(_dataDir + "epub_test.pdf");        
    }

    public static void ConvertPCLtoPDF_Advanced() {
        PclLoadOptions options = new PclLoadOptions();
        options.SupressErrors=true;
        Document pdfDocument= new Document(_dataDir + "demo.pcl", options);
        if (options.Exceptions!=null)
            for (Exception ex : options.Exceptions)
            {
                System.out.println(ex.getMessage());
            }
        pdfDocument.save(_dataDir + "pcl_test.pdf");        
    }
}
```

### Known Issues

1. テキスト文字列と画像の起点が、印刷方向が0ºでない場合、元のPCLファイルとはわずかに異なることがあります。ベクトル画像に関しても、ベクトルプロットの座標系が回転している場合（ROコマンドが先行する場合）、同様のことが言えます。
2. ベクトル画像内のラベルの起点が、次のコマンド列によって影響を受ける場合、元のPCLファイルとは異なることがあります：ラベル起点（LO）、変数テキストパスの定義（DV）、絶対方向（DI）、または相対方向（DR）。
3. ビットマップまたはTrueTypeのソフト（埋め込み）フォントでレンダリングされる必要があるテキストは、誤って読み取られることがあります。これは、現在これらのフォントが部分的にしかサポートされていないためです（「サポートされている機能の表」で例外を参照）。この状況では、ソフトフォント内の文字コードがデフォルトのものと一致する場合にのみ、テキストを正しく読み取ることができます。読み取られたテキストのスタイルも、ソフトフォントヘッダーでスタイルを設定する必要がないため、元のPCLファイルとは異なることがあります。

1. 解析されたPCLファイルにIntellifontまたはUniversalソフトフォントが含まれている場合、IntellifontおよびUniversalフォントはまったくサポートされていないため、例外がスローされます。
1. 解析されたPCLファイルにマクロコマンドが含まれている場合、マクロコマンドはサポートされていないため、解析の結果はソースファイルと大きく異なります。

## テキストをPDFに変換

**Aspose.PDF for Java** は、テキストファイルをPDF形式に変換する機能を提供します。この記事では、Aspose.PDFを使用してテキストファイルをどのように簡単かつ効率的にPDFに変換するかを示します。

テキストファイルをPDFに変換する必要がある場合、最初にリーダーでソーステキストファイルを読み込みます。テキストファイルの内容を読み込むためにStringBuilderを使用しました。Documentオブジェクトをインスタンス化し、Pagesコレクションに新しいページを追加します。TextFragmentの新しいオブジェクトを作成し、そのコンストラクターにStringBuilderオブジェクトを渡します。TextFragmentオブジェクトを使用してParagraphsコレクションに新しい段落を追加し、DocumentクラスのSaveメソッドを使用して生成されたPDFファイルを保存します。

{{% alert color="success" %}}
**オンラインでテキストをPDFに変換する**

Aspose.PDF for Java は、無料のオンラインアプリケーション["Text to PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf)を提供しており、その機能と品質を調査することができます。

[![Aspose.PDF テキストをPDFに変換する無料アプリ](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

### プレーンテキストファイルをPDFに変換する

```java
package com.aspose.pdf.examples;
/**
 * TXTをPDFに変換する
 */

import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertTextToPDF {

    private ConvertTextToPDF() {
    }

    final static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");
    final static Charset ENCODING = StandardCharsets.UTF_8;

    public static void main(String[] args) throws IOException {
        ConvertTXT_to_PDF_Simple();
    }

    public static void ConvertTXT_to_PDF_Simple() throws IOException {
        // ドキュメントオブジェクトを初期化する

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();
        Path txtDocumentFileName = Paths.get(_dataDir.toString(), "rfc822.txt");

        // 空のコンストラクタを呼び出してDocumentオブジェクトをインスタンス化する
        Document pdfDocument = new Document();

        // ドキュメントのPagesコレクションに新しいページを追加する
        Page page = pdfDocument.getPages().add();

        // TextFragmentのインスタンスを作成し、リーダーオブジェクトからのテキストを
        // 引数としてそのコンストラクタに渡す
        TextFragment text = new TextFragment(Files.readString(txtDocumentFileName, ENCODING));

        // 段落コレクションに新しいテキスト段落を追加し、TextFragmentオブジェクトを渡す
        page.getParagraphs().add(text);

        // 結果のPDFファイルを保存する
        pdfDocument.save(pdfDocumentFileName);
    }
```


### 事前フォーマットされたテキストファイルをPDFに変換する

```java
    public static void ConvertPreFormattedTextToPdf() throws IOException {

        Path txtDocumentFileName = Paths.get(_dataDir.toString(), "rfc822.txt");
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();

        // テキストファイルを文字列の配列として読み込む
        java.util.List<String> lines = Files.readAllLines(txtDocumentFileName, ENCODING);

        // 空のコンストラクタを呼び出してDocumentオブジェクトをインスタンス化する
        Document pdfDocument = new Document();

        // DocumentのPagesコレクションに新しいページを追加する
        Page page = pdfDocument.getPages().add();

        // より良いプレゼンテーションのために左と右のマージンを設定する
        page.getPageInfo().getMargin().setLeft(20);
        page.getPageInfo().getMargin().setRight(10);
        page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
        page.getPageInfo().getDefaultTextState().setFontSize(12);

        for (String line : lines) {
            // 行が「改ページ」文字を含んでいるか確認する
            // https://en.wikipedia.org/wiki/Page_breakを参照
            if (line.startsWith("\f")) {
                page = pdfDocument.getPages().add();
                page.getPageInfo().getMargin().setLeft(20);
                page.getPageInfo().getMargin().setRight(10);
                page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
                page.getPageInfo().getDefaultTextState().setFontSize(12);
            } else {
                // TextFragmentのインスタンスを作成し、
                // 引数として行を渡す
                TextFragment text = new TextFragment(line);

                // 新しいテキスト段落を段落コレクションに追加し、TextFragmentオブジェクトを渡す
                page.getParagraphs().add(text);
            }

            pdfDocument.save(pdfDocumentFileName);
        }
    }
}
```


## XPSをPDFに変換する

**Aspose.PDF for Java**は、<abbr title="XML Paper Specification">XPS</abbr>ファイルをPDF形式に変換する機能をサポートしています。タスクを解決するためにこの記事をチェックしてください。

XPS、XML Paper Specificationは、ドキュメントの作成と表示をWindowsに統合するために使用されるMicrosoftのファイル形式です。Aspose.PDF for Javaを使用すると、XPSファイルをAdobeのポータブルファイル形式であるPDFに変換することが可能です。

このファイル形式は基本的に圧縮されたXMLファイルであり、主に配布と保存に使用されます。編集が非常に難しく、主にMicrosoftによって実装されています。

[Aspose.PDF for Java](https://products.aspose.com/pdf/java)を使用してXPSファイルをPDFに変換するには、[XpsLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XpsLoadOptions)クラスを使用します。
 これは[LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions)オブジェクトを初期化するために使用されます。後で、このオブジェクトは[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)オブジェクトの初期化時に引数として渡され、PDFレンダリングエンジンがソースドキュメントの入力形式を決定するのに役立ちます。

XPとWindows 7の両方で、コントロールパネルからプリンターを確認すると、XPSプリンターが事前にインストールされているはずです。XPSファイルを作成するには、そのプリンターを出力デバイスとして使用できます。Windows 7では、ファイルをダブルクリックするだけでXPSビューアーで開くことができるはずです。[XPSビューアー](http://windows.microsoft.com/en-US/windows-vista/what-is-the-xps-viewer)をMicrosoftのウェブサイトからダウンロードすることもできます。

次のコードスニペットは、XPSファイルをPDF形式に変換するプロセスを示しています。

```java
public final class ConvertXPStoPDF {

    private ConvertXPStoPDF() {
    }

    final static Path _dataDir = Paths.get("/home/aspose/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {
        Convert_XSLFO_to_PDF();
    }

    public static void Convert_XSLFO_to_PDF() throws IOException {
        // ドキュメントオブジェクトを初期化

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();
        String xpsDocumentFileName = Paths.get(_dataDir.toString(), "demo.xml").toString();

        // XPSロードオプションを使用してLoadOptionオブジェクトをインスタンス化
        LoadOptions options = new XpsLoadOptions();

        // 空のコンストラクターを呼び出してDocumentオブジェクトをインスタンス化
        Document pdfDocument = new Document(xpsDocumentFileName, options);

        // 結果のPDFファイルを保存
        pdfDocument.save(pdfDocumentFileName);
    }
}
```

{{% alert color="success" %}}
**XPS形式をPDFにオンラインで変換してみてください**

Aspose.PDF for Javaは、オンライン無料アプリケーション["XPS to PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/)を提供しており、そこで機能と品質を調査することができます。

[![Aspose.PDF Convertion XPS to PDF with Free App](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}

## PostScriptをPDFに変換

**Aspose.PDF for Java**は、PostScriptファイルをPDF形式に変換する機能をサポートしています。Aspose.PDFの機能の一つとして、変換中に使用するフォントフォルダのセットを設定することができます。

PostScriptファイルをPDF形式に変換するために、Aspose.PDF for Javaは[PsLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PsLoadOptions)クラスを提供しており、これを使用してLoadOptionsオブジェクトを初期化します。このオブジェクトは後でDocumentオブジェクトのコンストラクタに引数として渡すことができ、これによりPDFレンダリングエンジンがソースドキュメントの形式を判断するのに役立ちます。


PostScriptファイルをPDF形式に変換するために、以下のコードスニペットを使用できます：

```java
public static void ConvertPostScriptToPDF_Simple(){
        // ドキュメントオブジェクトを初期化する

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo.pdf").toString();
        String psDocumentFileName = Paths.get(_dataDir.toString(), "demo.ps").toString();
        PsLoadOptions options = new PsLoadOptions();

        // Documentオブジェクトを作成する
        Document document = new Document(psDocumentFileName, options);

        // 出力PDFドキュメントを保存する
        document.save(pdfDocumentFileName);
    }
```

さらに、変換中に使用されるフォントフォルダのセットを設定できます：

```java
public static void ConvertPostscriptToPDFAvdanced() {
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo.pdf").toString();
        String psDocumentFileName = Paths.get(_dataDir.toString(), "demo.ps").toString();
        PsLoadOptions options = new PsLoadOptions();
        
        options.setFontsFolders(new String[] { "c:\tmp\fonts1", "c:\tmp\fonts2" });

        // Documentオブジェクトを作成する
        Document document = new Document(psDocumentFileName, options);

        // 出力PDFドキュメントを保存する
        document.save(pdfDocumentFileName);
    }
```


## XMLをPDFに変換する

XML形式は構造化データを保存するために使用されます。Aspose.PDFでは、XMLをPDFに変換する方法がいくつかあります。

{{% alert color="success" %}}
**オンラインでXMLをPDFに変換してみる**

Aspose.PDF for Javaは、オンラインで無料のアプリケーション「[XML to PDF](https://products.aspose.app/pdf/conversion/xml-to-pdf)」を提供しており、機能と品質を調査することができます。

[![Aspose.PDF Convertion XML to PDF with Free App](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
{{% /alert %}}

XSL-FO標準に基づくXMLドキュメントを使用するオプションを検討してください。

### XSL-FOをPDFに変換する

XSL-FOファイルのPDFへの変換は、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document)オブジェクトと[XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions)を使用して実装できます。

```java
package com.aspose.pdf.examples;
/**
 * XMLをPDFに変換する
 */

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertXMLtoPDF {

    private ConvertXMLtoPDF() {
    }

    final static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");
    public static void main(String[] args) throws IOException {
        Convert_XSLFO_to_PDF();
        Convert_XSLFO_to_PDF_Adv();
    }

    public static void Convert_XSLFO_to_PDF() throws IOException {
        // ドキュメントオブジェクトを初期化する

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();
        String xmlDocumentFileName = Paths.get(_dataDir.toString(), "demo.xml").toString();
        String xsltDocumentFileName = Paths.get(_dataDir.toString(), "employees.xslt").toString();

        XslFoLoadOptions options = new XslFoLoadOptions(xsltDocumentFileName);

        // 空のコンストラクタを呼び出してDocumentオブジェクトをインスタンス化する
        Document pdfDocument = new Document(xmlDocumentFileName,options);

        // 結果のPDFファイルを保存する
        pdfDocument.save(pdfDocumentFileName);
    }
}
```


### XSL-FOをPDFに変換し、エラーハンドリング戦略を設定する

```java
// ドキュメントオブジェクトを初期化する

String documentFileName = Paths.get(DATA_DIR.toString(), "demo_txt.pdf").toString();
String xmlDocumentFileName = Paths.get(DATA_DIR.toString(), "demo.xml").toString();
String xsltDocumentFileName = Paths.get(DATA_DIR.toString(), "employees.xslt").toString();

XslFoLoadOptions options = new XslFoLoadOptions(xsltDocumentFileName);

// エラーハンドリング戦略を設定する
options.setParsingErrorsHandlingType(XslFoLoadOptions.ParsingErrorsHandlingTypes.ThrowExceptionImmediately);

// 空のコンストラクタを呼び出してDocumentオブジェクトをインスタンス化する
Document document = new Document(xmlDocumentFileName, options);

// 結果のPDFファイルを保存する
document.save(documentFileName);
document.close();
```

## LaTeX/TeXをPDFに変換する

LaTeXファイル形式は、TeXファミリーの言語のLaTeX派生におけるマークアップを持つテキストファイル形式であり、LaTeXはTeXシステムの派生形式です。
 LaTeX (ˈleɪtɛk/ レイテックまたはラーテック) は、文書準備システムおよび文書マークアップ言語です。数学、物理学、コンピュータサイエンスを含む多くの分野で、科学文書の伝達および出版に広く使用されています。また、サンスクリット語やアラビア語を含む複雑な多言語資料を含む本や記事の準備および出版において重要な役割を果たしています。LaTeXは、TeX組版プログラムを使用して出力をフォーマットし、TeXマクロ言語で書かれています。

**Aspose.PDF for Java** は、TeXファイルをPDF形式に変換する機能をサポートしており、この要件を達成するために、com.aspose.pdfパッケージには[LatexLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LatexLoadOptions)というクラスがあり、LaTeXファイルを読み込み、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)クラスを使用して出力をPDF形式でレンダリングする機能を提供しています。 以下のコードスニペットは、LaTexファイルをPDF形式に変換するプロセスを示しています。

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertLATEXtoPDF {

    private ConvertLATEXtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // Latex読み込みオプションオブジェクトをインスタンス化
        TeXLoadOptions options = new TeXLoadOptions();
        
        // Documentオブジェクトを作成
        String latexFileName = Paths.get(_dataDir.toString(), "samplefile.tex").toString();
        Document document = new Document(latexFileName, options);

        // 出力PDFドキュメントを保存
        document.save(Paths.get(_dataDir.toString(),"TEXtoPDF.pdf").toString());
    }
}
```

{{% alert color="success" %}}
**LaTeX/TeXをPDFにオンラインで変換してみてください**


Aspose.PDF for Javaは、オンライン無料アプリケーション["LaTex to PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf)を提供しており、その機能と品質を試して調査することができます。
[![Aspose.PDF 変換 LaTeX/TeX から PDF への無料アプリ](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}