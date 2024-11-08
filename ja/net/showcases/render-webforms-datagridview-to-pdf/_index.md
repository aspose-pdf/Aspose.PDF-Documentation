---
title: WebForms DataGridViewをPDFにレンダリング
linktitle: WebForms DataGridViewをPDFにレンダリング
type: docs
weight: 20
url: /ja/net/render-webforms-datagridview-to-pdf/
description: このサンプルでは、Aspose.PDFライブラリを使用してWebFormをPDFにレンダリングする方法を示します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Aspose.PDF/Aspose.HTMLを使用してWebFormをPDFにエクスポートする方法

### はじめに

一般的に、WebFormをPDFドキュメントに変換するには追加のツールが必要です。このサンプルでは、Aspose.PDFライブラリを使用してWebFormをPDFにレンダリングする方法を示します。このサンプルにはAspose Export GridView To Pdf Controlも含まれており、_GridViewコントロールをPDFドキュメントにレンダリングする方法を示しています。_

## WebFormをPDFにレンダリングする方法

WebFormをPDFにレンダリングするための元のアイデアは、[System.Web.UI.Page](https://msdn.microsoft.com/en-US/library/System.Web.UI.Page.aspx)から継承されたヘルパークラスを作成し、Renderメソッドをオーバーライドすることです。

```csharp
void Render(HtmlTextWriter writer)
{
    if (RenderToPDF)
    {
        // PDFドキュメント用にWebページをレンダリング
    }
    else
    {
        // ブラウザでWebページをレンダリング
        base.Render(writer);
    }
}
```
HTMLをPDFにレンダリングするために使用できるAsposeツールは2つあります：

- Aspose.PDF for .NET
- Aspose Export GridView コントロール（Aspose.PDFに基づいています）

## ソースファイル

このサンプルには2つのデモレポートが含まれています。

- _Default.aspx_ は Aspose.PDF を使用してPDFへのエクスポートを示しています
- _Report2.aspx_ は Aspose Export GridView コントロールを使用してPDFへのエクスポートを示しています（Aspose.PDFに基づいています）

## 追加ファイル

`Helpers\PdfPage.cs` - Aspose.PDF APIの使用方法を示すヘルパークラスを含んでいます。

Aspose.Pdf.GridViewExport プロジェクトには、`Report2.aspx`でのデモンストレーションのために拡張された GridView コントロールが含まれています。
