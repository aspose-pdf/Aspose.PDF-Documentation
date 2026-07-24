---
title: Rust言語を使用したHello Worldの例
linktitle: Hello Worldの例
type: docs
weight: 40
url: /ja/rust-cpp/hello-world-example/
description: このサンプルは、Aspose.PDF for Rust を使用してテキスト Hello World を含むシンプルな PDF ドキュメントを作成する方法を示しています。
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Rust を使用した Hello World
Abstract: Rust 用 Aspose.PDF (C++ 経由) の入門ガイドは、ライブラリの使用方法を紹介し、PDF ドキュメントの作成と操作の基本手順をカバーしています。テキストコンテンツを含むシンプルな PDF ファイルを生成する方法を示す「Hello World」例が含まれており、開発者が API のコア機能をすばやく理解できるよう支援します。
SoftwareApplication: rust-cpp
---

「Hello World」例は、プログラミング言語やソフトウェアの機能をシンプルなユースケースで紹介するために伝統的に使用されます。

**Aspose.PDF for Rust** は、開発者が Rust で PDF ドキュメントの作成、操作、変換機能を組み込むことができる機能豊富な PDF API です。PDF、TXT、XLSX、EPUB、TEX、DOC、DOCX、PPTX、画像形式など、さまざまな人気ファイル形式をサポートしています。本記事では、テキスト "Hello World!" を含む PDF ドキュメントを作成します。Aspose.PDF for Rust を環境にインストールした後、コードサンプルを実行して Aspose.PDF API の動作を確認できます。
以下のコードスニペットはこれらの手順に従います：

1. 新しい PDF ドキュメント インスタンスを作成します。
1. PDF ドキュメントに新しいページを追加します using [page_add](https://reference.aspose.com/pdf/rust-cpp/core/page_add/) 関数。
1. 使用してページサイズを設定する [page_set_size](https://reference.aspose.com/pdf/rust-cpp/organize/page_set_size/).
1. 使用して最初のページに "Hello World!" テキストを追加する [page_add_text](https://reference.aspose.com/pdf/rust-cpp/organize/page_add_text/).
1. 使用してPDF文書を保存する [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) メソッド。

以下のコードスニペットは、Aspose.PDF for Rust API の動作を示す Hello World プログラムです。

```rs

    use asposepdf::{Document, PageSize};
    use std::error::Error;

    fn main() -> Result<(), Box<dyn Error>> {
        // Create a new PDF-document
        let pdf = Document::new()?;

        // Add a new page
        pdf.page_add()?;

        // Set the size of the first page to A4
        pdf.page_set_size(1, PageSize::A4)?;

        // Add "Hello World!" text to the first page
        pdf.page_add_text(1, "Hello World!")?;

        // Save the PDF-document as "hello.pdf"
        pdf.save_as("hello.pdf")?;

        println!("Saved PDF-document: hello.pdf");

        Ok(())
}
```
