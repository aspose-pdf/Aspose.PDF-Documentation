---
title: 在 PHP 中下载并配置 Aspose.PDF
linktitle: 在 PHP 中下载并配置 Aspose.PDF
type: docs
weight: 10
url: /zh/java/download-and-configure-aspose-pdf-in-php/
description: 了解如何在 PHP 中下载并配置 Aspose.PDF，以便在您的 PHP 项目中轻松集成和操作 PDF。
lastmod: "2026-10-06"
---
## 下载必需的库

下载下面提到的必需库。这些是执行 Aspose.PDF Java for PHP 示例所必需的。

- **Aspose:** [Aspose.PDF for Java 组件](https://downloads.aspose.com/pdf/java)
- PHP/Java 桥接

## 从社交编码站点下载示例

以下运行示例的发布版本可在以下提到的社交代码站点下载：

### GitHub

- **Aspose.PDF Java for PHP 示例**
  - [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)

## 在 Linux 平台上配置源代码

请按照以下简单步骤В 以打开并扩展源代码。

## 1. 安装 Tomcat 服务器

要安装 Tomcat 服务器，请在 Linux 控制台上执行以下命令.В 这将成功安装 Tomcat 服务器。

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}

## 2. 下载并配置 PHP/JavaBridge

要下载 PHP/JavaBridge 二进制文件，请在 Linux 控制台上执行以下命令。

{{< highlight actionscript3 >}}

  wget http://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

通过在 Linux 控制台上执行以下命令来解压 PHP/JavaBridge 二进制文件。

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

这将提取В **JavaBridge.war**В 文件。通过在 Linux 控制台上执行以下命令，将其复制到 tomcat88В **webapps**В 文件夹。

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war

{{< /highlight >}}

通过复制，tomcat8 将自动在 **webapps** 中创建一个新文件夹 "**JavaBridge**"。一旦文件夹创建完成，确保你的 tomcat8 正在运行，然后检查В  http://localhost:8080/JavaBridge В 在浏览器中，它应该打开 JavaBridge 的默认页面。

如果出现任何错误信息，请通过在 Linux 控制台上执行以下命令来安装В  **FastCGI**В 。

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi

{{< /highlight >}}

安装 php5.5 CGI 后，重启 tomcat8 服务器并检查\u0412  http://localhost:8080/JavaBridge В 再次在浏览器中。

如果出现\u0412\u00A0**JAVA_HOME**\u0412\u00A0 错误，则打开 /etc/default/tomcat8 文件并取消注释设置 JAVA_HOME 的行。检查\u0412 http://localhost:8080/JavaBridge В 在浏览器中再次打开，它应该带有 PHP/JavaBridge 示例页面。

## 3. 配置 Aspose.PDF Java for PHP 示例

克隆 PHP 示例，请在 webapps/JavaBridge 文件夹中执行以下命令。

{{< highlight actionscript3 >}}

$ git init

$ git clone [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]

{{< /highlight >}}

## 在 Windows 上配置源代码

请遵循以下简易步骤，在 Windows 平台上配置 PHP/Java Bridge

1. 安装 PHP5 并按常规方式进行配置
2. 如果您还没有 JRE 6（Java Runtime Environment），请安装它。您可以在 C:\Program Files 等位置检查是否已安装。您可以在此处下载。我使用 JRE 6，因为它兼容 PHP Java Bridge (PJB)。

3. 安装 Apache Tomcat 8.0。您可以在此处下载。

4. 下载 JavaBridge.war。
5. 将此文件复制到 tomcat webapps 目录。
(示例: C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps )

6. 重启 tomcat apache 服务。

7. 转到  http://localhost:8080/JavaBridge/test.php  检查 PHP 是否正常工作。您可以在那里找到其他示例。

8. 复制您的 [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) jar 文件至 C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib

9. 克隆 [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\ 文件夹中的示例。

10. 将文件夹 C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java 复制到您的 Aspose.PDF Java for PHP 示例文件夹。

11. 重启 Apache Tomcat 服务并开始使用示例。
