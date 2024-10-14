---
title: Aspose.PDF DOM APIの基礎
linktitle: DOM APIの基礎
type: docs
weight: 140
url: /net/basics-of-dom-api/
description: Aspose.PDF for .NETは、オブジェクトの観点からPDFドキュメントの構造を表すためにDOMのアイデアも使用しています。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## DOM APIへの紹介

ドキュメントオブジェクトモデル（DOM）は、オブジェクト指向モデルとして構造化ドキュメントを表現する形式です。DOMは、構造化ドキュメントをプラットフォームや言語に中立的な方法で表現するための公式なWorld Wide Web Consortium（W3C）標準です。

簡単に言うと、DOMはあるドキュメントの構造を表すオブジェクトのツリーです。
簡単な言葉で言えば、DOMはある文書の構造を表すオブジェクトのツリーです。

### PDF文書の紹介

ポータブルドキュメントフォーマット（PDF）は、ドキュメント交換のためのオープンスタンダードです。PDF文書はテキストとバイナリデータの組み合わせです。テキストエディタで開くと、文書の構造と内容を定義する生のオブジェクトが表示されます。

PDFファイルの論理構造は階層的であり、表示アプリケーションが文書のページとその内容を描画する順序を決定します。PDFは四つのコンポーネントで構成されています: オブジェクト、ファイル構造、文書構造、およびコンテンツストリーム。

### PDF文書構造

PDFファイルの構造が階層的であるため、Aspose.PDF for .NETも同じ方法で要素にアクセスします。次の階層は、PDF文書が論理的にどのように構造化されているか、そしてAspose.PDF for .NET DOM APIがそれをどのように構築するかを示しています。

![PDF文書構造](../images/structure.png)

### PDF文書要素へのアクセス

Documentオブジェクトはオブジェクトモデルのルートレベルにあります。
ドキュメントオブジェクトはオブジェクトモデルのルートレベルにあります。

- PDFドキュメントを開く
- DOMスタイルでPDFドキュメント構造にアクセスする
- PDFドキュメント内のデータを更新する
- PDFドキュメントを検証する
- PDFドキュメントを異なる形式にエクスポートする
- 最終的に更新されたPDFドキュメントを保存する

## 新しいAspose.PDF for .NET APIの使用方法

このトピックでは、新しいAspose.PDF for .NET APIについて説明し、迅速かつ簡単に開始する方法を案内します。特定の機能の使用方法に関する詳細は、この記事の一部ではありません。

Aspose.PDF for .NETは二つの部分で構成されています:

- Aspose.PDF for .NET DOM API
- Aspose.PDF.Facades (旧Aspose.PDF.Kit for .NET)
これらの領域の詳細は以下に記載されています。

### Aspose.PDF for .NET DOM API

Aspose.PDF for .NET DOM APIはPDFドキュメント構造に対応しており、ファイルやドキュメントレベルだけでなく、オブジェクトレベルでもPDFドキュメントを操作できるように支援します。
### Aspose.PDF

この名前空間は、PDFドキュメントを開いたり保存したりするDocumentクラスを提供します。Licenseクラスもこの名前空間の一部です。また、Page、PageCollection、FileSpecification、EmbeddedFileCollection、OutlineItemCollection、OutlineCollectionなど、PDFページ、添付ファイル、ブックマークに関連するクラスも提供します。

#### Aspose.Text

この名前空間は、テキストとそのさまざまな側面を操作するのに役立つクラスを提供します。例えば、Font、FontCollection、FontRepository、FontStyles、TextAbsorber、TextFragment、TextFragmentAbsorber、TextFragmentCollection、TextFragmentState、TextSegment、TextSegmentCollectionなどがあります。

#### Aspose.Text.TextOptions

この名前空間は、テキストの検索、編集、または置換のための異なるオプションを設定するクラスを提供します。例えば、TextEditOptions、TextReplaceOptions、TextSearchOptionsなどがあります。
この名前空間は、テキストの検索、編集、または置換のための異なるオプションを設定するクラスを提供します。たとえば、TextEditOptions、TextReplaceOptions、TextSearchOptionsなどがあります。

#### Aspose.InteractiveFeatures

この名前空間には、PDFドキュメントのインタラクティブ機能を扱うのに役立つクラスが含まれています。たとえば、ドキュメントとその他のアクションを扱うことなどです。この名前空間には、GoToAction、GoToRemoteAction、GoToURIActionなどのクラスが含まれています。

#### Aspose.InteractiveFeatures.Annotations

アノテーションは、PDFドキュメントのインタラクティブ機能の一部です。アノテーションのために専用の名前空間を設けています。この名前空間には、たとえばAnnotation、AnnotationCollection、CircleAnnotation、LinkAnnotationなど、アノテーションを扱うのに役立つクラスが含まれています。

#### Aspose.InteractiveFeatures.Forms

この名前空間には、PDFフォームおよびフォームフィールドを扱うのに役立つクラスが含まれています。たとえばForm、Field、TextBoxField、OptionCollectionなどがあります。

#### Aspose.PDF.Devices

PDFドキュメントに対してさまざまな操作を行うことができます。たとえば、PDFドキュメントをさまざまなイメージ形式に変換することなどができます。
PDFドキュメントには、PDFドキュメントをさまざまな画像形式に変換するなど、さまざまな操作を実行できます。

##### Aspose.PDF.Facades

以前のAspose.PDF for .NETよりも前に、既存のPDFファイルを操作するためにはAspose.PDF.Kit for .NETが必要でした。古いAspose.PDF.Kitのコードを実行するには、Aspose.PDF.Facades名前空間を使用できます。
