---
title: ページプロパティの取得と設定
linktitle: ページプロパティの取得と設定
type: docs
url: /ja/go-cpp/get-and-set-page-properties/
description: Aspose.PDF for Go を使用して PDF ドキュメントのページプロパティを取得および設定する方法を学び、カスタマイズされたドキュメントの書式設定を可能にします。
lastmod: "2026-07-04"
TechArticle: true
AlternativeHeadline: Aspose.PDF for Go でページプロパティを取得および設定する
Abstract: Aspose.PDF for Go via C++ は、PDF ドキュメントのページプロパティを取得および設定するための包括的な機能を提供し、開発者はサイズ、回転、余白、メタデータなどのさまざまなページ属性にアクセスして変更できます。これらの機能により、特定のアプリケーション要件を満たすようにドキュメントのレイアウトと外観を正確に制御できます。ライブラリは PDF ページのシームレスなカスタマイズと最適化を保証します。ドキュメントには、開発者がアプリケーション内でページプロパティを効率的に取得および更新できるようにする詳細なガイダンスとコードサンプルが提供されています。
SoftwareApplication: go-cpp
---


Aspose.PDF for Go を使用すると、PDF ファイル内のページのプロパティを読み取って設定できます。このセクションでは、PDF ファイルのページ数の取得方法、色などの PDF ページプロパティに関する情報の取得、そしてページプロパティの設定方法を示します。

## PDF ファイルのページ数を取得する

文書を扱う際、ページ数を把握する必要が生じることはよくあります。Aspose.PDF では、わずか 2 行以下のコードでこれを実現できます。

**Aspose.PDF for Go via C++** は Pages をカウントできる [PageCount](https://reference.aspose.com/pdf/go-cpp/core/pagecount/) 関数。

次のコードスニペットは、PDF ドキュメントを開き、ページ数を取得し、結果を出力するように設計されています。

その [PageCount](https://reference.aspose.com/pdf/go-cpp/core/pagecount/) このメソッドは、PDFドキュメントの総ページ数を取得するために呼び出されます。これは、特定のページを抽出したり、すべてのページに対して操作を実行したりするなど、ドキュメントの長さを知る必要があるタスクに役立ちます。このメソッドは、ドキュメントの構造を問い合わせるシンプルな方法です。

PDFファイルのページ数を取得するには:

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
      // PageCount() returns page count in PDF-document
      count, err := pdf.PageCount()
      if err != nil {
        log.Fatal(err)
      }
      // Print
      fmt.Println("Count:", count)
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

## ページサイズを設定する

この例では、メソッド pdf.PageSetSize() が PDF ドキュメントの最初のページのサイズを変更します。PageSizeA1 定数は、最初のページが A1 用紙サイズに設定されることを保証します。これは、ドキュメントを標準化された形式に変換する場合や、特定のコンテンツがページに正しく収まることを保証する場合に便利です。

1. [Open](https://reference.aspose.com/pdf/go-cpp/core/open/) メソッドを使用して PDF ドキュメントを開きます。
1. [PageSetSize](https://reference.aspose.com/pdf/go-cpp/organize/pagesetsize/) 関数を使用してページサイズを設定します。
1. [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) メソッドを使用してドキュメントを保存します。

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
        // PageSetSize(num int32, pageSize int32) sets size of page
        err = pdf.PageSetSize(1, asposepdf.PageSizeA1)
        if err != nil {
            log.Fatal(err)
        }
        // SaveAs(filename string) saves previously opened PDF-document with new filename
        err = pdf.SaveAs("sample_page1_SetSize_A1.pdf")
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```
