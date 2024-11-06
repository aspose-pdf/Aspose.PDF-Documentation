---
title: Aspose.PDF for PHP via Java をインストールする
linktitle: インストール
type: docs
weight: 20
url: ja/php-java/installation/
description: このセクションでは、Aspose.PDF for PHP via Java の製品説明と、NuGet を使用した場合と独自にインストールする手順を示します。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for PHP via Java は、スクリプトラッパー (aspose.pdf.php) と Aspose.PDF for Java の2つの別々のコンポーネントで構成されています。これらのコンポーネントは PHP/Java Bridge を介してやり取りし、それぞれが独自の環境と実行プロセスを必要とします。

## インストール

1. Tomcat を任意の場所にインストールします。例: \java\apache-tomcat-9.0.24。
1. JavaBridge.war を Tomcat の webapps フォルダーにコピーします。例: \java\apache-tomcat-9.0.24\webapps。
1. aspose-pdf-xx.x.jar を lib フォルダーにコピーします。例: \java\apache-tomcat-9.0.24\lib。
1. \bin\startup.bat を実行すると、JavaBridge.war は \java\apache-tomcat-9.0.24\webapps\JavaBridge にデプロイされます。

1. PHPが正常に動作することを確認するために、http://localhost:8080/JavaBridge/test.php をテストします。  
1. aspose.pdf.php と example.php を \java\apache-tomcat-9.0.24\webapps\JavaBridge にコピーします。  
1. http://localhost:8080/JavaBridge/example.php を開くか、以下のように独自のPHPファイルを作成します。  
JarとPHPライブラリはvendor/aspose/pdfフォルダにあります。