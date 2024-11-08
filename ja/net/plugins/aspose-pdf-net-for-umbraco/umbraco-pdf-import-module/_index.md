---
title: Umbraco PDFインポートモジュール
type: docs
weight: 10
url: /ja/net/umbraco-pdf-import-module/
description: Umbraco PDFインポートモジュールのインストールと使用方法について学ぶ
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## はじめに

**Aspose.PDF for .NET**は、PDF文書の作成と操作を行うコンポーネントであり、あなたの.NETアプリケーションがAdobe Acrobatを使用することなく、既存のPDF文書を読み書きし、操作することを可能にします。また、フォームを作成し、PDF文書に埋め込まれたフォームフィールドを管理することもできます。

**Aspose.PDF for .NET**は手頃な価格で、PDF圧縮オプション; テーブルの作成と操作; グラフオブジェクトのサポート; 広範なハイパーリンク機能; 拡張セキュリティコントロール; カスタムフォント処理; データソースとの統合; ブックマークの追加や削除; 目次の作成; 添付ファイルや注釈の追加、更新、削除; PDFフォームデータのインポートまたはエクスポート; テキストや画像の追加、置換、削除; ページの分割、連結、抽出、挿入; ページを画像に変換; PDF文書の印刷など、信じられないほど豊富な機能を提供します。
**Aspose.PDF for .NET** は手頃な価格で、PDFの圧縮オプション、表の作成と操作、グラフオブジェクトのサポート、広範なハイパーリンク機能、拡張セキュリティコントロール、カスタムフォントの処理、データソースとの統合、ブックマークの追加または削除、目次の作成、添付ファイルと注釈の追加、更新、削除、PDFフォームデータのインポートまたはエクスポート、テキストと画像の追加、交換または削除、ページの分割、連結、抽出または挿入、ページを画像に変換、PDFドキュメントの印刷など、信じられないほど豊富な機能を提供します。

### **モジュール機能**

Umbraco PDF Import は、開発者が他のソフトウェアを必要とせずに任意のPDFドキュメントの内容を取得/読み取ることを可能にする [Aspose](http://www.aspose.com/) からのオープンソースアドオンです。
Umbraco PDF インポートは、他のソフトウェアが必要なく、任意のPDFドキュメントの内容を読み取ることができる [Aspose](http://www.aspose.com/) からのオープンソースアドオンです。

## システム要件とサポートされるプラットフォーム

### **システム要件**

Aspose .NET Pdf インポートのUmbracoモジュールをセットアップするには、以下の要件を満たす必要があります:

- Umbraco 6.0 +

他のバージョンのUmbracoにこのモジュールをインストールしたい場合は、お気軽にお問い合わせください。

### **サポートされるプラットフォーム**

このモジュールはすべてのバージョンでサポートされています

- ASP.NET 4.0で動作するUmbraco

## ダウンロード

次の場所のいずれかからAspose .NET Pdf インポート for Umbracoをダウンロードできます

- [CodePlex](https://asposeumbraco.codeplex.com/releases)
- [Github](https://github.com/asposemarketplace/Aspose_for_Umbraco/releases)
- [Sourceforge](https://sourceforge.net/projects/asposeumbraco/files/)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-umbraco/downloads)
- [Umbraco](https://our.umbraco.org/projects/developer-tools/import-from-pdf-using-aspose-pdf)
 - [Umbraco](https://our.umbraco.org/projects/developer-tools/import-from-pdf-using-aspose-pdf)

## インストール

ダウンロードしたら、次の手順に従ってこのパッケージをUmbracoウェブサイトにインストールしてください：

1. 例えば <http://www.myblog.com/umbraco/> にログインして、Umbracoの**開発者**セクションにアクセスします。
1. ツリーから**パッケージ**フォルダを展開します。
   ここからパッケージをインストールする方法は二つあります：**ローカルパッケージをインストール**を選択するか、**Umbracoパッケージリポジトリ**をブラウズします。
1. **ローカルパッケージ**をインストールする場合は、パッケージを解凍せずにUmbracoにzipをロードします。
1. 画面の指示に従ってください。

**注記：** インストール時に「最大リクエスト長を超えました」のエラーが発生することがあります。Umbracoのweb.configファイルの「maxRequestLength」値を更新することで、この問題を簡単に修正できます。

```xml
  <httpRuntime requestValidationMode="2.0" enableVersionHeader="false" maxRequestLength="25000" />
```

## 使用方法

マクロをインストールした後、ウェブサイトで使用を開始するのは非常に簡単です：

1. 
1.
1. 画面の左下にあるセクション一覧から**設定**をクリックします。
1. **テンプレート**ノードを展開し、マクロを追加したいテンプレートを選択します。例えばブログ投稿など。
1. ボタンを追加したい選択したテンプレートの位置を選択します。
1. 上部リボンの**マクロを挿入**をクリックします。
1. **マクロを選択**からインストールされたマクロを選択し、**OK**をクリックします。

テンプレートが正常に追加されました。**Pdfからインポート**というタイトルのボタンが、このテンプレートを使用して作成されたすべてのページに表示されるようになりました。誰でもこのボタンをクリックするだけで、PDFドキュメントの内容をインポートできます。

## ビデオデモ

以下の[ビデオ](https://www.youtube.com/watch?v=zmZTJ86B25E)でモジュールの動作をご覧ください。

## サポート、拡張、貢献

### サポート

Asposeの初期から、良い製品を提供するだけでは十分ではないと認識していました。
Asposeの初期から、私たちは単に良い製品を提供するだけでは十分でないことを知っていました。

これが私たちが無料サポートを提供する理由です。製品を購入した人も評価版を使用している人も、全員が私たちの完全な注意と尊敬に値します。

以下のプラットフォームを使用して、Aspose.PDF .NET for Umbraco Modulesに関連する問題や提案をログに記録できます。

- [CodePlex](https://asposeumbraco.codeplex.com/workitem/list/basic)
- [Github](https://github.com/asposemarketplace/Aspose_for_Umbraco/issues)
- [Sourceforge](https://sourceforge.net/p/asposeumbraco/tickets/?source=navbar)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-umbraco/issues?status=new&status=open)

#### Pdfからのインポート

- [Microsoft Developer Network - Q and A](https://code.msdn.microsoft.com/Umbraco-Import-from-Pdf-d4659bc8/view/Discussions#content)

### 拡張と貢献

Aspose .NET PDF Import for Umbracoはオープンソースであり、そのソースコードは下記の主要なソーシャルコーディングウェブサイトで入手可能です。
Aspose .NET PDF Import for Umbracoはオープンソースで、そのソースコードは以下にリストされた主要なソーシャルコーディングウェブサイトで利用可能です。

#### ソースコード

以下の場所のいずれかから最新のソースコードを取得できます

- [CodePlex](https://asposeumbraco.codeplex.com/SourceControl/latest)
- [Github](https://github.com/asposemarketplace/Aspose_for_Umbraco)
- [Sourceforge](https://sourceforge.net/p/asposeumbraco/code/ci/master/tree/)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-umbraco/src)

#### ソースコードの設定方法

ソースコードを開いて拡張するためには、以下がインストールされている必要があります

- Visual Studio 2010 以降

次の簡単な手順に従って始めてください

1. ソースコードをダウンロード/クローンします。
1. Visual Studio 2010 を開き、**ファイル** > **プロジェクトを開く**を選択します
1. ダウンロードした最新のソースコードを参照し、**Aspose.Import from PDF.sln**を開きます

type: docs
changefreq: "monthly"
