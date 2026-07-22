---
title: RustでPDFにページ番号を追加する
linktitle: ページ番号の追加
type: docs
weight: 10
url: /ja/rust-cpp/add-page-number/
description: この記事では、Aspose.PDF for Rust via C++ を使用して既存の PDF ドキュメントにページ番号を追加する方法を示します。
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: ページ番号の追加
Abstract: Aspose.PDF for Rust via C++ は、開発者が既存の PDF ドキュメントに自動ページ番号付けを数行のコードで強化できるようにします。この例では、PDF ファイルを開き、すべてのページにページ番号を挿入し、更新されたドキュメントを新しいファイルとして保存する方法を示します。ページ番号付けを自動化することで、文書構造の一貫性が保たれ、レポート、契約書、マニュアル、その他配布や印刷を目的としたマルチページ出力に特に有用です。
SoftwareApplication: rust-cpp
---

Aspose.PDF for Rust via C++ は、PDF ドキュメントをプログラムから変更するための組み込み機能を提供します。この例では、アプリケーションが既存の PDF ファイルを開き、すべてのページに自動ページ番号付けを適用し、変更されたドキュメントを新しい名前で保存します。

このアプローチは、配布、印刷、またはアーカイブ目的の最終文書を生成する際に有用です。プロセスは数行のコードだけで済み、明示的に上書きしない限り元のファイルは変更されません。

ページ番号付けは、レポート、請求書、契約書、マニュアル、その他の複数ページ文書に共通の要件です。The [add_page_num()](https://reference.aspose.com/pdf/rust-cpp/organize/add_page_num/) メソッドは文書のすべてのページにページ番号を自動的に挿入し、ファイル全体で一貫したページ付けを確保します。

ページ番号を追加した後、更新された文書は新しい PDF ファイルとして保存されます。

1. 既存の PDF 文書を開きます。
1. ページ番号を付けるには [add_page_num()](https://reference.aspose.com/pdf/rust-cpp/organize/add_page_num/) メソッド。
1. 更新されたドキュメントを保存します。

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Add page number to a PDF-document
        pdf.add_page_num()?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_add_page_num.pdf")?;

        Ok(())
    }
```