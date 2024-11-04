---
title: Добавление подписи в PDF файл
type: docs
weight: 10
url: /net/add-signature-in-pdf/
description: Этот раздел объясняет, как добавить подпись в PDF файл с использованием класса PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Добавить цифровую подпись в PDF файл

Класс [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) позволяет добавить подпись в PDF файл. Вам необходимо создать объект класса [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) с использованием входного и выходного PDF-файлов. Вам также нужно создать объект [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle), в котором вы хотите добавить подпись, и для установки внешнего вида вы можете указать изображение, используя свойство [SignatureAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/properties/signatureappearance) объекта [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature). Aspose.Pdf.Facades также предоставляет различные виды подписей, такие как PKCS#1, PKCS#7 и PKCS#7Detached. Для создания подписи определенного типа вам необходимо создать объект конкретного класса, такого как **PKCS1**, **PKCS7** или **PKCS7Detached**, с использованием файла сертификата и пароля.

После создания объекта определенного типа подписи, вы можете использовать метод [Sign](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/sign/index) класса [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) для подписания PDF и передачи объекта конкретной подписи этому классу. Вы также можете указать другие атрибуты для этого метода. Наконец, вам нужно сохранить подписанный PDF, используя метод [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) класса [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature). Следующий фрагмент кода показывает, как добавить подпись в PDF файл.

```csharp
public static void AddPdfFileSignature()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample01.pdf");

            // Создать прямоугольник для расположения подписи
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);
            // Установить внешний вид подписи
            pdfSign.SignatureAppearance = _dataDir + "aspose-logo.png";

            // Создать любой из трех типов подписи
            PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

            pdfSign.Sign(1, "Я автор документа", "test01@aspose-pdf-demo.local", "Aspose Pdf Demo, Австралия", true, rect, signature);
            // Сохранить выходной PDF файл
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```
Следующий пример кода демонстрирует нам возможность подписать документ двумя подписями. В нашем примере мы ставим первую подпись на первую страницу, а вторую на вторую страницу. Вы можете указать нужные страницы.

```csharp
 public static void AddTwoSignature()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();

            // Подпись первой подписью

            pdfSign.BindPdf(_dataDir + "sample01.pdf");

            // Создать прямоугольник для расположения первой подписи
            System.Drawing.Rectangle rect1 = new System.Drawing.Rectangle(10, 10, 300, 50);

            // Создать объект первой подписи
            PKCS1 signature1 = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

            pdfSign.Sign(1, "Я автор документа", "test@aspose-pdf-demo.local", "Aspose Pdf Demo, Австралия", true, rect1, signature1);
            pdfSign.Save(_dataDir + "DigitallySign.pdf");


            // Подпись второй подписью

            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");

            // Создать прямоугольник для расположения второй подписи
            System.Drawing.Rectangle rect2 = new System.Drawing.Rectangle(10, 10, 300, 50);

            // Создать объект второй подписи
            PKCS1 signature2 = new PKCS1(_dataDir + "test02.pfx", "Aspose2021"); // PKCS#1

            pdfSign.Sign(2, "Я рецензент документа", "test02@aspose-pdf-demo.local", "Aspose Pdf Demo, Австралия", true, rect2, signature2);

            // Сохранить выходной PDF файл
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```

Для документа с формами или акроформами, который нужно подписать, см. следующий пример. 
Вам нужно создать объект класса [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature), используя входные и выходные PDF-файлы. Используйте [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesignature/bindpdf/methods/1) для связывания. Создайте подпись с возможностью добавления необходимых свойств. В нашем примере это 'Reason' и 'CustomAppearance'.

```csharp
 public static void AddPdfFileSignatureField()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample02.pdf");

            // Создайте любой из трех типов подписей
            PKCS1 signature = new PKCS1(_dataDir + "test02.pfx", "Aspose2021")
            {
                Reason = "Sign as Author",
                CustomAppearance = new SignatureCustomAppearance
                {
                    FontSize = 6,
                    FontFamilyName = "Calibri"
                }
            }; // PKCS#1
            pdfSign.Sign("Signature1", signature);
            // Сохранить выходной PDF-файл
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```

Если наш документ имеет два поля, алгоритм его подписания аналогичен первому примеру.

```csharp
public static void AddPdfFileSignatureField2()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample03.pdf");

            // Создайте любой из трех типов подписей
            PKCS1 signature1 = new PKCS1(_dataDir + "test01.pfx", "Aspose2021")
            {
                Reason = "Подписать как Автор",
                CustomAppearance = new SignatureCustomAppearance
                {
                    FontSize = 6
                }
            }; // PKCS#1
            pdfSign.Sign("Signature1", signature1);
            // Сохранить выходной PDF файл
            pdfSign.Save(_dataDir + "DigitallySign.pdf");

            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");

            // Создайте любой из трех типов подписей
            PKCS1 signature2 = new PKCS1(_dataDir + "test02.pfx", "Aspose2021")
            {
                Reason = "Подписать как Рецензент",
                CustomAppearance = new SignatureCustomAppearance
                {
                    FontSize = 6
                }
            }; // PKCS#1
            pdfSign.Sign("Signature2", signature2);
            // Сохранить выходной PDF файл
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```