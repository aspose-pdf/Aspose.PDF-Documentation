---
title: Pythonでデジタル署名を追加またはPDFにデジタル署名
linktitle: PDFにデジタル署名
type: docs
weight: 10
url: /ja/python-net/digitally-sign-pdf-file/
description: PythonでPDF文書にデジタル署名を行い、署名済みPDFを検証または有効性を確認します。
lastmod: "2025-06-07"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PythonでPDFファイルにデジタル署名
Abstract: 本ガイドでは、Aspose.PDF for Python via .NET を使用して PDF 文書にデジタル署名を行う方法を説明します。標準的および高度なデジタル署名の適用方法、証明書（PFX および PKCS#12）の使用、署名の外観と動作のカスタマイズについて詳しく解説します。ドキュメントには、既存の PDF に署名する方法、タイムスタンプを追加する方法、署名の有効性を検証する方法を示すコード例が含まれています。これにより、開発者は Python アプリケーションで文書の真正性、完全性、およびデジタル署名標準への準拠を確保できます。
---

## デジタル署名でPDFに署名

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    ppath_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pfxfile = self.data_dir + pfxfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Instantiate PdfFileSignature object
        with ap.facades.PdfFileSignature(document) as signature:
            # Create PKCS#7 object for sign
            pkcs = ap.forms.PKCS7(path_pfxfile, "12345")
            # Sign PDF file
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            #  Save PDF document
            signature.save(path_outfile)
```

**PKCS#7 デタッチド署名** は、コンテンツを署名ブロックに埋め込まずに文書にデジタル署名を追加します。

次の例では、PKCS#7 デタッチド デジタル署名を使用して PDF 文書に署名し、指定された矩形領域の最初のページに署名を適用します。

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pfxfile = self.data_dir + pfxfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Instantiate PdfFileSignature object using the opened document
        with ap.facades.PdfFileSignature(document) as signature:
            # Create PKCS#7 detached object for sign
            pkcs = ap.forms.PKCS7Detached(path_pfxfile, password, ap.DigestHashAlgorithm.SHA256)
            # Sign PDF file
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            #  Save PDF document
            signature.save(path_outfile)
```

この Python コードスニペットは、'file_sign.verify_signature()' メソッドを使用して PDF ファイル内のデジタル署名を検証します。

1. PDF の署名とやり取りできる PdfFileSignature のインスタンスを作成します。
1. 署名名のリストを取得します `get_signature_names(True)`。
1. リスト内の最初の署名を `verify_signature` でチェックし、指定された証明書への準拠を確認します。

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    # Create an instance of PdfFileSignature for working with signatures in the document
    with ap.facades.PdfFileSignature(path_infile) as file_sign:
        # Get a list of signatures
        signature_names = file_sign.get_signature_names(True)
        # Verify the signature with the given name.
        return file_sign.verify_signature(signature_names[0], certificate)
```

## デジタル署名にタイムスタンプを追加

### タイムスタンプ付きでPDFにデジタル署名する方法

Aspose.PDF for Python は、タイムスタンプサーバーまたは Web サービスを使用して PDF にデジタル署名することをサポートしています。

この要件を満たすために、Aspose.PDF 名前空間に [TimestampSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf/timestampsettings/) クラスが追加されました。以下のコードスニペットをご確認ください。タイムスタンプを取得し、PDF 文書に追加します。

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pfxfile = self.data_dir + pfxfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create an instance of PdfFileSignature for working with signatures in the document
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7(path_pfxfile, password)
            # Create TimestampSettings settings
            timestamp_settings = ap.TimestampSettings("https://freetsa.org/tsr",
                                                                "", ap.DigestHashAlgorithm.SHA256)  # User/Password can be omitted
            pkcs.timestamp_settings = timestamp_settings
            rect = drawing.Rectangle(100, 100, 200, 100)  # Creating a rectangle for the signature
            # Create any of the three signature types
            signature.sign(1, "Signature Reason", "Contact", "Location", True, rect, pkcs)
            # Save PDF document
                signature.save(path_outfile)
```

## ECDSA を使用した PDF 文書の署名

ECDSA（楕円曲線デジタル署名アルゴリズム）を使用して PDF 文書に署名することは、楕円曲線暗号を利用してデジタル署名を生成することを含みます。

上記のコードスニペットは、Aspose.PDF for Python を使用して PDF 文書に PKCS#7 デタッチド デジタル署名を適用する方法を示しています。文書をロードし、署名の外観とセキュリティ設定を構成し、結果を保存することで、この例は PDF ファイルにデジタル署名するための完全で信頼性の高いワークフローを実演しています。

この方法は、最初のページに安全で検証可能な署名を埋め込むことで文書の真正性と完全性を保証します。ダイジェストアルゴリズムとして SHA-256 を使用することで最新の暗号標準を満たし、署名の配置を制御できるため、可視的な承認マークに柔軟性を提供します。

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pfxfile = self.data_dir + pfxfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create an instance of PdfFileSignature to sign the document
        with ap.facades.PdfFileSignature(document) as signature:
            # Create a PKCS7Detached object using the provided certificate and password
            pkcs = ap.forms.PKCS7Detached(path_pfxfile, password, ap.DigestHashAlgorithm.SHA256)

            # Sign the first page of the document, setting the signature's appearance at the specified location
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)

            # Save PDF document
            signature.save(path_outfile)
```
