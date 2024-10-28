---
title: 下载和配置 Aspose.PDF 在 PHP 中
type: docs
weight: 10
url: /java/download-and-configure-aspose-pdf-in-php/
lastmod: "2021-06-05"
---

## 下载所需的库

下载下面提到的所需库。这些是执行 Aspose.PDF Java for PHP 示例所需的。

- **Aspose:** [Aspose.PDF for Java 组件](https://downloads.aspose.com/pdf/java)
- PHP/Java 桥

## 从社交编码网站下载示例

以下版本的运行示例可在下述社交编码网站上下载：

### GitHub

- **Aspose.PDF Java for PHP 示例**
  - [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)

## 如何在 Linux 平台上配置源代码

请按照以下简单步骤以使用并扩展源代码：

## 1. 安装 Tomcat 服务器

要安装 Tomcat 服务器，请在 Linux 控制台上发出以下命令。这将成功安装 Tomcat 服务器。

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}

## 2. 下载并配置 PHP/JavaBridge

为了下载 PHP/JavaBridge 二进制文件，请在 Linux 控制台上发出以下命令。

{{< highlight actionscript3 >}}

  wget http://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

通过在 Linux 控制台上发出以下命令解压 PHP/JavaBridge 二进制文件。

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

这将提取 **JavaBridge.war** 文件。通过在 Linux 控制台上发出以下命令，将其复制到 tomcat8 **webapps** 文件夹。

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war

{{< /highlight >}}

通过复制，tomcat8 将自动在 **webapps** 中创建一个新文件夹 "**JavaBridge**"。
 一旦创建文件夹，确保您的 tomcat8 正在运行，然后在浏览器中检查 http://localhost:8080/JavaBridge ，它应该打开 JavaBridge 的默认页面。

如果出现任何错误消息，请通过在 Linux 控制台上发出以下命令安装 **FastCGI**。

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi

{{< /highlight >}}

安装 php5.5 CGI 后，重启 tomcat8 服务器并在浏览器中再次检查 http://localhost:8080/JavaBridge。

如果显示 **JAVA_HOME** 错误，则打开 /etc/default/tomcat8 文件并取消注释设置 JAVA_HOME 的行。在浏览器中再次检查 http://localhost:8080/JavaBridge ，它应该显示 PHP/JavaBridge 示例页面。

## 3. 配置 Aspose.PDF Java for PHP 示例

通过在 webapps/JavaBridge 文件夹中发出以下命令来克隆 PHP 示例。

{{< highlight actionscript3 >}}

$ git init&nbsp;

$ git clone [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]
{{< /highlight >}}

## 如何在 Windows 上配置源代码

请按照以下简单步骤在 Windows 平台上配置 PHP/Java Bridge

1. 安装 PHP5 并按常规方式进行配置
2. 安装 JRE 6（Java 运行环境），如果您尚未安装。您可以在 C:\Program Files 等目录中检查。您可以在此处下载。我使用 JRE 6，因为它与 PHP Java Bridge (PJB) 兼容。

3. 安装 Apache Tomcat 8.0。您可以在此处下载

4. 下载 JavaBridge.war。
5. 将此文件复制到 tomcat webapps 目录。
（例如：C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps）

6. 重启 tomcat apache 服务。

7. 访问 http://localhost:8080/JavaBridge/test.php 检查 php 是否工作。您可以在此处找到其他示例

8. 将您的 [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) jar 文件复制到 C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib

9. 克隆 [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) 示例到 C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\ 文件夹中。

10. 复制文件夹 C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java 到你的 Aspose.PDF Java for PHP 示例文件夹中。

11. 重启 apache tomcat 服务并开始使用示例。