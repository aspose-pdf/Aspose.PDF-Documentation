---  
title: Aspose.PDF for Javaのインストール  
linktitle: インストール  
type: docs  
weight: 20  
url: ja/java/installation/  
description: このセクションでは、Aspose.PDF for Javaの製品説明と、自分でインストールする方法およびNuGetを使用する方法を示します。  
lastmod: "2021-06-05"  
sitemap:  
    changefreq: "weekly"  
    priority: 0.7  
---

## Aspose.PDF for Javaコンポーネント

{{% alert color="primary" %}}

**Aspose.PDFはJavaの** コンポーネントであり、開発者がプログラムで動的にPDFドキュメントを作成できるように設計されています。Aspose.PDF for Javaを使用すると、開発者はPDFドキュメントにテーブル、グラフ、画像、ハイパーリンク、カスタムフォントなどを挿入できます。さらに、PDFドキュメントを圧縮することも可能です。Aspose.PDF for Javaは、セキュアなPDFドキュメントを作成するための優れたセキュリティ機能を提供します。そして、Aspose.PDF for Javaの最も特徴的な機能は、APIとXMLテンプレートの両方からPDFドキュメントを作成できることです。

{{% /alert %}}

## 製品説明

 **Aspose.PDF for Java** はJavaを使用して実装されており、JDK 1.8以上で動作します。Aspose.PDF for Javaは、JSP/JSFウェブアプリケーションやWindowsアプリケーションなど、任意のアプリケーションに統合できます。

**Aspose.PDF for Java** は高速で軽量です。PDFドキュメントを効率的に作成し、アプリケーションのパフォーマンスを向上させます。Aspose.PDF for Javaは、その価格、優れたパフォーマンス、素晴らしいサポートのため、PDFドキュメントを作成する際に顧客の第一選択肢となっています。このライブラリを使用すると、Adobe Acrobatをインストールせずに、ゼロからPDFファイルを作成したり、既存のPDFドキュメントを完全に処理したりするための豊富な機能を実装できます。

# インストール

## Aspose.PDF for Javaを評価する

{{% alert color="primary" %}}

評価のために [Aspose.PDF for Java](https://releases.aspose.com/java/repo/com/aspose/aspose-pdf/) をダウンロードできます。
 ダウンロード評価版は、購入版ダウンロードと同じです。評価版は、[ライセンスを適用する](/pdf/java/licensing/)ために数行のコードを追加すると、ライセンス版になります。
{{% /alert %}}

評価版のAspose.PDFは全機能を提供しますが、2つの制限があります：

- 評価用の透かしが挿入されます。
- どのコレクションも4つ以上の要素を表示/編集することができません。
- **評価用透かしが表示されたドキュメント**

![Aspose.PDFの評価](evaluate-aspose-pdf_1.png)

評価版の制限なしでAspose.PDF for Javaをテストしたい場合は、30日間の一時ライセンスをリクエストすることもできます。[一時ライセンスを取得するには？](https://purchase.aspose.com/temporary-license) を参照してください。

## Aspose RepositoryからAspose.PDF for Javaをインストールする

AsposeはすべてのJava APIを[Aspose Repository](https://releases.aspose.com/java/repo/com/aspose/aspose-pdf/)にホストしています。 Aspose.PDF for Java APIをMavenプロジェクトで簡単に使用することができます。設定は簡単です。

### Asposeリポジトリの設定を指定する

まず、Mavenのpom.xmlでAsposeリポジトリの設定/場所を次のように指定する必要があります：

```xml
 <repositories>
    <repository>
        <id>AsposeJavaAPI</id>
        <name>Aspose Java API</name>
        <url>https://releases.aspose.com/java/repo/</url>
    </repository>
</repositories>
```

### Aspose.PDF for Java APIの依存関係を定義する

次に、pom.xmlでAspose.PDF for Java APIの依存関係を次のように定義します：

```xml
 <dependencies>
    <dependency>
        <groupId>com.aspose</groupId>
        <artifactId>aspose-pdf</artifactId>
        <version>21.7</version>
    </dependency>
</dependencies>
```

上記の手順を実行すると、MavenプロジェクトにAspose.PDF for Javaの依存関係が最終的に定義されます。

### JDK 11の互換性と使用ガイドライン

このAPIはJava 11環境に最適化されており、すべてのテストと機能が正常に動作します。 しかし、いくつかのクラスでは、クラスのクラスパスに外部依存関係を追加する必要があります: javax.xml.bind.annotation.adapters.HexBinaryAdapter は、JRE から削除されました。

例えば:

```xml
<dependency>
    <groupId>javax.xml.bind</groupId>
    <artifactId>jaxb-api</artifactId>
    <version>2.3.0</version>
</dependency>
```