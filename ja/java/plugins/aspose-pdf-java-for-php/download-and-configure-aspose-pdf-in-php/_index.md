---
title: "PHP での Aspose.PDF をダウンロードして設定"
linktitle: "PHP での Aspose.PDF をダウンロードして設定"
type: docs
weight: 10
url: /ja/java/download-and-configure-aspose-pdf-in-php/
description: PHP プロジェクト内で簡単に統合し PDF を操作できるように、PHP で Aspose.PDF をダウンロードして設定する方法を学びます。
lastmod: "2026-10-06"
---
## 必要なライブラリのダウンロード

以下に示す必要なライブラリをダウンロードしてください。これらは PHP 用 Aspose.PDF Java のサンプルを実行するために必要です。

- **Aspose:** [Aspose.PDF for Java コンポーネント](https://downloads.aspose.com/pdf/java)
- PHP/Java ブリッジ

## ソーシャルコーディングサイトからサンプルのダウンロード

以下に示す実行例のリリースは、下記のソーシャルコーディングサイトからダウンロードできます：

### GitHub

- **Aspose.PDF Java for PHP の例**
  - [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)

## Linux プラットフォームでのソースコード設定方法

以下の簡単な手順に従って、ソースコードを開いて拡張してください。

## 1. Tomcat サーバーのインストール

Tomcat サーバーをインストールするには、Linux コンソールで次のコマンドを実行してください。これにより Tomcat サーバーが正常にインストールされます。

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}

## 2. PHP/JavaBridge のダウンロードと構成

PHP/JavaBridge のバイナリをダウンロードするには、Linux コンソールで次のコマンドを実行してください。

{{< highlight actionscript3 >}}

  wget http://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

PHP/JavaBridge のバイナリを解凍するには、Linux コンソールで次のコマンドを実行してください。

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

これは **JavaBridge.war** ファイルを抽出します。Linux コンソールで次のコマンドを実行し、tomcat88 **webapps** フォルダーにコピーしてください。

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war

{{< /highlight >}}

コピーすると、tomcat8 は自動的に **webapps** フォルダー内に新しいフォルダー「**JavaBridge**」を作成します。フォルダーが作成されたら、tomcat8 が実行中であることを確認し、ブラウザーで http://localhost:8080/JavaBridge を開いてください。JavaBridge のデフォルトページが表示されるはずです。

エラーメッセージが表示された場合は、Linux コンソールで次のコマンドを実行して **FastCGI** をインストールしてください。

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi

{{< /highlight >}}

php5.5 CGI をインストールした後、tomcat8 サーバーを再起動し、ブラウザーで http://localhost:8080/JavaBridge を再び開いてください。

**JAVA_HOME** エラーが表示された場合は、/etc/default/tomcat8 ファイルを開き、JAVA_HOME を設定している行のコメントを解除してください。その後、ブラウザーで http://localhost:8080/JavaBridge を再び開くと、PHP/JavaBridge Examples ページが表示されるはずです。

## 3. Aspose.PDF Java for PHP のサンプルの設定

webapps/JavaBridge フォルダー内で次のコマンドを実行して、PHP のサンプルをクローンしてください。

{{< highlight actionscript3 >}}

$ git init&nbsp;

$ git clone [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]

{{< /highlight >}}

## Windows でソースコードを構成する方法

Windows プラットフォームで PHP/Java Bridge を設定するには、以下の手順に従ってください。

1. PHP5 をインストールし、通常通りに設定してください。
2. JRE 6（Java Runtime Environment）を、まだインストールしていない場合はインストールしてください。インストールの有無は、`C:\Program Files` などで確認できます。ダウンロードは以下から行えます。PHP Java Bridge（PJB）と互換性があるため、JRE 6 を使用しています。

3. Apache Tomcat 8.0 をインストールしてください。ダウンロードは以下から行えます。

4. JavaBridge.war をダウンロードしてください。
5. このファイルを Tomcat の webapps ディレクトリにコピーしてください。
（例：`C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps`）

6. Tomcat Apache サービスを再起動してください。

7. http://localhost:8080/JavaBridge/test.php にアクセスし、PHP が動作するかを確認してください。このページにはその他の例も掲載されています。

8. [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) の jar ファイルを、`C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib` にコピーしてください。

9. [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) のサンプルを、`C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\` フォルダー内にクローンしてください。

10. `C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java` フォルダーを、Aspose.PDF Java for PHP のサンプルフォルダーにコピーしてください。

11. Apache Tomcat サービスを再起動し、サンプルの使用を開始してください。
