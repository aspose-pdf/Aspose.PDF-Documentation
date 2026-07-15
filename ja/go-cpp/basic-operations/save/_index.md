---
title: PDFドキュメントをプログラムで保存する
linktitle: PDFを保存
type: docs
weight: 30
url: /ja/go-cpp/save-pdf-document/
description: C++ を使用した Aspose.PDF for Go で PDF ファイルを保存する方法を学びましょう。
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: C++ を使用した Aspose.PDF for Go で PDF ドキュメントを保存する
Abstract: Aspose.PDF for Go via C++ は、さまざまな形式や場所に PDF ドキュメントを高い効率と柔軟性で保存するための包括的な機能を提供します。このライブラリにより、開発者は PDF をファイルシステムやメモリストリームに保存したり、DOCX、XLSX、画像などの代替形式で出力したりできます。保存パラメータのカスタマイズ、ファイルサイズの最適化、データの完全性の確保といったオプションも用意されています。ドキュメントには、開発者がアプリケーションで PDF 保存機能を効率的に実装できるように、詳細な手順とコードサンプルが含まれています。
SoftwareApplication: go-cpp
---

## PDF ドキュメントをファイルシステムに保存する

この例では、[New](https://reference.aspose.com/pdf/go-cpp/core/new/) メソッドを使用して新しい PDF ドキュメントを作成する方法を示します。これにより、レポートや請求書などのドキュメントを動的に作成するための基本的な機能が提供されます。

コードはシンプルで、PDF ファイルにテキスト、画像、注釈を追加するなど、より複雑な機能のテンプレートとして使用できます。

この例では、Aspose.PDF Go ライブラリの基本的な使用方法を示し、ドキュメントの作成、変更、保存の機能を紹介します。

[Save As](https://reference.aspose.com/pdf/go-cpp/core/saveas/) メソッドを使用して、新しい PDF ドキュメントを保存します。

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
        // New creates a new PDF-document
        pdf, err := asposepdf.New()
        if err != nil {
            log.Fatal(err)
        }
        // SaveAs(filename string) saves previously opened PDF-document with new filename
        err = pdf.SaveAs("sample_New_SaveAs.pdf")
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```
