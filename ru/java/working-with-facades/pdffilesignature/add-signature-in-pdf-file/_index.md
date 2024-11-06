---
title: Добавить подпись в PDF файл
type: docs
weight: 10
url: ru/java/add-signature-in-pdf/
description: Этот раздел объясняет, как работать с подписью в PDF файле, используя класс PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Добавить цифровую подпись в PDF файл (фасады)

Класс [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) позволяет добавлять подпись в PDF файл. Вам нужно создать объект класса [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature), используя входные и выходные PDF файлы. Также необходимо создать объект Rectangle, в который вы хотите добавить подпись, и для установки внешнего вида вы можете указать изображение, используя свойство setSignatureAppearance объекта [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature).

Aspose.Pdf.Facades также предоставляет различные виды подписей, такие как PKCS#1, PKCS#7 и PKCS#7Detached.
 Для создания подписи определенного типа необходимо создать объект конкретного класса, такого как PKCS1, PKCS7 или PKCS7Detached, используя файл сертификата и пароль.

Как только объект определенного типа подписи создан, вы можете использовать метод sign класса [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) для подписания PDF и передать в этот класс объект конкретной подписи. Также вы можете указать другие атрибуты для этого метода. Наконец, вам нужно сохранить подписанный PDF, используя метод save класса [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature). Следующий фрагмент кода показывает, как добавить подпись в PDF файл.

```java
public static void AddPdfFileSignature() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample01.pdf");

        // Создайте прямоугольник для расположения подписи
        java.awt.Rectangle rect = new java.awt.Rectangle(10, 10, 300, 50);
        // Установите внешний вид подписи
        pdfSign.setSignatureAppearance(_dataDir + "aspose-logo.png");

        // Создайте любой из трех типов подписи
        PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

        pdfSign.sign(1, "Я автор документа", "test01@aspose-pdf-demo.local", "Aspose Pdf Demo, Австралия", true, rect,
                signature);
        // Сохраните выходной PDF файл
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```

Следующий пример кода показывает нам возможность подписать документ двумя подписями. В нашем примере мы ставим первую подпись на первую страницу, а вторую — на вторую страницу. Вы можете указать страницы, которые вам нужны.

```java
    public static void AddTwoSignature() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        // Подписать первой подписью

        pdfSign.bindPdf(_dataDir + "sample01.pdf");

        // Создать прямоугольник для расположения первой подписи
        java.awt.Rectangle rect1 = new java.awt.Rectangle(10, 10, 300, 50);

        // Создать объект первой подписи
        PKCS1 signature1 = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

        pdfSign.sign(1, "Я автор документа", "test@aspose-pdf-demo.local", "Aspose Pdf Demo, Австралия", true, rect1,
                signature1);
        pdfSign.save(_dataDir + "DigitallySign.pdf");

        // Подписать второй подписью

        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");

        // Создать прямоугольник для расположения второй подписи
        java.awt.Rectangle rect2 = new java.awt.Rectangle(10, 10, 300, 50);

        // Создать объект второй подписи
        PKCS1 signature2 = new PKCS1(_dataDir + "test02.pfx", "Aspose2021"); // PKCS#1

        pdfSign.sign(2, "Я рецензент документа", "test02@aspose-pdf-demo.local", "Aspose Pdf Demo, Австралия", true,
                rect2, signature2);

        // Сохранить выходной PDF файл
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```


Для документа с формами или акроформами, который необходимо подписать, см. следующий пример. Вам нужно создать объект класса [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature), используя входные и выходные PDF-файлы. Используйте bindPdf для связывания. Создайте подпись с возможностью добавления необходимых свойств. В нашем примере это "Reason" и "CustomAppearance".

```java
  public static void AddPdfFileSignatureField() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample02.pdf");

        // Создать любой из трех типов подписей
        PKCS1 signature = new PKCS1(_dataDir + "test02.pfx", "Aspose2021");
        signature.setReason("Подписать как Автор");

        SignatureCustomAppearance sca = new SignatureCustomAppearance();
        signature.setCustomAppearance(sca);
        sca.setFontSize(6);
        sca.setFontFamilyName("Calibri");

        // PKCS#1
        pdfSign.sign("Signature1", signature);
        // Сохранить выходной PDF-файл
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```


Если наш документ имеет два поля, алгоритм его подписания аналогичен первому примеру.

```java
   public static void AddPdfFileSignatureField2() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample03.pdf");

        // Создайте любой из трех типов подписей
        PKCS1 signature1 = new PKCS1(_dataDir + "test01.pfx", "Aspose2021");
        SignatureCustomAppearance sca = new SignatureCustomAppearance();
        signature1.setCustomAppearance(sca);
        sca.setFontSize(6);
        sca.setFontFamilyName("Calibri");

        signature1.setReason("Подпись как Автор"); // PKCS#1
        pdfSign.sign("Signature1", signature1);

        // Сохранить выходной PDF файл
        pdfSign.save(_dataDir + "DigitallySign.pdf");

        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");

        // Создайте любой из трех типов подписей
        PKCS1 signature2 = new PKCS1(_dataDir + "test02.pfx", "Aspose2021");
        signature2.setReason("Подпись как Рецензент"); // PKCS#1
        signature2.setCustomAppearance(sca);
        pdfSign.sign("Signature2", signature2);
        // Сохранить выходной PDF файл
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```