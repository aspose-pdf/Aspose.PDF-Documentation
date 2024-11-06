---
title: العمل مع العوامل
linktitle: العمل مع العوامل
type: docs
weight: 170
url: ar/java/operators/
description: يشرح هذا الموضوع كيفية استخدام العوامل مع Aspose.PDF. توفر فئات العوامل ميزات رائعة لتعديل PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## مقدمة لعوامل PDF واستخدامها

العامل هو كلمة مفتاحية في PDF تحدد بعض الإجراءات التي يجب تنفيذها، مثل رسم شكل بياني على الصفحة. يتم تمييز كلمة العامل المفتاحية عن الكائنات المسماة بعدم وجود حرف سلاش في البداية (2Fh). تكون العوامل ذات معنى فقط داخل تيار المحتوى.

تيار المحتوى هو كائن تيار PDF تتكون بياناته من تعليمات تصف العناصر الرسومية التي سيتم رسمها على صفحة. يمكن العثور على مزيد من التفاصيل حول عوامل PDF في [مواصفات PDF](https://www.adobe.com/devnet/pdf/pdf_reference.html).

### تفاصيل التنفيذ

يشرح هذا الموضوع كيفية استخدام العوامل مع Aspose.PDF.
 تم إضافة المثال المختار صورة إلى ملف PDF لتوضيح المفهوم. لإضافة صورة في ملف PDF، هناك حاجة إلى مشغلين مختلفين. يستخدم هذا المثال [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave)، [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/ConcatenateMatrix)، [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/Do)، و[GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore).

- يقوم المشغل [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave) بحفظ الحالة الرسومية الحالية لملف PDF.
- يشرح هذا الموضوع كيفية استخدام المشغلين مع Aspose.PDF. المثال المحدد يضيف صورة إلى ملف PDF لتوضيح المفهوم. لإضافة صورة في ملف PDF، هناك حاجة إلى مشغلين مختلفين. يستخدم هذا المثال [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave)، [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/ConcatenateMatrix)، [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/Do)، و [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore). 

المشغل (concatenate matrix) يُستخدم لتحديد كيفية وضع الصورة على صفحة PDF.
- المشغل [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/Do) يرسم الصورة على الصفحة.
- المشغل [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore) يستعيد الحالة الرسومية.

لإضافة صورة إلى ملف PDF:

1. قم بإنشاء كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) وافتح مستند PDF المدخل.
1. احصل على الصفحة المحددة التي سيتم إضافة الصورة إليها.
1. أضف الصورة إلى مجموعة الموارد الخاصة بالصفحة.
1. استخدم المشغلين لوضع الصورة على الصفحة:
   - أولاً، استخدم المشغل [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave) لحفظ الحالة الرسومية الحالية.
   - ثم استخدم المشغل [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/ConcatenateMatrix) لتحديد مكان وضع الصورة.
   - استخدم المشغل [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/Do) لرسم الصورة على الصفحة.
1. أخيرًا، استخدم المشغل [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore) لحفظ الحالة الرسومية المحدثة.

يظهر المقتطف البرمجي التالي كيفية استخدام مشغلي PDF.

```java
public class WorkingWithOperators {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Operators/";

    public static void AddImageUsingOpeartors() {

        // إنشاء مستند PDF جديد
        Document pdfDocument = new Document(_dataDir + "PDFOperators.pdf");

        // احصل على الصفحة التي تحتاج إلى إضافة الصورة إليها
        Page page = pdfDocument.getPages().get_Item(1);

        // تعيين الإحداثيات
        int lowerLeftX = 100;
        int lowerLeftY = 100;
        int upperRightX = 200;
        int upperRightY = 200;

        // تحميل الصورة إلى الدفق
        FileInputStream imageStream = null;
        try {
            imageStream = new FileInputStream(_dataDir + "PDFOperators.jpg");
        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

        // إضافة الصورة إلى مجموعة الصور في موارد الصفحة
        page.getResources().getImages().add(imageStream);

        // استخدام مشغل GSave: هذا المشغل يحفظ حالة الرسوميات الحالية
        page.getContents().add(new GSave());
        // إنشاء كائنات Rectangle وMatrix
        Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0,
                rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });

        // استخدام مشغل ConcatenateMatrix (دمج المصفوفة): يحدد كيفية وضع الصورة
        page.getContents().add(new ConcatenateMatrix(matrix));

        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());
        // استخدام مشغل Do: هذا المشغل يرسم الصورة
        page.getContents().add(new Do(ximage.getName()));
        // استخدام مشغل GRestore: هذا المشغل يعيد حالة الرسوميات
        page.getContents().add(new GRestore());

        // حفظ المستند المحدث
        pdfDocument.save(_dataDir + "PDFOperators_out.pdf");
    }
```


## رسم XForm على الصفحة باستخدام المشغلين

يوضح هذا الموضوع كيفية استخدام المشغلين GSave/GRestore، ومشغل ContatenateMatrix لتحديد موضع xForm ومشغل Do لرسم xForm على الصفحة.

يلف الكود أدناه المحتويات الحالية لملف PDF مع زوج المشغلين GSave/GRestore. تساعد هذه الطريقة في الحصول على حالة الرسوم الأولية في نهاية المحتويات الحالية. بدون هذه الطريقة، قد تبقى التحولات غير المرغوب فيها في نهاية سلسلة المشغلين الحالية.

```java
    public static void DrawXFormUsingOpeartors() {
        String imageFile = _dataDir + "aspose-logo.jpg";
        String inFile = _dataDir + "DrawXFormOnPage.pdf";
        String outFile = _dataDir + "blank-sample2_out.pdf";

        Document pdfDocument = new Document(inFile);
        OperatorCollection pageContents = pdfDocument.getPages().get_Item(1).getContents();

        // يوضح المثال
        // استخدام المشغلين GSave/GRestore
        // استخدام مشغل ContatenateMatrix لتحديد موضع xForm
        // استخدام مشغل Do لرسم xForm على الصفحة

        // لف المحتويات الحالية مع زوج المشغلين GSave/GRestore
        // هذا للحصول على حالة الرسوم الأولية في نهاية المحتويات الحالية
        // وإلا قد تبقى بعض التحولات غير المرغوب فيها في نهاية
        // سلسلة المشغلين الحالية
        pageContents.insert(1, new GSave());
        pageContents.add(new GRestore());

        // إضافة مشغل حفظ حالة الرسوم لتنظيف حالة الرسوم بشكل صحيح بعد
        // الأوامر الجديدة
        pageContents.add(new GSave());

        // إنشاء xForm
        XForm form = XForm.createNewForm(pdfDocument.getPages().get_Item(1), pdfDocument);
        pdfDocument.getPages().get_Item(1).getResources().getForms().add(form);
        form.getContents().add(new GSave());

        // تحديد عرض وارتفاع الصورة
        form.getContents().add(new ConcatenateMatrix(200, 0, 0, 200, 0, 0));

        // تحميل الصورة في التدفق
        FileInputStream imageStream = null;
        try {
            imageStream = new FileInputStream(imageFile);
        } catch (FileNotFoundException e) {
            // TODO معالجة كتلة استثناء
            e.printStackTrace();
        }

        // إضافة الصورة إلى مجموعة Images في موارد XForm
        form.getResources().getImages().add(imageStream);
        XImage ximage = form.getResources().getImages().get_Item(form.getResources().getImages().size());
        // باستخدام مشغل Do: هذا المشغل يرسم الصورة
        form.getContents().add(new Do(ximage.getName()));
        form.getContents().add(new GRestore());

        pageContents.add(new GSave());
        // وضع النموذج في الإحداثيات x=100 y=500
        pageContents.add(new ConcatenateMatrix(1, 0, 0, 1, 100, 500));
        // رسم النموذج باستخدام مشغل Do
        pageContents.add(new Do(form.getName()));
        pageContents.add(new GRestore());

        pageContents.add(new GSave());

        // وضع النموذج في الإحداثيات x=100 y=300
        pageContents.add(new ConcatenateMatrix(1, 0, 0, 1, 100, 300));

        // رسم النموذج باستخدام مشغل Do
        pageContents.add(new Do(form.getName()));
        pageContents.add(new GRestore());

        // استعادة حالة الرسوم باستخدام GRestore بعد GSave
        pageContents.add(new GRestore());
        pdfDocument.save(outFile);
    }
```


## إزالة كائنات الرسومات باستخدام فئات المشغل

توفر فئات المشغل ميزات رائعة لمعالجة ملفات PDF. عندما يحتوي ملف PDF على رسومات لا يمكن إزالتها باستخدام طريقة [DeleteImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#deleteImage--) الخاصة بفئة [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor)، يمكن استخدام فئات المشغل لإزالتها بدلاً من ذلك.

يوضح مقتطف الشيفرة التالي كيفية إزالة الرسومات. يرجى ملاحظة أنه إذا كان ملف PDF يحتوي على تسميات نصية للرسومات، فقد تظل موجودة في ملف PDF، باستخدام هذا النهج. لذلك ابحث عن مشغلات الرسومات للحصول على طريقة بديلة لحذف هذه الصور.

```java
    public static void RemoveGraphicsOpeartors() {
        Document pdfDocument  = new Document(_dataDir+ "RemoveGraphicsObjects.pdf");
        Page page = pdfDocument.getPages().get_Item(2);
        OperatorCollection oc = page.getContents();

        // مشغلات رسم المسارات المستخدمة
        Operator[] operators = new Operator[] {
                new Stroke(),
                new ClosePathStroke(),
                new Fill()
        };

        oc.delete(operators);
        pdfDocument.save(_dataDir+ "No_Graphics_out.pdf");
    }
```


## تغيير فضاء الألوان في مستند PDF

{{% alert color="primary" %}}

يدعم Aspose.PDF for Java 9.0.0 تغيير فضاء الألوان في مستند PDF. من الممكن تغيير اللون RGB إلى CMYK والعكس بالعكس.

{{% /alert %}}

تم تنفيذ الأساليب التالية في فئة [Operator](https://reference.aspose.com/java/pdf/com.aspose.pdf/Operator) للسماح لك بتغيير فضاء الألوان. استخدمه لتغيير بعض الألوان المحددة من RGB/CMYK إلى فضاء الألوان CMYK/RGB، مع الحفاظ على باقي مستند PDF كما هو.

{{% alert color="primary" %}}
**تغييرات API العامة**
تم تنفيذ الأساليب التالية:

- com.aspose.pdf.Operator.SetRGBColorStroke.getCMYKColor(new double[3], new double[4])
- com.aspose.pdf.Operator.SetRGBColor.getCMYKColor(new double[3], new double[4])
- com.aspose.pdf.Operator.SetCMYKColorStroke.getRGBColor(new double[4], new double[3])
- com.aspose.pdf.Operator.SetCMYKColor.getRGBColor(new double[4], new double[3])

{{% /alert %}}

يوضح مقتطف الكود التالي كيفية تغيير فضاء الألوان باستخدام Aspose.PDF for Java.

```java
Document doc = new Document("input_color.pdf");
OperatorCollection contents = doc.getPages().get_Item(1).getContents();
System.out.println("قيم مشغلي ألوان RGB في وثيقة pdf");
for (int j = 1; j <= contents.size(); j++) {
    Operator oper = contents.get_Item(j);
    if (oper instanceof Operator.SetRGBColor || oper instanceof Operator.SetRGBColorStroke)
        try {
            // تحويل RGB إلى لون CMYK
            System.out.println(oper.toString());

            double[] rgbFloatArray = new double[] { Double.valueOf(oper.getParameters().get(0).toString()), Double.valueOf(oper.getParameters().get(1).toString()), Double.valueOf(oper.getParameters().get(2).toString()), };
            double[] cmyk = new double[4];
            if (oper instanceof Operator.SetRGBColor) {
                ((Operator.SetRGBColor) oper).getCMYKColor(rgbFloatArray, cmyk);
                contents.set_Item(j, new Operator.SetCMYKColor(cmyk[0], cmyk[1], cmyk[2], cmyk[3]));
            } else if (oper instanceof Operator.SetRGBColorStroke) {
                ((Operator.SetRGBColorStroke) oper).getCMYKColor(rgbFloatArray, cmyk);
                contents.set_Item(j, new Operator.SetCMYKColorStroke(cmyk[0], cmyk[1], cmyk[2], cmyk[3]));
            } else
                throw new java.lang.Throwable("أمر غير مدعوم");

        } catch (Throwable e) {
            e.printStackTrace();
        }
}
doc.save("input_colorout.pdf");

// اختبار النتيجة
System.out.println("قيم مشغلي ألوان CMYK المحولة في وثيقة pdf الناتجة");
doc = new Document("input_colorout.pdf");
contents = doc.getPages().get_Item(1).getContents();
for (int j = 1; j <= contents.size(); j++) {
    Operator oper = contents.get_Item(j);
    if (oper instanceof Operator.SetCMYKColor || oper instanceof Operator.SetCMYKColorStroke) {
        System.out.println(oper.toString());
    }
}
```