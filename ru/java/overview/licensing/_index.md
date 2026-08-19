---
title: Лицензия Aspose PDF
linktitle: Лицензирование и ограничения
type: docs
weight: 50
url: /ru/java/licensing/
description: Aspose.PDF for Python приглашает своих клиентов приобрести лицензию Classic. Также можно использовать ограниченную лицензию, чтобы лучше изучить продукт.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Лицензирование Aspose.PDF for Java
Abstract: В статье рассматриваются ограничения и варианты лицензирования Aspose.PDF for Python. Подчеркивается, что версия оценки позволяет полностью протестировать функциональность, но добавляет водяной знак к сгенерированным PDF‑файлам, отображая надпись “Evaluation Only” вместе с информацией об авторском праве. Для пользователей, желающих выполнять тестирование без этих ограничений, доступна 30‑дневная временная лицензия. В статье также объясняется, как реализовать классическую лицензию, загрузив её из файла или потока, рекомендуется помещать файл лицензии в тот же каталог, что и файл Aspose.PDF.dll, и устанавливать лицензию с помощью класса `Aspose.Pdf.License`. Приведены фрагменты кода, иллюстрирующие процесс лицензирования.
---
## Ограничения версии оценки

Мы хотим, чтобы наши клиенты тщательно тестировали наши компоненты перед покупкой, поэтому оценочная версия позволяет использовать её так, как вы обычно делаете.

- **PDF создан с помощью водяного знака оценки.** Оценочная версия Aspose.PDF for Java предоставляет полный функционал продукта, но все страницы в сгенерированных PDF‑документах помечены водяным знаком \"Evaluation Only. Created with Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd\" в верхней части.

- **Ограничение количества элементов коллекции, которые могут быть обработаны.**
В оценочной версии любой коллекции вы можете обработать только четыре элемента (например, только 4 страницы, 4 поля формы и т.д.).

Вы можете скачать оценочную версию **Aspose.PDF** для Java с [Aspose Repository](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf). Оценочная версия предоставляет абсолютно такие же возможности, как и лицензированная версия продукта. Более того, оценочная версия просто становится лицензированной, когда вы покупаете лицензию и добавляете пару строк кода для применения лицензии.

Как только вы будете довольны оценкой **Aspose.PDF**, вы можете [приобрести лицензию](https://purchase.aspose.com/) на веб-сайте Aspose. Ознакомьтесь с различными предлагаемыми типами подписки. Если у вас есть какие-либо вопросы, не стесняйтесь обращаться к команде по продажам Aspose.

Каждая лицензия Aspose включает годовую подписку на бесплатные обновления до любых новых версий или исправлений, выпущенных в течение этого периода. Техническая поддержка бесплатна и не ограничена, и предоставляется как лицензированным, так и пользователям оценочной версии.

>Если вы хотите протестировать Aspose.PDF for Java без ограничений оценочной версии, вы можете также запросить 30‑дневную временную лицензию. Пожалуйста, обратитесь к [Как получить временную лицензию?](https://purchase.aspose.com/temporary-license)

## Классическая лицензия

Лицензию можно загрузить из файла или объекта потока. Самый простой способ установить лицензию — поместить файл лицензии в ту же папку, что и файл Aspose.PDF.dll, и указать имя файла без пути, как показано в примере ниже.

Лицензия представляет собой обычный текстовый файл XML, содержащий такие детали, как название продукта, количество разработчиков, которым она выдана, дата истечения подписки и т.п. Файл подписан цифровой подписью, поэтому не следует изменять файл; даже случайное добавление лишнего разрыва строки сделает его недействительным.

Вам необходимо установить лицензию перед выполнением любых операций с документами. Требуется установить лицензию только один раз за приложение или процесс.

Лицензию можно загрузить из потока или файла в следующих местах:

1. Явный путь.
1. Папка, содержащая aspose-pdf-xx.x.jar.

Используйте метод License.setLicense для лицензирования компонента. Часто самый простой способ установить лицензию — разместить файл лицензии в той же папке, что и Aspose.PDF.jar, и указать только имя файла без пути, как показано в следующем примере:

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

### Загрузка лицензии из объекта потока

Следующий пример показывает, как загрузить лицензию из потока.

```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Set license from Stream
license.setLicense(new java.io.FileInputStream("Aspose.Pdf.Java.lic"));
```

### Проверьте лицензию

Можно проверить, правильно ли установлена лицензия или нет. Класс Document имеет метод isLicensed, который вернёт true, если лицензия установлена правильно.

```java
License license = new License();
license.setLicense("Aspose.Pdf.Java.lic");
// Check if license has been validated
if (com.aspose.pdf.Document.isLicensed()) {
    System.out.println("License is Set!");
}
```

## Лицензия с измерением

Aspose.PDF позволяет разработчикам применять ключ с измерением. Это новый механизм лицензирования. Новый механизм лицензирования будет использоваться вместе с существующим методом лицензирования. Клиенты, которые хотят платить за использование функций API, могут использовать лицензирование с измерением.В Для получения более подробной информации, пожалуйста, обратитесь кВ [FAQ по лицензированию с измерением](https://purchase.aspose.com/faqs/licensing/metered)В разделе.

Новый классВ [Измеряемый](https://reference.aspose.com/pdf/java/com.aspose.pdf/Metered)В было введено для применения метрированного ключа. Ниже приведён пример кода, демонстрирующего, как задать публичный и приватный метрированный ключ.

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

## Использование нескольких продуктов Aspose

Если вы используете несколько продуктов Aspose в вашем приложении, например Aspose.PDF и Aspose.Words, вот несколько полезных советов.

- **Установите лицензию для каждого продукта Aspose отдельно.** Even if you have a single license file for all components, for example ‘Aspose.Total.lic’, you still need to call **License.SetLicense** separately for each Aspose product you are using in your application.
- **Используйте полностью квалифицированное имя класса лицензии.** Each Aspose product has a **License** class in its namespace. For example, Aspose.PDF has **com.aspose.pdf.License** and Aspose.Words has **com.aspose.words.License** class. Using the fully qualified class name allows you to avoid any confusion about which license is applied to which product.

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

