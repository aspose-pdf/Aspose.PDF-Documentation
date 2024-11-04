---
title: Aspose.PDF Java for PHP
type: docs
weight: 50
url: /java/aspose-pdf-java-for-php/
lastmod: "2021-06-05"
---

## Aspose.PDF Java for PHP 简介

### PHP / Java 桥

PHP/Java 桥是一个基于流的 XML [网络协议](http://php-java-bridge.sourceforge.net/pjb/PROTOCOL.TXT)实现，它可以用于将本地脚本引擎（例如 PHP、Scheme 或 Python）与 Java 虚拟机连接起来。它比通过 SOAP 的本地 RPC 快 50 倍，占用的 web 服务器资源更少。它比通过 Java 本地接口的直接通信更快、更可靠，并且无需额外的组件即可从 PHP 调用 Java 程序或从 Java 调用 PHP 程序。

在 [sourceforge.net](http://php-java-bridge.sourceforge.net/pjb/) 阅读更多信息

### Aspose.PDF for Java

Aspose.PDF for Java 是一个 PDF 文档创建组件，使您的 Java 应用程序可以在不使用 Adobe Acrobat 的情况下读取、写入和操作 PDF 文档。

Aspose.PDF for Java 是一个价格实惠的组件，提供了丰富的功能，包括：PDF 压缩选项、表格创建和操作、图形支持、图像功能、广泛的超链接功能、扩展的安全控制和自定义字体处理。

Aspose.PDF for Java 允许您通过提供的 API 和 XML 模板直接创建 PDF 文件。使用 Aspose.PDF for Java 还可以让您在短时间内为您的应用程序添加 PDF 功能。

### Aspose.PDF Java for PHP

项目 Aspose.PDF for PHP 展示了如何使用 Aspose.PDF Java API 在 PHP 中执行不同的任务。该项目旨在为希望在其 PHP 项目中使用 [PHP/Java Bridge](http://php-java-bridge.sourceforge.net/pjb/) 利用 Aspose.PDF for Java 的 PHP 开发人员提供有用的示例。

## 系统要求和支持的平台

### 系统要求

以下是通过 Java 使用 Aspose.PDF for PHP 的系统要求：

- 安装 Tomcat Server 8.0 或更高版本。
- 配置 PHP/JavaBridge。
- 安装 FastCGI。
- 下载 Aspose.PDF 组件。

### 支持的平台

以下是支持的平台：

- PHP 5.3 或更高版本
- Java 1.8 或更高版本

## 下载和配置

### 下载所需的库

下载下文中提到的所需库。这些是执行 Aspose.PDF Java for PHP 示例所需的。

- **Aspose:** [Aspose.PDF for Java 组件](https://downloads.aspose.com/pdf/java)
- PHP/Java Bridge

### 从社交编码网站下载示例

以下版本的运行示例可以在下面提到的社交编码网站上下载：

### GitHub

- Aspose.PDF Java for PHP 示例
  - [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)

### 如何在 Linux 平台上配置源代码

请按照以下简单步骤操作，以便在使用时打开和扩展源代码：

### 1. 安装 Tomcat Server

要安装 tomcat server，请在 linux 控制台上输入以下命令。这将成功安装 tomcat server。

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}

### 2. 下载并配置 PHP/JavaBridge

为了下载 PHP/JavaBridge 二进制文件，在 Linux 控制台上执行以下命令。

{{< highlight actionscript3 >}}

  wget http://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

通过在 Linux 控制台上执行以下命令解压 PHP/JavaBridge 二进制文件。

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

这将提取 **JavaBridge.war** 文件。通过在 Linux 控制台上执行以下命令将其复制到 tomcat8 的 **webapps** 文件夹中。

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war

{{< /highlight >}}

复制后，tomcat8 将自动在 **webapps** 中创建一个新文件夹 "**JavaBridge**"。

如果出现任何错误信息，请通过在 Linux 控制台上执行以下命令安装 **FastCGI**。

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi

{{< /highlight >}}

如果出现**JAVA_HOME**错误，请打开/etc/default/tomcat8文件，并取消设置JAVA_HOME的行的注释。

### 3. 配置 Aspose.PDF Java for PHP 示例

在webapps/JavaBridge文件夹中通过发出以下命令克隆PHP示例。

{{< highlight actionscript3 >}}

$ git init&nbsp;

$ git clone [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]

{{< /highlight >}}

### 如何在Windows平台上配置源代码

请按照以下简单步骤在Windows平台上配置PHP/Java Bridge

1. 安装PHP5并按常规方式进行配置
2. 安装JRE 6（Java运行环境），如果您还没有，可以在C:\Program Files等处检查。您可以在这里下载。我使用JRE 6，因为它与PHP Java Bridge (PJB)兼容。

3. 安装Apache Tomcat 8.0。您可以在这里下载。

4. 下载 [JavaBridge.war](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/JavaBridgeTemplate621.war/download)。将此文件复制到 tomcat 的 webapps 目录中。  
（例如：C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps）

5. 重启 tomcat apache 服务。

6. 访问 http://localhost:8080/JavaBridge/test.php 检查 php 是否正常工作。您可以在那里找到其他示例。

7. 将您的 [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) jar 文件复制到 C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib。

8. 克隆 [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) 示例到 C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\ 文件夹中。

9. 将文件夹 C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java 复制到您的 Aspose.PDF Java for PHP 示例文件夹。

10. 重启 apache tomcat 服务并开始使用示例。


## 支持、扩展和贡献

### 支持

从Aspose成立的第一天起，我们就知道仅仅为客户提供优质的产品是不够的。我们还需要提供良好的服务。我们自己也是开发人员，深知当技术问题或软件中的小毛病阻碍你完成工作时的沮丧。我们在这里是为了解决问题，而不是制造问题。

这就是为什么我们提供免费支持的原因。任何使用我们产品的人，无论是购买的还是试用的，都值得我们全心全意的关注和尊重。

您可以使用以下任何平台记录与 Aspose.Cells Java for PHP 相关的问题或建议：

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)

### 扩展和贡献

Aspose.PDF Java for PHP 是开源的，其源代码可以在以下列出的主要社交编程网站上找到。
 开发人员被鼓励下载源代码，并通过建议或添加新功能或改进现有功能来做出贡献，以便其他人也能从中受益。

### 源代码

您可以从以下位置之一获取最新的源代码

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)