---
title: Удалить подпись из PDF-файла
type: docs
weight: 20
url: ru/java/remove-signature-from-pdf/
description: Этот раздел объясняет, как работать с подписью в PDF-файле с использованием класса PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Удалить цифровую подпись из PDF-файла

Когда к файлу PDF добавлена подпись, ее можно удалить. Вы можете удалить либо конкретную подпись, либо все подписи в файле. Самый быстрый способ удаления подписи также удаляет поле подписи, но можно просто удалить подпись, сохранив поле подписи, чтобы файл можно было подписать снова.

Метод RemoveSignature класса [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) позволяет удалить подпись из PDF-файла.
 Этот метод принимает имя подписи в качестве входного параметра. Либо укажите имя подписи напрямую, чтобы удалить все подписи, получите имена подписей, используя метод [getSignNames](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature#getSignNames--).

Следующий фрагмент кода показывает, как удалить цифровую подпись из PDF-файла.

```java
 public static void RemoveSignature() {
        // Создать объект PdfFileSignature
        PdfFileSignature pdfSign = new PdfFileSignature();
        // Открыть PDF документ
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");
        // Получить список имен подписей
        List<String> sigNames = pdfSign.getSignNames();
        // Удалить все подписи из PDF файла
        for (int index = 0; index < sigNames.size(); index++) {
            System.out.println("Удалено " + sigNames.get(index));
            pdfSign.removeSignature(sigNames.get(index));
        }
        // Сохранить обновленный PDF файл
        pdfSign.save(_dataDir + "RemoveSignature_out.pdf");
    }
```

### Удаление подписи, но сохранение поля подписи

Как показано выше, метод [removeSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature#removeSignature-java.lang.String-) класса [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) позволяет удалять поля подписей из PDF-файлов. При использовании этого метода в версиях до 9.3.0 удаляются как подпись, так и поле подписи. Некоторые разработчики хотят удалить только подпись и сохранить поле подписи, чтобы можно было повторно подписать документ. Чтобы сохранить поле подписи и удалить только подпись, пожалуйста, используйте следующий фрагмент кода.

```java
 public static void RemoveSignatureButKeepField() {
        // Создать объект PdfFileSignature
        PdfFileSignature pdfSign = new PdfFileSignature();

        // Открыть PDF-документ
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");

        pdfSign.removeSignature("Signature1", false);

        // Сохранить обновленный PDF-файл
        pdfSign.save(_dataDir + "RemoveSignature_out.pdf");
    }
```


Следующий пример показывает, как удалить все подписи из полей.

```java
public static void RemoveSignatureButKeepField2() {
        // Создать объект PdfFileSignature
        PdfFileSignature pdfSign = new PdfFileSignature();

        // Открыть PDF документ
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");

        List<String> sigNames = pdfSign.getSignNames();
        for (String sigName : sigNames) {
            pdfSign.removeSignature(sigName, false);
        }

        // Сохранить обновленный PDF файл
        pdfSign.save(_dataDir + "RemoveSignature_out.pdf");
    }
```