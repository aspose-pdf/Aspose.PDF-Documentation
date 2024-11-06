---
title: Работа с подписью в PDF файле
type: docs
weight: 40
url: ru/net/working-with-signature-in-a-pdf-file/
description: Этот раздел объясняет, как извлечь информацию о подписи, извлечь изображение из подписи, изменить язык и т.д. с использованием класса PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Как извлечь информацию о подписи

Aspose.PDF для .NET поддерживает функцию цифровой подписи PDF файлов с использованием класса PdfFileSignature. В настоящее время также возможно определить действительность сертификата, но мы не можем извлечь весь сертификат. Информация, которую можно извлечь, включает открытый ключ, отпечаток и издателя и т.д.

Для извлечения информации о подписи мы ввели метод ExtractCertificate(..) в класс PdfFileSignature. Пожалуйста, обратите внимание на следующий фрагмент кода, который демонстрирует шаги по извлечению сертификата из объекта PdfFileSignature:

```csharp
public static void ExtractSignatureInfo()
        {
            string input = _dataDir + "DigitallySign.pdf";
            string certificateFileName = "extracted_cert.pfx";
            using (PdfFileSignature pdfFileSignature = new PdfFileSignature())
            {
                pdfFileSignature.BindPdf(input);
                var sigNames = pdfFileSignature.GetSignNames();
                if (sigNames.Count > 0)
                {
                    string sigName = sigNames[0];
                    if (!string.IsNullOrEmpty(sigName))
                    {
                        Stream cerStream = pdfFileSignature.ExtractCertificate(sigName);
                        if (cerStream != null)
                        {
                            using (cerStream)
                            {
                                using (FileStream fs = new FileStream(_dataDir + certificateFileName, FileMode.CreateNew))
                                {
                                    cerStream.CopyTo(fs);
                                }
                            }
                        }
                    }
                }
            }
        }
```

## Извлечение изображения из поля подписи (PdfFileSignature)

Aspose.PDF для .NET поддерживает функцию цифровой подписи PDF-файлов с использованием класса PdfFileSignature, и при подписании документа вы также можете установить изображение для SignatureAppearance. Теперь этот API также предоставляет возможность извлекать информацию о подписи, а также изображение, связанное с полем подписи.

Для извлечения информации о подписи мы представили метод ExtractImage(..) в классе PdfFileSignature. Пожалуйста, ознакомьтесь со следующим фрагментом кода, который демонстрирует шаги по извлечению изображения из объекта PdfFileSignature:

```csharp
public static void ExtractSignatureImage()
        {
            using (PdfFileSignature signature = new PdfFileSignature())
            {
                signature.BindPdf(_dataDir + "DigitallySign.pdf");

                if (signature.ContainsSignature())
                {
                    foreach (string sigName in signature.GetSignNames())
                    {
                        string outFile = _dataDir + "ExtractImages_out.jpg";
                        using (Stream imageStream = signature.ExtractImage(sigName))
                        {
                            if (imageStream != null)
                            {
                                imageStream.Position = 0;
                                using (FileStream fs = new FileStream(outFile, FileMode.OpenOrCreate))
                                {
                                    imageStream.CopyTo(fs);
                                }
                            }
                        }
                    }
                }
            }
        }
```

## Подавление местоположения и причины

Функциональность Aspose.PDF позволяет гибко настраивать экземпляр цифровой подписи. Класс [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) предоставляет возможность подписывать PDF файл. Реализация метода Sign позволяет подписывать PDF и передавать конкретный объект подписи этому классу. Метод Sign содержит набор атрибутов для настройки выходной цифровой подписи. В случае, если вам нужно скрыть некоторые текстовые атрибуты из результата подписи, вы можете оставить их пустыми. Следующий фрагмент кода демонстрирует, как подавить две строки местоположения и причины из блока подписи:

```csharp
public static void SupressLocationReason()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample01.pdf");

            // Create a rectangle for signature location
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);
            // Set signature appearance
            pdfSign.SignatureAppearance = _dataDir + "aspose-logo.png";

            // Create any of the three signature types
            PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

            pdfSign.Sign(1, string.Empty, "test01@aspose-pdf-demo.local", string.Empty, true, rect, signature);
            // Save output PDF file
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```

## Функции настройки для цифровой подписи

Aspose.PDF для .NET позволяет настраивать функции для цифровой подписи. Метод Sign класса [SignatureCustomAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturecustomappearance) реализует 6 перегрузок для вашего удобного использования. Например, вы можете настроить результирующую подпись только с помощью экземпляра класса SignatureCustomAppearance и его значений свойств. Следующий фрагмент кода демонстрирует, как скрыть надпись "Цифровая подпись от" из выходной цифровой подписи вашего PDF.

```csharp
  public static void CustomizationFeaturesForDigitalSign()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample01.pdf");

            // Создайте прямоугольник для расположения подписи
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);

            // Создайте любой из трех типов подписей
            PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

            SignatureCustomAppearance signatureCustomAppearance = new SignatureCustomAppearance
            {
                FontSize = 6,
                FontFamilyName = "Times New Roman",
                DigitalSignedLabel = "Подписано:"
            };
            signature.CustomAppearance = signatureCustomAppearance;

            pdfSign.Sign(1, true, rect, signature);
            // Сохраните выходной PDF файл
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```

## Изменение языка в тексте цифровой подписи

С использованием Aspose.PDF для .NET API, вы можете подписать PDF файл с использованием любого из следующих трех типов подписей:

- PKCS#1
- PKCS#7
- PKCS#7

Каждая из предоставленных подписей содержит набор свойств конфигурации, реализованных для вашего удобства (локализация, формат даты и времени, семейство шрифтов и т.д.). Класс [SignatureCustomAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturecustomappearance) предоставляет соответствующую функциональность. Следующий фрагмент кода демонстрирует, как изменить язык в тексте цифровой подписи:

```csharp
     public static void ChangeLanguageInDigitalSignText()
        {
            string inFile = _dataDir + "sample01.pdf";
            string outFile = _dataDir + "DigitallySign.pdf";

            using (Aspose.Pdf.Facades.PdfFileSignature pdfSign = new Aspose.Pdf.Facades.PdfFileSignature())
            {
                pdfSign.BindPdf(inFile);
                //создать прямоугольник для расположения подписи
                System.Drawing.Rectangle rect = new System.Drawing.Rectangle(310, 45, 200, 50);

                //создать любой из трех типов подписей
                PKCS7 pkcs = new PKCS7(_dataDir + "test01.pfx", "Aspose2021")
                {
                    Reason = "Pruebas Firma",
                    ContactInfo = "Contacto Pruebas",
                    Location = "Población (Provincia)",
                    Date = DateTime.Now
                };
                SignatureCustomAppearance signatureCustomAppearance = new SignatureCustomAppearance
                {
                    DateSignedAtLabel = "Fecha",
                    DigitalSignedLabel = "Digitalmente firmado por",
                    ReasonLabel = "Razón",
                    LocationLabel = "Localización",
                    FontFamilyName = "Arial",
                    FontSize = 10d,
                    Culture = System.Globalization.CultureInfo.InvariantCulture,
                    DateTimeFormat = "yyyy.MM.dd HH:mm:ss"
                };
                pkcs.CustomAppearance = signatureCustomAppearance;
                // подписать PDF файл
                pdfSign.Sign(1, true, rect, pkcs);
                //сохранить выходной PDF файл
                pdfSign.Save(outFile);
            }
        }
```