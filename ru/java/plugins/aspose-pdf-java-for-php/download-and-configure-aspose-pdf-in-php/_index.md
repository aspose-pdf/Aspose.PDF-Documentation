---
title: Загрузите и настройте Aspose.PDF на PHP
linktitle: Загрузите и настройте Aspose.PDF на PHP
type: docs
weight: 10
url: /java/download-and-configure-aspose-pdf-in-php/
description: Узнайте, как загрузить и настроить Aspose.PDF на PHP для простой интеграции и манипулирования PDF-файлами в ваших проектах PHP.
lastmod: "2026-06-09"
---
## Загрузите необходимые библиотеки

Загрузите необходимые библиотеки, указанные ниже. Они необходимы для выполнения примеров Aspose.PDF Java для PHP.

- **Aspose:** [Aspose.PDF для Java-компонента](https://downloads.aspose.com/pdf/java)
- PHP/Java-мост

## Загрузите примеры с сайтов социального кодирования

Следующие выпуски примеров выполнения доступны для загрузки на указанных ниже сайтах социального кодирования:

### GitHub

- **Aspose.PDF Java для примеров PHP**
  - [Aspose.PDF Java для PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)

## Как настроить исходный код на платформе Linux

Выполните следующие простые шаги, чтобы открыть и расширить исходный код при использовании:

## 1. Установите сервер Tomcat.

Чтобы установить сервер Tomcat, введите следующую команду в консоли Linux. Это позволит успешно установить сервер Tomcat.

{{< highlight actionscript3 >}}

 sudo apt-get установить tomcat8

{{< /highlight >}}

## 2. Загрузите и настройте PHP/JavaBridge.

Чтобы загрузить двоичные файлы PHP/JavaBridge, введите следующую команду на консоли Linux.

{{< highlight actionscript3 >}}

  wget http://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

Разархивируйте двоичные файлы PHP/JavaBridge, введя следующую команду на консоли Linux.

{{< highlight actionscript3 >}}

  разархивировать -d php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

Это приведет к извлечению файла **JavaBridge.war**. Скопируйте его в папку tomcat88 **webapps** , выполнив следующую команду на консоли Linux.

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war

{{< /highlight >}}

При копировании tomcat8 автоматически создаст новую папку «**JavaBridge**» в **веб-приложениях**. После создания папки убедитесь, что ваш tomcat8 запущен, а затем установите флажок  http://localhost:8080/JavaBridge в браузере. Должна открыться страница JavaBridge по умолчанию.

Если появится какое-либо сообщение об ошибке, установите  **FastCGI** , введя следующую команду на консоли Linux.

{{< highlight actionscript3 >}}

  sudo apt-get установить php55-cgi

{{< /highlight >}}

После установки php5.5 CGI перезапустите сервер tomcat8 и снова проверьте http://localhost:8080/JavaBridge в браузере.

Если отображается ошибка **JAVA_HOME** , откройте файл /etc/default/tomcat8 и раскомментируйте строку, которая устанавливает JAVA_HOME. Проверьте http://localhost:8080/JavaBridge Снова в браузере: должна появиться страница примеров PHP/JavaBridge.

## 3. Настройте Aspose.PDF Java для примеров PHP

Клонируйте примеры PHP, введя следующие команды в папке webapps/JavaBridge.

{{< highlight actionscript3 >}}

$ git init&nbsp;

$ git clone [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]

{{< /highlight >}}

## How to configure the source code on Windows

Please follow below simple steps to configure PHP/Java Bridge on Windows Platform

1. Установите PHP5 и настройте, как обычно.
2. Установите JRE 6 (среда выполнения Java), если она у вас еще не установлена. Вы можете проверить это в C:\Program Files и т. д. Вы можете скачать его здесь. Я использую JRE 6, поскольку он совместим с PHP Java Bridge (PJB).

3. Установите Apache Tomcat 8.0. Вы можете скачать его здесь

4. Загрузите JavaBridge.war.
5. Скопируйте этот файл в каталог веб-приложений Tomcat.
(ex: C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps )

6. Перезапустите службу Tomcat Apache.

7. Перейдите на http://localhost:8080/JavaBridge/test.php, чтобы проверить, работает ли PHP. Там вы можете найти другие примеры

8. Скопируйте JAR-файл [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) в C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib

9. Клонируйте примеры [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) в папке C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\.

10. Скопируйте папку C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java в папку примеров Aspose.PDF Java для PHP.

11. Перезапустите службу Apache Tomcat и начните использовать примеры.
