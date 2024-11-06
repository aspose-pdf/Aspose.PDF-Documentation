---
title: Get Resolution and Dimensions of Embedded Images using C++
linktitle: Get Resolution and Dimensions
type: docs
weight: 40
url: ar/cpp/get-resolution-and-dimensions-of-embedded-images/
description: تعرض هذه القسم تفاصيل حول الحصول على الدقة والأبعاد للصور المضمنة
lastmod: "2021-12-18"
---

تشرح هذه الموضوع كيفية استخدام فئات المشغل في مساحة الأسماء Aspose.PDF التي توفر القدرة على الحصول على معلومات الدقة والأبعاد حول الصور دون الحاجة إلى استخراجها.

هناك طرق مختلفة لتحقيق ذلك. يشرح هذا المقال كيفية استخدام `arraylist` و [فئات وضع الصورة](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement).

1. أولاً، قم بتحميل ملف PDF المصدر (مع الصور).
1. ثم قم بإنشاء كائن ArrayList للاحتفاظ بأسماء أي صور في الوثيقة.
1. احصل على الصور باستخدام خاصية Page.Resources.Images.
1. قم بإنشاء كائن مكدس للاحتفاظ بحالة الرسومات للصورة واستخدمه لتتبع حالات الصور المختلفة.
1. 
إنشاء كائن ConcatenateMatrix الذي يحدد التحويل الحالي. يدعم أيضًا تغيير الحجم، التدوير، وتشويه أي محتوى. يدمج المصفوفة الجديدة مع السابقة. يُرجى ملاحظة أنه لا يمكننا تحديد التحويل من الصفر ولكن فقط تعديل التحويل الحالي.  
1. نظرًا لأننا يمكننا تعديل المصفوفة باستخدام ConcatenateMatrix، قد نحتاج أيضًا إلى العودة إلى حالة الصورة الأصلية. استخدم [عامل التشغيل GSave](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_save/) و[عامل التشغيل GRestore](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_restore/). يتم اقتران هذه العوامل لذا يجب استدعاؤها معًا. على سبيل المثال، إذا قمت ببعض الأعمال الرسومية مع تحويلات معقدة وأخيراً إعادة التحويلات إلى الحالة الأولية، سيكون النهج شيئًا مثل هذا:

يوضح لك مقتطف الشيفرة التالي كيفية الحصول على أبعاد الصورة ودقتها دون استخراج الصورة من مستند PDF.

```cpp
void WorkingWithImages::GetResolutionAndDimensionsOfEmbeddedImages()
{
    String _dataDir("C:\\Samples\\");
    // تحميل ملف PDF المصدر
    auto document = MakeObject<Document>(_dataDir + u"ImageInformation.pdf");

    // تعريف الدقة الافتراضية للصورة
    int defaultResolution = 72;
    auto graphicsState = MakeObject<System::Collections::Generic::Stack<System::SmartPtr<object>>>();
    // تعريف كائن قائمة المصفوفة الذي سيحتفظ بأسماء الصور
    auto imageNames = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->get_Names();

    // إدخال كائن إلى المكدس
    graphicsState->Push(System::DynamicCast<object>(MakeObject<System::Drawing::Drawing2D::Matrix>(1, 0, 0, 1, 0, 0)));

    // الحصول على جميع العوامل في الصفحة الأولى من المستند
    for (auto op : document->get_Pages()->idx_get(1)->get_Contents())
    {
        // استخدام عوامل التشغيل GSave/GRestore لإعادة التحويلات إلى التي تم ضبطها مسبقًا
        auto opSaveState = System::DynamicCast<Aspose::Pdf::Operators::GSave>(op);
        auto opRestoreState = System::DynamicCast<Aspose::Pdf::Operators::GRestore>(op);

        // إنشاء كائن ConcatenateMatrix حيث يحدد مصفوفة التحويل الحالية.
        auto opCtm = System::DynamicCast<Aspose::Pdf::Operators::ConcatenateMatrix>(op);

        // إنشاء عامل Do الذي يرسم الكائنات من الموارد. يرسم الكائنات Form والكائنات Image
        auto opDo = System::DynamicCast<Aspose::Pdf::Operators::Do>(op);

        if (opSaveState != nullptr)
        {
            // حفظ الحالة السابقة ودفع الحالة الحالية إلى أعلى المكدس
            graphicsState->Push(System::DynamicCast<System::Drawing::Drawing2D::Matrix>(graphicsState->Peek())->Clone());
        }
        else if (opRestoreState != nullptr)
        {
            // التخلص من الحالة الحالية واستعادة الحالة السابقة
            graphicsState->Pop();
        }
        else if (opCtm != nullptr)
        {
            auto cm = MakeObject<System::Drawing::Drawing2D::Matrix>(
                (float)opCtm->get_Matrix()->get_A(),
                (float)opCtm->get_Matrix()->get_B(),
                (float)opCtm->get_Matrix()->get_C(),
                (float)opCtm->get_Matrix()->get_D(),
                (float)opCtm->get_Matrix()->get_E(),
                (float)opCtm->get_Matrix()->get_F());

            // مضاعفة المصفوفة الحالية مع مصفوفة الحالة
            System::DynamicCast<System::Drawing::Drawing2D::Matrix>(graphicsState->Peek())->Multiply(cm);
            continue;
        }
        else if (opDo != nullptr)
        {
            // في حالة كان هذا عامل رسم الصور
            if (imageNames->Contains(opDo->get_Name()))
            {
                auto lastCTM = System::DynamicCast<System::Drawing::Drawing2D::Matrix>(graphicsState->Peek());
                // إنشاء كائن XImage للاحتفاظ بالصور في الصفحة الأولى من pdf
                auto image = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->idx_get(opDo->get_Name());

                // الحصول على أبعاد الصورة
                double scaledWidth = Math::Sqrt(Math::Pow(lastCTM->get_Elements()->idx_get(0), 2) + Math::Pow(lastCTM->get_Elements()->idx_get(1), 2));
                double scaledHeight = Math::Sqrt(Math::Pow(lastCTM->get_Elements()->idx_get(2), 2) + Math::Pow(lastCTM->get_Elements()->idx_get(3), 2));
                // الحصول على معلومات الطول والعرض للصورة
                double originalWidth = image->get_Width();
                double originalHeight = image->get_Height();

                // حساب الدقة بناءً على المعلومات أعلاه
                double resHorizontal = originalWidth * defaultResolution / scaledWidth;
                double resVertical = originalHeight * defaultResolution / scaledHeight;

                // عرض معلومات الأبعاد والدقة لكل صورة
                Console::Write(_dataDir);
                Console::Write(u" image {0} ({1:.##}:{2:.##}): res {3:.##} x {4:.##}",
                    opDo->get_Name(), scaledWidth, scaledHeight, resHorizontal, resVertical);
            }
        }
    }
}
```
```