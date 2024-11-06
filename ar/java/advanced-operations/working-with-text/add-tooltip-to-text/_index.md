---
title: استخدام التلميح
linktitle: PDF Tooltip
type: docs
weight: 20
url: ar/java/pdf-tooltip/
description: تعلم كيفية إضافة تلميح إلى جزء من النص في PDF باستخدام Java وAspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## إضافة تلميح للنص المُبحَث بإضافة زر غير مرئي

غالبًا ما يكون من الضروري إضافة بعض التفاصيل لعبارة أو كلمة معينة كتلميح في مستند PDF بحيث يظهر عندما يحوم المستخدم بمؤشر الفأرة فوق النص. يوفر Aspose.PDF for Java هذه الميزة لإنشاء تلميحات بإضافة زر غير مرئي فوق النص المُبحَث. سيوضح لك مقتطف الشيفرة التالي كيفية تحقيق هذه الوظيفة:

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.ButtonField;
import com.aspose.pdf.Document;
import com.aspose.pdf.TextFragment;
import com.aspose.pdf.TextFragmentAbsorber;
import com.aspose.pdf.TextFragmentCollection;

public class ExampleToolTip {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddToolTip() {
        String outputFile = _dataDir + "Tooltip_out.pdf";

        // إنشاء مستند عينة مع نص
        Document doc = new Document();
        doc.getPages().add().getParagraphs().add(new TextFragment("حرك مؤشر الفأرة هنا لعرض تلميح"));
        doc.getPages().get_Item(1).getParagraphs().add(new TextFragment("حرك مؤشر الفأرة هنا لعرض تلميح طويل جدًا"));
        doc.save(outputFile);

        // فتح المستند مع النص
        Document document = new Document(outputFile);
        // إنشاء كائن TextAbsorber للعثور على جميع العبارات المطابقة للتعبير النمطي
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("حرك مؤشر الفأرة هنا لعرض تلميح");
        // قبول الـ Absorber لصفحات المستند
        document.getPages().accept(absorber);
        // الحصول على أجزاء النص المستخرجة
        TextFragmentCollection textFragments = absorber.getTextFragments();

        // تكرار خلال الأجزاء
        for(TextFragment fragment : textFragments)
        {
            // إنشاء زر غير مرئي على موضع جزء النص
            ButtonField field = new ButtonField(fragment.getPage(), fragment.getRectangle());
            // قيمة AlternateName ستظهر كتلميح بواسطة تطبيق العارض
            field.setAlternateName ("تلميح للنص.");
            // إضافة حقل الزر إلى المستند
            document.getForm().add(field);
        }

        // التالي سيكون مثال لتلميح طويل جدًا
        absorber = new TextFragmentAbsorber("حرك مؤشر الفأرة هنا لعرض تلميح طويل جدًا");
        document.getPages().accept(absorber);
        textFragments = absorber.getTextFragments();

        for(TextFragment fragment : textFragments)
        {
            ButtonField field = new ButtonField(fragment.getPage(), fragment.getRectangle());
            // تعيين نص طويل جدًا
            field.setAlternateName ("Lorem ipsum dolor sit amet, consectetur adipiscing elit," +
                                    " sed do eiusmod tempor incididunt ut labore et dolore magna" +
                                    " aliqua. Ut enim ad minim veniam, quis nostrud exercitation" +
                                    " ullamco laboris nisi ut aliquip ex ea commodo consequat." +
                                    " Duis aute irure dolor in reprehenderit in voluptate velit" +
                                    " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint" +
                                    " occaecat cupidatat non proident, sunt in culpa qui officia" +
                                    " deserunt mollit anim id est laborum.");
            document.getForm().add(field);
        }

        // حفظ المستند
        document.save(outputFile);
    }
}
```


{{% alert color="primary" %}}

بالنسبة لطول التلميح، يتم احتواء نص التلميح في مستند PDF كنوع سلسلة PDF، خارج تدفق المحتوى. لا يوجد تقييد فعلي على مثل هذه السلاسل في ملفات PDF (انظر ملحق مرجع PDF C.). ومع ذلك، فإن القارئ المتوافق (مثل Adobe Acrobat) الذي يعمل على معالج معين وفي بيئة تشغيل معينة لديه مثل هذا الحد. يرجى الرجوع إلى وثائق تطبيق قارئ PDF الخاص بك.

{{% /alert %}}

## إنشاء كتلة نصية مخفية وعرضها عند مرور الفأرة

في Aspose.PDF، يتم تنفيذ ميزة إخفاء الإجراءات والتي من خلالها يمكن إظهار/إخفاء حقل مربع النص (أو أي نوع آخر من التعليقات التوضيحية) عند دخول/خروج الفأرة فوق زر غير مرئي. لهذا الغرض، يتم استخدام فئة Aspose.Pdf.Annotations.HideAction لتعيين إجراء الإخفاء/الإظهار للكتلة النصية. يرجى استخدام مقتطف الشيفرة التالي لإظهار/إخفاء كتلة نصية عند دخول/خروج الفأرة.

يرجى أيضًا مراعاة أن الإجراءات في مستندات PDF تعمل بشكل جيد في القراء المتوافقين (مثل
 Adobe Reader) ولكن لا توجد ضمانات للقراء الآخرين لملفات PDF (مثل إضافات متصفحات الويب). لقد قمنا بإجراء تحقيق موجز ووجدنا:

- جميع عمليات تنفيذ إجراء الإخفاء في مستندات PDF تعمل بشكل جيد في Internet Explorer v.11.0.
- جميع عمليات تنفيذ إجراء الإخفاء تعمل أيضًا في Opera v.12.14، لكن لاحظنا بعض التأخير في الاستجابة عند فتح المستند لأول مرة.
- فقط التنفيذ باستخدام منشئ HideAction الذي يقبل اسم الحقل يعمل إذا كان Google Chrome v.61.0 يتصفح المستند؛ يرجى استخدام المنشئات المقابلة إذا كان التصفح في Google Chrome مهمًا:

>buttonField.Actions.OnEnter = new HideAction(floatingField.FullName, false);
>buttonField.Actions.OnExit = new HideAction(floatingField.FullName);

```java
    public static void name() {
        String outputFile = _dataDir + "TextBlock_HideShow_MouseOverOut_out.pdf";

        // إنشاء مستند نموذجي مع نص
        Document doc = new Document();
        doc.getPages().add().getParagraphs().add(new TextFragment("حرك مؤشر الماوس هنا لعرض النص العائم"));
        doc.save(outputFile);

        // فتح المستند مع النص
        Document document = new Document(outputFile);
        // إنشاء كائن TextAbsorber للعثور على جميع العبارات المطابقة للتعبير العادي
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("حرك مؤشر الماوس هنا لعرض النص العائم");
        // قبول الماص للصفحات المستند
        document.getPages().accept(absorber);
        // الحصول على أول جزء نص مستخرج
        TextFragmentCollection textFragments = absorber.getTextFragments();
        TextFragment fragment = textFragments.get_Item(1);

        // إنشاء حقل نصي مخفي للنص العائم في المستطيل المحدد للصفحة
        TextBoxField floatingField = new TextBoxField(fragment.getPage(), new Rectangle(100, 700, 220, 740));
        // تعيين النص ليعرض كقيمة للحقل
        floatingField.setValue ("هذا هو \"حقل النص العائم\".");
        // نوصي بجعل الحقل 'للقراءة فقط' لهذا السيناريو
        floatingField.setReadOnly(true);

        // تعيين العلم 'المخفي' لجعل الحقل غير مرئي عند فتح المستند
        floatingField.setFlags( floatingField.getFlags() | AnnotationFlags.Hidden);

        // تعيين اسم فريد للحقل ليس ضروريًا ولكنه مسموح
        floatingField.setPartialName ("FloatingField_1");

        // تعيين خصائص ظهور الحقل ليس ضروريًا ولكنه يجعله أفضل
        DefaultAppearance da = new DefaultAppearance("Helvetica", 16, java.awt.Color.RED);
        floatingField.setDefaultAppearance(da);
        //new DefaultAppearance("Helv", 10, Color.getBlue()
        floatingField.getCharacteristics().setBackground(Color.getLightBlue());
        floatingField.getCharacteristics().setBorder(Color.getDarkBlue());;
        floatingField.setBorder(new Border(floatingField));
        floatingField.getBorder().setWidth(1);
        floatingField.setMultiline(true);

        // إضافة الحقل النصي إلى المستند
        document.getForm().add(floatingField);

        // إنشاء زر غير مرئي في موضع جزء النص
        Field buttonField = new ButtonField(fragment.getPage(), fragment.getRectangle());
        // إنشاء إجراء إخفاء جديد للحقل المحدد (التعليق) وعلم عدم الرؤية.
        // (يمكنك أيضًا الإشارة إلى الحقل العائم بالاسم إذا حددته أعلاه.)
        // إضافة الإجراءات عند دخول/خروج الماوس في حقل الزر غير المرئي
        buttonField.getActions().setOnEnter(new HideAction(floatingField, false));
        buttonField.getActions().setOnExit (new HideAction(floatingField));

        // إضافة حقل الزر إلى المستند
        document.getForm().add(buttonField);

        // حفظ المستند
        document.save(outputFile);
    }
```