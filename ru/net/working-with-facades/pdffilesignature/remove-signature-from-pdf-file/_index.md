---
title: Удалить подпись из PDF файла
type: docs
weight: 20
url: ru/net/remove-signature-from-pdf/
description: Этот раздел объясняет, как удалить подпись из PDF файла, используя класс PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Удалить цифровую подпись из PDF файла

Когда подпись была добавлена в PDF файл, возможно её удаление. Вы можете удалить либо конкретную подпись, либо все подписи в файле. Самый быстрый метод удаления подписи также удаляет поле подписи, но возможно просто удалить подпись, сохранив поле подписи, чтобы файл мог быть подписан снова.

Метод RemoveSignature класса [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) позволяет удалить подпись из PDF файла. Этот метод принимает имя подписи в качестве входных данных. Либо укажите имя подписи напрямую, чтобы удалить все подписи, получите имена подписей, используя метод [GetSignNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/getsignername).

Следующий фрагмент кода показывает, как удалить цифровую подпись из PDF-файла.

```csharp
 public static void RemoveSignature()
        {
            // Создать объект PdfFileSignature
            PdfFileSignature pdfSign = new PdfFileSignature();
            // Открыть PDF документ
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");
            // Получить список имен подписей
            var sigNames = pdfSign.GetSignNames();
            // Удалить все подписи из PDF файла
            for (int index = 0; index < sigNames.Count; index++)
            {
                Console.WriteLine($"Удалено {sigNames[index]}");
                pdfSign.RemoveSignature(sigNames[index]);
            }
            // Сохранить обновленный PDF файл
            pdfSign.Save(_dataDir + "RemoveSignature_out.pdf");
        }
```
### Удалить подпись, но сохранить поле подписи

Как показано выше, метод [RemoveSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/removesignature) класса [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) позволяет удалять поля подписи из файлов PDF. При использовании этого метода с версиями до 9.3.0 удаляются как подпись, так и поле подписи. Некоторые разработчики хотят удалить только подпись и сохранить поле подписи, чтобы его можно было использовать для повторного подписания документа. Чтобы сохранить поле подписи и удалить только подпись, пожалуйста, используйте следующий фрагмент кода.

```csharp
public static void RemoveSignatureButKeepField()
        {
            // Создать объект PdfFileSignature
            PdfFileSignature pdfSign = new PdfFileSignature();

            // Открыть PDF документ
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");

            pdfSign.RemoveSignature("Signature1", false);

            // Сохранить обновленный PDF файл
            pdfSign.Save(_dataDir + "RemoveSignature_out.pdf");
        }
```

Следующий пример показывает, как удалить все подписи из полей.

```csharp
public static void RemoveSignatureButKeepField2()
        {
            // Создать объект PdfFileSignature
            PdfFileSignature pdfSign = new PdfFileSignature();

            // Открыть PDF документ
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");

            var sigNames = pdfSign.GetSignNames();
            foreach (var sigName in sigNames)
            {
                pdfSign.RemoveSignature(sigName, false);
            }

            // Сохранить обновленный PDF файл
            pdfSign.Save(_dataDir + "RemoveSignature_out.pdf");
        }

```