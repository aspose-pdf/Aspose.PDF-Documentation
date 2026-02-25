---
title: PythonでPDFをMicrosoft Wordドキュメントに変換する
linktitle: PDFをWordに変換
type: docs
weight: 10
url: /ja/python-net/convert-pdf-to-word/
lastmod: "2025-09-27"
description: Aspose.PDF を使用して、PythonでPDFドキュメントをWord形式に変換し、簡単に文書編集できる方法を学びます。
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PythonでPDFをWordに変換する方法
Abstract: この記事では、Python と Aspose.PDF ライブラリを使用して PDF ファイルを Microsoft Word フォーマット（DOC および DOCX）に変換するための包括的なガイドを提供します。PDF を編集可能な Word ドキュメントに変換する利点を概説し、テキスト、表、画像などのコンテンツ操作を容易にします。この記事では、PDF を DOC（Word 97-2003 フォーマット）および DOCX に変換する手順を、Python のコードスニペットを用いて示します。プロセスは、PDF から `Document` オブジェクトを作成し、`save()` メソッドと `SaveFormat` 列挙体を使用して目的のフォーマットで保存することを含みます。さらに、変換プロセスをさらにカスタマイズできる `DocSaveOptions` クラスを紹介し、認識モードの指定などが可能です。記事は、変換品質と機能をテストするために Aspose.PDF が提供するオンラインアプリケーションも紹介しています。コンテンツには、各フォーマットに対応するセクションへの構造化された概要とリンクが含まれています。
---

## PDF を DOC に変換

最も人気のある機能のひとつは PDF から Microsoft Word DOC への変換で、コンテンツ管理が容易になります。**Aspose.PDF for Python via .NET** は、PDF ファイルを DOC だけでなく DOCX フォーマットにも簡単かつ効率的に変換できます。

[DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) クラスは、PDF ファイルを DOC フォーマットに変換するプロセスを改善する多数のプロパティを提供します。これらのプロパティの中で、Mode は PDF コンテンツの認識モードを指定できます。このプロパティには RecognitionMode 列挙体の任意の値を指定できます。各値には特定の利点と制限があります：

手順: PythonでPDFをDOCに変換する

1. PDF を 'ap.Document' オブジェクトに読み込みます。
1. 'DocSaveOptions' インスタンスを作成します。
1. フォーマットプロパティを 'DocFormat.DOC' に設定し、出力が .doc フォーマット（古い Word フォーマット）になるようにします。
1. 指定した保存オプションを使用して、PDF を Word ドキュメントとして保存します。
1. 確認メッセージを出力します。

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.DocSaveOptions()
    save_options.format = apdf.DocSaveOptions.DocFormat.DOC
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**オンラインで PDF を DOC に変換してみる**

Aspose.PDF for Python は、オンラインの無料アプリケーション ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc) を提供しており、機能と品質を試すことができます。

[![PDF を DOC に変換](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## PDF を DOCX に変換

Aspose.PDF for Python API を使用すると、Python via .NET で PDF ドキュメントを DOCX に読み込み・変換できます。DOCX は、構造がプレーンバイナリから XML とバイナリファイルの組み合わせに変更された、Microsoft Word 文書のよく知られたフォーマットです。Docx ファイルは Word 2007 以降のバージョンで開くことができますが、DOC 拡張子をサポートする以前の MS Word では開けません。

以下の Python コードスニペットは、PDF ファイルを DOCX フォーマットに変換するプロセスを示しています。

手順: PythonでPDFをDOCXに変換する

1. 'ap.Document' を使用してソース PDF を読み込みます。
1. 'DocSaveOptions' のインスタンスを作成します。
1. フォーマットプロパティを 'DocFormat.DOC_X' に設定し、.docx ファイル（最新の Word フォーマット）を生成します。
1. 設定した保存オプションで PDF を DOCX ファイルとして保存します。
1. 変換後に確認メッセージを出力します。

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.DocSaveOptions()
    save_options.format = apdf.DocSaveOptions.DocFormat.DOC_X
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

[DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) クラスには Format というプロパティがあり、結果のドキュメントのフォーマット（DOC または DOCX）を指定できます。PDF ファイルを DOCX フォーマットに変換するには、DocSaveOptions.DocFormat 列挙体から Docx 値を渡してください。

{{% alert color="warning" %}}
**オンラインで PDF を DOCX に変換してみる**

Aspose.PDF for Python は、オンラインの無料アプリケーション ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx) を提供しており、機能と品質を試すことができます。

[![Aspose.PDF PDF を Word に変換 無料アプリ](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

