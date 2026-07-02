---
title: Aspose.PDF DOM API の基本
linktitle: DOM API の基本
type: docs
weight: 10
url: /ja/androidjava/basics-of-dom-api/
description: Aspose.PDF for Android via Java でも、PDF ドキュメントの構造をオブジェクトで表すために DOM の概念を使用します。この構造の説明はここで読むことができます。
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## DOM API の紹介

Document Object Model (DOM) は、構造化された文書をオブジェクト指向モデルとして表現する形式です。DOM は、プラットフォームおよび言語に依存しない方法で構造化文書を表現するための、World Wide Web Consortium (W3C) の公式標準です。

簡単に言うと、DOM は文書の構造を表すオブジェクトのツリーです。Aspose.PDF for Android via Java でも、PDF ドキュメントの構造をオブジェクトで表すために DOM の概念を使用します。ただし、DOM の要素（Elements など）の側面は、使用しているプログラミング言語の構文内で操作されます。DOM の公開インターフェイスは、そのアプリケーションプログラミングインターフェイス (API) で規定されています。

### PDFドキュメントの紹介

Portable Document Format（PDF）は文書交換のためのオープン標準です。PDFドキュメントはテキストとバイナリデータの組み合わせです。テキストエディタで開くと、ドキュメントの構造と内容を定義する生のオブジェクトが表示されます。

PDFファイルの論理構造は階層的で、ビューアアプリケーションがドキュメントのページとその内容を描画する順序を決定します。PDFは4つのコンポーネントで構成されています：オブジェクト、ファイル構造、ドキュメント構造、そしてコンテンツストリーム。

### PDFドキュメント構造

PDFファイルの構造が階層的であるため、Aspose.PDF for Javaも同様の方法で要素にアクセスします。以下の階層は、PDFドキュメントが論理的にどのように構成され、Aspose.PDF for Java DOM APIがそれをどのように構築するかを示しています。

![PDFドキュメント構造](https://docs.aspose.com/pdf/java/images/structure.png)

### PDFドキュメント要素へのアクセス

Document オブジェクトはオブジェクトモデルのルートレベルにあります。Aspose.PDF for Android via Java DOM API を使用すると、Document オブジェクトを作成し、階層内の他のすべてのオブジェクトにアクセスできます。Pages などのコレクションや Page のような個々の要素にアクセスすることもできます。DOM API は、以下に示すように PDF ドキュメントを操作するための単一のエントリポイントとエグジットポイントを提供します:

- PDF ドキュメントを開く
- DOM スタイルで PDF ドキュメント構造にアクセスする
- PDF ドキュメント内のデータを更新する
- PDF ドキュメントを検証する
- PDF ドキュメントをさまざまな形式にエクスポートする
- 最後に、更新された PDF ドキュメントを保存します

## 新しい Aspose.PDF for Android via Java API の使用方法

このトピックでは、新しい Aspose.PDF for Android via Java API を説明し、迅速かつ簡単に開始できるよう案内します。特定の機能の使用に関する詳細はこの記事の対象ではありませんのでご注意ください。

Aspose.PDF for Android via Java は 2 つの部分で構成されています：

- Aspose.PDF for Android via Java DOM API
- Aspose.PDF.Facades 

以下に、これらの各領域の詳細が示されています。

### Aspose.PDF for Android via Java DOM API

新しい Aspose.PDF for Android via Java DOM API は PDF 文書構造に対応しており、PDF 文書をファイルおよび文書レベルだけでなくオブジェクトレベルでも操作できるようにします。開発者が PDF 文書のすべての要素とオブジェクトにアクセスできる柔軟性を向上させました。Aspose.PDF DOM API のクラスを使用すると、プログラムから文書要素や書式設定にアクセスできます。この新しい DOM API は以下に示す複数の名前空間で構成されています：

### com.aspose.pdf

この名前空間は、PDF 文書を開いたり保存したりできる Document クラスを提供します。また、License クラスもこの名前空間の一部です。さらに、PDF ページ、添付ファイル、ブックマークに関連するクラス（例：com.aspose.pdf.Page、com.aspose.pdf.PageCollection、com.aspose.pdf.FileSpecification、com.aspose.pdf.EmbeddedFileCollection、com.aspose.pdf.OutlineItemCollection、com.aspose.pdf.OutlineCollection など）も提供します。

#### com.aspose.pdf.text

この名前空間は、テキストとそのさまざまな側面を扱うのに役立つクラスを提供します。たとえば com.aspose.pdf.Font、com.aspose.pdf.FontCollection、com.aspose.pdf.FontRepository、com.aspose.pdf.FontStyles、com.aspose.pdf.TextAbsorber、com.aspose.pdf.TextFragment、com.aspose.pdf.TextFragmentAbsorber、com.aspose.pdf.TextFragmentCollection、com.aspose.pdf.TextFragmentState、com.aspose.pdf.TextSegment および com.aspose.pdf.TextSegmentCollection などです。

#### com.aspose.pdf.TextOptions

この名前空間は、テキストの検索、編集、または置換のためにさまざまなオプションを設定できるクラスを提供します。たとえば com.aspose.pdf.TextEditOptions、com.aspose.pdf.TextReplaceOptions、 そして com.aspose.pdf.TextSearchOptions です。

#### com.aspose.pdf.PdfAction

この名前空間には、PDF ドキュメントのインタラクティブ機能を扱うのに役立つクラスが含まれています。たとえば、ドキュメントやその他のアクションの操作などです。この名前空間には、com.aspose.pdf.GoToAction、com.aspose.pdf.GoToRemoteAction と com.aspose.pdf.GoToURIAction などのクラスが含まれます。

#### com.aspose.pdf.Annotation

AnnotationsはPDFドキュメントのインタラクティブ機能の一部です。アノテーション用に専用の名前空間を用意しました。この名前空間には、アノテーションの操作を支援するクラスが含まれており、例えば com.aspose.pdf.Annotation、com.aspose.pdf.AnnotationCollection、com.aspose.pdf.CircleAnnotation、com.aspose.pdf.LinkAnnotation などがあります。

#### com.aspose.pdf.Form

この名前空間には、PDFフォームおよびフォームフィールドの操作を支援するクラスが含まれており、例えば com.aspose.pdf.Form、com.aspose.pdf.Field、com.aspose.pdf.TextBoxField、com.aspose.pdf.OptionCollection などがあります。

#### com.aspose.pdf.devices 

PDFドキュメントに対して、PDFをさまざまな画像形式に変換するなど、様々な操作を実行できます。ただし、これらの操作は Document オブジェクトに属さず、Document クラスを拡張してこれらの操作を行うことはできません。そのため、新しい DOM API では Device の概念を導入しました。

##### com.aspose.pdf.facades

Aspose.PDF for Java t.o.o が登場する以前は、既存の PDF ファイルを操作するために Aspose.PDF.Kit for Java が必要でした。古い Aspose.PDF.Kit のコードを実行するには、com.aspose.pdf.facades 名前空間を使用できます。

