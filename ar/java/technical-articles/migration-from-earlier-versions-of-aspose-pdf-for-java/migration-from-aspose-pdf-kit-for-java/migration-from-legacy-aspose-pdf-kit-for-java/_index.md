---
title: Migration from legacy Aspose.Pdf.Kit for Java
type: docs
weight: 10
url: ar/java/migration-from-legacy-aspose-pdf-kit-for-java/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

يوفر المكون الحالي Aspose.PDF.Kit for Java ميزات لمعالجة ملفات PDF الموجودة. ومع ذلك، في وقت قريب سيتم إيقاف هذا المكون كمنتج منفصل لأننا قمنا بنقل جميع فئاته وتعداداته تحت حزمة **com.aspose.pdf.facades** من الإصدار الجديد المحول تلقائيًا من Aspose.PDF for Java (4.x.x). الآن يوفر هذا الإصدار المحول تلقائيًا الفردي القدرات لإنشاء وكذلك معالجة ملفات PDF الموجودة.

{{% /alert %}}

## دعم للرمز القديم

خلال نشاط الانتقال بأكمله، لقد أخذنا بالتأكيد في الاعتبار تأثير هذا النشاط على العملاء الحاليين وحاولنا بذل قصارى جهدنا للحد من هذا التأثير قدر الإمكان.
 علاوة على ذلك، لقد ركزنا أيضًا على جعل الإصدار الجديد المنقول تلقائيًا متوافقًا مع الإصدارات السابقة بحيث تتطلب قاعدة الكود للعملاء الحاليين تغييرات طفيفة. حتى وإن كان الإصدار الجديد المنقول تلقائيًا يوفر نموذج كائن المستند (DOM) تحت حزمة com.aspose.pdf لإنشاء وكذلك معالجة ملفات PDF الموجودة، ولكن إذا كنت تود الاستمرار في استخدام كودك القديم المطور باستخدام Aspose.PDF.Kit لـ Java، تحتاج فقط إلى استيراد حزمة **com.aspose.pdf.facades** ويجب أن يعمل كودك (*باستثناء تحديث مراجع الفئات الصريحة*).

يظهر لك المقتطف التالي من الكود كيفية تشغيل كود Aspose.PDF.Kit لـ Java الحالي مع Aspose.PDF الجديد المنقول تلقائيًا لـ Java.

```java

import com.aspose.pdf.facades.*;

public class template {

    public static void main(String[] args) {

        try{

            // تحميل ملف PDF الحالي

            com.aspose.pdf.facades.PdfFileInfo fileInfo = new com.aspose.pdf.facades.PdfFileInfo("input.pdf");

            System.out.println("العنوان: " + fileInfo.getTitle());

            System.out.println("المؤلف:" + fileInfo.getAuthor());

            System.out.println("تاريخ الإنشاء:" + fileInfo.getCreationDate());

            System.out.println("المنشئ:" + fileInfo.getCreator());

            System.out.println("الكلمات المفتاحية:" + fileInfo.getKeywords());

            System.out.println("تاريخ التعديل:" + fileInfo.getModDate());

           }


catch(Exception ex)


{System.out.println(ex);}


}

}
```

## استخدام فئة ReplaceTextStrategy

من أجل ترحيل الشيفرة لفئة ReplaceTextStrategy، تم تحديث الطريقة **setScope(..)** إلى **setReplaceScope(..)**. يرجى الاطلاع على مقطع الشيفرة التالي.

```java

 // إنشاء كائن PdfContentEditor

com.aspose.pdf.facades.PdfContentEditor editor = new com.aspose.pdf.facades.PdfContentEditor();

// ربط ملف PDF المصدر

editor.bindPdf("input.pdf");

// إنشاء استراتيجية استبدال النص

com.aspose.pdf.facades.ReplaceTextStrategy strategy = new com.aspose.pdf.facades.ReplaceTextStrategy();

// تعيين المحاذاة لاستبدال النص

strategy.setAlignment(com.aspose.pdf.facades.AlignmentType.Left);

// النطاق لاستبدال النص

strategy.setReplaceScope(com.aspose.pdf.facades.ReplaceTextStrategy.Scope.REPLACE_ALL);

// تعيين استراتيجية الاستبدال

editor.setReplaceTextStrategy(strategy);

editor.replaceText("test","replaced");

// حفظ الملف المحدث

editor.save("TxtReplaceTest.pdf");
```