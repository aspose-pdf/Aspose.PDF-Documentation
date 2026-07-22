---
title: ページ プロパティの取得と設定
linktitle: ページ プロパティの取得と設定
type: docs
url: /ja/rust-cpp/get-and-set-page-properties/
description: Aspose.PDF for Rust を使用して PDF ドキュメントのページ プロパティを取得および設定する方法を学び、ドキュメントの書式設定をカスタマイズできるようにします。
lastmod: "2026-07-20"
TechArticle: true
AlternativeHeadline: Aspose.PDF for Rust を使用したページ プロパティの取得と設定
Abstract: C++ 経由の Aspose.PDF for Rust は、PDF ドキュメントにおけるページ プロパティの取得および設定に関する包括的な機能を提供し、サイズ、回転、余白、メタデータなどのさまざまなページ属性にアクセスして変更できるようにします。これらの機能により、特定のアプリケーション要件を満たすために、ドキュメントのレイアウトと外観を正確に制御できます。ライブラリは PDF ページのシームレスなカスタマイズと最適化を保証します。ドキュメントには、開発者がアプリケーション内でページ プロパティを効率的に取得および更新できるようにする詳細なガイダンスとコードサンプルが提供されています。
SoftwareApplication: rust-cpp
---


Aspose.PDF for Rust を使用すると、PDF ファイル内のページのプロパティを読み取りおよび設定できます。このセクションでは、PDF ファイルのページ数を取得し、カラーなどの PDF ページ プロパティに関する情報を取得してページ プロパティを設定する方法を示します。

## PDF ファイルのページ数を取得

ドキュメントを扱う際、しばしばそれらが何ページあるか知りたくなります。Aspose.PDF を使用すれば、これにはコードは2行以下で済みます。

**Aspose.PDF for Rust via C++** では、Pages をカウントできます [page_count](https://reference.aspose.com/pdf/rust-cpp/core/page_count/) 関数。

次のコードスニペットは、PDF ドキュメントを開き、ページ数を取得し、結果を出力するように設計されています。

その [page_count](https://reference.aspose.com/pdf/rust-cpp/core/page_count/) このメソッドは PDF ドキュメントの総ページ数を取得するために呼び出されます。特定のページを抽出したり、すべてのページに対して処理を行う必要があるタスクなど、ドキュメントの長さを知る必要がある場合に便利です。このメソッドは、ドキュメントの構造を問い合わせるシンプルな方法です。

PDF ファイルのページ数を取得するには：

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document from file
      let pdf = Document::open("sample.pdf")?;

      // Return page count in PDF-document
      let count = pdf.page_count()?;

      // Print the page count
      println!("Count: {}", count);

      Ok(())
  }
```

## ページサイズを設定

この例では、メソッド pdf.page_set_size() が PDF ドキュメントの最初のページのサイズを変更します。PageSize::A1 により、最初のページが A1 用紙サイズに設定されます。これは、ドキュメントを標準化された形式に変換する場合や、特定のコンテンツがページに正しく収まることを保証する場合に便利です。

1. PDF ドキュメントを開くには [open](https://reference.aspose.com/pdf/rust-cpp/core/open/) メソッド。
1. ページサイズの設定には [page_set_size](https://reference.aspose.com/pdf/rust-cpp/organize/page_set_size/) 関数。
1. Documentを使用して保存する [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) メソッド。

```rs

    use asposepdf::{Document, PageSize};

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Set the size of a page in the PDF-document
        pdf.page_set_size(1, PageSize::A1)?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_page1_set_size_A1.pdf")?;

        Ok(())
    }
```