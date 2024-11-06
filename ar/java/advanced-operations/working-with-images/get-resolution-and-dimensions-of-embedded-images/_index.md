---
title: احصل على دقة وأبعاد الصور المدمجة
linktitle: احصل على الدقة والأبعاد
type: docs
weight: 40
url: ar/java/get-resolution-and-dimensions-of-embedded-images/
description: يوضح هذا القسم تفاصيل الحصول على الدقة وأبعاد الصور المدمجة
lastmod: "2021-06-05"
---

يشرح هذا الموضوع كيفية استخدام فئات المشغل في مساحة الأسماء Aspose.PDF التي توفر القدرة على الحصول على معلومات الدقة والأبعاد حول الصور دون الحاجة إلى استخراجها.

هناك طرق مختلفة لتحقيق ذلك. يشرح هذا المقال كيفية استخدام `arraylist` وفئات [Image placement classes](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacement).

1. أولاً، قم بتحميل ملف PDF المصدر (مع الصور).
1. ثم قم بإنشاء كائن ArrayList لحفظ أسماء أي صور في المستند.
1. احصل على الصور باستخدام الخاصية Page.Resources.Images.
1. قم بإنشاء كائن stack لحفظ حالة الرسومات للصورة واستخدمه لمتابعة حالات الصور المختلفة.

1. قم بإنشاء كائن ConcatenateMatrix الذي يحدد التحويل الحالي. كما يدعم تكبير، تدوير، وإمالة أي محتوى. يقوم بدمج المصفوفة الجديدة مع السابقة. يرجى ملاحظة أننا لا يمكننا تحديد التحويل من البداية ولكن فقط تعديل التحويل الموجود.

1. لأننا يمكننا تعديل المصفوفة باستخدام ConcatenateMatrix، قد نحتاج أيضًا إلى العودة إلى حالة الصورة الأصلية. استخدم مشغلي GSave و GRestore. يتم إقران هذه المشغلين لذا يجب استدعاؤهما معًا. على سبيل المثال، إذا قمت ببعض الأعمال الرسومية باستخدام تحولات معقدة وأخيرًا تعيد التحولات إلى الحالة الأولية، فإن النهج سيكون شيئًا مثل هذا:

```java
// ارسم بعض النصوص
GSave

ConcatenateMatrix  // تدوير المحتويات بعد المشغل

// بعض الأعمال الرسومية

ConcatenateMatrix // تكبير (مع التدوير السابق) للمحتويات بعد المشغل

// بعض الأعمال الرسومية الأخرى

GRestore

// ارسم بعض النصوص
```

نتيجة لذلك، يتم رسم النص بشكل عادي ولكن يتم تنفيذ بعض التحولات بين مشغلي النص.
 من أجل عرض الصورة أو رسم كائنات النماذج والصور، نحتاج إلى استخدام المشغل Do.

لدينا أيضًا فئة تدعى XImage التي توفر خاصيتين، العرض والارتفاع، والتي يمكن استخدامها للحصول على أبعاد الصورة.

1. قم بإجراء بعض الحسابات لحساب دقة الصورة.
2. قم بعرض المعلومات في موجه الأوامر مع اسم الصورة.

يوضح لك مقتطف الشيفرة التالي كيفية الحصول على أبعاد الصورة ودقتها دون استخراج الصورة من وثيقة PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.operators.*;
import java.util.*;

public class ExampleImagesResolution {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ExampleAddPageNumber() 
    {
        // تحميل ملف PDF المصدر
        Document doc = new Document(_dataDir+ "ImageInformation.pdf");
        
        // تعريف الدقة الافتراضية للصورة
        int defaultResolution = 72;

        Stack<Object> graphicsState = new Stack<Object>();

        // تعريف كائن قائمة المصفوفة الذي سيحمل أسماء الصور
        List<String> imageNames = Arrays.asList(doc.getPages().get_Item(1).getResources().getImages().getNames());
        //ArrayList imageNames = new ArrayList<>(Arrays.asList(names));
        // إدراج كائن في المكدس
        graphicsState.push(new Matrix(1, 0, 0, 1, 0, 0));

        // الحصول على جميع المشغلين في الصفحة الأولى من الوثيقة
        for (Operator op : doc.getPages().get_Item(1).getContents())
        {
            // استخدام مشغلي GSave/GRestore لاستعادة التحويلات إلى ما تم تعيينه سابقًا
            GSave opSaveState = (GSave) op;
            GRestore opRestoreState = (GRestore) op;
            // إنشاء كائن ConcatenateMatrix حيث يحدد مصفوفة التحويل الحالي.
            ConcatenateMatrix opCtm = (ConcatenateMatrix) op;
            // إنشاء مشغل Do الذي يرسم الكائنات من الموارد. يرسم كائنات النماذج وكائنات الصورة
            Do opDo = (Do) op;

            if (opSaveState != null)
            {
                // حفظ الحالة السابقة ودفع الحالة الحالية إلى قمة المكدس
                Matrix m = new Matrix((Matrix)graphicsState.peek());
                graphicsState.push(m);
            }
            else if (opRestoreState != null)
            {
                // التخلص من الحالة الحالية واستعادة الحالة السابقة
                graphicsState.pop();
            }
            else if (opCtm != null)
            {
                Matrix cm = new Matrix(
                (float)opCtm.getMatrix().getA(),
                (float)opCtm.getMatrix().getB(),
                (float)opCtm.getMatrix().getC(),
                (float)opCtm.getMatrix().getD(),
                (float)opCtm.getMatrix().getE(),
                (float)opCtm.getMatrix().getF());

                // ضرب المصفوفة الحالية بمصفوفة الحالة
                ((Matrix)graphicsState.peek()).multiply(cm);

                continue;
            }
            else if (opDo != null)
            {
                // في حالة كان هذا مشغل رسم صورة
                if (imageNames.contains(opDo.getName()))
                {
                    Matrix lastCTM = (Matrix)graphicsState.peek();
                    // إنشاء كائن XImage لحمل صور الصفحة الأولى من pdf
                    XImage image = doc.getPages().get_Item(1).getResources().getImages().get_Item(opDo.getName());

                    // الحصول على أبعاد الصورة
                    double scaledWidth = Math.sqrt(Math.pow(lastCTM.getElements()[0], 2) + Math.pow(lastCTM.getElements()[1], 2));
                    double scaledHeight = Math.sqrt(Math.pow(lastCTM.getElements()[2], 2) + Math.pow(lastCTM.getElements()[3], 2));
                    // الحصول على معلومات الارتفاع والعرض للصورة
                    double originalWidth = image.getWidth();
                    double originalHeight = image.getHeight();

                    // حساب الدقة بناءً على المعلومات أعلاه
                    double resHorizontal = originalWidth * defaultResolution / scaledWidth;
                    double resVertical = originalHeight * defaultResolution / scaledHeight;

                    // عرض معلومات الأبعاد والدقة لكل صورة
                    System.out.printf(_dataDir + "image %s (%.2f:%.2f): res %.2f x %.2f",
                                        opDo.getName(), scaledWidth, scaledHeight, resHorizontal,
                                        resVertical);
                }
                // حفظ وثيقة الإخراج
                doc.save(_dataDir);
            }
        }
    }
}
```