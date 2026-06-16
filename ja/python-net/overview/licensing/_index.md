---
title: アスポーズ PDF ライセンス
linktitle: ライセンスと制限事項
type: docs
weight: 50
url: /ja/python-net/licensing/
description: Aspose.PDF for Python では、お客様にクラシックライセンスの取得を勧めています。また、限定ライセンスを使用して製品を詳しく調べることもできます。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python 用 Aspose.PDF のライセンス
Abstract: この記事では、Aspose.PDF for Python の制限事項とライセンスオプションについて説明しています。評価版ではすべての機能をテストできるが、生成された PDF には著作権情報とともに「評価のみ」というウォーターマークが追加されていることが強調されています。これらの制限なしでテストしたいユーザーには、30 日間の一時ライセンスがあります。この記事では、ファイルまたはストリームからクラシックライセンスをロードしてクラシックライセンスを実装する方法についてさらに説明します。ライセンスファイルを Aspose.PDF.dll ファイルと同じディレクトリに配置し、`Aspose.Pdf.License` クラスを使用してライセンスを設定することを推奨します。ライセンスプロセスを説明するコードスニペットが提供されています。
---

## 評価版の制限事項

評価版では、通常どおりに使用できるように、購入前にコンポーネントを徹底的にテストしていただきたいと考えています。

- **評価用ウォーターマーク付きで作成された PDF。** Aspose.PDF for Python の評価版ではすべての製品機能が提供されますが、生成された PDF ドキュメントのすべてのページには「評価版のみ」というウォーターマークが付いています。Aspose.PDF で作成されました。「著作権 2002-2020 Aspose Pty Ltd.」が一番上にあります。

>評価版の制限なしで Aspose.PDF をテストしたい場合は、30 日間の一時ライセンスをリクエストすることもできます。「」を参照してください。 [仮免許の取得方法は？](https://purchase.aspose.com/temporary-license)

## クラシックライセンス

ライセンスは、ファイルまたはストリームオブジェクトからロードできます。ライセンスを設定する最も簡単な方法は、以下の例のように、ライセンスファイルを Aspose.PDF.dll ファイルと同じフォルダに置き、パスなしでファイル名を指定することです。

Python 用 Aspose.PDF と一緒に他の Aspose for Python コンポーネントを使用する場合は、ライセンスの名前空間を次のように指定してください [アスポース.PDF.ライセンスクラス]().

```python

    license_file = LICENSE_FILE
    license = ap.License()
    license.set_license(license_file)
```
