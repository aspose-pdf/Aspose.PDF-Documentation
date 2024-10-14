---
title: יצירת אספקלריה חיצונית
type: docs
weight: 80
url: /net/creating-a-wrapper-assembly/
---

{{% alert color="primary" %}}

אם אתם זקוקים לשימוש במספר רב של מחלקות, שיטות ותכונות של Aspose.PDF עבור .NET, שקלו ליצור אספקלריה חיצונית (באמצעות C# או כל שפת תכנות .NET אחרת). אספקלריות חיצוניות עוזרות להימנע משימוש ישיר ב-Aspose.PDF עבור .NET מתוך קוד לא מנוהל.

גישה טובה היא לפתח אספקלריה של .NET שמתייחסת ל-Aspose.PDF עבור .NET ועושה את כל העבודה עם זה, ומחשפת רק קבוצה מינימלית של מחלקות ושיטות לקוד לא מנוהל. היישום שלכם אז צריך לעבוד רק עם ספריית האספקלריה שלכם.

הפחתת מספר המחלקות והשיטות שאתם צריכים לקרוא דרך COM Interop מפשטת את הפרויקט. שימוש במחלקות של .NET דרך COM Interop לעיתים דורש מיומנויות מתקדמות.

{{% /alert %}}

## אספקלריה של Aspose.PDF עבור .NET

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

