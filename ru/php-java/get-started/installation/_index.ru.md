---
title: Установка Aspose.PDF для PHP через Java
linktitle: Установка
type: docs
weight: 20
url: /php-java/installation/
description: Этот раздел содержит описание продукта и инструкции по установке Aspose.PDF для PHP через Java самостоятельно, а также с использованием NuGet.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF для PHP через Java состоит из двух отдельных компонентов: оболочки скрипта (aspose.pdf.php) и Aspose.PDF для Java. Эти компоненты взаимодействуют через PHP/Java Bridge, и каждый требует своей собственной среды и процесса выполнения.

## Установка

1. Установите Tomcat в любое место, например, \java\apache-tomcat-9.0.24.
1. Скопируйте JavaBridge.war в папку webapps Tomcat, например, \java\apache-tomcat-9.0.24\webapps.
1. Скопируйте aspose-pdf-xx.x.jar в папку lib, например, \java\apache-tomcat-9.0.24\lib.
1. Запустите \bin\startup.bat, JavaBridge.war будет развернут в \java\apache-tomcat-9.0.24\webapps\JavaBridge.

1. Проверьте http://localhost:8080/JavaBridge/test.php, чтобы убедиться, что PHP работает нормально.
1. Скопируйте aspose.pdf.php и example.php в \java\apache-tomcat-9.0.24\webapps\JavaBridge.
1. Откройте http://localhost:8080/JavaBridge/example.php или создайте свой собственный PHP файл следующим образом.
Вы найдете библиотеку Jar и PHP в папке vendor/aspose/pdf.