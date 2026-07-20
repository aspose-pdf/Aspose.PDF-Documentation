---
title: Rustを使用してAcroFormからデータを抽出する
linktitle: AcroFormからデータを抽出する
type: docs
weight: 50
url: /ja/rust-cpp/extract-data-from-acroform/
description: Aspose.PDFはPDFファイルからフォームフィールドデータを抽出することを簡単にします。AcroFormsからデータを抽出し、XML、FDFまたはXFDF形式で保存する方法を学びます。
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Rustを介してAcroFormからデータを抽出する方法
Abstract: この記事では、Aspose.PDF for Rust via C++ を使用して PDF ファイルから AcroForm データを抽出し、広く使用されているデータ交換フォーマットである XML、FDF、XFDF にエクスポートする方法を説明します。インタラクティブなフォームフィールドを含む PDF ドキュメントの開き方と、フォームフィールド名と値をプログラムでエクスポートして元の PDF 以外で再利用する方法を示します。各エクスポート形式に対する実用的な Rust のサンプルを提供することで、データ処理、フォーム送信、システム統合、長期データ保管などの一般的なワークフローを強調し、開発者がアプリケーション内で PDF フォームデータを効率的に管理および再利用できるよう支援します。
---

## PDF ファイルから XML へのデータエクスポート

このコードスニペットは、Aspose.PDF for Rust を使用して PDF ドキュメントから AcroForm データを XML ファイルへエクスポートする方法を示しています。
このプロセスは、フォーム フィールドを含む既存の PDF ファイルを開き、次にそれらのフィールドとその値を XML ドキュメントにエクスポートして、さらに処理、保存、またはデータ交換に使用します。

1. PDF 文書を開きます。
1. フォーム フィールド データを抽出し、XML ファイルとして保存するために 'export_xml' メソッドを呼び出します。

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Export from the previously opened PDF-document with AcroForm to XML-document
        pdf.export_xml("sample.xml")?;

        Ok(())
    }
```

## PDF ファイルから FDF へデータをエクスポート

Aspose.PDF for Rust via C++ を使用すると、PDF ドキュメントから AcroForm データを FDF ファイルへエクスポートできます。Forms Data Format (FDF) ファイルは、PDF とは別にフォームフィールド名と値を保存するため、データ交換、フォーム送信ワークフロー、および元のドキュメントに埋め込まずにフォームデータをアーカイブする際に便利です。

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Export from the previously opened PDF-document with AcroForm to FDF-document
        pdf.export_fdf("sample.fdf")?;

        Ok(())
    }
```

## PDF ファイルから XFDF へのデータエクスポート

XFDF (XML Forms Data Format) は、PDF ファイルとは別にフォームフィールド データを表す XML ベースのフォーマットで、データ交換、フォーム送信、Web ベースのワークフローとの統合に最適です。
Aspose.PDF for Rust via C++ は、PDF ドキュメントから AcroForm データを XFDF ファイルへエクスポートするのに役立ちます。

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Export from the previously opened PDF-document with AcroForm to XFDF-document
        pdf.export_xfdf("sample.xfdf")?;

        Ok(())
    }
```
