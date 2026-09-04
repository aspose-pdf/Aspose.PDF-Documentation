---
title: Скачать и настроить Aspose.PDF в PHP
linktitle: Скачать и настроить Aspose.PDF в PHP
type: docs
weight: 10
url: /java/download-and-configure-aspose-pdf-in-php/
description: Узнайте, как скачать и настроить Aspose.PDF в PHP для простой интеграции и работы с PDF‑файлами в ваших PHP‑проектах.
lastmod: "2026-06-09"
---
## Загрузите необходимых библиотек

Скачайте перечисленные ниже библиотеки. Они необходимы для выполнения примеров Aspose.PDF Java для PHP.

- **Aspose:** [Aspose.PDF for Java Component](https://downloads.aspose.com/pdf/java)
- PHP/Java Bridge

## Скачивание примеров с сайтов совместного программирования

Ниже представлены релизы работающих примеров, доступные для загрузки на указанных сайтах совместного программирования:

### GitHub

- **Aspose.PDF Java for PHP Examples**
  - [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)

## Как настроить исходный код на платформе Linux

Пожалуйста, выполните следующие простые шаги, чтобы открыть и расширить исходный код, используя:

## 1. Установка сервера Tomcat

Чтобы установить сервер Tomcat, выполните следующую команду в консоли Linux. Это успешно установит сервер Tomcat.

{{< highlight actionscript3 >}}
 sudo apt-get install tomcat8
{{< /highlight >}}

## 2. Скачивание и настройка PHP/JavaBridge

Чтобы скачать бинарные файлы PHP/JavaBridge, выполните следующую команду в консоли Linux.

{{< highlight actionscript3 >}}
 wget http://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip
{{< /highlight >}}

Распакуйте бинарные файлы PHP/JavaBridge, выполнив следующую команду в консоли Linux.

{{< highlight actionscript3 >}}
 unzip -d php-java-bridge_6.2.1_documentation.zip
{{< /highlight >}}

Будет извлечён файл **JavaBridge.war**. Скопируйте его в папку **webapps** Tomcat 8, выполнив следующую команду в консоли Linux.

{{< highlight actionscript3 >}}
 sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war
{{< /highlight >}}

После копирования Tomcat 8 автоматически создаст новую папку **JavaBridge** в **webapps**. Как только папка появится, убедитесь, что Tomcat 8 запущен, и проверьте в браузере http://localhost:8080/JavaBridge — должна открыться стартовая страница JavaBridge.

Если появилось сообщение об ошибке, установите **FastCGI**, выполнив следующую команду в консоли Linux.

{{< highlight actionscript3 >}}
 sudo apt-get install php55-cgi
{{< /highlight >}}

После установки php5.5 CGI перезапустите сервер Tomcat 8 и снова проверьте http://localhost:8080/JavaBridge в браузере.

Если отображается ошибка **JAVA_HOME**, откройте файл /etc/default/tomcat8 и раскомментируйте строку, задающую переменную JAVA_HOME. Снова проверьте http://localhost:8080/JavaBridge в браузере — должна открыться страница с примерами PHP/JavaBridge.

## 3. Настройка примеров Aspose.PDF Java для PHP

Клонируйте PHP‑примеры, выполнив следующие команды внутри папки webapps/JavaBridge.

{{< highlight actionscript3 >}}
$ git init 
$ git clone https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP
{{< /highlight >}}

## Как настроить исходный код на Windows

Пожалуйста, выполните ниже перечисленные простые шаги для настройки PHP/Java Bridge на платформе Windows.

1. Установите PHP 5 и настройте его как обычно.
2. Установите JRE 6 (Java Runtime Environment), если он у вас ещё не установлен. Проверьте наличие в C:\Program Files и т.д. Скачать можно здесь. Я использую JRE 6, так как она совместима с PHP Java Bridge (PJB).
3. Установите Apache Tomcat 8.0. Скачать можно здесь.
4. Скачайте файл **JavaBridge.war**.
5. Скопируйте этот файл в каталог **webapps** Tomcat (например, C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps).
6. Перезапустите службу Tomcat.
7. Перейдите по адресу http://localhost:8080/JavaBridge/test.php, чтобы проверить работу PHP. Другие примеры находятся там же.
8. Скопируйте ваш JAR‑файл [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) в C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib.
9. Клонируйте примеры [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) в C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\.
10. Скопируйте папку C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java в ваш каталог с примерами Aspose.PDF Java for PHP.
11. Перезапустите службу Apache Tomcat и начинайте использовать примеры.


