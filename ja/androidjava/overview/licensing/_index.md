---
title: ライセンスと制限
linktitle: ライセンスと制限
type: docs
weight: 50
url: /ja/androidjava/licensing/
description: Aspose.PDF for Android via Java は、クラシックライセンスとメーターライセンスを取得するよう顧客に勧めています。また、製品をよりよく探索するために限定ライセンスを使用します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 評価版の制限

私たちはお客様に購入前にコンポーネントを徹底的にテストしていただきたいと考えており、そのため評価版では通常どおり使用することができます。

- **評価用透かしで作成されたPDF。** Aspose.PDF for Android via Java の評価版は、製品の完全な機能を提供しますが、生成されたPDFドキュメントのすべてのページの上部に「Evaluation Only. Created with Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd」という透かしが入ります。

- **処理できるコレクションアイテム数の制限。**

評価版では、任意のコレクションから4つの要素のみを処理できます（例: 4ページ、4つのフォームフィールドなど）。

You can download an evaluation version of Aspose.PDF for Android via Java from [Aspose Repository](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf). The evaluation version provides absolutely the same capabilities as the licensed version of the product. Furthermore, evaluation version simply becomes licensed when you purchase a license and add a couple of lines of code to apply the license.

Aspose.PDF の評価にご満足いただけましたら、Aspose のウェブサイトで[ライセンスを購入](https://purchase.aspose.com/)できます。提供されているさまざまなサブスクリプションタイプを確認してください。質問がある場合は、Aspose の営業チームにお問い合わせください。

すべての Aspose ライセンスには、1年間の無料アップグレードサブスクリプションが付属しており、この期間中に新しいバージョンや修正が公開された場合に利用できます。技術サポートは無料で無制限に提供され、ライセンスユーザーと評価ユーザーの両方に提供されます。

>評価版の制限なしで Aspose.PDF for Android via Java をテストしたい場合は、30日間の一時ライセンスをリクエストすることもできます。
 [一時ライセンスの取得方法](https://purchase.aspose.com/temporary-license)を参照してください。

## クラシックライセンス

ライセンスはファイルまたはストリームオブジェクトから読み込むことができます。ライセンスを設定する最も簡単な方法は、ライセンスファイルをAspose.PDF.dllファイルと同じフォルダーに置き、パスなしでファイル名を指定することです。以下の例に示します。

ライセンスはプレーンテキストのXMLファイルで、製品名、ライセンスが付与されている開発者の数、サブスクリプションの有効期限などの詳細が含まれています。ファイルはデジタル署名されているため、ファイルを変更しないでください。ファイルに余分な改行を不注意に追加しても、無効になります。

ドキュメントを操作する前にライセンスを設定する必要があります。アプリケーションまたはプロセスごとに、ライセンスの設定は1回だけ必要です。

ライセンスは以下の場所からストリームまたはファイルとして読み込むことができます:

1. 明示的なパス。
1. aspose-pdf-xx.x.jarを含むフォルダー。

License.setLicenseメソッドを使用してコンポーネントにライセンスを設定します。 ライセンスを設定する最も簡単な方法は、ライセンスファイルをAspose.PDF.jarと同じフォルダに置き、次の例に示すようにパスを指定せずにファイル名だけを指定することです。

{{% alert color="primary" %}}

Aspose.PDF for Java 4.2.0から、ライセンスを初期化するために次のコード行を呼び出す必要があります。

{{% /alert %}}

### ファイルからライセンスを読み込む

この例では、**Aspose.PDF**がアプリケーションのJARが含まれているフォルダ内でライセンスファイルを見つけようとします。

```java
// ライセンスインスタンスを初期化
com.aspose.pdf.License license = new com.aspose.pdf.License();
// setLicenseメソッドを呼び出してライセンスを設定
license.setLicense("Aspose.Pdf.Java.lic");
```

### ストリームオブジェクトからライセンスを読み込む

次の例は、ストリームからライセンスを読み込む方法を示しています。

```java
// ライセンスインスタンスを初期化
com.aspose.pdf.License license = new com.aspose.pdf.License();
// ストリームからライセンスを設定
license.setLicense(new java.io.FileInputStream("Aspose.Pdf.Java.lic"));
```

#### 2005/01/22以前に購入したライセンスの設定
**Aspose.PDF** for Java は古いライセンスをサポートしなくなったため、新しいライセンスファイルを取得するには[営業チーム](https://company.aspose.com/contact)にお問い合わせください。

### ライセンスの検証

ライセンスが正しく設定されているかどうかを検証することが可能です。Document クラスには isLicensed メソッドがあり、ライセンスが正しく設定されている場合は true を返します。

```java
License license = new License();
license.setLicense("Aspose.Pdf.Java.lic");
// ライセンスが検証されているか確認する
if (com.aspose.pdf.Document.isLicensed()) {
    System.out.println("License is Set!");
}
```
## メーター制ライセンス

Aspose.PDF は、開発者がメーター制キーを適用できるようにします。これは新しいライセンスメカニズムです。新しいライセンスメカニズムは、既存のライセンス方法とともに使用されます。API 機能の使用量に基づいて請求を受けたいお客様は、メーター制ライセンスを使用できます。詳細については、[メーター制ライセンス FAQ](https://purchase.aspose.com/faqs/licensing/metered) セクションを参照してください。

```java
String publicKey = "";
String privateKey = "";

Metered m = new Metered();
m.setMeteredKey(publicKey, privateKey);

// オプションで、有効なライセンスが適用されている場合は true を返します;
// コンポーネントが評価モードで実行されている場合は false を返します。
License lic = new License();
System.out.println("License is set = " + lic.isLicensed());
```

## Asposeの複数製品の使用

アプリケーションで複数のAspose製品を使用する場合、例えばAspose.PDFとAspose.Words、以下はいくつかの有用なヒントです。

- **各Aspose製品に対してライセンスを個別に設定する。** すべてのコンポーネントに対して単一のライセンスファイルを持っている場合でも、例えば『Aspose.Total.lic』、アプリケーションで使用しているそれぞれのAspose製品に対して**License.SetLicense**を個別に呼び出す必要があります。
- **完全修飾されたライセンスクラス名を使用する。** 各Aspose製品には、その名前空間に**License**クラスがあります。例えば、Aspose.PDFには**com.aspose.pdf.License**があり、Aspose.Wordsには**com.aspose.words.License**クラスがあります。完全修飾されたクラス名を使用することで、どのライセンスがどの製品に適用されているかについての混乱を避けることができます。

```java
// Aspose.PdfのLicenseクラスをインスタンス化
com.aspose.pdf.License license = new com.aspose.pdf.License();
// ライセンスを設定
license.setLicense("Aspose.Total.Java.lic");

// Aspose.Words for Javaのライセンスを設定

// Aspose.WordsのLicenseクラスをインスタンス化
com.aspose.words.License licenseaw = new com.aspose.words.License();
// ライセンスを設定
licenseaw.setLicense("Aspose.Total.Java.lic");
```