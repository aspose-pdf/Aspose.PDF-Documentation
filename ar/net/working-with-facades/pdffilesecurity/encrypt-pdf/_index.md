```
---
title: تشفير ملف PDF
type: docs
weight: 10
url: /ar/net/encrypt-pdf-file/
description: يشرح هذا الموضوع كيفية تشفير ملف PDF باستخدام فئة PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

حماية مستند PDF من الوصول غير المصرح به من الخارج، خاصة أثناء مشاركة الملفات أو الأرشفة.

يمكن تشفير مستندات PDF السرية وحمايتها بكلمة مرور. فقط المستخدم الذي يعرف كلمة المرور سيكون قادرًا على فك التشفير وفتح وعرض هذه المستندات.

لنلق نظرة على كيفية عمل تشفير PDF باستخدام مكتبة Aspose.PDF.

## تشفير ملف PDF باستخدام أنواع وخوارزميات تشفير مختلفة

من أجل تشفير ملف PDF، تحتاج إلى إنشاء كائن [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) ثم استدعاء طريقة [EncryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile).
``` يمكنك تمرير كلمة مرور المستخدم، وكلمة مرور المالك، والامتيازات إلى طريقة [EncryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile). تحتاج أيضًا إلى تمرير قيم KeySize وAlgorithm لهذه الطريقة.

راجع قائمة ممكنة لمثل [CryptoAlgorithm](https://reference.aspose.com/pdf/net/aspose.pdf/cryptoalgorithm): 

|**اسم العضو**|**القيمة**|**الوصف**|
| :- | :- | :- |
|RC4x40|0|RC4 بطول مفتاح 40.|
|RC4x128|1|RC4 بطول مفتاح 128.|
|AESx128|2|AES بطول مفتاح 128.|
|AESx256|3|AES بطول مفتاح 256.|

يوضح لك مقطع الشيفرة التالي كيفية تشفير ملف PDF.

```csharp
public static void EncryptPDFFile()
        {
            // إنشاء كائن PdfFileSecurity
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.BindPdf(_dataDir + "sample.pdf");
            // تشفير الملف باستخدام تشفير 256 بت
            fileSecurity.EncryptFile("User_P@ssw0rd", "OwnerP@ssw0rd", DocumentPrivilege.Print, KeySize.x256, Algorithm.AES);
            fileSecurity.Save(_dataDir + "sample_encrypted.pdf");
        }
```