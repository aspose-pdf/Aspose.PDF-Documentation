---
title: ライセンスと制限
linktitle: ライセンスと制限
type: docs
weight: 90
url: /ja/php-java/licensing/
description: Aspose.PDF for PHP via Javaは、クラシックライセンスとメータードライセンスを取得するよう顧客に招待しています。また、製品をよりよく探求するために限定ライセンスを使用できます。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 評価版の制限

私たちはお客様に購入前にコンポーネントを徹底的にテストしていただきたいと考えているため、評価版は通常通りに使用することができます。

- **評価用透かしが付いたPDFの作成。** Aspose.PDF for PHP via Javaの評価版は、製品の全機能を提供しますが、生成されたPDFドキュメントのすべてのページには、上部に「Evaluation Only. Created with Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd」と透かしが入ります。

- **処理可能なコレクションアイテムの数の制限。**

評価版では、任意のコレクションから4つの要素（例えば、4ページ、4つのフォームフィールドなど）のみを処理できます。

You can download an evaluation version of **Aspose.PDF** for Java from [Aspose Repository](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf). 評価版は、製品のライセンス版と全く同じ機能を提供します。さらに、評価版はライセンスを購入し、ライセンスを適用するコードを数行追加することで、ライセンス版になります。

**Aspose.PDF** の評価に満足したら、Aspose のウェブサイトで[ライセンスを購入](https://purchase.aspose.com/)することができます。 提供されているさまざまなサブスクリプションタイプをよく理解してください。ご質問がある場合は、Aspose の営業チームに遠慮なくお問い合わせください。

すべての Aspose ライセンスには、1年間の無料アップグレードサブスクリプションが含まれており、この期間中にリリースされる新しいバージョンや修正を受け取ることができます。技術サポートは無料で無制限に提供され、ライセンスユーザーと評価ユーザーの両方に提供されます。

>Java 経由で PHP 用の Aspose.PDF を評価版の制限なしでテストしたい場合は、30 日間の一時的なライセンスをリクエストすることもできます。
 [一時ライセンスの取得方法](https://purchase.aspose.com/temporary-license)を参照してください。

## クラシックライセンス

ライセンスはファイルまたはストリームオブジェクトから読み込むことができます。ライセンスを設定する最も簡単な方法は、Aspose.PDF.dllファイルと同じフォルダーにライセンスファイルを置き、パスを指定せずにファイル名を指定することです。以下の例に示されているようにします。

ライセンスはプレーンテキストのXMLファイルで、製品名、ライセンスが付与されている開発者の数、サブスクリプションの有効期限などの詳細が含まれています。ファイルはデジタル署名されているため、ファイルを変更しないでください。ファイルに余分な改行を加えてしまっても無効になります。

ドキュメントで操作を行う前にライセンスを設定する必要があります。ライセンスはアプリケーションまたはプロセスごとに一度だけ設定する必要があります。

ライセンスは以下の場所からストリームまたはファイルとして読み込むことができます：

1. 明示的なパス。
1. aspose-pdf-xx.x.jarを含むフォルダー。

コンポーネントにライセンスを設定するには、License.setLicenseメソッドを使用します。 しばしばライセンスを設定する最も簡単な方法は、ライセンスファイルを Aspose.PDF.jar と同じフォルダに置き、次の例に示すようにパスを指定せずにファイル名だけを指定することです。

{{% alert color="primary" %}}

Aspose.PDF for PHP via Java バージョン 4.2.0 以降、ライセンスを初期化するために次のコード行を呼び出す必要があります。

{{% /alert %}}

### ファイルからライセンスを読み込む

この例では、**Aspose.PDF** はアプリケーションの JARs を含むフォルダ内でライセンスファイルを見つけようとします。

```java
// ライセンスインスタンスを初期化
com.aspose.pdf.License license = new com.aspose.pdf.License();
// setLicense メソッドを呼び出してライセンスを設定
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

#### 2005/01/22 以前に購入したライセンスの設定**Aspose.PDF** for Java は古いライセンスをサポートしなくなったため、新しいライセンスファイルを取得するには[営業チーム](https://company.aspose.com/contact)にお問い合わせください。

### ライセンスの検証

ライセンスが正しく設定されているかどうかを確認することが可能です。Document クラスにはライセンスが適切に設定されている場合に true を返す isLicensed メソッドがあります。

```java
License license = new License();
license.setLicense("Aspose.Pdf.Java.lic");
// ライセンスが検証されたかどうかを確認
if (com.aspose.pdf.Document.isLicensed()) {
    System.out.println("ライセンスが設定されています！");
}
```
## メータードライセンス

Aspose.PDF は開発者がメータードキーを適用することを可能にします。これは新しいライセンスメカニズムです。この新しいライセンスメカニズムは、既存のライセンス方法と共に使用されます。API 機能の使用に基づいて請求されたいお客様は、メータードライセンスを使用できます。詳細については、[メータードライセンス FAQ](https://purchase.aspose.com/faqs/licensing/metered) セクションを参照してください。

新しいクラス [Metered](https://reference.aspose.com/pdf/java/com.aspose.pdf/Metered) がメータードキーを適用するために導入されています。
 以下は、メーター制御されたパブリックキーとプライベートキーを設定する方法を示すサンプルコードです。

```java
String publicKey = "";
String privateKey = "";

Metered m = new Metered();
m.setMeteredKey(publicKey, privateKey);

// オプションで、有効なライセンスが適用されている場合はtrueを返し、
// コンポーネントが評価モードで動作している場合はfalseを返します。
License lic = new License();
System.out.println("ライセンスが設定されています = " + lic.isLicensed());
```
## Asposeの複数の製品を使用する

アプリケーションで複数のAspose製品を使用する場合、例えばAspose.PDFとAspose.Words、以下はいくつかの役立つヒントです。

- **各Aspose製品に対して個別にライセンスを設定する。** すべてのコンポーネントに対して単一のライセンスファイルがある場合でも、例えば 'Aspose.Total.lic'、アプリケーションで使用している各Aspose製品に対して**License.SetLicense**を個別に呼び出す必要があります。
- **完全修飾されたライセンスクラス名を使用する。** 各Aspose製品には、その名前空間に**License**クラスがあります。 たとえば、Aspose.PDFには**com.aspose.pdf.License**があり、Aspose.Wordsには**com.aspose.words.License**クラスがあります。完全修飾クラス名を使用することで、どのライセンスがどの製品に適用されるかについての混乱を避けることができます。

```java
// Aspose.PdfのLicenseクラスをインスタンス化
com.aspose.pdf.License license = new com.aspose.pdf.License();
// ライセンスを設定
license.setLicense("Aspose.Total.Java.lic");

// Java用Aspose.Wordsのライセンスを設定

// Aspose.WordsのLicenseクラスをインスタンス化
com.aspose.words.License licenseaw = new com.aspose.words.License();
// ライセンスを設定
licenseaw.setLicense("Aspose.Total.Java.lic");
```