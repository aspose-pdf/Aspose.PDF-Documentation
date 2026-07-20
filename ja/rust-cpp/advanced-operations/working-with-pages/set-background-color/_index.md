---
title: C++ を介して Rust で PDF の背景色を設定する
linktitle: 背景色を設定する
type: docs
weight: 80
url: /ja/rust-cpp/set-background-color/
description: C++ 経由で Rust を使用して、あなたの PDF ファイルの背景色を設定する。
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Rust を使用して PDF の背景色を設定する
Abstract: C++ 経由で提供される Aspose.PDF for Rust は、PDF ページの背景色を設定する機能を提供し、開発者がドキュメントの外観をカスタマイズできるようにします。この機能により、ページ全体の背景に単色を適用でき、ドキュメントの視覚的なプレゼンテーションが向上します。開発者は RGB や CMYK などの標準的なカラーモデルを使用して、色の値を簡単に指定できます。ドキュメントには、C++ アプリケーション内で背景色のカスタマイズを効果的に実装するための詳細な手順とコードサンプルが提供されています。
SoftwareApplication: rust-cpp
---

1. 提供されたコードスニペットは、Rust の Aspose.PDF ライブラリを使用して PDF ファイルの背景色を設定する方法を示しています。
1. その [開く](https://reference.aspose.com/pdf/rust-cpp/core/open/) このメソッドは指定された PDF ファイルをメモリにロードし、外観やコンテンツの変更など、さらなる操作を可能にします。
1. その [set_background](https://reference.aspose.com/pdf/rust-cpp/organize/set_background/) このメソッドは PDF ドキュメントに新しい背景色を適用します。RGB 値を使用して、ユーザーはドキュメントのビジュアルスタイルをカスタマイズできます。
1. その [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) メソッドは更新されたPDFを新しい名前で保存します。

このコードは、ブランド化されたレポートの作成、透かしの追加、または複数のドキュメント間での視覚的一貫性の向上など、PDFカスタマイズを自動化する必要があるアプリケーションに最適です。

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Set PDF-document background color using RGB values
      pdf.set_background(200, 100, 101)?;

      // Save the previously opened PDF-document with new filename
      pdf.save_as("sample_set_background.pdf")?;

      Ok(())
  }
```