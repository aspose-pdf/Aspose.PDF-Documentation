---
title: ASP - VBScript via COM Interop
type: docs
weight: 30
url: ja/net/asp-vbscript-via-com-interop/
---

## 前提条件

{{% alert color="primary" %}}

    「Use Aspose.pdf for .NET via COM Interop」という記事を確認してください。

{{% /alert %}}

## VB ScriptでのHello World! 例

{{% alert color="primary" %}}

これは、[Aspose.PDF for .NET](/pdf/net/) と VBScript を介して COM Interop を使用してサンプルテキストを含む PDF ファイルを作成する方法を示すシンプルなASPアプリケーションです。

{{% /alert %}}

```vb

<%@ LANGUAGE = VBScript %>
<% Option Explicit %>
<html>
    <head>
        <title>クラシカルASPサンプルでの Aspose.PDF for .NET の使用</title>
    </head>
<body>

<h3>クラシカルASPとVBScriptを使用してAspose.PDF for .NETでサンプルPDFドキュメントを作成</h3>

<%

'ライセンスを設定
Dim lic
Set lic = CreateObject("Aspose.PDF.License")
lic.SetLicense("D:\ASPOSE\Licences\Aspose.Total licenses\Aspose.Total.lic")

'空のコンストラクタを呼び出してPdfインスタンスをインスタンス化
Dim pdf
Set pdf = CreateObject("Aspose.PDF.Generator.Pdf")

'Pdfオブジェクトに新しいセクションを作成
Dim pdfsection
Set pdfsection = CreateObject("Aspose.PDF.Generator.Section")

'セクションをPdfオブジェクトに追加
pdf.Sections.Add(pdfsection)

'Textオブジェクトを作成
Dim SampleText
Set SampleText = CreateObject("Aspose.PDF.Generator.Text")

'テキストオブジェクトにテキストセグメントを追加
Dim seg1
Set seg1 = CreateObject("Aspose.PDF.Generator.Segment")

'セグメントにいくつかの内容を割り当て
seg1.Content = "HelloWorld using ASP and VBScript"

'段落にセグメント（赤いテキスト色）を追加
SampleText.Segments.Add(seg1)

'セクションの段落コレクションにテキスト段落を追加
pdfsection.Paragraphs.Add(SampleText)

'PDFドキュメントを保存
pdf.Save("d:\pdftest\HelloWorldinASP.pdf")

%>

    </body>
</html>
```
## VBScriptを使用したテキストの抽出

{{% alert color="primary" %}}
このVBScriptサンプルは、COMインターオペラビリティを介して既存のPDFドキュメントからテキストを抽出します。
エラー レンダリング マクロ 'code': lang パラメーターに無効な値が指定されました
{{% /alert %}}
