---
title: إزالة التوقيع من ملف PDF
type: docs
weight: 20
url: /ar/java/remove-signature-from-pdf/
description: يشرح هذا القسم كيفية التعامل مع التوقيع في ملف PDF باستخدام فئة PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## إزالة التوقيع الرقمي من ملف PDF

عند إضافة توقيع إلى ملفات PDF، من الممكن إزالته. يمكنك إزالة توقيع معين أو جميع التوقيعات في الملف. أسرع طريقة لإزالة التوقيع تزيل أيضًا حقل التوقيع، ولكن من الممكن إزالة التوقيع فقط، مع الحفاظ على حقل التوقيع حتى يمكن توقيع الملف مرة أخرى.

تتيح لك طريقة RemoveSignature في فئة [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) إزالة توقيع من ملف PDF.
 هذه الطريقة تأخذ اسم التوقيع كمدخل. يمكنك تحديد اسم التوقيع مباشرة، لإزالة جميع التوقيعات، احصل على أسماء التوقيعات باستخدام طريقة [getSignNames](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature#getSignNames--).

يظهر مقطع الكود التالي كيفية إزالة التوقيع الرقمي من ملف PDF.

```java
 public static void RemoveSignature() {
        // قم بإنشاء كائن PdfFileSignature
        PdfFileSignature pdfSign = new PdfFileSignature();
        // افتح مستند PDF
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");
        // احصل على قائمة بأسماء التوقيعات
        List<String> sigNames = pdfSign.getSignNames();
        // أزل جميع التوقيعات من ملف PDF
        for (int index = 0; index < sigNames.size(); index++) {
            System.out.println("Removed " + sigNames.get(index));
            pdfSign.removeSignature(sigNames.get(index));
        }
        // احفظ ملف PDF المحدث
        pdfSign.save(_dataDir + "RemoveSignature_out.pdf");
    }
```

### إزالة التوقيع لكن الاحتفاظ بحقل التوقيع

كما هو موضح أعلاه، فإن طريقة [removeSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature#removeSignature-java.lang.String-) في فئة [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) تتيح لك إزالة حقول التوقيع من ملفات PDF. عند استخدام هذه الطريقة مع الإصدارات قبل 9.3.0، يتم إزالة كل من التوقيع وحقل التوقيع. بعض المطورين يرغبون في إزالة التوقيع فقط والاحتفاظ بحقل التوقيع حتى يمكن استخدامه لإعادة توقيع المستند. للاحتفاظ بحقل التوقيع وإزالة التوقيع فقط، يرجى استخدام مقتطف الشيفرة التالي.

```java
 public static void RemoveSignatureButKeepField() {
        // إنشاء كائن PdfFileSignature
        PdfFileSignature pdfSign = new PdfFileSignature();

        // فتح مستند PDF
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");

        pdfSign.removeSignature("Signature1", false);

        // حفظ ملف PDF المحدث
        pdfSign.save(_dataDir + "RemoveSignature_out.pdf");
    }
```


The following example shows how to remove all signatures from fields.

```java
public static void RemoveSignatureButKeepField2() {
        // إنشاء كائن PdfFileSignature
        PdfFileSignature pdfSign = new PdfFileSignature();

        // فتح مستند PDF
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");

        List<String> sigNames = pdfSign.getSignNames();
        for (String sigName : sigNames) {
            pdfSign.removeSignature(sigName, false);
        }

        // حفظ ملف PDF المحدث
        pdfSign.save(_dataDir + "RemoveSignature_out.pdf");
    }
```