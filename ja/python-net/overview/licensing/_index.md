---
title: Aspose PDF ライセンス
linktitle: ライセンスと制限
type: docs
weight: 50
url: /ja/python-net/licensing/
description: Aspose.PDF for Python は顧客にクラシック ライセンスの取得を促しています。また、製品をよりよく探索するために制限付きライセンスを使用することもできます。
lastmod: "2025-02-21"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Python のライセンス情報
Abstract: この記事では、Aspose.PDF for Python の制限とライセンス オプションについて説明します。評価版はフル機能のテストが可能ですが、生成された PDF に「Evaluation Only」と著作権情報が含まれる透かしが追加されることを強調しています。これらの制限なしでテストしたいユーザーには、30 日間の一時ライセンスが利用できます。記事では、ファイルまたはストリームから読み込むことでクラシック ライセンスを実装する方法をさらに解説し、ライセンス ファイルを Aspose.PDF.dll と同じディレクトリに配置し、`Aspose.Pdf.License` クラスを使用してライセンスを設定することを推奨しています。ライセンス プロセスを示すコード スニペットが提供されています。
---

## 評価版の制限

お客様が購入前にコンポーネントを十分にテストできるように、評価版では通常通り使用できるようにしています。

- **評価用透かし付き PDF**。Aspose.PDF for Python の評価版は製品の全機能を提供しますが、生成された PDF ドキュメントのすべてのページの上部に「Evaluation Only. Created with Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd」という透かしが付けられます。

>評価版の制限なしで Aspose.PDF をテストしたい場合は、30 日間の一時ライセンスをリクエストすることもできます。詳細は[一時ライセンスの取得方法？](https://purchase.aspose.com/temporary-license)をご参照ください

## クラシック ライセンス

ライセンスはファイルまたはストリームオブジェクトから読み込むことができます。最も簡単な設定方法は、ライセンス ファイルを Aspose.PDF.dll と同じフォルダーに置き、パスなしでファイル名だけを指定することです。以下の例に示すように行います。

Aspose.PDF for Python と他の Aspose for Python コンポーネントを併用する場合は、[Aspose.Pdf.License クラス]() のようにライセンスの名前空間を指定してください。

```python

    license_file = LICENSE_FILE
    license = ap.License()
    license.set_license(license_file)
```

