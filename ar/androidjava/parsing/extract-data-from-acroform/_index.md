---
title:  استخراج البيانات من AcroForm
linktitle:  استخراج البيانات من AcroForm
type: docs
weight: 50
url: /ar/androidjava/extract-data-from-acroform/
description: توجد AcroForms في العديد من مستندات PDF. يهدف هذا المقال إلى مساعدتك في فهم كيفية استخراج البيانات من AcroForms باستخدام Aspose.PDF.
lastmod: "2026-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## استخراج حقول النموذج من مستند PDF

لا يتيح Aspose.PDF for Android عبر Java فقط إنشاء وملء حقول النموذج، بل يجعل من السهل أيضًا استخراج بيانات حقول النموذج أو معلومات حقول النموذج من ملفات PDF.

لنفترض أننا لا نعرف أسماء حقول النموذج مسبقًا. ثم يجب أن نتنقل عبر كل صفحة في PDF لاستخراج المعلومات حول جميع AcroForms في PDF بالإضافة إلى قيم حقول النموذج. للوصول إلى النموذج نحتاج إلى استخدام [getForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--) طريقة.

```java
 public void extractFormFields () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Get values from all fields
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

إذا كنت تعرف اسم حقول النموذج التي تريد استخراج القيم منها، يمكنك استخدام الفهرس في مجموعة Documents.Form لاسترجاع هذه البيانات بسرعة.

## استرجع قيمة حقل النموذج حسب العنوان

تسمح لك الخاصية Value لحقل النموذج بالحصول على قيمة حقل معين. للحصول على القيمة، احصل على حقل النموذج من الـ [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) الكائن [مجموعة حقول النموذج](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--). يختار هذا المثال [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) ويسترجع قيمتها باستخدام [getValue](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) طريقة.

```java

    public void extractFormDataByName () {
        // Open document
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

تسمح لك فئة Form بتصدير البيانات إلى ملف XML من ملف PDF باستخدام طريقة ExportXml. من أجل تصدير البيانات إلى XML، تحتاج إلى إنشاء كائن من فئة Form ثم استدعاء طريقة ExportXml باستخدام كائن FileStream. أخيراً، يمكنك إغلاق كائن FileStream وإتلاف كائن Form. يُظهر مقتطف الشفرة التالي كيفية تصدير البيانات إلى ملف XML.

```java
public void extractFormFieldsToXML () {
        // Open document
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
            // Create xml file.
            FileOutputStream xmlOutputStream;
            xmlOutputStream=new FileOutputStream(file.toString());
            // Export data
            form.exportXml(xmlOutputStream);

            // Close file stream
            xmlOutputStream.close();
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Close the document
        form.dispose();
    }
```

## تصدير البيانات إلى FDF من ملف PDF

لتصدير بيانات نماذج PDF إلى ملف XFDF، يمكننا استخدام [exportFdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportFdf-java.io.OutputStream-) طريقة في الـ [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) فئة.

يرجى ملاحظة، أن هذه فئة من `com.aspose.pdf.facades`. على الرغم من الاسم المتشابه، فإن هذه الفئة لها هدف مختلف قليلاً.

من أجل تصدير البيانات إلى FDF، تحتاج إلى إنشاء كائن من `Form` الفئة ثم استدعاء `exportXfdf` طريقة باستخدام الـ `OutputStream` كائن. يوضح مقطع التعليمات البرمجية التالي كيفية تصدير البيانات إلى ملف XFDF.

```java
public void extractFormExportFDF () {
        // Open document
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

            // Export data
            form.exportFdf(fdfOutputStream);

            // Close file stream
            fdfOutputStream.close();

        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## تصدير البيانات إلى XFDF من ملف PDF

لتصدير بيانات نماذج PDF إلى ملف XFDF، يمكننا استخدام [exportXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportXfdf-java.io.OutputStream-) طريقة في الـ [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) فئة.

من أجل تصدير البيانات إلى XFDF، تحتاج إلى إنشاء كائن من `Form` الفئة ثم استدعاء `exportXfdf` طريقة باستخدام الـ `OutputStream` كائن. 
توضح لك موجزة الشيفرة التالية كيفية تصدير البيانات إلى ملف XFDF.

```java
    public void extractFormExportXFDF () {
        // Open document
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

            // Export data
            form.exportXfdf(fdfOutputStream);

            // Close file stream
            fdfOutputStream.close();

        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

