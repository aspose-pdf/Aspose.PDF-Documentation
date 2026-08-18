---
title: 在 PHP 中下载并配置 Aspose.PDF
linktitle: 在 PHP 中下载并配置 Aspose.PDF
type: docs
weight: 10
url: /java/download-and-configure-aspose-pdf-in-php/
description: 了解如何在 PHP 中下载和配置 Aspose.PDF，以便在 PHP 项目中轻松集成和 PDF 操作。
lastmod: "2026-06-09"
---
## 下载所需的库

下载下面提到的所需库。这些是执行 Aspose.PDF Java for PHP 示例所需的。

- **Aspose:** [Java 组件的 Aspose.PDF](https://downloads.aspose.com/pdf/java)
- PHP/Java 桥

## 从社交编码网站下载示例

以下版本的运行示例可以在下面提到的社交编码网站上下载：

### GitHub

- **Aspose.PDF Java for PHP 示例**
  - [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)

## 如何在Linux平台上配置源代码

请按照以下简单步骤操作，以便在使用时打开和扩展源代码：

## 1.安装Tomcat服务器

要安装 Tomcat 服务器，请在 Linux 控制台上发出以下命令。这将成功安装 Tomcat 服务器。

{{< highlight actionscript3 >}}

 sudo apt-get 安装 tomcat8

{{< /highlight >}}

## 2.下载并配置PHP/JavaBridge

要下载 PHP/JavaBridge 二进制文件，请在 Linux 控制台上发出以下命令。

{{< highlight actionscript3 >}}

  wget http://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

通过在 Linux 控制台上发出以下命令来解压缩 PHP/JavaBridge 二进制文件。

{{< highlight actionscript3 >}}

  解压-d php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

这将提取 **JavaBridge.war**В 文件。通过在 Linux 控制台上发出以下命令，将其复制到 tomcat88*webapps** 文件夹。

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war

{{< /highlight >}}

通过复制，tomcat8会自动在**webapps**中创建一个新文件夹“**JavaBridge**”。创建文件夹后，确保您的 tomcat8 正在运行，然后在浏览器中检查“http://localhost:8080/JavaBridge”，它应该打开 JavaBridge 的默认页面。

如果出现任何错误消息，则通过在 Linux 控制台上发出以下命令来安装 **FastCGI**。

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi

{{< /highlight >}}

安装php5.5 CGI后，重新启动tomcat8服务器，并在浏览器中再次检查。

如果显示“**JAVA_HOME**”错误，则打开 /etc/default/tomcat8 文件并取消注释设置 JAVA_HOME 的行。再次在浏览器中检查http://localhost:8080/JavaBridge В，应该会出现 PHP/JavaBridge Examples 页面。

## 3. 为 PHP 示例配置 Aspose.PDF Java

通过在 webapps/JavaBridge 文件夹中发出以下命令来克隆 PHP 示例。

{{< highlight actionscript3 >}}

$ git 初始化

$ git 克隆 [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]

{{< /highlight >}}

## 如何在 Windows 上配置源代码

请按照以下简单步骤在 Windows 平台上配置 PHP/Java Bridge

1. 像平常一样安装 PHP5 并配置
2. 如果您还没有 JRE 6（Java 运行时环境），请安装它。您可以在C:\Program 文件等中检查此内容。您可以在此处下载。我使用 JRE 6，因为它与 PHP Java Bridge (PJB) 兼容。

3. 安装 Apache Tomcat 8.0。您可以在这里下载

4. 下载 JavaBridge.war。
5. 将此文件复制到 tomcat webapps 目录。
（例如：C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps ）

6. 重新启动tomcat apache服务。

7. 去http://localhost:8080/JavaBridge/test.php检查php是否工作。您可以在那里找到其他示例

8. 将 [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) jar 文件复制到 C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib

9. 克隆 C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\ 文件夹中的 [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) 示例。

10. 将文件夹 C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java 复制到 Aspose.PDF Java for PHP 示例文件夹。

11. 重新启动apache tomcat服务并开始使用示例。
