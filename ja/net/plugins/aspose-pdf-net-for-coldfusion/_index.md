---
title: Aspose.Pdf for .NETをColdfusionで使用する方法
type: docs
weight: 300
url: /ja/net/using-aspose-pdf-for-net-with-coldfusion/
description: Aspose.Pdf for .NETとColdfusionをPdfFileInfoクラスを使用して作業する必要があります
lastmod: "2021-07-14"
draft: false
---

{{% alert color="primary" %}}

この記事では、Aspose.PDF for .NETをColdfusionと一緒に使用する方法について説明します。Aspose.PDF for .NetとColdfusionの統合の詳細を理解するのに役立ちます。簡単な例を用いて、Aspose.PDF for .Netの機能をColdfusionアプリケーションに組み込むプロセスを示します。

{{% /alert %}}

## 背景

Aspose.PDF for .NETは、既存のPDFファイルを編集・操作する機能も提供するコンポーネントです。
Aspose.PDF for .NETは、既存のPDFファイルを編集および操作する機能も提供するコンポーネントです。

## 前提条件

Aspose.PDF for .NetをColdfusionで動かすためには、IIS、.Net 2.0、およびColdfusionが必要です。私はIIS 5、.Net 2.0、Coldfusion 8を使用してコンポーネントをテストしました。Coldfusionをインストールする際には、もう二つ確認する必要があります。まず、IISのどのサイトでColdfusionが動作するかを指定する必要があります。次に、Coldfusionインストーラーから「.Net Integration Services」を選択する必要があります。.Net Integration Servicesは、Coldfusionアプリケーションで.Netコンポーネントアセンブリにアクセスすることを可能にします。この場合、コンポーネントはAspose.PDF for .NETになります。

## 説明

まず、後で使用するためにDLL（Aspose.PDF .dll）をアクセスする場所にコピーする必要があります。これはパスとして設定され、以下に示すようにcfobjectタグのassembly属性に割り当てられます：

```html
<cfobject type = ".NET" name = "fileinfo" 
        class = "Aspose.PDF.Facades.PdfFileInfo" 
        assembly = "C:/Aspose/Net/Assembly/Aspose.PDF.dll">
```
上記のタグの属性クラスはAspose.PDF.Facadesクラスを指しており、この場合はPdfFileInfoです。name属性はクラスのインスタンス名であり、後でコードでクラスのメソッドやプロパティにアクセスするために使用されます。Type属性はコンポーネントのタイプを指定します - このケースでは.Netです。

Coldfusionで.Netコンポーネントを使用する際に覚えておくべき重要な点は、クラスオブジェクトのプロパティを取得または設定するとき、特定の構造に従う必要があることです。プロパティを設定するにはSet_propertynameのような構文を使用し、プロパティ値を取得するにはGet_propertynameを使用します。

例えば

プロパティ値を設定する：

```html
<cfset FilePath = ExpandPath("guide.pdf")>
```

プロパティ値を取得する：

```html
<cfoutput>#fileinfo.Get_title()#</cfoutput>
```

ColdfusionでAspose.PDF for .NETを使用するプロセスを理解するための基本的で完全な例を以下に示します。

### PDFファイル情報を表示しましょう

```html
<!--- PdfFileInfoクラスのインスタンスを作成 --->

<cfobject type = ".NET" name = "fileinfo" class = "Aspose.PDF.Facades.PdfFileInfo"

assembly = "C:/Aspose/Net/Assembly/Aspose.PDF.dll">

<!--- pdfファイルパスを取得 --->

<cfset FilePath = ExpandPath("guide.pdf")>

<!--- pdfファイルパスをクラスオブジェクトに割り当てて、inputfileプロパティを設定 --->

<cfset fileinfo.Set_inputfile(FilePath)>

<!--- ファイル情報を表示 --->

<cfoutput><b>タイトル:</b>#fileinfo.Get_title()#</cfoutput><br/>
<cfoutput><b>主題:</b>#fileinfo.Get_subject()#</cfoutput><br/>
<cfoutput><b>著者:</b>#fileinfo.Get_author()#</cfoutput><br/>
<cfoutput><b>作成者:</b>#fileinfo.Get_Creator()#</cfoutput><br/>

```
## 結論

{{% alert color="primary" %}}
この記事では、Coldfusionと.Netの統合の基本的なルールに従えば、ColdfusionアプリケーションでAspose.PDF for .NETを使用して、PDFドキュメントの操作に関連する多くの機能と柔軟性を取り入れることができることを見てきました。
{{% /alert %}}
