---
title: ASP.NETをVisual Studioを使わずに
type: docs
weight: 60
url: ja/net/asp-net-without-using-visual-studio/
---

{{% alert color="primary" %}}

[Aspose.PDF for .NET](/pdf/net/)を使って、Visual Studioを使用せずにASP.NETページやアプリケーションを開発することができます。この例では、HTMLとC#またはVB.NETのコードを1つの.aspxファイルに書き込む方法を紹介します。これは一般にインスタントASP.NETとして知られています。

{{% /alert %}}

## 実装の詳細

{{% alert color="primary" %}}

サンプルWebアプリケーションを作成し、Aspose.PDF.dllをウェブサイトディレクトリの"Bin"というディレクトリにコピーします（*binフォルダが存在しない場合は、作成してください*）。次に、.aspxページを作成し、以下のコードをコピーしてください。
この例では、[Aspose.PDF for .NET](/pdf/net/)をASP.NETページでインラインコードと共に使用し、サンプルテキストを含むシンプルなPDFドキュメントを作成する方法を示しています。
{{% /alert %}}

```cs

<%@ Page Language ="C#" %>
<%@ Import Namespace="System" %>
<%@ Import Namespace="System.IO" %>
<%@ Import Namespace="System.Data" %>
<%@ Import Namespace="Aspose.PDF" %>

<html>
    <head>
        <title> Aspose.PDF for .NETを使用したインラインASP.NET</title>
    </head>
    <body>
        <h3>Aspose.PDF for .NETを使用したインラインASP.NETでのシンプルなPDFドキュメントの作成</h3>
<%
    // ライセンス設定
    Aspose.PDF.License lic = new Aspose.PDF.License();
    lic.SetLicense("D:\\ASPOSE\\Licences\\Aspose.Total licenses\\Aspose.Total.lic");

    // ドキュメントオブジェクトの初期化
    Document document = new Document();
    // ページ追加
    Page page = document.Pages.Add();
    // 新しいページにテキストを追加
    page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
    // 更新されたPDFを保存
    var outputFileName = Path.Combine(_dataDir, "HelloWorld_out.pdf");
    document.Save( outputFileName );
%>

    </body>
</html>
```

