---
title: Работа с метаданными PDF файла
linktitle: Метаданные PDF файла
type: docs
weight: 140
url: ru/java/pdf-file-metadata/
description: Этот раздел объясняет, как получить информацию о PDF файле, как получить XMP метаданные из PDF файла, установить информацию о PDF файле.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Получение информации о PDF файле

Чтобы получить специфическую для файла информацию о PDF файле, сначала получите объект [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocumentInfo) с помощью класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) [getInfo()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getInfo--). Как только объект [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocumentInfo) получен, вы можете получить значения отдельных свойств.

Следующий фрагмент кода показывает, как установить информацию о PDF файле.

```java
public class ExampleMetadata {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Metadata/";

    public static void GetPDFFileInformation() {
        // Создать новый PDF документ
        Document pdfDocument = new Document(_dataDir + "sample.pdf");
        // Получить информацию о документе
        DocumentInfo docInfo = pdfDocument.getInfo();
        // Показать информацию о документе
        System.out.println("Автор: " + docInfo.getAuthor());
        System.out.println("Дата создания: " + docInfo.getCreationDate());
        System.out.println("Ключевые слова: " + docInfo.getKeywords());
        System.out.println("Дата изменения: " + docInfo.getModDate());
        System.out.println("Тема: " + docInfo.getSubject());
        System.out.println("Заголовок: " + docInfo.getTitle());
    }
```


## Установка информации о файле PDF

Aspose.PDF for Java позволяет устанавливать специфичную для файла информацию для PDF, такую как автор, дата создания, тема и заголовок.

Чтобы установить эту информацию:

1. Создайте объект [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocumentInfo).
1. Установите значения свойств.
1. Сохраните обновлённый документ, используя метод [save()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save-com.aspose.ms.System.IO.FileStream-) класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

{{% alert color="primary" %}}

Обратите внимание, что вы не можете установить значения для полей **Producer** и **Creator**, потому что Aspose.PDF for Java x.x.x будет отображаться против этих полей.

{{% /alert %}}

Следующий фрагмент кода показывает, как установить информацию о файле PDF.

```java
 public static void SetPDFFileInformation() {
        // Открыть документ
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // Указать информацию о документе
        DocumentInfo docInfo = new DocumentInfo(pdfDocument);

        docInfo.setAuthor("Aspose");
        docInfo.setCreationDate(new java.util.Date());
        docInfo.setKeywords("Aspose.Pdf, DOM, API");
        docInfo.setModDate(new java.util.Date());
        docInfo.setSubject("PDF Information");
        docInfo.setTitle("Setting PDF Document Information");

        // Сохранить выходной документ
        pdfDocument.save(_dataDir + "SetFileInfo_out.pdf");
    }
```


## Получение метаданных XMP из PDF-файла

Aspose.PDF для Java позволяет получить доступ к метаданным XMP PDF-файла.

Чтобы получить метаданные PDF-файла,

1. Создайте объект [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) и откройте входной PDF-файл.
1. Используйте свойство [getMetadata()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getMetadata--) для получения метаданных.

Следующий фрагмент кода показывает, как получить метаданные из PDF-файла.

```java
   public static void GetXMPMetadata() {

        // Открыть документ
        Document pdfDocument = new Document(_dataDir + "SetXMPMetadata.pdf");

        System.out.println("xmp:CreateDate: " + pdfDocument.getMetadata().get_Item("xmp:CreateDate"));
        System.out.println("xmp:Nickname: " + pdfDocument.getMetadata().get_Item("xmp:Nickname"));
        System.out.println("xmp:CustomProperty: " + pdfDocument.getMetadata().get_Item("xmp:CustomProperty"));

    }
```

## Установка метаданных XMP в PDF-файле

Aspose.PDF для Java позволяет устанавливать метаданные в PDF-файл.
 Чтобы установить метаданные:

1. Создайте объект [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Установите значения метаданных, используя свойство [getMetadata()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getMetadata--).
1. Сохраните обновленный документ, используя метод [save()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save-com.aspose.ms.System.IO.FileStream-) объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Следующий фрагмент кода показывает, как установить метаданные в PDF-файле.

```java
    public static void SetXMPMetadata() {

        // Открыть документ
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // Установить свойства
        pdfDocument.getMetadata().set_Item("xmp:CreateDate", new XmpValue(new java.util.Date()));
        pdfDocument.getMetadata().set_Item("xmp:Nickname", new XmpValue("Nickname"));
        pdfDocument.getMetadata().set_Item("xmp:CustomProperty", new XmpValue("Custom Value"));

        // Сохранить документ
        pdfDocument.save(_dataDir + "SetXMPMetadata.pdf");
    }
```

## Вставка метаданных с префиксом

Некоторым разработчикам необходимо создать новое пространство имен метаданных с префиксом. В следующем фрагменте кода показано, как вставить метаданные с префиксом.

```java
    public static void InsertMetadataWithPrefix() {
        // Открыть документ
        Document pdfDocument = new Document(_dataDir + "SetXMPMetadata.pdf");
        pdfDocument.getMetadata().registerNamespaceUri("adc", "http://tempuri.org/adc/1.0");
        pdfDocument.getMetadata().set_Item("adc:format", new XmpValue("application/pdf"));
        pdfDocument.getMetadata().set_Item("adc:title", new XmpValue("alternative title"));        
        // Сохранить документ
        pdfDocument.save(_dataDir + "SetPrefixMetadata_out.pdf");
    }
}
```