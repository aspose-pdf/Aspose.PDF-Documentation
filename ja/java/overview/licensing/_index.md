---
title: Aspose PDF ライセンス
linktitle: ライセンスと制限
type: docs
weight: 50
url: /ja/java/licensing/
description: "Aspose.PDF for Python では、顧客に対してクラシック ライセンスの取得を推奨しています。また、製品をよりよく探索できるよう、限定ライセンスの使用も可能です。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Java のライセンス
Abstract: "この記事では、Aspose.PDF for Python の制限とライセンスオプションについて説明しています。評価版はフル機能のテストが可能ですが、生成された PDF に透かしが追加され、「Evaluation Only」とともに著作権情報が表示されます。これらの制限なしでテストしたいユーザー向けに、30 日間の Temporary License が利用可能です。また、クラシック ライセンスをファイルまたはストリームからロードして実装する方法についても説明しており、ライセンス ファイルを Aspose.PDF.dll と同じディレクトリに配置し、`Aspose.Pdf.License` クラスを使用してライセンスを設定することを推奨しています。ライセンス プロセスを示すコード スニペットが提供されています。"
---
## 評価版の制限

私たちは顧客に購入前にコンポーネントを徹底的にテストしてもらいたく、評価版では通常通り使用できるようにしています。

- **評価用ウォーターマーク付きPDF。** Aspose.PDF for Java の評価版は製品の全機能を提供しますが、生成された PDF 文書のすべてのページの上部に「Evaluation Only. Created with Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd」というウォーターマークが付加されます。

- **処理できるコレクション項目数の上限。**
評価版では、任意のコレクションから処理できる要素は4つまでです（例：ページ4枚、フォームフィールド4つなど）。

Java 用の **Aspose.PDF** の評価版は、以下からダウンロードできます [Aspose リポジトリ](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf)。評価版は、製品のライセンス版とまったく同じ機能を提供します。さらに、評価版はライセンスを購入し、ライセンスを適用するための数行のコードを追加するだけで、ライセンス版に切り替わります。

**Aspose.PDF** の評価に満足したら、[ライセンスを購入する](https://purchase.aspose.com/) ことができます。提供されているさまざまなサブスクリプションタイプに慣れ親しんでください。質問がある場合は、遠慮なく Aspose の営業チームにお問い合わせください。

すべての Aspose ライセンスには、1 年間のサブスクリプションが付帯しており、その期間中にリリースされる新バージョンや修正に対して無料でアップグレードできます。テクニカルサポートは無料で無制限に提供され、ライセンスユーザーおよび評価ユーザーの両方に提供されます。

評価版の制限なしで Aspose.PDF for Java をテストしたい場合、
30 日間の一時ライセンスを要求することもできます。詳しくは、[Temporary License の取得方法は？](https://purchase.aspose.com/temporary-license) を参照してください。

## Classic ライセンス

ライセンスは、ファイルまたはストリーム オブジェクトから読み込むことができます。ライセンスを設定する最も簡単な方法は、以下の例に示すように、ライセンス ファイルを Aspose.PDF.dll ファイルと同じフォルダーに配置し、パスなしでファイル名だけを指定することです。

ライセンスはプレーン テキストの XML ファイルであり、製品名やライセンス対象の開発者数、サブスクリプションの有効期限などの詳細が含まれています。このファイルはデジタル署名されているため、変更しないでください。余分な改行を誤って追加しただけでも無効になります。

ドキュメントに対して操作を実行する前にライセンスを設定する必要があります。ライセンスは、アプリケーションまたはプロセスごとに一度だけ設定すればよいです。

ライセンスは、ストリームまたはファイルから、次の場所でロードできます。

1. 明示的なパスです。
1. aspose-pdf-`xx.x.jar` を含むフォルダーです。

License.`setLicense` メソッドを使用してコンポーネントにライセンスを設定します。ライセンスを設定する最も簡単な方法は、ライセンス ファイルを `Aspose.PDF.jar` と同じフォルダーに配置し、パスを指定せずにファイル名だけを指定することです。以下の例に示すように、

{{% alert color="primary" %}}

Aspose.PDF for Java 4.2.0 以降では、ライセンスを初期化するために次のコード行を呼び出す必要があります。

{{% /alert %}}

### ファイルからライセンスを読み込む

この例では、**Aspose.PDF** がアプリケーションの JAR が含まれるフォルダー内のライセンスファイルを検索しようとします。

```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Call setLicense method to set license
license.setLicense("Aspose.Pdf.Java.lic");
```

### ストリームオブジェクトからライセンスを読み込む

以下の例は、ストリームからライセンスを読み込む方法を示します。

```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Set license from Stream
license.setLicense(new java.io.FileInputStream("Aspose.Pdf.Java.lic"));
```

### ライセンスの検証

ライセンスが正しく設定されたかどうかを検証することが可能です。`Document` クラスには、ライセンスが正しく設定されている場合に true を返す `isLicensed` メソッドがあります。

```java
License license = new License();
license.setLicense("Aspose.Pdf.Java.lic");
// Check if license has been validated
if (com.aspose.pdf.Document.isLicensed()) {
    System.out.println("License is Set!");
}
```

## 従量制ライセンス

Aspose.PDF は、開発者が従量キーを適用できるようにします。これは新しいライセンス機構です。新しいライセンス機構は、既存のライセンス方式と併用されます。API 機能の使用量に基づいて課金されたい顧客は、従量ライセンスを使用できます。詳細については、[従量ライセンス FAQ](https://purchase.aspose.com/faqs/licensing/metered) セクションをご参照ください。

新しいクラス [Metered](https://reference.aspose.com/pdf/java/com.aspose.pdf/Metered) は、メーター キーを適用するために導入されました。以下は、メーターの公開キーとプライベートキーを設定する方法を示すサンプルコードです。

```java
String publicKey = "";
String privateKey = "";

Metered m = new Metered();
m.setMeteredKey(publicKey, privateKey);

// Optionally, the following two lines returns true if a valid license has been applied;
// false if the component is running in evaluation mode.
License lic = new License();
System.out.println("License is set = " + lic.isLicensed());
```

## Aspose の複数製品の使用

アプリケーションで複数の Aspose 製品（例: Aspose.PDF と Aspose.Words）を使用する場合、いくつかの便利なヒントをご紹介します。

- **各 Aspose 製品ごとにライセンスを個別に設定します。** たとえすべてのコンポーネント用の単一ライセンス ファイル（例: ’`Aspose.Total.lic`’）があっても、アプリケーションで使用している各 Aspose 製品に対して **License.SetLicense** を個別に呼び出す必要があります。
- **完全修飾ライセンス クラス名を使用します。** 各 Aspose 製品は名前空間に **License** クラスを持っています。たとえば、Aspose.PDF には **com.aspose.pdf.License** があり、Aspose.Words には **com.aspose.words.License** クラスがあります。完全修飾クラス名を使用することで、どのライセンスがどの製品に適用されているかについての混乱を防げます。

```java
// Instantiate the License class of Aspose.Pdf
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Set the license
license.setLicense("Aspose.Total.Java.lic");

// Setting license for Aspose.Words for Java

// Instantiate the License class of Aspose.Words
com.aspose.words.License licenseaw = new com.aspose.words.License();
// Set the license
licenseaw.setLicense("Aspose.Total.Java.lic");
```
