---
title: Загрузить и настроить Aspose.PDF в PHP
type: docs
weight: 10
url: /java/download-and-configure-aspose-pdf-in-php/
lastmod: "2021-06-05"
---

## Загрузить необходимые библиотеки

Скачайте указанные ниже необходимые библиотеки. Они необходимы для выполнения примеров Aspose.PDF Java для PHP.

- **Aspose:** [Aspose.PDF for Java Component](https://downloads.aspose.com/pdf/java)
- PHP/Java Bridge

## Скачать примеры с сайтов социального кодирования

Следующие релизы работающих примеров доступны для скачивания на указанных ниже сайтах социального кодирования:

### GitHub

- **Aspose.PDF Java для PHP Примеры**
  - [Aspose.PDF Java для PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)

## Как настроить исходный код на платформе Linux

Пожалуйста, выполните эти простые шаги, чтобы открыть и расширить исходный код, используя:

## 1. Установите сервер Tomcat

Чтобы установить сервер Tomcat, выполните следующую команду в консоли Linux. Это успешно установит сервер Tomcat.

## 2. Загрузить и настроить PHP/JavaBridge

Чтобы загрузить бинарные файлы PHP/JavaBridge, выполните следующую команду в консоли Linux.

{{< highlight actionscript3 >}}

  wget http://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

Распакуйте бинарные файлы PHP/JavaBridge, выполнив следующую команду в консоли Linux.

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

Это извлечет файл **JavaBridge.war**. Скопируйте его в папку **webapps** tomcat8, выполнив следующую команду в консоли Linux.

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war

{{< /highlight >}}

При копировании tomcat8 автоматически создаст новую папку "**JavaBridge**" в **webapps**.
 Как только папка создана, убедитесь, что ваш tomcat8 запущен, и затем проверьте http://localhost:8080/JavaBridge в браузере, должна открыться страница по умолчанию JavaBridge.

Если появляется сообщение об ошибке, установите **FastCGI** с помощью следующей команды в консоли Linux.

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi

{{< /highlight >}}

После установки php5.5 CGI, перезапустите сервер tomcat8 и снова проверьте http://localhost:8080/JavaBridge в браузере.

Если отображается ошибка **JAVA_HOME**, откройте файл /etc/default/tomcat8 и раскомментируйте строку, которая устанавливает JAVA_HOME. Снова проверьте http://localhost:8080/JavaBridge в браузере, должна появиться страница с примерами PHP/JavaBridge.

## 3. Настройка Aspose.PDF Java для PHP примеров

Клонируйте PHP примеры, выполнив следующие команды внутри папки webapps/JavaBridge.

{{< highlight actionscript3 >}}

$ git init&nbsp;

$ git clone [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]
{{< /highlight >}}

## Как настроить исходный код на Windows

Пожалуйста, выполните следующие простые шаги, чтобы настроить PHP/Java Bridge на платформе Windows

1. Установите PHP5 и настройте, как обычно
2. Установите JRE 6 (Java Runtime Environment), если у вас его еще нет. Вы можете проверить это в C:\Program Files и т.д. Вы можете скачать его здесь. Я использую JRE 6, так как он совместим с PHP Java Bridge (PJB).

3. Установите Apache Tomcat 8.0. Вы можете скачать его здесь

4. Скачайте JavaBridge.war.
5. Скопируйте этот файл в директорию webapps tomcat.
(например: C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps )

6. Перезапустите сервис tomcat apache.

7. Перейдите на http://localhost:8080/JavaBridge/test.php, чтобы проверить, работает ли php. Вы можете найти другие примеры там

8. Скопируйте ваш [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) jar файл в C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib

9. Клонируйте примеры [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) в папку C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\.

10. Скопируйте папку C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java в вашу папку с примерами Aspose.PDF Java for PHP.

11. Перезапустите службу Apache Tomcat и начните использовать примеры.