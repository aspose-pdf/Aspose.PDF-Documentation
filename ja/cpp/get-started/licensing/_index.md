---
title: Aspose PDF License
linktitle: Licensing and limitations
type: docs
weight: 90
url: /ja/cpp/licensing/
description: Aspose. PDF for C++ は、Classic ライセンスと Metered ライセンスを取得することをお勧めします。また、製品をよりよく探索するために制限付きライセンスを使用します。
lastmod: "2021-11-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 評価版の制限

お客様には購入前にコンポーネントを徹底的にテストしていただきたいと考えており、評価版では通常どおり使用することができます。ただし、API の評価版を使用する際には、以下の制限があります。

**評価ウォーターマーク付きで作成された PDF**
Aspose.PDF for C++ の評価版は完全な製品機能を提供しますが、生成された PDF ドキュメントのすべてのページには、「Evaluation Only. Created with Aspose.PDF. Copyright 2002-2017 Aspose Pty Ltd」というウォーターマークが上部に表示されます。

**処理可能なコレクションアイテムの数の制限**

評価版では、任意のコレクションから4つのアイテムのみを処理できます（例えば、4ページ、4つのフォームフィールドなど）。

## ファイルまたはストリームオブジェクトを使用してライセンスを適用する

ライセンスはファイルまたはストリームオブジェクトから読み込むことができます。Aspose.PDF for C++ は次の場所でライセンスを探そうとします:

1. 明示的なパス。
1. Aspose.PDF.dll を含むフォルダー。
1. Aspose.PDF.dll を呼び出したアセンブリを含むフォルダー。
1. エントリアセンブリ（あなたの .exe）を含むフォルダー。
1. Aspose.PDF.dll を呼び出したアセンブリに埋め込まれたリソース。

ライセンスを設定する最も簡単な方法は、ライセンスファイルを Aspose.PDF.dll ファイルと同じフォルダーに配置し、パスなしでファイル名を指定することです。以下の例に示します。

### ファイルからライセンスを読み込む

ライセンスを適用する最も簡単な方法は、ライセンスファイルを Aspose.PDF.dll ファイルと同じフォルダーに配置し、パスなしでファイル名を指定することです。

{{% alert color="primary" %}}

SetLicense メソッドを呼び出すときに渡すライセンス名は、ライセンスファイルの名前である必要があります。 ライセンスファイル名を「Aspose.PDF.lic.xml」に変更した場合、そのファイル名を Pdf->SetLicense(…) メソッドに渡します。

{{% /alert %}}

```cpp
auto lic = MakeObject<Aspose::Pdf::License>();
lic->SetLicense(L"Aspose.PDF.Cpp.lic");
```

### ストリームオブジェクトからライセンスを読み込む

次の例は、ストリームからライセンスを読み込む方法を示しています。

```cpp
intrusive_ptr<License>license = new License();
intrusive_ptr<FileStream> myStream = new FileStream(new String("Aspose.PDF.Cpp.lic"), FileMode_Open);

license->SetLicense(myStream);
```

## メータードライセンス

Aspose.PDFは、開発者がメータードキーを適用することを可能にします。これは新しいライセンス機構です。この新しいライセンス機構は、既存のライセンス方法と共に使用されます。API機能の使用量に基づいて課金されたい顧客は、メータードライセンスを使用できます。詳細は、メータードライセンスFAQセクションを参照してください。

メータードキーを適用するために新しいクラスMeteredが導入されました。 以下は、メーター付きの公開鍵と秘密鍵を設定する方法を示すサンプルコードです。

詳細については、[メーター付きライセンスのFAQ](https://purchase.aspose.com/faqs/licensing/metered)セクションを参照してください。