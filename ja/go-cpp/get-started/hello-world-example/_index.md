---
title: Go言語を使用したHello Worldの例
linktitle: Hello Worldの例
type: docs
weight: 40
url: /ja/go-cpp/hello-world-example/
description: このサンプルは、Aspose.PDF for Go を使用してテキスト Hello World を含むシンプルな PDF ドキュメントの作成方法を示しています。
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Go を使用した Hello World
Abstract: Aspose.PDF for Go via C++ の入門ガイドは、ライブラリの使用方法を紹介し、PDF ドキュメントの作成と操作の基本手順をカバーしています。テキストコンテンツを含むシンプルな PDF ファイルを生成する方法を示す 'Hello World' の例が含まれており、開発者が API のコア機能をすぐに理解できるよう支援します。
SoftwareApplication: go-cpp
---

「Hello World」例は、プログラミング言語やソフトウェアの機能をシンプルな使用例で紹介するために伝統的に使用されます。

**Aspose.PDF for Go** は、開発者が Go で PDF 文書の作成、操作、および変換機能を組み込むことができる機能豊富な PDF API です。PDF、TXT、XPS、EPUB、TEX、DOC、DOCX、PPTX、画像フォーマットなど、多くの一般的なファイル形式をサポートしています。本記事では、テキスト「Hello World!」を含む PDF 文書を作成します。環境に Aspose.PDF for Go をインストールした後、コードサンプルを実行して Aspose.PDF API の動作を確認できます。
以下のコードスニペットは次の手順に従います：

1. 新しい PDF 文書インスタンスを作成します。
1. PDF 文書に新しいページを追加するには、 [PageAdd](https://reference.aspose.com/pdf/go-cpp/core/pageadd/) 関数です。
1. ページサイズを設定するには [PageSetSize](https://reference.aspose.com/pdf/go-cpp/organize/pagesetsize/).
1. 最初のページに \u0022Hello World!\u0022 テキストを追加するには [PageAddText](https://reference.aspose.com/pdf/go-cpp/organize/pageaddtext/).
1. 修復された PDF ドキュメントを保存するには [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) メソッド。
1. PDFドキュメントを閉じ、割り当てられたリソースを解放します。

以下のコードスニペットは、Aspose.PDF for Go API の動作を示す Hello World プログラムです。

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
        // Create new PDF-document
        pdf, err := asposepdf.New()
        if err != nil {
                log.Fatal(err)
        }
        // Add new page
        err = pdf.PageAdd()
        if err != nil {
                log.Fatal(err)
        }
        // Set page size A4
        err = pdf.PageSetSize(1, asposepdf.PageSizeA4)
        if err != nil {
                log.Fatal(err)
        }
        // Add text on first page
        err = pdf.PageAddText(1, "Hello World!")
        if err != nil {
                log.Fatal(err)
        }
        // Save PDF-document with "hello.pdf" name
        err = pdf.SaveAs("hello.pdf")
        if err != nil {
                log.Fatal(err)
        }
        // Release allocated resources
        defer pdf.Close()
    }
```
