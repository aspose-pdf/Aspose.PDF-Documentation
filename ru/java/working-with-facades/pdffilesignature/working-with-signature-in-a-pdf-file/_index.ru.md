---
title: Работа с Подписью в PDF Файле
type: docs
weight: 40
url: /java/working-with-signature-in-a-pdf-file/
description: В этом разделе объясняется, как работать с Подписью в PDF файле, используя класс PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Как Извлечь Информацию о Подписи

Aspose.PDF для Java поддерживает возможность цифровой подписи PDF файлов с использованием класса PdfFileSignature. В настоящее время также возможно определить действительность сертификата, но мы не можем извлечь весь сертификат. Информация, которую можно извлечь, включает в себя открытый ключ, отпечаток и издателя и т.д.

Для извлечения информации о подписи мы ввели метод extractCertificate(..) в класс PdfFileSignature. Пожалуйста, посмотрите на следующий фрагмент кода, который демонстрирует шаги по извлечению сертификата из объекта PdfFileSignature:

```java
public static void ExtractSignatureInfo() {
        String input = _dataDir + "DigitallySign.pdf";
        String certificateFileName = "extracted_cert.pfx";
        PdfFileSignature pdfFileSignature = new PdfFileSignature();
        pdfFileSignature.bindPdf(input);
        List<String> sigNames = pdfFileSignature.getSignNames();

        if (sigNames.size() > 0) {
            String sigName = sigNames.get(0);
            if (sigName != "") {
                InputStream cerStream = pdfFileSignature.extractCertificate(sigName);
                if (cerStream != null) {
                    FileOutputStream fs;
                    try {
                        fs = new FileOutputStream(_dataDir + certificateFileName);
                        cerStream.transferTo(fs);
                    } catch (IOException e) {
                        e.printStackTrace();
                    }

                }
            }
        }
    }
```


## Извлечение изображения из поля подписи (PdfFileSignature)

Aspose.PDF для Java поддерживает возможность цифровой подписи PDF-файлов с использованием класса PdfFileSignature, и при подписании документа вы также можете установить изображение для SignatureAppearance. Теперь этот API также предоставляет возможность извлечения информации о подписи, а также изображения, связанного с полем подписи.

Для извлечения информации о подписи мы ввели метод [extractImage(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature#extractImage-java.lang.String-) в класс PdfFileSignature. Пожалуйста, ознакомьтесь с следующим фрагментом кода, который демонстрирует шаги по извлечению изображения из объекта PdfFileSignature:

```java
 public static void ExtractSignatureImage() {
        PdfFileSignature signature = new PdfFileSignature();
        signature.bindPdf(_dataDir + "DigitallySign.pdf");
        if (signature.containsSignature()) {
            for (String sigName : signature.getSignNames()) {
                String outFile = _dataDir + sigName + "_ExtractImages_out.jpg";
                InputStream imageStream = signature.extractImage(sigName);
                if (imageStream != null) {
                    FileOutputStream fs;
                    try {
                        fs = new FileOutputStream(outFile);
                        imageStream.transferTo(fs);
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
            }
        }
    }
```


## Подавление Местоположения и Причины

Функциональность Aspose.PDF позволяет гибко настраивать экземпляр цифровой подписи. Класс [PdfFileSignature ](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) предоставляет возможность подписывать PDF-файл. Реализация метода Sign позволяет подписывать PDF и передавать конкретный объект подписи этому классу. Метод Sign содержит набор атрибутов для настройки выходной цифровой подписи. В случае, если вам нужно подавить некоторые текстовые атрибуты из результирующей подписи, вы можете оставить их пустыми. Следующий фрагмент кода демонстрирует, как подавить две строки Местоположение и Причина из блока подписи:

```java
public static void SupressLocationReason() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample01.pdf");

        // Создание прямоугольника для расположения подписи
        java.awt.Rectangle rect = new java.awt.Rectangle(10, 10, 300, 50);

        // Установка внешнего вида подписи
        pdfSign.setSignatureAppearance(_dataDir + "aspose-logo.png");

        // Создание любого из трех типов подписей
        PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

        pdfSign.sign(1, "", "test01@aspose-pdf-demo.local", "", true, rect, signature);
        // Сохранение выходного PDF-файла
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```


## Функции настройки для цифровой подписи

Aspose.PDF для Java позволяет использовать функции настройки для цифровой подписи. Метод Sign класса SignatureCustomAppearance реализован с 6 перегрузками для вашего удобства. Например, вы можете настроить результат подписи только с помощью экземпляра класса SignatureCustomAppearance и значений его свойств. Следующий фрагмент кода демонстрирует, как скрыть надпись "Цифровая подпись от" в выходной цифровой подписи вашего PDF.

```java
    public static void CustomizationFeaturesForDigitalSign() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample01.pdf");

        // Создайте прямоугольник для расположения подписи
        java.awt.Rectangle rect = new java.awt.Rectangle(10, 10, 300, 50);

        // Создайте любой из трех типов подписей
        PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

        SignatureCustomAppearance signatureCustomAppearance = new SignatureCustomAppearance();
        signatureCustomAppearance.setFontSize(6);
        signatureCustomAppearance.setFontFamilyName("Times New Roman");
        signatureCustomAppearance.setDigitalSignedLabel("ПОДПИСАНО:");
        signature.setCustomAppearance(signatureCustomAppearance);

        pdfSign.sign(1, true, rect, signature);
        // Сохраните выходной файл PDF
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```


## Изменение языка в тексте цифровой подписи

С помощью Aspose.PDF для Java API вы можете подписать PDF-файл, используя любой из следующих трех типов подписей:

- PKCS#1
- PKCS#7
- PKCS#7

Каждая из предоставленных подписей содержит набор конфигурационных свойств, реализованных для вашего удобства (локализация, формат даты и времени, семейство шрифтов и т. д.). Класс SignatureCustomAppearance предоставляет соответствующую функциональность. Следующий фрагмент кода демонстрирует, как изменить язык в тексте цифровой подписи:

```java
     public static void ChangeLanguageInDigitalSignText() {
        String inFile = _dataDir + "sample01.pdf";
        String outFile = _dataDir + "DigitallySign.pdf";

        PdfFileSignature pdfSign = new PdfFileSignature();

        pdfSign.bindPdf(inFile);
        // создайте прямоугольник для расположения подписи
        java.awt.Rectangle rect = new java.awt.Rectangle(310, 45, 200, 50);

        // создайте любой из трех типов подписей
        PKCS7 pkcs = new PKCS7(_dataDir + "test01.pfx", "Aspose2021");
        pkcs.setReason("Pruebas Firma");
        pkcs.setContactInfo("Contacto Pruebas");
        pkcs.setLocation("Población (Provincia)");
        pkcs.setDate(new Date());
        SignatureCustomAppearance signatureCustomAppearance = new SignatureCustomAppearance();
        signatureCustomAppearance.setDateSignedAtLabel("Fecha");
        signatureCustomAppearance.setDigitalSignedLabel("Digitalmente firmado por");
        signatureCustomAppearance.setReasonLabel("Razón");
        signatureCustomAppearance.setLocationLabel("Localización");
        signatureCustomAppearance.setFontFamilyName("Arial");
        signatureCustomAppearance.setFontSize(10);
        signatureCustomAppearance.setCulture(new Locale("es", "ES"));
        // signatureCustomAppearance.setCulture (Locale.ROOT);
        signatureCustomAppearance.setDateTimeFormat("yyyy.MM.dd HH:mm:ss");
        pkcs.setCustomAppearance(signatureCustomAppearance);
        // подпишите PDF-файл
        pdfSign.sign(1, true, rect, pkcs);
        // сохраните выходной PDF-файл
        pdfSign.save(outFile);
    }
```