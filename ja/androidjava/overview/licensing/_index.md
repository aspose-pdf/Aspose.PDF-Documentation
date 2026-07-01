---
title: ライセンスと制限
linktitle: ライセンスと制限
type: docs
weight: 50
url: /ja/androidjava/licensing/
description: Aspose.PDF for Android via Java は、顧客に Classic license と Metered License の取得を推奨しています。また、製品をより詳しく探るために制限付きライセンスを使用することもできます。
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 評価版の制限

お客様が購入前にコンポーネントを十分にテストできるように、評価版では通常通り使用できるようになっています。

- **評価用透かしが付いた PDF** Aspose.PDF for Android via Java の評価版は製品の全機能を提供しますが、生成された PDF ドキュメントのすべてのページの上部に「Evaluation Only. Created with Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd」という透かしが入ります。

- **処理できるコレクション項目数の上限。**
評価版では、いずれのコレクションでも処理できる要素は4つまでです（例として、ページ4枚、フォームフィールド4件など）。

Aspose.PDF for Android via Java の評価版は以下からダウンロードできます [Aspose Repository](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf). 評価版は製品の有償版と全く同じ機能を提供します。さらに、ライセンスを購入し、ライセンスを適用するための数行のコードを追加するだけで、評価版は有償版になります。

**Aspose.PDF** の評価に満足したら、次のことができます [ライセンスを購入する](https://purchase.aspose.com/) Aspose のウェブサイトで。提供されているさまざまなサブスクリプションタイプに慣れてください。ご質問がある場合は、遠慮なく Aspose の営業チームにお問い合わせください。

すべての Aspose ライセンスには、1 年間のサブスクリプションが付属しており、その期間中にリリースされる新しいバージョンや修正への無料アップグレードが受けられます。テクニカルサポートは無料かつ無制限で、ライセンスユーザーおよび評価ユーザーの両方に提供されます。

>評価版の制限なしで Java を使用して Aspose.PDF for Android をテストしたい場合は、30 日間の一時ライセンスをリクエストすることもできます。参照してください [一時ライセンスの取得方法は？](https://purchase.aspose.com/temporary-license)

## クラシック ライセンス

ライセンスはファイルまたはストリームオブジェクトから読み込むことができます。ライセンスを設定する最も簡単な方法は、ライセンスファイルを Aspose.PDF.dll ファイルと同じフォルダーに配置し、パスなしでファイル名を指定することです。以下の例に示すように。

ライセンスはプレーンテキストの XML ファイルで、製品名、ライセンス対象の開発者数、サブスクリプションの有効期限などの詳細が含まれています。このファイルはデジタル署名されているため、ファイルを変更しないでください。余分な改行を誤って追加しただけでも無効になります。

ドキュメントの操作を行う前にライセンスを設定する必要があります。ライセンスの設定は、アプリケーションまたはプロセスあたり一度だけで構いません。

ライセンスはストリームまたはファイルから、以下の場所で読み込むことができます。

1. 明示的なパス。
1. aspose-pdf-xx.x.jar を含むフォルダー。

コンポーネントにライセンスを設定するには License.setLicense メソッドを使用します。ライセンスを設定する最も簡単な方法は、ライセンス ファイルを Aspose.PDF.jar と同じフォルダーに置き、以下の例に示すようにパスなしでファイル名だけを指定することです。

{{% alert color="primary" %}}

Aspose.PDF for Java 4.2.0 以降、ライセンスを初期化するために以下のコード行を呼び出す必要があります。

{{% /alert %}}

### ファイルからライセンスをロードする

この例では **Aspose.PDF** が、アプリケーションの JAR が含まれるフォルダー内のライセンス ファイルを探そうとします。

```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Call setLicense method to set license
license.setLicense("Aspose.Pdf.Java.lic");
```

### ストリーム オブジェクトからライセンスを読み込む

次の例は、ストリームからライセンスを読み込む方法を示しています。

```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Set license from Stream
license.setLicense(new java.io.FileInputStream("Aspose.Pdf.Java.lic"));
```

#### 2005/01/22以前に購入されたライセンスを設定する

**Aspose.PDF** for Java は古いライセンスをサポートしていませんので、弊社までご連絡ください [営業チーム](https://company.aspose.com/contact) 新しいライセンスファイルを取得する。

### ライセンスを検証する

ライセンスが正しく設定されているかどうかを検証することができます。Document クラスには、ライセンスが正しく設定されている場合に true を返す isLicensed メソッドがあります。

```java
License license = new License();
license.setLicense("Aspose.Pdf.Java.lic");
// Check if license has been validated
if (com.aspose.pdf.Document.isLicensed()) {
    System.out.println("License is Set!");
}
```
## 従量課金ライセンス

Aspose.PDF は開発者が従量キーを適用できるようにします。これは新しいライセンス機構です。新しいライセンス機構は既存のライセンス方法と併用されます。API機能の使用量に基づいて請求されたい顧客は従量制ライセンスを利用できます。 詳細については、こちらをご参照ください [従量制ライセンス FAQ](https://purchase.aspose.com/faqs/licensing/metered) セクション。

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
## Aspose の複数製品を使用する

アプリケーションで複数の Aspose 製品、たとえば Aspose.PDF と Aspose.Words を使用する場合、以下の便利なヒントをご紹介します。

- **各 Aspose 製品ごとにライセンスを個別に設定します。** たとえすべてのコンポーネントに対して単一のライセンス ファイル（例: 'Aspose.Total.lic'）があっても、アプリケーションで使用している各 Aspose 製品に対して **License.SetLicense** を個別に呼び出す必要があります。
- **完全修飾ライセンス クラス名を使用します。** 各 Aspose 製品には名前空間に **License** クラスが含まれています。たとえば、Aspose.PDF には **com.aspose.pdf.License** が、Aspose.Words には **com.aspose.words.License** クラスがあります。完全修飾クラス名を使用することで、どのライセンスがどの製品に適用されているかについての混乱を防ぐことができます。

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
