---
title: Aspose.PDF DOM APIの基本
linktitle: DOM APIの基本
type: docs
weight: 120
url: ja/cpp/basics-of-dom-api/
description: Aspose.PDF for C++は、オブジェクトとしてPDFドキュメントの構造を表現するためにDOMの概念も使用します。ここでは、この構造の説明を読むことができます。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## DOM APIの紹介

Document Object Model (DOM)は、オブジェクト指向モデルとして構造化された文書を表現する形式です。DOMは、プラットフォームおよび言語に依存しない方法で構造化された文書を表現するための公式なWorld Wide Web Consortium (W3C)標準です。

簡単に言うと、DOMは、ある文書の構造を表すオブジェクトの木構造です。 Aspose.PDF for C++も、オブジェクトの観点からPDFドキュメントの構造を表現するためにDOMの概念を使用します。しかし、DOMの側面（その要素など）は、使用しているプログラミング言語の構文内で操作されます。DOMのパブリックインターフェイスは、そのアプリケーションプログラミングインターフェイス（API）で指定されています。

### PDFドキュメントへの導入

ポータブルドキュメントフォーマット（PDF）は、ドキュメント交換のためのオープンスタンダードです。PDFドキュメントは、テキストとバイナリデータの組み合わせです。テキストエディタで開くと、ドキュメントの構造と内容を定義する生のオブジェクトが表示されます。

PDFファイルの論理構造は階層的であり、ビューアアプリケーションがドキュメントのページとその内容を描画する順序を決定します。PDFは、オブジェクト、ファイル構造、ドキュメント構造、コンテンツストリームの4つのコンポーネントで構成されています。

### PDFドキュメント構造

PDFファイルの構造が階層的であるため、Aspose.PDF for C++も同様に要素にアクセスします。 以下の階層は、PDF ドキュメントが論理的にどのように構造化されているか、そして Aspose.PDF for C++ DOM API がそれをどのように構築するかを示しています。

![PDF Document Structure](../images/structure.png)

### PDF ドキュメント要素へのアクセス

Document オブジェクトは、オブジェクトモデルのルートレベルにあります。Aspose.PDF for C++ DOM API は、Document オブジェクトを作成し、その階層内の他のすべてのオブジェクトにアクセスできるようにします。Pages のようなコレクションや、Page のような個々の要素にアクセスすることができます。DOM API は、以下に示すように、PDF ドキュメントを操作するための単一のエントリーポイントと出口ポイントを提供します。

- PDF ドキュメントを開く
- DOM スタイルで PDF ドキュメント構造にアクセスする
- PDF ドキュメントのデータを更新する
- PDF ドキュメントを検証する
- PDF ドキュメントを異なる形式にエクスポートする
- 最後に、更新された PDF ドキュメントを保存する

## 新しい Aspose.PDF for C++ API の使用方法

このトピックでは、新しい Aspose.PDF for C++ API を説明し、迅速かつ簡単に始めるためのガイドを提供します。 この特定の機能の使用に関する詳細は、この記事の一部ではないことに注意してください。

Aspose.PDF for C++ は、2つの部分で構成されています：

- Aspose.PDF for C++ DOM API
- Aspose.PDF.Facades

これらの各分野の詳細は以下に示されています。

### Aspose.PDF for C++ DOM API

Aspose.PDF for C++ DOM API は、PDF ドキュメントの構造に対応しており、ファイルやドキュメントレベルだけでなく、オブジェクトレベルでも PDF ドキュメントを操作するのに役立ちます。開発者が PDF ドキュメントのすべての要素およびオブジェクトにアクセスするためのより柔軟な方法を提供しています。Aspose.PDF DOM API のクラスを使用して、ドキュメントの要素やフォーマットにプログラム的にアクセスすることができます。この新しい DOM API は、以下に示すようにさまざまな名前空間で構成されています：

### Aspose::Pdf Namespace Reference

この名前空間は、PDF ドキュメントを開いたり保存したりすることができる Document クラスを提供します。

#### Aspose::Pdf::Text Namespace Reference

この名前空間は、テキストおよびそのさまざまな側面（例えば、Font、FontCollection、FontRepository、FontSource、TextAbsorber、TextFragment、TextFragmentAbsorber、TextFragmentCollection、TextFragmentState、TextSegment、TextSegmentCollection など）を操作するのに役立つクラスを提供します。
#### Aspose::Pdf::Collections Namespace Reference

この名前空間は、クラスAsposeHashDictionaryを提供します。

#### Aspose::Pdf::CommonData Namespace Reference

#### Aspose::Pdf::Diagnostics Namespace Reference

#### Aspose::Pdf::Drawing Namespace Reference

この名前空間は、Curve、Circle、Arc、Rectangle、Graphなどのクラスを提供し、PDFファイルにグラフィック要素を追加します。

#### Aspose::Pdf::Engine Namespace Reference

この名前空間は、Addressing、Interactive、Security、CommonData、IO、Presentationクラスを提供します。

#### Aspose::Pdf::GroupProcessor Namespace Reference

この名前空間は、クラスExtractorFactory - IPdfTypeExtractorオブジェクトを作成するためのファクトリを表す、IDocumentPageTextExtractor、IDocumentTextExtractor、IPdfTypeExtractorクラス - エクストラクタとのインターフェースを表すものを提供します。

#### Aspose::Pdf::Interchange Namespace Reference

#### Aspose::Pdf::LogicalStructure Namespace Reference

この名前空間は、AnnotationElement、AttributeOwnerStandard、CaptionElement、DocumentElement、FormElement、GroupingElement、ILSTextElement、PrivateElement、WarichuWTElementなどのクラスを提供します。

#### Aspose::Pdf::Operators Namespace Reference

この名前空間は次のオペレーターのクラスを提供します：BasicSetColorAndPatternOperator、BlockTextOperator、SetCharWidthBoundingBox、SetColorStroke、SetHorizontalTextScaling、SetTextRenderingMode、TextShowOperator、など。

#### Aspose::Pdf::Optimization Namespace Reference

この名前空間は2つのクラスを提供します - ImageCompressionOptionsとOptimizationOptions。

#### Aspose::Pdf::PageModel Namespace Reference

#### Aspose::Pdf::PdfAOptionClasses Namespace Reference

この名前空間は2つのクラスを提供します：FontEmbeddingOptions - PDF/A標準は、すべてのフォントがドキュメントに埋め込まれている必要があると要求します。このクラスには、フォントが宛先PCに存在しないためにフォントを埋め込むことができない場合のフラグが含まれています。ToUnicodeProcessingRules - このクラスは、「テキストをUnicodeにマップできません」というAdobe Preflightエラーを解決するために使用できるルールを説明します。

#### Aspose::Pdf::Sanitization Namespace Reference

この名前空間は2つのクラスを提供します：Details_SanitizationExceptionとIRecovery。

#### Aspose::Pdf::Tagged Namespace Reference

この名前空間は、クラス Details_TaggedException - ドキュメントのTaggedPDFコンテンツに対する例外を表します。ITaggedContent - ドキュメントのTaggedPdfコンテンツを操作するためのインターフェースを表します。そして、TaggedPdfExceptionCodeです。

#### Aspose::Pdf::Validation Namespace Reference

#### Aspose::Pdf::XfaConverter Namespace Reference

この名前空間は、関連データのカプセル化を処理するクラス XfaParserOptions を提供します。

#### Aspose::Pdf::Annotations Namespace Reference

注釈はPDFドキュメントのインタラクティブ機能の一部です。注釈に特化した名前空間を用意しています。この名前空間には、注釈を操作するのに役立つクラスが含まれています。例えば、Annotation、AnnotationCollection、CircleAnnotation、LinkAnnotationなどです。

#### Aspose::Pdf::Forms Namespace Reference

この名前空間には、PDFフォームおよびフォームフィールドを操作するのに役立つクラスが含まれています。例えば、Form、Field、TextBoxField、OptionCollectionなどです。

#### Aspose::Pdf::Devices Namespace Reference

We can perform various operations on the PDF documents such as converting PDF document to various image formats. However, such operations do not belong to the Document object and we cannot extend the Document class for such operations. That's why we have introduced the concept of the Device in the new DOM API.

##### Aspose::Pdf::Facades Namespace Reference

You can use Aspose.PDF.Facades namespace. This Namespace provides classes AutoFiller - represents a class to receive data from database or other datasource. Bookmark, Form, Stamp, PdfConverter anr more classes.

さまざまな画像形式に変換するなど、PDF ドキュメントに対してさまざまな操作を実行できます。ただし、そのような操作は Document オブジェクトに属しておらず、そのような操作のために Document クラスを拡張することはできません。そこで、新しい DOM API で Device の概念を導入しました。

##### Aspose::Pdf::Facades 名前空間リファレンス

Aspose.PDF.Facades 名前空間を使用できます。この名前空間は、AutoFiller クラスを提供します。これは、データベースやその他のデータソースからデータを受信するクラスを表します。ブックマーク、フォーム、スタンプ、PdfConverter などのクラス。