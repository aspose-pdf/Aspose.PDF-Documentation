---
title: PHP で Aspose.PDF をダウンロードして設定する
linktitle: PHP で Aspose.PDF をダウンロードして設定する
type: docs
weight: 10
url: /ja/java/download-and-configure-aspose-pdf-in-php/
description: PHP プロジェクト内で簡単に統合し PDF を操作できるように、PHP で Aspose.PDF をダウンロードして設定する方法を学びます。
lastmod: "2026-10-05"
---
## 必要なライブラリをダウンロード

以下に示す必要なライブラリをダウンロードしてください。これらは PHP 用 Aspose.PDF Java のサンプルを実行するために必要です。

- **Aspose:** [Aspose.PDF for Java コンポーネント](https://downloads.aspose.com/pdf/java)
- PHP/Java ブリッジ

## ソーシャルコーディングサイトからサンプルをダウンロード

以下に示す実行例のリリースは、下記のソーシャルコーディングサイトからダウンロードできます:

### GitHub

- **Aspose.PDF Java for PHP の例**
  - [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)

## Linux プラットフォームでソースコードを設定する方法

以下の簡単な手順に従ってください\u0412\u00A0使用しながらソースコードを開き、拡張するために:

## 1. Tomcat サーバーのインストール

Tomcatサーバーをインストールするには、Linuxコンソールで次のコマンドを実行してください。\u0412\u00A0これによりTomcatサーバーが正常にインストールされます。

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}

## 2. PHP/JavaBridge をダウンロードして構成する

PHP/JavaBridge のバイナリをダウンロードするには、Linux コンソールで次のコマンドを実行します。

{{< highlight actionscript3 >}}

  wget http://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

PHP/JavaBridge のバイナリを解凍するには、Linux コンソールで次のコマンドを実行します。

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

これは **JavaBridge.war** В ファイルを抽出します。Linux コンソールで次のコマンドを実行して、tomcat88 **webapps** フォルダーにコピーしてください。

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war

{{< /highlight >}}

コピーすると、tomcat8 は自動的に **webapps** に新しいフォルダー "**JavaBridge**" を作成します。フォルダーが作成されたら、tomcat8 が実行中であることを確認し、次にチェックしてくださいВ  http://localhost:8080/JavaBridge В ブラウザで、JavaBridge のデフォルトページが開くはずです。

エラー メッセージが表示された場合は、Linux コンソールで次のコマンドを実行して В **FastCGI** をインストールしてください。

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi

{{< /highlight >}}

php5.5 CGI をインストールした後、tomcat8 サーバーを再起動して確認してくださいВ  http://localhost:8080/JavaBridge В ブラウザーで再び。

IfВ **JAVA_HOME**В エラーが表示された場合は、/etc/default/tomcat8 ファイルを開き、JAVA_HOME を設定している行のコメントを解除してください。CheckВ http://localhost:8080/JavaBridge ブラウザで再びВを開くと、PHP/JavaBridge Examples ページが表示されるはずです。

## 3. Aspose.PDF Java for PHP のサンプルの設定

webapps/JavaBridge フォルダー内で次のコマンドを実行して、PHP のサンプルをクローンします。

{{< highlight actionscript3 >}}

$ git init&nbsp;

$ git clone [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]

{{< /highlight >}}

## Windows でソースコードを構成する方法

Windows プラットフォームで PHP/Java Bridge を設定するために、以下の簡単な手順に従ってください。

1. PHP5 をインストールし、通常通りに設定してください。
2. JRE 6（Java Runtime Environment）を、まだインストールしていない場合はインストールしてください。C:\Program Files などで確認できます。ここからダウンロードできます。PHP Java Bridge（PJB）と互換性があるため、私は JRE 6 を使用しています。

3. Apache Tomcat 8.0 をインストールしてください。ここからダウンロードできます。

4. JavaBridge.war をダウンロードしてください。
5. このファイルを tomcat の webapps ディレクトリにコピーしてください。
(例: C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps )

6. tomcat apache サービスを再起動します。

7. 移動  http://localhost:8080/JavaBridge/test.php  PHPが動作するかを確認するためです。そこに他の例があります。

8. コピーしてください [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib に jar ファイル

9. クローン [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\ フォルダー内のサンプル。

10. フォルダー C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java を、あなたの Aspose.PDF Java for PHP サンプルフォルダーにコピーしてください。

11. Apache Tomcat サービスを再起動し、サンプルの使用を開始してください。
