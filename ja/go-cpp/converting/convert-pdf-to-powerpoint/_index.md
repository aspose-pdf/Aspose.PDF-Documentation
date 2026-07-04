---
title: Go で PDF を PPTX に変換
linktitle: PDF を PowerPoint に変換
type: docs
weight: 30
url: /ja/go-cpp/convert-pdf-to-powerpoint/
lastmod: "2026-07-04"
description: Aspose.PDF を使用すると、Go で PDF を PPTX 形式に変換できます。
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF を PowerPoint に変換するための Golang ツール
Abstract: Aspose.PDF for Go via C++ は、元のレイアウト、書式設定、コンテンツ構造を保持しながら、PDF ドキュメントを PowerPoint（PPTX）形式に変換する信頼できるソリューションを提供します。この機能により、開発者は静的な PDF ファイルを動的で編集可能なプレゼンテーションにシームレスに変換できます。ライブラリは変換プロセスを制御するためのカスタマイズオプションを提供し、ビジネスやプロフェッショナルな利用に適した高品質な出力を保証します。ドキュメントには、開発者がアプリケーションに PDF から PowerPoint への変換機能を効率的に統合できるよう、ステップバイステップの指示とコードサンプルが含まれています。
SoftwareApplication: go-cpp
---

## PDF を PPTX に変換

提供された Go コードスニペットは、Aspose.PDF ライブラリを使用して PDF ドキュメントを PPTX に変換する方法を示しています。

1. PDF ドキュメントを開く。
1. PDF ファイルを PPTX に変換するには、 [SavePptx](https://reference.aspose.com/pdf/go-cpp/convert/savepptx/) function。
1. PDF ドキュメントを閉じ、割り当てられたリソースをすべて解放します。

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // SavePptX(filename string) saves previously opened PDF-document as PptX-document with filename
      err = pdf.SavePptX("sample.pptx")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**オンラインでPDFをPowerPointに変換してみる**

Aspose.PDF for Go は、オンラインの無料アプリケーションを提供します [\"PDF to PPTX\"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), 機能と品質を調べてみることができます。

[![Aspose.PDF を使用した無料アプリで PDF を PPTX に変換](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}