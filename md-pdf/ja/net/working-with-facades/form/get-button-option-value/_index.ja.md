---
title: ボタンオプション値を取得する
type: docs
weight: 40
url: /net/get-button-option-value/
description: このセクションでは、Formクラスを使用してAspose.PDF Facadesでボタンオプション値を取得する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

## 既存のPDFファイルからボタンオプション値を取得する

ラジオボタンは、異なるオプションを表示する方法を提供します。[Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form)クラスを使用すると、特定のラジオボタンのすべてのボタンオプション値を取得できます。[GetButtonOptionValues](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getbuttonoptionvalues)メソッドを使用してこれらの値を取得できます。このメソッドは、入力パラメーターとしてラジオボタンの名前を必要とし、Hashtableを返します。このHashtableを反復処理してオプション値を取得できます。以下のコードスニペットは、既存のPDFファイルからボタンオプション値を取得する方法を示しています。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Forms-GetButtonOptionValue-GetButtonOptionValue.cs" >}}

## 既存のPDFファイルから現在のボタンオプション値を取得する

ラジオボタンはオプション値を設定する方法を提供しますが、一度に選択できるのは1つだけです。現在選択されているオプション値を取得したい場合は、[GetButtonOptionCurrentValue** メソッドを使用できます。[Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) クラスはこのメソッドを提供します。[GetButtonOptionCurrentValue](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getbuttonoptioncurrentvalue) メソッドはラジオボタン名を入力パラメータとして要求し、値を文字列として返します。次のコードスニペットは、既存のPDFファイルから現在のボタンオプション値を取得する方法を示しています。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Forms-GetButtonOptionValue-GetCurrentValue.cs" >}}