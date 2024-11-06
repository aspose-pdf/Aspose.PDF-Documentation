---
title: Aspose.PDF Java for PHP
type: docs
weight: 50
url: ja/java/aspose-pdf-java-for-php/
lastmod: "2021-06-05"
---

## Aspose.PDF Java for PHPの紹介

### PHP / Java ブリッジ

PHP/Java ブリッジは、ストリーミング、XMLベースの[ネットワークプロトコル](http://php-java-bridge.sourceforge.net/pjb/PROTOCOL.TXT)の実装であり、PHP、Scheme、PythonなどのネイティブスクリプトエンジンをJava仮想マシンと接続するために使用できます。これはSOAPを介したローカルRPCよりも最大50倍高速で、ウェブサーバー側でのリソース消費が少なくて済みます。Java Native Interfaceを介した直接通信よりも[高速](http://php-java-bridge.sourceforge.net/pjb/FAQ.html#performance)で信頼性が高く、PHPからJava、またはJavaからPHPの手順を呼び出すために追加のコンポーネントを必要としません。

詳細は[sourceforge.net](http://php-java-bridge.sourceforge.net/pjb/)をご覧ください。

### Java用Aspose.PDF

Java用Aspose.PDFは、JavaアプリケーションがAdobe Acrobatを使用せずにPDFドキュメントの読み取り、書き込み、操作を可能にするPDFドキュメント作成コンポーネントです。

Aspose.PDF for Javaは、非常に豊富な機能を提供する手頃な価格のコンポーネントです。これには、PDF圧縮オプション、テーブルの作成と操作、グラフのサポート、画像機能、広範なハイパーリンク機能、拡張されたセキュリティコントロール、カスタムフォントの処理が含まれます。

Aspose.PDF for Javaを使用すると、提供されたAPIとXMLテンプレートを通じて直接PDFファイルを作成できます。Aspose.PDF for Javaを使用することで、短時間でアプリケーションにPDF機能を追加することもできます。

### Aspose.PDF Java for PHP

プロジェクトAspose.PDF for PHPは、PHPでAspose.PDF Java APIを使用してさまざまなタスクを実行する方法を示します。このプロジェクトは、[PHP/Java Bridge](http://php-java-bridge.sourceforge.net/pjb/)を使用してPHPプロジェクトでAspose.PDF for Javaを利用したいPHP開発者に有用な例を提供することを目的としています。

## システム要件とサポートプラットフォーム

### システム要件

以下は、Java経由でAspose.PDF for PHPを使用するためのシステム要件です。

- Tomcatサーバー8.0以上がインストールされている。
- PHP/JavaBridgeが構成されている。
- FastCGIがインストールされている。
- Aspose.PDFコンポーネントをダウンロード済み。

### サポートされているプラットフォーム

以下はサポートされているプラットフォームです：

- PHP 5.3以上
- Java 1.8以上

## ダウンロードと構成

### 必要なライブラリのダウンロード

以下に記載されている必要なライブラリをダウンロードしてください。これらはAspose.PDF Java for PHPの例を実行するために必要です。

- **Aspose:** [Aspose.PDF for Java Component](https://downloads.aspose.com/pdf/java)
- PHP/Java Bridge

### ソーシャルコーディングサイトから例をダウンロード

以下に記載されたソーシャルコーディングサイトで、実行可能な例をダウンロードできます：

### GitHub

- Aspose.PDF Java for PHPの例
  - [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)

### Linuxプラットフォームでソースコードを構成する方法

以下の簡単なステップに従って、使用中にソースコードを開いて拡張してください：

### 1. Tomcatサーバーをインストール

Tomcatサーバーをインストールするには、Linuxコンソールで以下のコマンドを発行してください。これにより、Tomcatサーバーが正常にインストールされます。

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}

### 2. PHP/JavaBridgeのダウンロードと設定

PHP/JavaBridgeのバイナリをダウンロードするには、Linuxコンソールで以下のコマンドを発行します。

{{< highlight actionscript3 >}}

  wget http://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

Linuxコンソールで以下のコマンドを発行してPHP/JavaBridgeのバイナリを解凍します。

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

これにより、**JavaBridge.war**ファイルが抽出されます。Linuxコンソールで以下のコマンドを発行して、これをtomcat8の**webapps**フォルダにコピーします。

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war

{{< /highlight >}}

コピーすることにより、tomcat8は自動的に**webapps**に新しいフォルダ"**JavaBridge**"を作成します。

エラーメッセージが表示された場合は、Linuxコンソールで以下のコマンドを発行して**FastCGI**をインストールします。

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi

{{< /highlight >}}

もし **JAVA_HOME** エラーが表示された場合は、/etc/default/tomcat8 ファイルを開き、JAVA_HOME を設定する行のコメントを解除します。

### 3. Aspose.PDF Java for PHP Examples の設定

webapps/JavaBridge フォルダ内で次のコマンドを発行して、PHP の例をクローンします。

{{< highlight actionscript3 >}}

$ git init&nbsp;

$ git clone [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]

{{< /highlight >}}

### Windows プラットフォームでソースコードを設定する方法

Windows プラットフォームで PHP/Java Bridge を設定するために、以下の簡単な手順に従ってください。

1. PHP5 をインストールし、通常どおり設定します
2. JRE 6 (Java Runtime Environment) をインストールします。まだお持ちでない場合は、C:\Program Files などで確認できます。こちらからダウンロードできます。PHP Java Bridge (PJB) と互換性があるため、JRE 6 を使用しています。

3. Apache Tomcat 8.0 をインストールします。こちらからダウンロードできます。

4. [JavaBridge.war](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/JavaBridgeTemplate621.war/download) をダウンロードします。このファイルを tomcat の webapps ディレクトリにコピーします。
（例：C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps）

5. tomcat apache サービスを再起動します。

6. http://localhost:8080/JavaBridge/test.php にアクセスして、PHP が動作するか確認します。そこに他の例も見つけることができます。

7. [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) の jar ファイルを C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib にコピーします。

8. [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) の例を C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\ フォルダ内にクローンします。

9. フォルダ C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java を Aspose.PDF Java for PHP 例のフォルダにコピーします。

10. apache tomcat サービスを再起動し、例の使用を開始します。


## サポート、拡張、および貢献

### サポート

Asposeの最初の日から、私たちはお客様に良い製品を提供するだけでは不十分であることを知っていました。私たちは良いサービスも提供する必要がありました。私たち自身も開発者であり、技術的な問題やソフトウェアの癖が原因でやりたいことができなくなることがどれほどイライラするか理解しています。私たちは問題を解決するためにここにいるのであって、問題を作り出すためではありません。

これが、私たちが無料サポートを提供している理由です。当社の製品を使用する人は、購入しているか評価版を使用しているかにかかわらず、私たちの完全な注意と尊重に値します。

Aspose.Cells Java for PHPに関連する問題や提案は、以下のプラットフォームを使用してログできます：

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)

### 拡張と貢献

Aspose.PDF Java for PHPはオープンソースであり、そのソースコードは以下にリストされている主要なソーシャルコーディングサイトで入手可能です。
 開発者はソースコードをダウンロードし、新機能の提案や追加、既存機能の改善を行うことで貢献することが奨励されています。他の人々もそれを利用できるようにするためです。

### ソースコード

最新のソースコードは、以下のいずれかの場所から入手できます

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)