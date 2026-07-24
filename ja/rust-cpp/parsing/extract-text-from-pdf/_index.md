---
title: Rust を使用して PDF からテキストを抽出する
linktitle: PDF からテキストを抽出する
type: docs
weight: 30
url: /ja/rust-cpp/extract-text-from-pdf/
description: この記事では、Aspose.PDF for Rust を使用して PDF ドキュメントからテキストを抽出するさまざまな方法について説明します。
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Rust でテキストを抽出する
Abstract: C++ を介した Aspose.PDF for Rust は、PDF ドキュメントからテキストを抽出するための強力で効率的な方法を提供します。このライブラリは複数の抽出技術をサポートしており、ユーザーはドキュメント全体、特定のページ、または PDF 内の事前定義された領域からテキストを取得できます。
SoftwareApplication: rust-cpp
---

## PDF ドキュメントからテキストを抽出する

PDFドキュメントからテキストを抽出することは、非常に一般的で有用な作業です。PDFには、さまざまな目的でアクセス、分析、または処理が必要な重要な情報が含まれていることがよくあります。テキストを抽出することで、データベース、レポート、その他のドキュメントへの再利用が容易になります。

テキストを抽出すると、PDFのコンテンツが検索可能になり、ユーザーは文書全体を手動で確認することなく、特定の情報を迅速に見つけることができます。

PDFドキュメントからテキストを抽出したい場合は、次のものを使用できます [extract_text](https://reference.aspose.com/pdf/rust-cpp/core/extract_text/) 関数。
Rustを使用してPDFファイルからテキストを抽出するためのコードスニペットをご確認ください。

1. 指定されたファイル名で PDF ドキュメントを開きます。
1. [extract_text](https://reference.aspose.com/pdf/rust-cpp/core/extract_text/) PDF ドキュメントからテキストコンテンツを抽出します。
1. 抽出したテキストをコンソールに出力します。

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Return the PDF-document contents as plain text
        let txt = pdf.extract_text()?;

        // Print extracted text
        println!("Extracted text:\n{}", txt);

        Ok(())
    }
```