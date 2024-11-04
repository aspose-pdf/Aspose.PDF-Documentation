---
title: Insert an Image into a Table Cell in PDF
type: docs
weight: 20
url: /java/insert-an-image-into-a-table-cell-in-pdf/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

الجداول هي عناصر مهمة لعرض البيانات. إنها توفر تنسيقًا قابلاً للعرض لتمثيل البيانات. غالبًا ما تُستخدم الجداول لعرض المعلومات الرقمية. توفر Aspose.PDF API فئة، Table، التي تتيح لك القدرة على إنشاء الجداول في ملف PDF.

بدلاً من إنشاء جدول بسيط، يمكنك تعيين خيارات تنسيق مختلفة، على سبيل المثال نمط حدود الجدول، معلومات الهوامش، المحاذاة، لون الخلفية، عرض العمود، معلومات العنوان، قيمة الصفوف التي سيتم تكرارها في كل صفحة والعديد من الخيارات الأخرى.

{{% /alert %}}

## نهج Aspose.PDF

وفقًا لنموذج DOM (نموذج كائن المستند) الخاص بنا، يتكون المستند من صفحات.
 صفحة تحتوي على فقرة واحدة أو أكثر، وقد تكون الفقرة صورة، نص، حقل نموذج، عنوان، مربع عائم، رسم بياني، مرفق، أو جدول. الجدول، بدوره، يحتوي على مجموعة من الصفوف وكل صف يحتوي على مجموعة من الخلايا. الخلية هي مجموعة من الفقرات.

لذا وفقًا لنموذج DOM الخاص بنا، يمكن لخلية الجدول أن تحتوي على أي من عناصر الفقرة المحددة أعلاه، بما في ذلك الصور.

## فهم عرض الخلية

يجب أن يكون لديك فهم واضح لعرض الخلية، خاصة عند عرض صورة في خلية جدول، بحيث يتم تثبيت عرض الصورة على عرض الخلية لتظهر بشكل صحيح. يمكن تحديد عرض الصورة باستخدام طريقة setFixedWidth() لفئة Image.

## مثال على الشيفرة

```java

 String dataDir = "C:\\temp\\";

// إنشاء كائن Document عن طريق استدعاء المنشئ الفارغ له

Document pdfDocument = new Document();

// إنشاء صفحة في كائن المستند

com.aspose.pdf.Page page = pdfDocument.getPages().add();



// إنشاء كائن جدول

Table table = new Table();

// إضافة الجدول في مجموعة الفقرات للصفحة المطلوبة

page.getParagraphs().add(table);

// تعيين عرض الأعمدة للجدول

table.setColumnWidths("100 100 120");



// تعيين حدود الجدول باستخدام كائن BorderInfo المخصص الآخر

table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 1F));



// إنشاء كائن صورة في الصفحة

com.aspose.pdf.Image img1 = new com.aspose.pdf.Image();

// تعيين مسار ملف الصورة

img1.setFile(dataDir + "logo.jpg");



img1.setFixWidth(100);

img1.setFixHeight(100);

// إنشاء صفوف في الجدول ثم خلايا في الصفوف

Row row1 = table.getRows().add();

row1.getCells().add("نص تجريبي في الخلية");

// إضافة الخلية التي تحتوي على الصورة

Cell cell2 = row1.getCells().add();

// إضافة الصورة إلى خلية الجدول

cell2.getParagraphs().add(img1);



row1.getCells().add("الخلية السابقة مع الصورة");

row1.getCells().get_Item(2).setVerticalAlignment(VerticalAlignment.Center);



// حفظ المستند

pdfDocument.save(dataDir + "Image_in_Cell.pdf");    

```