---
title: استخراج البيانات من AcroForm
linktitle: استخراج البيانات من AcroForm
type: docs
weight: 50
url: /ar/java/extract-data-from-acroform/
description: توجد AcroForms في العديد من مستندات PDF. يهدف هذا المقال إلى مساعدتك على فهم كيفية استخراج البيانات من AcroForms باستخدام Java وAspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## استخراج حقول النموذج من مستند PDF

Aspose.PDF for Java لا يتيح لك فقط إنشاء وملء حقول النموذج، ولكنه يسهل أيضًا استخراج بيانات الحقول أو معلومات الحقول من ملفات PDF.

افترض أننا لا نعرف أسماء حقول النموذج مسبقًا. ثم يجب علينا التكرار على كل صفحة في PDF لاستخراج معلومات حول جميع AcroForms في PDF وكذلك قيم حقول النموذج. للوصول إلى النموذج نحتاج لاستخدام طريقة [getForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--).

```java
public static void ExtractFormFields() {
    String path= "/home/admin/pdf-examples/Samples/StudentInfoFormElectronic.pdf";
    com.aspose.pdf.Document document = new com.aspose.pdf.Document(path);
    // الحصول على القيم من جميع الحقول
    for (com.aspose.pdf.Field formField : document.getForm().getFields()) {
        System.out.println("Field Name :" + formField.getPartialName());
        System.out.println("Value : " + formField.getValue());
    }
}
```


إذا كنت تعرف أسماء حقول النموذج التي ترغب في استخراج القيم منها، يمكنك استخدام الفهرس في مجموعة Documents.Form لاسترجاع هذه البيانات بسرعة.

## استرجاع قيمة حقل النموذج حسب العنوان

تسمح لك خاصية القيمة في حقل النموذج بالحصول على قيمة حقل معين. للحصول على القيمة، قم بالحصول على حقل النموذج من [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) في [مجموعة حقول النموذج](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--). هذا المثال يختار [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) ويسترجع قيمته باستخدام طريقة [getValue](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--).

```java
public static void ExtractFormDataByName() {
    String fileName = _dataDir+"/StudentInfoFormElectronic.pdf";
    com.aspose.pdf.Document document = new com.aspose.pdf.Document(fileName);        
    com.aspose.pdf.TextBoxField textBoxField1 = (com.aspose.pdf.TextBoxField)document.getForm().get("Last Name");

    System.out.println("Last Name :" + textBoxField1.getValue());
}
```


## استخراج حقول النموذج من مستند PDF إلى JSON

لتصدير بيانات النموذج إلى JSON، نوصي باستخدام مكتبة خارجية مثل [Gson](https://github.com/google/gson).
يظهر المقتطف التالي كيفية تصدير `Name` و `Value` إلى JSON:

```java
public static void ExtractFormFieldsToJson() {
    String path = "/home/admin/pdf-examples/Samples/StudentInfoFormElectronic.pdf";
    com.aspose.pdf.Document document = new com.aspose.pdf.Document(path);

    java.util.List<FormElement> formData = new java.util.ArrayList<FormElement>();
    for (com.aspose.pdf.Field formField : document.getForm().getFields()) {
        formData.add(new FormElement(formField.getPartialName(), formField.getValue()));
    }

    Gson gson = new Gson();
    String jsonString = gson.toJson(formData);
    System.out.println(jsonString);
}
```

في هذا المثال استخدمنا فئة إضافية

```java
public class FormElement {
    public FormElement(String partialName, String Value) {
        this.Name = partialName;
        this.Value = Value;
    }
    public String Name;
    public String Value;
}
```


## استخراج البيانات إلى XML من ملف PDF

تسمح لك فئة النموذج بتصدير البيانات إلى ملف XML من ملف PDF باستخدام طريقة ExportXml. من أجل تصدير البيانات إلى XML، تحتاج إلى إنشاء كائن من فئة النموذج ثم استدعاء طريقة ExportXml باستخدام كائن FileStream. أخيرًا، يمكنك إغلاق كائن FileStream والتخلص من كائن النموذج. يوضح لك مقطع الشيفرة التالي كيفية تصدير البيانات إلى ملف XML.

```java
public static void ExtractFormFieldsToXML() {

    String dataDir = "/home/admin/pdf-examples/Samples/StudentInfoFormElectronic.pdf";

    // فتح المستند
    com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form();
    form.bindPdf(dataDir + "input.pdf");

    try {
        // إنشاء ملف XML.
        FileOutputStream xmlOutputStream;

        xmlOutputStream = new FileOutputStream(dataDir + "input.xml");
        // تصدير البيانات
        form.exportXml(xmlOutputStream);

        // إغلاق تدفق الملف
        xmlOutputStream.close();

    } catch (IOException e) {

        e.printStackTrace();
    }

    // إغلاق المستند
    form.dispose();
    ;
}
```


## تصدير البيانات إلى FDF من ملف PDF

لتصدير بيانات النماذج من PDF إلى ملف XFDF، يمكننا استخدام الطريقة [exportFdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportFdf-java.io.OutputStream-) في فئة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form).

يرجى ملاحظة أن هذه الفئة من `com.aspose.pdf.facades`. على الرغم من تشابه الاسم، إلا أن لهذه الفئة غرضًا مختلفًا قليلاً.

من أجل تصدير البيانات إلى FDF، تحتاج إلى إنشاء كائن من فئة `Form` ثم استدعاء طريقة `exportXfdf` باستخدام كائن `OutputStream`. يوضح لك مقطع الكود التالي كيفية تصدير البيانات إلى ملف XFDF.

```java
 public static void ExtractFormExportFDF() {
        String pdfFileName = Paths.get(_dataDir, "StudentInfoFormElectronic.pdf").toString();
        String fdfFileName = Paths.get(_dataDir, "student.fdf").toString();
        com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form(pdfFileName);

        OutputStream fdfOutputStream;
        try {

            fdfOutputStream = new FileOutputStream(fdfFileName);

            // تصدير البيانات
            form.exportFdf(fdfOutputStream);

            // إغلاق تدفق الملف
            fdfOutputStream.close();

        } catch (IOException e) {
            // TODO: التعامل مع الاستثناء
            e.printStackTrace();
        }

    }
```


## تصدير البيانات إلى XFDF من ملف PDF

لتصدير بيانات النماذج في PDF إلى ملف XFDF، يمكننا استخدام الطريقة [exportXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportXfdf-java.io.OutputStream-) في فئة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form).

لكي تقوم بتصدير البيانات إلى XFDF، تحتاج إلى إنشاء كائن من فئة `Form` ومن ثم استدعاء طريقة `exportXfdf` باستخدام كائن `OutputStream`.
يعرض لك مقتطف الشيفرة البرمجية التالي كيفية تصدير البيانات إلى ملف XFDF.

```java
public static void ExtractFormExportXFDF() {
        String pdfFileName = Paths.get(_dataDir, "StudentInfoFormElectronic.pdf").toString();
        String fdfFileName = Paths.get(_dataDir, "student.xfdf").toString();
        com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form(pdfFileName);

        OutputStream fdfOutputStream;
        try {

            fdfOutputStream = new FileOutputStream(fdfFileName);

            // تصدير البيانات
            form.exportXfdf(fdfOutputStream);

            // إغلاق تدفق الملف
            fdfOutputStream.close();

        } catch (IOException e) {
            // TODO: التعامل مع الاستثناء
            e.printStackTrace();
        }
    }
```