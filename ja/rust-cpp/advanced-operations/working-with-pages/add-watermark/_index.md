---
title: Rust を使用して PDF に透かしを追加する
linktitle: 透かしを追加
type: docs
weight: 80
url: /ja/rust-cpp/add-watermarks/
description: この例では、C++ 経由で Rust 用 Aspose.PDF を使用して、PDF ドキュメントにカスタマイズ可能なテキスト透かしを追加する方法を示します。
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: テキスト透かしを追加
Abstract: C++ 経由で Rust 用 Aspose.PDF は、PDF ドキュメントにテキスト透かしを追加する柔軟な方法を提供します。この例では、テキスト内容、フォント、サイズ、色、位置、回転角度、レイヤー設定、および透明度を指定することで、カスタマイズ可能な透かしを挿入する方法を示します。透かしは、ブランディング、機密ラベル、ドラフトマーク、またはドキュメント保護のために一般的に使用されます。
SoftwareApplication: rust-cpp
---

その [add_watermark](https://reference.aspose.com/pdf/rust-cpp/organize/add_watermark/) このメソッドは、開発者がプログラム的に既存のPDFドキュメントにテキスト透かしを適用できるようにします。透かしは以下を含めて完全にカスタマイズ可能です:

- 透かしテキスト
- フォントファミリー
- フォントサイズ
- テキストカラー（HEX形式）
- X および Y の位置座標
- 回転角度
- 前面または背面の配置
- 不透明度（透過レベル）

この例では、アプリケーションが既存の PDF ファイルを開き、半透明の回転した透かしを適用し、変更されたドキュメントを新しいファイル名で保存します。

この機能は、文書をドラフト、機密、サンプルとしてマークしたり、配布前にブランド要素を追加したりするのに特に有用です。

1. 既存の PDF ドキュメントを開く。
1. add_watermark メソッドを呼び出し、透かしのプロパティを設定します。
1. 更新されたドキュメントを保存します。

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Add watermark to PDF-document
        pdf.add_watermark(
            "WATERMARK",
            "Arial",
            16.0,
            "#010101",
            100,
            100,
            45,
            true,
            0.5,
        )?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_add_watermark.pdf")?;

        Ok(())
    }
```