---
title: تحويل PDF/A إلى PDF 
linktitle: تحويل PDF/A إلى PDF
type: docs
weight: 350
url: /androidjava/convert-pdfa-to-pdf/
lastmod: "2021-06-05"
description: لتحويل PDF/A إلى PDF يجب إزالة القيود من المستند الأصلي. يتيح لك Aspose.PDF لـ Android عبر Java حل هذه المشكلة بسهولة وببساطة.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

تحويل مستند PDF/A إلى PDF يعني إزالة قيود <abbr title="أرشيف صيغة المستند المحمول">PDF/A</abbr> من المستند الأصلي. تحتوي فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) على طريقة RemovePdfaCompliance(..) لإزالة معلومات الامتثال الخاصة بـ PDF من ملف الإدخال/المصدر.

```java

    public void convertPDFAtoPDF() {
        String pdfaDocumentFileName = new File(fileStorage, "Conversion/sample-pdfa.pdf").toString();
        String pdfDocumentFileName = new File(fileStorage, "Conversion/sample-out.pdf").toString();

        try {
            // إنشاء كائن المستند
            document = new Document(pdfaDocumentFileName);

            // إزالة معلومات الامتثال الخاصة بـ PDF/A
            document.removePdfaCompliance();

            // حفظ الناتج بتنسيق XML
            document.save(pdfDocumentFileName);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);

    }
```


هذا المعلومات تُزال أيضًا إذا قمت بإجراء أي تغييرات في المستند (مثل إضافة صفحات). في المثال التالي، يفقد المستند الناتج التوافق مع PDF/A بعد إضافة الصفحة.

```java
   public void convertPDFAtoPDFAdvanced() {
        String pdfaDocumentFileName = new File(fileStorage, "Conversion/sample-pdfa.pdf").toString();
        String pdfDocumentFileName = new File(fileStorage, "Conversion/sample-out.pdf").toString();

        // إنشاء كائن المستند
        document = new Document(pdfaDocumentFileName);

        // إضافة صفحة جديدة (فارغة) تزيل معلومات التوافق مع PDF/A.
        document.getPages().add();

        // حفظ المستند المُحدث
        document.save(pdfDocumentFileName);
    }
```