---
title: GoでPDFページを削除する
linktitle: PDFページを削除する
type: docs
weight: 30
url: /ja/go-cpp/delete-pages/
description: Aspose.PDF for Go via C++ を使用して、PDF ファイルからページを削除できます。
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Go を使用した PDF ページの削除
Abstract: Aspose.PDF for Go via C++ は、PDF 文書からページを削除するための効率的な機能を提供し、開発者が不要または不必要なページを容易に除去できるようにします。ライブラリは、ページ番号または範囲を指定することで単一ページまたは複数ページの削除を可能にし、正確な文書修正を保証します。この機能は、冗長なコンテンツを排除し、文書構造を最適化することで PDF ファイルをスリム化するのに役立ちます。ドキュメントには、開発者がアプリケーション内でページ削除機能を効果的に実装できるよう、ステップバイステップの手順とコードサンプルが提供されています。
SoftwareApplication: go-cpp
---

**Aspose.PDF for Go via C++** を使用して PDF ファイルからページを削除できます。次のコードスニペットは、特定のページを削除して PDF ドキュメントを操作する方法を示しています。この方法は、ページの削除、変更後のドキュメントの保存、および適切なリソース管理を確保するための、PDF ドキュメント操作タスクにおいて効率的です。

1. PDF ファイルを開く。
1. 特定のページを削除する [PageDelete](https://reference.aspose.com/pdf/go-cpp/core/pagedelete/) 関数。
1. ドキュメントを保存する [Save](https://reference.aspose.com/pdf/go-cpp/core/save/) メソッド。

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
      // PageDelete(num int32) deletes specified page in PDF-document
      err = pdf.PageDelete(1)
      if err != nil {
        log.Fatal(err)
      }
      // Save() saves previously opened PDF-document
      err = pdf.Save()
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```
