---
title: تعيين الامتيازات، تشفير وفك تشفير ملف PDF
linktitle: تشفير وفك تشفير ملف PDF
type: docs
weight: 20
url: ar/java/set-privileges-encrypt-and-decrypt-pdf-file/
keywords: تشفير pdf، حماية بكلمة مرور pdf، فك تشفير pdf، java
description: تشفير ملف PDF باستخدام Java باستخدام أنواع وخوارزميات تشفير مختلفة. بالإضافة إلى فك تشفير ملفات PDF باستخدام كلمة مرور المالك.
lastmod: "2021-12-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## تعيين الامتيازات على ملف PDF موجود

لتعيين الامتيازات على ملف PDF، قم بإنشاء كائن من فئة DocumentPrivilege وحدد الحقوق التي تريد تطبيقها على المستند.
 بمجرد تعريف الامتيازات، مرر هذا الكائن كمعامل إلى طريقة [Encrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#encrypt-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-boolean-) الخاصة بكائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). يوضح لك المقتطف البرمجي التالي كيفية تعيين امتيازات ملف PDF.

```java
  public static void SetPrivilegesOnExistingPDF()
  {
   // قم بتحميل ملف PDF المصدر
   Document document = new Document(_dataDir + "input.pdf");

   // إنشاء كائن امتيازات المستند
   // تطبيق قيود على جميع الامتيازات
   DocumentPrivilege documentPrivilege = DocumentPrivilege.getForbidAll();
   // السماح بقراءة الشاشة فقط
   documentPrivilege.setAllowScreenReaders(true);
   // تشفير الملف بكلمة مرور للمستخدم والمالك.
   // يجب تعيين كلمة المرور، بحيث عند عرض المستخدم للملف بكلمة مرور المستخدم،
   // يتم تمكين خيار قراءة الشاشة فقط
   document.encrypt("user", "owner", documentPrivilege, CryptoAlgorithm.AESx128, false);
   // حفظ المستند المحدث
   document.save(_dataDir + "SetPrivileges_out.pdf");
  }
```

## تشفير ملف PDF باستخدام أنواع وخوارزميات تشفير مختلفة

يمكنك استخدام [Encrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#encrypt-java.lang.String-java.lang.String-int-int-) طريقة الكائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) لتشفير ملف PDF. يمكنك تمرير كلمة مرور المستخدم، كلمة مرور المالك، والأذونات إلى طريقة [Encrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#encrypt-java.lang.String-java.lang.String-int-int-). بالإضافة إلى ذلك، يمكنك تمرير أي قيمة من تعداد [CryptoAlgorithm](https://reference.aspose.com/pdf/java/com.aspose.pdf/CryptoAlgorithm). يوفر هذا التعداد تركيبات مختلفة من خوارزميات التشفير وأحجام المفاتيح. يمكنك تمرير القيمة التي تختارها. أخيرًا، احفظ ملف PDF المشفر باستخدام طريقة [save(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save--) للكائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

>يرجى تحديد كلمات مرور مختلفة للمستخدم والمالك أثناء تشفير ملف PDF.

يوضح مقتطف الشيفرة التالي كيفية تشفير ملفات PDF.

```java
public static void EncryptPDFFile() {
   // تحميل ملف PDF المصدر
   Document document = new Document(_dataDir + "input.pdf");

   // إنشاء كائن امتيازات المستند
   // تطبيق قيود على جميع الامتيازات
   DocumentPrivilege documentPrivilege = DocumentPrivilege.getForbidAll();
   // السماح بقراءة الشاشة فقط
   documentPrivilege.setAllowScreenReaders(true);
   // تشفير الملف بكلمة مرور المستخدم والمالك.
   // يجب تعيين كلمة المرور، حتى يتمكن المستخدم من عرض الملف باستخدام كلمة مرور المستخدم،
   // بحيث يتم تفعيل خيار قراءة الشاشة فقط
   document.encrypt("user", "owner", documentPrivilege, CryptoAlgorithm.AESx128, false);
   // حفظ المستند المحدث
   document.save(_dataDir + "SetPrivileges_out.pdf");
  }
```

## فك تشفير ملف PDF باستخدام كلمة مرور المالك

من أجل فك تشفير ملف PDF، تحتاج أولاً إلى إنشاء كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) وفتح ملف PDF باستخدام كلمة مرور المالك.
 بعد ذلك، تحتاج إلى استدعاء طريقة [Decrypt](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#decrypt--) الخاصة بكائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). أخيرًا، احفظ ملف PDF المحدث باستخدام طريقة Save الخاصة بكائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). يوضح لك مقتطف الشيفرة التالي كيفية فك تشفير ملف PDF.

```java
public static void DecryptPDFFile() {
   // فتح المستند
   Document document = new Document(_dataDir + "Decrypt.pdf", "password");
   // فك تشفير PDF
   document.decrypt();

   // حفظ ملف PDF المحدث
   document.save(_dataDir + "Decrypt_out.pdf");
  }
```

## تغيير كلمة مرور ملف PDF

إذا كنت ترغب في تغيير كلمة مرور ملف PDF، تحتاج أولاً إلى فتح ملف PDF باستخدام كلمة مرور المالك مع كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). بعد ذلك، تحتاج إلى استدعاء طريقة [ChangePasswords](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#changePasswords-java.lang.String-java.lang.String-java.lang.String-) لكائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). تحتاج إلى تمرير كلمة المرور الحالية للمالك مع كلمة المرور الجديدة للمستخدم وكلمة المرور الجديدة للمالك إلى هذه الطريقة. أخيرًا، احفظ ملف PDF المحدث باستخدام طريقة Save لكائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

يظهر لك مقتطف الشيفرة التالي كيفية تغيير كلمة مرور ملف PDF.

```java
public static void ChangePassword_PDF_File() {
   // فتح المستند
   Document document = new Document(_dataDir+ "ChangePassword.pdf", "owner");
   // تغيير كلمة المرور
   document.changePasswords("owner", "newuser", "newowner");
   // حفظ ملف PDF المحدث
   document.save(_dataDir + "ChangePassword_out.pdf");
  }
```

## كيف - تحديد ما إذا كانت مستند PDF الأصلي محميًا بكلمة مرور

يوفر Aspose.PDF for Java إمكانيات رائعة للتعامل مع مستندات PDF. عند استخدام فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) من الحزمة com.aspose.pdf لفتح مستند PDF محمي بكلمة مرور، نحتاج إلى توفير معلومات كلمة المرور كوسيطة لمنشئ Document وفي حالة عدم توفير هذه المعلومات، يتم إنشاء رسالة خطأ. في الواقع عند محاولة فتح ملف PDF باستخدام كائن Document، يحاول المنشئ قراءة محتويات ملف PDF وفي حالة عدم توفير كلمة المرور الصحيحة، يتم إنشاء رسالة خطأ (يحدث ذلك لمنع الوصول غير المصرح به إلى المستند).

عند التعامل مع ملفات PDF المشفرة، قد تواجه السيناريو الذي تكون فيه مهتمًا بالكشف عما إذا كان ملف PDF يحتوي على كلمة مرور للفتح و/أو كلمة مرور للتحرير. أحيانًا توجد مستندات لا تتطلب معلومات كلمة المرور أثناء فتحها، ولكنها تتطلب معلومات من أجل تعديل محتويات الملف. لذا، من أجل تلبية المتطلبات المذكورة أعلاه، توفر فئة PdfFileInfo الموجودة تحت حزمة com.aspose.pdf.facades الطرق التي يمكن أن تساعد في تحديد المعلومات المطلوبة.

### الحصول على معلومات حول أمان مستند PDF

تحتوي PdfFileInfo على ثلاث طرق للحصول على معلومات حول أمان مستند PDF.

1. طريقة getPasswordType() تُعيد قيمة تعداد PasswordType:
   1. PasswordType.None - المستند غير محمي بكلمة مرور
   1. PasswordType.User - تم فتح المستند بكلمة مرور المستخدم (أو كلمة المرور لفتح المستند)
   1. PasswordType.Owner - تم فتح المستند بكلمة مرور المالك (أو الأذونات، التعديل)
   1. PasswordType.Inaccessible - المستند محمي بكلمة مرور ولكن يلزم كلمة مرور لفتحه بينما تم تقديم كلمة مرور غير صحيحة (أو لم يتم تقديم كلمة مرور).
1. طريقة hasOpenPassword() تُستخدم لتحديد ما إذا كان الملف المُدخل يتطلب كلمة مرور عند فتحه.
1. طريقة hasEditPassword() تُستخدم لتحديد ما إذا كان الملف المُدخل يتطلب كلمة مرور لتعديل محتوياته.

### تحديد كلمة المرور الصحيحة من المصفوفة

أحيانًا يكون هناك حاجة لتحديد كلمة المرور الصحيحة من مجموعة كلمات المرور وفتح المستند باستخدام كلمة المرور الصحيحة. يوضح مقتطف الكود التالي الخطوات اللازمة للتكرار عبر مجموعة كلمات المرور ومحاولة فتح المستند بكلمة المرور الصحيحة.

```java
public static void DetermineCorrectPasswordFromArray() {
     // تحميل ملف PDF المصدر
   PdfFileInfo info = new PdfFileInfo();
   info.bindPdf(_dataDir + "IsPasswordProtected.pdf");
   // تحديد ما إذا كان ملف PDF المصدر مشفرًا
   System.out.println("الملف محمي بكلمة مرور " + info.isEncrypted());
   String[] passwords = { "test", "test1", "test2", "test3", "sample" };
   for (int passwordcount = 0; passwordcount < passwords.length; passwordcount++)
   {
    try
    {
     Document doc = new Document(_dataDir + "IsPasswordProtected.pdf", passwords[passwordcount]);
     if (doc.getPages().size() > 0)
      System.out.println("عدد الصفحات في المستند = " + doc.getPages().size());
    }
    catch (InvalidPasswordException ex)
    {
     System.out.println("كلمة المرور = " + passwords[passwordcount] + "  ليست صحيحة");
    }
   }
```