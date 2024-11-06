---
title: Aspose.PDF DOM APIの基本
linktitle: DOM APIの基本
type: docs
weight: 110
url: es/python-java/basics-of-dom-api/
description: Aspose.PDF for Javaは、PDFドキュメントの構造をオブジェクトとして表現するためにDOMの概念を使用します。ここで、この構造の説明を読むことができます。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## DOM APIの紹介

ドキュメントオブジェクトモデル（DOM）は、構造化されたドキュメントをオブジェクト指向モデルとして表現する形式です。DOMは、プラットフォームや言語に依存しない方法で構造化されたドキュメントを表現するための、公式なワールドワイドウェブコンソーシアム（W3C）の標準です。

簡単に言えば、DOMはあるドキュメントの構造を表現するオブジェクトの木です。
 Aspose.PDF for Java も、オブジェクトの観点からPDFドキュメントの構造を表現するためにDOMの概念を使用します。しかし、DOMの側面（例えばそのElements）は、使用しているプログラミング言語の構文内で操作されます。DOMのパブリックインターフェースは、そのアプリケーションプログラミングインターフェース（API）で指定されています。

### PDFドキュメントの紹介

ポータブルドキュメントフォーマット（PDF）は、ドキュメント交換のためのオープン標準です。PDFドキュメントは、テキストとバイナリデータの組み合わせです。テキストエディタで開くと、ドキュメントの構造と内容を定義する生のオブジェクトが表示されます。

PDFファイルの論理構造は階層的であり、表示アプリケーションがドキュメントのページとその内容を描画する順序を決定します。PDFは、オブジェクト、ファイル構造、ドキュメント構造、コンテンツストリームの4つのコンポーネントで構成されています。

### PDFドキュメント構造

PDFファイルの構造が階層的であるため、Aspose.PDF for Java も同様に要素にアクセスします。 以下の階層は、PDFドキュメントが論理的にどのように構造化されているかと、Aspose.PDF for Java DOM APIがそれをどのように構築するかを示しています。

![PDF Document Structure](../images/structure.png)

### PDFドキュメント要素へのアクセス

Documentオブジェクトは、オブジェクトモデルのルートレベルにあります。Aspose.PDF for Java DOM APIを使用すると、Documentオブジェクトを作成し、階層内の他のすべてのオブジェクトにアクセスできます。Pagesのようなコレクションや、Pageのような個々の要素にアクセスすることができます。DOM APIは、PDFドキュメントを操作するための単一のエントリーポイントと出口ポイントを提供します。以下に示すように：

- PDFドキュメントを開く
- DOMスタイルでPDFドキュメント構造にアクセスする
- PDFドキュメントのデータを更新する
- PDFドキュメントを検証する
- PDFドキュメントをさまざまな形式にエクスポートする
- 最後に、更新されたPDFドキュメントを保存する

## 新しいAspose.PDF for Java APIの使用方法

このトピックでは、新しいAspose.PDF for Java APIを説明し、迅速かつ簡単に始めるためのガイドを提供します。 この特定の機能の使用に関する詳細は、この記事の一部ではありません。

Aspose.PDF for Javaは、以下の2つの部分で構成されています：

- Aspose.PDF for Java DOM API
- Aspose.PDF.Facades

これらの各分野の詳細は以下に示します。

### Aspose.PDF for Java DOM API

新しいAspose.PDF for Java DOM APIは、PDFドキュメントの構造に対応しており、PDFドキュメントをファイルやドキュメントレベルだけでなく、オブジェクトレベルでも操作するのに役立ちます。開発者がPDFドキュメントのすべての要素やオブジェクトにアクセスするためのより多くの柔軟性を提供しています。Aspose.PDF DOM APIのクラスを使用することで、ドキュメント要素やフォーマットにプログラムでアクセスすることができます。この新しいDOM APIは、以下に示すさまざまな名前空間で構成されています：

### com.aspose.pdf

この名前空間は、PDFドキュメントを開いたり保存したりすることを可能にするDocumentクラスを提供します。 The License クラスもこの名前空間の一部です。また、com.aspose.pdf.Page、com.aspose.pdf.PageCollection、com.aspose.pdf.FileSpecification、com.aspose.pdf.EmbeddedFileCollection、com.aspose.pdf.OutlineItemCollection、com.aspose.pdf.OutlineCollection など、PDF ページ、添付ファイル、およびブックマークに関連するクラスも提供します。

#### com.aspose.pdf.text

この名前空間は、テキストとそのさまざまな側面を扱うのに役立つクラスを提供します。例えば、com.aspose.pdf.Font、com.aspose.pdf.FontCollection、com.aspose.pdf.FontRepository、com.aspose.pdf.FontStyles、com.aspose.pdf.TextAbsorber、com.aspose.pdf.TextFragment、com.aspose.pdf.TextFragmentAbsorber、com.aspose.pdf.TextFragmentCollection、com.aspose.pdf.TextFragmentState、com.aspose.pdf.TextSegment、com.aspose.pdf.TextSegmentCollection などがあります。

#### com.aspose.pdf.TextOptions

この名前空間は、テキストの検索、編集、置換のために異なるオプションを設定できるクラスを提供します。例えば、com.aspose.pdf.TextEditOptions、com.aspose.pdf.TextReplaceOptions、com.aspose.pdf.TextSearchOptions などがあります。
#### com.aspose.pdf.PdfAction

この名前空間には、PDFドキュメントのインタラクティブ機能を操作するのに役立つクラスが含まれています。たとえば、ドキュメントおよびその他のアクションを操作する場合です。この名前空間には、com.aspose.pdf.GoToAction、com.aspose.pdf.GoToRemoteAction、com.aspose.pdf.GoToURIAction などのクラスが含まれています。

#### com.aspose.pdf.Annotation

注釈は、PDFドキュメントのインタラクティブ機能の一部です。注釈用の名前空間を専用に設けています。この名前空間には、com.aspose.pdf.Annotation、com.aspose.pdf.AnnotationCollection、com.aspose.pdf.CircleAnnotation、com.aspose.pdf.LinkAnnotation など、注釈を操作するのに役立つクラスが含まれています。

#### com.aspose.pdf.Form

この名前空間には、PDFフォームおよびフォームフィールドを操作するのに役立つクラスが含まれています。たとえば、com.aspose.pdf.Form、com.aspose.pdf.Field、com.aspose.pdf.TextBoxField、com.aspose.pdf.OptionCollection などです。

#### com.aspose.pdf.devices

PDFドキュメントをさまざまな画像形式に変換するなど、PDFドキュメントに対してさまざまな操作を行うことができます。
 しかし、そのような操作はDocumentオブジェクトに属しておらず、そのような操作のためにDocumentクラスを拡張することはできません。そこで、新しいDOM APIでDeviceの概念を導入しました。

##### com.aspose.pdf.facades

以前はJava用のAspose.PDF t.o.oで既存のPDFファイルを操作するにはJava用のAspose.PDF.Kitが必要でした。古いAspose.PDF.Kitコードを実行するには、com.aspose.pdf.facades名前空間を使用できます。