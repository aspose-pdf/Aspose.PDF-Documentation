---
title: C++ 経由で Rust を使用した PDF ページの削除
linktitle: PDF ページの削除
type: docs
weight: 30
url: /ja/rust-cpp/delete-pages/
description: Aspose.PDF for Rust via C++ を使用して、PDF ファイルからページを削除できます。
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Rust を使用した PDF ページの削除
Abstract: Aspose.PDF for Rust via C++ は、PDF ドキュメントからページを削除するための効率的な機能を提供し、開発者が不要または不必要なページを簡単に削除できるようにします。ライブラリは、ページ番号や範囲を指定することで単一ページまたは複数ページの削除を可能にし、正確なドキュメントの変更を保証します。この機能は、冗長なコンテンツを排除し、ドキュメント構造を最適化することで PDF ファイルを効率化します。ドキュメントには、ステップバイステップの手順とコードサンプルが提供されており、開発者がアプリケーション内でページ削除機能を効果的に実装できるよう支援します。
SoftwareApplication: rust-cpp
---

**Aspose.PDF for Rust via C++** を使用して PDF ファイルからページを削除できます。次のコードスニペットは、特定のページを削除して PDF ドキュメントを操作する方法を示しています。この手法は、ページの削除、変更後のドキュメントの保存、適切なリソース管理を行うための PDF ドキュメント操作タスクにおいて効率的です。

1. PDF ファイルを開く。
1. 特定のページを削除する際に [page_delete](https://reference.aspose.com/pdf/rust-cpp/core/page_delete/) 関数。
1. Document を保存する際に [保存](https://reference.aspose.com/pdf/rust-cpp/core/save/) メソッド。

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document from file
        let pdf = Document::open("sample.pdf")?;

        // Delete specified page in PDF-document
        pdf.page_delete(1)?;

        // Save the previously opened PDF-document
        pdf.save()?;

        Ok(())
    }
```
