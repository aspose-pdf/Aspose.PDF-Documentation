---  
title: ライセンスと制限  
linktitle: ライセンスと制限  
type: docs  
weight: 90  
url: /java/licensing/  
description: Aspose.PDF for Java は、クラシックライセンスとメータードライセンスを取得することを顧客に勧めています。また、製品をよりよく探索するために限定ライセンスを使用します。  
lastmod: "2021-06-05"  
sitemap:  
    changefreq: "weekly"  
    priority: 0.7  
---  

## 評価版の制限

私たちは顧客に購入前にコンポーネントを十分にテストしていただきたいので、評価版では通常通りに使用することができます。

- **評価用の透かしが入ったPDFが作成されます。** Aspose.PDF for Javaの評価版は製品の全機能を提供しますが、生成されたPDFドキュメントのすべてのページの上部に「Evaluation Only. Created with Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd」という透かしが入ります。

- **処理可能なコレクションアイテムの数の制限。**

評価版では、いかなるコレクションからも4つの要素（例えば、4ページ、4つのフォームフィールドなど）のみを処理することができます。

You can download an evaluation version of **Aspose.PDF** for Java from [Aspose Repository](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf). The evaluation version provides absolutely the same capabilities as the licensed version of the product. Furthermore, evaluation version simply becomes licensed when you purchase a license and add a couple of lines of code to apply the license.

**Aspose.PDF** の評価版は、[Aspose リポジトリ](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf)からダウンロードできます。評価版は、製品のライセンス版とまったく同じ機能を提供します。さらに、ライセンスを購入し、ライセンスを適用するための数行のコードを追加すると、評価版がライセンス版になります。

Once you are happy with your evaluation of **Aspose.PDF**, you can [purchase a license](https://purchase.aspose.com/) at the Aspose website. Make yourself familiar with the different subscription types offered. If you have any questions, do not hesitate to contact the Aspose sales team.

**Aspose.PDF** の評価に満足したら、Aspose のウェブサイトで[ライセンスを購入](https://purchase.aspose.com/)できます。提供されているさまざまなサブスクリプションタイプを確認してください。ご不明な点がございましたら、Aspose の営業チームにお気軽にお問い合わせください。

Every Aspose license carries a one-year subscription for free upgrades to any new versions or fixes that come out during this time. Technical support is free and unlimited and provided both to licensed and evaluation users.

すべての Aspose ライセンスには、1年間のサブスクリプションが付属しており、この期間中にリリースされる新しいバージョンや修正プログラムへの無料アップグレードが含まれています。技術サポートは無料で無制限であり、ライセンスユーザーと評価ユーザーの両方に提供されます。

>If you want to test Aspose.PDF for Java without the evaluation version limitations, you can also request a 30-day Temporary License.

>評価版の制限なしで Aspose.PDF for Java をテストしたい場合は、30日間の一時ライセンスをリクエストすることもできます。
 [一時ライセンスの取得方法](https://purchase.aspose.com/temporary-license)を参照してください。

## クラシックライセンス

ライセンスはファイルまたはストリームオブジェクトから読み込むことができます。ライセンスを設定する最も簡単な方法は、ライセンスファイルをAspose.PDF.dllファイルと同じフォルダに置き、パスなしでファイル名を指定することです。以下の例に示されています。

ライセンスはプレーンテキストのXMLファイルで、製品名、ライセンスが与えられた開発者の数、サブスクリプションの有効期限などの詳細が含まれています。ファイルはデジタル署名されているため、ファイルを変更しないでください。ファイルに余分な改行を加えるだけでも無効になります。

ドキュメントで操作を行う前にライセンスを設定する必要があります。ライセンスはアプリケーションまたはプロセスごとに一度だけ設定する必要があります。

ライセンスは以下の場所からストリームまたはファイルで読み込むことができます：

1. 明示的なパス。
1. aspose-pdf-xx.x.jarを含むフォルダ。

License.setLicenseメソッドを使用してコンポーネントにライセンスを設定します。 ライセンスを設定する最も簡単な方法は、多くの場合、ライセンスファイルをAspose.PDF.jarと同じフォルダーに配置し、次の例に示すようにパスなしでファイル名だけを指定することです。

{{% alert color="primary" %}}

Aspose.PDF for Java 4.2.0以降では、ライセンスを初期化するために次のコード行を呼び出す必要があります。

{{% /alert %}}

### ファイルからライセンスを読み込む

この例では、**Aspose.PDF** がアプリケーションのJARが含まれるフォルダーでライセンスファイルを見つけようとします。

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

#### 2005/01/22以前に購入されたライセンスを設定する**Aspose.PDF** for Javaは、古いライセンスをサポートしなくなったため、新しいライセンスファイルを取得するには[営業チーム](https://company.aspose.com/contact)にお問い合わせください。

### ライセンスの検証

ライセンスが適切に設定されているかどうかを検証することができます。DocumentクラスにはisLicensedメソッドがあり、ライセンスが適切に設定されている場合はtrueを返します。

```java
License license = new License();
license.setLicense("Aspose.Pdf.Java.lic");
// ライセンスが検証されたかどうかを確認
if (com.aspose.pdf.Document.isLicensed()) {
    System.out.println("ライセンスが設定されています！");
}
```
## 計量制ライセンス

Aspose.PDFは、開発者が計量キーを適用することを可能にします。これは新しいライセンスメカニズムです。新しいライセンスメカニズムは、既存のライセンス方法と一緒に使用されます。API機能の使用量に基づいて請求されたい顧客は、計量制ライセンスを使用できます。詳細については、[計量制ライセンスFAQ](https://purchase.aspose.com/faqs/licensing/metered)セクションを参照してください。

新しいクラス[Metered](https://reference.aspose.com/pdf/java/com.aspose.pdf/Metered)が導入され、計量キーを適用します。
 以下は、メータードパブリックキーとプライベートキーの設定方法を示すサンプルコードです。

```java
String publicKey = "";
String privateKey = "";

Metered m = new Metered();
m.setMeteredKey(publicKey, privateKey);

// オプションで、有効なライセンスが適用されている場合はtrueを返します。
// コンポーネントが評価モードで実行されている場合はfalseを返します。
License lic = new License();
System.out.println("License is set = " + lic.isLicensed());
```
## Asposeの複数製品の使用

アプリケーションで複数のAspose製品を使用する場合、例えばAspose.PDFとAspose.Words、以下のいくつかの有用なヒントがあります。

- **各Aspose製品に対してライセンスを個別に設定します。** すべてのコンポーネントに対して単一のライセンスファイルを持っている場合でも、例えば 'Aspose.Total.lic'、アプリケーションで使用している各Aspose製品に対して**License.SetLicense**を個別に呼び出す必要があります。
- **完全修飾ライセンスクラス名を使用します。** 各Aspose製品は、その名前空間に**License**クラスを持っています。 たとえば、Aspose.PDFには**com.aspose.pdf.License**があり、Aspose.Wordsには**com.aspose.words.License**クラスがあります。完全修飾クラス名を使用することで、どのライセンスがどの製品に適用されているかについての混乱を避けることができます。

```java
// Aspose.Pdfのライセンスクラスをインスタンス化する
com.aspose.pdf.License license = new com.aspose.pdf.License();
// ライセンスを設定する
license.setLicense("Aspose.Total.Java.lic");

// Aspose.Words for Javaのライセンスを設定する

// Aspose.Wordsのライセンスクラスをインスタンス化する
com.aspose.words.License licenseaw = new com.aspose.words.License();
// ライセンスを設定する
licenseaw.setLicense("Aspose.Total.Java.lic");
```