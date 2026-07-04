---
title: Go を使用して PDF からテキストを抽出する
linktitle: PDF からテキストを抽出する
type: docs
weight: 30
url: /ja/go-cpp/extract-text-from-pdf/
description: この記事では、Aspose.PDF for Go を使用して PDF ドキュメントからテキストを抽出するさまざまな方法を説明します。
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Go でテキストを抽出する
Abstract: C++ 経由の Aspose.PDF for Go は、PDF ドキュメントからテキストを抽出するための強力かつ効率的な方法を提供します。このライブラリは複数の抽出手法をサポートしており、ユーザーは文書全体、特定のページ、または PDF 内の事前に定義された領域からテキストを取得できます。
SoftwareApplication: go-cpp
---

## PDF ドキュメントからテキストを抽出する

PDFドキュメントからテキストを抽出することは、非常に一般的で有用な作業です。PDFにはしばしば、さまざまな目的でアクセス、分析、または処理が必要な重要な情報が含まれています。テキストを抽出することで、データベース、レポート、その他の文書での再利用が容易になります。

テキストを抽出すると、PDFコンテンツが検索可能になり、ユーザーは文書全体を手動でレビューすることなく、特定の情報を迅速に見つけることができます。

PDFドキュメントからテキストを抽出したい場合は、以下を使用できます [ExtractText](https://reference.aspose.com/pdf/go-cpp/core/extracttext/) 関数。
Go を使用して PDF ファイルからテキストを抽出するための、以下のコードスニペットをご確認ください。

1. 指定されたファイル名で PDF ドキュメントを開きます。
1. [ExtractText](https://reference.aspose.com/pdf/go-cpp/core/extracttext/) PDF ドキュメントからテキスト コンテンツを抽出します。
1. 抽出されたテキストをコンソールに出力します。

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"
    import "fmt"

    func main() {
        // Open(filename string) opens a PDF-document with filename
        pdf, err := asposepdf.Open("sample.pdf")
        if err != nil {
            log.Fatal(err)

        }
        // ExtractText() returns PDF-document contents as plain text
        txt, err := pdf.ExtractText()
        if err != nil {
            log.Fatal(err)
        }
        // Print
        fmt.Println("Extracted text:\n", txt)
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```