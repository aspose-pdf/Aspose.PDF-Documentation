---
title: PythonでPDFをPDF/x形式に変換する
linktitle: PDFをPDF/x形式に変換する
type: docs
weight: 120
url: /ja/python-net/convert-pdf-to-pdf_x/
lastmod: "2025-09-27"
description: このトピックでは、Aspose.PDF for Python via .NET を使用して PDF を PDF/x 形式に変換する方法を示します。
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: PDF を PDF/x 形式に変換する方法
Abstract: この記事では、Aspose.PDF for Python を使用して PDF を PDF/A、PDF/E、PDF/X 形式に変換するための包括的なガイドを提供します。
---

**PDF to PDF/x 形式とは、PDF を追加の形式、つまり PDF/A、PDF/E、PDF/X に変換できることを意味します。**

## PDF を PDF/A に変換する

**Aspose.PDF for Python** は、PDF ファイルを <abbr title="Portable Document Format / A">PDF/A</abbr> 準拠の PDF ファイルに変換できるようにします。その前に、ファイルを検証する必要があります。このトピックではその方法を説明します。

{{% alert color="primary" %}}

Adobe Preflight を使用して PDF/A 準拠を検証していることに注意してください。市場のすべてのツールは独自の「PDF/A 準拠」の表現を持っています。参照用に PDF/A 検証ツールに関するこの記事をご確認ください。Adobe は PDF に関わるすべての中心にあるため、Aspose.PDF が PDF ファイルを生成する方法を検証するツールとして Adobe 製品を選択しました。

{{% /alert %}}

Document クラスの Convert メソッドを使用してファイルを変換します。PDF を PDF/A 準拠のファイルに変換する前に、Validate メソッドで PDF を検証します。検証結果は XML ファイルに保存され、この結果は Convert メソッドにも渡されます。ConvertErrorAction 列挙体を使用して、変換できない要素の操作を指定することもできます。

{{% alert color="success" %}}
**オンラインで PDF を PDF/A に変換してみる**

Aspose.PDF for Python は、オンラインの無料アプリケーション ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a) を提供しており、機能と品質を調べてみることができます。

[![Aspose.PDF 無料アプリで PDF を PDF/A に変換](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

「document.validate()」メソッドは、PDF ファイルが PDF/A-1B 標準（長期保存を目的とした ISO 標準化された PDF バージョン）に準拠しているかどうかを検証します。検証結果はログファイルに保存されます。

1. 'ap.Document' を使用して PDF ドキュメントをロードします。
1. ターゲットとなる準拠レベル (ap.PdfFormat.PDF_A_1B) で validate メソッドを呼び出します。
1. 検証結果が指定されたログファイルに書き込まれます。

```python

    path_infile = path.join(self.data_dir, infile)
    path_logfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.validate(path_logfile, ap.PdfFormat.PDF_A_1B)
```

### PDF を PDF/A-1B に変換する

以下のコードスニペットは、PDF ファイルを PDF/A-1B 形式に変換する方法を示しています。

1. 'ap.Document' を使用して PDF ドキュメントをロードします。
1. 以下のパラメータで convert メソッドを呼び出します。
- ログファイルパス - 変換プロセスとコンプライアンスチェックの詳細を保存します。
- ターゲット形式 - 'ap.PdfFormat.PDF_A_1B'（アーカイブ標準）。
- エラーアクション - 'ap.ConvertErrorAction.DELETE' – 準拠を妨げる要素を自動的に削除します。
1. 変換された PDF/A 準拠ファイルを出力パスに保存します。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.convert(
        self.data_dir + "pdf_pdfa.log",
        ap.PdfFormat.PDF_A_1B,
        ap.ConvertErrorAction.DELETE,
    )
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

### PDF を PDF 2.0 と PDF/A-4 に変換する

この例では、PDF ドキュメントを新しい標準形式である PDF 2.0 と PDF/A-4 に変換する方法を示します。
両方の変換により、最新の仕様とアーカイブ要件への準拠が確保されます。

1. ap.Document を使用して入力ドキュメントをロードします。
1. document.convert を呼び出して、PDF 2.0 への最初の変換を実行します。
- 変換詳細のログファイルパス。
- ターゲット形式 - 'ap.PdfFormat.V_2_0'。
- エラーアクション - 'ap.ConvertErrorAction.DELETE' （非準拠要素を削除）。
1. 同じメソッドを使用して PDF/A-4 への二番目の変換を実行し、ファイルがアーカイブ標準にも準拠していることを確認します。
1. 結果のドキュメントを指定された出力パスに保存します。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    document = ap.Document(path_infile)
    document.convert(path_logfile, ap.PdfFormat.V_2_0, ap.ConvertErrorAction.DELETE)

    document.convert(path_logfile, ap.PdfFormat.PDF_A_4, ap.ConvertErrorAction.DELETE)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

### 埋め込みファイル付きで PDF を PDF/A-3A に変換する

次のコードスニペットは、外部ファイルを PDF に埋め込み、その後 PDF を添付ファイルをサポートし、埋め込みコンテンツで長期保存に適した PDF/A-3A 形式に変換する方法を示します。

1. 'ap.Document' を使用して入力 PDF をロードします。
1. 埋め込むファイル（例: "aspose-logo.jpg"）を指す 'FileSpecification' オブジェクトを作成し、説明を付けます。
1. ファイル仕様を PDF の 'embedded_files' コレクションに追加します。
1. 'document.convert' を使用してドキュメントを PDF/A-3A に変換し、以下を指定します：
- ログファイルのパス。
- 目標フォーマット - 'ap.PdfFormat.PDF_A_3A'。
- エラーアクション - 'ap.ConvertErrorAction.DELETE'（準拠していない要素を削除）。
1. 変換された PDF を出力パスに保存します。
1. 確認メッセージを表示します。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    document = ap.Document(path_infile)

    fileSpecification = ap.FileSpecification(self.data_dir + "aspose-logo.jpg", "Large Image file")
    document.embedded_files.add(fileSpecification)
    document.convert(path_logfile, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

### フォント置換で PDF を PDF/A-1B に変換

この関数は、欠落したフォントを利用可能なフォントに置換しながら、PDF を PDF/A-1B 形式に変換します。これにより、変換された PDF の視覚的な一貫性が保たれ、アーカイブ基準に準拠します。

1. 'ap.Document' を使用して PDF をロードします。
1. 'document.convert' を使用して PDF を PDF/A-1B に変換し、以下を指定します：
- ログファイルのパス。
- 目標フォーマット - 'ap.PdfFormat.PDF_A_1B'。
- エラーアクション - 'ap.ConvertErrorAction.DELETE'（準拠していない要素を削除）。
1. 変換された PDF を出力パスに保存します。
1. 確認メッセージを表示します。

```python

    from os import path
    import aspose.pdf as ap 

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    try:
        ap.text.FontRepository.find_font("AgencyFB")

    except ap.FontNotFoundException:
        font_substitution = ap.text.SimpleFontSubstitution("AgencyFB", "Arial")
        ap.text.FontRepository.Substitutions.append(font_substitution)

    document = ap.Document(path_infile)
    document.convert(path_logfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

### 自動タグ付けで PDF を PDF/A-1B に変換

この関数は、アクセシビリティと構造的一貫性のためにコンテンツに自動的にタグ付けを行いながら、PDF ドキュメントを PDF/A-1B 形式に変換します。自動タグ付けにより、スクリーンリーダーの利用性が向上し、適切な意味構造が保証されます。

1. 'ap.Document' を使用して PDF をロードします。
1. 'PdfFormatConversionOptions' を作成し、以下を指定します：
- ログファイルのパス。
- 目標フォーマット - 'ap.PdfFormat.PDF_A_1B'。
- エラーアクション - 'ap.ConvertErrorAction.DELETE'（準拠していない要素を削除）。
1. 'AutoTaggingSettings' を設定します：
- 'enable_auto_tagging = True' を有効にします。
- 'heading_recognition_strategy = AUTO' を設定して見出しを自動検出します。
1. オートタグ付け設定を変換オプションに割り当てます。
1. 'document.convert(options)' を使用して PDF を変換します。
1. 変換された PDF を出力パスに保存します。
1. 確認メッセージを表示します。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    document = ap.Document(path_infile)
    options =  ap.PdfFormatConversionOptions(path_logfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE)

    auto_tagging_settings = ap.AutoTaggingSettings()
    auto_tagging_settings.enable_auto_tagging = True

    auto_tagging_settings.heading_recognition_strategy = ap.HeadingRecognitionStrategy.AUTO

    options.auto_tagging_settings = auto_tagging_settings
    document.convert(options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## PDF を PDF/E に変換

このスニペットは、PDF ドキュメントがエンジニアリングおよび技術文書向けの ISO 標準である PDF/E-1 に準拠しているかを検証します。検証結果はログファイルに保存されます。

1. 'ap.Document' を使用して PDF ドキュメントをロードします。
1. validate メソッドを呼び出し、以下を指定します：
- 検証結果を保存するログファイルのパス。
- 目標フォーマット - 'ap.PdfFormat.PDF_E_1'。
1. 検証結果はレビューのためにログファイルに保存されます。

```python

    path_infile = path.join(self.data_dir, infile)
    path_logfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.validate(path_logfile, ap.PdfFormat.PDF_E_1)
```

次の例は、エンジニアリングおよび技術文書向けの ISO 標準である PDF/E-1 フォーマットに PDF を変換する方法を示します。このフォーマットは、エンジニアリングワークフローに必要な正確なレイアウト、グラフィック、メタデータを保持します。

1. 'ap.Document' を使用して元の PDF をロードします。
1. 'PdfFormatConversionOptions' を作成し、以下を指定します：
- 変換問題の追跡用ログファイルのパス。
- 目標フォーマット - 'ap.PdfFormat.PDF_E_1'。
- エラーアクション - 'ap.ConvertErrorAction.DELETE'（準拠していない要素を削除）。
1. 'document.convert(options)' を使用して PDF を変換します。
1. 変換された PDF を指定された出力パスに保存します。
1. 確認メッセージを表示します。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    document = ap.Document(path_infile)
    options =  ap.PdfFormatConversionOptions(path_logfile, ap.PdfFormat.PDF_E_1, ap.ConvertErrorAction.DELETE)

    document.convert(options)

    # Save PDF document
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## PDF を PDF/X に変換

次のコードスニペットは、印刷・出版業界で一般的に使用される ISO 標準の PDF/X-4 フォーマットに PDF ドキュメントを変換します。PDF/X-4 は色精度を保証し、透明性を保持し、デバイス間で一貫した出力を実現するために ICC プロファイルを埋め込みます。

1. 'ap.Document' を使用して元の PDF をロードします。
1. 'PdfFormatConversionOptions' を作成し、指定します：
- ログファイルのパス。
- ターゲット形式 - 'ap.PdfFormat.PDF_X_4'。
- エラーアクション - 'ap.ConvertErrorAction.DELETE' を使用して、非準拠要素を削除します。
1. 'icc_profile_file_name' を使用して、カラー管理用の **ICC プロファイルファイル** を提供します。
1. 印刷要件のために条件識別子（例: "FOGRA39"）を含む **OutputIntent** を指定します。
1. 'document.convert()' を使用して PDF を変換します。
1. 変換された PDF を指定された出力パスに保存します。
1. 確認メッセージを出力します。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    document = ap.Document(path_infile)
    options =  ap.PdfFormatConversionOptions(path_logfile, ap.PdfFormat.PDF_X_4, ap.ConvertErrorAction.DELETE)

    # Provide the name of the external ICC profile file (optional)
    options.icc_profile_file_name = path.join(self.data_dir,"ISOcoated_v2_eci.icc")
    # Provide an output condition identifier and other necessary OutputIntent properties (optional)
    options.output_intent = ap.OutputIntent("FOGRA39")

    document.convert(options)

    # Save PDF document
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```
