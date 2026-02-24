---
title: PDFへのスマートカード署名の追加方法
linktitle: スマートカードを使ったPDF署名
type: docs
weight: 30
url: /ja/python-net/sign-pdf-document-from-smart-card/
description: Aspose.PDF for Python via .NET を使用すると、署名フィールドを使用してスマートカードから PDF ドキュメントに署名できます。
lastmod: "2025-06-22"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PythonでスマートカードからPDFドキュメントに署名する
Abstract: このガイドでは、Aspose.PDF for Python via .NET を使用してスマートカードで PDF ドキュメントにデジタル署名する方法を説明します。Windows 証明書ストアを介してハードウェアデバイス（USB トークンやスマートカードなど）に保存された証明書にアクセスし、PDF ファイルの署名に適用する手順を示します。ドキュメントには、適切な証明書の検索、署名プロパティの設定、および PDF へのデジタル署名の埋め込み方法を示すコード例が含まれています。これにより、デジタル署名標準に準拠した安全なハードウェア支援署名が可能となり、信頼性の高いエンタープライズや法的ワークフローに適しています。
---

Aspose.PDF は、視覚的および暗号的な署名コンポーネントの統合において強力な機能を提供し、デジタル署名された PDF ドキュメントの真正性とプロフェッショナルな提示を確保します。

## 署名フィールドを使用したスマートカードでのサイン

この例では、Aspose.PDF for Python を使用して外部証明書で PDF ドキュメントにデジタル署名し、カスタム署名外観画像を適用する方法を示します。

1. PDF ドキュメントを開く。
1. PdfFileSignature オブジェクトを作成し、ドキュメントにバインドする。
1. カスタムメソッド `get_local_certificate()` を使用してローカルのデジタル証明書を取得する。
1. 選択した証明書に基づき ExternalSignature を設定する。
1. カスタム署名外観画像（例：会社ロゴや手書きサイン）を適用する。
1. 指定したメタデータ（理由、連絡先、場所）を使用してドキュメントの最初のページにデジタル署名する。
1. 署名済みドキュメントを新しい出力ファイルに保存する。

この方法は、ハードウェアトークン、証明書ストア、信頼できるプロバイダーなどの外部証明書を使用してプログラム的に署名を適用し、個別のビジュアルレイアウトで表示する必要があるケースに最適です。

以下は、スマートカードから PDF ドキュメントに署名するためのコードスニペットです。

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pngfile = self.data_dir + pngfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        with ap.facades.PdfFileSignature() as pdf_signature:
            # Bind PDF document
            pdf_signature.bind_pdf(document)
            selected_certificates = self.get_local_certificate()
            # Set an external signature settings
            external_signature = ap.forms.ExternalSignature(selected_certificates)
            pdf_signature.signature_appearance = path_pngfile
            # Sign the document
            pdf_signature.sign(1, "Reason", "Contact", "Location", True, drawing.Rectangle(100, 100, 200, 200),
                                external_signature)
            # Save PDF document
            pdf_signature.save(path_outfile)
```

## デジタル署名の検証

このコードスニペットは、Aspose.PDF for Python を使用して PDF ドキュメント内のデジタル署名を検証する方法を示します。

1. PDF ファイルを開く。
1. 'PdfFileSignature オブジェクト' を作成し、ドキュメントにバインドする。
1. 'get_signature_names()' を使用してすべての署名フィールド名のリストを取得する。
1. 各署名を反復し、'verify_signature()' で有効性を検証する。
1. 署名の検証に失敗した場合は例外をスローする。

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    # Open PDF document
    with ap.Document(path_infile) as document:
        with ap.facades.PdfFileSignature(document) as pdf_signature:
            signature_names = pdf_signature.get_signature_names(True)
            for index in range(len(signature_names)):
                if not pdf_signature.verify_signature(signature_names[index]):
                    raise Exception("Not verified")
```

## 外部証明書で署名

このコードスニペットは、外部証明書を使用して Aspose.PDF for Python で PDF ドキュメントにデジタル署名フィールドを追加し、署名する方法を示します。

1. PDF ファイルをバイナリ ストリームとして開く。
1. SignatureField を作成し、指定位置にドキュメントの最初のページに配置する。
1. カスタムメソッド `get_local_certificate()` を使用してローカルのデジタル証明書を取得する。
1. 権限、理由、連絡先情報などのメタデータを含む ExternalSignature を設定する。
1. 署名フィールドに一意のフィールド名を割り当てる（partial_name = "sig1"）。
1. 署名フィールドを PDF のフォームフィールドに追加する。
1. 外部証明書でフィールドに署名する。
1. 署名済みドキュメントを出力ファイルに保存する。

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open a document stream
    with open(path_infile, "rb+") as file_stream:
        # Open PDF document from stream
        document = ap.Document(file_stream)

        # Create a signature field
        signature_field = ap.forms.SignatureField(document.pages[1], ap.Rectangle(100, 400, 10, 10, True))
        selected_certificate = self.get_local_certificate()

        # Set external signature settings
        external_signature = ap.forms.ExternalSignature(selected_certificate)
        external_signature.authority = "Me"
        external_signature.reason = "Reason"
        external_signature.contact_info = "Contact"

        # Set a name of signature field
        signature_field.partial_name = "sig1"

        # Add the signature field to the document
        document.form.add(signature_field, 1)

        # Sign the document
        signature_field.sign(external_signature)

        # Save PDF document
        document.save(path_outfile)
```


