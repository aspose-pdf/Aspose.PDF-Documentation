---
title: ASP - JScript via COM Interop
type: docs
weight: 40
url: /net/asp-jscript-via-com-interop/
---
{{% alert color="primary" %}}

これは、[Aspose.PDF for .NET](/pdf/net/) と JScript を COM Interop 経由で使用して、PDFファイルに単純なテキスト文字列を追加する方法を示すシンプルなASPアプリケーションです。

{{% /alert %}}

例:

{{% alert color="primary" %}}

```javascript
<%@ LANGUAGE = JScript %>
<html>
    <head>
        <title>Aspose.PDF for .NET を古典的なASPサンプルで使用</title>
    </head>
    <body>
        <h3>Aspose.PDF for .NET を使用して古典的なASPとJScriptでサンプルPDFドキュメントを作成</h3>
<%
// ライセンスを設定
var lic = Server.CreateObject("Aspose.PDF.License");
lic.SetLicense("D:\\ASPOSE\\Aspose.Total.lic");

// 空のコンストラクタを呼び出すことによりPdfインスタンスをインスタンス化
var pdf = Server.CreateObject("Aspose.PDF.Document");

// PDFオブジェクトに新しいページを作成
var pdfpage = pdf.Pages.Add();

// テキストフラグメントオブジェクトを作成
var sampleText = Server.CreateObject("Aspose.Pdf.Text.TextFragment");

// フラグメントにいくつかのコンテンツを割り当て
sampleText.Text = "HelloWorld using ASP and JScript";

// セクションのパラグラフコレクションにテキストパラグラフを追加
pdfpage.Paragraphs.Add(sampleText);

// PDFドキュメントを保存
pdf.Save("d:\\pdftest\\HelloWorldinASP.pdf");

%>
    </body>
</html>
```

```
{{% /alert %}}
```
