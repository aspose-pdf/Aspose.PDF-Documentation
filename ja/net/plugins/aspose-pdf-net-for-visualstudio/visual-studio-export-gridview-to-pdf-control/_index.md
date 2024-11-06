---
title: Visual Studio Export GridView To PDF コントロール
type: docs
weight: 10
url: ja/net/visual-studio-export-gridview-to-pdf-control/
---

## はじめに

Export GridView To Pdf コントロールは、ASP.NET サーバーコントロールであり、GridView の内容を [Aspose.PDF](http://www.aspose.com/.net/pdf-component.aspx) を使用して Pdf ドキュメントにエクスポートすることができます。これは GridView コントロールの上部に **Pdf へエクスポート** ボタンを追加します。このボタンをクリックすると、GridView コントロールの内容が動的に Pdf ドキュメントにエクスポートされ、その後エクスポートされたファイルが数秒でユーザーが選択したディスクの場所に自動的にダウンロードされます。

### モジュールの特徴

この初期バージョンのコントロールは、次の機能を提供します：

- 編集、共有、印刷に非常に人気のある Pdf ドキュメントで、お気に入りのオンライン GridView コンテンツのオフラインコピーを取得します。
- デフォルトの ASP.NET GridView コントロールから継承されているため、そのすべての機能とプロパティを持っています。
- .NET 2.0 から始まるすべての .NET バージョンで動作します。
- エクスポートボタンのテキストをカスタマイズ/ローカライズする機能。
- エクスポートボタンのテキストをカスタマイズ/ローカライズする機能。
- GridViewの内容が広く、デフォルトのポートレートモードでは収まらない場合に、ランドスケープモードでエクスポートするオプション。
- CSSを使用してエクスポートボタンに独自のテーマの外観を適用。
- エクスポートされたドキュメントの上部にカスタム見出しを追加するオプション。
- 設定可能なディスクパスにサーバー上で各エクスポートされたドキュメントを保存するオプション。
- ページングが有効な場合に、現在のページまたはすべてのページをエクスポートするオプション。

## システム要件とサポートされるプラットフォーム

### システム要件

Export GridView To Pdf Control for Visual Studioは、IISと.NETフレームワーク2.0以上がインストールされている任意のシステムで使用できます。

### サポートされるプラットフォーム

Export GridView To Pdf Control for Visual Studioは、.NETフレームワーク2.0以上を実行しているすべてのバージョンのASP.NETでサポートされています。このコントロールをASP.NETアプリケーションで使用するために、以下のいずれかのVisual Studioバージョンを使用できます。

- Visual Studio 2005
- Visual Studio 2008
- Visual Studio 2010
- Visual Studio 2012
- Visual Studio 2013

## ダウンロード
## ダウンロード

以下の場所のいずれかからExport GridView To Pdfコントロールをダウンロードできます

- [CodePlex](https://asposevs.codeplex.com/releases/view/617022)
- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-.NET/releases/tag/AsposeExportGridViewToPdfControl_1.0)

## インストール

Export GridView To Pdfコントロールのインストールは非常にシンプルで簡単です。以下の簡単な手順に従ってください

### **Visual Studio 2010、2012、2013用**

1. ダウンロードしたzipファイル（Aspose.PDF.GridViewExport_1.0.zip）を解凍します。
1. VSIXファイルAspose.PDF.GridViewExport.vsixをダブルクリックします。
1. 使用可能でサポートされているインストールされているVisual Studioのバージョンを示すダイアログが表示されます。
1. Export GridView To Pdfコントロールを追加したいバージョンを選択します。
1. インストールをクリックします。

インストールが完了すると、成功ダイアログが表示されます。

**注:** 変更を有効にするには、Visual Studioを再起動してください。

### **Visual Studio 2005、2008およびExpressエディション用**

以下の手順に従って、他のASP.NETコントロールと同様に、Visual Studioで簡単にドラッグアンドドロップできるようにExport GridView To Pdfコントロールを統合してください。
Visual Studioで他のASP.NETコントロールのようにドラッグアンドドロップで簡単に統合できるように、Export GridView To Pdfコントロールを統合するために以下のステップに従ってください。

1. ダウンロードしたzipファイルを解凍します。すなわち、Aspose.PDF.GridViewExport.NET2.0_1.0.zip
1. Visual Studioを管理者として実行していることを確認してください

ツールメニューで、ツールボックス項目の選択をクリックします。

1. 参照をクリックします。
   「開く」ダイアログボックスが表示されます。
1. 解凍したフォルダに移動し、Aspose.PDF.GridViewExport.dllを選択します。
1. OKをクリックします。

aspxまたはascxコントロールを左側のツールボックスで開くと、一般タブの下にExportGridViewToPdfが表示されます。

![todo:image_alt_text](visual-studio-export-gridview-to-pdf-control_2.png)

## 使用方法

インストール後、ASP.NETアプリケーションでこのコントロールを使用するのは非常に簡単です

|**.NET framework 4.0以上の場合**|**.NET framework 2.0以上の場合**|** |
| :- | :- | :- |
|Visual Studio 2010以上で.NET framework 4.0以上で実行されているアプリケーションでは、ツールバーのAsposeタブに**ExportGridViewToPdf**コントロールが表示されるはずです。
.NETフレームワーク4.0以降で動作するアプリケーションにおいて、Visual Studio 2010以降を使用している場合、以下に示すようにツールバーの**Aspose**タブに**ExportGridViewToPdf**コントロールが表示されるはずです。

### ExportGridViewToPdfコントロールを手動で追加する

Visual Studioのツールボックスを使用する上記の方法に問題がある場合、.NETフレームワーク2.0以上で動作するASP.NETアプリケーションにこのコントロールを手動で追加することができます。

1. Visual Studioを使用している場合は、管理者として実行してください
1. ASP.NETプロジェクトまたはWebアプリケーションに、ダウンロードパッケージから抽出した**Aspose.PDF.GridViewExport.dll**への参照を追加します。このフォルダに対してWebアプリケーション/Visual Studioが完全なアクセス権を持っていない場合、アクセス拒否の例外が発生する可能性があります。
1. 以下の行をページ、コントロールまたはMasterPageの先頭に追加します。

```csharp
 <%@ Register assembly="Aspose.PDF.GridViewExport" namespace="Aspose.PDF.GridViewExport" tagprefix="aspose" %>
```
```csharp
 <aspose:ExportGridViewToPdf ID="ExportGridViewToPdf1" runat="server"></aspose:ExportGridViewToPdf>
```

### FAQs

よくある質問とこのコントロールの使用中に直面する可能性がある問題

<div class="schema-faq-code" itemscope="" itemtype="https://schema.org/FAQPage">
    <div itemscope="" itemprop="mainEntity" itemtype="https://schema.org/Question" class="faq-question">
        <h3 itemprop="name" class="faq-q">1. ToolboxにExportGridViewToPdfコントロールが表示されません</h3>
        <div itemscope="" itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
             <div itemprop="text" class="faq-a">
               <p><strong>Visual Studio 2010以降</strong></p>
<ol><li>ダウンロードしたパッケージに含まれるVSIX拡張ファイルを使用してこのコントロールをインストールしたことを確認してください。確認するには、ツール -&gt; 拡張機能と更新に移動します。インストールされている項目の下で 'Aspose Export Export GridView To Pdf Control' を見るはずです。表示されない場合は、再インストールを試してください</li>
<li>.NETフレームワーク4.0以上でWebアプリケーションが動作していることを確認してください。それ以下の.NETフレームワークのバージョンの場合は、上記の代替方法を確認してください。</li>

- Webアプリケーションが.NETフレームワーク4.0以上で動作していることを確認してください。それ以下のバージョンの.NETフレームワークの場合は、上記の代替方法を確認してください。
- 以前のバージョンの Visual Studio
- 上記の指示に従って、このコントロールをツールボックスに手動で追加したことを確認してください。

2. アプリケーションの実行時に「アクセスが拒否されました」というエラーが発生しています
- この問題が本番環境で発生している場合、Aspose.PDF.dll と Aspose.PDF.GridViewExport.dll の両方を bin フォルダにコピーしていることを確認してください。
- Visual Studioを使用している場合は、すでに管理者としてログインしている場合でも、管理者として実行することを確認してください。
```

<div>
    <div>
        <div>
            <div>
               <ol>
                <li>Visual Studioを使用する場合は、管理者としてすでにログインしている場合でも、管理者として実行するようにしてください。</li>
               </ol>
            </div>
        </div>
    </div>
</div>

### **Aspose .NET Export GridView To Pdf コントロールのプロパティ**

このコントロールが提供するクールな機能を設定および使用するために公開されているプロパティは次のとおりです

|**プロパティ名**|**タイプ**|**例/可能な値**|**説明**|
| :- | :- | :- | :- |
|ExportButtonText|string|Export to Pdf|既定のテキストを上書きするためにこのプロパティを使用できます|
|ExportButtonCssClass|string|btn btn-primary|エクスポートボタンの外側のdivに適用されるCssクラス。ボタンにcssを適用するには、.yourClass inputを使用できます|
|ExportInLandscape|bool|true or false|trueの場合、出力ドキュメントの向きをランドスケープに変更します。デフォルトはポートレートです|
| | | | |
|ExportFileHeading|string|GridView Export Example Report|見出しにスタイルを追加するためにhtmlタグを使用できます|
|ExportOutputPathOnServer|string|c:/temp|エクスポートのコピーが自動的に保存されるサーバー上のローカル出力ディスクパス|
```
|ExportOutputPathOnServer|string|c:/temp|サーバー上のローカル出力ディスクパス。ここにエクスポートのコピーが自動的に保存されます。
|ExportDataSource|object|allRowsDataTable|このデータバインドコントロールがデータ項目のリストを取得するオブジェクトを設定します。オブジェクトにはエクスポートする必要があるすべてのデータを含む必要があります。このプロパティは通常のDataSourceプロパティに加えて使用され、カスタムページングが有効にされていて現在のページが画面に表示される行のみを取得する場合に便利です。
|LicenseFilePath|string| |サーバー上のライセンスファイルへのローカルパス。例：c:/inetpub/Aspose.PDF.lic|

以下に示すのは、すべてのプロパティを使用したExport GridView to Pdfコントロールの例です。

```csharp
<aspose:ExportGridViewToPdf Width="800px" ID="ExportGridViewToPdf1" ExportButtonText="Export to Pdf"
    CssClass="table table-hover table-bordered" ExportButtonCssClass="myClass" ExportOutputFormat="Doc"
    ExportInLandscape="true" ExportOutputPathOnServer="c:\\temp" ExportFileHeading="<h4>Example Report</h4>"
    OnPageIndexChanging="ExportGridViewToPdf1_PageIndexChanging" PageSize="5" AllowPaging="True"
    LicenseFilePath="c:\\inetpub\\Aspose.PDF.lic"
    runat="server" CellPadding="4" ForeColor="#333333" GridLines="Both">
</aspose:ExportGridViewToPdf>
```
## ビデオデモ

以下の[ビデオ](https://www.youtube.com/watch?v=WNJ7T8u4JlM)をご覧ください。

### サポート

Asposeの初期から、良い製品を提供するだけでは十分ではないと考えていました。良いサービスを提供することも必要でした。私たちは自身も開発者であり、技術的な問題やソフトウェアの癖が作業を妨げるときのイライラを理解しています。私たちは問題を解決するためにここにいます。

これが、無料サポートを提供する理由です。製品を購入した人も、評価版を使用している人も、全てのユーザーに同じ注意と尊敬を払います。

以下のプラットフォームを使用して、このPdfに関連する問題や提案をログすることができます。

- [CodePlex](https://asposevs.codeplex.com/workitem/list/basic)
- [Visual Studio Gallery - Q and A](https://visualstudiogallery.msdn.microsoft.com/fb8b9944-cfe5-44a9-8aa7-c785d32d1066)
- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-.NET/issues)
- [Microsoft Developer Network - Q and A](https://code.msdn.microsoft.com/Aspose-NET-Export-GridView-caddbb6d/view/Discussions#content)
- [Microsoft Developer Network - Q and A](https://code.msdn.microsoft.com/Aspose-NET-Export-GridView-caddbb6d/view/Discussions#content)

### 拡張と貢献

Aspose .NET Export GridView To Pdf for Visual Studioはオープンソースであり、そのソースコードは以下にリストされている主要なソーシャルコーディングウェブサイトで入手できます。開発者はソースコードをダウンロードし、自分の要件に応じて機能を拡張することを奨励されます。

#### ソースコード

以下の場所のいずれかから最新のソースコードを入手できます

- [CodePlex](https://asposevs.codeplex.com/SourceControl/latest#Aspose.PDF.GridViewExport/)
- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-.NET/tree/master/Plugins/Visual%20Studio/Aspose.PDF.GridViewExport)

#### ソースコードの設定方法

ソースコードを開いて拡張するためには、以下のものをインストールしておく必要があります

- Visual Studio 2010

これらの簡単な手順に従って開始してください

1. ソースコードをダウンロード/クローンします。
1.
1.
1. ダウンロードした最新のソースコードを参照し、**Aspose.PDF.GridViewExport.sln** を開きます。

#### ソースコードの概要

ソリューションには三つのプロジェクトが含まれています

- Aspose.PDF.GridViewExport - VSIXパッケージと.NET 4.0用のServer Pdfを含んでいます。
- Aspose.PDF.GridViewExport_DotNet_2.0 - .NET 2.0用の拡張GridView Pdf
- Aspose.PDF.GridViewExport.Website - Word Exportable GridView PdfをテストするためのWebプロジェクトです。
