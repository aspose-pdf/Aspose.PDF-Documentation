---
title: Aspose.PDF DOM APIの基本
linktitle: DOM APIの基本
type: docs
weight: 10
url: /ja/androidjava/basics-of-dom-api/
description: Aspose.PDF for Android via Javaは、PDFドキュメントの構造をオブジェクトとして表現するためにDOMの概念を使用しています。ここで、この構造の説明を読むことができます。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## DOM APIの紹介

ドキュメントオブジェクトモデル（DOM）は、構造化文書をオブジェクト指向モデルとして表現する形式です。DOMは、プラットフォームおよび言語に依存しない方法で構造化文書を表現するための公式なW3C（World Wide Web Consortium）標準です。

簡単に言うと、DOMはある文書の構造を表すオブジェクトの木です。
 Aspose.PDF for Android via Javaは、オブジェクトに関してPDFドキュメントの構造を表すためにDOMの概念も使用します。ただし、DOMの側面（その要素など）は、使用中のプログラミング言語の構文内で操作されます。DOMの公開インターフェイスは、そのアプリケーションプログラミングインターフェイス（API）で指定されています。

### PDFドキュメントの紹介

ポータブルドキュメントフォーマット（PDF）は、ドキュメント交換のためのオープンスタンダードです。PDFドキュメントは、テキストとバイナリデータを組み合わせたものです。テキストエディタで開くと、ドキュメントの構造と内容を定義する生のオブジェクトが表示されます。

PDFファイルの論理構造は階層的であり、表示アプリケーションがドキュメントのページとその内容を描く順序を決定します。PDFは、オブジェクト、ファイル構造、ドキュメント構造、およびコンテンツストリームの4つのコンポーネントで構成されています。

### PDFドキュメント構造

PDFファイルの構造が階層的であるため、Aspose.PDF for Javaも同様に要素にアクセスします。 以下の階層は、PDF文書が論理的にどのように構造化されているか、およびAspose.PDF for Java DOM APIがそれをどのように構築するかを示しています。

![PDF Document Structure](https://docs.aspose.com/pdf/java/images/structure.png)

### PDF文書要素へのアクセス

Documentオブジェクトはオブジェクトモデルのルートレベルにあります。Aspose.PDF for Android via Java DOM APIを使用すると、Documentオブジェクトを作成し、階層内の他のすべてのオブジェクトにアクセスできます。Pagesのようなコレクションや、Pageなどの個別の要素にアクセスすることができます。DOM APIは、以下に示すように、PDF文書を操作するための単一のエントリーおよびエグジットポイントを提供します。

- PDF文書を開く
- DOMスタイルでPDF文書の構造にアクセスする
- PDF文書内のデータを更新する
- PDF文書を検証する
- PDF文書を異なる形式にエクスポートする
- 最後に、更新されたPDF文書を保存する

## 新しいAspose.PDF for Android via Java APIの使用方法

このトピックでは、新しいAspose.PDF for Android via Java APIを説明し、迅速かつ簡単に始めるためのガイドを提供します。 この記事には特定の機能の使用に関する詳細は含まれていないことに注意してください。

Aspose.PDF for Android via Javaは、以下の2つの部分で構成されています：

- Aspose.PDF for Android via Java DOM API
- Aspose.PDF.Facades

以下にそれぞれの領域の詳細を示します。

### Aspose.PDF for Android via Java DOM API

新しいAspose.PDF for Android via Java DOM APIは、PDFドキュメントの構造に対応しており、ファイルやドキュメントレベルだけでなく、オブジェクトレベルでもPDFドキュメントを操作するのに役立ちます。開発者がPDFドキュメントのすべての要素やオブジェクトにアクセスするための柔軟性をより高めました。Aspose.PDF DOM APIのクラスを使用することで、ドキュメント要素やフォーマットにプログラムからアクセスすることができます。この新しいDOM APIは、以下に示すような様々な名前空間で構成されています：

### com.aspose.pdf

この名前空間は、PDFドキュメントを開いたり保存したりするためのDocumentクラスを提供します。 The License クラスもこの名前空間の一部です。また、com.aspose.pdf.Page、com.aspose.pdf.PageCollection、com.aspose.pdf.FileSpecification、com.aspose.pdf.EmbeddedFileCollection、com.aspose.pdf.OutlineItemCollection、com.aspose.pdf.OutlineCollection など、PDF ページ、添付ファイル、ブックマークに関連するクラスも提供しています。

#### com.aspose.pdf.text

この名前空間は、テキストとそのさまざまな側面を操作するのに役立つクラスを提供します。例えば、com.aspose.pdf.Font、com.aspose.pdf.FontCollection、com.aspose.pdf.FontRepository、com.aspose.pdf.FontStyles、com.aspose.pdf.TextAbsorber、com.aspose.pdf.TextFragment、com.aspose.pdf.TextFragmentAbsorber、com.aspose.pdf.TextFragmentCollection、com.aspose.pdf.TextFragmentState、com.aspose.pdf.TextSegment、そして com.aspose.pdf.TextSegmentCollection などです。

#### com.aspose.pdf.TextOptions

この名前空間は、テキストの検索、編集、置換のためのさまざまなオプションを設定できるクラスを提供します。例えば、com.aspose.pdf.TextEditOptions、com.aspose.pdf.TextReplaceOptions、そして com.aspose.pdf.TextSearchOptions などです。
#### com.aspose.pdf.PdfAction

この名前空間には、PDFドキュメントのインタラクティブな機能を操作するためのクラスが含まれています。たとえば、ドキュメントやその他のアクションを操作する場合です。この名前空間には、com.aspose.pdf.GoToAction、com.aspose.pdf.GoToRemoteAction、com.aspose.pdf.GoToURIActionなどのクラスが含まれています。

#### com.aspose.pdf.Annotation

注釈は、PDFドキュメントのインタラクティブな機能の一部です。注釈専用の名前空間を用意しています。この名前空間には、注釈を操作するためのクラスが含まれています。たとえば、com.aspose.pdf.Annotation、com.aspose.pdf.AnnotationCollection、com.aspose.pdf.CircleAnnotation、com.aspose.pdf.LinkAnnotationなどがあります。

#### com.aspose.pdf.Form

この名前空間には、PDFフォームおよびフォームフィールドを操作するためのクラスが含まれています。たとえば、com.aspose.pdf.Form、com.aspose.pdf.Field、com.aspose.pdf.TextBoxField、およびcom.aspose.pdf.OptionCollectionなどです。

#### com.aspose.pdf.devices 

PDFドキュメントをさまざまな画像形式に変換するなど、PDFドキュメントに対してさまざまな操作を実行できます。
 しかし、そのような操作はDocumentオブジェクトには属しておらず、そのような操作のためにDocumentクラスを拡張することはできません。これが、新しいDOM APIでDeviceの概念を導入した理由です。

##### com.aspose.pdf.facades

以前は、既存のPDFファイルを操作するためにAspose.PDF for Javaに加えてAspose.PDF.Kit for Javaが必要でした。古いAspose.PDF.Kitのコードを実行するには、com.aspose.pdf.facades名前空間を使用できます。