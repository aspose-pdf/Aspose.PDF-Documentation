---
title: 安装通过 Java 的 Aspose.PDF for PHP
linktitle: 安装
type: docs
weight: 20
url: zh/php-java/installation/
description: 本节展示了产品描述及通过 Java 安装 Aspose.PDF for PHP 的说明，以及使用 NuGet 的说明。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

通过 Java 的 Aspose.PDF for PHP 由两个独立的组件组成：脚本包装器 (aspose.pdf.php) 和 Aspose.PDF for Java。这些组件通过 PHP/Java Bridge 进行交互，每个组件都需要自己的环境和执行过程。

## 安装

1. 在任意位置安装 Tomcat，例如 \java\apache-tomcat-9.0.24。
1. 将 JavaBridge.war 复制到 Tomcat 的 webapps 文件夹，例如 \java\apache-tomcat-9.0.24\webapps。
1. 将 aspose-pdf-xx.x.jar 复制到 lib 文件夹，例如 \java\apache-tomcat-9.0.24\lib。
1. 运行 \bin\startup.bat，JavaBridge.war 将被部署到 \java\apache-tomcat-9.0.24\webapps\JavaBridge。

1. 测试 http://localhost:8080/JavaBridge/test.php 以确保 PHP 正常工作。
1. 复制 aspose.pdf.php 和 example.php 到 \java\apache-tomcat-9.0.24\webapps\JavaBridge。
1. 打开 http://localhost:8080/JavaBridge/example.php 或按如下方式创建您自己的 PHP 文件。
您将在 vendor/aspose/pdf 文件夹中找到 Jar 和 PHP 库。