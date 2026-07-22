---
title: Rust で PDF を PPTX に変換
linktitle: PDF を PowerPoint に変換
type: docs
weight: 30
url: /ja/rust-cpp/convert-pdf-to-powerpoint/
lastmod: "2026-07-20"
description: Aspose.PDF は Rust を使用して PDF を PPTX 形式に変換できるようにします。
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF を PowerPoint に変換する Rust ツール
Abstract: C++ 経由で提供される Aspose.PDF for Rust は、PDF ドキュメントを PowerPoint（PPTX）形式に変換する際に、元のレイアウト、書式設定、コンテンツ構造を保持する信頼性の高いソリューションを提供します。この機能により、開発者は静的な PDF ファイルを動的で編集可能なプレゼンテーションにシームレスに変換できます。ライブラリは変換プロセスを制御するカスタマイズオプションを提供し、ビジネスやプロフェッショナルな用途に適した高品質な出力を保証します。ドキュメントには、開発者がアプリケーションに PDF から PowerPoint への変換を効率的に組み込むための手順別の指示とコードサンプルが提供されています。
SoftwareApplication: rust-cpp
---

## PDF を PPTX に変換

提供されたRustコードスニペットは、Aspose.PDFライブラリを使用してPDFドキュメントをPPTXに変換する方法を示しています：

1. PDFドキュメントを開く。
1. 次を使用してPDFファイルをPPTXに変換する [save_pptx](https://reference.aspose.com/pdf/rust-cpp/convert/save_pptx/) 関数。

```rust

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as PptX-document
      pdf.save_pptx("sample.pptx")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**PDF を PowerPoint にオンラインで変換してみてください**

Aspose.PDF for Rust はオンラインの無料アプリケーションをご提供します ["PDF を PPTX に変換"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), 機能と品質を実際に調べてみることができます。

[![Aspose.PDF 無料アプリで PDF を PPTX に変換](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}