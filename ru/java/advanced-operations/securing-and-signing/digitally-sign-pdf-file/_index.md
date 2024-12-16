---
title: How to digitally sign PDF
linktitle: Digitally sign PDF
type: docs
weight: 10
url: /ru/java/digitally-sign-pdf-file/
description: Подпишите PDF документы с использованием Java. Проверьте или подтвердите цифровую подпись PDF с помощью Java-приложения с библиотекой PDF. Вы можете сертифицировать PDF файл с помощью PKCS1-сертификата.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

При подписании PDF документа с использованием подписи вы, по сути, подтверждаете, что его содержимое должно оставаться "как есть". Следовательно, любые изменения, сделанные после этого, аннулируют подпись, и таким образом, вы узнаете, если документ был изменен. Предварительная сертификация документа позволяет вам указать изменения, которые пользователь может внести в документ, не аннулируя сертификацию.

Другими словами, документ все еще будет считаться сохраняющим свою целостность, и получатель все еще сможет доверять документу. Для получения дополнительной информации, пожалуйста, посетите страницу Сертификация и подписание PDF.

Для выполнения вышеуказанного требования были внесены следующие изменения в общедоступный API.

isCertified(…) метод добавлен в класс PdfFileSignature.

## Подпись PDF с помощью цифровых подписей

```java
public class ExampleDigitallySign {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Secure-Sign/";

    public static void SignDocument() {
        String inFile = _dataDir + "DigitallySign.pdf";
        String outFile = _dataDir + "DigitallySign_out.pdf";
        Document document = new Document(inFile);

        PdfFileSignature signature = new PdfFileSignature(document);

        PKCS7 pkcs = new PKCS7("/home/aspose/pdf-examples/Samples/test.pfx", "Pa$$w0rd2020"); // Используйте объекты PKCS7/PKCS7Detached
                                                                                             
        signature.sign(1, true, new java.awt.Rectangle(300, 100, 400, 200), pkcs);
        // Сохранить выходной PDF файл
        signature.save(outFile);
    }
```

## Добавление временной метки к цифровой подписи

Aspose.PDF для Java поддерживает цифровую подпись PDF с использованием сервера временных меток или веб-сервиса.

В целях выполнения этого требования в пространство имен Aspose.PDF был добавлен класс [TimestampSettings](https://reference.aspose.com/pdf/java/com.aspose.pdf/TimestampSettings). Пожалуйста, обратите внимание на следующий фрагмент кода, который получает метку времени и добавляет ее в PDF-документ:

```java
    public static void SignWithTimeStampServer() {
        Document document = new Document(_dataDir + "SimpleResume.pdf");
        PdfFileSignature signature = new PdfFileSignature(document);

        PKCS7 pkcs = new PKCS7("/home/aspose/pdf-examples/Samples/test.pfx", "Start2020");
        TimestampSettings timestampSettings = new TimestampSettings("https://freetsa.org/tsr", ""); // Пользователь/Пароль могут быть
                                                                                                    // опущены
        pkcs.setTimestampSettings(timestampSettings);
        java.awt.Rectangle rect = new java.awt.Rectangle(100, 100, 200, 100);
        // Создать любой из трех типов подписи
        signature.sign(1, "Причина подписи", "Контакт", "Местоположение", true, rect, pkcs);
        // Сохранить выходной PDF-файл
        signature.save(_dataDir + "DigitallySignWithTimeStamp_out.pdf");
    }
```