---
title: تحسين PDF باستخدام C++
linktitle: تحسين PDF
type: docs
weight: 30
url: /cpp/optimize-pdf/
description: تحسين ملف PDF، تقليص جميع الصور، تقليل حجم PDF، إزالة تضمين الخطوط، تمكين إعادة استخدام محتوى الصفحة، إزالة أو تسطيح التعليقات التوضيحية باستخدام C++.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

أولاً وقبل كل شيء، أي تحسين تقوم به لملفات PDF هو من أجل المستخدم. في ملفات PDF، يتمثل تحسين المستخدم بشكل كبير في تقليل حجم ملفات PDF الخاصة بك من أجل زيادة سرعة تحميلها. هذه هي المهمة الأكثر شيوعًا.
يمكننا استخدام عدة تقنيات لتحسين PDF، ولكن الأهم:

- تحسين محتوى الصفحة للتصفح عبر الإنترنت
- تقليص أو ضغط جميع الصور
- تمكين إعادة استخدام محتوى الصفحة
- دمج التدفقات المكررة
- إزالة تضمين الخطوط
- إزالة الكائنات غير المستخدمة
- إزالة أو تسطيح حقول النماذج
- إزالة أو تسطيح التعليقات التوضيحية

## تحسين مستند PDF للويب

عندما تواجه مهمة تحسين محتوى مستند PDF الخاص بك للحصول على ترتيب أفضل في محركات البحث، فإن Aspose.PDF for C++ لديه الحل.

1. افتح مستند الإدخال في كائن [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. استخدم طريقة [Optimize](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a04d95824c334f5e543c13f69a19d9cda).
1. احفظ المستند المحسّن باستخدام طريقة Save.

يعرض مقطع الشيفرة التالي كيفية تحسين مستند PDF للويب.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
// تحسين مستند PDF للويب
void OptimizeForWeb() {
    // سلسلة لمسار الاسم
    String _dataDir("C:\\Samples\\");

    // سلسلة لاسم ملف الإدخال
    String outfilename("OptimizeDocument_out.pdf");

    // فتح المستند
    auto document = MakeObject<Document>();

    // قم بتنفيذ بعض العمليات (إضافة صفحات، صور، إلخ)
    // ...

    // تحسين للويب
    document->Optimize();

    // حفظ المستند الناتج
    document->Save(_dataDir + outfilename);
}
```

## تقليل حجم PDF

تسمح لك طريقة [OptimizeResources()](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#aea33aac69a42423efb82bcdb359f2ec6) بتقليل حجم المستند عن طريق إزالة المعلومات غير الضرورية. بشكل افتراضي، تعمل هذه الطريقة كما يلي:

- تتم إزالة الموارد غير المستخدمة في صفحات المستند
- يتم دمج الموارد المتساوية في كائن واحد
- يتم حذف الكائنات غير المستخدمة

المقتطف أدناه هو مثال. لاحظ، مع ذلك، أن هذه الطريقة لا يمكن أن تضمن تقليص المستند.

```cpp
void ReduceSizePDF() {

    // String for path name
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String outfilename("ShrinkDocument_out.pdf");

    // Open document
    auto document = MakeObject<Document>();
    // Make some operations (add pages, images, etc) 
    // ...

    // Optimize PDF document. Note, though, that this method cannot guarantee document shrinking 
    document->OptimizeResources();

    // Save output document
    document->Save(_dataDir + outfilename);
}
```

## إدارة استراتيجية التحسين

يمكننا أيضًا تخصيص استراتيجية التحسين. حاليًا، تستخدم طريقة [OptimizeResources()](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#aea33aac69a42423efb82bcdb359f2ec6) خمس تقنيات. يمكن تطبيق هذه التقنيات باستخدام طريقة OptimizeResources() مع معلمة [OptimizationOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document.optimization_options/).

### تقليص أو ضغط جميع الصور

لتحسين الصور في مستند PDF الخاص بك، سنستخدم [Aspose.Pdf.Optimization](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.optimization). لحل مشكلة تحسين الصور، لدينا الخيارات التالية: تقليل جودة الصورة و/أو تغيير دقتها. في أي حال، يجب تطبيق [ImageCompressionOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options/). في المثال التالي، نقوم بتصغير الصور عن طريق تقليل [ImageQuality](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#a92ee855b042a6b310984b4966ea7154e) إلى 50.

```cpp
void CompressImage() {
    // سلسلة لمسار الاسم
    String _dataDir("C:\\Samples\\");

    // سلسلة لاسم الملف المدخل
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // فتح الوثيقة
    auto document = MakeObject<Document>(_dataDir + infilename);

    // تهيئة خيارات التحسين
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // تعيين خيار ضغط الصور
    optimizationOptions->get_ImageCompressionOptions()->set_CompressImages(true);
    // تعيين خيار جودة الصورة
    optimizationOptions->get_ImageCompressionOptions()->set_ImageQuality(50);

    // تحسين وثيقة PDF باستخدام خيارات التحسين
    document->OptimizeResources(optimizationOptions); 
    // حفظ الوثيقة المحدثة
    document->Save(_dataDir + outfilename);
}
```
لضبط الصورة عند دقة أقل، قم بتعيين [ResizeImages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#a0e5aad7e140ee380c09ebbb8a5238ff6) إلى true و [MaxResolution](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#a05a4d1ace23ef074b3dc203cb213755e) إلى القيمة المقابلة.

```cpp
void ResizeImagesWithLowerResolution() {
    // سلسلة لاسم المسار
    String _dataDir("C:\\Samples\\");

    // سلسلة لاسم الملف المدخل
    String infilename("ResizeImage.pdf");
    String outfilename("ResizeImages_out.pdf");

    // فتح المستند
    auto document = MakeObject<Document>(_dataDir + infilename);

    // تهيئة خيارات التحسين
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // تعيين خيار ضغط الصور
    optimizationOptions->get_ImageCompressionOptions()->set_CompressImages(true);
    // تعيين خيار جودة الصورة
    optimizationOptions->get_ImageCompressionOptions()->set_ImageQuality(75);

    // تعيين خيار تغيير حجم الصور
    optimizationOptions->get_ImageCompressionOptions()->set_ResizeImages(true);
    // تعيين خيار الدقة القصوى
    optimizationOptions->get_ImageCompressionOptions()->set_MaxResolution(300);

    // تحسين مستند PDF باستخدام خيارات التحسين
    document->OptimizeResources(optimizationOptions);
    // حفظ المستند المحدث
    document->Save(_dataDir + outfilename);
}
```

Aspose.PDF for C++ يمنحك أيضًا التحكم في إعدادات وقت التشغيل. اليوم، يمكننا استخدام خوارزميتين - القياسية والسريعة. للتحكم في وقت التنفيذ يجب علينا تعيين خاصية [Version](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#aa2f1d93725ce56f8fabe692152bbf3a4).

المقطع التالي يوضح خوارزمية السريعة:

```cpp
void ResizeImagesWithLowerResolutionFast() {
    auto time = System::DateTime::get_Now().get_Ticks();
    // سلسلة لأسم المسار
    String _dataDir("C:\\Samples\\");

    // سلسلة لأسم الملف المدخل
    String infilename("ResizeImage.pdf");
    String outfilename("ResizeImages_out.pdf");

    // فتح المستند
    auto document = MakeObject<Document>(_dataDir + infilename);

    // تهيئة خيارات التحسين
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // تعيين خيار CompressImages
    optimizationOptions->get_ImageCompressionOptions()->set_CompressImages(true);
    // تعيين خيار ImageQuality
    optimizationOptions->get_ImageCompressionOptions()->set_ImageQuality(75);

    // تعيين خيار ResizeImage
    optimizationOptions->get_ImageCompressionOptions()->set_ResizeImages(true);
    // تعيين إصدار ضغط الصورة إلى السريع
    optimizationOptions->get_ImageCompressionOptions()->set_Version (Aspose::Pdf::Optimization::ImageCompressionVersion::Fast);

    // تحسين مستند PDF باستخدام خيارات التحسين
    document->OptimizeResources(optimizationOptions);
    // حفظ المستند المحدث
    document->Save(_dataDir + outfilename);
    std::cout << "Ticks: " << System::DateTime::get_Now().get_Ticks() - time << std::endl;
}
```

### إزالة الكائنات غير المستخدمة

في بعض الأحيان قد تحتاج إلى إزالة بعض الكائنات غير المستخدمة من مستند PDF الخاص بك والتي لم يتم الإشارة إليها في الصفحات. قد يحدث هذا، على سبيل المثال، عندما تتم إزالة صفحة من شجرة صفحات المستند ولكن لم تتم إزالة كائن الصفحة نفسه. إزالة هذه الكائنات لا يجعل المستند غير صالح بل يجعله أصغر حجمًا. تحقق من الشيفرة التالية:

```cpp
void RemovingUnusedObject() { 
    // String for path name
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Initialize OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Set RemoveUsedObject option
    optimizationOptions->set_RemoveUnusedObjects(true);

    // Optimize PDF document using OptimizationOptions
    document->OptimizeResources(optimizationOptions);

    // Save updated document
    document->Save(_dataDir + outfilename); 
}
```

### إزالة التدفقات غير المستخدمة

في بعض الأحيان يحتوي المستند على تدفقات موارد غير مستخدمة. هذه التدفقات ليست "كائنات غير مستخدمة" لأنها مشار إليها من قاموس موارد الصفحة. وبالتالي، لا تتم إزالتها باستخدام طريقة "إزالة الكائنات غير المستخدمة". ولكن هذه التدفقات لا تُستخدم أبدًا مع محتويات الصفحة. قد يحدث هذا في حالات عندما يتم إزالة صورة من الصفحة ولكن ليس من موارد الصفحة. أيضًا، تحدث هذه الحالة غالبًا عندما يتم استخراج الصفحات من المستند وصفحات المستند تحتوي على موارد "مشتركة"، أي نفس كائن الموارد. يتم تحليل محتويات الصفحة من أجل تحديد ما إذا كان تدفق الموارد مستخدمًا أم لا. يتم إزالة التدفقات غير المستخدمة. في بعض الأحيان يقلل ذلك من حجم المستند. يشبه استخدام هذه التقنية الخطوة السابقة:

```cpp
void RemovingUnusedStreams() { 
    // String for path name
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Open document
    auto document = MakeObject<Document>();

    // Initialize OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Set RemoveUsedStreams option
    optimizationOptions->set_RemoveUnusedStreams(true);

    // Optimize PDF document using OptimizationOptions
    document->OptimizeResources(optimizationOptions);

    // Save updated document
    document->Save(_dataDir + outfilename); 
}
```

### ربط تدفقات مكررة

يمكن أن تحتوي بعض المستندات على عدة تدفقات موارد مكررة (مثل الصور، على سبيل المثال). قد يحدث هذا، على سبيل المثال، عندما يتم دمج مستند مع نفسه. يحتوي المستند الناتج على نسختين مستقلتين من نفس تدفق الموارد. نقوم بتحليل جميع تدفقات الموارد ومقارنتها. إذا كانت التدفقات مكررة، يتم دمجها، أي يتم الاحتفاظ بنسخة واحدة فقط. يتم تغيير المراجع بشكل مناسب، ويتم إزالة نسخ الكائن. في بعض الحالات، يساعد ذلك في تقليل حجم المستند.

```cpp
void LinkingDuplicateStreams() { 
    // سلسلة لاسم المسار
    String _dataDir("C:\\Samples\\");

    // سلسلة لاسم الملف المدخل
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // فتح المستند
    auto document = MakeObject<Document>(_dataDir + infilename);

    // تهيئة خيارات التحسين
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // ضبط خيار LinkDuplcateStreams
    optimizationOptions->set_LinkDuplcateStreams(true);

    // تحسين مستند PDF باستخدام خيارات التحسين
    document->OptimizeResources(optimizationOptions);

    // حفظ المستند المحدث
    document->Save(_dataDir + outfilename); 
}
```

بالإضافة إلى ذلك، يمكننا استخدام إعدادات [AllowReusePageContent](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.optimization_options#aedaab36eaf8ed5059a2b1e11275bf6d8). إذا تم تعيين هذه الخاصية إلى true، سيتم إعادة استخدام محتوى الصفحة عند تحسين المستند للصفحات المتطابقة.

```cpp
void AllowReusePageContent() { 
    // سلسلة لأسم المسار
    String _dataDir("C:\\Samples\\");

    // سلسلة لأسم الملف المدخل
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // فتح المستند
    auto document = MakeObject<Document>(_dataDir + infilename);

    // تهيئة خيارات التحسين
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // تعيين خيار AllowReusePageContent
    optimizationOptions->set_AllowReusePageContent(true);

    // تحسين مستند PDF باستخدام خيارات التحسين
    document->OptimizeResources(optimizationOptions);

    // حفظ المستند المحدث
    document->Save(_dataDir + outfilename); 
}
```


### إزالة تضمين الخطوط

عند إنشاء نسخة PDF من ملف التصميم الشخصي الخاص بك، يتم إضافة نسخة من جميع الخطوط الضرورية إلى ملف PDF نفسه. هذا هو التضمين. بغض النظر عن مكان فتح هذا الـ PDF، سواء كان على جهاز الكمبيوتر الخاص بك، أو على جهاز كمبيوتر صديقك، أو على جهاز الكمبيوتر لمزود الطباعة الخاص بك، ستكون جميع الخطوط الصحيحة موجودة وستظهر بشكل صحيح.

ولكن، إذا كان المستند يستخدم الخطوط المضمنة، فهذا يعني أن جميع بيانات الخطوط يتم تخزينها في المستند. الميزة هي أن المستند يمكن عرضه بغض النظر عما إذا كان الخط مثبتًا على جهاز المستخدم أم لا. ولكن تضمين الخطوط يجعل المستند أكبر. طريقة إزالة التضمين للخطوط تزيل جميع الخطوط المضمنة. وبالتالي، يقل حجم المستند ولكن قد يصبح المستند نفسه غير قابل للقراءة إذا لم يتم تثبيت الخط الصحيح.
```
```cpp
void UnembedFonts() {
    // String for path name
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir+infilename);

    // Initialize OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Set AllowReusePageContent option
    optimizationOptions->set_UnembedFonts(true);

    // Optimize PDF document using OptimizationOptions
    document->OptimizeResources(optimizationOptions);

    // Save updated document
    document->Save(_dataDir + outfilename);
}
```

The optimization resources apply these methods to the document. If any of these methods are applied, the document size will most probably decrease. If none of these methods is applied, the document size will not change which is obvious.

## طرق إضافية لتقليل حجم مستند PDF

### إزالة أو تسطيح التعليقات التوضيحية

وجود التعليقات التوضيحية في مستند PDF يزيد من حجمه بشكل طبيعي. يمكن حذف التعليقات التوضيحية عندما لا تكون ضرورية. عندما تكون مطلوبة ولكن لا تحتاج إلى تحرير إضافي، يمكن تسطيحها. كلتا هاتين التقنيتين ستقللان من حجم الملف.

```cpp
void FlatteningAnnotation() {
    // سلسلة لاسم المسار
    String _dataDir("C:\\Samples\\");

    // سلسلة لاسم الملف المدخل
    String infilename("OptimizeDocument.pdf");
    // سلسلة لاسم الملف الناتج
    String outfilename("OptimizeDocument_out.pdf");

    // فتح المستند
    auto document = MakeObject<Document>(_dataDir + infilename);

    // تسطيح التعليقات التوضيحية
    for(auto page : document->get_Pages())
    {
        for(auto annotation : page->get_Annotations())
        {
        annotation->Flatten();
        }
    }
    // حفظ المستند المحدث
    document->Save(_dataDir + outfilename);
}
```

### إزالة حقول النماذج

سيؤدي إزالة النماذج من ملف PDF الخاص بك أيضًا إلى تحسين المستند.
إذا كان مستند PDF يحتوي على AcroForms، يمكننا محاولة تقليل حجم الملف عن طريق تسطيح حقول النماذج.

```cpp
void FlatteningFormFields() {
    // سلسلة لاسم المسار
    String _dataDir("C:\\Samples\\");

    // سلسلة لاسم الملف المدخل
    String infilename("OptimizeFormField.pdf");
    // سلسلة لاسم الملف الناتج
    String outfilename("OptimizeFormField_out.pdf");

    // فتح المستند
    auto document = MakeObject<Document>(_dataDir + infilename);

    // تسطيح حقول النماذج
    // تسطيح النماذج
    if (document->get_Form()->get_Fields()->get_Count() > 0)
    {
        for(auto item : document->get_Form()->get_Fields())
        {
            item->Flatten();
        }
    }
    // حفظ المستند المحدث
    document->Save(_dataDir + outfilename);
}
```

### تحويل ملف PDF من فضاء الألوان RGB إلى التدرج الرمادي

يتألف ملف PDF من نص، صورة، مرفق، تعليقات توضيحية، رسوم بيانية، وغيرها من الكائنات. قد تصادف متطلبًا لتحويل ملف PDF من مساحة ألوان RGB إلى التدرج الرمادي ليكون أسرع أثناء طباعة تلك الملفات. أيضًا، عند تحويل الملف إلى التدرج الرمادي، يتم تقليل حجم المستند، ولكنه يمكن أن يؤدي أيضًا إلى انخفاض في جودة المستند. هذه الميزة مدعومة حاليًا بواسطة ميزة Pre-Flight في Adobe Acrobat، ولكن عند الحديث عن أتمتة Office، فإن Aspose.PDF هو الحل النهائي لتوفير مثل هذه المزايا لتلاعب المستندات. لتحقيق هذا المتطلب، يمكن استخدام الكود التالي.

```cpp
void ConvertPDFfromColorspaceToGrayscale() {
    // String for path name
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String infilename("OptimizeDocument.pdf");
    // String for output file name
    String outfilename("Test-gray_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto strategy = MakeObject<Aspose::Pdf::RgbToDeviceGrayConversionStrategy>();
    for (int idxPage = 1; idxPage <= document->get_Pages()->get_Count(); idxPage++)
    {
        // Get instance of particular page inside PDF
        auto page = document->get_Pages()->idx_get(idxPage);
        // Convert the RGB colorspace image to GrayScale colorspace
        strategy->Convert(page);
    }
    // Save resultant file
    document->Save(_dataDir + outfilename); 
}
```
### ضغط FlateDecode

يوفر Aspose.PDF لـ C++ دعم ضغط FlateDecode لوظيفة تحسين PDF.
لتحسين الصورة باستخدام ضغط FlateDecode، قم بتعيين خيارات التحسين إلى Flate.
يوضح مقتطف الشيفرة أدناه كيفية استخدام الخيار في التحسين لتخزين الصور باستخدام ضغط **FlateDecode**:

```cpp
void FlatDecodeCompression() {
 // سلسلة لمسار الاسم
 String _dataDir("C:\\Samples\\");

 // سلسلة لاسم الملف المدخل
 String infilename("FlateDecodeCompression.pdf");
 // سلسلة لاسم الملف الناتج
 String outfilename("FlateDecodeCompression_out.pdf");

 // فتح المستند
 auto document = MakeObject<Document>(_dataDir + infilename);

 // تهيئة خيارات التحسين
 auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

 // لتحسين الصورة باستخدام ضغط FlateDecode، قم بتعيين خيارات التحسين إلى Flate
 optimizationOptions->get_ImageCompressionOptions()->set_Encoding(Aspose::Pdf::Optimization::ImageEncoding::Flate);

 // تحسين مستند PDF باستخدام خيارات التحسين
 document->OptimizeResources(optimizationOptions);

 // حفظ المستند المحدث
 document->Save(_dataDir + outfilename);
}
```

### **تخزين الصورة في XImageCollection**

يوفر Aspose.PDF لـ C++ القدرة على تخزين صور جديدة في [XImageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image_collection) باستخدام ضغط FlateDecode. لتمكين هذا الخيار يمكنك استخدام علم **ImageFilterType.Flate**.
يُظهر مقتطف الشيفرة التالي كيفية استخدام هذه الوظيفة:

```cpp
void StoreImageInXImageCollection() {

 // سلسلة لاسم المسار
 String _dataDir("C:\\Samples\\");

 // سلسلة لاسم الملف الناتج
 String outfilename("FlateDecodeCompression_out.pdf");

 // فتح المستند
 auto document = MakeObject<Document>();
 
 auto page = document->get_Pages()->Add();
 
 auto imageStream = System::IO::File::OpenRead(_dataDir + u"aspose-logo.jpg");
 
 page->get_Resources()->get_Images()->Add(imageStream, Aspose::Pdf::ImageFilterType::Flate);
 
 auto ximage = page->get_Resources()->get_Images()->idx_get(page->get_Resources()->get_Images()->get_Count());

 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());

 // تعيين الإحداثيات
 int lowerLeftX = 0;
 int lowerLeftY = 0;
 int upperRightX = 600;
 int upperRightY = 600;
 
 auto rectangle = MakeObject<Rectangle>(lowerLeftX, lowerLeftY, upperRightX, upperRightY);

 auto matrix = MakeObject<Matrix>(new double[] {rectangle->get_URX() - rectangle->get_LLX(), 0, 0, rectangle->get_URY() - rectangle->get_LLY(), rectangle->get_LLX(), rectangle->get_LLY()});
 // استخدام مُشغل ConcatenateMatrix (دمج المصفوفة): يحدد كيفية وضع الصورة
 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(matrix));
 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));
 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

 document->Save(_dataDir + outfilename);
}
```