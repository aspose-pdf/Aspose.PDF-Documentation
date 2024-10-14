---
title: إنشاء تجميع الغلاف
type: docs
weight: 80
url: /net/creating-a-wrapper-assembly/
---

{{% alert color="primary" %}}

إذا كنت بحاجة لاستخدام العديد من الفصول والطرق والخصائص في Aspose.PDF لـ .NET، فكر في إنشاء تجميع غلاف (باستخدام C# أو أي لغة برمجة .NET أخرى). تجميعات الغلاف تساعد على تجنب استخدام Aspose.PDF لـ .NET مباشرة من الكود غير المدار.

الطريقة المثلى هي تطوير تجميع .NET يشير إلى Aspose.PDF لـ .NET ويقوم بكل العمل معه، ويعرض فقط مجموعة صغيرة من الفصول والطرق للكود غير المدار. ثم يجب أن يعمل تطبيقك فقط مع مكتبة الغلاف الخاصة بك.

تقليل عدد الفصول والطرق التي تحتاج إلى استدعائها عبر COM Interop يبسط المشروع. غالبًا ما يتطلب استخدام فصول .NET عبر COM Interop مهارات متقدمة.

{{% /alert %}}

## Aspose.PDF لـ .NET الغلاف

```csharp

using System;
using System.Runtime.InteropServices;
namespace PdfText
{
    [Guid("FC969AC9-6591-46FB-A4AB-DB12A776F3BF")]
    [InterfaceType(ComInterfaceType.InterfaceIsIDispatch)]
    public interface IPetriever
    {
        [DispId(1)]
        void SetLicense(string file);

        [DispId(2)]
        string GetText(string file);
    }

    [Guid("3D59100F-3CC5-463D-B509-58FA0520B436")]
    [ClassInterface(ClassInterfaceType.None)]

    [ComSourceInterfaces(typeof(IPetriever))]

    public class Petriever : IPetriever
    {
        public void SetLicense(string file)
        {
            License lic = new License();
            lic.SetLicense(file);
        }

        public string GetText(string file)
        {
            // open document
            Document doc = new Document(file);

            // create TextAbsorber object to extract text
            TextAbsorber absorber = new TextAbsorber();

            // accept the absorber for all document's pages
            doc.Pages.Accept(absorber);

            // get the extracted text

            string text = absorber.Text;
            return text;

        }
    }
}

```

