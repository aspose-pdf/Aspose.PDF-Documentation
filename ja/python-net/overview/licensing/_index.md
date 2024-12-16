---
title: Aspose PDF ライセンス
linktitle: ライセンスと制限
type: docs
weight: 50
url: /ja/python-net/licensing/
description: Aspose. PDF for Pythonは、クラシックライセンスを取得することを顧客に提案します。また、製品をよりよく探索するために、限定ライセンスを使用することも可能です。
lastmod: "2022-12-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 評価版の制限

私たちはお客様に購入前にコンポーネントを十分にテストしていただきたいと考えています。そのため、評価版では通常のように使用することができます。

- **評価用透かしが付いたPDF。** Aspose.PDF for Pythonの評価版は、製品の全機能を提供しますが、生成されたPDFドキュメントのすべてのページには、上部に「Evaluation Only. Created with Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd」という透かしが入ります。

>評価版の制限なしでAspose.PDFをテストしたい場合は、30日間の一時ライセンスもリクエストできます。
 Please refer to [一時ライセンスの取得方法](https://purchase.aspose.com/temporary-license)

## クラシックライセンス

ライセンスはファイルまたはストリームオブジェクトから読み込むことができます。ライセンスを設定する最も簡単な方法は、ライセンスファイルをAspose.PDF.dllファイルと同じフォルダに置き、パスを指定せずにファイル名を指定することです。以下の例に示されています。

Aspose.PDF for Pythonと一緒に他のAspose for Pythonコンポーネントを使用する場合は、[Aspose.Pdf.Licenseクラス]()のようにライセンスの名前空間を指定してください。

```python

    license_file = LICENSE_FILE
    license = ap.License()
    license.set_license(license_file)
```