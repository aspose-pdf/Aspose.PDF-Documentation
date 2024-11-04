---
title: استخراج وحفظ مرفق
linktitle: استخراج وحفظ مرفق
type: docs
weight: 20
url: /java/extract-and-save-an-attachment/
description: Aspose.PDF for Java يتيح لك الحصول على جميع المرفقات من مستند PDF. أيضًا، يمكنك الحصول على مرفق فردي من المستند الخاص بك.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## الحصول على المرفقات من مستند PDF

مع Aspose.PDF، من الممكن الحصول على جميع المرفقات من مستند PDF. هذا مفيد إما عندما تريد حفظ المستندات بشكل منفصل عن الـ PDF، أو إذا كنت بحاجة إلى إزالة المرفقات من PDF.

توضح مقتطفات الشفرات التالية كيفية الحصول على جميع المرفقات من مستند PDF.

```java
   public static void GetAttachmentsFromPDFDocument() {
// فتح المستند
Document pdfDocument = new Document(_dataDir+"input.pdf");
  // الحصول على ملف مضمّن معين
  FileSpecification fileSpecification = pdfDocument.getEmbeddedFiles().get_Item(1);
  // الحصول على خصائص الملف
  System.out.printf("Name: - " + fileSpecification.getName());
  System.out.printf("\nDescription: - " + fileSpecification.getDescription());
  System.out.printf("\nMime Type: - " + fileSpecification.getMIMEType());
  // الحصول على المرفق من ملف PDF
  try {
   InputStream input = fileSpecification.getContents();
   File file = new File(fileSpecification.getName());
   // إنشاء مسار للملف من pdf
   file.getParentFile().mkdirs();
   // إنشاء واستخراج الملف من pdf
   java.io.FileOutputStream output = new java.io.FileOutputStream(fileSpecification.getName(), true);
   byte[] buffer = new byte[4096];
   int n = 0;
   while (-1 != (n = input.read(buffer)))
    output.write(buffer, 0, n);
   // إغلاق كائن InputStream
   input.close();
   output.close();
  } catch (IOException e) {
   e.printStackTrace();
  }
  // إغلاق كائن المستند
  pdfDocument.dispose();
        
    }

```


## الحصول على معلومات المرفق

كما ذكر في [الحصول على المرفقات من مستند PDF](/pdf/java/get-attachments-from-a-pdf-document/)، يتم الاحتفاظ بمعلومات المرفق في كائن [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification)، ويتم جمعها مع مرفقات أخرى في مجموعة EmbeddedFiles الخاصة بكائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

يوفر كائن [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) طرقًا للحصول على معلومات حول المرفق، على سبيل المثال:

- getName() – يحصل على اسم الملف.
- [getDescription()](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification#getDescription--) – يحصل على وصف الملف.
- getMIMEType() – يحصل على نوع MIME للملف.
- getParams() – معلومات حول معلمات الملف، على سبيل المثال CheckSum، CreationDate، ModDate و Size.

للحصول على هذه المعلمات، تأكد أولاً من أن طريقة getParams() لا ترجع قيمة null.

إما أن تقوم بالتكرار عبر جميع المرفقات في مجموعة EmbeddedFiles باستخدام حلقة for، أو تحصل على مرفق فردي بتحديد قيمة الفهرس الخاصة به.
 The following code snippet shows how to get information about a specific attachment.

```java
    public static void GetAttachmentInformation() {
  // فتح المستند
  Document pdfDocument = new Document(_dataDir+"input.pdf");
  // الحصول على ملف مضمّن معين
  FileSpecification fileSpecification = pdfDocument.getEmbeddedFiles().get_Item(1);
  // الحصول على خصائص الملف
  System.out.println("Name:-" + fileSpecification.getName());
  System.out.println("Description:- " + fileSpecification.getDescription());
  System.out.println("Mime Type:-" + fileSpecification.getMIMEType());
  // التحقق مما إذا كان كائن المعاملات يحتوي على المعاملات
  if (fileSpecification.getParams() != null) {
   System.out.println("CheckSum:- " + fileSpecification.getParams().getCheckSum());
   System.out.println("Creation Date:- " + fileSpecification.getParams().getCreationDate());
   System.out.println("Modification Date:- " + fileSpecification.getParams().getModDate());
   System.out.println("Size:- " + fileSpecification.getParams().getSize());
  } 
```