---
title: Aspose.PDF Java для PHP
type: docs
weight: 50
url: ru/java/aspose-pdf-java-for-php/
lastmod: "2021-06-05"
---

## Введение в Aspose.PDF Java для PHP

### PHP / Java Bridge

PHP/Java Bridge — это реализация потокового, XML-основанного [сетевого протокола](http://php-java-bridge.sourceforge.net/pjb/PROTOCOL.TXT), который может использоваться для соединения встроенного скриптового движка, например PHP, Scheme или Python, с виртуальной машиной Java. Он работает до 50 раз быстрее, чем локальный RPC через SOAP, требует меньше ресурсов на стороне веб-сервера. Он [быстрее](http://php-java-bridge.sourceforge.net/pjb/FAQ.html#performance) и надежнее, чем прямая связь через Java Native Interface, и не требует дополнительных компонентов для вызова Java-процедур из PHP или PHP-процедур из Java.

Подробнее читайте на [sourceforge.net](http://php-java-bridge.sourceforge.net/pjb/)

### Aspose.PDF для Java

Aspose.PDF для Java — это компонент для создания PDF-документов, который позволяет вашим Java-приложениям читать, записывать и обрабатывать PDF-документы без использования Adobe Acrobat.

Aspose.PDF for Java - это компонент по доступной цене, который предлагает невероятное количество функций, включая: опции сжатия PDF, создание и обработку таблиц, поддержку графиков, функции работы с изображениями, обширную функциональность гиперссылок, расширенные средства безопасности и работу с пользовательскими шрифтами.

Aspose.PDF for Java позволяет создавать PDF-файлы напрямую через предоставленный API и XML-шаблоны. Использование Aspose.PDF for Java также позволит вам быстро добавить возможности PDF в ваши приложения.

### Aspose.PDF Java для PHP

Проект Aspose.PDF для PHP показывает, как различные задачи могут выполняться с использованием Aspose.PDF Java API в PHP. Этот проект нацелен на предоставление полезных примеров для PHP-разработчиков, которые хотят использовать Aspose.PDF for Java в своих PHP-проектах, используя [PHP/Java Bridge](http://php-java-bridge.sourceforge.net/pjb/).

## Системные требования и поддерживаемые платформы

### Системные требования

Ниже приведены системные требования для использования Aspose.PDF для PHP через Java:

- Установлен Tomcat Server 8.0 или выше.
- PHP/JavaBridge настроен.
- FastCGI установлен.
- Загружен компонент Aspose.PDF.

### Поддерживаемые платформы

Ниже перечислены поддерживаемые платформы:

- PHP 5.3 или выше
- Java 1.8 или выше

## Загрузки и настройка

### Загрузка необходимых библиотек

Загрузите необходимые библиотеки, указанные ниже. Они необходимы для выполнения примеров Aspose.PDF Java для PHP.

- **Aspose:** [Aspose.PDF для компонента Java](https://downloads.aspose.com/pdf/java)
- PHP/Java Bridge

### Загрузка примеров с социальных кодирующих сайтов

Следующие выпуски работающих примеров доступны для загрузки на ниже указанных социальных кодирующих сайтах:

### GitHub

- Примеры Aspose.PDF Java для PHP
  - [Aspose.PDF Java для PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)

### Как настроить исходный код на платформе Linux

Пожалуйста, выполните следующие простые шаги, чтобы открыть и расширить исходный код при использовании:

### 1. Установите Tomcat Server

Чтобы установить сервер Tomcat, выполните следующую команду в консоли Linux. Это успешно установит сервер Tomcat.

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}

### 2. Скачать и настроить PHP/JavaBridge

Чтобы скачать бинарные файлы PHP/JavaBridge, выполните следующую команду в консоли Linux.

{{< highlight actionscript3 >}}

  wget http://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

Распакуйте бинарные файлы PHP/JavaBridge, выполнив следующую команду в консоли Linux.

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

Это извлечет файл **JavaBridge.war**. Скопируйте его в папку **webapps** tomcat88, выполнив следующую команду в консоли Linux.

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war

{{< /highlight >}}

При копировании tomcat8 автоматически создаст новую папку "**JavaBridge**" в **webapps**.

Если появляется сообщение об ошибке, установите **FastCGI**, выполнив следующую команду в консоли Linux.

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi

{{< /highlight >}}

Если отображается ошибка **JAVA_HOME**, откройте файл /etc/default/tomcat8 и раскомментируйте строку, которая устанавливает JAVA_HOME.

### 3. Настройка Aspose.PDF Java для PHP примеров

Клонируйте PHP-примеры, выполнив следующие команды в папке webapps/JavaBridge. 

{{< highlight actionscript3 >}}

$ git init&nbsp;

$ git clone [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]

{{< /highlight >}}

### Как настроить исходный код на платформе Windows

Пожалуйста, выполните следующие простые шаги для настройки PHP/Java Bridge на платформе Windows

1. Установите PHP5 и настройте как обычно
2. Установите JRE 6 (Java Runtime Environment), если у вас его еще нет. Вы можете проверить это в C:\Program Files и т.д. Вы можете скачать его здесь. Я использую JRE 6, так как он совместим с PHP Java Bridge (PJB).

3. Установите Apache Tomcat 8.0. Вы можете скачать его здесь

4. Загрузите [JavaBridge.war](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/JavaBridgeTemplate621.war/download). Скопируйте этот файл в директорию webapps tomcat.  
(например: C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps )

5. Перезапустите сервис apache tomcat.

6. Перейдите по адресу http://localhost:8080/JavaBridge/test.php, чтобы проверить, работает ли php. Вы можете найти другие примеры там.

7. Скопируйте ваш файл jar [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) в C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib

8. Клонируйте примеры [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) в папку C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\.

9. Скопируйте папку C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java в папку с примерами Aspose.PDF Java for PHP.

10. Перезапустите сервис apache tomcat и начните использовать примеры.


## Поддержка, расширение и вклад

### Поддержка

С самых первых дней Aspose мы знали, что просто предоставлять нашим клиентам хорошие продукты будет недостаточно. Нам также нужно было предоставить хороший сервис. Мы сами разработчики и понимаем, как это расстраивает, когда техническая проблема или особенность в программном обеспечении мешает вам делать то, что вам нужно. Мы здесь, чтобы решать проблемы, а не создавать их.

Именно поэтому мы предлагаем бесплатную поддержку. Любой, кто использует наш продукт, будь то купивший его или использующий для оценки, заслуживает нашего полного внимания и уважения.

Вы можете зарегистрировать любые проблемы или предложения, связанные с Aspose.Cells Java для PHP, используя любую из следующих платформ:

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)

### Расширение и вклад

Aspose.PDF Java для PHP является открытым исходным кодом, и его исходный код доступен на основных сайтах социального кодирования, перечисленных ниже.
 Разработчикам рекомендуется загружать исходный код и вносить свой вклад, предлагая или добавляя новые функции или улучшая существующие, чтобы другие также могли извлечь из этого пользу.

### Исходный код

Вы можете получить последний исходный код из одного из следующих мест:

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)