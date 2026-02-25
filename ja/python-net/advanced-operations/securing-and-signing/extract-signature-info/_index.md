---
title: 署名の詳細を抽出
linktitle: 署名の詳細を抽出
type: docs
weight: 20
url: /ja/python-net/extract-image-and-signature-information/
description: Aspose.PDF for Python を使用して PDF ドキュメントのデジタル署名から画像を抽出する方法。
lastmod: "2025-06-22"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF の署名情報を取得
Abstract: この記事では、Aspose.PDF for Python を使用して PDF ドキュメントから画像とデジタル署名情報を抽出する方法を示します。埋め込まれた画像の特定、アクセス、保存の手順とコードサンプル、さらにデジタル署名のメタデータや検証ステータスの取得方法を段階的に説明します。
---

## 署名フィールドから画像を抽出

Aspose.PDF for Python via .NET は、[signature_field](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/) クラスを使用して PDF ファイルにデジタル署名を付与する機能をサポートしています。

このコードスニペットは、Aspose.PDF for Python を使用して PDF ドキュメントからデジタル署名画像を抽出する方法を示しています。

手順:

1. PDF ドキュメントを開く。
1. フォーム フィールドを反復処理し、SignatureField オブジェクトを探す。
1. 各署名に関連付けられた画像を抽出する（利用可能な場合）。
1. 抽出した署名画像を JPEG ファイルとして保存する。

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Searching for signature fields
        for field in document.form:
            signature_field = field if isinstance(field, ap.forms.SignatureField) else None
            if signature_field is None:
                continue

            image_stream = signature_field.extract_image()
            if image_stream is None:
                continue

            image = drawing.Bitmap.from_stream(image_stream)
            # Save the image
            image.save(path_outfile, drawing.imaging.ImageFormat.jpeg)
```

## 署名情報の抽出

Aspose.PDF for Python via .NET は、SignatureField クラスを使用して PDF ファイルにデジタル署名を付与する機能をサポートしています。現在、証明書の有効性を判定することはできますが、証明書全体を抽出することはできません。抽出可能な情報は、公開鍵、サムプリント、発行者などです。

署名情報を抽出するために、[SignatureField](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/) クラスに [ExtractCertificate](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/#methods) メソッドを導入しました。以下のコードスニペットは、SignatureField オブジェクトから証明書を抽出する手順を示していますので、ご覧ください。

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Searching for signature fields
        for field in document.form:
            signature_field = field if isinstance(field, ap.forms.SignatureField) else None
            if signature_field is None:
                continue
            # Extract certificate
            certificate_stream = signature_field.extract_certificate()
            if certificate_stream is None:
                continue
            # Save certificate
            with certificate_stream:
                bytes_data = bytearray(certificate_stream.length)
                with open(path_outfile, "wb") as file_stream:
                    certificate_stream.read(bytes_data, 0, len(bytes_data))
                    file_stream.write(bytes_data)
```

ドキュメントの署名アルゴリズムに関する情報を取得できます。

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            # Get signature names
            signature_names = signature.get_signature_names(True)
            signatures_info_list = signature.get_signatures_info()
            for sig_info in signatures_info_list:
                print(sig_info.DIGEST_HASH_ALGORITHM)
                print(sig_info.ALGORITHM_TYPE)
                print(sig_info.CRYPTOGRAPHIC_STANDARD)
                    print(sig_info.signature_name)
```

## 署名の改ざんチェック

このコードスニペットは、Aspose.PDF for Python を使用して PDF ドキュメント内の改ざんされたデジタル署名を検出する方法を示しています。

手順は以下です:

1. PDF ドキュメントを開く。
1. ドキュメントを解析するために 'SignaturesCompromiseDetector' インスタンスを作成する。
1. 改ざんされた（無効または変更された）デジタル署名がないかチェックする。
1. 見つかった改ざんされた署名の名前を出力する。
1. 署名カバレッジを報告する—有効な署名で保護されているドキュメントの範囲を示す。

この機能は、法的、金融、コンプライアンス重視の環境など、ドキュメントの真正性と完全性を検証しなければならないユースケースで重要です。開発者は署名された PDF の改ざんや破損を自動的に検出できます。

Aspose.PDF はデジタル署名検証のための包括的なツールセットを提供し、ドキュメントの信頼性を確保した安全な署名対応アプリケーションの構築を容易にします。

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create the compromise detector instance
        detector = ap.SignaturesCompromiseDetector(document)
        result = []

        # Check for compromise
        if detector.check(result):
            print("No signature compromise detected")
            return

        # Get information about compromised signatures
        if result[0].has_compromised_signatures:
            print(f"Count of compromised signatures: {len(result[0].COMPROMISED_SIGNATURES)}")
            for signature_name in result[0].COMPROMISED_SIGNATURES:
                print(f"Signature name: {signature_name.FULL_NAME}")

        # Get info about signatures coverage
        print(result[0].signatures_coverage)
```

