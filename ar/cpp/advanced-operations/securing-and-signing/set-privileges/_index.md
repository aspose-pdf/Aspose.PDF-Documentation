---
title: تعيين الامتيازات، تشفير وفك تشفير ملف PDF باستخدام C++
linktitle: تشفير وفك تشفير ملف PDF
type: docs
weight: 20
url: ar/cpp/set-privileges-encrypt-and-decrypt-pdf-file/
keywords: تشفير pdf، حماية pdf بكلمة مرور، فك تشفير pdf، c++
description: تشفير ملف PDF باستخدام C++ باستخدام أنواع مختلفة من التشفير والخوارزميات. أيضًا، فك تشفير ملفات PDF باستخدام كلمة مرور المالك.
lastmod: "2021-12-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## تعيين الامتيازات على ملف PDF موجود

لضبط الامتيازات على ملف PDF موجود، يستخدم Aspose.PDF for C++ فئة [DocumentPrivilege](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.document_privilege/) وتحديد الحقوق التي تريد تطبيقها على المستند. بمجرد تحديد الامتيازات، قم بتمرير هذا الكائن كحجة إلى طريقة [Encrypt](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#af7adb89eb21ef5e78b2ef5ce04fabcd7) لكائن [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

يظهر لك الجزء التالي من الشيفرة كيفية تعيين امتيازات ملف PDF.

```cpp
void SecuringAndSigning::SetPrivilegesOnExistingPDF() {
    // سلسلة لمسار الاسم.
    String _dataDir("C:\\Samples\\");

    // تحميل ملف PDF المصدر
    auto document = MakeObject<Document>(_dataDir + u"input.pdf");

    // إنشاء كائن امتيازات الوثيقة

    // تطبيق القيود على جميع الامتيازات
    auto documentPrivilege = DocumentPrivilege::get_ForbidAll();
    // السماح فقط بقراءة الشاشة
    documentPrivilege->set_AllowScreenReaders(true);

    // تشفير الملف بكلمة مرور المستخدم والمالك.
    // يجب تعيين كلمة المرور، بحيث بمجرد أن يشاهد المستخدم الملف بكلمة مرور المستخدم،

    // تم تفعيل خيار قراءة الشاشة فقط
    document->Encrypt(u"user", u"owner", documentPrivilege, CryptoAlgorithm::AESx128, false);

    // حفظ الوثيقة المحدثة
    document->Save(_dataDir + u"SetPrivileges_out.pdf");
}
```

## تشفير ملف PDF باستخدام أنواع خوارزميات تشفير مختلفة

لاستخدام تشفير ملف PDF، استخدم [Encrypt](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#af7adb89eb21ef5e78b2ef5ce04fabcd7) طريقة كائن [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) لتشفير ملف PDF.


The following code snippet shows you how to encrypt PDF files.

```cpp
void SecuringAndSigning::EncryptPDFFile() {
    // String for path name.
    String _dataDir("C:\\Samples\\");

    // Load a source PDF file
    auto document = MakeObject<Document>(_dataDir + u"input.pdf");

    // Instantiate Document Privileges object
    // Apply restrictions on all privileges
    auto documentPrivilege = DocumentPrivilege::get_ForbidAll();
    // Only allow screen reading
    documentPrivilege->set_AllowScreenReaders(true);
    // Encrypt the file with User and Owner password.
    // Need to set the password, so that once the user views the file with user
    // password,
    // Only screen reading option is enabled
    document->Encrypt(u"user", u"owner", documentPrivilege, CryptoAlgorithm::AESx128, false);
    // Save updated document
    document->Save(_dataDir + u"SetPrivileges_out.pdf");
}
```

## فك تشفير ملف PDF باستخدام كلمة مرور المالك

من أجل فك تشفير ملف PDF، تحتاج أولاً إلى إنشاء كائن [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) وفتح ملف PDF باستخدام كلمة مرور المالك. بعد ذلك، تحتاج إلى استدعاء طريقة [Decrypt](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a9c26014465f4368edc6fc62b7ef3d76a).

```cpp
void SecuringAndSigning::DecryptPDFFile() {

// سلسلة لمسار الاسم.

String _dataDir("C:\\Samples\\");

// فتح المستند

auto document = MakeObject<Document>(_dataDir + u"Decrypt.pdf", u"password");

// فك تشفير PDF

document->Decrypt();

// حفظ PDF المحدث

document->Save(_dataDir + u"Decrypt_out.pdf");
}
```

## تغيير كلمة مرور ملف PDF

نظرًا لأن ملفات PDF الخاصة بك يمكن أن تحمل معلومات مهمة وسرية، يجب أن تظل آمنة. بناءً على ذلك، قد تحتاج إلى تغيير كلمة مرور مستند PDF الخاص بك.

إذا كنت ترغب في تغيير كلمة مرور ملف PDF، فأنت بحاجة أولاً إلى فتح ملف PDF باستخدام كلمة مرور المالك مع كائن [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). بعد ذلك، تحتاج إلى استدعاء طريقة [ChangePasswords](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a9952055c2ac0afea827ce400b5ec951d).

يعرض لك المقتطف البرمجي التالي كيفية تغيير كلمة مرور ملف PDF.
```cpp
void SecuringAndSigning::ChangePassword_PDF_File() {

// String for path name.

String _dataDir("C:\\Samples\\");


// Open document

auto document = MakeObject<Document>(_dataDir + u"ChangePassword.pdf", u"owner");

// Change password

document->ChangePasswords(u"owner", u"newuser", u"newowner");

// Save updated PDF

document->Save(_dataDir + u"ChangePassword_out.pdf");
}
```

## كيفية - تحديد ما إذا كان ملف PDF محمي بكلمة مرور

لا يمكن فتح مستند PDF مشفر بكلمة مرور المستخدم بدون كلمة مرور. 
من الأفضل أن نحدد ما إذا كان المستند محميًا بكلمة مرور قبل أن نحاول فتحه. في بعض الأحيان، هناك مستندات لا تتطلب معلومات كلمة المرور أثناء فتحها، لكنها تتطلب معلومات من أجل تحرير محتويات الملف. لذلك من أجل تلبية المتطلبات المذكورة أعلاه، توفر فئة [PdfFileInfo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_file_info/) الموجودة تحت Aspose.PDF.Facades الخصائص التي يمكن أن تساعد في تحديد المعلومات المطلوبة.

### الحصول على معلومات حول أمان مستند PDF

يحتوي PdfFileInfo على ثلاث خصائص للحصول على معلومات حول أمان مستند PDF.

1. الخاصية PasswordType تعيد قيمة تعداد PasswordType:
   - PasswordType.None - المستند غير محمي بكلمة مرور
   - PasswordType.User - تم فتح المستند بكلمة مرور المستخدم (أو فتح المستند)
   - PasswordType.Owner - تم فتح المستند بكلمة مرور المالك (أو الأذونات، التحرير)

   - PasswordType.Inaccessible - المستند محمي بكلمة مرور ولكن هناك حاجة إلى كلمة المرور لفتحه بينما تم توفير كلمة مرور غير صحيحة (أو لم يتم توفير كلمة مرور).
```
2. الخاصية المنطقية HasOpenPassword - تُستخدم لتحديد ما إذا كان الملف المُدخل يتطلب كلمة مرور عند فتحه.
3. الخاصية المنطقية HasEditPassword - تُستخدم لتحديد ما إذا كان الملف المُدخل يتطلب كلمة مرور لتحرير محتوياته.

### تحديد كلمة المرور الصحيحة من المصفوفة

أحيانًا يكون هناك متطلب لتحديد كلمة المرور الصحيحة من مصفوفة كلمات المرور وفتح المستند باستخدام كلمة المرور الصحيحة. يوضح الجزء التالي من الكود الخطوات اللازمة للتكرار عبر مصفوفة كلمات المرور ومحاولة فتح المستند بكلمة المرور الصحيحة.

```cpp
void SecuringAndSigning::DetermineCorrectPasswordFromArray() {


// String for path name.

String _dataDir("C:\\Samples\\");


// Load source PDF file

auto info = MakeObject<PdfFileInfo>(_dataDir + u"IsPasswordProtected.pdf");


// Determine if the source PDF is encrypted

Console::WriteLine(u"File is password protected {0}", info->get_IsEncrypted());

const int count = 5;

String passwords[count] = { u"test", u"test1", u"test2", u"owner", u"sample" };


for (int passwordcount = 0; passwordcount < count; passwordcount++)

{


try


{



auto document = MakeObject<Document>(_dataDir + u"IsPasswordProtected.pdf", passwords[passwordcount]);



auto pages = document->get_Pages()->get_Count();



if (pages > 0)




Console::WriteLine(u"Number of Page in document are = {0}", pages);


}


catch (Aspose::Pdf::InvalidPasswordException ex)


{



Console::WriteLine(u"Password = {0} is not correct", passwords[passwordcount]);


}

}

Console::WriteLine(u"Test finished");
}
```
```