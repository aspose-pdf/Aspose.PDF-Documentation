---
title: Go を使用して PDF にテキストを追加する
linktitle: PDF にテキストを追加する
type: docs
weight: 10
url: /ja/go-cpp/add-text-to-pdf-file/
description: Aspose.PDF を使用してコンテンツの強化とドキュメント編集を行う方法として、Go で PDF ドキュメントにテキストを追加する方法を学びます。
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
AlternativeHeadline: Aspose.PDF for Go を使用して PDF にテキストを追加する
Abstract: Aspose.PDF for C++ および Go のドキュメントの「Add Text to PDF File」セクションでは、プログラムで PDF ドキュメントにテキストを挿入するためのステップバイステップの手順が提供されています。テキスト追加のさまざまな方法をカバーしており、位置指定、フォントのカスタマイズ、色の調整、テキストの配置オプションなどが含まれます。このガイドでは、PDF の特定のページや場所にテキストを追加する方法を示し、正確なコンテンツ配置を保証します。詳細なコード例と解説により、開発者はテキスト挿入機能を自分のアプリケーションに簡単に統合でき、PDF ドキュメントの管理が向上します。
SoftwareApplication: go-cpp
---

既存の PDF ファイルにテキストを追加するには：

1. PDF ファイルを開く。
1. PDF ドキュメントにテキストを追加するには [PageAddText](https://reference.aspose.com/pdf/go-cpp/organize/pageaddtext/) 関数。
1. 変更を同じファイルに保存します。

## テキストの追加

次のコードスニペットは、既存のPDFファイルにテキストを追加する方法を示しています。

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
        // PageAddText(num int32, addText string) adds text on page
        err = pdf.PageAddText(1, "added text")
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
