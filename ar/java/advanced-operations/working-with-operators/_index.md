---
title: العمل مع مشغلي PDF في Java
linktitle: العمل مع المشغلين
type: docs
weight: 90
url: /java/working-with-operators/
description: تعرف على كيفية استخدام عوامل تشغيل PDF ذات المستوى المنخفض في Java لمعالجة دفق المحتوى، ووضع الصور، وإعادة استخدام XForm، وتنظيف الرسومات.
lastmod: "2026-06-25"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استخدم عوامل تشغيل PDF ذات المستوى المنخفض للتحكم في تدفق المحتوى في Java
Abstract: تشرح هذه المقالة كيفية العمل مع عوامل تشغيل PDF ذات المستوى المنخفض في Aspose.PDF لـ Java. تعرف على كيفية وضع الصور بدقة، ورسم محتوى XForm القابل لإعادة الاستخدام، وإزالة عوامل تشغيل الرسوم من صفحات PDF.
---
## مقدمة لمشغلي PDF واستخداماتهم

عامل التشغيل عبارة عن كلمة أساسية بتنسيق PDF تحدد بعض الإجراءات التي يجب تنفيذها، مثل رسم شكل رسومي على الصفحة. تتميز الكلمة الأساسية للمشغل عن كائن مسمى بغياب حرف Solidus الأولي (2Fh). العوامل ذات معنى فقط داخل تدفق المحتوى.

تدفق المحتوى هو كائن دفق PDF تتكون بياناته من تعليمات تصف العناصر الرسومية التي سيتم رسمها على الصفحة. يمكن العثور على مزيد من التفاصيل حول عوامل تشغيل PDF في [مواصفات PDF](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

استخدم هذه الصفحة عندما تحتاج إلى التحكم المباشر في تدفق محتوى PDF في Java، مثل وضع صورة باستخدام مصفوفة رياضية صريحة، أو إعادة استخدام نفس الرسم عدة مرات من خلال XForm، أو حذف تعليمات الرسم ذات المستوى المنخفض من الصفحة.

## أضف صورة باستخدام عوامل تشغيل PDF

استخدم عوامل التشغيل ذات المستوى المنخفض عندما يجب التحكم في موضع الصورة بدقة على مستوى دفق المحتوى بدلاً من التحكم من خلال واجهات برمجة تطبيقات التخطيط ذات المستوى الأعلى.

1. افتح ملف PDF المصدر باستخدام [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) واحصل على [الصفحة] المستهدفة (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. أضف دفق صورة الإدخال إلى موارد الصفحة واحتفظ باسم المورد الذي تم إرجاعه.
1. قم بإنشاء [مستطيل](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) يحدد المنطقة المستهدفة وقم ببناء [مصفوفة](https://reference.aspose.com/pdf/java/com.aspose.pdf/matrix/) من حدودها.
1. استخدم [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/gsave/) للحفاظ على حالة الرسومات الحالية، و[ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/concatenatematrix/) لتحديد موضع الصورة، و[Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/do/) لطلائها، و[GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/grestore/) لاستعادة الحالة السابقة.
1. احفظ مستند PDF المحدث.

```java
public static void addImageUsingPdfOperators(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        Page page = document.getPages().get_Item(1);
        String imageName = page.getResources().getImages().add(imageStream);

        Rectangle rectangle = new Rectangle(100, 100, 200, 200, true);
        Matrix matrix = new Matrix(new double[]{
                rectangle.getURX() - rectangle.getLLX(),
                0,
                0,
                rectangle.getURY() - rectangle.getLLY(),
                rectangle.getLLX(),
                rectangle.getLLY()
        });

        page.getContents().add(new GSave());
        page.getContents().add(new ConcatenateMatrix(matrix));
        page.getContents().add(new Do(imageName));
        page.getContents().add(new GRestore());
        document.save(outputFile.toString());
    }
    System.out.println("Image added with PDF operators to " + outputFile);
}
```

## ارسم محتوى XForm قابلاً لإعادة الاستخدام على الصفحة

استخدم هذا الأسلوب عندما يجب عرض نفس الصورة أو الرسم أكثر من مرة دون تكرار المورد في ملف PDF.

1. افتح ملف PDF المصدر باستخدام [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)، واحصل على [الصفحة] المستهدفة(https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)، وقم بالوصول إلى [OperatorCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/operatorcollection/).
1. قم بتغليف محتويات الصفحة الحالية باستخدام [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/gsave/) و[GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/grestore/) حتى لا تتسرب التحويلات اللاحقة إلى تدفق المحتوى الأصلي.
1. قم بإنشاء مورد [XForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/)، وأضف الصورة إلى موارد النموذج، واستخدم [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/concatenatematrix/) بالإضافة إلى [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/do/) لرسم الصورة داخل النموذج.
1. ضع نفس النموذج في إحداثيات صفحات متعددة عن طريق إضافة مصفوفة ترجمة وتنفيذ اسم النموذج باستخدام عامل التشغيل `Do`.
1. قم باستعادة حالة الرسومات وحفظ ملف PDF الناتج.

```java
public static void drawXFormOnPage(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        Page page = document.getPages().get_Item(1);
        OperatorCollection pageContents = page.getContents();

        pageContents.insert(1, new GSave());
        pageContents.add(new GRestore());
        pageContents.add(new GSave());

        XForm form = XForm.createNewForm(page, document);
        page.getResources().getForms().add(form);

        form.getContents().add(new GSave());
        form.getContents().add(new ConcatenateMatrix(200, 0, 0, 200, 0, 0));
        String imageName = form.getResources().getImages().add(imageStream);
        form.getContents().add(new Do(imageName));
        form.getContents().add(new GRestore());

        addFormAt(pageContents, form.getName(), 100, 500);
        addFormAt(pageContents, form.getName(), 100, 300);

        pageContents.add(new GRestore());
        document.save(outputFile.toString());
    }
    System.out.println("XForm drawn on page in " + outputFile);
}

private static void addFormAt(OperatorCollection pageContents, String formName, double x, double y) {
    pageContents.add(new GSave());
    pageContents.add(new ConcatenateMatrix(1, 0, 0, 1, x, y));
    pageContents.add(new Do(formName));
    pageContents.add(new GRestore());
}
```

## قم بإزالة عوامل تشغيل الرسومات من الصفحة

استخدم هذا المثال عندما تحتوي الصفحة على عوامل رسم متجهة يجب إزالتها مباشرةً من تدفق المحتوى.

1. افتح ملف PDF المصدر باستخدام [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) واحصل على [الصفحة] المستهدفة (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. كرر من خلال عوامل تشغيل محتوى الصفحة واجمع مثيلات [Stroke](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/stroke/)، و[ClosePathStroke](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/closepathstroke/)، و[Fill](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/fill/).
1. احذف عوامل التشغيل المجمعة من محتويات الصفحة واحفظ ملف PDF المحدث.

تقوم هذه التقنية بإزالة تعليمات الرسم المستهدفة فقط. إذا كانت الصفحة تحتوي أيضًا على تسميات نصية ذات صلة أو عوامل تشغيل أخرى غير رسومية، فستظل هذه العناصر في تدفق المحتوى وقد تحتاج إلى تصريح تنظيف منفصل.

```java
public static void removeGraphicsObjects(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        List<Operator> operatorsToRemove = new ArrayList<>();
        for (Object item : page.getContents()) {
            Operator operator = (Operator) item;
            if (operator instanceof Stroke || operator instanceof ClosePathStroke || operator instanceof Fill) {
                operatorsToRemove.add(operator);
            }
        }
        page.getContents().delete(operatorsToRemove);
        document.save(outputFile.toString());
    }
    System.out.println("Graphics operators removed in " + outputFile);
}
```

## موضوعات ذات صلة

- [عمليات PDF المتقدمة في Java](/pdf/java/advanced-operations/)
- [التعامل مع الصور في ملف PDF باستخدام Java](/pdf/java/working-with-images/)
- [العمل مع صفحات PDF في Java](/pdf/java/working-with-pages/)
- [العمل باستخدام الرسومات المتجهة في Java](/pdf/java/working-with-vector-graphics/)
