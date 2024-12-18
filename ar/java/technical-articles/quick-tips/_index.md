---
title: نصائح سريعة
type: docs
weight: 50
url: /ar/java/quick-tips/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

تحتوي هذه الصفحة على بعض النصائح السريعة المتعلقة بـ Aspose.PDF لـ Java API

{{% /alert %}}

## إضافة JavaScript إلى PDF

يمكن استخدام جزء الشيفرة التالي لتعيين/إضافة JavaScript إلى ملف PDF.

```java

String path = "D:\\";
String fileOut = path + "JavaScript.pdf";
IDocument document = null;
try
{

    document = new Document();
    document.getPages().add();
    document.getPages().add();

    //إضافة JavaScript على مستوى المستند
    //إنشاء JavascriptAction مع العبارات JavaScript المطلوبة
    JavascriptAction javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

    //تعيين كائن JavascriptAction إلى الإجراء المطلوب في المستند
    document.setOpenAction(javaScript);
    document.setOpenAction(new JavascriptAction("app.alert('Hello PDF')"));

    //إضافة JavaScript على مستوى الصفحة
    document.getActions().setBeforeClosing(new JavascriptAction("app.alert('document is closing')"));

    document.getPages().get_Item(1).getActions().setOnOpen(new JavascriptAction("app.alert('page 1 is opened')"));

    document.getPages().get_Item(2).getActions().setOnOpen(new JavascriptAction("app.alert('page 2 is opened')"));

    document.getPages().get_Item(2).getActions().setOnClose(new JavascriptAction("app.alert('page 2 is closed')"));

    document.save(fileOut);

}
finally { if (document != null) document.dispose(); document = null; }

```


**بعض الأمثلة الإضافية**

```java

// بعد الطباعة
document.getActions().setAfterPrinting(new JavascriptAction("app.alert('تمت طباعة الملف')"));

// بعد الحفظ
document.getActions().setAfterSaving(new JavascriptAction("app.alert('تم حفظ الملف')"));


```

## تحرير الذاكرة المستخدمة

إذا كنت قد أكملت العمل مع Aspose.PDF لـ Java وتريد تحرير الذاكرة من مثيلات ثابتة مختلفة، لجعل الذاكرة القصوى متاحة لعمليات أخرى، يجب عليك تنفيذ سطر الكود التالي:

```java

 com.aspose.pdf.MemoryCleaner.clear();

```

## تحميل PDF من ByteArrayInputStream

يظهر الكود التالي خطوات تحميل ملف PDF إلى ByteArray ثم إنشاء كائن Document باستخدام ByteArrayInputStream.

```java

 // ملف PDF المصدر

java.io.File file = new java.io.File("c:/pdftest/result.pdf");

java.io.FileInputStream fis = new java.io.FileInputStream(file);

//System.out.println(file.exists() + "!!");

//InputStream in = resource.openStream();

java.io.ByteArrayOutputStream bos = new java.io.ByteArrayOutputStream();

byte[] buf = new byte[1024];

try {

    for (int readNum; (readNum = fis.read(buf)) != -1;) {

        bos.write(buf, 0, readNum); //لا شك هنا هو 0

        //يكتب len بايت من المصفوفة البايت المحددة بدءًا من الإزاحة off إلى دفق إخراج المصفوفة البايت هذا.

        System.out.println("تم قراءة " + readNum + " بايت،");

    }

} catch (java.io.IOException ex) {


}

byte[] bytes = bos.toByteArray();

// إنشاء كائن Document باستخدام ByteArrayInputStream أثناء تمرير مصفوفة البايت كوسيط

com.aspose.pdf.Document doc = new 
com.aspose.pdf.Document(new java.io.ByteArrayInputStream(bytes));

// الحصول على عدد الصفحات في ملف PDF

 System.out.println(doc.getPages().size());

```


## حفظ ملف PDF إلى ByteArrayOutputStream

يوضح مقتطف الشيفرة التالي الخطوات اللازمة لحفظ ملف PDF الناتج في ByteArrayOutputStream.

```java

 com.aspose.pdf.Document pdfDocument = new 
com.aspose.pdf.Document("source.pdf");

java.io.InputStream is = null;

java.io.ByteArrayOutputStream os = new java.io.ByteArrayOutputStream();

try{

pdfDocument.save(os,com.aspose.pdf.SaveFormat.Doc);

System.out.println(os.size());

is = new java.io.ByteArrayInputStream(os.toByteArray());

            os.close();

            os.flush();

pdfDocument.close();

}catch (Throwable e) {}

```