---
title: Aspose.PDF DOM APIの基本
linktitle: DOM APIの基本
type: docs
weight: 110
url: /java/basics-of-dom-api/
description: Aspose.PDF for Javaは、PDFドキュメントの構造をオブジェクトとして表現するためにDOMの概念を使用します。ここでは、この構造の説明を読むことができます。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## DOM APIの紹介

Document Object Model (DOM) は、構造化されたドキュメントをオブジェクト指向モデルとして表現する形式です。DOMは、プラットフォームや言語に依存しない形で構造化されたドキュメントを表現するためのWorld Wide Web Consortium (W3C) の公式標準です。

簡単に言うと、DOMはあるドキュメントの構造を表すオブジェクトのツリーです。
 Aspose.PDF for Java は、PDF ドキュメントの構造をオブジェクトとして表現するために DOM の概念を使用します。ただし、DOM の側面（その要素など）は、使用中のプログラミング言語の構文内で操作されます。DOM の公開インターフェースは、そのアプリケーションプログラミングインターフェース (API) で指定されています。

### PDF ドキュメントの紹介

ポータブルドキュメントフォーマット (PDF) は、ドキュメント交換のためのオープン標準です。PDF ドキュメントはテキストとバイナリデータの組み合わせです。テキストエディタで開くと、ドキュメントの構造と内容を定義する生のオブジェクトが表示されます。

PDF ファイルの論理構造は階層的であり、表示アプリケーションがドキュメントのページとその内容を描画する順序を決定します。PDF は、オブジェクト、ファイル構造、ドキュメント構造、およびコンテンツストリームの 4 つのコンポーネントで構成されています。

### PDF ドキュメントの構造

PDF ファイルの構造は階層的であるため、Aspose.PDF for Java も同じ方法で要素にアクセスします。 以下の階層は、PDFドキュメントがどのように論理的に構造化されているか、そしてAspose.PDF for Java DOM APIがどのようにそれを構築しているかを示しています。

![PDFドキュメントの構造](../images/structure.png)

### PDFドキュメント要素へのアクセス

Documentオブジェクトはオブジェクトモデルのルートレベルにあります。Aspose.PDF for Java DOM APIを使用すると、Documentオブジェクトを作成し、階層内の他のすべてのオブジェクトにアクセスできます。Pagesのようなコレクションや、Pageのような個々の要素にアクセスすることができます。DOM APIは、以下に示すように、PDFドキュメントを操作するための単一のエントリーポイントと出口ポイントを提供します。

- PDFドキュメントを開く
- DOMスタイルでPDFドキュメントの構造にアクセスする
- PDFドキュメントのデータを更新する
- PDFドキュメントを検証する
- PDFドキュメントを異なる形式にエクスポートする
- 最後に、更新されたPDFドキュメントを保存する

## 新しいAspose.PDF for Java APIの使い方

このトピックでは、新しいAspose.PDF for Java APIを説明し、迅速かつ簡単に始めるためのガイドを提供します。 この特定の機能の使用に関する詳細は、この記事の一部ではないことに注意してください。

Aspose.PDF for Java は、以下の2つの部分で構成されています：

- Aspose.PDF for Java DOM API
- Aspose.PDF.Facades

以下に、これらの各領域の詳細を示します。

### Aspose.PDF for Java DOM API

新しい Aspose.PDF for Java DOM API は PDF ドキュメントの構造に対応しており、ファイルおよびドキュメントレベルだけでなく、オブジェクトレベルでも PDF ドキュメントを操作するのに役立ちます。開発者が PDF ドキュメントのすべての要素とオブジェクトにアクセスするための柔軟性をより高めました。Aspose.PDF DOM API のクラスを使用して、ドキュメントの要素やフォーマットにプログラム的にアクセスすることができます。この新しい DOM API は、以下に示すようにさまざまな名前空間で構成されています：

### com.aspose.pdf

この名前空間は、PDF ドキュメントを開いたり保存したりするための Document クラスを提供します。 The License クラスもこの名前空間の一部です。また、com.aspose.pdf.Page、com.aspose.pdf.PageCollection、com.aspose.pdf.FileSpecification、com.aspose.pdf.EmbeddedFileCollection、com.aspose.pdf.OutlineItemCollection、com.aspose.pdf.OutlineCollection など、PDF ページ、添付ファイル、およびブックマークに関連するクラスも提供します。

#### com.aspose.pdf.text

この名前空間は、例えば com.aspose.pdf.Font、com.aspose.pdf.FontCollection、com.aspose.pdf.FontRepository、com.aspose.pdf.FontStyles、com.aspose.pdf.TextAbsorber、com.aspose.pdf.TextFragment、com.aspose.pdf.TextFragmentAbsorber、com.aspose.pdf.TextFragmentCollection、com.aspose.pdf.TextFragmentState、com.aspose.pdf.TextSegment、com.aspose.pdf.TextSegmentCollection など、テキストとその様々な側面を扱うのに役立つクラスを提供します。

#### com.aspose.pdf.TextOptions

この名前空間は、例えば com.aspose.pdf.TextEditOptions、com.aspose.pdf.TextReplaceOptions、com.aspose.pdf.TextSearchOptions など、テキストの検索、編集、または置換のための様々なオプションを設定できるクラスを提供します。
#### com.aspose.pdf.PdfAction

この名前空間には、PDFドキュメントのインタラクティブな機能を操作するのに役立つクラスが含まれています。たとえば、ドキュメントやその他のアクションを操作することができます。この名前空間には、com.aspose.pdf.GoToAction、com.aspose.pdf.GoToRemoteAction、com.aspose.pdf.GoToURIActionなどのクラスが含まれています。

#### com.aspose.pdf.Annotation

注釈は、PDFドキュメントのインタラクティブ機能の一部です。注釈に専用の名前空間を設けています。この名前空間には、注釈を操作するのに役立つクラスが含まれています。たとえば、com.aspose.pdf.Annotation、com.aspose.pdf.AnnotationCollection、com.aspose.pdf.CircleAnnotation、com.aspose.pdf.LinkAnnotationなどです。

#### com.aspose.pdf.Form

この名前空間には、PDFフォームやフォームフィールドを操作するのに役立つクラスが含まれています。たとえば、com.aspose.pdf.Form、com.aspose.pdf.Field、com.aspose.pdf.TextBoxField、com.aspose.pdf.OptionCollectionなどです。

#### com.aspose.pdf.devices 

PDFドキュメントをさまざまな画像形式に変換するなど、PDFドキュメントに対してさまざまな操作を行うことができます。
 しかし、そのような操作はDocumentオブジェクトに属しておらず、そのような操作のためにDocumentクラスを拡張することはできません。だからこそ、新しいDOM APIでDeviceの概念を導入しました。

##### com.aspose.pdf.facades

以前はJava用Aspose.PDFを使用するには、既存のPDFファイルを操作するためにAspose.PDF.Kit for Javaが必要でした。古いAspose.PDF.Kitコードを実行するには、com.aspose.pdf.facades名前空間を使用できます。