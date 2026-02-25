---
title: PythonでPDFファイルメタデータを扱う
linktitle: PDFファイルメタデータ
type: docs
weight: 200
url: /ja/python-net/pdf-file-metadata/
description: Aspose.PDF を使用して、Python で著者やタイトルなどの PDF メタデータを抽出および管理する方法を探ります。
lastmod: "2025-05-12"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Pythonを使用してPDFのメタデータを取得および設定する
Abstract: この記事は、Aspose.PDF for Python via .NET を使用した PDF メタデータの操作に関する包括的なガイドを提供します。著者、作成日、キーワードなど、文書のカタログ化、検索最適化、または検証に重要なメタデータプロパティを抽出および設定する方法を概説しています。コードスニペットでは、`Document` クラスと `info` プロパティを使用して PDF からメタデータを取得し、`DocumentInfo` オブジェクトで新しいメタデータを設定し、変更を保存する方法を示しています。さらに、XMP メタデータをプログラムで更新する方法も示しており、文書の整理と検索性を向上させます。この記事では、名前空間 URI を登録してカスタムプレフィックスでメタデータを挿入する方法も説明しています。これらの機能は、アプリケーション内で PDF 文書情報を効果的に管理したい開発者にとって不可欠です。
---

## PDFファイル情報の取得

このコードスニペットは、Aspose.PDF for Python via .NET を使用して PDF ドキュメントからメタデータを抽出する方法を示します。Document オブジェクトの info プロパティにアクセスすることで、著者、作成日、キーワード、更新日、サブジェクト、タイトルといった重要な情報を取得します。この機能は、文書のカタログ化、検索最適化、または文書プロパティの検証が必要なアプリケーションにとって不可欠です。

1. Documentクラスを使用してPDFファイルを開く
1. infoプロパティを介してドキュメントのメタデータを取得する
1. メタデータ情報を表示する。目的のメタデータフィールドを出力する

```python

    import aspose.pdf as ap

    def get_pdf_file_information():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf()

        # Open PDF document
        document = ap.Document(data_dir + "GetFileInfo.pdf")

        # Get document information
        doc_info = document.info

        # Display document information
        print(f"Author: {doc_info.author}")
        print(f"Creation Date: {doc_info.creation_date}")
        print(f"Keywords: {doc_info.keywords}")
        print(f"Modify Date: {doc_info.mod_date}")
        print(f"Subject: {doc_info.subject}")
        print(f"Title: {doc_info.title}")
```

## PDFファイル情報の設定

Aspose.PDF for Python via .NET を使用すると、PDF に対して著者、作成日、サブジェクト、タイトルなどのファイル固有の情報を設定できます。この情報を設定するには、以下の手順を実行します。

1. Documentクラスを使用してPDFファイルを開く。
1. [DocumentInfo]() オブジェクトを作成し、目的のメタデータプロパティを設定する。
1. 保存メソッドを使用して変更を新しい PDF ファイルに保存する。

以下のコードスニペットは、PDF ファイル情報の設定方法を示しています。

```python

    import aspose.pdf as ap
    import datetime

    def set_file_information():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_workingdocuments()

        # Open PDF document
        document = ap.Document(data_dir + "SetFileInfo.pdf")

        # Specify document information
        doc_info = ap.DocumentInfo(document)
        doc_info.author = "Aspose"
        doc_info.creation_date = datetime.datetime.now()
        doc_info.keywords = "Aspose.Pdf, DOM, API"
        doc_info.mod_date = datetime.datetime.now()
        doc_info.subject = "PDF Information"
        doc_info.title = "Setting PDF Document Information"
        doc_info.producer = "Custom producer"
        doc_info.creator = "Custom creator"

        # Save PDF document
        document.save(data_dir + "SetFileInfo_out.pdf")
```

## PDFファイルのXMPメタデータを設定する

このコードスニペットは、Aspose.PDF for Python via .NET を使用して PDF ドキュメントの XMP メタデータをプログラムで設定または更新する方法を示します。xmp:CreateDate、xmp:Nickname、カスタム定義フィールドなどのプロパティを変更することで、標準化されたメタデータを PDF ファイルに埋め込むことができます。この手法は、文書の整理を強化し、検索性を向上させ、重要な情報をファイルに直接埋め込む際に特に有用です。

Aspose.PDF を使用すると、PDF ファイルにメタデータを設定できます。メタデータを設定するには、次の手順を行います。

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラスを使用してPDFファイルを開く。
1. 特定のキーに値を割り当てて XMP メタデータを変更する。
1. 更新された PDF ドキュメントを保存する。

以下のコードスニペットは、PDF ファイルにメタデータを設定する方法を示しています。

```python

    import aspose.pdf as ap
    import datetime

    def set_xmp_metadata():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf()

        # Open PDF document
        document = ap.Document(data_dir + "SetXMPMetadata.pdf")

        # Set XMP metadata properties
        document.metadata["xmp:CreateDate"] = datetime.datetime.now().isoformat()
        document.metadata["xmp:Nickname"] = "Nickname"
        document.metadata["xmp:CustomProperty"] = "Custom Value"

        # Save the updated PDF document
        document.save(data_dir + "SetXMPMetadata_out.pdf")
```

## プレフィックス付きメタデータの挿入

一部の開発者は、プレフィックス付きの新しいメタデータ名前空間を作成する必要があります。以下のコードスニペットは、プレフィックスを使用してメタデータを挿入する方法を示しています。

```python

    import aspose.pdf as ap
    import datetime

    def set_prefix_metadata():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf()

        # Open PDF document
        document = ap.Document(data_dir + "SetXMPMetadata.pdf")

        # Register a namespace URI for the 'xmp' prefix
        document.metadata.register_namespace_uri("xmp", "http://ns.adobe.com/xap/1.0/")

        # Set the metadata property using the registered prefix
        document.metadata["xmp:ModifyDate"] = datetime.datetime.now().isoformat()  # ISO 8601 format

        # Save the updated PDF document
        document.save(data_dir + "SetPrefixMetadata_out.pdf")
```
