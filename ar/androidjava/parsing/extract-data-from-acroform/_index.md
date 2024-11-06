---
title: استخراج البيانات من AcroForm
linktitle: استخراج البيانات من AcroForm
type: docs
weight: 50
url: ar/androidjava/extract-data-from-acroform/
description: توجد AcroForms في العديد من مستندات PDF. تهدف هذه المقالة إلى مساعدتك في فهم كيفية استخراج البيانات من AcroForms باستخدام Aspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## استخراج حقول النموذج من مستند PDF

لا يتيح لك Aspose.PDF لنظام Android عبر Java إنشاء وملء حقول النموذج فحسب، بل يسهل أيضًا استخراج بيانات حقول النموذج أو معلومات حقول النموذج من ملفات PDF.

افترض أننا لا نعرف أسماء حقول النموذج مسبقًا. ثم يجب علينا التكرار عبر كل صفحة في PDF لاستخراج معلومات حول جميع AcroForms في PDF وكذلك قيم حقول النموذج. للوصول إلى النموذج، نحتاج إلى استخدام طريقة [getForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--).

```java
 public void extractFormFields () {
        // افتح المستند
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // احصل على القيم من جميع الحقول
        StringBuilder sb=new StringBuilder();
        for (com.aspose.pdf.Field formField : document.getForm().getFields()) {
            sb.append("Field Name: ");
            sb.append(formField.getPartialName());
            sb.append(" Value: ");
            sb.append(formField.getValue());
            sb.append('\n');
        }
        resultMessage.setText(sb);
    }
```


إذا كنت تعرف أسماء حقول النموذج التي ترغب في استخراج القيم منها، يمكنك استخدام الفهرس في مجموعة Documents.Form لاسترداد هذه البيانات بسرعة.

## استرداد قيمة حقل النموذج حسب العنوان

تسمح لك خاصية Value لحقل النموذج بالحصول على قيمة حقل معين. للحصول على القيمة، احصل على حقل النموذج من [كائن المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) [مجموعة حقول النموذج](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--). يختار هذا المثال [حقل مربع النص](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) ويسترد قيمته باستخدام طريقة [getValue](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--).

```java

    public void extractFormDataByName () {
        // فتح المستند
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        com.aspose.pdf.TextBoxField textBoxField1
                =(com.aspose.pdf.TextBoxField) document.getForm().get("Last Name");

        resultMessage.setText("Last Name: " + textBoxField1.getValue());

    }
```


## استخراج البيانات إلى XML من ملف PDF

تسمح لك فئة Form بتصدير البيانات إلى ملف XML من ملف PDF باستخدام طريقة ExportXml. من أجل تصدير البيانات إلى XML، تحتاج إلى إنشاء كائن من فئة Form ثم استدعاء طريقة ExportXml باستخدام كائن FileStream. أخيرًا، يمكنك إغلاق كائن FileStream والتخلص من كائن Form. يعرض لك مقطع الشفرة التالي كيفية تصدير البيانات إلى ملف XML.

```java
public void extractFormFieldsToXML () {
        // فتح المستند
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        com.aspose.pdf.facades.Form form=new com.aspose.pdf.facades.Form();
        form.bindPdf(document);
        File file=new File(fileStorage, "output.xml");
        try {
            // إنشاء ملف xml.
            FileOutputStream xmlOutputStream;
            xmlOutputStream=new FileOutputStream(file.toString());
            // تصدير البيانات
            form.exportXml(xmlOutputStream);

            // إغلاق تدفق الملف
            xmlOutputStream.close();
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // إغلاق المستند
        form.dispose();
    }
```


## تصدير البيانات إلى FDF من ملف PDF

لتصدير بيانات النماذج من PDF إلى ملف XFDF، يمكننا استخدام طريقة [exportFdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportFdf-java.io.OutputStream-) في فئة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form).

يرجى ملاحظة أن هذه فئة من `com.aspose.pdf.facades`. على الرغم من الاسم المشابه، فإن لهذه الفئة غرضًا مختلفًا قليلاً.

من أجل تصدير البيانات إلى FDF، تحتاج إلى إنشاء كائن من فئة `Form` ومن ثم استدعاء طريقة `exportXfdf` باستخدام كائن `OutputStream`. يوضح لك مقتطف الشيفرة التالي كيفية تصدير البيانات إلى ملف XFDF.

```java
public void extractFormExportFDF () {
        // فتح المستند
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        File file=new File(fileStorage, "student.fdf");

        com.aspose.pdf.facades.Form form=new com.aspose.pdf.facades.Form(document);
        FileOutputStream fdfOutputStream;
        try {

            fdfOutputStream=new FileOutputStream(file.toString());

            // تصدير البيانات
            form.exportFdf(fdfOutputStream);

            // إغلاق تدفق الملف
            fdfOutputStream.close();

        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


## تصدير البيانات إلى XFDF من ملف PDF

لتصدير بيانات نماذج PDF إلى ملف XFDF، يمكننا استخدام طريقة [exportXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportXfdf-java.io.OutputStream-) في فئة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form).

من أجل تصدير البيانات إلى XFDF، تحتاج إلى إنشاء كائن من فئة `Form` ثم استدعاء طريقة `exportXfdf` باستخدام كائن `OutputStream`. 
يظهر لك مقتطف الكود التالي كيفية تصدير البيانات إلى ملف XFDF.

```java
    public void extractFormExportXFDF () {
        // فتح المستند
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        File file=new File(fileStorage, "student.xfdf");

        com.aspose.pdf.facades.Form form=new com.aspose.pdf.facades.Form(document);
        FileOutputStream fdfOutputStream;
        try {

            fdfOutputStream=new FileOutputStream(file.toString());

            // تصدير البيانات
            form.exportXfdf(fdfOutputStream);

            // إغلاق تدفق الملف
            fdfOutputStream.close();

        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```