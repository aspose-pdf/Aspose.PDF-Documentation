---
title: إزالة التوقيع من ملف PDF
type: docs
weight: 20
url: /net/remove-signature-from-pdf/
description: يوضح هذا القسم كيفية إزالة التوقيع من ملف PDF باستخدام فئة PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## إزالة التوقيع الرقمي من ملف PDF

عند إضافة توقيع إلى ملفات PDF، من الممكن إزالته. يمكنك إزالة توقيع معين أو جميع التوقيعات في ملف. الطريقة الأسرع لإزالة التوقيع تزيل أيضًا حقل التوقيع، ولكن من الممكن فقط إزالة التوقيع مع الاحتفاظ بحقل التوقيع بحيث يمكن توقيع الملف مرة أخرى.

تسمح لك طريقة RemoveSignature للفئة [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) بإزالة توقيع من ملف PDF. هذه الطريقة تأخذ اسم التوقيع كمدخل. يمكنك تحديد اسم التوقيع مباشرة، لإزالة جميع التوقيعات، احصل على أسماء التوقيعات باستخدام طريقة [GetSignNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/getsignername).

يظهر المقطع البرمجي التالي كيفية إزالة التوقيع الرقمي من ملف PDF.

```csharp
 public static void RemoveSignature()
        {
            // إنشاء كائن PdfFileSignature
            PdfFileSignature pdfSign = new PdfFileSignature();
            // فتح مستند PDF
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");
            // الحصول على قائمة بأسماء التوقيعات
            var sigNames = pdfSign.GetSignNames();
            // إزالة جميع التوقيعات من ملف PDF
            for (int index = 0; index < sigNames.Count; index++)
            {
                Console.WriteLine($"Removed {sigNames[index]}");
                pdfSign.RemoveSignature(sigNames[index]);
            }
            // حفظ ملف PDF المحدث
            pdfSign.Save(_dataDir + "RemoveSignature_out.pdf");
        }
```
### إزالة التوقيع ولكن الاحتفاظ بحقل التوقيع

كما هو موضح أعلاه، تتيح لك طريقة [RemoveSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/removesignature) في فئة [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) إزالة حقول التوقيع من ملفات PDF. عند استخدام هذه الطريقة مع الإصدارات قبل 9.3.0، يتم إزالة كل من التوقيع وحقل التوقيع. يرغب بعض المطورين في إزالة التوقيع فقط والاحتفاظ بحقل التوقيع بحيث يمكن استخدامه لإعادة توقيع المستند. للاحتفاظ بحقل التوقيع وإزالة التوقيع فقط، يُرجى استخدام مقطع الكود التالي.

```csharp
public static void RemoveSignatureButKeepField()
        {
            // إنشاء كائن PdfFileSignature
            PdfFileSignature pdfSign = new PdfFileSignature();

            // فتح مستند PDF
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");

            pdfSign.RemoveSignature("Signature1", false);

            // حفظ ملف PDF المحدث
            pdfSign.Save(_dataDir + "RemoveSignature_out.pdf");
        }
```

The following example shows how to remove all signatures from fields.

```csharp
public static void RemoveSignatureButKeepField2()
        {
            // إنشاء كائن PdfFileSignature
            PdfFileSignature pdfSign = new PdfFileSignature();

            // فتح مستند PDF
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");

            var sigNames = pdfSign.GetSignNames();
            foreach (var sigName in sigNames)
            {
                pdfSign.RemoveSignature(sigName, false);
            }

            // حفظ ملف PDF المحدث
            pdfSign.Save(_dataDir + "RemoveSignature_out.pdf");
        }

```