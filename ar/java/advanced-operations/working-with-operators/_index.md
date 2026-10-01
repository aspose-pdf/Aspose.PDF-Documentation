---
title: العمل مع مشغلات PDF في Java
linktitle: العمل مع المشغلات
type: docs
weight: 90
url: /ar/java/working-with-operators/
description: تعرف على كيفية استخدام مشغلات PDF منخفضة المستوى في Java لتعديل تدفق المحتوى، وضع الصور، إعادة استخدام XForm، وتنظيف الرسومات.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استخدم مشغلات PDF منخفضة المستوى للتحكم في تدفق المحتوى في Java
Abstract: تشرح هذه المقالة كيفية العمل مع عوامل PDF منخفضة المستوى في Aspose.PDF for Java. تعلّم كيفية وضع الصور بدقة، ورسم محتوى XForm قابل لإعادة الاستخدام، وإزالة عوامل الرسوم من صفحات PDF.
---
## مقدمة عن عوامل PDF واستخدامها

العامل هو كلمة مفتاح في PDF تحدد إجراءً يجب تنفيذّه، مثل رسم شكل رسومي على الصفحة. تُميز كلمة مفتاح العامل عن كائن مسمى بغياب حرف المائلة الأول (2Fh). تكون العوامل ذات معنى فقط داخل تدفق المحتوى.

تدفق المحتوى هو كائن تدفق PDF يتكون بياناته من تعليمات تصف العناصر الرسومية التي ستُرسم على الصفحة. يمكن العثور على مزيد من التفاصيل حول عوامل PDF في [مواصفات PDF](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

استخدم هذه الصفحة عندما تحتاج إلى التحكم المباشر في تدفق محتوى PDF في Java، مثل وضع صورة بحسابات مصفوفة صريحة، أو إعادة استخدام نفس الرسم عدة مرات عبر XForm، أو حذف تعليمات الرسم منخفضة المستوى من صفحة.

## إضافة صورة باستخدام عوامل PDF

استخدم العوامل منخفضة المستوى عندما يجب التحكم بدقة في وضع الصورة على مستوى content-stream بدلاً من خلال APIs تخطيط عالية المستوى.

1. افتح ملف PDF المصدر باستخدام [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) واحصل على الهدف [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. أضف تدفق الصورة الإدخالية إلى موارد الصفحة واحتفظ باسم المورد المعاد.
1. إنشاء [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) الذي يحدد المنطقة المستهدفة ويُنشئ [Matrix](https://reference.aspose.com/pdf/java/com.aspose.pdf/matrix/) من حدوده.
1. استخدام [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/gsave/) لحفظ حالة الرسومات الحالية، [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/concatenatematrix/) لوضع الصورة، [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/do/) لتلوينه، و [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/grestore/) لإعادة الحالة السابقة.
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

## رسم محتوى XForm القابل لإعادة الاستخدام على صفحة

استخدم هذا النهج عندما يجب عرض نفس الصورة أو الرسم البياني أكثر من مرة دون تكرار المورد في ملف PDF.

1. افتح ملف PDF المصدر باستخدام [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/), احصل على الهدف [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/), والوصول إلى الخاص به [OperatorCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/operatorcollection/).
1. غلف محتويات الصفحة الحالية بـ [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/gsave/) و [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/grestore/) حتى لا تتسرب التحولات اللاحقة إلى تدفق المحتوى الأصلي.
1. إنشاء [XForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/) المورد، أضف الصورة إلى موارد النموذج، واستخدم [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/concatenatematrix/) زائد [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/do/) لرسم الصورة داخل النموذج.
1. ضع النموذج نفسه عند إحداثيات صفحات متعددة عن طريق إضافة مصفوفة تحويل وتنفيذ اسم النموذج مع `Do` المشغل.
1. استعد حالة الرسومات واحفظ ملف PDF الناتج.

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

## إزالة عمليات الرسومات من صفحة

استخدم هذا المثال عندما تحتوي الصفحة على عوامل رسم متجهية يجب إزالتها مباشرةً من تدفق المحتوى.

1. افتح ملف PDF المصدر باستخدام [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) واحصل على الهدف [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. المرور عبر مشغّلات محتوى الصفحة وجمع نماذج من [Stroke](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/stroke/), [ClosePathStroke](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/closepathstroke/)، و [Fill](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/fill/).
1. احذف المشغلين المجمّعين من محتويات الصفحة واحفظ ملف PDF المحدث.

تزيل هذه التقنية تعليمات الرسم المستهدفة فقط. إذا كانت الصفحة تحتوي أيضًا على تسميات نصية ذات صلة أو عمليات تشغيل غير رسومية أخرى، فإن تلك العناصر تظل في تدفق المحتوى وقد تحتاج إلى إجراء تنظيف منفصل.

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

## المواضيع ذات الصلة

- [عمليات PDF المتقدمة في Java](/pdf/ar/java/advanced-operations/)
- [العمل مع الصور في PDF باستخدام Java](/pdf/ar/java/working-with-images/)
- [العمل مع صفحات PDF في Java](/pdf/ar/java/working-with-pages/)
- [العمل مع الرسومات المتجهة في جافا](/pdf/ar/java/working-with-vector-graphics/)
