---
title: تحويل PDF/A إلى PDF
linktitle: تحويل PDF/A إلى PDF
type: docs
weight: 350
url: /ar/androidjava/convert-pdfa-to-pdf/
lastmod: "2026-06-30"
description: لتحويل PDF/A إلى PDF يجب عليك إزالة القيود من المستند الأصلي. Aspose.PDF for Android via Java يتيح لك حل هذه المشكلة بسهولة وبساطة.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

تحويل مستند PDF/A إلى PDF يعني إزالة <abbr title=\"Portable Document Format Archive\"
\">PDF/A</abbr> تقييد من المستند الأصلي. الفئة [وثيقة](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) يحتوي على طريقة RemovePdfaCompliance(..) لإزالة
معلومات امتثال PDF من ملف الإدخال/المصدر.

```java

    public void convertPDFAtoPDF() {
        String pdfaDocumentFileName = new File(fileStorage, "Conversion/sample-pdfa.pdf").toString();
        String pdfDocumentFileName = new File(fileStorage, "Conversion/sample-out.pdf").toString();

        try {
            // Create Document object
            document = new Document(pdfaDocumentFileName);

            // Remove PDF/A compliance information
            document.removePdfaCompliance();

            // Save output in XML format
            document.save(pdfDocumentFileName);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);

    }
```

تتم أيضًا إزالة هذه المعلومات إذا قمت بإجراء أي تغييرات على المستند (e.g. إضافة صفحات). في المثال التالي، يفقد المستند الناتج توافقه مع PDF/A بعد إضافة الصفحة.

```java
   public void convertPDFAtoPDFAdvanced() {
        String pdfaDocumentFileName = new File(fileStorage, "Conversion/sample-pdfa.pdf").toString();
        String pdfDocumentFileName = new File(fileStorage, "Conversion/sample-out.pdf").toString();

        // Create Document object
        document = new Document(pdfaDocumentFileName);

        // Adding a new (empty) page removes PDF/A compliance information.
        document.getPages().add();

        // Save updated document
        document.save(pdfDocumentFileName);
    }
```




