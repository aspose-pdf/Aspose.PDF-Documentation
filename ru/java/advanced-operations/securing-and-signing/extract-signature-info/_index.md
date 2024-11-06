---
title: Извлечение информации об изображении и подписи
linktitle: Извлечение информации об изображении и подписи
type: docs
weight: 30
url: ru/java/extract-image-and-signature-information/
description: Вы можете извлечь изображения из поля подписи и извлечь информацию о подписи, используя класс SignatureField с Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Извлечение изображения из поля подписи

Aspose.PDF for Java поддерживает возможность цифровой подписи PDF-файлов с использованием класса [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField), и при подписании документа вы также можете установить изображение для SignatureAppearance. Теперь этот API также предоставляет возможность извлечения информации о подписи, а также изображения, связанного с полем подписи.

Для того чтобы извлечь информацию о подписи, мы добавили метод [ExtractImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField#extractImage--) в класс [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField).
 Пожалуйста, посмотрите на следующий фрагмент кода, который демонстрирует шаги извлечения изображения из объекта SignatureField:

```java
public class ExampleExtractImageAndSignature {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Secure-Sign/";

    public static void ExtractingImageFromSignatureField() {
        Document pdfDocument = new Document(_dataDir + "ExtractingImage.pdf");

        int i = 0;
        try {
            for (WidgetAnnotation field : pdfDocument.getForm()) {
                SignatureField sf = (SignatureField) field;
                if (sf != null) {
                    FileOutputStream output = new FileOutputStream(_dataDir + "im" + i + ".jpeg");
                    InputStream tempStream = sf.extractImage();
                    byte[] b = new byte[tempStream.available()];
                    tempStream.read(b);
                    output.write(b);
                    output.close();
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (pdfDocument != null)
                pdfDocument.dispose();
        }

    }
```

### Заменить изображение подписи

Иногда может возникнуть необходимость заменить только изображение уже существующего поля подписи в PDF-файле. Чтобы выполнить это требование, сначала нам нужно найти поля формы внутри PDF-файла, определить поля подписи, получить размеры (прямоугольные размеры) поля подписи и затем наложить изображение с теми же размерами.

## Извлечение информации о подписи

Aspose.PDF для Java поддерживает функцию цифровой подписи PDF-файлов с использованием класса [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField). В настоящее время мы также можем определить действительность сертификата, но не можем извлечь весь сертификат. Информация, которую можно извлечь, включает открытый ключ, отпечаток, издателя и т.д.

Для извлечения информации о подписи мы ввели метод [ExtractCertificate](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField#extractCertificate--) в класс [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField).
 Пожалуйста, ознакомьтесь со следующим фрагментом кода, который демонстрирует шаги по извлечению сертификата из объекта SignatureField:

```java
    public static void ExtractSignatureInformation() throws IOException {
        String input = _dataDir + "ExtractSignatureInfo.pdf";
        Document pdfDocument = new Document(input);

        for (WidgetAnnotation field : pdfDocument.getForm()) {
            SignatureField sf = (SignatureField) field;
            if (sf != null) {
                InputStream cerStream = sf.extractCertificate();
                if (cerStream != null) {

                    byte[] buffer = new byte[cerStream.available()];
                    cerStream.read(buffer);

                    File targetFile = new File(_dataDir+"targetFile.cer");
                    OutputStream outStream = new FileOutputStream(targetFile);
                    outStream.write(buffer);
                    outStream.close();
                }
            }
        }
    }
}
```