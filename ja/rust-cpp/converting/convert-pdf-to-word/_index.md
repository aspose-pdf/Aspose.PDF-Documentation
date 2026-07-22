---
title: RustでPDFをWord文書に変換する
linktitle: PDFをWordに変換する
type: docs
weight: 10
url: /ja/rust-cpp/convert-pdf-to-doc/
lastmod: "2026-07-20"
description: PDFをDOC（DOCX）に変換するためのRustコードの書き方を学びましょう。
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Rust を使用したPDFからWordへの変換ツール
Abstract: Aspose.PDF for Rust via C++ は、元のテキスト、画像、表、および全体的な文書構造を保持しながら、PDF ドキュメントを DOC 形式にシームレスに変換できるようにします。この機能により、開発者は静的な PDF を編集可能な Word ファイルに変換し、さらに修正や処理を行うことができます。このライブラリは、変換出力を制御するためのさまざまなカスタマイズオプションを提供し、高い忠実度と正確性を保証します。ドキュメントには、開発者がアプリケーションで PDF から DOC への変換を効率的に実装できるよう、詳細な手順とサンプルコードが含まれています。
SoftwareApplication: rust-cpp
---

Microsoft Word や DOC および DOCX 形式をサポートするその他のワードプロセッサで PDF ファイルの内容を編集します。PDF ファイルは編集可能ですが、DOC および DOCX ファイルの方が柔軟でカスタマイズしやすくなります。

## PDF を DOC に変換

提供されたRustコードスニペットは、Aspose.PDFライブラリを使用してPDFドキュメントをDOCに変換する方法を示しています:

1. PDFドキュメントを開く。
1. 使用してPDFファイルをDOCに変換する [save_doc](https://reference.aspose.com/pdf/rust-cpp/convert/save_doc/) 関数。

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as Doc-document
      pdf.save_doc("sample.doc")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**PDF をオンラインで DOC に変換してみてください**

Aspose.PDF for Rust はオンライン無料アプリケーションを提供します ["PDF を DOC に変換"](https://products.aspose.app/pdf/conversion/pdf-to-doc), そこで機能と品質を調査してみることができます。

[![PDF を DOC に変換](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc) 
{{% /alert %}}

## PDF を DOCX に変換

Aspose.PDF for Rust API を使用すると、PDF ドキュメントを DOCX に読み取りおよび変換できます。DOCX は、構造がプレーンなバイナリから XML とバイナリ ファイルの組み合わせに変更された、Microsoft Word ドキュメントのよく知られたフォーマットです。Docx ファイルは Word 2007 およびそれ以降のバージョンで開くことができますが、DOC ファイル拡張子をサポートする以前のバージョンの MS Word では開けません。

提供された Rust コードスニペットは、Aspose.PDF ライブラリを使用して PDF ドキュメントを DOCX に変換する方法を示しています：

1. PDFドキュメントを開く。
1. PDF ファイルを DOCX に変換するには使用 [save_docx](https://reference.aspose.com/pdf/rust-cpp/convert/save_docx/) 関数。

```rust

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as DocX-document
      pdf.save_docx("sample.docx")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**PDF を DOCX にオンラインで変換してみましょう**

Aspose.PDF for Rust はオンライン無料アプリケーションを提供します [\"PDF を Word に\"](https://products.aspose.app/pdf/conversion/pdf-to-docx), そこで機能と品質を調査してみることができます。

[![Aspose.PDF 変換 PDF to Word 無料アプリ](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## 強化認識モードで PDF を DOCX に変換

強化認識モードを使用して、Aspose.PDF for Rust を使い PDF ドキュメントを Microsoft Word（DOCX）ファイルに変換します。

拡張認識モードは、完全に編集可能な DOCX を生成し、次を保持します:

 - 段落構造
 - ネイティブ Word テーブルとしての表
 - 論理的なテキストフローと書式設定

1. ソースPDFファイルを開きます。
1. 拡張レイアウト認識を有効にして、PDFをDOCXファイルとして保存します。

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as DocX-document with Enhanced Recognition Mode (fully editable tables and paragraphs)
      pdf.save_docx_enhanced("sample_enhanced.docx")?;

      Ok(())
  }
```
