---
title: PDFを暗号化および復号化する
linktitle: PDFファイルを暗号化および復号化する
type: docs
weight: 30
url: /ja/python-cpp/set-privileges-encrypt-and-decrypt-pdf-file/
description: Pythonを介してC++アプリケーションでPDFファイルを暗号化および復号化します。
lastmod: "2024-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 異なる暗号化タイプとアルゴリズムを使用してPDFファイルを暗号化する

PDFファイルを保護する効果的な方法の一つは、暗号化です。この記事では、Aspose.PDFライブラリを使用してPythonでPDFドキュメントを暗号化する方法を探ります。

PDFの暗号化は、暗号化アルゴリズムを使用してPDFドキュメントの内容をスクランブルし、不正アクセスを防ぐことを含みます。暗号化されたPDFファイルを開くにはパスワードが必要であり、印刷、コピー、編集などの操作に制限がある場合があります。

- **ユーザーパスワード** が設定されている場合、PDFを開くために提供する必要があるものです。Acrobat/Readerはユーザーにユーザーパスワードを入力するよう求めます。正しくない場合、ドキュメントは開きません。
- **オーナーパスワード** が設定されている場合、印刷、編集、抽出、コメントなどの権限を制御します。
 Acrobat/Readerは、権限設定に基づいてこれらのことを許可しません。権限を設定/変更する場合は、このパスワードが必要です。

以下のコードスニペットは、PDFファイルを暗号化する方法を示しています。

1. 入力および出力ファイルパスを作成する
1. AsposePDFPythonWrappersを使用してPDFドキュメントを読み込む
1. 暗号化されたドキュメントの権限を定義する
1. 使用する暗号化アルゴリズムを定義する
1. 'document.encrypt'メソッドを使用して、指定されたユーザーおよびオーナーパスワード、権限、および暗号化アルゴリズムでドキュメントを暗号化する
1. 'document.save'メソッドを使用して、暗号化されたドキュメントを指定された出力ファイルに保存する。

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    # サンプルファイルのディレクトリパスを設定
    dataDir = os.path.join(os.getcwd(), "samples")

    # 入力ファイルパスを設定
    input_file = os.path.join(dataDir, "sample.pdf")

    # 出力ファイルパスを設定
    output_file = os.path.join(dataDir, "results", "sample-enc.pdf")

    # AsposePDFPythonWrappersを使用してPDFドキュメントを読み込む
    document = apw.Document(inputFile)

    # 暗号化されたドキュメントの権限を定義する
    permission = apCore.Permissions(apCore.Permissions.ExtractContent | apCore.ModifyContent)

    # 使用する暗号化アルゴリズムを定義する
    cryptoAlgorithm = apCore.CryptoAlgorithm.RC4x128

    # 指定されたユーザーおよびオーナーパスワード、権限、および暗号化アルゴリズムでドキュメントを暗号化する
    document.encrypt("user", "owner", permission, cryptoAlgorithm)

    # 暗号化されたドキュメントを指定された出力ファイルに保存する
    document.save(output_file)
```

## オーナーパスワードを使用してPDFファイルを復号化する

1. 入力ファイルと出力ファイルのパスを作成する
1. AsposePDFPythonWrappersモジュールからDocumentクラスの新しいインスタンスを作成する
1. [document_decrypt](https://reference.aspose.com/pdf/python-cpp/core/document_decrypt/) メソッドを使用してドキュメントを復号化する
1. [document_save](https://reference.aspose.com/pdf/python-cpp/core/document_save/) 関数を使用してsave()メソッドで復号化したドキュメントを出力ファイルパスに保存する

```Python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    # サンプルファイルのディレクトリパスを設定する
    dataDir = os.path.join(os.getcwd(), "samples")

    # 入力ファイルのパスを設定する
    input_file = os.path.join(dataDir, "sample_enc.pdf")

    # 出力ファイルのパスを設定する
    output_file = os.path.join(dataDir, "results", "sample-dec.pdf")

    # AsposePDFPythonWrappersモジュールからDocumentクラスの新しいインスタンスを作成する
    document = apw.Document(input_file, "owner")

    # decrypt()メソッドを使用してドキュメントを復号化する
    document.decrypt()

    # save()メソッドで復号化したドキュメントを出力ファイルパスに保存する
    document.save(output_file)
```