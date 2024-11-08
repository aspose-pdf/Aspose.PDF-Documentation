---
title: PHPでAspose.PDFをダウンロードして設定する
type: docs
weight: 10
url: /ja/java/download-and-configure-aspose-pdf-in-php/
lastmod: "2021-06-05"
---

## 必要なライブラリをダウンロード

以下に記載されている必要なライブラリをダウンロードします。これらは、Aspose.PDF Java for PHPの例を実行するために必要です。

- **Aspose:** [Aspose.PDF for Java コンポーネント](https://downloads.aspose.com/pdf/java)
- PHP/Java Bridge

## ソーシャルコーディングサイトからの例のダウンロード

以下に記載されているソーシャルコーディングサイトでダウンロード可能な実行例のリリースがあります：

### GitHub

- **Aspose.PDF Java for PHP 例**
  - [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)

## Linuxプラットフォームでソースコードを設定する方法

以下の簡単な手順に従って、使用中のソースコードを開いて拡張してください：

## 1. Tomcatサーバーのインストール

Tomcatサーバーをインストールするには、Linuxコンソールで以下のコマンドを発行します。これにより、Tomcatサーバーが正常にインストールされます。

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}

## 2. PHP/JavaBridgeをダウンロードして設定する

PHP/JavaBridgeのバイナリをダウンロードするために、Linuxコンソールで以下のコマンドを発行します。

{{< highlight actionscript3 >}}

  wget http://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}


Linuxコンソールで以下のコマンドを発行して、PHP/JavaBridgeのバイナリを解凍します。

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}


これにより、**JavaBridge.war**ファイルが抽出されます。Linuxコンソールで以下のコマンドを発行して、これをtomcat8の**webapps**フォルダにコピーします。

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war

{{< /highlight >}}


コピーすることにより、tomcat8は**webapps**に新しいフォルダ"**JavaBridge**"を自動的に作成します。
 フォルダーが作成されたら、tomcat8が実行中であることを確認し、ブラウザで http://localhost:8080/JavaBridge をチェックしてください。JavaBridge のデフォルトページが開くはずです。

エラーメッセージが表示された場合は、Linuxコンソールで以下のコマンドを発行して **FastCGI** をインストールしてください。

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi

{{< /highlight >}}

php5.5 CGIをインストールした後、tomcat8サーバーを再起動し、ブラウザで http://localhost:8080/JavaBridge を再度チェックしてください。

**JAVA_HOME** エラーが表示された場合は、/etc/default/tomcat8 ファイルを開き、JAVA_HOME を設定する行のコメントを外します。ブラウザで http://localhost:8080/JavaBridge を再度チェックしてください。PHP/JavaBridge の例のページが表示されるはずです。

## 3. Aspose.PDF Java for PHP の例を設定する

webapps/JavaBridge フォルダー内で以下のコマンドを発行して、PHP の例をクローンします。

{{< highlight actionscript3 >}}

$ git init&nbsp;

$ git clone [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]
{{< /highlight >}}

## Windowsでソースコードを設定する方法

WindowsプラットフォームでPHP/Java Bridgeを設定するために、以下の簡単な手順に従ってください。

1. PHP5を通常通りにインストールして設定します。
2. JRE 6 (Java Runtime Environment) をインストールします。既にインストールされていない場合は、C:\Program Filesなどで確認できます。ここからダウンロードできます。PHP Java Bridge (PJB) と互換性があるため、JRE 6を使用しています。

3. Apache Tomcat 8.0をインストールします。ここからダウンロードできます。

4. JavaBridge.warをダウンロードします。
5. このファイルをtomcatのwebappsディレクトリにコピーします。
（例：C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps）

6. tomcat apacheサービスを再起動します。

7. http://localhost:8080/JavaBridge/test.php にアクセスして、PHPが動作するか確認します。その他の例もそこで見つけることができます。

8. [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) のjarファイルを C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib にコピーします。

9. C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\ フォルダ内に [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) の例をクローンします。

10. フォルダ C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java を Aspose.PDF Java for PHP の例のフォルダにコピーします。

11. Apache Tomcat サービスを再起動し、例を使用し始めます。