---
title: Aspose PDF ライセンス
linktitle: ライセンスと制限
type: docs
weight: 90
url: /ja/rust-cpp/licensing/
description: Aspose. PDF for Rust は、顧客にクラシック ライセンスの取得を促します。また、製品をよりよく検証するために限定ライセンスの使用も可能です。
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: C++ 経由の Aspose.PDF for Rust のライセンス
Abstract: C++ 経由の Aspose.PDF for Rust のライセンスページでは、製品に利用可能なライセンスオプションが説明されています。顧客は、クラシック ライセンス、メータード ライセンス、または評価目的の限定ライセンスのいずれかを選択できます。このページは、正規ライセンスを取得することの利点も強調しており、フル機能の解除や評価制限の除去などが挙げられます。
SoftwareApplication: rust-cpp
---

## ライセンス

- この **Rust ソースコード** は MIT ライセンスの下でライセンスされています。
- この **shared library** (AsposePDFforRust_windows_amd64.dll、libAsposePDFforRust_linux_amd64.so、libAsposePDFforRust_darwin_amd64.dylib、libAsposePDFforRust_darwin_arm64.dylib) はプロプライエタリであり、商用ライセンスが必要です。全機能を使用するには、ライセンスを取得しなければなりません。

## 評価版

評価のために **Aspose.PDF for Rust via C++** を無料で使用できます。評価版は製品のほぼすべての機能を提供しますが、いくつかの制限があります。同じ評価版はライセンスを購入し、ライセンスを適用するコード行を数行追加することで正式にライセンスされたものになります。

- 評価版の制限なく Aspose.PDF for Rust をテストしたい場合は、30 日間の一時ライセンスをリクエストすることもできます。詳細は以下をご参照ください。 [一時ライセンスの取得方法は？](https://purchase.aspose.com/temporary-license)?

### 評価版の制限

お客様が購入前にコンポーネントを十分にテストできるように、評価版では通常通りご利用いただけます。

- **評価ウォーターマーク付きで作成されたドキュメント**。Aspose.PDF for Rust の評価版は製品の全機能を提供しますが、生成されたファイルのすべてのページの上部に「Evaluation Only. Created with Aspose.PDF. Copyright 2002-2025 Aspose Pty Ltd.」というテキストがウォーターマークとして入ります。
- **処理できるページ数の制限**。評価版では、ドキュメントの最初の4ページのみを処理できます。

### 本番環境での使用

本番環境では商用ライセンスキーが必要です。商用ライセンスの購入については、弊社までご連絡ください。

### ライセンスを適用

ライセンスファイル (Aspose.PDF.RustViaCPP.lic) を使用して、Aspose.PDF for Rust のフル機能を有効にするためにライセンスを適用しています。

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Set license with filename
        pdf.set_license("Aspose.PDF.RustViaCPP.lic")?;

        // Now you can work with the licensed PDF document
        // ...

        Ok(())
    }
```