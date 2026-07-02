---
title: Лицензирование и ограничения
linktitle: Лицензирование и ограничения
type: docs
weight: 50
url: /ru/androidjava/licensing/
description: Aspose.PDF for Android via Java приглашает своих клиентов получить Classic license и Metered License. Также можно использовать ограниченную лицензию, чтобы лучше изучить продукт.
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ограничения оценочной версии

Мы хотим, чтобы наши клиенты тщательно протестировали наши компоненты перед покупкой, поэтому оценочная версия позволяет использовать её так, как вы обычно делаете.

- **PDF создан с водяным знаком оценки.** Оценочная версия Aspose.PDF for Android via Java предоставляет весь функционал продукта, но все страницы в создаваемых PDF‑документах помечены водяным знаком "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd" в верхней части.

- **Предел количества элементов коллекции, которые можно обработать.**
В оценочной версии из любой коллекции можно обработать только четыре элемента (например, только 4 страницы, 4 поля формы и т.д.).

Вы можете скачать оценочную версию Aspose.PDF for Android via Java с [Репозиторий Aspose](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf). Оценочная версия предоставляет абсолютно те же возможности, что и лицензированная версия продукта. Кроме того, оценочная версия просто становится лицензированной, когда вы покупаете лицензию и добавляете несколько строк кода для применения лицензии.

Когда вы будете довольны оценкой **Aspose.PDF**, вы можете [приобрести лицензию](https://purchase.aspose.com/) на сайте Aspose. Ознакомьтесь с различными типами предлагаемых подписок. Если у вас есть вопросы, не стесняйтесь обращаться в отдел продаж Aspose.

Каждая лицензия Aspose включает однолетнюю подписку на бесплатные обновления до любых новых версий или исправлений, выпускаемых в течение этого периода. Техническая поддержка предоставляется бесплатно и без ограничений как лицензированным, так и пользователям оценочных версий.

>Если вы хотите протестировать Aspose.PDF for Android через Java без ограничений версии оценки, вы также можете запросить 30‑дневную временную лицензию. Пожалуйста, см. [Как получить временную лицензию?](https://purchase.aspose.com/temporary-license)

## Классическая лицензия

Лицензию можно загрузить из файла или объекта потока. Самый простой способ установить лицензию — разместить файл лицензии в той же папке, что и файл Aspose.PDF.dll, и указать имя файла без пути, как показано в примере ниже.

Лицензия представляет собой обычный текстовый XML‑файл, содержащий такие сведения, как название продукта, количество разработчиков, на которое она выдана, срок действия подписки и т.д. Файл подписан цифровой подписью, поэтому его не следует изменять; даже случайное добавление лишнего переноса строки в файл сделает его недействительным.

Вам необходимо установить лицензию перед выполнением любых операций с документами. Требуется установить лицензию только один раз за приложение или процесс.

Лицензия может быть загружена из потока или файла в следующих местах:

1. Явный путь.
1. Папка, содержащая aspose-pdf-xx.x.jar.

Используйте метод License.setLicense для лицензирования компонента. Часто самый простой способ установить лицензию — поместить файл лицензии в ту же папку, что и Aspose.PDF.jar, и указать только имя файла без пути, как показано в следующем примере:

{{% alert color="primary" %}}

Начиная с Aspose.PDF for Java 4.2.0, вам необходимо вызвать следующие строки кода для инициализации лицензии.

{{% /alert %}}

### Загрузка лицензии из файла

В этом примере **Aspose.PDF** попытается найти файл лицензии в папке, содержащей JAR‑файлы вашего приложения.

```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Call setLicense method to set license
license.setLicense("Aspose.Pdf.Java.lic");
```

### Загрузка лицензии из объектного потока

В следующем примере показано, как загрузить лицензию из потока.

```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Set license from Stream
license.setLicense(new java.io.FileInputStream("Aspose.Pdf.Java.lic"));
```

#### Установка лицензии, приобретённой до 2005/01/22

**Aspose.PDF** for Java больше не поддерживает старые лицензии, поэтому, пожалуйста, свяжитесь с нашей [командой продаж](https://company.aspose.com/contact) чтобы получить новый файл лицензии.

### Проверить лицензию

Можно проверить, правильно ли лицензия установлена или нет. Класс Document имеет метод isLicensed, который вернёт true, если лицензия была правильно установлена.

```java
License license = new License();
license.setLicense("Aspose.Pdf.Java.lic");
// Check if license has been validated
if (com.aspose.pdf.Document.isLicensed()) {
    System.out.println("License is Set!");
}
```
## Лицензия с учётом использования

Aspose.PDF позволяет разработчикам применять metered key. Это новый механизм лицензирования. Новый механизм лицензирования будет использоваться вместе с существующим методом лицензирования. Клиенты, которые хотят платить за использование функций API, могут использовать лицензирование по измерению. Для получения более подробной информации, пожалуйста, обратитесь к [FAQ по лицензированию с измерением](https://purchase.aspose.com/faqs/licensing/metered) раздел.

```java
String publicKey = "";
String privateKey = "";

Metered m = new Metered();
m.setMeteredKey(publicKey, privateKey);

// Optionally, the following two lines returns true if a valid license has been applied;
// false if the component is running in evaluation mode.
License lic = new License();
System.out.println("License is set = " + lic.isLicensed());
```
## Использование нескольких продуктов от Aspose

Если вы используете несколько продуктов Aspose в своем приложении, например Aspose.PDF и Aspose.Words, ниже приведены несколько полезных советов.

- **Установите лицензию для каждого продукта Aspose отдельно.** Даже если у вас есть единый файл лицензии для всех компонентов, например 'Aspose.Total.lic', вам всё равно необходимо вызвать **License.SetLicense** отдельно для каждого продукта Aspose, который вы используете в своём приложении.
- **Используйте полностью квалифицированное имя класса лицензии.** Каждый продукт Aspose имеет класс **License** в своём пространстве имён. Например, у Aspose.PDF класс **com.aspose.pdf.License**, а у Aspose.Words — класс **com.aspose.words.License**. Использование полностью квалифицированного имени класса помогает избежать путаницы, какой лицензией покрывается какой продукт.

```java
// Instantiate the License class of Aspose.Pdf
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Set the license
license.setLicense("Aspose.Total.Java.lic");

// Setting license for Aspose.Words for Java

// Instantiate the License class of Aspose.Words
com.aspose.words.License licenseaw = new com.aspose.words.License();
// Set the license
licenseaw.setLicense("Aspose.Total.Java.lic");
```
