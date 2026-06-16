---
title: Python で PDF を PDF/A、PDF/E、および PDF/X に変換
linktitle: PDF を PDF/A、PDF/E、および PDF/X に変換
type: docs
weight: 120
url: /ja/python-net/convert-pdf-to-pdf_x/
lastmod: "2026-06-09"
description: アーカイブ、アクセシビリティ、印刷のワークフローを実現するために、.NET 経由の Aspose.PDF for Python を使用して PDF ファイルを Python で PDF/A、PDF/E、および PDF/X に変換する方法を学びましょう。
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: PDF を PDF/X フォーマットに変換する方法
Abstract: この記事では、Aspose.PDF for Python を使用して PDF を PDF/A、PDF/E、および PDF/X 形式に変換するための包括的なガイドを提供しています。
---

**PDF から PDF/X 形式への変換とは、PDF を別の形式、つまり PDF/A、PDF/E、PDF/X に変換できることを意味します。**

## PDF ファイルを PDF/A に変換

**Python用アスポースPDF**を使用すると、PDFファイルを次の形式に変換できます <abbr title="Portable Document Format / A">PDF/A</abbr> 準拠している PDF ファイル。その前に、ファイルを検証する必要があります。このトピックではその方法を説明します。

{{% alert color="primary" %}}

PDF/A適合の検証はアドビプリフライトに従いますのでご注意ください。市場に出回っているすべてのツールには、独自の PDF/A 適合性の「表現」があります。PDF/A 検証ツールに関するこの記事を参考にしてください。Aspose.PDF が PDF ファイルを生成する方法を確認するためにアドビ製品を選んだのは、PDF に関連するあらゆることの中心がアドビだからです。

{{% /alert %}}

ドキュメントクラスの Convert メソッドを使用してファイルを変換します。PDF を PDF/A 準拠ファイルに変換する前に、Validate メソッドを使用して PDF を検証してください。検証結果は XML ファイルに保存され、その結果も Convert メソッドに渡されます。ConvertErrorAction 列挙を使用して変換できない要素に対するアクションを指定することもできます。

{{% alert color="success" %}}
**オンラインでPDF/AをPDF/Aに変換してみてください**

Python 用の Aspose.PDF はオンラインアプリケーションを提供します [「PDF から PDF/A-1A へ」](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)ここで、機能や動作品質を調べてみるといいかもしれません。

[![Aspose.PDF アプリで PDF を PDF/A に変換](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

'document.validate () 'メソッドは、PDF ファイルが PDF/A-1B 標準（長期間のアーカイブ用に設計された PDF の ISO 標準バージョン）に準拠しているかどうかを検証します。検証結果はログファイルに保存されます。

### PDF を PDF/A-1B に変換

次のコードスニペットは、PDF ファイルを PDF/A-1B 形式に変換する方法を示しています。

1. 「AP.ドキュメント」を使用してPDFドキュメントをロードします。
1. 次のパラメータを指定して convert メソッドを呼び出します。
    -ログファイルパス-変換プロセスとコンプライアンスチェックの詳細を保存します。
    -ターゲットフォーマット-'ap.pdfFormat.pdf_a_1b' (アーカイブスタンダード)
    -エラーアクション-'ap.ConvertErrorAction.Delete' — コンプライアンスを妨げる要素を自動的に削除します。
1. 変換された PDF/A 準拠ファイルを出力パスに保存します。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA(infile, outfile):
    """Convert PDF to PDF/A-1B format."""

    document = ap.Document(infile)
    document.convert(
        outfile.replace(".pdf", "-log.xml"),
        ap.PdfFormat.PDF_A_1B,
        ap.ConvertErrorAction.DELETE,
    )
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

### PDF を PDF 2.0 および PDF/A-4 に変換

この例は、PDF ドキュメントを新しい標準形式である PDF 2.0 と PDF/A-4 に変換する方法を示しています。
どちらの変換も、最新の仕様とアーカイブ要件への準拠を保証するのに役立ちます。

1. AP.Document を使用して入力ドキュメントをロードします。
1. PDF 2.0 への最初の変換を実行するには、次のようにして document.convert を呼び出します。
    -コンバージョンの詳細のログファイルパス。
    -ターゲットフォーマット-'ap.PDFFormat.v_2_0'。
    -エラーアクション-「AP.ConvertErrorAction.Delete」を使用して、準拠していない要素を削除します。
1. 同じ方法を使用してPDF/A-4への2回目の変換を行い、ファイルがアーカイブ標準にも準拠していることを確認します。
1. 結果のドキュメントを指定した出力パスに保存します。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA4(infile, outfile):
    logfile = outfile.replace(".pdf", "_log.xml")

    document = ap.Document(infile)
    document.convert(logfile, ap.PdfFormat.V_2_0, ap.ConvertErrorAction.DELETE)
    document.convert(logfile, ap.PdfFormat.PDF_A_4, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```

### 埋め込みファイルを含む PDF を PDF/A-3A に変換

次のコードスニペットは、外部ファイルを PDF に埋め込み、その PDF を PDF/A-3A 形式に変換する方法を示しています。PDF/A-3A 形式は添付ファイルをサポートし、埋め込みコンテンツを含む長期間のアーカイブに適しています。

1. 「AP.ドキュメント」を使用して入力PDFをロードします。
1. 埋め込むファイル (例:"aspose-logo.jpg「) を指す「FileSpecification」オブジェクトを作成し、説明を付けます。
1. PDF の「embedded_files」コレクションにファイル仕様を追加します。
1. 「document.convert」を使用してドキュメントをPDF/A-3Aに変換し、以下を指定します。
    -ログファイルパス。
    -ターゲットフォーマット-「AP.PDFFormat.pdf_a_3a」。
    -エラーアクション-「AP.ConvertErrorAction.Delete」を使用して、準拠していない要素を削除します。
1. 変換された PDF を出力パスに保存します。
1. 確認メッセージを印刷します。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA_with_attachment(infile, attachement_file, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")
    document = ap.Document(infile)

    fileSpecification = ap.FileSpecification(attachement_file, "Large Image file")
    document.embedded_files.add(fileSpecification)
    document.convert(
        logfile, ap.PdfFormat.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE
    )
    document.save(outfile)
```

### フォントの代替機能を使用して PDF を PDF/A-1B 形式に変換

この関数は PDF を PDF/A-1B 形式に変換しますが、不足しているフォントは使用可能なフォントに置き換えて処理します。これにより、変換された PDF の見た目の一貫性が保たれ、アーカイブ標準に準拠していることが保証されます。

1. 「AP.ドキュメント」を使用してPDFをロードします。
1. 「document.convert」を使用して PDF を PDF/A-1B に変換し、以下を指定します。
    -ログファイルパス。
    -ターゲットフォーマット-「AP.PDFFormat.pdf_A_1B」。
    -エラーアクション-「AP.ConvertErrorAction.Delete」を使用して、準拠していない要素を削除します。
1. 変換された PDF を出力パスに保存します。
1. 確認メッセージを印刷します。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA_replace_missing_fonts(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")
    try:
        ap.text.FontRepository.find_font("AgencyFB")

    except ap.FontNotFoundException:
        font_substitution = ap.text.SimpleFontSubstitution("AgencyFB", "Arial")
        ap.text.FontRepository.Substitutions.append(font_substitution)

    document = ap.Document(infile)
    document.convert(logfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```

### 自動タグ付け機能で PDF を PDF/A-1B 形式に変換

この機能は、アクセシビリティと構造の一貫性を保つためにコンテンツに自動的にタグを付けながら、PDF ドキュメントを PDF/A-1B 形式に変換します。自動タグ付けにより、スクリーンリーダーによる文書の使いやすさが向上し、適切なセマンティック構造が保証されます。

1. 「AP.ドキュメント」を使用してPDFをロードします。
1. 以下を指定して「PDF 形式変換オプション」を作成します。
    -ログファイルパス。
    -ターゲットフォーマット-「AP.PDFFormat.pdf_A_1B」。
    -エラーアクション-「AP.ConvertErrorAction.Delete」を使用して、準拠していない要素を削除します。
1. 「自動タグ設定」の設定:
    -「自動タグ付けを有効化 = True」を有効にします。
    -「見出し認識戦略 = 自動」を設定すると、見出しが自動的に検出されます。
1. 自動タグ設定を変換オプションに割り当てます。
1. 「ドキュメント.変換 (オプション)」を使用して PDF を変換します。
1. 変換された PDF を出力パスに保存します。
1. 確認メッセージを印刷します。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA_with_automatic_tagging(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")

    document = ap.Document(infile)
    options = ap.PdfFormatConversionOptions(
        logfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE
    )

    auto_tagging_settings = ap.AutoTaggingSettings()
    auto_tagging_settings.enable_auto_tagging = True

    auto_tagging_settings.heading_recognition_strategy = (
        ap.HeadingRecognitionStrategy.AUTO
    )

    options.auto_tagging_settings = auto_tagging_settings
    document.convert(options)
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## PDF ファイルを PDF/E ファイルに変換

このコードスニペットは、PDFドキュメントをPDF/E-1形式に変換する方法を示しています。PDF/E-1形式は、エンジニアリングおよび技術文書用に調整されたISO標準です。この形式では、エンジニアリングワークフローに必要な正確なレイアウト、グラフィックス、メタデータが保存されます。

1. 「AP.ドキュメント」を使用してソースPDFをロードします。
1. 以下を指定して「PDF 形式変換オプション」を作成します。
    -変換の問題を追跡するためのログファイルパス。
    -ターゲットフォーマット-「AP.PDFFormat.pdf_e_1」。
    -エラーアクション-「AP.ConvertErrorAction.Delete」を使用して、準拠していない要素を削除します。
1. 「ドキュメント.変換 (オプション)」を使用して PDF を変換します。
1. 変換された PDF を指定した出力パスに保存します。
1. 確認メッセージを印刷します。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDF_E(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")

    document = ap.Document(infile)
    options = ap.PdfFormatConversionOptions(
        logfile, ap.PdfFormat.PDF_E_1, ap.ConvertErrorAction.DELETE
    )

    document.convert(options)

    # Save PDF document
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## PDF ファイルを PDF/X 形式に変換

次のコードスニペットは、PDF ドキュメントを PDF/X-4 形式に変換します。これは、印刷および出版業界で一般的に使用されている ISO 標準です。PDF/X-4 は色の正確さを保ち、透明度を維持し、ICC プロファイルを埋め込んで、デバイス間で一貫した出力を実現します。

1. 「AP.ドキュメント」を使用してソースPDFをロードします。
1. 以下を指定して「PDF 形式変換オプション」を作成します。
    -ログファイルパス。
    -ターゲットフォーマット-「AP.PDFFormat.PDF_X_4」。
    -エラーアクション-「AP.ConvertErrorAction.Delete」を使用して、準拠していない要素を削除します。
1. 「icc_profile_file_name」を使用して、カラーマネジメント用の**ICCプロファイルファイル**を指定します。
1. 印刷要件には、**OutputIntent**を条件識別子 (例:「FOGRA39」) とともに指定します。
1. 'document.convert () 'を使用して PDF を変換します。
1. 変換された PDF を指定した出力パスに保存します。
1. 確認メッセージを印刷します。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDF_X(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")

    document = ap.Document(infile)
    options = ap.PdfFormatConversionOptions(
        logfile, ap.PdfFormat.PDF_X_4, ap.ConvertErrorAction.DELETE
    )

    # Provide the name of the external ICC profile file (optional)
    options.icc_profile_file_name = path.join(
        path.dirname(infile), "ISOcoated_v2_eci.icc"
    )
    # Provide an output condition identifier and other necessary OutputIntent properties (optional)
    options.output_intent = ap.OutputIntent("FOGRA39")

    document.convert(options)

    # Save PDF document
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## 関連コンバージョン

- [PDF をワードに変換](/pdf/ja/python-net/convert-pdf-to-word/) 標準検証後の編集可能なコンテンツワークフロー用
- [PDF ファイルを HTML 形式に変換](/pdf/ja/python-net/convert-pdf-to-html/) ターゲット出力が標準ベースの PDF ではなく Web 対応の場合。
