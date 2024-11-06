---
title: Установка Aspose.PDF для Java
linktitle: Установка
type: docs
weight: 20
url: ru/java/installation/
description: Этот раздел показывает описание продукта и инструкции по установке Aspose.PDF для Java самостоятельно, а также с использованием NuGet.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Компонент Aspose.PDF для Java

{{% alert color="primary" %}}

**Aspose.PDF это Java** компонент, созданный, чтобы позволить разработчикам создавать PDF документы, будь то простые или сложные, программно на лету. Aspose.PDF для Java позволяет разработчикам вставлять таблицы, графики, изображения, гиперссылки, собственные шрифты - и многое другое - в PDF документы. Более того, также возможно сжимать PDF документы. Aspose.PDF для Java предоставляет отличные функции безопасности для разработки защищенных PDF документов. И самой отличительной особенностью Aspose.PDF для Java является поддержка создания PDF документов как через API, так и из XML шаблонов.

{{% /alert %}}

## Описание продукта

**Aspose.PDF for Java** реализован с использованием Java и работает с JDK 1.8 и выше. Aspose.PDF for Java может быть интегрирован в любое приложение, например, веб-приложение JSP/JSF или приложение для Windows.

**Aspose.PDF for Java** быстрый и легковесный. Он эффективно создает PDF-документы и помогает вашему приложению работать лучше. Aspose.PDF for Java является первым выбором наших клиентов при создании PDF-документов благодаря своей цене, превосходной производительности и отличной поддержке. Используя эту библиотеку, вы можете реализовать богатые возможности для создания PDF-файлов с нуля или полностью обрабатывать существующие PDF-документы без установки Adobe Acrobat.

# Установка

## Оценка Aspose.PDF for Java

{{% alert color="primary" %}}

Вы можете скачать [Aspose.PDF for Java](https://releases.aspose.com/java/repo/com/aspose/aspose-pdf/) для оценки.
 Скачивание для оценки такое же, как и скачивание после покупки. Версия для оценки становится лицензированной, когда вы добавляете несколько строк кода, чтобы [применить лицензию](/pdf/java/licensing/).

{{% /alert %}}

Версия для оценки Aspose.PDF предоставляет полную функциональность продукта, но имеет два ограничения:

- Вставляет водяной знак для оценки.
- Не более четырех элементов любой коллекции могут быть просмотрены/отредактированы.
- **Документ, показывающий водяной знак для оценки**

![Оценка Aspose.PDF](evaluate-aspose-pdf_1.png)

{{% alert color="primary" %}}

Если вы хотите протестировать Aspose.PDF для Java без ограничений версии для оценки, вы также можете запросить 30-дневную временную лицензию. Пожалуйста, обратитесь к [Как получить временную лицензию?](https://purchase.aspose.com/temporary-license)

{{% /alert %}}

## Установка Aspose.PDF для Java из репозитория Aspose

Aspose размещает все Java API в [репозитории Aspose](https://releases.aspose.com/java/repo/com/aspose/aspose-pdf/). Вы можете легко использовать Aspose.PDF для Java API непосредственно в ваших Maven проектах с простыми настройками.

### Укажите конфигурацию репозитория Aspose

Сначала вам нужно указать конфигурацию / расположение репозитория Aspose в вашем Maven pom.xml следующим образом:

```xml
 <repositories>
    <repository>
        <id>AsposeJavaAPI</id>
        <name>Aspose Java API</name>
        <url>https://releases.aspose.com/java/repo/</url>
    </repository>
</repositories>
```

### Определите зависимость Aspose.PDF для Java API

Затем определите зависимость Aspose.PDF для Java API в вашем pom.xml следующим образом:

```xml
 <dependencies>
    <dependency>
        <groupId>com.aspose</groupId>
        <artifactId>aspose-pdf</artifactId>
        <version>21.7</version>
    </dependency>
</dependencies>
```

После выполнения вышеуказанных шагов, зависимость Aspose.PDF для Java будет окончательно определена в вашем Maven проекте.

### Совместимость с JDK 11 и руководство по использованию

API оптимизировано для среды Java 11, и все тесты и функциональность работают корректно. Однако для некоторых классов следует добавить внешнюю зависимость, чтобы добавить classpath класса: javax.xml.bind.annotation.adapters.HexBinaryAdapter, который был удален из JRE.

Например:

```xml
<dependency>
    <groupId>javax.xml.bind</groupId>
    <artifactId>jaxb-api</artifactId>
    <version>2.3.0</version>
</dependency>
```