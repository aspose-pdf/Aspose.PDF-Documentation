---
title: Licensing and limitations
linktitle: Licensing and limitations
type: docs
weight: 50
url: /ru/androidjava/licensing/
description: Aspose.PDF for Android via Java приглашает своих клиентов приобрести Классическую лицензию и Лицензию с учетом использования. Также используйте ограниченную лицензию для более полного изучения продукта.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ограничения пробной версии

Мы хотим, чтобы наши клиенты тщательно тестировали наши компоненты перед покупкой, поэтому пробная версия позволяет использовать её, как обычно.

- **PDF создается с водяным знаком оценки.** Пробная версия Aspose.PDF for Android via Java предоставляет полную функциональность продукта, но все страницы в созданных PDF-документах помечены водяным знаком "Только для оценки. Создано с помощью Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd" вверху.

- **Ограничение на количество элементов коллекции, которые могут быть обработаны.**

В пробной версии из любой коллекции вы можете обработать только четыре элемента (например, только 4 страницы, 4 поля формы и т.д.).

You can download an evaluation version of Aspose.PDF for Android via Java from [Aspose Repository](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf). The evaluation version provides absolutely the same capabilities as the licensed version of the product. Furthermore, evaluation version simply becomes licensed when you purchase a license and add a couple of lines of code to apply the license.

Вы можете загрузить оценочную версию Aspose.PDF для Android через Java из [репозитория Aspose](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf). Оценочная версия предоставляет абсолютно те же возможности, что и лицензированная версия продукта. Более того, оценочная версия просто становится лицензированной, когда вы покупаете лицензию и добавляете несколько строк кода для применения лицензии.

Once you are happy with your evaluation of **Aspose.PDF**, you can [purchase a license](https://purchase.aspose.com/) at the Aspose website. Make yourself familiar with the different subscription types offered. If you have any questions, do not hesitate to contact the Aspose sales team.

Когда вы будете довольны своей оценкой **Aspose.PDF**, вы можете [приобрести лицензию](https://purchase.aspose.com/) на сайте Aspose. Ознакомьтесь с различными типами подписок, которые предлагаются. Если у вас есть какие-либо вопросы, не стесняйтесь обращаться в отдел продаж Aspose.

Every Aspose license carries a one-year subscription for free upgrades to any new versions or fixes that come out during this time. Technical support is free and unlimited and provided both to licensed and evaluation users.

Каждая лицензия Aspose включает годовую подписку на бесплатные обновления до любых новых версий или исправлений, которые выходят в течение этого времени. Техническая поддержка бесплатная и неограниченная, предоставляется как лицензированным, так и оценочным пользователям.

>If you want to test Aspose.PDF for Android via Java without the evaluation version limitations, you can also request a 30-day Temporary License.

>Если вы хотите протестировать Aspose.PDF для Android через Java без ограничений оценочной версии, вы также можете запросить 30-дневную временную лицензию.
 Пожалуйста, обратитесь к [Как получить временную лицензию?](https://purchase.aspose.com/temporary-license)

## Классическая лицензия

Лицензию можно загрузить из файла или объекта потока. Самый простой способ установить лицензию — поместить файл лицензии в ту же папку, что и файл Aspose.PDF.dll, и указать имя файла без пути, как показано в примере ниже.

Лицензия представляет собой текстовый XML-файл, который содержит такие детали, как название продукта, количество разработчиков, на которых она лицензирована, дата окончания подписки и так далее. Файл подписан цифровой подписью, поэтому не изменяйте файл; даже случайное добавление дополнительного разрыва строки в файл сделает его недействительным.

Необходимо установить лицензию перед выполнением любых операций с документами. Вам нужно установить лицензию только один раз для каждого приложения или процесса.

Лицензию можно загрузить из потока или файла в следующих местах:

1. Явный путь.
1. Папка, содержащая aspose-pdf-xx.x.jar.

Используйте метод License.setLicense для лицензирования компонента. Часто самый простой способ установить лицензию — поместить файл лицензии в ту же папку, что и Aspose.PDF.jar, и указать только имя файла без пути, как показано в следующем примере:

{{% alert color="primary" %}}

Начиная с Aspose.PDF for Java 4.2.0, вам нужно вызвать следующие строки кода для инициализации лицензии.

{{% /alert %}}

### Загрузка лицензии из файла

В этом примере **Aspose.PDF** попытается найти файл лицензии в папке, содержащей JAR-файлы вашего приложения.

```java
// Инициализация экземпляра лицензии
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Вызов метода setLicense для установки лицензии
license.setLicense("Aspose.Pdf.Java.lic");
```

### Загрузка лицензии из объекта потока

Следующий пример показывает, как загрузить лицензию из потока.

```java
// Инициализация экземпляра лицензии
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Установка лицензии из потока
license.setLicense(new java.io.FileInputStream("Aspose.Pdf.Java.lic"));
```

#### Установка лицензии, приобретенной до 2005/01/22
**Aspose.PDF** для Java больше не поддерживает старые лицензии, поэтому, пожалуйста, свяжитесь с нашей [командой продаж](https://company.aspose.com/contact), чтобы получить новый лицензионный файл.

### Проверка лицензии

Можно проверить, правильно ли установлена лицензия. Класс Document имеет метод isLicensed, который вернет true, если лицензия установлена правильно.

```java
License license = new License();
license.setLicense("Aspose.Pdf.Java.lic");
// Проверяем, была ли лицензия подтверждена
if (com.aspose.pdf.Document.isLicensed()) {
    System.out.println("Лицензия установлена!");
}
```
## Лицензия с оплатой за использование

Aspose.PDF позволяет разработчикам применять ключи с оплатой за использование. Это новый механизм лицензирования. Новый механизм лицензирования будет использоваться вместе с существующим методом лицензирования. Те клиенты, которые хотят получать счета на основе использования функций API, могут использовать лицензию с оплатой за использование. Для получения более подробной информации, пожалуйста, обратитесь к разделу [Часто задаваемые вопросы о лицензировании с оплатой за использование](https://purchase.aspose.com/faqs/licensing/metered).

```java
String publicKey = "";
String privateKey = "";

Metered m = new Metered();
m.setMeteredKey(publicKey, privateKey);

// При желании, следующие две строки возвращают true, если применена допустимая лицензия;
// false, если компонент работает в режиме оценки.
License lic = new License();
System.out.println("Лицензия установлена = " + lic.isLicensed());
```

## Использование нескольких продуктов от Aspose

Если вы используете несколько продуктов Aspose в вашем приложении, например Aspose.PDF и Aspose.Words, вот несколько полезных советов.

- **Устанавливайте лицензию для каждого продукта Aspose отдельно.** Даже если у вас есть один лицензионный файл для всех компонентов, например 'Aspose.Total.lic', вам все равно нужно вызывать **License.SetLicense** отдельно для каждого продукта Aspose, который вы используете в вашем приложении.
- **Используйте полное имя класса лицензии.** Каждый продукт Aspose имеет класс **License** в своем пространстве имен. Например, Aspose.PDF имеет класс **com.aspose.pdf.License**, а Aspose.Words имеет класс **com.aspose.words.License**. Использование полного имени класса позволяет избежать путаницы относительно того, какая лицензия применяется к какому продукту.

```java
// Создание экземпляра класса License для Aspose.Pdf
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Установка лицензии
license.setLicense("Aspose.Total.Java.lic");

// Установка лицензии для Aspose.Words для Java

// Создание экземпляра класса License для Aspose.Words
com.aspose.words.License licenseaw = new com.aspose.words.License();
// Установка лицензии
licenseaw.setLicense("Aspose.Total.Java.lic");
```