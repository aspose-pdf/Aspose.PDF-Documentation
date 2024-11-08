---
title: Pythonを使用したフォームの操作
linktitle: PDFドキュメントのフォーム
type: docs
weight: 60
url: /ja/python-java/forms/
lastmod: "2023-05-19"
description: このセクションには、Python APIを使用してPDFドキュメントのフォームを操作することに関連する記事が含まれています。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

フォームは、情報を収集および保存する目的でユーザーが情報を選択または記入するための領域を持つファイルです。

AcroFormsはフォームフィールドを含むPDFファイルです。これらのフィールドには、エンドユーザーまたはフォームの作成者によって（手動または自動プロセスを通じて）データを入力することができます。内部的には、AcroFormsはPDFドキュメントに適用された注釈またはフィールドです。

このセクションでは、Aspose.PDFを使用してプログラムでPDFドキュメントを完成させるための迅速で簡単なアプローチを説明します。また、Aspose.PDF for Javaを使用して、既存のPDF内のAcroFormsのフィールドを発見しマッピングする方法についても説明します。

**Aspose.PDF for Python via Java** ライブラリを使用すると、PDFドキュメントのフォームをうまく、迅速かつ簡単に操作することができます。

- **AcroForms** - フォームを作成し、フォームフィールドを入力し、フォームからデータを抽出し、JavaライブラリでPDFのフィールドを変更します。
- **XFA Forms** - XFAフィールドを入力し、XFAを変換し、XFAフィールドのプロパティを取得します。

## 次の機能が利用可能です:

- fdfのエクスポート/インポート
- xfdfのエクスポート/インポート
- xmlのエクスポート/インポート
- XfaDataのエクスポート/設定
- フィールドを埋める
- フィールドをフラット化する
- 有効なラジオボタンの値を決定する
- フィールド名、フラグ、タイプ、値を取得する
- フィールドの名前を変更する

```python

from asposepdf import Api, Forms


# ライセンスの初期化
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

DIR_INPUT = baseDir+"testdata/forms/"
DIR_OUTPUT = baseDir+"testout/"

# フィールド入力の例

input_pdf1 = DIR_INPUT + "Testing.pdf"
output_pdf = DIR_OUTPUT + "test5_1.pdf"

form = Forms.Form(sourceFileName=input_pdf1)
print(form.getFieldType("form1[0].Page1[0].fldBarCode1[0]"))
form.fillField("form1[0].Page1[0].fldBarCode1[0]", "54321")

form.save(output_pdf)
```