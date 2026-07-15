---
title: Aspose PDF ライセンス
linktitle: ライセンスと制限事項
type: docs
weight: 90
url: /ja/go-cpp/licensing/
description: Aspose. PDF for Go は顧客にクラシック ライセンスの取得を促しています。また、製品をより良く探索するために制限付きライセンスの使用も可能です。
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: C++ 経由での Aspose.PDF for Go のライセンス
Abstract: C++ 経由での Aspose.PDF for Go のライセンスページでは、製品に利用可能なライセンスオプションが説明されています。顧客はクラシック ライセンス、メーター ライセンス、または評価目的の制限付きライセンスのいずれかを選択できます。このページは、正規ライセンスを取得することで、機能をすべて利用できるようになり、評価の制限が解除されるといった利点も強調しています。
SoftwareApplication: go-cpp
---


## 評価版の制限

お客様が購入前に当社のコンポーネントを徹底的にテストできるように、評価版では通常通りご利用いただけます。

- **評価用ウォーターマークが付いたドキュメント。** Aspose.PDF for Go の評価版は製品のすべての機能を提供しますが、生成されたファイルのすべてのページの上部にテキスト "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2025 Aspose Pty Ltd." がウォーターマークとして表示されます。

- **処理できるページ数を制限します。**
評価版では、ドキュメントの最初の4ページのみを処理できます。

>評価版の制限なしで Aspose.PDF for Go をテストしたい場合は、30 日間の一時ライセンスをリクエストすることもできます。詳細は、以下をご参照ください。 [一時ライセンスの取得方法は？](https://purchase.aspose.com/temporary-license)

## クラシック ライセンス

ライセンス ファイル (Aspose.PDF.GoViaCPP.lic) を使用して、Aspose.PDF ライブラリの完全な機能を有効にするためにライセンスを適用します。

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
        // SetLicense(filename string) licenses with filename
        err = pdf.SetLicense("Aspose.PDF.GoViaCPP.lic")
        if err != nil {
            log.Fatal(err)
        }
        // Working with PDF-document
        // ...
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```
