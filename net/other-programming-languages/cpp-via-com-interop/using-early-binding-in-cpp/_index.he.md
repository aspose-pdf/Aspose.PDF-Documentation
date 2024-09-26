---
title: שימוש בקישור מוקדם ב-CPP
type: docs
weight: 10
url: /net/using-early-binding-in-cpp/
---

## דרישות מוקדמות

{{% alert color="primary" %}}

אנא הרשם ל-Aspose.PDF עבור .NET עם COM Interop, אנא בדוק את המאמר בשם [שימוש ב-Aspose.pdf עבור .NET באמצעות COM Interop](/pdf/net/use-aspose-pdf-for-net-via-com-interop/).

{{% /alert %}}

## דוגמה

{{% alert color="primary" %}}

זוהי דוגמת קוד C++ פשוטה לחילוץ טקסט מקבצי PDF באמצעות COM Interop באמצעות קישור מוקדם. לפני הרצת הדוגמה שים לב ש

- **#import** *typelib.tlb* גורם למהדר של C++ ליצור שני קבצים: *typelib.tlh* ו-*typelib.tli*. כברירת מחדל, קבצים אלו נוצרים רק פעם אחת, כך שתצטרך לקומפל את הפרויקט מחדש במלואו כדי לקבל גרסאות חדשות שלהם.
- לעיתים קרובות, ייבוא של קובץ TLB אחד בלבד יוביל למספר גדול של שגיאות מהדר.
- לעיתים קרובות, ייבוא של קובץ TLB אחד בלבד עלול להוביל למספר רב של שגיאות מהמהדר.

```cpp
// ספריות טיפוס המתייחסות זו לזו:
```

ויש בו מספר פקודות **#import**. פשוט העתק אותם לתוך הקוד שלך לפני ייבוא ספריית הטיפוס הראשית ועשה זאת באותו ***סדר***. כך תטפל בסוג הבעיה הראשון. הסוג הבא של בעיה נובע מהעובדה שסביבת C++ מכילה מספר גדול של מקרוס, פונקציות מוגדרות מראש וכו', אשר עלולות להתנגש עם שיטות בספריית הטיפוס. לדוגמה, הפונקציה GetType כבר משמשת רחבות ב-C++ אך גם Aspose.PDF משתמשת בה. מצאתי שתכונות **rename** ו-**auto_rename** של פקודת **#import** מאוד נוחות להיפטר מאזהרות ושגיאות אפשריות.

- לעיתים קרובות, מחלקות במרחבי שמות **uses** נוגעות בשמות בספריית הטיפוס, ולכן במקרים כאלה יש להשתמש בשם המחלקה המלא במקום **using namespace**. לדוגמה, ראה איך קוראים ל-StringToBSTR בקטע הקוד שלמטה.
{{% /alert %}}

לפרטים נוספים אנא עיין בפוסט [זה](http://www.drdobbs.com/writing-com-clients-with-late-and-early/184403558).
לפרטים נוספים אנא עיינו [בפוסט הזה](http://www.drdobbs.com/writing-com-clients-with-late-and-early/184403558).

דוגמת C++

```cpp
#include "stdafx.h"
#import "C:\Windows\Microsoft.NET\Framework\v2.0.50727\System.Drawing.tlb"
#import "C:\Windows\Microsoft.NET\Framework\v4.0.30319\mscorlib.tlb" auto_rename

#import "C:\Temp\Aspose.PDF.tlb" rename("GetType", "GetType_") auto_rename

using namespace System;
String ^earlyBinding(String ^file)
{
    String ^text;
    // יצירת ComHelper

    Aspose_Pdf::_ComHelperPtr comHelperPtr;
    HRESULT hr = comHelperPtr.CreateInstance(__uuidof(Aspose_Pdf::ComHelper));
    if (FAILED(hr))
    {
        Console::WriteLine(L"אירעה שגיאה");
    }
    else
    {
        // הגדרת רישיון
        Aspose_Pdf::_LicensePtr licPtr;
        licPtr.CreateInstance(__uuidof(Aspose_Pdf::License));
        licPtr->SetLicense("C:\\Temp\\Aspose.PDF.lic");
        licPtr.Release();

        // קבלת מסמך
        Aspose_Pdf::_DocumentPtr docPtr;
        docPtr = comHelperPtr->OpenFile((BSTR)System::Runtime::InteropServices::Marshal::StringToBSTR(file).ToPointer());

        comHelperPtr.Release();

        // יצירת Absorber
        Aspose_Pdf::_TextAbsorberPtr absorberPtr;
        HRESULT hRes = absorberPtr.CreateInstance(__uuidof(Aspose_Pdf::TextAbsorber));

        // סריקת טקסט
        docPtr->GetPages()->Accept_4(absorberPtr);

        // אחזור טקסט
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
        Console::WriteLine("חסרים פרמטרים\nהשימוש:testCOM <קובץ pdf>");
        return 0;
    }

    String ^text = earlyBinding(args[0]);
    CoUninitialize();
    Console::WriteLine("טקסט שנספג:");
    Console::WriteLine("---\n{0}", text != nullptr ? text->Trim() : "<ריק>");
    Console::WriteLine("---");
    return 0;
}
```

