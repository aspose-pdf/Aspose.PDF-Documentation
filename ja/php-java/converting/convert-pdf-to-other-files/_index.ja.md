---
title: PDFファイルを他の形式に変換する
linktitle: PDFを他の形式に変換する
type: docs
weight: 90
url: /php-java/convert-pdf-to-other-files/
lastmod: "2024-05-20"
description: このトピックでは、Aspose.PDFがPDFファイルを他のファイル形式に変換できる方法を紹介します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## PDFをEPUBに変換

{{% alert color="success" %}}
**PDFをEPUBにオンラインで変換してみる**

Aspose.PDF for PHPは、オンラインで無料のアプリケーション["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub)を提供しており、その機能と品質を調査することができます。

[![Aspose.PDF Convertion PDF to EPUB with Free App](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="電子出版物">EPUB</abbr>**（電子出版物の略）は、国際デジタル出版フォーラム（IDPF）による無料でオープンな電子書籍の標準です。
 ファイルは拡張子.epubを持っています。EPUBはリフロー可能なコンテンツ用に設計されており、EPUBリーダーは特定の表示デバイスに最適化されたテキストを表示することができます。EPUBは固定レイアウトコンテンツもサポートしています。このフォーマットは、出版社や変換ハウスが社内で使用するための単一のフォーマットとして意図されており、配布や販売にも使用されます。Open eBook標準に取って代わるものです。

Aspose.PDF for PHPは、PDFドキュメントをEPUB形式に変換する機能をサポートしています。Aspose.PDF for PHPには[EpubSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/EpubSaveOptions)という名前のクラスがあり、[Document.save(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#save-java.lang.String-)メソッドの第二引数として使用して、EPUBファイルを生成することができます。この要件を達成するために、以下のコードスニペットを使用してください。

```php
// Documentクラスの新しいインスタンスを作成し、入力PDFファイルをロードします
$document = new Document($inputFile);

// EpubSaveOptionsクラスの新しいインスタンスを作成します
$saveOption = new EpubSaveOptions();

// 指定された保存オプションを使用して、ドキュメントをEPUB形式で保存します
$document->save($outputFile, $saveOption);
```

## PDFをLaTeX/TeXに変換する

**Aspose.PDF for PHP**は、PDFをLaTeX/TeXに変換することをサポートしています。
LaTeXファイル形式は、特別なマークアップを持つテキストファイル形式であり、高品質な組版のためにTeXベースのドキュメント準備システムで使用されます。

PDFファイルをTeXに変換するには、Aspose.PDFには変換プロセス中に一時的な画像を保存するための`setOutDirectoryPath`メソッドを提供するクラス[LaTeXSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LaTeXSaveOptions)があります。

以下のコードスニペットは、JavaでPDFファイルをTEX形式に変換するプロセスを示しています。

```php
// 新しいDocumentオブジェクトを作成し、入力PDFファイルを読み込む
$document = new Document($inputFile);

// 新しいLaTeXSaveOptionsオブジェクトを作成
$saveOption = new LaTeXSaveOptions();
$saveOption->setOutDirectoryPath ($pathToOutputDirectory)

// ドキュメントをLaTeXとして保存
$document->save($outputFile, $saveOption);
```

{{% alert color="success" %}}
**PDFをLaTeX/TeXにオンラインで変換してみてください**

Aspose.PDF for PHPは、オンラインで無料のアプリケーション["PDFからLaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex)を提供しており、その機能と品質を試して調査することができます。

[![Aspose.PDF Convertion PDF to LaTeX/TeX with Free App](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## PDFをテキストに変換

**Aspose.PDF for PHP**は、PDFドキュメント全体および単一ページをテキストファイルに変換することをサポートしています。

### PDFドキュメント全体をテキストファイルに変換

[TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber)クラスのVisitメソッドを使用して、PDFドキュメントをTXTファイルに変換できます。

次のコードスニペットは、すべてのページからテキストを抽出する方法を説明しています。

```php
// PDFドキュメントをロードする
$document = new Document($inputFile);

// ドキュメントからテキストを抽出するためのTextAbsorberオブジェクトを作成する
$textAbsorber = new TextAbsorber();

// ドキュメントからテキストを抽出する
$textAbsorber->visit($document);
$content = $textAbsorber->getText();

// 抽出したテキストを出力ファイルに保存する
file_put_contents($outputFile, $content);

// 出力ファイルのファイルサイズを取得する
$fileSize = filesize($outputFile);
```

{{% alert color="success" %}}
**PDFをテキストにオンラインで変換してみてください**

Aspose.PDF for PHPは、オンラインで無料で利用できるアプリケーション「[PDF to Text](https://products.aspose.app/pdf/conversion/pdf-to-txt)」を提供しており、機能と品質を試すことができます。

[![Aspose.PDF Convertion PDF to Text with Free App](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

### PDFページをテキストファイルに変換する

Aspose.PDF for PHPを使用して、PDFドキュメントをTXTファイルに変換できます。このタスクを解決するには、[TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber)クラスのVisitメソッドを使用する必要があります。

次のコードスニペットは、特定のページからテキストを抽出する方法を説明しています。

```php
// PDFドキュメントを読み込む
$document = new Document($inputFile);

// ドキュメントからテキストを抽出するためのTextAbsorberオブジェクトを作成する
$textAbsorber = new TextAbsorber();

$array = array(1, 3, 4);

foreach ($array as $page) {
    $textAbsorber->visit($document->getPages()->get_Item($page));
    $content = $textAbsorber->getText();
    
    $outputFile = $dataDir . DIRECTORY_SEPARATOR . 'result-pdf-to-text'. $page . '.txt';
    // 抽出したテキストを出力ファイルに保存する
    file_put_contents($outputFile, $content);
}
```


## PDFをXPSに変換する

**Aspose.PDF for PHP**は、PDFファイルを<abbr title="XML Paper Specification">XPS</abbr>形式に変換する機能を提供します。Javaを使用してPDFファイルをXPS形式に変換するためのコードスニペットを試してみましょう。

{{% alert color="success" %}}
**PDFをXPSにオンラインで変換してみましょう**

Aspose.PDF for PHPは、オンラインで無料で使用できるアプリケーション「[PDF to XPS](https://products.aspose.app/pdf/conversion/pdf-to-xps)」を提供しており、その機能と動作の品質を調査することができます。

[![Aspose.PDF Convertion PDF to XPS with Free App](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

XPSファイルタイプは主にMicrosoft CorporationによるXML Paper Specificationに関連付けられています。XML Paper Specification (XPS)は、かつてMetroというコードネームで呼ばれており、次世代印刷パス(NGPP)のマーケティングコンセプトを包含しているもので、Windowsオペレーティングシステムに文書作成と閲覧を統合するためのMicrosoftの取り組みです。

PDFファイルをXPSに変換するために、Aspose.PDFには[XpsSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XpsSaveOptions)クラスがあり、これはDocument.save(..)コンストラクタの第2引数として使用され、XPSファイルを生成するために使用されます。
 以下のコードスニペットは、PDFファイルをXPS形式に変換するプロセスを示しています。

```php
// 新しいDocumentオブジェクトを作成し、入力PDFファイルを読み込む
$document = new Document($inputFile);

// 新しいXpsSaveOptionsオブジェクトを作成する
$saveOption = new XpsSaveOptions();

// 指定された保存オプションを使用してドキュメントをXPSとして保存する
$document->save($outputFile, $saveOption);
```