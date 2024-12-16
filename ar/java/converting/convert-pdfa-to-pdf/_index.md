---
title: تحويل PDF/A إلى تنسيق PDF
linktitle: تحويل PDF/A إلى تنسيق PDF
type: docs
weight: 110
url: /ar/java/convert-pdfa-to-pdf/
lastmod: "2021-11-19"
description: يوضح هذا الموضوع كيفية استخدام Aspose.PDF لتحويل ملف PDF/A إلى مستند PDF باستخدام مكتبة Java.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## تحويل مستند PDF/A إلى PDF

تحويل مستند PDF/A إلى PDF يعني إزالة قيود <abbr title="أرشيف تنسيق المستند المحمول">PDF/A</abbr> من المستند الأصلي. تحتوي فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) على الطريقة RemovePdfaCompliance(..) لإزالة معلومات الالتزام بمعيار PDF من الملف المدخل/المصدر.

```java
public static void runPDFA_to_PDF() {
    String pdfaDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF.pdf").toString();
    String documentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF_out.pdf").toString();

    // إنشاء كائن المستند
    Document document = new Document(pdfaDocumentFileName);

    // إزالة معلومات الالتزام بمعيار PDF/A
    document.removePdfaCompliance();

    // حفظ المخرجات بتنسيق XML
    document.save(documentFileName);
    document.close();
}
```


هذه المعلومات تُزال أيضًا إذا قمت بإجراء أي تغييرات في المستند (مثل إضافة صفحات). في المثال التالي، يفقد المستند الناتج الامتثال لـ PDF/A بعد إضافة الصفحة.

```java
public static void runPDFAtoPDFAdvanced() {
    String pdfaDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF.pdf").toString();
    String documentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF_out.pdf").toString();

    // إنشاء كائن المستند
    Document document = new Document(pdfaDocumentFileName);

    // إضافة صفحة جديدة (فارغة) يزيل معلومات الامتثال لـ PDF/A.
    document.getPages().add();

    // حفظ المستند المحدث
    document.save(documentFileName);
    document.close();
}
```