---
title: Rust を使用した C++ で PDF ページを回転
linktitle: PDF ページを回転
type: docs
weight: 50
url: /ja/rust-cpp/rotate-pages/
description: このトピックでは、Rust を使用して C++ 経由で既存の PDF ファイルのページ向きをプログラムで回転させる方法について説明します。
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Rust を使用した PDF ページの回転
Abstract: Aspose.PDF for Rust via C++ は、PDF ドキュメント内のページを回転させる堅牢な機能を提供し、開発者が必要に応じてページ向きを変更できるようにします。このライブラリは、ページを 90 度、180 度、または 270 度回転させることをサポートし、ドキュメントのレイアウトを迅速かつ効率的に調整できます。この機能は、向きが誤っているページの修正やドキュメントの提示方法を変更するのに便利です。ドキュメントには、開発者がアプリケーションにページ回転機能をシームレスに統合できるように、ステップバイステップの手順とコードサンプルが含まれています。
SoftwareApplication: rust-cpp
---

このセクションでは、Rust を使用して既存の PDF ファイルのページ向きを横向きから縦向き、またはその逆に変更する方法について説明します。

ページを回転させることで、プロフェッショナルな環境でのPDFの印刷や表示時に適切な配置が保証されます

1. PDFドキュメントを開きます。
1. PDFページを回転させます。The [回転](https://reference.aspose.com/pdf/rust-cpp/organize/rotate/) 関数は特定の回転（この場合、180度）を指定されたページに適用します。
1. 変更を新しいファイルに保存します。The [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) この関数は、元の PDF を保持しながら更新されたバージョンを保存するために、新しい PDF ファイルを作成します。

この例では、PDF ドキュメントの特定のページを回転させます。

```rs

    use asposepdf::{Document, Rotation};

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Rotate PDF-document
        pdf.rotate(Rotation::On270)?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_rotate.pdf")?;

        Ok(())
    }
```