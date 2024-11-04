---
title: PDFファイルを他の形式に変換する
linktitle: PDFを他の形式に変換する
type: docs
weight: 90
url: /java/convert-pdf-to-other-files/
lastmod: "2021-11-19"
description: このトピックでは、Aspose.PDFがPDFファイルを他のファイル形式に変換する方法を紹介します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## PDFをEPUBに変換

{{% alert color="success" %}}
**PDFをEPUBにオンラインで変換してみる**

Aspose.PDF for Javaは、オンラインで無料アプリケーション["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub)を提供しており、その機能と品質を試してみることができます。

[![Aspose.PDF Convertion PDF to EPUB with Free App](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="電子出版物">EPUB</abbr>**（電子出版物の略）は、国際デジタル出版フォーラム（IDPF）による無料でオープンな電子書籍の標準です。
 Files have the extension .epub.EPUBはリフロー可能なコンテンツ用に設計されており、EPUBリーダーは特定の表示デバイスに最適化されたテキストを表示できます。EPUBは固定レイアウトのコンテンツもサポートしています。この形式は、出版社や変換会社が社内で使用するためだけでなく、配布や販売のための単一の形式として意図されています。Open eBook標準を置き換えます。

Aspose.PDF for Javaは、PDFドキュメントをEPUB形式に変換する機能をサポートしています。Aspose.PDF for Javaには[EpubSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/EpubSaveOptions)というクラスがあり、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..)メソッドの第2引数として使用して、EPUBファイルを生成できます。この要件を達成するために、次のコードスニペットを試してみてください。

```java
// PDFドキュメントをロード
Document document = new Document(DATA_DIR + "PDFToEPUB.pdf");
// Epub保存オプションをインスタンス化
EpubSaveOptions options = new EpubSaveOptions();
// コンテンツのレイアウトを指定
options.setContentRecognitionMode(EpubSaveOptions.RecognitionMode.Flow);
// ePUBドキュメントを保存
document.save(DATA_DIR + "PDFToEPUB_out.epub", options);
document.close();
```

## PDFをLaTeX/TeXに変換する

**Aspose.PDF for Java**はPDFをLaTeX/TeXに変換することをサポートしています。LaTeXファイル形式は特別なマークアップを持つテキストファイル形式で、高品質な組版のためのTeXベースのドキュメント準備システムで使用されます。

PDFファイルをTeXに変換するために、Aspose.PDFには[TeXSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TeXSaveOptions)クラスがあり、変換プロセス中に一時的な画像を保存するための`setOutDirectoryPath`メソッドを提供します。

以下のコードスニペットは、JavaでPDFファイルをTEX形式に変換するプロセスを示しています。

```java
String documentFileName = Paths.get(DATA_DIR.toString(), "PDFToTeX.pdf").toString();
String texDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFToTeX_out.tex").toString();

// Documentオブジェクトを作成
Document document = new Document(documentFileName);

// LaTex保存オプションをインスタンス化
TeXSaveOptions saveOptions = new TeXSaveOptions();

// 出力ディレクトリを指定
String pathToOutputDirectory = DATA_DIR.toString();

// 保存オプションオブジェクトの出力ディレクトリパスを設定
saveOptions.setOutDirectoryPath(pathToOutputDirectory);

// PDFファイルをLaTex形式で保存
document.save(texDocumentFileName, saveOptions);
document.close();
```


{{% alert color="success" %}}
**PDFをLaTeX/TeXにオンラインで変換してみる**

Aspose.PDF for Javaは、オンライン無料アプリケーション["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex)を提供しています。ここで、その機能と品質を調査することができます。

[![Aspose.PDF Convertion PDF to LaTeX/TeX with Free App](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## PDFをテキストに変換

**Aspose.PDF for Java**は、PDF文書全体および単一ページをテキストファイルに変換することをサポートしています。

### PDF文書全体をテキストファイルに変換

[TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber)クラスのVisitメソッドを使用して、PDF文書をTXTファイルに変換することができます。

以下のコードスニペットは、すべてのページからテキストを抽出する方法を説明しています。

```java
// ドキュメントを開く
String pdfFileName = Paths.get(DATA_DIR.toString(), "demo.pdf").toString();
String txtFileName = Paths.get(DATA_DIR.toString(), "PDFToTXT_out.txt").toString();

// PDF文書を読み込む
Document document = new Document(pdfFileName);
TextAbsorber ta = new TextAbsorber();
ta.visit(document);
// 抽出したテキストをテキストファイルに保存
BufferedWriter writer = new BufferedWriter(new FileWriter(txtFileName));
writer.write(ta.getText());
writer.close();
```


{{% alert color="success" %}}
**オンラインでPDFをテキストに変換してみてください**

Aspose.PDF for Javaは、オンラインで無料アプリケーション["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt)を提供しており、その機能と品質を試すことができます。

[![Aspose.PDF Convertion PDF to Text with Free App](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

### PDFページをテキストファイルに変換する

Aspose.PDF for Javaを使用して、PDFドキュメントをTXTファイルに変換できます。このタスクを解決するには、[TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber)クラスのVisitメソッドを使用する必要があります。

以下のコードスニペットは、特定のページからテキストを抽出する方法を説明しています。

```java
String pdfFileName = Paths.get(DATA_DIR.toString(), "demo.pdf").toString();
String txtFileName = Paths.get(DATA_DIR.toString(), "PDFToTXT_out.txt").toString();

// PDFドキュメントを読み込む
Document document = new Document(pdfFileName);

TextAbsorber ta = new TextAbsorber();
int[] pages = new int[] { 1, 3, 4 };

for (int page : pages) {
    ta.visit(document.getPages().get_Item(page));
}

// 抽出したテキストをテキストファイルに保存する
BufferedWriter writer = new BufferedWriter(new FileWriter(txtFileName));
writer.write(ta.getText());
writer.close();
document.close();
```


## PDFをXPSに変換

**Aspose.PDF for Java**は、PDFファイルを<abbr title="XML Paper Specification">XPS</abbr>形式に変換する機能を提供します。JavaでPDFファイルをXPS形式に変換するために、以下のコードスニペットを使用してみましょう。

{{% alert color="success" %}}
**オンラインでPDFをXPSに変換してみる**

Aspose.PDF for Javaは、オンラインで無料アプリケーション["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps)を提供しており、その機能と品質を試すことができます。

[![Aspose.PDF Convertion PDF to XPS with Free App](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

XPSファイル形式は、主にMicrosoft CorporationによるXML Paper Specificationに関連付けられています。XML Paper Specification (XPS)は、以前はMetroというコードネームで知られ、次世代プリントパス (NGPP) のマーケティングコンセプトを包括し、Windowsオペレーティングシステムへの文書作成と表示の統合を目指すMicrosoftの取り組みです。

PDFファイルをXPSに変換するために、Aspose.PDFには[XpsSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XpsSaveOptions)クラスがあり、これはXPSファイルを生成するためにDocument.save(..)コンストラクタの第2引数として使用されます。
 以下のコードスニペットは、PDFファイルをXPS形式に変換するプロセスを示しています。

```java
String documentFileName = Paths.get(DATA_DIR.toString(), "sample.pdf").toString();
String xpsDocumentFileName = Paths.get(DATA_DIR.toString(), "sample-res-xps.xps").toString();

// Documentオブジェクトを作成
Document document = new Document(documentFileName);

// XPS保存オプションをインスタンス化
XpsSaveOptions saveOptions = new XpsSaveOptions();

// 出力をXML形式で保存
document.save(xpsDocumentFileName, saveOptions);
document.close();
```