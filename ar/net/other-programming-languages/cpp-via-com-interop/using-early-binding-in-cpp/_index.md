---
title: استخدام الربط المبكر في CPP
type: docs
weight: 10
url: ar/net/using-early-binding-in-cpp/
---

## المتطلبات الأساسية

{{% alert color="primary" %}}

يرجى تسجيل Aspose.PDF لـ .NET مع COM Interop، يرجى التحقق من المقال المسمى [استخدام Aspose.pdf لـ .NET عبر COM Interop](/pdf/net/use-aspose-pdf-for-net-via-com-interop/).

{{% /alert %}}

## عينة

{{% alert color="primary" %}}

هذا مثال بسيط لكود C++ لاستخراج النص من ملفات PDF باستخدام COM Interop باستخدام الربط المبكر. قبل تشغيل العينة، انتبه إلى أن:

- **#import** *typelib.tlb* يجعل مُترجم C++ يُنتج ملفين: *typelib.tlh* و *typelib.tli*. بشكل افتراضي، يتم إنتاج هذه الملفات مرة واحدة فقط، لذا تحتاج إلى إعادة ترجمة المشروع بالكامل للحصول على نسخ جديدة منها.
- غالبًا ما يؤدي استيراد ملف TLB واحد فقط إلى عدد كبير من أخطاء المترجم.

{{% /alert %}}
- غالبًا ما يؤدي استيراد ملف TLB واحد فقط إلى العديد من أخطاء المترجم.

```cpp
// Cross-referenced type libraries:
```
{{% alert color="primary" %}}

ويحتوي على واحد أو أكثر من **#import**. فقط انسخها في كودك قبل استيراد مكتبة النوع الرئيسية وقم بذلك بـ***نفس*** الترتيب. وبذلك ستتغلب على النوع الأول من المشكلات. يأتي النوع التالي من المشكلات من حقيقة أن بيئة C++ لديها عدد كبير من الماكروهات، والوظائف المحددة مسبقًا، إلخ، والتي يمكن أن تتعارض مع طرق مكتبة النوع. على سبيل المثال، تم استخدام GetType بشكل واسع بالفعل في C++ ولكن Aspose.PDF لديها أيضًا. وجدت أن سمات **rename** و **auto_rename** لأمر **#import** مريحة جدًا للتخلص من التحذيرات والأخطاء المحتملة.

- أحيانًا تتعارض الفصول في أسماء الفضاءات **uses** مع الأسماء في مكتبة النوع، لذا في مثل هذه الحالات يجب استخدام الاسم الكامل للفصل بدلاً من **using namespace**. على سبيل المثال، انظر كيف يتم استدعاء StringToBSTR في الجزء البرمجي أدناه.
{{% /alert %}}

لمزيد من التفاصيل يرجى الاطلاع على [هذا](http://www.drdobbs.com/writing-com-clients-with-late-and-early/184403558) المنشور.
للتفاصيل يرجى الاطلاع على [هذا](http://www.drdobbs.com/writing-com-clients-with-late-and-early/184403558) المنشور.

مثال بلغة C++

```cpp
#include "stdafx.h"
#import "C:\Windows\Microsoft.NET\Framework\v2.0.50727\System.Drawing.tlb"
#import "C:\Windows\Microsoft.NET\Framework\v4.0.30319\mscorlib.tlb" auto_rename

#import "C:\Temp\Aspose.PDF.tlb" rename("GetType", "GetType_") auto_rename

using namespace System;
String ^earlyBinding(String ^file)
{
    String ^text;
    // إنشاء ComHelper

    Aspose_Pdf::_ComHelperPtr comHelperPtr;
    HRESULT hr = comHelperPtr.CreateInstance(__uuidof(Aspose_Pdf::ComHelper));
    if (FAILED(hr))
    {
        Console::WriteLine(L"حدث خطأ");
    }
    else
    {
        // تعيين الرخصة
        Aspose_Pdf::_LicensePtr licPtr;
        licPtr.CreateInstance(__uuidof(Aspose_Pdf::License));
        licPtr->SetLicense("C:\\Temp\\Aspose.PDF.lic");
        licPtr.Release();

        // الحصول على المستند
        Aspose_Pdf::_DocumentPtr docPtr;
        docPtr = comHelperPtr->OpenFile((BSTR)System::Runtime::InteropServices::Marshal::StringToBSTR(file).ToPointer());

        comHelperPtr.Release();

        // إنشاء Absorber
        Aspose_Pdf::_TextAbsorberPtr absorberPtr;
        HRESULT hRes = absorberPtr.CreateInstance(__uuidof(Aspose_Pdf::TextAbsorber));

        // تصفح النص
        docPtr->GetPages()->Accept_4(absorberPtr);

        // استرجاع النص
        BSTR extractedText = absorberPtr->GetText();
        text = gcnew String(extractedText);
        docPtr.Release();
        absorberPtr.Release();
    }
    return text;
}

int main(array<System::String ^> ^args)
{
    CoInitialize(NULL);
    if (args->Length != 1)
    {
        Console::WriteLine("المعلمات مفقودة\nالاستخدام:testCOM <ملف pdf>");
        return 0;
    }

    String ^text = earlyBinding(args[0]);
    CoUninitialize();
    Console::WriteLine("النص المستخلص:");
    Console::WriteLine("---\n{0}", text != nullptr ? text->Trim() : "<فارغ>");
    Console::WriteLine("---");
    return 0;
}
```

