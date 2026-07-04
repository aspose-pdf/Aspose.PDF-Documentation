---
title: GoでPDFの背景色を設定する
linktitle: 背景色を設定する
type: docs
weight: 80
url: /ja/go-cpp/set-background-color/
description: GoでPDFファイルの背景色を設定する。
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Goを使用してPDFの背景色を設定する
Abstract: Aspose.PDF for Go via C++ は、PDF ページの背景色を設定する機能を提供し、開発者がドキュメントの外観をカスタマイズできるようにします。この機能により、ページ全体の背景に単色を適用でき、ドキュメントの視覚的な表現が向上します。開発者は RGB や CMYK などの標準カラーモデルを使用して、色の値を簡単に指定できます。ドキュメントには、C++ アプリケーション内で背景色のカスタマイズを効果的に実装するための詳細な手順とコードサンプルが提供されています。
SoftwareApplication: go-cpp
---

1. 提供されたコードスニペットは、Go で Aspose.PDF ライブラリを使用して PDF ファイルの背景色を設定する方法を示しています。
1. その [Open](https://reference.aspose.com/pdf/go-cpp/core/open/) メソッドは指定されたPDFファイルをメモリにロードし、外観やコンテンツの変更など、さらなる操作を可能にします。
1. その [SetBackground](https://reference.aspose.com/pdf/go-cpp/organize/setbackground/) メソッドはPDFドキュメントに新しい背景色を適用します。RGB値により、ユーザーはドキュメントのビジュアルスタイルをカスタマイズできます。
1. その [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) メソッドは更新された PDF を新しい名前で保存します。

このコードは、ブランド化されたレポートの作成、透かしの追加、または複数の文書間での視覚的一貫性の向上など、PDF カスタマイズを自動化する必要があるアプリケーションに最適です。

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
      // SetBackground(r, g, b int32) sets PDF-document background color
      err = pdf.SetBackground(200, 100, 101)
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_SetBackground.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```