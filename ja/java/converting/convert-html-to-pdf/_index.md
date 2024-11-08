---
title: HTMLをPDFファイルに変換するJava
linktitle: HTMLをPDFファイルに変換
type: docs
weight: 40
url: /ja/java/convert-html-to-pdf/
lastmod: "2021-11-19"
description: このトピックでは、Aspose.PDFがHTMLおよびMHTML形式をPDFファイルに変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## 概要

この記事では、Javaを使用してHTMLをPDFに変換する方法を説明します。コードは非常にシンプルで、HTMLをDocumentクラスにロードし、出力PDFとして保存するだけです。JavaでMHTMLをPDFに変換するのも同様です。以下のトピックをカバーしています。

- [Java HTMLからPDFへ](#convert-html-to-pdf)
- [Java MHTMLからPDFへ](#convert-mhtml-to-pdf)
- [Java HTMLをPDFに変換](#convert-html-to-pdf)
- [Java MHTMLをPDFに変換](#convert-mhtml-to-pdf)
- [Java HTMLからPDFを作成](#convert-html-to-pdf)
- [Java MHTMLからPDFを作成](#convert-mhtml-to-pdf)
- [Java HTMLからPDFコンバーター - WebページをPDFに変換する方法](#convert-html-to-pdf)

- [Java HTMLからPDFライブラリ、APIまたはコードを使用してプログラムでHTMLからPDFをレンダリング、保存、生成または作成](#convert-html-to-pdf)

## Java HTML to PDF コンバーターライブラリ

**Aspose.PDF for Java** は、既存のHTMLドキュメントをPDFにシームレスに変換できるPDF操作APIです。HTMLをPDFに変換するプロセスは柔軟にカスタマイズできます。

## HTMLをPDFに変換

以下のJavaコードサンプルは、HTMLドキュメントをPDFに変換する方法を示しています。

1. [HtmlLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions) クラスのインスタンスを作成します。
1. [Document](https://reference.aspose.com/page/java/com.aspose.page/document) オブジェクトを初期化します。
1. **Document.save(String)** メソッドを呼び出して出力PDFドキュメントを保存します。

```java
// ソースPDFドキュメントを開く
Document document = new Document(DATA_DIR + "PDFToHTML.pdf")

// HTML SaveOptionsオブジェクトをインスタンス化
HtmlSaveOptions htmlsaveOptions = new HtmlSaveOptions();

// ドキュメントを保存
document.save(DATA_DIR + "MultiPageHTML_out.html", htmlsaveOptions);
```

{{% alert color="success" %}}
**HTMLをPDFにオンラインで変換してみてください**

Asposeは、オンラインで無料のアプリケーション["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf)を提供しており、機能と品質を調査することができます。

[![Aspose.PDF Convertion HTML to PDF using Free App](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf) {{% /alert %}}

## HTMLからPDFへの高度な変換

HTML変換エンジンには、変換プロセスを制御するためのいくつかのオプションがあります。

### メディアクエリのサポート

1. HTML [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions) を作成します。
1. プリントまたはスクリーンモードを設定します。
1. [Document オブジェクト](<https://reference.aspose.com/page/java/com.aspose.page/document>) を初期化します。
1. 出力PDFドキュメントを保存します。

メディアクエリは、異なるデバイスに合わせたスタイルシートを配信するための一般的な技術です。[HtmlMediaType](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlMediaType) プロパティを使用してデバイスタイプを設定できます。

```java
// HTML LoadOptionsを作成
HtmlLoadOptions options = new HtmlLoadOptions();

// プリントまたはスクリーンモードを設定
options.setHtmlMediaType(HtmlMediaType.Print);

// ドキュメントオブジェクトを初期化
String htmlFileName = Paths.get(DATA_DIR.toString(), "test.html").toString();
Document document = new Document(htmlFileName, options);

// 出力PDFドキュメントを保存
document.save(Paths.get(DATA_DIR.toString(), "HTMLtoPDF.pdf").toString());
document.close();
```


### フォント埋め込みの有効化（無効化）

1. 新しいHtml [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions) を追加します。
1. フォント埋め込みを有効/無効にします。
1. 新しいドキュメントを保存します。

HTMLページはしばしばフォントを使用します（例：ローカルフォルダのフォント、Google Fontsなど）。ドキュメント内のフォント埋め込みを制御することも、[IsEmbedFonts](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions#isEmbedFonts--) プロパティを使用して可能です。

```java
HtmlLoadOptions options = new HtmlLoadOptions();
// フォント埋め込みを有効/無効にします
options.setEmbedFonts(true);

Document document = new Document(DATA_DIR + "test_fonts.html", options);
document.save(DATA_DIR + "html_test.PDF");
document.close();
```

### 外部リソースの読み込みを管理する

変換エンジンは、HTMLドキュメントに関連付けられた特定のリソースの読み込みを制御するメカニズムを提供します。

[HtmlLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions) クラスには [CustomLoaderOfExternalResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions#setCustomLoaderOfExternalResources-com.aspose.pdf.LoadOptions.ResourceLoadingStrategy-) プロパティがあり、これを使用してリソースローダーの動作を定義できます。

```java
HtmlLoadOptions options = new HtmlLoadOptions();

options.setCustomLoaderOfExternalResources(
        new LoadOptions.ResourceLoadingStrategy() {
            public LoadOptions.ResourceLoadingResult invoke(String resourceURI) {
                // 置換のためのクリアテンプレートリソースを作成:
                LoadOptions.ResourceLoadingResult res = new LoadOptions.ResourceLoadingResult(new byte[] {});
                // i.imgur.comサーバーの場合は空のバイト配列を返す
                if (resourceURI.contains("i.imgur.com")) {
                    return res;
                } else {
                    // デフォルトのリソースローダーでリソースを処理
                    res.setLoadingCancelled(true);
                    return res;
                }
            }   
});

Document document = new Document(DATA_DIR + "test.html", options);
document.save(DATA_DIR + "html_test.PDF");
document.close();    
```

## MHTMLをPDFに変換

{{% alert color="success" %}}
**オンラインでMHTMLをPDFに変換してみてください**


Aspose.PDF for Javaは、オンラインの無料アプリケーション["MHTML to PDF"](https://products.aspose.app/pdf/conversion/mhtml-to-pdf)を提供しており、その機能と品質を調査することができます。

[![Aspose.PDF Convertion MHTML to PDF using Free App](mhtml.png)](https://products.aspose.app/pdf/conversion/mhtml-to-pdf)
{{% /alert %}}

<abbr title="MIME encapsulation of aggregate HTML documents">MHTML</abbr>、MIME HTMLの略であり、通常は外部リンクによって表されるリソース（例えば画像、Flashアニメーション、Javaアプレット、オーディオファイル）をHTMLコードと共に1つのファイルに統合するために使用されるウェブページアーカイブ形式です。MHTMLファイルの内容は、MIMEタイプmultipart/relatedを使用してHTMLメールメッセージとしてエンコードされます。

次のコードスニペットは、MHTMLファイルをJavaでPDF形式に変換する方法を示しています。

```java
// MHTMLファイルの読み込みオプションを指定するためのMhtLoadOptionsのインスタンスを作成します。
MhtLoadOptions options = new MhtLoadOptions();

// MHTMLファイルのパスを設定します。
String mhtmlFileName = Paths.get(DATA_DIR.toString(), "samplefile.mhtml").toString();

// MHTMLファイルをDocumentオブジェクトに読み込みます。
Document document = new Document(mhtmlFileName, options);

// ドキュメントをPDFファイルとして保存します。
document.save(Paths.get(DATA_DIR.toString(), "MarkdowntoPDF.pdf").toString());

// ドキュメントを閉じます。
document.close();
```